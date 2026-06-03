# Video Script: Module 16 — Security+ SY0-701 Exam Preparation (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Overview

This is Module 16, Part 1 — the first half of our capstone exam preparation for the CompTIA Security+ SY0-701 certification. We have covered sixteen weeks of security concepts, and now we consolidate that knowledge into a focused, exam-ready review.

In Part 1 we tackle Domain 1 (General Security Concepts, 12% of the exam) and Domain 2 (Threats, Vulnerabilities, and Mitigations, 22% of the exam). Together these two domains account for more than one-third of your exam score, so mastering them is non-negotiable.

By the end of Part 1 you will be able to recall core AAA and cryptography concepts under timed pressure, distinguish threat actor types by motivation and capability, categorize malware families by behavior, and identify the high-yield exam traps that catch students most often.

---

## Section 1 — Exam Format Quick Briefing

Before diving into domain content, let us orient ourselves to what the exam actually looks like.

The SY0-701 exam consists of a maximum of 90 questions completed in 90 minutes. That is one minute per question, which sounds comfortable until you hit the performance-based questions (PBQs). PBQs are drag-and-drop, simulated command-line, or lab-style items that can take three to five minutes each. There are typically between three and five PBQs on any given exam.

The passing score is 750 out of 900.

The five domains and their exam weights are:

- Domain 1 — General Security Concepts: 12%
- Domain 2 — Threats, Vulnerabilities, and Mitigations: 22%
- Domain 3 — Security Architecture: 18%
- Domain 4 — Security Operations: 28%
- Domain 5 — Security Program Management and Oversight: 20%

Domain 4 is the heaviest at 28%, meaning Operations topics generate more questions than any other domain. Domain 2 is close behind at 22%. Keep those weights in mind as you prioritize your remaining study time.

---

## Section 2 — Domain 1: General Security Concepts (12%)

### Subsection 2.1 — AAA Framework

AAA stands for Authentication, Authorization, and Accounting. These three functions underpin nearly every access control system you will encounter.

**Authentication** answers the question "Who are you?" It is the process of verifying an identity claim. Methods include:

- Something you know: passwords, PINs, security questions
- Something you have: smart cards, hardware tokens, mobile authenticators
- Something you are: biometrics — fingerprint, retina, voice
- Somewhere you are: geolocation-based access
- Something you do: behavioral biometrics such as typing cadence

Multi-factor authentication (MFA) requires at least two distinct factor categories. Combining a password (know) with a phone-based TOTP code (have) is MFA. Combining two passwords is not MFA — both are "something you know."

**Exam Trap 1**: The exam will describe a scenario where a user enters a password and then answers a security question. Students often mark this as MFA. It is not — both factors are "something you know," making it single-factor with redundancy.

**Authorization** answers "What are you allowed to do?" It occurs after successful authentication. Models include:

- Mandatory Access Control (MAC): Labels and clearances assigned by a central authority. The OS enforces access — users cannot change it. Common in government environments.
- Discretionary Access Control (DAC): The resource owner controls permissions. NTFS file permissions are a classic DAC example.
- Role-Based Access Control (RBAC): Permissions are tied to roles, not individuals. A "payroll clerk" role grants access to payroll data regardless of who holds that role.
- Attribute-Based Access Control (ABAC): Access decisions use multiple attributes — user department, time of day, device type. Most flexible, most complex.
- Rule-Based Access Control: A rule set (often firewall-style ACLs) governs access. Not the same as RBAC — a common exam confusion point.

**Accounting** answers "What did you do?" It is the logging and audit trail of user actions. Non-repudiation depends on robust accounting — if Alice denies sending an email, the log record and digital signature together provide non-repudiation.

### Subsection 2.2 — Cryptography Fundamentals

Symmetric encryption uses the same key to encrypt and decrypt. It is fast and suited for bulk data. Examples include AES (128, 192, 256-bit keys), 3DES (legacy, being phased out), and ChaCha20. The key distribution problem is symmetric encryption's primary weakness — securely sharing the key before communication begins is difficult at scale.

Asymmetric encryption uses a key pair: a public key and a private key. What the public key encrypts, only the private key decrypts, and vice versa. RSA, ECC (Elliptic Curve Cryptography), and Diffie-Hellman are asymmetric algorithms. Asymmetric encryption is computationally expensive, so it is typically used for key exchange rather than bulk encryption.

Hybrid encryption combines both: asymmetric encryption exchanges a symmetric session key, then symmetric encryption handles the data. TLS uses exactly this pattern.

Hashing produces a fixed-length digest from arbitrary input. Hashing is one-way — you cannot reverse a hash to get the original data. Common algorithms:

- MD5: 128-bit; deprecated for security use due to collision vulnerabilities
- SHA-1: 160-bit; deprecated
- SHA-256, SHA-384, SHA-512: Current standard family (SHA-2)
- SHA-3: Newer; different internal construction (Keccak)

A collision occurs when two different inputs produce the same hash. MD5 and SHA-1 have known practical collision attacks.

**Exam Trap 2**: "Which algorithm provides confidentiality?" points to encryption. "Which provides integrity?" points to hashing. "Which provides non-repudiation?" points to digital signatures (asymmetric + hashing combined). Know which security property each mechanism addresses.

### Subsection 2.3 — PKI and Certificates

A Public Key Infrastructure (PKI) is the ecosystem of policies, procedures, hardware, software, and people that manage digital certificates.

Key roles:

- Certificate Authority (CA): Issues and signs certificates. The CA's signature is what makes a certificate trusted.
- Registration Authority (RA): Verifies identity before the CA issues a certificate. Offloads vetting from the CA.
- Certificate Revocation List (CRL): A periodically published list of revoked certificates. Drawback: not real-time.
- Online Certificate Status Protocol (OCSP): Real-time certificate validity check. More current than CRL.
- Certificate Pinning: The application hard-codes the expected certificate or public key. Prevents substitution even if a rogue CA issues a fraudulent cert.

An X.509 certificate contains the subject's public key, the subject's identity information, the CA's digital signature, validity dates, and the certificate's serial number.

Trust chains work from the end-entity certificate up through intermediate CAs to a root CA. Your browser's trust store holds trusted root CA certificates. If any link in the chain is broken or revoked, the certificate is untrusted.

**Exam Trap 3**: Self-signed certificates are not trusted by external parties because no recognized CA signed them. They are fine for internal testing but will generate browser warnings in production.

---

## Section 3 — Domain 2: Threats, Vulnerabilities, and Mitigations (22%)

### Subsection 3.1 — Threat Actor Categories

Threat actors differ by motivation, capability, and resources. The exam will describe a scenario and ask you to identify the actor type.

| Actor Type | Motivation | Capability | Resources |
|---|---|---|---|
| Nation-State (APT) | Espionage, disruption, IP theft | Very high | Very high (government-funded) |
| Organized Crime | Financial gain | High | Substantial |
| Hacktivist | Ideology, activism | Moderate | Moderate |
| Insider Threat | Various: revenge, money, ideology | Varies (has legitimate access) | Internal |
| Script Kiddie | Recognition, curiosity | Low | Low (uses existing tools) |
| Competitor | Business advantage | Varies | Varies |

**Advanced Persistent Threats (APTs)** are characterized by long dwell times — they remain undetected in a network for months or years, performing low-and-slow reconnaissance before executing their objective. The SolarWinds compromise is a textbook APT example.

### Subsection 3.2 — Social Engineering

Social engineering exploits human psychology rather than technical vulnerabilities. The exam covers these techniques extensively.

**Phishing** is mass-scale deceptive email designed to steal credentials or deliver malware. Variants:

- Spear phishing: Targeted at a specific individual, using personalized details to increase believability
- Whaling: Spear phishing aimed at executives (C-suite)
- Vishing: Voice-based phishing via phone
- Smishing: SMS-based phishing
- Business Email Compromise (BEC): Impersonating a trusted executive to authorize fraudulent wire transfers

**Pretexting** involves creating a fabricated scenario (a pretext) to manipulate a target. For example, an attacker calls IT posing as a new employee who needs an account reset.

**Baiting** leaves physical media (USB drives) in public areas hoping someone will plug them in. The Stuxnet worm used USB baiting to breach air-gapped Iranian nuclear facilities.

**Tailgating / Piggybacking**: Following an authorized person through a secured door. Tailgating implies the victim is unaware; piggybacking implies the victim knowingly holds the door.

**Watering Hole Attack**: Compromise a website frequented by the target group. Rather than attacking the hardened corporate network directly, the attacker infects a third-party site the employees trust.

**Indicators of Social Engineering**:

- Urgency or pressure ("You must respond within the hour")
- Authority claims ("This is the CEO's office")
- Requests that bypass normal procedures
- Too-good-to-be-true offers

### Subsection 3.3 — Malware Taxonomy

Malware categories on the exam:

**Virus**: Requires a host file; self-replicates by attaching to other files. Requires user execution to spread.

**Worm**: Self-replicates and spreads across networks autonomously without user interaction. WannaCry used the EternalBlue SMB exploit to spread worm-style.

**Trojan**: Disguises itself as legitimate software. Does not self-replicate. Payload executes when the user runs the "legitimate" program.

**Ransomware**: Encrypts victim data; demands payment for decryption key. Modern variants (double-extortion) also exfiltrate data and threaten public release.

**Rootkit**: Hides its presence and other malware by modifying the OS kernel or bootloader. Extremely difficult to detect because security tools run above the rootkit.

**Keylogger**: Records keystrokes to capture credentials.

**Spyware**: Collects user information without consent. Adware is a subtype delivering unwanted ads.

**Botnet / Bot**: Compromised systems controlled by a Command and Control (C2) server. Used for DDoS, spam campaigns, and credential-stuffing attacks.

**Fileless Malware**: Resides entirely in memory, using legitimate tools (PowerShell, WMI). Leaves no disk artifacts; evades traditional AV.

**Logic Bomb**: Dormant code that triggers on a specific event or date — often planted by a disgruntled insider.

**Exam Trap 4**: The question will describe malware that "spreads automatically across the network without user interaction." That is a worm, not a virus. Viruses need a user to execute them.

### Subsection 3.4 — Vulnerability Concepts

**Vulnerability scanning** is active discovery of known weaknesses. Scanners check systems against a database of CVEs (Common Vulnerabilities and Exposures). They are non-destructive but may cause disruption on fragile systems.

**Penetration testing** goes further — it attempts to exploit discovered vulnerabilities to demonstrate real-world impact. Pen test phases:

1. Planning and reconnaissance
2. Scanning and enumeration
3. Exploitation
4. Post-exploitation (lateral movement, privilege escalation)
5. Reporting

**CVSS (Common Vulnerability Scoring System)**: A standardized 0-10 score quantifying vulnerability severity. Factors include attack vector, complexity, privileges required, user interaction, and impact on confidentiality, integrity, and availability.

**Zero-day vulnerability**: A flaw unknown to the vendor, with no available patch. Extremely valuable to attackers.

**CVE vs. CWE**:

- CVE (Common Vulnerabilities and Exposures): A specific, numbered instance of a vulnerability in a specific product
- CWE (Common Weakness Enumeration): A category of software weaknesses (e.g., CWE-89 = SQL Injection as a class)

### Subsection 3.5 — Attack Frameworks

**MITRE ATT&CK** is a knowledge base of adversary tactics, techniques, and procedures (TTPs) observed in real-world attacks. It is organized into:

- Tactics: The adversary's goal (e.g., Initial Access, Persistence, Lateral Movement, Exfiltration)
- Techniques: How the tactic is achieved (e.g., Spearphishing Attachment under Initial Access)
- Sub-techniques: Granular implementation details

ATT&CK is used by defenders to map observed behaviors to known adversary patterns and identify detection gaps.

**Cyber Kill Chain** (Lockheed Martin) describes the stages of an attack from the attacker's perspective:

1. Reconnaissance
2. Weaponization
3. Delivery
4. Exploitation
5. Installation
6. Command and Control (C2)
7. Actions on Objectives

The key insight: defenders who can interrupt any stage stop the attack. Early-stage disruption (Reconnaissance, Delivery) is more cost-effective than late-stage response (C2, Exfiltration).

**Diamond Model**: Focuses on the relationship between adversary, capability, infrastructure, and victim. Useful for attribution and understanding adversary patterns across multiple incidents.

---

## Section 4 — High-Yield Exam Traps Recap

Let us consolidate the exam traps from both domains before we close Part 1.

**Trap 1**: Two "something you know" factors = single-factor authentication.

**Trap 2**: Encryption → confidentiality. Hashing → integrity. Digital signatures → non-repudiation and integrity.

**Trap 3**: Self-signed certificates are not trusted by external parties — no CA vouches for them.

**Trap 4**: Autonomous network spread = worm. User execution required = virus.

**Trap 5**: Tailgating is unauthorized physical access. The victim does not know. Piggybacking = victim knowingly holds the door.

**Trap 6**: Vulnerability scanning identifies weaknesses. Penetration testing exploits them to confirm impact. Scanning alone does not equal a pen test.

**Trap 7**: A zero-day has no available patch. An unpatched known vulnerability has a patch — the organization just hasn't applied it yet. These are different risk categories.

---

## Section 5 — Domain 1 and 2 Practice Questions

Work through these before watching Part 2. These are exam-style questions patterned after SY0-701 item formats.

**Question 1**: A user at a help desk receives a call from someone claiming to be the CFO who needs an urgent password reset before a board meeting. The caller provides the CFO's employee ID and birth year. Which social engineering technique is being used?

- A) Vishing with pretexting
- B) Spear phishing
- C) Tailgating
- D) Baiting

Answer: A. The attack is delivered by voice (vishing) and uses a fabricated scenario of urgency and authority (pretexting).

**Question 2**: An organization discovers that malware has been running in system memory for three months without leaving files on disk. Security tools did not detect it. Which malware category BEST describes this?

- A) Rootkit
- B) Logic bomb
- C) Fileless malware
- D) Worm

Answer: C. Fileless malware operates entirely in memory and uses legitimate OS tools, avoiding disk artifacts that traditional AV scans.

**Question 3**: Which cryptographic mechanism provides BOTH integrity and non-repudiation?

- A) Symmetric encryption
- B) Hashing
- C) Digital signature
- D) Key exchange

Answer: C. A digital signature hashes the message and encrypts the hash with the sender's private key, providing integrity (hash) and non-repudiation (only the private key owner could have signed it).

**Question 4**: A security analyst notices that a threat actor maintained access to the network for 14 months before detection, slowly exfiltrating intellectual property. Which actor type BEST describes this behavior?

- A) Script kiddie
- B) Hacktivist
- C) Nation-state APT
- D) Insider threat

Answer: C. Long dwell time, low-and-slow exfiltration, and IP theft targeting are hallmarks of an APT campaign.

---

## Closing — Part 1 Summary

You have reviewed the two foundational exam domains. Domain 1 gives you the security vocabulary the exam builds on — AAA, cryptography, and PKI. Domain 2 gives you the threat landscape vocabulary — actor types, social engineering, malware behavior, vulnerability management, and attack frameworks.

In Part 2 we cover the three remaining domains: Architecture (18%), Operations (28%), and Program Management (20%). We also cover exam strategy including PBQ approach, time management, and the elimination technique that can recover correct answers even when you are uncertain.

See you in Part 2.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
