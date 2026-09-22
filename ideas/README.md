# NHS Ideas / Leads

This directory contains **investigative and editorial leads**, not findings.

A lead exists because one or more observations suggest a useful question. It must remain clearly distinguishable from verified evidence.

## Machine-readable frontmatter

The YAML frontmatter is the authoritative machine state and must conform to `schema/idea-lead.schema.json`.

Narrative sections explain the signal and reasoning but do not replace required frontmatter.

## Rules

- Every lead must point to the source/evidence that triggered it.
- Phrase the lead as a testable question or observed signal, not an accusation.
- Preserve counter-evidence and failed hypotheses.
- Update an existing lead when the same pattern recurs instead of creating duplicates.
- Link active follow-up to one or more `WATCH-NHS-*` objects.
- Do **not** store `next_check`, expected dates, last-check state or operational watch status in a lead; watches are the sole authority for those fields.
- Record what future evidence would strengthen or weaken the question.
- Promote a lead to a normal evidence-backed record only when the repository contains evidence supporting the resulting factual claim.
- Close or mark a lead unsupported when later evidence does not sustain it.
- Preserve closure reasoning in the lead narrative and close the associated watch with its own closure reason so the same unsupported theory is not repeatedly rediscovered.

## Lifecycle

`new → developing → recurring → promoted`

or

`new/developing → unsupported/closed`

Status does not measure importance.

## IDs

Use sequential stable IDs:

`LEAD-NHS-YYYY-NNNN`

## Useful outputs

Over time this layer should support queries such as:

- What keeps recurring?
- Which NHS organisations repeatedly appear across different issues?
- Which announced reforms have weak or missing implementation evidence?
- Which new datasets could support deeper investigation?
- What national stories have a Yorkshire or local-service angle?
- Where do official claims and measured outcomes appear to diverge?
- Which leads have weakened or been disproved?
