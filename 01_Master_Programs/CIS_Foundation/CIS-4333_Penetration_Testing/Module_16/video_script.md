# Video Script: Module 16 — PenTest+ PT0-002 Exam Preparation and Capstone

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 30–35 minutes
- **Segments:** 7
- **Visual Aids:** PT0-002 domain breakdown pie chart, tool mapping tables, exam strategy slides, PBQ walkthrough diagram
- **Lab Environment:** Capstone written assessment — no live systems

---

## Segment 1: Course Retrospective and Exam Overview (Lines 1–35)

[SLIDE: Module 16 Title Card]

Welcome to Module 16 — the final module of CIS-4333 Penetration Testing. This module serves two purposes: comprehensive review of all course material aligned to PT0-002 exam domains, and the capstone assessment that synthesizes everything you have learned.

Let me start with a moment of appreciation. Over sixteen modules, you have covered the complete penetration testing discipline: planning and authorization, reconnaissance and OSINT, vulnerability scanning, exploitation, post-exploitation, privilege escalation, wireless attacks, social engineering, physical security, report writing, legal considerations, and specialized environments. That is a significant body of knowledge.

[SLIDE: PT0-002 Exam Overview]

The CompTIA PenTest+ PT0-002 exam:

- Format: Maximum 85 questions
- Types: Multiple choice and performance-based questions (PBQs)
- Duration: 165 minutes
- Passing score: 750 on a scale of 100–900
- Languages: English, Japanese
- Cost: $392 (check CompTIA's website for current pricing)
- Recommended experience: 3–4 years of hands-on information security experience

[SLIDE: PT0-002 Domain Weights]

The exam covers five domains:

Domain 1 — Planning and Scoping: 14%

Domain 2 — Information Gathering and Vulnerability Scanning: 22%

Domain 3 — Attacks and Exploits: 30%

Domain 4 — Reporting and Communication: 16%

Domain 5 — Tools and Code Analysis: 18%

Domain 3 (Attacks) is the heaviest weight at 30%. But notice that Domains 2 and 5 together account for 40% — reconnaissance, scanning, and tool knowledge are heavily tested.

[PAUSE for transition]

---

## Segment 2: Domain 1 Review — Planning and Scoping (Lines 36–65)

[SLIDE: Domain 1 Key Topics]

Domain 1 covers 14% of the exam. Topics:

Governance, risk, and compliance: Industry frameworks (NIST, ISO 27001, PCI DSS, HIPAA), regulatory requirements by sector, risk management concepts.

Scope and organizational requirements: Defining in-scope systems, understanding third-party authorization requirements, cloud provider testing policies, technical and environmental constraints.

Ethical hacking mindset: Maintaining professional integrity, staying within scope, communicating findings professionally, responsible disclosure.

[SLIDE: Domain 1 Must-Know Items]

For Domain 1, know specifically:

The components of a Scope of Work: parties, scope definition, testing period, authorization statement, deliverables.

The Rules of Engagement document and what it contains.

Why the get-out-of-jail letter is carried during physical testing.

The CFAA "exceeds authorized access" provision.

The difference between bug bounty, responsible disclosure, and contracted testing.

Regulatory requirements: HIPAA (PHI), PCI DSS (cardholder data), FERPA (student records), GLBA (financial information).

[SLIDE: Domain 1 Scenario Pattern]

Typical Domain 1 exam question pattern: "A tester is asked to test a web application. During testing, they discover the application communicates with a third-party payment processor. What must the tester do?" Answer: Stop testing the third-party system, document the finding, recommend the client obtain authorization from the processor.

[PAUSE for transition]

---

## Segment 3: Domain 2 Review — Recon and Vulnerability Scanning (Lines 66–100)

[SLIDE: Domain 2 Key Topics]

Domain 2 accounts for 22% of the exam. Topics:

Passive reconnaissance: OSINT techniques, source categories (WHOIS, DNS, certificate transparency, LinkedIn, Shodan).

Active reconnaissance: DNS enumeration, port scanning, service fingerprinting, web application crawling.

Vulnerability scanning: Scanner types (network, web, authenticated vs. unauthenticated), interpreting results, tool knowledge.

[SLIDE: Passive Recon — Key Sources]

For passive reconnaissance, know these sources:

WHOIS: Domain registration information including registrant, creation date, name servers.

DNS records: A, AAAA, MX, TXT, NS, SOA, CNAME, SRV. DNS zone transfer (AXFR) if misconfigured.

Certificate Transparency Logs: crt.sh reveals all TLS certificates issued for a domain — a primary source for subdomain enumeration.

Shodan: Internet-connected device search engine. Identifies exposed services by IP, ASN, or domain.

LinkedIn: Organizational hierarchy, technology stack clues from job postings.

theHarvester: Aggregates emails, names, and domains from multiple OSINT sources.

[SLIDE: Active Recon — Key Tools]

For active reconnaissance:

Nmap: Port scanning, service version detection, OS fingerprinting. Know key flags: `-sS` (SYN scan), `-sV` (version), `-A` (aggressive), `-p-` (all ports), `-T4` (timing), `-oA` (all formats output), `-sU` (UDP).

Masscan: High-speed port scanning. Faster than Nmap for large IP ranges.

Nikto: Web server vulnerability scanner.

Gobuster/Dirb: Directory and file brute-forcing on web applications.

Enum4linux: Windows/Samba enumeration.

[SLIDE: Vulnerability Scanners]

Know the difference:

Network vulnerability scanners: Nessus, OpenVAS/Greenbone, Nexpose/InsightVM. Identify host vulnerabilities across the network.

Web application scanners: Nikto (quick), OWASP ZAP (deep), Burp Suite Pro (manual + automated).

Authenticated vs. unauthenticated scans: Authenticated scans use valid credentials to assess the system from an insider perspective. Results are more complete. Unauthenticated scans simulate an external attacker.

[PAUSE for transition]

---

## Segment 4: Domain 3 Review — Attacks and Exploits (Lines 101–145)

[SLIDE: Domain 3 Key Topics]

Domain 3 is the largest at 30% of the exam. It covers:

Social engineering attacks: Phishing, vishing, pretexting, tailgating, baiting, shoulder surfing, elicitation.

Network attacks: Packet analysis, deauthentication, ARP spoofing, VLAN hopping, MAC flooding, DNS poisoning.

Wireless attacks: WPA2 handshake capture, cracking, evil twin, PMKID attack, deauthentication.

Application attacks: SQL injection, XSS, SSRF, XXE, directory traversal, IDOR, deserialization.

Post-exploitation: Lateral movement, pivoting, persistence, credential harvesting, data exfiltration.

Physical attacks: Tailgating, badge cloning, lock picking, dumpster diving.

[SLIDE: Must-Know Attacks]

The following attack types appear frequently in PT0-002 scenarios:

SQL Injection — basic syntax, blind vs. error-based, SQLMap tool.

Cross-Site Scripting (XSS) — reflected vs. stored vs. DOM-based.

SSRF — internal resource access, AWS IMDS exploitation.

Pass the Hash — NTLM hash use without cracking for lateral movement.

Kerberoasting — requesting and cracking service ticket hashes offline.

LLMNR/NBT-NS Poisoning — Responder capturing NTLM hashes.

WPA2 cracking — handshake capture with airodump-ng, crack with aircrack-ng or Hashcat.

Buffer overflow — concepts (stack vs. heap), NOP sled, shellcode execution.

[SLIDE: Post-Exploitation Tools]

Know these tools for post-exploitation:

Metasploit: Framework for exploitation, Meterpreter shell, post-exploitation modules.

Mimikatz: Windows credential extraction — pass-the-hash, sekurlsa::logonpasswords, lsadump::sam.

BloodHound: Active Directory attack path visualization.

Impacket: Python tools for Windows protocol attacks (secretsdump, psexec, smbclient).

CrackMapExec: Active Directory penetration testing tool.

Responder: LLMNR/NBT-NS poisoning for credential capture.

PowerSploit/PowerShell Empire: PowerShell-based post-exploitation.

[PAUSE for transition]

---

## Segment 5: Domain 4 and Domain 5 Review (Lines 146–185)

[SLIDE: Domain 4 — Reporting and Communication]

Domain 4 covers 16% of the exam.

Report structure: Executive summary, scope and methodology, findings, remediation, appendices.

Finding components: Title, risk rating, CVSS score, description, evidence, impact, affected assets, remediation.

CVSS 3.1 scoring: Know all base metric options. Know the qualitative rating thresholds (Critical ≥ 9.0, High 7.0–8.9, Medium 4.0–6.9, Low 0.1–3.9).

Communication: How to present to technical vs. non-technical audiences. Professional language standards. Handling client disputes.

[SLIDE: Domain 4 Must-Know Scenarios]

"A client asks you to remove a Critical finding from the report because they have already mitigated it." — Keep the finding, add a "Mitigated" note with evidence of the fix if the client verifies remediation.

"A finding was discovered after the testing period ended due to log review." — This may be included as a post-assessment finding with clear documentation of the timeline.

"The CISO asks for the raw Nmap output immediately after scanning." — This is a reasonable request; testers often provide interim deliverables. Ensure client authorization explicitly permits this (it should be in the ROE).

[SLIDE: Domain 5 — Tools and Code Analysis]

Domain 5 covers 18% of the exam. Key topics:

Tool categories and uses: Know which tool category (scanner, exploitation framework, credential attacker, etc.) each major tool belongs to.

Script analysis: Read a Python, Bash, or PowerShell script and identify what it does.

Exploit modification: Understand how to configure a Metasploit module or modify a simple script.

Use case identification: Given a scenario, identify the appropriate tool.

[SLIDE: Domain 5 Tool Mapping Table]

Master this mapping:

| Category | Tools |
|----------|-------|
| Exploitation framework | Metasploit, CANVAS |
| Credential attacks | Hashcat, John the Ripper, Hydra, Medusa |
| Reconnaissance | Nmap, Masscan, theHarvester, Maltego, Recon-ng |
| Web application | Burp Suite, OWASP ZAP, Nikto, SQLMap, WFuzz |
| Wireless | Aircrack-ng, Airodump-ng, Kismet, Hashcat |
| Password cracking | Hashcat, John the Ripper, Mimikatz, Responder |
| Scripting | Python, Bash, PowerShell, Ruby |
| Forensics/Analysis | Wireshark, Autopsy, Volatility |
| Cloud | Pacu, ScoutSuite, Prowler, CloudFox |
| Mobile | MobSF, Drozer, Frida, Objection |

[PAUSE for transition]

---

## Segment 6: Performance-Based Questions and Exam Strategy (Lines 186–215)

[SLIDE: Performance-Based Questions]

PT0-002 includes performance-based questions (PBQs) that simulate real-world scenarios in an interactive environment. PBQs may include:

- Configuring a tool correctly to achieve a specific objective
- Analyzing tool output and identifying findings
- Matching attacks to scenarios
- Ordering steps in a methodology
- Identifying vulnerabilities in a code snippet

PBQs appear at the beginning of the exam. They take more time than multiple-choice questions. Many candidates skip PBQs initially and return after completing all multiple-choice questions.

[SLIDE: Exam Strategy]

Practical exam strategy:

Skip and return: If a PBQ or difficult question takes more than 3 minutes, mark it and move on. Return with remaining time.

Eliminate first: For multiple-choice questions, eliminate clearly wrong answers first. With two remaining options, your odds are 50/50. Educated guesses are better than no answer — there is no penalty for wrong answers on the PT0-002.

Read for keywords: Exam questions often contain key words that point to the correct answer: "MOST appropriate," "FIRST action," "BEST describes." These qualifiers change which answer is correct.

The "least privilege" principle: Many authorization and access control questions have an answer consistent with least privilege. When in doubt, the answer that grants minimum necessary access is often correct.

[SLIDE: Scenario Question Framework]

For scenario-based questions, apply this decision framework:

Step 1: What is the attacker's (or tester's) objective?

Step 2: What phase of the penetration testing methodology does this describe?

Step 3: What tool or technique is specific to this phase and objective?

Step 4: What legal or ethical constraint applies?

This four-step framework resolves most scenario questions without memorizing individual fact trivia.

[SLIDE: What NOT to Do on the Exam]

Common exam mistakes:

Overthinking: The exam tests practical knowledge, not edge cases. The most straightforward interpretation of a scenario is usually correct.

Ignoring authorization: Questions that describe testing activities — if one answer involves proceeding without proper authorization and another involves stopping to get authorization, the authorized option is almost always correct.

Confusing tool purposes: Know what each major tool does specifically. Aircrack-ng cracks WPA2; it does not capture packets. Airodump-ng captures packets; it does not crack them.

[PAUSE for transition]

---

## Segment 7: Capstone Introduction and Closing (Lines 216–240)

[SLIDE: Capstone Overview]

The Module 16 capstone is a 20-question scenario-based assessment covering all five PT0-002 domains. It simulates the PT0-002 exam format with multiple-choice and scenario questions.

The capstone is worth 20% of your course grade. You have 45 minutes to complete it under exam conditions — closed book, no notes.

After the capstone, you will complete a comprehensive reflection: which domains felt most solid, which need additional study, and what your exam preparation plan looks like for the actual PT0-002.

[SLIDE: Beyond the Certification]

As you complete this course and prepare for the PT0-002, I want to leave you with a professional perspective.

The certification validates a baseline of knowledge. The work that follows — hands-on practice, real engagements, continued learning — builds the expertise. Platforms like Hack The Box, TryHackMe, and VulnHub provide safe, legal environments for continued skill development.

Every technique in this course is powerful and potentially dangerous. The professional and ethical framework you have studied throughout this course — authorization, scope, proportionality, honest reporting — is what makes the difference between a security professional and a criminal. Both know the same techniques. Only one has permission to use them and the professional obligation to use them responsibly.

[SLIDE: Final Message]

Authorization is the foundation.

Ethics is the framework.

Skill serves the mission.

The mission is to make systems safer for everyone.

Congratulations on completing CIS-4333 Penetration Testing. Good luck on the PT0-002 exam. I have no doubt you are prepared.

[END RECORDING]
