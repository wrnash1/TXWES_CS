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

---

## Part 9 — Challenge Exercise

### Challenge 1: Advanced Incident Timeline Reconstruction and Attribution Analysis

A managed security services provider (MSSP) has been engaged to investigate a suspected breach at a manufacturing company. The company produces proprietary industrial control system (ICS) components with significant intellectual property value. The MSSP has collected the following additional artifact sets beyond those available to internal analysts.

**Artifact Set D — VPN Gateway Logs:**

```text
2026-06-15 23:04:11 UTC | VPN_AUTH_SUCCESS | User: m.chen | Source IP: 185.220.101.14 | Country: RU | MFA: bypassed (token reuse)
2026-06-15 23:07:44 UTC | VPN_AUTH_SUCCESS | User: m.chen | Source IP: 185.220.101.14 | Tunnel duration: 4h 22m
2026-06-16 03:29:55 UTC | VPN_DISCONNECT | User: m.chen | Bytes transferred: 47.3 GB outbound
```

**Artifact Set E — EDR Process Tree (from engineering workstation ENG-MC-07):**

```text
[23:08:31] explorer.exe (PID 2144)
  └── cmd.exe (PID 7822) - spawned via scheduled task
        └── powershell.exe -exec bypass -enc [base64] (PID 9103)
              └── 7z.exe a -p secret123 C:\Temp\archive.7z C:\Projects\ICS_Designs\ (PID 11204)
              └── net.exe use \\10.0.8.44\share$ /user:DOMAIN\svc_backup (PID 11398)
              └── robocopy.exe C:\Temp\ \\10.0.8.44\share$ /E (PID 11512)
```

**Artifact Set F — DNS Query Log (from ENG-MC-07):**

```text
2026-06-15 23:09:01 UTC | Query: api.github-updates.net | Response: 185.220.101.14
2026-06-15 23:09:02 UTC | Query: api.github-updates.net | Response: 185.220.101.14
[repeated 847 times at 17-second intervals over 4 hours]
```

1. Reconstruct the complete attack timeline from VPN authentication through data staging and exfiltration. For each phase of the attack, identify: the MITRE ATT&CK tactic, a specific technique name (IDs not required), the artifact that provides evidence, and the defender action that could have interrupted the attack at that phase.

2. The VPN log shows `MFA: bypassed (token reuse)`. Research and explain the specific MFA attack technique this represents, describe how it works mechanically, and identify which MFA authenticator type is immune to this attack and why.

3. Artifact Set F shows 847 DNS queries to the same IP at 17-second intervals over four hours. Name this activity, explain its purpose in the attack chain, and describe two network-level detective controls that would have generated alerts on this pattern. For each control, specify what threshold or signature would trigger the alert.

4. The manufacturing company wants to assess whether this incident constitutes a reportable breach under the NIST Cybersecurity Framework and any applicable US federal law. The stolen data includes blueprints for ICS components used in US power grid infrastructure. Identify: the specific federal regulation or executive order that applies to ICS/critical infrastructure data, the reporting obligation and timeline, and the government agency that must be notified.

### Challenge 2: IR Plan Development and Tabletop Exercise Design

A regional hospital network with three campuses has no formal IR plan. They have experienced two incidents in the past year: a phishing-based compromise of a radiology technician's account and a ransomware attack that encrypted a file server containing non-PHI administrative documents. Neither incident was handled with a documented procedure — the IT team responded informally.

1. Design a complete IR plan framework for this hospital network. Your framework must address all four NIST SP 800-61 phases and include: for Preparation — the minimum viable IR team roles (list six roles with a one-sentence description of each), the three most critical tools that must be in the jump kit, and the two external relationships that must be established before an incident; for Detection and Analysis — the three log sources that must be aggregated into a SIEM for healthcare environments and a classification matrix with at least four incident categories and their corresponding severity levels; for Containment/Eradication/Recovery — the specific authority levels required to approve network isolation of a clinical system, and the backup verification requirement before any clinical system is restored; for Post-Incident Activity — the minimum content requirements for the post-incident report.

2. Design a one-hour tabletop exercise for this hospital's IR team based on the following scenario: At 2:00 AM on a Saturday, the hospital's on-call IT technician receives automated alerts that all workstations on the nursing floors are displaying ransom notes. The hospital's EHR system appears unaffected. The technician is the only IT staff member available. Design the exercise with: an opening scenario inject, four sequential decision points spaced 10 minutes apart (each inject should escalate the scenario), a debrief question for each decision point that reveals a gap in the current (nonexistent) IR plan, and a list of five specific gaps the exercise is designed to surface.

3. After the tabletop exercise, the hospital's CISO asks you to prioritize the five gaps identified. Create a risk-tiered remediation roadmap organizing the five gaps into three tiers (immediate — 0 to 30 days, short-term — 30 to 90 days, long-term — 90 to 180 days). For each gap, specify: the specific IR plan artifact or process that addresses it, the HIPAA Security Rule section that requires it, and the estimated staff effort to implement.

4. The hospital's legal counsel asks whether the ransomware incident from last year required HIPAA breach notification. The encrypted file server contained only administrative files (budget spreadsheets, vendor contracts, HR schedules) — no PHI. Apply HIPAA's breach notification risk assessment framework (the four-factor test) to determine whether notification was required, and explain what additional investigation the hospital should have conducted at the time to document the risk assessment.

### Reflection Questions

1. After completing both challenges, explain why dwell time — the period between initial compromise and detection — is the single most impactful metric for determining the severity of a security breach outcome. Use the manufacturing company incident from Challenge 1 to illustrate: what additional harm occurred during the 4+ hours of undetected access that would not have occurred if detection happened within 15 minutes, and identify the two specific detective controls whose absence most directly contributed to the extended dwell time.

2. In Challenge 2, you designed an IR plan for a hospital with no formal procedures. A board member argues that paying for an IR retainer with an MSSP is unnecessary because "we have IT staff who can handle incidents." Identify three specific IR capabilities that an MSSP retainer provides that an internal IT team cannot replicate without dedicated investment, explain the concept of "IR readiness" and why it cannot be improvised during an active incident, and describe what a minimum viable IR program looks like for a 500-employee organization that cannot afford a full MSSP retainer.

---

*End of Lab — Module 11*
