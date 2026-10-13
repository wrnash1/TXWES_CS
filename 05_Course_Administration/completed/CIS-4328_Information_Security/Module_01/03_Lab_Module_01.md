# Lab Activity — Module 01: Threat Classification Exercise

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | Authorized Educational Use Only

---

## Lab Overview

**Lab Title:** Threat and Control Classification Exercise

**Estimated Completion Time:** 60–90 minutes

**Submission:** Upload your completed deliverables to Canvas before the module deadline.

**Learning Objectives:**

- Classify attack descriptions by threat actor type, CIA triad property, and active/passive category.
- Apply the security controls framework to map controls to both category (Physical/Technical/Administrative) and function (Preventive/Detective/Corrective/Deterrent/Compensating/Directive).
- Analyze an organization's security posture and identify gaps.
- Connect lab findings to SY0-701 exam scenario reasoning.

---

## Background

In this lab you will act as a security analyst conducting a threat and control classification review for Ridgeline Financial Services, a mid-size credit union with 200 employees, two branch offices, and an online banking portal. You have been given a set of incident descriptions and a list of existing security controls. Your task is to classify each item using the frameworks from Module 01.

This lab uses scenario-based analysis only. No tools are installed, no systems are accessed, and no actual attacks are performed. All work is analytical and document-based, consistent with the type of performance-based questions (PBQs) that appear on the SY0-701 exam.

---

## Part A — Attack Scenario Classification (40 points)

Read each incident description below. For each one, complete the classification table by identifying:

1. The **Threat Actor Type** (Nation-State, Organized Crime, Hacktivist, Insider Threat, Script Kiddie)
2. The **CIA Triad Property** primarily violated (Confidentiality, Integrity, Availability, or Non-repudiation)
3. The **Attack Category** (Eavesdropping, Traffic Analysis, Replay, Injection, Man-in-the-Middle, Denial of Service, Brute Force, Zero-Day, or Social Engineering)
4. Whether the attack is **Active or Passive**
5. One **recommended technical control** to mitigate or detect this attack

### Incident Descriptions

**Incident 1:**
Ridgeline's IT team discovers that a competitor's employee has been running automated credential-stuffing scripts against the online banking portal login page for the past two weeks, using a list of username/password pairs leaked from an unrelated breach. Over 12,000 login attempts were recorded. Three accounts were successfully compromised.

**Incident 2:**
An employee in the loan processing department has been copying customer account files to a personal USB drive every Friday afternoon for three months. She recently resigned and accepted a position at a competing institution. The behavior was only discovered after her departure when an audit flagged her USB write activity in the endpoint logs.

**Incident 3:**
The online banking portal goes offline for four hours during peak business hours on a Monday morning. Log analysis shows that the web server received 2.3 million HTTP GET requests in a 10-minute window originating from thousands of different IP addresses distributed across multiple countries.

**Incident 4:**
A security researcher discovers an unknown vulnerability in the core banking software that Ridgeline uses. No patch exists. Within 72 hours of the researcher's private disclosure to the vendor, an attacker who apparently independently discovered the same flaw begins exploiting it against financial institutions, including Ridgeline.

**Incident 5:**
An attacker connects to the same coffee shop Wi-Fi network as a Ridgeline teller who is working remotely. The attacker uses ARP poisoning to position themselves between the teller's laptop and the router, silently capturing all unencrypted HTTP traffic including session cookies for internal applications that do not enforce HTTPS.

**Incident 6:**
Ridgeline's public-facing website is defaced overnight. The homepage is replaced with a political message criticizing the credit union's investment practices. The attackers post a statement on social media claiming responsibility and announcing they will leak internal documents unless the credit union divests from certain holdings within 48 hours.

**Incident 7:**
A network administrator captures packets on the internal VLAN between the core banking server and a workstation used by the finance team. Review of the captured data reveals that the legacy accounting application transmits usernames and passwords in plaintext over the network, with no encryption in transit.

**Incident 8:**
Ridgeline receives a targeted spear-phishing email claiming to be from their core banking software vendor. The email contains a link to a convincing replica of the vendor's support portal. Two employees enter their credentials on the fake site. The attacker then uses those credentials to access Ridgeline's vendor support portal and download configuration files containing database connection strings.

### Part A Deliverable — Classification Table

Create a table with the following columns and complete one row per incident:

| Incident | Threat Actor Type | CIA Property Violated | Attack Category | Active or Passive | Recommended Technical Control |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |

**Part A is worth 40 points — 5 points per incident.**

For full credit on each incident, all five fields must be correctly identified and the recommended control must be technically appropriate and specifically address the attack vector described.

---

## Part B — Security Controls Assessment (40 points)

Ridgeline Financial Services has the following security controls in place. For each control, identify:

1. The **Control Category** (Physical, Technical, or Administrative)
2. The **Control Function** (Preventive, Detective, Corrective, Deterrent, Compensating, or Directive)
3. A brief **justification** (one to two sentences explaining why you selected those classifications)

### Ridgeline's Current Controls

**Control 1:** All employees must complete a mandatory 30-minute information security awareness training course every year. Completion is tracked in the HR system and non-completion results in a written warning.

**Control 2:** The data center entrance uses a mantrap — a double-door system where the first door must close and the person must be badge-authenticated before the second door opens.

**Control 3:** All system and application logs are forwarded in real time to a centralized SIEM platform hosted in a separate network zone. Log retention is set to 13 months.

**Control 4:** A backup generator provides power to all critical systems if utility power is lost. The generator is tested monthly and fuel is maintained for 72 hours of operation.

**Control 5:** After a ransomware incident at a peer institution, Ridgeline's IT team installed endpoint detection and response software on all workstations. The EDR software monitors process behavior and alerts the SOC team when suspicious activity is detected.

**Control 6:** The server room door has a combination lock that requires a six-digit PIN. The PIN is posted on a sticky note on the door because staff found it inconvenient to remember. As a compensating measure, a security camera monitors the hallway outside the server room.

**Control 7:** A policy document titled "Acceptable Use of Information Technology Resources" is distributed to all employees on their first day and must be signed before network access is granted.

**Control 8:** After discovering that several employees had local administrator rights on their workstations that they did not need, the IT team revoked those rights and implemented a standard user account baseline using Group Policy.

### Part B Deliverable — Controls Classification Table

| Control | Category | Function | Justification |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

**Part B is worth 40 points — 5 points per control.**

Note: Control 6 describes a situation where a compensating control is in place because the primary control (the PIN) has been effectively defeated. For full credit, your classification must address both the primary and compensating aspects.

---

## Part C — Security Posture Gap Analysis (20 points)

Based on your work in Parts A and B, write a short gap analysis memo addressed to Ridgeline's Chief Information Security Officer. Your memo must:

1. Identify **three specific security gaps** revealed by the incidents in Part A that Ridgeline's existing controls in Part B do not adequately address. (6 points)
2. For each gap, recommend **one specific additional control** — stating its category and function — that would close the gap. (6 points)
3. Explain which **CIA Triad property** is most at risk for Ridgeline based on the overall pattern of incidents, and justify your answer. (4 points)
4. Identify which **threat actor type** poses the greatest current risk to Ridgeline and explain why. (4 points)

**Format:** 300–450 words. Use complete sentences. Use the control classification vocabulary from Module 01.

---

## Submission Instructions

Submit the following to Canvas before the module deadline:

- Part A: Completed classification table (may be in a Word document, Google Doc, or PDF)
- Part B: Completed controls classification table with justifications
- Part C: Gap analysis memo

Label each part clearly. Include your full name and student ID on all submitted documents.

---

## 100-Point Rubric

| Component | Points Available | Scoring Criteria |
|---|---|---|
| Part A — Attack Classification Table | 40 | 5 pts per incident. Full credit requires correct entries in all five columns and a technically appropriate recommended control. Partial credit of 3 pts awarded if three or more columns are correct. |
| Part B — Controls Classification Table | 40 | 5 pts per control. Full credit requires correct Category, correct Function, and a complete justification. Partial credit of 3 pts if Category and Function are correct but justification is missing. |
| Part C — Gap Analysis Memo | 20 | 6 pts for identifying three valid gaps with evidence from Parts A/B; 6 pts for three corresponding control recommendations with correct category and function labels; 4 pts for CIA property analysis; 4 pts for threat actor risk analysis. |
| **Total** | **100** | |

---

## Answer Key Notes for Instructor Use

Part A selected answers for reference:

- Incident 1: Organized Crime or Script Kiddie (either acceptable) / Confidentiality / Brute Force (credential stuffing is a brute-force variant) / Active / Account lockout policy or CAPTCHA or MFA
- Incident 2: Insider Threat / Confidentiality / Data Exfiltration (accept as active) / Active / DLP (Data Loss Prevention) tool with USB write blocking
- Incident 3: Any actor type acceptable (DDoS can be from any) / Availability / Denial of Service / Active / DDoS mitigation service / rate limiting
- Incident 4: Nation-State (zero-day with rapid weaponization suggests sophistication) / Varies / Zero-Day Exploit / Active / EDR behavioral monitoring, network segmentation
- Incident 5: Organized Crime or any / Confidentiality / Man-in-the-Middle (ARP poisoning) / Active / HTTPS enforcement, VPN requirement for remote work
- Incident 6: Hacktivist / Integrity (defacement) and Confidentiality (threatened leak) / accept either / Active / Web application firewall, integrity monitoring on web root
- Incident 7: This describes a vulnerability discovery, not an attack — accept Passive if student notes the sniffer is not attacking; the underlying issue is unencrypted protocol / Confidentiality / Eavesdropping / Passive / Enforce TLS on all internal application traffic
- Incident 8: Organized Crime / Confidentiality / Social Engineering / Phishing / Active / Security awareness training, email filtering, MFA on vendor portal

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Threat Actor Motivation Mapping

Using the MITRE ATT&CK framework at <https://attack.mitre.org/groups/>, look up two real-world threat actor groups — one attributed to a nation-state and one attributed to organized crime.

1. For each group, record: the group name, attributed country or criminal organization, primary motivation, and at least three TTPs (tactics, techniques, procedures) listed in their ATT&CK profile.
2. Map each group's TTPs to the CIA Triad property most threatened by each technique.
3. For each group, identify one IOC category (network, host, account, file) that would be most useful for detecting their activity in an enterprise environment and explain why.

### Challenge 2: Security Control Gap Analysis for a Real Scenario

A small regional hospital has the following current security controls in place: signature-based antivirus on all workstations, a perimeter firewall with no egress filtering, annual security awareness training, and paper sign-in logs for the server room.

1. Map each existing control to the correct Category (Physical/Technical/Administrative) and Function (Preventive/Detective/Corrective/Deterrent/Compensating/Directive).
2. Identify at least four security gaps — controls that are absent — and for each gap, name the specific attack scenario from Ridgeline's Module 01 incident list that the missing control would address.
3. Propose a prioritized remediation plan listing the three most critical missing controls in order of priority. Justify each prioritization using the CIA Triad property most at risk.

### Reflection Questions

1. After completing both challenges, explain in your own words why threat actor motivation matters when selecting security controls. Give a specific example where the same vulnerability would require different control responses depending on whether the threat actor is a nation-state versus a script kiddie.
2. In the hospital gap analysis, one of the existing controls — annual security awareness training — is classified as Administrative/Preventive. A security manager argues that training is actually a Directive control because it tells employees what to do. How would you resolve this classification disagreement, and what does the correct classification tell you about the control's purpose?

---

Texas Wesleyan University — CIS-4328 Information Security — Module 01 Lab

Proprietary and Confidential. Not for disclosure outside of authorized course use.
