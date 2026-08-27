# Lab Activity: Module 12 — Digital Forensics and Post-Incident Analysis

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Lab Overview

In this lab you will apply digital forensics and post-incident analysis concepts to a realistic incident scenario. You will document an evidence collection process, construct a chain of custody form, perform a basic root cause analysis, and produce a structured after-action report excerpt. No specialized forensic software installation is required — this lab focuses on documentation, process, and analytical skills.

**Estimated Time:** 90–120 minutes

**Submission Format:** Single PDF or Word document containing all deliverables labeled by exercise number.

---

## Scenario — Acme Financial Services Credential Theft Incident

Acme Financial Services is a regional bank with 1,200 employees. On Monday at 9:17 AM, the IT help desk received three calls from employees unable to log in to the core banking application. The security operations team investigated and discovered that an attacker had obtained valid credentials for a privileged service account named `svc_banking_admin`. Evidence suggests the account was used to access the database server and export customer account records between 2:00 AM and 3:47 AM Sunday night.

The following systems and data sources are available for investigation.

- **WEB01** — Internet-facing web application server (Windows Server 2019, powered on)
- **DB01** — Core banking database server (Windows Server 2022, powered on)
- **IDAUTHLOG** — Identity and access management authentication logs (90-day retention, 47 GB)
- **FIREWALL-01** — Perimeter firewall with NetFlow records (30-day retention)
- **SIEM01** — Splunk SIEM with aggregated logs from all servers (12-month retention)
- **EMAIL01** — Exchange email server (Windows Server 2019, powered on)
- **WORKSTATION-112** — Laptop assigned to employee James Cortez, IT administrator (powered off, physically secured)

The CISO has confirmed that legal counsel has been notified and a legal hold is in effect covering all systems listed above and all emails related to the incident from the past 90 days.

---

## Exercise 1 — Evidence Identification and Prioritization (20 points)

### Task 1A — Evidence Source Inventory

Review the scenario and create a complete evidence source inventory table. For each evidence source, document the evidence type, volatility level, potential investigative value, and recommended collection priority (1 = highest priority).

Your table must include all seven evidence sources listed in the scenario. Use the following column headings.

| Evidence Source | Evidence Type | Volatility | Investigative Value | Collection Priority |
|---|---|---|---|---|
| (fill in for all 7 sources) | | | | |

### Task 1B — Order of Volatility Justification

Write a 150–200 word paragraph justifying your collection priority order. Your justification must reference the order of volatility principle, explain why memory-resident evidence on powered-on systems takes priority over disk-based evidence, and address what evidence would be permanently lost if WORKSTATION-112 were powered on without first capturing its current state.

### Task 1C — Legal Hold Compliance Check

Based on the scenario, identify two specific actions the security team must NOT take due to the active legal hold, and explain the legal consequence of each prohibited action. Format your response as a two-row table with columns "Prohibited Action" and "Legal Consequence."

---

## Exercise 2 — Chain of Custody Documentation (25 points)

### Task 2A — Complete the Chain of Custody Form

Using the template below, complete a chain of custody form for the acquisition of the WORKSTATION-112 hard drive. You will need to invent plausible but realistic details for fields not provided in the scenario (investigator name, badge number, storage location, etc.). All invented details must be internally consistent and realistic.

**CHAIN OF CUSTODY FORM — Evidence Record**

| Field | Value |
|---|---|
| Evidence ID | COC-2024-0617-001 |
| Incident Reference | INC-2024-0617-ACME |
| Evidence Description | (complete this) |
| Make / Model | Dell Latitude 5540 |
| Serial Number | (invent a realistic value) |
| Condition at Collection | (describe) |
| Collected By — Name | (complete this) |
| Collected By — Title | (complete this) |
| Collected By — Badge / ID | (complete this) |
| Collection Date | (complete this) |
| Collection Time | (complete this — include time zone) |
| Collection Location | (complete this) |
| System State at Collection | Powered off, screen closed, no external devices attached |
| Write Blocker Used | (yes or no — and specify device) |
| MD5 Hash of Image | (invent a realistic 32-character hex value) |
| SHA-256 Hash of Image | (invent a realistic 64-character hex value) |
| Image File Name | (invent a realistic filename) |
| Image Storage Location | (complete this) |
| Transfer 1 — From | (complete this) |
| Transfer 1 — To | (complete this) |
| Transfer 1 — Date and Time | (complete this) |
| Transfer 1 — Purpose | Forensic analysis |
| Transfer 1 — Method | (complete this) |
| Storage Facility | (complete this) |
| Access Restrictions | (complete this) |

### Task 2B — Hash Verification Memo

Write a 75–100 word internal memo from the forensic investigator to the evidence custodian confirming that the SHA-256 hash of the forensic image was verified against the original hash at the start of analysis and the hashes matched. Include the evidence ID, the hash values from your form, the date and time of verification, and a statement that the evidence is confirmed unaltered and cleared for analysis.

---

## Exercise 3 — Root Cause Analysis (25 points)

### Task 3A — Five Whys Analysis

Apply the Five Whys technique to the following problem statement derived from the scenario.

**Problem Statement:** A privileged service account was used by an unauthorized actor to export customer records from the database server, and the activity went undetected for approximately 107 minutes.

Complete the Five Whys table below. Each "Why" answer must be specific to the Acme Financial Services scenario — do not give generic answers.

| Level | Question | Answer |
|---|---|---|
| Problem | Why did this incident occur? | A privileged service account was compromised and used to export customer records undetected |
| Why 1 | Why was the attacker able to obtain valid credentials for the service account? | (your answer) |
| Why 2 | Why was [answer from Why 1] possible? | (your answer) |
| Why 3 | Why was [answer from Why 2] allowed? | (your answer) |
| Why 4 | Why was [answer from Why 3] not prevented? | (your answer) |
| Why 5 — Root Cause | Why did [answer from Why 4] exist? | (your root cause answer) |

### Task 3B — Fishbone Diagram Description

You do not need to draw a graphic fishbone diagram. Instead, write a structured list that represents the fishbone diagram content for this incident. Identify at least two contributing factors in each of the four categories: People, Process, Technology, and Policy. For each contributing factor, write one sentence explaining how it contributed to the incident.

### Task 3C — Remediation Recommendations

Based on your Five Whys root cause and fishbone contributing factors, write three specific remediation recommendations. Each recommendation must include a title, a one-paragraph description of what should be done, an assigned owner role (not a person's name), a priority level, and a target completion timeframe.

---

## Exercise 4 — After-Action Report Excerpt (30 points)

### Task 4A — Executive Summary

Write a 200–250 word executive summary for the Acme Financial Services after-action report. The executive summary must be written for a non-technical audience (board members and senior executives). It must cover the nature of the incident, the timeline at a high level, the business impact, the current status, and two key recommendations. Do not use technical jargon without brief explanation.

### Task 4B — Incident Timeline

Construct a detailed incident timeline table using the information provided in the scenario and any reasonable inferences you make. Include at least eight timeline entries. Each entry must have a timestamp (or estimated timestamp), a description of the event, the evidence source that confirms or supports the entry, and a confidence level (confirmed, probable, or estimated).

| Timestamp | Event Description | Evidence Source | Confidence |
|---|---|---|---|
| (fill in at least 8 rows) | | | |

### Task 4C — Lessons Learned Tracker

Create a lessons learned tracking table with at least four entries derived from your root cause analysis and findings. Each entry must include a unique ID, a finding description, the assigned owner role, the priority level, the target completion date, and the verification method.

| ID | Finding | Owner Role | Priority | Target Date | Verification Method |
|---|---|---|---|---|---|
| LL-001 | (complete) | | | | |
| LL-002 | (complete) | | | | |
| LL-003 | (complete) | | | | |
| LL-004 | (complete) | | | | |

---

## Deliverables Summary

Submit a single document containing all of the following items, clearly labeled.

1. Exercise 1A — Evidence Source Inventory table
2. Exercise 1B — Order of Volatility Justification paragraph
3. Exercise 1C — Legal Hold Compliance Check table
4. Exercise 2A — Completed Chain of Custody form
5. Exercise 2B — Hash Verification Memo
6. Exercise 3A — Five Whys table
7. Exercise 3B — Fishbone Diagram Description (structured list)
8. Exercise 3C — Three Remediation Recommendations
9. Exercise 4A — Executive Summary
10. Exercise 4B — Incident Timeline table
11. Exercise 4C — Lessons Learned Tracker table

---

## Grading Rubric

| Exercise | Criteria | Points |
|---|---|---|
| 1A — Evidence Inventory | All 7 sources present; volatility and priority correct | 10 |
| 1B — Volatility Justification | References order of volatility; addresses WS-112 memory risk | 5 |
| 1C — Legal Hold Compliance | Two accurate prohibited actions with correct legal consequences | 5 |
| 2A — Chain of Custody Form | All fields completed; internally consistent; write blocker noted | 15 |
| 2B — Hash Verification Memo | Professional format; correct elements; hashes consistent with form | 10 |
| 3A — Five Whys | Each level is specific and logically connected; root cause is systemic | 10 |
| 3B — Fishbone Description | Four categories; two factors each; each factor explained | 8 |
| 3C — Recommendations | Three recommendations; all required elements present; actionable | 7 |
| 4A — Executive Summary | Non-technical; 200–250 words; all required content present | 10 |
| 4B — Incident Timeline | Eight or more entries; timestamps plausible; sources cited | 10 |
| 4C — Lessons Learned Tracker | Four entries; all fields complete; verification methods specific | 10 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Forensic Readiness Gap Assessment

You have been engaged as a consultant to assess an organization's forensic readiness. The organization has 400 employees, runs a hybrid cloud environment (on-premises Windows servers plus AWS), and has experienced two security incidents in the past year where evidence was unavailable or incomplete.

1. Review the six forensic readiness requirements listed in the Module 12 Reading Guide (Section 1). For each requirement, draft a one-sentence assessment question the organization must be able to answer affirmatively to be considered ready. Then create a two-column table rating each requirement as Met, Partially Met, or Not Met, based on the following information: logging is enabled on servers but not on cloud workloads; there is no defined evidence custodian role; the IR plan references forensics but contains no evidence handling procedures; legal counsel has never been consulted about a legal hold process; one investigator attended a forensics course two years ago; physical evidence storage consists of a locked filing cabinet with no access log.
2. Identify the two highest-priority gaps from your assessment and write a one-paragraph remediation recommendation for each, including the assigned owner role and a target completion timeframe of 90 days or less.
3. Draft a one-page forensic readiness policy statement (100–150 words) that the CISO could present to the board for approval. The policy must address scope, ownership, minimum logging requirements, evidence custodian designation, and annual review frequency.
4. Estimate the cost-benefit impact of the top two gaps: for each, describe one scenario where the gap would have caused measurable harm (legal sanctions, evidence loss, regulatory penalty), and explain how remediating the gap would reduce that risk.

### Challenge 2: Anti-Forensic Technique Recognition and Documentation

During an investigation of a suspected data theft incident at a financial firm, the forensic team discovers several anomalies: the Windows Security event log on the affected server was cleared at 2:48 AM (Event ID 1102 captured in SIEM); prefetch files are absent despite the system having been running for eight months; a directory named `C:\Windows\Temp\svchost` contains files with .jpg extensions whose headers do not match JPEG format; and the suspect employee's user profile folder has a last-accessed timestamp of exactly midnight — an unlikely precision for normal user activity.

1. For each of the four anomalies, identify the anti-forensic technique being used (log clearing, prefetch disabling, steganography or extension masking, timestamp manipulation) and write two sentences explaining how each technique hinders a forensic investigation.
2. For each anomaly, identify one forensic countermeasure or investigative technique that can recover or corroborate evidence despite the anti-forensic action.
3. Document all four findings in an after-action report "Findings and Gaps" table using the format from Section 4 of the Reading Guide. Each finding must include a finding ID, description, category (People / Process / Technology / Policy), severity (Critical / High / Medium), recommended remediation, assigned owner role, and target date.
4. Write a 75–100 word recommendation to the CISO explaining why centralized, tamper-resistant logging (SIEM with immutable log storage) is the most important single control for defeating anti-forensic log clearing techniques.

### Reflection Questions

1. A forensic investigation produces a complete root cause analysis with five findings, but none of the findings are assigned to owners or given target completion dates. From a CISM governance perspective, explain why this after-action report fails its primary purpose, and describe what governance mechanism would ensure findings are tracked to closure.
2. An organization's legal counsel tells the CISO that the organization is "practically forensically ready" because it owns EnCase licenses and has a trained investigator. Based on the ISACA definition of forensic readiness covered in this module, evaluate whether this characterization is accurate and identify at least three elements of forensic readiness that tool ownership and a single trained investigator do not address.
