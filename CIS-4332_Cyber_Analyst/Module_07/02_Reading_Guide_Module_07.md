# Reading Guide: Module 07 - Malware Analysis Fundamentals

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Introduction

Malware analysis gives SOC analysts the ability to move from detecting that something happened to understanding what happened and why. This module covers the vocabulary, methodology, and analytical techniques needed to classify malicious software, perform basic static and dynamic analysis, extract indicators of compromise, and map malware behaviors to MITRE ATT&CK. These skills are foundational for the CySA+ exam and for every tier of SOC analyst work.

---

## Section 1: Malware Categories

### 1.1 Malware Type Reference Table

| Malware Type | Primary Behavior | Key Distinguishing Characteristic | ATT&CK Reference |
|---|---|---|---|
| Virus | Replicates by attaching to legitimate files | Requires user action to spread; modifies host files | T1204 (User Execution) |
| Worm | Self-replicates across networks | No user interaction required; spreads autonomously | T1210 (Exploit Public-Facing App) |
| Trojan | Appears legitimate; delivers malicious payload | Relies on social engineering; does not self-replicate | T1204.002 (Malicious File) |
| RAT (Remote Access Trojan) | Backdoor with full remote control | Persistent C2 channel; supports file ops, keylogging, screenshots | T1219 (Remote Access Software) |
| Ransomware | Encrypts files; demands payment | Double-extortion variants also exfiltrate data before encrypting | T1486 (Data Encrypted for Impact) |
| Rootkit | Hides its own presence in the OS | Operates at kernel or hypervisor level; infected OS cannot be trusted | T1014 (Rootkit) |
| Keylogger | Records keystrokes | Hooks Windows API calls to intercept input | T1056.001 (Keylogging) |
| Spyware | Silently exfiltrates user data | No obvious disruption; victim may be unaware for extended period | T1041 (Exfiltration Over C2) |
| Botnet Agent | Executes commands from C2 server | Part of a larger network; used for DDoS, spam, cryptomining | T1071 (Application Layer Protocol C2) |
| Fileless Malware | Executes entirely in memory | No malicious file on disk; uses LOLBins or script engines | T1059 (Command and Scripting Interpreter) |

### 1.2 Ransomware Double-Extortion Model

Modern ransomware operations follow a two-phase extortion model:

Phase 1 — Exfiltration: Before encrypting, attackers exfiltrate sensitive files to attacker-controlled infrastructure. This provides leverage beyond just file recovery.

Phase 2 — Encryption: The malware encrypts victim files using strong asymmetric or hybrid cryptography. Decryption requires a key held by the attacker.

Extortion: Victims are threatened with public release of exfiltrated data if ransom is not paid, even if they restore from backups.

Detection opportunity: The exfiltration phase (large outbound data transfers to unusual destinations) is often detectable before encryption begins.

---

## Section 2: Malware Analysis Methodology

### 2.1 Static vs. Dynamic Analysis Comparison

| Attribute | Static Analysis | Dynamic Analysis |
|---|---|---|
| Execution required | No — sample is never run | Yes — sample executes in sandbox |
| Safety | Safe on any workstation | Requires isolated sandbox environment |
| Primary outputs | File hash, strings, import table, PE headers, disassembly | Process tree, network IOCs, registry changes, file drops, API calls, mutex names |
| Defeated by | Packing, obfuscation, encryption | Sandbox evasion, environment checks, time-delayed execution |
| Speed | Fast — immediate results | Slower — requires detonation and observation period |
| Depth | Limited for obfuscated/packed samples | Reveals actual runtime behavior regardless of obfuscation |
| Tools | Strings, PE-bear, CFF Explorer, Ghidra, IDA Pro, YARA | Cuckoo Sandbox, Any.run, Joe Sandbox, Hybrid Analysis, REMnux |

### 2.2 Static Analysis Techniques

File hashing: Compute MD5, SHA-1, and SHA-256 hashes of the sample. Query against VirusTotal, internal threat intelligence platform, and ISAC feeds. A hash match provides immediate context: malware family, behavior profile, existing IOCs.

Strings extraction: Extract printable ASCII and Unicode strings from the binary. High-value findings include:

- Embedded URLs and IP addresses (C2 infrastructure)
- Registry key paths (persistence mechanism)
- Filenames and directory paths (file drop locations)
- Error messages and function names (operational clues)
- Mutex names (per-instance uniqueness identifiers)
- Base64-encoded strings (may decode to additional IOCs)

PE header analysis: Portable Executable files contain a header structure with security-relevant fields:

- Compilation timestamp: May indicate when the malware was built (note: can be forged)
- Section names: Standard sections are `.text`, `.data`, `.rdata`. Unusual names like `.UPX0` indicate the UPX packer was used.
- Import Address Table (IAT): Lists every DLL and function the binary calls. High-risk imports include CreateRemoteThread, VirtualAllocEx, WriteProcessMemory, OpenProcess (process injection), CryptEncrypt (ransomware), and URLDownloadToFile (downloader).
- Entropy: Values near 8.0 in a section indicate packed or encrypted content.

### 2.3 Dynamic Analysis and Sandbox Reports

A sandbox report includes the following components analysts must be able to interpret:

Threat verdict and score: Overall confidence the sample is malicious, based on behavioral scoring.

Process tree: The full parent-child execution chain from sample launch through all spawned processes. Mirrors what EDR would capture on a real compromised endpoint.

Behavioral indicators: Categorized list of what the sample did, often tagged to ATT&CK techniques:

```text
[PERSISTENCE]  Creates Registry Run key
               HKCU\Software\Microsoft\Windows\CurrentVersion\Run
               Value: WindowsSecurityService
               ATT&CK: T1547.001

[PERSISTENCE]  Creates Scheduled Task
               Name: WindowsSecurityUpdate
               Command: C:\Users\...\AppData\Roaming\svch0st.exe
               ATT&CK: T1053.005

[COMMAND AND CONTROL]  TCP connection established
               Destination: 198.51.100.82:4444
               ATT&CK: T1071.001

[DEFENSE EVASION]  Creates process with misleading name
               Path: C:\Users\...\AppData\Roaming\svch0st.exe
               ATT&CK: T1036.005
```

Network activity log: All DNS queries, TCP/UDP connections, HTTP requests with full headers and payload summaries.

File system activity: All files created, modified, deleted, or renamed during execution.

Registry activity: All keys created or modified.

---

## Section 3: IOC Extraction Reference

### 3.1 IOC Types Produced by Malware Analysis

| IOC Type | Source | Example | SIEM/EDR Use |
|---|---|---|---|
| File hash (SHA-256) | Static and dynamic | `a3f5b2c1d4e6...` | EDR cross-endpoint file hash hunt |
| File path | Dynamic (file create events) | `C:\Users\...\AppData\Roaming\svch0st.exe` | EDR path hunt; FIM alert |
| C2 IP address | Dynamic (network log) | `198.51.100.82` | SIEM outbound connection rule; firewall block |
| C2 domain | Dynamic (DNS query log) | `updates.windows-security.net` | DNS sinkhole; SIEM DNS query rule |
| Mutex name | Dynamic (API call log) | `{6F29A05E-1012-4B7D-9B1E-11AB34CC66D7}` | EDR mutex hunt |
| Registry key | Dynamic (registry activity) | `HKCU\...\Run\WindowsSecurityService` | EDR registry monitor; FIM registry alert |
| Scheduled task name | Dynamic (process/registry) | `WindowsSecurityUpdate` | EDR scheduled task hunt; Event ID 4698 |
| User-agent string | Dynamic (HTTP log) | `Mozilla/5.0 (compatible; MSIE 9.0)` | SIEM HTTP user-agent filter |
| Embedded URL | Static (strings) | `http://198.51.100.47/stage2.exe` | SIEM URL filter; proxy block |
| Service name | Dynamic (service creation) | `WinSystemMon` | EDR service hunt; Event ID 7045 |

### 3.2 Malware Evasion Techniques

| Technique | How It Works | Detection Approach |
|---|---|---|
| Packing | Compresses/encrypts code; unpacks at runtime | High entropy sections; PE section names like .UPX0 |
| Obfuscation | Renames variables, inserts junk code | Code structure analysis; behavioral analysis still works |
| Process injection | Runs code inside a legitimate process | EDR process access events; Sysmon Event ID 10 |
| Process hollowing | Replaces legitimate process code | Parent-child mismatch; memory region discrepancy |
| DLL sideloading | Places malicious DLL alongside legitimate app | Unexpected DLL load path; hash mismatch for known DLL |
| Masquerading | Names files like system processes | File path outside expected system directory |
| Sandbox detection | Checks for VM artifacts; delays execution | Multi-stage detonation; longer sandbox runtime; user interaction simulation |
| Living off the land | Uses legitimate system tools | EDR behavioral context; parent-child process anomalies |

---

## Section 4: Malware Behavior to ATT&CK Mapping

### 4.1 Tactic-Level Behavior Reference

| Observed Behavior | ATT&CK Tactic | ATT&CK Technique | Technique ID |
|---|---|---|---|
| Office macro spawns PowerShell | Execution | Command and Scripting Interpreter: PowerShell | T1059.001 |
| Certutil downloads file from internet | Command and Control | Ingress Tool Transfer | T1105 |
| Registry Run key modified | Persistence | Boot or Logon Autostart Execution: Registry Run Keys | T1547.001 |
| Scheduled task created | Persistence | Scheduled Task/Job: Scheduled Task | T1053.005 |
| LSASS memory accessed | Credential Access | OS Credential Dumping: LSASS Memory | T1003.001 |
| Whoami, ipconfig, net user executed | Discovery | System Information Discovery + Account Discovery | T1082, T1087 |
| SMB connection to another host | Lateral Movement | Remote Services: SMB/Windows Admin Shares | T1021.002 |
| Files encrypted with new extension | Impact | Data Encrypted for Impact | T1486 |
| Large outbound transfer on port 443 | Exfiltration | Exfiltration Over C2 Channel | T1041 |
| Process injected into explorer.exe | Defense Evasion | Process Injection | T1055 |
| Binary named svch0st.exe | Defense Evasion | Masquerading: Match Legitimate Name or Location | T1036.005 |
| Connects to external IP on port 4444 | Command and Control | Application Layer Protocol | T1071.001 |

---

## Section 5: File Integrity Monitoring (FIM)

### 5.1 FIM Overview

File Integrity Monitoring (FIM) establishes cryptographic baselines of critical files and registry paths and alerts when those baselines change. FIM is a key detective control for detecting:

- Malware dropping files into system directories
- Rootkit modifications to OS files
- Persistence mechanism installation (registry key modifications)
- Unauthorized configuration file changes
- Evidence of tamper after a security incident

### 5.2 FIM Implementation

FIM protects two categories of resources:

File system: `C:\Windows\System32\`, `C:\Windows\SysWOW64\`, `/etc/`, `/bin/`, `/sbin/`, `/usr/sbin/`, critical application binaries, configuration files.

Registry (Windows): `HKLM\SYSTEM\CurrentControlSet\Services`, `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`, `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.

FIM tools generate alerts containing: affected path, original hash, new hash, modification timestamp, and the account that made the change. These alerts should be forwarded to the SIEM for correlation with concurrent process creation and network events.

---

## Section 6: SOC Malware Analysis Workflow

### 6.1 Six-Step Workflow

```text
Step 1: Hash and query
        Compute SHA-256 of sample.
        Query VirusTotal, internal TIP, ISAC feeds.
        If known: extract existing IOCs and ATT&CK profile.

Step 2: Static quick-scan
        Run strings extraction — extract URLs, IPs, registry paths.
        Check PE imports for high-risk API calls.
        Check section entropy for packer indicators.

Step 3: Sandbox if needed
        Submit to isolated sandbox for detonation.
        Review process tree, network activity, registry changes,
        file drops, API call log.
        Extract all IOCs from report.

Step 4: Hunt with IOCs
        Use EDR cross-endpoint query to hunt:
        - File hash across all endpoints
        - C2 IP/domain in outbound connection logs
        - Scheduled task name or registry key value
        - Mutex name in memory scan
        Determine scope: how many endpoints are affected?

Step 5: Feed IOCs into SIEM
        Create detection rules from extracted IOCs.
        Add C2 IPs and domains to threat intelligence block lists.
        Configure EDR to alert on hash and mutex matches.

Step 6: Document and share
        Record IOCs, ATT&CK mapping, and timeline in ticket.
        If ISAC-eligible: share under TLP:AMBER or TLP:WHITE.
        Update playbook with any new response steps identified.
```

---

## CySA+ Exam Tips

Exam Tip 1: Know malware categories by behavior, not just name. Ransomware encrypts files. RAT provides remote control. Rootkit hides itself. Fileless malware executes in memory only. These behavioral distinctions are what exam scenarios test.

Exam Tip 2: Static analysis does not execute the sample. Dynamic analysis does execute the sample in a sandbox. If a question asks how to safely determine what a file does at runtime, the answer is sandbox (dynamic analysis), not static analysis.

Exam Tip 3: Packing defeats static analysis. A packed sample shows high section entropy and minimal meaningful strings. Sandbox detonation is required to see the unpacked behavior.

Exam Tip 4: The PE Import Address Table reveals capabilities before execution. CreateRemoteThread + VirtualAllocEx + WriteProcessMemory = process injection capability. This is testable on CySA+.

Exam Tip 5: Sandbox evasion is a real technique. Sophisticated malware checks for VM artifacts (low uptime, known sandbox process names, missing user activity history) and does nothing malicious when detected. Analysts should use extended sandbox runtimes and human-behavior simulation options when available.

Exam Tip 6: IOC types to know for the exam: file hashes, IP addresses, domain names, URLs, registry key paths, mutex names, file paths, user-agent strings. Each maps to a specific detection mechanism (SIEM rule, EDR query, DNS sinkhole, firewall block).

Exam Tip 7: ATT&CK technique IDs to know for malware behaviors: T1059.001 (PowerShell), T1105 (Ingress Tool Transfer), T1547.001 (Registry Run Keys), T1053.005 (Scheduled Task), T1003.001 (LSASS), T1486 (Data Encrypted for Impact), T1055 (Process Injection), T1036.005 (Masquerading), T1041 (Exfiltration over C2).

Exam Tip 8: Double-extortion ransomware exfiltrates before encrypting. The exfiltration phase is detectable in network telemetry. FIM detects the encryption phase (mass file renames/overwrites). Know both phases for exam scenarios.

---

## Glossary

- API Call Log: Record of Windows API function calls made by a process during sandbox execution; reveals capabilities and behavior
- Botnet: Network of compromised systems controlled by an attacker's C2 server
- C2 (Command and Control): Attacker-controlled infrastructure used to issue commands and receive data from compromised systems
- Double-Extortion: Ransomware model that combines data exfiltration and encryption for two leverage points
- Dynamic Analysis: Malware analysis that executes the sample in a sandbox to observe runtime behavior
- Entropy: Statistical measure of randomness in data; high entropy in PE sections indicates packing or encryption
- FIM (File Integrity Monitoring): Detective control that alerts on changes to cryptographic baselines of protected files and registry keys
- Import Address Table (IAT): PE header structure listing all DLLs and API functions a binary calls at runtime
- Mutex: Named synchronization object; malware uses mutexes to prevent multiple instances from running
- Packing: Technique that compresses/encrypts malware code to defeat static analysis and AV signature scanning
- PE (Portable Executable): Standard Windows executable file format; contains header, sections, and import/export tables
- RAT (Remote Access Trojan): Malware providing persistent remote control capability over a compromised system
- Rootkit: Malware designed to hide its own presence by operating below or within the OS
- Sandbox: Isolated, instrumented virtual environment for safely executing and observing malware behavior
- Static Analysis: Malware analysis that examines the artifact without executing it
- Strings: Tool and technique for extracting printable character sequences from binary files

---

## Required Resources

- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com

---

## Study Checklist

- [ ] List the ten malware categories and describe the behavioral characteristic that distinguishes each
- [ ] Explain the difference between static and dynamic analysis without notes
- [ ] Describe what a PE Import Address Table reveals and identify three high-risk API imports
- [ ] List five IOC types produced by sandbox dynamic analysis
- [ ] Explain what packing is and why it defeats static analysis
- [ ] Map six malware behaviors to their ATT&CK tactic and technique IDs
- [ ] Describe what FIM monitors and how it detects persistence mechanism installation
- [ ] Walk through the six-step SOC malware analysis workflow from memory
- [ ] Review all eight exam tips
- [ ] Complete the Module 07 Lab
- [ ] Complete the Module 07 Quiz
- [ ] Post initial response to the Module 07 Discussion board by Wednesday at 11:59 PM
