# Lab: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

**Title:** Memory Forensics and Log Analysis Investigation

**Duration:** Approximately 90 minutes

**Environment:** Volatility 3 (free, open source), FTK Imager Free, provided forensic artifacts, Windows or Linux

**Skill Level:** Intermediate — requires completion of Module 12 video lectures and Reading Guide

---

## Objectives

Upon completing this lab, you will be able to:

1. Install and run Volatility 3 to analyze a memory image
2. Use Volatility plugins to identify running processes, network connections, and suspicious code injection
3. Analyze a simulated Windows Event Log export to identify attacker activity
4. Complete a chain of custody form for collected evidence
5. Interpret web server log entries to identify attack attempts
6. Produce a brief forensic findings report documenting discovered artifacts

---

## Prerequisites

- Python 3.6+ installed ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- Volatility 3 installed (instructions below)
- FTK Imager Free (optional — installation instructions included)
- Internet connection for downloading tools and sample files

---

## Part 1 — Environment Setup (15 minutes)

### Step 1.1 — Install Volatility 3

Volatility 3 is a Python-based memory forensics framework. Install it via pip:

```bash
pip install volatility3
```

Or install from source:

```bash
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip install -r requirements.txt
```

Verify installation:

```bash
python vol.py --help
```

### Step 1.2 — Download the Lab Memory Image

Download the sample Windows memory image used for this lab:

**Memory image:** A sample infected Windows 7 SP1 memory image from the Volatility Foundation's test suite is available at:

[https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples](https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples)

Download: `cridex.vmem` — a Windows XP memory image captured during a Cridex malware infection (classic teaching sample).

If the above link is unavailable, the instructor will provide an alternative link on the course LMS.

**File size:** approximately 128 MB

Note the MD5 hash of the file you download for the chain of custody entry in Part 3.

### Step 1.3 — (Optional) Install FTK Imager Free

FTK Imager is available free from Exterro/AccessData:

[https://www.exterro.com/digital-forensics-software/ftk-imager](https://www.exterro.com/digital-forensics-software/ftk-imager)

This is optional for this lab (the memory image is pre-provided) but you should install it to familiarize yourself with the tool for the Reading Guide review questions.

---

## Part 2 — Memory Forensics with Volatility (35 minutes)

All commands below use Volatility 3 syntax. Run them from the directory containing `vol.py` (or `volatility3/vol.py`). Replace `cridex.vmem` with the path to your downloaded memory image.

### Step 2.1 — Identify the OS Profile

```bash
python vol.py -f cridex.vmem windows.info
```

Record in your lab notes:

- Operating system version
- Architecture (32-bit or 64-bit)
- System time when memory was captured

### Step 2.2 — List Running Processes

```bash
python vol.py -f cridex.vmem windows.pslist
```

Review the output. Look for:

- Processes with unusual parent/child relationships (e.g., `explorer.exe` spawning `cmd.exe`)
- Processes with suspicious names or numbers of instances
- System processes running from unusual paths

Record in your lab notes: List any processes you find suspicious and explain why.

```bash
python vol.py -f cridex.vmem windows.pstree
```

The pstree plugin shows processes in a hierarchical tree by parent-child relationship. This makes it easier to identify injected processes or unusual execution chains.

**Lab Reflection Question 1:** Describe what you observe in the process tree. Are there any parent-child relationships that seem abnormal? What would a normal Windows XP process tree look like for `explorer.exe`?

### Step 2.3 — Network Connections

```bash
python vol.py -f cridex.vmem windows.netscan
```

Review the output for:

- Established connections to external IP addresses
- Listening ports on unusual port numbers
- Connections to port 80/443 from processes that should not make web connections

Record in your lab notes:

- All external IP addresses in the connection list
- The process names associated with suspicious connections

**Lab Reflection Question 2:** Do any network connections appear suspicious? Research the destination IP addresses using a public WHOIS service (such as arin.net for IP lookups). What do you find? (Note: for this lab, the IPs in the cridex sample are documented; the purpose is practicing the investigative methodology.)

### Step 2.4 — Detecting Code Injection with malfind

```bash
python vol.py -f cridex.vmem windows.malfind
```

The malfind plugin identifies memory regions that are:

- Marked as executable
- Not backed by a file on disk
- Contain MZ headers (executable code)

These characteristics are indicators of code injection or process hollowing — techniques used by malware to hide in legitimate processes.

Record in your lab notes:

- How many suspicious memory regions were found
- Which processes contain the flagged memory regions
- The hex dump shown for each finding — what does the `MZ` marker indicate?

**Lab Reflection Question 3:** Explain what code injection is and why a legitimate process having executable memory not backed by a file on disk is suspicious. How does this relate to fileless malware concepts from the lecture?

### Step 2.5 — DLL and Command Line Analysis

Run the following to gather additional context:

```bash
python vol.py -f cridex.vmem windows.cmdline
python vol.py -f cridex.vmem windows.dlllist --pid [PID of suspicious process]
```

Replace `[PID]` with the process ID of any suspicious process found in Step 2.2 or 2.4.

Record in your lab notes: Any unusual DLLs loaded by suspicious processes, or suspicious command-line arguments.

---

## Part 3 — Chain of Custody Documentation (10 minutes)

Complete the following chain of custody form for the memory image you analyzed. Use the actual filename and hash of your downloaded file.

### Evidence Chain of Custody Form

| Field | Value |
|---|---|
| Evidence ID | LAB12-MEM-001 |
| Evidence Type | RAM Memory Image |
| File Name | |
| File Size | |
| MD5 Hash (record actual hash) | |
| SHA-256 Hash (record actual hash) | |
| Source / Origin | Downloaded from Volatility Foundation GitHub |
| Date/Time Obtained | |
| Obtained by (your full name) | |
| Storage Location | |
| Analysis Performed By | |
| Analysis Date | |
| Notes | |

To calculate the hash on Windows:

```powershell
Get-FileHash cridex.vmem -Algorithm MD5
Get-FileHash cridex.vmem -Algorithm SHA256
```

To calculate on Linux/macOS:

```bash
md5sum cridex.vmem
sha256sum cridex.vmem
```

---

## Part 4 — Windows Event Log Analysis (15 minutes)

The following is a simulated excerpt from a Windows Security Event Log export. Analyze it as if you were investigating a suspected intrusion.

```
Date: 2024-11-15 02:17:44
EventID: 4624
Account: Administrator
Logon Type: 3 (Network)
Source IP: 185.220.101.45
Workstation: FINANCE-PC-04

Date: 2024-11-15 02:18:02
EventID: 4688
Process: cmd.exe
Parent Process: services.exe
Command Line: cmd.exe /c whoami

Date: 2024-11-15 02:18:15
EventID: 4688
Process: net.exe
Parent Process: cmd.exe
Command Line: net user hacker P@ssw0rd123 /add

Date: 2024-11-15 02:18:16
EventID: 4720
Account Created: hacker
Created By: Administrator

Date: 2024-11-15 02:18:17
EventID: 4688
Process: net.exe
Parent Process: cmd.exe
Command Line: net localgroup administrators hacker /add

Date: 2024-11-15 02:19:34
EventID: 4688
Process: mimikatz.exe
Parent Process: cmd.exe
Command Line: mimikatz.exe privilege::debug sekurlsa::logonpasswords

Date: 2024-11-15 02:21:55
EventID: 7045
Service Name: WindowsUpdater
Service File: C:\Windows\Temp\svchost32.exe

Date: 2024-11-15 02:22:01
EventID: 1102
Log: Security
Cleared By: Administrator
```

**Task 4.1 — Event Log Analysis Table**

Complete the table for each log entry:

| Timestamp | Event ID | What Happened | Why It Is Significant | MITRE ATT&CK Technique (research or guess) |
|---|---|---|---|---|
| 02:17:44 | 4624 | | | |
| 02:18:02 | 4688 | | | |
| 02:18:15 | 4688 | | | |
| 02:18:16 | 4720 | | | |
| 02:18:17 | 4688 | | | |
| 02:19:34 | 4688 | | | |
| 02:21:55 | 7045 | | | |
| 02:22:01 | 1102 | | | |

**Lab Reflection Question 4:** Write a narrative attack timeline (five to eight sentences) describing what the attacker did on FINANCE-PC-04 from 02:17 to 02:22. Identify which specific actions were most damaging and explain why.

---

## Part 5 — Web Server Log Analysis (15 minutes)

Analyze the following Apache web server log excerpt:

```
192.168.1.105 - - [15/Nov/2024:09:01:22] "GET /search?q=test HTTP/1.1" 200 4523
192.168.1.105 - - [15/Nov/2024:09:01:45] "GET /search?q=test' HTTP/1.1" 200 4523
192.168.1.105 - - [15/Nov/2024:09:01:47] "GET /search?q=test'-- HTTP/1.1" 500 892
192.168.1.105 - - [15/Nov/2024:09:01:49] "GET /search?q=1+OR+1%3D1 HTTP/1.1" 200 18934
192.168.1.105 - - [15/Nov/2024:09:01:52] "GET /search?q=1+UNION+SELECT+username%2Cpassword+FROM+users-- HTTP/1.1" 200 19102
192.168.1.105 - - [15/Nov/2024:09:02:14] "GET /admin HTTP/1.1" 302 -
192.168.1.105 - - [15/Nov/2024:09:02:15] "GET /admin/login HTTP/1.1" 200 3412
192.168.1.105 - - [15/Nov/2024:09:02:31] "POST /admin/login HTTP/1.1" 200 512
192.168.1.105 - - [15/Nov/2024:09:02:33] "GET /admin/users HTTP/1.1" 200 45201
```

**Task 5.1 — Log Analysis**

Answer the following questions based on the log:

1. What type of attack is visible in the first seven log entries? Be specific about the technique and explain your reasoning using the URL parameters.

2. What does the HTTP 500 response in the third entry indicate?

3. Decode `%3D` and `%2C` from the UNION SELECT entry. What do these characters represent and why would an attacker URL-encode them?

4. What appears to have happened at 09:02:31 and 09:02:33? What sequence of events does this suggest?

5. From a forensics perspective, what additional evidence sources would you want to collect to continue this investigation? List at least three.

---

## Lab Report Submission Requirements

Submit a single document containing:

1. Completed memory forensics notes from Part 2 (all recorded observations)
2. Answers to Lab Reflection Questions 1, 2, and 3
3. Completed chain of custody form with actual hash values from Part 3
4. Completed event log analysis table and Lab Reflection Question 4 narrative
5. Answers to all five web server log analysis questions from Part 5

**Format:** PDF or Word document

**Minimum length:** 700 words excluding tables and log excerpts

---

## Grading Rubric

| Component | Points |
|---|---|
| Memory forensics — Volatility output recorded and analyzed | 25 |
| Lab Reflection Questions 1–3 | 30 |
| Chain of custody form — complete with actual hash values | 15 |
| Event log analysis table and narrative | 20 |
| Web server log analysis — all five questions | 10 |
| **Total** | **100** |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 12*
