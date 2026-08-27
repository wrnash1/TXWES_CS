# Reading Guide: Module 15 — Legal, Regulatory, and Compliance Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 1 (Information Security Governance) and Domain 3 (Information Security Program Development and Management)

---

## Introduction

Welcome to Module 15. This module examines the legal and regulatory environment that every information security manager must navigate. Governance without regulatory context is incomplete — you cannot build an effective security program without understanding the compliance obligations that shape its requirements, its scope, and its accountability structures.

The CISM exam tests regulatory knowledge primarily through scenario-based questions that ask you to identify the correct governance action, notification obligation, or program response in a given regulatory context. This reading guide provides comprehensive coverage of major frameworks, comparison tables, audit management, and a compliance calendar to support both exam preparation and practical application.

---

## 1. High-Yield Glossary

The following terms are essential for the CISM exam and for professional practice in compliance-adjacent security roles.

**General Data Protection Regulation (GDPR)**: The European Union's comprehensive data protection law, effective May 2018. Applies extraterritorially to any organization processing personal data of EU residents. Establishes data subject rights, controller and processor obligations, supervisory authority oversight, and penalties up to 4% of global annual turnover for the most serious violations.

**Health Insurance Portability and Accountability Act (HIPAA)**: U.S. federal law governing the privacy and security of Protected Health Information (PHI) and electronic PHI (ePHI) held by covered entities and their business associates. The Privacy Rule, Security Rule, and Breach Notification Rule are its three security-relevant components.

**Payment Card Industry Data Security Standard (PCI-DSS)**: A contractual security standard maintained by the PCI Security Standards Council. Applies to organizations that store, process, or transmit cardholder data. Compliance is enforced by card brands through merchant agreements, not by government regulation.

**Sarbanes-Oxley Act (SOX)**: U.S. federal law enacted in 2002 governing internal controls over financial reporting for publicly traded companies. Section 404 requires management assessment and external auditor attestation of ICFR effectiveness. IT General Controls (ITGCs) are the IT security controls that directly support SOX compliance.

**California Consumer Privacy Act (CCPA) / California Privacy Rights Act (CPRA)**: California's comprehensive privacy law framework. CCPA (2020) established foundational consumer rights; CPRA (2023) expanded those rights and created the California Privacy Protection Agency as an enforcement body.

**Data subject**: Under GDPR, a natural person whose personal data is being processed. Data subjects hold rights including access, rectification, erasure, portability, and the right to object.

**Data controller**: The entity that determines the purposes and means of processing personal data. Controllers bear primary regulatory responsibility under GDPR.

**Data processor**: An entity that processes personal data on behalf of a controller. Processors have direct GDPR obligations and must operate under a Data Processing Agreement.

**Protected Health Information (PHI)**: Under HIPAA, individually identifiable health information held or transmitted by a covered entity or business associate in any form or medium.

**IT General Controls (ITGCs)**: SOX-relevant controls over logical access, change management, computer operations, and program development that ensure the integrity of financial reporting systems.

**Audit**: An independent, systematic examination of controls, processes, and records to assess conformance with a defined standard.

**Control mapping**: The practice of linking individual security controls to multiple regulatory requirements, enabling a single control to satisfy obligations across frameworks simultaneously.

**GRC platform**: Governance, Risk, and Compliance software that automates evidence collection, control testing, policy management, and regulatory reporting.

**Regulatory inventory**: A documented catalog of all applicable laws, regulations, contractual standards, and industry frameworks, with assigned ownership and compliance status.

**Unified compliance framework**: An approach to compliance management that uses a single master control library mapped to multiple regulatory requirements, eliminating duplicative compliance programs.

**Compensating control**: An alternative control that provides equivalent security protection when the standard-specified control cannot be implemented as written. Compensating controls must be documented and approved by the relevant auditor or regulatory body.

**Safe harbor**: A provision in a law or regulation that protects an organization from liability if it meets specified criteria. Many state breach notification laws provide safe harbors for encrypted data.

**Fair Information Practice Principles (FIPPs)**: A foundational set of privacy principles originating from a 1973 U.S. government report, including Notice, Choice, Access, Security, and Enforcement. Most privacy laws are structured around these principles.

**Supervisory authority**: Under GDPR, the independent public authority responsible for monitoring compliance within an EU member state. Organizations must report certain breaches to the relevant supervisory authority within 72 hours.

**Business associate**: Under HIPAA, a person or entity that performs functions or activities involving PHI on behalf of a covered entity. Business associates must sign a Business Associate Agreement and are directly liable for HIPAA compliance.

---

## 2. Major Regulatory Framework Comparison

The following table compares the six most significant regulatory frameworks by their key characteristics.

### Framework Comparison Table

| Attribute | GDPR | HIPAA | PCI-DSS | SOX | CCPA/CPRA | GLBA |
|---|---|---|---|---|---|---|
| **Jurisdiction** | EU + extraterritorial | United States | Global (contractual) | U.S. public companies | California + extraterritorial | United States |
| **Governing body** | EU supervisory authorities | HHS / OCR | PCI Security Standards Council | SEC / PCAOB | California Privacy Protection Agency | FTC |
| **Enforcement type** | Regulatory (government) | Regulatory (government) | Contractual (card brands) | Regulatory (government) | Regulatory + private right of action | Regulatory (government) |
| **Applies to** | Any org processing EU personal data | Healthcare covered entities + BAs | Orgs handling cardholder data | Publicly traded companies | For-profit businesses meeting thresholds | Financial institutions |
| **Primary data type** | Personal data (any) | Protected Health Information (PHI) | Cardholder data (CHD/SAD) | Financial reporting data | Personal information (California residents) | Non-public personal information |
| **Breach notification (supervisory)** | 72 hours | Not required to supervisory | Not required | Not required | Not required | Not required |
| **Breach notification (individuals)** | "Without undue delay" when high risk | Within 60 days of discovery | Not specified in standard | Not specified | Expedient, most restrictive state law | Expedient |
| **Maximum penalty** | €20M or 4% global revenue | $1.9M/year per category | Loss of card processing | Criminal prosecution | $7,500 per intentional violation | $100K per violation |
| **Individual rights** | 8 data subject rights | Access and amendment | None (consumer) | None (consumer) | 6 consumer rights | Opt-out of sharing |
| **Audit/assessment** | DPA audits; internal audits | HHS OCR audit; BA audits | QSA/SAQ assessment | External auditor (SOX 404) | CPPA enforcement | FTC examination |

---

## 3. Regulatory Breach Notification Comparison

Timing and scope of breach notification obligations vary significantly across frameworks. Security managers must identify the most restrictive applicable deadline when multiple frameworks apply.

### Breach Notification Requirements by Framework

| Framework | Notify Whom | Deadline | Threshold | Notes |
|---|---|---|---|---|
| GDPR (Art. 33) | Supervisory authority | 72 hours from awareness | Any personal data breach unless no risk to individuals | Partial notification allowed; update within reasonable period |
| GDPR (Art. 34) | Affected individuals | "Without undue delay" | High risk to individuals' rights and freedoms | Content requirements specified |
| HIPAA Breach Notification Rule | Affected individuals | Within 60 days of discovery | Unsecured PHI | Safe harbor for encrypted PHI |
| HIPAA (500+ in state) | Prominent media outlets | Within 60 days | Breaches affecting 500+ state residents | In addition to individual notification |
| HIPAA (all breaches) | HHS Secretary | Within 60 days (500+) or annually (under 500) | All PHI breaches | Annual log for small breaches |
| SEC Cyber Disclosure Rule | Investors (Form 8-K) | Within 4 business days of materiality determination | Material cybersecurity incidents | Public companies only |
| CCPA (California) | Affected residents | Expedient and without unreasonable delay | Unencrypted personal information | Private right of action for covered data types |
| Most state laws | Affected residents | Varies: 30, 45, 60, or 90 days | Varies by state and data type | 50 different laws with different triggers |

When an incident triggers multiple notification obligations, the security manager must build a notification matrix tracking each deadline separately and ensuring the most restrictive deadline is met first.

---

## 4. HIPAA Safeguard Categories

HIPAA's Security Rule organizes required safeguards into three categories. Understanding which category a control falls into is tested on the CISM exam.

### HIPAA Security Rule Safeguard Categories

| Category | Examples | Required vs. Addressable |
|---|---|---|
| **Administrative Safeguards** | Security Officer designation; Risk Analysis; Workforce training; Access management procedures; Contingency planning | Mix of required and addressable |
| **Physical Safeguards** | Facility access controls; Workstation use policies; Device disposal procedures; Visitor management | Mix of required and addressable |
| **Technical Safeguards** | Access controls (unique user IDs); Audit controls; Integrity controls; Transmission encryption | Mix of required and addressable |

Note that "addressable" does not mean optional. An addressable safeguard must either be implemented as specified or replaced with an alternative measure that achieves the same security objective, with documentation of the rationale.

---

## 5. PCI-DSS Requirements Summary

### PCI-DSS v4.0 — Six Goals and Twelve Requirements

| Goal | Requirements |
|---|---|
| Build and maintain a secure network and systems | 1. Install and maintain network security controls; 2. Apply secure configurations to all system components |
| Protect cardholder data | 3. Protect stored account data; 4. Protect cardholder data with strong cryptography during transmission over open, public networks |
| Maintain a vulnerability management program | 5. Protect all systems and networks from malicious software; 6. Develop and maintain secure systems and software |
| Implement strong access control measures | 7. Restrict access to system components and cardholder data by business need to know; 8. Identify users and authenticate access to system components; 9. Restrict physical access to cardholder data |
| Regularly monitor and test networks | 10. Log and monitor all access to system components and cardholder data; 11. Test security of systems and networks regularly |
| Maintain an information security policy | 12. Support information security with organizational policies and programs |

---

## 6. SOX IT General Controls Framework

### SOX ITGC Control Domains

| ITGC Domain | Control Objectives | Examples |
|---|---|---|
| **Logical Access** | Ensure only authorized users access financial systems; prevent unauthorized data modification | User provisioning/deprovisioning; privileged access management; MFA for financial systems; access reviews |
| **Change Management** | Ensure only authorized, tested changes are made to financial systems | Change advisory board approval; separation of duties (dev vs. prod); change testing documentation; emergency change procedures |
| **Computer Operations** | Ensure financial systems are available, backed up, and recoverable | Backup and recovery testing; job scheduling monitoring; incident management for financial systems; capacity monitoring |
| **Program Development** | Ensure new financial applications are properly designed, tested, and approved | SDLC governance; user acceptance testing documentation; production migration controls; vendor assessment |

---

## 7. Privacy Law — Individual Rights Comparison

### Consumer/Data Subject Rights by Framework

| Right | GDPR | CCPA/CPRA | HIPAA | GLBA |
|---|---|---|---|---|
| Right to know/access | Yes | Yes | Yes (medical records) | Limited |
| Right to correct/rectify | Yes | Yes (CPRA) | Yes (amendment) | No |
| Right to delete/erasure | Yes | Yes | Limited | No |
| Right to portability | Yes | Yes | No | No |
| Right to opt out of sale/sharing | N/A | Yes | N/A | Yes (opt out of sharing) |
| Right to restrict processing | Yes | Yes (sensitive PI) | No | No |
| Right to object to automated decisions | Yes | No | No | No |
| Right to non-discrimination | No | Yes | No | No |

---

## 8. Compliance Calendar — Annual Program Activities

A well-run compliance program operates on a predictable annual calendar. The following template represents a baseline for organizations subject to HIPAA, PCI-DSS, and SOX. Adapt timing based on your organization's fiscal year and audit cycles.

### Annual Compliance Activity Calendar

| Month | Activity | Framework(s) |
|---|---|---|
| January | Annual security awareness training launch; PCI-DSS SAQ/ROC preparation kickoff | All |
| February | HIPAA risk analysis review; prior year breach log submitted to HHS (under 500 cases) | HIPAA |
| March | SOX ITGC testing — first quarter; PCI-DSS penetration test (if annual schedule) | SOX, PCI-DSS |
| April | Third-party vendor compliance reviews; GRC platform evidence refresh | All |
| May | HIPAA Security Rule addressable specification review; privacy notice updates | HIPAA, GDPR |
| June | SOX ITGC testing — second quarter; mid-year compliance dashboard to board | SOX, All |
| July | PCI-DSS quarterly vulnerability scans; access recertification campaigns | PCI-DSS, HIPAA |
| August | Annual penetration testing (if calendar-year schedule); HIPAA training completion verification | All |
| September | SOX ITGC testing — third quarter; pre-audit readiness assessment | SOX |
| October | External SOX 404 audit fieldwork (calendar year companies); PCI-DSS ROC fieldwork | SOX, PCI-DSS |
| November | Annual policy review and updates; GDPR processing activity records review | All |
| December | SOX ITGC fourth quarter testing; year-end compliance reporting to board and audit committee; remediation status updates | SOX, All |

---

## 9. Audit Preparation Best Practices

Security managers who prepare proactively for audits consistently achieve better outcomes and experience less organizational disruption. The following practices distinguish mature compliance programs.

### Pre-Audit Readiness

Conduct a self-assessment against the applicable framework before auditors arrive. Use the same questionnaires, walkthroughs, and evidence requests the external auditor will use. Address identified gaps before the formal audit begins.

Maintain a continuously updated evidence repository. Evidence collected during operations — screenshots, reports, approval records, training completion logs — should be archived in a GRC platform or structured folder system organized by control and time period.

Designate an audit liaison. A single point of contact for the audit manages evidence requests, schedules interviews, tracks open items, and ensures auditors have what they need without disrupting the broader team.

### During Fieldwork

Respond to evidence requests within agreed timelines. Delays in evidence production create negative audit impressions and can extend the audit timeline significantly.

Do not volunteer information beyond the scope of the question. Answer what is asked completely and accurately, and let the auditor drive the scope.

Document all auditor requests and your responses. This creates a record of what was provided and protects against scope creep or disputed findings.

### Managing Findings

Review draft findings carefully. Factual inaccuracies in audit findings — incorrect descriptions of processes, misattributed controls — should be corrected during the management response period.

Provide management responses that acknowledge findings honestly and describe specific, time-bound remediation actions. Vague management responses ("management will consider improvements") are viewed negatively by auditors and oversight bodies.

Prioritize remediation by residual risk, not by finding severity as assessed by the auditor. Some findings that appear minor from a compliance standpoint may represent significant operational security risks.

---

## 10. Unified Compliance Framework Architecture

### Control-to-Regulation Mapping Example

The following example illustrates how a single encryption control can satisfy multiple regulatory obligations simultaneously.

**Control Statement**: "All sensitive data stored in production databases is encrypted using AES-256. Encryption keys are managed through a dedicated key management system with quarterly rotation."

| Regulatory Obligation | Satisfied Requirement | Notes |
|---|---|---|
| GDPR Article 32 | Appropriate technical measures to protect personal data | Encryption is explicitly mentioned as an example of an appropriate measure |
| HIPAA Security Rule | Technical safeguard — data at rest encryption (addressable) | Satisfies the addressable encryption requirement with documented implementation |
| PCI-DSS Requirement 3 | Protection of stored cardholder data | Meets Requirement 3.5 (strong cryptography) |
| SOX ITGC | Logical access controls — data protection | Contributes to financial data integrity controls |
| CCPA | Reasonable security practices | Encryption creates safe harbor for certain breach scenarios |
| GLBA Safeguards Rule | Encryption of customer information at rest | FTC Safeguards Rule explicitly requires encryption of customer information |

This is the operational power of unified compliance. One control, documented once, satisfies six regulatory obligations. Multiply this across your entire control library and the efficiency gains become substantial.

---

## 11. Exam Preparation Tips — Module 15 Focus Areas

The CISM exam regularly tests regulatory knowledge through scenario-based questions. The following patterns appear frequently.

**Notification timeline questions**: Know the GDPR 72-hour supervisory notification deadline and the HIPAA 60-day individual notification deadline. These are the two most commonly tested timelines.

**Regulatory scope questions**: Know which regulations apply to which types of organizations. Scenario questions often describe a company's business type and ask which regulation applies.

**Compliance vs. security questions**: The exam may present scenarios where compliance would be satisfied by a weaker control, but sound security practice requires a stronger one. Always choose the option that reflects sound governance and risk management, not minimal compliance.

**Audit authority questions**: Understand the difference between internal audit (first-party), customer/partner audit (second-party), and independent external audit (third-party). Know which frameworks use which audit types.

**Control mapping questions**: Understand that a single control can satisfy multiple frameworks. Questions about resource-efficient compliance programs often test this concept.

---

## 12. 50-Point Study Checklist — Module 15

Use this checklist to verify your readiness for the Module 15 quiz and the course final exam.

### GDPR

- [ ] State the legal basis requirements for processing personal data under GDPR
- [ ] Name all eight data subject rights under GDPR
- [ ] Explain the controller versus processor distinction and its compliance implications
- [ ] State the Article 33 supervisory notification deadline (72 hours)
- [ ] Identify the two tiers of GDPR penalties and their maximum amounts
- [ ] Explain what a Data Processing Agreement is and when it is required
- [ ] Describe GDPR's extraterritorial scope — when it applies to non-EU organizations

### HIPAA

- [ ] Name the three components of HIPAA relevant to information security
- [ ] Define Protected Health Information (PHI) and electronic PHI (ePHI)
- [ ] Identify the three categories of HIPAA Security Rule safeguards
- [ ] Explain the difference between "required" and "addressable" HIPAA safeguards
- [ ] State the Breach Notification Rule timeline for individual notification (60 days)
- [ ] Describe the media notification requirement for breaches affecting 500+ state residents
- [ ] Explain what a Business Associate Agreement (BAA) is and who must sign one

### PCI-DSS

- [ ] List the six PCI-DSS goals and twelve requirements by number
- [ ] Explain the difference between a QSA ROC and an SAQ
- [ ] Describe the PCI-DSS v4.0 customized approach and how it differs from the defined approach
- [ ] Identify the consequences of PCI-DSS non-compliance
- [ ] Explain the cardholder data environment (CDE) scoping concept

### SOX

- [ ] Explain Sections 302 and 404 of SOX and their implications for IT
- [ ] Name the four IT General Control domains
- [ ] Describe management's role in SOX 404 assessment versus the external auditor's role
- [ ] Identify the personal liability implications of SOX certifications for executives

### CCPA/CPRA

- [ ] State the three threshold criteria for CCPA applicability
- [ ] List the six consumer rights under CCPA/CPRA
- [ ] Explain CCPA's private right of action for data breaches
- [ ] Describe what rights CPRA added beyond CCPA

### Additional Frameworks

- [ ] Identify what organizations are subject to GLBA and the FTC Safeguards Rule
- [ ] Describe FISMA's requirements and how FedRAMP extends them
- [ ] Explain what FERPA protects and to whom it applies
- [ ] Identify the five Fair Information Practice Principles (FIPPs)

### Audit Management

- [ ] Define first-party, second-party, and third-party audits with examples of each
- [ ] Describe the five phases of the audit lifecycle
- [ ] Explain what an audit liaison's role includes
- [ ] Identify best practices for managing audit findings and management responses

### Compliance Program Management

- [ ] Define a regulatory inventory and explain what it should contain
- [ ] Explain control mapping and give an example of one control satisfying multiple frameworks
- [ ] Describe the purpose and components of an exception management process
- [ ] Identify the components of an annual compliance calendar
- [ ] Explain what a GRC platform is and what functions it automates

### Emerging Regulatory Trends

- [ ] Identify at least four U.S. states with comprehensive privacy laws beyond California
- [ ] Describe the SEC's cyber disclosure rule and its 4-business-day requirement
- [ ] Explain the EU AI Act's risk-tiered approach to AI regulation
- [ ] Identify what CIRCIA requires of critical infrastructure operators

---

## Required Readings

- [GDPR Full Text — Articles 32, 33, and 34](https://gdpr-info.eu/) — Free access to the authoritative GDPR text. Focus on Articles 5 (principles), 13-14 (transparency), 17 (erasure), 32 (security), 33-34 (breach notification), and 83 (penalties).

- [HHS HIPAA Security Rule Summary](https://www.hhs.gov/hipaa/for-professionals/security/index.html) — Free official summary of HIPAA Security Rule requirements organized by safeguard category.

- [PCI-DSS v4.0 Summary of Changes](https://www.pcisecuritystandards.org/document_library/) — Free PCI SSC document summarizing what changed from v3.2.1 to v4.0.

- [NIST SP 800-53 Rev. 5 Control Catalog](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Free NIST publication providing the control catalog used as the foundation for FISMA compliance and widely used in unified compliance mapping.

---

---

## 9. Supplemental Resources

**1. IAPP — Introduction to U.S. Privacy Law**
<https://iapp.org/resources/article/introduction-to-u-s-state-privacy-law/>
The International Association of Privacy Professionals maintains up-to-date summaries of U.S. state privacy laws including CCPA/CPRA, Virginia CDPA, Colorado CPA, and others. Essential for tracking the evolving U.S. state privacy landscape covered in this module's emerging trends section.

**2. PCI Security Standards Council — PCI-DSS v4.0 Resource Hub**
<https://www.pcisecuritystandards.org/pci_security/maintaining_payment_security>
The official PCI SSC resource hub includes the full PCI-DSS v4.0 standard, SAQ forms, ROC templates, and the Summary of Changes document. Free registration provides access to all documents needed for the PCI-DSS compliance content in this module.

**3. NIST Privacy Framework Version 1.0**
<https://www.nist.gov/privacy-framework>
NIST's voluntary privacy risk management framework that complements NIST CSF. Provides a structured approach to identifying and managing privacy risks that aligns with GDPR, CCPA, and other privacy regulation requirements covered in this module. Useful for understanding how privacy governance integrates with broader cybersecurity governance.

End of Reading Guide — Module 15
