# Discussion — Module 02

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: IAM Design and Least-Privilege Access Control

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose any scenario.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The Over-Privileged Pipeline

A startup's engineering team has been running a data processing pipeline on a Compute Engine VM for the past year. During a security review, you discover that the VM's service account has been granted `roles/owner` at the project level — a configuration set up quickly during the initial launch and never revisited. The pipeline only needs to read data from one Cloud Storage bucket, write results to a BigQuery dataset, and publish messages to a single Pub/Sub topic.

In 175–225 words, address the following:

- What specific security risks does the `roles/owner` grant create for this pipeline?
- Design a least-privilege replacement using specific predefined roles. Identify each role by name and explain why it is needed.
- What process would you recommend the team adopt going forward to prevent over-privileged service accounts from being created under time pressure?

---

## Scenario B — The Contractor Access Problem

Your company regularly hires short-term contractors who need access to GCP resources for project durations of 30 to 90 days. The current process is that a team lead sends an email to the cloud admin, who then manually grants `roles/editor` to the contractor's Gmail account at the project level. When the contract ends, access is sometimes not revoked for weeks because the revocation process relies on HR notifying the cloud admin.

In 175–225 words, address the following:

- What are the security risks in the current process? Identify at least two distinct problems.
- Propose a redesigned access management workflow using GCP IAM features. Consider Google Groups, IAM Conditions, and role selection.
- How would you ensure that access is automatically revoked when a contract ends, using GCP features rather than manual processes?

---

## Scenario C — The Multi-Team Project

A large enterprise has a single GCP project shared by three teams: the backend engineering team, the data analytics team, and the security operations team. Currently all three teams' members have `roles/editor` on the project because it was easier to set up initially. You have been asked to re-architect the IAM configuration to apply least privilege without disrupting each team's ability to do their work.

In 175–225 words, address the following:

- What are the risks of three teams sharing `roles/editor` on the same project?
- Design an IAM structure that gives each team the access they need. For each team, identify specific predefined roles (by name) that are appropriate for their typical tasks.
- Would you recommend keeping all three teams in one project or separating them into multiple projects? Justify your recommendation using IAM inheritance principles.

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Challenges an assumption in the classmate's role selection with a more appropriate alternative
- Points out a predefined role the classmate overlooked that would strengthen the design
- Identifies a practical operational challenge with the classmate's proposed workflow
- Connects the scenario to the lab exercise or to a specific ACE exam objective

Responses that consist only of agreement without substantive additions receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions in the chosen scenario. Uses accurate GCP IAM terminology. Names specific predefined roles correctly. 175–225 words. Demonstrates understanding of least privilege and IAM design.
- 3–4 pts: Addresses most sub-questions but uses vague role names, contains inaccuracies, or falls outside the word count.
- 1–2 pts: Only addresses one sub-question or contains significant IAM misconceptions.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each contributing specific technical content.
- 2 pts: Only one qualifying response, or both are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: In practice, IAM design is one of the first things a cloud security team reviews when they inherit an environment. The patterns you discuss here — least privilege, service accounts over user keys, time-bounded access — are not theoretical. They come up in every real GCP security audit. Ground your responses in the specific role names and GCP features covered in the module.

---

End of Discussion — Module 02

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
