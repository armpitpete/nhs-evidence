# NHS Evidence

An evidence-led repository for accumulating, normalising and linking NHS-related information over time, with a separate intelligence layer for developing story and investigation ideas.

## Purpose

The repository is designed to answer questions across time, not merely archive documents. It should make it possible to trace an NHS policy, inquiry, organisation, statistic or incident across later publications and outcomes.

A second purpose is **idea generation**: repeated scanning should surface implementation gaps, recurring organisations, unusual statistics, contradictions, local angles, overdue promises and patterns worth investigating. Leads are stored separately from evidence so an interesting hypothesis is never silently promoted into fact.

## Core rules

1. **Evidence before conclusion.** Preserve what the source actually supports.
2. **Separate fact, attributed claim and inference.** Do not silently convert one into another.
3. **Separate leads from evidence.** A lead may be worth pursuing without yet being established.
4. **Stable IDs.** Every source, evidence record, lead and watch gets a durable ID.
5. **Explicit provenance.** Every substantive record points back to one or more source IDs.
6. **Explicit uncertainty.** Unknown, disputed and inferred fields stay visibly marked.
7. **Link rather than duplicate.** Reuse existing organisations, topics, policies, events, leads and watches.
8. **No unsupported causation.** Temporal association is not evidence of causation.
9. **Negative findings matter.** A tested hypothesis that is not supported remains useful institutional memory.
10. **Public-repo minimisation.** Follow the ingestion boundary in `governance/INGESTION_BOUNDARY.md`.

## Structure

- `sources/` — normalized captures of source documents, datasets and pages.
- `records/` — atomic evidence records extracted from sources.
- `ideas/` — developing story/investigation leads, explicitly not established evidence.
- `watches/` — expected events, deadlines, promised follow-ups and future checks.
- `scans/` — dated daily intelligence-scan receipts.
- `syntheses/weekly/` — weekly pattern and follow-up synthesis.
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

## Daily intelligence workflow

The **Merrin Task Registry** owns scheduling. No standalone ChatGPT automation is authoritative for this repository.

Daily intake:

1. Scan new NHS-related material.
2. Check due watches and expected events even when there is no new news story.
3. Prioritise primary/authoritative sources.
4. Use reputable journalism as discovery material and follow it back to primary evidence where possible.
5. Deduplicate against existing sources, records, leads and watches.
6. Capture new evidence and link it to existing entities.
7. Update existing leads before creating new ones.
8. Record strengthening, weakening and negative findings.
9. Write a dated scan receipt under `scans/`.
10. Commit to the current ISO-week intake branch.
11. Run `python3 scripts/validate_repository.py` before presenting the candidate.
12. Do **not** merge protected `main` without explicit authorization.

## Weekly intake cycles

New work is grouped by ISO week under branches named:

`intake/YYYY-Www`

The weekly synthesis freezes the week's evidence window for review. See `automation/INTAKE_CYCLES.md`.

## Current state

**NHS Evidence Intelligence v0.3 — MERGED / ACCEPTED.**

Accepted protected-main baseline:

`06f6a79b2a2572f0a6241847ee47ad78eb4a9fce`

PR #3 merged on 22 September 2026 after exact-main validation and hostile review passed. The 2026-W39 intake branch continues to collect post-acceptance daily evidence for the next protected review boundary.
