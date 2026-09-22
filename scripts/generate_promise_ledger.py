#!/usr/bin/env python3
"""Generate the derived Promise Ledger."""

from __future__ import annotations
import argparse
from pathlib import Path
from validate_accountability import frontmatter_text,scalar,relation_targets

ROOT=Path(__file__).resolve().parents[1]

def esc(v):
    return (v or "—").replace("|","\\|").replace("\n"," ")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",default="index/promise-ledger.md"); args=ap.parse_args()
    baselines={}; changes={}
    for path in sorted((ROOT/"records").rglob("*.md")):
        fm=frontmatter_text(path)
        if fm is None: continue
        ident=scalar(fm,"id"); role=scalar(fm,"accountability_role")
        if role=="baseline": baselines[ident]=(path,fm)
        elif role=="status-change":
            target=scalar(fm,"accountability_for")
            changes.setdefault(target,[]).append((scalar(fm,"date") or scalar(fm,"date_added") or "",ident,fm))
    lines=[
      "# NHS Promise Ledger","",
      "Derived view — **not an authority source**. Baselines and status-change records remain authoritative evidence; WATCH-NHS objects own future check timing.","",
      "| Baseline | Commitment | Issuer / responsible | Deadline | Current evidence-backed status | Latest status evidence | Watch |",
      "| --- | --- | --- | --- | --- | --- | --- |"
    ]
    for ident,(path,fm) in sorted(baselines.items()):
        if scalar(fm,"commitment_kind") not in {"promise","target","obligation","publication-commitment"}: continue
        ev=sorted(changes.get(ident,[]),key=lambda x:(x[0],x[1]))
        if ev: _,latest_id,latest_fm=ev[-1]; status=scalar(latest_fm,"promise_status")
        else: latest_id="—"; status=scalar(fm,"promise_status")
        watch=next((x for x in relation_targets(fm) if x.startswith("WATCH-NHS-")),"—")
        lines.append(f"| {esc(ident)} | {esc(scalar(fm,'commitment_scope'))} | {esc(scalar(fm,'commitment_issuer'))} / {esc(scalar(fm,'commitment_responsible'))} | {esc(scalar(fm,'commitment_deadline'))} | {esc(status)} | {esc(latest_id)} | {esc(watch)} |")
    lines += ["","## Interpretation rules","",
      "- A blank or absent later status is not failure; it means the preserved baseline remains the last supported state.",
      "- fulfilled and unmet require separate evidence records.",
      "- Absence of public evidence is represented as an evidence gap/unverifiable state, not silently as non-delivery.",
      "- Historical baselines are never rewritten to display the latest state.",""]
    out=ROOT/args.output; out.parent.mkdir(parents=True,exist_ok=True); out.write_text("\n".join(lines),encoding="utf-8")
    print(out.relative_to(ROOT)); return 0

if __name__=="__main__": raise SystemExit(main())
