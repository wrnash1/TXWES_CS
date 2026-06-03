# Video Script: Module 06 — SIEM and Log Analysis

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## SEGMENT 1 — Introduction and Why SIEM Matters (0:00–3:00)

Welcome back to CIS-4332. I'm Professor Nash, and today we're tackling one of the most fundamental tools in a security operations center: the Security Information and Event Management system — SIEM.

If you picture a modern SOC, the analysts are almost certainly staring at a SIEM dashboard. It is the central nervous system of security operations. It collects logs from across the environment, normalizes them into a common format, runs correlation logic to detect threats, and fires alerts that put analysts on the right targets.

Here is the core problem SIEM solves: scale. A mid-sized enterprise generates millions of log events every single day — from firewalls, domain controllers, web servers, cloud platforms, endpoints, and applications. No human can read that volume. SIEM exists to aggregate all of that data, find the signals that matter, and surface them to analysts at machine speed.

The CompTIA CySA+ CS0-003 exam tests SIEM extensively across Domain 1, Security Operations, and Domain 4, Reporting and Communication. By the end of this module you will understand SIEM architecture, log sources and normalization, correlation rules, alert tuning, and the basics of two platforms you will encounter in real SOCs: Splunk and Microsoft Sentinel.

Let's get into it.

---

## SEGMENT 2 — SIEM Architecture (3:00–7:30)

[SHOW TOOL: Architectural diagram with five labeled layers: Collection, Normalization, Correlation, Alerting/SOAR, Storage/Search]

A SIEM has five architectural layers. Understanding how data flows through these layers is essential for the exam and for troubleshooting in production.

### Layer 1 — Log Collection and Ingestion

The SIEM must first receive log data. It uses several mechanisms to do this.

Agents are lightweight software deployed on endpoints and servers. They collect local logs and forward them to the SIEM, typically over an encrypted channel. Agentless collection uses push protocols — syslog over UDP or TCP port 514, Windows Event Forwarding over WinRM, or SNMP from network devices.

API-based connectors are increasingly important for cloud sources. AWS CloudTrail, Microsoft Entra ID (Azure AD), and Okta all expose APIs that SIEM connectors poll on a schedule to retrieve logs.

The SIEM ingestion pipeline handles deduplication, buffering, and flow control to prevent log loss during traffic spikes.

### Layer 2 — Normalization and Parsing

Raw logs from different sources look completely different. A Cisco ASA firewall log uses different field names, formats, and delimiters than a Windows Security event or an Apache web server log. Normalization translates these varied formats into a common schema so the SIEM can compare data across sources.

[SHOW TOOL: Side-by-side of raw syslog vs. normalized event record — field mapping highlighted]

This is where field mapping happens. A source IP might be labeled `src` in a firewall log, `RemoteAddress` in a Windows event, and `c-ip` in an IIS log. After normalization, all three map to the same field in the SIEM's data model. This is what makes cross-source correlation possible.

### Layer 3 — Correlation Engine

The correlation engine is where detection happens. It continuously evaluates incoming events against a library of rules — logical conditions that define suspicious patterns. When a rule's conditions are met, the engine generates an alert. We will spend significant time on correlation rules in Segment 5.

### Layer 4 — Alerting and SOAR Integration

When a correlation rule fires, the SIEM creates a notable event or alert. Modern SIEMs integrate tightly with SOAR platforms — Security Orchestration, Automation, and Response. SOAR can automatically enrich an alert with threat intel lookups, asset data, and user context, create a ticket in ServiceNow or Jira, and trigger a response playbook — all without an analyst touching it.

### Layer 5 — Storage and Search

SIEMs store logs for both real-time investigation and long-term compliance. Retention requirements vary by regulation: PCI DSS requires one year, HIPAA commonly requires six years. Analysts search stored logs during threat hunting and post-incident forensics, sometimes looking back months into historical data.

---

## SEGMENT 3 — Log Sources (7:30–11:30)

[SHOW TOOL: Table of log source categories with examples and key security value]

The value of your SIEM is directly proportional to what you feed it. Let's walk through the most important log sources a security analyst works with.

### Network Logs

Firewall logs record every connection attempt — source IP, destination IP, port, protocol, and whether the traffic was allowed or denied. They are your first line of visibility into what is entering and leaving the network.

Router and switch logs capture routing changes, interface events, and spanning tree activity — useful for detecting network-level anomalies and topology changes.

NetFlow data is flow-level metadata: source, destination, protocol, bytes, and duration, without capturing full packet content. NetFlow is invaluable for detecting large data transfers, beaconing, and lateral movement patterns even when you cannot decrypt the traffic.

DNS logs record every query — what names were resolved, by whom, and when. Attackers use DNS for command and control, and DNS logs are the primary data source for detecting domain generation algorithm traffic and DNS tunneling.

### Endpoint Logs

Windows Security Event Log is one of the most important sources in most enterprise environments. Key event IDs you must know for the exam:

- 4624 — Successful logon
- 4625 — Failed logon
- 4648 — Logon using explicit credentials
- 4672 — Special privileges assigned to new logon
- 4688 — Process creation (requires audit policy enabled)
- 4698 — Scheduled task created
- 4720 — User account created
- 4776 — NTLM authentication attempt

On Linux endpoints, `/var/log/auth.log` captures authentication events. `/var/log/syslog` or `/var/log/messages` captures general system activity. Auditd provides detailed syscall-level logging when configured and is essential for compliance environments.

### Application and Service Logs

Web server logs — Apache, Nginx, IIS — record every HTTP request with client IP, URI, response code, and bytes transferred. These are the primary source for detecting web application attacks.

Database logs capture queries, authentication events, schema changes, and privilege operations. Application-level logs from custom business applications capture business logic events that no network sensor can see.

Authentication platform logs from Active Directory, Okta, Azure AD, and similar identity providers track logins, MFA results, password changes, and account lockouts — essential for detecting credential-based attacks.

### Cloud Logs

[SHOW TOOL: AWS CloudTrail event record — who, what action, what resource, from where]

AWS CloudTrail records every API call made in an AWS account — CreateUser, AttachRolePolicy, DescribeInstances — with the caller identity, source IP, and timestamp. This is the equivalent of a Windows Security Event Log for your cloud infrastructure.

Azure Monitor and Azure Activity Logs serve the same function in Microsoft environments. Google Cloud Audit Logs in GCP. These logs are non-negotiable for cloud security visibility and are increasingly tested on CySA+.

---

## SEGMENT 4 — Log Normalization and Standards (11:30–13:30)

[SHOW TOOL: CEF log format example — header and extension fields labeled]

Since logs look different from every source, the industry has developed normalization standards that SIEMs use internally and that vendors use for log formatting.

Common Event Format, or CEF, was developed by ArcSight and is widely used by security products. A CEF log has a header section with vendor, product, severity, and a message string, followed by key-value extension fields.

The Elastic Common Schema, or ECS, is used by Elastic SIEM. It defines standard field names for common data types — `source.ip`, `destination.port`, `process.name` — so that logs from any source can be queried with the same field names after parsing.

Microsoft Sentinel uses the Advanced Security Information Model, or ASIM, which provides normalization parsers that translate logs from dozens of sources into standardized tables. An ASIM query written against the `NetworkSession` table works regardless of whether the underlying data came from a Palo Alto firewall or an Azure NSG.

Syslog itself is a transport standard — RFC 3164 and RFC 5424 define the format of the PRI (priority/facility), header (timestamp, hostname), and MSG (message content) sections. Understanding syslog structure helps analysts troubleshoot parsing failures and write custom parsers.

---

## SEGMENT 5 — Correlation Rules and Use Case Development (13:30–17:30)

[SHOW TOOL: Correlation rule editor in Splunk ES or Sentinel Analytics rules blade]

Correlation rules are the detection logic of the SIEM. Let's break down what they contain and walk through five concrete examples.

### Anatomy of a Correlation Rule

Every rule has four components:

- A trigger condition — the events or pattern that must occur
- A time window — how long the pattern can span
- A threshold — how many occurrences trigger the rule
- An action — what happens when the rule fires

### Use Case 1 — Brute Force Followed by Success

Trigger: Five or more Windows Event ID 4625 (failed logon) for the same account within two minutes, followed by Event ID 4624 (successful logon) within five minutes.

This detects credential stuffing and password spray attacks that ultimately succeed — the most dangerous kind.

[SHOW TOOL: Splunk SPL query for brute force detection]

```spl
index=wineventlog EventCode=4625
| bucket _time span=2m
| stats count as failures by _time, Account_Name, src_ip
| where failures >= 5
| join type=inner Account_Name
    [search index=wineventlog EventCode=4624 earliest=-7m | table Account_Name]
| table _time, Account_Name, failures, src_ip
```

### Use Case 2 — Impossible Travel

Trigger: A user authenticates successfully from two geographic locations that cannot be physically reached within the time between authentications.

This detects credential compromise even when the password is correct, because the attacker's location is physically impossible.

### Use Case 3 — Privilege Escalation

Trigger: Event ID 4672 (Special Privileges Assigned) for an account not in the domain admin or privileged users group, following a standard-user logon.

### Use Case 4 — Lateral Movement

Trigger: A workstation-class endpoint (not a server) successfully authenticates to more than three other workstations within 15 minutes using NTLM authentication (Logon Type 3).

### Use Case 5 — Data Exfiltration

Trigger: Outbound traffic to a non-corporate IP exceeding 100 MB in one hour from a host whose 30-day average outbound transfer is under 10 MB per hour.

[SHOW TOOL: Microsoft Sentinel KQL query for data exfiltration detection]

```kql
NetworkSessions
| where TimeGenerated > ago(1h)
| where Direction == "Outbound"
| where not(ipv4_is_private(DestinationIp))
| summarize TotalBytes = sum(SentBytes) by SourceIp, DestinationIp
| where TotalBytes > 100000000
| order by TotalBytes desc
```

---

## SEGMENT 6 — Alert Tuning and Noise Reduction (17:30–20:30)

[SHOW TOOL: Graph showing daily alert volume vs. analyst capacity — alert fatigue visualization]

Here is a hard operational truth: most production SIEMs fire thousands of alerts per day. The majority are false positives. Alert fatigue is one of the leading causes of analyst burnout and, more critically, missed real detections. Tuning is not optional — it is a continuous maintenance responsibility.

### The False Positive and False Negative Tradeoff

A false positive is an alert that fires when no real threat exists. A false negative is a real threat that generates no alert. Every tuning decision moves you along this tradeoff curve. Lower your threshold and you catch more threats but generate more false positives. Raise your threshold and you reduce noise but risk missing lower-confidence attacks.

### Tuning Strategies

Allowlisting removes known-good activity from rules. Your vulnerability scanner generates port-scan-like traffic every night at 2 AM. Add the scanner's IP to an exception list so it does not trigger the port scan rule.

Threshold adjustment raises the bar for noisy rules. If a rule fires after two failed logins and your help desk users frequently mistype passwords, raise the threshold to ten or fifteen.

Contextual enrichment adds asset criticality and user risk scores to alerts. The same event from a critical financial server versus a developer sandbox should carry different severity levels.

Suppression windows prevent alerts during scheduled maintenance activities when behavior patterns are abnormal by design.

Scheduled rule review commits your team to a weekly report of the top-ten noisiest rules — adjust thresholds or retire rules that have produced zero true positives in 90 days.

### Key Metrics to Track

- Mean Time to Detect (MTTD) — time from compromise to detection
- Mean Time to Respond (MTTR) — time from detection to containment
- True positive rate per rule
- False positive rate per rule
- Alert-to-incident conversion rate

---

## SEGMENT 7 — Splunk and Microsoft Sentinel Basics (20:30–23:30)

[SHOW TOOL: Splunk Web — Search and Reporting interface with SPL query entered]

### Splunk

Splunk is deployed in a large share of enterprise SOCs. Its query language is SPL — Search Processing Language. Every SPL query starts with a search against an index and then pipes data through transforming commands.

Essential SPL commands to know for CySA+:

- `index=` — which data index to search
- `sourcetype=` — filter by log type
- `stats count by field` — aggregate counts
- `eval field=expression` — create calculated fields
- `rex field=_raw "regex"` — extract fields with regex
- `table field1, field2` — format output columns
- `where condition` — filter results after aggregation
- `timechart` — time-series aggregation for trending

Splunk Enterprise Security adds a Common Information Model (CIM) that normalizes field names across data sources — `src_ip`, `dest_ip`, `user`, `action` — so correlation searches written against the CIM work regardless of the underlying sourcetype.

[SHOW TOOL: Microsoft Sentinel — Analytics rules blade and Log Analytics workspace with KQL query]

### Microsoft Sentinel

Microsoft Sentinel is a cloud-native SIEM/SOAR built on Azure Log Analytics. Its query language is KQL — Kusto Query Language. KQL is a read-only, pipe-based language optimized for log data.

A basic KQL detection query looks like this:

```kql
SecurityEvent
| where EventID == 4625
| where TimeGenerated > ago(24h)
| summarize FailedAttempts = count() by Account, IpAddress
| where FailedAttempts >= 5
| order by FailedAttempts desc
```

Sentinel's strengths include native integration with Microsoft 365 Defender, Entra ID, and Azure Defender, hundreds of pre-built analytics rules mapped to MITRE ATT&CK, Workbooks for visualization, and Playbooks — Azure Logic Apps workflows — for automated response.

---

## SEGMENT 8 — Wrap-Up and CySA+ Alignment (23:30–24:00)

For the CySA+ CS0-003 exam, focus on these key concepts from today.

SIEM collects, normalizes, correlates, and alerts. The five architectural layers are collection, normalization, correlation, alerting/SOAR, and storage.

Log sources: Windows Event IDs 4624, 4625, 4648, 4672, 4688, 4698. Firewall, DNS, NetFlow, cloud API logs. Know what each source provides.

Correlation rules: trigger condition, time window, threshold, action. Know the five use case examples — brute force, impossible travel, privilege escalation, lateral movement, data exfiltration.

Alert tuning: allowlisting, threshold adjustment, contextual enrichment, suppression, scheduled review. The false positive/negative tradeoff is a tested CySA+ concept.

Platforms: Splunk uses SPL; Sentinel uses KQL. Know basic query structure for both.

In the lab this week you will write SPL queries against a sample dataset and analyze a noisy correlation rule, proposing specific tuning changes. Next module we move into Threat Intelligence.

See you there.

---

End of Module 06 Video Script

Total estimated runtime: 22–24 minutes
