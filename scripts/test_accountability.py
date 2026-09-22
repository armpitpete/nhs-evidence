#!/usr/bin/env python3
"""Canonical and hostile tests for Accountability & Promise Tracking v0.1."""

from __future__ import annotations
import json
import re
import shutil
import tempfile
from pathlib import Path
from validate_accountability import validate_accountability

ROOT=Path(__file__).resolve().parents[1]

def replace(path,old,new):
    text=path.read_text(encoding="utf-8")
    if old not in text: raise AssertionError(f"mutation anchor missing: {old!r}")
    path.write_text(text.replace(old,new,1),encoding="utf-8")

def expect_error(root,needle):
    errs=validate_accountability(root)
    if not any(needle in e for e in errs): raise AssertionError(f"expected {needle!r}; got {errs}")

def clone_temp(td):
    dst=Path(td)/"repo"; shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns(".git","__pycache__")); return dst

def main():
    live=validate_accountability(ROOT)
    if live: raise AssertionError(f"live candidate invalid: {live}")

    scenarios=json.loads((ROOT/"tests/accountability_scenarios.json").read_text(encoding="utf-8"))
    for case in scenarios:
        if case["events"][-1]!=case["expected"]: raise AssertionError(case["name"])

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); p=t/"records/2026/REC-NHS-2026-0006-marthas-rule-national-standard.md"
        replace(p,"promise_status: announced","promise_status: fulfilled"); expect_error(t,"baseline promise_status must remain")

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); p=t/"records/2026/REC-NHS-2026-0006-marthas-rule-national-standard.md"
        replace(p,"Implement the three core components of Martha's Rule.","Implement only one component of Martha's Rule."); expect_error(t,"baseline fingerprint mismatch")

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); p=t/"records/2026/REC-NHS-2026-0011-marthas-rule-implementation-started.md"
        replace(p,"source_ids:\n  - SRC-NHSE-MR-OVERVIEW-2026-09-22\n  - SRC-NHSE-MR-STATS-2026-07","source_ids: []"); expect_error(t,"requires at least one source_id")

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); p=t/"records/2026/REC-NHS-2026-0011-marthas-rule-implementation-started.md"
        replace(p,"explanation_status: unknown","explanation_status: established"); expect_error(t,"requires explanation_evidence_ids")

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); src=t/"records/2026/REC-NHS-2026-0011-marthas-rule-implementation-started.md"
        text=src.read_text(encoding="utf-8").replace("REC-NHS-2026-0011","REC-NHS-2026-0999",1).replace("promise_status: implementation-started","promise_status: unmet",1).replace("transition_type: implementation-started","transition_type: unmet",1).replace("explanation_status: unknown","failure_basis: absence-only\nexplanation_status: unknown",1)
        (t/"records/2026/REC-NHS-2026-0999-hostile-unmet.md").write_text(text,encoding="utf-8"); expect_error(t,"unmet status requires positive evidence")

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); p=t/"watches/2026/WATCH-NHS-2026-0004-mental-health-crisis-york.md"
        text=p.read_text(encoding="utf-8"); text=re.sub(r'expected_event: ".*?"','expected_event: "Look for more information."',text,count=1); p.write_text(text,encoding="utf-8"); expect_error(t,"watch expected_event is vague")

    with tempfile.TemporaryDirectory() as td:
        t=clone_temp(td); (t/"records/2026/REC-NHS-2026-0006-marthas-rule-national-standard.md").unlink(); expect_error(t,"accountability_for must reference a baseline record")

    print(f"PASS: {len(scenarios)} canonical accountability scenarios")
    print("PASS: hostile tests reject historical rewrite, unsupported status, causal overclaim, vague watch and orphaned status evidence")
    return 0

if __name__=="__main__": raise SystemExit(main())
