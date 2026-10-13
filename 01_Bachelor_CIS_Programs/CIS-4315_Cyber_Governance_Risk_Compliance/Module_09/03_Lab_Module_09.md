# Lab Activity: Module 09 — Security Monitoring, Metrics, and Reporting

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Lab Overview

**Lab Title**: Building a Security Metrics Dashboard and Executive Report for Meridian Financial

**Estimated Time**: 90–120 minutes

**Format**: Individual assignment with written deliverables

**Submission**: Upload all deliverables as a single PDF or ZIP to the course LMS by the posted due date.

---

## Scenario Background

You are the newly appointed Information Security Manager at **Meridian Financial Services**, a mid-sized regional bank serving approximately 450,000 customers. Meridian processes credit card transactions and stores protected health information for its employee benefits platform, placing the organization under both PCI-DSS and HIPAA obligations.

The bank's CISO, Dana Reyes, has asked you to establish a formal security metrics and reporting program. Currently, the security team produces ad hoc reports with no consistent format, metrics are collected inconsistently, and the board has never received a structured security report. A recent internal audit cited the lack of a security monitoring framework as a significant gap.

Your task is to design the metrics framework, propose a dashboard structure, and produce an initial executive security report using the sample data provided below.

---

## Sample Data — Meridian Financial Q1 Security Snapshot

Use this data for all deliverables. Do not invent additional data unless instructed.

### Vulnerability Management

- Total vulnerabilities identified in Q1 scan: 847

- Critical severity: 23

- High severity: 104

- Critical patched within SLA (72 hours): 19 of 23 (83%)

- High patched within SLA (7 days): 71 of 104 (68%)

- Critical vulnerabilities older than 30 days: 8

- Systems scanned / total systems: 412 of 490 (84%)

### Incident Metrics

- Total security incidents Q1: 34

- Critical incidents: 2

- Mean Time to Detect (MTTD): 4.2 hours (Q4 prior year: 6.8 hours)

- Mean Time to Respond (MTTR): 9.1 hours (Q4 prior year: 14.3 hours)

- Incidents involving PHI exposure: 1 (reported to HIPAA privacy officer)

### Access Control

- Privileged accounts reviewed on schedule: 87 of 102 (85%)

- Failed access reviews resulting in deprovisioning: 13

- MFA enrollment — all employees: 94%

- Service accounts with excessive privileges: 7 (open remediation items)

### Security Awareness

- Security awareness training completion — all staff: 89%

- Phishing simulation click rate: 11% (Q4 prior year: 19%)

### Compliance Posture

- PCI-DSS controls passing: 218 of 241 (90%)

- HIPAA Security Rule controls compliant: 83 of 93 (89%)

- Open audit findings: 14 (3 critical, 6 high, 5 medium)

---

## Task 1 — Define the Metrics Framework (20 points)

Using the sample data and your knowledge of NIST SP 800-55, define a formal metrics framework for Meridian Financial.

### Task 1 Instructions

Step 1: Select exactly **six KPIs** and **four KRIs** from the sample data. For each metric, complete the table below.

Step 2: For each selected metric, justify why it meets at least three of the five NIST SP 800-55 criteria (measurable, actionable, relevant, comparable, cost-effective).

Step 3: Identify one metric from the sample data that you consider a vanity metric and explain why it fails the criteria.

### Task 1 Deliverable Template

Create a table with the following columns for each of your ten metrics:

| Metric Name | Type (KPI/KRI) | Current Value | Target | Data Source | NIST Criteria Met | Justification |
|---|---|---|---|---|---|---|
| (fill in) | | | | | | |

Your vanity metric analysis should be a short paragraph of three to five sentences.

---

## Task 2 — Design the Dashboard Structure (25 points)

Design a two-dashboard system for Meridian Financial: one executive dashboard and one operational dashboard.

### Task 2 Instructions

Step 1: For the **Executive Dashboard**, specify:

- The five metrics to display (select from your Task 1 KPIs and KRIs).

- The visualization type for each (RAG status tile, trend line, bar chart, gauge).

- The refresh frequency.

- The primary audience and what decisions the dashboard supports.

Step 2: For the **Operational SOC Dashboard**, specify:

- The six metrics to display (may include additional operational metrics not in Task 1).

- The visualization type for each.

- The refresh frequency.

- The primary audience and what decisions the dashboard supports.

Step 3: Write a brief rationale (one paragraph per dashboard, four to six sentences each) explaining your design choices and how they reflect audience-appropriate information delivery.

### Task 2 Deliverable

Two completed dashboard design tables and two rationale paragraphs. You do not need to build a functional dashboard — a design specification in table format is sufficient.

---

## Task 3 — Write the Executive Security Report (35 points)

Using the Q1 sample data and your metrics framework from Task 1, write the Q1 Executive Security Report for Meridian Financial's board of directors.

### Task 3 Instructions

Your report must follow this exact structure:

**Section 1 — Executive Summary** (2–3 paragraphs): Overall security posture assessment, most significant developments in Q1, and a clear bottom-line assessment. Do not use undefined technical acronyms without providing a brief definition.

**Section 2 — Metrics Scorecard**: A table containing all ten metrics from Task 1 with current value, target, trend direction (up/down/stable), and RAG status. Include a brief narrative sentence below the table explaining the overall scorecard picture.

**Section 3 — Risk Register Summary**: Identify the top four risks suggested by the Q1 data. For each risk, provide: risk description, current risk rating (High/Medium/Low), remediation status, and recommended action.

**Section 4 — Program Highlights and Actions Required**: List three highlights (improvements made in Q1) and two explicit asks requiring board action (frame these as decisions the board must make, not tasks for the security team).

### Task 3 Quality Criteria

- Written in plain business language, accessible to a non-technical board audience.

- Every technical term defined on first use.

- Risk framed in business terms (regulatory exposure, financial impact, reputational risk).

- Explicit, specific recommendations — not vague suggestions.

---

## Task 4 — SIEM Correlation Rule Design (20 points)

Meridian Financial is deploying a new enterprise SIEM. You are responsible for the initial correlation rule set.

### Task 4 Instructions

Step 1: Using the incident and access control data from the Q1 snapshot, identify **three threat scenarios** that Meridian Financial should prioritize for SIEM detection.

Step 2: For each threat scenario, design a SIEM correlation rule using the template below.

Step 3: For each rule, explain how alert fatigue could affect this rule and describe one tuning action you would take within the first 90 days of deployment.

### Task 4 Deliverable Template

For each of three correlation rules:

| Field | Value |
|---|---|
| Rule Name | |
| Threat Scenario | |
| Data Sources Required | |
| Event Pattern (describe in plain language) | |
| Time Window | |
| Threshold | |
| Alert Severity | |
| Recommended Response | |
| Alert Fatigue Risk | |
| Tuning Action | |

---

## Grading Rubric

| Deliverable | Points | Criteria |
|---|---|---|
| Task 1 — Metrics Framework | 20 | 6 KPIs and 4 KRIs correctly identified; NIST criteria applied accurately; vanity metric analysis is correct and well-reasoned |
| Task 2 — Dashboard Design | 25 | Both dashboards designed with appropriate metrics for each audience; visualization types appropriate; rationale demonstrates understanding of audience-appropriate reporting |
| Task 3 — Executive Report | 35 | All four sections present and complete; plain language throughout; risks framed in business terms; explicit board asks included; professional quality |
| Task 4 — SIEM Rules | 20 | Three threat scenarios relevant to Meridian's risk profile; correlation rule logic is sound; alert fatigue analysis is realistic; tuning actions are specific |
| **Total** | **100** | |

### Grading Notes

- Points are deducted for undefined technical acronyms in the executive report (2 points per instance).

- Deliverables submitted as separate files rather than a single organized document lose 5 points.

- Reports that use bullet points in place of required paragraphs in Tasks 3 and 4 rationale sections lose up to 10 points.

---

## Submission Checklist

Before submitting, verify:

- [ ] Task 1 table includes exactly 6 KPIs and 4 KRIs with all columns completed.

- [ ] Task 1 vanity metric paragraph is present.

- [ ] Task 2 includes two dashboard design tables and two rationale paragraphs.

- [ ] Task 3 Executive Report contains all four sections in correct order.

- [ ] Task 3 Executive Summary contains 2–3 paragraphs with no undefined acronyms.

- [ ] Task 3 Metrics Scorecard table is complete with trend and RAG status.

- [ ] Task 3 Risk Register covers four risks with all columns completed.

- [ ] Task 3 Program Highlights includes three highlights and two board asks.

- [ ] Task 4 includes three completed correlation rule tables.

- [ ] Task 4 includes alert fatigue analysis and tuning action for each rule.

- [ ] All deliverables compiled in a single PDF or ZIP file.

---

## Learning Connection

This lab directly applies CISM Domain 3 competencies. The metrics framework you build in Task 1 mirrors the process a CISM-certified manager uses to establish a security measurement program. The executive report in Task 3 is the primary vehicle by which CISOs maintain board-level accountability for security programs. The SIEM rule design in Task 4 connects security monitoring architecture to governance requirements.

Keep your completed lab. The frameworks and templates you develop here can be adapted as study references for the CISM exam.

---

## Part 9 — Challenge Exercise

These challenges extend the Module 09 lab into advanced security monitoring and metrics scenarios. Complete both challenges and the reflection questions for up to 15 bonus points.

---

### Challenge 1: SIEM Correlation Rule Design and Tuning

Meridian Financial's SOC has deployed a new SIEM and the security engineering team must build a correlation rule library. The threat intelligence team has identified three priority detection scenarios based on recent incident data from the financial services sector.

**Scenario A — Credential Stuffing Against Online Banking Portal**: Attackers are using lists of breached credentials to attempt automated logins to customer banking accounts. Typical pattern: high volume of failed authentications from distributed IP ranges, followed by successful logins from the same IP ranges.

**Scenario B — Data Exfiltration via Cloud Storage**: Insiders and external attackers are uploading large volumes of sensitive data to personal cloud storage accounts (Google Drive, Dropbox, OneDrive) from corporate devices during or after business hours.

**Scenario C — Privileged Account Misuse**: Privileged service accounts are being used interactively (human login) rather than running only as automated processes, indicating potential credential compromise or insider misuse.

**Step 1**: For each scenario, design a SIEM correlation rule. For each rule provide: the log sources required, the detection logic (conditions that must be true to fire the alert), the time window, the severity level, and the initial response action when the alert fires.

**Step 2**: After 30 days of operation, the SOC reports the following false positive rates: Scenario A rule — 6% false positive rate; Scenario B rule — 43% false positive rate; Scenario C rule — 78% false positive rate. For rules B and C, identify the most likely sources of false positives given the scenario context and propose specific tuning changes (additional conditions, exclusion lists, threshold adjustments) to bring the false positive rate below 15% without eliminating true positive coverage.

**Step 3**: The CISO wants to add a UEBA layer to complement the SIEM rules. Explain what additional detection value UEBA would provide for each of the three scenarios that the static SIEM correlation rules cannot provide, and describe what baseline data UEBA would need for each scenario.

---

### Challenge 2: Executive Security Metrics Dashboard Redesign

Meridian Financial's board has complained that the current quarterly security report is "too technical, too long, and doesn't help us make decisions." The current report is 22 pages and includes: raw vulnerability scan output (847 rows), a list of all security incidents with technical descriptions, firewall rule change logs, and patch compliance percentages by system.

**Step 1**: Critique the current report format. Identify at least five specific reasons why the existing report fails to serve the board's governance and decision-making function, referencing the principles of effective executive security reporting from the reading guide.

**Step 2**: Design a replacement executive security dashboard using the three-layer framework (strategic/executive, tactical/management, operational/analyst). For each layer, specify: the audience, the update frequency, the format (dashboard, report, scorecard), and five specific metrics or data elements it should contain. Use the Meridian Financial scenario facts from the main lab to ensure the metrics are contextually relevant.

**Step 3**: The CFO reviews your proposed executive dashboard and asks: "How do I know if our security program is improving or getting worse?" Design a trend-based security program health scorecard with at least six metrics that, when viewed together over four quarters, would give the CFO a clear answer to this question. For each metric, specify the direction of improvement (higher is better / lower is better), the data source, and what a concerning trend would look like.

---

### Reflection Questions

Answer each reflection question in four to six sentences.

1. A security manager argues that the most important security metric is the number of incidents prevented — not incidents detected or responded to — because prevention is the primary goal of a security program. Explain why "incidents prevented" is difficult to measure reliably, what proxy metrics can be used to approximate prevention effectiveness, and what the governance risk is of building an executive dashboard primarily around prevention metrics.

2. SIEM platforms are powerful but produce significant operational complexity — requiring ongoing rule tuning, log source integration maintenance, analyst training, and false positive management. Describe the conditions under which a mid-sized organization might conclude that a managed detection and response (MDR) service is more appropriate than an internally operated SIEM, and explain what governance oversight responsibilities the organization retains even when it outsources detection and response to a third party.
