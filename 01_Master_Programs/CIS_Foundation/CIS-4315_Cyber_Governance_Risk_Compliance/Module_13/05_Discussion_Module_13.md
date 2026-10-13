# Discussion Forum: Module 13 — Business Continuity Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

## Instructions

This discussion has three scenarios. You will select **one scenario** for your initial post. Read all three scenarios before choosing — select the one that you can engage with most substantively based on your background or professional interest.

**Initial Post:** Due Wednesday at 11:59 PM. Your response to the selected scenario must be 175–225 words. Focus on analysis and professional reasoning, not just description.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who responded to **different** scenarios than your own. Each reply must be a minimum of 75 words and must add analytical value — agreement alone is not sufficient.

---

## Scenario A — The Assumption That Was Never Tested

Cascade Financial Partners is a mid-size investment advisory firm. Five years ago, the firm documented an RTO of four hours for its client portfolio management system and invested in a warm standby environment at a colocation facility twenty miles away. The plan was approved by the CIO and filed. It has never been tested.

Last month, a fiber cut disrupted the firm's primary data center connectivity. The IT team attempted to activate the warm standby for the first time under real conditions. They discovered that the replication process had silently failed eighteen months earlier due to a software version incompatibility. The standby environment contained data that was nineteen months old. Recovery from a cold backup took eleven hours — nearly three times the four-hour RTO.

The CIO is now defending the BCP program to the board and has asked you, as the Information Security Manager, to produce a corrective action plan.

In your response:

1. Identify the specific control failures that contributed to this outcome, distinguishing between plan design failures and maintenance failures.

2. Explain what a testing program (specifying type and frequency) would have most likely detected and at what point.

3. Propose three specific, actionable improvements to the BCP program that address the root causes, not just the symptoms.

---

## Scenario B — BIA Without Teeth

Northgate University is a regional four-year institution with approximately 8,000 students. The university's IT department recently completed its first Business Impact Analysis. The BIA identified sixteen critical processes and produced an RTO matrix. However, when the BIA results were presented to the Provost and VP of Finance, both executives declined to fund any of the recommended continuity strategies, citing budget constraints.

The VP of Finance stated: "Our endowment is solid. If systems go down, we will deal with it. We have dealt with outages before." The IT Director, frustrated by the outcome, has asked you to help make a stronger case.

In your response:

1. Explain what critical information the executives appear to be missing in their risk assessment. What questions should the BIA have answered that may not have been communicated effectively?

2. Describe how you would reframe the BCP investment conversation for non-technical senior leadership. What financial, regulatory, or reputational evidence would strengthen the case?

3. Identify at least one low-cost continuity strategy option that could address one of the sixteen critical processes without requiring a major capital investment, and explain why it is viable despite budget constraints.

---

## Scenario C — Cloud Continuity and Contractual Gaps

Streamline Logistics operates a nationwide freight coordination platform. The company recently migrated its operations to a major public cloud provider. The cloud architecture uses a single-region deployment with automated daily snapshots. The company's BCP documentation, written before the cloud migration, still references the old on-premises warm standby site that was decommissioned during the migration.

The company's largest enterprise customer has just issued a contractual addendum requiring Streamline to demonstrate an RTO of two hours and an RPO of fifteen minutes for the freight coordination platform. The current single-region cloud deployment with daily snapshots cannot meet either requirement.

The Chief Operating Officer has asked you to assess the gap and recommend a cloud architecture that meets the contractual requirements.

In your response:

1. Analyze the gap between the current architecture and the contractual RTO/RPO requirements. Be specific about what each metric requires technically.

2. Recommend a cloud continuity architecture that can meet both the two-hour RTO and the fifteen-minute RPO. Describe at least two specific cloud DR patterns (such as pilot light, warm standby, or multi-region active-active) and explain which is most appropriate for this use case.

3. Identify at least two BCP documentation updates that are required regardless of the technical architecture change, and explain why documentation currency matters independently of technical capability.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5–6 pts | Addresses all three response elements with analytical depth. Uses accurate terminology from Module 13. Meets 175–225 word range. Demonstrates application of BIA, RTO/RPO/MTPD, strategy, or testing concepts. |
| 3–4 pts | Addresses most response elements but lacks depth in one area. Minor terminology errors or imprecise application of concepts. |
| 1–2 pts | Superficial response. Addresses only one element or demonstrates limited engagement with module content. |
| 0 pts | No initial post submitted by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive replies to two classmates who chose different scenarios. Each reply is 75+ words. Adds analytical content — alternative perspective, additional evidence, constructive challenge, or real-world example. |
| 2–3 pts | One substantive reply and one brief reply, or two replies that are supportive but do not add analytical value. |
| 1 pt | One reply only, or replies are too brief (under 75 words each). |
| 0 pts | No peer responses submitted. |

---

## Guidance for Strong Posts

Strong initial posts do the following:

- Use specific module terminology (RPO, RTO, MTPD, BIA, tabletop, simulation, full interruption) accurately and in context.

- Demonstrate analytical reasoning — explain *why* something is a problem or *why* a recommendation is appropriate, not just *what* should be done.

- Connect the scenario to the broader BCP lifecycle (initiation, BIA, strategy, plan, test, maintain).

- Reference real-world analogues from your professional or academic experience where relevant.

Strong peer responses do the following:

- Engage with a specific point the classmate made — agree or disagree with reasoning, not just conclusions.

- Add a dimension the classmate did not address (for example, a regulatory angle, a cost consideration, or an alternative strategy).

- Ask a follow-up question that extends the conversation constructively.
