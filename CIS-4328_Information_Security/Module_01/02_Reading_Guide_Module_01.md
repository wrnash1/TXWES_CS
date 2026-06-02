# Reading Guide — Module 01: Threats, Attacks, and Vulnerabilities

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 | Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

---

## Introduction

Welcome to Module 01 — Threats, Attacks, and Vulnerabilities. This reading guide is your primary study document for the module. It expands on the video lectures with detailed definitions, comparison tables, and exam-focused analysis. Complete this guide before attempting the quiz or lab.

Module 01 establishes the vocabulary and reasoning framework for the entire course. The SY0-701 exam dedicates 22 percent of its weight to Domain 2, making this material among the highest-yield content you will study.

---

## 1. Core Concepts and Definitions

### The CIA Triad

The CIA Triad represents the three foundational objectives of information security. Every security control maps back to one or more of these properties.

**Confidentiality** ensures that information is accessible only to those authorized to access it. Violations of confidentiality occur when unauthorized parties read, copy, or exfiltrate data. Technical controls for confidentiality include symmetric encryption (AES), asymmetric encryption (RSA), and access control lists. Administrative controls include classification policies and need-to-know enforcement.

**Integrity** ensures that data is accurate, complete, and has not been altered without authorization. Violations of integrity occur when an attacker modifies data, an error corrupts a file, or a system state is changed without proper authorization. Technical controls for integrity include cryptographic hashing (SHA-256, SHA-3), digital signatures, and file integrity monitoring systems. Administrative controls include change management procedures and separation of duties.

**Availability** ensures that systems and data are accessible to authorized users when needed. Violations of availability include denial-of-service attacks, hardware failure, ransomware that encrypts and locks data, and natural disasters that destroy infrastructure. Technical controls for availability include redundant systems, load balancing, failover clustering, and backup and recovery procedures. Administrative controls include business continuity plans and disaster recovery plans.

**Non-repudiation** extends the triad as a fourth property. Non-repudiation ensures that a party cannot deny having performed an action. It is enforced through digital signatures — a user signs a transaction with their private key, and the signature can be verified by anyone with the corresponding public key, proving the signer's identity. Non-repudiation is essential in legal, financial, and contractual contexts.

---

## 2. Security Controls — Category and Function Matrix

### Control Categories

| Category | Also Called | Description | Examples |
|---|---|---|---|
| Physical | Physical | Tangible, touchable barriers and mechanisms | Fences, locks, mantraps, guards, cameras |
| Technical | Logical | Software, hardware, or firmware enforcement | Firewalls, IDS, encryption, MFA, ACLs |
| Administrative | Managerial | Policies, procedures, and human-process controls | AUP, training, background checks, audits |

### Control Functions

| Function | Description | Physical Example | Technical Example | Administrative Example |
|---|---|---|---|---|
| Preventive | Stops an attack before it occurs | Door lock | Firewall | Acceptable Use Policy |
| Detective | Identifies attacks in progress or after the fact | Security camera | IDS / SIEM alert | Security audit |
| Corrective | Restores secure state after an incident | Fire suppression system | Backup restore | Incident response plan |
| Deterrent | Discourages attack without physically blocking | Warning signs | Login banners | Security awareness training |
| Compensating | Substitutes for a primary control that cannot be implemented | Secondary access card reader | Encryption on unpatched legacy system | Increased monitoring of vulnerable systems |
| Directive | Provides guidance on expected behavior | Posted safety rules | Automated policy enforcement | Mandatory training completion |

**Exam Tip 1:** On SY0-701, every scenario question about a control will require you to identify both its category (Physical/Technical/Administrative) and its function (Preventive/Detective/Corrective/Deterrent/Compensating/Directive). Practice applying both axes simultaneously.

---

## 3. Threat Actor Comparison Table

| Threat Actor | Primary Motivation | Sophistication Level | Resource Level | Typical Tactics | Example |
|---|---|---|---|---|---|
| Nation-State | Espionage, sabotage, geopolitical advantage | Advanced (APT capability) | Nation-level funding | Zero-days, supply chain attacks, long dwell time | Stuxnet, SolarWinds compromise |
| Organized Crime | Financial gain | High | Well-funded criminal networks | Ransomware, banking trojans, credential theft | REvil ransomware group |
| Hacktivist | Ideology, political cause, public embarrassment | Moderate | Crowdsourced, volunteer | DDoS, website defacement, data leaking | Anonymous operations |
| Insider Threat | Financial, revenge, coercion, negligence | Varies (has authorized access) | Authorized internal access | Data exfiltration, sabotage, policy violations | Edward Snowden NSA disclosures |
| Script Kiddie | Notoriety, curiosity, thrill | Low | Minimal | Pre-built tools, automated scanners, known CVE exploitation | Mass web defacement campaigns |
| Competitor | Economic advantage | Varies | Corporate resources | Corporate espionage, social engineering | Trade secret theft |

**Exam Tip 2:** The exam will describe a scenario and ask you to identify the most likely threat actor. Focus on three attributes: motivation, level of sophistication, and available resources. Nation-state = patient, stealthy, strategic. Script kiddie = opportunistic, noisy, uses known tools.

---

## 4. Vulnerability Classes

### Software Vulnerabilities

**Buffer Overflow** — A program writes more data to a buffer than it can hold, overwriting adjacent memory. This can allow an attacker to inject and execute arbitrary code. Buffer overflows are among the oldest and most dangerous software vulnerabilities.

**Race Condition** — A flaw where a program's behavior depends on the timing or sequence of events. An attacker who can influence timing can change outcomes. Time-of-Check/Time-of-Use (TOCTOU) is a classic race condition subtype.

**Integer Overflow** — When an arithmetic operation produces a value that exceeds the maximum size of the data type, the value wraps around to an unexpected small or negative number, potentially causing program logic errors.

**Null Pointer Dereference** — A program attempts to use a null (empty) pointer as if it points to valid memory, causing a crash. Repeated crashes can be exploited for denial-of-service attacks.

### Configuration Vulnerabilities

**Default Credentials** — Vendor-supplied usernames and passwords (admin/admin, admin/password) that are publicly documented. Organizations that deploy equipment without changing default credentials are trivially compromised.

**Open Ports** — Network ports left open for services that are not needed. Every open port is a potential entry point. Port scanning tools like Nmap allow attackers to enumerate open ports rapidly.

**Excessive Permissions** — User accounts or service accounts granted more access than required for their function. A violation of the principle of least privilege.

**Unencrypted Protocols** — Use of protocols such as Telnet, FTP, or HTTP for sensitive communications, exposing credentials and data to interception.

### Operational Vulnerabilities

**Missing Patches** — Failure to apply vendor-released security updates. The interval between patch release and deployment is a window of active exploitation.

**Unsupported Software** — Applications and operating systems that have reached end-of-life and no longer receive security patches. Running unsupported software permanently exposes the organization to unpatched CVEs.

**Weak Passwords** — Simple, guessable, or reused passwords that can be compromised by brute force or credential stuffing attacks.

---

## 5. Attack Categories Reference Table

| Attack Category | Definition | Active or Passive | Primary CIA Target | Example |
|---|---|---|---|---|
| Eavesdropping | Capturing network traffic without modification | Passive | Confidentiality | Packet sniffing with Wireshark |
| Traffic Analysis | Inferring information from traffic patterns without reading content | Passive | Confidentiality | Analyzing metadata to map org structure |
| Shoulder Surfing | Visually observing someone entering sensitive information | Passive | Confidentiality | Watching a PIN entry at an ATM |
| Replay Attack | Capturing and retransmitting valid authentication tokens | Active | Integrity, Authentication | Retransmitting a captured Kerberos ticket |
| Injection Attack | Inserting malicious content into an input or data stream | Active | Integrity, Confidentiality | SQL injection in a web login form |
| Man-in-the-Middle | Intercepting and potentially altering communication between two parties | Active | Confidentiality, Integrity | ARP poisoning to redirect LAN traffic |
| Denial of Service | Overwhelming resources to deny access to legitimate users | Active | Availability | SYN flood against a web server |
| Brute Force | Systematically trying all possible passwords until correct | Active | Authentication | Automated password guessing tool |
| Zero-Day Exploit | Attacking an unknown, unpatched vulnerability | Active | Varies | Nation-state attack using an undisclosed flaw |

---

## 6. Common Ports Reference Table

| Port | Protocol | Service | Security Notes |
|---|---|---|---|
| 21 | TCP | FTP | Unencrypted — use SFTP (22) or FTPS (990) instead |
| 22 | TCP | SSH / SFTP | Encrypted remote access and file transfer |
| 23 | TCP | Telnet | Unencrypted — replace with SSH (22) |
| 25 | TCP | SMTP | Email transmission — often blocked outbound to prevent spam |
| 53 | TCP/UDP | DNS | DNS poisoning and tunneling attacks target this port |
| 80 | TCP | HTTP | Unencrypted web — use HTTPS (443) for sensitive content |
| 110 | TCP | POP3 | Unencrypted email retrieval |
| 143 | TCP | IMAP | Unencrypted email sync |
| 443 | TCP | HTTPS | Encrypted web traffic using TLS |
| 445 | TCP | SMB | File sharing — target of WannaCry and NotPetya |
| 3389 | TCP | RDP | Remote Desktop — frequent brute-force and exploitation target |

---

## 7. Indicators of Compromise (IOC) Overview

Indicators of Compromise are pieces of forensic evidence suggesting a system has been breached. Security operations teams use IOCs to detect, contain, and investigate incidents.

**Network IOCs:**

- Unusual large outbound data transfers to unknown foreign IP addresses.
- Connections to domains with recent registration dates or known bad reputation.
- Use of non-standard ports for common protocols.
- DNS queries to domains that follow domain generation algorithm patterns.

**Host IOCs:**

- New files created in system directories outside of maintenance windows.
- Unexpected scheduled tasks, services, or startup registry entries.
- Processes spawning unexpected child processes (for example, Word spawning PowerShell).
- Security tools disabled or uninstalled.

**Account IOCs:**

- Login from a geographic location inconsistent with the user's normal pattern.
- Multiple consecutive failed logins followed by a successful login.
- New privileged accounts created without a corresponding IT change ticket.
- Access to sensitive resources outside normal business hours.

---

## 8. Threat Intelligence Sources

| Source Type | Description | Best Used For |
|---|---|---|
| OSINT | Open-source intelligence from public internet, news, and research | Initial reconnaissance context, broad threat landscape |
| ISAC | Sector-specific sharing organizations (FS-ISAC, H-ISAC) | Industry-specific threats and peer organization incidents |
| Commercial Feed | Paid, curated intelligence with IOCs and TTPs | Real-time operational intelligence for SOC teams |
| CISA Advisories | US government alerts on active threats and critical CVEs | Government and critical infrastructure threats |
| Dark Web Monitoring | Monitoring criminal forums for stolen data or planned attacks | Early warning of credential theft or targeted attacks |
| Internal Telemetry | SIEM data, firewall logs, EDR alerts from within the org | Incident detection and response within the environment |

---

## 9. Security+ Exam Tips for Module 01

**Exam Tip 1:** Domain 2 is 22% of SY0-701 — the second-highest weighted domain. Budget significant study time here.

**Exam Tip 2:** Never interchange vulnerability, threat, and risk. Vulnerability = the weakness. Threat = the actor or event that could exploit it. Risk = likelihood × impact.

**Exam Tip 3:** Nation-state actor questions involve long dwell time, custom malware, strategic objectives, and zero-day exploits. If the scenario is patient, stealthy, and geopolitically motivated, the answer is nation-state.

**Exam Tip 4:** Passive attacks do not modify data. If the scenario says "captured," "monitored," or "observed" without any change to data, the attack is passive.

**Exam Tip 5:** Non-repudiation is enforced by digital signatures, not just any authentication mechanism. MFA proves identity at login; a digital signature proves identity at the time of a specific action.

**Exam Tip 6:** Attack surface reduction questions ask what you would do first. The answer is almost always: disable unused services or apply the principle of least privilege.

**Exam Tip 7:** IOC questions describe an observable symptom. Work backward from the symptom to the cause. Cleared event logs = attacker covering tracks. Impossible travel login = credential compromise.

**Exam Tip 8:** For control classification, the question will often give you a scenario rather than naming the control directly. A "sign warning employees not to plug in unknown USB drives" is Administrative/Deterrent. An automated script that blocks USB ports is Technical/Preventive.

---

## 10. Required Study Resources

Complete the following before taking the Module 01 quiz:

- Professor Messer's SY0-701 study notes covering Domain 2 objectives, available free at professormesser.com.
- Professor Messer's SY0-701 video lectures for Domain 2 objectives, available at professormesser.com.
- CompTIA's official SY0-701 exam objectives document, available at comptia.org.

---

## 11. Study Checklist

Work through this checklist before moving to the quiz:

- [ ] Define each CIA Triad property and give one technical control for each.
- [ ] Explain non-repudiation and identify the control that enforces it.
- [ ] Classify any given control using both the category axis and the function axis.
- [ ] Describe each of the five threat actor types by motivation, sophistication, and resource level.
- [ ] Distinguish between a vulnerability, a threat, and risk using the formal definitions.
- [ ] Identify all six vulnerability classes and give an example of each.
- [ ] Classify any attack scenario as active or passive and identify the CIA property targeted.
- [ ] List at least five common port numbers and their associated services.
- [ ] Describe three network IOCs and three host IOCs.
- [ ] Identify the appropriate threat intelligence source given a specific operational need.
- [ ] Complete the Module 01 Lab activity on threat classification.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
- [ ] Post two peer replies by Sunday at 11:59 PM.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 01 Reading Guide

Proprietary and Confidential. Not for disclosure outside of authorized course use.
