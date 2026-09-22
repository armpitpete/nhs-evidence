# Daily NHS Intelligence Intake — Lean v0.4

## Authority

Scheduling is owned by the **Merrin Task Registry**:

- **T-113** — daily NHS intelligence intake
- **T-114** — weekly NHS intelligence synthesis
- **T-115** — monthly NHS intelligence synthesis

Standalone ChatGPT scheduling for this work is retired. Protected `main` is never merged by these tasks without explicit owner authorization.

## Objective

Build useful cumulative NHS intelligence without turning evidence-management overhead into the project.

Daily intake is **triage, not exhaustive research**.

## Two daily questions

Every run asks:

1. **What materially changed since the last scan?**
2. **Which `WATCH-NHS-*` objects are due now?**

If neither produces a material change, write a concise no-material-change receipt and stop.

## Source plan

### Core daily

Check a bounded high-signal set:

1. due `WATCH-NHS-*` sources;
2. NHS England;
3. Department of Health and Social Care / GOV.UK health publications;
4. recent CQC and HSSIB material with plausible system significance.

This is not an exhaustive crawl.

### Rotating authoritative sources

Check a small rotating subset rather than every source family every day:

- NICE;
- UKHSA;
- ONS;
- Parliamentary and Health Service Ombudsman;
- National Audit Office;
- NHS Resolution;
- Parliament committees/statements;
- coroners' Prevention of Future Deaths material;
- NHS Blood and Transplant;
- HQIP / national clinical audits;
- professional regulators;
- formal patient-experience sources.

The scan receipt records which rotating families were actually checked.

### Triggered/local sources

Check individual trusts, ICBs, York/Scarborough services and other local bodies **only when**:

- an active lead/watch requires it;
- a material national development creates a clear local question; or
- a credible discovery source points to a specific local development.

Do not attempt to survey all trusts or ICBs daily.

### Discovery

Use a bounded reputable-news scan to discover evidence that primary feeds may obscure. Reporting is discovery material unless it independently warrants durable capture; follow back to primary evidence where possible.

## Durable promotion threshold

A useful item may remain only in the daily scan receipt.

Create a durable `SRC-*` / `REC-*` object only when at least one of these is true:

- it materially changes an existing lead or conclusion boundary;
- it establishes a fact likely to be reused later;
- it creates, satisfies or materially changes an observable watch;
- it supplies important comparable data;
- it materially contradicts or revises existing evidence;
- it supports a bounded new investigation or synthesis question.

Otherwise record the item, attribution and link in the scan receipt and leave it unpromoted.

## Lead promotion

Daily creation of a new `LEAD-NHS-*` should be uncommon.

Create one immediately only where the evidence already supports a bounded, falsifiable/usefully testable question. Otherwise carry the signal in the daily receipt for the weekly synthesis to assess.

Update an existing lead before creating a new one.

## Watch threshold

Create a `WATCH-NHS-*` only for a reasonably observable future event or condition with a meaningful re-check.

Good examples:

- published deadline;
- expected statistics release;
- inquiry/recommendation response;
- implementation milestone;
- known follow-up inspection or formal update.

Do not create a watch whose real meaning is merely "look for anything interesting about this topic". Keep that question in the lead.

## Ingestion discipline

- Deduplicate before creating.
- Prefer primary-source evidence.
- Preserve publication and event dates separately where relevant.
- Separate source facts, attributed statements and analysis.
- Never infer misconduct or causation from correlation.
- Record negative findings only where they genuinely test an existing question.
- Do not lower the evidence threshold on a slow news day.
- Apply `governance/INGESTION_BOUNDARY.md` before committing non-public or personal information.
- Do not put operational `next_check`, expected-date or last-result state in evidence records or leads; link to a watch instead.

## One-commit daily rule

A completed daily run should produce **one atomic intake commit** containing that day's scan and any promoted evidence/lead/watch/index changes.

Preferred commit form:

`NHS intelligence intake — YYYY-MM-DD`

Use the Git data/tree path or a controlled working copy to batch the files. Do not create a file-by-file commit chain.

Do not rewrite or force-push already-published candidate history merely to make older commits prettier; the rule applies prospectively.

## Validation gate

Before moving the weekly branch to the daily candidate, run:

```bash
python3 scripts/validate_repository.py
git diff --check
```

A non-zero result blocks the candidate.

## Branching

Use the current ISO-week branch: `intake/YYYY-Www`.

See `automation/INTAKE_CYCLES.md`.

## Notification rule

Surface only meaningful new developments, strong leads, overdue expected events or action that requires owner attention. Routine no-change scans remain in the repository audit trail.
