# Discussion Forum: Module 16 — Data+ DA0-001 Exam Preparation and Capstone

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Overview

This discussion asks you to apply integrated knowledge from all five Data+ exam domains to professional decision-making scenarios that mirror the scenario-based reasoning tested on the certification exam. Choose one of the three scenarios below, write an original post of 175–225 words, then respond to at least two classmates who chose different scenarios. Responses must be 75–100 words and add new reasoning rather than simply agreeing.

---

### Scenario A — The Pipeline Architecture Decision

A mid-sized retail company is migrating its analytics infrastructure to Google Cloud. The data engineering team proposes two options. Option 1: transform all raw transaction data in a staging server before loading structured data into BigQuery. Option 2: load raw JSON files from the point-of-sale API directly into Google Cloud Storage, then use BigQuery SQL to transform and aggregate inside the warehouse. The VP of Analytics wants to know which approach is more appropriate for a cloud-native architecture and why.

Write a post recommending Option 2 and justifying the recommendation. Address the following:

* Identify the pipeline pattern for each option using precise technical terminology.
* What is the primary advantage of Option 2 for a cloud-native environment?
* What data quality risk does Option 2 introduce, and how would you mitigate it?
* How does the schema-on-read vs. schema-on-write distinction relate to this decision?

---

### Scenario B — The Statistical Significance Miscommunication

A product team runs an A/B test on a new checkout flow. The analyst reports: "The test page produced a 7% increase in conversion rate with a p-value of 0.03 — the result is statistically significant at alpha = 0.05." The product manager responds: "Great — there is only a 3% chance this result was a fluke. Let's roll this out to everyone." The VP of Product asks you, as the senior analyst, to evaluate whether the product manager's statement is accurate and whether the rollout decision is well-supported.

Write a post that corrects the misinterpretation and frames a sound recommendation. Address the following:

* What does p = 0.03 actually mean, and why is the product manager's statement a misinterpretation?
* Is a 7% lift statistically significant at alpha = 0.05 sufficient to justify a full rollout? What additional evidence would you want?
* What is the difference between statistical significance and practical significance?
* What Type I error risk is present and how would you communicate it to the VP?

---

### Scenario C — The Governance Review

A retail analytics team shares a customer behavior dataset with an external market research firm. The dataset includes purchase amounts, browsing categories, and ZIP codes for 500,000 customers. The legal team has verified that names, email addresses, and account numbers have been removed. The data governance officer argues the dataset requires additional review before sharing. A data engineer on the team says it is fine because all direct identifiers are gone.

Write a post supporting the governance officer's position. Address the following:

* Why is the removal of direct identifiers insufficient to guarantee anonymization?
* Which column or combination of columns poses a re-identification risk and under which research framework?
* Which regulation applies if any of these customers are California residents, and what obligation does it create for the company?
* What anonymization technique would you recommend that reduces re-identification risk while preserving analytical utility for the research firm?

---

### Peer Response Requirements

Respond to at least two classmates who chose different scenarios. Each response must:

* Be 75–100 words
* Identify one specific point you agree with and explain why
* Raise one question or alternative consideration the original poster did not address
* Reference at least one technical concept by name (pipeline pattern, data quality dimension, p-value interpretation rule, regulatory framework, anonymization technique, or algorithmic bias type)

---

## Discussion Rubric

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 6 | Addresses all four required points with precise cross-domain vocabulary (ETL vs. ELT, schema-on-read, p-value, Type I error, statistical vs. practical significance, quasi-identifier, GDPR/CCPA/HIPAA, anonymization technique names). Reasoning connects concepts from multiple Data+ domains to the specific scenario. Within 175–225 words. |
| 4–5 | Addresses most points. One explanation relies on terminology without demonstrating understanding of the underlying mechanism or regulatory requirement. |
| 2–3 | Addresses some points. Technical or governance recommendations are made without justification tied to the scenario. |
| 0–1 | Post is missing, too brief, or does not engage with the scenario. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 | Responds to at least two classmates with substantive engagement — challenges a pipeline architecture choice, corrects a p-value interpretation, identifies a missing regulatory obligation, or proposes a stronger anonymization technique with reasoning. Names at least one technical concept, regulation, or Data+ domain term. Minimum 75 words per response. |
| 2–3 | Responses are primarily agreement or restatement without new reasoning. |
| 0–1 | Only one response submitted or responses are too brief. |

---

### Submission Deadline

Initial post due by Thursday 11:59 PM. Peer responses due by Sunday 11:59 PM of the same week.
