# Quiz: Module 14 — Governance, Compliance, and Regulatory Frameworks

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

## Questions

### Question 1

A company based in Canada operates an e-commerce website that accepts orders from customers in France and Germany. The company collects names, addresses, and payment details. Which regulation most directly governs how this company must handle the European customers' personal data?

A. HIPAA
B. SOX
C. GDPR
D. PCI-DSS

Correct Answer: C

Explanation: GDPR applies to any organization that processes personal data of EU residents, regardless of where the organization is headquartered. The Canadian company processing French and German customers' data is subject to GDPR. HIPAA covers healthcare data in the US. SOX covers US public companies' financial reporting. PCI-DSS governs cardholder data but is a contractual standard, not a data protection regulation.

---

### Question 2

A security analyst discovers that a cloud storage vendor used by a hospital to archive patient records has no signed agreement defining the vendor's data protection obligations. Under HIPAA, which requirement is the hospital violating?

A. The Minimum Necessary Standard
B. The requirement to have a Business Associate Agreement in place
C. The 60-day breach notification requirement
D. The requirement to conduct an annual risk analysis

Correct Answer: B

Explanation: HIPAA requires covered entities to have a signed Business Associate Agreement (BAA) with any vendor that handles protected health information on their behalf. Without a BAA, the hospital is out of compliance regardless of how the vendor actually handles the data. The other options describe real HIPAA requirements but are not the issue described in this scenario.

---

### Question 3

An organization has documented that it uses AES-256 for all encryption of data at rest on servers containing sensitive data. This document is reviewed and approved annually by the security team. Which type of governance document does this best represent?

A. Policy
B. Guideline
C. Procedure
D. Standard

Correct Answer: D

Explanation: A standard is a specific, measurable requirement that supports a higher-level policy. Specifying AES-256 as the required algorithm is a standard — it is mandatory and measurable. A policy would state the high-level requirement ("sensitive data must be encrypted at rest") without specifying the algorithm. A procedure would provide step-by-step implementation instructions. A guideline is non-mandatory.

---

### Question 4

A retail merchant processes approximately 2 million credit card transactions per year. The merchant stores the cardholder's full name, primary account number (PAN), expiration date, and the 3-digit CVV security code in its transaction database after each sale is completed. Which stored data element is explicitly prohibited by PCI-DSS?

A. Full cardholder name
B. Primary account number (PAN)
C. Expiration date
D. CVV security code

Correct Answer: D

Explanation: PCI-DSS explicitly prohibits storing Sensitive Authentication Data (SAD) after authorization is complete. The CVV/CVC security code is classified as SAD and must never be stored post-authorization. The PAN (if stored) must be protected with strong encryption or tokenization, but it is not prohibited from storage. Cardholder name and expiration date are cardholder data that may be stored with appropriate protections.

---

### Question 5

A software developer at a publicly traded company has the ability to write code changes to the company's financial reporting system and also has deployment access to push those changes directly to the production environment without any approval. Which internal control principle required for SOX compliance does this situation violate?

A. Data minimization
B. Segregation of duties
C. Privacy by Design
D. Least privilege

Correct Answer: B

Explanation: SOX Section 404 requires effective internal controls over financial reporting. Segregation of duties (SoD) is a core IT General Control (ITGC) that prevents one person from having conflicting access — in this case, both writing and deploying financial system code without oversight. While least privilege is also relevant, the specific SOX ITGC concept being violated is segregation of duties.

---

### Question 6

An organization wants to understand its current cybersecurity capabilities, identify where it wants to be in 18 months, and prioritize investments to close the gap. Which NIST Cybersecurity Framework concept most directly supports this activity?

A. Tiers 1 through 4 maturity ratings
B. Current Profile and Target Profile comparison
C. Annex A control selection
D. Plan-Do-Check-Act cycle

Correct Answer: B

Explanation: The NIST CSF Current Profile describes an organization's existing cybersecurity practices mapped to the framework. The Target Profile describes the desired future state. Comparing the two produces a gap analysis that drives prioritized investment. Tiers describe organizational maturity but are not the primary gap analysis tool. Annex A is an ISO 27001 concept. PDCA is the ISO 27001 improvement cycle.

---

### Question 7

An organization pursuing ISO 27001 certification has completed its risk assessment and selected applicable controls from Annex A. Which required document must it produce that lists all Annex A controls, indicates which are applicable, and provides justification for any controls that were excluded?

A. Risk Treatment Plan
B. Information Security Policy
C. Statement of Applicability
D. ISMS Scope Document

Correct Answer: C

Explanation: The Statement of Applicability (SoA) is a mandatory ISO 27001 document that lists all Annex A controls, indicates whether each is applicable to the organization, and justifies any exclusions. It is a key deliverable for certification audits. The Risk Treatment Plan documents how risks will be addressed. The Information Security Policy is the top-level governance document. The Scope Document defines the ISMS boundaries.

---

### Question 8

A healthcare organization experiences a ransomware attack that encrypts files containing ePHI for 12,000 patients across three states. Assuming the encryption constitutes a breach under HIPAA's definition, what are the organization's notification obligations?

A. Notify affected individuals within 30 days; no media notification required
B. Notify affected individuals within 60 days; notify media in each affected state; notify HHS
C. Notify HHS within 24 hours; notify affected individuals within 72 hours
D. Notify affected individuals within 60 days; notify the FBI immediately

Correct Answer: B

Explanation: HIPAA's Breach Notification Rule requires covered entities to notify affected individuals within 60 days of discovering a breach. When a breach affects 500 or more residents of a state, the covered entity must also notify prominent media outlets in that state without unreasonable delay. All breaches must be reported to HHS. The 72-hour notification rule is a GDPR requirement, not HIPAA.

---

### Question 9

A company collects customer email addresses to send order confirmation emails. Six months later, marketing wants to use those same email addresses to send promotional newsletters. The customers never consented to marketing communications. Which privacy principle does using the emails for marketing violate?

A. Data minimization
B. Right to erasure
C. Purpose limitation
D. Privacy by Design

Correct Answer: C

Explanation: Purpose limitation is the principle that data collected for one specific purpose must not be used for a different purpose without obtaining new consent. The customers provided their email addresses for transactional communication only. Using them for marketing without consent violates purpose limitation. Data minimization concerns the quantity of data collected, not its reuse. Right to erasure is a data subject right. Privacy by Design concerns how systems are built.

---

### Question 10

A manager in the finance department is responsible for deciding how long financial records must be retained and who within the department may access them. She has delegated the task of configuring access controls in the financial system to the IT team. Which data governance roles do the manager and IT team respectively hold?

A. Manager: Data Steward; IT team: Data Owner
B. Manager: Data Custodian; IT team: Data Processor
C. Manager: Data Owner; IT team: Data Custodian
D. Manager: Data Controller; IT team: Data Processor

Correct Answer: C

Explanation: The data owner is the business role accountable for the data — they make decisions about classification, access, and retention. The data custodian is the technical role responsible for implementing the controls defined by the owner. The manager making decisions about retention and access is the data owner. The IT team implementing those controls is the data custodian. Data controller and data processor are GDPR-specific terms not applicable in this internal governance context.

---

---

### Question 11 (5 points)

A security architect is reviewing the governance document hierarchy for a financial services firm. The document being reviewed states: "All production firewall rule changes must be submitted via the change management portal at least 48 hours before implementation, tested in a staging environment, and approved by both the Security Operations Manager and the Network Engineering Lead before deployment." Which type of governance document is this?

- A) Policy
- B) Standard
- C) Procedure
- D) Guideline

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A policy provides a high-level mandatory direction such as "All firewall changes must follow a formal approval process." It does not specify the portal name, the 48-hour window, the test environment requirement, or the named approvers — those step-by-step implementation details are characteristic of a procedure.
- Why B is incorrect: A standard specifies a measurable requirement that supports a policy, such as "Firewall rules must use deny-all default with explicit permit rules." A standard defines what is required, not the step-by-step process for how to accomplish it.
- Why D is incorrect: A guideline is non-mandatory best practice. This document uses mandatory language ("must be submitted," "must be tested," "approved before deployment") — it is enforceable, not advisory.

---

### Question 12 (5 points)

An organization subject to GDPR receives a request from a customer asking to receive a copy of all personal data the company holds about them in a portable, machine-readable format. Which GDPR data subject right is being exercised?

- A) Right to erasure (right to be forgotten)
- B) Right to rectification
- C) Right to data portability
- D) Right to restrict processing

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: The right to erasure allows a data subject to request that their personal data be deleted. The customer is requesting a copy of their data, not deletion.
- Why B is incorrect: The right to rectification allows a data subject to correct inaccurate personal data. No inaccuracy is mentioned — the customer is requesting their data in a portable format.
- Why D is incorrect: The right to restrict processing limits how the organization uses personal data. The customer is not limiting use — they are requesting their data for transfer, which is the data portability right under GDPR Article 20.

---

### Question 13 (5 points)

A company discovers that a terminated employee's Active Directory account was not disabled until 47 days after their last day. During that period, the account was used to access the company's financial reporting system six times. Which HIPAA or SOX concept most directly requires preventing this type of access?

- A) Minimum Necessary Standard
- B) Business Associate Agreement requirement
- C) Access control and timely deprovisioning as an IT General Control
- D) Data classification policy

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: The Minimum Necessary Standard is a HIPAA Privacy Rule concept limiting how much PHI is disclosed for a given purpose. It does not address deprovisioning of terminated employee accounts in a financial system.
- Why B is incorrect: A Business Associate Agreement is a HIPAA contract requirement between a covered entity and a vendor handling PHI. It is not applicable to an internal employee access control failure.
- Why D is incorrect: Data classification policies define sensitivity levels and handling requirements for data types. While classification informs who should have access, the control gap described is specifically about timely deprovisioning — an identity and access management IT General Control required under SOX Section 404.

---

### Question 14 (5 points)

A US-based university stores academic records and financial aid data for 45,000 students. The university also has exchange students from EU member countries. Which combination of regulations most directly applies to the university's data handling obligations?

- A) PCI-DSS and SOX only
- B) FERPA for student records and GDPR for EU students' personal data
- C) HIPAA for all student health records and SOX for financial aid data
- D) GDPR applies to all students because EU students are present on campus

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: PCI-DSS applies if the university accepts payment card transactions, but it is a cardholder data standard, not a student records regulation. SOX applies to publicly traded companies — most universities are not publicly traded.
- Why C is incorrect: HIPAA applies to healthcare data held by covered entities (healthcare providers, insurers, clearinghouses). A university's general student health records may fall under HIPAA only if the university operates a clinic as a covered entity, not automatically for all universities.
- Why D is incorrect: GDPR does not apply to all students simply because some EU students are physically present in the US. GDPR applies specifically to the personal data of EU residents — so EU students' data is subject to GDPR, but domestic US students' data is not governed by GDPR.

---

### Question 15 (5 points)

An organization has implemented ISO 27001 and is preparing for its Stage 2 certification audit. The auditor asks to see the document that lists every Annex A control, indicates which controls the organization has implemented, and explains why certain controls were excluded. The organization cannot produce this document. What is the consequence?

- A) The auditor will note a minor nonconformity and allow the organization to correct it within 90 days
- B) The certification audit will fail because this is a mandatory ISO 27001 deliverable
- C) The organization may still receive conditional certification if all other clause requirements are met
- D) The missing document only matters if the organization has more than 500 employees

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The Statement of Applicability (SoA) is not an optional document. It is explicitly required by ISO 27001 Clause 6.1.3(d) as a mandatory output of the risk treatment process. Absence of a mandatory document is a major nonconformity that prevents certification.
- Why C is incorrect: ISO 27001 certification requires compliance with all mandatory clauses, including Clause 6.1.3 which mandates the SoA. Conditional certification for missing mandatory documents is not a provision of the ISO 27001 certification process.
- Why D is incorrect: ISO 27001 applies equally to organizations of all sizes. Mandatory clause requirements do not scale based on employee count. The SoA is required regardless of organizational size.

---

### Question 16 (5 points)

A healthcare organization's CISO receives a report that a ransomware attack encrypted ePHI files on 12 servers affecting approximately 6,200 patients across four states. The attack occurred on Monday. Today is Wednesday. By when must the organization notify affected individuals, and by when must it notify HHS?

- A) Notify individuals within 30 days; notify HHS immediately
- B) Notify individuals within 60 days of discovery; notify HHS within 60 days; notify media in each of the four affected states without unreasonable delay
- C) Notify individuals within 72 hours; notify HHS within 72 hours
- D) Notify individuals within 60 days; notify HHS annually in the next submission window

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: HIPAA's Breach Notification Rule requires notification to individuals within 60 days of discovery, not 30 days. The 30-day timeline does not exist in HIPAA.
- Why C is incorrect: The 72-hour notification requirement is from GDPR (notification to the supervisory authority). HIPAA's timeline is 60 days for individual notification.
- Why D is incorrect: HHS must be notified within 60 days of discovery for breaches affecting 500 or more individuals — not annually. Annual reporting to HHS applies only to breaches affecting fewer than 500 individuals in a state.

---

### Question 17 (5 points)

An e-commerce company wants to stop storing customer credit card numbers in its database after each transaction is complete. Instead, it will store a randomly generated alphanumeric string that maps back to the actual card number only in a separate, highly secured vault managed by a third-party payment processor. Which data protection technique is the company implementing?

- A) Encryption at rest using AES-256
- B) Hashing with SHA-256
- C) Tokenization
- D) Data masking

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Encryption at rest stores a mathematically transformed version of the actual card number that can be decrypted using a key. Tokenization replaces the card number with a random surrogate value with no mathematical relationship to the original — the mapping exists only in the token vault.
- Why B is incorrect: Hashing produces a fixed-length digest and is one-way (irreversible). Credit card processing requires the ability to retrieve the original number for refunds and chargebacks. Tokenization preserves retrievability through the vault while protecting the number in the merchant's database.
- Why D is incorrect: Data masking replaces sensitive data with realistic-looking but fictitious data (e.g., showing only the last four digits of a card number). The company described wants to retain the ability to retrieve the full original card number through the vault, which is the defining characteristic of tokenization, not masking.

---

### Question 18 (5 points)

A security manager is comparing NIST CSF and ISO 27001 to recommend one to the board for adoption. The board wants a framework that provides independent third-party certification that can be shown to customers and business partners. Which framework meets this requirement and why?

- A) NIST CSF, because it is a government-published framework with the highest credibility
- B) ISO 27001, because it is certifiable through accredited third-party auditors and produces a recognized certification
- C) Both frameworks are equally certifiable through the same audit process
- D) Neither framework produces third-party certification; both are self-assessment tools only

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: NIST CSF is a voluntary framework without a formal certification process. Organizations use it for self-assessment and gap analysis, but there is no NIST CSF certificate issued by an accredited third party. Government publication does not equal certifiability.
- Why C is incorrect: NIST CSF and ISO 27001 have different structures for external validation. ISO 27001 has a well-defined certification audit process through accredited bodies. NIST CSF does not have an equivalent certification mechanism.
- Why D is incorrect: ISO 27001 is explicitly certifiable. Organizations can engage accredited certification bodies (such as BSI, DNV, or Bureau Veritas) to perform Stage 1 and Stage 2 audits and issue certificates valid for three years with annual surveillance audits.

---

### Question 19 (5 points)

Under GDPR, an organization that determines the purpose and means of processing personal data is called a data controller. An organization that processes personal data on behalf of the controller is called a data processor. A hospital uses a cloud-based radiology imaging platform. The hospital decides which patient images are stored, for how long, and who may access them. The cloud vendor hosts the infrastructure and executes automated image processing algorithms. Which role does each party hold?

- A) Hospital: data processor; cloud vendor: data controller
- B) Hospital: data custodian; cloud vendor: data owner
- C) Hospital: data controller; cloud vendor: data processor
- D) Both are data controllers because both interact with the same personal data

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: This inverts the definitions. The hospital determines the purpose (patient care) and means (which images to store, retention period, access controls) — these are the defining characteristics of a data controller. The cloud vendor executes processing on behalf of the hospital, which defines the processor role.
- Why B is incorrect: Data custodian and data owner are internal data governance roles used within an organization, not GDPR legal designations. GDPR uses controller and processor to describe the legal relationship between separate entities.
- Why D is incorrect: Dual controller status requires both parties to independently determine the purpose and means of processing. The cloud vendor processes images according to the hospital's instructions and does not independently determine what data is collected, how long it is retained, or who may access it — it is a processor, not a controller.

---

### Question 20 (5 points)

An organization's compliance team is preparing for a PCI-DSS assessment. The network team has isolated all systems that store, process, or transmit cardholder data onto a dedicated VLAN with strict firewall rules preventing direct communication with other internal networks. Which PCI-DSS benefit does this architecture most directly provide?

- A) It eliminates the need for encryption of cardholder data at rest within the isolated VLAN
- B) It reduces the scope of the PCI-DSS assessment to the cardholder data environment and its direct connections
- C) It satisfies the PCI-DSS requirement for multi-factor authentication on all systems
- D) It allows the organization to use a Self-Assessment Questionnaire regardless of transaction volume

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Network segmentation reduces scope but does not eliminate encryption requirements. PCI-DSS Requirement 3 mandates encryption of stored cardholder data (specifically, the PAN must be rendered unreadable) regardless of whether the system is network-segmented.
- Why C is incorrect: Multi-factor authentication is a separate PCI-DSS requirement (Requirement 8) that applies to administrative access to systems in the cardholder data environment. Network segmentation does not satisfy MFA requirements.
- Why D is incorrect: The eligibility to use a Self-Assessment Questionnaire is determined by merchant transaction volume level (Level 1 through Level 4), not by whether network segmentation is implemented. Level 1 merchants must undergo a QSA assessment regardless of segmentation.

---

End of Quiz — Module 14
