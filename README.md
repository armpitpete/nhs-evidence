# NHS Evidence

An evidence-led repository for accumulating, normalising and linking NHS-related information over time, with a separate intelligence layer for developing story and investigation ideas.

## Purpose

The repository is designed to answer questions across time, not merely archive documents. It should make it possible to trace an NHS policy, inquiry, organisation, statistic or incident across later publications and outcomes.

A second purpose is **idea generation**: repeated daily scanning should surface implementation gaps, recurring organisations, unusual statistics, contradictions, local angles and patterns worth investigating. Leads are stored separately from evidence so an interesting hypothesis is never silently promoted into fact.

## Core rules

1. **Evidence before conclusion.** Preserve what the source actually supports.
2. **Separate fact, attributed claim and inference.** Do not silently convert one into another.
3. **Separate leads from evidence.** A lead may be worth pursuing without yet being established.
4. **Stable IDs.** Every source, evidence record and lead gets an ID that does not change when filenames move.
5. **Explicit provenance.** Every substantive record points back to one or more source IDs.
6. **Explicit uncertainty.** Unknown, disputed and inferred fields stay visibly marked.
7. **Link rather than duplicate.** Reuse existing organisations, topics, policies and events.
8. **No unsupported causation.** Temporal association is not evidence of causation.
9. **Public-repo copyright discipline.** Do not republish complete third-party documents unless reuse rights are clear. Store metadata, factual summaries, short quotations where justified, and links or private source references.

## Structure

- `sources/` — normalized captures of source documents, datasets and pages.
- `records/` — atomic evidence records extracted from sources.
- `ideas/` — developing story/investigation leads, explicitly not established evidence.
- `scans/` — dated daily intelligence-scan receipts.
- `topics/` — durable topic nodes used across records.
- `organisations/` — durable organisation nodes.
- `people/` — durable person nodes where needed.
- `policies/` — policy and guidance nodes.
- `inquiries/` — inquiry nodes.
- `statistics/` — durable statistical series and releases.
- `consultations/` — consultation records.
- `timelines/` — derived chronological views.
- `index/` — machine-readable relationship indexes.
- `schema/` — evidence and lead contracts.
- `automation/` — standing ingestion instructions.

## Evidence record model

Each evidence record should contain:

- stable `id`
- `type`
- `title`
- date or date range
- status
- source IDs
- factual summary
- tags
- explicit relations to other IDs
- uncertainty/limitations where relevant
- follow-up state when the item needs future checking

## Idea lead model

A lead records **why something may be worth investigating**, not a conclusion.

Each lead should contain:

- stable `LEAD-NHS-...` ID
- title and status
- first-seen / last-seen dates
- the observed signal
- why it may matter
- supporting source/evidence IDs
- relevant organisations/topics/places
- questions that would test the lead
- what evidence would strengthen or weaken it
- clear limitations

Useful lead classes include:

- implementation gap
- recurring organisation
- unusual statistic
- contradiction or policy tension
- local/Yorkshire angle
- emerging trend
- patient-safety signal
- workforce/finance pressure
- regulatory follow-up
- data-release opportunity

## Relationship vocabulary

Initial relationship types:

- `derived_from`
- `mentions`
- `about`
- `implements`
- `responds_to`
- `measured_by`
- `follows`
- `supersedes`
- `related_to`

The vocabulary can grow, but new relation types should have a clear meaning and not duplicate an existing one.

## Daily ingestion workflow

1. Scan the previous day's NHS-related material.
2. Prioritise primary sources: NHS England, DHSC, CQC, NICE, UKHSA, ONS, trusts and ICBs.
3. Use reputable journalism as discovery material and attribute it clearly.
4. Deduplicate against existing sources, records and leads.
5. Capture new primary evidence and assign stable source IDs.
6. Extract atomic evidence records only where useful.
7. Link new evidence to existing topics, organisations, policies, inquiries and prior records.
8. Create or update leads where the material suggests a worthwhile question or pattern.
9. Write a dated scan receipt under `scans/`.
10. Update the standing `automation/daily-nhs-intake` branch and its pull request.
11. Do **not** merge protected `main` without explicit authorization.

A quiet day is still a valid scan. Record that it was checked rather than manufacturing a story.

## Current state

**NHS Evidence Model v0.2 — daily intelligence intake candidate.**

Foundation v0.1 was accepted on 22 September 2026. Daily scanning begins 23 September 2026.
