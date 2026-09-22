# NHS Evidence

An evidence-led repository for accumulating, normalising and linking NHS-related information over time.

## Purpose

The repository is designed to answer questions across time, not merely archive documents. It should make it possible to trace an NHS policy, inquiry, organisation, statistic or incident across later publications and outcomes.

## Core rules

1. **Evidence before conclusion.** Preserve what the source actually supports.
2. **Separate fact, attributed claim and inference.** Do not silently convert one into another.
3. **Stable IDs.** Every source and extracted record gets an ID that does not change when filenames move.
4. **Explicit provenance.** Every substantive record points back to one or more source IDs.
5. **Explicit uncertainty.** Unknown, disputed and inferred fields stay visibly marked.
6. **Link rather than duplicate.** Reuse existing organisations, topics, policies and events.
7. **No unsupported causation.** Temporal association is not evidence of causation.
8. **Public-repo copyright discipline.** Do not republish complete third-party documents unless reuse rights are clear. Store metadata, factual summaries, short quotations where justified, and links or private source references.

## Structure

- `sources/` — one normalized capture per source document, bulletin, dataset or page.
- `records/` — atomic evidence records extracted from sources.
- `topics/` — durable topic nodes used across records.
- `organisations/` — durable organisation nodes.
- `people/` — durable person nodes where needed.
- `policies/` — policy and guidance nodes.
- `inquiries/` — inquiry nodes.
- `statistics/` — durable statistical series and releases.
- `consultations/` — consultation records.
- `timelines/` — derived chronological views.
- `index/` — machine-readable relationship indexes.
- `schema/` — record contracts.

## Record model

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

## Ingestion workflow

1. Capture the source and assign a source ID.
2. Summarise the complete source at factual level.
3. Extract atomic records only where useful.
4. Link records to existing entities/topics.
5. Add watches for expected future publications or follow-up.
6. When new evidence arrives, update links rather than rewriting history.
7. Preserve contradictions and revisions as evidence instead of deleting them.

## Current state

**NHS Evidence Model v0.1 — foundation candidate.**

The first captured source is NHS England's *The Week* bulletin supplied on 22 September 2026.
