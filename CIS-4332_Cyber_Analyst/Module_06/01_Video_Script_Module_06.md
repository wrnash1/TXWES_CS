# Video Script: Module 06 - Endpoint Detection and Response

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20-24 minutes

## CySA+ CS0-003 Domain Alignment: Domain 1 - Security Operations (33%)

---

### [00:00 - 01:30] Introduction

Professor Nash on camera. Title card: Module 06 — Endpoint Detection and Response.

"Welcome to Module 06. We have covered log analysis and network traffic analysis. Now we go to the endpoint — the workstation or server where the attack actually executes. This is where the attacker runs code, steals credentials, establishes persistence, and moves laterally.

Endpoint Detection and Response — EDR — is the technology category that gives analysts deep, real-time visibility into what is happening at the process and file system level on individual endpoints. EDR has transformed the SOC over the past decade. It captures the data that traditional antivirus misses and gives responders the ability to investigate, contain, and remediate from a central console without physically touching the affected machine.

In this module we cover what EDR is, how it works, the key telemetry it captures, how to use it for investigation, and the most important endpoint-based attack patterns the CySA+ exam tests. Let's get started."

---

### [01:30 - 05:00] Traditional Antivirus vs. EDR

"To understand what EDR offers, you need to understand what traditional antivirus does not.

Traditional antivirus — AV — works primarily through signature-based detection. It compares files on disk or in memory against a database of known malicious file signatures (typically file hashes or byte sequence patterns). When a file matches a known signature, AV quarantines or deletes it.

The limitations of traditional AV are well-known and well-exploited by attackers:

Signature-based detection misses novel malware that has no existing signature. A new ransomware variant not yet in the database will execute freely.

Fileless malware — attacks that execute entirely in memory using legitimate Windows tools, with no malicious file written to disk — are invisible to file-based AV scanning.

Living-off-the-land techniques use Windows built-in tools like PowerShell, WMI, and certutil in ways that are difficult to distinguish from normal administrative activity.

EDR addresses these limitations by shifting from file-based signature detection to behavioral telemetry. Instead of asking 'does this file match a known bad signature,' EDR asks 'what is this process actually doing — what files is it creating, what registry keys is it modifying, what network connections is it making, what other processes is it spawning?'

EDR captures a continuous stream of behavioral telemetry from every monitored endpoint and sends that telemetry to a central management platform where analysts can query it, create detection rules, and initiate response actions remotely."

---

### [05:00 - 09:00] EDR Capabilities and Telemetry

"Let me walk through the core capabilities of an EDR platform and the types of telemetry it captures.

Process execution telemetry — every process that starts on the endpoint is recorded: the process name, the full path, the command line arguments, the parent process, the user, and the timestamp. This is equivalent to Sysmon Event ID 1 at much greater scale and fidelity. From this data, analysts can reconstruct a process tree — the parent-child relationship that shows how a malicious process was spawned.

File system telemetry — file creates, modifies, renames, and deletes are recorded. When malware drops a payload to disk, the EDR captures it. The hash of the dropped file is computed and can be compared against threat intelligence databases instantly.

Registry telemetry — registry key creates, modifies, and deletes. This is critical for detecting persistence mechanisms like T1547.001 Run Keys.

Network telemetry — outbound connections from each process. Not just the connection, but which specific process opened the socket. This directly answers the analyst's question: what is this process connecting to?

Memory operations — process injection (Sysmon equivalent to Event ID 10), thread injection, and other in-memory manipulation techniques that leave no file on disk.

User activity — logon events, privilege changes, and account activity at the endpoint level.

Response capabilities — beyond detection, EDR platforms allow analysts to take response actions remotely: isolate the host from the network (while maintaining the management connection for continued investigation), terminate a process, quarantine a file, collect a memory dump, or execute a script for remediation. These capabilities allow a Tier 2 analyst to fully investigate and contain an incident without physical access to the affected machine."

---

### [09:00 - 13:00] Key Endpoint Attack Patterns

"Let me walk through the most important endpoint attack patterns that an EDR analyst must recognize, all of which are tested on the CySA+ exam.

Pattern 1: Malicious Office document execution chain. A user opens a Word document. The document contains a macro. The macro spawns winword.exe (the Word process) as a parent, which then spawns cmd.exe or powershell.exe as a child process. This parent-child relationship is highly suspicious — Microsoft Word should almost never be spawning command shells. The EDR process tree makes this immediately visible.

Pattern 2: PowerShell execution with encoded commands. An attacker uses PowerShell with the -EncodedCommand flag to pass a base64-encoded command, bypassing basic script block detection. EDR captures the full command line including the encoded argument. Sysmon Event ID 1 also captures this. The presence of -EncodedCommand or -enc in a PowerShell command line is a high-fidelity indicator.

Pattern 3: LOLBin abuse. Living Off the Land Binaries are legitimate Windows system tools repurposed by attackers. Common examples:
certutil.exe used to decode base64 or download files from the internet
mshta.exe used to execute HTA (HTML Application) payloads
regsvr32.exe used to execute malicious DLLs
rundll32.exe used to execute malicious DLLs
wscript.exe or cscript.exe used to run VBScript or JScript payloads
Detecting LOLBin abuse requires behavioral context — the tool itself is legitimate, but its use in a specific context (unexpected parent, unusual arguments, network connection) reveals the abuse.

Pattern 4: Credential dumping. A process accessing lsass.exe memory (Sysmon Event ID 10), or the use of credential dumping tools like Mimikatz. EDR platforms often have specific detections for these patterns and can alert in real time.

Pattern 5: Persistence establishment. Registry Run key modifications (T1547.001), scheduled task creation (T1053.005), or service installation (T1543.003). EDR captures all of these and can alert specifically when unexpected accounts modify persistence mechanisms."

[SHOW DIAGRAM: Process tree visualization. Root node: explorer.exe (user session). Child node: WINWORD.EXE. Under WINWORD.EXE: cmd.exe (highlighted red — suspicious). Under cmd.exe: powershell.exe -enc [base64 string] (highlighted red — encoded command). Under powershell.exe: svchost32.exe at C:\Users\Public\ (highlighted red — suspicious path). Annotations pointing to each red node: "Word should not spawn cmd.exe," "Encoded command hides payload," "Executable in user-writable path — not a real svchost."]

---

### [13:00 - 16:30] EDR Investigation Workflow

"When an EDR alert fires, the analyst follows an investigation workflow that leverages the platform's telemetry and response capabilities.

Step 1: Triage the alert. The EDR console shows the alert with the triggering event and the endpoint affected. The analyst reviews the alert type, severity, and the specific process or event that triggered it.

Step 2: Examine the process tree. For process-based detections, the process tree shows the parent-child execution chain. The analyst follows the tree up to find the root cause — what was the first suspicious process, and how did it get there?

Step 3: Review the full timeline. The analyst pivots to the full event timeline for the affected host and the relevant time window. They look at file operations, network connections, and registry changes associated with the suspicious process.

Step 4: Check file hashes. If a suspicious file was created, the analyst hashes it and queries the threat intelligence database. A match to a known malware family immediately elevates the incident.

Step 5: Scope the impact. Using the EDR query capabilities, the analyst searches across all endpoints for the same indicator — the same hash, the same process name, the same registry key modification. This determines whether the compromise is isolated to one host or has spread.

Step 6: Contain if confirmed. If the investigation confirms a true positive, the analyst isolates the host via the EDR console (network isolation while maintaining management connectivity) and escalates to Tier 2 for full incident response.

This workflow is tested on the CySA+ exam in scenario format. Know the order: triage, process tree, timeline, hash check, scope, contain."

---

### [16:30 - 19:30] UEBA and Host-Based Indicators

"Modern EDR platforms often include or integrate with User and Entity Behavior Analytics — UEBA. UEBA builds a baseline of normal behavior for each user and entity (host) and alerts when behavior deviates significantly from the baseline.

For example, if a user's account has never logged in outside business hours and never accessed sensitive file shares, a sudden 2 AM login combined with large file share access would be anomalous for that specific user's profile — even if it would not trigger a rule-based alert.

UEBA is particularly valuable for detecting insider threats and account compromise scenarios where the attacker is using legitimate credentials. Rules-based detection struggles with these cases because the credentials and access are technically authorized.

On the CySA+ exam, the distinction between SIEM correlation rules (rule-based detection) and UEBA (behavior-baseline detection) is tested. Know that UEBA detects anomalies specific to individual baselines; SIEM rules detect patterns that match predefined thresholds."

---

### [19:30 - 22:00] XDR — Extended Detection and Response

"Before we close, let me introduce Extended Detection and Response — XDR — because it appears on the CySA+ exam and is increasingly discussed in enterprise security programs.

XDR is an evolution of EDR. While EDR focuses exclusively on endpoint telemetry, XDR integrates telemetry from multiple security layers: endpoints, network, email, cloud, and identity. It correlates events across all of these sources in a unified detection and investigation platform.

The benefit of XDR is a more complete picture of an attack. A phishing email that delivered a malicious attachment (email telemetry) that exploited a vulnerability and established a C2 connection (network telemetry) from a specific endpoint (EDR telemetry) using a compromised account (identity telemetry) is visible as one correlated incident in XDR, rather than separate alerts in separate tools.

For the exam: EDR = endpoint only. XDR = cross-layer, integrates multiple security telemetry sources. Both support detection, investigation, and response. Neither is a replacement for a SIEM — they are complementary."

---

### [22:00 - 24:00] Module Summary and Lab Preview

"Let's bring it together.

Traditional AV uses signature detection. EDR uses behavioral telemetry — process execution, file system, registry, network, memory.

Key EDR capabilities: process tree visualization, file hash checking, remote isolation, cross-endpoint searching.

Key malicious patterns: Office document macro chains, encoded PowerShell, LOLBin abuse, credential dumping, persistence mechanisms.

EDR investigation workflow: triage, process tree, timeline, hash check, scope, contain.

UEBA adds behavioral baseline analytics to detect anomalous individual behavior.

XDR integrates EDR with network, email, cloud, and identity telemetry for unified cross-layer detection.

In the Module 06 lab, you will analyze simulated EDR telemetry — process trees, timeline events, and file operations — to identify attack patterns and classify the activity by ATT&CK technique. Read the Reading Guide first for the LOLBin reference table and process tree analysis examples.

Study resources: professormesser.com and comptia.org. See you in Module 07."

---

End of Module 06 Video Script

Study Resources: comptia.org | professormesser.com
