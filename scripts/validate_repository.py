#!/usr/bin/env python3
"""Validate structural invariants for the NHS evidence repository.

Dependency-free by design: validates the repository's constrained Markdown
frontmatter conventions and cross-reference invariants using Python stdlib.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

from validate_accountability import validate_accountability

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

ID_RE = re.compile(r"^(?:SRC|REC|LEAD|WATCH|TOPIC)-[A-Z0-9][A-Z0-9-]*$")
LEAD_RE = re.compile(r"^LEAD-NHS-\d{4}-\d{4}$")
WATCH_RE = re.compile(r"^WATCH-NHS-\d{4}-\d{4}$")
FORBIDDEN_KEYS = {"follow_up", "home_address", "private_email", "phone", "password", "token", "secret", "medical_record"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"Authorization:\s*Bearer\s+\S+", re.I),
]

def err(path: Path | str, message: str) -> None:
    ERRORS.append(f"{path}: {message}")

def frontmatter_text(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        err(path, "unterminated frontmatter")
        return None
    return text[4:end]

def scalar(fm: str, key: str) -> str | None:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return None
    value = m.group(1).strip()
    if value in {"", "null", "~"}:
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value

def simple_list(fm: str, key: str) -> list[str] | None:
    inline = re.search(rf"(?m)^{re.escape(key)}:\s*\[(.*?)\]\s*$", fm)
    if inline:
        body = inline.group(1).strip()
        if not body:
            return []
        return [x.strip().strip('"').strip("'") for x in body.split(",") if x.strip()]
    start = re.search(rf"(?m)^{re.escape(key)}:\s*$", fm)
    if not start:
        return None
    lines = fm[start.end():].splitlines()
    out: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z0-9_]+:", line):
            break
        m = re.match(r"^\s{2}-\s+(.*)$", line)
        if m:
            value = m.group(1).strip()
            # list-of-maps (e.g. relations) is not a simple list
            if re.match(r"^[A-Za-z0-9_]+:", value):
                return None
            out.append(value.strip('"').strip("'"))
        elif line.startswith("  "):
            continue
        else:
            break
    return out

def top_keys(fm: str) -> set[str]:
    return set(re.findall(r"(?m)^([A-Za-z0-9_]+):", fm))

def valid_date(value: str | None) -> bool:
    if value is None:
        return True
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False

def valid_datetime(value: str | None) -> bool:
    if value is None:
        return True
    try:
        dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def relation_targets(fm: str) -> list[str]:
    start = re.search(r"(?m)^relations:\s*$", fm)
    if not start:
        return []
    block = fm[start.end():]
    next_top = re.search(r"(?m)^([A-Za-z0-9_]+):", block)
    if next_top:
        block = block[:next_top.start()]
    return re.findall(r"(?m)^\s{4}target:\s*['\"]?([^'\"\n]+)", block)

def load_schemas() -> None:
    expected = {
        "schema/evidence-record.schema.json",
        "schema/idea-lead.schema.json",
        "schema/watch.schema.json",
    }
    for rel in expected:
        path = ROOT / rel
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            err(rel, f"invalid JSON schema: {exc}")

def scan_secret_patterns() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".csv", ".py", ".yml", ".yaml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                err(path.relative_to(ROOT), f"possible credential material matches {pattern.pattern!r}")

def main() -> int:
    load_schemas()
    scan_secret_patterns()

    docs: list[tuple[Path, str]] = []
    ids: dict[str, Path] = {}
    source_signatures: dict[tuple[str, str, str, str], Path] = {}

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        fm = frontmatter_text(path)
        if fm is None:
            continue
        rel = path.relative_to(ROOT)
        docs.append((rel, fm))
        ident = scalar(fm, "id")
        if ident:
            if ident in ids:
                err(rel, f"duplicate id {ident}; first seen in {ids[ident]}")
            else:
                ids[ident] = rel
            if not ID_RE.match(ident):
                err(rel, f"id has unexpected form: {ident}")
        forbidden = top_keys(fm) & FORBIDDEN_KEYS
        if forbidden:
            err(rel, f"forbidden operational/sensitive frontmatter keys: {sorted(forbidden)}")

        if rel.parts and rel.parts[0] == "sources":
            sig = (
                scalar(fm, "publisher") or "",
                scalar(fm, "title") or "",
                scalar(fm, "captured") or "",
                scalar(fm, "original_url") or "",
            )
            if any(sig):
                if sig in source_signatures:
                    err(rel, f"duplicate source signature; first seen in {source_signatures[sig]}")
                else:
                    source_signatures[sig] = rel

    # Cross-document validation after ID set is complete.
    for rel, fm in docs:
        parts = rel.parts
        ident = scalar(fm, "id") or ""

        if parts[0] == "ideas" and len(parts) > 2:
            required_scalars = ["id", "title", "status", "first_seen", "last_seen", "lead_class"]
            for key in required_scalars:
                if scalar(fm, key) is None:
                    err(rel, f"missing required scalar {key}")
            if ident and not LEAD_RE.match(ident):
                err(rel, f"lead id does not match required pattern: {ident}")
            status = scalar(fm, "status")
            if status not in {"new", "developing", "recurring", "promoted", "closed", "unsupported"}:
                err(rel, f"invalid lead status {status!r}")
            for key in ["first_seen", "last_seen"]:
                value = scalar(fm, key)
                if not value or not valid_date(value):
                    err(rel, f"invalid ISO date for {key}: {value!r}")
            for key in ["source_ids", "evidence_ids", "watch_ids", "questions", "limitations"]:
                values = simple_list(fm, key)
                if values is None:
                    err(rel, f"missing or non-simple list {key}")
                elif key in {"questions", "limitations"} and not values:
                    err(rel, f"{key} must not be empty")
                elif key == "watch_ids" and status in {"new", "developing", "recurring"} and not values:
                    err(rel, "active lead must reference at least one WATCH-NHS object")
            for key in ["source_ids", "evidence_ids", "watch_ids", "related_ids"]:
                for target in simple_list(fm, key) or []:
                    if target not in ids:
                        err(rel, f"{key} references missing id {target}")

        if parts[0] == "watches" and len(parts) > 2:
            for key in ["id", "title", "status", "watch_reason", "expected_event"]:
                if scalar(fm, key) is None:
                    err(rel, f"missing required scalar {key}")
            if ident and not WATCH_RE.match(ident):
                err(rel, f"watch id does not match required pattern: {ident}")
            status = scalar(fm, "status")
            if status not in {"open", "due", "satisfied", "closed", "superseded"}:
                err(rel, f"invalid watch status {status!r}")
            for key in ["source_ids", "evidence_ids", "related_ids"]:
                values = simple_list(fm, key)
                if values is None:
                    err(rel, f"missing or non-simple list {key}")
                for target in values or []:
                    if target not in ids:
                        err(rel, f"{key} references missing id {target}")
            for key in ["expected_by", "next_check"]:
                value = scalar(fm, key)
                if not valid_date(value):
                    err(rel, f"invalid ISO date for {key}: {value!r}")
            last_checked = scalar(fm, "last_checked")
            if not valid_datetime(last_checked):
                err(rel, f"invalid ISO datetime for last_checked: {last_checked!r}")
            last_result = scalar(fm, "last_result")
            if last_result not in {None, "not-checked", "no-change", "changed", "satisfied", "source-unavailable"}:
                err(rel, f"invalid last_result {last_result!r}")

        if parts[0] == "records" and len(parts) > 2:
            for key in ["id", "type", "title", "status", "date_added"]:
                if scalar(fm, key) is None:
                    err(rel, f"missing required scalar {key}")
            if scalar(fm, "type") == "watch":
                err(rel, "evidence records cannot be operational watch objects")
            if scalar(fm, "status") == "watch":
                err(rel, "evidence-record status cannot be watch")
            if not valid_date(scalar(fm, "date_added")):
                err(rel, f"invalid date_added {scalar(fm, 'date_added')!r}")
            for key in ["source_ids", "tags"]:
                values = simple_list(fm, key)
                if values is None:
                    err(rel, f"missing or non-simple list {key}")
            for target in simple_list(fm, "source_ids") or []:
                if target not in ids:
                    err(rel, f"source_ids references missing id {target}")
            for target in relation_targets(fm):
                if target not in ids:
                    err(rel, f"relation target missing id {target}")

    # Accountability / promise-tracking invariants.
    ERRORS.extend(validate_accountability(ROOT))

    # Relationship index resolution.
    idx = ROOT / "index" / "relations.csv"
    if idx.exists():
        with idx.open(encoding="utf-8", newline="") as fh:
            for row_no, row in enumerate(csv.DictReader(fh), start=2):
                for field in ("from_id", "to_id"):
                    target = (row.get(field) or "").strip()
                    if target and target not in ids:
                        err(idx.relative_to(ROOT), f"row {row_no} {field} references missing id {target}")

    # Ensure schema no longer permits operational watch records.
    evidence_schema = json.loads((ROOT / "schema/evidence-record.schema.json").read_text(encoding="utf-8"))
    if "watch" in evidence_schema["properties"]["type"]["enum"]:
        err("schema/evidence-record.schema.json", "type enum still permits watch")
    if "watch" in evidence_schema["properties"]["status"]["enum"]:
        err("schema/evidence-record.schema.json", "status enum still permits watch")

    if ERRORS:
        print(f"FAIL: {len(ERRORS)} repository validation error(s)")
        for item in ERRORS:
            print(f" - {item}")
        return 1

    print(f"PASS: validated {len(ids)} stable IDs across {len(docs)} frontmatter documents")
    print("PASS: WATCH-NHS objects are sole operational follow-up authority")
    print("PASS: references, relationship index and secret-pattern checks")
    print("PASS: accountability baselines, status evidence, remedies and watch-link invariants")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
