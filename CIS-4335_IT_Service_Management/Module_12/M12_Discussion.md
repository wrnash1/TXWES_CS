# Discussion: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

Choose **one** of the three scenarios below. Write an initial post of 175–225 words, then respond substantively to **two classmates** who chose different scenarios. Initial post due by Thursday 11:59 PM; peer responses due by Sunday 11:59 PM.

---

## Scenario A: The Regulatory Deadline Dilemma

A regional healthcare company must deploy a HIPAA-compliant patient portal update by Friday to meet a federal deadline. The release includes a critical privacy consent form. Testing is 95% complete — three edge-case scenarios remain untested due to a test environment outage that was resolved today. The deployment team recommends proceeding; the QA lead recommends a 48-hour hold. Friday is in two days.

**Prompt:** How should the Release Manager resolve this conflict? Apply at least two ITIL 4 guiding principles to your recommendation. What conditions or safeguards, if any, would make a "proceed" decision defensible? What makes a "hold" decision defensible despite the regulatory deadline?

---

## Scenario B: The Canary That Stopped Singing

A fintech startup deployed a payment processing update using a canary strategy. The canary (2% of users) showed excellent error rates for six hours. The team expanded to 25% of users. Within 30 minutes, a high-severity defect appeared — certain international transactions were being declined incorrectly. The team rolled back the 25% cohort but the initial 2% canary group had already been processing transactions for six hours.

**Prompt:** Evaluate the canary deployment process. At what point did the strategy succeed and where did it fall short? What monitoring or acceptance criteria might have caught the international transaction defect earlier? How should the PIR address both the technical finding and the canary monitoring design?

---

## Scenario C: Automation Without Governance

A software company adopted full Continuous Deployment — every commit that passes automated tests is immediately deployed to production. The engineering team is proud of their 50 deployments per day. However, the IT Service Management team is struggling: incidents are difficult to trace to specific deployments, change records are not being created, and the Help Desk has no advance warning of changes. Senior leadership is concerned about audit exposure.

**Prompt:** Is 50 deployments per day inherently problematic from an ITIL 4 perspective, or is the deployment frequency not the issue? What governance controls should be layered onto the CI/CD pipeline to align with ITIL 4 without sacrificing deployment speed? How do you balance the ITIL principles of "optimize and automate" with "keep it simple and practical" in this context?

---

## Peer Response Guidelines

Your peer responses should:

- Engage specifically with your classmate's argument — do not simply restate the scenario.
- Offer one point of agreement with evidence or elaboration.
- Offer one point of constructive challenge or an alternative perspective.
- Be 75–100 words.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses the scenario with depth and accuracy | 4 |
| ITIL 4 concepts correctly applied and cited | 2 |
| First peer response — substantive engagement | 2 |
| Second peer response — substantive engagement | 2 |
| **Total** | **10** |

---

*End of Module 12 Discussion*
