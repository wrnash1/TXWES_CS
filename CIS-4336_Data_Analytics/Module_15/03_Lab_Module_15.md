# Lab: Module 15 — Data Ethics, Privacy, and Regulatory Compliance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Lab Overview

In this lab you will conduct a privacy audit of a synthetic dataset, apply anonymization decisions, analyze a machine learning model for potential bias, and document compliance obligations. This is a written analysis lab — no coding is required. The skills developed here are directly applicable to analyst roles in healthcare, finance, government, and any data-intensive industry.

**Estimated time:** 75–90 minutes

**Tools required:** Word processor or markdown editor

**Deliverable:** A single document named `module15_lab_[YourLastName].pdf`

---

### Learning Objectives

By completing this lab you will be able to:

* Identify PII and quasi-identifiers in a dataset and assess re-identification risk
* Select appropriate anonymization techniques for specific data fields
* Determine which privacy regulations apply to a described scenario
* Identify potential sources of algorithmic bias in a model description
* Write a data handling policy for a specific data type

---

### Part 1: PII Audit (25 minutes)

#### Step 1.1 — Review the Dataset Schema

A regional health clinic has asked you to audit the following patient dataset before it is shared with a public health research team. The dataset contains one row per clinic visit.

| Column | Sample Values |
|---|---|
| visit_id | 10042, 10043, 10044 |
| patient_name | Jane Smith, Carlos Rivera |
| date_of_birth | 1978-03-15, 1990-11-02 |
| ssn_last4 | 7731, 2289 |
| zip_code | 76105, 76112 |
| gender | Female, Male |
| diagnosis_code | E11.9, J45.901 |
| diagnosis_description | Type 2 Diabetes, Asthma |
| insurance_type | Medicaid, Private |
| visit_date | 2024-03-01, 2024-03-02 |
| provider_id | P-0042, P-0017 |
| clinic_location | Fort Worth North, Fort Worth South |

#### Step 1.2 — Classify Each Column

For each column, complete the table below:

| Column | Classification | Justification |
|---|---|---|
| visit_id | | |
| patient_name | | |
| date_of_birth | | |
| ssn_last4 | | |
| zip_code | | |
| gender | | |
| diagnosis_code | | |
| diagnosis_description | | |
| insurance_type | | |
| visit_date | | |
| provider_id | | |
| clinic_location | | |

Use these classification labels:

* Direct identifier — uniquely identifies an individual on its own
* Quasi-identifier — can identify when combined with other fields
* Non-identifying — contains no identifying information
* Sensitive non-PII — sensitive but not personally identifying

#### Step 1.3 — Re-identification Risk Assessment

Write 3–5 sentences answering: If `patient_name` were removed, could individuals still be re-identified from the remaining columns? Reference at least two specific columns in your analysis and cite the quasi-identifier concept from the reading.

---

### Part 2: Anonymization Plan (20 minutes)

The research team needs a de-identified dataset for a study on diabetes and asthma prevalence by geographic area and demographic group. They do not need to link records back to individual patients.

For each column requiring action, specify the anonymization technique and describe exactly how it would be applied:

| Column | Action | How Applied |
|---|---|---|
| patient_name | Suppress | Remove column entirely |
| date_of_birth | | |
| ssn_last4 | | |
| zip_code | | |
| gender | | |
| diagnosis_code | | |
| visit_date | | |

For three of your choices, write a one-sentence justification explaining why you chose that technique over alternatives.

---

### Part 3: Regulatory Compliance Determination (15 minutes)

For each scenario, identify which regulation(s) apply, state one specific obligation the organization has, and describe one penalty for non-compliance.

**Scenario A:** A US hospital shares a de-identified patient dataset with a university research team in Boston.

* Applicable regulation(s):
* One specific obligation:
* One penalty for non-compliance:

**Scenario B:** A Dallas-based retail company collects purchase history, location data, and browsing behavior from 60,000 California residents. It shares this data with advertising partners.

* Applicable regulation(s):
* One specific obligation:
* One penalty for non-compliance:

**Scenario C:** A telehealth startup based in Berlin offers services to patients across the EU. It stores patient session records including video transcripts.

* Applicable regulation(s):
* One specific obligation:
* One penalty for non-compliance:

---

### Part 4: Algorithmic Bias Analysis (15 minutes)

A financial services company built a loan approval model using 10 years of historical application data. The model has an overall approval rate of 78%. However, when the results are stratified by applicant ZIP code, applicants from ZIP codes with predominantly minority populations have an approval rate of 42%, compared to 84% for applicants from majority-white ZIP codes.

Answer all four questions:

**Question 1:** What type of bias is most likely present? Explain your reasoning.

**Question 2:** ZIP code is not a protected attribute under the Equal Credit Opportunity Act. Does this mean the model is compliant? Explain proxy discrimination in your answer.

**Question 3:** What additional analysis would you perform before reporting this finding to the compliance team?

**Question 4:** What is one change to the modeling process that could reduce this disparity while preserving predictive accuracy?

---

### Part 5: Data Handling Policy Draft (5 minutes)

Write a brief data handling policy (8–12 sentences) for the following scenario:

A university analytics team wants to use student grade records and course enrollment data to build a model predicting students at risk of dropping out. The team plans to share model predictions with academic advisors.

Your policy must address:

* What data will be collected and what will not
* How long the data will be retained
* Who may access it and under what conditions
* How model predictions will and will not be used
* What student rights apply

---

### Submission Instructions

Compile all five parts into a single PDF document named `module15_lab_[YourLastName].pdf`. All tables must be complete — tables with blank cells receive no credit for those rows.

---

### Grading Rubric

| Criterion | Points |
|---|---|
| Part 1: All 12 columns correctly classified with justification | 20 |
| Part 1: Re-identification risk assessment demonstrates quasi-identifier understanding | 10 |
| Part 2: Anonymization technique correct and applied specifically for each column | 20 |
| Part 3: Correct regulation identified with obligation and penalty for all three scenarios | 15 |
| Part 4: All four bias questions answered with accurate reasoning | 20 |
| Part 5: Policy addresses all five required elements and is professionally written | 15 |
| **Total** | **100** |
