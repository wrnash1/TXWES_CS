# Quiz: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

This quiz contains 20 questions aligned to Security+ SY0-701 exam objectives. Time limit: 30 minutes. Each question is worth 5 points. A score of 75 or higher (15/20) is required to pass.

---

## Questions

**Question 1**

A digital forensics investigator arrives at a scene where a suspect's laptop is powered on and displaying an active desktop. According to the order of volatility, what should the investigator collect FIRST?

- A. A forensic image of the hard drive
- B. The contents of system RAM
- C. Log files stored on the hard drive
- D. Files in the user's Documents folder

---

**Question 2**

A forensic investigator connects a suspect hard drive to their forensic workstation. Before imaging, they insert a hardware device between the drive and the workstation that allows all read operations but blocks all write operations. What is this device called?

- A. Forensic bridge
- B. Write blocker
- C. Hash validator
- D. Chain-of-custody seal

---

**Question 3**

After creating a forensic image, an investigator calculates the SHA-256 hash of both the original drive and the forensic image. The hashes match. What has the investigator confirmed?

- A. The drive contains no malware
- B. The forensic image is an exact, unmodified copy of the original drive
- C. The chain of custody is complete
- D. The suspect modified the drive after acquisition

---

**Question 4**

An investigator uses the `dd` command to image a suspect drive. Later, another investigator needs to analyze the image using a commercial forensic suite. The commercial suite refuses to open the `.img` file. What is the likely cause and what image format would have been more compatible?

- A. dd produces E01 format which is not universally supported; use raw format instead
- B. dd produces a raw format which some tools do not natively support; FTK Imager's E01 format includes metadata and is more widely supported
- C. dd cannot image NTFS drives; FTK Imager should have been used
- D. dd produces SHA-256 encrypted images that require a decryption key

---

**Question 5**

A security analyst uses the Volatility framework's `malfind` plugin on a memory image. The plugin identifies a memory region in `explorer.exe` that is marked executable, is not backed by a file on disk, and contains an MZ header. What attack technique does this most likely indicate?

- A. SQL injection
- B. Code injection (process hollowing or DLL injection)
- C. Brute force password attack
- D. ARP poisoning

---

**Question 6**

A forensic investigator discovers that a malware sample executed entirely in memory using PowerShell without writing any files to disk. The attacker then deleted all PowerShell logs. Which forensic technique is MOST likely to reveal the malicious PowerShell commands that were executed?

- A. File carving on unallocated disk space
- B. Analysis of Prefetch files
- C. Memory forensics on a RAM capture taken during or after the attack
- D. Review of the Windows Security Event Log

---

**Question 7**

A Windows forensic analyst examines a compromised system and finds a file in `C:\Windows\Prefetch\` named `MIMIKATZ.EXE-3A1F9C2B.pf`. The executable itself is not present on the system. What does this Prefetch file prove?

- A. Mimikatz was never actually run on this system
- B. Mimikatz was executed on this system at some point before the Prefetch file was created
- C. The Prefetch file itself is the malware
- D. Mimikatz is a legitimate Windows system tool

---

**Question 8**

An investigator reviews Windows Security Event Logs and finds multiple Event ID 4625 entries with the same source IP address and different account names over a five-minute period. What type of attack does this pattern indicate?

- A. Pass-the-hash
- B. Session hijacking
- C. Brute force or credential stuffing
- D. Privilege escalation

---

**Question 9**

A forensic analyst finds the following Windows Event Log entry:

```
EventID: 7045
Service Name: WinUpdate32
Service File: C:\Users\Public\svchost.exe
```

What does this entry most likely represent?

- A. A legitimate Windows update service
- B. An attacker-installed persistence mechanism via a malicious service
- C. A failed service installation
- D. A security patch being applied

---

**Question 10**

An attacker modifies the `$STANDARD_INFORMATION` attribute timestamps on a malware file to make it appear the file was created three years ago. However, the `$FILE_NAME` attribute timestamps still show the actual creation time. What anti-forensics technique is this and what forensic artifact reveals it?

- A. Log wiping; revealed by event log analysis
- B. Timestomping; revealed by the discrepancy between $STANDARD_INFORMATION and $FILE_NAME timestamps in the MFT
- C. Steganography; revealed by file carving
- D. Living off the land; revealed by Prefetch files

---

**Question 11**

A forensic investigator recovers images from a hard drive that were deleted six months ago. The investigator found the images in unallocated space by scanning for JPEG file headers (`FF D8 FF`) and footers (`FF D9`). What forensic technique was used?

- A. Slack space analysis
- B. Log carving
- C. File carving
- D. Hash matching

---

**Question 12**

During a forensic investigation, an analyst discovers evidence that the subject was committing tax fraud unrelated to the original investigation (which was about data theft). The analyst is a corporate investigator, not law enforcement. What is the MOST appropriate immediate action?

- A. Continue analyzing only the data theft evidence and ignore the tax fraud
- B. Immediately send all evidence to the IRS
- C. Preserve all discovered evidence, stop reviewing out-of-scope material, and consult with legal counsel
- D. Delete the tax fraud evidence to protect the company from liability

---

**Question 13**

A forensic examiner analyzes a cloud-hosted application investigation. The organization used AWS and needs to review who accessed the S3 bucket containing sensitive data. Which AWS service provides the required audit log?

- A. Amazon CloudWatch Metrics
- B. AWS Config
- C. AWS CloudTrail
- D. Amazon GuardDuty

---

**Question 14**

An analyst reviews the following web server log entry:

```
GET /search?q=1+UNION+SELECT+username,password+FROM+users-- HTTP/1.1
```

What attack does this log entry represent?

- A. Cross-site scripting (XSS)
- B. SQL injection using UNION-based extraction
- C. Directory traversal
- D. Command injection

---

**Question 15**

A forensic investigator receives a hard drive and immediately begins analysis on the original drive without creating a forensic image. During analysis, the investigator's tool updates file access timestamps on several files. Why is this a critical error?

- A. The analysis will be slower without an image
- B. Modifying the original evidence violates forensic integrity principles and may make evidence inadmissible; the investigator can no longer prove the evidence is in its original state
- C. The hard drive may overheat without an imaging step
- D. Updated timestamps are not legally significant

---

**Question 16**

Which Volatility 3 plugin is MOST useful for identifying memory regions in a running process that contain executable code not backed by a file on disk — a primary indicator of fileless malware?

- A. `windows.pslist`
- B. `windows.netscan`
- C. `windows.malfind`
- D. `windows.cmdline`

---

**Question 17**

An investigator performs live acquisition on a running Windows server to preserve volatile evidence. The investigation is expected to lead to criminal prosecution. What additional step is MOST important during live acquisition to protect the forensic integrity of the collected data?

- A. Shut down the server before any acquisition
- B. Document every command run and every action taken, with timestamps, in the chain of custody record
- C. Image the disk before capturing RAM
- D. Notify the suspect before beginning acquisition

---

**Question 18**

An attacker used Windows Event Log clearing to hide their activities. An investigator finds the Security log is empty but notices the following entry at the beginning of the log:

```
EventID: 1102 — The audit log was cleared. Subject: Administrator
```

What does this entry indicate?

- A. The event log cleared itself automatically due to size limits
- B. An administrator cleared the Security event log, which is itself a suspicious action that was logged even after clearing
- C. All security events were successfully deleted without a trace
- D. The system needs to be patched to prevent log clearing

---

**Question 19**

A forensic investigator is documenting chain of custody for a seized USB drive. Which TWO items are MOST critical to include in the chain of custody record for this physical evidence? (Select TWO)

- A. The drive's purchase price
- B. The MD5 hash of the drive's contents
- C. The name and signature of every person who has handled the drive
- D. The make, model, and serial number of the drive
- E. The color and brand of the tamper-evident packaging used

---

**Question 20**

During a memory forensics investigation, Volatility's `windows.netscan` output shows a network connection from `svchost.exe` to IP address `185.220.101.45` on port 4444. Port 4444 is commonly used by Metasploit's Meterpreter reverse shell. What does this finding indicate?

- A. svchost.exe is functioning normally
- B. svchost.exe has likely been compromised and is maintaining a command-and-control connection
- C. The system is conducting a port scan
- D. Port 4444 is a standard Windows update port

---

## Answer Key

*For instructor use only — do not distribute to students*

| Question | Answer | Objective |
|---|---|---|
| 1 | B | 4.3 — Order of volatility |
| 2 | B | 4.5 — Write blocker |
| 3 | B | 4.5 — Hash verification |
| 4 | B | 4.5 — Forensic image formats |
| 5 | B | 4.5 — Code injection via malfind |
| 6 | C | 4.5 — Memory forensics / fileless |
| 7 | B | 4.5 — Prefetch execution evidence |
| 8 | C | 4.3 — Event log / brute force |
| 9 | B | 4.3 — Malicious service persistence |
| 10 | B | 4.5 — Timestomping / MFT |
| 11 | C | 4.5 — File carving |
| 12 | C | 4.5 — Legal scope / counsel |
| 13 | C | 4.3 — AWS CloudTrail |
| 14 | B | 4.3 — SQL injection UNION |
| 15 | B | 4.5 — Forensic integrity / original evidence |
| 16 | C | 4.5 — Volatility malfind |
| 17 | B | 4.5 — Live acquisition documentation |
| 18 | B | 4.3 — Event ID 1102 |
| 19 | C, D | 4.5 — Chain of custody elements |
| 20 | B | 4.5 — Memory analysis / C2 connection |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 12*
