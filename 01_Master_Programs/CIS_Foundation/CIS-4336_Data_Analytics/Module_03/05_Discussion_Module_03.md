# Discussion — Module 03: Data Cleaning and Transformation

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 (6 initial post + 4 peer responses)

---

## Overview

This discussion asks you to apply data cleaning judgment to realistic scenarios where there is no single correct answer. Choose one scenario from the three options below. Write an initial post of 175–225 words, then respond to at least two classmates by Sunday at 11:59 PM.

Professor Nash's note: The goal of these scenarios is to develop your professional judgment, not to recite definitions. Strong posts demonstrate reasoning about tradeoffs — why one technique is better than another given the specific context. Weak posts apply rules mechanically without considering context.

---

## Scenario A — Missing Data in a Medical Trial

A research team is analyzing results from a 500-patient clinical trial. The dataset includes patient age, gender, treatment group (A or B), weekly pain scores (1–10) recorded for 12 weeks, and a final outcome variable (recovered: yes/no). The dataset has the following missing data patterns:

- 22 patients (4.4%) have at least one missing weekly pain score, distributed randomly across weeks 3–9
- 8 patients (1.6%) have no pain scores at all — they dropped out after week 2
- 15 patients (3%) are missing the final outcome variable

In 175–225 words, address all three of the following:

1. For each of the three missing data patterns, recommend a specific handling strategy and justify it. Consider the implications for the clinical validity of the analysis.
2. The 8 complete dropouts present a particular challenge. Explain why simply deleting these 8 patients could introduce bias, and describe a more defensible approach.
3. Should the 15 patients with a missing outcome variable be included in the final analysis? What does "missing not at random" mean in this context, and why might it apply here?

---

## Scenario B — Outlier Decision in Sales Data

A retail analytics team is preparing a year-end sales dataset. The `transaction_amount` column contains 95,000 records with a mean of $87.50 and a standard deviation of $62.00. The IQR method flags 127 transactions above $285. Upon investigation, the team discovers:

- 95 of the 127 flagged transactions are corporate bulk orders (legitimate, verified)
- 24 are from a single day during a promotional event where prices were doubled by error (data entry mistake)
- 8 have no supporting documentation and cannot be verified

In 175–225 words, address all three of the following:

1. For each of the three groups of flagged transactions, recommend a specific action and justify it using both the analytical and business-context reasoning.
2. What is the risk of removing all 127 flagged transactions without investigation? How would that affect the mean and total revenue figures reported to leadership?
3. The 8 unverifiable transactions represent less than 0.01% of the dataset. A colleague argues they are too small to matter and should be left in. Do you agree? Provide a principled argument for your position.

---

## Scenario C — Standardization Tradeoffs

A data engineer is combining customer records from three systems after a company acquisition: the acquiring company's CRM, the acquired company's legacy database, and a third-party partner data feed. Key fields include customer name, address, phone number, and email address. After merging, the combined dataset has 280,000 records, but the data team suspects significant overlap — the same customers may exist in all three systems with slightly different representations.

In 175–225 words, address all three of the following:

1. Identify three specific standardization tasks that must be completed before deduplication can work reliably. For each, explain what the inconsistency would look like and what the standardization step would produce.
2. Describe the difference between exact deduplication and fuzzy matching in this context. Give an example of a customer record pair that exact deduplication would miss but fuzzy matching would catch.
3. After standardization and deduplication, the dataset shrinks from 280,000 to 195,000 records — a 30% reduction. A business stakeholder is alarmed and asks whether data was "lost." How would you explain this reduction to a non-technical audience?

---

## Discussion Rubric

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 6 | Addresses all three questions with well-reasoned, context-specific answers. Demonstrates judgment beyond rule recitation. Within 175–225 words. |
| 4–5 | Addresses most questions. One answer lacks depth or applies a technique without adequate justification. |
| 2–3 | Addresses some questions. Primarily recites definitions without applying them to the specific scenario. |
| 0–1 | Post is missing, too brief, or fails to engage with the scenario. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 | Responds to at least two classmates with substantive engagement — challenges an assumption, offers an alternative technique, or extends the argument with a real-world example. Minimum 60 words per response. |
| 2–3 | Responds to two classmates but responses are primarily agreement or restatement. Only one substantive response provided. |
| 0–1 | Only one response submitted or responses are too brief. |

---

## Deadlines

- Initial post: Wednesday at 11:59 PM
- Peer responses: Sunday at 11:59 PM
