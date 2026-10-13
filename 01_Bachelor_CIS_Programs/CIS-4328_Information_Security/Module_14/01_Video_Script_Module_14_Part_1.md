# Video Script: Module 14 — Governance, Compliance, and Regulatory Frameworks (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00–0:45]

Welcome back to CIS-4328 Information Security. I'm Professor Nash, and this is Module 14, Part 1.

If you've ever wondered why organizations spend enormous resources on compliance programs — audits, policy documents, training, certifications — this module answers that question directly. Governance and compliance are the structural backbone of any security program. They translate business risk and legal obligation into concrete, day-to-day security behavior.

In Part 1 today we will cover the major regulatory frameworks your organization is likely to encounter, including GDPR, HIPAA, PCI-DSS, and SOX. In Part 2 we will shift to the frameworks you use to *build* your program — NIST CSF and ISO 27001 — along with data classification and privacy principles.

Let's get into it.

---

### [SECTION 1: What Is Governance? — 1:00–3:30]

Security governance is the set of policies, roles, responsibilities, and processes that direct how an organization manages information security. It answers three questions:

- Who is responsible for security decisions?
- What rules must be followed?
- How do we verify we are following them?

Governance operates at multiple layers. At the top is the **board and executive leadership** — they set risk appetite and sign off on security strategy. Below that are **management-level policies** — things like the Acceptable Use Policy, the Password Policy, the Incident Response Policy. At the operational layer are **standards, procedures, and guidelines** that tell employees exactly how to implement policy.

The Security+ exam will test you on the hierarchy of governance documents:

- **Policy** — high-level, mandatory statement of intent. Example: "All sensitive data must be encrypted at rest."
- **Standard** — specific, measurable requirement that supports a policy. Example: "AES-256 must be used for data at rest."
- **Procedure** — step-by-step instructions. Example: "To encrypt a database volume, follow these twelve steps…"
- **Guideline** — recommended, non-mandatory best practice.

Know that hierarchy cold. It appears frequently on the exam in scenario questions.

---

### [SECTION 2: GDPR — General Data Protection Regulation — 3:30–6:00]

GDPR is a European Union regulation that came into force in May 2018. Despite being an EU law, it has global reach — it applies to *any* organization that processes personal data of EU residents, regardless of where the organization is headquartered.

Key GDPR concepts to know:

**Data Subject** — the individual whose personal data is being processed. The data subject has explicit rights under GDPR.

**Data Controller** — the organization that determines why and how personal data is processed. Controllers bear primary legal responsibility.

**Data Processor** — a third party that processes data on behalf of the controller. Cloud providers, payroll companies, and analytics vendors are common processors.

**Lawful basis for processing** — you cannot collect or use personal data without a legal justification. The six bases include consent, contract, legal obligation, vital interests, public task, and legitimate interests.

**Key rights of data subjects:**

- Right to access — individuals can request a copy of their data
- Right to erasure ("right to be forgotten") — individuals can request deletion
- Right to data portability — individuals can request data in a machine-readable format
- Right to rectification — individuals can correct inaccurate data

**72-hour breach notification** — if a data breach occurs that is likely to result in risk to individuals, GDPR requires notification to the supervisory authority within 72 hours of becoming aware.

**Penalties** — up to 4% of global annual turnover or €20 million, whichever is higher. These are not hypothetical; Meta, Google, and Amazon have all received nine-figure GDPR fines.

For the Security+ exam, focus on: the 72-hour notification requirement, the roles of controller vs. processor, and the concept of Privacy by Design — which means embedding privacy protections into systems from the start, not as an afterthought.

---

### [SECTION 3: HIPAA — Health Insurance Portability and Accountability Act — 6:00–8:30]

HIPAA is a US federal law that protects the privacy and security of Protected Health Information, which we abbreviate as PHI. PHI includes any individually identifiable health information — name, diagnosis, treatment records, insurance details — that is created, received, maintained, or transmitted by a covered entity.

**Covered entities** include healthcare providers, health plans, and healthcare clearinghouses. **Business associates** are vendors that handle PHI on behalf of covered entities — they must sign a Business Associate Agreement (BAA) and are subject to HIPAA directly.

HIPAA has two main rules relevant to security:

**The Privacy Rule** governs *who* can access PHI and for what purposes. It gives patients the right to access their own records and limits disclosures without authorization.

**The Security Rule** governs the *technical, physical, and administrative safeguards* required to protect electronic PHI (ePHI). This is where security practitioners spend most of their time.

The Security Rule's three safeguard categories:

- **Administrative safeguards** — risk analysis, workforce training, contingency planning
- **Physical safeguards** — facility access controls, workstation security, device controls
- **Technical safeguards** — access controls, audit controls, integrity controls, transmission security

**Breach Notification Rule** — covered entities must notify affected individuals within 60 days of discovering a breach. If the breach affects 500 or more individuals in a state, the media must also be notified.

For the Security+ exam: know the covered entity / business associate distinction, the three safeguard types, and that HIPAA applies to ePHI specifically under the Security Rule.

---

### [SECTION 4: PCI-DSS — Payment Card Industry Data Security Standard — 8:30–11:00]

PCI-DSS is not a law — it is a contractual standard created by the major card brands (Visa, Mastercard, American Express, Discover, JCB) through the PCI Security Standards Council. Any organization that stores, processes, or transmits cardholder data must comply or risk losing the ability to accept card payments.

**Cardholder data** includes the Primary Account Number (PAN), cardholder name, expiration date, and service code. Sensitive Authentication Data — like CVV codes and PIN blocks — must never be stored after authorization.

PCI-DSS version 4.0 (the current version as of 2024) is organized around **12 requirements** grouped into 6 goals:

**Goal 1: Build and maintain a secure network**

- Requirement 1: Install and maintain network security controls
- Requirement 2: Apply secure configurations to all system components

**Goal 2: Protect account data**

- Requirement 3: Protect stored account data
- Requirement 4: Protect cardholder data with strong cryptography during transmission

**Goal 3: Maintain a vulnerability management program**

- Requirement 5: Protect all systems against malware
- Requirement 6: Develop and maintain secure systems and software

**Goal 4: Implement strong access control**

- Requirements 7, 8, 9: Restrict access by need-to-know, identify and authenticate users, restrict physical access

**Goal 5: Monitor and test networks**

- Requirement 10: Log and monitor all access to system components and cardholder data
- Requirement 11: Test security of systems and networks regularly

**Goal 6: Maintain an information security policy**

- Requirement 12: Support information security with organizational policies and programs

**Compliance levels** are based on transaction volume. Level 1 merchants (over 6 million transactions/year) must undergo an annual on-site audit by a Qualified Security Assessor (QSA). Lower-volume merchants complete a Self-Assessment Questionnaire (SAQ).

For the Security+ exam: know that PCI-DSS is industry-driven (not law), understand the 12 requirements at a high level, and know that CVV / security codes must not be stored post-authorization.

---

### [SECTION 5: SOX — Sarbanes-Oxley Act — 11:00–13:00]

SOX was enacted in 2002 in response to accounting scandals at Enron and WorldCom. It applies to all publicly traded companies in the United States and focuses primarily on financial reporting integrity.

From an IT security perspective, SOX Section 404 is most important. It requires management to assess and report on the effectiveness of internal controls over financial reporting. Because financial data lives in IT systems, IT controls are directly in scope.

**IT General Controls (ITGCs)** that SOX auditors examine:

- Logical access controls — who can access financial systems
- Change management — how changes to financial systems are authorized and tested
- Computer operations — backup and recovery procedures
- Program development — how new applications are built and validated

**Section 302** requires the CEO and CFO to personally certify the accuracy of financial reports. This creates executive accountability that flows directly to IT security teams.

SOX is enforced by the SEC and PCAOB (Public Company Accounting Oversight Board). Violations can result in criminal penalties including fines and imprisonment for executives.

For the Security+ exam: understand that SOX primarily concerns financial data integrity and that IT controls are central to SOX compliance for public companies.

---

### [CLOSING — 13:00–15:00]

Let's recap what we covered in Part 1:

- Governance defines the hierarchy of security documents: policy, standard, procedure, guideline
- GDPR applies globally to EU personal data; key items are 72-hour breach notification, controller vs. processor, and Privacy by Design
- HIPAA protects PHI with administrative, physical, and technical safeguards; know covered entities vs. business associates
- PCI-DSS is a contractual standard with 12 requirements protecting cardholder data
- SOX focuses on financial reporting integrity and IT general controls for public companies

In Part 2 we will cover NIST CSF and ISO 27001, data classification schemes, privacy principles, and how to prepare for a compliance audit. See you there.

---

*End of Part 1 Script*
