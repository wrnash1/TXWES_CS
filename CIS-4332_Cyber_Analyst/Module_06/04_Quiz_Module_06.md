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
