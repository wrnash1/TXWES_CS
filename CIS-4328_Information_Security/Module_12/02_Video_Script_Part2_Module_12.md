# Video Script: Module 12 — Digital Forensics (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — File System Forensics Concepts (4 minutes)

Welcome back to Module 12. In Part 1 we covered the forensic process, write blockers, disk imaging, and memory forensics. Now let us look at what forensic analysis of a file system reveals and how logs support investigations.

### How File Systems Store Evidence

Modern file systems — NTFS (Windows), ext4 (Linux), APFS (macOS) — maintain metadata about every file and directory. This metadata is forensically invaluable:

**Timestamps (MAC times):** Every file has three critical timestamps:

- **M (Modified)** — when the file content was last changed
- **A (Accessed)** — when the file was last read
- **C (Created/Changed)** — when the file was created on this filesystem, or when metadata changed (note: this is NOT the "birth" timestamp and can be misleading)

For NTFS, there are actually two sets of timestamps per file: the `$STANDARD_INFORMATION` attribute (visible to users and applications) and the `$FILE_NAME` attribute (stored in the MFT directory entry, harder to modify). Attackers who use timestamp manipulation tools (anti-forensics technique called "timestomping") often modify the `$STANDARD_INFORMATION` timestamps but leave the `$FILE_NAME` timestamps unmodified — a discrepancy that reveals the tampering.

**Master File Table (MFT):** NTFS uses a Master File Table to track every file and directory on the volume. Every file has an MFT record. Even when a file is deleted, its MFT record is not immediately overwritten — it is marked as available for reuse. Until overwritten, the MFT record contains the file's name, size, timestamps, and potentially some file content (for small files, content is stored directly in the MFT record in what is called "resident data"). Forensic tools can recover metadata and sometimes content from MFT records of deleted files.

**Unallocated space and file carving:** When a file is deleted, the filesystem marks its clusters as unallocated and removes the directory entry, but the data remains on disk until new data overwrites those clusters. File carving is the technique of scanning unallocated space for recognizable file headers and footers (magic bytes) to reconstruct deleted files even without a directory entry.

For example, JPEG files begin with the bytes `FF D8 FF` and end with `FF D9`. A forensic tool can scan unallocated space looking for these byte sequences and recover deleted images without needing a directory entry.

**Slack space:** Two types are relevant:

- **File slack**: the space between the end of a file's actual data and the end of its last allocated cluster. A 1,500-byte file in a 4,096-byte cluster has 2,596 bytes of file slack. This space contains remnants of whatever was previously stored in those clusters.
- **Volume slack (drive slack)**: space between the last partition and the end of the physical drive.

Slack space can contain remnants of previously deleted files or fragments of data from earlier use of those clusters.

### Prefetch Files and Execution Evidence

Windows maintains Prefetch files (`C:\Windows\Prefetch\`) that track which executables have run on the system, when they last ran, how many times they have run, and what files they accessed. Prefetch is invaluable for proving that a particular executable ran on a system even if the executable itself has been deleted.

A forensic analyst who finds `MIMIKATZ.EXE-XXXXXXXX.pf` in the Prefetch directory has evidence that Mimikatz (a credential dumping tool) ran on this system, even if the attacker deleted the executable.

---

## Segment 2 — Log Analysis in Digital Forensics (4 minutes)

Log analysis is the forensic examination of log files — system, application, network, and security logs — to reconstruct the timeline of events during an incident.

### Windows Event Logs

Windows Event Logs are stored in `.evtx` format and viewable via Event Viewer or tools like EvtxECmd (Eric Zimmermann's command-line parser). Key log channels:

**Security.evtx** — the most forensically important:

- **Event ID 4624** — successful logon. Records: account name, logon type, source network address, authentication package.
- **Event ID 4625** — failed logon. Evidence of brute force or credential stuffing attempts.
- **Event ID 4648** — logon with explicit credentials. Indicates use of RunAs or pass-the-hash.
- **Event ID 4688** — process creation (if audit policy enables process tracking). Records: new process name, parent process, command line (if configured).
- **Event ID 4698/4702** — scheduled task created/modified. Attackers use scheduled tasks for persistence.
- **Event ID 4720/4726** — account created/deleted.
- **Event ID 4776** — credential validation (NTLM). Can indicate Mimikatz-style hash cracking if repeated rapidly.

**System.evtx:**

- **Event ID 7045** — new service installed. Attackers often install malicious services for persistence.

**PowerShell operational logs:**

- **Event ID 4103/4104** — script block logging. Records PowerShell commands as they execute. Capturing this during an investigation can reveal entire malicious PowerShell scripts.

### Linux/Unix Logs

Linux logs are text files, typically in `/var/log/`:

- `/var/log/auth.log` or `/var/log/secure` — authentication events: SSH logins, sudo use, su commands
- `/var/log/syslog` or `/var/log/messages` — general system events
- `/var/log/apache2/access.log`, `/var/log/nginx/access.log` — web server access logs
- `/var/log/audit/audit.log` — if Linux Audit is enabled, records file access, system calls, and command execution

For forensic log analysis on Linux, examine:

- **bash history** (`~/.bash_history`) — commands run by the user. Attackers often `history -c` to clear it, but forensic images may recover it from unallocated space.
- **cron jobs** — scheduled tasks that an attacker may have added for persistence
- **/etc/passwd and /etc/shadow** — accounts present on the system; look for accounts added by attackers

### Web Server Log Analysis

Web server logs record every HTTP request. For application-layer attacks, they are the primary evidence source:

- Source IP address
- Timestamp
- HTTP method (GET, POST, PUT, DELETE)
- Requested URL (including query parameters)
- HTTP response code
- User agent string
- Bytes transferred

SQL injection attempts appear as unusual characters in URL parameters: single quotes, SQL keywords (UNION, SELECT, INSERT), and comment sequences (-- or #). A log entry like:

```
GET /search?q=1'+OR+'1'%3D'1 HTTP/1.1
```

is a classic SQL injection probe. The URL-encoded characters (`%3D` = `=`) reveal the attacker is testing for the vulnerability.

XSS attempts appear as script tags, event handlers, or encoded JavaScript in URL parameters.

### Network Traffic Analysis

Packet captures (PCAP files) and NetFlow data are forensic evidence sources for network-layer investigation:

- **Wireshark** analyzes PCAP files to reconstruct sessions, extract files transferred, and identify protocol anomalies
- **tcpdump** captures network traffic on Linux systems
- **NetFlow** records connection metadata (source/destination IP, port, bytes, duration) without full packet content — valuable for reconstructing communication patterns without the storage overhead of full packet capture

For encrypted traffic (TLS/HTTPS), full packet content is not readable without the private key. However, metadata analysis (connection frequency, volume, destination) and JA3 fingerprinting (TLS client fingerprinting) can identify malicious communications even in encrypted traffic.

---

## Segment 3 — Legal Considerations in Digital Forensics (4 minutes)

Digital forensics exists in a legal context. The technical skills are only half of the discipline — the legal framework determines what evidence you can collect, how you collect it, and whether it will be admissible.

### Authorization to Examine

In a corporate internal investigation, you typically have authorization to examine company-owned systems under the company's acceptable use policy (AUP). Employees who signed the AUP have been notified that their use of company systems is subject to monitoring.

You do NOT automatically have authorization to:

- Examine an employee's personal device (even if connected to company Wi-Fi)
- Access the employee's personal cloud accounts
- Access systems owned by third parties, customers, or partners
- Access systems in other jurisdictions without legal clearance

If criminal prosecution is contemplated, involve law enforcement before collection. Law enforcement obtains search warrants that authorize collection in ways that protect evidence from Fourth Amendment challenges.

**Scope creep** is a real risk in forensic investigations. During an investigation, you may discover evidence of unrelated crimes or policy violations. Consult with legal counsel before acting on out-of-scope discoveries.

### The Fourth Amendment and Digital Forensics

The Fourth Amendment protects against unreasonable search and seizure by government actors. Private employers are NOT government actors and are generally not bound by the Fourth Amendment in their own investigations. However:

- Law enforcement investigations ARE bound by Fourth Amendment protections
- Evidence collected improperly by law enforcement may be excluded under the "exclusionary rule"
- In some jurisdictions, evidence obtained by a private party at law enforcement's direction may face the same scrutiny

### Anti-Forensics Awareness

Attackers attempt to hide their activities and frustrate forensic investigations. Common anti-forensics techniques:

- **Timestomping** — modifying file timestamps to mislead investigators about when files were created or modified
- **Log wiping** — deleting or truncating log files (forensic images capture the state at collection; gaps in logs are themselves evidence)
- **Secure deletion** — overwriting file data before deletion (tools like Eraser on Windows, shred on Linux). On SSDs, wear leveling and TRIM complicate recovery from secure deletion
- **Encryption** — encrypting evidence containers or entire drives (BitLocker, VeraCrypt). Encryption keys in memory (captured via memory forensics) may provide a path around this
- **Steganography** — hiding data inside innocuous files (images, audio) to conceal exfiltrated data or command-and-control communications
- **Living off the land** — using system-native tools (PowerShell, WMI, WMIC) instead of custom malware to minimize forensic artifacts

Awareness of anti-forensics techniques allows investigators to recognize their artifacts: mismatched timestamps, deleted log files, encrypted containers, unusual native tool usage are all indicators worth documenting.

### Expert Witness Testimony

A digital forensics analyst who testifies as an expert witness in court must:

- Qualify their expertise (education, certifications, experience)
- Explain complex technical findings in terms understandable to a lay jury
- Testify only to what the evidence shows, not beyond
- Acknowledge uncertainty honestly
- Withstand cross-examination by opposing counsel

Common certifications for forensic analysts: CFCE (Certified Forensic Computer Examiner), EnCE (EnCase Certified Examiner), GCFE/GCFA (GIAC Certified Forensic Examiner/Analyst), AccessData ACE.

---

## Segment 4 — Forensics in the Cloud (3 minutes)

Traditional disk-and-memory forensics assumes physical access to the hardware being examined. Cloud forensics presents new challenges:

**No physical media access** — You cannot insert a write blocker between yourself and an AWS EC2 instance. Instead, you create a snapshot of the EBS volume and analyze the snapshot.

**Ephemeral infrastructure** — Serverless functions and containers may not persist long enough to capture. Log-forward everything to a SIEM in real time so you have evidence even if the compute instance is gone.

**Provider-controlled logs** — Cloud providers maintain audit logs (CloudTrail for AWS, Activity Log for Azure, Cloud Audit Logs for GCP). You must request or export these logs. They may have limited retention windows. An IR procedure must include immediate log preservation from cloud providers at incident declaration.

**Multi-tenant concerns** — You cannot image the physical server in a cloud data center because other customers' data is on the same hardware. Forensic copies are taken at the virtual layer (VM snapshots, EBS snapshots, container filesystem exports).

**Legal jurisdiction** — Cloud data may reside in multiple countries. Data collection across borders may require compliance with local data protection laws, mutual legal assistance treaties (MLATs), or provider-specific legal processes.

Cloud forensic workflow:

1. Preserve cloud logs immediately (CloudTrail, VPC flow logs, CloudWatch)
2. Take a snapshot of affected EBS volumes / VM disks before terminating instances
3. Capture memory if possible (AWS SSM can run commands to capture memory on running instances)
4. Export relevant API logs from the provider
5. Analyze snapshots and logs in a forensic environment separate from production

---

## Module 12 Full Summary

Digital forensics is the science of reconstructing digital events in a legally defensible manner:

- Five phases: Identification, Preservation, Collection, Analysis, Reporting
- Write blockers prevent evidence modification; MD5/SHA-256 hashes verify integrity
- Disk imaging with dd and FTK Imager creates bit-for-bit forensic copies
- File system forensics: MAC timestamps, MFT records, unallocated space, file carving, Prefetch files
- Memory forensics with Volatility reveals fileless malware, credentials, and network connections
- Log analysis: Windows Event IDs (4624, 4625, 4688, 7045, 4698), Linux auth logs, web server logs, NetFlow
- Legal considerations: authorization scope, Fourth Amendment, anti-forensics awareness
- Cloud forensics: snapshots instead of imaging, provider log preservation, ephemeral infrastructure challenges

For Security+, know the phases, write blockers, order of volatility (covered in Module 11), key forensic tools, and what log types support what type of investigation. Complete the reading, lab, and quiz. See you in Module 13.

---

*End of Part 2 Script*
