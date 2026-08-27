# Lab Activity: Module 02 - Threat Intelligence and MITRE ATT&CK Mapping

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will apply MITRE ATT&CK and Cyber Threat Intelligence concepts to realistic attack scenarios. You will map observed attacker behaviors to ATT&CK tactics and techniques, assess intelligence using the TLP framework, and build an initial detection recommendation. All data is provided within this document. This is an educational simulation conducted in an authorized learning environment.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 02 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Map a described attack behavior to the correct ATT&CK tactic and technique
- Identify ATT&CK sub-techniques using decimal notation
- Evaluate intelligence source quality and apply TLP markings appropriately
- Recommend detection rules based on ATT&CK technique knowledge
- Compare Kill Chain phase mapping to ATT&CK tactic mapping for the same event

---

## Required Reference

Keep the Module 02 Reading Guide open during this lab. You will need Section 2.3 (the 14 tactics table) and Section 2.4 (the high-frequency technique table) to complete the mapping exercises.

---

## Exercise 1: ATT&CK Scenario Mapping (50 points)

### Exercise 1 Scenario — Operation SilentRoute

The following is a condensed incident narrative based on a generic multi-stage intrusion. Your task is to map each numbered behavioral observation to the correct ATT&CK tactic and, where applicable, a specific technique or sub-technique from the Reading Guide or your knowledge of the ATT&CK Enterprise matrix.

### Incident Narrative

A financial services company experienced a targeted intrusion over a six-day period. The following behaviors were observed and logged:

Day 1, 09:14 UTC — A company HR recruiter received an email appearing to come from a job candidate. The email contained a Word document titled "Resume_JohnSmith.docx" attached directly to the message. The recruiter opened the document.

Day 1, 09:15 UTC — The Word document executed an embedded macro. The macro used Windows PowerShell to download a secondary payload from an external URL and write it to `C:\Users\Public\svchost32.exe`.

Day 1, 09:16 UTC — The downloaded file `svchost32.exe` was executed by the macro. The file established an outbound HTTPS connection to 185.220.101.47 on port 443.

Day 1, 09:22 UTC — A new scheduled task named `MicrosoftEdgeUpdateCore` was created in the Windows Task Scheduler, configured to execute `C:\Users\Public\svchost32.exe` every 30 minutes.

Day 1, 10:05 UTC — From the HR recruiter's workstation, a series of Windows commands were executed: `whoami`, `ipconfig /all`, `net user`, `net localgroup administrators`, and `arp -a`.

Day 2, 14:30 UTC — The attacker used the C2 connection to attempt disabling Windows Defender using PowerShell: `Set-MpPreference -DisableRealtimeMonitoring $true`.

Day 3, 08:45 UTC — The attacker executed `mimikatz` on the compromised workstation and successfully extracted NTLM password hashes from LSASS memory.

Day 3, 09:12 UTC — Using the extracted credentials, the attacker authenticated via Remote Desktop Protocol (RDP) to an internal server at 10.0.5.15 from the compromised workstation.

Day 4, 11:00 UTC — On the internal server, the attacker ran a directory traversal query and identified a shared folder containing financial transaction records.

Day 4, 11:30 UTC — The attacker compressed the financial records into a ZIP archive named `update_pkg.zip`.

Day 5, 02:00 UTC — The ZIP archive was transferred to 185.220.101.47 via the existing HTTPS C2 connection.

Day 6, 07:00 UTC — The attacker executed a PowerShell command that deleted all Volume Shadow Copies on both the recruiter's workstation and the internal server: `vssadmin delete shadows /all /quiet`.

### Mapping Table

For each observation below, identify the ATT&CK tactic and the most specific technique or sub-technique available. Use the technique ID (e.g., T1566.001) where possible. If the Reading Guide does not list the specific technique, use the best-matching tactic and a brief technique description.

| Obs # | Behavior Described | ATT&CK Tactic | Technique ID and Name | Justification |
|---|---|---|---|---|
| 1 | Targeted email with malicious Word document attachment delivered to recruiter | | | |
| 2 | Macro executed PowerShell to download and write secondary payload to disk | | | |
| 3 | Secondary payload established outbound HTTPS connection to external IP | | | |
| 4 | Scheduled task created to re-execute payload every 30 minutes | | | |
| 5 | Attacker ran whoami, ipconfig, net user, net localgroup, arp | | | |
| 6 | PowerShell command used to disable Windows Defender real-time monitoring | | | |
| 7 | Mimikatz extracted NTLM hashes from LSASS memory | | | |
| 8 | Attacker used extracted credentials to RDP to internal server | | | |
| 9 | Attacker queried shared folder for financial records | | | |
| 10 | Financial records compressed into ZIP archive | | | |
| 11 | ZIP archive transferred to attacker-controlled IP via C2 channel | | | |
| 12 | Volume Shadow Copies deleted from both systems | | | |

Scoring: 4 points per row — 1 for tactic, 2 for technique ID and name, 1 for justification. Total: 48 points.

### Kill Chain Comparison (2 points)

Select any two of the 12 observations above and map each to its corresponding Cyber Kill Chain phase (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives). For each, explain in one sentence how the Kill Chain phase maps to the ATT&CK tactic you identified.

---

## Exercise 2: Intelligence Assessment (25 points)

### Exercise 2 Overview

You have received the following four intelligence items from different sources. For each item, perform the tasks described below.

### Intelligence Item 2-A

Source: Public security vendor blog post published yesterday
Content: Analysis of a new ransomware family targeting manufacturing companies. Includes SHA-256 hashes of malware samples, C2 domain names, and behavioral analysis mapped to ATT&CK techniques T1486 and T1490.
TLP Marking: TLP:CLEAR

### Intelligence Item 2-B

Source: A peer analyst at a partner financial institution who called you directly
Content: A list of 15 IP addresses observed in an active campaign against financial sector targets in the last 48 hours. The peer says: "Do not share this beyond your team — we haven't disclosed this to our leadership yet."
TLP Marking: No TLP marking provided

### Intelligence Item 2-C

Source: CISA advisory AA24-001A published on cisa.gov
Content: Advisory warning of active exploitation of CVE-2024-12345 in VPN appliances. Includes IOCs and recommended mitigations. Marked TLP:CLEAR.
TLP Marking: TLP:CLEAR

### Intelligence Item 2-D

Source: A colleague forwarded an email they received from an anonymous sender claiming to work inside a threat actor organization. The email claims to contain advance knowledge of planned attacks on energy sector targets next month.
TLP Marking: None

### Task 2A — Intelligence Classification (12 points)

For each intelligence item (A through D), answer the following three questions (1 point each, 3 points per item):

1. What intelligence type is this — Strategic, Operational, or Tactical?
2. Who is the appropriate audience for this intelligence in a SOC?
3. What is the appropriate TLP marking that should be applied or confirmed before distributing this intelligence internally?

### Task 2B — Source Reliability Assessment (8 points)

For each intelligence item (A through D), rate the source reliability on a scale of High, Medium, or Low. In 2-3 sentences per item, explain your rating. Consider factors such as: Is the source authoritative? Is it verifiable? Is the content attributed to a named, accountable organization? Is it corroborated by other sources?

### Task 2C — Operational Action (5 points)

Choose the two intelligence items you rated as highest reliability. For each, describe in 3-4 sentences what specific operational action your SOC should take within the next 24 hours based on that intelligence. Be specific — name the log source, the type of rule you would write, or the block action you would implement.

---

## Exercise 3: Detection Recommendation (25 points)

### Exercise 3 Overview

Using the ATT&CK mappings you developed in Exercise 1, you will now build detection recommendations for three of the twelve observed behaviors.

Select observations 4, 7, and 12 from Exercise 1 (Scheduled Task creation, LSASS Memory dump, and Volume Shadow Copy deletion).

### Task 3A — Detection Logic (15 points)

For each of the three selected observations, complete the following template (5 points per observation):

```text
DETECTION RECOMMENDATION
ATT&CK Technique:   [Technique ID and Name]
Tactic:             [Tactic Name]
Log Source Required: [e.g., Windows Event Log, Sysmon, EDR telemetry]
Event ID or Signal: [e.g., Event ID 4698, Sysmon Event ID 10]
Detection Logic:    [Describe in plain language what the SIEM rule should look for]
False Positive Risk: [What legitimate activity might trigger this rule?]
Tuning Suggestion:  [How would you reduce false positives?]
```

### Task 3B — Prioritization Justification (10 points)

Of the three detection recommendations you wrote, rank them 1 (highest priority) to 3 (lowest priority) in terms of the urgency to implement them. Write a 4-6 sentence justification that addresses:

- Which technique, if undetected, provides the attacker with the most durable advantage in the environment?
- Which technique, once executed, is the hardest to recover from without the detection in place?
- How does the Pyramid of Pain inform your prioritization? (Hint: consider what level each technique maps to on the Pyramid)

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1 — Mapping Table (12 rows) | 48 | 1 pt tactic, 2 pts technique ID and name, 1 pt justification per row |
| Exercise 1 — Kill Chain Comparison | 2 | Correct Kill Chain phase identification with ATT&CK tactic connection |
| Exercise 2A — Intelligence Classification | 12 | 3 pts per item: type, audience, TLP marking |
| Exercise 2B — Source Reliability Assessment | 8 | 2 pts per item: correct rating with substantive 2-3 sentence explanation |
| Exercise 2C — Operational Action | 5 | Specific, actionable steps for two items; names log source, rule type, or block action |
| Exercise 3A — Detection Recommendations | 15 | 5 pts per recommendation: all template fields complete, logic is accurate |
| Exercise 3B — Prioritization Justification | 10 | Correct ranking, Pyramid of Pain reasoning, recovery-impact analysis |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date at the top.
3. Submit to the Canvas Module 02 Lab assignment by the posted deadline.
4. Late submissions are subject to the course late policy described in the syllabus.

---

## Academic Integrity Notice

This lab contains an educational simulation of a cyber intrusion for learning purposes. All work must be your own. Do not share answers before the submission deadline. Reference the MITRE ATT&CK Enterprise Matrix at attack.mitre.org and study materials at professormesser.com and comptia.org for additional context.

---

## Part 9 — Challenge Exercise

### Challenge 1: ATT&CK Coverage Gap Analysis

You are given a simplified detection inventory. Your organization has active SIEM rules for: T1078 (Valid Accounts), T1059.001 (PowerShell), T1566.001 (Spearphishing Attachment), and T1486 (Data Encrypted for Impact). A threat intelligence report indicates a threat actor targeting your industry commonly uses: T1078, T1059.001, T1547.001 (Registry Run Keys), T1003.001 (LSASS Memory), T1071.001 (Web Protocols C2), and T1486.

1. Build a coverage table listing each of the six threat actor techniques, whether your organization has a detection, and the ATT&CK tactic each belongs to.
2. For each uncovered technique, identify the log source most likely to produce detectable evidence (e.g., Windows Security Event Log, Sysmon, network proxy logs).
3. Write a one-sentence detection hypothesis for T1003.001 in this format: "Alert when [observable event] occurs on [asset type] during [time or context condition]."
4. Explain which of the uncovered techniques poses the highest risk if undetected and justify your answer using the Pyramid of Pain.

### Challenge 2: Intelligence Product Assessment

You receive two intelligence reports about the same threat actor. Report A is a vendor blog post published 11 months ago listing 14 IP addresses and 3 file hashes. Report B is a CISA advisory published last week describing the actor's TTPs, preferred initial access methods, and targeted sectors, with ATT&CK technique mappings.

1. Classify each report by intelligence type (strategic, operational, or tactical) and justify your classification.
2. Assign a source reliability rating (A–F per NATO STANAG 2511 conventions or equivalent) to each report and explain your reasoning.
3. Identify which report provides more durable defensive value and explain why using the Pyramid of Pain framework.

### Reflection Questions

1. A colleague argues that MITRE ATT&CK and the Cyber Kill Chain accomplish the same thing and organizations only need one. Based on the differences you studied in Section 4, write a two-sentence explanation of why both frameworks provide complementary rather than redundant value.
2. In your own words, explain the intelligence lifecycle phase where an analyst's judgment matters most, and describe one way that analytical bias could negatively affect the quality of finished intelligence.
