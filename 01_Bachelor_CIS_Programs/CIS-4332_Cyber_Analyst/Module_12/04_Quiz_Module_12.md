# Quiz: Module 12 — Digital Forensics for Security Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Instructions

Select the best answer for each question. Distractor analysis is provided after each question to support exam preparation.

---

## Question 1

A security analyst is first on scene at a potentially compromised Windows workstation that is still powered on. Ransomware is suspected but not yet confirmed. In what order should the analyst collect evidence, following the order of volatility principle?

- A) Hard drive image, then RAM dump, then network traffic capture
- B) RAM dump, then network traffic capture, then hard drive image
- C) Network traffic capture, then hard drive image, then RAM dump
- D) Hard drive image, then network traffic capture, then RAM dump

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Imaging the hard drive first wastes time and may allow RAM contents — active processes, network connections, encryption keys — to be lost if the system shuts down during imaging. Disk contents will persist; RAM will not. Why B is correct: The order of volatility requires collecting the most perishable evidence first. RAM contains running processes, active C2 connections, and in-memory decrypted payloads that vanish on power-off. Network traffic captures in-flight data that stops when connections close. Disk contents persist through power cycles. This sequence maximizes evidence recovery. Why C is incorrect: Hard drive imaging before RAM violates volatility order and risks losing critical in-memory evidence. Why D is incorrect: Same error as A — disk imaging before RAM is never correct under volatility ordering.

---

## Question 2

A forensic analyst uses Volatility's `malfind` plugin against a memory image and finds a memory region in `svchost.exe` with RWX (read-write-execute) permissions containing what appears to be a PE header (`MZ` magic bytes). What does this finding most strongly indicate?

- A) The svchost.exe process has been patched with a legitimate security update that requires executable memory regions
- B) Code injection — a malicious process has injected shellcode or a PE file into the svchost.exe address space
- C) A memory leak in svchost.exe is causing uninitialized memory regions to appear executable
- D) The memory image was corrupted during acquisition, producing false-positive malfind results

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Security patches do not create RWX memory regions with PE headers inside running processes. Legitimate code uses appropriate memory protections; injected code uses RWX to permit execution of arbitrary payloads. Why B is correct: `malfind` flags memory regions that are executable, have been modified, and contain suspicious patterns like PE headers. An RWX region with an MZ header inside `svchost.exe` — a trusted Windows system process — is the textbook signature of process injection (T1055). Attackers inject into trusted processes to evade security products that whitelist system process activity. Why C is incorrect: Memory leaks produce garbage data, not valid PE headers. A coherent MZ structure in an unexpected region is deliberate code, not a memory management artifact. Why D is incorrect: Acquisition corruption does not consistently produce valid PE headers. Corrupted images typically manifest as hash mismatches, not coherent PE structures inside specific processes.

---

## Question 3

An analyst examining a Windows disk image in Autopsy finds a prefetch file for `mimikatz.exe` in `C:\Windows\Prefetch\`. The executable is not present anywhere on the disk. What is the forensic significance of this finding?

- A) The prefetch file is unreliable evidence and cannot confirm that mimikatz was executed
- B) The prefetch file proves mimikatz.exe was executed on the system even though the attacker deleted the executable
- C) The prefetch file proves mimikatz is currently running in memory on the compromised system
- D) Prefetch files are only created for Microsoft-signed executables, so this is a false positive

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Windows prefetch files are highly reliable forensic artifacts created by the Superfetch service when an executable runs for the first time, and updated on subsequent executions. They record execution timestamps and a list of files accessed. Why B is correct: Prefetch files persist in the registry after an executable is deleted. The file's existence proves mimikatz.exe was executed — the attacker's cleanup did not remove the forensic trace. This is precisely the value of prefetch analysis: it survives anti-forensic file deletion. Why C is incorrect: Prefetch files record past execution history, not current runtime state. To confirm current execution, use memory forensics (pslist, malfind), not disk artifacts. Why D is incorrect: Prefetch files are created for any executed binary regardless of code signing status. Windows does not filter prefetch creation by publisher.

---

## Question 4

During network forensics, an analyst applies the Wireshark filter `dns` and observes hundreds of queries from a single internal host, all under the same parent domain but with each subdomain being a long random-looking string. What malware technique does this most strongly indicate?

- A) DNS cache poisoning — the attacker is injecting malicious responses into the organization's resolver
- B) DNS tunneling or DGA-based C2 — the malware is encoding data in DNS queries or using generated subdomains to reach its C2 server
- C) DNS amplification DDoS — the host is being used as a reflector to amplify traffic toward a victim
- D) Zone transfer abuse — the attacker is attempting to download the organization's entire DNS zone

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: DNS cache poisoning involves injecting forged responses into a resolver — it does not produce high volumes of queries with random subdomains from an infected host. Why B is correct: Two related malicious patterns fit this observation. DNS tunneling encodes C2 commands or exfiltrated data in the subdomain portion of queries, generating high query volumes with long random-looking subdomains. DGA malware generates pseudo-random domain names to locate its C2 server, producing many queries to random subdomains under a registered parent domain. Both are key network forensics indicators. Why C is incorrect: DNS amplification attacks originate from spoofed source IPs targeting external victims; the traffic direction and pattern are entirely different. Why D is incorrect: Zone transfer requests are a single AXFR query to an authoritative nameserver, not hundreds of repeated queries to random subdomains.

---

## Question 5

An analyst discovers that all MACB timestamps on a malicious batch file show a creation date of January 1, 2010 — years before the OS was installed. What anti-forensic technique has the attacker used, and how might a skilled analyst detect it?

- A) Log clearing — the batch file's true creation time cannot be recovered
- B) Timestomping — the MACB timestamps were altered, but the true time may be recoverable by comparing `$STANDARD_INFORMATION` vs. `$FILE_NAME` MFT attributes
- C) Steganography — a hidden creation date was embedded in the file's metadata
- D) A rootkit is hiding the batch file from the file system, making timestamp analysis impossible

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Log clearing affects Windows event logs, not file system timestamps. The scenario describes manipulated MACB timestamps, which is a distinct technique. Why B is correct: Timestomping modifies a file's MACB timestamps using tools like Meterpreter's `timestomp` command to push the file off analysts' timelines. However, the NTFS MFT stores timestamps in two attributes: `$STANDARD_INFORMATION` (modifiable by user-space tools) and `$FILE_NAME` (only modifiable by the OS kernel). Timestomping tools typically only update `$STANDARD_INFORMATION`, leaving `$FILE_NAME` with the true creation time. Comparing both attributes detects the manipulation. Why C is incorrect: Steganography hides data inside file content, not metadata timestamps. Why D is incorrect: If a rootkit were hiding the file, the analyst would not have found and examined it at all.

---

## Question 6

Which of the following actions would break the chain of custody for a memory image?

- A) Running Volatility analysis on a copy of the image while retaining the original
- B) Transferring the image to another analyst via shared network drive without documenting the transfer
- C) Storing the image on an encrypted external drive in a locked evidence room
- D) Computing and recording the SHA-256 hash of the image immediately after acquisition

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Performing analysis on a copy while preserving the original is correct forensic practice. Working from copies is required to protect original evidence from modification. Why B is correct: Chain of custody requires that every transfer of evidence be documented — who transferred it, to whom, when, and for what purpose. An undocumented transfer creates a gap that allows opposing counsel to argue the evidence could have been tampered with. Why C is incorrect: Encrypted, physically secured storage is best-practice evidence handling and does not break custody. Why D is incorrect: Hashing evidence immediately after acquisition is a required chain-of-custody step. It creates the cryptographic fingerprint that proves the evidence has not been altered.

---

## Question 7

An analyst examining a disk image finds that Windows Security event log entries prior to 14:00 UTC are present, but all entries from 14:00 UTC onward are absent, even though the incident occurred at 14:32 UTC. What is the most likely explanation, and what event ID would confirm it?

- A) The disk image was acquired before 14:00 UTC so events after that time were not captured
- B) The attacker cleared the Security event log at approximately 14:00 UTC; Event ID 1102 in the System log would confirm this
- C) Windows automatically rotates event logs every few hours, discarding entries; this is normal behavior
- D) The SIEM ingested the log entries and they were deleted from disk as part of normal SIEM operation

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: If the image was acquired after the incident, events from 14:00–14:32 UTC should be present. Their absence indicates deletion, not acquisition timing. Why B is correct: Attackers frequently clear Windows event logs after gaining access. Clearing the Security log generates Event ID 1102 in the Security log itself, but that entry is also cleared. However, a record of the log-clear action is written to the System event log. Event ID 1102 in any surviving log confirms deliberate log clearing at that timestamp. Why C is incorrect: Windows event logs rotate by overwriting oldest entries when the log reaches maximum size — they do not delete entries in bulk at a fixed time interval. A clean cut at exactly 14:00 UTC is not consistent with rotation. Why D is incorrect: SIEM ingestion reads logs and forwards them; it does not delete source log files from the local system.

---

## Question 8

A threat actor uses only `certutil.exe`, `wmic.exe`, and PowerShell (all native Windows tools) to download a payload, execute it, and establish persistence. Which forensic artifact is most likely to preserve evidence of this activity?

- A) The activity is completely undetectable because native tools are excluded from antivirus scanning
- B) The activity creates no network traffic, so Wireshark analysis will show nothing
- C) Windows Event ID 4688 (Process Creation) and PowerShell Script Block Logging will record the commands executed if audit policies are enabled
- D) Only memory forensics can detect living-off-the-land attacks because they leave no disk artifacts

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Native tools are not excluded from detection — EDR products specifically monitor suspicious use of `certutil.exe`, WMIC, and PowerShell because attackers use them. Why B is incorrect: Native tools still generate network traffic. `certutil.exe` downloading a payload produces HTTP/HTTPS connections identical to any other download, fully visible in network captures and firewall logs. Why C is correct: Living-off-the-land techniques avoid dropped executables but cannot avoid process execution records if proper audit policies are in place. Event ID 4688 records every process launch with command line when configured. PowerShell Script Block Logging captures full script content, even encoded or obfuscated scripts. These are the primary detection mechanisms for LotL attacks. Why D is incorrect: The statement "no disk artifacts of any kind" is false. Windows event logs and PowerShell logs are disk artifacts. Memory forensics adds value but is not the only detection path.

---

## Question 9

An analyst uses Autopsy to examine a disk image and finds Shellbag entries referencing a folder path `C:\Users\jdoe\AppData\Roaming\ExfilData\` that no longer exists on the file system. What is the forensic value of this finding?

- A) Shellbag entries only record folders that currently exist; this entry indicates database corruption
- B) The Shellbag entry proves the user's account navigated to that folder path, even though the folder has since been deleted
- C) Shellbag entries are created for all folders automatically by the OS, so this entry has no investigative value
- D) The entry indicates the folder was accessed remotely via SMB, not by a local interactive session

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Shellbag entries persist in the Windows registry after the referenced folder is deleted. Their persistence is precisely what makes them forensically valuable. Why B is correct: Shellbag entries are written to the registry when a user opens a folder in Windows Explorer. They persist after the folder is deleted. The path `ExfilData` suggests data staging. The Shellbag proves the folder existed and was navigated by the user account's Windows shell — evidence of activity that survives the attacker's folder deletion cleanup. Why C is incorrect: Shellbag entries are created based on actual user shell navigation, not automatically for all folders. A folder never opened in Explorer has no Shellbag entry. Why D is incorrect: Shellbag entries are created by the Windows Explorer shell for the logged-on local user's graphical session. Remote SMB access would appear in Security event logs, not Shellbags.

---

## Question 10

A forensic analyst acquires a RAM image from a compromised Linux server and recovers bash history entries using Volatility. Which finding would be MOST significant for understanding privilege escalation?

- A) A history entry showing `ls -la /tmp`
- B) A history entry showing `sudo bash -i` followed by `id` returning `uid=0(root)`
- C) A history entry showing `cat /etc/motd`
- D) A history entry showing `ping google.com`

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Listing `/tmp` is a common reconnaissance step but does not indicate privilege escalation. It is worth noting as attacker activity but is not the most significant finding. Why B is correct: `sudo bash -i` spawns an interactive root shell using sudo, and the subsequent `id` output confirming `uid=0(root)` is definitive proof of successful privilege escalation. This maps to MITRE ATT&CK T1548.003 (Abuse Elevation Control Mechanism: Sudo). It is the highest-impact finding in the list because it demonstrates the attacker achieved root access and complete system control. Why C is incorrect: Viewing `/etc/motd` is reconnaissance, not privilege escalation. It confirms the attacker was logged in but does not indicate elevated access. Why D is incorrect: A ping test is network connectivity verification. It has no privilege escalation significance.

---

## Question 11 (5 points)

A forensic analyst uses the Volatility `netscan` plugin on a Windows memory image. The output shows an established TCP connection from the compromised host to 198.51.100.77:4444, with the local process listed as `svchost.exe` (PID 3844). The analyst then runs `pstree` and finds PID 3844's parent process is `cmd.exe` (PID 2201), and PID 2201's parent is `winword.exe` (PID 1744). What is the forensic significance of this process ancestry?

- A) The process tree is normal — svchost.exe frequently spawns from cmd.exe during Windows updates
- B) The process ancestry reveals an abnormal parent-child chain: Word spawned cmd.exe which spawned a process named svchost.exe connecting to a C2 server — indicating a macro-delivered payload that injected into or impersonated svchost.exe for network communication
- C) The connection to port 4444 is a standard Windows Update port and requires no investigation
- D) Volatility's pstree output is unreliable for parent-process analysis and should not be used for attribution

Correct Answer: B

Distractor Analysis:

- A is incorrect. The legitimate Windows `svchost.exe` is spawned by `services.exe` — not by `cmd.exe` spawned by `winword.exe`. This parent-child chain is abnormal and indicative of malware.
- B is correct. The complete chain — `winword.exe → cmd.exe → svchost.exe` with an outbound C2 connection on port 4444 — is a well-known attacker pattern: a malicious Word macro (delivered via phishing) executes cmd.exe which launches a malicious process masquerading as `svchost.exe`. Port 4444 is commonly associated with Meterpreter. The memory-based view provided by Volatility reveals this chain that may not be visible in disk-based analysis if the malicious process avoided writing artifacts.
- C is incorrect. Port 4444 is not a Windows Update port. Windows Update uses HTTPS (443). Port 4444 has no legitimate Windows service association and is a well-known Meterpreter/Metasploit default listener port.
- D is incorrect. Volatility's `pstree` plugin parses the Windows kernel's EPROCESS doubly-linked list and is widely validated for parent-process relationship reconstruction. It is a reliable forensic technique.

---

## Question 12 (5 points)

During a disk forensic examination, an analyst finds that a file named `report_final.docx` has a Last Modified timestamp of 2024-03-15 but the NTFS $MFT entry for the same file shows a $FILE_NAME creation timestamp of 2024-11-14 — a date 8 months later. What forensic technique does this discrepancy indicate?

- A) The file was opened in read-only mode, which updates the $MFT entry but not the file's content timestamp
- B) Timestomping — the attacker modified the $STANDARD_INFORMATION timestamps to make the file appear older, but the $FILE_NAME attribute timestamps were not modified and reveal the true file creation date
- C) The NTFS $MFT is corrupted, making the timestamps unreliable for forensic purposes
- D) Microsoft Word automatically changes Last Modified timestamps when a file is moved between folders

Correct Answer: B

Distractor Analysis:

- A is incorrect. Read-only access updates access timestamps in some configurations but does not change creation timestamps. More importantly, the discrepancy described (8-month gap between two timestamp fields in the same file) is not explained by read-only access.
- B is correct. Timestomping (ATT&CK T1070.006) is the technique of modifying a file's $STANDARD_INFORMATION timestamps (which are easily writable with standard tools like `timestomp.exe` or PowerShell) to make the file appear older. However, the $FILE_NAME attribute's timestamps are updated by the NTFS kernel driver on file operations and are more resistant to user-mode modification. A discrepancy between the two timestamp sets is a well-documented indicator of timestomping.
- C is incorrect. Isolated timestamp inconsistencies between two attributes within the same file record are not evidence of MFT corruption. MFT corruption typically manifests as unreadable records or inconsistent metadata across many files.
- D is incorrect. Microsoft Word does not automatically modify creation timestamps when files are moved. Moving a file within the same NTFS volume preserves the original timestamps.

---

## Question 13 (5 points)

A forensic examiner is analyzing Windows Prefetch files on a compromised workstation. The examiner finds a Prefetch file for `MIMIKATZ.EXE-AB1234CD.pf` with an embedded last run time of 2024-11-14 03:22:41. The binary `mimikatz.exe` is no longer present on disk. What does this Prefetch finding prove?

- A) Nothing — Prefetch files are unreliable since they can be created without the program actually running
- B) Mimikatz was executed on this system at 03:22:41 on 2024-11-14, providing execution evidence that persists even after the binary is deleted
- C) The Prefetch file indicates mimikatz.exe is currently running in memory
- D) Prefetch files record program installation events, not execution events

Correct Answer: B

Distractor Analysis:

- A is incorrect. Windows Prefetch files are created by the OS when a program is executed (loaded into memory for the first time from that path). They cannot be created without execution. They are reliable execution artifacts used in professional forensic investigations.
- B is correct. Prefetch files record execution evidence — the program name, run count, last run timestamp, and libraries loaded. The deleted binary does not affect the Prefetch file's persistence. This is forensically significant because the attacker deleted the tool but failed to delete the Prefetch artifact, providing evidence of execution time.
- C is incorrect. Prefetch files record historical execution data. They do not indicate current process state. Checking currently running processes requires live system analysis or memory forensics.
- D is incorrect. Prefetch files are execution artifacts, not installation artifacts. Installation events may appear in Event Logs or the Windows Installer database — not Prefetch.

---

## Question 14 (5 points)

During a Wireshark analysis of a PCAP captured during an incident, an analyst applies the display filter `tcp.stream eq 14` and uses `Follow TCP Stream`. The reassembled stream content shows plaintext HTTP requests and responses including what appears to be attacker commands issued to a web shell. What is the forensic value of TCP stream reconstruction?

- A) TCP stream reconstruction decrypts TLS-encrypted content to reveal the original plaintext
- B) TCP stream reconstruction reassembles fragmented TCP segments in sequence to display the complete, bidirectional application-layer content of a single conversation — enabling recovery of commands, responses, and file transfers from unencrypted traffic
- C) TCP stream reconstruction converts binary packet data to ASCII for human reading regardless of the protocol
- D) The `Follow TCP Stream` feature only works for HTTP traffic and cannot reconstruct other protocols

Correct Answer: B

Distractor Analysis:

- A is incorrect. TCP stream reconstruction does not decrypt TLS-encrypted content — the TLS encryption operates above TCP. Without the private key or session key, stream reconstruction of TLS traffic shows only ciphertext. The scenario specifies the traffic is plaintext HTTP.
- B is correct. TCP operates at the transport layer and segments application data across multiple packets. Wireshark's `Follow TCP Stream` reassembles these segments in sequence and presents the complete application-layer conversation — in this case, the web shell HTTP requests and responses — in a human-readable format. This is invaluable for extracting commands executed through a web shell.
- C is incorrect. TCP stream reconstruction reassembles the actual data payload as-is. If the data is binary (e.g., a file transfer), it appears as binary. Wireshark does offer encoding options (hex, ASCII) for display, but it does not convert binary to ASCII automatically.
- D is incorrect. `Follow TCP Stream` works for any TCP-based protocol — HTTP, SMTP, FTP command channels, telnet, and others — not just HTTP.

---

## Question 15 (5 points)

A Windows forensic examination reveals the following artifact: `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.docx` contains a binary value referencing `2024_Q4_Payroll_Export.docx` with a timestamp of 03:44 AM. No matching file exists anywhere on the disk. What does this artifact prove?

- A) The registry entry is corrupted and has no forensic value
- B) The user (or an attacker using the user's account) recently accessed a file named `2024_Q4_Payroll_Export.docx` — the file may have been deleted after access, but the registry artifact proves the access occurred
- C) The file is stored in an encrypted container that the examiner cannot access
- D) RecentDocs entries are created when files are downloaded, not when they are opened

Correct Answer: B

Distractor Analysis:

- A is incorrect. A registry entry referencing a deleted file is expected behavior — RecentDocs entries persist after the referenced file is deleted. This is what makes them forensically valuable. The entry is not corrupted.
- B is correct. Windows RecentDocs registry entries are written when a user opens a file through Windows Explorer or an application's File > Open dialog. They persist after the file is deleted. The entry for `2024_Q4_Payroll_Export.docx` at 03:44 AM — combined with the absence of the file — suggests the file was accessed then deleted. This is evidence of file access and potential data staging followed by anti-forensic deletion.
- C is incorrect. Nothing in the RecentDocs entry format indicates encrypted container storage. The absence of the file on disk is more consistent with deletion than encryption.
- D is incorrect. RecentDocs entries are created on file open, not file download. Download artifacts appear in browser history databases (Chrome History, Firefox places.sqlite) and sometimes in Windows download folders' Zone.Identifier alternate data streams.

---

## Question 16 (5 points)

An anti-forensic technique is detected where an attacker used `wevtutil cl Security` to clear the Windows Security Event Log. Which forensic artifact may still provide evidence of the events that occurred before the log was cleared?

- A) Windows Prefetch files for the security auditing process
- B) The SIEM, if logs were forwarded to a centralized platform in real time before clearing
- C) The Windows Event Log file's free space sectors
- D) Active Directory replication logs on domain controllers

Correct Answer: B

Distractor Analysis:

- A is incorrect. Prefetch files record execution of programs, not the content of security events. The Prefetch file for `wevtutil.exe` would show the clearing tool was run but would not contain the deleted security events themselves.
- B is correct. If the organization configured real-time log forwarding to a SIEM before the clearing occurred, the events that were forwarded before deletion are preserved in the SIEM's indexed storage. This is the primary reason why security best practices emphasize real-time log forwarding — it ensures that local log clearing cannot destroy evidence already captured externally.
- C is incorrect. When Windows Event Log records are deleted (cleared), the log file is truncated and the sectors are not forensically recoverable in the way that deleted files can sometimes be recovered from unallocated disk space. The log binary format does not leave remnants in free space that standard forensic tools can reconstruct.
- D is incorrect. Active Directory replication logs record domain replication events, not Windows Security Event Log content. The security events that were cleared would not be found in AD replication data.

---

## Question 17 (5 points)

A forensic examiner is working on a case where the organization suspects data exfiltration. The examiner runs the Volatility `filescan` plugin on a memory image and finds multiple file handles open to files with paths containing the string `\Temp\`. What specific information does `filescan` provide that disk analysis alone cannot?

- A) `filescan` decrypts files that were encrypted on disk at the time of acquisition
- B) `filescan` identifies file objects currently open in kernel memory — including files that may not exist on disk yet (open handles to newly created files before the write is flushed) or files deleted on disk while still open by a running process
- C) `filescan` is identical to directory listing and provides no additional value over standard disk enumeration
- D) `filescan` recovers deleted files from NTFS unallocated clusters

Correct Answer: B

Distractor Analysis:

- A is incorrect. Volatility's `filescan` identifies file objects in kernel memory — it does not decrypt encrypted content. Encrypted file data remains encrypted whether found via memory analysis or disk analysis.
- B is correct. `filescan` enumerates kernel FILE_OBJECT structures in memory, which represent files currently open by running processes. This captures files that may not yet be visible on disk (written but not yet flushed from OS cache), and critically, files that have been "deleted" from disk but whose handles are still open by a running process — a common anti-forensic pattern where malware deletes its own executable after loading it into memory.
- C is incorrect. `filescan` is not equivalent to directory listing. It operates at the kernel file object level and can find files that are not visible through normal directory enumeration.
- D is incorrect. File carving from unallocated clusters is performed by tools like Autopsy, FTK, or foremost — not by Volatility's `filescan`. `filescan` works on live memory objects, not disk-level data structures.

---

## Question 18 (5 points)

During a forensic investigation, an analyst must determine whether a specific user account was used to log on interactively to a workstation at 02:00 AM. Which Windows artifact provides the most direct evidence of interactive logon activity?

- A) Windows Security Event Log Event ID 4624 with Logon Type 2 (interactive) and Logon Type 10 (remote interactive/RDP)
- B) Windows Prefetch files for `explorer.exe`
- C) NTFS $MFT entry for the user's profile folder
- D) Windows Registry `LastWrite` time on `HKCU\Software`

Correct Answer: A

Distractor Analysis:

- A is correct. Event ID 4624 is the definitive Windows artifact for logon events. Logon Type 2 confirms local interactive logon (physical keyboard/screen). Logon Type 10 confirms Remote Desktop Protocol logon. These events record the exact timestamp, account name, domain, source IP (for RDP), and logon ID — providing complete, timestamped authentication evidence.
- B is incorrect. Prefetch for `explorer.exe` would indicate the Windows shell ran, which may correlate with an interactive session, but it does not directly log user account identity, timestamp precision, or logon type. It is a supporting artifact, not primary logon evidence.
- C is incorrect. The NTFS $MFT creation or access timestamp on the user profile folder may reflect when the profile was created or last accessed but is not a reliable, precise logon timestamp. Profile folder timestamps can be affected by many routine operations.
- D is incorrect. Registry `LastWrite` times on `HKCU` can indicate when registry modifications occurred but do not specifically record logon events or account identity.

---

## Question 19 (5 points)

An investigator receives a Volatility output showing a process named `svchost.exe` running from the path `C:\Users\Public\Downloads\svchost.exe` (PID 4412). A separate Volatility `dlllist` output for PID 4412 shows unusual DLLs loaded from the same `Downloads` directory. What is the forensic conclusion?

- A) This is the legitimate Windows svchost.exe process — its path variation is a normal Windows update behavior
- B) This is a masquerading process: legitimate svchost.exe runs from `C:\Windows\System32\` — a process with the same name running from a user's Downloads folder with non-system DLLs is almost certainly malware using the masquerade technique to avoid detection
- C) The Volatility output is unreliable when processes run from non-system directories
- D) Processes in the Downloads folder cannot execute because Windows prevents code execution from that location by default

Correct Answer: B

Distractor Analysis:

- A is incorrect. The legitimate Windows `svchost.exe` always runs from `C:\Windows\System32\svchost.exe` and is always launched by `services.exe`. Any `svchost.exe` running from a user-writable location like `Downloads` is not the legitimate system binary.
- B is correct. Running malicious processes with the same name as legitimate system processes is ATT&CK T1036.005 (Masquerading: Match Legitimate Name or Location). The Downloads folder path, non-system DLLs, and the process name combination are definitive indicators of a masquerading malware process. The memory-based Volatility analysis reveals the true path, which disk-based artifact cleaning may have attempted to obscure.
- C is incorrect. Volatility's process listing and path information are extracted directly from kernel EPROCESS structures — the process path comes from the PE image mapping. The tool is reliable regardless of the process's execution location.
- D is incorrect. Windows does not block code execution from the Downloads folder by default. While Software Restriction Policies or AppLocker can be configured to block execution from user-writable directories, these are non-default controls not present in most environments.

---

## Question 20 (5 points)

A forensic analysis of a compromised Windows endpoint uses the Volatility `malfind` plugin and identifies a region of memory in the `explorer.exe` process that is marked PAGE_EXECUTE_READWRITE, contains no file-backed mapping, and begins with the MZ header (`4D 5A`). What does this finding indicate?

- A) Normal Windows memory allocation used by the graphics subsystem
- B) Process hollowing or code injection: an executable has been written directly into explorer.exe's memory space, executing without a corresponding file on disk — a classic indicator of fileless malware or process injection
- C) The explorer.exe process has loaded a third-party plugin that uses executable memory regions
- D) The MZ header in memory indicates the file was deleted from disk after being loaded — no further investigation is needed

Correct Answer: B

Distractor Analysis:

- A is incorrect. Windows graphics subsystem allocations do not produce MZ headers in executable memory regions. PAGE_EXECUTE_READWRITE with an MZ header and no file backing is not normal memory allocation behavior.
- B is correct. The combination of PAGE_EXECUTE_READWRITE permissions (writable AND executable — rarely legitimate), no file backing (the memory region does not correspond to a mapped DLL or executable file on disk), and an MZ header (the DOS executable signature) is the definitive Volatility `malfind` signature for injected shellcode or process hollowing. This is ATT&CK T1055 (Process Injection), specifically used by fileless malware to execute code without leaving a binary on disk.
- C is incorrect. Legitimate third-party plugins (loaded DLLs) appear as file-backed memory mappings and would show a corresponding DLL path in the `dlllist` output. A non-file-backed MZ in an executable region is not consistent with legitimate plugin loading.
- D is incorrect. A deleted DLL that was loaded before deletion would still show in the memory region as file-backed with a path (even a deleted path notation). A completely non-file-backed region with MZ header indicates injection, not a deleted loaded file.
