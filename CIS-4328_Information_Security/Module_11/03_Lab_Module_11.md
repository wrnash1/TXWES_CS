# Lab: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

In this lab you will walk through an incident response simulation. You will analyze a set of pre-collected log files and system artifacts to identify indicators of compromise, document your findings in an incident timeline, apply the NIST IR lifecycle phases, and produce a structured incident report. You will also practice chain of custody documentation.

**Estimated completion time:** 90 to 120 minutes

**Tools required:** Text editor, spreadsheet application, web browser (to reference NIST SP 800-61), Notepad++ or equivalent for log viewing

---

## Learning Outcomes

By completing this lab you will be able to:

- Identify indicators of compromise from realistic log data.
- Map investigative activities to NIST SP 800-61 phases.
- Construct an incident timeline from log evidence.
- Document chain of custody for collected evidence.
- Produce a structured incident report using the standard format.

---

## Scenario

You are a security analyst at Ridgeline Financial Services, a mid-sized financial technology company. At 09:14 on a Monday morning, the HR department contacts the Security Operations Center to report that an employee's email account has been sending unusual messages to external addresses over the weekend.

You are the first analyst assigned to the incident. The following artifacts have been collected for your analysis.

---

## Artifact Set A — Email Gateway Logs (Excerpt)

```
2026-06-01 22:03:14 UTC | FROM: j.harrison@ridgeline.com | TO: dropbox-share-9921@proton.me | SUBJECT: Q2 payroll export | ATTACH: payroll_Q2_2026.xlsx | SIZE: 4.2MB
2026-06-01 22:04:30 UTC | FROM: j.harrison@ridgeline.com | TO: dropbox-share-9921@proton.me | SUBJECT: HR records June | ATTACH: employee_data_all.xlsx | SIZE: 11.7MB
2026-06-01 22:05:55 UTC | FROM: j.harrison@ridgeline.com | TO: dropbox-share-9921@proton.me | SUBJECT: Benefits vendor list | ATTACH: vendors_2026.pdf | SIZE: 890KB
2026-06-01 22:06:40 UTC | FROM: j.harrison@ridgeline.com | TO: dropbox-share-9921@proton.me | SUBJECT: Re: vendor list | ATTACH: none | SIZE: 1KB
```

---

## Artifact Set B — Active Directory Authentication Logs (Excerpt)

```
2026-06-01 20:11:05 UTC | LOGON_SUCCESS | User: j.harrison | Source IP: 92.45.17.203 | Workstation: N/A | Auth: OWA (Outlook Web Access)
2026-06-01 20:11:22 UTC | LOGON_FAILURE | User: j.harrison | Source IP: 92.45.17.203 | Reason: Bad password (attempt 1)
2026-06-01 20:11:24 UTC | LOGON_FAILURE | User: j.harrison | Source IP: 92.45.17.203 | Reason: Bad password (attempt 2)
2026-06-01 20:11:30 UTC | LOGON_SUCCESS | User: j.harrison | Source IP: 92.45.17.203 | Workstation: N/A | Auth: OWA
2026-06-01 17:43:12 UTC | LOGON_SUCCESS | User: j.harrison | Source IP: 10.0.3.45 | Workstation: WKSTN-JH-04 | Auth: Kerberos
```

Note: j.harrison's HR record lists their primary workstation as `WKSTN-JH-04`. The IP address 10.0.3.45 is an internal corporate IP. The IP address 92.45.17.203 is an external IP that geolocates to Eastern Europe.

---

## Artifact Set C — Threat Intelligence Check Results

Your threat intelligence platform returns the following for IP 92.45.17.203:

- Classification: Malicious
- First seen: 2026-04-12
- Associated campaigns: credential stuffing, business email compromise
- Reported by: 14 community threat feeds
- Related IOCs: proton.me throwaway domains used for data staging

---

## Part 1 — Detection and Analysis

### Step 1 — IOC Identification

Review Artifact Sets A, B, and C. Create a table listing every Indicator of Compromise you can identify. For each IOC, list:

- IOC type (IP address, domain, file name, behavior)
- IOC value
- Source artifact set

**Lab Question 1:** List at least six IOCs from the artifact sets. Which IOC is most significant from an attribution standpoint and why?

### Step 2 — Incident Classification

Based on your IOC analysis, classify this incident using the categories from the module: malware infection, unauthorized access, denial of service, data exfiltration, insider threat, or social engineering.

**Lab Question 2:** Is this incident best classified as unauthorized access, data exfiltration, or both? Explain your reasoning. What additional evidence would help you determine whether this was an insider threat vs. external account compromise?

### Step 3 — Timeline Construction

Using all three artifact sets, construct a chronological timeline of the incident from the earliest observable event to the last known attacker action.

Format your timeline as:

```
[Timestamp UTC] | [Event description] | [Source artifact]
```

**Lab Question 3:** Based on your timeline, how much time elapsed between the attacker's first failed login attempt and the last data exfiltration email? What does the log sequence at 20:11 suggest about the attacker's credential access method?

---

## Part 2 — Containment

### Step 1 — Containment Actions

You have confirmed this is an active incident involving unauthorized access to an email account and active data exfiltration.

**Lab Question 4:** List three specific short-term containment actions you would take immediately. For each action, state whether it is a short-term or long-term containment measure, and identify any potential side effects (e.g., business disruption, evidence loss).

### Step 2 — Containment Trade-offs

**Lab Question 5:** The HR director asks you to immediately reset j.harrison's password to stop any further access. The forensic investigator asks you to wait 30 minutes to image j.harrison's mailbox first. Describe the trade-off. What is the risk of waiting? What is the risk of acting immediately?

---

## Part 3 — Evidence Preservation and Chain of Custody

### Step 1 — Evidence List

Based on the scenario, list all digital evidence that should be collected and preserved.

**Lab Question 6:** Create an evidence inventory list. For each item, state the evidence type (email logs, authentication logs, disk image, etc.), its location (system name or service), and why it is relevant to this incident.

### Step 2 — Chain of Custody Form

Complete the following chain of custody form for one piece of evidence from your inventory. Fill in all fields with realistic, specific information based on the scenario.

```
CHAIN OF CUSTODY FORM
Evidence Tag: _______________________
Case Number: IR-2026-0601-001
Date/Time of Collection: ____________
Collected By (Name/Role): ___________
System/Location: ____________________
Description of Evidence: ____________
MD5 Hash: __________________________
SHA-256 Hash: ______________________
Storage Location: ___________________
Collected For: ______________________

Transfer Log:
From: ________ To: ________ Date/Time: ________ Purpose: ________
```

**Lab Question 7:** Why are both MD5 and SHA-256 hashes recorded rather than just one? Under what circumstances might MD5 alone be insufficient to prove integrity?

---

## Part 4 — Communication

**Lab Question 8:** Ridgeline Financial Services is subject to PCI-DSS because it processes payment card data. The exfiltrated payroll file contains employee SSNs and bank account numbers but no payment card numbers. The employee_data_all.xlsx file contents are unknown at this stage.

Based on this information, identify:

1. Which regulatory notification obligations may apply and within what timeframe.
2. Who should be notified internally in the first 60 minutes.
3. Whether law enforcement should be contacted, and what factors influence that decision.

---

## Part 5 — Lessons Learned

**Lab Question 9:** Based on the incident artifacts, identify three controls that were missing or inadequate and that would have either prevented this incident or detected it significantly earlier. For each control, specify whether it addresses the Prevention, Detection, or Containment capability gap.

**Lab Question 10:** Draft a one-paragraph executive summary for the post-incident report. The summary should be suitable for a non-technical audience (e.g., the CFO or board of directors) and cover: what happened, what data was affected, what the organization did, and what will be done to prevent recurrence.

---

## Deliverables

Submit a lab report containing:

- Answers to Lab Questions 1 through 10.
- Completed IOC table from Part 1.
- Completed incident timeline from Part 1.
- Completed chain of custody form from Part 3.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — IOC identification, classification, timeline (Questions 1–3) | 30 |
| Part 2 — Containment analysis (Questions 4–5) | 20 |
| Part 3 — Evidence and chain of custody (Questions 6–7) | 20 |
| Part 4 — Communication obligations (Question 8) | 15 |
| Part 5 — Lessons learned and executive summary (Questions 9–10) | 15 |
| **Total** | **100** |

---

*End of Lab — Module 11*
