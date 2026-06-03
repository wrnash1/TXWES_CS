# Video Script: Module 16 — Security+ SY0-701 Exam Preparation (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Overview

Welcome back to Module 16, Part 2. In Part 1 we locked in Domains 1 and 2. Now we complete the review with Domain 3 (Security Architecture, 18%), Domain 4 (Security Operations, 28%), and Domain 5 (Security Program Management and Oversight, 20%). Then we close with the exam strategy session that ties everything together.

Domain 4 is the single largest domain at 28%. It covers what security professionals do every day — monitor, detect, respond, and recover. Do not underweight your preparation here.

---

## Section 1 — Domain 3: Security Architecture (18%)

### Subsection 1.1 — Cloud Security Concepts

Cloud service models define the boundary of customer responsibility:

- **IaaS (Infrastructure as a Service)**: Provider manages hardware, networking, and virtualization. Customer manages OS, middleware, applications, and data. Most customer control, most customer responsibility.
- **PaaS (Platform as a Service)**: Provider adds OS and runtime. Customer manages applications and data only.
- **SaaS (Software as a Service)**: Provider manages everything. Customer only manages data and user access.

The shared responsibility model is a critical exam concept. Who patches the OS in IaaS? The customer. Who patches the OS in SaaS? The provider. The exam will describe a scenario and ask you to identify whose responsibility a given security control is.

Cloud deployment models:

- Public cloud: Infrastructure shared among multiple tenants (AWS, Azure, GCP)
- Private cloud: Infrastructure dedicated to one organization
- Hybrid cloud: Combination of public and private
- Community cloud: Shared by organizations with common interests (government, healthcare)

**Exam Trap 1**: "The customer is always responsible for their data" is true in all three service models. The scope of additional responsibilities shrinks from IaaS to SaaS, but data ownership stays with the customer.

### Subsection 1.2 — Network Segmentation and Zero Trust

**Network segmentation** divides a network into zones to limit lateral movement. Key zones:

- DMZ (Demilitarized Zone): Hosts public-facing services (web servers, mail relays). Isolated from the internal network by firewalls on both sides.
- Intranet: Internal trusted network
- Extranet: Controlled access for external partners
- VLAN (Virtual LAN): Logical segmentation within a physical switch fabric

**Zero Trust Architecture (ZTA)** is built on the principle "never trust, always verify." Key tenets:

- No implicit trust based on network location — being inside the corporate perimeter does not grant trust
- Every access request is authenticated, authorized, and continuously validated
- Least privilege access — users receive only the minimum rights needed
- Micro-segmentation — network segments so granular that lateral movement is almost impossible
- Continuous monitoring and logging of all traffic

NIST SP 800-207 is the definitive reference for Zero Trust architecture.

**Software-Defined Networking (SDN)**: Separates the control plane (routing decisions) from the data plane (packet forwarding). The centralized controller enables dynamic, policy-driven network reconfiguration.

**SASE (Secure Access Service Edge)**: Converges networking and security functions into a cloud-delivered service. Combines SD-WAN with cloud-native security including CASB, ZTNA, and FWaaS.

### Subsection 1.3 — Infrastructure Security

**Defense in depth** layers multiple security controls so that no single failure causes a breach. Physical → Network → Host → Application → Data.

**Air gap**: Complete physical isolation from other networks. Used in industrial control systems (ICS/SCADA) and classified environments.

**Screened subnet**: An architecture where a subnet sits between two firewalls — the outer firewall faces the internet, and the inner firewall faces the internal network. Equivalent to a DMZ.

**Honeypot and Honeynet**: Deliberately vulnerable systems designed to lure attackers. Honeypot = single system; Honeynet = network of honeypots. Used for threat intelligence gathering and early warning.

**Deception technology**: Broader term for fake assets (honey credentials, honey files, honey subnets) distributed throughout the environment to detect unauthorized internal activity.

---

## Section 2 — Domain 4: Security Operations (28%)

### Subsection 2.1 — Incident Response

The NIST incident response lifecycle has four phases:

1. **Preparation**: Policies, playbooks, tools, training, communication plans
2. **Detection and Analysis**: Identifying that an incident occurred; determining scope, impact, and type
3. **Containment, Eradication, and Recovery**: Isolating affected systems, removing root cause, restoring normal operations
4. **Post-Incident Activity**: Lessons learned, updating playbooks, legal/regulatory reporting

**Exam Trap 2**: Containment comes before eradication. You stop the bleeding before you clean the wound. Students frequently reverse these two phases.

Incident categories you must know:

- Data breach: Unauthorized access and exfiltration of sensitive data
- Ransomware: Encryption-based extortion
- DDoS: Distributed Denial of Service
- Insider threat incident: Malicious or negligent actions by authorized users
- Business Email Compromise (BEC): Fraudulent financial transactions via impersonation

**Chain of custody**: The documented record of every person who handled digital evidence. Essential for legal admissibility. Any gap in chain of custody can invalidate evidence in court.

**Forensics order of volatility**: Collect evidence from most volatile to least volatile.

1. CPU registers, cache
2. RAM
3. Network connections, routing tables
4. Running processes
5. Disk (non-volatile storage)
6. Remote logs
7. Archival media

### Subsection 2.2 — SIEM and Log Analysis

A **Security Information and Event Management (SIEM)** system collects, aggregates, normalizes, and correlates log data from across the environment to detect threats.

Core SIEM functions:

- Log aggregation: Centralizing logs from firewalls, endpoints, servers, applications
- Normalization: Converting disparate log formats into a common schema
- Correlation: Applying rules to detect patterns that indicate threats (e.g., multiple failed logins from one source followed by a success = possible brute force)
- Alerting: Notifying analysts when rules trigger
- Dashboards and reporting: Visualizing security posture

**Security Orchestration, Automation, and Response (SOAR)** extends SIEM by automating the response workflow. When the SIEM generates an alert, SOAR can automatically quarantine an endpoint, block an IP at the firewall, and open a ticket — without waiting for an analyst.

**Log types you must recognize**:

- Syslog: Standard Unix/Linux logging protocol
- Windows Event Logs: Security, System, Application event channels; critical Event IDs include 4624 (successful logon), 4625 (failed logon), 4648 (logon with explicit credentials), 4720 (user account created)
- NetFlow: Network metadata (source/dest IP, ports, bytes, packets) — does not contain payload
- PCAP: Full packet capture — contains payload, used for deep forensic analysis

### Subsection 2.3 — Identity and Access Management

**Privileged Access Management (PAM)**: Controls and monitors accounts with elevated privileges. PAM solutions include features such as:

- Just-in-time (JIT) access: Privileges granted for a specific task window, then automatically revoked
- Session recording: Video record of privileged sessions for audit
- Password vaulting: Storing and rotating privileged account credentials automatically

**Identity Provider (IdP)**: A system that creates, maintains, and manages identity information. Examples: Azure Active Directory, Okta, Google Workspace.

**Single Sign-On (SSO)**: One authentication event grants access to multiple applications. Reduces password fatigue. Protocols:

- SAML 2.0: XML-based; widely used for enterprise SSO between IdP and service providers
- OAuth 2.0: Authorization framework; grants limited access to resources without exposing credentials
- OpenID Connect (OIDC): Authentication layer on top of OAuth 2.0; provides identity tokens

**Exam Trap 3**: OAuth is authorization, not authentication. OIDC adds authentication to OAuth. The exam will describe a scenario where an app "delegates authentication" — that is OIDC, not plain OAuth.

**Directory Services**: LDAP (Lightweight Directory Access Protocol) is the protocol used to query and modify directory information. Active Directory uses LDAP as its query protocol.

**Kerberos**: The authentication protocol used internally by Active Directory. Uses tickets rather than passwords for ongoing authentication after initial login. Key ticket types:

- TGT (Ticket Granting Ticket): Obtained at initial login; used to request service tickets
- Service Ticket (TGS): Grants access to a specific service

**Pass-the-Hash** and **Pass-the-Ticket** are attacks that steal cached authentication material to authenticate without knowing the plaintext password.

---

## Section 3 — Domain 5: Security Program Management and Oversight (20%)

### Subsection 3.1 — Governance, Risk, and Compliance (GRC)

**Governance** ensures security decisions align with business objectives. It includes the policies, standards, procedures, and guidelines that define how the organization manages security.

Hierarchy:

- Policy: High-level statement of intent ("All sensitive data shall be encrypted at rest")
- Standard: Specific, measurable requirement ("AES-256 must be used for sensitive data encryption")
- Procedure: Step-by-step instructions for implementing the standard
- Guideline: Recommended (not mandatory) best practices

**Risk management** is the continuous process of identifying, assessing, and responding to risks.

Risk treatment options:

- Avoidance: Eliminate the activity that creates the risk
- Mitigation: Implement controls to reduce likelihood or impact
- Transference: Shift risk to a third party (cyber insurance, outsourcing)
- Acceptance: Acknowledge the risk and choose to absorb it (residual risk after other treatments)

**Risk assessment formulas**:

- Asset Value × Exposure Factor = Single Loss Expectancy (SLE)
- SLE × Annual Rate of Occurrence (ARO) = Annual Loss Expectancy (ALE)
- ALE Before Control − ALE After Control − Annual Cost of Control = Return on Security Investment (ROSI)

**Exam Trap 4**: Risk transference does not eliminate the risk. The organization retains liability. Cyber insurance pays out after a breach — it does not prevent one.

### Subsection 3.2 — Compliance Frameworks

**Regulatory vs. voluntary frameworks**:

- HIPAA: US law; mandates protections for Protected Health Information (PHI). Non-compliance triggers civil and criminal penalties.
- PCI DSS: Payment card industry standard; required for any organization handling cardholder data. Contractual, not law in most jurisdictions.
- GDPR: EU law; applies to any organization processing EU resident personal data. Fines up to 4% of global annual revenue.
- SOC 2: Voluntary auditing standard for service organizations; evaluates controls around security, availability, processing integrity, confidentiality, and privacy.
- NIST CSF (Cybersecurity Framework): Voluntary framework organized into five functions — Identify, Protect, Detect, Respond, Recover.
- ISO/IEC 27001: International standard for information security management systems (ISMS).

**Exam Trap 5**: PCI DSS is not a law — it is an industry standard enforced through contractual agreements with payment card networks. HIPAA is a law with criminal penalties.

### Subsection 3.3 — Data Privacy and Classification

**Data classification** labels data by sensitivity:

- Public: No harm if disclosed
- Internal/Private: Low harm; not intended for external audiences
- Confidential: Significant harm if disclosed; requires access controls
- Restricted/Top Secret: Severe harm if disclosed; strictest controls

**Data states**:

- Data at rest: Stored on disk, tape, or other persistent media — encrypt with AES-256
- Data in transit: Moving across a network — encrypt with TLS 1.2 or 1.3
- Data in use: Being processed in memory — most difficult to protect; trusted execution environments (TEEs) help

**Data loss prevention (DLP)**: Technology that detects and prevents unauthorized exfiltration of sensitive data. Can operate at the endpoint, network, or cloud level.

**Privacy-enhancing technologies**:

- Tokenization: Replace sensitive data (e.g., credit card number) with a random token. Original data stored separately in a secure vault.
- Anonymization: Remove all identifying information so data cannot be re-linked to an individual.
- Pseudonymization: Replace identifying information with pseudonyms; re-identification possible with a key. Pseudonymized data is still personal data under GDPR.

---

## Section 4 — Exam Strategy

### Subsection 4.1 — Time Management

You have 90 minutes for up to 90 questions. That is 60 seconds average per question. Performance-based questions (PBQs) appear first in most CompTIA exams. Here is the recommended approach:

1. **Skip PBQs on first pass**: Flag them and move to multiple-choice questions. PBQs can consume 5+ minutes each. Answer all MCQs first.
2. **Set a checkpoint**: After 75 questions, if less than 45 minutes remain, you are on pace. If more than 45 minutes remain, you are ahead.
3. **Return to PBQs**: Use remaining time for PBQs. Even a partial attempt on a PBQ earns partial credit.
4. **Never leave a question blank**: CompTIA does not penalize wrong answers. Guess if you must.

### Subsection 4.2 — The Elimination Technique

When uncertain, eliminate obviously wrong answers first. CompTIA MCQs typically have one clearly wrong answer, one plausible distractor, and two close contenders. Eliminating the obvious wrong answer improves your odds from 25% to 33% immediately. Eliminating the distractor brings you to 50%.

**Distractor patterns to watch for**:

- The answer that is technically true but does not answer the specific question asked
- The answer that uses the correct terminology but applies it to the wrong scenario
- The answer that describes a real tool or process but uses it for the wrong purpose
- Answers that mix two concepts (e.g., "encrypts and hashes simultaneously" — no such single mechanism exists)

### Subsection 4.3 — Scenario Question Strategy

Scenario questions describe a situation and ask what you "should do first," "would BEST address," or "is MOST likely." Key guidance:

- "Should do first" — think about the sequence of the relevant framework (IR lifecycle, risk treatment, etc.)
- "BEST" or "MOST" — you are choosing among options that may all be partially correct; select the one most aligned with established frameworks and least-privilege principles
- "MOST likely" — pick the most statistically common or contextually obvious answer, not the exotic edge case

### Subsection 4.4 — Final High-Yield Topics Checklist

Review these if you have remaining study time before the exam. These topics are historically disproportionately represented on the SY0-701:

- Authentication factor categories and MFA requirements
- Symmetric vs. asymmetric encryption use cases
- PKI trust chain and certificate revocation (CRL vs. OCSP)
- Incident response lifecycle phases and their order
- NIST CSF five functions
- Shared responsibility model by service layer
- Zero Trust core principles
- SIEM vs. SOAR distinction
- Risk treatment options (especially transference vs. acceptance)
- GDPR vs. HIPAA vs. PCI DSS applicability
- Data states and appropriate encryption standards
- Windows Event IDs: 4624, 4625, 4648, 4720, 4726
- Order of volatility for forensic evidence collection
- PAM and JIT access concepts
- Kerberos ticket types (TGT vs. TGS)

---

## Section 5 — Final Practice Questions

**Question 5**: A security team has confirmed ransomware on three servers. What is the FIRST action they should take?

- A) Eradicate the malware using an updated antivirus tool
- B) Notify law enforcement
- C) Contain the affected systems by isolating them from the network
- D) Restore from the most recent backup

Answer: C. Containment precedes eradication and recovery. Isolating the systems prevents ransomware from spreading to additional hosts.

**Question 6**: An organization stores customer credit card data. Which compliance framework MOST directly applies?

- A) HIPAA
- B) GDPR
- C) PCI DSS
- D) SOC 2

Answer: C. PCI DSS is specifically designed for organizations that store, process, or transmit payment card data.

**Question 7**: A company pays $500,000 annually for cyber liability insurance after a risk assessment identified a $2 million ALE for a data breach scenario. Which risk treatment strategy does this represent?

- A) Risk avoidance
- B) Risk acceptance
- C) Risk mitigation
- D) Risk transference

Answer: D. Paying an insurance premium to shift the financial consequence of a risk to a third party is risk transference.

**Question 8**: An analyst reviewing Active Directory logs sees Event ID 4648 repeated 40 times for the same account within two minutes. What does this MOST likely indicate?

- A) Normal user behavior during a password change
- B) A pass-the-ticket attack using cached Kerberos credentials
- C) An attacker attempting to authenticate using explicit credentials, possibly in a credential-stuffing attack
- D) A service account restarting background services

Answer: C. Event ID 4648 logs an explicit credentials logon — using credentials other than the currently logged-in user. Repeated occurrences in rapid succession are consistent with automated credential-stuffing or lateral movement attempts.

**Question 9**: Which Zero Trust principle specifically prevents an attacker who has compromised one network segment from freely moving to others?

- A) Continuous verification
- B) Micro-segmentation
- C) Least privilege
- D) Identity-based access

Answer: B. Micro-segmentation creates fine-grained network segments that require separate authentication and authorization to cross, containing lateral movement.

**Question 10**: A developer asks the security team if the company's new SaaS payroll application needs a firewall configured. The SaaS vendor says no firewall is needed. Who is responsible for network controls in a SaaS deployment?

- A) The customer's security team
- B) The SaaS vendor
- C) A shared responsibility between customer and vendor
- D) The cloud infrastructure provider

Answer: B. In SaaS, the vendor manages the infrastructure, platform, and application including network controls. The customer is responsible for data and user access management only.

---

## Section 6 — Capstone Summary

You have completed the full five-domain review for CompTIA Security+ SY0-701.

**Domain 1** gave you the vocabulary: AAA, cryptographic mechanisms, and PKI trust infrastructure.

**Domain 2** gave you the threat landscape: actor motivation, social engineering vectors, malware taxonomy, vulnerability management, and attack frameworks.

**Domain 3** gave you architectural patterns: cloud shared responsibility, Zero Trust, network segmentation, and defense in depth.

**Domain 4** gave you the operational toolkit: incident response phases, SIEM/SOAR correlation, identity federation protocols, and forensic evidence handling.

**Domain 5** gave you the governance layer: GRC, risk treatment math, compliance framework applicability, data classification, and privacy-enhancing technologies.

The exam is 90 questions in 90 minutes. Skip PBQs first, pace yourself, use elimination on difficult questions, and never leave a blank answer.

You have done the work in this course. The knowledge is there. Trust your preparation.

Good luck on the Security+ exam, and congratulations on completing CIS-4328 Information Security.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
