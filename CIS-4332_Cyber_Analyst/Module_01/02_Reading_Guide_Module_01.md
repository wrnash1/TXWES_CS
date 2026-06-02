# Reading Guide: Module 01 - Security Operations & Analyst Role

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Introduction

Module 01 establishes the conceptual and operational foundation for everything that follows in this course. Before you can analyze threats, hunt adversaries, or write detection rules, you need to understand the environment you work in — the Security Operations Center — and the professional role you occupy as an analyst. This module maps directly to CompTIA CySA+ CS0-003 **Domain 1: Security Operations**, which represents the single largest domain on the exam at 33% of the total score.

Work through every section of this guide before completing the lab. All glossary terms are fair game on the quiz. The exam tip boxes contain patterns that appear repeatedly in CySA+ scenario questions.

---

## Section 1: The Security Operations Center

### 1.1 SOC Definition and Mission

A Security Operations Center is a centralized team, facility, and set of processes responsible for continuously monitoring an organization's security posture, detecting threats, investigating incidents, and coordinating response. The SOC operates 24 hours a day, 7 days a week in enterprise environments.

The SOC mission is typically described with three verbs:

- **Detect** — identify malicious or suspicious activity as quickly as possible
- **Respond** — contain the threat and minimize damage
- **Recover** — restore normal operations and prevent recurrence

The SOC is distinct from an IT operations team. IT builds and maintains systems. The SOC watches those systems for threats. In many organizations, SOC and IT teams must coordinate during incidents, which requires clear communication protocols.

### 1.2 SOC Models

Organizations implement SOCs in different configurations depending on size, budget, and risk posture.

| Model | Description | Typical User |
|---|---|---|
| Internal SOC | Fully in-house team, dedicated facility | Large enterprises, regulated industries |
| Virtual SOC | Remote analysts, no dedicated facility | Mid-size organizations |
| Co-Managed SOC | Internal staff augmented by MSSP | Organizations with partial security staff |
| Fully Outsourced (MSSP) | Managed Security Service Provider operates SOC | Small organizations, budget-constrained |
| Hybrid SOC | Combination of internal and outsourced functions | Large organizations with specialized needs |

### 1.3 The Tiered Analyst Model

The tiered model is a core CySA+ exam topic. Know each tier's responsibilities precisely.

| Tier | Title | Primary Responsibilities |
|---|---|---|
| Tier 1 | Alert Monitor / SOC Analyst I | Alert queue monitoring, playbook execution, false positive filtering, initial documentation, escalation to Tier 2 |
| Tier 2 | Incident Responder / SOC Analyst II | Deep investigation, multi-source correlation, threat containment, incident management, incident reporting |
| Tier 3 | Threat Hunter / Senior Analyst | Proactive threat hunting, malware analysis, custom detection rule development, SME support, TTP research |
| SOC Manager | Program Manager | Staffing, metrics, executive reporting, legal/HR coordination, program improvement |

Escalation flows upward: Tier 1 escalates to Tier 2. Knowledge flows downward: Tier 3 findings improve Tier 1 playbooks.

---

## Section 2: The CIA Triad

### 2.1 Core Definitions

The CIA Triad is the foundational security model. Every security control, every threat, and every incident can be analyzed through its three pillars.

| Pillar | Definition | Example Attack | Example Control |
|---|---|---|---|
| Confidentiality | Only authorized parties can access information | Data exfiltration, eavesdropping, credential theft | Encryption, access controls, DLP, MFA |
| Integrity | Data is not altered without authorization | Log tampering, SQL injection, man-in-the-middle modification | Hashing, digital signatures, FIM, change management |
| Availability | Systems and data are accessible when needed | Ransomware, DDoS, destructive malware | Redundancy, backups, failover, rate limiting |

### 2.2 Applying the CIA Triad to Scenarios

When the exam presents a scenario and asks which pillar was violated, use this decision logic:

- Did the attacker **see** something they should not have seen? → Confidentiality
- Did the attacker **change** something without authorization? → Integrity
- Did the attacker **prevent access** to something? → Availability

Many real-world attacks violate multiple pillars simultaneously. Ransomware encrypts files (Availability) and sometimes exfiltrates data before encrypting (Confidentiality). Prioritize the primary harm for exam answers.

---

## Section 3: Data Sources and the SIEM

### 3.1 Log Sources

| Source | What It Records | Key Fields |
|---|---|---|
| Firewall logs | Connection attempts (allowed/denied) at network perimeter | Source IP, destination IP, port, protocol, action |
| Authentication logs | Login attempts (success/failure), account lockouts | Username, source IP, timestamp, result, event ID |
| Endpoint logs | Process creation, file activity, registry changes, host connections | PID, process name, parent process, file path, user |
| Network traffic | Protocol-level data, flow records, packet captures | Source/dest IP and port, bytes, flags, protocol |
| Application logs | Web server requests, database queries, email gateway events | URL, HTTP status, query text, sender/recipient |
| DNS logs | Domain name queries and responses | Queried domain, response IP, client IP, query type |
| DHCP logs | IP address assignment and release events | MAC address, assigned IP, lease time, hostname |

### 3.2 SIEM Functions

The SIEM (Security Information and Event Management) platform performs four key functions:

1. **Log aggregation** — collects logs from all sources in the environment
2. **Normalization** — converts logs from different formats into a common schema
3. **Correlation** — applies rules that compare events across sources and time windows to detect patterns
4. **Alerting** — generates alerts when correlation rules fire

The SIEM does NOT block traffic. Blocking is performed by the IPS, firewall, or EDR tool. This distinction is frequently tested.

### 3.3 Sample SIEM Query Syntax

Different SIEM platforms use different query languages. Below are examples in Splunk SPL and a generic SQL-style syntax.

**Splunk SPL — Failed authentication events in the last 24 hours:**

```splunk
index=authentication action=failure earliest=-24h
| stats count by src_ip, user
| where count > 10
| sort -count
```

**Splunk SPL — Successful login after multiple failures (brute-force success pattern):**

```splunk
index=authentication
| transaction user maxspan=1h
| where mvcount(action) > 1 AND mvfind(action, "success") >= 0
| table _time, user, src_ip, action
```

**Generic SQL-style SIEM query — Firewall connections to known malicious IPs:**

```sql
SELECT timestamp, src_ip, dest_ip, dest_port, action
FROM firewall_logs
WHERE dest_ip IN (SELECT ip FROM threat_intel_feed WHERE category = 'malicious')
  AND timestamp > NOW() - INTERVAL 1 HOUR
ORDER BY timestamp DESC;
```

---

## Section 4: Alert Triage and the Analyst Workflow

### 4.1 The Five-Step Triage Process

| Step | Action | Key Questions |
|---|---|---|
| 1. Review | Read the alert details | What rule fired? What is the severity? What are the source and destination? |
| 2. Gather context | Pull supporting data — logs, TI feeds, asset inventory | Is the source IP known malicious? Is this user/system expected to do this? |
| 3. Classify | Determine true positive or false positive | Does the evidence confirm malicious or suspicious activity? |
| 4. Document | Record findings and reasoning in the ticketing system | What evidence did you examine? Why did you make this determination? |
| 5. Escalate or close | Escalate TPs to Tier 2; close FPs with tuning notes | Is immediate containment required? |

### 4.2 Alert Classification Matrix

| Classification | Alert Fired? | Actual Attack? | Meaning |
|---|---|---|---|
| True Positive (TP) | Yes | Yes | Real threat correctly detected — escalate |
| False Positive (FP) | Yes | No | Legitimate activity incorrectly flagged — close and tune |
| True Negative (TN) | No | No | No threat, no alert — desired state |
| False Negative (FN) | No | Yes | Real threat missed — most dangerous scenario |

False negatives represent detection gaps. They are identified through threat hunting, post-incident analysis, or red team exercises.

---

## Section 5: Indicators of Compromise

### 5.1 IOC Types and Examples

| IOC Type | Description | Examples |
|---|---|---|
| File-based | Cryptographic hash of a known malicious file | MD5: d41d8cd98f00b204e9800998ecf8427e |
| Network-based | Malicious IP, domain, or URL | 185.220.101.0/24, evil-c2-domain.ru |
| Host-based | Registry modifications, scheduled tasks, abnormal processes | HKLM\Software\Microsoft\Windows\CurrentVersion\Run malware_persist |
| Behavioral | Patterns of activity suggesting compromise | Outbound DNS queries to newly registered domains at 2 AM |
| Email-based | Sender addresses, subject lines, attachment hashes associated with phishing | Sender spoofing [email protected] |

### 5.2 The Pyramid of Pain

The Pyramid of Pain (David Bianco) describes the difficulty for defenders to detect versus the cost to attackers to change each IOC type.

| Level | IOC Type | Detection Difficulty | Attacker Cost to Change |
|---|---|---|---|
| Base | Hash values | Easy for defenders | Near zero — recompile or add a byte |
| 2 | IP addresses | Easy | Low — use new infrastructure |
| 3 | Domain names | Moderate | Low — register new domain |
| 4 | Network/host artifacts | Moderate | Moderate — change tooling |
| 5 | Tools | Hard | High — develop or adapt new tools |
| Top | TTPs | Hardest | Highest — change fundamental behavior |

Blocking at the TTP level makes attacks genuinely difficult. Blocking only at the hash level provides minimal lasting protection.

---

## Section 6: Key Metrics

### 6.1 SOC Performance Metrics

| Metric | Definition | Why It Matters |
|---|---|---|
| Mean Time to Detect (MTTD) | Average time from intrusion start to SOC detection | High MTTD = detection gaps or rule tuning issues |
| Mean Time to Respond (MTTR) | Average time from detection to containment/remediation | High MTTR = slow playbooks or staffing issues |
| False Positive Rate | Percentage of alerts that are not real threats | High FPR = rule over-sensitivity, analyst fatigue |
| Dwell Time | How long an attacker was active before detection | High dwell time = threat hunting gap |
| Alert Volume | Total alerts generated per time period | Sudden spikes may indicate active attack or rule change |

---

## Section 7: Relevant Frameworks

### 7.1 Intelligence Frameworks Overview

| Framework | Purpose | Key Concepts |
|---|---|---|
| MITRE ATT&CK | Adversary tactics and techniques | 14 tactics, hundreds of techniques, organized by kill chain phase |
| Cyber Kill Chain (Lockheed Martin) | Linear attack progression model | 7 phases from Reconnaissance to Actions on Objectives |
| Diamond Model | Analytical model for intrusion analysis | Four vertices: Adversary, Capability, Infrastructure, Victim |
| NIST CSF | Cybersecurity risk framework | Identify, Protect, Detect, Respond, Recover |

Module 02 covers MITRE ATT&CK in full depth. For now, understand that these frameworks give analysts a shared vocabulary for describing and organizing threat information.

---

## CySA+ Exam Tips

**Exam Tip 1 — Triage order:** When asked what a Tier 1 analyst should do first upon receiving an alert, the answer is always to verify the alert is genuine before taking containment action. Premature blocking or escalation without investigation is a trap answer.

**Exam Tip 2 — SIEM vs. IPS:** The SIEM generates alerts. The IPS blocks traffic. Exam questions sometimes describe a SIEM as if it takes action — it does not. The analyst takes action based on SIEM output.

**Exam Tip 3 — CIA Triad scenarios:** For any attack scenario, identify whether the attacker viewed (Confidentiality), changed (Integrity), or blocked access to (Availability) a resource. Many attacks touch multiple pillars — select the primary impact.

**Exam Tip 4 — False negatives are the most dangerous:** The exam may ask which alert classification is most concerning. False negatives represent undetected attacks — they are the most dangerous because you have no visibility.

**Exam Tip 5 — Escalation criteria:** Know what triggers escalation from Tier 1 to Tier 2: confirmed true positive with evidence of active compromise, lateral movement indicators, data exfiltration signals, or incidents affecting critical systems or high-value accounts.

**Exam Tip 6 — Dwell time:** If an exam question asks about a long undetected intrusion, the contributing factor is high dwell time. The mitigation is improved threat hunting capabilities and better behavioral detection rules.

**Exam Tip 7 — Pyramid of Pain application:** If an exam question asks which indicator type provides the most lasting protection when blocked, the answer is TTPs. Hashes and IPs are easy for attackers to cycle.

**Exam Tip 8 — Documentation requirement:** Alert documentation is not optional — it is required for audit trails, incident reports, legal proceedings, and detection rule tuning. Exam questions on SOC best practices will include documentation as a correct answer component.

---

## Glossary

- **CIA Triad** — Confidentiality, Integrity, Availability; the three pillars of information security
- **SIEM** — Security Information and Event Management; aggregates logs and generates correlation-based alerts
- **IOC** — Indicator of Compromise; observable artifact suggesting a system has been compromised
- **TTP** — Tactics, Techniques, and Procedures; describes how an adversary operates
- **True Positive** — Alert fired and a real threat exists
- **False Positive** — Alert fired but no real threat exists
- **False Negative** — Real threat exists but no alert fired
- **True Negative** — No threat and no alert
- **MTTD** — Mean Time to Detect; average time from intrusion to detection
- **MTTR** — Mean Time to Respond; average time from detection to containment
- **Dwell Time** — Duration an attacker operates in an environment before detection
- **Playbook** — Documented step-by-step procedure for responding to a specific alert type
- **Runbook** — Operational procedure guide; often used synonymously with playbook
- **Tier 1 Analyst** — Entry-level SOC analyst responsible for initial alert triage
- **Tier 2 Analyst** — Mid-level analyst responsible for incident investigation and containment
- **Tier 3 Analyst** — Senior analyst responsible for threat hunting and detection development
- **SOC Manager** — Program lead responsible for SOC staffing, metrics, and executive reporting
- **MSSP** — Managed Security Service Provider; outsourced SOC services
- **Pyramid of Pain** — Framework describing the relative value and difficulty of blocking different IOC types
- **Dwell Time** — How long an attacker remained undetected in an environment

---

## Required Resources

- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com

---

## Study Checklist

- [ ] Read Section 1 and be able to describe the SOC mission and tiered analyst model without notes
- [ ] Read Section 2 and practice applying the CIA Triad to attack scenarios
- [ ] Read Section 3 and understand what a SIEM does and does not do
- [ ] Read Section 4 and memorize the five-step triage process and the four alert classifications
- [ ] Read Section 5 and know all five IOC types and the Pyramid of Pain levels
- [ ] Read Section 6 and be able to define MTTD, MTTR, dwell time, and false positive rate
- [ ] Read Section 7 and understand the purpose of MITRE ATT&CK, Kill Chain, and the Diamond Model
- [ ] Review all eight CySA+ exam tips
- [ ] Review the glossary and self-test by covering definitions
- [ ] Complete the Module 01 Lab activity
- [ ] Complete the Module 01 Quiz
- [ ] Post your initial response to the Module 01 Discussion board by Wednesday at 11:59 PM
