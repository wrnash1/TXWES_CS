# Discussion Forum: Module 14 — Disaster Recovery Management

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

## Instructions

This discussion has three scenarios. You will select **one scenario** for your initial post. Read all three scenarios before choosing — select the one you can engage with most substantively based on your background or professional interest.

**Initial Post:** Due Wednesday at 11:59 PM. Your response to the selected scenario must be 175–225 words. Focus on analysis and professional reasoning, not just description.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who responded to **different** scenarios than your own. Each reply must be a minimum of 75 words and must add analytical value — agreement alone is not sufficient.

---

## Scenario A — The DR Plan That Could Not Be Executed

Vanguard Manufacturing operates a single production facility in Houston, Texas. Hurricane Harvey in 2017 caused a ten-day flooding event that disabled the primary data center. The IT team attempted to activate their DR plan, which referenced a warm site at a colocation facility also located in Houston — twelve miles from the primary. The warm site was also flooded. The backup tapes stored at the warm site were destroyed.

Vanguard lost fourteen days of production data and required six weeks to restore operations from archived cloud backups that had not been updated in the plan. The total business impact exceeded $3.2 million.

The company has hired you to build a new DR program that will not repeat these failures.

In your response:

1. Identify at least three specific DR program design failures that contributed to the fourteen-day data loss and six-week recovery. Be precise — identify the failure type (site selection, backup strategy, testing gap, documentation gap, etc.) and explain why each constitutes a failure.

2. Explain the geographic diversity principle and how it should have been applied to Vanguard's site selection.

3. Propose two specific changes to the backup strategy that would have reduced data loss and accelerated recovery, and explain how each change addresses a root cause from your analysis.

---

## Scenario B — Cloud DR Scope Creep and Unvalidated RTOs

SkyBridge Analytics is a SaaS company providing business intelligence dashboards to 400 enterprise customers. The company migrated its entire infrastructure to AWS twelve months ago. At migration time, the CTO verbally stated: "AWS handles DR for us now." No formal DR plan was written. No testing has occurred.

SkyBridge's most critical service — the real-time dashboard delivery engine — has a contractual SLA to customers requiring 99.9% monthly uptime and a two-hour response-to-restoration commitment in the event of a service disruption.

Last month, an AWS US-East-1 region outage caused a five-hour disruption. SkyBridge had no ability to fail over to another region. Customer SLAs were violated. Three enterprise customers have issued formal notices of contract review.

The board has asked you, as the newly appointed CISO, to assess the DR posture and deliver a remediation plan.

In your response:

1. Explain what the CTO's statement — "AWS handles DR for us" — misunderstands about cloud provider responsibility versus organizational DR accountability.

2. Given the two-hour contractual RTO obligation, identify which AWS DR pattern is most appropriate for the dashboard delivery engine and explain why the current single-region deployment does not meet this requirement.

3. Identify at least two contractual or documentation gaps beyond the technical architecture that contributed to the scope of the incident and the customer relationship risk, and propose how each would be addressed in a formal DR program.

---

## Scenario C — Backup Strategy Failure Under Ransomware Attack

Redwood Community College serves 18,000 students and employs 1,200 staff. In April, the college was hit by ransomware that encrypted all systems connected to the domain, including the student information system, the financial aid platform, and the learning management system. Within six hours of the attack, the ransomware operators had also encrypted the college's connected backup storage (a NAS device on the domain network) and deleted all versioned backups in the college's primary cloud backup account, whose credentials were stored in plain text in an administrator account that was compromised.

The college had no immutable backups. Recovery from scratch took three weeks. Financial aid disbursements to 4,000 students were delayed. The incident attracted state legislative scrutiny.

You have been engaged as an external consultant to help the college build a resilient backup and recovery architecture.

In your response:

1. Identify the specific backup architecture failures that allowed the ransomware to destroy all recovery options. For each failure, name the backup principle or control that was absent.

2. Describe a compliant 3-2-1-1 backup architecture for the college that would survive the same attack scenario. Be specific about where each copy lives, what media type it uses, and how immutability is enforced.

3. Explain what DR testing approach should have detected these backup vulnerabilities before the incident occurred, and describe what a test in that category would have looked like for this organization.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5–6 pts | Addresses all three response elements with analytical depth. Uses accurate terminology from Module 14. Meets 175–225 word range. Demonstrates application of site types, backup strategy, cloud DR, testing, or failover concepts. |
| 3–4 pts | Addresses most response elements but lacks depth in one area. Minor terminology errors or imprecise application of concepts. |
| 1–2 pts | Superficial response. Addresses only one element or demonstrates limited engagement with module content. |
| 0 pts | No initial post submitted by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive replies to two classmates who chose different scenarios. Each reply is 75+ words. Adds analytical content — alternative perspective, additional evidence, constructive challenge, or real-world example. |
| 2–3 pts | One substantive reply and one brief reply, or two replies that are supportive but do not add analytical value. |
| 1 pt | One reply only, or replies are too brief. |
| 0 pts | No peer responses submitted. |

---

## Guidance for Strong Posts

Strong initial posts do the following:

- Use specific module terminology (hot site, warm site, cold site, pilot light, warm standby, RPO, RTO, parallel test, full cutover, 3-2-1-1, CDP, failover, failback) accurately and in context.

- Demonstrate analytical reasoning — explain *why* something is a failure and *why* a recommendation resolves the root cause, not just *what* should be changed.

- Connect the scenario to the broader DR lifecycle (site selection, replication strategy, backup architecture, testing, plan documentation).

- Reference real-world events, professional experience, or published guidance where relevant.

Strong peer responses do the following:

- Engage with a specific point the classmate made — add evidence, offer an alternative framing, or respectfully challenge a conclusion with reasoning.

- Identify a dimension the classmate did not address (for example, a cost consideration, a regulatory angle, or a cloud-specific nuance).

- Ask a follow-up question that advances the conversation analytically.
