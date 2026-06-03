# Reading Guide: Module 12 — Digital Forensics and Post-Incident Analysis

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Overview

This reading guide supports Module 12. Digital forensics and post-incident analysis represent the final phase of the incident response lifecycle. While containment and eradication stop the immediate harm, forensics and post-incident review produce the evidence, accountability, and improvement insights that justify your program's existence to regulators, executives, and courts. This guide provides structured reference material, frameworks, key definitions, and CISM exam tips aligned to Domain 4 competencies.

---

## Section 1 — Digital Forensics Fundamentals

### The DFRWS Forensic Process Model

The Digital Forensic Research Workshop established a widely adopted process model with six phases.

| Phase | Description | Key Deliverable |
|---|---|---|
| Identification | Recognize and document potential evidence sources | Evidence inventory |
| Preservation | Prevent alteration; image media; apply write blockers | Forensic image and hash log |
| Collection | Acquire evidence per documented procedures | Chain of custody form |
| Examination | Apply forensic techniques to extract relevant data | Examination notes |
| Analysis | Interpret extracted data to answer investigative questions | Findings report |
| Presentation | Communicate findings clearly and credibly | Forensic report |

### Forensic Readiness

Forensic readiness is the organizational state of being prepared to conduct digital investigations before an incident occurs. ISACA defines forensic readiness as maximizing an organization's ability to use digital evidence while minimizing the cost of an investigation.

Key forensic readiness requirements include the following.

- Logging enabled on all critical systems with sufficient retention (minimum 12 months recommended)
- Defined evidence custodian roles and responsibilities
- Documented evidence handling procedures in the incident response plan
- Legal hold process coordinated with legal counsel
- Investigator training and toolset availability
- Secure, tamper-evident evidence storage

### Evidence Types in Digital Investigations

| Evidence Type | Description | Volatility |
|---|---|---|
| RAM and Memory | Running processes, open connections, keys, credentials | Extremely volatile — lost on power-off |
| Network traffic | Packet captures, flow records, proxy logs | Volatile — lost if not actively captured |
| Operating system logs | System, security, application event logs | Moderate — may be overwritten |
| Application logs | Web server, database, authentication logs | Moderate |
| File system | Files, metadata, deleted file remnants, timestamps | Persistent but can be overwritten |
| Removable media | USB drives, external drives | Persistent |
| Cloud logs | Provider activity logs such as CloudTrail and Azure Monitor | Persistent but provider-controlled |

The **order of volatility** principle states that investigators should collect the most volatile evidence first. Memory must be captured before the system is powered down.

---

## Section 2 — Chain of Custody

### Definition

Chain of custody is the chronological documentation that records the seizure, custody, control, transfer, analysis, and disposition of evidence. It must be unbroken from first collection to final presentation.

### Required Documentation Elements

| Element | Details Required |
|---|---|
| Evidence ID | Unique alphanumeric identifier assigned at collection |
| Item description | Type, make, model, serial number, physical condition |
| Collector identity | Full name, role, badge or employee number |
| Collection date and time | ISO 8601 format recommended; include time zone |
| Collection location | Physical location or system hostname and IP |
| System state | Powered on or off, logged in or out, running processes if applicable |
| Hash values | MD5 and/or SHA-256 computed immediately at collection |
| Transfer record | Sender, receiver, date and time, method, purpose for every transfer |
| Storage record | Location, access controls, environmental conditions |
| Disposition | Final outcome — returned, destroyed, archived, or submitted to court |

### Hash Integrity Verification

Hashing provides a mathematical fingerprint of evidence. If the hash computed at collection matches the hash computed at analysis, the evidence has not been altered. Any change to even a single bit will produce a completely different hash value.

| Algorithm | Output Size | Current Status |
|---|---|---|
| MD5 | 128 bit | Acceptable for integrity checks; not for security applications |
| SHA-1 | 160 bit | Deprecated for security; still found in legacy systems |
| SHA-256 | 256 bit | Current standard; recommended for all forensic work |

### Legal Hold

A legal hold is a formal directive from legal counsel requiring the preservation of potentially relevant information when litigation is reasonably anticipated. Key points for CISM candidates are listed below.

- Legal holds suspend normal retention and deletion schedules
- Scope must be precisely defined covering custodians, data types, and date ranges
- Failure to comply with a legal hold can result in spoliation sanctions
- The CISO must coordinate with legal counsel and records management
- Legal holds apply to both on-premises and cloud-hosted data

---

## Section 3 — Forensic Tools Reference

### Disk Forensics Tools

| Tool | Type | Primary Use |
|---|---|---|
| EnCase (OpenText) | Commercial | Disk imaging, analysis, court-ready reporting |
| FTK — Forensic Toolkit | Commercial | Disk imaging, keyword indexing, email analysis |
| Autopsy and The Sleuth Kit | Open source | Disk analysis, timeline generation, artifact extraction |
| dd and dcfldd | Open source | Command-line disk imaging on Linux and Unix systems |
| FTK Imager (free) | Commercial free tier | Standalone imaging and hash verification |

### Memory Forensics Tools

| Tool | Type | Primary Use |
|---|---|---|
| Volatility Framework | Open source | Memory image analysis, process extraction, malware detection |
| Rekall | Open source | Advanced memory forensics; largely merged into Volatility |
| WinPmem | Open source | Windows memory acquisition |
| LiME | Open source | Linux memory acquisition as a kernel module |

### Network Forensics Tools

| Tool | Type | Primary Use |
|---|---|---|
| Wireshark | Open source | Packet capture analysis, session reconstruction |
| Zeek (formerly Bro) | Open source | Network monitoring and protocol analysis |
| NetworkMiner | Open source and commercial | Passive network sniffer and analyzer |
| Security Onion | Open source | Full network security monitoring distribution |
| Arkime (formerly Moloch) | Open source | Large-scale packet capture indexing |

### Log Analysis and SIEM Tools

| Tool | Type | Primary Use |
|---|---|---|
| Splunk | Commercial | Log aggregation, correlation, and investigation |
| IBM QRadar | Commercial | SIEM with behavioral analytics |
| Microsoft Sentinel | Cloud-native | Azure-integrated SIEM and SOAR |
| Elastic SIEM | Open source and commercial | Log search and threat hunting |
| Graylog | Open source and commercial | Centralized log management |

---

## Section 4 — After-Action Reports

### Purpose and Governance Context

The after-action report transforms incident experience into organizational learning and documented evidence of due care. From a governance perspective, after-action reports serve five purposes.

1. They document organizational response capability for regulators and auditors
2. They provide evidence that identified risks are being addressed
3. They create accountability for improvement recommendations
4. They inform risk register updates and control assessments
5. They support insurance and legal proceedings

### Standard After-Action Report Structure

| Section | Content | Audience |
|---|---|---|
| Executive Summary | Incident overview, business impact, status | Board, senior leadership |
| Incident Summary | Who, what, when, where, how | Security team, management |
| Detailed Timeline | Chronological event reconstruction with sources | Investigators, auditors |
| Response Assessment | What worked, what did not, metrics vs targets | Security team, operations |
| Root Cause Analysis | Fundamental causes with evidence | Security team, risk management |
| Findings and Gaps | Specific control and process deficiencies | CISO, risk committee |
| Recommendations | Prioritized actions with owners and due dates | Management, team leads |
| Appendices | Evidence inventory, tool logs, communications | Legal, auditors |

### AAR Timing Guidance

| Incident Severity | Initial Hot Wash | Comprehensive Review |
|---|---|---|
| Critical (P1) | Within 24–48 hours | Within 10 business days |
| High (P2) | Within 72 hours | Within 15 business days |
| Medium (P3) | Within 1 week | Within 30 days |
| Low (P4) | Not required | Within 60 days |

---

## Section 5 — Root Cause Analysis

### The Five Whys Technique

The Five Whys is an iterative interrogative technique developed at Toyota and widely adopted in information security root cause analysis. Starting from the problem statement, you ask "why" five or more times, with each answer forming the basis of the next question. The process continues until you reach a cause that has no further causal predecessor — the root cause.

Strengths include simplicity, speed, no special tools required, and encouragement of systemic thinking. Limitations include a tendency toward single-cause thinking, potential to miss contributing factors in complex incidents, and a requirement for a skilled facilitator to avoid premature stopping.

### Fishbone Diagram — Ishikawa Method

The fishbone diagram maps all contributing causes of a problem across defined categories. The problem is placed at the head of the fish. The major bones represent categories, and sub-bones represent specific contributing factors within each category.

Standard categories for information security root cause analysis include the following.

| Category | Examples |
|---|---|
| People | Insufficient training, role ambiguity, fatigue, human error |
| Process | Missing procedures, incomplete playbooks, approval bottlenecks |
| Technology | Unpatched systems, misconfigured controls, tool gaps |
| Environment | Physical security gaps, third-party dependencies, regulatory changes |
| Policy | Outdated policies, untracked exceptions, no enforcement mechanism |

### Fault Tree Analysis

Fault tree analysis is a top-down deductive technique that models how multiple contributing failures combine to produce an undesirable outcome. It uses Boolean logic gates to show which combinations of conditions must be present for the outcome to occur. Fault tree analysis is most useful when root cause analysis must address complex, multi-factor incidents involving simultaneous failures across detection, prevention, and response controls.

### Lessons Learned Tracking

Root cause findings have no value unless they are acted upon. Lessons learned must be entered into a formal tracking system with the following attributes.

- Unique identifier linked to the incident record
- Finding description with sufficient detail to be actionable
- Assigned owner who is an individual, not a team
- Priority level: critical, high, medium, or low
- Target completion date
- Current status
- Verification method describing how completion will be confirmed

---

## CISM Exam Tips — Module 12

The following points are frequently tested on the CISM examination.

- **Forensic readiness** is a proactive governance function, not a reactive one. The CISM candidate must understand it as a program-level capability that must exist before incidents occur.
- **Write blockers** are the primary control for evidence preservation during disk imaging. Their absence invalidates the forensic process.
- **Chain of custody** is the documentation that makes digital evidence legally admissible. A single undocumented transfer breaks the chain.
- **SHA-256** is the current recommended hashing algorithm for forensic integrity verification.
- **Order of volatility** means memory first, then network state, then disk. Collect the most volatile evidence before taking any action that could destroy it.
- **After-action reports** must include recommendations with owners and due dates. Findings without recommendations are incomplete from a governance standpoint.
- **Legal holds** must be triggered by legal counsel, not by the security team independently. The CISO's role is to implement and enforce the hold.
- The **Five Whys** technique is the most commonly referenced root cause analysis method in CISM study materials. Know how to apply it to a scenario.

---

## Key Definitions — Module 12 Glossary

| Term | Definition |
|---|---|
| Chain of custody | Documented record of evidence handling from collection to final disposition |
| Digital forensics | Scientific application of methods to identify, preserve, analyze, and present digital evidence |
| Evidence custodian | Individual formally responsible for maintaining and documenting evidence integrity |
| Forensic image | Bit-for-bit copy of storage media used in place of the original during analysis |
| Forensic readiness | Organizational capability to collect and preserve evidence before incidents occur |
| Hash value | Cryptographic fingerprint used to verify that evidence has not been altered |
| Legal hold | Legal counsel directive to preserve potentially relevant information for litigation |
| Order of volatility | Principle that the most transient evidence should be collected first |
| Root cause analysis | Technique for identifying the fundamental cause of a problem rather than its symptoms |
| Write blocker | Hardware or software device that prevents write operations on forensic evidence media |

---

## Study Checklist — Module 12

Review each item below before proceeding to the lab and quiz.

- [ ] I can name and describe the four core forensic principles: identification, preservation, analysis, and presentation
- [ ] I understand why write blockers are required and what happens without them
- [ ] I can list all required fields on a chain of custody form
- [ ] I know the difference between MD5, SHA-1, and SHA-256 and which is recommended for forensic work
- [ ] I understand what a legal hold is and who initiates it
- [ ] I can identify at least two tools in each forensic category: disk, memory, network, and log analysis
- [ ] I can describe the structure of a complete after-action report
- [ ] I can apply the Five Whys technique to a realistic incident scenario
- [ ] I understand the purpose and categories of a fishbone diagram
- [ ] I know what forensic readiness means and why it is a governance responsibility
- [ ] I understand the order of volatility and can apply it to evidence collection sequencing
