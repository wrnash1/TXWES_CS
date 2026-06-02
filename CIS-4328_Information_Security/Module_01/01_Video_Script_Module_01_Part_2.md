# Video Script — Module 01, Part 2: Threats, Attacks, and Vulnerabilities (Applied and Exam Strategy)

## CIS-4328 Information Security | Texas Wesleyan University

### Instructor: Professor Nash | CompTIA Security+ SY0-701 Alignment

### Estimated Duration: 11 minutes

---

## Opening — Recap and Transition

**[INSTRUCTOR ON CAMERA]**

Welcome back. In Part 1 we built the conceptual foundation: the CIA Triad, the controls framework, threat actor types, vulnerability classes, and active versus passive attacks. In Part 2 we are going to do three things: apply those concepts to attack surface analysis, walk through how these topics appear on the actual SY0-701 exam in scenario-based questions, and give you a practical exam strategy for Module 01 questions.

---

## Section 1 — Attack Surface Analysis

**[SHOW DIAGRAM: A target organization represented as a series of concentric rings. Outermost ring: Internet-facing services — web servers, email, VPN endpoints. Middle ring: Internal network — workstations, file servers, printers. Inner ring: Data assets — databases, intellectual property, customer records. Arrows labeled Attack Vector point inward from the outside.]**

**[Alt-text: Concentric rings diagram titled Attack Surface. Outermost ring is labeled Internet-Facing Services and lists web servers, email gateways, and VPN endpoints. Middle ring is labeled Internal Network and lists workstations, file servers, and printers. Inner ring is labeled Data Assets and lists databases and customer records. Red arrows labeled Attack Vector point from outside the diagram toward the center.]**

The **attack surface** is the total set of entry points where an attacker can attempt to compromise a system or extract data. Every open port, every running service, every user account, and every piece of software installed on a system contributes to the attack surface.

**Attack surface reduction** is one of the most important principles in security architecture. The steps to reduce attack surface are:

- Disable unused services and ports.
- Remove software that is not needed for the system's function.
- Apply the principle of least privilege — grant users only the access they need to perform their job.
- Segment networks so that a compromise of one zone does not give an attacker access to the entire organization.
- Patch vulnerabilities promptly to eliminate known entry points.

**Attack vectors** are the specific paths an attacker uses to reach a target. Common vectors include:

- **Email** — phishing messages that deliver malware or steal credentials.
- **Web application** — input validation flaws like SQL injection and cross-site scripting.
- **Network** — exploitation of open ports and unpatched services.
- **Physical** — tailgating into secured areas, USB drop attacks.
- **Supply chain** — compromise of a third-party vendor whose software is then distributed to the target.

**Exam Tip:** SY0-701 scenario questions will describe a breach and ask you to identify the attack vector. Focus on how the attacker first gained entry, not on what they did after entry.

---

## Section 2 — Indicators of Compromise

**[SHOW DIAGRAM: Three-column table. Column 1: Indicator Category. Column 2: Example. Column 3: What It Suggests. Rows cover: Unusual Outbound Traffic, Account Privilege Escalation, Unexpected New Admin Accounts, Unusual Login Times/Locations, Anomalous Process Execution.]**

**[Alt-text: Three-column table titled Indicators of Compromise. Row 1: Unusual Outbound Traffic — Large data transfer to unknown foreign IP — Data exfiltration. Row 2: Account Privilege Escalation — Standard user account gains admin rights without IT ticket — Insider threat or credential compromise. Row 3: Unexpected New Admin Accounts — New local admin account created after business hours — Attacker establishing persistence. Row 4: Unusual Login Times — User account authenticates at 3 AM from a foreign country — Credential theft or account compromise. Row 5: Anomalous Process Execution — System32 process spawning PowerShell — Fileless malware or living-off-the-land attack.]**

An **Indicator of Compromise** — IOC — is a piece of forensic evidence that suggests a system may have been breached. Security operations centers use IOCs to detect and respond to attacks in progress.

Key IOC categories tested on SY0-701:

**Network-based IOCs** include unusual outbound traffic volumes, connections to known malicious IP addresses or domains, and use of non-standard ports for common protocols (for example, HTTP traffic on port 8888 instead of 80).

**Host-based IOCs** include new or modified files in system directories, unexpected scheduled tasks or startup entries, unfamiliar running processes, and disabled security tools.

**Account-based IOCs** include login attempts from impossible travel locations, multiple failed authentication attempts followed by a successful one (brute force success), and newly created privileged accounts.

**Log-based IOCs** include cleared security event logs, gaps in log timestamps, and log entries showing access to sensitive resources outside normal business hours.

---

## Section 3 — Exam Scenario Walkthroughs

**[INSTRUCTOR ON CAMERA]**

Let me walk you through three exam-style scenarios so you can see how these concepts are tested. This is exactly the kind of reasoning the SY0-701 expects.

**Scenario A:**

A company discovers that a threat actor spent six months quietly mapping their internal network, stealing R&D documents, and exfiltrating them to a server overseas — all without triggering any alerts. What type of threat actor is most consistent with this behavior, and what attack category does this represent?

Answer: Nation-state actor conducting an Advanced Persistent Threat campaign. The long dwell time, patient reconnaissance, and strategic objective of stealing intellectual property are hallmarks of a nation-state operation. This is an active attack — data was exfiltrated, meaning it was accessed and transmitted.

**Scenario B:**

An employee receives an email that appears to come from their CEO asking them to transfer funds to a new vendor account. The email header analysis reveals the message originated from a domain similar to — but not identical to — the company domain. What type of attack is this?

Answer: This is a business email compromise attempt using a homograph or look-alike domain. The attack vector is email. The threat actor is likely organized crime. No vulnerability in the company's software was exploited — the human was the vulnerability. This is a social engineering attack, which we cover in depth in Module 02.

**Scenario C:**

A security analyst notices that a web server's hash-based file integrity monitoring system has flagged three files in the web root as modified. The changes were made at 2 AM when no deployments were scheduled. What CIA triad property has been violated, and what should the analyst do first?

Answer: Integrity has been violated — files were modified without authorization. The analyst should first preserve the current state for forensic analysis before making any changes. They should then check the web application logs to identify how the files were modified, isolate the server to prevent further damage, and initiate the incident response process.

---

## Section 4 — Threat Intelligence Sources

**[SHOW DIAGRAM: Hub-and-spoke diagram. Center hub: Threat Intelligence. Spokes leading to: OSINT, ISAC, Commercial Feeds, Dark Web Monitoring, Government Advisories (CISA).]**

**[Alt-text: Hub-and-spoke diagram titled Threat Intelligence Sources. Central hub labeled Threat Intelligence. Five spokes extend to: OSINT — Open-Source Intelligence from public internet sources; ISAC — Information Sharing and Analysis Centers for sector-specific threat sharing; Commercial Feeds — Paid threat intelligence subscriptions; Dark Web Monitoring — Surveillance of criminal forums for stolen data or sale of exploits; Government Advisories — CISA alerts and FBI notifications.]**

**Threat intelligence** is processed information about current and emerging threats used to inform defensive decisions. The SY0-701 exam tests your ability to identify and apply threat intelligence sources.

- **OSINT** — Open-Source Intelligence gathered from publicly available sources: news reports, social media, security research blogs, and public vulnerability databases like the National Vulnerability Database.
- **ISACs** — Information Sharing and Analysis Centers are sector-specific organizations where companies share threat intelligence with peers in the same industry. The Financial Services ISAC and Healthcare ISAC are common examples.
- **Commercial threat feeds** — paid subscriptions that provide curated, real-time intelligence about threat actor TTPs (Tactics, Techniques, and Procedures), malware indicators, and compromised credential lists.
- **CISA advisories** — the Cybersecurity and Infrastructure Security Agency publishes alerts and advisories about active threats, vulnerabilities, and recommended mitigations.

**Exam Tip:** The SY0-701 may ask you to recommend a threat intelligence source for a specific context. ISACs are the correct answer when the scenario involves sharing intelligence with peers in the same industry sector.

---

## Section 5 — Exam-Day Strategy for Module 01

**[INSTRUCTOR ON CAMERA]**

Here is your exam-day strategy specifically for the threat, attack, and vulnerability questions on SY0-701.

First, before you read the answer choices, read the question stem and identify: Who is the threat actor? What CIA property is targeted? Is this active or passive? These three questions will eliminate at least two wrong answers in almost every Module 01 scenario.

Second, watch for trap vocabulary. The exam will use "vulnerability," "threat," and "risk" in the same question. Do not swap their definitions. A vulnerability is the weakness. A threat exploits the weakness. Risk is the probability times the impact.

Third, nation-state questions almost always involve long dwell time, advanced persistent threat behavior, or supply chain compromise. Organized crime questions almost always involve ransomware or financial theft. Hacktivists almost always involve DDoS or data leaking for public embarrassment. Script kiddie questions involve opportunistic scanning with known tools.

Fourth, for control classification questions — eliminate Physical first if the scenario describes software or policies, eliminate Administrative if the scenario describes automated enforcement, and eliminate Technical if the scenario describes a written rule or training program.

Fifth, use the process of elimination aggressively. The SY0-701 has 90 questions in 90 minutes. You have about one minute per question. On hard questions, eliminate what you know is wrong, make your best choice, flag it, and move on. Return to flagged questions after completing the test.

For comprehensive study on every SY0-701 objective, visit **professormesser.com**. Professor Messer's free study notes and video series are written specifically for the current exam version and are updated when the exam changes. This is the study resource I recommend above all others for this course.

---

## Closing

**[INSTRUCTOR ON CAMERA]**

That wraps up Module 01. You now have the vocabulary and the reasoning framework to attack — pun intended — the rest of this course. Every module from here builds on the CIA Triad, the controls framework, and the threat actor taxonomy we established today.

Complete the Reading Guide, do the Lab activity, take the Quiz, and post to the Discussion before the deadlines. See you in Module 02 — Social Engineering and Phishing.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 01 Part 2

Proprietary and Confidential. Not for disclosure outside of authorized course use.
