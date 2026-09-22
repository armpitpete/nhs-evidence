# NHS Watches

Watches represent **future conditions or expected events**, not claims.

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

Use a watch when the useful question is: "What should happen next, and when should we check?"

Examples:

- consultation response expected;
- implementation deadline approaching;
- inquiry recommendation response due;
- scheduled statistics release;
- next CQC inspection or HSSIB recommendation response;
- promised publication not yet found.

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

Never treat absence of a publication as evidence of failure until the relevant deadline/expectation is established.
