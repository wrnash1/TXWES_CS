# Discussion Forum: Module 15 — DevOps, Agile, and ITIL 4 Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

The integration of DevOps, Agile, and ITIL 4 raises real organizational questions that have no single correct answer. These scenarios ask you to reason through trade-offs, make recommendations grounded in the frameworks, and engage critically with your classmates' perspectives. Avoid generic definitions — apply the concepts to the specific context of each scenario.

---

## Scenario 1: The Change Advisory Board Bottleneck

A financial technology company has adopted DevOps practices and now deploys 40–60 times per week using an automated pipeline. However, their Change Advisory Board meets once per week on Thursdays. Every deployment — regardless of size or risk — must be approved by the CAB before it proceeds to production. This means that on Monday, a critical security patch must wait until Thursday before it can be deployed. A product manager has proposed eliminating the CAB entirely. The CISO is opposed.

**Initial Post Prompt (Due Wednesday at 11:59 PM):**

In 175–225 words, respond to the following:

- Using ITIL 4's three change types, explain how this company should restructure its change authorization model — without eliminating the CAB — to support both DevOps deployment frequency and appropriate governance.
- What criteria would you use to distinguish standard changes (automated pipeline deployment) from normal changes (requiring CAB review) for this company's specific context?
- Why is the CISO's concern about eliminating the CAB valid, even in a DevOps environment?

**Peer Response Prompt (Due Sunday at 11:59 PM):**

Respond to at least two classmates' posts (minimum 75 words each):

- Evaluate whether their standard change criteria are specific enough to be operationalized — could a developer determine if their change qualifies without asking a manager?
- Challenge or affirm their assessment of the CISO's concern
- Propose one specific scenario that would require a normal change review even in a high-frequency DevOps environment

---

## Scenario 2: The Value Stream Wake-Up Call

A government agency's IT department conducts its first-ever value stream map for its software delivery process. The results are sobering: total lead time from approved user story to production is 67 days. The total value-added time — actual coding, testing, and deployment work — is 9 days. The remaining 58 days are consumed by approval queues, meeting schedules, and handoffs between teams. The agency's CIO presents this data to senior leadership and receives the response: "Those approval steps are required for security and compliance reasons. You cannot remove them."

**Initial Post Prompt (Due Wednesday at 11:59 PM):**

In 175–225 words, respond to the following:

- How would you respond to the CIO's challenge? Are all 58 days of wait time genuinely required for compliance, or is there a distinction between compliance-required process and accumulated bureaucratic waste?
- Identify two specific types of wait time in a government IT context that are genuinely compliance-required versus two that are likely remediable waste.
- What would an achievable future-state value-added ratio look like for a government agency — and why would 100% value-added ratio be neither achievable nor desirable?

**Peer Response Prompt (Due Sunday at 11:59 PM):**

Respond to at least two classmates' posts (minimum 75 words each):

- Evaluate their compliance vs. waste distinction — do you agree with their classifications? Offer a specific counterexample if you disagree.
- Add one technique from Lean or Agile that could reduce wait time without eliminating any genuinely required compliance step
- Discuss whether the government context makes the DevOps velocity-governance trade-off fundamentally different from a private sector context

---

## Scenario 3: The SRE Adoption Conflict

A retail e-commerce company is piloting Site Reliability Engineering for its most critical service — the shopping cart and checkout flow. The SRE team has set an SLO of 99.95% monthly availability and calculated a monthly error budget of 21.9 minutes. In month two of the pilot, two deployments caused incidents that consumed 19 minutes of the error budget in the first two weeks of the month. The SRE team proposes freezing all non-critical deployments for the remaining two weeks. The product team pushes back: "We have 12 features ready to ship and a marketing campaign launching next week that depends on three of them."

**Initial Post Prompt (Due Wednesday at 11:59 PM):**

In 175–225 words, respond to the following:

- Evaluate the SRE team's proposal to freeze deployments using the error budget framework — is this the right decision? Are there alternatives?
- How should the three marketing-campaign-dependent features be handled given the error budget situation?
- What does this scenario reveal about the organizational communication that must accompany an SRE adoption — specifically what stakeholders need to understand about error budgets before the model is deployed?

**Peer Response Prompt (Due Sunday at 11:59 PM):**

Respond to at least two classmates' posts (minimum 75 words each):

- Evaluate whether their approach to the marketing campaign features is consistent with the error budget model or represents an exception that could undermine the model
- Add one specific way the SRE team could have prevented this conflict through earlier stakeholder communication
- Discuss whether a 99.95% SLO is appropriate for this service or whether it should be calibrated differently

---

## Discussion Rubric (10 Points Total)

**Initial Post (6 Points):**

- 5–6 pts: Thoroughly addresses all prompt questions with accurate DevOps, Agile, and ITIL 4 terminology, substantive reasoning, and meets the word count requirement.
- 3–4 pts: Addresses most prompt questions but lacks depth, accuracy, or sufficient use of course concepts.
- 0–2 pts: Incomplete, off-topic, or missing initial post.

**Peer Responses (4 Points):**

- 4 pts: Substantive replies to at least two peers that advance the discussion with new analysis, challenges, or examples.
- 2 pts: Replies to only one peer, or responses are superficial without meaningful addition to the conversation.
- 0 pts: No peer responses submitted.
