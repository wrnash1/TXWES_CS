# Lab Activity: Module 06 — SIEM and Log Analysis

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Lab Overview

In this lab you will perform hands-on SIEM analysis using provided log datasets and pre-built query environments. You will write SPL and KQL queries to detect attack patterns, analyze a noisy correlation rule and propose tuning changes, and evaluate a set of SIEM alerts to classify true positives and false positives.

All exercises use provided sample data or in-browser query sandboxes — no SIEM installation is required.

- Total Points: 100
- Estimated Completion Time: 75–90 minutes
- Submission: Upload your completed Lab Report to Canvas, Module 06 Lab assignment

---

## Learning Objectives

By completing this lab you will be able to:

- Write Splunk SPL queries to detect brute force and lateral movement patterns
- Write Microsoft Sentinel KQL queries to surface authentication anomalies
- Analyze correlation rule output and identify tuning improvements
- Classify SIEM alerts as true positive, false positive, or requires investigation
- Recommend specific log sources to add to a SIEM to fill detection gaps

---

## Lab Environment Access

### Splunk Exercises (Exercises 1 and 2)

Use the Splunk Attack Range sandbox at `https://tryhackme.com` (TryHackMe "Splunk: Basics" and "Splunk 2" rooms) or the Splunk Boss of the SOC dataset at `https://bots.splunk.com`.

If sandbox access is unavailable, submit query screenshots from the Splunk free developer instance at `https://www.splunk.com/en_us/download/splunk-enterprise.html` (90-day free trial).

### KQL Exercises (Exercise 3)

Use the Microsoft Sentinel demo environment at `https://aka.ms/SentinelLab` or the Azure Log Analytics demo workspace at `https://aka.ms/lademo`.

---

## Exercise 1 — SPL Query Writing (35 points)

### Exercise 1 Background

You are a Tier 1 analyst in a SOC. Your SIEM has just ingested Windows Security Event logs from the past 24 hours across the corporate domain. You need to write SPL queries to surface specific threat indicators.

Use the index `wineventlog` or `main` depending on your sandbox. All queries should target the time range `earliest=-24h`.

### Task 1A — Failed Login Analysis (10 points)

Write an SPL query that:

1. Searches for failed logon events (EventCode 4625)
2. Groups results by Account_Name and src_ip
3. Returns only accounts with five or more failures
4. Sorts results by failure count descending
5. Displays columns: Account_Name, src_ip, failure_count

Submit: The complete SPL query and a screenshot of the results table.

Expected query structure:

```spl
index=wineventlog EventCode=4625 earliest=-24h
| stats count as failure_count by Account_Name, src_ip
| where failure_count >= 5
| sort -failure_count
| table Account_Name, src_ip, failure_count
```

Scoring: 5 points for correct query logic; 5 points for screenshot showing non-empty results or documented explanation if dataset yields zero results.

### Task 1B — Brute Force with Successful Login (15 points)

Write an SPL query that:

1. Identifies accounts with five or more failed logins (EventCode 4625) within any two-minute window
2. Correlates those accounts against successful logins (EventCode 4624) in the same hour
3. Returns only accounts that appear in both result sets
4. Displays: Account_Name, failure_count, successful_login_time

Submit: The complete SPL query with explanation of each pipe stage (2–3 sentences per stage) and a screenshot of results.

Scoring: 7 points for correct query; 8 points for accurate explanation of each query stage.

### Task 1C — High-Volume Outbound Traffic (10 points)

Write an SPL query using network flow data (index `netflow` or `network`) that:

1. Filters for outbound traffic only (direction=outbound or dest_ip not in RFC 1918 ranges)
2. Sums bytes transferred per source IP per destination IP
3. Returns only source/destination pairs exceeding 50 MB (52,428,800 bytes)
4. Sorts by bytes descending

Submit: The complete SPL query and screenshot. If your sandbox lacks network flow data, write the query with a comment explaining the expected dataset and submit the query code only for partial credit.

---

## Exercise 2 — Correlation Rule Tuning Analysis (30 points)

### Exercise 2 Background

The SOC manager has flagged the following correlation rule as "extremely noisy" — it is generating over 400 alerts per day, nearly all false positives. Review the rule definition and answer the analysis questions.

### Rule Under Review

```text
Rule Name: Multiple Failed Logins — Any Account
Platform: Splunk Enterprise Security
Search:
    index=wineventlog EventCode=4625
    | bucket _time span=5m
    | stats count as failures by _time, Account_Name
    | where failures >= 2
    | eval severity="high"

Threshold: 2 failures in 5 minutes
Severity: High
Current alert volume: 412 per day
Confirmed true positives last 90 days: 3
Average analyst time per alert: 8 minutes
```

### Task 2A — False Positive Root Cause Analysis (10 points)

In 5–7 sentences, identify at least three specific reasons why this rule generates an excessive number of false positives. Your analysis should address:

- Why the threshold of two failures is inappropriate for most enterprise environments
- What types of legitimate user behavior would routinely trigger this rule
- What types of automated or system-generated activity would trigger this rule

### Task 2B — Tuning Recommendation (12 points)

Propose a revised version of the rule that would significantly reduce false positives without eliminating true positive detection. Your answer must include:

1. A revised SPL query implementing your tuning changes
2. A written explanation of each change made (3–4 sentences per change)
3. An explanation of any detection capability trade-offs your tuning introduces

Your revised rule should implement at least three of the following tuning techniques:

- Raise the failure threshold
- Add a time-bucketing window
- Exclude known service accounts or scanner IPs
- Correlate failures with a subsequent successful login
- Add asset criticality context to severity

### Task 2C — Operational Impact Calculation (8 points)

Using the current rule statistics provided, calculate:

1. The total analyst hours per day consumed by this rule (show your calculation)
2. The true positive rate over the 90-day period (total TPs / total alerts; show your calculation assuming 412 alerts/day is consistent)
3. Based on these numbers, justify in 3–4 sentences whether this rule should be retired, significantly retuned, or kept as-is

---

## Exercise 3 — KQL Query Writing in Microsoft Sentinel (20 points)

### Exercise 3 Background

Using the Azure Log Analytics demo workspace at `https://aka.ms/lademo`, write KQL queries against the `SecurityEvent` and `SigninLogs` tables.

### Task 3A — Privilege Escalation Detection (10 points)

Write a KQL query that:

1. Finds accounts that received Event ID 4672 (Special Privileges Assigned) in the past 24 hours
2. Joins against Event ID 4624 for the same account to verify a preceding logon
3. Filters out accounts that are members of known admin groups (use `AccountType != "Machine"` as a proxy)
4. Returns: Account, TimeGenerated, LogonType, IpAddress

Submit: The complete KQL query and a screenshot of results.

Expected query pattern:

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4672
| join kind=inner (
    SecurityEvent
    | where EventID == 4624
    | where AccountType != "Machine"
    | project Account, LogonTime=TimeGenerated, LogonType, IpAddress
) on Account
| project Account, PrivilegeTime=TimeGenerated, LogonTime, LogonType, IpAddress
| order by PrivilegeTime desc
```

### Task 3B — Failed Authentication Summary Dashboard Query (10 points)

Write a KQL query suitable for a Sentinel Workbook visualization that:

1. Queries `SecurityEvent` for Event ID 4625 over the past 7 days
2. Creates a time chart showing failed login attempts per hour
3. Groups by Account to show top 10 accounts with most failures
4. Outputs results suitable for a bar chart visualization

Submit: The complete KQL query, a screenshot of the visualization, and a 3–4 sentence explanation of what the chart reveals about authentication health.

---

## Exercise 4 — Alert Triage and Classification (15 points)

### Exercise 4 Background

Review the five SIEM alerts below and classify each as: True Positive (TP), False Positive (FP), or Requires Further Investigation (RFI). Provide a 3–4 sentence justification for each classification.

### Alert 4-01

```text
Rule: Brute Force — Domain Admin Account
Account: administrator@corp.local
Failed logins: 47 in 3 minutes from 10.0.9.12
Followed by: Successful login at 14:23:44 from same IP
Asset 10.0.9.12: Developer workstation — jsmith
User jsmith: Has never previously logged into administrator account
```

Classification and justification:

### Alert 4-02

```text
Rule: High Volume Outbound Transfer
Source: backup-server-01 (10.0.5.10)
Destination: 203.0.113.45 (external IP — classified as backup cloud provider)
Transfer: 4.2 GB between 02:00 and 04:00 AM
Scheduled backup window: 01:00 to 05:00 AM daily
Historical pattern: Same transfer volume and destination 6 days per week for 18 months
```

Classification and justification:

### Alert 4-03

```text
Rule: New Local Admin Account Created
Event: EventID 4720 — new account "svc_winmon" created on WS-ACCTG-04
Created by: jdoe (standard accounts-payable user — no admin privileges documented)
Time: 14:47 UTC on Tuesday
IT change tickets: No change ticket for this account creation found
```

Classification and justification:

### Alert 4-04

```text
Rule: Impossible Travel
User: m.chen@corp.local
Login 1: 08:15 AM — Chicago, IL (corporate office VPN — expected)
Login 2: 09:02 AM — London, UK (47 minutes later)
Note: m.chen is a global account manager who travels internationally weekly
HR record: m.chen had a London client meeting scheduled this week
```

Classification and justification:

### Alert 4-05

```text
Rule: DNS Query Volume Anomaly
Source: WS-FINANCE-09
Queries in 1 hour: 8,441 unique subdomains under the domain "updates-cdn-service.net"
Historical baseline: average 80 unique DNS queries per hour for this host
Domain age (VirusTotal): registered 3 days ago
Domain reputation: 0/86 vendors flag as malicious (no reputation yet)
```

Classification and justification:

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| 1A — Failed Login SPL | 10 | Correct query logic; screenshot submitted |
| 1B — Brute Force SPL | 15 | Correct correlation query; clear stage explanation |
| 1C — Outbound Traffic SPL | 10 | Correct query; network data explanation if unavailable |
| 2A — Root Cause Analysis | 10 | Three accurate FP reasons identified with explanation |
| 2B — Tuning Recommendation | 12 | Revised query; three tuning techniques; trade-off discussed |
| 2C — Operational Impact | 8 | Correct calculations shown; justified recommendation |
| 3A — Privilege Escalation KQL | 10 | Correct join query; screenshot submitted |
| 3B — Dashboard KQL | 10 | Correct timechart query; visualization; health interpretation |
| 4 — Alert Triage (5 alerts) | 15 | 3 pts each: correct TP/FP/RFI classification + justification |
| Total | 100 | |

---

## Submission Instructions

1. Use a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present all queries in fenced code blocks.
4. Include screenshots for all tasks that require them.
5. Submit to the Canvas Module 06 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All log data and alert examples in this lab are fabricated for educational purposes. All work must be your own. Do not share query solutions in public forums. Reference `comptia.org` and `professormesser.com` for additional study context.
