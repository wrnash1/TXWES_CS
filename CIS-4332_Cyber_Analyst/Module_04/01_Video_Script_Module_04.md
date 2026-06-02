# Video Script: Module 04 - Log Analysis and SIEM Operations

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20-24 minutes

## CySA+ CS0-003 Domain Alignment: Domain 1 - Security Operations (33%)

---

### [00:00 - 01:30] Introduction

Professor Nash on camera. Title card: Module 04 — Log Analysis and SIEM Operations.

"Welcome to Module 04. Every security analyst's most fundamental daily skill is reading logs. Logs are the raw record of what happened on a system, a network device, or an application. They are the evidence trail that tells you whether something malicious occurred, when it started, what was affected, and how far it spread.

In this module, we cover the anatomy of log entries across the most common source types, how a SIEM collects and correlates those logs, how to write effective SIEM queries, and how to identify suspicious patterns in log data. These skills map directly to Domain 1 of the CySA+ exam and appear in scenario questions throughout the entire exam. Let's get started."

---

### [01:30 - 05:30] Log Sources and Log Formats

"Before you can analyze a log, you need to understand where it came from and what format it uses. Let me walk you through the major log sources a SOC analyst works with every day.

Windows Event Logs are one of the most important sources for endpoint investigation. They are stored locally on Windows systems and use a structured format with an Event ID — a numeric code that identifies exactly what type of event occurred. You need to memorize the most important Windows Event IDs. Let me give you the critical ones:

Event ID 4624 — Successful account logon. This fires every time a user successfully authenticates on a Windows system. Always note the logon type: Type 2 is interactive (local keyboard), Type 3 is network (file share, remote system), Type 10 is RemoteInteractive (RDP).

Event ID 4625 — Failed account logon. A high count of 4625 events from the same source is a brute-force indicator.

Event ID 4648 — Logon using explicit credentials. This fires when a process or user passes specific credentials rather than using the current session token — a common indicator of Pass-the-Hash attacks.

Event ID 4688 — A new process was created. This is your process creation log — essential for detecting malicious execution.

Event ID 4698 — A scheduled task was created. Key for detecting T1053 persistence.

Event ID 4720 — A user account was created. Attackers creating new accounts fire this event.

Event ID 4776 — Domain controller attempted to validate credentials. Fires on NTLM authentication attempts.

Sysmon Events extend Windows logging. Sysmon is a free tool from Microsoft Sysinternals that provides detailed process, network, and file activity logging. Key Sysmon Event IDs:

Sysmon Event ID 1 — Process creation with full command line
Sysmon Event ID 3 — Network connection from a process
Sysmon Event ID 10 — Process access — used to detect LSASS dumping
Sysmon Event ID 11 — File creation
Sysmon Event ID 13 — Registry value set

Linux logs use a different structure. The primary system log is typically at /var/log/syslog or /var/log/messages. Authentication events go to /var/log/auth.log or /var/log/secure. The standard format is: timestamp, hostname, process name, PID, and message. Linux logs use syslog severity levels — Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug.

Firewall logs record connection-level data: source IP, destination IP, source port, destination port, protocol, and action (permit or deny). A firewall log entry tells you what tried to connect to what, not what happened inside the connection.

Authentication logs from Active Directory or LDAP record user login activity centrally. These are invaluable for detecting credential abuse across the environment.

Web server access logs (Apache, Nginx, IIS) record every HTTP request: timestamp, source IP, HTTP method, requested URL, HTTP status code, and response size. These are essential for detecting web application attacks."

---

### [05:30 - 09:30] How a SIEM Works

"Now let's talk about how all of these logs get consolidated and turned into actionable alerts.

The SIEM — Security Information and Event Management — is the centralized platform that collects, normalizes, correlates, and alerts on log data. Let me walk through the SIEM pipeline.

Step 1: Log collection. Agents on endpoints forward logs to the SIEM in real time. Network devices use syslog protocol to forward logs. Cloud environments use API connectors. The goal is to get logs off the source system as fast as possible — if an attacker deletes local logs, the SIEM copy is preserved.

Step 2: Normalization. Different log sources use different formats — Windows uses XML, Linux uses syslog text, firewalls use proprietary formats. The SIEM normalizes all of these into a common schema, mapping fields from different sources to standard names. Source IP, destination IP, user, action — these become consistent field names regardless of which source produced the log.

Step 3: Correlation. Correlation rules are the intelligence layer of the SIEM. A correlation rule says: if events matching condition A are followed by events matching condition B within a defined time window and from the same source, generate an alert. Example: if more than 10 failed logon events for the same username occur within 5 minutes, followed by a successful logon, fire a Brute Force Success alert.

Step 4: Alerting. When a correlation rule fires, the SIEM generates an alert with the supporting log evidence attached. The alert appears in the analyst queue.

Step 5: Investigation. The analyst queries the SIEM to pull additional context — the full timeline around the event, other activity from the same source, related events on other systems.

The SIEM does not block traffic. It detects and alerts. Automated response (blocking, isolation) requires integration with an EDR or SOAR platform acting on SIEM output."

[SHOW SCREEN: Mock SIEM dashboard. Left panel: Alert Queue showing 5 alerts with severity badges (2 High, 2 Medium, 1 Low). Center: Log Source Health indicator — Firewall green, AD green, Endpoint green, DNS yellow (warning). Right panel: Top Source IPs bar chart and Authentication Failures Over Time line graph with a visible spike.]

---

### [09:30 - 13:00] Writing SIEM Queries

"Writing effective SIEM queries is a core analyst skill. Different SIEM platforms use different query languages. Splunk uses SPL — Search Processing Language. Elastic uses KQL — Kibana Query Language. Microsoft Sentinel uses KQL — Kusto Query Language. The CySA+ exam is platform-agnostic, but you should understand the concepts that apply to all of them.

Every SIEM query has three components: the search scope (what index or data source), the filter conditions (what events you want), and the analysis operations (counting, grouping, sorting).

Let me walk through several practical query examples.

Query 1 — Find all failed authentication events in the last 24 hours grouped by username:

In Splunk SPL, this looks like:
index=wineventlog EventCode=4625 earliest=-24h
pipe stats count by TargetUserName
pipe sort -count

What this does: searches the Windows Event Log index for Event ID 4625 (failed logon) in the last 24 hours, counts how many failed attempts there are per username, and sorts from most to least. A username with 500 failures in 24 hours is a brute-force target.

Query 2 — Detect brute-force success: multiple failures from the same IP followed by success:

index=wineventlog (EventCode=4625 OR EventCode=4624) earliest=-1h
pipe stats values(EventCode) as events, count by src_ip, TargetUserName
pipe where mvcount(events) > 1 AND count > 10

This finds source IPs where both failure (4625) and success (4624) events appear for the same username, with more than 10 total events.

Query 3 — Identify processes with network connections not seen before (baseline deviation):

index=sysmon EventCode=3 earliest=-24h
pipe stats count by Image, dest_ip
pipe where Image IN (list of known-safe binaries) NOT match
pipe sort -count

This looks for new outbound network connections from known-but-unusual processes.

The key discipline for query writing is starting broad and narrowing. Begin with a wide time window and basic filter. Review the results. Add conditions to remove known-good activity. This iterative process is called search refinement."

---

### [13:00 - 16:30] Identifying Suspicious Patterns

"Now let me walk you through the most important suspicious log patterns that a CySA+ exam question might present.

Pattern 1: Brute-force authentication attack. Dozens to hundreds of Event ID 4625 failures for the same account from the same source IP, potentially followed by a 4624 success. The key indicator is the volume and velocity — legitimate failed logins are scattered; brute-force events are dense and rapid.

Pattern 2: Pass-the-Hash. Event ID 4648 — explicit credential use — followed by network logon events (logon type 3) on multiple systems. The attacker is using a captured credential hash to authenticate laterally without knowing the plaintext password.

Pattern 3: Scheduled task persistence. Event ID 4698 — new scheduled task created — especially by a non-admin account, or for a task name that mimics a legitimate Windows task name. Check the command line executed by the task.

Pattern 4: LSASS credential dumping. Sysmon Event ID 10 with TargetImage matching lsass.exe. The SourceImage is the process accessing LSASS — if it is something unexpected like cmd.exe, powershell.exe, or a suspicious executable, this is a credential dumping attempt.

Pattern 5: Beaconing. A host making regular outbound connections to the same external IP at consistent intervals — every 30 seconds, every 5 minutes, every hour. This regularity is characteristic of malware communicating with a command-and-control server. Human traffic is irregular; beaconing is not.

Pattern 6: Data staging and exfiltration. Large file transfers from a database server or file share to a single workstation (collection), followed by large outbound transfers from that workstation to an external IP (exfiltration). Look for unusually large DNS queries or HTTPS POST requests.

Pattern 7: Lateral movement with RDP. Event ID 4624 logon type 10 (RemoteInteractive) on multiple internal systems in sequence, using the same credentials. An attacker pivoting from one system to others via RDP leaves a chain of Type 10 logon events."

---

### [16:30 - 19:30] Log Integrity and Retention

"Two operational topics that appear on the CySA+ exam: log integrity and log retention.

Log integrity is the assurance that log records have not been tampered with. An attacker who gains system access will often try to delete or modify local logs to cover their tracks. Controls for log integrity include:

Forwarding logs in real time to a remote, centralized, write-protected SIEM — once the log entry is transmitted off the source system, a local deletion does not erase the SIEM copy.

Using a write-once storage or append-only log sink — some environments send logs to storage where entries can be added but not modified or deleted.

Cryptographic log signing — each log entry is signed at the time of creation; signature validation detects tampering.

Log retention is the policy governing how long logs are kept. Retention requirements vary by regulation and by incident investigation needs. General guidance for the exam: Authentication and access logs — minimum 90 days to 1 year. Security-relevant logs (SIEM events, firewall logs, endpoint security events) — 1 year is a common standard. Some regulations require longer: PCI DSS requires 12 months online with 3 months immediately available. HIPAA does not specify log retention but requires 6-year retention of security documentation.

Short retention windows are a significant investigation problem. If an incident is discovered months after it occurred, log data that was deleted before the investigation began may make it impossible to reconstruct the attack timeline."

---

### [19:30 - 22:00] SIEM Use Cases and Exam Tips

"Let me close with practical SIEM use cases and key exam tips.

Common SIEM use cases beyond alert generation:

Threat hunting — analysts query the SIEM proactively looking for indicators of techniques that haven't triggered a rule yet. We cover this in depth in Module 14.

Compliance reporting — the SIEM can produce automated reports showing that all required log sources are active, that access to privileged systems is logged, and that sensitive data handling is monitored.

Incident investigation — after an incident is detected, analysts use the SIEM to reconstruct the timeline, identify all affected systems, and determine the full scope of the breach.

Baseline comparison — analyzing historical data to understand normal behavior so that deviations are more visible.

Exam tips specific to this module:

Know the Windows Event IDs I gave you. They appear directly in CySA+ scenario questions. You will see a log entry and be asked to identify what it means or what attack it indicates.

Know that the SIEM normalizes logs but does not change the original log content — normalization maps fields to standard names while preserving the original data.

Know that log retention is a compliance and investigation requirement, not just a storage question.

For study resources: comptia.org for the official exam objectives, and professormesser.com for free video content mapped to every CS0-003 objective."

---

### [22:00 - 24:00] Module Summary and Lab Preview

"Let's summarize Module 04.

Logs are the primary evidence source in security analysis. Major sources include Windows Event Logs, Sysmon, Linux syslog, firewall logs, authentication logs, and web server access logs.

Key Windows Event IDs: 4624 (successful logon), 4625 (failed logon), 4648 (explicit credentials), 4688 (process creation), 4698 (scheduled task), 4720 (account creation), and Sysmon 10 (process access — LSASS).

The SIEM pipeline: collection, normalization, correlation, alerting, investigation.

Suspicious patterns: brute-force, Pass-the-Hash, scheduled task persistence, LSASS dumping, beaconing, data staging, RDP lateral movement.

Log integrity and retention are operational and compliance requirements.

In the Module 04 lab, you will receive sample log entries for multiple source types, identify suspicious patterns, and write SIEM queries targeting those patterns. This is the core hands-on skill of a Tier 1 analyst. Read the Reading Guide first for the full event ID reference table and query syntax examples.

See you in Module 05."

---

End of Module 04 Video Script

Study Resources: comptia.org | professormesser.com
