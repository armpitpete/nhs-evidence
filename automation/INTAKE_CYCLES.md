# Weekly Intake Cycle Contract — Lean v0.4

## Purpose

Keep daily intake small and intelligible while giving deeper reasoning a clear weekly home.

## Branch naming

Use one intake branch per ISO week:

`intake/YYYY-Www`

Example: `intake/2026-W39`.

## Daily operation

T-113 performs bounded triage and, where justified, updates evidence/leads/watches.

Each completed daily run should add at most one atomic intake commit to the weekly branch:

`NHS intelligence intake — YYYY-MM-DD`

The daily commit may contain several file changes; it must not be split into a commit per file.

The existing multi-commit history created before Lean v0.4 is retained. Do not force-rewrite candidate history simply for cosmetic cleanup.

## Weekly operation owns deeper reasoning

T-114 runs on Sunday and:

1. reviews the week's daily receipts, including signals that were not promoted;
2. completes the weekly synthesis;
3. decides which signals deserve durable promotion;
4. updates, consolidates, weakens, closes or carries leads forward;
5. checks watch quality, due/overdue state and duplicate/vague watches;
6. records negative findings and source gaps;
7. tests recurring themes only across distinct evidence;
8. identifies implementation/accountability gaps and Yorkshire/local angles;
9. verifies the weekly branch is internally coherent;
10. freezes the week's branch for human/protected merge review.

The weekly task may deepen research on the strongest signals. That work should not be pushed back into routine daily scanning.

It must not merge protected `main` without explicit owner authorization.

## Watch hygiene at week close

A watch remains open only if it represents a reasonably observable future condition and still has a useful re-check.

At weekly close:

- satisfy/close watches whose expected event occurred;
- supersede duplicates;
- extend dates only with evidence;
- move vague "keep looking" questions back into the associated lead rather than keeping indefinite watches.

Preserve history; do not delete watches merely to simplify counts.

## If the previous week has not merged

Do not discard evidence.

Create the new week's branch from the previous weekly head so history remains cumulative. Open the new week's PR against `main`; it may temporarily contain earlier unmerged work. Mark the older PR as superseded by the newer cumulative candidate rather than rewriting history.

Once an earlier candidate is merged, reconcile the current week's base/diff before presenting its protected merge gate.

## Architecture freeze

Daily/weekly operation must use the existing v0.3 ontology. A workflow inconvenience is not sufficient reason to add a new entity type or graph layer.

## Protected boundary

No intake, weekly synthesis or monthly synthesis task may:

- merge protected `main`;
- force-push or rewrite accepted history;
- delete evidence to make a candidate cleaner;
- bypass source/provenance requirements.

Those remain separate owner-authorized actions.
