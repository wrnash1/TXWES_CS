# Lab Activity: Module 14 — Risk and Compliance in ITSM

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Scenario: Pinnacle Health Partners

Pinnacle Health Partners (PHP) is a health insurance organization providing coverage to 820,000 members across five states. The IT department manages the systems that process member enrollment, claims adjudication, provider data, and customer support. PHP is subject to HIPAA, has recently been selected for a SOC 2 Type II audit by its largest employer client, and the CISO has initiated an ISO 27001 gap analysis in preparation for eventual certification.

You are the IT Compliance Analyst. You will complete four exercises that build PHP's compliance foundation.

---

## Exercise 1: Risk Register Development (25 points)

PHP's security team has identified the following five risks during a recent threat assessment. Complete the risk register entries below.

**Risk 1:** A former employee's VPN credentials were not revoked upon termination. The account remains active and could be used for unauthorized access to the claims processing system.

**Risk 2:** PHP's primary data center uses a single internet service provider for external connectivity. A provider outage would make the member portal and provider network unavailable.

**Risk 3:** PHP's claims adjudication platform vendor announced end-of-life for the current version in 14 months. Running end-of-life software means no security patches will be available after that date.

**Risk 4:** The claims processing team uses email to transmit Excel files containing member PHI to the actuarial team. Email is not encrypted in transit for internal messages.

**Risk 5:** PHP's annual penetration test has not been scheduled and is now nine months overdue. Without a recent pen test, PHP has no current assessment of its external attack surface.

For each risk, complete the following fields:

| Field | Risk 1 | Risk 2 | Risk 3 | Risk 4 | Risk 5 |
|---|---|---|---|---|---|
| Risk category | | | | | |
| Likelihood (1–5) | | | | | |
| Impact (1–5) | | | | | |
| Risk score | | | | | |
| Response strategy | | | | | |
| Proposed control or action | | | | | |

After completing the table, write a 100–150 word justification explaining which risk you would prioritize for immediate action and why. Consider both the risk score and the nature of the harm.

---

## Exercise 2: ISO 27001 Gap Analysis (25 points)

PHP is conducting a preliminary gap analysis against six ISO 27001 Annex A controls. Review the current state of each control and determine the gap status.

| Annex A Control | Requirement Summary | PHP's Current State | Gap Status |
|---|---|---|---|
| A.9.2.6 — Removal of access rights | Access rights must be removed upon termination or role change | IT Help Desk removes access within 5 business days of HR notification; Risk 1 above demonstrates this is not always followed | ? |
| A.12.6.1 — Management of technical vulnerabilities | Timely identification and remediation of technical vulnerabilities | Patching is performed monthly for servers; pen testing is overdue (Risk 5) | ? |
| A.8.1.1 — Inventory of assets | All assets must be identified and an inventory maintained | Asset spreadsheet updated quarterly; 14 months stale (see Module 13 scenario) | ? |
| A.13.2.1 — Information transfer policies | Policies must govern the transfer of information | No formal policy exists governing email vs. encrypted transfer for PHI (Risk 4) | ? |
| A.17.1.2 — Implementing business continuity | Business continuity plans must be implemented and maintained | PHP has a documented BCP; last tested 18 months ago | ? |
| A.16.1.1 — Responsibilities and procedures for incident management | Documented incident management procedures must exist | PHP has a documented incident response plan; tested via tabletop exercise last quarter | ? |

### Task 2a: Gap assessment

For each control, assign a gap status using one of three designations: **Compliant**, **Partial Gap** (control exists but has deficiencies), or **Full Gap** (control is absent or fundamentally inadequate). Provide a one-sentence justification for each assessment.

### Task 2b: Remediation prioritization

Two of the six controls have the most direct connection to the HIPAA obligation to protect PHI. Identify those two controls and write a 100–150 word prioritization rationale explaining which should be addressed first and why.

### Task 2c: Statement of Applicability note

The Statement of Applicability (SoA) documents which controls are selected and which are excluded with justification. PHP is a U.S. health insurer, not a company with classified government contracts. Write one sentence explaining whether control A.7.2.3 — Disciplinary process (HR controls for information security policy violations) would likely appear as "selected and implemented" or "excluded" in PHP's SoA, and why.

---

## Exercise 3: SOC 2 Evidence Mapping (25 points)

PHP's SOC 2 Type II audit covers the Security criterion. The auditor has requested evidence for the following five control activities. For each activity, identify the ITSM practice that generates the evidence and describe what specific documentation or system record would satisfy the auditor's request.

**Control Activity 1:** Evidence that all changes to production systems are authorized before implementation.

- ITSM practice that generates evidence: _______________
- Specific evidence document or record: _______________

**Control Activity 2:** Evidence that access to the claims processing system is reviewed regularly and revoked for users who no longer require it.

- ITSM practice that generates evidence: _______________
- Specific evidence document or record: _______________

**Control Activity 3:** Evidence that security incidents are detected, logged, and responded to within defined timeframes.

- ITSM practice that generates evidence: _______________
- Specific evidence document or record: _______________

**Control Activity 4:** Evidence that software deployed to production has been tested and approved before release.

- ITSM practice that generates evidence: _______________
- Specific evidence document or record: _______________

**Control Activity 5:** Evidence that the organization maintains an inventory of systems that process member PHI.

- ITSM practice that generates evidence: _______________
- Specific evidence document or record: _______________

After completing the mapping table, write a 75–100 word paragraph explaining why SOC 2 Type II is more valuable to PHP's enterprise clients than SOC 2 Type I. Reference the distinction between design adequacy and operating effectiveness.

---

## Exercise 4: Compliance Dashboard Design (25 points)

PHP's CISO has asked you to design a compliance dashboard for the IT leadership team. The dashboard must serve three audiences: the CISO (strategic overview), the IT Operations Manager (tactical control status), and the external auditor during audit preparation.

### Task 4a: Dashboard metrics

Identify six metrics the dashboard should display. For each metric, specify:

- Metric name
- What it measures
- Which audience it primarily serves (CISO, Operations, Auditor)
- How it would be visualized (percentage, count, traffic-light status, trend chart, etc.)

Present your answer as a table with those four columns.

### Task 4b: Dashboard layout description

Write a 150–200 word description of how you would organize the dashboard visually. Address:

- What appears in the top-level summary section (for the CISO audience)
- What drill-down detail is available (for the Operations Manager)
- What evidence summary section supports the auditor
- How open risks and open audit findings would be surfaced

### Task 4c: Risk register integration

The compliance dashboard should link to PHP's risk register. Write 75–100 words describing how the dashboard would display the five risks from Exercise 1 — specifically how it would show risk status, response progress, and residual risk in a way that gives the CISO actionable visibility without requiring them to read the full register.

---

## Submission

Submit your completed lab document to the Canvas assignment portal by the due date. All four exercises must be substantively completed. Tables must be filled in with specific content, not placeholder text. Written responses must demonstrate understanding of risk and compliance concepts, not just restate the scenario.

**Grading:** Each exercise is worth 25 points distributed across tasks based on completeness, accuracy, and quality of reasoning.
