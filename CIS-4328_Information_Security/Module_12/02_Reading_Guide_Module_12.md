# Reading Guide: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports Module 12: Digital Forensics. You will study the forensic process, evidence collection tools, memory analysis, log analysis, file system forensics, and the legal framework governing digital investigations. These topics map to Security+ Domain 4 and are foundational for incident response, security operations, and any career path involving investigation or compliance.

**Estimated reading and study time:** 2.5 to 3 hours

---

## Learning Objectives

By the end of this module you should be able to:

- Describe the stages of the digital forensic process.
- Explain the purpose and operation of write blockers.
- Describe how to create a forensically sound disk image using dd and FTK Imager.
- Identify what types of evidence can be recovered from memory analysis.
- Describe MAC times and their significance in timeline reconstruction.
- Explain the legal bases that authorize digital forensic investigations.
- Describe the structure and contents of a forensic report.

---

## Required Reading

- **NIST SP 800-86** — Guide to Integrating Forensic Techniques into Incident Response (free at csrc.nist.gov)
- **SWGDE Best Practices for Digital and Multimedia Evidence** — Sections 1 through 4
- **Professor Messer Security+ SY0-701 Study Guide** — Domain 4 sections on digital forensics
- **Volatility Documentation** — Overview and plugin reference at volatilityfoundation.org

---

## Section A — The Forensic Process

The digital forensic process provides a structured, repeatable methodology that supports both technical accuracy and legal defensibility. NIST SP 800-86 describes four primary stages.

### Stage 1 — Identification

Identification determines what potential evidence sources exist. In a typical investigation this includes:

- Endpoint devices: workstations, laptops, mobile phones.
- Server systems: file servers, email servers, domain controllers.
- Network devices: firewalls, routers, switches with logging enabled.
- Cloud services: email (O365, Gmail), cloud storage (SharePoint, OneDrive, S3), SaaS applications.
- External media: USB drives, portable hard drives, optical media.

Identification must also assess legal authority. Before collecting from any source, the investigator must confirm authorization — consent, warrant, or other legal basis.

### Stage 2 — Preservation

Preservation prevents evidence modification. Key actions:

- Attach write blockers to all storage media before connecting to forensic workstations.
- Issue legal holds to suspend data retention policies for affected systems.
- Document the state of systems (running vs. powered off) at the time of collection.
- Apply the order of volatility — capture volatile evidence before non-volatile.

### Stage 3 — Collection

Collection is the acquisition of evidence using validated tools and documented procedures. All collection activities are logged in the chain of custody. Hash values are computed and recorded for all collected items.

### Stage 4 — Analysis

Analysis extracts meaning from collected evidence. Analysis is always performed on forensic copies. Findings are documented in working notes as analysis proceeds, forming the basis of the final report.

### Stage 5 — Reporting

The forensic report translates technical findings into findings suitable for legal, executive, or law enforcement audiences.

---

## Section B — Write Blockers and Disk Imaging

### Write Blockers

A write blocker prevents any write operations from reaching a storage device while allowing reads to proceed normally. Hardware write blockers are preferred in legal investigations because they operate at the hardware layer, independent of operating system software.

**Why write blockers matter:** Modern operating systems modify storage devices automatically on mount — updating last-access times, writing journal entries, updating metadata. These modifications alter the device's hash and make it impossible to prove the evidence is unchanged from the time of seizure.

### dd — Disk Imaging

`dd` (Data Duplicator) is a standard Unix/Linux command that copies data at the block level. For forensic imaging:

```
dd if=/dev/sdb of=/forensic/images/sdb.img bs=4096 conv=noerror,sync
```

After imaging:

```
md5sum /dev/sdb && md5sum /forensic/images/sdb.img
sha256sum /dev/sdb && sha256sum /forensic/images/sdb.img
```

Both hashes must match to confirm the image is identical to the source.

**dcfldd** enhances dd with integrated hashing and verification during the imaging process, reducing the time required for post-imaging verification.

### FTK Imager

FTK Imager (free from Exterro/AccessData) provides a Windows GUI for forensic imaging. Key features:

- Supports E01, raw (dd), AD1 formats.
- Generates hash verification reports automatically after imaging.
- Can acquire live memory from Windows systems.
- Allows read-only mounting of forensic images for browsing.
- Can preview file system contents without creating an image (triage).

**E01 format (Expert Witness Format)** is the most common format for enterprise and law enforcement forensics. It stores compressed, segmented images with embedded hash values, examiner notes, and case information — making it self-documenting and court-friendly.

---

## Section C — Memory Analysis

### What Memory Contains

RAM holds the working state of a live system. Forensically, memory may contain:

- All running processes, including hidden/injected malware.
- Open and recently closed network connections (attacker C2 communication).
- Plaintext credentials cached by LSASS (Windows password manager).
- Encryption keys held by volume managers (BitLocker) or ransomware.
- Command history from terminal sessions.
- Injected malicious code residing in legitimate process memory.
- Registry hives loaded in memory.

### Memory Acquisition Tools

- **WinPmem**: Open-source, command-line memory acquisition for Windows.
- **DumpIt**: Single-executable memory capture, popular in IR jump kits.
- **LiME (Linux Memory Extractor)**: Loadable kernel module for Linux memory acquisition.
- **FTK Imager**: GUI-based memory capture available in Windows.

### Volatility Framework

Volatility is the industry standard open-source framework for memory analysis. It supports images from Windows, Linux, and macOS.

Key Volatility plugins:

| Plugin | Purpose |
|---|---|
| `pslist` | Lists processes from the EPROCESS linked list |
| `pstree` | Shows parent-child process relationships |
| `psscan` | Scans raw memory for EPROCESS structures (finds hidden processes) |
| `netscan` | Lists network connections from memory |
| `hashdump` | Extracts NTLM password hashes from LSASS |
| `malfind` | Finds memory regions with suspicious execute permissions |
| `dlllist` | Lists DLLs loaded by each process |
| `cmdline` | Shows command-line arguments for each process |

The difference between `pslist` and `psscan` is significant. `pslist` reads the OS's linked list of processes — an attacker can unlink a process from this list to hide it. `psscan` searches raw memory for process structures directly and can find processes that `pslist` misses.

---

## Section D — Log Analysis

### Windows Event Log Key Event IDs

Forensic investigators focus on specific event IDs when reviewing Windows Security logs:

| Event ID | Meaning | Forensic Significance |
|---|---|---|
| 4624 | Successful logon | Track user logon activity and source IPs |
| 4625 | Failed logon | Brute force detection |
| 4648 | Logon using explicit credentials | Possible pass-the-hash or lateral movement |
| 4720 | User account created | Attacker persistence via new accounts |
| 4732 | User added to local group | Privilege escalation |
| 4688 | Process created | Track command execution (requires audit policy) |
| 4698 | Scheduled task created | Common persistence mechanism |
| 7045 | Service installed | Common persistence mechanism |
| 1102 | Audit log cleared | Attacker covering tracks |

### Linux Log Files

| Log File | Contents |
|---|---|
| /var/log/auth.log | SSH logins, sudo usage, authentication events |
| /var/log/syslog | General system events |
| /var/log/apache2/access.log | Web server requests |
| ~/.bash_history | User command history |
| /var/log/lastlog | Last login per user |

### Timeline Analysis

Timeline analysis merges events from multiple log sources, normalized to UTC, into a single chronological record. This allows reconstruction of the attacker's full activity sequence. Key tools:

- **Plaso (log2timeline)**: Extracts timestamps from forensic images and log files, creates unified supertimeline files.
- **Timeline Explorer**: Windows GUI tool for reviewing timeline files.

---

## Section E — File System Forensics

### MAC Times

Every file has timestamps that record its history. On Windows (NTFS) and Linux (ext4) the three key timestamps are:

- **Modified (M)**: When the file content was last changed.
- **Accessed (A)**: When the file was last read.
- **Created/Changed (C)**: When the file was created (Windows) or when its metadata last changed (Linux).

**Timestomping** is the modification of MAC times by an attacker to disguise when files were created or modified. For example, setting a malware file's timestamps to match legitimate Windows system files makes it appear to be original OS content.

### Deleted File Recovery

When a file is deleted:

1. The directory entry (MFT record in NTFS) is marked as available.
2. The data blocks are marked as unallocated.
3. The data remains on disk until overwritten.

Forensic tools scan unallocated space to recover deleted files. The likelihood of recovery decreases the longer the system has been in use after deletion and the higher the disk activity.

**File carving** recovers files based on known file signatures (magic bytes). Common signatures: JPEG (`FF D8 FF`), PDF (`25 50 44 46`), ZIP (`50 4B 03 04`). File carving works even without intact file system metadata.

---

## Section F — Legal Considerations

### Authorization

Three legal bases for forensic access:

1. **Consent**: System owner or authorized representative grants permission. In corporate investigations, acceptable use policies provide employee consent for company-owned devices.
2. **Search warrant**: Court-issued authorization for law enforcement to search specific systems.
3. **Exigent circumstances**: Imminent destruction of evidence or threat to life justifies warrantless access in narrowly defined emergency situations.

### Relevant Laws

- **ECPA (Electronic Communications Privacy Act)**: Governs access to stored electronic communications.
- **CFAA (Computer Fraud and Abuse Act)**: Prohibits unauthorized computer access. Investigators must ensure their access is authorized.
- **GDPR**: Processing EU residents' personal data requires lawful basis; forensic investigations of EU employee data must comply.
- **Fourth Amendment (US)**: Protects against unreasonable government searches. Applies to law enforcement investigations; corporate investigators are generally not bound by the Fourth Amendment.

---

## Key Terms

- **Forensic process**: Identification, preservation, collection, analysis, reporting
- **Write blocker**: Device that allows read access while preventing writes to evidence
- **dd**: Unix bit-copy utility used for disk imaging
- **FTK Imager**: Free forensic imaging tool supporting E01 and raw formats
- **E01 format**: Expert Witness Format — compressed, self-documenting forensic image
- **Volatility**: Open-source memory forensics framework
- **Memory acquisition**: Capturing RAM contents before system shutdown
- **Order of volatility**: Hierarchy prioritizing most-fleeting evidence first
- **MAC times**: Modified, Accessed, Changed/Created timestamps on files
- **Timestomping**: Modifying timestamps to obscure file activity
- **File carving**: Recovering files from unallocated space using file signatures
- **Timeline analysis**: Merging multi-source log events into a unified chronology
- **Chain of custody**: Documented record of all evidence handling
- **Legal hold**: Instruction to suspend deletion of records for potential litigation
- **ECPA**: Electronic Communications Privacy Act
- **CFAA**: Computer Fraud and Abuse Act

---

## Review Questions

1. What are the five stages of the forensic process?
2. Why does connecting a storage device to a Windows computer without a write blocker invalidate forensic integrity?
3. What does the `conv=noerror,sync` option in a dd command do?
4. What is the difference between the `pslist` and `psscan` Volatility plugins?
5. Name four types of evidence that can be found in a Windows RAM image.
6. What does Windows Event ID 1102 indicate and why is it forensically significant?
7. What is timestomping, and what does evidence of it suggest about an attacker?
8. Explain how file carving can recover deleted files even when file system metadata is destroyed.
9. What is the legal basis for corporate digital forensic investigations of employee-owned devices versus company-owned devices?
10. What is the purpose of the forensic report and what must it contain?

---

## Certification Exam Tip

Security+ SY0-701 tests digital forensics with scenario-based questions. Common question types: "Which action should the investigator perform first on a live system?" (answer involves volatile memory or order of volatility), "What device prevents modification of evidence during imaging?" (write blocker), and "Which tool creates a bit-for-bit copy of a drive?" (dd, dcfldd, or FTK Imager). Know the difference between dd and FTK Imager (command-line vs. GUI, raw vs. E01 output) and understand what chain of custody protects.

---

*End of Reading Guide — Module 12*
