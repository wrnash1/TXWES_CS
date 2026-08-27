# Reading Guide: Module 04 - Log Analysis and SIEM Operations

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Introduction

Log analysis is the daily operational core of SOC work. Every threat detection, every incident investigation, and every compliance audit depends on the quality and completeness of log data. This module builds the reference foundation you need to read logs fluently, write effective SIEM queries, and recognize suspicious patterns across multiple log sources. The Windows Event ID table and SIEM query examples in this guide are your primary working references for the Module 04 lab.

---

## Section 1: Windows Event Log Reference

### 1.1 Critical Windows Security Event IDs

Memorize these Event IDs. They appear directly in CySA+ scenario questions where you are given a log entry and asked to identify the event type or the attack it indicates.

| Event ID | Name | Security Significance |
|---|---|---|
| 4624 | Successful account logon | Baseline authentication event; logon type field is critical (see 1.2) |
| 4625 | Failed account logon | High volume = brute-force indicator; source IP is key field |
| 4627 | Group membership information during logon | Reveals privilege context of authenticated session |
| 4648 | Logon using explicit credentials | Attacker passing harvested credentials; indicator of Pass-the-Hash or credential abuse |
| 4657 | Registry value modified | Detect registry-based persistence (T1547) |
| 4672 | Special privileges assigned to new logon | Detects privileged logon; fires for admin and service accounts |
| 4688 | Process creation | Key for detecting malicious execution; includes command-line (if auditing enabled) |
| 4698 | Scheduled task created | Persistence detection — T1053.005 |
| 4702 | Scheduled task modified | Task modification for persistence or execution change |
| 4720 | User account created | Detect attacker-created accounts |
| 4722 | User account enabled | May indicate reactivation of dormant account for persistence |
| 4732 | User added to security-enabled local group | Detect privilege escalation via group membership |
| 4740 | User account locked out | Indicator of brute-force attack; account lockout policy triggered |
| 4756 | User added to universal security group | Domain-level group membership change |
| 4776 | NTLM credential validation | Pass-the-Hash; NTLM authentication events |
| 7045 | Service installed | Persistence via service creation (T1543.003) |

### 1.2 Windows Logon Types

The Logon Type field in Event ID 4624 and 4625 identifies how the authentication occurred.

| Logon Type | Code | Description | Security Relevance |
|---|---|---|---|
| Interactive | 2 | Local keyboard and screen logon | Normal user activity at physical workstation |
| Network | 3 | Remote file share, SMB, or mapped drive | Common in lateral movement; Pass-the-Hash traffic |
| Batch | 4 | Scheduled task or batch job | Normal for automated tasks; flag unexpected accounts |
| Service | 5 | Service account logon | Normal; flag if service account name is unexpected |
| Unlock | 7 | Workstation screen unlock | Normal user activity |
| NetworkCleartext | 8 | Cleartext password over network | Legacy; indicates potential credential exposure |
| Interactive (new credentials) | 9 | Runas with different credentials | Credential use indicator |
| RemoteInteractive | 10 | RDP session | Key lateral movement indicator; trace RDP chains |
| CachedInteractive | 11 | Logon using cached domain credentials | Offline logon; may indicate disconnected system |

### 1.3 Sysmon Event IDs

Sysmon (System Monitor) provides detailed Windows telemetry beyond native Event Log. Key event IDs:

| Sysmon Event ID | Name | Security Use |
|---|---|---|
| 1 | Process creation | Full command line including arguments; detect LOLBins and encoded commands |
| 2 | File creation time changed | Anti-forensic timestamp manipulation |
| 3 | Network connection | Outbound connections from processes; detect C2 beaconing |
| 8 | CreateRemoteThread | Code injection detection |
| 10 | Process access | LSASS memory access — detect T1003.001 credential dumping |
| 11 | File created | File drop detection |
| 12/13/14 | Registry object create/modify/delete | Registry persistence detection |
| 22 | DNS query | Domain lookups by process; detect DGA and C2 domains |

---

## Section 2: Linux and Syslog Reference

### 2.1 Key Linux Log Files

| Log File | Contents | Key Events |
|---|---|---|
| /var/log/auth.log (Debian/Ubuntu) | Authentication and sudo events | SSH logins, su, sudo, PAM failures |
| /var/log/secure (RHEL/CentOS) | Same as auth.log for RHEL systems | SSH logins, sudo, PAM failures |
| /var/log/syslog | General system messages | Service starts/stops, kernel messages |
| /var/log/messages | Same as syslog on some distributions | General system activity |
| /var/log/cron | Cron job execution | Scheduled job persistence detection |
| /var/log/apache2/access.log | Web server access events | HTTP requests, status codes, source IPs |
| /var/log/nginx/access.log | Nginx access events | Same fields as Apache |
| /var/log/audit/audit.log | Linux Audit Daemon events | System call auditing, file access, privilege use |

### 2.2 Syslog Severity Levels

| Level | Code | Description |
|---|---|---|
| Emergency | 0 | System is unusable |
| Alert | 1 | Action must be taken immediately |
| Critical | 2 | Critical conditions |
| Error | 3 | Error conditions |
| Warning | 4 | Warning conditions |
| Notice | 5 | Normal but significant condition |
| Informational | 6 | Informational messages |
| Debug | 7 | Debug-level messages |

### 2.3 Sample Linux Auth Log Entry

```text
Nov 14 02:17:43 webserver-prod-01 sshd[12345]: Failed password for svc_deploy
    from 203.0.113.47 port 51234 ssh2
Nov 14 02:17:51 webserver-prod-01 sshd[12346]: Accepted password for svc_deploy
    from 203.0.113.47 port 51235 ssh2
```

Fields: timestamp, hostname, process[PID], event message with username, source IP, source port, protocol.

---

## Section 3: Firewall Log Reference

### 3.1 Firewall Log Fields

| Field | Description | Security Use |
|---|---|---|
| Timestamp | Date and time of connection | Timeline construction |
| Source IP | Originating IP address | Attacker IP, internal host pivot |
| Destination IP | Target IP address | Attack target identification |
| Source Port | Originating port | Ephemeral port; helps trace sessions |
| Destination Port | Target service port | Identifies service being targeted |
| Protocol | TCP, UDP, ICMP | Protocol anomaly detection |
| Action | Permit, Deny, Drop | Blocked vs. allowed traffic |
| Interface | Network interface | Ingress/egress direction |
| Bytes | Data transferred | Large transfers = possible exfiltration |

### 3.2 Sample Firewall Log Entry (Generic Format)

```text
2024-11-14T02:15:00Z DENY TCP 203.0.113.47:51100 -> 10.10.5.22:22 [POLICY:EXTERNAL_BLOCK]
2024-11-14T02:15:01Z DENY TCP 203.0.113.47:51101 -> 10.10.5.22:22 [POLICY:EXTERNAL_BLOCK]
2024-11-14T02:17:43Z PERMIT TCP 203.0.113.47:51235 -> 10.10.5.22:22 [POLICY:EXTERNAL_ALLOW]
```

A sequence of DENY entries from the same source to the same destination followed by a PERMIT is a classic brute-force firewall signature.

---

## Section 4: Web Server Access Log Reference

### 4.1 Apache/Nginx Combined Log Format

```text
203.0.113.47 - - [14/Nov/2024:02:19:01 +0000] "GET /admin/config.php HTTP/1.1"
    404 512 "-" "sqlmap/1.7.8#stable (https://sqlmap.org)"
```

Fields in order: client IP, ident (usually -), auth user (usually -), timestamp, request line (method URL protocol), HTTP status code, response bytes, referer, user-agent.

### 4.2 HTTP Status Codes — Security Significance

| Code | Meaning | Security Significance |
|---|---|---|
| 200 | OK | Successful request |
| 301/302 | Redirect | May indicate redirect hijacking or phishing infrastructure |
| 400 | Bad Request | Malformed requests; may indicate fuzzing or scanning |
| 401 | Unauthorized | Authentication failure; brute force or credential stuffing |
| 403 | Forbidden | Authorization failure; directory traversal attempts |
| 404 | Not Found | Scanning for files/directories that don't exist |
| 500 | Internal Server Error | Application crash; may indicate successful injection |
| 503 | Service Unavailable | DDoS impact or resource exhaustion |

### 4.3 Suspicious Web Log Patterns

A spike in 404 responses from a single IP often indicates directory enumeration or scanning. SQL injection attempts appear in the URL as encoded characters or SQL keywords. User-agent strings containing scanner names (sqlmap, nikto, nmap, dirb) identify automated attack tools. A single IP responsible for a large percentage of all requests suggests DoS or automated attack activity.

---

## Section 5: SIEM Operations

### 5.1 SIEM Pipeline

| Stage | Function |
|---|---|
| Collection | Agents, syslog, API connectors gather logs from all sources |
| Normalization | Maps diverse log formats to a common schema with standard field names |
| Correlation | Rules compare events across sources and time windows to detect patterns |
| Alerting | Generates analyst-visible alerts when correlation rules fire |
| Investigation | Analyst queries SIEM for additional context around alerts |
| Retention | Logs stored for compliance and investigation requirements |

### 5.2 SIEM Query Syntax — Splunk SPL

Failed logins in last 24 hours by source IP:

```splunk
index=wineventlog EventCode=4625 earliest=-24h
| stats count by src_ip, TargetUserName
| where count > 10
| sort -count
```

Brute-force success — failure followed by success, same user same IP:

```splunk
index=wineventlog (EventCode=4624 OR EventCode=4625) earliest=-1h
| stats values(EventCode) as codes, count by src_ip, TargetUserName
| where mvcount(codes) > 1 AND mvfind(codes, "4624") >= 0 AND count > 5
| table src_ip, TargetUserName, codes, count
```

Scheduled task creation by non-system account:

```splunk
index=wineventlog EventCode=4698 earliest=-24h
| where SubjectUserName != "SYSTEM" AND SubjectUserName != "LOCAL SERVICE"
| table _time, ComputerName, TaskName, SubjectUserName
```

LSASS access detection (Sysmon):

```splunk
index=sysmon EventCode=10 TargetImage="*\\lsass.exe"
| stats count by SourceImage, GrantedAccess, ComputerName
| sort -count
```

DNS queries to long or randomized domain names (potential DGA):

```splunk
index=dns query_length > 30
| stats count by query, src_ip
| where count < 3
| sort -query_length
```

Beaconing detection — regular interval outbound connections:

```splunk
index=network dest_zone=external earliest=-4h
| bin _time span=5m
| stats count by src_ip, dest_ip, _time
| streamstats window=6 global=f stdev(count) as dev by src_ip, dest_ip
| where dev < 1.0
| table src_ip, dest_ip, count, dev
```

### 5.3 SIEM Correlation Rule Concepts

A correlation rule consists of:

- Event criteria: what log events match (field values, event codes)
- Threshold: how many matching events trigger the rule
- Time window: the period within which the events must occur
- Grouping: which field ties events together (same source IP, same username)
- Alert severity: how the resulting alert is classified

Example rule logic in plain language: "If more than 10 Event ID 4625 events occur for the same TargetUserName from the same source IP within 5 minutes, generate a HIGH severity alert titled 'Brute Force Attempt.'"

---

## Section 6: Log Integrity and Retention

### 6.1 Log Integrity Controls

| Control | Description | Protection Provided |
|---|---|---|
| Real-time forwarding to SIEM | Logs sent off-system immediately | Attacker cannot delete SIEM copy by compromising source |
| Write-once storage | Log sink that permits writes but not modifications | Tamper evidence; integrity assurance |
| Cryptographic signing | Each entry signed at creation | Detects any modification after the fact |
| NTP synchronization | All systems synchronized to common time source | Enables accurate timeline reconstruction across sources |

### 6.2 Log Retention Standards

| Regulation/Standard | Log Retention Requirement |
|---|---|
| PCI DSS 4.0 | 12 months total; 3 months must be immediately available |
| HIPAA | 6 years for security documentation; no explicit log period specified |
| NIST SP 800-92 | Context-dependent; recommends 1-3 years for security logs |
| SOC 2 Type II | Evidence of monitoring must be retained for audit period (typically 12 months) |
| GDPR | Logs containing personal data governed by data minimization and purpose limitation |

---

## Section 7: IOC Types in Log Context

| IOC Type | Log Source | What to Look For |
|---|---|---|
| Malicious IP | Firewall, web server, DNS | Source or destination matching known-bad IPs |
| Malicious domain | DNS logs, proxy logs | Queries to DGA domains, newly registered domains, known-bad domains |
| Suspicious user agent | Web server access log | Scanner tool signatures, unusual browser strings |
| Unusual process | Windows Event 4688, Sysmon 1 | LOLBins in unexpected contexts, encoded commands |
| Credential abuse | Windows Event 4624/4625/4648 | Off-hours logons, unexpected logon types, lateral movement chains |
| File hash | EDR telemetry, Sysmon 11 | Known-malicious hash matches in file creation events |

---

## CySA+ Exam Tips

Exam Tip 1: Memorize Windows Event IDs 4624, 4625, 4648, 4688, 4698, 4720, and 4776. These appear in scenario questions where you identify what an event indicates.

Exam Tip 2: Logon Type 3 (Network) is associated with lateral movement and Pass-the-Hash. Logon Type 10 (RemoteInteractive) is RDP. Know both.

Exam Tip 3: The SIEM normalizes log formats but does not modify original log content. Normalization maps fields to common names.

Exam Tip 4: High-volume Event ID 4625 events from the same IP in a short time window = brute-force indicator. The volume and velocity are the key tells.

Exam Tip 5: Sysmon Event ID 10 targeting lsass.exe indicates credential dumping (T1003.001). This is one of the most common exam scenario patterns.

Exam Tip 6: Log retention is a compliance requirement. PCI DSS 12-month retention with 3-month immediate availability is the most commonly tested regulatory requirement.

Exam Tip 7: Real-time log forwarding to a centralized SIEM is the primary control against log deletion by attackers. Once a log entry is in the SIEM, deleting it from the source system does not remove it from the investigation record.

Exam Tip 8: Beaconing is characterized by regular, repetitive outbound connections to the same external destination at consistent time intervals. This regularity distinguishes it from normal human-generated traffic.

---

## Glossary

- Beaconing: Regular, automated outbound communications from malware to a C2 server at consistent intervals
- Correlation Rule: SIEM logic that fires an alert when multiple events match defined conditions within a time window
- Event ID: Numeric code identifying a specific type of Windows log event
- LOLBin: Living Off the Land Binary; legitimate system tool used by attackers to avoid detection
- Logon Type: Field in Windows Event 4624/4625 identifying the authentication method used
- Normalization: SIEM process of mapping diverse log formats to a common schema
- Pass-the-Hash: Authentication attack using a captured NTLM hash without knowing the plaintext password
- Sysmon: Microsoft Sysinternals System Monitor; provides detailed Windows process and network telemetry
- SIEM: Security Information and Event Management; centralizes logs, applies correlation, and generates alerts
- SPL: Splunk Processing Language; query language used in Splunk SIEM
- Syslog: Standard protocol for forwarding log messages from network devices and Linux systems

---

## Required Resources

- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com

---

## Study Checklist

- [ ] Recite the 16 Windows Event IDs in the reference table with their event names without notes
- [ ] Identify the security significance of Logon Types 2, 3, 8, 9, 10 from memory
- [ ] List the key Sysmon Event IDs and their detection use cases
- [ ] Read and interpret a sample Linux auth log entry correctly
- [ ] List all firewall log fields and explain their security significance
- [ ] Interpret HTTP status codes from a web server access log for security relevance
- [ ] Describe the five SIEM pipeline stages in order
- [ ] Read and explain each of the six SPL query examples in Section 5.2
- [ ] Explain how correlation rules work: criteria, threshold, time window, grouping
- [ ] Describe log integrity controls and why real-time forwarding is the primary defense against log deletion
- [ ] State PCI DSS log retention requirements
- [ ] Review all eight exam tips
- [ ] Complete the Module 04 Lab
- [ ] Complete the Module 04 Quiz
- [ ] Post initial response to the Module 04 Discussion board by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft — Windows Security Event Log Reference (Event IDs)**
<https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/security-auditing-overview>
Microsoft's official documentation for Windows Security Event IDs, audit policy categories, and log field definitions. Use this as a reference when working through the Event ID table in Section 1 — each link leads to a detailed description of the event's fields, trigger conditions, and recommended monitoring guidance.

**2. Florian Roth — Sigma Rules Repository (GitHub)**
<https://github.com/SigmaHQ/sigma>
Sigma is the open-source standard for writing SIEM-agnostic detection rules. The repository contains hundreds of community-contributed rules mapped to MITRE ATT&CK techniques. Reviewing a few rules for techniques you know (e.g., T1059.001 PowerShell, T1547.001 Registry Run Keys) illustrates how the log analysis concepts in this module translate into production detection logic.

**3. Splunk — Search Tutorial and SPL Quick Reference**
<https://docs.splunk.com/Documentation/Splunk/latest/SearchTutorial/WelcometotheSearchTutorial>
Splunk's free interactive search tutorial walks through SPL query construction from basic keyword searches to stats, eval, and transaction commands. Even without a Splunk license, working through the tutorial exercises reinforces the query patterns covered in Section 5 of this guide.
