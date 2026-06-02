# Discussion — Module 01

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: GCP Resource Hierarchy and Infrastructure Design

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose the same scenario or a different one.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The University Cloud Migration

Texas Wesleyan University is planning to migrate its on-premises IT infrastructure to Google Cloud. The university has four departments — Computer Science, Business, Student Services, and Athletics — each with its own budget, team of IT staff, and set of applications. The CTO wants each department to have autonomy over its own GCP resources while still allowing the central IT office to enforce security policies across all departments. The CTO has heard about GCP Folders, Projects, and Organization Policies, but is unsure how to structure the hierarchy and where to apply controls.

In 175–225 words, design a GCP resource hierarchy for this scenario. Address the following:

- How would you use the Organization node, Folders, and Projects to reflect the university's structure?
- Where in the hierarchy would you apply IAM policies to give departments autonomy while preserving central IT control?
- Identify one Organization Policy constraint that would be critical to apply at the Organization level and explain why.

---

## Scenario B — The Startup Budget Crisis

A startup's engineering team is running all development and production workloads in a single GCP Project in `us-central1-a`. Last month their bill unexpectedly reached $4,200 — nearly double their budget. The CTO asks you to implement controls so that the team is always aware of spending before it spirals, and to architect the environment to prevent a single data center failure from taking down the production application. The team has a modest budget and cannot afford multi-region deployment.

In 175–225 words, address the following:

- What specific GCP billing controls would you implement, and what are their limitations?
- How would you re-architect the deployment to improve availability within the single-region budget constraint?
- If the team decides to build automation that actually stops resources when spending crosses a threshold, what GCP services would you use and what is the architectural flow?

---

## Scenario C — The Cloud Governance Audit

Your company's internal security audit reveals that several engineers have been creating GCP Projects using personal `@gmail.com` accounts rather than corporate accounts, and some projects have resources running in unauthorized regions outside of North America. Additionally, the audit finds that some projects have no Billing Account linked, meaning cloud usage in those projects is either unpaid or masked from financial reporting.

In 175–225 words, address the following:

- How does using personal Gmail accounts instead of a corporate Google Workspace domain affect the GCP resource hierarchy and governance capabilities?
- What Organization Policy constraint would you apply to prevent resource creation outside approved regions, and at what hierarchy level?
- What process or GCP feature would help ensure all new Projects are linked to an approved Billing Account before any resources can be created?

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Points out an assumption in the classmate's design and offers an alternative
- Adds a GCP feature or constraint the classmate did not mention that strengthens their solution
- Raises a realistic operational challenge with the classmate's approach and suggests a mitigation
- Connects the classmate's scenario to something from the lab or from the ACE exam guide

Responses that only say "Good post" or "I agree with your approach" without elaboration receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions in the chosen scenario with accurate GCP terminology, a coherent design rationale, and 175–225 words. Demonstrates understanding of hierarchy, IAM inheritance, and Organization Policies.
- 3–4 pts: Addresses most sub-questions but lacks technical depth, contains inaccuracies in GCP terminology, or falls outside the word count range.
- 1–2 pts: Addresses only one sub-question or contains significant factual errors about GCP hierarchy or billing.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each adding substantive technical content to the conversation.
- 2 pts: Only one qualifying peer response submitted, or both responses are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: There is no single correct answer to any of these scenarios. Cloud architecture involves real trade-offs between cost, complexity, security, and operational overhead. What matters in your initial post is that your design decisions are well-reasoned, technically grounded in GCP's actual capabilities, and directly responsive to the constraints stated in the scenario.

---

End of Discussion — Module 01

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
