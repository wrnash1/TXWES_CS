# Lab Activity: Module 15 — Compliance Gap Analysis Exercise

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 1 (Information Security Governance) and Domain 3 (Information Security Program Development and Management)

---

## Overview

In this lab you will conduct a structured compliance gap analysis for a fictional healthcare payment processing company. The scenario requires you to identify applicable regulatory frameworks, map existing controls to requirements, identify gaps, and produce a prioritized remediation roadmap. This exercise mirrors the work information security managers perform when organizations prepare for audits, enter new business lines, or respond to regulatory changes.

Estimated time to complete: 90 to 120 minutes.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Identify which regulatory frameworks apply to a described organization
- Map existing security controls to specific regulatory requirements
- Identify gaps between current controls and regulatory obligations
- Prioritize remediation actions using a risk-based approach
- Produce a compliance gap analysis deliverable in a format suitable for executive presentation

---

## Scenario: MedPay Solutions

MedPay Solutions is a mid-sized company headquartered in Dallas, Texas. The company processes medical billing payments on behalf of 47 independent physician practices across five states. Their operations include the following characteristics:

- Annual revenue: $18 million
- Transactions processed per year: approximately 1.2 million, involving Visa, Mastercard, and Discover payments
- Data processed: patient names, dates of birth, diagnosis codes, procedure codes, insurance information, and payment card numbers
- Customer base: physician practices in Texas, California, Oklahoma, Arkansas, and New Mexico
- Technology environment: cloud-hosted billing platform (AWS), on-premises data center for archived records, 140 employees, 12 of whom are remote
- Third parties: cloud hosting provider, third-party payroll processor, a marketing analytics vendor that receives de-identified patient demographic data

MedPay Solutions currently has the following controls in place:

- Annual security awareness training for all employees
- Firewall and intrusion detection at the network perimeter
- Password policy requiring minimum 8 characters with complexity
- Encryption of payment card data in transit (TLS 1.2)
- Quarterly vulnerability scans of the internal network
- An incident response procedure document (last updated 3 years ago)
- No documented risk assessment process
- No formal vendor management program
- No encryption of archived records stored in the on-premises data center
- No multi-factor authentication on any systems
- A privacy notice posted on the company website (last reviewed 2 years ago)

---

## Part A — Regulatory Applicability Analysis

### Instructions

Review the MedPay Solutions scenario and complete the Regulatory Applicability Worksheet below. For each framework listed, determine whether it applies to MedPay Solutions, identify the basis for applicability, and note any thresholds or conditions that affect applicability.

### Regulatory Applicability Worksheet

Complete the following table. Write your analysis in the Notes column for each framework.

| Framework | Applies? | Basis for Applicability | Key Obligations Triggered | Notes |
|---|---|---|---|---|
| HIPAA Privacy Rule | | | | |
| HIPAA Security Rule | | | | |
| HIPAA Breach Notification Rule | | | | |
| PCI-DSS v4.0 | | | | |
| CCPA/CPRA | | | | |
| SOX | | | | |
| GLBA Safeguards Rule | | | | |
| Texas Data Privacy and Security Act | | | | |
| State breach notification laws (multi-state) | | | | |

### Guidance Questions for Part A

Answer the following questions in complete sentences as part of your Part A submission.

1. MedPay processes both PHI and cardholder data. Does this create any conflicts between HIPAA and PCI-DSS requirements, or do the frameworks complement each other? Explain your reasoning.

2. MedPay has California-based physician practice clients whose patients may be California residents. Does CCPA apply? Identify which CCPA threshold(s) MedPay may meet.

3. MedPay shares de-identified data with a marketing analytics vendor. Under HIPAA, what are the two methods for de-identification, and does the description of this practice raise any compliance concerns?

4. If MedPay experienced a breach of patient payment records, which frameworks would trigger mandatory notification obligations? Build a notification matrix showing each obligation and its deadline.

---

## Part B — Control Gap Analysis

### Part B Instructions

Using the list of existing controls described in the MedPay Solutions scenario, complete the Control Gap Analysis Worksheet. For each regulatory requirement listed, identify whether MedPay's current controls satisfy the requirement, partially satisfy it, or represent a gap. Provide a brief explanation for each assessment.

### Control Gap Analysis Worksheet

| Requirement | Framework | Control Status | Existing Control (if any) | Gap Description |
|---|---|---|---|---|
| Risk analysis must be conducted and documented | HIPAA Security Rule (Required) | | | |
| Multi-factor authentication for access to ePHI systems | HIPAA Security Rule (Addressable) | | | |
| Encryption of ePHI at rest | HIPAA Security Rule (Addressable) | | | |
| Workforce training on security policies and procedures | HIPAA Security Rule (Required) | | | |
| Business Associate Agreements with all business associates | HIPAA Privacy Rule (Required) | | | |
| Incident response plan — current and tested | HIPAA Security Rule (Required) | | | |
| Multi-factor authentication for all non-console access | PCI-DSS Requirement 8.4 | | | |
| Encryption of stored cardholder data | PCI-DSS Requirement 3.5 | | | |
| Penetration testing at least annually | PCI-DSS Requirement 11.4 | | | |
| Vendor/third-party security assessment | PCI-DSS Requirement 12.8 | | | |
| Password length minimum 12 characters (PCI-DSS v4.0) | PCI-DSS Requirement 8.3 | | | |
| Privacy notice current and accurate | CCPA | | | |
| Data subject rights fulfillment process | CCPA | | | |
| Encryption of customer information at rest | GLBA Safeguards Rule | | | |
| Annual security program report to board/management | GLBA Safeguards Rule | | | |

### Guidance Questions for Part B

Answer the following questions as part of your Part B submission.

1. MedPay's password policy requires a minimum of 8 characters. PCI-DSS v4.0 raised the minimum to 12 characters for user accounts. How should MedPay document this gap, and what is the remediation action?

2. The incident response procedure is 3 years old and untested. Under HIPAA, what specific administrative safeguard does this violate, and what does remediation require?

3. MedPay has no formal vendor management program. Identify at least three specific compliance obligations across different frameworks that this gap affects.

---

## Part C — Prioritized Remediation Roadmap

### Part C Instructions

Based on your gap analysis in Part B, create a prioritized remediation roadmap. Prioritization should reflect both regulatory risk (likelihood and severity of regulatory action) and operational security risk. Do not simply list findings in alphabetical order — a prioritized roadmap demonstrates sound risk management judgment.

### Remediation Roadmap Template

Complete the following table with your top eight remediation actions. Add rows as needed.

| Priority | Gap Description | Framework(s) | Remediation Action | Owner (Role) | Target Date | Resource Estimate | Risk if Not Addressed |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |

### Guidance Questions for Part C

Answer the following questions as part of your Part C submission.

1. You identified no formal risk analysis process as a gap. Why does a documented risk analysis affect the prioritization and defensibility of all other remediation actions? Use CISM Domain 2 principles to support your answer.

2. MedPay's leadership asks you to deprioritize the encryption of archived on-premises records because the project will cost $180,000. Draft a brief risk acceptance memo (3 to 5 sentences) that leadership would need to sign to formally document this decision. Include the residual risk, compensating controls proposed, and the conditions under which the decision would be revisited.

3. How would you present the remediation roadmap to MedPay's board of directors? Describe the key metrics and risk indicators you would include and explain why technical control details should not be the focus of a board presentation.

---

## Part D — Unified Control Mapping Exercise

### Part D Instructions

Select three of the gaps you identified in Part B that appear in multiple frameworks simultaneously. For each gap, complete the unified control mapping table below, showing how a single remediation action would satisfy multiple regulatory obligations.

### Unified Control Mapping Table

| Control Statement | Regulatory Obligation 1 | Regulatory Obligation 2 | Regulatory Obligation 3 | Justification |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

After completing the table, write a 150 to 200 word paragraph explaining to a non-technical executive why a unified compliance approach is more cost-effective than building separate compliance programs for each regulation. Use your MedPay examples to make the argument concrete.

---

## Deliverables

Submit the following to the Canvas LMS assignment portal.

1. Completed Regulatory Applicability Worksheet (Part A) with all guidance questions answered
2. Completed Control Gap Analysis Worksheet (Part B) with all guidance questions answered
3. Completed Prioritized Remediation Roadmap (Part C) with all guidance questions answered
4. Completed Unified Control Mapping Table (Part D) with explanatory paragraph

Format: Submit as a single PDF or Word document. Use the section headings from this lab as your document structure. Tables may be recreated in Word, Google Docs, or Excel and pasted as screenshots if needed.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part A — Regulatory applicability correctly identified with reasoning | 20 |
| Part B — Gap analysis accurately assesses each control's compliance status | 25 |
| Part C — Remediation roadmap is risk-prioritized with business-level rationale | 25 |
| Part D — Unified mapping demonstrates cross-framework efficiency | 15 |
| Writing quality — complete sentences, professional terminology, clear analysis | 15 |
| Total | 100 |

---

## Resources

- [GDPR Full Text](https://gdpr-info.eu/) — Articles 32–34 for security and breach notification requirements
- [HHS HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html) — Official safeguard categories and implementation specifications
- [PCI-DSS v4.0 Summary of Changes](https://www.pcisecuritystandards.org/) — Key changes from v3.2.1 including MFA and password requirements
- [FTC GLBA Safeguards Rule](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act) — Updated 2023 requirements
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Unified control catalog for cross-framework mapping

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Framework Breach Notification Gap Analysis

HealthBridge Financial is a healthcare lending company that processes patient financing applications. It holds electronic protected health information (ePHI) under HIPAA, payment card data under PCI-DSS, and personal information of approximately 4,200 EU residents under GDPR. On a Tuesday morning at 8:00 AM, the security team confirms a breach: an unencrypted database backup containing all three data types was inadvertently exposed on a public cloud storage bucket for seventeen days before discovery.

1. For each of the three applicable frameworks (HIPAA Breach Notification Rule, GDPR Article 33, and PCI-DSS Incident Response Requirements), complete a notification timeline table with these columns: Framework, Notification Target, Deadline (calculated from the Tuesday 8:00 AM discovery), What Must Be Included in the Notification, and Consequence of Missing the Deadline. Use real regulatory deadlines — do not estimate.
2. Identify the single notification deadline that poses the greatest immediate compliance risk, and draft a sample notification to the appropriate authority for that framework. The notification must include all elements required by the applicable regulation. Where specific data is not available from the scenario, use plausible placeholder values clearly labeled as such.
3. The organization's legal counsel argues that because the data was "only" in a cloud storage bucket — not exfiltrated by an attacker — this may not be a "breach" requiring notification under HIPAA. Evaluate this argument by applying the HIPAA Breach Notification Rule's presumption of breach standard and the four-factor risk assessment used to rebut the presumption. Based on your analysis, state whether notification is required and why.
4. Build a cross-framework notification coordination matrix showing which notifications can be managed with a single communication versus which require separate filings, and propose a notification sequencing schedule for the first 72 hours after discovery.

### Challenge 2: Compliance Control Gap Mapping and Exception Management

The compliance team at HealthBridge Financial has completed an internal control assessment and identified the following five gaps. For each gap, perform a complete compliance analysis.

**Gap 1:** Multi-factor authentication is not enforced for remote access to systems containing cardholder data. (Current state: password-only; Applicable requirement: PCI-DSS v4.0 Requirement 8.4.2)

**Gap 2:** The organization has not conducted a HIPAA Security Rule risk analysis in three years. (Applicable requirement: 45 CFR § 164.308(a)(1))

**Gap 3:** EU resident data subjects have submitted eleven access requests in the past year; the average response time was 47 days. (Applicable requirement: GDPR Article 15 and Article 12(3) — one-month response deadline)

**Gap 4:** The organization's data retention schedule deletes all records at seven years, but EU resident personal data records in the financing database have been retained for nine years without documented justification. (Applicable requirement: GDPR Article 5(1)(e) storage limitation)

**Gap 5:** The disaster recovery plan has not been tested in two years. (Applicable requirement: HIPAA Security Rule 45 CFR § 164.308(a)(7)(ii)(D) and PCI-DSS v4.0 Requirement 12.10.2)

For each gap: identify the specific regulatory citation violated, classify the severity (Critical / High / Medium) with justification, draft a one-paragraph management response suitable for inclusion in an audit finding response, assign an owner role, and set a remediation target date within 90 days that is realistic given the gap's complexity.

### Reflection Questions

1. A compliance manager proposes eliminating the organization's annual SOC 2 Type II audit to reduce costs, arguing that the organization already completes HIPAA and PCI-DSS assessments and that SOC 2 is redundant. From a stakeholder trust and governance perspective, explain what SOC 2 Type II provides that HIPAA and PCI-DSS assessments do not, and identify at least two business contexts in which the absence of a SOC 2 report would create a material disadvantage.
2. An organization operating under both GDPR and CCPA receives a deletion request from a California resident who is also an EU citizen. The organization's legal team argues that it only needs to honor the request once since both laws require deletion. Identify at least two ways in which the GDPR right to erasure (Article 17) and the CCPA right to delete differ in their scope, exceptions, or procedural requirements — and explain why a legally compliant response must address both frameworks independently rather than treating them as identical obligations.

End of Lab — Module 15
