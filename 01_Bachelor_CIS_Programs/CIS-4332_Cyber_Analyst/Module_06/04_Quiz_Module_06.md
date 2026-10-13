# Quiz: Module 06 — SIEM and Log Analysis

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer.

---

## Question 1

A SIEM receives log data from a Palo Alto firewall that labels the originating IP as `src`, from a Windows domain controller that labels it as `IpAddress`, and from a Linux server that labels it as `client_ip`. After ingestion, all three appear as the same field name in SIEM queries. Which SIEM process is responsible for this?

- A) Log compression, which removes duplicate field names to reduce storage
- B) Normalization, which maps diverse source-specific field names to a common schema
- C) Deduplication, which merges events from different sources that share the same IP address
- D) Correlation, which joins events from multiple sources based on matching IP values

Correct Answer: B

Distractor Analysis:

- A is incorrect. Log compression reduces storage size; it does not change field naming conventions or enable cross-source field mapping.
- B is correct. Normalization (also called field mapping or parsing) is the SIEM process that translates source-specific field names into a common schema. After normalization, `src`, `IpAddress`, and `client_ip` all map to a standardized field such as `src_ip` or `source.ip`, enabling queries and correlation rules to work uniformly across all sources.
- C is incorrect. Deduplication removes duplicate events — identical events received multiple times. It does not perform field name translation.
- D is incorrect. Correlation applies detection logic to find patterns across events. It depends on normalized fields already being in place, but it does not perform the field mapping itself.

---

## Question 2

A SOC analyst needs to detect lateral movement where an attacker is using stolen NTLM credentials to authenticate to multiple workstations. Which Windows Security Event ID and Logon Type combination provides the most direct evidence of this activity?

- A) Event ID 4624, Logon Type 2 (Interactive)
- B) Event ID 4625, Logon Type 10 (RemoteInteractive)
- C) Event ID 4624, Logon Type 3 (Network) with NTLM authentication
- D) Event ID 4688 (Process Creation) with `net.exe` as the created process

Correct Answer: C

Distractor Analysis:

- A is incorrect. Logon Type 2 is an interactive (local keyboard) logon. It indicates physical or console access, not network-based lateral movement using pass-the-hash techniques.
- B is incorrect. Event ID 4625 is a failed logon — it would not represent a successful lateral movement authentication. Logon Type 10 is RDP; while RDP lateral movement exists, it is not the primary indicator for pass-the-hash patterns, which use NTLM over network logons.
- C is correct. Pass-the-hash lateral movement generates Event ID 4624 (successful logon) with Logon Type 3 (network authentication) using NTLM. A workstation-class host generating multiple Type 3 NTLM logins to other workstations within a short time window is a high-fidelity lateral movement indicator detectable in SIEM correlation rules.
- D is incorrect. Event ID 4688 with `net.exe` shows a command being run — it might indicate reconnaissance or lateral movement tool use, but it does not directly evidence the authentication event that constitutes lateral movement itself.

---

## Question 3

An analyst reviews a SIEM alert: five failed login attempts (Event ID 4625) for `admin@corp.local` in two minutes, followed immediately by a successful login (Event ID 4624) from the same source IP. The source IP belongs to the organization's automated password-reset testing tool. How should the analyst classify this alert?

- A) True positive — any brute force against an admin account is a confirmed threat regardless of source
- B) False positive — the alert fired correctly based on its rule logic but the source is a known legitimate automated tool
- C) False negative — the alert should not have fired because the source IP is known good
- D) True negative — no attack occurred and no alert fired

Correct Answer: B

Distractor Analysis:

- A is incorrect. True positive means the alert indicates a real threat. A known automated password-reset tool performing its designed function is not a threat, even if it triggers the rule's threshold. Classifying all admin account alerts as TPs regardless of context would generate unsustainable workload.
- B is correct. This is a false positive — the correlation rule fired correctly based on its logic (five failures followed by success), but the underlying activity is benign. The appropriate tuning action is to allowlist the password-reset tool's IP address in the rule. This is a classic example of why tuning and context enrichment are necessary.
- C is incorrect. "False negative" means a real threat was not detected. In this case an alert did fire — so it cannot be a false negative. The source being legitimate does not make it a false negative; it makes the fired alert a false positive.
- D is incorrect. True negative means no alert fired and no attack occurred. An alert did fire in this scenario, so it cannot be a true negative regardless of whether the activity was benign.

---

## Question 4

A company's SIEM currently has a correlation rule that fires 600 alerts per day with a true positive rate of 1%. The SOC manager wants to reduce alert volume while maintaining detection capability. Which two tuning actions would most directly reduce false positive volume without eliminating true positive detection?

- A) Delete the rule entirely and rely on manual log review
- B) Raise the event threshold and add allowlist entries for known-good sources
- C) Lower the event threshold to generate more alerts and increase true positive catch rate
- D) Disable the SIEM's normalization to reduce event processing overhead

Correct Answer: B

Distractor Analysis:

- A is incorrect. Deleting the rule eliminates both false positives and true positives. This is not a tuning action — it is rule retirement, which may be appropriate in some cases but is not a strategy for maintaining detection capability.
- B is correct. Raising the threshold reduces noise from low-count events that represent normal behavior. Adding allowlist entries for known-good sources (scanner IPs, service accounts, backup systems) removes the most common false positive sources. Together, these two actions address the most common causes of excessive false positive volume.
- C is incorrect. Lowering the threshold would generate even more alerts and increase the false positive rate, making the problem worse. Generating more alerts does not improve the true positive catch rate — it increases noise.
- D is incorrect. Normalization is what makes correlation possible across diverse log sources. Disabling normalization would break detection, not improve alert quality.

---

## Question 5

Which of the following best describes the purpose of integrating a SOAR platform with a SIEM?

- A) SOAR replaces the SIEM's storage layer, reducing infrastructure costs
- B) SOAR automatically enriches alerts, creates tickets, and executes response playbooks triggered by SIEM alerts, reducing analyst manual workload
- C) SOAR converts SIEM logs into normalized CEF format for long-term archival
- D) SOAR provides the underlying correlation engine that the SIEM queries for detection rules

Correct Answer: B

Distractor Analysis:

- A is incorrect. SOAR does not replace SIEM storage. They are separate platform categories — SIEM handles data collection, normalization, and correlation; SOAR handles response orchestration.
- B is correct. SOAR (Security Orchestration, Automation, and Response) integrates with SIEM alerts as triggers. When a SIEM alert fires, SOAR can automatically look up threat intel on IOCs, pull asset context from a CMDB, create a ticket in ServiceNow, block a firewall rule, and notify the on-call analyst — all without human action. This dramatically reduces MTTD and MTTR.
- C is incorrect. Log normalization is performed by the SIEM ingestion pipeline, not SOAR. CEF conversion is a log formatting step during collection, not SOAR's function.
- D is incorrect. The SIEM contains its own correlation engine. SOAR does not provide the detection logic — it provides the response automation layer that acts on what the SIEM detects.

---

## Question 6

An analyst is writing a Splunk SPL query to identify workstations that made DNS queries to more than 500 unique subdomains under a single parent domain within one hour — a potential indicator of domain generation algorithm (DGA) malware. Which SPL command should the analyst use to count distinct subdomain values per source IP?

- A) `stats count by src_ip, query`
- B) `stats dc(query) as unique_subdomains by src_ip`
- C) `eval unique_subdomains=count(query)`
- D) `dedup query | stats count by src_ip`

Correct Answer: B

Distractor Analysis:

- A is incorrect. `stats count by src_ip, query` counts total events grouped by both source IP and query — it produces one row per src_ip/query combination, not a count of unique queries per source IP.
- B is correct. `dc()` is Splunk's distinct count function. `stats dc(query) as unique_subdomains by src_ip` counts the number of unique values of the `query` field for each source IP — exactly the metric needed to identify hosts contacting an unusually high number of unique subdomains, which is a DGA indicator.
- C is incorrect. `eval` creates new fields using expressions but does not perform aggregate counting across events. `count(query)` is not a valid eval function syntax in SPL.
- D is incorrect. `dedup query | stats count by src_ip` removes duplicate query values globally before counting — it would mix subdomains across all source IPs rather than counting distinct queries per source IP independently.

---

## Question 7

A SIEM correlation rule is designed to detect data exfiltration by alerting when a single host transfers more than 100 MB outbound to an external IP in one hour. The rule has been in production for six months and has never generated a confirmed true positive. The SOC manager asks the analyst what to do with it. Which action is most appropriate?

- A) Lower the threshold to 10 MB to generate more alerts and increase detection opportunity
- B) Keep the rule unchanged because data exfiltration is rare and the absence of TPs means it is working as intended
- C) Review the rule's logic, data sources, and threshold against observed baseline traffic; retire or significantly retune based on findings
- D) Duplicate the rule and apply it to inbound traffic as well to cover more attack scenarios

Correct Answer: C

Distractor Analysis:

- A is incorrect. Lowering the threshold without understanding why the rule generates no TPs would likely generate a flood of false positives. Threshold changes should be evidence-based.
- B is incorrect. Zero TPs in six months does not mean the rule is working — it may mean the rule is misconfigured, querying the wrong data source, or that the threshold is so high it cannot fire under real-world conditions. Regular rule review is essential.
- C is correct. A rule with zero true positives over 90+ days warrants investigation before continued operation. The analyst should verify the rule queries the correct index and fields, check whether baseline traffic patterns make the threshold realistic, compare against known test exfiltration scenarios if available, and either retune or retire the rule based on findings.
- D is incorrect. Duplicating a broken rule for inbound traffic does not address the root cause problem. Applying broken logic to more scenarios multiplies noise without improving detection.

---

## Question 8

Which log source would provide the most direct evidence that an IAM user in AWS performed unauthorized privilege escalation by attaching an administrator policy to their own account?

- A) AWS VPC Flow Logs
- B) AWS CloudTrail
- C) Windows Security Event Log
- D) AWS GuardDuty findings

Correct Answer: B

Distractor Analysis:

- A is incorrect. VPC Flow Logs capture network flow metadata — source/destination IPs, ports, bytes, and allow/deny actions at the network level. They do not record IAM API calls or policy attachment operations.
- B is correct. AWS CloudTrail records every API call made in an AWS account, including IAM operations such as `AttachUserPolicy`, `CreateAccessKey`, and `PutUserPolicy`. A CloudTrail record of an IAM user calling `AttachUserPolicy` with an `AdministratorAccess` policy ARN against their own account is direct evidence of privilege escalation. CloudTrail is the primary log source for all AWS control-plane security investigations.
- C is incorrect. Windows Security Event Logs are generated by Windows operating systems and domain controllers. They have no visibility into AWS IAM operations, which occur in the AWS control plane.
- D is incorrect. GuardDuty is a threat detection service that generates findings based on its own analysis of CloudTrail, VPC Flow Logs, and DNS logs. While GuardDuty might generate a finding for this behavior, the underlying evidence is in CloudTrail. GuardDuty findings are alerts, not the raw log evidence.

---

## Question 9

A security analyst is reviewing a Microsoft Sentinel KQL query designed to detect failed logins. The query uses `summarize FailCount = count() by Account, IpAddress, bin(TimeGenerated, 5m)`. What does the `bin(TimeGenerated, 5m)` function accomplish in this query?

- A) It limits the query to return only the five most recent events per account
- B) It rounds the TimeGenerated timestamp down to the nearest five-minute interval, grouping events into five-minute buckets for time-window aggregation
- C) It filters events to only include those generated within the last five minutes
- D) It converts the TimeGenerated field from UTC to a five-minute offset time zone

Correct Answer: B

Distractor Analysis:

- A is incorrect. `bin()` does not limit row counts or filter by recency. Limiting to the most recent N events would require `top N by TimeGenerated` or a `where TimeGenerated > ago()` clause.
- B is correct. In KQL, `bin(TimeGenerated, 5m)` rounds each timestamp down to the nearest five-minute boundary — for example, 14:23:47 becomes 14:20:00. When used inside a `summarize` statement, this groups all events within the same five-minute window together, enabling detection rules that count events within rolling time windows rather than across the entire query period.
- C is incorrect. Filtering to the last five minutes would require `where TimeGenerated > ago(5m)`. The `bin()` function is a grouping/bucketing operation, not a filter.
- D is incorrect. KQL's `bin()` function is a data grouping operator. Time zone conversion uses the `datetime_utc_to_local()` function.

---

## Question 10

A SIEM analyst reviews the following two metrics from the past quarter: MTTD improved from 72 hours to 18 hours; MTTR remained unchanged at 6 hours. What does this data most accurately indicate about the SOC's security posture?

- A) The SOC has both improved its detection capability and its response capability over the quarter
- B) The SOC has significantly improved its detection speed, but response time has not improved — suggesting detection improvements have not been paired with response process improvements
- C) The SOC's response capability has degraded because MTTR is too high relative to the improved MTTD
- D) An MTTD of 18 hours is still too slow for effective security operations and the improvement is not meaningful

Correct Answer: B

Distractor Analysis:

- A is incorrect. The data shows MTTD improved but MTTR did not change. Stating that both improved is factually inaccurate based on the provided metrics.
- B is correct. MTTD dropping from 72 to 18 hours indicates the SOC is detecting threats significantly faster — likely due to improved SIEM tuning, better correlation rules, or increased log coverage. However, MTTR remaining at 6 hours suggests that once an incident is detected, the response process has not been accelerated. This is a meaningful finding: faster detection is valuable, but the overall time-to-containment improvement is limited if response processes are not also optimized.
- C is incorrect. MTTR has not increased — it is unchanged. "Degraded" would imply MTTR increased. An unchanged MTTR is neither degraded nor improved.
- D is incorrect. An MTTD improvement from 72 to 18 hours — a 75% reduction — is a very significant operational improvement. Industry targets vary widely by organization and threat type, but this improvement represents substantial progress that would reduce attacker dwell time and blast radius.

---

## Question 11 (5 points)

A SOAR playbook is triggered when a SIEM detects a phishing email alert. The playbook automatically: (1) extracts the sender address, (2) queries VirusTotal for the sender domain, (3) pulls all emails from the same sender in the past 7 days, and (4) creates a ticket in the ticketing system with the findings. What is the primary benefit of automating these steps?

- A) SOAR automation eliminates the need for Tier 1 analysts entirely
- B) Automating repetitive data gathering steps reduces analyst time spent on low-value work, enabling faster triage and allowing analysts to focus on investigative judgment
- C) SOAR ensures that all phishing alerts are automatically classified as true positives
- D) Automating the ticket creation step is the only SOAR benefit — all other steps must remain manual for accuracy

Correct Answer: B

Distractor Analysis:

- A is incorrect. SOAR automation handles repetitive, rule-based steps but does not replace the analyst's judgment required to investigate context, classify the alert, and determine appropriate response actions.
- B is correct. SOAR automation reduces mean time to triage by performing data gathering in seconds that would take a human analyst minutes or hours. This allows Tier 1 analysts to spend their time on analysis and decision-making rather than manually running lookups and copying data into tickets.
- C is incorrect. SOAR automates data collection and enrichment — it does not make classification decisions. Classification requires analyst judgment applied to the enriched data.
- D is incorrect. Automated ticket creation is one benefit, but SOAR's primary value is in orchestrating multi-step enrichment workflows, not just ticketing.

---

## Question 12 (5 points)

In Microsoft Sentinel KQL, an analyst wants to find all successful logins (EventID 4624) where the source IP address appears in a custom watchlist named `MaliciousIPs`. Which KQL approach correctly implements this lookup?

- A) `SecurityEvent | where EventID == 4624 | join MaliciousIPs on IpAddress`
- B) `SecurityEvent | where EventID == 4624 | lookup kind=leftouter (print IpAddress="malicious") on IpAddress`
- C) `SecurityEvent | where EventID == 4624 | where IpAddress in ((_GetWatchlist('MaliciousIPs') | project SearchKey))`
- D) `SecurityEvent | filter EventID = 4624 | match MaliciousIPs.IpAddress`

Correct Answer: C

Distractor Analysis:

- A is incorrect. The `join` operator in KQL requires both sides to be tabular data sources with matching column names. You cannot directly join a table to a watchlist name string without the `_GetWatchlist()` function to materialize it.
- B is incorrect. This query uses `print` to create a single-row table — it is syntactically plausible but logically incorrect. It would only match a single hardcoded IP, not an entire watchlist.
- C is correct. `_GetWatchlist('MaliciousIPs')` is the correct KQL function to retrieve a Sentinel watchlist as a tabular result. Wrapping it in a `where ... in (...)` subquery then filters the SecurityEvent results to only rows where the source IP appears in the watchlist.
- D is incorrect. `filter` and `match` are not valid KQL operators in this context. KQL uses `where` for row filtering. The syntax in option D is invalid.

---

## Question 13 (5 points)

Which log normalization standard defines a common schema for security events with fields like `src_ip`, `dest_ip`, `user`, `action`, and `outcome`, enabling SIEM rules to work across different data sources without source-specific parsing?

- A) Syslog (RFC 5424)
- B) Common Information Model (CIM)
- C) CEF (Common Event Format)
- D) LEEF (Log Event Extended Format)

Correct Answer: B

Distractor Analysis:

- A is incorrect. Syslog (RFC 5424) is a log transport and format standard for transmitting messages — it defines message structure (priority, header, message body) but does not define a normalized security field schema like `src_ip` or `action`.
- B is correct. The Common Information Model (CIM) — used primarily in Splunk — defines a standardized field naming schema that maps data from different sources into common fields. This allows SIEM correlation rules and reports to reference `src_ip` rather than source-specific field names.
- C is incorrect. CEF (Common Event Format), developed by ArcSight, is a log event format that structures events in key-value pairs. It is a format, not a full normalization schema defining semantic field names.
- D is incorrect. LEEF (Log Event Extended Format) is a proprietary IBM QRadar log format. It defines how events are transmitted to QRadar but is not a cross-platform normalization standard.

---

## Question 14 (5 points)

A SIEM correlation rule generates 1,200 alerts per day but only 18 (1.5%) are confirmed true positives. Management asks the analyst to improve signal quality. Which tuning strategy would most directly reduce the false positive rate while preserving true positive detection?

- A) Delete the rule and rely on manual log review to find the 18 daily true positives
- B) Add contextual exceptions for known-good source IPs, service accounts, and authorized scheduled processes that consistently trigger the rule without malicious behavior
- C) Raise the threshold to a level so high that the rule fires only once per week regardless of activity
- D) Change all Medium severity alerts to Informational to reduce analyst workload

Correct Answer: B

Distractor Analysis:

- A is incorrect. Deleting the rule eliminates all 18 daily true positive detections — 18 confirmed incidents would go undetected every day. The cost of deletion far outweighs the false positive noise.
- B is correct. Adding documented exceptions for consistently false-positive-generating sources (known service accounts, authorized automation tools, scheduled tasks) reduces noise on the specific sources that are confirmed legitimate, while the rule continues firing on all other sources including attackers.
- C is incorrect. Setting the threshold artificially high reduces true positives along with false positives. Attackers who observe the threshold can stay below it, defeating detection entirely.
- D is incorrect. Changing severity does not reduce alert volume — analysts still process the same number of events. It reduces urgency but not workload.

---

## Question 15 (5 points)

An analyst is reviewing a SIEM dashboard and notices a spike in Event ID 4688 (Process Create) alerts originating from a single workstation — `WS-HR-07` — showing `powershell.exe` spawning from `winword.exe` 14 times in 6 minutes. What is the most likely explanation for this activity?

- A) A standard Microsoft Office macro running scheduled document saves
- B) A malicious document executing an embedded PowerShell payload — a common initial compromise technique (ATT&CK T1566.001 + T1059.001)
- C) Windows Defender running a scheduled PowerShell-based scan triggered by a Word document
- D) The HR software legitimately uses Word to invoke PowerShell for its reporting module

Correct Answer: B

Distractor Analysis:

- A is incorrect. Microsoft Word's auto-save function uses internal Office processes. It does not invoke `powershell.exe` as a child process. Legitimate Word macros that integrate with Office services also do not typically spawn PowerShell from the document process 14 times in 6 minutes.
- B is correct. A parent-child relationship where `winword.exe` spawns `powershell.exe` is a well-known malicious document execution indicator. Threat actors use embedded malicious macros to launch PowerShell for download cradles, remote code execution, or in-memory payload execution. The frequency (14 times in 6 minutes) further suggests automated malicious activity.
- C is incorrect. Windows Defender executes as `MsMpEng.exe` or other Defender process names — not as child processes of `winword.exe`.
- D is incorrect. Legitimate HR software that integrates PowerShell through Word would be a known, documented, and typically rare integration. Fourteen invocations in 6 minutes during a business day without a corresponding business event is not consistent with routine software operation.

---

## Question 16 (5 points)

Which SIEM capability is specifically designed to link multiple related events into a single case record so that analysts can view the full attack chain rather than investigating each alert individually?

- A) Log normalization
- B) Alert correlation / incident grouping
- C) Log retention
- D) Field extraction

Correct Answer: B

Distractor Analysis:

- A is incorrect. Log normalization converts disparate log formats into a common schema. It enables correlation but is not itself the linking capability.
- B is correct. Alert correlation and incident grouping (sometimes called alert clustering or case management integration) links related SIEM alerts into a single incident case. This allows an analyst to see, for example, that a port scan alert, a brute-force alert, and a successful logon alert are all related to the same source IP and attack chain rather than three separate investigations.
- C is incorrect. Log retention defines how long logs are stored and made available for query. It does not link related alerts together into cases.
- D is incorrect. Field extraction parses raw log text to identify and label structured data fields. It is a parsing function, not a case-linking function.

---

## Question 17 (5 points)

An analyst is asked to write a KQL query in Microsoft Sentinel to detect when any user's account is both created (EventID 4720) and used to log on (EventID 4624) within 10 minutes of creation — a potential indicator of a backdoor account. Which KQL operator best enables this time-correlated join?

- A) `union`
- B) `join kind=inner` with a time filter
- C) `summarize` with `bin(TimeGenerated, 10m)`
- D) `project`

Correct Answer: B

Distractor Analysis:

- A is incorrect. `union` combines rows from two tables vertically (stacking them) — it does not correlate rows from different event types based on matching fields and time proximity.
- B is correct. A `join kind=inner` on the account name between the 4720 and 4624 event tables, with a `where` clause filtering for logon times within 10 minutes of creation time, correctly identifies accounts created and immediately used. This is the standard KQL approach for time-correlated multi-event detection.
- C is incorrect. `summarize` with `bin()` groups events into time buckets but does not correlate two different event types based on a shared identifier (the account name) and a time relationship between them.
- D is incorrect. `project` selects and renames columns — it is a projection/output formatting operator with no joining or time-correlation capability.

---

## Question 18 (5 points)

A SOC analyst is configuring a new SIEM data source. The analyst chooses to use an agent installed on the source system that forwards logs to the SIEM's indexer in real time rather than having the SIEM periodically poll the source via API. What is the primary operational advantage of agent-based log forwarding over API polling?

- A) Agent-based forwarding reduces the SIEM's storage requirements by compressing logs
- B) Agent-based forwarding provides lower latency and does not depend on the SIEM having network access to the source system's API endpoint
- C) API polling produces more detailed logs than agent-based forwarding
- D) Agent-based forwarding eliminates the need for log normalization

Correct Answer: B

Distractor Analysis:

- A is incorrect. Agent-based forwarding may compress logs in transit, but that is a secondary feature. The primary architectural advantage is not compression.
- B is correct. Agent-based forwarding delivers logs continuously in near real time, reducing the latency between event occurrence and SIEM ingestion. It also pushes logs outbound from the source, eliminating the requirement for the SIEM to have inbound API access to the source system — which can be a firewall or access control challenge in segmented environments.
- C is incorrect. The log detail level (fields captured, verbosity) is determined by the source system's logging configuration, not by the transport method. API polling and agent-based forwarding can both deliver the same log content.
- D is incorrect. Both agent-based and API-based log delivery still require normalization because the raw log format (e.g., Windows XML events, CEF) must be parsed and mapped to the SIEM's common schema.

---

## Question 19 (5 points)

A SIEM alert fires based on a "Rare Process Execution" rule — a process `svchost32.exe` was created from `C:\Users\Public\Downloads\`. An analyst checking the parent process finds `winword.exe`. Which action is the correct immediate response for a Tier 1 analyst?

- A) Close the alert as a false positive because svchost.exe is a legitimate Windows system process
- B) Classify as a true positive: the process name misspells a system process (masquerading), the unusual parent (Word spawning a host process), and the non-system-directory path are all red flags — escalate to Tier 2 with full process tree details
- C) Block the IP address of the workstation at the perimeter firewall
- D) Reimage the workstation immediately without documenting findings

Correct Answer: B

Distractor Analysis:

- A is incorrect. The legitimate Windows process is `svchost.exe` in `C:\Windows\System32\`. `svchost32.exe` in a user's Downloads folder is a masquerading technique (ATT&CK T1036.005). The misspelling and unusual path are immediate red flags. Closing as a false positive without investigation is dangerous.
- B is correct. Three simultaneous indicators are present: masqueraded process name, non-standard path (Downloads vs. System32), and unusual parent process (Word). The correct Tier 1 action is to classify as a true positive and escalate with the full process tree — parent process, command line, and file path — documented for Tier 2 investigation.
- C is incorrect. Blocking the workstation at the perimeter firewall would not contain local execution and may alert the attacker. Containment decisions belong to Tier 2 after confirmation.
- D is incorrect. Reimaging before documentation destroys forensic evidence and is a Tier 2/3 response action requiring management authorization.

---

## Question 20 (5 points)

Which of the following best describes the role of a SIEM's threat intelligence integration capability?

- A) The SIEM's TI integration allows it to automatically patch vulnerable systems when an IOC matches a CVE
- B) TI integration enriches SIEM alerts with context from external threat feeds — allowing correlation rules to automatically flag events involving known-malicious IPs, domains, or file hashes — reducing manual lookups by analysts
- C) TI integration converts all SIEM alerts into TLP:RED intelligence reports for external sharing
- D) TI integration replaces SIEM correlation rules with real-time threat actor tracking

Correct Answer: B

Distractor Analysis:

- A is incorrect. SIEMs are detection and alerting platforms. They do not patch systems. Patch management is performed by vulnerability management and endpoint management tools.
- B is correct. SIEM threat intelligence integration automatically enriches events by checking observed IPs, domains, URLs, and file hashes against threat intelligence feeds. When a match is found, the alert is automatically annotated with TI context (threat category, confidence, source), reducing the time analysts spend manually querying TI platforms during triage.
- C is incorrect. SIEMs consume threat intelligence — they do not produce TLP-marked intelligence reports for external sharing. Threat intelligence production is performed by CTI teams using separate platforms.
- D is incorrect. TI integration does not replace correlation rules. Rules define what patterns trigger alerts; TI integration enriches those alerts with context after they fire.
