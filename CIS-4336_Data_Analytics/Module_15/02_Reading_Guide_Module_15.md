# Reading Guide: Module 15 — Data Ethics, Privacy, and Regulatory Compliance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Introduction

Welcome to **Module 15 — Data Ethics, Privacy, and Regulatory Compliance**. Data analysts work with personal, financial, and health information that belongs to real people. The legal and ethical obligations that govern this work are not optional and are not someone else's responsibility — they belong to every member of a data team. This module covers the three primary privacy regulations tested on the Data+ exam, PII identification and protection, data anonymization techniques, algorithmic bias, and the principles of responsible data use.

Domain 5 of the Data+ exam — Data Governance — accounts for approximately 15% of exam questions. Understanding these topics also protects you professionally: data privacy violations can result in personal liability in addition to organizational penalties.

---

### Learning Objectives

By the end of this module you will be able to:

* Describe the scope, applicability, and key rights of GDPR, CCPA, and HIPAA
* Identify direct and indirect (quasi-) identifiers in a dataset
* Apply at least four anonymization techniques and evaluate their tradeoffs
* Explain three sources of algorithmic bias and how analysts can detect them
* Describe the seven principles of responsible data use
* Map compliance obligations to analyst-level responsibilities

---

### Section 1: Privacy Regulations

#### GDPR — General Data Protection Regulation

The GDPR took effect on May 25, 2018 and applies to the processing of personal data of individuals located in the European Union, regardless of where the processing organization is based. A company headquartered in Houston that has 10 EU customers is subject to GDPR for those customers' data.

Key GDPR principles:

* **Lawfulness, fairness, and transparency** — processing must have a legal basis and must be disclosed to data subjects.
* **Purpose limitation** — data collected for one purpose cannot be repurposed without new consent.
* **Data minimization** — collect only what is necessary for the stated purpose.
* **Accuracy** — personal data must be kept accurate and up to date.
* **Storage limitation** — data must not be kept longer than necessary.
* **Integrity and confidentiality** — appropriate security measures must protect the data.

Individual rights under GDPR:

* Right to access — data subjects can request a copy of their data.
* Right to rectification — data subjects can correct inaccurate data.
* Right to erasure (right to be forgotten) — data subjects can request deletion under specified conditions.
* Right to data portability — data subjects can request their data in a machine-readable format.
* Right to object — data subjects can object to processing for direct marketing.

GDPR penalties: up to €20 million or 4% of annual global revenue, whichever is greater, for serious violations.

#### CCPA — California Consumer Privacy Act

The CCPA took effect January 1, 2020 and applies to for-profit businesses that collect personal information from California residents and meet at least one of these thresholds: annual gross revenue above $25 million; buys, sells, or receives the personal information of 50,000 or more consumers; or derives 50% or more of annual revenue from selling personal information.

Key CCPA rights:

* Right to know — consumers can request disclosure of what personal information is collected, used, shared, or sold.
* Right to delete — consumers can request deletion of their personal information.
* Right to opt-out — consumers can direct a business not to sell their personal information.
* Right to non-discrimination — businesses cannot discriminate against consumers who exercise their CCPA rights.

The CPRA (California Privacy Rights Act), effective 2023, expanded CCPA to add a right to correct inaccurate personal information and restrictions on sensitive personal information.

#### HIPAA — Health Insurance Portability and Accountability Act

HIPAA was enacted in 1996 and governs **Protected Health Information (PHI)** — any individually identifiable health information. HIPAA applies to **covered entities** (healthcare providers, health plans, healthcare clearinghouses) and their **business associates** (any organization that handles PHI on behalf of a covered entity).

The two key rules:

* **Privacy Rule** — controls who can access and use PHI; requires written authorization for most disclosures; grants patients the right to access their own records.
* **Security Rule** — requires administrative, physical, and technical safeguards to protect electronic PHI (ePHI). Technical safeguards include access controls, audit controls, encryption, and integrity verification.

HIPAA violations can result in civil penalties ranging from $100 to $50,000 per violation (up to $1.9 million per year for identical violations) and criminal penalties up to 10 years in prison for willful misuse.

#### Comparison Summary

| Feature | GDPR | CCPA | HIPAA |
|---|---|---|---|
| Jurisdiction | EU residents worldwide | California residents | US health data |
| Who it governs | Any org processing EU data | Qualifying businesses | Covered entities and BAs |
| Key right | Right to erasure | Right to opt-out of sale | Right to access own PHI |
| Penalty (max) | 4% global revenue | $7,500 per intentional violation | $1.9M per year per violation type |

---

### Section 2: PII — Personally Identifiable Information

#### Direct vs. Indirect Identifiers

**Direct identifiers** can uniquely identify a person on their own:

* Full name
* Social Security Number or national ID number
* Email address
* Phone number
* Driver license number
* Passport number
* Biometric data (fingerprint, facial scan, retina scan)
* Vehicle identification number
* Account number

**Quasi-identifiers** (indirect identifiers) cannot identify a person alone but can in combination:

* Date of birth
* ZIP or postal code
* Gender
* Race or ethnicity
* Job title
* Employer
* Medical condition (without name)

Latanya Sweeney's research demonstrated that 87% of US residents are uniquely identifiable using only three quasi-identifiers: 5-digit ZIP code, full birth date, and gender. This finding — published in 2000 and still valid — explains why seemingly innocuous dataset columns create serious privacy risks.

#### Analyst Obligations for PII

As a data analyst, your PII obligations include:

* Inventorying which columns contain PII before sharing any dataset
* Applying appropriate anonymization before publishing or sharing
* Not joining datasets in ways that re-identify individuals who were previously anonymous
* Reporting suspected PII breaches to your organization's privacy officer immediately
* Not retaining PII beyond its stated retention period

---

### Section 3: Data Anonymization Techniques

#### Data Masking

Data masking replaces sensitive values with fake but realistic-looking data. A Social Security Number is replaced with a different number in the same format. An email address is replaced with a fictitious address. Masking is irreversible — the original value is gone. It is used primarily in non-production environments (testing, development) where real data is needed for format but not content.

#### Pseudonymization

Pseudonymization replaces real identifiers with tokens or surrogate keys. Unlike masking, the original value is retained in a separate, secured mapping table, making pseudonymization reversible if the mapping is available. GDPR explicitly states that pseudonymized data is still personal data because re-identification is possible. Pseudonymization reduces risk but does not eliminate legal obligations.

#### Data Generalization

Generalization replaces precise values with broader categories:

* Birth date → age bracket (25–34)
* ZIP code → state
* Exact salary → salary range ($50,000–$60,000)
* City → metropolitan region

Generalization reduces identifying power while preserving some analytical utility. The tradeoff is reduced precision in analysis.

#### Data Aggregation

Aggregation reports statistics about groups rather than individual records:

* Report average salary by department, not each individual salary
* Report total purchases by region, not individual transaction records
* Report count of diagnoses by age group, not individual patient records

Aggregation is the most common technique in published analytics and public data releases.

#### k-Anonymity

k-anonymity ensures that every record in a published dataset is indistinguishable from at least k-1 other records on the quasi-identifier combination. If k=5 and the quasi-identifiers are zip code, age bracket, and gender, then every combination of those three values appears in at least 5 rows. An attacker trying to identify a specific individual from a quasi-identifier combination will find at least 5 candidates.

Limitations: k-anonymity does not protect against attribute linkage attacks (when all k records share the same sensitive attribute value). L-diversity and t-closeness are extensions that address this limitation.

#### Data Suppression

Suppression removes records or columns that cannot be adequately protected. If a rare disease appears in only two people in a dataset, those rows must be suppressed before publication because the small group size makes re-identification trivial.

#### Anonymization Technique Comparison

| Technique | Reversible? | Data Utility | Use Case |
|---|---|---|---|
| Masking | No | Lost for that field | Testing environments |
| Pseudonymization | Yes (with map) | Retained | Production analytics with controlled access |
| Generalization | No | Reduced | Published datasets |
| Aggregation | No | Retained at group level | Public reporting |
| k-Anonymity | No | Reduced | Public microdata release |
| Suppression | No | Lost for removed rows | Small-cell protection |

---

### Section 4: Algorithmic Bias

#### Definition

Algorithmic bias is a systematic, repeatable error in a model's outputs that creates unfair outcomes for identifiable groups. It differs from random error in that the error consistently disadvantages the same demographic. Algorithmic bias is not always intentional — it can emerge from data collection practices, historical inequalities, or flawed assumptions embedded in model design.

#### Sources of Bias

**Historical bias** — training data reflects historical discrimination or inequality. A resume screening model trained on who was historically hired learns to replicate past hiring patterns, including any discriminatory ones. The data is an accurate representation of the past; the problem is that the past was not equitable.

**Measurement bias** — the variable being measured is less accurate for some groups than others. Early pulse oximeters overestimated blood oxygen levels in patients with darker skin tones. Models trained on that device's readings learned a systematically wrong signal for that demographic.

**Sampling bias** — the training dataset does not represent the deployment population. A facial recognition system trained on data with 80% lighter-skinned faces will perform worse on darker-skinned faces when deployed on a diverse population.

**Proxy discrimination** — the model does not use a protected attribute (race, gender, religion) directly but uses a variable that is strongly correlated with it. Using ZIP code as a predictor can encode racial demographics. Using surname can encode ethnicity.

**Label bias** — the labels used to train the model are themselves biased. If criminal recidivism labels are based on re-arrest rather than re-offense, and if policing rates differ by neighborhood, the labels reflect policing intensity rather than actual recidivism.

#### Analyst Responsibilities for Bias Detection

As an analyst, bias detection responsibilities include:

* Examining model error rates stratified by demographic group — not just overall accuracy
* Checking whether the training dataset is representative of the deployment population
* Auditing feature importance for proxy variables correlated with protected attributes
* Documenting assumptions about the training data and model purpose
* Escalating concerns about potential discriminatory outputs to legal or compliance teams

Disparate impact analysis compares the rate of a favorable outcome for a protected group to the rate for the majority group. In the US, a rate below 80% of the majority rate is a threshold for potential discriminatory impact (the four-fifths rule).

---

### Section 5: Principles of Responsible Data Use

The following principles synthesize requirements from GDPR, professional ethics frameworks, and industry best practices:

* **Data minimization** — collect and retain only the data needed for the stated purpose. Do not collect "just in case."
* **Purpose limitation** — do not repurpose data for uses beyond what data subjects consented to.
* **Transparency** — be honest with data subjects, stakeholders, and the public about what data is collected and how it is used.
* **Consent** — obtain informed consent before collecting personal data where required by applicable law.
* **Fairness** — ensure model outputs do not systematically disadvantage protected groups.
* **Accountability** — designate a responsible owner for data governance obligations. Under GDPR, organizations above a threshold must appoint a Data Protection Officer.
* **Security** — protect personal data with appropriate technical controls including encryption at rest and in transit, role-based access control, and audit logging.

---

### Key Terms

* **GDPR** — General Data Protection Regulation; EU regulation governing personal data processing with effect worldwide for EU resident data.
* **CCPA** — California Consumer Privacy Act; grants California residents rights over their personal information.
* **HIPAA** — Health Insurance Portability and Accountability Act; governs protected health information for US covered entities.
* **PII (Personally Identifiable Information)** — any data that can identify a specific individual, directly or in combination.
* **PHI (Protected Health Information)** — individually identifiable health information governed by HIPAA.
* **quasi-identifier** — an indirect identifier that cannot identify a person alone but can in combination with other fields.
* **data masking** — replacing sensitive values with fictional data; irreversible.
* **pseudonymization** — replacing identifiers with tokens while retaining a mapping table; reversible.
* **data generalization** — replacing precise values with ranges or broader categories.
* **k-anonymity** — a property ensuring each record is indistinguishable from at least k-1 others on quasi-identifiers.
* **data suppression** — removing records or fields that cannot be adequately protected.
* **algorithmic bias** — systematic, unfair error in model outputs that consistently disadvantages an identifiable group.
* **historical bias** — bias introduced when training data reflects historical inequalities.
* **proxy discrimination** — using a variable correlated with a protected attribute to produce discriminatory outcomes without using the protected attribute directly.
* **disparate impact** — when a neutral policy or model produces disproportionately negative outcomes for a protected group.
* **data minimization** — the principle of collecting only data that is necessary for the stated purpose.

---

### Review Questions

1. A healthcare software company based in Austin, Texas builds a mobile app used by patients in Germany. Which privacy regulation(s) apply to the patient data collected by the app?

2. A researcher publishes a dataset with name and email address removed, but ZIP code, birth date, and gender are included. Is this dataset sufficiently anonymized? Explain using the quasi-identifier concept.

3. What is the difference between pseudonymization and data masking? Under GDPR, which one still counts as personal data?

4. A hiring algorithm was trained on historical data from a company where 80% of senior hires were men. The model now recommends far fewer women for promotion. Which type of bias is this and what would you do to address it?

5. Describe the HIPAA Security Rule's three categories of safeguards and give one example of each.

---

### OER Resources

* **IAPP Privacy Fundamentals — free resources** — [iapp.org/resources](https://iapp.org/resources/)
* **GDPR full text (EU)** — [gdpr-info.eu](https://gdpr-info.eu/)
* **California CCPA official resource** — [oag.ca.gov/privacy/ccpa](https://oag.ca.gov/privacy/ccpa)
* **HHS HIPAA guidance** — [hhs.gov/hipaa](https://www.hhs.gov/hipaa/index.html)
* **AI Fairness 360 — IBM bias detection toolkit** — [aif360.res.ibm.com](https://aif360.res.ibm.com/)

---

## 9. Supplemental Resources

**1. NIST Privacy Framework — Overview**
<https://www.nist.gov/privacy-framework>
The U.S. National Institute of Standards and Technology Privacy Framework provides a structured approach to managing privacy risk across identify, govern, control, communicate, and protect functions. Complements the GDPR and HIPAA content in Module 15 by showing how a US government framework approaches data privacy obligations.

**2. Google Model Cards — Research Overview**
<https://modelcards.withml.googl.github.io/about.html>
The original Google research page introducing model cards as a tool for ethical AI documentation. Covers the standardized format for reporting model purpose, training data, performance metrics across demographic groups, and known limitations — directly relevant to the AI fairness and responsible analytics content in Module 15.

**3. FTC — Understanding the Fair Credit Reporting Act (for Data Analysts)**
<https://www.ftc.gov/business-guidance/privacy-security/credit-reporting>
The FTC's guidance on FCRA obligations for organizations that use consumer data in decisions about credit, employment, housing, and insurance. Directly relevant to the bias-in-algorithmic-decision-making and regulatory compliance topics covered in Module 15.
