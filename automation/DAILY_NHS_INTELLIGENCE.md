# Daily NHS Intelligence Intake

## Authority

Scheduling is owned by the **Merrin Task Registry**:

- **T-113** — daily NHS intelligence intake
- **T-114** — weekly NHS intelligence synthesis
- **T-115** — monthly NHS intelligence synthesis

Standalone ChatGPT scheduling for this work is retired. Protected `main` is never merged by these tasks without explicit owner authorization.

## Objective

Build a cumulative NHS intelligence resource that supports evidence retrieval, follow-up accountability and generation of new article/investigation ideas.

## Daily source priority

### Tier 1 — core authoritative sources

Check routinely:

1. NHS England
2. Department of Health and Social Care
3. Care Quality Commission
4. NICE
5. UK Health Security Agency
6. Office for National Statistics
7. Health Services Safety Investigations Body (HSSIB)
8. NHS trusts and integrated care boards

### Tier 2 — oversight, accountability and specialist sources

Check on a rolling or triggered basis:

- Parliamentary and Health Service Ombudsman
- NHS Resolution
- National Audit Office
- coroners' Prevention of Future Deaths reports
- Parliament: Health and Social Care Committee, Public Accounts Committee, written statements and relevant deposited material
- NHS Blood and Transplant
- Healthcare Quality Improvement Partnership and national clinical audits
- professional regulators where directly relevant
- Healthwatch and other formal patient-experience evidence where relevant

### Discovery

Use reputable national, specialist and local journalism to discover developments that primary-source feeds may not surface clearly. Reporting must be attributed and should be followed back to primary documentation wherever possible.

## Two daily questions

Every run must ask both:

1. **What changed since the last scan?**
2. **What old question, deadline, promise or expected publication is due for re-checking now?**

The second question is mandatory. The project must not become dependent on the news cycle.

## What to look for

- patient safety
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
- overdue recommendations, promises, consultations or implementation dates

## Ingestion discipline

- Deduplicate before creating.
- Prefer primary-source evidence.
- Preserve publication and event dates separately where relevant.
- Separate source facts, attributed statements and analysis.
- Never infer misconduct or causation from correlation.
- Update existing timelines/leads/watches when new evidence extends an old story.
- Record negative findings where they genuinely test an existing lead.
- Do not lower the evidence threshold on a slow news day.
- Apply `governance/INGESTION_BOUNDARY.md` before committing non-public or personal information.

## Branching

Use the current ISO-week branch: `intake/YYYY-Www`.

The first cycle, 2026-W39, supersedes the earlier standing-branch experiment. See `automation/INTAKE_CYCLES.md`.

## Notification rule

Surface only meaningful new developments, strong leads, overdue expected events or action that requires owner attention. Routine no-change scans remain in the repository audit trail.
