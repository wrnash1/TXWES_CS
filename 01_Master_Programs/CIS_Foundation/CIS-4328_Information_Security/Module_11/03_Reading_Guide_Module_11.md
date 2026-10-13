# Reading Guide: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports the Module 11 video lectures on incident response. The Security+ exam dedicates significant weight to Domain 4 (Operations and Incident Response), and NIST SP 800-61 is the primary reference framework. Complete all assigned readings before the quiz and lab.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Map incident response activities to the four NIST SP 800-61 phases
2. Identify the IR team roles and their responsibilities during an incident
3. Describe communication best practices for internal and external stakeholders
4. Apply the order of volatility to prioritize evidence collection
5. Explain chain of custody requirements and their legal significance
6. Explain the purpose and content of a post-incident lessons learned meeting and report
7. Define MTTD and MTTR and explain how they measure IR program maturity

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**NIST SP 800-61 Revision 2 — Computer Security Incident Handling Guide**

- Publisher: National Institute of Standards and Technology
- Access: [https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
- Read: Chapter 2 (Organizing a Computer Security Incident Response Capability), Chapter 3 (Handling an Incident), and Chapter 4 (Coordination and Information Sharing)
- Focus areas: IR lifecycle phases, incident categorization, team structure, evidence handling, communication

Estimated reading time: 60–75 minutes for assigned chapters.

### Supplemental Reading

**SANS Institute — Incident Handler's Handbook**

- Access: [https://www.sans.org/white-papers/33901/](https://www.sans.org/white-papers/33901/)
- Read: Full document (approximately 40 minutes)
- Focus areas: practical IR procedure, evidence handling, communication during incidents

**CISA — Incident Response Plan Basics**

- Access: [https://www.cisa.gov/topics/cybersecurity-best-practices/organizations-and-cyber-safety/incident-response-plans](https://www.cisa.gov/topics/cybersecurity-best-practices/organizations-and-cyber-safety/incident-response-plans)
- Read: Full page
- Focus areas: IR plan components, federal guidance

---

## Key Terms and Definitions

**Incident Response (IR)** — The organized approach an organization takes to preparing for, detecting, containing, and recovering from security incidents.

**CSIRT (Computer Security Incident Response Team)** — The designated team responsible for executing incident response procedures; also called an IRT or CERT.

**NIST SP 800-61** — NIST Special Publication 800-61, "Computer Security Incident Handling Guide" — the primary US government IR framework, widely adopted in private sector organizations.

**Preparation Phase** — The IR lifecycle phase focused on building response capabilities before incidents occur: developing the IR plan, forming the team, deploying detection tools, conducting training.

**Detection and Analysis Phase** — The IR lifecycle phase focused on identifying that an incident has occurred, validating the alert, and determining scope and severity.

**Containment Phase** — The IR lifecycle phase focused on stopping the incident from spreading; includes short-term containment (immediate isolation) and long-term containment (durable controls).

**Eradication Phase** — The IR lifecycle phase focused on removing the attacker's presence, malware, and persistence mechanisms from the environment.

**Recovery Phase** — The IR lifecycle phase focused on restoring systems to normal operation, rebuilding from clean backups, and validating system integrity.

**Post-Incident Activity (Lessons Learned)** — The IR lifecycle phase focused on analyzing what happened, what worked, what did not, and implementing improvements.

**Incident Commander** — The individual who leads the incident response, coordinates the team, makes tactical decisions, and briefs leadership.

**Runbook / Playbook** — A documented, step-by-step procedure for responding to a specific incident type (e.g., ransomware playbook, phishing playbook).

**Order of Volatility** — The sequence in which evidence should be collected, from most volatile (will be lost soonest) to least volatile; RAM before disk, network state before file system.

**Volatile Evidence** — Digital evidence that exists only in memory or transient system state and will be lost when the system is powered off: running processes, network connections, RAM contents.

**Chain of Custody** — Documentation that records who collected, handled, transferred, and accessed evidence, providing a traceable and verifiable record of evidence integrity.

**Forensic Image** — A bit-for-bit copy of storage media that preserves all data including deleted files, unallocated space, and file system metadata; used for analysis in place of the original.

**MTTD (Mean Time to Detect)** — The average time between initial compromise and detection of the incident by the organization.

**MTTR (Mean Time to Respond/Recover)** — The average time from detection to full recovery and restoration of normal operations.

**Tabletop Exercise** — A discussion-based exercise in which the IR team walks through a simulated incident scenario to test the IR plan and identify gaps without deploying technical resources.

**Indicators of Compromise (IOCs)** — Forensic artifacts that indicate a system may have been breached: malicious IP addresses, file hashes, registry keys, domain names used by attackers.

**ISAC (Information Sharing and Analysis Center)** — Sector-specific organizations that facilitate sharing of threat intelligence among members; examples: FS-ISAC (financial sector), H-ISAC (healthcare), MS-ISAC (multi-state for government).

**TTPs (Tactics, Techniques, and Procedures)** — The behavior of a threat actor: the high-level goals they pursue (tactics), the technical methods they use (techniques), and the specific implementations of those techniques (procedures). Documented in the MITRE ATT&CK framework.

---

## Concept Deep Dives

### NIST IR Lifecycle — Activities by Phase

Study this table to map specific actions to the correct phase — a common exam question format.

| Activity | Phase |
|---|---|
| Writing the incident response plan | Preparation |
| Conducting a tabletop exercise | Preparation |
| Deploying a SIEM | Preparation |
| Triaging an IDS alert | Detection and Analysis |
| Identifying affected systems | Detection and Analysis |
| Prioritizing incident severity | Detection and Analysis |
| Disconnecting an infected host from the network | Containment |
| Blocking a malicious IP at the firewall | Containment |
| Removing malware from a compromised endpoint | Eradication |
| Patching the vulnerability that was exploited | Eradication |
| Restoring data from backup | Recovery |
| Rebuilding a compromised server | Recovery |
| Returning a system to production | Recovery |
| Conducting a lessons learned meeting | Post-Incident Activity |
| Updating the incident response playbook | Post-Incident Activity |
| Writing the incident report | Post-Incident Activity |

### Order of Volatility — Memory Aid

Most volatile → Least volatile:

**"CPU Runs Swiftly — Networks Fly, Disks Remain"**

- CPU registers and cache
- RAM (system memory)
- Swap/paging file
- Network connections and ARP cache
- File system (temp files, active logs)
- Disk storage (persistent data)
- Remote logging
- Backup media

Collect in this order. Never power off before collecting RAM if you can avoid it.

### Chain of Custody Elements Checklist

Every item in an evidence inventory must have:

- Unique evidence identifier / label
- Description (type, model, serial number if applicable)
- Collection date, time, and location
- Collector name and signature
- MD5 and SHA-256 hashes (for digital evidence)
- Tamper-evident packaging description (for physical evidence)
- Transfer log (each person who received the evidence)
- Current storage location

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **4.2** — Given a scenario, apply the appropriate incident response procedure (NIST phases, IR plan components)
- **4.3** — Given an incident, utilize appropriate data sources to support an investigation (evidence types, order of volatility)
- **4.4** — Given an incident, apply mitigation techniques or controls to secure an environment (containment and eradication actions)

### High-Probability Exam Topics from This Module

- Correctly sequencing NIST IR phases when given a scenario activity
- Identifying the correct phase for "blocking a malicious IP" (containment), "conducting tabletop exercises" (preparation), and "holding a lessons learned meeting" (post-incident)
- Ordering evidence collection by volatility (RAM before disk, network before file system)
- Identifying what chain of custody establishes (traceability, integrity, admissibility)
- Distinguishing MTTD from MTTR
- Identifying the purpose of out-of-band communication during incidents

---

## Review Questions (Self-Check — Not Graded)

1. An analyst detects a running malware process on a Windows endpoint that is actively exfiltrating data. The analyst must collect evidence but also needs to stop the exfiltration immediately. List the steps you would take in order, referencing the order of volatility and the tension between evidence preservation and containment.

2. An organization's IR plan has not been updated in three years. A ransomware incident occurs and responders find that the playbook references systems that no longer exist and communication procedures that use a messaging platform the company discontinued. What specific preparation activities would have prevented this operational failure?

3. After a breach, the organization's legal team wants to pursue criminal charges against the identified attacker. The investigating detective states that the chain of custody documentation is insufficient. What specific records would be needed, and at what point in the IR process should they have been established?

4. A company experiences an incident. Detection occurs 180 days after the initial compromise. What MTTD metric would you report, and what does this number tell you about the organization's detection capabilities?

5. The lessons learned meeting reveals that during the incident, multiple executives called individual analysts directly for status updates, disrupting the response. What specific communication control in the IR plan would prevent this in the future?

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 11*
