# Reading Guide: Module 11 — Incident Detection and Response Procedures

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Overview

This reading guide provides comprehensive reference material for Module 11. Where Module 10 established the planning foundation, Module 11 covers the execution of incident response across the detection, containment, eradication, recovery, and lessons-learned phases. Understanding these procedures at a management level — not just as a technical operator but as a CISM-aligned security manager — is essential for both the certification exam and professional practice.

Work through each section in order. Complete the study checklist before attempting the quiz.

---

## Section 1 — Incident Detection

### 1.1 Detection Technologies

A mature incident detection capability requires a layered technology stack. No single tool provides complete visibility. The following technologies form the core detection architecture in most enterprise environments:

| Technology | Abbreviation | Primary Function | Key Strength | Key Gap |
|---|---|---|---|---|
| Security Information and Event Management | SIEM | Log aggregation, correlation, alerting | Cross-source correlation | Quality depends on log coverage |
| Endpoint Detection and Response | EDR | Endpoint process, file, and network monitoring | Deep endpoint visibility | Limited network-layer view |
| Network Detection and Response | NDR | Network traffic analysis and anomaly detection | Lateral movement detection | Cannot see encrypted payloads |
| Intrusion Detection System | IDS | Signature and anomaly-based traffic inspection | Known threat detection | High false positive rate |
| User and Entity Behavior Analytics | UEBA | Baseline behavior modeling and anomaly detection | Insider threat detection | Requires extended baseline period |
| Deception Technology (honeypots) | — | Lure and detect unauthorized access | High-fidelity alerts (almost no false positives) | Limited coverage |

### 1.2 Indicators of Compromise

An Indicator of Compromise (IoC) is forensic evidence that a system or network has been or may be compromised. IoCs form the foundation of detection rule logic.

| IoC Type | Examples | Detection Method |
|---|---|---|
| File hash | MD5/SHA-256 of known malware | EDR, AV scanning |
| IP address | Known C2 server IP | Firewall, DNS, SIEM |
| Domain name | Malicious domain used for C2 | DNS logs, proxy logs |
| URL | Phishing URL or malware download link | Web proxy logs |
| Registry key | Persistence mechanism at Run key location | EDR, HIDS |
| Behavioral | PowerShell spawning from Word.exe | EDR behavioral rules |
| Network pattern | Periodic beaconing to external IP | NDR, SIEM |

### 1.3 Indicators of Attack vs. Indicators of Compromise

An important distinction in modern threat detection:

- **Indicator of Compromise (IoC)**: Evidence that a compromise has already occurred. Reactive — detected after the fact.

- **Indicator of Attack (IoA)**: Evidence that an attack is in progress. Proactive — focused on attacker behavior patterns rather than known artifacts.

IoA-based detection is more valuable against sophisticated adversaries who use legitimate tools (living off the land) to avoid leaving IoC fingerprints. EDR platforms have shifted toward IoA-based behavioral detection to address this.

### 1.4 Detection Gaps and Blind Spots

Every detection architecture has gaps. Common blind spots:

- **Encrypted traffic**: TLS encryption hides payload content from network-based IDS/NDR. Requires SSL inspection or endpoint-based telemetry.

- **Insider threats with legitimate access**: Authorized users with excessive permissions may not trigger rule-based detection. Requires UEBA behavioral analytics.

- **Cloud and SaaS environments**: Many organizations have limited log coverage from cloud platforms and SaaS applications.

- **IoT and operational technology (OT)**: These devices often cannot support traditional agents and generate limited security telemetry.

---

## Section 2 — Triage and Analysis

### 2.1 The Triage Process

Triage is the structured process of determining whether an alert represents a genuine security threat and, if so, classifying its severity and scope. Effective triage is the difference between an overworked SOC drowning in alerts and a functional security operations capability.

The four triage questions:

1. Is this genuine? (True positive vs. false positive determination)

2. What is the scope? (Single endpoint? Multiple systems? Network segment?)

3. What is the severity? (What data and functions are at risk? What is the regulatory exposure?)

4. What is the urgency? (Active in-progress attack vs. historical indicator?)

### 2.2 Triage Steps

| Step | Activity | Tool / Method |
|---|---|---|
| Alert validation | Review raw log data supporting the alert | SIEM log drill-down |
| Contextual enrichment | Gather asset classification, user profile, threat intel | CMDB, threat intel feeds |
| False positive assessment | Determine if alert matches known-good baseline | Historical data, suppression rules |
| Severity classification | Apply IRP severity criteria | IRP classification framework |
| Scope mapping | Identify all affected systems and users | EDR pivot, network logs |
| Escalation decision | Apply escalation criteria from IRP | IRP escalation criteria |

### 2.3 Dwell Time

Dwell time is the period between when an attacker gains initial access and when the organization detects the intrusion. It is a critical security metric that measures detection effectiveness.

- Industry average dwell time: approximately 200 days (varies by source and year).

- Organizations with mature detection programs: 30–60 days average.

- Organizations with UEBA and behavioral detection: can reduce to single-digit days.

Reducing dwell time is the primary operational objective of a detection program. Every day of undetected attacker presence increases the scope of damage and data exposure.

### 2.4 Forensic Evidence Preservation During Analysis

When an incident is identified, forensic evidence must be preserved before any containment or remediation actions are taken, whenever time permits.

**Volatile evidence** — Evidence that exists only in memory or active processes and will be lost on system restart or isolation:

- RAM contents (running processes, encryption keys, network connections)

- Active network connections

- Running processes and their command-line arguments

- Logged-in user sessions

**Persistent evidence** — Evidence stored in a more durable form:

- File system artifacts

- Registry contents

- Log files

- Browser history and cached data

Order of volatility (collect most volatile first): network state, RAM, disk.

---

## Section 3 — Containment

### 3.1 Containment Strategy Selection

NIST SP 800-61 defines two containment strategies that are applied in sequence or in combination depending on the incident type:

**Short-term containment**: Immediate actions to stop active harm. Prioritizes speed over investigation completeness.

- Network isolation of affected endpoints

- Account lockout or deactivation

- Firewall rule blocking malicious traffic

- DNS blocking of C2 domain

**Long-term containment**: Sustained controls maintained during investigation. Allows investigation to continue without allowing the attacker to operate freely.

- Temporary access controls

- Enhanced monitoring on affected network segments

- Parallel clean system deployment while affected systems remain isolated

### 3.2 Containment Decision Matrix

| Incident Type | Short-Term Action | Long-Term Action | Evidence Priority |
|---|---|---|---|
| Ransomware | Immediate network isolation | Enhanced monitoring for re-entry | Low — speed dominates |
| APT/espionage | Covert monitoring (watch before acting) | Gradual containment to avoid tipping off actor | High — understand full scope |
| Data breach | Block exfiltration, isolate affected system | Credential rotation, enhanced DLP | High — understand scope of exposure |
| Insider threat | Account lockout (coordinate with HR/Legal first) | Access monitoring | Critical — chain of custody |
| DDoS | Upstream scrubbing, rate limiting | Traffic pattern analysis | Low — service restoration priority |
| Phishing | Block sender, isolate clicked endpoints | Email quarantine, user notification | Medium |

### 3.3 Evidence vs. Speed Trade-off

The decision to isolate immediately versus collect evidence before isolating is one of the most consequential tactical decisions in incident response.

**Isolate immediately** when:

- Ransomware is actively encrypting files.

- Confirmed data exfiltration is in progress.

- Critical systems or safety functions are at risk.

**Collect evidence first** when:

- The attack is not actively causing damage.

- Law enforcement involvement is anticipated.

- Understanding the full scope requires observing attacker movement.

- Advanced persistent threat (APT) activity is suspected and the organization needs to understand objectives.

The IRP should pre-authorize specific approaches for common incident types so this decision does not need to be made under pressure.

---

## Section 4 — Eradication

### 4.1 Eradication Activities

Eradication is the process of completely removing the threat actor's presence from the environment. Containment stops the active harm; eradication eliminates the threat so that recovery can proceed safely.

Eradication activities:

**Malware removal**: Use EDR and forensic tools to identify and remove all malicious files, scripts, and executables. Verify through multiple methods — hash matching, behavioral analysis, manual inspection.

**Persistence mechanism elimination**: Attackers establish persistence through multiple mechanisms. Common persistence locations:

- Windows: Registry Run keys, scheduled tasks, services, WMI subscriptions, startup folders, BITS jobs

- Linux: Cron jobs, init scripts, systemd services, bash profile modifications

- Web applications: Web shells, backdoored plugins

**Credential rotation**: All credentials that may have been exposed — user passwords, service account passwords, API keys, certificates — must be rotated. Prioritize privileged credentials.

**Vulnerability remediation**: The attack vector that allowed initial access must be closed before recovery begins. This may include applying a patch, correcting a misconfiguration, updating access controls, or deploying a compensating control.

### 4.2 Eradication Validation

Eradication is not complete until it is validated. Validation activities:

- Full EDR scan of all systems in the affected environment.

- Review of all scheduled tasks, services, and startup items across affected systems.

- Network traffic review to confirm no communication to previously identified C2 infrastructure.

- Log review for re-entry indicators.

- Threat intelligence check: has the attacker TTP (tactics, techniques, procedures) been seen elsewhere in the environment?

### 4.3 Eradication Failure

A common and dangerous failure mode is incomplete eradication — removing the visible malware while missing secondary persistence mechanisms. An attacker who regains access after a seemingly complete recovery has demonstrated that eradication was not thorough.

Signs of incomplete eradication:

- Recurrence of the same IoC within days of recovery.

- New alerts matching the same attacker profile shortly after recovery.

- Attacker-related activity from a previously uncompromised system.

---

## Section 5 — Recovery

### 5.1 Recovery Principles

Recovery restores affected systems to normal operation. The governing principle of recovery is **restore from known-clean state**. A system restored from a backup that predates the compromise — or from a clean image — is presumed safe. A system simply "cleaned" of malware without a full rebuild carries residual risk.

### 5.2 Recovery Steps

| Step | Activity | Dependency |
|---|---|---|
| 1 | Identify recovery point — last known-clean backup or image | Eradication complete |
| 2 | Validate backup integrity | Backup not taken during compromise window |
| 3 | Rebuild or restore system | Clean backup confirmed |
| 4 | Apply current patches and configurations | System rebuilt |
| 5 | Deploy enhanced monitoring | System restored |
| 6 | Validate business function | Operations team sign-off |
| 7 | Return system to production | Monitoring confirmed active |

### 5.3 Recovery Time Coordination

Recovery must be coordinated with the Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP):

- System restoration sequence follows the DRP priority tier list.

- Business unit owners authorize return to production for their systems.

- Enhanced monitoring period (typically 2–4 weeks) before declaring full recovery.

- Post-recovery monitoring for signs of attacker re-entry.

---

## Section 6 — Post-Incident Activity

### 6.1 Lessons-Learned Review

The lessons-learned review is a structured meeting held within two weeks of incident closure. It is distinct from the post-incident forensic investigation — it focuses on process improvement, not evidence gathering.

Required participants: IR Manager, Technical Lead, Communications Lead, Legal, and any team member involved in a significant response decision.

Agenda structure:

1. Timeline reconstruction — what happened, when, and who knew what.

2. What worked well — preserve and reinforce effective practices.

3. What could be improved — where were the gaps, delays, and failures?

4. Root cause analysis — technical and process root causes.

5. Action items — specific, assigned, time-bound improvement actions.

### 6.2 Root Cause Analysis Methods

| Method | Description | Use Case |
|---|---|---|
| Five Whys | Iterative "why?" questions drilling to fundamental cause | Simple, single-cause incidents |
| Fishbone (Ishikawa) | Visual mapping of contributing causes by category | Complex, multi-factor incidents |
| Timeline analysis | Reconstruction of event sequence to identify decision failures | Communication and escalation failures |
| Fault tree analysis | Logical diagram tracing failure paths from outcome to causes | Technical control failures |

### 6.3 IRP Update Requirements

Every significant incident must produce an IRP update. Required review areas:

- Were all roles staffed and available? Update contacts and backup coverage if not.

- Did the severity classification framework work? Revise criteria if incidents were consistently under- or over-classified.

- Did the escalation criteria trigger at the right time? Revise triggers if escalation was late or premature.

- Were the procedures accurate? Update any steps that did not reflect what the team actually did.

- Were there notification timeline failures? Strengthen the external notification tracking process.

### 6.4 Incident Documentation Requirements

| Document | Content | Retention |
|---|---|---|
| Incident ticket | Summary, timeline, severity, resolution | Per policy, typically 3–7 years |
| Evidence log | Chain of custody for all collected evidence | Per legal hold or 7 years |
| Decision log | Significant decisions with rationale and decision-maker | Per legal hold |
| Notification log | All external notifications with timestamps | Per regulatory requirement |
| Lessons-learned report | Findings and action items | Indefinite |

---

## Section 7 — CISM Exam Alignment

### 7.1 Domain 4 Objectives Covered

This module addresses CISM Domain 4 — Incident Management objectives:

- Execute incident detection, triage, and classification procedures.

- Apply containment, eradication, and recovery strategies aligned to NIST SP 800-61.

- Conduct post-incident reviews to identify improvements.

- Maintain incident documentation for governance, legal, and regulatory purposes.

### 7.2 High-Probability Exam Topics

- **Short-term vs. long-term containment**: Know the distinction and when each applies.

- **Evidence vs. speed trade-off**: Know when to prioritize forensic preservation and when to prioritize immediate containment.

- **Eradication completeness**: Understand why credential rotation and vulnerability remediation are required eradication steps.

- **Known-clean backup**: Understand why recovery must restore from a state that predates the compromise.

- **Lessons-learned structure**: Know the purpose, participants, and agenda of the post-incident review.

- **IRP update authorization**: Know that IRP changes must go through the same authorization process as the original plan.

### 7.3 Sample CISM Exam Question

**Question**: An organization discovers active ransomware on three servers. The IR team has contained the affected systems. Which of the following should occur BEFORE system recovery begins?

A. Hold the lessons-learned meeting to document the incident.
B. Validate that all malware, persistence mechanisms, and the initial vulnerability have been fully eradicated.
C. Restore all affected systems from the most recent backup regardless of backup date.
D. Notify all employees that the incident has been resolved.

**Correct Answer: B** — Eradication must be complete and validated before recovery begins. Recovering before eradication is complete risks re-infection from residual malware or persistence mechanisms. Option A is post-recovery. Option C risks restoring from a compromised backup. Option D is premature and violates need-to-know principles.

---

## Study Checklist

Before attempting the Module 11 quiz, verify:

- [ ] I can name five detection technology types and describe the primary function of each.

- [ ] I can define IoC and IoA and explain the difference.

- [ ] I can describe the four triage questions and explain why each matters.

- [ ] I can explain what dwell time is and why reducing it is important.

- [ ] I can describe the order of volatility for forensic evidence collection.

- [ ] I can distinguish short-term from long-term containment with examples.

- [ ] I can describe the evidence vs. speed trade-off and when each priority applies.

- [ ] I can list four eradication activities required before recovery.

- [ ] I can explain why recovery must use a known-clean backup.

- [ ] I can describe the structure of a lessons-learned review.

- [ ] I can explain what IRP update authorization requires.

- [ ] I can identify four types of incident documentation and their purpose.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| EDR | Endpoint Detection and Response — agent-based endpoint monitoring and threat detection platform |
| NDR | Network Detection and Response — network traffic analysis for anomaly and threat detection |
| IoC | Indicator of Compromise — forensic evidence that a system has been compromised |
| IoA | Indicator of Attack — behavioral evidence that an attack is in progress |
| Dwell time | Time between attacker initial access and detection |
| Short-term containment | Immediate disruptive action to stop active harm |
| Long-term containment | Sustained controls maintained during investigation |
| Eradication | Complete removal of attacker presence including malware, persistence, and entry vector |
| Known-clean backup | Backup taken before the attacker established presence in the environment |
| Order of volatility | Sequence for collecting forensic evidence from most to least perishable |
| Lessons-learned review | Post-incident structured meeting to identify process improvements |
| Chain of custody | Documentation tracking evidence handling from collection through disposition |

---

## Recommended References

- NIST SP 800-61 Rev. 2, Computer Security Incident Handling Guide — Chapters 3 and 4

- ISACA CISM Review Manual, Domain 4 — Incident Management

- SANS Incident Handler's Handbook

- MITRE ATT&CK Framework — Techniques reference for detection and eradication

- CIS Controls v8 — Controls 13 (Network Monitoring), 17 (Incident Response Management)

## 9. Supplemental Resources

**1. MITRE ATT&CK Framework — Enterprise Techniques**
https://attack.mitre.org/techniques/enterprise/
The authoritative reference for attacker tactics, techniques, and procedures (TTPs). Use this resource to understand the detection opportunities at each phase of an attack — from initial access through persistence, lateral movement, and exfiltration. Directly applicable to building SIEM detection rules and eradication checklists.

**2. CIS Controls v8 — Implementation Guidance**
https://www.cisecurity.org/controls/v8
The Center for Internet Security Controls v8 provides prioritized security actions organized into Implementation Groups. Controls 13 (Network Monitoring and Defense) and 17 (Incident Response Management) directly align with Module 11 content on detection architecture and the incident response lifecycle.

**3. CISA Known Exploited Vulnerabilities Catalog**
https://www.cisa.gov/known-exploited-vulnerabilities-catalog
CISA's continuously updated catalog of vulnerabilities confirmed to be actively exploited in the wild. Critical resource for eradication planning — when identifying the attack vector used for initial access, this catalog helps confirm whether the vulnerability has been weaponized and prioritizes remediation urgency.
