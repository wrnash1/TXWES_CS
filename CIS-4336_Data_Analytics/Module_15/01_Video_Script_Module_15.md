# Video Script: Module 15 — Data Ethics, Privacy, and Regulatory Compliance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Estimated Duration:** 18–22 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **Data Ethics, Privacy, and Regulatory Compliance**.

**Audio:** "Welcome to Module 15. This is one of the most important modules in this course — not because it has the most technical content, but because the decisions we cover here have real consequences for real people. Data analysts work with personal, financial, and health information every day. How you handle that data, what protections you apply, and how you ensure that analytical outputs do not harm the people whose data produced them — these are professional and legal obligations. The CompTIA Data+ exam tests these topics in Domain 5, Data Governance. Let's get into it."

**Study Link:** [IAPP Privacy Fundamentals — free resources](https://iapp.org/resources/article/privacy-fundamentals/)

---

### [02:00 – 06:30] Data Privacy Regulations

**Visual:** Map of the United States and Europe with regulation names placed by geography, then a timeline showing enactment dates.

**Alt-text:** A split screen. Left: a map of Europe with "GDPR — EU, effective May 2018" labeled. Right: a US map with "HIPAA — 1996" near Washington DC, "CCPA — California, effective 2020" near Sacramento, and "COPPA — 1998" near Washington DC.

**Audio:** "Three regulations are tested on the Data+ exam and are foundational knowledge for any analyst: GDPR, CCPA, and HIPAA.

**GDPR — General Data Protection Regulation** took effect in May 2018 across the European Union. It applies to any organization that processes data of EU residents, regardless of where the organization is headquartered. This means a company based in Dallas that has customers in Germany must comply with GDPR for those customers' data. Key GDPR principles include lawful basis for processing, data minimization, purpose limitation, accuracy, storage limitation, and individual rights including the right to access, the right to correct, the right to delete, and the right to data portability.

**CCPA — California Consumer Privacy Act** took effect January 1, 2020 and gives California residents rights over their personal information: the right to know what data is collected, the right to opt out of data sales, and the right to non-discrimination for exercising privacy rights. The CPRA — California Privacy Rights Act — expanded CCPA in 2023.

**HIPAA — Health Insurance Portability and Accountability Act** was enacted in 1996 and governs protected health information, called PHI. It applies to covered entities — healthcare providers, health plans, healthcare clearinghouses — and their business associates. HIPAA mandates the Privacy Rule (controls use and disclosure of PHI) and the Security Rule (technical and physical safeguards for electronic PHI).

For the Data+ exam, know what each regulation covers, who it applies to, and what individual rights it grants."

---

### [06:30 – 10:00] PII — Personally Identifiable Information

**Visual:** Two-column table: left column shows direct identifiers; right column shows indirect identifiers (quasi-identifiers).

**Alt-text:** Table with columns Direct Identifiers and Quasi-Identifiers. Direct: full name, Social Security Number, email address, driver license number, account number. Quasi: zip code, birth date, gender, ethnicity, job title.

**Audio:** "PII — Personally Identifiable Information — is any data that can be used to identify a specific individual, either on its own or in combination with other data. This definition is more nuanced than most people realize.

**Direct identifiers** can identify a person on their own: full name, Social Security Number, email address, phone number, biometric data.

**Quasi-identifiers** are indirect — they cannot identify a person alone but can when combined. A classic study by researcher Latanya Sweeney showed that 87% of Americans could be uniquely identified using only three quasi-identifiers: 5-digit zip code, birth date, and gender. This is why anonymization is harder than it looks.

As an analyst, you must:

* Know which columns in your dataset contain PII
* Apply appropriate protections before sharing or publishing data
* Not store PII beyond the period required for its stated purpose
* Report breaches according to your organization's incident response policy

Under GDPR, unauthorized disclosure of personal data can result in fines up to 4% of annual global revenue or €20 million, whichever is greater."

---

### [10:00 – 14:00] Data Anonymization Techniques

**Visual:** A table showing a raw patient records dataset transforming through three anonymization stages.

**Alt-text:** Three side-by-side tables. Left: raw data with Name, DOB, Diagnosis, ZIP. Center: after masking — Name replaced with XXXX, DOB replaced with Year only. Right: after k-anonymization — zip code generalized to 3-digit prefix, age replaced with age range.

**Audio:** "Anonymization is the process of modifying data so that individuals cannot be identified. There are several techniques, each with different tradeoffs between privacy protection and data utility.

**Data masking** replaces sensitive values with fictional but realistic-looking data. A Social Security Number 123-45-6789 becomes 987-65-4321. Masking preserves the format — useful for testing — but the masked data retains no analytical value for that column.

**Pseudonymization** replaces real identifiers with pseudonyms — surrogate keys or tokens. Unlike masking, pseudonymization is reversible if you have the mapping table. GDPR treats pseudonymized data as personal data because re-identification is possible.

**Data aggregation** reports group statistics rather than individual records. Instead of individual salary records, report average salary by department.

**Data generalization** replaces precise values with ranges. Birth date becomes age bracket (25–34). ZIP code becomes state. This reduces precision but removes the identifying power of exact values.

**k-anonymity** ensures that each record is indistinguishable from at least k-1 other records on quasi-identifier combinations. If k=5, every combination of zip code, age range, and gender appears at least 5 times in the dataset.

**Data suppression** removes rows or columns that cannot be sufficiently protected. If a disease occurs in only two people in a dataset, those rows should be suppressed entirely."

---

### [14:00 – 17:30] Algorithmic Bias

**Visual:** A diagram showing how biased training data produces biased model outputs, which then feed into biased decisions.

**Alt-text:** A flow chart: Biased historical data enters the training pipeline, a model learns the bias, biased predictions are made, those predictions drive decisions that perpetuate the original disparity.

**Audio:** "Algorithmic bias occurs when a model produces outputs that systematically disadvantage one demographic group over another. Bias in models is not hypothetical — it has occurred in real hiring tools, criminal recidivism scoring systems, facial recognition, and credit scoring.

Bias enters machine learning through three main paths:

**Historical bias** — the training data reflects historical inequalities. A hiring model trained on who was hired in the past may learn to prefer certain demographics because the historical hiring was itself biased.

**Measurement bias** — one group's outcomes are measured differently or less accurately than another's. Facial recognition systems trained mostly on one demographic perform less accurately on others.

**Proxy discrimination** — a model does not directly use a protected attribute like race, but uses a correlated proxy such as zip code or school attended. The discriminatory effect is identical even though the protected attribute was not in the training data.

Your responsibility as an analyst includes asking: Who does this model affect? Are error rates consistent across demographic groups? Was the training data representative of the population the model will be applied to? These are not just ethical questions — in regulated industries, they are legal requirements."

---

### [17:30 – 20:30] Responsible Data Use

**Visual:** A checklist slide with seven responsible data use principles.

**Audio:** "Responsible data use means operating within a framework that respects individuals, follows the law, and produces outcomes that are fair and beneficial. The key principles for analysts are:

First — **data minimization**: collect and retain only the data needed for the stated purpose.

Second — **purpose limitation**: do not use data collected for one purpose for a different purpose without new consent.

Third — **transparency**: be honest with data subjects about how their data is used.

Fourth — **consent**: in many contexts, you must obtain informed consent before collecting or processing personal data.

Fifth — **fairness**: model outputs must not discriminate based on protected characteristics.

Sixth — **accountability**: someone in the organization must own data governance obligations and be answerable for violations.

Seventh — **security**: personal data must be protected with appropriate technical controls — encryption, access controls, audit logs.

On the Data+ exam, Domain 5 — Data Governance — includes all of these principles. You will see scenario questions where you must identify which principle is being violated or which regulation applies."

---

### [20:30 – 22:00] Exam Connection and Wrap-Up

**Visual:** Data+ domain map with Domain 5 — Data Governance — highlighted.

**Audio:** "Domain 5 of the Data+ exam covers data governance, data quality, and privacy regulations. You need to know GDPR, CCPA, and HIPAA — who they apply to, what rights they grant, and what the analyst's obligations are. You also need to understand PII, anonymization techniques, and algorithmic bias. This week's lab walks you through a data audit exercise where you identify PII, apply anonymization decisions, and flag a dataset for regulatory compliance. See you there."

---

### Instructor Notes

* This module pairs well with a guest speaker from a compliance or legal team
* The Latanya Sweeney quasi-identifier study is an excellent discussion starter
* Data+ Domain 5 is approximately 15% of exam questions
