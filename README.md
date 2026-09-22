# NHS Evidence

An evidence-led repository for accumulating, normalising and linking NHS-related information over time, with a separate intelligence layer for developing story and investigation ideas.

## Canonical mission

> **Build a longitudinal evidence memory of the NHS that can detect meaningful change, connect it across time, and turn those changes into evidence-led questions and investigations.**

## Longitudinal invariant

> **Never overwrite the old position with the new one. Preserve both, identify the transition, and distinguish the observed change from any explanation for why it happened.**

This applies to policy, guidance, implementation, deadlines, scope, ownership, funding, metrics, definitions, institutional language and stated priorities.

The system may conclude that a documented position changed when primary evidence supports that comparison. It must not silently infer why the change occurred. Explanations require their own evidence and must remain clearly labelled as attributed explanation, inference or unresolved question.

## Purpose

The repository is designed to answer questions across time, not merely archive documents. It should make it possible to trace an NHS policy, inquiry, organisation, statistic or incident across later publications and outcomes.

A second purpose is **idea generation**: repeated scanning should surface implementation gaps, recurring organisations, unusual statistics, contradictions, local angles, overdue promises and patterns worth investigating. Leads are stored separately from evidence so an interesting hypothesis is never silently promoted into fact.

## Core rules

1. **Evidence before conclusion.** Preserve what the source actually supports.
2. **Separate fact, attributed claim and inference.** Do not silently convert one into another.
3. **Preserve historical state.** Never replace an earlier documented position with a later one; retain both and record the transition.
4. **Separate change from explanation.** "The position changed" may be an evidence-backed observation. "It changed because..." requires separate evidence.
5. **Separate leads from evidence.** A lead may be worth pursuing without yet being established.
6. **Stable IDs.** Every durable source, evidence record, lead and watch gets a stable ID.
7. **Explicit provenance.** Every substantive durable record points back to one or more source IDs.
8. **Explicit uncertainty.** Unknown, disputed and inferred fields stay visibly marked.
9. **Link rather than duplicate.** Reuse existing organisations, topics, policies, events, leads and watches.
10. **No unsupported causation.** Temporal association is not evidence of causation.
11. **Negative findings matter.** A tested hypothesis that is not supported remains useful institutional memory.
12. **Public-repo minimisation.** Follow the ingestion boundary in `governance/INGESTION_BOUNDARY.md`.
13. **Promote selectively.** Not every useful webpage or daily observation becomes a durable source/record object.

## Structure

- `sources/` — normalized captures of source documents, datasets and pages that cross the durable-promotion threshold.
- `records/` — atomic evidence records worth retaining and reusing.
- `ideas/` — developing story/investigation leads, explicitly not established evidence.
- `watches/` — observable expected events, deadlines, promised follow-ups and future checks.
- `scans/` — dated daily triage/intelligence receipts.
- `syntheses/weekly/` — weekly pattern, promotion and change-detection synthesis.
- `syntheses/monthly/` — cross-week institutional-memory and direction-of-change synthesis.
- `topics/` — durable topic nodes used across records.
- `organisations/` — durable organisation nodes.
- `people/` — durable person nodes where needed.
- `policies/` — policy and guidance nodes.
- `inquiries/` — inquiry nodes.
- `statistics/` — durable statistical series and releases.
- `consultations/` — consultation records.
- `timelines/` — derived chronological views.
- `index/` — machine-readable relationship indexes.
- `schema/` — evidence, lead and watch contracts.
- `automation/` — registry-owned operating contracts.
- `governance/` — ingestion and publication boundaries.

## Lean operating model

### Daily — detect

Ask:

1. What materially changed?
2. Which previous known state does the new material alter, narrow, expand, supersede or contradict?
3. Which existing watch is due?

The daily process is deliberately bounded. It records interesting-but-unpromoted material in the scan receipt and creates durable source/record/lead/watch objects only when the promotion threshold is met.

When change is detected, preserve the earlier state and the later state. Do not rewrite history into a single "current" version.

### Weekly — connect

The weekly synthesis does the deeper reasoning:

- compare old and new positions;
- identify transitions in policy, scope, deadlines, ownership, metrics, funding, implementation or institutional language;
- decide which daily signals deserve promotion;
- update, merge, close or weaken leads;
- identify recurrence only where multiple events support it;
- inspect watch quality and overdue promises;
- look for contradictions, implementation gaps and Yorkshire/local angles;
- separate observed change from explanations for the change.

### Monthly — test direction

Monthly synthesis asks what can be supported across several weekly windows, including whether apparently isolated changes amount to a sustained change in direction.

It must not manufacture a month-scale pattern from a partial or thin evidence window.

## Architecture freeze

The v0.3 information architecture is now **frozen while it proves its usefulness**.

Do not add new entity classes, scoring layers, question objects, signal objects, special investigation objects or new graph subsystems unless a demonstrated operating failure cannot be solved within the existing:

`source → record/topic → lead → watch → scan → synthesis`

model.

Change detection must first be implemented through preserved versions, relations, timelines and synthesis rather than by inventing a new entity class.

Operational simplification is preferred over ontology growth.

## Weekly intake cycles

New work is grouped by ISO week under branches named:

`intake/YYYY-Www`

The weekly synthesis freezes the week's evidence window for review. See `automation/INTAKE_CYCLES.md`.

## Current state

**NHS Evidence Intelligence v0.3 — MERGED / ACCEPTED.**

Accepted protected-main baseline:

`06f6a79b2a2572f0a6241847ee47ad78eb4a9fce`

**Lean Intake v0.4 — operational candidate** on the active 2026-W39 intake branch.

v0.4 changes operating effort, not the accepted evidence ontology: lighter daily triage, selective promotion, atomic daily commits, stronger weekly synthesis, tighter watch hygiene, explicit longitudinal change detection and a full-month threshold for monthly synthesis.


## Accountability & Promise Tracking v0.1

The accountability layer applies longitudinal memory to public commitments.

Operating loop:

**commitment → preserved baseline → watch → delivery/change evidence → status history → accountability question → remedy evidence → re-check**

A promise baseline is evidence, not a separate authority object. Later delivery/change evidence is stored as a new record pointing back to the baseline. The baseline is never rewritten to show the current state.

The system represents successful delivery and improvement with the same evidential care as failure. Absence of evidence is not proof of non-delivery.

See `governance/ACCOUNTABILITY_PROMISE_TRACKING_V0.1.md`.


## Accountability & Promise Tracking v0.1 acceptance state

**MACHINE COMPLETE / OWNER HUMAN REVIEW PENDING / NOT MERGED**

The v0.1 candidate has implemented immutable commitment baselines, separate status history, fair failure/uncertainty handling, remedy evidence, hostile validation, the derived Promise Ledger, accountability timelines, and weekly/monthly reporting contracts.

The Week 39 report currently present is a **partial-window prototype through 22 September 2026**, not the scheduled full weekly report. Protected-main acceptance remains subject to owner review and exact-head merge authorization.
