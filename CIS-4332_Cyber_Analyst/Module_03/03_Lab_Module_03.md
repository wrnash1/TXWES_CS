# Lab Activity: Module 03 - Vulnerability Management: Scanning and Prioritization

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 2 - Vulnerability Management (30%)

---

## Lab Overview

In this lab you will analyze simulated vulnerability scan output, apply CVSS scoring knowledge, and make evidence-based prioritization decisions. You will also recommend remediation strategies and produce a condensed executive summary of your findings. All data is provided within this document. No scanner software installation is required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 03 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Interpret vulnerability scan output including CVE IDs, CVSS scores, and severity labels
- Apply risk-based prioritization criteria beyond CVSS score alone
- Recommend the appropriate remediation type for specific vulnerability findings
- Identify false positive candidates in scan output
- Produce a prioritized remediation plan in the format used by enterprise vulnerability management programs

---

## Exercise 1: Scan Output Analysis (40 points)

### Exercise 1 Overview

The following table represents a subset of findings from a vulnerability scan of a medium-sized organization's environment. The scan was credentialed and performed from inside the network. Review all ten findings and complete the tasks below.

### Scan Results Table

| Finding ID | CVE | CVSS Score | Severity | Affected Host | Host Role | Internet-Facing | Exploit Available | KEV Listed |
|---|---|---|---|---|---|---|---|---|
| F-01 | CVE-2024-1001 | 9.8 | Critical | 10.0.1.5 | Public web server (customer portal) | Yes | Yes | Yes |
| F-02 | CVE-2024-1002 | 7.5 | High | 10.0.2.10 | Internal file server (employee HR records) | No | No | No |
| F-03 | CVE-2024-1003 | 9.1 | Critical | 10.0.3.15 | Isolated QA test server (no production data) | No | No | No |
| F-04 | CVE-2024-1004 | 6.5 | Medium | 10.0.1.5 | Public web server (customer portal) | Yes | Yes | No |
| F-05 | CVE-2024-1005 | 4.3 | Medium | 10.0.4.20 | Developer workstation (one user) | No | No | No |
| F-06 | CVE-2024-1006 | 8.1 | High | 10.0.5.30 | Domain controller (primary AD) | No | Yes | No |
| F-07 | CVE-2024-1007 | 5.9 | Medium | 10.0.1.5 | Public web server (customer portal) | Yes | No | No |
| F-08 | CVE-2024-1008 | 3.1 | Low | 10.0.6.40 | Network printer | No | No | No |
| F-09 | CVE-2024-1009 | 9.3 | Critical | 10.0.7.50 | VPN concentrator (remote access gateway) | Yes | No | No |
| F-10 | CVE-2024-1010 | 7.2 | High | 10.0.2.10 | Internal file server (employee HR records) | No | No | No |

### Task 1A — Prioritized Remediation Ranking (20 points)

Rank all ten findings from highest priority (1) to lowest priority (10) for remediation. You may not use CVSS score as your only criterion. For each finding in your top five (ranks 1-5), write a 2-3 sentence justification that explicitly references at least two prioritization factors from the Reading Guide (KEV status, exploitability, exposure, asset criticality, CVSS score, compensating controls).

Format your answer as a ranked table with a Justification column for ranks 1-5.

| Rank | Finding ID | CVE | CVSS | Key Justification Factors | 2-3 Sentence Justification |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | |  |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

Scoring: 2 points per finding for correct ranking order in top 5 (relative to other students' justified rankings); 1 point per justification for use of correct terminology; partial credit available.

### Task 1B — Remediation Type Recommendation (12 points)

For findings F-01, F-03, F-06, and F-09, recommend the most appropriate remediation type: patch, configuration change, compensating control, or risk acceptance. For each recommendation, write a 2-sentence explanation.

### Task 1C — False Positive Assessment (8 points)

Finding F-03 is a Critical CVSS 9.1 vulnerability on an isolated QA test server with no production data. A colleague suggests this is effectively a false positive because "it cannot cause real harm." Do you agree or disagree with calling this a false positive? In 4-6 sentences, explain your position using the correct definition of a false positive from the Reading Guide, and explain what the correct classification is for F-03.

---

## Exercise 2: CVSS Scoring Analysis (25 points)

### Exercise 2 Overview

A security vendor has published the following vulnerability description. Read it carefully and answer the questions that follow.

### Vulnerability Description

A buffer overflow vulnerability exists in the authentication module of a widely deployed VPN appliance. The vulnerability can be triggered by an unauthenticated remote attacker by sending a specially crafted HTTP request to the management interface, which is exposed on TCP port 8443. Successful exploitation allows the attacker to execute arbitrary code with root-level privileges on the appliance. No user interaction is required. A proof-of-concept exploit has been published on a public security research platform. The vendor has released a patch. The management interface is internet-accessible by default on standard deployments.

### Task 2A — CVSS Base Metric Analysis (15 points)

For each of the following CVSS v3.1 Base metrics, identify the correct value for this vulnerability and provide a one-sentence justification based on the vulnerability description above.

| Metric | Your Value | Justification |
|---|---|---|
| Attack Vector (AV) | | |
| Attack Complexity (AC) | | |
| Privileges Required (PR) | | |
| User Interaction (UI) | | |
| Confidentiality Impact (C) | | |
| Integrity Impact (I) | | |
| Availability Impact (A) | | |

Scoring: 2 points per metric — 1 for correct value, 1 for accurate justification. Scope (S) is excluded from this exercise.

### Task 2B — Temporal Score Reasoning (5 points)

Explain in 3-4 sentences how the temporal score for this vulnerability would differ from the base score, and what specific factor in the vulnerability description most significantly affects the temporal score.

### Task 2C — Environmental Score Application (5 points)

Your organization uses this VPN appliance for all remote access. The management interface is segmented to a restricted internal VLAN accessible only to network administrators, not the public internet. In 3-4 sentences, explain how this environmental context should affect your organization's effective score for this vulnerability, and whether this environmental factor eliminates or only reduces the risk.

---

## Exercise 3: Prioritization Decision Memo (20 points)

### Exercise 3 Overview

Using the scan results from Exercise 1, write a prioritized remediation memo addressed to your IT infrastructure manager. This memo must communicate the top three findings requiring immediate action and explain why, in language accessible to a technical but non-security-specialist audience.

### Memo Format Requirements

Your memo must include the following sections and meet the length requirements:

Section 1 — Executive Summary (3-5 sentences): Briefly describe the overall scan scope and the most critical finding category. Do not use CVE IDs in this section — use plain language.

Section 2 — Top Three Immediate Actions (one paragraph per finding, 4-6 sentences each): For each of your top three findings, describe: what the vulnerability is (in plain language), why it is the highest priority, what the remediation action is, and what the target completion timeline should be.

Section 3 — Remaining Findings Summary (2-4 sentences): Briefly acknowledge the remaining findings and indicate when and how they will be addressed.

Section 4 — Risk Acceptance Statement: State whether any finding in the full scan should be considered for risk acceptance and justify the recommendation.

Scoring: 5 points for executive summary clarity and accuracy; 10 points for top three finding descriptions (technical accuracy, plain-language communication, timeline appropriateness); 3 points for remaining findings summary; 2 points for risk acceptance statement.

---

## Exercise 4: Scan Configuration Decisions (15 points)

### Exercise 4 Overview

Answer the following questions about vulnerability scanning configuration and methodology.

### Scan Question 1 (5 points)

Your manager asks you to choose between running credentialed and uncredentialed scans for the organization's internal server fleet. She says: "Uncredentialed scans are faster and we don't have to manage scan credentials. Why not just use those?" Write a 4-5 sentence response that defends the use of credentialed scanning for internal assets by explaining the specific technical advantages credentialed scanning provides over uncredentialed scanning.

### Scan Question 2 (5 points)

Your organization currently runs vulnerability scans quarterly. A new compliance requirement mandates monthly scans, but the security team lead suggests moving to continuous scanning instead. In 4-5 sentences, explain the security benefit of continuous scanning versus monthly scanning, and identify one operational challenge that continuous scanning introduces that must be addressed.

### Scan Question 3 (5 points)

Your scan results for a Linux server show a Critical vulnerability in OpenSSL version 1.0.2. Your system administrator says: "That version is not actually installed — the server runs a distribution that backported the security fix into an older version string." In 4-5 sentences, explain what type of scan finding this represents, why it occurs, and what the analyst should do to verify the administrator's claim and resolve the finding appropriately.

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Prioritized Ranking | 20 | Logical ranking justified by multiple factors; correct use of KEV, exploitability, criticality terminology |
| Exercise 1B — Remediation Types | 12 | Correct remediation type selected with accurate 2-sentence explanation for each of four findings |
| Exercise 1C — False Positive Assessment | 8 | Correct definition of false positive applied; finding correctly classified with clear reasoning |
| Exercise 2A — CVSS Base Metrics | 15 | Correct metric values with accurate justifications tied to vulnerability description |
| Exercise 2B — Temporal Score | 5 | Correct identification of temporal factor; accurate explanation of score modification |
| Exercise 2C — Environmental Score | 5 | Accurate assessment of environmental context impact; distinguishes reduction from elimination |
| Exercise 3 — Remediation Memo | 20 | All four sections present; technical accuracy; plain-language communication; realistic timelines |
| Exercise 4 — Scan Configuration | 15 | 5 points per question; technically accurate, specific reasoning for each answer |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Submit to the Canvas Module 03 Lab assignment by the posted deadline.
4. Late submissions are subject to the course late policy in the syllabus.

---

## Academic Integrity Notice

All work must be your own. The scan data in this lab is fabricated for educational purposes. Do not share answers before the submission deadline. Reference the CySA+ exam objectives at comptia.org and study materials at professormesser.com for additional context.

---

## Part 9 — Challenge Exercise

### Challenge 1: Prioritization Under Constraint

Your team has capacity to remediate exactly 3 findings this sprint. You have the following open findings: (1) CVE-2021-44228 (Log4Shell, CVSS 10.0) on an internet-facing Java application server — in the KEV catalog; (2) CVE-2023-22515 (Confluence RCE, CVSS 10.0) on an internal Confluence server accessible only from the corporate network — in the KEV catalog; (3) CVE-2022-30190 (Follina, CVSS 7.8) on 340 employee workstations — in the KEV catalog; (4) CVE-2022-1388 (F5 BIG-IP RCE, CVSS 9.8) on a load balancer in the DMZ — not in KEV; (5) CVE-2020-1472 (Zerologon, CVSS 10.0) on a domain controller — in the KEV catalog.

1. Select your top 3 remediation priorities and rank them. Justify each selection using at least two factors beyond CVSS score alone (e.g., asset criticality, exposure, KEV status, blast radius).
2. For the two findings you deferred, write a one-sentence compensating control recommendation for each that reduces risk while the patch is pending.
3. Explain why remediating the 340 workstations (Follina) in a single sprint may be operationally infeasible and what phased approach you would recommend.

### Challenge 2: Scan Result Interpretation

A credentialed scan of a Linux web server returns these findings: (A) OpenSSL 1.1.1 — CVE with CVSS 8.1, patch available; (B) Apache httpd 2.4.49 — CVE-2021-41773 (path traversal/RCE, CVSS 9.8), patch available, in KEV; (C) MySQL 5.7.38 — CVE with CVSS 5.4, no patch available from vendor; (D) PHP 7.4.3 — version identified but no CVE matched by scanner. The administrator states the server also runs a custom Python application, which the scanner did not assess.

1. Classify each finding (A–D) by remediation type: patch, workaround, compensating control, or risk acceptance — and justify each choice.
2. Explain what additional scanning action should be taken for the custom Python application and why the scanner's silence does not mean the application is vulnerability-free.
3. Write an executive one-paragraph summary (4–5 sentences) of the server's risk posture suitable for a non-technical manager.

### Reflection Questions

1. A peer argues that CVSS is the only metric needed for vulnerability prioritization because it provides an objective score. Construct a two-sentence counter-argument using a specific example where a CVSS 9.x finding should be deprioritized below a CVSS 7.x finding.
2. Describe one real-world scenario where accepting risk for a known vulnerability would be a defensible, professionally sound decision, and identify what documentation would be required to make that decision auditable.
