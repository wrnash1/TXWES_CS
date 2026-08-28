# Video Script — Module 01, Part 1: Threats, Attacks, and Vulnerabilities (Theory)

## CIS-4328 Information Security | Texas Wesleyan University

### Instructor: Professor Nash | CompTIA Security+ SY0-701 Alignment

### Estimated Duration: 13 minutes

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 01 | Texas Wesleyan University"]**

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome to CIS-4328 Information Security. I'm Professor Nash, and this is Module 01 — Threats, Attacks, and Vulnerabilities.

This module is the front door of the entire CompTIA Security+ exam. The SY0-701 blueprint places threats, vulnerabilities, and mitigations in Domain 2, which carries 22 percent of the total exam weight. That means roughly one in five questions you will see on test day traces back directly to what we cover right here, right now.

Before we can defend anything, we have to understand what we are defending against. That means learning the vocabulary of attack — threat actors, vulnerability classes, attack categories, and the foundational security model that ties everything together. Let's get into it.

---

## Section 1 — The CIA Triad

**[SHOW DIAGRAM: Triangle with three labeled vertices — Confidentiality (top), Integrity (bottom-left), Availability (bottom-right). Center label reads "CIA Triad — Foundation of Information Security." Below each vertex: Confidentiality = Encryption; Integrity = Hashing; Availability = Redundancy.]**

**[Alt-text: An equilateral triangle. The top vertex is labeled Confidentiality. The bottom-left vertex is labeled Integrity. The bottom-right vertex is labeled Availability. The center reads CIA Triad. Below each vertex is a one-line control example.]**

Every security control ever designed — every firewall rule, every password policy, every backup procedure — exists to protect one or more of three properties. We call them the CIA Triad.

**Confidentiality** means data is accessible only to authorized parties. If an unauthorized person reads your data, confidentiality has been violated. The primary technical control for confidentiality is encryption. When data is encrypted, only someone with the correct key can read it.

**Integrity** means data is accurate and has not been altered without authorization. If an attacker modifies a file and you cannot detect the change, integrity has been violated. The primary technical control for integrity is hashing. A hash function produces a fixed-length fingerprint of a file. If even one byte changes, the hash changes — and the mismatch reveals the tampering.

**Availability** means systems and data are accessible when authorized users need them. A denial-of-service attack targets availability. The primary technical controls for availability are redundancy, failover clustering, and backups.

There is a fourth concept that extends the triad: **Non-repudiation**. Non-repudiation means a user cannot credibly deny having performed an action. If you digitally sign an email, the signature proves you sent it. You cannot come back later and say "That wasn't me." Non-repudiation is enforced by digital signatures and audit logs.

**Exam Tip:** Every Security+ scenario question about a security control will ask which CIA triad property it protects. Map every control to one or more of these three properties before selecting your answer.

---

## Section 2 — Security Controls Framework

**[SHOW DIAGRAM: Two-axis grid. Horizontal axis shows three Control Categories: Physical, Technical/Logical, Administrative/Managerial. Vertical axis shows six Control Functions: Preventive, Detective, Corrective, Deterrent, Compensating, Directive. Representative examples appear in each cell.]**

**[Alt-text: A six-by-three grid titled Security Controls Framework. Columns are Physical, Technical, Administrative. Rows are Preventive, Detective, Corrective, Deterrent, Compensating, Directive. Sample cell values: Physical/Preventive = Mantrap; Technical/Preventive = Firewall; Administrative/Preventive = Acceptable Use Policy; Physical/Detective = Security Camera; Technical/Detective = IDS/SIEM; Administrative/Detective = Security Audit; Technical/Corrective = Backup Restore; Physical/Deterrent = Warning Signs; Technical/Compensating = Encryption when patching is delayed.]**

Security controls are categorized along two dimensions: what they are made of, and what function they perform.

The three categories by composition:

- **Physical controls** are tangible barriers you can touch. Fences, locks, mantraps, security guards, and security cameras are physical controls.
- **Technical controls** — also called Logical controls — use software, hardware, or firmware to enforce policy. Firewalls, encryption, access control lists, multi-factor authentication, and intrusion detection systems are technical controls.
- **Administrative controls** — also called Managerial controls — are policies, procedures, and processes that govern human behavior. Acceptable Use Policies, security awareness training, background checks, and risk assessments are administrative controls.

The six control functions:

- **Preventive** — stops an attack before it succeeds. A firewall blocking inbound traffic is preventive.
- **Detective** — identifies an attack in progress or one that has already occurred. An IDS alert is detective.
- **Corrective** — restores the system to a secure state after an incident. Restoring from backup is corrective.
- **Deterrent** — discourages attackers without physically stopping them. A "Premises Monitored by Security Cameras" sign is deterrent.
- **Compensating** — a substitute control used when the primary control cannot be implemented. If a legacy system cannot support MFA, encrypting its data segment may serve as a compensating control.
- **Directive** — provides guidance or instructions on correct behavior. Mandatory annual security awareness training is directive.

**Exam Tip:** The SY0-701 exam frequently presents a scenario and asks you to classify the control shown. Know all three categories and all six functions and practice mapping examples to both axes simultaneously.

---

## Section 3 — Threat Actors and Their Attributes

**[SHOW DIAGRAM: Table with five columns — Threat Actor Type, Motivation, Technical Sophistication, Resources, Typical Attack Vector. Five rows: Nation-State, Organized Crime, Hacktivist, Insider Threat, Script Kiddie.]**

**[Alt-text: A five-column comparison table titled Threat Actor Attributes. Row 1: Nation-State — Espionage and Disruption, Advanced, Nation-level funding, Zero-days and supply chain. Row 2: Organized Crime — Financial gain, High, Well-funded networks, Ransomware and banking trojans. Row 3: Hacktivist — Ideology, Moderate, Crowdsourced, Website defacement and DDoS. Row 4: Insider Threat — Revenge or financial or accidental, Varies, Authorized access, Data exfiltration and sabotage. Row 5: Script Kiddie — Notoriety, Low, Minimal, Pre-built exploit tools.]**

A **threat actor** is any individual, group, or entity that poses a potential danger to an organization's information systems. The SY0-701 exam expects you to identify threat actors by their attributes — motivation, sophistication, and resources — because those attributes determine the nature of the attack.

**Nation-State Actors** are government-sponsored groups with substantial funding, advanced technical capabilities, and long-term strategic objectives. They pursue espionage, intellectual property theft, and critical infrastructure disruption. Their attacks are characterized by patient reconnaissance, custom malware, and zero-day exploits. The term Advanced Persistent Threat — APT — is closely associated with nation-state actors, though it technically applies to any sophisticated, long-duration campaign.

**Organized Crime Groups** are financially motivated and operate like businesses. Modern ransomware operations are often run by organized crime syndicates. They have significant resources and use commercially available exploit kits alongside custom tools.

**Hacktivists** are motivated by ideology, political causes, or social justice. They may deface websites, leak documents, or launch denial-of-service attacks. Sophistication varies from volunteers with basic skills to expert contributors.

**Insider Threats** are dangerous because they already have authorized access. An insider might be a disgruntled employee seeking revenge, a careless employee who accidentally exposes data, or a contractor covertly exfiltrating trade secrets. Detecting insiders requires behavioral analytics and anomaly detection rather than perimeter defenses.

**Script Kiddies** are low-skill actors who use pre-built tools and exploit frameworks without deep technical understanding. Their attacks are opportunistic and rely on known, unpatched vulnerabilities. They are dangerous in volume — automated scanning tools allow a single script kiddie to probe millions of targets.

---

## Section 4 — Vulnerability Classes

**[SHOW DIAGRAM: Hierarchy chart titled Vulnerability Classes. Top node: Vulnerability. Four child nodes: Software Flaw, Misconfiguration, Weak Credential, Missing Patch. Each child has two sub-nodes with examples.]**

**[Alt-text: A hierarchy diagram. Root node: Vulnerability. Four branches: Software Flaw — sub-nodes Buffer Overflow and Race Condition; Misconfiguration — sub-nodes Default Credentials and Open Ports; Weak Credential — sub-node Password Reuse; Missing Patch — sub-node Publicly Known CVE.]**

A **vulnerability** is a weakness in a system, application, or process that a threat actor can exploit to cause harm. Three terms must be held distinct:

- A **vulnerability** is the weakness itself.
- A **threat** is the actor or event that could exploit the vulnerability.
- **Risk** is the likelihood that the threat will exploit the vulnerability multiplied by the potential impact if it does.

Common vulnerability classes:

**Software Flaws** — coding errors such as buffer overflows, where data is written past the end of an allocated memory buffer and can overwrite adjacent memory to allow code execution. Race conditions are timing-based flaws where an attacker manipulates the sequence of operations to alter program behavior.

**Misconfigurations** — services left on default settings, unnecessary ports left open, default vendor credentials never changed. Misconfigurations account for a large proportion of real-world breaches.

**Weak or Default Credentials** — vendor-default passwords, simple passwords, or reusing the same password across multiple systems.

**Missing Patches** — failure to apply vendor-released security updates. Once a CVE entry is published, attackers have a documented recipe for exploitation.

**Zero-Day Vulnerabilities** — vulnerabilities unknown to the vendor with no available patch. Because no signature exists for a zero-day, defenses must rely on behavioral analysis and endpoint detection and response tools.

---

## Section 5 — Active vs. Passive Attacks

**[SHOW DIAGRAM: Two-column comparison table. Left column header: Passive Attacks. Right column header: Active Attacks. A vertical dividing line is labeled with the question: "Does the attack modify data?" Left = No. Right = Yes.]**

**[Alt-text: Two-column table. Left column: Passive Attacks — Eavesdropping captures traffic without modification; Traffic Analysis infers information from patterns; Shoulder Surfing observes input visually. Right column: Active Attacks — Replay retransmits captured valid packets; Injection inserts malicious content into a data stream; Man-in-the-Middle intercepts and modifies communication; Denial of Service overwhelms resources to deny access.]**

The SY0-701 exam distinguishes between passive and active attacks.

**Passive attacks** observe or collect information without modifying the data stream. They are difficult to detect because they leave no trace of alteration. Examples include network packet sniffing, traffic analysis, and shoulder surfing. The primary defense against passive attacks is encryption — if data is unreadable, capturing it yields no useful intelligence.

**Active attacks** modify, inject, or disrupt data. They include:

- **Replay attacks** — an attacker captures a legitimate authentication token and retransmits it later to gain unauthorized access. Defense: timestamps and session tokens that expire.
- **Injection attacks** — an attacker inserts malicious content into an input field or data stream. SQL injection is the classic example. Defense: input validation and parameterized queries.
- **Man-in-the-Middle attacks** — an attacker secretly intercepts communication between two parties and can read, modify, or inject messages. Defense: end-to-end encryption and certificate validation.
- **Denial-of-Service attacks** — an attacker overwhelms a target's resources, denying service to legitimate users. Defense: rate limiting, DDoS mitigation services, and redundancy.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

In Part 1 we covered the CIA Triad and non-repudiation, the security controls framework with three categories and six functions, the five major threat actor types and their distinguishing attributes, common vulnerability classes, and the distinction between passive and active attacks.

In Part 2, we will apply these concepts to real exam scenarios, walk through attack surface analysis, and cover exam-day strategy for Module 01 questions.

For additional study, visit **professormesser.com** — Professor Messer's free SY0-701 course is one of the best resources available for this exam. See you in Part 2.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 01 Part 1

Proprietary and Confidential. Not for disclosure outside of authorized course use.
