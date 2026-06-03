# Discussion Forum: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

Release and Deployment Management is where IT strategy becomes operational reality. The decisions made in a deployment window — which approach to use, how detailed the rollback plan is, what gets documented in release notes — can mean the difference between a seamless update and a production incident that affects thousands of users. This discussion asks you to apply module concepts to real-world deployment scenarios.

---

## Scenario 1: The Missing Rollback Plan

A regional insurance company is deploying a new claims-processing module on a Friday night. The release manager confirms the deployment plan covers the deployment steps and post-deployment tests but notices the rollback section is blank — the team "didn't have time to write it." The deployment proceeds. At 1 AM Saturday, a critical integration with the policy database fails and affects all claims adjusters. The team spends four hours diagnosing and manually reversing the deployment because there is no documented rollback procedure.

**Initial Post Prompt (Due Wednesday at 11:59 PM):**

In 175–225 words, respond to the following:

- From an ITIL 4 perspective, what governance failure allowed this deployment to proceed without a rollback plan, and which practice should have caught it?
- Describe what a complete rollback plan for this scenario should have included — specifically address the database integration component.
- What would you recommend the organization add to its deployment approval checklist to prevent this from recurring?

**Peer Response Prompt (Due Sunday at 11:59 PM):**

Read at least two classmates' posts and write a substantive reply (minimum 75 words each) that does one or more of the following:

- Offers an alternative view of which practice bears primary responsibility for the governance failure
- Challenges or builds on their rollback plan recommendation with a specific technical consideration
- Shares a real or hypothetical example that illustrates the stakes of inadequate rollback planning

---

## Scenario 2: Choosing the Right Deployment Approach

A university is upgrading its student information system — the platform that manages enrollment, grades, financial aid, and scheduling for 18,000 students. The upgrade window is the week after final exams. The system has a complex Oracle database back-end, and the new version includes a schema migration. The CIO wants "the safest possible approach." Three team members disagree on the approach: one advocates big bang (simpler to manage), one advocates phased deployment (limit exposure), and one advocates blue-green (instant rollback if needed).

**Initial Post Prompt (Due Wednesday at 11:59 PM):**

In 175–225 words, respond to the following:

- Evaluate all three proposed approaches for this specific scenario — consider the database schema migration, the user population size, and the timing.
- Recommend one approach and justify your recommendation using ITIL 4 Release and Deployment Management principles.
- Identify the single greatest risk in your recommended approach and explain how you would mitigate it.

**Peer Response Prompt (Due Sunday at 11:59 PM):**

Respond to at least two classmates whose recommendation differs from yours. In each reply (minimum 75 words):

- Acknowledge the merit in their recommendation
- Identify one specific risk in their chosen approach that they may not have addressed
- Propose a mitigation for that risk or explain why you believe it makes their approach unsuitable for this scenario

---

## Scenario 3: Post-Implementation Review Culture

A mid-sized logistics company has conducted post-implementation reviews after every major release for the past three years. However, the PIR reports consistently identify the same three problems — deployment windows routinely run over by 30–45 minutes, release notes omit database dependency information, and rollback plans are written but never tested before go-live. Despite three years of PIR reports documenting these patterns, nothing has changed.

**Initial Post Prompt (Due Wednesday at 11:59 PM):**

In 175–225 words, respond to the following:

- What does this pattern reveal about how this organization is conducting its PIRs? What is missing from their process beyond just writing the report?
- Connect this scenario to ITIL 4's Continual Improvement practice — specifically the role of the Continual Improvement Register in turning PIR findings into action.
- Describe two concrete process changes the organization should implement immediately, including who should own each change and how success would be measured.

**Peer Response Prompt (Due Sunday at 11:59 PM):**

Respond to at least two classmates' posts (minimum 75 words each):

- Evaluate whether their proposed process changes address the root cause or only the symptoms
- Add one recommendation they did not include
- Discuss whether organizational culture or process design is the deeper issue in this scenario

---

## Discussion Rubric (10 Points Total)

**Initial Post (6 Points):**

- 5–6 pts: Thoroughly addresses all prompt questions with accurate ITIL 4 terminology, substantive reasoning, and meets the word count requirement.
- 3–4 pts: Addresses most prompt questions but lacks depth, accuracy, or sufficient use of course concepts.
- 0–2 pts: Incomplete, off-topic, or missing initial post.

**Peer Responses (4 Points):**

- 4 pts: Substantive replies to at least two peers that advance the discussion with new analysis, challenges, or examples.
- 2 pts: Replies to only one peer, or responses are superficial (e.g., "Great point!" without substance).
- 0 pts: No peer responses submitted.
