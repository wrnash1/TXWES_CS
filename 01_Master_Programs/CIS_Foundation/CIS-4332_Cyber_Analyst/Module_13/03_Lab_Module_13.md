# Lab Activity: Module 13 — Compliance and Security Controls Validation

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Lab Overview

In this lab you will perform a compliance gap analysis against the CIS Controls v8 Implementation Group 1 for a simulated small-to-medium enterprise. You will assess current control states from provided documentation, map them to CIS Control requirements, identify gaps, rate their severity, and produce a formal gap report and remediation roadmap.

This lab directly mirrors analyst work in compliance assessments, audit preparation, and security program development — and maps to CySA+ exam objectives covering security controls and compliance reporting.

**Estimated Time:** 90–120 minutes

**Tools Required:** Spreadsheet application (Excel, Google Sheets, or LibreOffice Calc), text editor or word processor, CIS Controls v8 reference (free at cisecurity.org)

---

## Scenario Background

You have been engaged as a security analyst to assess the security posture of Meridian Financial Services, a regional accounting firm with 85 employees, three office locations, and a cloud-hosted document management platform. The firm is preparing for a SOC 2 Type II audit and wants to understand its current gaps against CIS Controls v8 Implementation Group 1 (IG1) before the auditors arrive.

You have been provided with the following documentation (simulated in this lab):

- Network diagram showing three office sites connected via VPN to a central cloud environment
- Asset inventory spreadsheet (last updated 14 months ago, estimated 60% complete)
- Software list from IT (manually maintained, estimated 70% complete)
- Current security policies (acceptable use policy, password policy, remote access policy)
- Most recent vulnerability scan report (performed 11 months ago using a free scanner)
- Active Directory configuration summary (password policy, MFA status, admin account inventory)
- Firewall ruleset summary
- Backup configuration report
- Security awareness training completion report (last training cycle: 18 months ago, 62% completion)

---

## Part 1 — CIS IG1 Control Mapping

CIS Controls v8 IG1 contains 56 specific safeguards across the 18 controls. For this lab you will assess the following 10 representative IG1 safeguards.

Create a Control Assessment Table in your lab report spreadsheet with the following columns:

- CIS Safeguard ID
- Safeguard Description
- Current State (Implemented / Partial / Not Implemented)
- Supporting Evidence (what documentation supports your rating)
- Gap Description (if partial or not implemented)
- Risk Rating (High / Medium / Low)

### Safeguards to Assess

Assess each of the following based on the scenario documentation provided above:

**Safeguard 1.1** — Establish and maintain a detailed enterprise asset inventory. Document all enterprise assets with the potential to store or process data.

**Safeguard 2.1** — Establish and maintain a software inventory. Maintain a list of all authorized software.

**Safeguard 3.3** — Configure data access control lists based on a user's need to know.

**Safeguard 4.1** — Establish and maintain a secure configuration process for enterprise assets and software.

**Safeguard 5.2** — Use unique passwords. Ensure all enterprise assets use unique, complex passwords.

**Safeguard 5.3** — Disable dormant accounts within 45 days.

**Safeguard 6.3** — Require MFA for externally exposed applications.

**Safeguard 7.3** — Perform automated operating system patch management with a defined cadence.

**Safeguard 11.2** — Perform automated backups.

**Safeguard 14.1** — Establish and maintain a security awareness program. Ensure all staff complete security awareness training annually.

### Assessment Instructions

For each safeguard, review the relevant scenario documentation and determine the current state:

- **Implemented** — The safeguard is fully in place with documented evidence
- **Partial** — The safeguard is partially in place (for example, MFA is implemented for most but not all externally exposed applications)
- **Not Implemented** — No satisfying control exists

Assign a risk rating based on the criticality of the safeguard and the organization's exposure:

- **High** — The absence of this control creates significant, likely-to-be-exploited risk
- **Medium** — The absence creates meaningful risk but with some mitigating factors
- **Low** — The absence creates limited risk given compensating controls or low threat likelihood

---

## Part 2 — Gap Analysis Summary

Using your Control Assessment Table from Part 1, answer the following in your lab report:

1. How many of the 10 assessed safeguards are fully implemented, partially implemented, and not implemented?
2. Which three gaps carry the highest risk rating? For each, explain in two to three sentences why you rated it High.
3. Which single gap, if left unaddressed, would most likely result in a finding during the SOC 2 audit? Justify your selection by referencing the specific SOC 2 Trust Service Criteria it relates to (hint: SOC 2 Trust Services Criteria include Security, Availability, Processing Integrity, Confidentiality, Privacy).
4. Identify any gaps that have a compensating control relationship — where one gap is partially offset by another implemented safeguard.

---

## Part 3 — Control Classification Exercise

For each of the following security controls, classify by type (Technical / Administrative / Physical) AND function (Preventive / Detective / Corrective / Deterrent). A control may have more than one classification.

Present your answers in a table with columns: Control Description, Type, Function, Justification.

Controls to classify:

1. Multifactor authentication on all remote access portals
2. Annual security awareness training for all employees
3. Locked server room with badge access
4. SIEM alert rules for failed login attempts exceeding threshold
5. Automated daily backup of all financial records to off-site storage
6. Acceptable use policy prohibiting personal email on company devices
7. Network firewall blocking inbound connections on all ports except 443
8. Video surveillance cameras in the data center
9. Incident response plan and trained response team
10. Automatic screen lock after 10 minutes of inactivity

---

## Part 4 — Audit Evidence Package Planning

Assume Meridian Financial Services has just remediated all identified gaps and is preparing for the SOC 2 audit. Create an audit evidence plan for the following three controls:

For each control, specify: what evidence you would collect, how you would collect it (tool, method, or process), the time period the evidence must cover, and how you would verify the evidence's integrity.

Controls to plan evidence for:

1. MFA enforcement for externally exposed applications (Safeguard 6.3)
2. Automated backup operations with verified recovery capability (Safeguard 11.2)
3. Security awareness training completion at or above 90% (Safeguard 14.1)

---

## Part 5 — Remediation Roadmap

Based on your gap analysis findings, create a remediation roadmap for Meridian Financial Services. The roadmap should be a prioritized action plan table with the following columns:

- Priority (1 = highest)
- Gap (reference CIS Safeguard ID)
- Recommended Action
- Responsible Owner (role, not name — for example, IT Administrator, CISO, HR Manager)
- Target Completion (use relative timeframes: 30 days, 60 days, 90 days, 6 months)
- Estimated Effort (Low / Medium / High)

Include all gaps identified in Part 1. Prioritize by risk rating — High gaps first, then Medium, then Low. Within the same risk tier, prioritize by effort (low-effort high-risk items first).

---

## Deliverables

Submit a single PDF to Canvas containing:

1. Part 1 — Control Assessment Table (10 rows)
2. Part 2 — Gap Analysis Summary (questions 1–4)
3. Part 3 — Control Classification Table (10 rows)
4. Part 4 — Audit Evidence Package Plan (3 controls)
5. Part 5 — Remediation Roadmap table

**Grading:** 100 points total. Parts 1 and 5 are worth 25 points each. Parts 2, 3, and 4 are worth 17 points each.

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Framework Gap Analysis Under Constraint

You are the sole security analyst at a 200-employee regional accounting firm. The firm processes payment card data for clients and stores health benefit enrollment records for employees. An external auditor has flagged three findings from a recent assessment:

- **Finding A**: Antivirus signatures have not been updated on 40% of endpoints for more than 30 days. No centralized patch status reporting exists.
- **Finding B**: Privileged administrative accounts share the same password as standard user accounts for the same individuals. No privileged access management (PAM) solution is in place.
- **Finding C**: No formal vendor risk assessment process exists. Third-party software vendors have not been evaluated for security posture before contract award.

1. For each finding (A, B, C), identify: the applicable CIS Control and Safeguard ID (v8), the NIST CSF function and subcategory code, and whether the finding constitutes a potential PCI DSS or HIPAA violation. Provide the specific PCI DSS requirement number or HIPAA rule reference for each applicable regulatory finding.
2. The firm's IT team has a budget of $0 for the next 90 days — no new tools can be purchased. For each finding, propose one compensating control that can be implemented using only native OS features, free open-source tools, or administrative processes. Identify what residual risk remains after each compensating control.
3. Rank the three findings by remediation priority using the CVSS environmental score concept (impact × exploitability × scope). Explain your ranking with at least two factors per finding that influenced the priority decision.
4. Write a one-paragraph executive summary (4–6 sentences) addressed to the firm's CEO that describes the risk posture without using technical jargon. The summary must convey urgency without causing panic and must include one concrete business impact example for each finding.

### Challenge 2: Audit Evidence Package Construction

You are preparing for a SOC 2 Type II audit covering the 12-month period January–December of the previous year. The auditors have requested evidence for three controls:

- **Control 1**: All privileged user accounts are reviewed quarterly and deprovisioned within 24 hours of employee termination.
- **Control 2**: Security patches rated Critical or High are applied to production systems within 30 days of release.
- **Control 3**: Security awareness training is completed by 100% of employees annually, with documented acknowledgment of the acceptable use policy.

For each control:

1. Identify the minimum evidence artifacts required to satisfy a SOC 2 Type II auditor. For each artifact, specify the source system (e.g., Active Directory, ITSM tool, LMS), the format (export, screenshot, log), and the time range that must be covered.
2. Identify one failure scenario — a realistic situation where your organization might technically have the control but the evidence package would still fail the audit — and explain what documentation gap caused the failure.
3. Write a one-paragraph management assertion for each control (3–4 sentences) in the format used in actual SOC 2 reports: describe what the control does, how it operates, who is responsible, and how its effectiveness is monitored.

### Reflection Questions

1. The NIST CSF and CIS Controls are both widely used frameworks, but they serve different primary audiences and purposes. Explain the key difference in how each framework is designed to be used, and describe a scenario where an organization should reference both frameworks simultaneously rather than choosing one over the other.
2. Gap analysis findings are often technically accurate but organizationally ineffective if presented without business context. Describe two techniques an analyst can use to translate a technical control gap into language that motivates a non-technical executive to approve remediation funding, and explain why each technique is effective.
