# Daily NHS Intelligence Intake

## Objective

Build the repository into a cumulative NHS intelligence resource that supports both evidence retrieval and generation of new article/investigation ideas.

## Standing branch

Daily work goes to:

`automation/daily-nhs-intake`

Maintain one open pull request from that branch to `main`. Do not merge protected `main` without explicit authorization.

## Daily source priority

### Primary / authoritative

1. NHS England
2. Department of Health and Social Care
3. Care Quality Commission
4. NICE
5. UK Health Security Agency
6. Office for National Statistics
7. NHS trusts and integrated care boards
8. NHS Blood and Transplant, HQIP and other relevant national bodies

### Discovery

Use reputable national, specialist and local journalism to find developments that primary-source feeds may not surface clearly. Reporting must be attributed and should be followed back to primary documentation wherever possible.

## What to look for

- patient-safety developments
- inspection/regulatory findings
- maternity/neonatal care
- emergency and ambulance pressures
- waiting lists and access
- workforce, sickness and pay
- finance and productivity
- digital systems/data programmes
- public-health surveillance
- medicines/treatment guidance
- inequalities
- complaints and patient experience
- implementation of announced reforms
- inquiries/inquests
- unusual or newly released statistics
- repeated appearances of the same trust, ICB, supplier or policy
- Yorkshire/local implications
- contradictions between stated policy and observed outcomes

## Ingestion discipline

- Deduplicate before creating.
- Prefer primary-source evidence.
- Preserve publication/event dates separately where relevant.
- Separate source facts, attributed statements and analysis.
- Never infer misconduct or causation from correlation.
- Update existing timelines/leads when new evidence extends an old story.
- Record negative findings where they genuinely test an existing lead.
- A slow news day is not a reason to lower the evidence threshold.

## Notification rule

Notify the user only when the scan produces meaningful new developments or strong leads. Otherwise update the scan receipt quietly.
