# Reading Guide: Module 06 — SIEM and Log Analysis

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4332 &BULL; CYBERSECURITY ANALYST & THREAT HUNTING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Introduction

Security Information and Event Management systems are the operational hub of every mature SOC. A SIEM aggregates log data from hundreds of sources, normalizes it into a common schema, runs detection logic against it in real time, and gives analysts a single pane of glass for investigation and reporting. This guide covers the architecture, log sources, normalization standards, correlation rule design, alert tuning, and the two platforms — Splunk and Microsoft Sentinel — most commonly encountered in enterprise environments and tested on the CySA+ exam.

---

## Section 1 — SIEM Architecture

### 1.1 Five-Layer Architecture Overview

| Layer | Function | Key Components |
|---|---|---|
| Collection / Ingestion | Receive logs from all sources | Agents, syslog forwarders, API connectors, WEF |
| Normalization / Parsing | Convert diverse formats to common schema | Field mapping, CEF/ECS/ASIM parsers |
| Correlation Engine | Apply detection rules to event streams | Rule library, time windows, thresholds |
| Alerting / SOAR | Generate alerts and trigger responses | Notable events, ticketing integration, playbooks |
| Storage / Search | Retain logs for investigation and compliance | Hot/warm/cold storage tiers, index management |

### 1.2 Log Ingestion Methods

| Method | Protocol / Mechanism | Typical Use Case |
|---|---|---|
| Agent-based | Proprietary agent (Splunk UF, Elastic Agent) | Endpoints, servers requiring rich telemetry |
| Syslog push | UDP/TCP port 514, RFC 3164/5424 | Network devices, Linux systems, firewalls |
| Windows Event Forwarding | WinRM / WEF subscriptions | Windows endpoints without agents |
| API polling | REST/OAuth | Cloud services (CloudTrail, Entra ID, Okta) |
| SNMP | SNMP traps | Network devices, legacy infrastructure |
| Database connector | JDBC/ODBC | Database audit logs |

### 1.3 SOAR Integration Points

Modern SIEMs integrate with SOAR platforms (Splunk SOAR, Microsoft Sentinel Playbooks, Palo Alto XSOAR) to automate:

- Threat intelligence enrichment on alert IOCs
- Asset and user context lookup
- Ticket creation in ITSM systems
- Automated containment actions (firewall block, account disable)
- Analyst notification and escalation routing

---

## Section 2 — Log Sources and Their Security Value

### 2.1 Network Log Sources

| Source | Key Fields | Primary Security Use |
|---|---|---|
| Firewall logs | src_ip, dst_ip, port, protocol, action | Perimeter visibility, blocked/allowed traffic analysis |
| DNS logs | query name, query type, response, client IP | C2 detection, DGA detection, DNS tunneling |
| NetFlow / IPFIX | src/dst IP, port, bytes, duration, protocol | Lateral movement, beaconing, data exfiltration volume |
| Proxy logs | URL, user-agent, response code, client IP | Web-based C2, malicious downloads, policy violations |
| IDS/IPS alerts | Signature name, severity, src/dst | Known attack pattern alerting |
| VPN logs | User, source IP, connection time, bytes | Remote access anomalies, split tunneling abuse |

### 2.2 Windows Security Event Log — Critical Event IDs

| Event ID | Event Name | Security Significance |
|---|---|---|
| 4624 | Successful logon | Authentication tracking; logon type reveals method |
| 4625 | Failed logon | Brute force detection; lockout analysis |
| 4648 | Logon with explicit credentials | Pass-the-hash, credential reuse detection |
| 4672 | Special privileges assigned | Privilege escalation detection |
| 4688 | Process creation | Execution chain analysis (requires audit policy) |
| 4698 | Scheduled task created | Persistence mechanism detection |
| 4720 | User account created | Unauthorized account creation |
| 4732 | Member added to security-enabled local group | Privilege escalation via group membership |
| 4756 | Member added to universal security group | Domain-level group escalation |
| 4776 | NTLM authentication | Pass-the-hash, Kerberoasting context |
| 7045 | New service installed | Persistence via service installation |

### 2.3 Logon Type Values (Event ID 4624 / 4625)

| Logon Type | Value | Description | Attack Relevance |
|---|---|---|---|
| Interactive | 2 | Local keyboard logon | Physical access or console session |
| Network | 3 | SMB, WMI, scheduled tasks | Lateral movement via pass-the-hash |
| Batch | 4 | Scheduled task execution | Persistence mechanism activity |
| Service | 5 | Service startup | Service-based persistence |
| RemoteInteractive | 10 | RDP session | RDP-based lateral movement |
| CachedInteractive | 11 | Cached credentials | Offline credential use |

### 2.4 Linux / Unix Log Sources

| Log File | Contents | Key Security Events |
|---|---|---|
| /var/log/auth.log | Authentication events | SSH logins, sudo use, su attempts |
| /var/log/syslog | General system messages | Service starts/stops, kernel messages |
| /var/log/secure | Auth events (RHEL/CentOS) | Same as auth.log on Debian-based |
| /var/log/audit/audit.log | Auditd syscall records | File access, process exec, privilege ops |
| /var/log/faillog | Failed login records | Brute force tracking |
| /var/log/wtmp | Login/logout records | Historical session tracking |

### 2.5 Cloud Log Sources

| Platform | Log Source | What It Records |
|---|---|---|
| AWS | CloudTrail | All API calls: who, what action, what resource, source IP, time |
| AWS | VPC Flow Logs | Network flow metadata (src/dst IP, port, bytes, action) |
| AWS | GuardDuty Findings | Threat detection alerts (brute force, crypto mining, exfiltration) |
| Azure | Activity Log | Control-plane operations in Azure subscription |
| Azure | Entra ID Sign-in Logs | User and service principal authentication with risk scores |
| Azure | Microsoft Defender XDR | Unified security alerts across endpoint, email, identity, cloud |
| GCP | Cloud Audit Logs | Admin activity, data access, system events |

---

## Section 3 — Log Normalization Standards

### 3.1 Normalization Standards Comparison

| Standard | Maintained By | Used In | Key Characteristic |
|---|---|---|---|
| CEF (Common Event Format) | ArcSight / Micro Focus | Many vendor products | Header + key-value extensions; widely supported |
| ECS (Elastic Common Schema) | Elastic | Elastic SIEM / OpenSearch | JSON-based; dotted field hierarchy (source.ip) |
| ASIM (Advanced Security Info Model) | Microsoft | Microsoft Sentinel | KQL parsers; unified tables across diverse sources |
| CIM (Common Information Model) | Splunk | Splunk ES | Field name standards across Splunk data models |
| OCSF (Open Cybersecurity Schema Framework) | OCSF Community | Multi-vendor cloud | JSON; event class taxonomy; AWS, Splunk, CrowdStrike contributors |

### 3.2 Syslog Structure (RFC 5424)

```text
<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID [SD-ID] MSG

Example:
<134>1 2024-11-14T14:22:01.000Z firewall01 cisco-asa 12345 - - \
  %ASA-6-302013: Built outbound TCP connection 12345 for \
  outside:198.51.100.47/4444 (198.51.100.47/4444) to \
  inside:10.0.1.45/52314 (10.0.1.45/52314)

PRI = facility (16) * 8 + severity (6) = 134
Facility 16 = local0
Severity 6 = informational
```

---

## Section 4 — Correlation Rule Design

### 4.1 Rule Components

| Component | Description | Example |
|---|---|---|
| Trigger condition | Event types and field values that must match | EventID=4625 AND Account_Name=X |
| Time window | Maximum span over which events are correlated | Within 2 minutes |
| Threshold | Minimum occurrence count to fire | 5 or more events |
| Grouping key | Field that ties events together | Account_Name, src_ip |
| Action | Alert severity, notification, SOAR trigger | Create critical alert, page on-call |

### 4.2 Common SIEM Use Cases — Detection Patterns

| Use Case | Events Required | Time Window | Threshold | ATT&CK Tactic |
|---|---|---|---|---|
| Brute force + success | 4625 then 4624, same user | 5 minutes | 5 failures | Credential Access |
| Impossible travel | 4624 from two distant geos | 2 hours | N/A — geo distance | Initial Access |
| Privilege escalation | 4624 (std user) then 4672 | 10 minutes | 1 occurrence | Privilege Escalation |
| Lateral movement | 4624 Logon Type 3, NTLM, workstation-to-workstation | 15 minutes | 3+ unique targets | Lateral Movement |
| Data exfiltration | NetFlow outbound bytes to external IP | 1 hour | >100 MB | Exfiltration |
| Account creation | 4720 by non-admin account | Immediate | 1 occurrence | Persistence |
| Scheduled task persistence | 4698 from non-standard process | Immediate | 1 occurrence | Persistence |

### 4.3 Splunk SPL — Key Query Patterns

```spl
# Brute force detection
index=wineventlog EventCode=4625
| bucket _time span=2m
| stats count as failures by _time, Account_Name, src_ip
| where failures >= 5

# Failed then successful login correlation
index=wineventlog (EventCode=4625 OR EventCode=4624)
| eval event_type=if(EventCode==4625,"failure","success")
| stats values(event_type) as types, count by Account_Name, src_ip
| where mvfind(types,"failure") >= 0 AND mvfind(types,"success") >= 0
| table Account_Name, src_ip, types, count

# Outbound DNS query volume (possible DGA or tunneling)
index=dns
| stats count as query_count, dc(query) as unique_domains by src_ip
| where unique_domains > 500
| sort -unique_domains
```

### 4.4 Microsoft Sentinel KQL — Key Query Patterns

```kql
// Brute force detection
SecurityEvent
| where EventID == 4625
| where TimeGenerated > ago(1h)
| summarize FailCount = count() by Account, IpAddress, bin(TimeGenerated, 2m)
| where FailCount >= 5

// Impossible travel — Entra ID sign-ins
SigninLogs
| where ResultType == 0
| summarize Locations = make_set(Location), Times = make_list(TimeGenerated)
    by UserPrincipalName
| where array_length(Locations) > 1

// New admin group member added
SecurityEvent
| where EventID == 4732
| where TargetUserName contains "admin" or TargetUserName contains "Domain Admins"
| project TimeGenerated, SubjectUserName, MemberName, TargetUserName
```

---

## Section 5 — Alert Tuning

### 5.1 Tuning Strategy Reference

| Strategy | Description | Best Applied When |
|---|---|---|
| Allowlisting | Exclude known-good sources or accounts from rules | Scanner IPs, service accounts, scheduled jobs generate consistent noise |
| Threshold adjustment | Raise failure/count threshold to reduce noise | Legitimate users regularly exceed low thresholds |
| Contextual enrichment | Add asset criticality or user risk to alert scoring | Same rule should not generate same severity for all hosts |
| Suppression windows | Disable or lower severity during maintenance | Patch Tuesday, DR testing, business-hours-only rules |
| Rule retirement | Remove rules with zero true positives in 90 days | Regular review process catches dead rules |
| Baseline tuning | Adjust rules based on observed normal behavior | After 30-day observation period in new environments |

### 5.2 Key SOC Metrics

| Metric | Definition | Target |
|---|---|---|
| MTTD | Mean time from compromise to detection | Less than 24 hours (industry goal) |
| MTTR | Mean time from detection to containment | Varies by severity; critical < 4 hours |
| True positive rate | Confirmed incidents / total alerts | As high as possible (>30% is reasonable) |
| False positive rate | False alerts / total alerts | As low as possible; <70% is a common tuning goal |
| Alert-to-incident rate | Alerts escalated to incidents / total alerts | Track trending over time |

---

## Section 6 — Platform Basics

### 6.1 Splunk Architecture

| Component | Role |
|---|---|
| Indexer | Receives, indexes, and stores data |
| Search Head | Runs SPL queries; user interface |
| Forwarder (Universal) | Lightweight log collection agent on endpoints |
| Heavy Forwarder | Parses and filters data before indexing |
| Deployment Server | Manages forwarder configurations centrally |
| Splunk ES | Premium SIEM app; adds correlation searches, CIM, notable events |

### 6.2 Microsoft Sentinel Architecture

| Component | Role |
|---|---|
| Log Analytics Workspace | Underlying data store; KQL query target |
| Data Connectors | Ingest data from Microsoft and third-party sources |
| Analytics Rules | Scheduled KQL queries that generate incidents |
| Incidents | Grouped alerts with investigation workbench |
| Workbooks | Azure Monitor visualization dashboards |
| Playbooks | Azure Logic Apps for automated response |
| ASIM Parsers | Normalize source-specific logs to standard tables |

---

## CySA+ Exam Tips

Exam Tip 1: SIEM normalization enables cross-source correlation. If a question asks why a SIEM can correlate a firewall log with a Windows event, the answer is normalization — field mapping to a common schema.

Exam Tip 2: Know your Windows Event IDs. 4624/4625 (success/fail logon), 4688 (process creation), 4698 (scheduled task), 4672 (special privileges), 4720 (account created) appear regularly in CySA+ scenario questions.

Exam Tip 3: Logon Type 3 (network) is the key indicator for pass-the-hash and lateral movement detection. NTLM + Logon Type 3 from a workstation source is the pattern.

Exam Tip 4: Alert tuning is not about eliminating all false positives — it is about finding the right balance. The exam may ask you to identify the appropriate tuning strategy for a specific noisy-rule scenario.

Exam Tip 5: MTTD and MTTR are both tested metrics. MTTD is a detection quality metric; MTTR is a response capability metric. Understand the difference and how SIEM improvements reduce both.

Exam Tip 6: Splunk uses SPL; Sentinel uses KQL. Both are pipe-based query languages. You do not need to be an expert in either for the exam, but you need to recognize basic query structure.

Exam Tip 7: CEF, ECS, ASIM, and CIM are all normalization schemas. CEF is vendor-neutral and widely used. CIM is Splunk-specific. ASIM is Sentinel-specific. ECS is Elastic-specific.

Exam Tip 8: SOAR integration allows automated enrichment and response triggered by SIEM alerts. The SIEM detects; SOAR acts. Playbooks are the SOAR automation unit in Sentinel.

---

## Glossary

- ASIM: Advanced Security Information Model — Microsoft Sentinel's normalization framework
- CEF: Common Event Format — ArcSight-developed log format standard
- CIM: Common Information Model — Splunk's field normalization standard
- Correlation Rule: Logic definition that triggers an alert when a pattern of events is detected
- ECS: Elastic Common Schema — Elastic's field normalization standard
- False Negative: A real threat that generates no alert
- False Positive: An alert that fires for a non-threatening event
- KQL: Kusto Query Language — Sentinel and Azure Log Analytics query language
- MTTD: Mean Time to Detect — average time from attack start to detection
- MTTR: Mean Time to Respond — average time from detection to containment
- NetFlow: Network flow metadata standard; captures traffic summaries without packet content
- Normalization: Process of mapping log fields from diverse sources to a common schema
- SIEM: Security Information and Event Management — aggregation, correlation, alerting platform
- SOAR: Security Orchestration, Automation, and Response — automated playbook execution
- SPL: Search Processing Language — Splunk's query language
- Syslog: Standard protocol and format for log transmission (RFC 3164, RFC 5424)

---

## Study Checklist

- [ ] Describe the five SIEM architectural layers and what each does
- [ ] List six log ingestion methods and when each is used
- [ ] Identify the security significance of Windows Event IDs 4624, 4625, 4648, 4672, 4688, 4698, 4720
- [ ] Explain Logon Types 2, 3, 10 and their attack relevance
- [ ] Describe four log normalization standards and which platform each belongs to
- [ ] Write a brute-force correlation rule in both SPL and KQL from memory
- [ ] Explain five alert tuning strategies and when to apply each
- [ ] Define MTTD and MTTR and explain how SIEM improvements affect both
- [ ] Describe the architectural components of Splunk and Microsoft Sentinel
- [ ] Review all eight exam tips
- [ ] Complete the Module 06 Lab
- [ ] Complete the Module 06 Quiz
- [ ] Post initial response to the Module 06 Discussion by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Sentinel — KQL Quick Reference and Learning Path**
<https://learn.microsoft.com/en-us/azure/data-explorer/kql-quick-reference>
Microsoft's official KQL quick reference covering query operators, aggregation functions, and time-window operations. The learning path also includes interactive practice environments. Working through KQL exercises is essential for building the query fluency tested in the Module 06 lab and on the CySA+ exam's SIEM scenario questions.

**2. Splunk — SIEM Use Case Library (Splunk Security Essentials)**
<https://splunkbase.splunk.com/app/3435>
Splunk Security Essentials is a free Splunk app providing a library of detection use cases mapped to MITRE ATT&CK. Each use case includes the SPL query, data requirements, and expected alert behavior. Browsing the use cases — even without a running Splunk instance — illustrates how production correlation rules are structured for real-world attack patterns.

**3. CISA — SOAR Capability Fact Sheet**
<https://www.cisa.gov/sites/default/files/publications/CISA_Cyber_Essentials_Toolkit_6.pdf>
CISA's guidance document covering security orchestration and automation for organizations building or maturing SOC capabilities. Reading this alongside Section 7 of this guide reinforces when SOAR automation is appropriate, what tasks are best automated versus reserved for human judgment, and how automation supports faster response metrics.
