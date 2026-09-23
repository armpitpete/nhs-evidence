# Accountability & Promise Tracking v0.1 — acceptance receipt

Status: **MERGED / ACCEPTED**

## Authority

This candidate implements the frozen contract in `governance/ACCOUNTABILITY_PROMISE_TRACKING_V0.1.md`.

It does not create a new source of truth. Evidence records preserve commitments and later status/remedy evidence; WATCH-NHS remains the sole operational timing authority.

## Acceptance question

> Given a real NHS commitment, can the system preserve exactly what was promised, continuously determine what actually happened, detect when the commitment changes, distinguish delivery from failure or uncertainty, and generate a fair evidence-backed accountability question or remedy without rewriting history or inventing causation?

## Machine result

**PASS on the implementation candidate and PASS again on the resulting protected-main merge SHA.**

Validated evidence included:

- repository structural validation;
- accountability baseline/status/remedy/watch-link validation;
- 12 canonical lifecycle scenarios;
- hostile rejection of historical baseline rewrite;
- hostile rejection of unsupported fulfilment/non-delivery status;
- hostile rejection of causal explanation without evidence;
- hostile rejection of vague indefinite watches;
- hostile rejection of orphaned status evidence;
- Promise Ledger reproducibility;
- relationship/index/secret-pattern checks;
- `git diff --check`;
- comparison against protected main.

Final candidate exact-head validation passed at `48b21028158576f4c3426a3f98be37318742a95c`.

Protected merge produced `a2635f29a514bcdfc7c5a994146006d3f131f49b`, with exact parents:

- previous protected main: `06f6a79b2a2572f0a6241847ee47ad78eb4a9fce`;
- accepted PR #4 head: `48b21028158576f4c3426a3f98be37318742a95c`.

Post-merge exact-main validation passed.

## Live pilot cases

### Martha's Rule

The contractual obligation to implement all three core components by **31 March 2027** is preserved as an immutable baseline.

Later evidence is a separate status record: **implementation-started**.

The deadline has not passed. The system does not call the promise fulfilled or unmet.

### Thirlwall

The system preserves separately:

1. NHS organisational review/follow-up actions;
2. the government's promise to publish a full response after detailed consideration.

Immediate work is not silently converted into completion of either baseline. No missed-deadline finding is made where no deadline is established.

### ONS September releases

Confirmed publication dates are preserved as a publication commitment.

The release calendar is not treated as proof that publication occurred. The watch must observe publication before a fulfilled/delayed/unmet status is created.

### Mental-health crisis emergency care

HSSIB provides demonstrated national patient-safety problem evidence plus formal remedy recommendations.

Those recommendations are stored as **official-recommendation remedy evidence**, not silently converted into DHSC/NHS England promises and not presented as proven solutions.

## Fairness properties demonstrated

- old position is preserved;
- later state is a new record;
- absence of evidence is not non-delivery;
- success/improvement is structurally representable alongside failure;
- an unmet finding requires positive non-delivery evidence or deadline plus authoritative non-delivery evidence;
- recommendations, aspirations, forecasts and announcements are distinct from promises/obligations;
- explanation/cause is separately classified and evidenced;
- remedy confidence is separate from failure severity;
- the Promise Ledger is derived and reproducible rather than authoritative.

## Reporting outputs

Candidate includes:

- `index/promise-ledger.md`;
- commitment timelines;
- weekly NHS Accountability Report template;
- monthly NHS Accountability Review template;
- partial Week 39 accountability prototype.

The full Week 39 report is date-gated to **27 September 2026 at 18:00 Europe/London**. The first full monthly accountability review covers October 2026 and is due **1 November 2026 at 10:00**.

## Known limitations

1. The live pilot has not yet reached a due commitment that can honestly demonstrate a real-world **fulfilled** status. Fulfilment is tested in canonical scenarios but must not be fabricated in live evidence.
2. The Week 39 prototype covers only evidence available through 22 September; it is not a full weekly conclusion.
3. The protected-main history currently contains no accepted accountability baseline, so cross-branch historical preservation checking becomes materially useful after the first accepted merge.
4. Some commitments have no stated deadline. They can be watched for an observable event but cannot fairly be labelled late without a supported time expectation.
5. Remedy evidence may identify credible interventions without establishing that they will solve a specific local problem.

## Human review

**APPROVED by owner on 22 September 2026.**

The owner explicitly approved the Accountability & Promise Tracking v0.1 human review and authorized merging PR #4 at exact head `48b21028158576f4c3426a3f98be37318742a95c` into protected `main`.

## Protected merge receipt

PR #4 was merged successfully.

Resulting protected-main SHA:

`a2635f29a514bcdfc7c5a994146006d3f131f49b`

Post-merge exact-main checks passed.

## Final state

**Accountability & Promise Tracking v0.1 — MERGED / ACCEPTED.**
