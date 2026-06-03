# Discussion Forum: Module 08 — Post-Exploitation and Lateral Movement

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Professor Nash's Note on Professional Ethics

Post-exploitation is where penetration testing most closely resembles what real attackers do. The techniques in this module — privilege escalation, credential dumping, pass-the-hash, pivoting — are the exact same techniques used in the most significant breaches of the past decade. The difference between a penetration tester and an attacker is authorization, documentation, and intent.

Your obligation as a professional is not just to avoid harm during a test, but to actively help the organization understand and close the gaps you find. A great penetration tester does not just demonstrate that they can dump credentials and move laterally — they clearly explain why it matters, what the real-world attacker path looks like, and what specific controls would have stopped them. That communication is as important as the technical work. The discussions below develop that skill.

---

## Discussion Scenario 1 — The Credential Cascade

A penetration tester is conducting an authorized internal test for a financial services firm. Starting from a phishing simulation that grants a shell as a marketing department user, the tester uses privilege escalation to gain SYSTEM access on the marketing workstation, then runs credential dumping to extract NTLM hashes from LSASS memory.

Among the hashes recovered is one for `svc_backup` — a service account. Using pass-the-hash, the tester authenticates to a backup server and discovers the `svc_backup` account has read access to a shared storage path containing full database backups — including one labeled `customer_financial_data_2025.bak`.

The tester does NOT download the database backup. They document the access path and stop there.

**Discussion Prompt:**

In 175–225 words, address the following:

- Why is stopping at the point of demonstrated access — without downloading the sensitive data — the professionally correct decision?
- How should the tester document and communicate this finding to demonstrate maximum impact without actually exfiltrating client data?
- What does this attack chain (phishing → local escalation → credential dump → lateral movement → data access) illustrate about the concept of defense-in-depth?
- What specific security controls, if any one of them were in place, would have broken this attack chain?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 2 — The Forgotten Backdoor

Six months after completing a penetration test for a manufacturing company, a security analyst at the company notices unusual outbound traffic originating from a server that was part of the penetration test scope. Investigation reveals an active reverse shell connection making regular callbacks to an external IP address.

The analyst contacts the penetration testing firm. The firm reviews their records and discovers that a junior tester forgot to remove a Meterpreter persistence module installed during the engagement. The connection has been active for six months. During that period, no one used it — but the access existed.

**Discussion Prompt:**

In 175–225 words, address the following:

- What professional and contractual failures occurred, and who bears responsibility?
- What harm could have resulted during the six-month window, even if the tester did not actively use the backdoor?
- What processes should penetration testing firms implement to prevent this type of oversight?
- What are the legal implications for the firm, and what is their obligation to the client now that the issue has been discovered?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 3 — Communicating Impact to Non-Technical Stakeholders

A penetration tester has just completed a full-scope internal test. The findings include: privilege escalation from a help desk user to Domain Admin in under 90 minutes, pass-the-hash lateral movement to 14 additional systems, and demonstrated read access to the HR payroll database. No actual data was exfiltrated.

The tester is presenting findings to the organization's executive team — a group that includes the CFO, COO, and General Counsel. None of them have technical backgrounds. The CISO is present but has asked the tester to explain findings directly to the executives without technical jargon.

**Discussion Prompt:**

In 175–225 words, address the following:

- How would you translate the technical findings (privilege escalation, pass-the-hash, lateral movement to 14 systems, payroll DB access) into language that communicates real business risk to a non-technical executive audience?
- What analogy or story structure would you use to explain the attack chain without requiring the audience to understand NTLM hashing or Active Directory?
- Why is the "we did not actually take any data" point both reassuring and insufficient as a complete risk statement?
- What should a professional penetration tester always make clear when presenting findings — even to friendly, authorized clients?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|---------|
| Initial Post — Technical Accuracy | 3 | Demonstrates accurate understanding of post-exploitation concepts from Module 08 |
| Initial Post — Ethical Reasoning | 2 | Addresses authorization, documentation, and professional obligations with specificity |
| Initial Post — Word Count and Format | 1 | 175–225 words, organized response, professional tone |
| Peer Response 1 | 2 | Minimum 75 words, adds substantive analysis or challenges a point with reasoning |
| Peer Response 2 | 2 | Minimum 75 words, introduces a new consideration or connects to course concepts |

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
