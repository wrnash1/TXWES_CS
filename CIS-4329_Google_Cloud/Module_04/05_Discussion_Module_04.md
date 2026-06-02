# Discussion — Module 04

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Storage Design — Classes, Lifecycle, and Access Control

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose any scenario.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The Media Archive Strategy

A regional television station is migrating its entire video archive to Google Cloud. The archive contains 50 years of footage — approximately 2 petabytes of video files. The station's usage pattern is:

- Current season content (last 12 months): accessed daily for production and re-broadcast
- Content from 1 to 5 years ago: accessed approximately once per month for retrospective programming
- Content older than 5 years: accessed at most once or twice per year for anniversary specials
- Content older than 20 years: almost never accessed; kept strictly for historical preservation

The station has a fixed monthly storage budget and wants to minimize costs without deleting any content.

In 175–225 words, address the following:

- Map each age tier of content to the appropriate Cloud Storage class and justify each choice.
- Design a lifecycle policy that automates these transitions. Describe the specific rules (action, condition) even if you do not write exact JSON.
- The station's content management system needs programmatic read access to all buckets. What IAM configuration would you apply, and would you use a service account or user credentials?

---

## Scenario B — The Healthcare Compliance Challenge

A regional hospital is migrating its electronic health records (EHR) system to Google Cloud. EHR files must be retained for a minimum of 10 years under HIPAA regulations. Files cannot be modified or deleted during the retention period. The hospital's security team is also concerned about accidental deletion by authorized administrators who have broad storage permissions.

In 175–225 words, address the following:

- Which specific Cloud Storage feature would you use to enforce the 10-year retention requirement? Explain the difference between an unlocked and a locked retention policy and which you would recommend for HIPAA compliance.
- The hospital's existing data governance team says "we'll use object versioning because it lets us recover deleted files." Why is versioning alone insufficient for HIPAA retention compliance? What does it protect against that a retention policy does not, and vice versa?
- What bucket location type would you choose for EHR data that must remain within the United States, and why?

---

## Scenario C — The External Partner Sharing Problem

A pharmaceutical company runs a research collaboration with three university partners. The company stores proprietary research datasets in a private Cloud Storage bucket. Each university needs periodic access to different specific files — not the entire bucket. The universities use various systems and email domains (not Google Workspace). Access to each file should expire after 72 hours, after which the university must request fresh access. The company's security policy prohibits making any bucket or object publicly accessible.

In 175–225 words, address the following:

- What Cloud Storage feature would you use to provide file-level, time-limited access to the university partners without violating the public access prohibition?
- The company's developer suggests using `allAuthenticatedUsers` instead because "all three universities have users with Google accounts." Explain why this is still inappropriate and what the security difference is between `allAuthenticatedUsers` and a signed URL.
- Describe the operational workflow for the sharing process: how does a university researcher request a file, how does the company IT team generate access, and how does the 72-hour expiration enforce itself without manual intervention?

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Identifies a minimum storage duration implication the classmate did not address in their storage class selection
- Points out a security gap in the classmate's access control design
- Raises a regulatory or compliance consideration the classmate overlooked
- Connects the scenario to a specific gcloud storage command from the lab

Responses that consist only of praise or agreement without substantive additions receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions accurately. Uses correct storage class names and retention/versioning terminology. Justifies design choices with reference to access frequency, minimum storage durations, or compliance requirements. 175–225 words.
- 3–4 pts: Addresses most sub-questions but contains inaccuracies in storage class selection, ignores minimum storage durations, or lacks justification.
- 1–2 pts: Only addresses one sub-question or contains significant factual errors about Cloud Storage features.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each contributing specific technical content.
- 2 pts: Only one qualifying response, or both are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Storage cost optimization is one of the most tangible wins in cloud migrations. When organizations move from on-premises storage — where the cost of a disk is a one-time capital expense — to cloud object storage where you pay by the gigabyte per month, choosing the wrong storage class can mean paying 20x more than necessary for data nobody is reading. The lifecycle policy system exists precisely to automate this optimization. In your discussion posts, show that you understand the trade-offs between access cost and storage cost at each tier.

---

End of Discussion — Module 04

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
