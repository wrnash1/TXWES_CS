# Lab Activity: Module 14 — Governance, Compliance, and Regulatory Frameworks

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

**Estimated Time:** 90 minutes

**Format:** Individual written analysis with structured deliverables

**Submission:** Upload completed responses as a single PDF or Word document to the course LMS.

In this lab you will apply the governance and compliance concepts from Module 14 to a realistic organizational scenario. You will perform a basic compliance gap analysis, develop a data classification scheme, and draft a short security policy — skills directly tested on the Security+ exam and required in real security roles.

---

## Scenario: Lakewood Medical Associates

Lakewood Medical Associates (LMA) is a regional healthcare network with 12 clinics and 850 employees across Texas. LMA recently acquired a smaller practice and is now expanding its IT infrastructure. The CISO has asked the security team to assess compliance readiness and strengthen foundational governance documents.

LMA's current situation:

- Stores and transmits electronic patient records (diagnoses, prescriptions, insurance billing)
- Accepts credit card payments at all 12 clinics
- Employs a cloud-based EHR (Electronic Health Records) vendor under a signed contract
- Has a written Acceptable Use Policy last updated in 2019
- Has no formal data classification scheme
- Has no documented risk assessment on file
- Recently hired 40 new staff with no security awareness training completed
- Is a private company (not publicly traded)

---

## Part 1: Regulatory Applicability Analysis (25 points)

### Part 1 Instructions

For each regulation or framework listed below, determine whether it applies to LMA, explain why or why not, and identify the single most important compliance obligation LMA must address under that regulation.

Complete the following table in your submission:

| Regulation / Framework | Applies to LMA? (Yes/No) | Justification | Most Critical Obligation for LMA |
|------------------------|--------------------------|---------------|----------------------------------|
| HIPAA | | | |
| PCI-DSS | | | |
| GDPR | | | |
| SOX | | | |
| NIST CSF | | | |
| ISO 27001 | | | |

### Guidance Notes

- For GDPR, consider whether LMA has any patients who are EU residents or citizens.
- For NIST CSF, recall that it is voluntary — but "voluntary" does not mean "not applicable."
- For ISO 27001, consider what "applies" means for a voluntary certifiable standard.
- Your justifications should be 2–4 sentences each.

---

## Part 2: Data Classification Scheme (25 points)

### Part 2 Instructions

LMA has no data classification scheme. Design one appropriate for a healthcare organization.

**Step 1:** Define three classification levels for LMA. For each level, provide:

- A level name (appropriate for healthcare)
- A one-sentence definition
- Two examples of data at that level from LMA's environment
- Required handling controls (storage, transmission, destruction — at least one control per category)

Present your three levels in a structured format (table or numbered sections).

**Step 2:** Assign a classification level to each of the following data elements LMA holds. Justify each assignment in one sentence:

- Patient name and diagnosis
- Patient credit card number used for copay
- Employee home address in HR records
- Clinic location hours posted on the public website
- Internal IT network diagram
- EHR vendor contract terms
- Aggregate (de-identified) statistics on flu cases by zip code

**Step 3:** Identify who should serve as the data owner and data custodian for patient health records at LMA. Describe each role's specific responsibilities in this context.

---

## Part 3: Compliance Gap Analysis — HIPAA Security Rule (25 points)

### Part 3 Instructions

Using the three HIPAA Security Rule safeguard categories (Administrative, Physical, Technical), assess LMA's current compliance posture based on the scenario facts provided.

For each category, complete the following:

### Administrative Safeguards Gap Analysis

List three required administrative safeguard controls. For each, indicate whether LMA currently meets, partially meets, or does not meet the requirement based on the scenario, and describe the gap.

Use this format:

- Control name
- Status: Meets / Partial / Does Not Meet
- Gap description (1–2 sentences)

Required administrative safeguard controls to assess:

1. Security Management Process (including risk analysis)
2. Workforce Training and Awareness
3. Contingency Plan

### Physical Safeguards Gap Analysis

Assess these three physical safeguard controls for LMA:

1. Facility Access Controls
2. Workstation Use Policy
3. Device and Media Controls

### Technical Safeguards Gap Analysis

Assess these three technical safeguard controls for LMA:

1. Access Control (unique user IDs, automatic logoff)
2. Audit Controls (hardware/software activity logs)
3. Transmission Security (encryption of ePHI in transit)

### Gap Summary

After completing all nine control assessments, write a 3–5 sentence executive summary suitable for LMA's CISO that describes the most critical gaps and recommended remediation priorities.

---

## Part 4: Security Policy Drafting (25 points)

### Part 4 Instructions

LMA's Acceptable Use Policy is seven years old and does not address mobile devices, cloud services, or remote work — all now common at LMA. Draft a new section to be added to the AUP titled "Mobile Device and Remote Access Policy."

Your policy section must:

- Follow the correct structure for a security policy (not a procedure or guideline)
- Be mandatory in tone ("must," "shall," "is prohibited" — not "should" or "recommended")
- Address at least four of the following topics:
  - Approved mobile devices and enrollment requirements
  - Encryption requirements for mobile devices accessing ePHI
  - Remote access methods (VPN, MFA requirements)
  - Prohibited activities on personal devices used for work
  - Lost or stolen device reporting and response
  - Cloud storage restrictions for PHI

Your policy section should include:

- A purpose statement
- A scope statement (who the policy applies to)
- At least six specific policy statements
- A violations/enforcement clause

Length: 300–500 words.

---

## Submission Requirements

Organize your submission with clearly labeled sections corresponding to Parts 1 through 4. Include your name, course number, and date on the cover page.

**Grading Rubric Summary:**

- Part 1 — Regulatory Applicability: 25 points (accuracy of applicability determination + quality of justification)
- Part 2 — Data Classification: 25 points (completeness of scheme, accuracy of assignments, role clarity)
- Part 3 — Gap Analysis: 25 points (correct identification of gaps, relevance to scenario, quality of executive summary)
- Part 4 — Policy Draft: 25 points (correct policy structure, mandatory tone, topical coverage, professional writing)

---

## Study Connection

This lab directly prepares you for Security+ SY0-701 performance-based questions in which you must:

- Identify the applicable compliance framework for a given organizational scenario
- Distinguish between policy types and write appropriate governance documents
- Assess control gaps and recommend remediation actions
- Apply data classification concepts to realistic data inventories

Review Module 14 Parts 1 and 2 and the Reading Guide before beginning. Pay particular attention to the HIPAA safeguard categories and the governance document hierarchy.

---

## Part 9 — Challenge Exercise

### Challenge 1: Cross-Framework Compliance Mapping

A multinational financial technology company (fintech) is headquartered in Texas, processes credit card payments for customers in the US and EU, employs 3,400 people, and is publicly traded on the NYSE. The company stores cardholder data, employee PII, and EU customer personal data in a shared cloud database hosted on AWS.

1. Identify every compliance framework from this module that applies to this company. For each, state: what data or activity triggers applicability, the single most operationally demanding requirement, and the maximum penalty for non-compliance.
2. The company's legal team asks whether a single ISO 27001 certification could satisfy all of its compliance obligations. Write a 200-word response explaining what ISO 27001 certification does and does not cover in relation to the other applicable frameworks.
3. Design a data flow diagram (described in text) showing how cardholder data moves from a customer payment at checkout through the company's systems. For each stage in the flow, identify which compliance framework's requirements are most directly triggered and name one specific control required at that stage.

### Challenge 2: Governance Document Suite Development

A regional hospital network has no formal governance document hierarchy. The CISO has been asked to build one from scratch, starting with three foundational documents covering encryption, mobile devices, and third-party vendor access.

1. Draft a one-paragraph **information security policy** statement for each of the three topics. Each policy statement must: be mandatory in tone, state the high-level requirement without specifying implementation details, and be written at a level appropriate for board approval.
2. For the encryption topic, draft a supporting **standard** that specifies: the minimum encryption algorithm and key length for data at rest, the minimum TLS version for data in transit, and the requirement for encrypted backups. The standard must be specific and measurable.
3. For the mobile device topic, draft a four-step **procedure** that an IT administrator would follow when a physician reports a lost mobile device that was enrolled in the MDM system and had access to patient records. The procedure must address containment, notification, evidence preservation, and documentation.

### Reflection Questions

1. A company's lawyers argue that because they use a PCI-DSS-compliant payment processor, the company itself has no PCI-DSS obligations. Is this argument correct? Explain what the shared responsibility model means in the context of PCI-DSS and where the merchant's obligations begin and end.
2. A CISO tells the board: "We are HIPAA compliant." A board member asks, "Who certified you?" The CISO is silent. Why is there no "HIPAA certification," and what evidence should the CISO present instead to demonstrate HIPAA compliance to the board?

---

End of Lab — Module 14
