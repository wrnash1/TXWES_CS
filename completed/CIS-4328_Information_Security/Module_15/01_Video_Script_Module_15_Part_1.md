# Video Script: Module 15 — Security Operations (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00–0:45]

Welcome back to CIS-4328 Information Security. I'm Professor Nash, and this is Module 15, Part 1.

We have now covered threats, cryptography, network architecture, identity management, and governance. This module pulls the operational layer together. Security Operations is the largest single domain on the Security+ SY0-701 exam — 28% of your score — and it is the domain most directly tied to what practitioners actually do every day.

In Part 1 today we cover the Security Operations Center, SIEM and SOAR platforms, vulnerability scanning with Nessus, and patch management. In Part 2 we shift to configuration management baselines, change control, and security metrics.

Let's get started.

---

### [SECTION 1: The Security Operations Center — 0:45–3:30]

A Security Operations Center, or SOC, is the team and facility responsible for monitoring, detecting, analyzing, and responding to cybersecurity incidents on a continuous basis. The SOC is the nerve center of operational security.

**SOC staffing models** vary by organization size and budget:

- **In-house SOC** — the organization employs its own analysts 24/7. Offers maximum control and context about the organization's specific environment. Expensive to operate.
- **Managed Security Service Provider (MSSP)** — a third-party organization operates the SOC. Common for mid-size organizations that cannot justify full-time SOC staff.
- **Hybrid SOC** — in-house team handles business hours and escalations; MSSP handles overnight and weekends. Balances cost and control.

**SOC analyst tiers** define roles and responsibilities:

**Tier 1 — Alert Triage:** Reviews incoming alerts from the SIEM, determines whether an alert is a true positive or false positive, and escalates genuine incidents. Tier 1 analysts handle high volume, routine work.

**Tier 2 — Incident Investigation:** Conducts deeper analysis of confirmed incidents. Examines logs, network traffic, and endpoint data to determine scope and impact. Performs initial containment actions.

**Tier 3 — Threat Hunting and Response:** Proactively searches for threats that have evaded automated detection. Leads complex incident investigations, performs forensic analysis, and develops new detection rules.

**SOC Manager** oversees the team, manages relationships with stakeholders, and ensures SLAs are met.

**Key SOC metrics** you should know for the exam:

- **Mean Time to Detect (MTTD)** — average time between an incident occurring and the SOC identifying it. Lower is better.
- **Mean Time to Respond (MTTR)** — average time between detection and successful containment or remediation. Lower is better.
- **False Positive Rate** — percentage of alerts that are not real incidents. High false positive rates burn analyst time and lead to alert fatigue.
- **Alert fatigue** is a real operational risk — when analysts are overwhelmed with false positives, real threats get missed.

---

### [SECTION 2: SIEM — Security Information and Event Management — 3:30–7:00]

A SIEM is the central technology platform of most SOC operations. It collects, aggregates, correlates, and analyzes security log data from across the enterprise in real time.

**Core SIEM functions:**

**Log aggregation** — the SIEM collects logs from firewalls, servers, endpoints, applications, identity systems, and network devices. All those logs flow into a central repository. Without centralized logging, you have no unified view of what is happening.

**Normalization** — raw log formats differ wildly between vendors and systems. The SIEM normalizes logs into a common schema so they can be compared and correlated. Windows Event Logs, Cisco ASA syslog, and Linux auth.log all look different — normalization makes them comparable.

**Correlation** — the most powerful SIEM function. Correlation rules link related events across multiple systems to identify patterns that individually look benign but together indicate an attack. Classic example: one failed login is noise; 500 failed logins across 50 accounts in 60 seconds is a credential stuffing attack.

**Alerting** — when correlation rules match, the SIEM generates an alert for analyst review.

**Dashboard and reporting** — SIEMs provide real-time dashboards for SOC analysts and compliance reports for auditors.

**Retention** — SIEMs store historical log data, which is essential for forensic investigation of past incidents and regulatory compliance.

**Common SIEM products** you may encounter in the field:

- **Splunk** — market leader, extremely powerful search and analytics engine. Enterprise-grade, expensive.
- **Microsoft Sentinel** — cloud-native SIEM on Azure. Tight integration with Microsoft 365 and Azure services.
- **IBM QRadar** — widely deployed in large enterprises and government environments.
- **Elastic SIEM** — open-source foundation with commercial add-ons; popular in organizations with strong technical teams.

**For the Security+ exam:** Know that SIEM performs log aggregation, normalization, and correlation. Know the difference between SIEM and SOAR, which we cover next.

---

### [SECTION 3: SOAR — Security Orchestration, Automation, and Response — 7:00–9:30]

SOAR extends the SIEM by adding automation and orchestration. Where a SIEM detects and alerts, a SOAR takes action.

**SOAR capabilities:**

**Orchestration** — SOAR integrates with all the tools in the security stack: firewalls, endpoint detection platforms, ticketing systems, threat intelligence feeds, email gateways, identity platforms. It acts as the connective tissue between tools that otherwise operate in silos.

**Automation** — SOAR executes playbooks automatically in response to specific alert types. A playbook is a predefined sequence of response actions. Example: when a SIEM alert fires for a suspected phishing email, the SOAR playbook automatically extracts the email, queries VirusTotal for the URL, checks the sender against threat intel, quarantines the email, and opens a ticket — all without human intervention.

**Case management** — SOAR provides an incident case management workflow so analysts can track investigation progress, document findings, and collaborate.

**The key distinction for the exam:**

- **SIEM** = detect and alert (passive visibility)
- **SOAR** = respond and automate (active response)

In modern SOCs, SIEM and SOAR are often integrated in the same platform (Splunk SOAR, Microsoft Sentinel with Logic Apps). But the exam tests them as distinct concepts, so know the difference.

**Benefits of SOAR:**

- Reduces analyst workload by automating repetitive tasks
- Enables faster response — seconds instead of minutes
- Ensures consistent, documented response to every incident
- Reduces mean time to respond

---

### [SECTION 4: Vulnerability Scanning — Nessus — 9:30–12:30]

Vulnerability scanning is the process of systematically identifying known vulnerabilities in systems, applications, and network devices. Unlike penetration testing, vulnerability scanning does not exploit vulnerabilities — it identifies and reports them.

**How vulnerability scanners work:**

1. The scanner discovers hosts on the network (via ping sweep or network range specification)
2. It probes each host for open ports and running services (similar to Nmap)
3. It queries a vulnerability database and tests each discovered service for known vulnerabilities using check plugins
4. It generates a report ranking findings by severity

**Nessus** is the most widely deployed commercial vulnerability scanner in the world, developed by Tenable. It is also heavily tested on the Security+ exam.

**Nessus key concepts:**

**Plugins** — each vulnerability check in Nessus is a plugin. Nessus has over 170,000 plugins covering operating systems, applications, network devices, and compliance benchmarks. Plugins are updated continuously as new vulnerabilities are discovered.

**Scan policies** — define which checks to run, which credentials to use, and performance settings. You create a policy, apply it to a scan, and run it against a target range.

**Credentialed vs. uncredentialed scanning:**

- **Uncredentialed (unauthenticated) scan** — scanner connects from outside, like an attacker would. Identifies network-accessible vulnerabilities. Limited visibility into local system state.
- **Credentialed (authenticated) scan** — scanner logs into each system with credentials. Sees installed software, patch levels, configuration settings, registry keys. Far more thorough. Produces fewer false negatives.

Security+ exam tip: Credentialed scans provide more accurate and complete results. Uncredentialed scans represent what an external attacker could see.

**Severity ratings in Nessus:** Nessus uses the Common Vulnerability Scoring System (CVSS) to rate findings:

- Critical (9.0–10.0)
- High (7.0–8.9)
- Medium (4.0–6.9)
- Low (0.1–3.9)
- Info (0.0) — informational findings, not vulnerabilities

**Scan frequency:** Best practice is to scan continuously or at least weekly. PCI-DSS requires quarterly external scans by an Approved Scanning Vendor (ASV) and after any significant network change.

**False positives** are a reality in vulnerability scanning. Analysts must validate scanner findings — especially for critical and high findings — before escalating to remediation teams.

---

### [CLOSING — 12:30–15:00]

Let's recap Part 1:

- The SOC operates in tiers; Tier 1 triages alerts, Tier 2 investigates, Tier 3 hunts. Key metrics are MTTD and MTTR.
- SIEM aggregates, normalizes, and correlates logs from across the enterprise to generate actionable alerts.
- SOAR extends SIEM with automation and orchestration; playbooks enable automated response without human intervention.
- Nessus performs vulnerability scanning using plugins; credentialed scans are more thorough; findings are rated by CVSS severity.

In Part 2 we will cover patch management, configuration baselines, change control procedures, and security metrics. These topics complete the Security Operations domain picture.

See you in Part 2.

---

*End of Part 1 Script*
