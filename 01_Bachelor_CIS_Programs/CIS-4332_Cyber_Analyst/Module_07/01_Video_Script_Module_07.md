# Video Script: Module 07 - Malware Analysis Fundamentals

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20-24 minutes

## CySA+ CS0-003 Domain Alignment: Domain 1 - Security Operations (33%)

---

### [00:00 - 01:30] Introduction

Professor Nash on camera. Title card: Module 07 — Malware Analysis Fundamentals.

"Welcome to Module 07. So far in this course we have built skills in log analysis, network traffic analysis, and endpoint detection. All of those disciplines assume you are looking at behavior — what a system is doing. This module adds a different lens: examining the malware itself.

Malware analysis is the practice of dissecting malicious software to understand what it does, how it does it, and what traces it leaves behind. As a SOC analyst you will not always perform deep reverse engineering — that is typically a Tier 3 or malware research function. But you absolutely need to understand the outputs of malware analysis: the IOCs it produces, the techniques it maps to, and how to use those findings to hunt across your environment.

This module covers malware categories, the difference between static and dynamic analysis, sandbox analysis, key behavioral indicators, and how everything maps to ATT&CK. Let's get into it."

---

### [01:30 - 05:00] Malware Categories

"Before we analyze malware we need a shared vocabulary for what we are analyzing. Malware is not one thing — it is a category of many types of malicious software, each with distinct behavior and objective.

Virus — a program that replicates by attaching itself to legitimate files. Requires user interaction to spread. Becoming less common but still appears on certification exams.

Worm — self-replicating malware that spreads across networks without user interaction. Notable examples: WannaCry used a worm component to spread laterally via SMB after initial exploitation.

Trojan — malware disguised as a legitimate program. Users execute it willingly. Trojans do not self-replicate; they rely on social engineering for delivery.

Remote Access Trojan, or RAT — a Trojan that provides the attacker with persistent backdoor access and remote control of the infected host. RATs typically support file operations, keylogging, screenshot capture, and C2 communication.

Ransomware — encrypts victim files and demands payment for the decryption key. Modern ransomware is often double-extortion — encrypts files and also exfiltrates them, threatening public release if ransom is not paid. Maps to ATT&CK T1486 (Data Encrypted for Impact).

Rootkit — malware designed to hide its own presence by operating at or below the operating system level. Kernel-mode rootkits modify OS data structures. Detecting rootkits requires out-of-band analysis because the infected OS cannot be trusted.

Keylogger — captures and records keystrokes, commonly to harvest credentials. Can be hardware or software. Software keyloggers often hook Windows API calls to intercept input before it is processed by the application.

Spyware — silently collects and exfiltrates information about the user — browsing history, credentials, documents — without obvious ransomware-style disruption.

Botnet agent (bot) — a compromised endpoint enrolled in a botnet. The attacker's C2 server issues commands to all enrolled bots simultaneously — for distributed denial of service, spam campaigns, or cryptocurrency mining.

Fileless malware — executes entirely in memory using legitimate system tools. Leaves no persistent file on disk. Traditional AV cannot detect it. We covered this in Module 06 in the context of EDR detection.

On the CySA+ exam, questions about malware categories test behavioral recognition: given a described behavior, identify the malware type. The exam will not ask you to write malware — it will ask you to classify what you are seeing in an EDR alert or sandbox report."

[SHOW DIAGRAM: Malware category table with columns: Malware Type, Primary Behavior, Key Characteristic, ATT&CK Technique Reference. Rows for all ten types listed above.]

---

### [05:00 - 10:00] Static vs. Dynamic Analysis

"Malware analysis has two fundamental methodologies: static analysis and dynamic analysis. Understanding when to use each — and what each can and cannot reveal — is a core CySA+ exam topic.

Static analysis examines a malware sample without executing it. You are inspecting the artifact itself.

What static analysis produces:

File hash — compute MD5, SHA-1, and SHA-256 hashes of the sample. Query those hashes against threat intelligence databases. A hash match to a known malware family tells you a great deal immediately. This is the fastest and safest first step.

Strings extraction — the strings utility extracts printable character sequences from the binary. You may find embedded URLs, IP addresses, registry key paths, filenames, error messages, mutex names, or encryption keys that were not obfuscated. This is high-value for IOC extraction.

PE header analysis — Windows executables are Portable Executable (PE) files. The PE header contains: compilation timestamp, section names, import address table (what DLLs and functions the malware calls), export table, and embedded resources. The import table is particularly valuable — an executable that imports CreateRemoteThread, VirtualAllocEx, WriteProcessMemory, and OpenProcess is showing you a process injection capability before you run a single line of code.

Entropy analysis — legitimate executables have predictable entropy distributions. A section with very high entropy (close to 8.0) likely contains encrypted or compressed code — a common packer indicator. Packed malware unpacks itself at runtime, which defeats static analysis.

Disassembly — tools like Ghidra (free, NSA-developed) and IDA Pro (commercial) disassemble the binary into assembly code. This is where advanced static analysis lives and requires significant expertise.

Limitation of static analysis: Packing and obfuscation defeat it. Many modern malware samples are packed — compressed and encrypted — so the actual malicious code is hidden until runtime. Static analysis on a packed sample shows you the unpacking stub, not the real payload.

Dynamic analysis executes the malware in a controlled environment and observes what it actually does at runtime. The controlled environment is a sandbox.

What dynamic analysis produces:

Process activity — what processes the malware created, what parent-child relationships formed, what process injection occurred.

File system changes — what files were created, modified, or deleted, and where.

Registry changes — what registry keys were created or modified. Persistence mechanisms almost always show up here.

Network activity — what DNS queries were made, what IP addresses were connected to, on what ports, what data was transmitted.

API calls — sandboxes hook Windows API calls and log every call. This reveals behavioral capabilities even when the code is obfuscated.

Mutex creation — malware often creates named mutexes to prevent multiple instances from running simultaneously. A mutex name is a high-fidelity IOC.

The limitation of dynamic analysis is evasion. Sophisticated malware detects sandbox environments and either does nothing or executes benign behavior. Sandbox detection techniques include checking for: low uptime, too little memory, missing user activity, known sandbox process names, registry artifacts specific to virtual machines.

For the CySA+ exam: When asked how to safely analyze a suspicious file to determine if it is malicious, the answer is dynamic analysis in a sandbox — not executing it on a production workstation. When asked what static analysis reveals, the answer includes file hashes, embedded strings, and import tables."

[SHOW DIAGRAM: Two-column comparison. Left column: Static Analysis — tools, outputs, limitations. Right column: Dynamic Analysis — tools, outputs, limitations. Center: when to use each.]

---

### [10:00 - 14:30] Sandbox Analysis and IOC Extraction

"Let me walk through what a sandbox report looks like and how an analyst uses it.

When you submit a sample to a sandbox — commercial tools like Any.run, Joe Sandbox, or Hybrid Analysis, or an on-premises open-source tool like Cuckoo Sandbox — the platform detonates the sample in an instrumented VM and generates a report.

The report includes:

A threat score or verdict — a numerical confidence that the sample is malicious, based on the behaviors observed.

A process tree — the hierarchy of processes the malware spawned during execution. This directly mirrors what an EDR would show you on a real compromised endpoint.

Behavioral indicators — a categorized list of what the sample did, often tagged to ATT&CK techniques. For example: 'Creates scheduled task (T1053.005),' 'Accesses LSASS memory (T1003.001),' 'Connects to external IP on port 443 (T1071.001).'

IOCs extracted from the execution:

Network IOCs: C2 IP addresses and domain names, destination ports, HTTP request paths, user-agent strings. These become your threat intelligence feed entries and your SIEM detection rules.

File IOCs: paths and hashes of files the malware dropped. These become your EDR hash hunts and file quarantine targets.

Registry IOCs: specific registry keys and values created for persistence. These become your EDR registry monitoring rules.

Mutex names: specific strings the malware used as mutex names. These are often unique per malware family and are excellent detection signatures.

Let me walk through a realistic example. A sandbox report for a sample shows:

The sample creates a copy of itself at a path in AppData using a name that mimics a legitimate Windows process with a subtle character substitution — a zero replacing the letter O.

It creates a Registry Run key pointing to the copied binary, and a scheduled task that runs every five minutes.

It connects to an external IP on port 4444 via TCP immediately after execution.

It queries a domain that is not a Microsoft domain despite appearing to be one.

It creates a mutex with a unique GUID-style name.

From this report, an analyst extracts: three persistence IOCs (file path, Run key, scheduled task name), one C2 IP, one C2 domain, one port number, and one mutex name. Each becomes a detection rule, a threat hunting query, and a threat intelligence record.

The analyst then uses the EDR to run a cross-endpoint query to determine if any other endpoints in the environment are running a process with the same hash, connecting to this IP, or containing this scheduled task name."

---

### [14:30 - 18:00] Malware Behaviors and ATT&CK Mapping

"Understanding malware behavior means being able to look at what a piece of malware does and immediately map it to ATT&CK tactics and techniques. This is a core analyst skill.

Let me walk through the most commonly tested malware behaviors and their ATT&CK mappings.

Defense evasion: Malware uses many techniques to avoid detection. Process injection (T1055) — injecting malicious code into a legitimate process so the malicious activity appears to come from that process. Process hollowing (T1055.012) — creating a legitimate process in a suspended state, replacing its code with malicious code, then resuming it. DLL sideloading (T1574.002) — placing a malicious DLL alongside a legitimate application that loads it by name. Masquerading (T1036) — naming malware files to resemble system processes.

Credential access: Keylogging (T1056.001) captures credentials typed by the user. LSASS memory access (T1003.001) extracts authentication hashes from the Windows credential cache. Browser credential dumping reads saved passwords from browser storage.

Discovery: Immediately after compromise, attackers run discovery commands to understand what they landed on. System information discovery (T1082): systeminfo, whoami. Network configuration discovery (T1016): ipconfig, arp, netstat. Account discovery (T1087): net user, net localgroup administrators. Process discovery (T1057): tasklist. All of these were visible in the Module 06 lab process tree.

Lateral movement: After gaining a foothold, attackers move to other systems. Pass-the-hash (T1550.002), remote services via RDP (T1021.001), SMB/Windows Admin Shares (T1021.002), remote execution via PsExec or WMI.

Exfiltration: Moving data out of the environment. Exfiltration over C2 channel (T1041), exfiltration over web service (T1567), DNS tunneling (T1048.003).

Impact: The end-stage destructive or disruptive action. Data encryption for ransomware (T1486), service stop (T1489), disk wipe (T1561).

For the exam, the most frequently tested mapping is: malware behavior described in a scenario — you identify the ATT&CK tactic and technique. Know the technique IDs for the behaviors listed above."

---

### [18:00 - 21:00] Malware Analysis in SOC Operations

"How does malware analysis fit into the SOC workflow you are building throughout this course?

When a malware sample is identified — through EDR alert, email gateway detection, or incident response — the SOC analyst follows this workflow:

Step 1: Hash and query. Compute the file hash. Query it against threat intelligence — VirusTotal, internal TIP, ISAC feeds. If it is a known family, you have immediate context: name, behavior, IOCs, ATT&CK mapping, remediation steps.

Step 2: Static quick-scan. Even for a known sample, run strings extraction to confirm embedded network IOCs. The sample may be a variant with a different C2 than what is in published intelligence.

Step 3: Sandbox if needed. If the hash is not recognized or the strings are obfuscated, submit to sandbox. Review the behavior report. Extract all IOCs.

Step 4: Hunt with IOCs. Using the EDR cross-endpoint query, hunt for the file hash, the C2 IP, the domain, the mutex name, and the registry key across all endpoints. Identify scope.

Step 5: Feed IOCs into SIEM. Create detection rules from the extracted IOCs. Future activity matching these indicators fires alerts immediately.

Step 6: Document and share. Add the IOCs and ATT&CK mapping to your threat intelligence platform. If your organization participates in an ISAC, share the intelligence under TLP:AMBER or TLP:WHITE as appropriate."

---

### [21:00 - 24:00] Module Summary and Lab Preview

"Let's bring together what we covered.

Malware categories: virus, worm, Trojan, RAT, ransomware, rootkit, keylogger, spyware, botnet agent, fileless malware. Know the behavioral characteristics of each.

Static analysis: no execution required. Produces file hashes, strings, PE import tables, entropy indicators. Defeated by packing.

Dynamic analysis: execute in sandbox. Produces process trees, network IOCs, registry changes, file drops, API call logs, mutex names. May be defeated by sandbox evasion.

Sandbox reports include a process tree, behavioral indicator list tagged to ATT&CK, and extracted IOCs.

Malware behaviors map to ATT&CK tactics: defense evasion, credential access, discovery, lateral movement, exfiltration, impact.

SOC malware analysis workflow: hash and query, static scan, sandbox, hunt with IOCs, feed to SIEM, document and share.

In the Module 07 lab you will analyze a provided simulated sandbox report, extract all IOCs, map behaviors to ATT&CK techniques, and write a threat intelligence summary. Read the Reading Guide first for the full malware category reference and the IOC extraction table.

Study resources: professormesser.com and comptia.org. See you in Module 08."

---

End of Module 07 Video Script

Study Resources: comptia.org | professormesser.com
