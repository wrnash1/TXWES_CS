# Quiz: Module 15 — Data Ethics, Privacy, and Regulatory Compliance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A US-based e-commerce company with annual revenue of $30 million processes purchase data from 80,000 California residents. Which privacy regulation requires this company to offer California customers the right to opt out of the sale of their personal information?

A) GDPR — applies to EU residents' data; the California customer base is not covered by GDPR unless those specific customers are EU residents.

B) HIPAA — governs protected health information; purchase data from an e-commerce company is not health data.

C) CCPA — applies to for-profit businesses meeting revenue or data volume thresholds that collect personal information from California residents; this company meets both thresholds.

D) FERPA — governs educational records; not applicable to retail purchase data.

#### Q1 Correct Answer: C

#### Q1 Distractor Analysis

A is only relevant if the customers are EU residents. B applies to health information, not retail purchase data. D governs student education records, not consumer data.

---

### Question 2

A healthcare data analyst removes the patient name and Social Security Number from a dataset before sharing it with a research partner. The dataset still contains date of birth, ZIP code, and gender. Which statement best describes the privacy status of this dataset?

A) The dataset is fully anonymized because the direct identifiers have been removed.

B) The dataset still carries re-identification risk because the remaining fields are quasi-identifiers that can uniquely identify individuals in combination.

C) The dataset is pseudonymized because a mapping from the removed fields could theoretically be reconstructed.

D) The dataset is compliant with HIPAA because only non-health columns remain.

#### Q2 Correct Answer: B

#### Q2 Distractor Analysis

A is incorrect; removing direct identifiers does not eliminate re-identification risk from quasi-identifiers. Research shows ZIP code, birth date, and gender together can identify 87% of US individuals. C is incorrect; pseudonymization retains a mapping table; removing fields without a mapping is masking, not pseudonymization. D is incorrect; date of birth, ZIP, and gender can still constitute PHI in a health context.

---

### Question 3

An analyst applies k-anonymity with k=4 to a patient dataset using ZIP code, age bracket, and gender as quasi-identifiers. What property is guaranteed in the published dataset?

A) Every patient's name appears at least four times in the dataset.

B) Every combination of ZIP code, age bracket, and gender appears in at least four rows, making any individual indistinguishable from at least three others on those attributes.

C) The dataset contains exactly four rows per patient, one for each quarter of the year.

D) The probability of re-identifying any individual is exactly 25%.

#### Q3 Correct Answer: B

#### Q3 Distractor Analysis

A is incorrect; k-anonymity applies to quasi-identifier combinations, not to names. C describes a time-series structure unrelated to k-anonymity. D is incorrect; k-anonymity guarantees at least k records per combination but does not specify a fixed probability of re-identification.

---

### Question 4

A company trains a loan approval model. It does not include race as a feature, but it includes applicants' ZIP codes. Applicants from certain ZIP codes are approved at substantially lower rates, and those ZIP codes are predominantly minority communities. Which type of bias does this represent?

A) Measurement bias — the approval variable is measured inaccurately for some groups.

B) Sampling bias — the training dataset does not represent the deployment population.

C) Proxy discrimination — ZIP code serves as a proxy for race, producing disparate outcomes based on a protected characteristic without using the characteristic directly.

D) Label bias — the training labels (approved/denied) were assigned incorrectly.

#### Q4 Correct Answer: C

#### Q4 Distractor Analysis

A is incorrect; there is no indication the approval outcome is measured inaccurately. B may be a contributing factor but does not describe the specific mechanism of using ZIP as a racial proxy. D is incorrect; the labels are the historical decisions, not necessarily mislabeled.

---

### Question 5

Under GDPR, which of the following best describes the maximum financial penalty for a serious violation such as processing data without a lawful basis?

A) $50,000 per violation, capped at $500,000 annually.

B) Up to €20 million or 4% of annual global revenue, whichever is greater.

C) Up to $1.9 million per year for repeated violations.

D) Up to 10 years imprisonment for the data controller.

#### Q5 Correct Answer: B

#### Q5 Distractor Analysis

A describes a hypothetical figure, not GDPR. C describes HIPAA maximum civil penalties for repeated violations. D describes HIPAA criminal penalties for willful misuse, not GDPR.

---

### Question 6

A data analyst replaces all patient Social Security Numbers in a testing database with randomly generated numbers in the same format, keeping no record of the original values. Which anonymization technique has been applied?

A) Pseudonymization — the values have been replaced with tokens and can be reversed.

B) Data masking — the original values are replaced with fictitious data with no way to recover the original; the transformation is irreversible.

C) Data generalization — the values have been replaced with less precise ranges.

D) Aggregation — the values have been combined into group summaries.

#### Q6 Correct Answer: B

#### Q6 Distractor Analysis

A is incorrect; pseudonymization retains a mapping table that allows re-identification. The scenario explicitly states no record of original values is kept. C describes replacing with ranges, not format-preserving random substitution. D describes summarizing groups, not replacing individual values.

---

### Question 7

Which of the following HIPAA rules establishes requirements for administrative, physical, and technical safeguards to protect electronic PHI?

A) HIPAA Privacy Rule — governs the use and disclosure of PHI but does not specify technical controls.

B) HIPAA Security Rule — requires covered entities to implement specific safeguards for electronic PHI including access controls, encryption, and audit logs.

C) HIPAA Breach Notification Rule — requires covered entities to notify affected individuals when unsecured PHI is breached.

D) HIPAA Enforcement Rule — establishes procedures for investigating complaints and penalties; does not specify technical controls.

#### Q7 Correct Answer: B

#### Q7 Distractor Analysis

A governs use and disclosure, not technical security controls. C is about post-breach notification, not preventive safeguards. D is the enforcement mechanism, not the safeguard specification.

---

### Question 8

A researcher studies historical criminal sentencing data and finds that a recidivism prediction model used by courts assigns higher risk scores to defendants from lower-income ZIP codes. The model was trained on re-arrest data rather than re-offense data. Which combination of bias types is most likely present?

A) Sampling bias and measurement bias only.

B) Historical bias — the training data reflects historical over-policing patterns — and label bias — re-arrest reflects policing intensity rather than actual reoffending.

C) Proxy discrimination and data leakage.

D) Overfitting — the model memorized the training data and is not generalizing.

#### Q8 Correct Answer: B

#### Q8 Distractor Analysis

A identifies bias types but does not describe the specific mechanisms — historical and label bias are more precise diagnoses here. C introduces data leakage, which is a model evaluation concept unrelated to the described bias. D is a model complexity issue, not a fairness issue.

---

### Question 9

An analyst on a data team proposes collecting customers' age, location, and browsing history "just in case" it is useful for future models. Which data ethics principle does this violate?

A) Transparency — the customers have not been told about the data collection.

B) Data minimization — organizations should collect only data needed for a stated purpose; collecting data speculatively violates this principle.

C) Fairness — speculative collection may produce biased model inputs.

D) Security — storing extra data increases the attack surface but does not describe the primary principle violation.

#### Q9 Correct Answer: B

#### Q9 Distractor Analysis

A may also be violated but is a secondary concern compared to the direct violation of data minimization described in the scenario. C and D are downstream considerations; the primary principle being violated is the prohibition on collecting data without a stated purpose.

---

### Question 10

Which Data+ exam domain directly covers privacy regulations, PII handling, data governance, and responsible data use as tested in Module 15?

A) Domain 1 — Data Concepts and Environments.

B) Domain 2 — Data Mining.

C) Domain 3 — Data Analysis and Statistics.

D) Domain 5 — Data Governance, which covers data quality, compliance regulations, master data management, and responsible use of data.

#### Q10 Correct Answer: D

#### Q10 Distractor Analysis

A covers foundational data concepts and technology environments. B covers data collection and transformation. C covers statistical analysis and analytical methods. D explicitly includes privacy regulations, PII, compliance, and governance — the content of Module 15.

---

### Answer Key

| Question | Correct Answer |
|---|---|
| 1 | C |
| 2 | B |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | B |
| 10 | D |
