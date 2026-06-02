# Lab Activity: Module 01 - Security Operations & Analyst Role

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will perform the core activities of a Tier 1 SOC analyst: reviewing an alert, gathering contextual evidence, classifying the alert, and documenting your findings. All data is provided within this document. No external tools or network access are required. You are working in an educational, simulated SOC environment.

Total Points: 100

Estimated Completion Time: 60-90 minutes

Submission: Upload your completed Lab Report document to the Canvas assignment portal.

---

## Learning Objectives

By completing this lab you will be able to:

- Trace an incoming SIEM alert through the five-step Tier 1 triage workflow
- Classify a set of provided artifacts as specific IOC types
- Apply the CIA Triad to identify which security pillar an attack targets
- Document analyst findings in the format used by professional SOC teams
- Distinguish true positives, false positives, false negatives, and true negatives from scenario descriptions

---

## Lab Setup

No special software installation is required. You will need:

- This lab document (printed or on-screen)
- A text editor, word processor, or the Lab Report Template provided in Canvas
- Access to the course Reading Guide for Module 01 as a reference

Work through each exercise in order. Each exercise builds on the knowledge from the previous one.

---

## Exercise 1: SOC Alert Triage (40 points)

### Exercise 1 Scenario

You are a Tier 1 analyst at the beginning of your shift. The SIEM has generated the following alert. Your task is to triage this alert using the five-step workflow from the Reading Guide.

### Alert Details

```text
ALERT ID:       SOC-2024-0847
Severity:       HIGH
Rule:           Brute Force Success - SSH
Timestamp:      2024-11-14  02:17:43 UTC
Source IP:      203.0.113.47
Destination IP: 10.10.5.22  (internal hostname: WEBSERVER-PROD-01)
Destination Port: 22 (SSH)
User Account:   svc_deploy
Event Summary:  47 failed SSH authentication attempts from source IP
                203.0.113.47 over 8 minutes, followed by one successful
                authentication at 02:17:43 UTC using account svc_deploy.
```

### Supporting Context

#### Threat Intelligence Lookup — 203.0.113.47

```text
Source: Internal TI Feed
IP: 203.0.113.47
Classification: SUSPICIOUS
Tags: TOR exit node, prior association with credential-stuffing campaigns
Last seen: 2024-11-13
Confidence: MEDIUM
```

#### Asset Inventory Lookup — 10.10.5.22

```text
Hostname: WEBSERVER-PROD-01
Role: Production web server (public-facing e-commerce application)
Owner: IT Infrastructure Team
Criticality: HIGH
Normal SSH access: Restricted to internal jump host 10.10.1.5 only.
                   No authorized SSH from external IPs.
```

#### Account Lookup — svc_deploy

```text
Account type: Service account
Purpose: Automated deployment scripts
Normal login hours: Monday-Friday 08:00-18:00 UTC via internal jump host
Last authorized login: 2024-11-13 14:22:01 UTC from 10.10.1.5
MFA: Not configured on this account
```

### Task 1A — Apply the Five-Step Triage Workflow (25 points)

Document your triage process for alert SOC-2024-0847. For each step, write a complete response using the evidence provided above. Your responses will be graded on completeness, accuracy, and use of correct SOC terminology.

#### Step 1 — Review the Alert (3 points)

In 2-4 sentences, summarize what the alert is telling you. Include the rule that fired, the severity, the affected asset, and the timestamp.

> *Write your response here.*

#### Step 2 — Gather Context (5 points)

Summarize the relevant contextual findings from each of the three supporting data sources: Threat Intelligence, Asset Inventory, and Account lookup. Note any findings that increase or decrease your suspicion that this is a real attack.

> *Write your response here.*

#### Step 3 — Classify the Alert (5 points)

Is this alert a true positive or a false positive? Justify your classification in 3-5 sentences. Reference at least three specific pieces of evidence from the supporting context.

> *Write your response here.*

#### Step 4 — Document the Finding (7 points)

Write a formal analyst note in the format below. Fill in every field. This note is what Tier 2 would receive when you escalate.

```text
ANALYST NOTE
Alert ID:           SOC-2024-0847
Analyst:            [Your name]
Classification:     [True Positive / False Positive]
Severity:           [HIGH / MEDIUM / LOW]
Summary:            [2-3 sentence description of the event]
Evidence:           [List 3-5 specific evidence items that support your classification]
TI Findings:        [What the TI lookup returned and its relevance]
Recommended Action: [What should happen next]
Escalate to Tier 2: [Yes / No]
```

#### Step 5 — Escalate or Close (5 points)

State whether you are escalating this alert or closing it. If escalating, identify what information you would verbally communicate to the Tier 2 analyst in a 60-second handoff. If closing, explain your reasoning and what tuning action, if any, you would recommend.

> *Write your response here.*

### Task 1B — CIA Triad Analysis (15 points)

Based on the confirmed incident in this scenario, answer the following questions.

#### CIA Question 1 (5 points)

Which pillar(s) of the CIA Triad is this attack most directly threatening? Explain your reasoning.

> *Write your response here.*

#### CIA Question 2 (5 points)

If the attacker gained persistent access and began downloading the e-commerce customer database from WEBSERVER-PROD-01, which CIA Triad pillar would be violated? How does this differ from your answer to CIA Question 1?

> *Write your response here.*

#### CIA Question 3 (5 points)

If the attacker's ultimate goal were to encrypt WEBSERVER-PROD-01 with ransomware and render the site unavailable, which CIA Triad pillar would be most directly violated? Identify one technical control that would reduce the impact of this attack.

> *Write your response here.*

---

## Exercise 2: IOC Classification (30 points)

### Exercise 2 Scenario

Your Tier 2 analyst has shared a set of artifacts collected during investigation of the SOC-2024-0847 incident. Your task is to classify each artifact as the correct IOC type, assign a Pyramid of Pain level, and briefly explain the significance of each IOC.

### Artifact Set

| Artifact ID | Artifact Value | Your IOC Type | Pyramid Level | Significance |
|---|---|---|---|---|
| A-01 | MD5 hash: `a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4` found in `/tmp/` on WEBSERVER-PROD-01 | | | |
| A-02 | IP address 203.0.113.47 communicating with internal systems | | | |
| A-03 | Domain `update-pkg-cdn.info` queried by WEBSERVER-PROD-01 at 02:19 UTC | | | |
| A-04 | Registry key `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\svchost32` created on a workstation during post-login activity | | | |
| A-05 | Scheduled task `SystemHealthCheck` created at 02:21 UTC running `C:\Windows\Temp\svc.exe` | | | |
| A-06 | Pattern: outbound connections to port 4444 from multiple internal hosts between 02:15 and 02:30 UTC | | | |

Use the following IOC types: File-based, Network-based, Host-based, Behavioral, Email-based.

Use Pyramid of Pain levels: Hash, IP, Domain, Network/Host Artifact, Tool, TTP.

### Task 2A — Complete the IOC Table (18 points)

Fill in the three blank columns for each of the six artifacts above (3 points per row: 1 for IOC type, 1 for Pyramid level, 1 for significance explanation).

### Task 2B — Pyramid of Pain Reflection (12 points)

Answer each question in 3-5 sentences.

#### Pyramid Question 1 (4 points)

An attacker who knows their IP address (A-02) has been blocked simply switches to a new IP address from a different provider. Why does this illustrate the weakness of blocking at the IP level, and what higher-level indicator from your artifact set would be more durable to block?

> *Write your response here.*

#### Pyramid Question 2 (4 points)

Artifact A-06 describes a behavioral pattern — outbound connections to port 4444 from multiple hosts. At what Pyramid of Pain level does this IOC sit? Why is a behavioral detection rule that catches this pattern more valuable than a hash-based rule targeting the specific file `svc.exe`?

> *Write your response here.*

#### Pyramid Question 3 (4 points)

If threat hunters identified that the attacker consistently uses a specific sequence of actions — SSH brute force, service account compromise, scheduled task persistence, outbound C2 on a non-standard port — this sequence represents a TTP. Why does blocking at the TTP level impose the most cost on the attacker?

> *Write your response here.*

---

## Exercise 3: Alert Classification Scenarios (20 points)

For each scenario below, identify the correct alert classification: True Positive (TP), False Positive (FP), False Negative (FN), or True Negative (TN). Provide a one-sentence justification for each answer.

### Classification Scenarios

### Scenario 3-01 (4 points)

A SIEM rule fires an alert when a user attempts to access a file share outside business hours. The alert fires at 11 PM for a system administrator who is authorized to access all file shares at any time and is performing scheduled overnight maintenance. The administrator is on the approved after-hours access list.

Classification: \_\_\_\_ Justification: \_\_\_\_

### Scenario 3-02 (4 points)

A SIEM rule is configured to detect lateral movement by flagging internal hosts that connect to more than 20 other internal hosts within a 5-minute window. A penetration tester authorized under a current statement of work runs an internal network scan. No alert fires during the scan.

Classification: \_\_\_\_ Justification: \_\_\_\_

### Scenario 3-03 (4 points)

An analyst receives an alert that a known malicious IP address made a connection to the organization's public-facing web server. The TI feed confirms the IP is a documented command-and-control address for a ransomware group. The web server logs show the connection was made and a response was returned.

Classification: \_\_\_\_ Justification: \_\_\_\_

### Scenario 3-04 (4 points)

A user calls the help desk to report that their workstation is behaving strangely — applications are closing unexpectedly and the CPU is running at 100%. The SOC checks the SIEM alert queue and finds no alerts associated with that workstation for the past 48 hours. Post-incident forensic analysis later confirms the workstation had been infected with a keylogger for 36 hours before the user called.

Classification: \_\_\_\_ Justification: \_\_\_\_

### Scenario 3-05 (4 points)

A SIEM rule monitors for failed VPN authentication attempts and fires an alert when there are more than 5 failures from a single IP in 10 minutes. An analyst investigates and finds that an employee forgot their password and tried to log in 7 times before calling the help desk to reset it. No successful login occurred from the external IP.

Classification: \_\_\_\_ Justification: \_\_\_\_

---

## Exercise 4: SOC Metrics Analysis (10 points)

### Exercise 4 Scenario

You have been asked to review the following monthly SOC metrics report and identify operational problems.

```text
MONTHLY SOC METRICS — NOVEMBER 2024
Total alerts generated:         14,200
True positives confirmed:           87
False positives closed:         14,113
False positive rate:             99.4%
Mean Time to Detect (MTTD):      72 hours
Mean Time to Respond (MTTR):     18 hours
Dwell time (average):            68 hours
Escalations to Tier 2:              87
Escalations resolved < 4 hrs:       31
```

#### Metrics Question 1 (4 points)

The false positive rate is 99.4%. Describe two operational consequences this creates for the SOC team. What is the recommended remediation action?

> *Write your response here.*

#### Metrics Question 2 (3 points)

The MTTD is 72 hours and dwell time is 68 hours. What does the near-equal relationship between these two metrics tell you about when threats are typically being detected? What program investment would most directly reduce dwell time?

> *Write your response here.*

#### Metrics Question 3 (3 points)

Only 31 of 87 Tier 2 escalations (35.6%) were resolved within 4 hours. Suggest two specific process improvements that could improve this MTTR metric.

> *Write your response here.*

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Five-Step Triage | 25 | Each step graded for completeness, accuracy, and use of SOC terminology |
| Exercise 1B — CIA Triad Analysis | 15 | Correct pillar identification with justified reasoning for each question |
| Exercise 2A — IOC Table | 18 | 3 points per artifact row: 1 for IOC type, 1 for Pyramid level, 1 for significance |
| Exercise 2B — Pyramid of Pain Reflection | 12 | Depth of analysis, correct level identification, practical reasoning |
| Exercise 3 — Alert Classifications | 20 | 4 points per scenario: 2 for correct classification, 2 for accurate justification |
| Exercise 4 — Metrics Analysis | 10 | Correct identification of problems, practical and specific recommendations |
| Total | 100 | |

---

## Submission Instructions

1. Complete all exercises in a single document using the Lab Report Template from Canvas or a document with clearly labeled section headers matching this lab.
2. Include your full name, student ID, and the date at the top of your submission.
3. Submit to the Canvas Module 01 Lab assignment by the posted deadline.
4. Late submissions are subject to the course late policy in the syllabus.

---

## Academic Integrity Notice

All work submitted must be your own. The scenarios in this lab are educational simulations. Do not use real organizational data. Do not share your answers with classmates before the submission deadline. Reference the CySA+ CS0-003 exam objectives at comptia.org and study materials at professormesser.com for additional context.
