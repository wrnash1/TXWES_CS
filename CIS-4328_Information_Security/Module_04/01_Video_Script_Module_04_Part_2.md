# Video Script: Module 04 — Threats, Attacks, and Vulnerabilities (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Part 2 of Module 04. In Part 1 we built the threat taxonomy. Now we cover defenses, detection strategies, and the Security+ exam traps that trip up even prepared students.

The goal of Part 2 is not just to know what attacks are — it is to know what defenders do about them, and to recognize how the exam questions are written so that you can distinguish the correct answer from a plausible-sounding distractor.

---

### [SECTION 1 — Malware Defenses — 0:45]

Each malware category has a primary defensive control. The exam often asks which control is most appropriate for a given scenario.

#### Ransomware Defenses

The Security+ exam consistently links ransomware to these controls:

- **Immutable, offline backups** — the only reliable recovery path. Cloud-synced backups that the ransomware can also reach do not count. The exam specifically tests this: "online backups" are not sufficient against ransomware.

- **Email filtering and sandboxing** — blocks the most common delivery vector before it reaches endpoints.

- **Endpoint Detection and Response (EDR)** — behavioral detection catches encryption activity in progress, enabling faster containment.

- **Network segmentation** — limits lateral movement; contains the blast radius when an endpoint is compromised.

- **User training** — reduces successful phishing delivery.

**Exam trap**: A question asks "What is the BEST control to recover from ransomware?" The answer is **offline backups**, not antivirus, not EDR. Recovery is the keyword.

#### Rootkit Defenses

- **Secure Boot** — uses a chain of trust from UEFI firmware through the bootloader to the OS kernel; prevents bootkits from loading.

- **TPM attestation** — cryptographically measures the boot sequence and detects unauthorized modifications.

- **Out-of-band scanning** — scanning the drive from a separate, trusted OS (live boot media) bypasses the compromised OS entirely.

- **Reinstallation from known-good media** — the standard remediation when a rootkit is confirmed.

**Exam trap**: "You suspect a rootkit is hiding malware on a system. What should you do to confirm?" The answer is out-of-band scanning or booting from trusted media, NOT running a scan from within the potentially compromised OS.

#### Spyware Defenses

- **Endpoint protection with behavioral analysis** — detects unexpected data exfiltration.

- **Data Loss Prevention (DLP)** — monitors and blocks unauthorized data movement.

- **Mobile Device Management (MDM)** — enforces application allow lists and prevents sideloading on mobile devices.

#### Backdoor and Persistence Defenses

- **Privileged Access Management (PAM)** — limits which accounts can create new privileged accounts or modify system services.

- **File integrity monitoring (FIM)** — detects unauthorized changes to system binaries, scheduled tasks, and registry run keys.

- **Network monitoring** — detects unusual outbound connections that indicate command-and-control (C2) communication.

---

### [SECTION 2 — Anti-Phishing Controls — 4:30]

Technical controls for phishing operate at multiple layers.

#### Email Authentication Protocols

Three protocols work together to validate email sender identity:

- **SPF (Sender Policy Framework)** — a DNS TXT record listing IP addresses authorized to send email for a domain. Receiving mail servers check SPF to verify the sending IP.

- **DKIM (DomainKeys Identified Mail)** — the sending server signs outgoing email with a private key. Receivers verify the signature using a public key published in DNS. Proves the email has not been tampered with in transit.

- **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** — uses SPF and DKIM results to decide what to do with failing emails: none (monitor only), quarantine, or reject. Also generates aggregate reports.

**Exam order**: SPF → DKIM → DMARC. DMARC depends on SPF and DKIM. If a question asks which protocol provides the enforcement policy, the answer is DMARC.

#### User Awareness Training

Technical controls stop the emails they recognize. User training stops the ones that get through. Security+ treats user awareness as a **complementary control**, not a replacement for technical controls.

**Simulated phishing campaigns** — sending test phishing emails to employees and tracking click rates — are the standard method for measuring and improving awareness over time.

---

### [SECTION 3 — Social Engineering Defenses — 7:00]

#### Verification Procedures

Every social engineering attack depends on the target skipping verification. Defenses include:

- **Callback verification** — hang up and call the requester back on a number from the official directory.

- **Out-of-band confirmation** — use a second communication channel (e.g., confirm a phone request via email to a known address).

- **Identity verification policies** — documented procedures employees follow before granting access or releasing information, regardless of how authoritative the requester sounds.

#### Physical Security Controls

Against tailgating and piggybacking:

- **Mantraps (airlock vestibules)** — two doors where the first must close before the second opens; prevents following.

- **Security guards** — human verification of identity before entry.

- **Badge policies** — visible ID requirements, challenge culture (employees are expected to question anyone without a visible badge).

---

### [SECTION 4 — Supply Chain Risk Management — 8:30]

#### Vendor Risk Assessment

Before onboarding a vendor, organizations assess their security posture through:

- Security questionnaires and audits.

- Review of certifications (SOC 2 Type II, ISO 27001).

- Penetration test report reviews.

#### Contractual Controls

- **Right-to-audit clauses** — contractual right to audit the vendor's security practices.

- **Minimum security requirements** — SLAs specifying security standards the vendor must maintain.

#### Software Bill of Materials (SBOM)

An SBOM is a formal inventory of all components in a software product — including open-source libraries and their versions. When a new vulnerability like Log4Shell is discovered, an organization with SBOMs can immediately identify which of their products are affected.

**Exam point**: SBOMs are a direct mitigation for open-source dependency supply chain attacks. Security+ SY0-701 explicitly includes SBOM awareness.

#### Code Integrity Verification

- **Signed software updates** — necessary but not sufficient (as SolarWinds showed).

- **Build environment security** — the SolarWinds lesson is that the build pipeline itself must be hardened and monitored.

---

### [SECTION 5 — Vulnerability Management — 10:00]

#### CVE and CVSS

Every publicly disclosed vulnerability receives a **CVE (Common Vulnerabilities and Exposures)** identifier — a unique reference number like CVE-2021-44228 (Log4Shell).

The **CVSS (Common Vulnerability Scoring System)** provides a numerical severity score from 0 to 10:

- 0.1–3.9: Low

- 4.0–6.9: Medium

- 7.0–8.9: High

- 9.0–10.0: Critical

**Exam point**: CVSS scores inform prioritization but do not replace contextual risk assessment. A Critical CVSS score on a system with no network exposure may be lower priority than a Medium score on an internet-facing system.

#### Patch Management Cadence

- **Emergency patching** — for actively exploited vulnerabilities (zero-days once a patch is available, or Critical/High CVSS scores with known exploitation).

- **Regular patch cycles** — scheduled monthly or quarterly maintenance windows for lower-severity patches.

- **Compensating controls** — when patching is not immediately possible (legacy systems, uptime requirements), apply network controls, IDS signatures, or WAF rules to reduce exposure.

---

### [SECTION 6 — EXAM TRAPS AND QUESTION ANALYSIS — 12:00]

Let's work through the specific ways Security+ question writers test this domain.

#### Trap 1: Malware Type by Propagation

Question stem: "A piece of malware has infected multiple systems across a network. No user interaction was involved in spreading it."

Wrong answers: virus, trojan.

Correct answer: **worm** — self-propagating, no user action required.

The distractor is "virus" because viruses are the most familiar term, but viruses require a host file and user action.

#### Trap 2: Phishing Scope

Question stem: "An attacker researches a specific VP of Finance and sends a carefully crafted email referencing her current projects."

Wrong answer: phishing (too generic).

Correct answer: **spear phishing**. The targeting and research distinguish it. If the target were a C-level executive, whaling would also be correct — but the VP title makes spear phishing the better answer unless the question says C-suite.

#### Trap 3: Rootkit Detection

Question stem: "A security analyst suspects a rootkit is installed but scans from within the OS return clean results."

Wrong answer: run the scan again with updated definitions.

Correct answer: **boot from trusted media and scan offline**. The compromised OS cannot be trusted to report accurately.

#### Trap 4: Supply Chain vs. Zero-Day

Question stem: "An attacker inserted malicious code into a software update that was cryptographically signed by the vendor."

Wrong answers: zero-day exploit, man-in-the-middle attack.

Correct answer: **supply chain attack**. The signing happened after the insertion. The attacker compromised the build process, not a vulnerability in the product itself.

#### Trap 5: Pharming vs. Phishing

Question stem: "A user visits a bank website by typing the URL correctly and still lands on a fraudulent site."

Wrong answer: phishing (requires a malicious link the user clicks).

Correct answer: **pharming** (DNS cache poisoning or hosts file modification redirected the legitimate request).

#### Trap 6: Best Recovery Control for Ransomware

Question stem: "What is the MOST effective control for recovering from a ransomware attack?"

Wrong answers: antivirus, EDR, user training.

Correct answer: **offline backups**. The question says "recovering from," not "preventing." Recovery requires clean data. The other options help prevent or detect but do not provide recovery capability.

---

### [OUTRO — 15:00]

You now have both the knowledge and the exam strategy for Module 04.

Key review points:

- Match malware types to their **propagation mechanism**.

- Distinguish phishing variants by **scope** (mass vs. targeted vs. executive vs. voice vs. SMS vs. redirect).

- Recognize social engineering by the **psychological lever** (authority, urgency, curiosity, reciprocity).

- Supply chain attacks compromise the **trusted distribution channel**, not the end product directly.

- Zero-days have **no patch at time of exploitation**.

- IoCs are the **signals** that trigger investigation.

Complete the Module 04 quiz and lab before moving to Module 05, where we cover cryptography — the technical foundation that underlies most of the defenses we just discussed.

---

*End of Part 2 — Module 04*
