#!/usr/bin/env python3
"""Reject deletion or material mutation of accepted accountability baselines."""

from __future__ import annotations
import argparse
import subprocess
from pathlib import Path
from validate_accountability import frontmatter_text,scalar,baseline_fingerprint

ROOT=Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(["git",*args],cwd=ROOT,text=True,stderr=subprocess.STDOUT)

def fm_from_text(text):
    if not text.startswith("---\n"): return None
    end=text.find("\n---\n",4)
    return None if end<0 else text[4:end]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--against",required=True); args=ap.parse_args()
    try:
        paths=git("ls-tree","-r","--name-only",args.against,"--","records").splitlines()
    except subprocess.CalledProcessError as exc:
        print(f"FAIL: cannot read baseline ref {args.against}: {exc.output.strip()}"); return 2
    errors=[]; checked=0
    for rel in paths:
        try: old=git("show",f"{args.against}:{rel}")
        except subprocess.CalledProcessError: continue
        oldfm=fm_from_text(old)
        if oldfm is None or scalar(oldfm,"accountability_role")!="baseline": continue
        checked+=1; path=ROOT/rel
        if not path.exists():
            errors.append(f"{rel}: accepted accountability baseline deleted"); continue
        newfm=frontmatter_text(path)
        if newfm is None or scalar(newfm,"accountability_role")!="baseline":
            errors.append(f"{rel}: accepted accountability baseline role removed"); continue
        if baseline_fingerprint(oldfm)!=baseline_fingerprint(newfm):
            errors.append(f"{rel}: accepted accountability baseline material changed")
    if errors:
        print(f"FAIL: {len(errors)} accountability history error(s)")
        for e in errors: print(" -",e)
        return 1
    print(f"PASS: {checked} accepted accountability baseline(s) preserved against {args.against}")
    return 0

if __name__=="__main__": raise SystemExit(main())
