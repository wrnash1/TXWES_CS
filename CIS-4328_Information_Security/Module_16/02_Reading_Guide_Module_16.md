# Reading Guide: Module 16 — Security+ SY0-701 Exam Preparation and Capstone

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Purpose of This Guide

This reading guide consolidates the authoritative references for all five SY0-701 domains covered in Module 16. Use it alongside both video scripts. For each exam objective, you will find the primary reading, secondary references, and focused reading questions that mirror the cognitive level of actual exam items.

---

## Primary Textbook Reference

**CompTIA Security+ Study Guide: Exam SY0-701** — Mike Chapple and David Seidl (Sybex)

Review the following chapters for Module 16:

- Chapters 1–3: Security Concepts, Cryptography, PKI (Domain 1)
- Chapters 4–6: Threats, Vulnerabilities, Social Engineering (Domain 2)
- Chapters 7–9: Security Architecture, Cloud, Network Design (Domain 3)
- Chapters 10–14: Security Operations, Incident Response, Identity Management (Domain 4)
- Chapters 15–18: GRC, Risk, Compliance, Data Privacy (Domain 5)

---

## Authoritative Standards and Frameworks

### Domain 1 — General Security Concepts

**NIST SP 800-63B** — Digital Identity Guidelines: Authentication and Lifecycle Management

- Read Section 4 (Authenticator Types) and Section 5 (Authenticator and Verifier Requirements)
- Focus on memorized secret authenticators, look-up secrets, and multi-factor cryptographic devices

**NIST SP 800-57 Part 1** — Recommendation for Key Management

- Read Section 5 (Cryptographic Key Types) and Section 6 (Cryptoperiods)
- Focus on key lifecycle stages: generation, distribution, storage, use, revocation, and destruction

**RFC 5280** — Internet X.509 Public Key Infrastructure Certificate and CRL Profile

- Read Section 4.1 (Basic Certificate Fields) to understand what fields appear on an X.509 certificate
- This directly supports PKI exam objectives

### Domain 2 — Threats, Vulnerabilities, and Mitigations

**MITRE ATT&CK Framework** — Available at attack.mitre.org

- Review the Enterprise matrix Tactics column: Initial Access through Exfiltration
- For each tactic, note 2–3 example techniques you could recognize in a scenario
- Pay particular attention to: T1566 (Phishing), T1078 (Valid Accounts), T1027 (Obfuscated Files), T1486 (Data Encrypted for Impact)

**MITRE ATT&CK** — Mitigation objects (M#### entries)

- Review mitigations for the above four techniques to understand the defensive countermeasures ATT&CK recommends

**CVSS v3.1 User Guide** — Available at first.org/cvss

- Read Section 2 (Base Metrics) covering Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, and three impact metrics
- Understand how a Critical (9.0–10.0) score differs from a High (7.0–8.9) score in terms of base metric values

**Lockheed Martin Cyber Kill Chain** — Available at lockheedmartin.com/cyber

- Review all seven stages and the corresponding defensive actions at each stage
- Note: Disrupting the kill chain at Delivery (Stage 3) is generally more cost-effective than responding at Exfiltration (Stage 7)

### Domain 3 — Security Architecture

**NIST SP 800-207** — Zero Trust Architecture

- Read Section 2 (Zero Trust Basics) and Section 3 (Zero Trust Architecture Logical Components)
- Focus on the Policy Engine, Policy Administrator, and Policy Enforcement Point model

**CIS Controls Version 8** — Available at cisecurity.org

- Review Controls 1–6 (Inventory, Software, Data Protection, Secure Configuration, Account Management, Access Control Management)
- These map directly to SY0-701 architecture objectives

**Cloud Security Alliance (CSA)** — Cloud Controls Matrix (CCM) v4

- Review the IAM and IVS (Infrastructure and Virtualization Security) domains
- Focus on shared responsibility delineation across IaaS, PaaS, and SaaS

### Domain 4 — Security Operations

**NIST SP 800-61 Rev. 2** — Computer Security Incident Handling Guide

- Read Section 2.3 (Incident Response Team Structure), Section 3 (Handling an Incident), and Section 3.6 (Post-Incident Activity)
- This is the canonical reference for the IR lifecycle on the Security+ exam

**NIST SP 800-86** — Guide to Integrating Forensic Techniques into Incident Response

- Read Section 4 (Performing the Forensic Process) for the order of volatility
- Section 5 covers media, network, software, and database forensics

**Windows Security Event Log Reference** — Microsoft Docs

- Review Event IDs: 4624, 4625, 4634, 4648, 4720, 4722, 4726, 4740, 4768, 4769, 4771
- For each, know what it logs and what malicious pattern it could indicate

**OWASP Top Ten 2021** — Available at owasp.org

- Review all ten categories; focus on A01 (Broken Access Control), A03 (Injection), A07 (Identification and Authentication Failures), A09 (Security Logging and Monitoring Failures)

### Domain 5 — Security Program Management and Oversight

**NIST Cybersecurity Framework (CSF) 2.0** — Available at nist.gov/cyberframework

- Review the six functions: Govern, Identify, Protect, Detect, Respond, Recover
- Note: CSF 2.0 added "Govern" as a sixth function; CSF 1.1 had only five

**ISO/IEC 27001:2022** — Overview sections available from iso.org

- Review Annex A control categories to understand the ISMS control framework
- Focus on domains: Access Control (A.9), Cryptography (A.10), Operations Security (A.12), Incident Management (A.16)

**GDPR Official Text** — Articles 5, 25, 32, 33, 34

- Article 5: Principles relating to processing of personal data (lawfulness, purpose limitation, data minimization)
- Article 25: Data protection by design and by default
- Article 32: Security of processing (encryption, pseudonymization requirements)
- Articles 33–34: Notification obligations after a personal data breach

**PCI DSS v4.0 Summary** — Available at pcisecuritystandards.org

- Review the 12 requirements at a summary level
- Understand scope: applies to any entity storing, processing, or transmitting cardholder data

---

## Focused Reading Questions

Answer these questions as you read. They reflect the scenario-based format of the actual exam.

### Domain 1 Questions

1. A company encrypts files using AES-256 for storage and then uses RSA-2048 to encrypt the AES key for transmission. What is this pattern called, and what security problem does it solve?

2. A new employee's certificate is signed by an intermediate CA, which is signed by the corporate root CA. The root CA certificate expires next month. What happens to all end-entity certificates in the chain when the root expires?

3. Explain the difference between CRL and OCSP. In a high-security environment with real-time revocation requirements, which is preferred and why?

### Domain 2 Questions

4. A threat actor sends an email to a CFO impersonating the CEO, requesting a $200,000 wire transfer to a vendor for an urgent deal. What social engineering technique is this, and what two organizational controls would most directly prevent it?

5. An analyst identifies malware that uses Windows Management Instrumentation (WMI) to execute PowerShell commands and communicates over port 443 with a legitimate-looking domain. The malware leaves no files on disk. What malware category is this, and why does it evade traditional antivirus?

6. Using the CVSS v3.1 framework, describe what combination of base metrics would produce a Critical (CVSS 10.0) score. What real-world vulnerability scenario approaches this profile?

### Domain 3 Questions

7. A company is migrating its HR application to a SaaS platform. The CISO asks who is responsible for patching the application server. Who is responsible, and how does this responsibility shift when the company uses IaaS instead?

8. A security architect proposes implementing micro-segmentation for the enterprise data center. What specific attack technique does micro-segmentation most directly prevent, and what tool or technology is commonly used to implement it?

9. Describe the three logical components of Zero Trust Architecture as defined in NIST SP 800-207. How do they interact for a single access request?

### Domain 4 Questions

10. An incident responder arrives at a workstation suspected of compromise. List the evidence sources they should collect in order, explaining why volatile sources come first.

11. A SIEM generates an alert after correlating these events within 10 minutes: 50 failed SSH login attempts from IP 203.0.113.42 against the same account, followed by one successful login. Write a one-paragraph description of the incident and identify the MITRE ATT&CK tactic most applicable to this sequence.

12. Explain the difference between SAML 2.0 and OpenID Connect. For a new mobile application that needs to authenticate users via Google accounts, which protocol is more appropriate and why?

### Domain 5 Questions

13. Calculate the ALE for the following scenario: A customer database has an asset value of $5,000,000. Historical data suggests there is a 20% chance of a breach in any given year (ARO = 0.2) and a typical breach exposes 40% of the data (Exposure Factor = 0.4). A new DLP system costs $80,000 per year and is expected to reduce the exposure factor to 10%.

14. A healthcare company operates in California, processes EU patient records, and accepts credit card payments. List the three compliance frameworks that directly apply, and identify the most severe penalty structure among them.

15. Explain the difference between anonymization and pseudonymization under GDPR. Why is pseudonymized data still considered personal data while anonymized data is not?

---

## Key Terms for Module 16

Study these terms until you can define each without prompting:

- AAA (Authentication, Authorization, Accounting)
- AES, RSA, ECC, SHA-256, HMAC
- PKI, CA, RA, CRL, OCSP, X.509
- MAC, DAC, RBAC, ABAC
- APT, threat actor, threat vector, threat surface
- Phishing, spear phishing, whaling, vishing, smishing, BEC
- Virus, worm, Trojan, ransomware, rootkit, fileless malware, logic bomb
- CVE, CWE, CVSS, zero-day
- MITRE ATT&CK, Cyber Kill Chain, Diamond Model
- Zero Trust, micro-segmentation, SASE
- IaaS, PaaS, SaaS, shared responsibility model
- DMZ, VLAN, air gap, screened subnet
- IR lifecycle phases (NIST SP 800-61)
- SIEM, SOAR, EDR, XDR
- Order of volatility, chain of custody
- SAML, OAuth 2.0, OIDC, LDAP, Kerberos, TGT, TGS
- PAM, JIT access, privilege escalation
- GRC, risk appetite, risk tolerance
- SLE, ALE, ARO, exposure factor, ROSI
- Risk avoidance, mitigation, transference, acceptance
- NIST CSF, ISO 27001, HIPAA, GDPR, PCI DSS, SOC 2
- Data at rest, in transit, in use
- DLP, tokenization, anonymization, pseudonymization

---

## Exam Readiness Self-Assessment

Rate your confidence for each domain on a scale of 1 (need significant review) to 5 (ready to test):

| Domain | Topic | Self-Rating (1–5) |
|---|---|---|
| Domain 1 | AAA and authentication factors | |
| Domain 1 | Symmetric vs. asymmetric encryption | |
| Domain 1 | PKI, certificates, CRL, OCSP | |
| Domain 2 | Threat actor types and motivations | |
| Domain 2 | Social engineering techniques | |
| Domain 2 | Malware taxonomy | |
| Domain 2 | CVSS, CVE, vulnerability scanning | |
| Domain 2 | MITRE ATT&CK and Kill Chain | |
| Domain 3 | Cloud shared responsibility model | |
| Domain 3 | Zero Trust principles | |
| Domain 3 | Network segmentation, DMZ, VLAN | |
| Domain 4 | IR lifecycle phases and order | |
| Domain 4 | SIEM correlation and log analysis | |
| Domain 4 | Identity federation (SAML, OIDC) | |
| Domain 4 | Forensics order of volatility | |
| Domain 5 | Risk treatment options | |
| Domain 5 | ALE/SLE calculations | |
| Domain 5 | GDPR, HIPAA, PCI DSS applicability | |
| Domain 5 | Data classification and DLP | |

Any domain rated 3 or below should receive focused review time before your exam date.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*

---

### Introduction
Welcome to **Module 16 – Final Exam Prep and CompTIA Security+ SY0-701 Certification**! This module prepares you for both the course final exam and the CompTIA Security+ SY0-701 certification exam. Rather than introducing new content, this module synthesizes all five exam domains covered in Modules 01–15 and provides targeted review strategies for the most heavily tested scenario types.

---

### 1. High-Yield Domain Review Summary
The SY0-701 exam is divided into five domains. Review each domain's core concepts using the summaries below:

*   **Domain 1 – General Security Concepts (12%)**: CIA Triad (Confidentiality, Integrity, Availability), cryptography fundamentals (symmetric vs. asymmetric, hashing, digital signatures, key exchange), PKI (CA hierarchy, CSR, X.509 certificates, CRL, OCSP), and access control models (MAC, DAC, RBAC, ABAC). Key trap: Two passwords are NOT MFA — different factor categories are required.
*   **Domain 2 – Threats, Vulnerabilities, and Mitigations (22%)**: Threat actor types (nation-state, hacktivist, insider, script kiddie), social engineering (phishing, spear phishing, whaling, vishing, smishing, pretexting, pharming), application attacks (SQLi, XSS, buffer overflow, CSRF, directory traversal, TOCTOU), network attacks (DDoS types, ARP poisoning, DNS poisoning, IP spoofing, Smurf), and malware types (ransomware, RAT, rootkit, keylogger, logic bomb). Key trap: Pharming redirects users via DNS/hosts file — it is not phishing.
*   **Domain 3 – Security Architecture (18%)**: Network security controls (stateful firewall vs. NGFW vs. IDS vs. IPS), VPN types (IPsec tunnel/transport, SSL/TLS clientless), cloud service models and shared responsibility (IaaS/PaaS/SaaS), virtualization security (VM escape, container breakout), wireless security (WPA3/SAE, evil twin, deauth attacks), and Zero Trust architecture. Key trap: IDS detects only — IPS blocks inline.
*   **Domain 4 – Security Operations (28%)**: Incident response lifecycle (NIST: Preparation → Detection → Containment → Eradication → Recovery → Post-Incident), digital forensics (order of volatility, chain of custody, write blockers, forensic imaging), threat intelligence (IOCs, MITRE ATT&CK, STIX/TAXII), authentication (MFA factors, biometric FAR/FRR/CER, SSO, SAML), identity and access management (least privilege, SoD, provisioning/deprovisioning, PAM), and security tools (SIEM, SOAR, EDR, CASB, CSPM). Key trap: Contain before eradicating — never wipe a system before imaging it.
*   **Domain 5 – Security Program Management and Oversight (20%)**: Risk management (ALE = SLE × ARO, risk response strategies: mitigate/avoid/transfer/accept), business continuity (BCP, RTO, RPO, hot/warm/cold sites), governance (policy vs. standard vs. guideline vs. procedure), compliance frameworks (PCI-DSS, HIPAA, GDPR, NIST CSF, ISO 27001), data classification, privacy principles (PII, PHI, data minimization, purpose limitation), and third-party risk management. Key trap: RTO = downtime limit; RPO = data loss limit.

---

### 2. Certification Exam Strategy Tips
*   **Exam Format:** SY0-701 consists of a maximum of 90 questions with a 90-minute time limit. Questions include multiple choice (single answer), multiple response (select all that apply), and performance-based questions (PBQs — drag-and-drop, matching, simulations). PBQs appear first; most candidates skip them initially and return after completing multiple choice.
*   **Scenario Question Strategy:** SY0-701 is scenario-heavy — most questions describe a situation and ask you to identify the attack, select the best control, or determine the correct response. Read the last sentence of the scenario first (the actual question) before reading the full scenario to focus your analysis on what is being asked.
*   **Eliminate Clearly Wrong Answers:** Most SY0-701 questions have one or two obviously incorrect distractors (often from a different domain or a completely irrelevant concept). Eliminate those first to improve your odds on uncertain questions.
*   **"Best" and "Most" Language:** When a question asks for the "best" or "most effective" control, there may be multiple technically correct answers — select the one most directly targeted at the specific risk described. Comprehensive controls that address the root cause beat generic or partial controls.
*   **Passing Score:** CompTIA SY0-701 has a passing score of 750 on a scale of 100–900. CompTIA does not penalize for wrong answers, so never leave a question blank — guess if necessary.
*   **Registration:** Register for the SY0-701 exam through [CompTIA's official certification portal](https://www.comptia.org/certifications/security). Exam vouchers are available through Pearson VUE testing centers or online proctored testing.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) covers all five domains with practice questions, performance-based question walkthroughs, and exam day strategy guidance — use it as your primary free study resource alongside this course.

---

### Required Readings & Videos
To prepare for the final exam and certification:
*   **Required Reading:** Review all five domain sections in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on any domain where your practice quiz scores were weakest.
*   **Required Video:** Review the complete [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). Prioritize the domain sections covering your weakest areas identified through practice testing.

---

### Lab & Command Integration
This module has no new lab activity. Use the available time to complete any outstanding practice exams, review flagged questions from previous module quizzes, and attempt full-length SY0-701 practice tests under timed conditions.

---

### 3. Final Exam Preparation Checklist
- [ ] Review the Domain 1 glossary: CIA Triad, cryptography types, PKI chain of trust, access control models.
- [ ] Review the Domain 2 glossary: Threat actor types, social engineering attacks, application and network attacks.
- [ ] Review the Domain 3 glossary: Firewall types, IDS vs. IPS, VPN protocols, cloud service models, wireless security.
- [ ] Review the Domain 4 glossary: NIST IR phases, order of volatility, MFA factor types, SIEM vs. SOAR vs. EDR.
- [ ] Review the Domain 5 glossary: ALE formula, RTO vs. RPO, policy hierarchy, PCI-DSS/HIPAA/GDPR applicability.
- [ ] Complete at least two full-length practice exams using [Professor Messer's SY0-701 practice tests](https://www.professormesser.com/) or another reputable source.
- [ ] Review every question you answered incorrectly on practice exams and identify the domain and concept gap.
- [ ] Register for the SY0-701 exam at [Pearson VUE / CompTIA certification portal](https://www.comptia.org/certifications/security).
