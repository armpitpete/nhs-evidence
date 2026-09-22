# Accountability & Promise Tracking v0.1 — authority contract

Status: **CONTRACT FROZEN — candidate implementation**

## Mission

Build a longitudinal evidence memory of the NHS that can detect meaningful change, hold institutions to their stated commitments, identify failures and improvements, and turn the evidence into accountability reporting, practical remedy analysis and bounded investigations.

## Hard invariant

**Never overwrite the old position with the new one. Preserve both, identify the transition, and distinguish the observed change from any explanation for why it happened.**

## Authority boundary

v0.1 extends the accepted evidence model. It does **not** create a new authority object.

- Evidence records preserve promises, obligations, targets, recommendations, delivery evidence, outcomes and remedies.
- WATCH-NHS objects remain the sole operational authority for expected events and future check timing.
- Leads contain questions and hypotheses.
- Scans are audit receipts.
- Weekly/monthly syntheses derive accountability views from those objects.
- The derived Promise Ledger is a view, never a source of truth.

The operating loop is:

**commitment → preserved baseline → watch → delivery/change evidence → status history → accountability question → remedy evidence → re-check**

## Material commitment test

A statement is promoted as a material commitment only when it is attributable to an authoritative body and sufficiently testable.

Allowed commitment classes:

- promise
- target
- obligation
- publication-commitment
- recommendation
- aspiration
- forecast
- announcement

Recommendations, aspirations, forecasts and announcements are preserved as their own class and must not be silently treated as promises.

## Baseline contract

A material baseline captures issuer, responsible body, date, scope, deadline where one exists, success criterion, source and commitment class.

A baseline always starts at **promise_status: announced**. Later status is represented by a **new status-change evidence record**, never by rewriting the baseline.

Baseline material fields are protected by a deterministic fingerprint and, after acceptance on protected main, by history comparison.

## Promise status vocabulary

- announced
- implementation-started
- on-track
- fulfilled
- partially-fulfilled
- delayed
- scope-changed
- target-changed
- responsibility-changed
- superseded
- withdrawn
- unmet
- unverifiable

### Evidence rule

A consequential status requires inspectable source evidence.

**Absence of evidence is not evidence of non-delivery.** An unmet status requires either positive evidence that the commitment was not delivered, or a passed deadline plus authoritative evidence establishing non-delivery.

If delivery cannot be established, use unverifiable or retain the prior supported state and record the evidence gap.

## Transition classes

- implementation-started
- implementation-update
- fulfilled
- partial-delivery
- deadline-change
- scope-change
- target-change
- responsibility-change
- measurement-change
- outcome-change
- superseded
- withdrawn
- unmet
- evidence-gap

A wording change is material only when it changes meaning, certainty, obligation, scope, responsibility, measurement or interpretation.

## Explanation rule

Each status-change record states one explanation status:

- established
- attributed
- inferred
- unknown

Observed transition and explanation are separate. Established, attributed and inferred explanations require linked evidence. Unknown is the default when cause is not established.

## Failure contract

A failure finding requires a defined expectation and evidence of divergence.

Recognised classes include missed deadline, incomplete implementation, scope reduction, target reduction, promised service unavailable, implementation without expected outcome, repeated patient-safety failure, governance/accountability breakdown, measurement/reporting failure and transparency/evidence failure.

The system distinguishes demonstrated failure, potential failure, unresolved evidence gap and apparent failure later disproved. It preserves counter-evidence and successful delivery.

## Remedy contract

For a material demonstrated problem, ask what might correct it, while keeping remedy confidence separate from problem severity.

Allowed remedy evidence levels:

- official-recommendation
- evaluated
- comparator-supported
- proposed
- speculative

A proposed remedy is not presented as "the solution" unless evidence justifies that claim.

## Daily operation

T-113 checks due promise watches first, detects material commitments, compares new evidence against preserved previous states, creates status-change records only when supported, records improvement as readily as failure, carries uncertainty forward, and produces one atomic daily commit.

## Weekly operation

T-114 performs Promise Review, Change Detection Review, Failure Review, Improvement Review, Remedy Review, Yorkshire/local comparison and next accountability checks.

The weekly report prioritises state change, not publication volume.

## Monthly operation

T-115 asks whether multiple weekly transitions show a sustained direction of travel. It must not promote a single event into a monthly pattern.

## Escalation

Escalation means deeper evidence work, not automatic accusation or external contact.

Triggers include missed deadline, material scope/target change, responsibility transfer, changed success criterion, contradictory delivery evidence, repeated failure, disappearance of promised evidence and material divergence between outcome and commitment.

## Acceptance test

Given a real NHS commitment, the system must preserve exactly what was promised, determine the supported current state, detect later material changes, distinguish delivery/failure/uncertainty, and generate a fair evidence-backed accountability question or remedy without rewriting history or inventing causation.
