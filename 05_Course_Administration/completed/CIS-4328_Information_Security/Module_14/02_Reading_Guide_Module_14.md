# Reading Guide: Module 14 — Governance, Compliance, and Regulatory Frameworks

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports Module 14's lecture content and prepares you for the module quiz, lab, and the SY0-701 certification exam. Governance and compliance topics appear throughout the Security+ exam, primarily in Domain 5: Security Program Management and Oversight, but compliance-driven controls surface across all five domains.

Work through each section actively — write answers in your own words, not copied from the text.

---

## Section 1: Governance Foundations

### Governance Key Terms

- **Governance** — the system of policies, roles, and processes that directs how an organization manages security risk and makes security decisions
- **Policy** — a mandatory, high-level statement of direction approved by leadership
- **Standard** — a specific, measurable requirement that supports a policy
- **Procedure** — a step-by-step set of instructions for implementing a standard
- **Guideline** — a recommended, non-mandatory best practice
- **Risk appetite** — the level of risk an organization is willing to accept in pursuit of its objectives

### Governance Reading Questions

1. Explain the difference between a policy and a standard. Give an original example of each related to password security.

2. A company has a written rule stating that "all laptops must use full-disk encryption with AES-256." Is this a policy, a standard, or a procedure? Justify your answer.

3. Why is it important for the board of directors to be involved in setting security governance? What happens when security decisions are made only at the IT level?

4. List and describe the three types of security roles typically defined in a governance framework: data owner, data custodian, and data steward.

### Governance Exam Focus Points

- Document hierarchy: policy → standard → procedure → guideline (mandatory to non-mandatory)
- Governance is distinct from compliance; governance defines the rules, compliance verifies they are followed
- The Security+ exam frequently presents scenarios requiring you to identify the appropriate governance document type

---

## Section 2: GDPR

### GDPR Key Terms

- **Personal data** — any information relating to an identified or identifiable natural person
- **Data subject** — the individual whose personal data is processed
- **Data controller** — entity that determines the purpose and means of processing
- **Data processor** — entity that processes data on behalf of the controller
- **Privacy by Design** — embedding privacy protections into systems from inception
- **Data Protection Officer (DPO)** — required role under GDPR for certain organizations; oversees compliance

### GDPR Reading Questions

1. A US-based company operates a website that sells products to customers in Germany. Does GDPR apply to this company? Explain why or why not.

2. A user submits a request to a company asking that all of their personal data be deleted. What GDPR right are they exercising? What limitations might apply to this right?

3. A healthcare company suffers a data breach exposing patient email addresses. Under GDPR, what is the notification timeline? Who must be notified first?

4. Explain the difference between a data controller and a data processor. Provide a real-world example of each in the context of a payroll service.

5. What does "legitimate interests" mean as a lawful basis for processing under GDPR? Give an example.

### GDPR Exam Focus Points

- 72-hour breach notification to the supervisory authority
- Controller vs. processor distinction; both are accountable but controllers bear primary responsibility
- GDPR applies to EU residents' data regardless of where the processing organization is located
- Privacy by Design is a GDPR principle, not just a best practice — it is codified in Article 25

---

## Section 3: HIPAA

### HIPAA Key Terms

- **Protected Health Information (PHI)** — individually identifiable health information held by covered entities
- **Electronic PHI (ePHI)** — PHI in electronic form; specifically governed by the Security Rule
- **Covered entity** — healthcare provider, health plan, or healthcare clearinghouse subject to HIPAA
- **Business Associate** — a person or entity that performs functions involving PHI on behalf of a covered entity
- **Business Associate Agreement (BAA)** — required contract between a covered entity and a business associate
- **Minimum necessary standard** — use or disclose only the minimum PHI needed to accomplish the purpose

### HIPAA Reading Questions

1. A hospital uses a cloud storage provider to store patient records. Is the cloud provider a covered entity or a business associate? What document must be in place between them?

2. Compare and contrast the HIPAA Privacy Rule and the Security Rule. What does each govern?

3. List the three categories of safeguards required by the HIPAA Security Rule and give two examples of controls in each category.

4. A healthcare provider discovers that a laptop containing 200 patient records was stolen. Under the Breach Notification Rule, what are the notification obligations?

5. Why is the "minimum necessary standard" an important privacy principle under HIPAA? How does it relate to the concept of least privilege in security?

### HIPAA Exam Focus Points

- HIPAA Security Rule governs ePHI specifically
- Three safeguard categories: administrative, physical, technical — all three are required
- Business Associate Agreements are required; business associates are directly liable under the HITECH Act
- Breach notification: 60 days for individual notification; immediate media notification if 500+ individuals in a state are affected

---

## Section 4: PCI-DSS

### PCI-DSS Key Terms

- **Cardholder data** — PAN, cardholder name, expiration date, service code
- **Sensitive Authentication Data (SAD)** — CVV/CVC, PIN blocks, full magnetic stripe data — must not be stored post-authorization
- **Cardholder Data Environment (CDE)** — systems that store, process, or transmit cardholder data plus connected systems
- **Qualified Security Assessor (QSA)** — a PCI-certified auditor authorized to assess Level 1 merchants
- **Self-Assessment Questionnaire (SAQ)** — compliance questionnaire for lower-volume merchants
- **Network segmentation** — isolating the CDE from other networks to reduce scope

### PCI-DSS Reading Questions

1. A retail company processes 4 million credit card transactions per year. What PCI-DSS compliance level does this represent, and what are the annual compliance requirements?

2. Why is network segmentation important for PCI-DSS compliance? How does it affect the scope of an audit?

3. An e-commerce company stores the full card number, expiration date, cardholder name, and CVV code in its database after a transaction is complete. Which of these data elements violates PCI-DSS requirements?

4. PCI-DSS Requirement 11 addresses testing security systems. Describe two specific activities this requirement mandates.

5. Is PCI-DSS a law or a contractual obligation? What happens if a merchant is found non-compliant after a breach?

### PCI-DSS Exam Focus Points

- CVV/security codes must never be stored after authorization — this is frequently tested
- PCI-DSS is not a law; it is enforced through card brand contracts
- Network segmentation reduces scope; without it, all connected systems may be in scope
- Know the 12 requirements at a high level and their associated goals

---

## Section 5: SOX and IT General Controls

### Key Terms

- **Sarbanes-Oxley Act (SOX)** — US federal law requiring accurate financial reporting and internal controls for public companies
- **Section 302** — requires CEO and CFO to certify financial statement accuracy
- **Section 404** — requires assessment of internal controls over financial reporting
- **IT General Controls (ITGCs)** — IT controls that support the accuracy and integrity of financial systems
- **PCAOB** — Public Company Accounting Oversight Board; oversees audits of public companies
- **Segregation of duties (SoD)** — preventing a single person from having conflicting privileges in financial systems

### Reading Questions

1. SOX was enacted partly in response to accounting fraud. How do IT security controls relate to financial statement accuracy?

2. List the four categories of IT General Controls and explain why each matters for SOX compliance.

3. A developer at a public company can both write code for the financial system and deploy it to production without approval. Which SOX principle does this violate?

4. What are the consequences for a CEO or CFO who knowingly certifies false financial statements under SOX Section 302?

### SOX Exam Focus Points

- SOX applies only to publicly traded US companies
- Section 404 is where IT controls get examined
- Segregation of duties is a core ITGC and appears on the Security+ exam independently
- SOX violations are criminal, not just civil

---

## Section 6: NIST CSF and ISO 27001

### NIST CSF and ISO 27001 Key Terms

- **NIST Cybersecurity Framework (CSF)** — voluntary framework for managing cybersecurity risk; version 2.0 adds the Govern function
- **Current Profile / Target Profile** — snapshots of where an organization is and where it wants to be under NIST CSF
- **ISO/IEC 27001** — international standard for an Information Security Management System (ISMS)
- **ISMS** — Information Security Management System; the set of policies and processes for managing information security
- **Statement of Applicability (SoA)** — required ISO 27001 document listing applicable Annex A controls
- **PDCA cycle** — Plan-Do-Check-Act; the improvement cycle underlying ISO 27001

### NIST CSF and ISO 27001 Reading Questions

1. An organization uses NIST CSF to assess its security posture and scores itself at Tier 2. What does this mean, and what would advancement to Tier 3 require?

2. Compare NIST CSF and ISO 27001. What are three key differences between them?

3. What is the purpose of the Statement of Applicability in ISO 27001? Why must it document controls that are excluded as well as those that are included?

4. NIST CSF v2.0 added the "Govern" function. Why was this addition significant? What security activities does it encompass?

5. An organization wants to pursue ISO 27001 certification. Describe the high-level steps involved in the certification process.

### NIST CSF and ISO 27001 Exam Focus Points

- NIST CSF: 6 functions — Govern, Identify, Protect, Detect, Respond, Recover
- ISO 27001 is certifiable; NIST CSF is not
- Current Profile vs. Target Profile is a NIST CSF concept used in gap analysis
- ISO 27001 Annex A has 93 controls in 4 themes (v2022)

---

## Section 7: Data Classification and Privacy

### Data Classification Key Terms

- **Data classification** — categorizing data by sensitivity to determine appropriate handling requirements
- **Data owner** — business role accountable for data; assigns classification
- **Data custodian** — technical role responsible for implementing controls assigned by the owner
- **Data minimization** — collecting only the minimum data necessary for the intended purpose
- **Purpose limitation** — data collected for one purpose may not be used for another without consent
- **Fair Information Practice Principles (FIPPs)** — foundational privacy principles: notice, choice, access, integrity, enforcement

### Data Classification Reading Questions

1. A company maintains the following data: employee health insurance records, the company cafeteria menu, internal budget spreadsheets, and customer credit card numbers. Assign a classification level to each and justify your choice.

2. How do data classification levels drive technical security controls? Give two examples showing how controls differ between Restricted and Public data.

3. Explain the difference between data minimization and purpose limitation. Why are both important principles even for data that is legitimately collected?

4. What is the role of the data custodian, and how does it differ from the data owner? Why is separating these roles important from a governance standpoint?

### Data Classification Exam Focus Points

- Data owner assigns classification; custodian implements controls
- Retention and destruction requirements are driven by classification and applicable regulations
- Data minimization reduces breach impact and is a GDPR legal requirement
- Privacy and security are related but distinct concepts — know the difference

---

## Audit Preparation Checklist

Use this checklist when preparing for any compliance audit scenario:

- [ ] All policies reviewed and approved within the past 12 months
- [ ] Risk assessment completed and documented
- [ ] Control inventory maintained and mapped to applicable framework requirements
- [ ] Vulnerability scans performed on schedule; results remediated or documented as accepted risk
- [ ] Access control reviews completed; least privilege verified
- [ ] Security awareness training completion rates documented
- [ ] Incident response procedures tested via tabletop exercise
- [ ] Change management records complete and current
- [ ] Evidence archive organized by control area
- [ ] Internal audit completed before external engagement

---

## Key Comparisons Table

| Framework | Type | Scope | Enforced By | Certifiable? |
|-----------|------|-------|-------------|-------------|
| GDPR | Regulation | EU personal data worldwide | Supervisory authorities | No |
| HIPAA | Federal law | US healthcare PHI | HHS/OCR | No |
| PCI-DSS | Contractual standard | Cardholder data globally | Card brands | Yes (QSA audit) |
| SOX | Federal law | US public companies | SEC/PCAOB | No |
| NIST CSF | Voluntary framework | Any organization | Self-imposed | No |
| ISO 27001 | International standard | Any organization | Accredited auditors | Yes |

---

## Module 14 Summary

Governance and compliance form the legal and organizational foundation for all security work. Whether you are a security analyst, an architect, or a manager, you will work within these frameworks daily. The Security+ exam tests both the specific details of each regulation (breach notification timelines, data types protected, who is covered) and the broader concepts of how governance programs are built and audited.

As you prepare for the quiz, be sure you can:

- Distinguish between regulatory requirements (GDPR, HIPAA, SOX) and contractual standards (PCI-DSS)
- Identify which framework applies to a given scenario
- Explain the hierarchy of governance documents
- Describe the roles of data owner, custodian, and steward
- Map the NIST CSF functions and ISO 27001 PDCA cycle from memory

---

## 9. Supplemental Resources

**1. NIST Cybersecurity Framework 2.0 — Official Publication**
[https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
The official NIST CSF 2.0 homepage provides the full framework document, implementation guides, and quick-start guides for different organization types. CSF 2.0 added the Govern function and is directly tested on the Security+ SY0-701 exam.

**2. GDPR Full Text — EUR-Lex Official Journal**
[https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
The complete text of the General Data Protection Regulation. For exam and professional purposes, focus on Articles 5 (data processing principles), 25 (privacy by design), 32 (security of processing), and 33–34 (breach notification timelines). Essential reference for any scenario question involving EU personal data.

**3. PCI Security Standards Council — PCI DSS v4.0 Resource Hub**
[https://www.pcisecuritystandards.org/document_library](https://www.pcisecuritystandards.org/document_library)
The PCI SSC document library provides the full PCI DSS v4.0 standard, a summary of changes from v3.2.1, and supporting guidance documents. Review the "At a Glance" summary for the 12 requirements — this is the level of detail tested on Security+.

---

End of Reading Guide — Module 14
