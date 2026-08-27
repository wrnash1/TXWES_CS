# Lab Activity: Module 16 — CySA+ CS0-003 Capstone Practice Exam

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Lab Overview

This capstone lab is a 20-question practice exam covering all four CySA+ CS0-003 exam domains. Questions are scenario-based and written to match the format, difficulty, and reasoning style of the actual CompTIA CySA+ exam.

Complete this practice exam under timed conditions: allow yourself 40 minutes (2 minutes per question). After completing it, review the answer key and distractor analysis carefully. For each question you answered incorrectly, note the domain and topic, then return to the relevant module reading guide for review.

**Estimated Time:** 40 minutes for exam, 30–60 minutes for answer review

**Tools Required:** No external tools needed. Complete on paper or in a word processor.

---

## Instructions

Read each question carefully. Identify what is being asked — the question stem often contains keywords like "first," "best," "most appropriate," and "most likely" that distinguish the correct answer from plausible distractors. Select one answer unless the question specifies multiple.

Do not look up answers during the timed portion. Work from your knowledge.

---

## Practice Exam Questions

### Question 1 — Domain 1: Security Operations

An analyst receives a SIEM alert for 500 failed SSH login attempts against a Linux server from a single external IP in 10 minutes, followed by one successful login. Which term best describes the attack represented by this event sequence?

- A) Credential stuffing — using a list of known username/password pairs
- B) Password spraying — trying one password against many accounts
- C) Brute force attack — systematically trying many passwords against one or more accounts until successful
- D) Dictionary attack — using common word lists only, not random character sequences

Submit answer: ______

---

### Question 2 — Domain 2: Vulnerability Management

A vulnerability scanner reports a critical CVE with a CVSS v3 base score of 9.8 affecting a server in a development lab that is isolated from the production network and the internet, contains only synthetic test data, and is used by two developers for testing only. A separate High vulnerability (CVSS 7.5) affects an internet-facing web server handling customer payment transactions. Which vulnerability should be remediated first?

- A) The CVSS 9.8 vulnerability, because critical vulnerabilities always take priority over high vulnerabilities
- B) The CVSS 7.5 vulnerability on the internet-facing payment server, because business context (public exposure, payment data, customer risk) makes it higher actual risk
- C) Both simultaneously, because SLAs require all critical and high vulnerabilities to be patched within the same window
- D) Neither — isolated development servers and internet-facing servers are both out of scope for standard patching

Submit answer: ______

---

### Question 3 — Domain 3: Incident Response

An analyst has confirmed a malware infection on a workstation. The malware is actively exfiltrating data. Which is the correct sequence of actions?

- A) Eradicate the malware → contain the host → recover the system → document the incident
- B) Contain the host to stop exfiltration → eradicate the malware → recover the system → conduct post-incident review
- C) Conduct post-incident review → contain the host → eradicate the malware → recover the system
- D) Document the incident in full → contain the host → eradicate the malware → recover the system

Submit answer: ______

---

### Question 4 — Domain 4: Reporting and Communication

A CISO asks an analyst to produce a report for the board of directors summarizing the organization's vulnerability management program performance over the past quarter. Which metric is MOST appropriate as the primary performance indicator for a board-level audience?

- A) A list of every vulnerability discovered during the quarter, sorted by CVSS score
- B) The percentage of critical and high vulnerabilities remediated within the defined SLA, with trend comparison to the previous quarter
- C) The number of vulnerability scans performed, broken down by scan type and target subnet
- D) The CVE IDs of the top 10 unpatched vulnerabilities with their technical exploitation details

Submit answer: ______

---

### Question 5 — Domain 1: Security Operations

A security analyst reviews a network flow record showing repeated outbound HTTPS connections from an internal server to the same external IP every 58–62 seconds for 72 hours, including overnight and on weekends, with consistent 2–4 KB payloads. Which threat indicator does this most strongly suggest?

- A) Brute force attack — the server is attempting to authenticate to an external service
- B) Data exfiltration via large HTTP transfers
- C) C2 beaconing — an automated, regularly timed connection consistent with malware check-in behavior
- D) Port scanning — the server is probing external services

Submit answer: ______

---

### Question 6 — Domain 3: Digital Forensics

A forensic analyst acquires a disk image from a compromised Windows system and loads it in Autopsy. The analyst needs to determine whether a specific executable was run on the system before it was deleted. Which artifact in Autopsy is most directly useful for proving the executable was run?

- A) The Windows Registry SOFTWARE hive
- B) The Windows Prefetch file for the executable
- C) The Windows Update log
- D) Browser history files

Submit answer: ______

---

### Question 7 — Domain 2: Vulnerability Management

A vulnerability scan report shows that a web server has an SSL/TLS certificate using SHA-1 hashing, TLS 1.0 and 1.1 enabled, and a self-signed certificate. The CVSS score for each finding ranges from 4.0 to 6.5. However, the server handles authentication for the organization's customer portal. A separate server hosting internal documentation has a Critical CVSS 9.1 finding for an outdated CMS with known exploits. Which finding represents the higher business risk?

- A) The internal documentation server — CVSS 9.1 is always higher priority than CVSS 4.0–6.5 findings
- B) The customer portal SSL/TLS findings — weak cryptography on authentication-handling infrastructure poses direct risk to customer credentials even at lower CVSS scores
- C) Both are equal risk because both affect production systems
- D) Neither requires immediate remediation because neither has been actively exploited

Submit answer: ______

---

### Question 8 — Domain 1: Threat Intelligence

A threat intelligence team receives an intelligence report containing STIX-formatted data including a campaign object, associated threat actor TTPs, and a list of malicious IP addresses and file hashes currently used in active attacks against healthcare organizations. The IOC data needs to be automatically ingested into the organization's SIEM. Which component of the STIX/TAXII ecosystem handles this automated sharing and ingestion?

- A) STIX — it handles both the data format and the transport mechanism
- B) TAXII — it is the transport protocol that defines how STIX-formatted intelligence is shared between platforms
- C) MISP — it replaces both STIX and TAXII for all intelligence sharing needs
- D) OpenIOC — it is the standardized format for all machine-readable threat intelligence

Submit answer: ______

---

### Question 9 — Domain 3: Incident Response

During a ransomware incident, the IR team discovers that the attacker has been present for 11 days before the encryption event. Which IR performance metric most directly measures this gap, and which phase failure does it reflect?

- A) MTTR — the Response function failed because analysts did not respond quickly enough
- B) MTTC — the Containment function failed because the attacker was not isolated in time
- C) MTTD — the Detection function failed because the attacker was present for 11 days before being identified
- D) Mean Time Between Incidents — the Prevention function failed because the same incident type recurred

Submit answer: ______

---

### Question 10 — Domain 2: Vulnerability Management

An analyst performs a non-credentialed external vulnerability scan of the organization's public-facing web application and finds no critical vulnerabilities. A credentialed internal scan performed the same day finds 14 critical vulnerabilities on the same server. What is the most likely explanation for this discrepancy?

- A) The external scanner is more accurate because it simulates real attacker perspective
- B) The internal scan is malfunctioning — false positives are causing inflated findings
- C) The non-credentialed scan can only see network-exposed services and lacks OS-level access, missing vulnerabilities in installed packages, services, and configurations only visible with authentication
- D) The credentialed scan must have used a different scanner version, causing incompatible results

Submit answer: ______

---

### Question 11 — Domain 1: Security Operations

A Tier 1 analyst receives an alert for unusual PowerShell activity on a developer workstation. Investigation shows the developer ran `powershell.exe -ExecutionPolicy Bypass -File build_script.ps1` as part of an authorized development build process. The analyst closes the alert as a false positive. Which action should the analyst take beyond just closing the ticket?

- A) Escalate to a Tier 3 analyst for secondary review before closing
- B) Document the finding and submit a tuning request to reduce false positives from authorized developer build scripts by scoping the detection rule to exclude the known-good process and user context
- C) Disable PowerShell monitoring entirely to prevent future alerts from developers
- D) Delete the build script from the developer's workstation to prevent future alerts

Submit answer: ______

---

### Question 12 — Domain 4: Reporting and Communication

After a significant data breach, the organization's CISO asks the security team to produce a post-incident report for the executive leadership team. Which section is MOST important to include to support future investment decisions and program improvement?

- A) A complete list of all IP addresses and domains associated with the attacker
- B) The technical CVE IDs of every vulnerability exploited during the attack
- C) Lessons learned — specific gaps identified, actions already taken, and concrete recommendations with cost estimates for preventing recurrence
- D) Raw SIEM log output showing the timeline of attacker activity

Submit answer: ______

---

### Question 13 — Domain 3: Digital Forensics

An analyst uses Volatility's `malfind` plugin and finds a suspicious memory region in `explorer.exe` containing executable code. The analyst wants to determine what network connections this injected code is maintaining. Which Volatility plugin is most appropriate for this follow-on investigation?

- A) `pslist` — to list all running processes
- B) `netscan` — to list active and recently closed network connections, filterable by process
- C) `dlllist` — to list DLLs loaded by explorer.exe
- D) `cmdline` — to view command-line arguments for explorer.exe

Submit answer: ______

---

### Question 14 — Domain 1: Security Operations

An analyst is building a SOAR playbook for phishing alerts. The playbook should automatically quarantine the email across all inboxes if the sender domain is confirmed malicious, and create an IR ticket. Which design element ensures the playbook does not accidentally quarantine emails from a legitimate domain that is temporarily misclassified in the threat intelligence feed?

- A) Set the playbook to run only on Tuesdays when the analyst team is at full staff
- B) Require a confidence threshold — only auto-quarantine if the domain is classified as malicious by at least three independent threat intelligence sources
- C) Disable the quarantine action entirely and route all phishing alerts to analyst review
- D) Quarantine emails from all external senders to eliminate false positives

Submit answer: ______

---

### Question 15 — Domain 2: Vulnerability Management

A security team runs a vulnerability scan and finds that an application server is running OpenSSL 1.0.2 (end-of-life, no longer receiving security patches). The development team says updating OpenSSL would require six months of application testing before production deployment. Which approach best addresses the risk while the long-term remediation is in progress?

- A) Do nothing — the server is internal and therefore low risk
- B) Take the server offline until the update can be applied
- C) Implement compensating controls such as network segmentation isolating the server, enhanced monitoring for exploitation attempts, and a WAF rule blocking known exploitation patterns for known OpenSSL vulnerabilities
- D) Purchase a new server with a current OS version and migrate the application immediately

Submit answer: ______

---

### Question 16 — Domain 1: Security Operations

An analyst examines a Windows Security event log and finds repeated Event ID 4648 entries showing `jdoe` authenticating to 12 different servers using explicit credentials over a 4-minute period. Event ID 4624 for `jdoe` shows a normal workstation logon earlier that morning. What does this pattern most likely indicate?

- A) The user jdoe is performing normal administrative tasks requiring authentication to multiple servers
- B) Pass-the-hash or credential theft — an attacker using jdoe's harvested credentials to authenticate to multiple servers in rapid succession, consistent with lateral movement
- C) A software deployment system running automated updates using jdoe's service account
- D) A failed MFA enrollment causing repeated authentication prompts

Submit answer: ______

---

### Question 17 — Domain 3: Incident Response

During the lessons learned meeting following a ransomware incident, the IR team identifies that the attacker gained initial access through a phishing email that bypassed email filtering because the sender domain had a high reputation score (registered 3 years ago, previously used for legitimate email). The team recommends a new control. Which control MOST directly addresses this specific attack vector?

- A) Deploy an EDR solution on all endpoints
- B) Implement sandboxing for email attachments and links that detonates them in an isolated environment before delivery, regardless of sender reputation
- C) Increase the frequency of vulnerability scans
- D) Deploy a network intrusion detection system

Submit answer: ______

---

### Question 18 — Domain 4: Reporting and Communication

A security analyst has identified a critical vulnerability in the organization's public-facing login portal that allows authentication bypass. The analyst needs to brief the CTO (technical background, operational focus) and the CFO (financial background, risk focus) on the same finding. Which approach is most appropriate?

- A) Give both executives identical technical briefing documents to ensure consistent messaging
- B) For the CTO: describe the technical mechanism, affected systems, and specific remediation steps. For the CFO: describe business risk, potential regulatory fine exposure, customer trust impact, and cost of remediation vs. cost of breach
- C) Escalate only to the CISO and let the CISO communicate to both executives
- D) Send the full CVSS score report to both executives without additional context

Submit answer: ______

---

### Question 19 — Domain 1: Threat Hunting

A threat hunter has completed a hunt for evidence of T1136.001 (Create Account: Local Account) — attacker-created local user accounts — across all Windows endpoints. The hunt searched 30 days of Security event logs (Event ID 4720) and found no unauthorized account creation events. Which statement best represents how this finding should be recorded and used?

- A) The negative finding should not be documented since nothing was discovered
- B) The negative finding confirms the hypothesis was tested, establishes a 30-day baseline, and should be documented with the data sources, time range, and queries used — a new detection rule for Event ID 4720 on non-standard accounts should also be proposed if one does not exist
- C) The negative finding means the organization has no insider threat risk and no further hunting for this technique is needed
- D) The negative finding indicates the EDR platform is malfunctioning because it should have found something

Submit answer: ______

---

### Question 20 — Domain 2: Vulnerability Management

An organization's vulnerability management program has the following remediation SLAs: Critical: 15 days, High: 30 days, Medium: 90 days, Low: 180 days. A quarterly report shows that 78% of Critical vulnerabilities were remediated within SLA, 91% of High vulnerabilities were remediated within SLA, and 34% of Medium vulnerabilities were remediated within SLA. Which finding from this data most requires a program management response?

- A) High vulnerability SLA compliance at 91% is too low and should be 100%
- B) Critical vulnerability SLA compliance at 78% means that 22% of the most severe vulnerabilities exceeded the 15-day remediation window — this is the most important finding requiring immediate attention
- C) Medium vulnerability SLA compliance at 34% indicates a significant backlog of medium vulnerabilities that requires resource allocation or SLA adjustment
- D) The data is insufficient to draw any conclusions — the total number of vulnerabilities in each category is needed

Submit answer: ______

---

## Answer Key

Submit your answers before reviewing this section.

1. C — Brute force (systematic trial until success)
2. B — Business context overrides raw CVSS score
3. B — Contain → Eradicate → Recover → Post-Incident (NIST phases)
4. B — SLA compliance rate is the board-appropriate performance metric
5. C — Consistent interval + consistent payload = C2 beaconing
6. B — Prefetch files prove execution history
7. B — Business context (customer auth, credential risk) elevates medium findings
8. B — TAXII is the transport protocol; STIX is the format
9. C — 11-day gap before detection = MTTD failure
10. C — Non-credentialed scans lack OS-level visibility
11. B — False positive → documentation + tuning request
12. C — Lessons learned with recommendations supports investment decisions
13. B — `netscan` reveals network connections by process
14. B — Multi-source confidence threshold reduces false automation
15. C — Compensating controls bridge the remediation gap
16. B — Rapid multi-server auth = lateral movement via credential theft
17. B — Sandbox detonation catches reputation-bypassing attachments
18. B — Tailor communication to audience role and concern
19. B — Negative findings require documentation and detection rule proposal
20. B — Critical SLA breach is highest priority despite medium backlog size

---

## Answer Review Instructions

For each incorrect answer: record the question number, the domain, and the topic in a study log. Return to the relevant module's reading guide section for that topic and re-read it. Then re-read this question and understand why the correct answer is right and why your answer was wrong.

Target: 16 correct or higher before taking the actual CySA+ exam.

---

## Part 9 — Challenge Exercise

### Challenge 1: Cross-Domain Integration Scenario

The following scenario spans all four CySA+ exam domains. Read the full scenario, then answer all questions.

**Scenario**: At 03:47 AM on a Tuesday, a SIEM correlation rule fires on the following events occurring within 8 minutes:

- Event A: Successful VPN authentication from `rsmith@corp.local` sourced from an IP in Malaysia (last known login was from Texas, 6 hours prior)
- Event B: Process creation on `PAYROLL-SRV-02` — `powershell.exe -enc [300-character base64 string]` with parent `wmiprvse.exe`
- Event C: 14 Event ID 4624 Type 3 logons to `PAYROLL-SRV-02` from the VPN IP within 4 minutes
- Event D: `PAYROLL-SRV-02` generating outbound HTTPS connections to `185.44.77.210:443` — 847 KB transferred outbound in 6 minutes

A CISA advisory published 3 days ago identified `185.44.77.210` as a known C2 IP for threat actor group TA-PAY, which targets payroll processing systems for financial fraud.

**Domain 1 Questions (Security Operations):**

1. Map each of the four events (A, B, C, D) to the most specific MITRE ATT&CK technique and tactic. For Event B, explain what `wmiprvse.exe` as a parent process indicates (reference T1047). For Event D, explain what the outbound byte volume suggests about the direction of data flow.
2. Write the SIEM correlation rule logic (in plain language, not SPL or KQL syntax) that would have detected this attack chain as a single correlated incident rather than four independent alerts. Specify the time window, the required event types, and the field correlations (e.g., same source IP, same destination hostname) required.
3. Design a SOAR playbook (enrichment-first, decision-gated) for this alert type. List at minimum five automated enrichment steps, the decision logic for automatic escalation vs. analyst review, and the specific high-impact actions that require analyst approval before execution.

**Domain 2 Questions (Vulnerability Management):**

4. The post-incident investigation reveals that the attacker's WMI-based lateral movement (Event B) was possible because `PAYROLL-SRV-02` had an unpatched vulnerability (CVE-2023-XXXX, CVSS 8.8) that allowed WMI remote command execution without authentication. The CVE was published 47 days ago with a 30-day Critical/High SLA. Calculate the SLA breach duration and classify the vulnerability management program failure — was it a scanning failure (vulnerability never discovered), a prioritization failure (discovered but deprioritized), or a remediation execution failure (prioritized but not completed)?
5. Propose three specific process improvements to prevent this specific SLA failure pattern from recurring. For each, specify the process gap it addresses and which team (security, IT operations, change management) is responsible.

**Domain 3 Questions (Incident Response and Forensics):**

6. Using NIST 800-61 phases, document the correct sequence of analyst actions from the moment the SIEM alert fires through eradication completion. Include at minimum: the triage actions, the containment decision (what to isolate, when, and why), evidence preservation considerations (volatile evidence must be captured before isolation), notification requirements (legal, HR, executive), and the eradication steps.
7. For forensic analysis of `PAYROLL-SRV-02`, you have 15 minutes before the server must be isolated. List the volatile evidence you will collect in priority order, the tool you will use for each, and what each artifact would prove about the attacker's activity.

**Domain 4 Questions (Reporting and Communication):**

8. Write a 90-second verbal escalation script for handing this incident from the Tier 1 analyst who received the SIEM alert to the Tier 2 analyst. The script must cover: what the alert shows, what enrichment has been done, what the confirmed indicators are, what immediate containment you recommend, and what the Tier 2 analyst should investigate first.
9. Write an executive summary paragraph (5–7 sentences) for the CISO describing this incident, its potential business impact (payroll data compromise, regulatory exposure), what has been done in the first 30 minutes, and what decisions the CISO needs to make in the next hour.

### Challenge 2: Comprehensive Exam Skills Self-Assessment

Answer each of the following 10 rapid-response questions without referring to notes. These questions cover the highest-frequency topics across all four CySA+ domains. After answering, evaluate your responses against the answer key below.

1. Name the four NIST 800-61 IR phases in order.
2. What does MTTD stand for and what does a 30-day MTTD indicate about the Detection function?
3. Name the Volatility plugin that detects process injection and describe what signature it looks for.
4. What is the difference between CVSS Base Score and CVSS Environmental Score?
5. Define "chain of custody" and name one action that breaks it.
6. What does TLP:RED mean and who may receive TLP:RED-marked intelligence?
7. Name three Windows artifacts that prove a program executed, even after the executable is deleted.
8. What is the primary functional difference between a SIEM and a SOAR?
9. In the Pyramid of Pain, which indicator type is at the top and why is it at the top?
10. Name the MITRE ATT&CK technique for using `certutil.exe` to decode malicious payloads and explain why this is classified as Defense Evasion.

**Self-Assessment Answer Key:**

1. Preparation → Detection and Analysis → Containment, Eradication, and Recovery → Post-Incident Activity
2. Mean Time to Detect — a 30-day MTTD means the attacker was undetected for 30 days after gaining access; this represents a critical Detection phase failure
3. `malfind` — looks for memory regions with PAGE_EXECUTE_READWRITE permissions that contain an MZ header (PE executable code signature), indicating process injection
4. CVSS Base Score measures the inherent technical severity of the vulnerability in isolation; Environmental Score adjusts the base score based on the specific deployment context (asset criticality, compensating controls, exploit maturity in the environment)
5. Chain of custody is the documented, unbroken record of every person who handled a piece of evidence; broken by: analyzing evidence without logging access, failing to hash evidence at collection, transferring evidence without documentation, or allowing unauthorized access
6. TLP:RED means the information is restricted to the specific individuals (not organizations) to whom it was shared in the original disclosure; it may not be forwarded beyond the original recipients
7. Prefetch files (`C:\Windows\Prefetch\`), Windows Registry ShimCache/AppCompatCache, Amcache.hve
8. A SIEM collects and correlates log data to generate alerts; a SOAR receives those alerts, enriches them with external intelligence, executes automated decision logic, and triggers response actions across integrated tools
9. TTPs (Tactics, Techniques, and Procedures) — at the top because they represent the attacker's behavior and operational habits, which are the hardest attributes to change; forcing an attacker to change their TTPs requires significant re-tooling and retraining
10. T1140 (Deobfuscate/Decode Files or Information) — certutil is a trusted, signed Windows binary; using it to decode malicious content bypasses application control tools that whitelist Microsoft-signed binaries, making it a defense evasion technique

### Reflection Questions

1. Having completed all 16 modules of CIS-4332, identify the two topic areas where you feel least confident and describe a specific study plan (resources to review, practice activities, time allocation) for each area that you will complete before taking the CySA+ CS0-003 exam. Be specific about which modules, which sections, and which practice questions you will prioritize.
2. The CySA+ exam uses scenario-based questions that often include a "most appropriate" or "best first step" qualifier. Describe the reasoning framework you will use when all four answer choices appear plausible — what criteria do you apply to eliminate distractors, and how do NIST frameworks and ATT&CK help you select the correct answer in ambiguous scenarios?
