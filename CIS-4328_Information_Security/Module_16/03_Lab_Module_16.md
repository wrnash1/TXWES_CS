# Lab Activity: Module 16 — Security+ SY0-701 Exam Preparation and Capstone

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Overview

This final lab has two parts. Part A is a hands-on technical exercise using open-source security tools to reinforce the exam domains. Part B is a structured exam simulation that replicates the SY0-701 timed environment. Together they represent 90–120 minutes of active preparation that targets the highest-weighted exam domains.

---

## Learning Objectives

By completing this lab you will be able to:

- Use Nmap to perform a basic vulnerability-oriented network scan and interpret the results
- Analyze Windows Security Event Log entries and map them to attack patterns
- Apply the NIST IR lifecycle to a realistic incident scenario
- Complete a 20-question timed practice exam under simulated test conditions
- Perform a post-practice-exam gap analysis targeting domains where errors occurred

---

## Prerequisites

- A Windows, Linux, or macOS workstation
- Nmap installed (available free at nmap.org) or access to TryHackMe / Hack The Box free tier
- Access to the Windows Event Viewer (Windows users) or a sample EVTX log file (all platforms — provided below)
- Professor Messer's SY0-701 practice exam access (free at professormesser.com) or any comparable practice exam resource

---

## Part A: Technical Security Exercises (45–60 minutes)

### Exercise 1 — Nmap Reconnaissance and Service Enumeration (20 minutes)

This exercise reinforces Domain 2 (Threats, Vulnerabilities) and Domain 3 (Architecture) by simulating the reconnaissance phase of the Cyber Kill Chain.

#### Task 1.1 — Install and verify Nmap

Download and install Nmap from nmap.org. Verify the installation:

```
nmap --version
```

Expected output: version string confirming Nmap is installed (e.g., `Nmap version 7.94`).

#### Task 1.2 — Scan your local subnet

Perform a host discovery scan on your local network segment. Replace `192.168.1.0/24` with your actual subnet if different:

```
nmap -sn 192.168.1.0/24
```

The `-sn` flag performs a ping scan (host discovery only) without port scanning. This is a safe, non-intrusive scan.

Record the number of hosts discovered and their IP addresses.

#### Task 1.3 — Service version scan on your own machine

Perform a service and version detection scan against your own workstation's localhost:

```
nmap -sV -p 22,80,443,3389,5432,8080 127.0.0.1
```

This scans six common ports for service banner information. Do not scan any system you do not own or have explicit permission to scan.

#### Task 1.4 — Interpret and document findings

For each open port found in Task 1.3, answer these questions:

- What service is running on this port?
- What is the potential security risk if this port is exposed to the internet?
- What control would you recommend to mitigate that risk?

#### Deliverable 1

A table with columns: Port, Service Detected, Security Risk, Recommended Control. Minimum three rows (or "no open ports detected" with an explanation of why a secure system would show this result).

---

### Exercise 2 — Windows Event Log Analysis (20 minutes)

This exercise reinforces Domain 4 (Security Operations) by practicing SIEM-style log analysis.

#### Task 2.1 — Examine recent Security Event Log entries

On a Windows workstation, open Event Viewer:

1. Press Win + R, type `eventvwr.msc`, press Enter
2. Navigate to Windows Logs → Security
3. Filter the log for the following Event IDs: 4624, 4625, 4648, 4720

For each Event ID found, record:

- When it occurred (timestamp)
- Which account was involved
- The Logon Type (for 4624 and 4625) — types 2 (interactive), 3 (network), 10 (remote interactive) are most relevant

If you are on Linux/macOS, use the sample scenario below instead.

#### Task 2.2 — Sample scenario analysis (Linux/macOS alternative)

Analyze this simulated Windows Security event log excerpt. Answer the questions that follow:

```
[2026-06-01 02:14:07] Event ID 4625 — Logon Failure
  Account: administrator
  Failure Reason: Unknown user name or bad password
  Source IP: 198.51.100.42
  Logon Type: 3

[2026-06-01 02:14:09] Event ID 4625 — Logon Failure
  Account: administrator
  Source IP: 198.51.100.42
  Logon Type: 3

[2026-06-01 02:14:11] Event ID 4625 — Logon Failure
  Account: administrator
  Source IP: 198.51.100.42
  Logon Type: 3

... (47 more identical entries in 90 seconds)

[2026-06-01 02:15:52] Event ID 4624 — Logon Success
  Account: administrator
  Source IP: 198.51.100.42
  Logon Type: 3
```

**Analysis Questions**:

1. What type of attack does this sequence indicate? What specific term describes this automated technique?
2. Which MITRE ATT&CK technique (T-number and name) maps to this activity?
3. What is the significance of Logon Type 3 in this context?
4. What three defensive controls would you recommend to prevent this attack from succeeding?
5. According to the NIST IR lifecycle, what phase are you currently in, and what is the next phase?

#### Deliverable 2

Written answers to the five analysis questions, minimum two sentences each.

---

### Exercise 3 — Incident Response Tabletop (15 minutes)

This exercise reinforces Domain 4 (Security Operations) IR lifecycle phases.

#### Scenario

Your organization's SOC receives the following alert at 10:47 AM on a Tuesday:

A SIEM correlation rule triggered: 14 endpoints in the Finance department made DNS queries to the domain `update-adobe-flash[.]com` within a 6-minute window. Network egress logs show encrypted outbound connections from 3 of those endpoints to IP 198.51.100.77 on port 443. Two of the three endpoints are currently showing high CPU utilization (85–95%). HR confirms that a company-wide email about a mandatory "Adobe security update" was sent this morning — but IT did not send that email.

#### Tabletop Tasks

For each NIST IR phase, document what the security team should do in this specific scenario:

**Phase 1 — Preparation**: What pre-existing documentation, tools, or procedures should already be in place that this scenario tests?

**Phase 2 — Detection and Analysis**: The SOC has just received the alert. What additional data should analysts gather before declaring this a confirmed incident? Name at least three specific data sources.

**Phase 3 — Containment**: What immediate containment steps should be taken? Distinguish between short-term containment (stops active spread now) and long-term containment (allows forensic investigation to continue).

**Phase 4 — Eradication**: Once the threat is fully understood, what eradication steps are required? What is the danger of eradicating before completing forensic analysis?

**Phase 5 — Recovery**: How would the team safely return the three affected endpoints to production? What validation steps are needed before restoring full network access?

**Phase 6 — Post-Incident Activity**: What should be included in the post-incident report? Who should receive it?

#### Deliverable 3

Written tabletop response addressing all six phases. Minimum one substantive paragraph per phase.

---

## Part B: Timed Exam Simulation (45–60 minutes)

### Exercise 4 — Full Practice Exam Under Test Conditions

This is the most important exam preparation activity you can do.

#### Setup

Before starting:

- Close all other applications
- Set a timer for 90 minutes
- Have only the practice exam open — no notes, no browser tabs, no video

#### Recommended Practice Exam Sources (free)

- Professor Messer SY0-701 practice exams: professormesser.com
- CompTIA sample questions: comptia.org/certifications/security
- Jason Dion practice tests: a paid option with 6 full-length exams

Use a source with at minimum 90 questions so you can simulate a full exam attempt.

#### During the Exam Simulation

Apply these strategies as practiced in the video scripts:

- Skip performance-based questions (PBQs) on first pass; flag and return
- Read the last sentence of each scenario question first to identify what is being asked
- Eliminate obviously wrong answers before selecting among close contenders
- Never leave a question unanswered — guess if necessary
- Watch your time: target 75 questions in the first 45 minutes

#### Task 4.1 — Complete the 90-question simulation

Complete the full exam without pausing. Record your final score when time expires or all questions are answered.

#### Task 4.2 — Gap Analysis

After completing the simulation, perform a structured gap analysis:

For every incorrect answer, document:

- The question number
- The domain (1–5) it belongs to
- What the correct answer is
- Why your chosen answer was wrong (distractor category: wrong scope, wrong service, wrong phase, correct concept applied incorrectly)

Create a domain score summary:

| Domain | Questions Attempted | Correct | Score % |
|---|---|---|---|
| Domain 1 — General Security Concepts | | | |
| Domain 2 — Threats, Vulnerabilities | | | |
| Domain 3 — Security Architecture | | | |
| Domain 4 — Security Operations | | | |
| Domain 5 — Program Management | | | |
| Total | | | |

#### Task 4.3 — Targeted review

For any domain scoring below 70%, complete a focused review before your actual exam:

- Below 70% on Domain 1: Re-read cryptography and PKI sections of your study guide
- Below 70% on Domain 2: Review MITRE ATT&CK matrix and malware taxonomy
- Below 70% on Domain 3: Review NIST SP 800-207 Zero Trust and cloud shared responsibility
- Below 70% on Domain 4: Re-read NIST SP 800-61 IR lifecycle and Event Log reference
- Below 70% on Domain 5: Practice ALE/SLE calculations and review GDPR/PCI DSS/HIPAA scope

#### Deliverable 4

Your domain score summary table and a list of at minimum five incorrect questions with gap analysis notes.

---

## Deliverables Summary

| Deliverable | Description | Points |
|---|---|---|
| Deliverable 1 | Nmap port scan results table (3+ rows) | 20 |
| Deliverable 2 | Event log analysis — five question answers | 20 |
| Deliverable 3 | IR tabletop — six phase responses | 25 |
| Deliverable 4 | Practice exam score + gap analysis (5+ items) | 35 |
| Total | | 100 |

Submit all four deliverables as a single document via Canvas LMS.

---

## Grading Rubric Detail

**Deliverable 1 (20 pts)**: 5 pts for completing the scan and showing output. 5 pts per row for accurate service identification, meaningful risk description, and a specific (not generic) control recommendation. Partial credit for fewer than three rows.

**Deliverable 2 (20 pts)**: 4 pts per question answer. Full credit requires: correct attack technique name (Q1), correct ATT&CK T-number (Q2), correct Logon Type interpretation (Q3), three specific distinct controls with brief justification (Q4), correct IR phase identification with correct next phase (Q5).

**Deliverable 3 (25 pts)**: ~4 pts per phase. Full credit requires phase-specific actions tied to this scenario (not generic IR descriptions). Containment must distinguish short-term from long-term. Eradication must note the forensic analysis prerequisite.

**Deliverable 4 (35 pts)**: 10 pts for completing the simulation and providing the domain score table. 25 pts for the gap analysis — 5 pts per analyzed question for correct domain identification, correct answer notation, and meaningful distractor explanation.

---

## The Actual Exam — Final Reminder

Your final exam for this course is the official **CompTIA Security+ SY0-701** certification exam. Schedule it at a Pearson VUE testing center or via online proctoring at comptia.org/certifications/security.

Upon completion, upload your official score report (PDF, screenshot, or photograph of the printed report) to the designated Canvas assignment. Your course grade will include the prorated exam score as outlined in the syllabus grading policy.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*

---

**Objective:** 
Your final exam for this course is the official **CompTIA Security+ (SY0-701)** certification exam. You must schedule and take this exam at the ComputerMinds testing center.

**Instructions:**
1. Arrive at the ComputerMinds testing center at your scheduled time with two forms of valid ID.
2. Complete the CompTIA Security+ (SY0-701) exam.
3. Once finished, you will receive an official printout or digital copy of your score report.

**Deliverable:**
Upload a scanned copy, clear photograph, or official PDF of your final score report to this Canvas drop-box. 

*Note: Your final grade will be calculated based on the prorated score of this exam as outlined in the Syllabus Grading Policy.*

---

## Part 9 — Challenge Exercise

### Challenge 1: Full-Spectrum Incident Response Simulation

A regional hospital network's SOC receives the following sequence of events over a 72-hour period:

- **Hour 0**: A phishing email impersonating the hospital's IT helpdesk is delivered to 340 staff. The email links to a credential harvesting page mimicking the hospital's VPN login portal.
- **Hour 2**: Fourteen staff members submit credentials to the fake portal. The threat actor uses harvested credentials to authenticate to the hospital's Remote Desktop Gateway from four distinct Eastern Europe IP addresses.
- **Hour 6**: Lateral movement begins — the attacker uses compromised credentials to access three clinical workstations and the billing server. A SIEM alert fires on anomalous after-hours RDP lateral movement.
- **Hour 18**: The attacker deploys ransomware that begins encrypting file shares, including the EHR system's shared storage. Ransom demand: $2.4 million in cryptocurrency within 48 hours.
- **Hour 72**: The hospital must decide whether to pay the ransom, restore from backup, or negotiate.

**Task 1.1 — NIST IR Phase Mapping**: For each of the six NIST IR phases, identify the specific actions the hospital's security team should have taken or should take at each phase in this scenario. For each phase, identify at least one preparation gap that allowed the attack to progress to the next stage.

**Task 1.2 — MITRE ATT&CK Mapping**: Map each of the five attacker actions described (phishing delivery, credential theft, RDP authentication, lateral movement, ransomware deployment) to the correct MITRE ATT&CK tactic and technique. Use the format: Tactic Name (TA####) — Technique Name (T####).

**Task 1.3 — Containment Decision Analysis**: At Hour 18, the SOC has three containment options: (A) isolate only the confirmed-affected clinical workstations, (B) take the entire EHR system offline and isolate the affected network segment, or (C) allow operations to continue while monitoring to gather more threat intelligence. Evaluate each option against the criteria of: patient safety impact, data loss risk, forensic preservation, and recovery timeline. Which option do you recommend and why?

**Task 1.4 — Ransom Decision Framework**: At Hour 72, draft a one-page memo to the hospital CEO that: (1) explains the legal and ethical considerations of paying the ransom, (2) assesses whether the hospital can restore operations from backup without paying, and (3) identifies the regulatory reporting obligations triggered by this incident (name the specific regulation, the notification timeline, and the recipient).

---

### Challenge 2: Cross-Domain Security Architecture Review

A fintech startup is launching a cloud-native payment processing platform. The architecture consists of: a React front-end hosted on AWS CloudFront, a Node.js API layer on AWS Lambda, a PostgreSQL database on AWS RDS with Multi-AZ, and a third-party fraud detection microservice accessed via API over the internet. The company will process Visa and Mastercard transactions, store cardholder data for recurring billing, and serve customers in the US and EU.

**Task 2.1 — Threat Modeling**: Using the STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), identify one realistic threat for each STRIDE category specific to this architecture. For each threat, identify the component most at risk and one specific mitigating control.

**Task 2.2 — Compliance Obligation Matrix**: Identify every compliance obligation triggered by this architecture. For each, specify: the framework name, what specific aspect of the architecture triggers it, the most operationally demanding single requirement, and the maximum penalty for non-compliance. Present as a table.

**Task 2.3 — Defense-in-Depth Architecture Review**: The security team has implemented: TLS 1.2 in transit, AES-256 encryption at rest for the RDS database, API gateway rate limiting, and AWS WAF in front of CloudFront. Identify three significant security gaps not addressed by the current controls. For each gap, name the missing control, explain the specific attack it prevents, and reference the relevant SY0-701 exam objective domain.

**Task 2.4 — Identity Architecture Design**: The platform needs to support: customer authentication via social login (Google/Apple), internal developer access to AWS resources with MFA, and the third-party fraud detection service accessing the API. For each of the three access patterns, specify: the appropriate identity protocol (SAML, OIDC, OAuth 2.0, AWS IAM roles, etc.), the minimum required MFA method, and the access revocation mechanism.

---

### Reflection Questions

1. Throughout this course you have studied five Security+ exam domains: General Security Concepts, Threats and Vulnerabilities, Security Architecture, Security Operations, and Security Program Management. Reflecting on the incidents and scenarios in this lab, identify the single domain where you believe real-world organizations most frequently have critical gaps, and explain your reasoning using two specific examples from the lab scenarios above. Then describe what a newly hired security analyst could realistically accomplish in their first 90 days to begin closing gaps in that domain.

2. The CompTIA Security+ certification is often described as a "mile wide and an inch deep" — broad coverage of many topics without deep specialization in any single area. Some hiring managers argue this breadth is exactly what entry-level security roles require; others argue that hands-on certifications like CEH or OSCP provide more practical value. Evaluate both positions. Based on your experience completing this course, what do you believe is the appropriate next certification or skill development path after Security+, and how does it build on the foundation this course established?

---

End of Lab — Module 16
