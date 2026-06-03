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

End of Quiz — Module 14
