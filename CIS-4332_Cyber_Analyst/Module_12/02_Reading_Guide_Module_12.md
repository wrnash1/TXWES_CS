# Reading Guide: Module 12 — Digital Forensics for Security Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Introduction

Module 12 develops your foundational digital forensics skills. Where Module 11 covered what to do when an incident occurs, this module covers how to prove what happened — with precision, integrity, and evidence that can withstand scrutiny.

Digital forensics is the discipline of collecting, preserving, analyzing, and presenting digital evidence. For security analysts, this means being able to extract meaningful answers from RAM images, disk images, and network captures. It means knowing which artifacts survive attacker cleanup attempts, and how to build a timeline that reconstructs the full story of an intrusion.

The CySA+ CS0-003 exam tests forensics under Domain 4 (Incident Response and Digital Forensics). Questions are scenario-based and require you to select the correct tool, technique, or artifact for a given investigative need. This reading guide prepares you to answer those questions and, more importantly, to do this work in the field.

---

## Section 1 — High-Yield Glossary

**Order of Volatility** — The principle that evidence should be collected from most volatile (disappears first) to least volatile (persists longest). RAM contents are lost when power is cut. Disk contents persist. Collecting in volatility order maximizes evidence recovery.

**Memory Forensics** — The analysis of a RAM dump to extract evidence of running processes, network connections, loaded code, and in-memory artifacts that would not appear on disk.

**Disk Forensics** — The analysis of a disk image to recover files, deleted data, file system metadata, and application artifacts that establish what actions occurred on the system.

**Network Forensics** — The capture and analysis of network traffic to understand what data traversed the network during an incident, including attacker commands and exfiltrated data.

**Forensic Image** — A bit-for-bit copy of storage media (disk) or a captured dump of RAM, created with tools that do not modify the source. Analysts work from images, never from originals.

**Chain of Custody** — The documented, unbroken record of every person who collected, handled, transferred, or analyzed a piece of evidence from collection through final disposition.

**MACB Timestamps** — The four file system timestamps: Modified (file content last changed), Accessed (file last read), Changed (metadata last changed), Born/Created (file creation time). Analysts use these to reconstruct activity timelines.

**Timestomping** — An anti-forensic technique where an attacker modifies a file's MACB timestamps to disguise when the file was created or modified.

**Prefetch File** — A Windows performance optimization file created when a program is first executed. Prefetch files prove a program ran even if the executable has since been deleted.

**Master File Table (MFT)** — The NTFS file system's index of every file and directory on a volume, including metadata for files that have been deleted. MFT records persist after file deletion until overwritten.

**Volatility** — An open-source memory forensics framework that analyzes RAM images using plugins to extract processes, network connections, injected code, and other artifacts.

**Autopsy** — A graphical digital forensics platform built on The Sleuth Kit, used to analyze disk images for file artifacts, deleted data, registry contents, and browser history.

**Wireshark** — An open-source packet capture and protocol analysis tool used for network forensics, traffic reconstruction, and C2 channel analysis.

**Living-off-the-Land (LotL)** — An attacker technique that uses legitimate, pre-installed OS tools (PowerShell, WMI, certutil, mshta) to perform malicious actions while generating minimal suspicious artifacts.

---

## Section 2 — Forensic Principles Deep Dive

### Preservation

Every forensic action must preserve the integrity of original evidence. This is non-negotiable. Working from original media — even read-only — risks accidental modification through OS file access timestamps, swap file writes, and other background processes.

The correct workflow is: create a forensic image (using write blockers for disk media), hash the image and the original separately, verify hashes match, then do all analysis on the image.

A write blocker is a hardware or software device that intercepts write commands to the source media, allowing reads but preventing any writes. Hardware write blockers are preferred for legal investigations.

### Chain of Custody

A chain of custody form captures:

- Evidence item identifier (label, case number)
- Description of the item
- Collection date, time, and location
- Collector's name and signature
- Each subsequent handler, with date, time, reason for access, and signature

Digital evidence should be hashed (SHA-256) at collection and the hash recorded on the custody form. Any subsequent analysis should re-verify the hash before beginning. A hash mismatch indicates potential tampering and must be investigated before proceeding.

### Documentation Standards

Every investigative action must be logged with:

- Date and time (UTC)
- Analyst name
- Action taken (tool run, query executed, artifact examined)
- Exact commands or tool settings used
- Results observed
- Any inferences drawn and the evidence supporting them

The documentation standard is "recreatable" — another analyst should be able to follow your documentation and independently arrive at the same findings.

---

## Section 3 — Memory Forensics with Volatility

### Acquiring Memory

Memory acquisition must be performed on a live system before shutdown. Once power is cut, RAM contents are gone.

Common acquisition tools:

- **WinPmem** — Windows, command-line, open source
- **DumpIt** — Windows, single executable, minimal footprint
- **LiME (Linux Memory Extractor)** — Linux kernel module, produces raw or padded format images
- **Magnet RAM Capture** — Windows GUI, free

Always hash the resulting image file immediately after acquisition and record the hash in your case notes.

### Volatility Workflow

Volatility 3 (the current version) does not require specifying an OS profile — it auto-detects from the image. Volatility 2 requires profile specification using `imageinfo` first.

Essential plugins and their investigative value:

- `windows.pslist` — Lists all running processes with PID, PPID, start time. The starting point for every memory investigation.
- `windows.pstree` — Displays the process parent-child tree. Malware often spawns from unexpected parents (e.g., Word spawning PowerShell).
- `windows.netscan` — Lists network connections, including established, listening, and recently closed. Reveals C2 connections.
- `windows.malfind` — Scans for memory regions with RWX (read-write-execute) permissions containing executable code — a signature of process injection.
- `windows.dlllist` — Lists DLLs loaded by each process. Unexpected or misspelled DLLs indicate hijacking.
- `windows.cmdline` — Shows command-line arguments passed to each process. Reveals encoded PowerShell and suspicious parameters.
- `windows.hashdump` — Extracts NTLM password hashes from memory.

### Process Anomalies to Investigate

When reviewing `pstree` output, watch for:

- `explorer.exe` spawning `cmd.exe` or `powershell.exe` — common malware execution pattern
- `svchost.exe` with a parent other than `services.exe` — classic process masquerading
- Processes with names similar to legitimate system processes (e.g., `svch0st.exe`, `lsas.exe`)
- Processes running from unusual paths (e.g., `C:\Users\Public\` instead of `C:\Windows\System32\`)
- `powershell.exe` with base64-encoded command-line arguments

---

## Section 4 — Disk Forensics with Autopsy

### Creating a Forensic Image

Disk images are created with tools like `dd` (Linux), FTK Imager (Windows GUI), or Guymager. The image is a bit-for-bit copy of the source disk, including deleted files, slack space, and unallocated space.

The E01 (Expert Witness Format) is the most common format for legal investigations. It includes built-in hashing and compression. Raw (dd) format is simpler and widely compatible but lacks built-in integrity verification.

### Autopsy Case Setup

When opening a new case in Autopsy:

1. Create a new case with a case number and investigator name
2. Add a data source (the disk image file)
3. Select ingest modules — the automated analysis tasks Autopsy will run (keyword search, hash lookup, recent activity extraction, etc.)
4. Wait for ingest to complete before beginning manual analysis

### Key Artifact Locations in Windows

The Windows Registry is stored in hive files on disk. Key hive files and their contents:

- `SYSTEM` — hardware, services, network configuration
- `SOFTWARE` — installed applications, OS settings
- `SAM` — local user account hashes
- `NTUSER.DAT` — per-user settings, recently accessed files (MRU lists), typed URLs, run history

Persistence-related registry keys to examine:

- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`
- `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

Prefetch files are stored in `C:\Windows\Prefetch\` with the extension `.pf`. Each file is named with the executable name and a hash. Prefetch files contain the last eight execution times and a list of files accessed during execution.

Windows Event Logs are stored in `C:\Windows\System32\winevt\Logs\` as `.evtx` files. Critical event IDs:

- 4624 — Successful logon
- 4625 — Failed logon
- 4648 — Logon with explicit credentials
- 4688 — Process creation (requires audit policy)
- 7045 — New service installed
- 1102 — Audit log cleared

---

## Section 5 — Network Forensics with Wireshark

### Essential Filter Syntax

Wireshark display filters narrow traffic to relevant packets. Common filters:

- `ip.addr == 192.168.1.100` — traffic to or from a specific IP
- `tcp.port == 443` — HTTPS traffic
- `dns` — all DNS queries and responses
- `http.request` — HTTP GET and POST requests
- `tcp contains "password"` — TCP streams containing the string "password"

### Following TCP Streams

Right-click any TCP packet and select "Follow TCP Stream" to reconstruct the full conversation between two endpoints as readable text. This is how analysts read HTTP C2 channel commands, FTP file transfers, and plaintext credentials.

### Protocol Anomalies

Key anomalies to look for:

- DNS queries with unusually long subdomains (DNS tunneling indicator)
- HTTP requests with non-standard or missing Host headers
- TLS connections to IPs rather than domain names (common in commodity malware)
- Repeated equal-interval connections to external hosts (beaconing)
- Large HTTP POST requests to unusual external destinations (data exfiltration)

---

## Section 6 — Timeline Reconstruction

A forensic super-timeline combines all timestamps from all evidence sources into one chronological record. This reveals the full attack sequence and identifies gaps in the attacker's activities.

Plaso (log2timeline) is the primary tool for automated super-timeline generation. It ingests disk images, event log files, registry hives, and other sources, extracts all timestamps, and outputs a single sorted timeline file.

Manual timeline construction in a spreadsheet is appropriate for smaller investigations. Columns should include: Timestamp (UTC), Source, Event Type, Description, Analyst Notes.

A complete timeline answers:

- When did the attacker first access the system?
- What was the sequence of attacker actions?
- When did the attacker establish persistence?
- When did data exfiltration begin?
- How long was the attacker present before detection?

---

## Section 7 — CySA+ Exam Focus Areas

For the exam, know these forensic topics precisely:

- Order of volatility — be able to sequence evidence collection correctly in a scenario
- Volatility plugins — match each plugin to its output (pslist for processes, netscan for connections, malfind for injected code)
- Windows artifacts — match each artifact (prefetch, registry, event logs, MFT) to what it proves
- Chain of custody — identify what breaks custody and why it matters
- Anti-forensic techniques — recognize timestomping, log clearing, and LotL usage in scenarios
- Wireshark — understand filter syntax and when to use stream reconstruction

---

## Study Checklist

- [ ] Define all glossary terms without referencing notes
- [ ] Describe the order of volatility and explain why RAM is captured before disk
- [ ] List five Volatility plugins and state what each reveals
- [ ] Name four Windows disk artifacts and describe what each proves
- [ ] Write three Wireshark display filters and explain what each captures
- [ ] Explain what breaks chain of custody and why it matters legally
- [ ] Describe two anti-forensic techniques and how an analyst detects them
- [ ] Complete the Module 12 Lab
- [ ] Complete the Module 12 Quiz
- [ ] Post your Module 12 Discussion initial post by Wednesday

---

## Required Resources

- Volatility Foundation documentation — volatilityfoundation.org
- Autopsy documentation — sleuthkit.org/autopsy
- Wireshark User's Guide — wireshark.org/docs
- NIST SP 800-86 — Guide to Integrating Forensic Techniques into IR (free: nvlpubs.nist.gov)
- CompTIA CySA+ CS0-003 Exam Objectives — Domain 4
- Module 12 Video Lecture (Professor Nash)
