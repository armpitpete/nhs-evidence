# Weekly Intake Cycle Contract

## Purpose

Keep daily intake operationally simple while preventing one permanent pull request from growing without bound.

## Branch naming

Use one intake branch per ISO week:

`intake/YYYY-Www`

Example: `intake/2026-W39`.

## Daily operation

T-113 commits daily scan/evidence/lead/watch updates to the active weekly branch.

Each weekly branch has one pull request representing that evidence window.

## Week close

T-114 runs on Sunday and:

1. completes the weekly synthesis;
2. checks unresolved watches and lead state;
3. records negative findings and source gaps;
4. verifies the weekly branch is internally coherent;
5. freezes the week's branch for human/protected merge review.

It must not merge protected `main` without explicit owner authorization.

## If the previous week has not merged

Do not discard evidence.

Create the new week's branch from the previous weekly head so history remains cumulative. Open the new week's PR against `main`; it may temporarily contain earlier unmerged work. Mark the older PR as superseded by the newer cumulative candidate rather than rewriting history.

Once an earlier candidate is merged, reconcile the current week's base/diff before presenting its protected merge gate.

## First-cycle migration

The experimental standing branch `automation/daily-nhs-intake` and PR #2 are superseded by `intake/2026-W39`. The old branch is retained as historical evidence; it is not deleted automatically.

## Protected boundary

No intake, weekly synthesis or monthly synthesis task may:

- merge protected `main`;
- force-push or rewrite accepted history;
- delete evidence to make a candidate cleaner;
- bypass source/provenance requirements.

Those remain separate owner-authorized actions.
