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
