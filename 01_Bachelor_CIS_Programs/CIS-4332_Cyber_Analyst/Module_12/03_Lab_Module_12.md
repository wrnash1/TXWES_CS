# Lab Activity: Module 12 — Digital Forensics for Security Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Lab Overview

This lab develops hands-on digital forensics skills across three evidence domains: memory forensics, disk artifact analysis, and network forensics. You will analyze provided forensic artifacts from a simulated compromise, apply the correct tools and techniques, and produce findings that answer the investigator's core question: what exactly did the attacker do?

**Estimated Time:** 2–3 hours

**Tools Required:**

- Volatility 3 (free download: volatilityfoundation.org)
- Autopsy 4.x (free download: sleuthkit.org/autopsy)
- Wireshark (free download: wireshark.org)
- Provided lab artifact files (download from Canvas Module 12 Lab folder)

**Lab Files (download from Canvas):**

- `lab12_memory.raw` — Windows 10 RAM image (2 GB)
- `lab12_disk.E01` — Windows 10 disk image
- `lab12_capture.pcap` — Network packet capture

---

## Scenario

Your organization's EDR alerted on suspicious process behavior from a finance department workstation (`FINANCE-WS-12`) at 14:32 UTC on the day of capture. The system was isolated before shutdown, allowing a live memory image to be captured. A disk image and a 30-minute network capture were also collected.

Your task is to determine what the attacker did, when, and what data may have been compromised.

---

## Part 1 — Memory Forensics with Volatility

### Step 1.1 — Verify the Memory Image

Before analysis, verify the image integrity.

On Windows (PowerShell):

```powershell
Get-FileHash -Algorithm SHA256 lab12_memory.raw
```

On Linux/macOS:

```bash
sha256sum lab12_memory.raw
```

Record the hash in your lab report. Compare it against the expected hash posted in Canvas. A matching hash confirms the image is unaltered.

### Step 1.2 — List Running Processes

Run the process list plugin:

```bash
python3 vol.py -f lab12_memory.raw windows.pslist
```

In your lab report:

1. How many processes are listed?
2. Identify any processes running from unusual paths (not `C:\Windows\` or `C:\Program Files\`).
3. Identify any processes with names that resemble legitimate system processes but contain typos or extra characters.

### Step 1.3 — Examine the Process Tree

Run the process tree plugin:

```bash
python3 vol.py -f lab12_memory.raw windows.pstree
```

In your lab report:

1. Identify any process with an unexpected parent. For example, `powershell.exe` spawned by `winword.exe` or `excel.exe`.
2. Record the PID and PPID for any suspicious parent-child relationship you find.
3. What attack technique does this parent-child relationship suggest? Reference the MITRE ATT&CK technique ID.

### Step 1.4 — Examine Network Connections

Run the network scan plugin:

```bash
python3 vol.py -f lab12_memory.raw windows.netscan
```

In your lab report:

1. List all ESTABLISHED connections, including local address, remote address, remote port, and the process that owns the connection.
2. Identify any connections to external (non-RFC-1918) IP addresses.
3. Look up each external IP in a threat intelligence source (VirusTotal, AbuseIPDB). Record the findings.

### Step 1.5 — Check for Code Injection

Run the memory region scanner:

```bash
python3 vol.py -f lab12_memory.raw windows.malfind
```

In your lab report:

1. How many suspicious memory regions did `malfind` identify?
2. Which processes contain suspicious regions?
3. What characteristic of the memory region does `malfind` flag as suspicious?

---

## Part 2 — Disk Forensics with Autopsy

### Step 2.1 — Create a New Case

Open Autopsy and create a new case:

- Case Name: `Lab12_Investigation`
- Case Number: `CIS4332-L12`
- Investigator Name: Your name

Add `lab12_disk.E01` as the data source. Enable the following ingest modules:

- Recent Activity
- Hash Lookup (use the NIST NSRL database if available)
- Keyword Search (add keywords: `powershell`, `cmd.exe`, `whoami`, `mimikatz`)
- Windows Registry

Wait for ingest to complete before proceeding.

### Step 2.2 — Examine Prefetch Files

Navigate to: Results > Extracted Content > Run Programs

In your lab report:

1. List all programs that appear in prefetch analysis.
2. Identify any programs that should not be on a standard finance workstation.
3. For each suspicious program, record the last execution time and the execution count.

### Step 2.3 — Examine the Windows Registry

Navigate to: Results > Extracted Content > Installed Programs and OS Accounts

Also use the Registry Viewer to examine:

- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

In your lab report:

1. List all entries found in the Run keys.
2. Identify any entry that references an unusual path or executable name.
3. What persistence technique does this represent? Reference the MITRE ATT&CK technique.

### Step 2.4 — Examine Windows Event Logs

Navigate to: Results > Extracted Content > Recent Documents

Also review Security event log entries under Data Sources > lab12_disk.E01 > vol1 > Windows > System32 > winevt > Logs > Security.evtx

In your lab report, find and document:

1. All Event ID 4624 entries (successful logon) in the 2-hour window around the 14:32 alert. Note the logon type and source IP for each.
2. Any Event ID 7045 entries (new service installed).
3. Any Event ID 1102 entries (audit log cleared). If present, record the time.

---

## Part 3 — Network Forensics with Wireshark

### Step 3.1 — Open the Capture

Open `lab12_capture.pcap` in Wireshark.

Review the Protocol Hierarchy (Statistics > Protocol Hierarchy) and the Conversations view (Statistics > Conversations > TCP tab).

In your lab report:

1. What are the top 3 protocols by packet count?
2. Which external IP address has the highest byte count in TCP conversations?

### Step 3.2 — Filter for C2 Traffic

Apply the following filter to isolate connections to the suspicious external IP identified in Step 1.4:

```text
ip.addr == <suspicious_ip>
```

Follow the TCP stream of the longest connection to this IP (right-click a packet > Follow > TCP Stream).

In your lab report:

1. What protocol is being used inside this connection?
2. Can you read the content of the conversation, or is it encrypted?
3. If readable, what commands or data can you identify in the stream?

### Step 3.3 — Identify Exfiltration

Apply the following filter to find large HTTP POST requests:

```text
http.request.method == "POST"
```

For each POST request found:

1. Record the destination IP, destination port, URI path, and request size.
2. If the content type is readable (not encrypted), describe what data appears to be transmitted.
3. Does the timing of this POST correlate with any events found in the disk or memory analysis?

---

## Part 4 — Timeline Reconstruction

Using all findings from Parts 1, 2, and 3, construct a chronological incident timeline in your lab report.

Create a table with the following columns:

- Timestamp (UTC)
- Evidence Source (Memory / Disk / Network)
- Event Description
- Significance / Analyst Note

Your timeline must include at minimum:

- The earliest indicator of attacker activity
- The malware execution event
- The persistence installation event
- The C2 connection establishment
- The data exfiltration event (if identified)
- The time of the EDR alert

---

## Part 5 — Chain of Custody Documentation

Complete a chain of custody record for `lab12_memory.raw`. Your record must include:

1. Evidence identifier and description
2. Collection method (tool used, date/time, analyst name)
3. SHA-256 hash at collection
4. Storage location
5. Your access entry (date/time, reason, action taken)

---

## Deliverables

Submit a single PDF to Canvas containing:

1. Part 1 — Memory forensics findings (Steps 1.1–1.5)
2. Part 2 — Disk forensics findings (Steps 2.1–2.4)
3. Part 3 — Network forensics findings (Steps 3.1–3.3)
4. Part 4 — Incident timeline table
5. Part 5 — Chain of custody record

**Grading:** 100 points total. Parts 1–3 are worth 20 points each. Parts 4 and 5 are worth 10 points each.

---

## Part 9 — Challenge Exercise

### Challenge 1: Memory Forensics — Process Injection Detection

You are analyzing a Volatility output from a compromised workstation. The `pstree` output shows: `wininit.exe (PID 392) → services.exe (PID 488) → svchost.exe (PID 1044)` and separately `winlogon.exe (PID 440) → userinit.exe (PID 1188) → explorer.exe (PID 1832) → cmd.exe (PID 2240) → powershell.exe (PID 3108)`. The `malfind` output for PID 1832 (explorer.exe) shows a PAGE_EXECUTE_READWRITE region at base address 0x00B40000 containing the MZ header. The `netscan` output shows PID 1832 with an established connection to 198.51.100.44:443.

1. Identify all anomalous indicators in the Volatility output and explain what each indicates about attacker activity (provide ATT&CK technique ID for each).
2. What Volatility command would you run next to extract the injected code from the explorer.exe memory region at 0x00B40000, and what tool would you use to analyze the extracted binary?
3. The `netscan` output shows `explorer.exe` with an outbound connection. Why is this suspicious, and how does it relate to the injected code finding?
4. Write a Volatility command sequence (3–4 commands) that you would use to build a complete picture of the attack chain from this memory image.

### Challenge 2: Artifact Correlation for Timeline Reconstruction

You have the following artifacts from a compromised workstation examination:

- **Windows Security Event Log**: EID 4624 Logon Type 3 for `DOMAIN\jsmythe` from 10.10.22.14 at 01:47:22 AM
- **Prefetch**: `MIMIKATZ.EXE-C1234567.pf` with last run 01:49:08 AM, run count 3
- **ShimCache / AppCompatCache**: Entry for `C:\Temp\update_svc.exe` with last modified 01:48:44 AM
- **RecentDocs**: Reference to `HR_Annual_Payroll_2024.xlsx` at 01:52:30 AM (file not on disk)
- **MFT $LogFile**: `HR_Annual_Payroll_2024.xlsx` deleted at 01:54:11 AM
- **Shellbags**: `C:\Users\jsmythe\Desktop\ExfilPrep\` navigated at 01:50:12 AM (folder deleted)

1. Build a complete 8-entry incident timeline from the artifacts above, with timestamp, artifact source, and one-sentence description of what the artifact proves for each entry.
2. Identify which artifacts survived the attacker's anti-forensic cleanup and explain what specific cleanup action failed to eliminate each artifact.
3. Based on the evidence, write a one-paragraph forensic conclusion paragraph suitable for inclusion in an incident report, addressing: attack entry, privilege escalation, data access, exfiltration staging, and anti-forensic activity.

### Reflection Questions

1. An attacker who clears the Windows Security Event Log, deletes the malware binary, deletes staged exfiltration files, and clears browser history has attempted thorough anti-forensic cleanup. Identify three artifact categories they likely missed and explain what each would still prove.
2. Explain why forensic examination of RAM should be prioritized over disk imaging when an analyst has only 20 minutes before the system must be shut down, citing at least two specific types of volatile evidence that would be permanently lost.
