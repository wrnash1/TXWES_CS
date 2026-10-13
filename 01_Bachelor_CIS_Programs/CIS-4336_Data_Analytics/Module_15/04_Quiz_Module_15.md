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

---

### Question 11 (5 points)

Under GDPR, which legal basis most commonly applies when a user voluntarily submits their email address through a website registration form to receive a newsletter?

A) Vital interests — used when processing is necessary to protect someone's life.

B) Legal obligation — used when processing is required by law, not voluntary user action.

C) Consent — the user has freely given, specific, and informed agreement to processing their data for the stated purpose.

D) Legitimate interests — appropriate when the organization's interest overrides user rights without requiring explicit consent.

#### Q11 Correct Answer: C

#### Q11 Distractor Analysis

Voluntary form submission for a newsletter is the textbook example of consent as a legal basis under GDPR Article 6. Vital interests (A) apply in life-threatening situations, not marketing. Legal obligation (B) applies when a law mandates processing. Legitimate interests (D) is used without explicit consent and is not appropriate when consent is easily obtainable.

---

### Question 12 (5 points)

A hospital uses a third-party cloud provider to store electronic health records. Under HIPAA, what agreement must exist between the hospital and the cloud provider?

A) A GDPR Data Processing Agreement because cloud data crosses international borders.

B) A Business Associate Agreement (BAA) — required when a covered entity shares PHI with a vendor or contractor who processes that PHI on its behalf.

C) A CCPA Data Sale Opt-Out Contract because patient data is being shared with a third party.

D) No agreement is required if the cloud provider is located in the United States.

#### Q12 Correct Answer: B

#### Q12 Distractor Analysis

HIPAA requires a Business Associate Agreement whenever a covered entity (the hospital) shares PHI with a business associate (the cloud provider) that handles the data. A GDPR agreement (A) is for EU data, not US healthcare. CCPA (C) governs consumer data rights, not healthcare vendor contracts. D is incorrect; US location does not eliminate the BAA requirement.

---

### Question 13 (5 points)

An analytics team removes names, emails, and phone numbers from a marketing dataset but retains income bracket, age group, and purchase category. A data privacy officer warns that re-identification is still possible. Which concept explains this risk?

A) Differential privacy — small statistical noise is insufficient to protect precise records.

B) Quasi-identifiers — attributes that are not direct identifiers but can uniquely identify individuals in combination, especially when cross-referenced with external datasets.

C) Data leakage — the suppressed fields are still accessible through model predictions.

D) Aggregation failure — grouped statistics can be reversed to individual records.

#### Q13 Correct Answer: B

#### Q13 Distractor Analysis

Income bracket, age group, and purchase category are quasi-identifiers — individually non-identifying, but in combination with each other or with an external dataset they may re-identify specific individuals. Differential privacy (A) is a mathematical technique for adding noise, not a description of the risk. Data leakage (C) describes a model training error, not a re-identification mechanism. Aggregation failure (D) describes statistical disclosure, a related but distinct concept.

---

### Question 14 (5 points)

Which of the following actions constitutes a data breach notification trigger under GDPR?

A) An employee accidentally sends a non-confidential internal memo to the wrong colleague.

B) A database containing personal data of EU residents is accessed by an unauthorized third party, exposing names, addresses, and payment card numbers.

C) An analyst exports a de-identified summary report to a shared drive.

D) A company updates its privacy policy without notifying users in advance.

#### Q14 Correct Answer: B

#### Q14 Distractor Analysis

Under GDPR Article 33, a personal data breach — including unauthorized access to personal data — must be reported to the supervisory authority within 72 hours. A is not a personal data breach. C involves de-identified data, which is not personal data under GDPR. D is a transparency and notification obligation under Article 13/14, not a breach notification requirement.

---

### Question 15 (5 points)

A company's employee directory dataset includes: employee name, job title, department, and work email. Under GDPR, which of the following statements is most accurate?

A) This dataset does not require privacy protection because it contains only work-related information.

B) Names and work emails are personal data under GDPR because they relate to identified individuals; the organization must have a lawful basis for processing this data.

C) Only the employee name requires protection; job title and department are not personal data.

D) This dataset is exempt from GDPR because it is used for internal purposes only.

#### Q15 Correct Answer: B

#### Q15 Distractor Analysis

GDPR defines personal data broadly as any information relating to an identified or identifiable natural person. Employee names and work emails clearly meet this definition. A is incorrect; professional data is still personal data. C is incorrect; all fields in the record relate to an identifiable person. D is incorrect; internal use does not exempt data from GDPR requirements.

---

### Question 16 (5 points)

A machine learning model trained to approve rental applications produces approval rates of 82% for applicants from primarily white ZIP codes and 41% for applicants from primarily minority ZIP codes, even though income and credit scores are equivalent. What is the most appropriate first step for an ethics review?

A) Retrain the model with a larger dataset to reduce random variation.

B) Remove income and credit score from the model to create a race-neutral decision.

C) Conduct a disparate impact analysis to measure whether the gap is statistically significant and investigate which features are driving the differential outcome.

D) Replace the model with a human review process for all applications from minority ZIP codes.

#### Q16 Correct Answer: C

#### Q16 Distractor Analysis

The first step in an ethics review is to measure and understand the disparity — disparate impact analysis quantifies whether the gap is statistically significant and attribution analysis identifies the features responsible. A addresses noise but not systematic bias. B removing legitimate features does not address proxy discrimination in remaining features and may harm the model's legitimate predictive power. D creates a separate process based on ZIP code, which is itself potentially discriminatory.

---

### Question 17 (5 points)

The principle of "purpose limitation" under GDPR means:

A) An organization may only store data for a maximum of 12 months before deletion.

B) Data collected for one specific, stated purpose may not be used for a different, incompatible purpose without obtaining new consent or another lawful basis.

C) Organizations must limit the number of purposes they state in their privacy policy to three or fewer.

D) Data may only be processed by employees whose job title includes the word "analyst."

#### Q17 Correct Answer: B

#### Q17 Distractor Analysis

Purpose limitation (GDPR Article 5(1)(b)) requires that personal data collected for one stated purpose not be repurposed for an incompatible use. A describes data retention limitation — a separate principle. C and D have no basis in GDPR.

---

### Question 18 (5 points)

An organization wants to train a customer behavior model but cannot share raw customer data due to privacy regulations. Instead, it adds calibrated statistical noise to the query results before releasing model training data. Which privacy-preserving technique is this?

A) K-anonymity — ensures each quasi-identifier combination appears k times.

B) Data masking — irreversibly replaces values with fictitious data.

C) Pseudonymization — replaces direct identifiers with tokens using a mapping table.

D) Differential privacy — adds mathematically calibrated noise so that individual records cannot be inferred from model outputs or aggregate query results.

#### Q18 Correct Answer: D

#### Q18 Distractor Analysis

Differential privacy is the specific technique of adding calibrated random noise to query results or model outputs so that no individual's data can be inferred with high confidence. K-anonymity (A) suppresses or generalizes records but does not add noise. Data masking (B) replaces values but does not protect aggregate query results. Pseudonymization (C) replaces identifiers with tokens but does not protect against statistical inference.

---

### Question 19 (5 points)

A data science team is building a credit scoring model. To ensure ethical AI practice, they document: the training data sources, all feature engineering decisions, model version history, and known performance gaps across demographic groups. What governance artifact does this describe?

A) A data catalog entry for the credit scoring dataset.

B) A model card — a standardized document describing a model's intended use, performance metrics, limitations, and fairness evaluation.

C) A data lineage diagram showing ETL pipeline transformations.

D) A business glossary definition for the "credit score" metric.

#### Q19 Correct Answer: B

#### Q19 Distractor Analysis

A model card (introduced by Google in 2019) is a short document capturing a model's purpose, training data, evaluation results, and known biases — exactly what is described. A data catalog (A) documents data assets, not models. Data lineage (C) traces data transformations, not model documentation. A business glossary (D) defines metric terms, not model behavior.

---

### Question 20 (5 points)

Which statement correctly distinguishes anonymization from pseudonymization under GDPR?

A) Anonymized data is still personal data under GDPR and requires a lawful basis; pseudonymized data does not.

B) Pseudonymized data is still personal data under GDPR because it can be re-identified using the mapping key; truly anonymized data (where re-identification is not reasonably possible) falls outside GDPR's scope.

C) Anonymization and pseudonymization are interchangeable terms in GDPR; both require consent.

D) Pseudonymization removes all direct identifiers; anonymization removes all quasi-identifiers in addition to direct identifiers.

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

GDPR Recital 26 specifies that truly anonymized data — where re-identification is not reasonably possible — is not personal data and falls outside GDPR. Pseudonymized data (where a mapping key exists) is still personal data and GDPR continues to apply. A reverses the distinction. C is incorrect; they are distinct techniques with different legal implications. D describes operational steps, not the legal distinction.

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
| 11 | C |
| 12 | B |
| 13 | B |
| 14 | B |
| 15 | B |
| 16 | C |
| 17 | B |
| 18 | D |
| 19 | B |
| 20 | B |
