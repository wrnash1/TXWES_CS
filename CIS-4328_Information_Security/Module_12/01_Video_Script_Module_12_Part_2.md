# Video Script: Module 12 — Digital Forensics (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 12 | Texas Wesleyan University"]**

---

## Opening — Part 2

**[INSTRUCTOR ON CAMERA]**

Welcome back to Module 12. In Part 1 we covered the forensic process, write blockers, and disk imaging tools. In Part 2 we turn to what happens after collection: memory analysis, log analysis, and the legal and ethical framework that governs the entire discipline.

---

## Section 1 — Memory Analysis

**[SHOW SLIDE: Memory analysis diagram — RAM contents taxonomy]**

RAM analysis is one of the highest-value forensic activities in modern investigations. In RAM at the moment of capture you can find:

- **Running processes**: Every process executing on the system, including hidden malware that does not appear in normal process listings.
- **Network connections**: Open and recently closed TCP/UDP connections — who was the machine talking to?
- **Loaded DLLs and modules**: Libraries loaded by processes, including injected malicious modules.
- **Encryption keys**: Symmetric encryption keys held in RAM by encrypted volume managers (BitLocker, VeraCrypt) and by ransomware.
- **Plaintext passwords**: Credentials cached by LSASS (Windows Local Security Authority Subsystem Service).
- **Command history**: Recent commands run in cmd.exe or PowerShell, even if the terminal was closed.
- **Artifacts of code injection**: Malicious code injected into legitimate process memory space.

### Memory Acquisition Tools

**WinPmem** is an open-source memory acquisition driver for Windows. It creates a raw memory image that can be analyzed with Volatility.

**DumpIt** (from Magnet Forensics) is a single-executable memory acquisition tool for Windows. It requires no installation and produces a raw memory dump with a single click, making it ideal for IR jump kits.

**FTK Imager** can also acquire memory from the live Windows target via its "Capture Memory" function.

### Volatility Framework

Volatility is an open-source memory forensics framework written in Python. It is the industry standard tool for analyzing RAM images. Volatility supports dozens of plugins that extract specific types of information from memory images.

Key Volatility commands:

- `volatility -f memory.dmp imageinfo` — identifies the operating system and profile to use for analysis
- `volatility -f memory.dmp --profile=Win10x64_19041 pslist` — lists running processes
- `volatility -f memory.dmp --profile=Win10x64_19041 pstree` — shows process parent-child relationships (useful for detecting process injection)
- `volatility -f memory.dmp --profile=Win10x64_19041 netscan` — shows network connections from memory
- `volatility -f memory.dmp --profile=Win10x64_19041 hashdump` — extracts NTLM password hashes from LSASS
- `volatility -f memory.dmp --profile=Win10x64_19041 malfind` — finds memory regions with execute permissions that may contain injected code

---

## Section 2 — Log Analysis

**[SHOW SLIDE: Log analysis diagram — log sources and correlation]**

Logs are the narrative record of what happened on a system. Without logs, an investigation is working blind. With comprehensive logs, an investigator can reconstruct an attacker's actions step by step.

### Windows Event Logs

Windows records security events in the Security Event Log. Critical Event IDs for forensic investigation:

- **4624** — Successful logon
- **4625** — Failed logon
- **4648** — Logon using explicit credentials (pass-the-hash indicator)
- **4720** — User account created
- **4728/4732** — User added to security group
- **4688** — Process creation (requires audit policy to be enabled)
- **4698** — Scheduled task created (persistence mechanism)
- **7045** — New service installed (persistence mechanism)
- **1102** — Audit log cleared (attacker covering tracks)

Windows Event Log files have the extension .evtx and can be analyzed with the built-in Event Viewer, PowerShell, or dedicated forensic tools like Eric Zimmermann's tools (EvtxECmd, Timeline Explorer).

### Linux Logs

Linux systems store logs in `/var/log/`. Key files:

- `/var/log/auth.log` or `/var/log/secure` — authentication events (SSH logins, sudo usage)
- `/var/log/syslog` or `/var/log/messages` — general system events
- `/var/log/apache2/access.log` — web server access
- `/var/log/lastlog` — last login record per user
- `.bash_history` — command history per user account

### Web Server Logs

Web server access logs record every HTTP request received. Format (Combined Log Format):

```
192.168.1.100 - - [01/Jun/2026:14:23:11 +0000] "GET /admin/login.php HTTP/1.1" 200 1452 "-" "sqlmap/1.7"
```

Fields: client IP, ident, user, timestamp, request, response code, bytes, referer, user agent.

The user agent in this example — `sqlmap/1.7` — is an immediate red flag. SQLmap is an automated SQL injection tool. A legitimate user's browser would not appear as sqlmap.

### Log Correlation and Timeline

Effective log analysis correlates events across multiple sources on a common timeline. This is called timeline analysis. The investigator:

1. Collects logs from all relevant sources (endpoint, web server, DNS, firewall, Active Directory).
2. Normalizes timestamps to a single timezone (UTC is the standard).
3. Merges events into a unified timeline.
4. Reconstructs the attacker's actions in sequence.

A SIEM performs this correlation automatically during operations. In forensic investigations, tools like Plaso (log2timeline) automate timeline creation from raw forensic images and log files.

---

## Section 3 — File System Forensics

**[SHOW SLIDE: File system metadata diagram — MAC times]**

File systems record metadata about every file. This metadata is valuable forensic evidence.

**MAC times** refer to three timestamps:

- **M-time (Modified)**: When the file content was last changed.
- **A-time (Accessed)**: When the file was last read.
- **C-time (Changed / Creation)**: When the file's metadata was last changed (Unix) or when the file was created (Windows).

Attackers and forensic investigators both pay close attention to MAC times. Timestomping is the practice of modifying MAC times to obscure when malicious files were created or modified. Evidence of timestomping can itself be significant — it indicates an attacker who was aware of forensic investigation and attempted to cover their tracks.

**Deleted files**: When a file is deleted, in most file systems only the directory entry pointing to the file is removed. The actual data blocks are marked as available for reuse but are not overwritten until new data is written. Forensic tools can recover deleted files from unallocated space until those blocks are overwritten.

**File carving**: File carving recovers files based on known file signatures (magic bytes at the beginning of the file) rather than file system entries. It can recover files even when file system metadata is damaged or deleted.

---

## Section 4 — Legal Considerations

**[SHOW SLIDE: Legal framework diagram — authorization sources]**

Digital forensic investigations operate within a legal framework that defines what investigators may access and how. Unauthorized access — even by a well-meaning investigator — can constitute a crime and render evidence inadmissible.

### Authorization Sources

Three primary sources of authorization:

1. **Consent**: The owner of a system or account voluntarily permits access. Employees typically consent to investigation of company-owned systems through acceptable use policy agreements. This is the most common basis for corporate investigations.

2. **Search warrant**: A judge issues a warrant authorizing law enforcement to search specific systems or accounts for specified evidence. Warrants must describe what is to be searched and what evidence is sought — they are not blanket authorizations.

3. **Exigent circumstances**: Emergency situations that justify immediate action without a warrant — typically when evidence is about to be destroyed or someone is in imminent danger.

### Privacy Laws Affecting Forensics

- **ECPA (Electronic Communications Privacy Act)**: Governs access to stored electronic communications and prohibits interception without authorization.
- **CFAA (Computer Fraud and Abuse Act)**: Prohibits unauthorized access to computer systems. Investigators must ensure their access is authorized.
- **GDPR**: Requires that personal data of EU residents be processed lawfully. Forensic collection of EU employee data must comply with GDPR lawful basis requirements.

### Corporate Investigations

In corporate settings, HR and legal must be involved early. Acceptable use policies that employees sign upon joining typically include language authorizing the company to monitor and investigate company-owned devices and systems. This consent language is the legal basis for most corporate digital forensic investigations.

Investigations involving suspected crimes — fraud, intellectual property theft, extortion — should be coordinated with legal counsel who can determine whether law enforcement involvement is appropriate and when.

---

## Section 5 — Forensic Report Writing

**[SHOW SLIDE: Forensic report structure template]**

The forensic report is the examiner's testimony on paper. It must be:

- **Complete**: All methods, tools, and findings documented.
- **Accurate**: Every factual claim supportable by evidence.
- **Clear**: Understandable to a non-technical judge, jury, or executive.
- **Objective**: The examiner reports what the evidence shows, not what a client wants to hear.

A forensic report structure typically includes:

1. Case identification and examiner credentials.
2. Executive summary.
3. Scope and objectives.
4. Evidence received — descriptions, hash values, chain of custody.
5. Methodology — tools used, acquisition process.
6. Findings — detailed narrative of what was discovered.
7. Conclusions — what the evidence means.
8. Appendices — hash logs, tool verification reports, supporting exhibits.

---

## Closing

**[INSTRUCTOR ON CAMERA]**

Digital forensics is the science that turns raw technical evidence into actionable, defensible conclusions. Every technique we covered — memory acquisition, log analysis, file carving, MAC time analysis — serves the ultimate goal: producing findings that can withstand the most adversarial examination.

For Security+, know the forensic process stages, understand write blockers and their purpose, know what dd and FTK Imager do, understand the order of volatility, and be able to describe the legal bases that authorize forensic investigations.

Complete the Reading Guide, Lab, Quiz, and Discussion for Module 12. Module 13 is Risk Management — bringing together threat, vulnerability, and impact into a structured decision framework. I'll see you there.

---

*End of Part 2*
