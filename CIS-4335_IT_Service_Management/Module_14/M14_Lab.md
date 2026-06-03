# Lab: Module 14 — Risk and Compliance in IT Service Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Lab Overview

**Title:** Risk Register Construction and Compliance Gap Assessment

**Duration:** 90–120 minutes

**Format:** Individual written deliverables

**Submission:** Upload completed documents to the LMS by the module deadline.

In this lab you will build a partial risk register for a fictional organization, apply risk response strategies, map ITIL practices to compliance control evidence, and analyze a compliance gap finding.

---

## Scenario

**Organization:** Meridian Health Partners (MHP)

**Type:** Regional healthcare IT services company providing electronic health record (EHR) hosting, telehealth platform, and medical billing software to 14 independent physician practices.

**Regulatory environment:**

- HIPAA (Health Insurance Portability and Accountability Act) — protects patient health information.
- SOC 2 Type II — required by three large physician practice customers as a contract condition.
- State data breach notification law — requires notification within 72 hours of discovering a breach affecting more than 500 residents.

**Recent developments:**

- The company experienced a phishing attack last quarter. One employee clicked a malicious link; the attacker gained read access to a shared folder containing billing records for approximately 2,400 patients for 11 days before detection. A HIPAA breach notification was filed.
- A SOC 2 Type II audit is scheduled in four months.
- The IT team has identified that 23% of servers are running operating systems past their vendor end-of-support date.
- One senior database administrator (DBA) holds the master credentials and institutional knowledge for all three database systems. No cross-training has occurred.
- The telehealth platform vendor has not provided a SOC 2 report or responded to the last two security questionnaires.

---

## Part 1: Build a Risk Register (40 minutes)

Using the risk register framework from the reading guide, create complete entries for five risks identified in the scenario.

### Risk Register Template

Complete one table per risk. Use the following fields:

- **Risk ID** (assign your own numbering)
- **Risk statement** (if/then/affects format)
- **Category** (Technology, Operational, Regulatory, People, Vendor)
- **Likelihood** (1–5)
- **Impact** (1–5)
- **Risk score** (Likelihood × Impact)
- **Risk owner** (assign a realistic role title, e.g., "VP of IT Operations")
- **Existing controls** (what is already in place to manage this risk)
- **Control effectiveness** (Strong / Moderate / Weak / None)
- **Residual risk score** (your assessment after current controls)
- **Response strategy** (Avoid / Transfer / Mitigate / Accept)
- **Action plan** (at least three specific, actionable steps with owner roles and timeframes)
- **Review date** (assign a realistic future date)

### Five Risks to Document

**Risk 1:** Phishing and credential compromise (use the recent incident as context — the risk has materialized; document it as ongoing).

**Risk 2:** End-of-support operating systems creating unpatched vulnerability exposure.

**Risk 3:** Key person dependency on the senior DBA.

**Risk 4:** Third-party telehealth vendor security posture unknown.

**Risk 5:** Failure to achieve SOC 2 Type II certification, resulting in loss of three major customer contracts.

### After Completing the Five Entries

**Written response (100–150 words):** Rank your five risks by residual risk score (highest to lowest). Justify why the top-ranked risk should be the organization's first priority, and explain what a realistic 90-day remediation plan would look like for that risk.

---

## Part 2: Compliance Control Mapping (25 minutes)

MHP is preparing for its SOC 2 Type II audit. The auditors will evaluate controls against the **Security** and **Availability** Trust Services Criteria.

**Task:** For each SOC 2 control area listed below, identify which ITIL 4 practice(s) generate relevant evidence, and describe what specific evidence artifact would satisfy the auditor's request.

| SOC 2 Control Area | Relevant ITIL 4 Practice(s) | Evidence Artifact |
|---|---|---|
| Changes to production systems are authorized and documented | | |
| Incidents are logged, classified, and responded to within defined timeframes | | |
| System availability is monitored with alerting for threshold breaches | | |
| Vendor/supplier security assessments are conducted for critical third parties | | |
| Access to sensitive data is reviewed periodically and revoked upon employee termination | | |
| Disaster recovery plans are documented and tested at least annually | | |

For each row, provide:

- At least one specific ITIL practice name.
- A concrete evidence artifact (e.g., "Change request records from the ITSM platform showing CAB approval for all Normal changes, covering the 12-month audit period").

---

## Part 3: HIPAA Breach Analysis and Risk Response (25 minutes)

The phishing incident described in the scenario has been reported as a HIPAA breach. You have been asked to conduct a risk analysis for the root cause and recommend controls to prevent recurrence.

### Breach Timeline

- Day 1: Employee clicks phishing link; attacker gains access.
- Day 12: Routine access log review by a junior analyst flags unusual after-hours access patterns.
- Day 13: IT security investigates; confirms attacker had read access to a shared billing records folder.
- Day 14: Attacker access is terminated; incident declared contained.
- Day 17: HIPAA breach notification filed (11 days after breach, within the 60-day HIPAA requirement; 17 days from initial event).

**Task 3a — Root Cause Analysis:** Using the "5 Whys" technique, identify the chain of causes leading to the breach. Begin with "An attacker gained access to patient billing records" and trace back through at least five causal layers.

**Task 3b — Risk Control Recommendations:** Identify five specific controls that, if implemented, would have either prevented the breach or significantly reduced its impact or duration. For each control, specify:

- The control name.
- Whether it is a preventive, detective, or corrective control.
- How it would have affected this specific incident.
- The ITIL 4 practice most closely associated with implementing or governing this control.

**Task 3c — Residual Risk Statement:** After all five controls are implemented, write a revised risk register entry for the phishing/credential compromise risk (Risk 1 from Part 1). Has the risk score changed? Is the response strategy still Mitigate, or has it shifted?

---

## Submission Requirements

Submit one document (PDF or Word) containing:

- Part 1: Five complete risk register entries and prioritization written response.
- Part 2: Completed SOC 2 control mapping table.
- Part 3: 5 Whys analysis, five control recommendations, and revised risk entry.

**Minimum length:** 1,000 words across written sections.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Risk register quality (completeness, realism, correct response strategies) | 35 |
| Prioritization and 90-day plan reasoning | 10 |
| SOC 2 control mapping accuracy | 25 |
| Breach analysis depth and control recommendation quality | 20 |
| Professional writing and formatting | 10 |
| **Total** | **100** |

---

*End of Module 14 Lab — approximately 160 lines*
