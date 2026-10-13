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

---

## Part 9 — Challenge Exercise

### Challenge 1: Automated PII Detection and Classification Script

Build a Python function that scans a pandas DataFrame and automatically flags columns that likely contain personally identifiable information based on column names and value patterns.

1. Create a function `detect_pii(df)` that checks each column against two criteria: (a) a list of high-risk column name keywords (e.g., `['name', 'email', 'phone', 'ssn', 'dob', 'address', 'zip', 'ip']`), and (b) a regex pattern check on column values for common PII formats (email: `\S+@\S+\.\S+`, US phone: `\d{3}[-.\s]?\d{3}[-.\s]?\d{4}`, SSN: `\d{3}-\d{2}-\d{4}`). The function returns a DataFrame with columns: `column_name`, `detection_method`, `pii_type`, and `risk_level` (High/Medium).
2. Create a synthetic test DataFrame with 10 columns: some with obvious PII (email, phone), some with quasi-identifiers (zip_code, birth_year, gender), and some with no PII (product_id, amount, region). Run `detect_pii()` on it and print the results. Write two sentences evaluating the limitations of automated PII detection — specifically, what types of PII would this function miss?

```python
import pandas as pd
import re

PII_NAME_KEYWORDS = ["name", "email", "phone", "ssn", "dob", "address", "zip", "ip",
                     "birth", "passport", "license", "national_id", "credit"]

PII_PATTERNS = {
    "email":   (r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", "High"),
    "US_phone":(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "High"),
    "SSN":     (r"\b\d{3}-\d{2}-\d{4}\b", "High"),
    "IPv4":    (r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "Medium"),
}

def detect_pii(df):
    results = []
    for col in df.columns:
        col_lower = col.lower()
        for kw in PII_NAME_KEYWORDS:
            if kw in col_lower:
                results.append({
                    "column_name": col,
                    "detection_method": "column_name",
                    "pii_type": kw,
                    "risk_level": "High" if kw in ["ssn","email","phone","passport"] else "Medium"
                })
                break

        sample = df[col].dropna().astype(str).head(50)
        for pii_type, (pattern, risk) in PII_PATTERNS.items():
            hits = sample.str.contains(pattern, regex=True, na=False).sum()
            if hits > 0:
                results.append({
                    "column_name": col,
                    "detection_method": "value_pattern",
                    "pii_type": pii_type,
                    "risk_level": risk
                })

    return pd.DataFrame(results).drop_duplicates(subset=["column_name", "pii_type"])
```

### Challenge 2: Fairness Audit on a Simulated Loan Dataset

Perform a quantitative fairness audit on a simulated binary classification outcome dataset to measure disparate impact.

1. Generate a synthetic loan decision dataset with 1,000 records containing: `applicant_id`, `age_group` (25-34, 35-44, 45-54, 55-64), `income_bracket` (Low, Medium, High), `credit_tier` (1-5), `zip_group` (A through E where C and D are predominantly minority areas), and `approved` (0/1). Construct the dataset so that zip groups C and D have systematically lower approval rates (approx. 40%) compared to A, B, E (approx. 75%), even within the same income and credit tier.
2. Compute the approval rate for each `zip_group` and the overall rate. Apply the **80% rule (four-fifths rule)** from US employment and housing law: a group has disparate impact if its approval rate is less than 80% of the highest group's approval rate. Print a fairness audit table showing each group's approval rate, the ratio to the highest-approval group, and a PASS/FAIL flag. Write three sentences describing what actions a compliance officer would take if the audit reveals a FAIL for one or more groups.

```python
import pandas as pd
import numpy as np

np.random.seed(99)
n = 1000
zip_groups = np.random.choice(list("ABCDE"), n, p=[0.2, 0.2, 0.2, 0.2, 0.2])
credit_tier = np.random.randint(1, 6, n)
income_bracket = np.random.choice(["Low", "Medium", "High"], n, p=[0.3, 0.4, 0.3])
age_group = np.random.choice(["25-34","35-44","45-54","55-64"], n)

base_prob = 0.75
approved = []
for z, c in zip(zip_groups, credit_tier):
    p = base_prob + (c - 3) * 0.05
    if z in ["C", "D"]: p -= 0.35
    p = max(0.05, min(0.95, p))
    approved.append(np.random.binomial(1, p))

df_loans = pd.DataFrame({
    "applicant_id": range(1, n+1),
    "zip_group": zip_groups,
    "credit_tier": credit_tier,
    "income_bracket": income_bracket,
    "age_group": age_group,
    "approved": approved
})

overall_rate = df_loans["approved"].mean()
group_rates = df_loans.groupby("zip_group")["approved"].mean()
max_rate = group_rates.max()

audit = group_rates.reset_index()
audit.columns = ["zip_group", "approval_rate"]
audit["ratio_to_max"] = (audit["approval_rate"] / max_rate).round(3)
audit["four_fifths_flag"] = audit["ratio_to_max"].apply(
    lambda r: "PASS" if r >= 0.80 else "FAIL"
)
audit["approval_rate"] = audit["approval_rate"].round(3)
print(f"Overall approval rate: {overall_rate:.3f}")
print(f"Highest group rate:    {max_rate:.3f}")
print("\nFairness Audit (80% Rule):")
print(audit.to_string(index=False))
```

### Reflection Questions

1. In Challenge 1, the `detect_pii()` function relies on column names and value regex patterns. Describe two categories of PII that this automated approach would consistently miss, and explain what additional data profiling or domain knowledge would be needed to detect them.
2. In Challenge 2, the four-fifths rule is a legal heuristic, not a guarantee of fairness. A zip group could have a 79% approval rate compared to an 85% maximum (ratio = 0.93 — PASS under the four-fifths rule) yet still have a statistically significant disparity. What statistical test would you apply to determine whether observed approval rate differences are statistically significant, and at what alpha level would you recommend setting the threshold for a lending compliance audit?
