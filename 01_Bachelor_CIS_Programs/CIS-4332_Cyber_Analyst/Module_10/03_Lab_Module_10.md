# Lab Activity: Module 10 — Digital Forensics: Evidence Collection and Chain of Custody

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will analyze a simulated digital forensics scenario for a compromised Windows workstation. You will apply the order of volatility to determine correct evidence collection sequence, review a chain of custody form for procedural errors, analyze provided forensic artifacts to answer investigative questions, and write a forensic evidence summary. All scenario data and artifacts are provided within this document. No forensic software is required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 10 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Apply the order of volatility to determine correct evidence collection sequence for a running system
- Identify procedural errors in a chain of custody form and explain their forensic significance
- Analyze Windows forensic artifact data to answer specific investigative questions
- Map forensic artifact findings to incident timeline events
- Write a forensic evidence summary suitable for an incident ticket and potential legal review

---

## Scenario Context

Your DFIR team has been called to investigate a compromised Windows workstation (WS-ACCOUNTING-07) at Apex Capital Partners, a financial services firm. An employee reported unusual system behavior: new browser tabs opening automatically, unusually slow system performance, and an unrecognized process in Task Manager. Your team has been asked to conduct a forensic investigation to determine what happened, what data was accessed or exfiltrated, and what persistence mechanisms the attacker established.

The workstation was still running when your team arrived. A less experienced team member had already connected a USB drive directly to the workstation to copy suspicious files — without using a write blocker. The system has not been shut down.

System details:

- Hostname: WS-ACCOUNTING-07
- OS: Windows 10 22H2
- User: jgarcia (accountant — access to client financial records)
- IP: 10.14.5.47
- Incident detection time: Tuesday 09:15 AM

---

## Scenario Artifact Package

### Artifact A: Running System State (captured via live response tools)

```text
ACTIVE NETWORK CONNECTIONS (netstat -ano output):

  TCP  10.14.5.47:49821  185.220.101.47:4444  ESTABLISHED  PID 3812
  TCP  10.14.5.47:49844  198.51.100.23:443    ESTABLISHED  PID 3812
  TCP  10.14.5.47:49201  10.14.5.1:445        CLOSE_WAIT   PID 4

RUNNING PROCESSES (tasklist, selected):

  PID 3812  svchost32.exe  C:\Users\jgarcia\AppData\Roaming\svchost32.exe
  PID 1024  WINWORD.EXE    C:\Program Files\Microsoft Office\
  PID 2188  explorer.exe
  PID 4     System

ARP CACHE (arp -a, selected):

  10.14.5.1    00-0c-29-4a-7f-2b  dynamic
  10.14.5.22   00-0c-29-bb-3e-55  dynamic  [WS-ACCOUNTING-12]
  10.14.5.100  00-50-56-c0-00-01  dynamic  [DC-APEX-01]
```

### Artifact B: Windows Event Log Excerpts (Security.evtx)

```text
Event ID: 4688 (Process Creation)
  Time:    Tuesday 07:42:18 AM
  Account: jgarcia
  Process: C:\Users\jgarcia\AppData\Roaming\svchost32.exe
  Parent:  C:\Program Files\Microsoft Office\WINWORD.EXE
  CommandLine: svchost32.exe -c C:\Users\jgarcia\AppData\Roaming\cfg.dat

Event ID: 4720 (User Account Created)
  Time:    Tuesday 07:48:33 AM
  Account: SYSTEM
  New Account: apexsvc
  Target Domain: WS-ACCOUNTING-07

Event ID: 4732 (Member Added to Group)
  Time:    Tuesday 07:48:35 AM
  Account: SYSTEM
  Member: apexsvc
  Group: Administrators

Event ID: 4624 (Successful Logon)
  Time:    Tuesday 08:02:44 AM
  Account: apexsvc
  Logon Type: 3 (Network)
  Source IP: 10.14.5.47
  Destination: DC-APEX-01 (10.14.5.100)

Event ID: 4648 (Explicit Credential Logon)
  Time:    Tuesday 08:12:02 AM
  Account: jgarcia
  Target Account: APEX\domain_admin_backup
  Target Host: DC-APEX-01
```

### Artifact C: File System Artifacts

```text
PREFETCH FILES (C:\Windows\Prefetch\):

  SVCHOST32.EXE-A3F4B2C1.pf  Created: Tuesday 07:42:15 AM
  CERTUTIL.EXE-B5C6D7E8.pf   Created: Tuesday 07:43:02 AM
  NET.EXE-C9D0E1F2.pf         Created: Tuesday 07:48:28 AM
  PROCDUMP.EXE-D3E4F5A6.pf    Created: Tuesday 07:55:14 AM
  ROBOCOPY.EXE-E7F8A9B0.pf    Created: Tuesday 08:08:22 AM

RECENTLY DELETED FILES (recovered from $MFT unallocated entries):

  C:\Users\jgarcia\AppData\Local\Temp\dump.bin   Deleted: Tuesday 07:56:08 AM
                                                  Size: 62,447,104 bytes
  C:\Users\jgarcia\AppData\Local\Temp\data.zip   Deleted: Tuesday 08:15:33 AM
                                                  Size: 187,334,222 bytes

REGISTRY RUN KEY:
  HKCU\Software\Microsoft\Windows\CurrentVersion\Run\MicrosoftSvcUpdate
  Value: C:\Users\jgarcia\AppData\Roaming\svchost32.exe -c C:\Users\jgarcia\AppData\Roaming\cfg.dat
```

### Artifact D: Chain of Custody Form (submitted by first responder)

```text
CHAIN OF CUSTODY FORM
Evidence Item:  WS-ACCOUNTING-07 — USB collection drive
Date Collected: Tuesday
Collected By:   [illegible signature]
Hash of Collection: Not recorded
Storage Location: Left on analyst desk in open office area

TRANSFER LOG:
  Transfer 1:
    From: First Responder
    To: DFIR Lead
    Date/Time: [blank]
    Reason: Hand-off for analysis
    Signatures: First Responder signed / DFIR Lead — not signed

  Transfer 2:
    From: DFIR Lead
    To: External Forensic Consultant
    Date/Time: Wednesday 10:00 AM
    Reason: Expert analysis
    Signatures: Both signed

ANALYSIS LOG:
  Analyst: DFIR Lead
  Date: Tuesday
  Actions: Copied files from collection drive to analysis laptop
  Hash Verification: Not performed
  Note: Analyzed original USB drive directly (not a forensic copy)
```

---

## Exercise 1: Order of Volatility and Collection Sequence (25 points)

### Task 1A — Correct Collection Sequence (15 points)

Given that WS-ACCOUNTING-07 was still running when your team arrived, describe the correct order of evidence collection. For each step in your sequence:

1. Identify the evidence source
2. Explain what specific data that source contains that is relevant to this investigation
3. Identify the tool or method you would use to collect it

Your sequence must address at minimum: RAM, active network connections, running processes, and disk/file system. You must also address the problem created by the first responder's direct USB connection — what forensic contamination occurred and what can still be done to document it.

Scoring: 3 points per correctly ordered evidence source with tool identified (up to 5 sources = 15 points).

### Task 1B — Contamination Assessment (10 points)

The first responder connected a USB drive directly to WS-ACCOUNTING-07 without a write blocker. In 4-5 sentences, address:

1. What specific changes to WS-ACCOUNTING-07's file system occurred when the USB drive was connected, even before any files were copied
2. Whether WS-ACCOUNTING-07's disk image can still be used as forensic evidence given the contamination — and what documentation must accompany it to explain the contamination
3. What the correct procedure should have been and why hardware write blockers are preferred over software

---

## Exercise 2: Chain of Custody Review (25 points)

### Task 2A — Error Identification (15 points)

Review Artifact D (Chain of Custody Form). Identify every procedural error in the chain of custody form. For each error:

1. Identify the specific field or entry that contains the error
2. Explain why the error is a problem — what forensic or legal consequence does it create?
3. Describe what the correct entry should have been

You must identify a minimum of six distinct errors. Scoring: 2 points per correctly identified and explained error.

### Task 2B — Admissibility Assessment (10 points)

In 4-5 sentences, assess whether the evidence collected via this chain of custody would likely be admissible in a legal proceeding. Address:

1. Which specific errors are most damaging to admissibility and why
2. Whether any of the errors can be corrected retroactively and how
3. What additional documentation should be created immediately to minimize the legal risk

---

## Exercise 3: Forensic Artifact Analysis (30 points)

### Task 3A — Attack Timeline Reconstruction (20 points)

Using the artifact data from Artifacts A, B, and C, reconstruct the attack timeline in chronological order. For each event in your timeline:

1. Provide the timestamp
2. Describe what happened
3. Identify which artifact(s) support this event
4. Map the event to a MITRE ATT&CK technique (name and technique ID)

Your timeline must account for all significant events from the initial malware execution through the lateral movement attempt. You must identify a minimum of six distinct timeline events.

Scoring: 3 points per event (1 for correct timestamp + description, 1 for supporting artifact, 1 for ATT&CK technique).

### Task 3B — Artifact Questions (10 points)

Answer the following four investigative questions using the artifact data provided. Each answer must cite the specific artifact that supports it.

Question 1: What evidence indicates that credentials were harvested from the workstation? Identify the specific tool that was likely used and the artifact that reveals it was run.

Question 2: What evidence indicates lateral movement was attempted or completed to a domain controller? Name the specific event ID and logon type that demonstrates this.

Question 3: What is the estimated size of the data that was likely exfiltrated? Identify the artifact that supports this estimate and explain what the data files likely contained.

Question 4: How did the malware survive reboots? Identify the specific persistence mechanism and its exact registry path from the artifact data.

---

## Exercise 4: Forensic Evidence Summary (20 points)

### Task 4A — Forensic Evidence Summary (20 points)

Write a forensic evidence summary for WS-ACCOUNTING-07 suitable for inclusion in the incident ticket and for review by legal counsel. Your summary must include the following labeled sections:

Evidence Collected: List all evidence collected, the method of collection, and the chain of custody status of each item.

Attack Timeline: A condensed version of your timeline from Exercise 3 in prose form.

Key Findings: Three to five bullet points summarizing the most significant forensic findings (credential harvesting evidence, lateral movement, data exfiltration indicators, persistence mechanism).

ATT&CK Summary: List all technique IDs identified during the investigation with their corresponding tactic and a one-sentence description.

Chain of Custody Issues: Document the chain of custody problems identified in Exercise 2 and their potential legal impact.

Recommended Actions: List three specific recommendations — one for immediate IR action, one for evidence handling going forward, and one for detection improvement.

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Collection Sequence | 15 | Correct order with tools identified; contamination problem addressed |
| Exercise 1B — Contamination Assessment | 10 | Specific contamination changes described; admissibility addressed; correct procedure explained |
| Exercise 2A — Error Identification | 15 | Minimum 6 errors identified with consequences and correct entries |
| Exercise 2B — Admissibility Assessment | 10 | Most damaging errors identified; retroactive correction addressed |
| Exercise 3A — Attack Timeline | 20 | Minimum 6 events with timestamps, supporting artifacts, and ATT&CK technique IDs |
| Exercise 3B — Artifact Questions | 10 | All 4 questions answered with specific artifact citations |
| Exercise 4A — Evidence Summary | 20 | All six sections present; chain of custody issues documented; ATT&CK summary complete |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present the attack timeline as a formatted table or numbered chronological list.
4. Submit to the Canvas Module 10 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All scenario data and artifact content in this lab is fabricated for educational purposes. All work must be your own. Reference professormesser.com and comptia.org for additional study context.

---

## Part 9 — Challenge Exercise

### Challenge 1: Order of Volatility Decision Under Time Pressure

You arrive on-scene at a compromised Windows workstation at 09:47 AM. The system is powered on and logged in. The user is present and reports seeing the screen "flicker" and an unknown window open briefly 20 minutes ago. A USB thumb drive of unknown ownership is plugged in. No forensic tools are pre-staged on the workstation.

1. List the first six evidence collection actions in the correct order of volatility, specifying the tool you would use for each step (e.g., `winpmem` for RAM, `FTK Imager` for disk) and estimating the time requirement for each step.
2. The user asks if they should restart the computer because it "might clear the virus." Write a one-paragraph response explaining why restarting is contraindicated at this stage and what evidence would be permanently lost.
3. The USB drive is of unknown provenance. Describe the forensic handling procedure for the USB drive — including whether to remove it, when, and what documentation is required.
4. You discover the workstation lacks any pre-installed forensic tools and the organization's forensic kit is 45 minutes away. Identify two built-in Windows tools that can be used for initial volatile data capture and describe what data each captures.

### Challenge 2: Chain of Custody Challenge

During evidence handling for this investigation, the following events occurred: (1) RAM image was collected to the examiner's personal external hard drive rather than evidence media; (2) the examiner emailed the SHA-256 hash of the disk image to the case manager without recording it in the evidence log first; (3) a second analyst accessed the original RAM image file to run a Volatility analysis without documenting the access; (4) the USB drive was placed in a standard zip-lock bag rather than an anti-static evidence bag.

1. For each of the four chain of custody failures, identify the specific issue, explain the legal or investigative consequence, and describe the correct procedure that should have been followed.
2. Which of the four failures most seriously jeopardizes the admissibility of the evidence in a legal proceeding, and why?
3. Write a corrective chain of custody log entry for the RAM image access in event (3), filling in all required fields (date/time, accessor, action, reason, hash verification status).

### Reflection Questions

1. Explain why a forensic image (bit-for-bit copy with hash verification) is required rather than a simple file copy when collecting a disk image for investigation, and describe what a hash mismatch between the original and the copy would indicate.
2. Describe a realistic scenario where an analyst would need to choose between preserving volatile evidence and following an established IR playbook step that requires system isolation — and explain how you would resolve this conflict.
