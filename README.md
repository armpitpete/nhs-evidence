# NHS Evidence

An evidence-led repository for accumulating, normalising and linking NHS-related information over time, with a separate intelligence layer for developing story and investigation ideas.

## Purpose

The repository is designed to answer questions across time, not merely archive documents. It should make it possible to trace an NHS policy, inquiry, organisation, statistic or incident across later publications and outcomes.

A second purpose is **idea generation**: repeated scanning should surface implementation gaps, recurring organisations, unusual statistics, contradictions, local angles, overdue promises and patterns worth investigating. Leads are stored separately from evidence so an interesting hypothesis is never silently promoted into fact.

## Core rules

1. **Evidence before conclusion.** Preserve what the source actually supports.
2. **Separate fact, attributed claim and inference.** Do not silently convert one into another.
3. **Separate leads from evidence.** A lead may be worth pursuing without yet being established.
4. **Stable IDs.** Every durable source, evidence record, lead and watch gets a stable ID.
5. **Explicit provenance.** Every substantive durable record points back to one or more source IDs.
6. **Explicit uncertainty.** Unknown, disputed and inferred fields stay visibly marked.
7. **Link rather than duplicate.** Reuse existing organisations, topics, policies, events, leads and watches.
8. **No unsupported causation.** Temporal association is not evidence of causation.
9. **Negative findings matter.** A tested hypothesis that is not supported remains useful institutional memory.
10. **Public-repo minimisation.** Follow the ingestion boundary in `governance/INGESTION_BOUNDARY.md`.
11. **Promote selectively.** Not every useful webpage or daily observation becomes a durable source/record object.

## Structure

- `sources/` — normalized captures of source documents, datasets and pages that cross the durable-promotion threshold.
- `records/` — atomic evidence records worth retaining and reusing.
- `ideas/` — developing story/investigation leads, explicitly not established evidence.
- `watches/` — observable expected events, deadlines, promised follow-ups and future checks.
- `scans/` — dated daily triage/intelligence receipts.
- `syntheses/weekly/` — weekly pattern, promotion and follow-up synthesis.
- `syntheses/monthly/` — cross-week institutional-memory synthesis.
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

### Daily — triage

Ask:

1. What materially changed?
2. Which existing watch is due?

The daily process is deliberately bounded. It records interesting-but-unpromoted material in the scan receipt and creates durable source/record/lead/watch objects only when the promotion threshold is met.

### Weekly — connect

The weekly synthesis does the deeper reasoning:

- decide which daily signals deserve promotion;
- update, merge, close or weaken leads;
- identify recurrence only where multiple events support it;
- inspect watch quality and overdue promises;
- look for contradictions, implementation gaps and Yorkshire/local angles.

### Monthly — test durability

Monthly synthesis asks what can be supported across several weekly windows. It must not manufacture a month-scale pattern from a partial or thin evidence window.

## Architecture freeze

The v0.3 information architecture is now **frozen while it proves its usefulness**.

Do not add new entity classes, scoring layers, question objects, signal objects, special investigation objects or new graph subsystems unless a demonstrated operating failure cannot be solved within the existing:

`source → record/topic → lead → watch → scan → synthesis`

model.

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

v0.4 changes operating effort, not the accepted evidence ontology: lighter daily triage, selective promotion, atomic daily commits, stronger weekly synthesis, tighter watch hygiene and a full-month threshold for monthly synthesis.
