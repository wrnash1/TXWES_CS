# Reading Guide: Module 16 - Final Exam Prep and CompTIA Security+ SY0-701 Certification
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

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
