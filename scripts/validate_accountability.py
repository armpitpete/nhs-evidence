#!/usr/bin/env python3
"""Accountability & Promise Tracking v0.1 invariants."""

from __future__ import annotations
import datetime as dt
import hashlib
import re
from pathlib import Path

ROLES={"baseline","status-change","outcome-evidence","remedy-evidence"}
KINDS={"promise","target","obligation","publication-commitment","recommendation","aspiration","forecast","announcement"}
MATERIAL_KINDS={"promise","target","obligation","publication-commitment"}
STATUSES={"announced","implementation-started","on-track","fulfilled","partially-fulfilled","delayed","scope-changed","target-changed","responsibility-changed","superseded","withdrawn","unmet","unverifiable"}
TRANSITIONS={"implementation-started","implementation-update","fulfilled","partial-delivery","deadline-change","scope-change","target-change","responsibility-change","measurement-change","outcome-change","superseded","withdrawn","unmet","evidence-gap"}
EXPLANATIONS={"established","attributed","inferred","unknown"}
REMEDY_LEVELS={"official-recommendation","evaluated","comparator-supported","proposed","speculative"}
STATUS_TRANSITION={
 "implementation-started":{"implementation-started","implementation-update"},
 "on-track":{"implementation-update"},
 "fulfilled":{"fulfilled"},
 "partially-fulfilled":{"partial-delivery"},
 "delayed":{"deadline-change"},
 "scope-changed":{"scope-change"},
 "target-changed":{"target-change"},
 "responsibility-changed":{"responsibility-change"},
 "superseded":{"superseded"},
 "withdrawn":{"withdrawn"},
 "unmet":{"unmet"},
 "unverifiable":{"evidence-gap"},
}

def frontmatter_text(path: Path) -> str | None:
    text=path.read_text(encoding="utf-8")
    if not text.startswith("---\n"): return None
    end=text.find("\n---\n",4)
    return None if end < 0 else text[4:end]

def scalar(fm: str,key: str) -> str | None:
    m=re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$",fm)
    if not m: return None
    value=m.group(1).strip()
    if value in {"","null","~"}: return None
    if len(value)>=2 and value[0]==value[-1] and value[0] in {'"',"'"}: return value[1:-1]
    return value

def simple_list(fm: str,key: str) -> list[str] | None:
    inline=re.search(rf"(?m)^{re.escape(key)}:\s*\[(.*?)\]\s*$",fm)
    if inline:
        body=inline.group(1).strip()
        return [] if not body else [x.strip().strip('"').strip("'") for x in body.split(",") if x.strip()]
    start=re.search(rf"(?m)^{re.escape(key)}:\s*$",fm)
    if not start: return None
    out=[]
    for line in fm[start.end():].splitlines():
        if not line.strip(): continue
        if re.match(r"^[A-Za-z0-9_]+:",line): break
        m=re.match(r"^\s{2}-\s+(.*)$",line)
        if m:
            value=m.group(1).strip()
            if re.match(r"^[A-Za-z0-9_]+:",value): return None
            out.append(value.strip('"').strip("'"))
        elif line.startswith("  "): continue
        else: break
    return out

def relation_targets(fm: str) -> list[str]:
    start=re.search(r"(?m)^relations:\s*$",fm)
    if not start: return []
    block=fm[start.end():]
    next_top=re.search(r"(?m)^([A-Za-z0-9_]+):",block)
    if next_top: block=block[:next_top.start()]
    return re.findall(r"(?m)^\s{4}target:\s*['\"]?([^'\"\n]+)",block)

def valid_date(value: str | None) -> bool:
    if value is None: return True
    try:
        dt.date.fromisoformat(value); return True
    except ValueError: return False

def baseline_fingerprint(fm: str) -> str:
    fields=[
      scalar(fm,"id") or "", scalar(fm,"commitment_kind") or "",
      scalar(fm,"commitment_issuer") or "", scalar(fm,"commitment_responsible") or "",
      scalar(fm,"commitment_date") or "", scalar(fm,"commitment_deadline") or "",
      scalar(fm,"commitment_scope") or "", scalar(fm,"commitment_success_criteria") or "",
    ]
    return hashlib.sha256("|".join(fields).encode("utf-8")).hexdigest()

def validate_accountability(root: Path) -> list[str]:
    errors=[]
    records={}
    baselines={}
    changes={}

    def err(path,message): errors.append(f"{path}: {message}")

    for path in sorted((root/"records").rglob("*.md")):
        fm=frontmatter_text(path)
        if fm is None: continue
        ident=scalar(fm,"id")
        if ident: records[ident]=(path,fm)

    for ident,(path,fm) in records.items():
        rel=path.relative_to(root)
        role=scalar(fm,"accountability_role")
        if role is None: continue
        if role not in ROLES:
            err(rel,f"invalid accountability_role {role!r}"); continue
        if not (simple_list(fm,"source_ids") or []):
            err(rel,"accountability evidence requires at least one source_id")

        if role=="baseline":
            required=["commitment_kind","commitment_issuer","commitment_responsible","commitment_date","commitment_scope","commitment_success_criteria","promise_status","baseline_fingerprint"]
            for key in required:
                if scalar(fm,key) is None: err(rel,f"baseline missing {key}")
            kind=scalar(fm,"commitment_kind")
            if kind not in KINDS: err(rel,f"invalid commitment_kind {kind!r}")
            if scalar(fm,"promise_status")!="announced":
                err(rel,"baseline promise_status must remain 'announced'; later state belongs in a status-change record")
            if not valid_date(scalar(fm,"commitment_date")): err(rel,"invalid commitment_date")
            if not valid_date(scalar(fm,"commitment_deadline")): err(rel,"invalid commitment_deadline")
            fp=scalar(fm,"baseline_fingerprint")
            if fp and fp!=baseline_fingerprint(fm):
                err(rel,"baseline fingerprint mismatch; historical material fields changed")
            baselines[ident]=(path,fm)

        elif role=="status-change":
            for key in ["accountability_for","promise_status","transition_type","assessment_basis","explanation_status"]:
                if scalar(fm,key) is None: err(rel,f"status-change missing {key}")
            status=scalar(fm,"promise_status")
            trans=scalar(fm,"transition_type")
            if status not in STATUSES or status=="announced": err(rel,f"invalid status-change promise_status {status!r}")
            if trans not in TRANSITIONS: err(rel,f"invalid transition_type {trans!r}")
            elif status in STATUS_TRANSITION and trans not in STATUS_TRANSITION[status]:
                err(rel,f"promise_status {status!r} incompatible with transition_type {trans!r}")
            explanation=scalar(fm,"explanation_status")
            if explanation not in EXPLANATIONS: err(rel,f"invalid explanation_status {explanation!r}")
            if explanation and explanation!="unknown" and not (simple_list(fm,"explanation_evidence_ids") or []):
                err(rel,f"explanation_status {explanation!r} requires explanation_evidence_ids")
            if status=="unmet" and scalar(fm,"failure_basis") not in {"positive-evidence","deadline-and-authoritative-non-delivery"}:
                err(rel,"unmet status requires positive evidence or deadline + authoritative non-delivery evidence; absence alone is insufficient")
            target=scalar(fm,"accountability_for") or ""
            when=scalar(fm,"date") or scalar(fm,"date_added") or ""
            changes.setdefault(target,[]).append((when,status or "",path))

        elif role=="outcome-evidence":
            for key in ["accountability_for","assessment_basis"]:
                if scalar(fm,key) is None: err(rel,f"outcome-evidence missing {key}")

        elif role=="remedy-evidence":
            for key in ["remedy_for","remedy_evidence_level","assessment_basis"]:
                if scalar(fm,key) is None: err(rel,f"remedy-evidence missing {key}")
            if scalar(fm,"remedy_evidence_level") not in REMEDY_LEVELS:
                err(rel,f"invalid remedy_evidence_level {scalar(fm,'remedy_evidence_level')!r}")

    for ident,(path,fm) in records.items():
        role=scalar(fm,"accountability_role")
        if role in {"status-change","outcome-evidence"}:
            target=scalar(fm,"accountability_for")
            if target not in baselines:
                err(path.relative_to(root),f"accountability_for must reference a baseline record; got {target!r}")
        if role=="remedy-evidence":
            target=scalar(fm,"remedy_for")
            if target not in records:
                err(path.relative_to(root),f"remedy_for must reference an evidence record; got {target!r}")
        for target in simple_list(fm,"explanation_evidence_ids") or []:
            if target not in records: err(path.relative_to(root),f"explanation_evidence_ids references missing record {target}")

    for target,events in changes.items():
        by_date={}
        for when,status,_ in events: by_date.setdefault(when,set()).add(status)
        for when,statuses in by_date.items():
            if len(statuses)>1: err("records",f"conflicting promise statuses for {target} on {when}: {sorted(statuses)}")

    for ident,(path,fm) in baselines.items():
        if scalar(fm,"commitment_kind") not in MATERIAL_KINDS: continue
        watch_targets=[x for x in relation_targets(fm) if x.startswith("WATCH-NHS-")]
        if not watch_targets and not changes.get(ident):
            err(path.relative_to(root),"material commitment baseline has neither WATCH-NHS relation nor later status evidence")

    vague=re.compile(r"^(?:monitor (?:this )?topic|keep watching|look for (?:more )?information|look for anything interesting)\.?$",re.I)
    for path in sorted((root/"watches").rglob("*.md")):
        fm=frontmatter_text(path)
        if fm is not None and vague.match((scalar(fm,"expected_event") or "").strip()):
            err(path.relative_to(root),"watch expected_event is vague; keep generic research questions in a lead")

    return errors
