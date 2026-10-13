# Video Script: Module 16 — PenTest+ Exam Preparation and Capstone

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome to Module 16 — the final module of CIS-4333. I am Professor Nash, and today we are
doing something different from every other module this semester. Instead of introducing new
content, we are pulling the entire course together: reviewing the domain structure of the
PenTest+ exam, hitting the highest-yield topics across all five domains, practicing exam
strategy, and walking through a complete capstone scenario that mirrors what you will
encounter on test day.

If you have been with us since Module 1, you have already covered everything this exam tests.
Today is about making sure you can retrieve it under pressure, apply it to scenario-based
questions, and walk into the testing center with a clear, confident strategy.

Let us start with the exam structure.

---

## SEGMENT 2 — PenTest+ PT0-002 Domain Breakdown (1:30–5:00)

The CompTIA PenTest+ PT0-002 exam contains a maximum of 85 questions. You have 165 minutes.
The passing score is 750 on a 900-point scale. The exam uses multiple-choice questions and
performance-based questions (PBQs) — scenario-driven simulations requiring you to analyze
tool output, complete a command, or select an ordered sequence of actions.

The five domains and their exam weights are:

| Domain | Title | Weight |
|--------|-------|--------|
| 1 | Planning and Scoping | 14% |
| 2 | Information Gathering and Vulnerability Scanning | 22% |
| 3 | Attacks and Exploits | 30% |
| 4 | Reporting and Communication | 18% |
| 5 | Tools and Code Analysis | 16% |

Domain 3 (Attacks and Exploits) is the largest single domain at 30%. Domain 2 (Information
Gathering) is second at 22%. Together these two domains represent more than half the exam.

### What Each Domain Tests

**Domain 1 — Planning and Scoping (14%)**: Engagement types (white-box, grey-box, black-box),
rules of engagement, legal agreements (NDA, MSA, SOW), scope definition, compliance
considerations (PCI-DSS, HIPAA, SOX), and resource requirements.

**Domain 2 — Information Gathering and Vulnerability Scanning (22%)**: OSINT techniques,
passive vs. active reconnaissance, DNS enumeration, network scanning (Nmap), vulnerability
scanning (Nessus, OpenVAS), service enumeration, and interpreting scan output.

**Domain 3 — Attacks and Exploits (30%)**: Network attacks (ARP spoofing, pass-the-hash,
Kerberoasting), web application attacks (SQLi, XSS, IDOR, SSRF), wireless attacks (WPA2
cracking, evil twin), social engineering, exploitation frameworks (Metasploit), post-
exploitation (privilege escalation, lateral movement, persistence, data exfiltration), and
evasion techniques.

**Domain 4 — Reporting and Communication (18%)**: Report types, finding components, CVSS
scoring, sensitive data handling, attestation, post-engagement cleanup, evidence handling,
retesting, and client communication. Modules 14 and 15 of this course covered this domain
in full.

**Domain 5 — Tools and Code Analysis (16%)**: Tool identification and use cases (Nmap,
Metasploit, Burp Suite, Nikto, sqlmap, Hydra, John the Ripper, Aircrack-ng, BloodHound,
Mimikatz), bash and Python scripting for automation, and basic code analysis for
identifying vulnerabilities in provided code snippets.

---

## SEGMENT 3 — High-Yield Topic Review: Enumeration (5:00–8:30)

Let us review the topics most likely to appear in Domain 2 questions.

### Nmap Scan Types

Know these Nmap flags by memory:

- `-sS` — TCP SYN scan (stealthy, default with root)
- `-sT` — TCP Connect scan (full three-way handshake, no root required)
- `-sU` — UDP scan (slower, used for DNS, SNMP, TFTP)
- `-sV` — Service version detection
- `-O` — OS detection
- `-A` — Aggressive: OS, version, scripts, traceroute
- `-p-` — All 65,535 ports
- `-T0` through `-T5` — Timing templates (T0 slowest/stealthiest, T5 fastest/noisiest)
- `--script vuln` — NSE vulnerability scripts
- `-oN`, `-oX`, `-oG` — Output formats: Normal, XML, Greppable

### DNS Enumeration

Tools and techniques: `nslookup`, `dig`, `dnsenum`, `fierce`, `subfinder`.

Key techniques: zone transfer (`dig axfr @nameserver domain.com`), subdomain brute-force,
reverse DNS lookup, MX/TXT/SPF record analysis.

A successful zone transfer is a finding in itself — it means the DNS server allows
unauthenticated zone transfers, exposing the full host list.

### OSINT Tools

- **theHarvester**: email addresses, subdomains, and employee names from public sources
- **Maltego**: visual relationship mapping across OSINT sources
- **Shodan**: internet-facing device search engine; find exposed services and banners
- **Recon-ng**: modular OSINT framework with API integrations
- **WHOIS**: domain registration details, registrar, contact info, registration dates

### Vulnerability Scanning

Nessus and OpenVAS produce vulnerability scan reports. For the exam, know:

- Authenticated vs. unauthenticated scans: authenticated scans log into targets and
  produce far more accurate results, including missing patches and local configuration
  issues
- False positives: scanner reports a vulnerability that does not actually exist; must be
  manually verified
- False negatives: scanner misses a real vulnerability; manual testing catches what
  scanners miss

---

## SEGMENT 4 — High-Yield Topic Review: Attacks and Exploits (8:30–13:00)

Domain 3 is 30% of the exam. Here are the most-tested concepts.

### Metasploit Framework

Key components: `msfconsole`, `search`, `use`, `info`, `set RHOSTS`, `set LHOST`,
`set PAYLOAD`, `run`/`exploit`, `sessions`, `background`.

Post-exploitation modules: `post/windows/gather/hashdump`, `post/multi/recon/local_exploit_suggester`,
`post/windows/manage/migrate`.

Meterpreter commands: `sysinfo`, `getuid`, `getsystem`, `hashdump`, `upload`, `download`,
`shell`, `migrate`, `run persistence`.

### Web Application Attacks

**SQL Injection (SQLi)**: Unsanitized user input concatenated into SQL queries. Manual test:
append a single quote `'` to a parameter; look for database errors. Tool: `sqlmap`.
Prevention: parameterized queries (prepared statements). CWE-89.

**Cross-Site Scripting (XSS)**: Stored (persisted in database), Reflected (in URL
parameter), DOM-based. Payload: `<script>alert(1)</script>`. Impact: session hijacking,
credential theft. Prevention: output encoding, Content Security Policy. CWE-79.

**Insecure Direct Object Reference (IDOR)**: Manipulate object identifiers in requests
to access unauthorized resources. Example: changing `user_id=1001` to `user_id=1002` in
an API call to access another user's data. CWE-639.

**Server-Side Request Forgery (SSRF)**: Attacker causes the server to make HTTP requests
to internal resources. Can reach cloud metadata endpoints (`169.254.169.254`) or internal
services. CWE-918.

**Command Injection**: User input passed unsanitized to an OS shell function. Test with
`;id`, `|whoami`, `&&cat /etc/passwd`. CWE-78.

### Windows Post-Exploitation

**Pass the Hash (PtH)**: Use an NTLM hash directly for authentication without cracking it.
Tools: `pth-winexe`, Mimikatz `sekurlsa::pth`, Metasploit `psexec` with hash.

**Kerberoasting**: Request Kerberos service tickets for SPNs, extract ticket hashes, crack
offline. Tool: `GetUserSPNs.py` (Impacket), Rubeus. Targets service accounts with weak
passwords.

**BloodHound**: Visualizes Active Directory attack paths using graph theory. Identifies
shortest path to Domain Admin via misconfigurations in ACLs, group memberships, and
delegation settings.

**Mimikatz**: Extracts credentials from Windows memory (LSASS). Key commands:
`privilege::debug`, `sekurlsa::logonpasswords`, `lsadump::sam`. Requires SYSTEM or
SeDebugPrivilege.

### Privilege Escalation

Linux: SUID/SGID binaries (`find / -perm -4000`), writable cron jobs, sudo misconfigurations
(`sudo -l`), PATH hijacking, kernel exploits.

Windows: Unquoted service paths, weak service permissions, AlwaysInstallElevated,
token impersonation (`incognito`), UAC bypass techniques.

---

## SEGMENT 5 — Exam Strategy (13:00–16:30)

### Scenario-Based Questions

PenTest+ is heavily scenario-based. Questions present a real-world situation and ask what
the tester should do next, which tool to use, or which finding classification is correct.
A reliable approach for scenario questions:

1. **Identify the phase**: Is this reconnaissance, scanning, exploitation, post-exploitation,
   or reporting? The correct answer often depends on what phase the scenario is in.
2. **Identify the constraint**: Is the tester authorized? Is there a scope limitation? Is
   the client's system fragile? Constraints narrow the correct action.
3. **Eliminate the extremes**: Remove the option that is clearly too aggressive and the
   option that is clearly too passive or irrelevant.
4. **Apply the principle**: Use the specific concept from the relevant domain — CVSS
   scoring, cleanup obligation, tool purpose, legal agreement type.

### Elimination Technique

On multiple-choice questions with four options, most questions have two clearly wrong
distractors and two plausible options. The winning technique:

- Eliminate based on factual incorrectness: the option with a wrong definition, a
  misidentified tool, or an impossible outcome
- Between the remaining two, apply the scenario constraint: which option is consistent
  with authorized testing, professional standards, and the specific phase?

### Time Management

165 minutes for 85 questions = approximately 1 minute 56 seconds per question. In practice:

- Spend 60–75 seconds on straightforward knowledge questions (definitions, tool flags)
- Spend 2–3 minutes on performance-based questions and complex scenarios
- Mark and skip questions you are unsure about; return to them after answering everything
  you know confidently
- Never leave a question blank — there is no penalty for wrong answers on PT0-002

### Performance-Based Questions

PBQs appear at the start of the exam. They often involve:

- Analyzing Nmap output and identifying open ports, services, or vulnerable versions
- Completing a Metasploit command sequence with the correct module path and options
- Ordering the steps of an engagement phase in the correct sequence
- Identifying which tool output corresponds to a specific technique

Spend reasonable time on PBQs but do not let one difficult PBQ consume 15 minutes. Mark it
and move on; return with remaining time.

---

## SEGMENT 6 — Practice Question Walkthrough (16:30–19:30)

Let us work through three practice questions using the strategy above.

### Practice Question A

A penetration tester is performing a black-box external assessment. During reconnaissance,
they discover the target organization's internal IP addressing scheme and the names of three
internal servers by querying a public DNS server. What technique produced this information?

- A) Active port scanning with Nmap
- B) DNS zone transfer against a misconfigured authoritative name server
- C) Passive OSINT using the company's LinkedIn profile
- D) Subdomain brute-force with Gobuster

**Analysis**: The question says "querying a public DNS server" and the result includes
internal IP addresses — information that should not be publicly available. That is the signal
for a zone transfer. A misconfigured authoritative name server allows anyone to request a
full zone dump. The correct answer is B.

Eliminate A because port scanning does not produce DNS records. Eliminate C because LinkedIn
does not list internal IP addresses. Eliminate D because brute-force would find subdomains
by guessing names, not by retrieving the full zone contents in one query.

### Practice Question B

A tester obtains a low-privilege shell on a Linux web server. Running `sudo -l` produces the
following output: `(ALL) NOPASSWD: /usr/bin/find`. Which command exploits this misconfiguration
to escalate privileges to root?

- A) `sudo find / -name "*.conf" -exec cat {} \;`
- B) `sudo find / -exec /bin/sh \;`
- C) `sudo find /etc/passwd -readable -type f`
- D) `find / -perm -4000 -type f`

**Analysis**: The misconfiguration is that the tester can run `find` as root without a
password. The GTFOBins technique for `find` is using `-exec` to spawn a shell. Option B
runs `/bin/sh` as root via the exec flag — that is a privilege escalation to a root shell.
The correct answer is B.

Option A uses exec but only cats config files — useful for information gathering, not
privilege escalation. Option C is a file permission check, not escalation. Option D is
a SUID binary search run without sudo — it does not use the sudo misconfiguration at all.

### Practice Question C

After completing an engagement, the client asks whether they can post the pentest report to
their public-facing investor relations website to demonstrate security diligence. What is
the tester's correct response?

- A) Approve the posting because transparency builds public trust
- B) Decline to provide guidance — what the client does with the report is entirely their
  business decision
- C) Strongly advise against public posting because the report contains specific
  vulnerability details, affected system identifiers, and evidence that could directly
  enable attacks against the client
- D) Approve posting of the executive summary only; the technical report must remain
  confidential by default

**Analysis**: Posting a pentest report publicly — even just the executive summary — reveals
information about the organization's security posture to potential attackers. The executive
summary identifies the organization's biggest weaknesses. The technical report is even worse:
it contains specific hosts, CVEs, and evidence. The correct answer is C.

Option A ignores the security consequences of disclosure. Option B is a professional
abdication — the tester has an obligation to advise on exactly this kind of question.
Option D is closer but still wrong — the executive summary should not be posted publicly
either, for the same reason.

---

## SEGMENT 7 — Capstone Scenario Summary (19:30–22:00)

Let us walk through a complete simulated engagement summary to consolidate everything from
the course into one narrative.

### Engagement: Horizon Logistics (Simulated)

**Engagement Type**: Grey-box internal and external assessment. Client provided network
diagrams and a list of in-scope IP ranges. No credentials provided. Testing window: 10
business days.

**Phase 1 — Planning and Scoping**: Signed NDA, MSA, and SOW. Rules of engagement defined
no denial-of-service testing against production systems. Agreed out-of-hours window for
any exploitation that might cause service disruption.

**Phase 2 — Reconnaissance**: theHarvester identified employee names and email format
(`firstname.lastname@horizonlogistics.com`). Shodan revealed an externally-facing Fortinet
VPN concentrator running a known vulnerable firmware version. DNS enumeration found 12
subdomains; one (`staging.horizonlogistics.com`) resolved to an internal IP — leaked
internal addressing.

**Phase 3 — Scanning**: Nmap `-sS -sV -O -p-` against external ranges identified 4 open
ports on the VPN concentrator: 443, 8443, 10443. Nessus authenticated scan of internal
subnet identified 7 Medium and 2 High findings related to missing patches.

**Phase 4 — Exploitation**: CVE-2022-40684 (Fortinet authentication bypass) confirmed
exploitable on the VPN concentrator — obtained admin access without credentials. From that
foothold, pivoted to the internal network. Kerberoasting via Impacket yielded a crackable
service account hash for `svc_backup`. Service account had local admin rights on 14 servers.
Lateral movement to a domain controller using pass-the-hash produced a Domain Admin session.

**Phase 5 — Post-Exploitation**: BloodHound mapping revealed three additional paths to
Domain Admin. Captured domain password hashes. Simulated exfiltration of a sample HR data
file via HTTP to the tester's C2 server to demonstrate data egress capability.

**Phase 6 — Cleanup**: All payloads, shells, and created artifacts removed per engagement
log. Cleanup attestation delivered.

**Phase 7 — Reporting**: Executive summary rated organization at Critical overall risk.
Technical report contained 11 findings (2 Critical, 4 High, 3 Medium, 2 Low). All six
finding components present for each finding. Debrief conducted: executive session with CISO
and CTO, technical session with the security operations team.

This end-to-end flow — planning through reporting — is the complete PT0-002 domain lifecycle.
Every step maps to a testable exam objective.

---

## SEGMENT 8 — Certification Maintenance and Closing (22:00–24:00)

### After You Pass

CompTIA PenTest+ is valid for three years. To renew, earn 60 Continuing Education Units (CEUs)
within that period. CEU-eligible activities include:

- Training courses and college coursework in cybersecurity
- CompTIA CertMaster CE (online renewal assessment)
- Industry conference attendance (DEF CON, Black Hat, BSides events)
- Publishing security research, blog posts, or instructional content
- Earning a higher-level certification (CEH, OSCP, PNPT) — which automatically renews
  lower-level CompTIA certs under the higher-cert umbrella program

### Next Certifications to Consider

After PenTest+, natural progression paths include:

- **CompTIA CASP+** (advanced security practitioner, enterprise-level)
- **Offensive Security OSCP** (Offensive Security Certified Professional — the hands-on
  gold standard for penetration testing; requires 24-hour practical exam)
- **PNPT** (Practical Network Penetration Tester, by TCM Security — highly regarded,
  practical, more accessible than OSCP as a stepping stone)
- **eJPT** (eLearnSecurity Junior Penetration Tester — entry-level practical, good if
  OSCP feels too advanced right now)

### Closing Thoughts

You have completed CIS-4333. Over sixteen modules you built a systematic penetration testing
methodology: planning, reconnaissance, scanning, exploitation, post-exploitation, and
reporting. You practiced in authorized lab environments. You learned not just the technical
skills but the professional and ethical obligations that distinguish a legitimate penetration
tester from a threat actor.

The skills you have developed are powerful. Use them responsibly, professionally, and only
with explicit authorization.

Good luck on your PenTest+ exam. I am proud of the work you have put in this semester.

---

*End of Module 16 Video Script*
