# Reading Guide: Module 04 — Threats, Attacks, and Vulnerabilities

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports Module 04 of CIS-4328. It covers the full threat and attack taxonomy tested on the Security+ exam, with emphasis on malware categories, phishing variants, social engineering techniques, supply chain risk, zero-day exploits, and indicators of compromise.

All readings in this course use zero-cost, openly licensed resources.

---

## Learning Objectives

By the end of this module, you will be able to:

- Classify malware by mechanism, propagation method, and primary goal.

- Distinguish phishing variants by scope, target, and delivery channel.

- Identify social engineering attacks by the psychological trigger exploited.

- Explain supply chain attack vectors at hardware, software, and vendor levels.

- Define zero-day exploits and describe their relationship to vulnerability management.

- Recognize common indicators of compromise across network, host, file, and behavioral categories.

---

## Primary Reading: NIST and CISA Resources

### Reading 1 — NIST SP 800-83 Rev. 1: Guide to Malware Incident Prevention and Handling

Source: [https://csrc.nist.gov/publications/detail/sp/800-83/rev-1/final](https://csrc.nist.gov/publications/detail/sp/800-83/rev-1/final)

Read: Executive Summary and Section 2 (Malware Categories and Characteristics).

Focus areas:

- The distinction between viruses, worms, and trojans.

- How rootkits subvert OS reporting mechanisms.

- The relationship between backdoors and persistence.

### Reading 2 — CISA Phishing Guidance

Source: [https://www.cisa.gov/topics/cybersecurity-best-practices/phishing](https://www.cisa.gov/topics/cybersecurity-best-practices/phishing)

Read: All sections.

Focus areas:

- How spear phishing differs from bulk phishing in targeting methodology.

- The role of OSINT in phishing attack preparation.

- Technical email authentication controls: SPF, DKIM, DMARC.

### Reading 3 — CISA Supply Chain Risk Management

Source: [https://www.cisa.gov/supply-chain](https://www.cisa.gov/supply-chain)

Read: Overview and Key Practices sections.

Focus areas:

- How the SolarWinds attack succeeded despite signed software.

- The concept of a Software Bill of Materials (SBOM).

- Vendor risk assessment as a risk management control.

---

## Supplemental Reading: MITRE ATT&CK Framework

### Reading 4 — MITRE ATT&CK Tactics Overview

Source: [https://attack.mitre.org/tactics/enterprise/](https://attack.mitre.org/tactics/enterprise/)

Read: Initial Access, Execution, and Persistence tactic pages.

Focus areas:

- Specific techniques used for initial access (phishing, supply chain compromise).

- Persistence techniques including scheduled tasks, registry run keys, and backdoor installation.

- How ATT&CK technique IDs (e.g., T1566 for Phishing) appear in threat intelligence reports.

This framework is increasingly referenced on the Security+ exam and in industry job roles. Familiarity with the tactic structure — not memorization of individual technique IDs — is the goal.

---

## Concept Reference Tables

### Table 1 — Malware Classification

| Type | Primary Mechanism | Propagation | Primary Goal |
|---|---|---|---|
| Virus | Attaches to legitimate file | Requires user action | Damage or theft |
| Worm | Self-contained executable | Network self-propagation | Spread and payload delivery |
| Trojan | Disguised as legitimate software | Social engineering | Remote access or theft |
| Ransomware | Encrypts files or locks system | Usually phishing or RDP | Financial extortion |
| Spyware | Silent data collection | Bundled software or exploit | Intelligence gathering |
| Rootkit | Hides its own presence | Via other malware | Persistence and concealment |
| Backdoor | Bypasses authentication | Installed post-compromise | Re-entry and persistence |
| RAT | Full remote control | Trojan delivery | Command and control |

### Table 2 — Phishing Variant Comparison

| Variant | Target Scope | Delivery Channel | Key Characteristic |
|---|---|---|---|
| Phishing | Mass/broad | Email | Volume-based; generic lures |
| Spear Phishing | Specific individual or group | Email | Personalized; OSINT-driven |
| Whaling | C-suite executives | Email | High-value target; BEC risk |
| Vishing | Individuals | Voice/phone | Authority and urgency |
| Smishing | Individuals | SMS | Mobile-optimized lures |
| Pharming | Any web user | DNS/hosts redirect | No user click required |

### Table 3 — Social Engineering Techniques

| Technique | Mechanism | Key Psychological Trigger |
|---|---|---|
| Pretexting | Fabricated identity/scenario | Trust and authority |
| Baiting | Physical or digital lure | Curiosity |
| Quid pro quo | Offer of help in exchange | Reciprocity |
| Tailgating | Physical follow-through | Social pressure |
| Piggybacking | Authorized person complicit | Social compliance |

---

## Key Terms and Definitions

**Threat** — Any potential danger to information systems or data.

**Vulnerability** — A weakness in a system, process, or control that can be exploited.

**Attack** — The act of exploiting a vulnerability to cause harm.

**Malware** — Malicious software designed to damage, disrupt, or gain unauthorized access to a system.

**Ransomware** — Malware that encrypts data or locks a system and demands payment for restoration.

**Rootkit** — Malware designed to conceal its presence from the operating system and security tools.

**Backdoor** — An undocumented or hidden method for bypassing normal authentication.

**Spear Phishing** — Targeted phishing attack using personalized information gathered through research.

**Whaling** — Spear phishing directed at senior executives.

**Vishing** — Voice-based phishing conducted over telephone.

**Pharming** — Redirection of legitimate website traffic to a fraudulent site via DNS or hosts file manipulation.

**Social Engineering** — Psychological manipulation of individuals to gain unauthorized access or information.

**Supply Chain Attack** — Compromise of a target through a trusted vendor, library, or hardware component.

**Zero-Day Exploit** — Exploitation of a vulnerability for which no patch yet exists.

**Indicator of Compromise (IoC)** — Forensic evidence suggesting a system has been or is being compromised.

**CVE** — Common Vulnerabilities and Exposures; a standardized identifier for publicly disclosed vulnerabilities.

**CVSS** — Common Vulnerability Scoring System; a numerical severity score from 0 to 10.

**SBOM** — Software Bill of Materials; an inventory of all components in a software product.

**SPF** — Sender Policy Framework; a DNS record specifying authorized email sending IP addresses.

**DKIM** — DomainKeys Identified Mail; cryptographic signature on outbound email.

**DMARC** — Domain-based Message Authentication, Reporting, and Conformance; enforcement policy combining SPF and DKIM.

**Living-off-the-Land (LOLBin)** — Using legitimate, pre-installed system tools for malicious purposes to evade detection.

**RaaS** — Ransomware-as-a-Service; a criminal business model leasing ransomware capabilities to affiliates.

---

## Security+ Exam Alignment

The following SY0-701 exam objectives are covered in this module:

- 2.1 — Compare and contrast common threat actors, motivations, and attack vectors.

- 2.2 — Explain common threat vectors and attack surfaces.

- 2.3 — Explain various types of vulnerabilities.

- 2.4 — Given a scenario, analyze indicators of malicious activity.

- 2.5 — Explain the purpose of mitigation techniques used to secure the enterprise.

---

## Critical Thinking Questions

Work through these questions after completing the readings. They are designed to prepare you for Security+ scenario questions, not just factual recall.

1. An employee reports that their computer is running slowly and making unexpected network connections late at night. What types of malware could produce this behavior? What initial investigation steps would you take?

2. A company's email gateway blocked a phishing attempt, but a near-identical email sent to the CEO's personal email address — which the CEO sometimes uses for work — was not blocked. What attack category does this represent? What controls would address the gap?

3. After a vendor releases a signed software update, incident responders discover that malware was present in the update package. The software's code signing certificate was valid. What type of attack occurred? What control could reduce the risk of this attack in the future?

4. A user navigates to their bank's website by typing the URL directly and is presented with a fake login page. Their browser shows the correct URL in the address bar. What attack technique is most likely responsible? What technical control would prevent it?

5. A security team discovers that an attacker has been present on the network for three weeks but has not yet triggered any antivirus alerts. The attacker has created a new local administrator account and modified a Windows scheduled task. Classify what the attacker has done using appropriate terminology. What IoCs should the team look for?

---

## Review Checklist

Before moving to the Module 04 quiz and lab, verify you can do each of the following without notes:

- Name all malware types in Table 1 and describe the primary mechanism of each.

- Distinguish spear phishing from whaling and explain how the exam tests this distinction.

- Explain why pharming is different from phishing in a way that would satisfy a Security+ question.

- Describe three IoC categories and give one example from each.

- Explain the SolarWinds attack in two sentences and identify it as a supply chain attack.

- Define zero-day and explain what happens to the classification once a patch is released.

- State the purpose of SPF, DKIM, and DMARC individually, then explain how they work together.

---

Module 04 Reading Guide — End
