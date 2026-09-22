# NHS Watches

Watches represent **observable future conditions or expected events**, not claims and not generic research interests.

## Sole operational authority

`WATCH-NHS-*` objects are the repository's **only authority** for:

- expected event;
- expected-by date;
- next check;
- last checked;
- last result;
- operational watch status;
- closure reason.

Evidence records preserve what a source said. Leads preserve questions and hypotheses. They may reference watches, but must not duplicate operational timing or check state.

## Creation threshold

Create a watch only when all of the following are true:

1. there is a reasonably observable future event/condition;
2. checking again at a defined or justified interval could change the evidence state;
3. the event is linked to existing evidence or a bounded lead.

Good examples:

- consultation response expected;
- implementation deadline approaching;
- inquiry recommendation response due;
- scheduled statistics release;
- expected inspection/update;
- promised publication not yet observed.

Do **not** create a watch equivalent to "monitor this topic" or "look for more information". Keep that as a lead question until an observable trigger exists.

## IDs

`WATCH-NHS-YYYY-NNNN`

## Required state

A watch records:

- trigger/expected event;
- why it matters;
- source/evidence IDs;
- related lead/record IDs;
- expected date when known;
- next check;
- last checked;
- result;
- status;
- closure reason when applicable.

## Weekly hygiene

T-114 reviews open watches weekly:

- close/satisfy completed watches;
- supersede duplicates;
- identify overdue watches;
- reject vague indefinite monitoring;
- preserve closed/superseded history rather than deleting it.

Never treat absence of a publication as evidence of failure until the relevant deadline/expectation is established.
