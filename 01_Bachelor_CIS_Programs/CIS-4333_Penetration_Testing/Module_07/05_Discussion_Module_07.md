# Discussion Forum: Module 07 — Exploitation Techniques

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Professor Nash's Note on Professional Ethics

Exploitation is the phase that carries the most weight — both technically and ethically. When you execute an exploit against a target, you are demonstrating that a theoretical risk is real. That is powerful and valuable for the client. It is also the phase with the greatest potential for harm if performed carelessly or without authorization.

Professional penetration testers think through every exploit before running it: What will it do? Could it crash the service? Could it affect other users? Is it within scope? Can I roll back if something goes wrong? These are not bureaucratic questions — they are how experienced testers protect clients and themselves.

The discussions below ask you to think through difficult but realistic scenarios. There are no easy answers, and that is intentional. The goal is to develop the judgment that technical training alone cannot provide.

---

## Discussion Scenario 1 — The Critical System Dilemma

A penetration tester is conducting an authorized internal test for a logistics company. The scope includes all systems on the `10.0.0.0/8` internal network. During scanning, the tester discovers that a server at `10.10.50.15` is running Windows Server 2012 R2 and appears vulnerable to EternalBlue (MS17-010) based on Nmap NSE script results.

The tester is about to run the Metasploit `ms17_010_eternalblue` module when a colleague mentions that the hostname `10.10.50.15` resolves to `prod-erp-db01.logistics.local` — a name suggesting this may be a production database server.

The `check` command in the module returns: "The target appears to be vulnerable."

**Discussion Prompt:**

In 175–225 words, address the following:

- What additional information should the tester gather before executing the exploit against this specific target?
- What are the risks of exploiting a production database server, and how do these risks influence the tester's decision?
- What should be documented and communicated to the client before proceeding?
- How does this scenario illustrate the difference between "technically authorized" and "professionally appropriate"?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 2 — The Public Exploit Problem

A junior penetration tester searches GitHub for a proof-of-concept exploit for a recently disclosed CVE affecting a target web application. They find a Python script posted three days ago by an anonymous account. The script has 47 stars and a few comments saying "works great."

The tester copies the script to their Kali machine, glances at the first ten lines, and prepares to run it against the authorized target. A more experienced team member suggests reading the full script first.

The junior tester opens the full file and discovers that in addition to the CVE exploit code, the script contains a second function that — when run — copies all files from the current user's home directory and sends them to an external IP address.

**Discussion Prompt:**

In 175–225 words, address the following:

- What professional practice failure nearly occurred, and what are the consequences of running this script as-is?
- Describe the minimum review a penetration tester should perform before executing any public exploit code — what should they look for?
- How does this scenario reflect the real-world threat of supply chain attacks and malicious open-source contributions?
- What process should penetration testing teams use to vet and approve third-party exploit code before use on engagements?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 3 — Zero-Day Responsibility

A seasoned penetration tester is conducting a web application assessment for a healthcare provider. During manual testing, the tester discovers a vulnerability in a widely-used electronic health records (EHR) software package — one used by thousands of hospitals worldwide. The vulnerability allows unauthenticated remote code execution. The tester confirms it against the authorized lab instance.

Importantly, this is not a known CVE. The tester discovered it independently. No patch exists. The EHR vendor is a large corporation known for slow security responses. The tester estimates that millions of patient records across all customer organizations are potentially at risk.

**Discussion Prompt:**

In 175–225 words, address the following:

- What is responsible disclosure, and what specific steps does it require in this scenario?
- What are the tester's obligations to the healthcare provider client, to the EHR vendor, and to the patients whose data is at risk?
- What timeline is considered professionally appropriate between private disclosure to the vendor and public disclosure if the vendor does not respond?
- What resources (organizations, frameworks, or programs) exist to assist penetration testers in coordinating responsible disclosure for vulnerabilities discovered during engagements?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|---------|
| Initial Post — Technical Accuracy | 3 | Demonstrates accurate understanding of exploitation concepts from Module 07 |
| Initial Post — Ethical Reasoning | 2 | Addresses scope, risk, authorization, and professional obligations with specificity |
| Initial Post — Word Count and Format | 1 | 175–225 words, organized response, professional tone |
| Peer Response 1 | 2 | Minimum 75 words, adds substantive analysis or challenges a point with reasoning |
| Peer Response 2 | 2 | Minimum 75 words, introduces a new consideration or connects to course concepts |

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
