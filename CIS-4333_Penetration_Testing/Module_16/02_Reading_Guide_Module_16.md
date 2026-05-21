# Reading Guide: Module 16 - Final Exam Prep & CompTIA PenTest+ PT0-002 Certification
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 16 - Final Exam Prep & CompTIA PenTest+ PT0-002 Certification**! This final module brings together everything covered across the course into a structured review of all five PT0-002 exam domains. The CompTIA PenTest+ PT0-002 exam consists of up to 85 questions — a mix of multiple-choice and performance-based questions — with a passing score of 750 out of 900. Candidates have 165 minutes to complete the exam.

This module is your opportunity to consolidate knowledge gaps, reinforce high-yield concepts, and build the exam-day confidence that comes from having systematically worked through all domain content. Use this guide to identify which domains and techniques need additional review before scheduling your certification exam.

---

### 1. High-Yield Glossary – Cross-Domain Review
Review these essential concepts carefully. These represent the highest-frequency PT0-002 exam topics across all five domains:

*   **PT0-002 Domain Weights (Memorize These)**: Planning & Scoping **14%**, Information Gathering & Vulnerability Scanning **22%**, Attacks & Exploits **30%**, Reporting & Communication **18%**, Tools & Code Analysis **16%**. The largest domain — Attacks & Exploits — covers exploitation, post-exploitation, privilege escalation, lateral movement, social engineering, wireless attacks, web application attacks, and cloud/container attacks. Reporting is the second-most-commonly underestimated domain.

*   **Pentest Methodology Sequence**: The PT0-002 exam tests the correct order of phases: (1) Planning & Scoping — define scope, RoE, legal authorization; (2) Information Gathering — OSINT, passive recon, active scanning; (3) Vulnerability Scanning — Nessus/OpenVAS, CVSS scoring, false positive analysis; (4) Exploitation — Metasploit, payloads, reverse shells; (5) Post-Exploitation — privilege escalation, lateral movement, persistence, credential harvesting; (6) Reporting — findings documentation, CVSS severity, executive summary, remediation recommendations, cleanup. Know the sequence — PT0-002 presents out-of-order scenarios as exam traps.

*   **Key Tools by Domain**: Information Gathering: `theHarvester`, `maltego`, `recon-ng`, `nmap`, `dig`, `whois`, Shodan. Vulnerability Scanning: Nessus, OpenVAS. Exploitation: Metasploit (`msfconsole`, `msfvenom`), Burp Suite, `sqlmap`, SET. Post-Exploitation: Mimikatz, Impacket suite (`psexec.py`, `GetUserSPNs.py`), BloodHound, LinPEAS/WinPEAS, `aircrack-ng` suite. Password Attacks: Hashcat, John the Ripper, Hydra. Reporting: CVSS calculator, documentation tools.

*   **Legal and Authorization Framework**: PT0-002 exam scenarios frequently test authorization requirements. Key documents: Authorization/Permission Letter (the "get-out-of-jail card"), Rules of Engagement (RoE — what is in scope and permitted), Master Service Agreement (MSA — overarching business relationship), Non-Disclosure Agreement (NDA — confidentiality), Statement of Work (SOW — specific deliverables and timeline). Cloud testing additionally requires compliance with the cloud provider's penetration testing policy (AWS, Azure, GCP each have separate policies).

*   **CVSS v3.1 Severity Ranges and Common Exam Traps**: Critical 9.0–10.0, High 7.0–8.9, Medium 4.0–6.9, Low 0.1–3.9. A remotely exploitable, unauthenticated vulnerability with full system impact = Critical. Exam traps include: confusing false positives with false negatives, confusing LHOST with RHOSTS, mixing up bind vs. reverse shells, treating encoding as reliable AV bypass, and applying WPS attacks to WPA2-Enterprise networks.

---

### 2. Certification Exam Tips
*   **Exam Format:** Up to 85 questions, 165 minutes, passing score 750/900 (on a scaled 100–900 range). Performance-based questions (PBQs) appear at the beginning — they simulate real tools and scenarios. Do not spend too much time on PBQs during the exam; flag them and return after completing multiple-choice questions.
*   **Highest-Frequency Attack Techniques:** SQLi, XSS, Kerberoasting, Pass-the-Hash, SUID binary abuse, WPA2 handshake capture, spear phishing, SSRF → IMDS cloud attack chain, and AV evasion (especially LoTL and behavioral vs. signature detection distinctions).
*   **Reporting Domain is High-Value:** Candidates who study only attack techniques leave 18% of exam weight uncovered. Review: executive summary vs. technical findings audience distinction, CVSS scoring rationale, risk acceptance documentation, and post-engagement cleanup attestation.
*   **Tools & Code Analysis (16%):** PT0-002 expects you to read simple scripts and identify what they do. Review: bash one-liners for enumeration, Python socket code, PowerShell execution policy bypass, and identifying malicious script patterns (reverse shell callbacks, file downloads via LOLBins).
*   **Exam Trap — Scope and Authorization:** Any scenario where a tester acts outside the agreed scope, skips authorization steps, or tests cloud/third-party systems without provider consent is incorrect — regardless of technical justification. Authorization and RoE compliance questions always have one clearly correct ethical answer.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — This browser-based, guided learning path covers all PT0-002 domains with hands-on rooms for every major topic. Completing the full path provides practical reinforcement of every concept tested on the exam. No local VM or special hardware required — all labs run in the browser.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — This free, full-length YouTube course maps directly to all five PT0-002 domains. Use it as a comprehensive final review resource — watch at 1.25–1.5x speed and pause to test yourself on each concept before moving forward.

---

### Required Readings & Videos
To prepare for this module's exam review, you must complete the following:
*   **Required Reading:** Complete any remaining rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) that correspond to domains where you feel least confident — particularly Reporting & Communication and Tools & Code Analysis, which are commonly under-practiced. TryHackMe is a browser-based cybersecurity training platform — all practice is hands-on and maps directly to PT0-002 objectives.
*   **Required Video:** Watch the full [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) as a complete final review. This free YouTube course covers every PT0-002 domain in sequence. Use it alongside your course notes to reinforce concepts and identify any remaining knowledge gaps before the certification exam.

---

### Lab & Command Integration
In this final module's review activity, you will perform the following consolidation steps:
*   **Domain self-assessment**: For each of the five PT0-002 domains, write a 2–3 sentence summary of the most important concepts, tools, and exam traps — without referring to your notes. Then compare against your notes to identify gaps. Repeat for any domain where your self-assessment was incomplete.
*   **Command-line review**: Without looking up syntax, write the correct command for each of the following: (1) Nmap SYN scan with version detection and OS detection; (2) Hashcat NTLM dictionary attack; (3) airmon-ng enabling monitor mode; (4) msfvenom reverse TCP Meterpreter payload for Windows; (5) find all SUID binaries on a Linux system. Verify your answers against module notes.
*   **Practice exam**: Complete a full-length PT0-002 practice exam (available through CompTIA's CertMaster Practice or third-party providers) under timed conditions — 85 questions in 165 minutes. Review every missed question against the specific module content where that topic was covered.

---

### 3. Study Checklist
- [ ] Review all five PT0-002 domain weights and confirm you can describe the top 3 exam topics in each domain.
- [ ] Complete remaining TryHackMe rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) for any under-studied domains.
- [ ] Watch the complete [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) as a final review.
- [ ] Complete a full-length timed practice exam and review all missed questions.
- [ ] Schedule your PT0-002 certification exam through CompTIA's exam registration portal.
