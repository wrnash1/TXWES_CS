# Quiz: Module 11 — Incident Response for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Instructions

Select the best answer for each question. Distractor analysis is provided after each question to support exam preparation.

---

## Question 1

According to NIST SP 800-61 Rev. 2, which of the following correctly lists the four phases of the incident response lifecycle in order?

- A) Detection, Containment, Eradication, Recovery
- B) Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity
- C) Identification, Protection, Detection, Response
- D) Triage, Containment, Lessons Learned, Reporting

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: This list omits Preparation and Post-Incident Activity, which are both defined phases in NIST 800-61. Preparation is the foundation of the entire framework; without it the other phases are reactive and poorly coordinated.
- Why B is correct: NIST SP 800-61 Rev. 2 defines exactly these four phases in this order. The exam expects precise recall of this framework. Note that phases three and four are often grouped as one phase in the document.
- Why C is incorrect: This sequence resembles the NIST Cybersecurity Framework five functions (Identify, Protect, Detect, Respond, Recover), not the IR lifecycle phases from 800-61. Confusing these two frameworks is a common exam mistake.
- Why D is incorrect: Triage is an activity within Detection and Analysis, not a standalone phase. This sequence reflects informal incident handling language rather than the formal NIST framework.

---

## Question 2

A security analyst receives a SIEM alert for unusual outbound traffic from a finance workstation. After initial review the analyst determines the traffic is a scheduled cloud backup job. Which term best describes this outcome?

- A) True positive — a real threat was correctly identified
- B) False negative — a real threat was missed
- C) False positive — the alert fired but no actual incident occurred
- D) Benign true positive — malicious activity occurred but caused no harm

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A true positive means the alert correctly identified actual malicious activity. The cloud backup traffic is legitimate, so the alert did not detect a real threat.
- Why B is incorrect: A false negative means malicious activity occurred but was not detected. In this scenario there was no malicious activity — the alert fired on a legitimate event.
- Why C is correct: A false positive occurs when an alert fires but the activity is not malicious. The scheduled backup is legitimate traffic. This is the most common category of alert in mature SOC environments and the primary driver of analyst alert fatigue.
- Why D is incorrect: A benign true positive describes a situation where the alerted activity was technically malicious but caused no impact (for example, malware that failed to execute). The backup job was never malicious.

---

## Question 3

During triage of a confirmed ransomware incident, the analyst must choose between immediately isolating the affected host (which will destroy volatile memory evidence) or preserving memory before isolation (which allows ransomware to continue encrypting for several additional minutes). Which factor should most heavily influence this decision?

- A) The analyst's personal preference for forensic completeness over business continuity
- B) The organization's incident response playbook guidance for ransomware, which defines this tradeoff explicitly
- C) The vendor recommendation printed in the EDR product documentation
- D) The number of files already encrypted, with isolation preferred only when fewer than 100 files are affected

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Personal preference is never the appropriate basis for IR decisions during an active incident. Decisions must be grounded in policy, procedure, and organizational risk tolerance — not individual judgment.
- Why B is correct: The ransomware playbook exists precisely to resolve this tradeoff before the incident occurs, when analysts can think clearly without time pressure. Good playbooks define whether evidence preservation or immediate containment takes priority for each incident type. Following the playbook ensures consistent, policy-aligned decision-making.
- Why C is incorrect: Vendor documentation addresses product functionality, not organizational policy decisions. The tradeoff between evidence and containment is a business risk decision, not a product feature.
- Why D is incorrect: A file count threshold is not a recognized IR decision framework. Ransomware can encrypt thousands of files per minute; a 100-file threshold would be meaningless in practice.

---

## Question 4

Which of the following is the primary purpose of the Post-Incident Activity phase in NIST SP 800-61?

- A) To notify affected customers and regulatory bodies of the data breach within required timeframes
- B) To conduct a lessons learned review, identify gaps in controls and process, and implement corrective actions
- C) To archive all incident evidence to long-term storage for future legal proceedings
- D) To restore affected systems to full production operation and verify business function recovery

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Regulatory notification is a legal obligation that occurs during and immediately after containment, not a purpose of the post-incident phase. Notification timing is often driven by regulatory deadlines independent of the NIST phase structure.
- Why B is correct: NIST 800-61 defines the purpose of Post-Incident Activity as learning from the incident to improve future response. This includes a formal lessons learned meeting, timeline reconstruction, gap identification, and action items. Organizations that skip this phase repeat the same failures.
- Why C is incorrect: Evidence archiving is a documentation and chain-of-custody activity that occurs throughout the incident, not specifically in the post-incident phase. It supports future proceedings but is not the purpose of this phase.
- Why D is incorrect: Restoring systems to production is Recovery, the final step of Phase 3. Post-Incident Activity begins after recovery is complete and business operations have resumed.

---

## Question 5

An analyst is documenting an incident and writes the following entry: "It looks like the attacker probably moved laterally to the database server at some point during the night." Which documentation problem does this entry demonstrate?

- A) The entry is too long and should be summarized to a single sentence
- B) The entry uses vague language, an unsupported inference, and lacks a timestamp — all of which undermine the record's evidentiary value
- C) The entry uses first-person perspective, which is prohibited in incident documentation
- D) The entry does not include the analyst's employee ID number, which is required by NIST 800-61

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Entry length is not the problem. Concise entries are good practice, but shortening this entry would remove detail, not fix the core issues.
- Why B is correct: Three distinct documentation failures are present. "It looks like" is vague language that signals uncertainty without evidence. "probably moved laterally" is an unsupported inference presented as fact. "at some point during the night" provides no precise timestamp. Incident records must be factual, timestamped, and clearly distinguish observed evidence from analyst inferences.
- Why C is incorrect: First-person perspective is acceptable in incident documentation. The analyst is describing their own observations and actions. What matters is accuracy and precision, not grammatical perspective.
- Why D is incorrect: NIST 800-61 does not specify employee ID requirements in documentation entries. This is an invented procedural requirement.

---

## Question 6

A security analyst receives an escalation from a Tier 1 analyst regarding suspicious authentication events. Which of the following conditions would most strongly justify the Tier 1 analyst escalating immediately rather than continuing independent investigation?

- A) The alert was generated by a rule that has historically produced false positives
- B) The affected user account belongs to a member of the IT help desk team
- C) The authentication anomaly appears to involve a domain administrator account and spans three geographically separated offices simultaneously
- D) The alert was triggered outside of normal business hours

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A history of false positives is a reason to investigate carefully, not to escalate immediately. The analyst should perform triage to determine if this instance is also a false positive before consuming senior resources.
- Why B is incorrect: Help desk accounts have elevated privileges but are not the highest-priority escalation trigger. The scope and nature of the activity, not just the account type, drive escalation decisions.
- Why C is correct: Two factors here independently justify immediate escalation and together make it urgent. Domain administrator compromise gives an attacker maximum blast radius across the entire environment. Simultaneous activity across three geographically separated offices indicates either a coordinated attack or account use from multiple locations at once — both are high-severity indicators that require senior IR involvement immediately.
- Why D is incorrect: After-hours alerts are a useful anomaly indicator and warrant investigation, but after-hours timing alone is not an escalation criterion. Many legitimate administrative tasks occur outside business hours.

---

## Question 7

What does the metric "Mean Time to Contain" (MTTC) measure in an incident response program?

- A) The average time from when a threat actor first gains access to a system until the organization detects the intrusion
- B) The average time from when an incident is detected until all affected systems are fully restored to normal operation
- C) The average time from when an incident is confirmed until containment actions have successfully stopped the spread of the threat
- D) The average time between recurring incidents of the same type across a fiscal year

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: The time from initial access to detection is called "dwell time" — a critical threat intelligence metric but not MTTC.
- Why B is incorrect: The time from detection to full restoration describes Mean Time to Recover or Mean Time to Resolve, which encompasses eradication and recovery as well as containment.
- Why C is correct: MTTC measures the containment phase specifically — how quickly analysts can stop an incident from spreading after it is confirmed. It is one of the three primary IR effectiveness metrics alongside MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond).
- Why D is incorrect: Recurrence rate over time is a different metric that measures program effectiveness at preventing repeat incidents. It has no relationship to response timing.

---

## Question 8

Which document format is recommended by the security community for sharing Indicators of Compromise between organizations and threat intelligence platforms?

- A) CSV (Comma-Separated Values) with a custom column schema defined by the sharing organization
- B) STIX (Structured Threat Information eXpression) formatted according to the OASIS standard
- C) Plain-text email with IoCs listed one per line and annotated with analyst comments
- D) JSON with a proprietary schema defined by the SIEM vendor

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: CSV is a simple data format with no standardized schema for threat intelligence. Custom schemas are not interoperable across organizations or platforms without translation work.
- Why B is correct: STIX is the industry-standard format for representing threat intelligence including IoCs, threat actors, campaigns, and TTPs. Paired with TAXII (the transport protocol), STIX enables automated, machine-readable IoC sharing between organizations, ISACs, and threat intelligence platforms. CySA+ expects you to know STIX as the IoC sharing standard.
- Why C is incorrect: Plain-text email is informal, not machine-readable, and not interoperable with automated threat intelligence systems. It is used in ad-hoc communication but is not a recommended standard.
- Why D is incorrect: Proprietary SIEM schemas are vendor-specific and not interoperable. They may be used for internal data storage but cannot be used for cross-organizational sharing without conversion.

---

## Question 9

A security analyst has confirmed a malware infection on a workstation, removed the malicious executable, and verified the system is clean. Three days later the same malware reappears on the same workstation. Which eradication failure most likely caused this recurrence?

- A) The analyst failed to change the user's Active Directory password during recovery
- B) A persistence mechanism such as a scheduled task or registry run key was not identified and removed during eradication
- C) The antivirus signature database was not updated before the eradication scan was performed
- D) The analyst did not notify the user that their system had been infected

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Password changes address credential compromise but do not affect malware persistence. Malware that reinstalls itself does so through execution mechanisms, not authentication.
- Why B is correct: Malware recurrence within days of eradication is the classic indicator of an unremoved persistence mechanism. Common mechanisms include scheduled tasks, registry Run/RunOnce keys, WMI event subscriptions, service registrations, startup folder entries, and browser extensions. If only the executable is removed without eliminating the dropper or re-execution trigger, the malware returns on the next system restart or trigger event.
- Why C is incorrect: Outdated signatures could allow re-infection from an external source but would not explain the malware reappearing on a cleaned system that was not re-exposed. The recurrence pattern points to an internal persistence mechanism, not a signature gap.
- Why D is incorrect: User notification is a communication step that may help prevent future incidents but has no technical relationship to the eradication of an existing infection.

---

## Question 10

An analyst is performing the scoping phase of a confirmed intrusion. The initial indicator is a single compromised workstation. Which action is most critical to determine whether the incident is contained to that one host?

- A) Run a full vulnerability scan against the compromised workstation to identify all exploitable services
- B) Review Active Directory authentication logs and network flow data to identify any lateral movement originating from the compromised host
- C) Immediately reimage the workstation from a known-good backup and monitor for recurrence
- D) Interview the workstation's primary user to determine whether they clicked a suspicious link

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Vulnerability scanning the compromised host identifies attack surface but does not answer whether the attacker has already moved to other systems. Scope determination requires looking outward from the compromised host, not inward.
- Why B is correct: Lateral movement is the primary scoping concern after initial compromise is confirmed. Reviewing AD authentication logs for logins from the compromised host's IP to other internal systems, and reviewing network flows for internal SMB, RDP, or other protocol connections, directly reveals whether the attacker has moved beyond the initial foothold. This is the correct scoping action.
- Why C is incorrect: Reimaging before scoping is a containment and recovery action, not a scoping action. Reimaging before scope is determined may eliminate the only host with evidence of lateral movement, leaving the analyst blind to the full incident extent.
- Why D is incorrect: User interviews can provide useful context about the infection vector but do not determine whether lateral movement has occurred. Scope determination requires technical log evidence, not user recollection.

---

## Question 11 (5 points)

An analyst is handling a confirmed phishing-delivered malware incident. The malware has established C2 beaconing. The analyst wants to stop ongoing C2 communication without shutting down the system, in order to preserve volatile memory evidence. Which containment action achieves both goals?

- A) Disconnect all network cables from the building's core switch
- B) Use the EDR agent to isolate the host from the network while keeping the OS running, preserving RAM for forensic acquisition
- C) Change the system's DNS server to 127.0.0.1 to prevent domain resolution
- D) Enable the Windows Firewall with default rules on the affected workstation

Correct Answer: B

Distractor Analysis:

- A is incorrect. Disconnecting the entire building's core switch would affect all users, disrupting business operations far beyond the scope of a single workstation incident. This is a disproportionate containment action.
- B is correct. EDR host isolation (available in most modern EDR platforms including CrowdStrike, SentinelOne, and Microsoft Defender for Endpoint) blocks all network communication for the isolated host while keeping the operating system running. This stops C2 beaconing while preserving the running state — RAM, active processes, network connections — for subsequent forensic acquisition.
- C is incorrect. Changing the DNS server to localhost prevents DNS resolution but does not stop C2 communication if the malware uses hardcoded IP addresses rather than domain names. This is a partial, unreliable containment measure.
- D is incorrect. Enabling Windows Firewall with default rules may not block the specific outbound connections used by the malware, particularly if the C2 uses common ports like 80 or 443. Default firewall rules are not the same as host isolation.

---

## Question 12 (5 points)

According to NIST SP 800-61, which IR phase includes activities such as acquiring forensic evidence, determining the attack vector, and assessing the full scope of systems affected?

- A) Phase 1 — Preparation
- B) Phase 2 — Detection and Analysis
- C) Phase 3 — Containment, Eradication, and Recovery
- D) Phase 4 — Post-Incident Activity

Correct Answer: B

Distractor Analysis:

- A is incorrect. Phase 1 (Preparation) is proactive — it involves building IR capabilities before incidents occur: writing playbooks, training staff, deploying tools, and establishing communication protocols. It does not involve responding to a specific active incident.
- B is correct. Phase 2 (Detection and Analysis) encompasses detecting the incident, triaging alerts, acquiring forensic evidence, determining the initial attack vector, scoping affected systems, and classifying the incident severity. This is where the investigation and scope determination work occurs.
- C is incorrect. Phase 3 (Containment, Eradication, and Recovery) begins after the scope is understood. It focuses on stopping the attack, removing the threat, and restoring operations — not on initial investigation and evidence collection.
- D is incorrect. Phase 4 (Post-Incident Activity) occurs after the incident is fully resolved and involves lessons-learned reviews, metrics reporting, and playbook updates.

---

## Question 13 (5 points)

An incident timeline is being reconstructed for a compromise that began with a phishing email. The analyst has confirmed the following events but is missing the timestamps for two of them. Which source would most reliably provide the exact timestamp for when the malicious attachment was first opened on the victim workstation?

- A) The email gateway's message delivery timestamp
- B) Windows Security Event Log Event ID 4688 (Process Create) for the process spawned by the opened document
- C) The network firewall's connection log showing the first outbound connection from the victim host
- D) The user's recollection of when they opened the email

Correct Answer: B

Distractor Analysis:

- A is incorrect. The email gateway's delivery timestamp records when the email arrived in the mail server — not when the user opened the attachment. There can be a gap of hours or days between email delivery and attachment opening.
- B is correct. Windows Security Event ID 4688 (with command-line auditing enabled) records the exact timestamp, process name, and parent process when a new process is created. When a malicious document is opened, it spawns child processes (cmd.exe, powershell.exe, etc.) that generate 4688 events with precise timestamps — the most reliable source for the exact moment of execution.
- C is incorrect. The first outbound network connection from the host may occur seconds to minutes after the document is opened, depending on the malware's behavior. This provides a lower bound but not the precise attachment-opening timestamp.
- D is incorrect. User recollection of when they opened an email or attachment is imprecise and unreliable for forensic timeline accuracy. Human memory cannot provide minute-level precision consistently.

---

## Question 14 (5 points)

During an active incident response, a Tier 2 analyst discovers that the attacker accessed the organization's Active Directory server and ran `dcsync` to extract password hashes for all domain accounts. What is the correct immediate response action for this finding?

- A) Reset only the compromised user's password and close the ticket
- B) Initiate a full Active Directory credential reset — all domain account passwords including service accounts, privileged accounts, and the KRBTGT account (twice) — because the attacker now has the ability to forge Kerberos tickets
- C) Run a vulnerability scan on the Active Directory server to identify how access was obtained
- D) Restore the Active Directory server from last night's backup to remove the dcsync artifact

Correct Answer: B

Distractor Analysis:

- A is incorrect. Resetting only the compromised user's password is wholly insufficient. DCSync extracts hashes for ALL domain accounts. Every account's hash is now compromised, and the attacker can use those hashes for pass-the-hash attacks, crack them offline, or forge Golden Tickets using the KRBTGT hash.
- B is correct. DCSync (ATT&CK T1003.006) is one of the most severe IR findings because the attacker possesses Kerberos Key Distribution Center (KDC) secrets. The KRBTGT account hash enables Golden Ticket attacks — indefinitely valid forged Kerberos tickets. Resetting KRBTGT twice (to invalidate all cached tickets) and resetting all privileged and service account passwords is the required response. Replacing all credentials is the only way to eliminate the attacker's ability to authenticate.
- C is incorrect. Vulnerability scanning is a post-containment activity. Running a scan during active credential compromise does not address the immediate threat of all domain hashes being in the attacker's possession.
- D is incorrect. Restoring AD from backup does not remove the extracted hashes from the attacker's possession. The hashes are already exfiltrated and usable. Restoration may also be inappropriate if the backup itself predates detectable attacker activity.

---

## Question 15 (5 points)

An analyst is classifying an incident's severity. The affected system is a payment card processing server, 14,000 customer card records may be exposed, the system has been offline for 6 hours causing transaction processing failure, and the initial access vector has not yet been identified. Which severity level best fits this incident?

- A) Low — only one server is affected
- B) Medium — the server is now offline so the threat is contained
- C) Critical — combination of high-value data exposure, significant business impact, regulatory implications, and unresolved attack vector indicating potential ongoing attacker access
- D) High — the incident is contained to a single system without evidence of lateral movement

Correct Answer: C

Distractor Analysis:

- A is incorrect. Severity is not determined by the number of affected systems alone. A single system containing payment card data for 14,000 customers and causing $X per hour in transaction losses is not a Low severity incident by any established severity framework.
- B is incorrect. The system being offline does not mean the threat is contained — the attacker may have already exfiltrated data, and the initial access vector is unknown, meaning other systems may be at risk. The business impact of ongoing transaction failure also increases severity.
- C is correct. Multiple severity multipliers are present: critical asset type (payment processing), potential data exposure triggering PCI DSS notification requirements, significant business continuity impact (6 hours of transaction downtime), and unknown attack vector (indicating potential ongoing exposure). This combination maps to Critical severity in virtually all established severity frameworks.
- D is incorrect. "No lateral movement detected" reduces the scope concern but does not reduce the severity given the data exposure, regulatory implications, and business impact. Severity and scope are distinct assessments.

---

## Question 16 (5 points)

What is the primary purpose of an IR playbook, and how does it differ from a general incident response plan?

- A) An IR plan is a technical document; a playbook is an executive summary of the plan
- B) An IR plan defines the overall IR program, governance, roles, and general process; a playbook is a step-by-step procedural guide for responding to a specific incident type
- C) A playbook applies to all incident types; an IR plan is specific to ransomware
- D) They are identical documents with different names used in different organizations

Correct Answer: B

Distractor Analysis:

- A is incorrect. This reverses the relationship. An IR plan is the governance and strategic document. A playbook is a tactical, specific, operational procedure — not an executive summary.
- B is correct. An IR plan establishes the overall program: organizational roles and responsibilities, communication escalation paths, legal and regulatory obligations, and general process phases. A playbook (or runbook) is a specific, action-by-action procedure for a defined incident type — such as phishing response, ransomware response, or insider threat response. Playbooks are derived from and reference the IR plan.
- C is incorrect. Playbooks are incident-type specific. A ransomware playbook is different from a phishing playbook which is different from a DDoS playbook. The IR plan provides the overarching framework that all playbooks follow.
- D is incorrect. While terminology varies by organization, the plan/playbook distinction reflects genuinely different levels of specificity and operational detail. They serve different purposes.

---

## Question 17 (5 points)

During the scoping phase of a ransomware incident, an analyst determines that 47 servers are encrypted. The analyst must identify additional systems that may be infected but not yet encrypted. Which data source is most useful for finding additional potentially compromised systems?

- A) The vulnerability scanner's most recent scan report showing which servers have Critical CVEs
- B) Network flow data showing internal lateral movement from the first confirmed encrypted server over the past 72 hours
- C) The organization's asset inventory spreadsheet listing all servers and their IP addresses
- D) A query of the ticketing system for open change requests in the past month

Correct Answer: B

Distractor Analysis:

- A is incorrect. Vulnerability scan results show what CVEs exist on systems — not whether those systems were accessed by the attacker. Unpatched systems are not necessarily compromised just because they could be exploited.
- B is correct. Ransomware typically pre-stages lateral movement before deploying encryption — often operating for days before the encryption payload activates. Network flow data showing internal lateral movement (RDP, SMB, WMI) originating from confirmed compromised systems over the previous 72 hours is the most direct evidence of which systems the attacker may have accessed prior to triggering the ransomware.
- C is incorrect. An asset inventory lists what systems exist — it does not indicate which ones the attacker accessed. It is useful for understanding scope boundaries but does not identify compromised systems.
- D is incorrect. Change requests in the ticketing system are authorized change records. Attacker lateral movement would not appear in the change management system.

---

## Question 18 (5 points)

A lessons-learned review is conducted two weeks after a ransomware incident. The review identifies that the attack was initially detected via a user phone call to the help desk, not via any automated SIEM alert. What detection gap does this finding most clearly indicate?

- A) The SOC needs more Tier 1 analysts to handle higher alert volumes
- B) The SIEM lacks behavioral detection rules that would have identified the attacker's pre-encryption reconnaissance and lateral movement activity during the 72-hour dwell period
- C) The help desk staff need more security awareness training to ask better questions when users report problems
- D) The organization needs to purchase a more expensive EDR tool

Correct Answer: B

Distractor Analysis:

- A is incorrect. The problem is not alert volume — the SIEM generated no relevant alerts at all during 72 hours of attacker activity. Adding analysts to triage a queue that is not generating true positive alerts would not close the detection gap.
- B is correct. A 72-hour dwell period with no SIEM alerts despite active lateral movement indicates that the detection rules did not cover the attacker's activity. Behavioral rules for lateral movement (RDP to many hosts, SMB enumeration, DCSync, scheduled task creation across multiple systems) should have generated alerts. The lessons-learned action item is to develop and tune behavioral detection coverage for pre-ransomware reconnaissance patterns.
- C is incorrect. Help desk training is a useful complementary control but does not address the fundamental SIEM detection gap. The goal of a mature SOC is automated detection, not reliance on user phone calls.
- D is incorrect. Purchasing a different EDR tool is a potential contributing action, but the root cause identified is a lack of detection rules — not tool capability. The existing toolset likely could have detected the activity if properly configured.

---

## Question 19 (5 points)

Which NIST SP 800-61 phase is specifically designed to prevent a recurrence of the same type of incident by identifying root causes and implementing process improvements?

- A) Phase 1 — Preparation
- B) Phase 2 — Detection and Analysis
- C) Phase 3 — Containment, Eradication, and Recovery
- D) Phase 4 — Post-Incident Activity

Correct Answer: D

Distractor Analysis:

- A is incorrect. Phase 1 (Preparation) builds IR capabilities before incidents occur. It does not analyze the root cause of a specific resolved incident.
- B is incorrect. Phase 2 (Detection and Analysis) investigates an active incident. While root cause analysis may begin during Phase 2, formal root cause review and improvement recommendations are Post-Incident Activity deliverables.
- C is incorrect. Phase 3 focuses on stopping the current incident, removing the threat, and restoring operations. Process improvement recommendations do not belong to this operational phase.
- D is correct. NIST SP 800-61 Section 3.4 defines Post-Incident Activity as the phase for lessons-learned meetings, root cause analysis, IR metrics reporting, playbook improvements, and detection rule updates. This phase is explicitly designed to prevent recurrence of the same incident type.

---

## Question 20 (5 points)

An analyst is determining whether to prioritize evidence preservation or rapid containment for a live compromised server. The server is actively exfiltrating data to an external IP at 200 MB per minute. Which action is most appropriate?

- A) Preserve all volatile evidence (RAM, network state) before taking any containment action regardless of ongoing data loss
- B) Immediately isolate the server to stop ongoing exfiltration, then acquire available forensic evidence from the isolated system — accepting that some volatile network state may be partially preserved by the EDR agent's isolation log
- C) Take no action until legal counsel approves, since containment could constitute destruction of evidence
- D) Monitor the exfiltration passively for 4 hours to gather more evidence before interrupting the attacker

Correct Answer: B

Distractor Analysis:

- A is incorrect. While evidence preservation is important, allowing 200 MB per minute of data exfiltration to continue to preserve volatile state is disproportionate. Modern EDR isolation captures connection state at the time of isolation. The balance between preservation and containment must account for the ongoing harm rate.
- B is correct. At 200 MB/min, data exfiltration constitutes serious, ongoing harm. The correct decision is to isolate immediately to stop the exfiltration, accepting some volatile evidence trade-off. Modern EDR agents log the network state at isolation time, capturing partial volatile evidence. This is the standard IR trade-off decision: active harm rate high → containment takes priority over complete evidence preservation.
- C is incorrect. Waiting for legal counsel while active data exfiltration continues is not operationally sound. IR playbooks pre-authorize containment actions for active exfiltration scenarios. Legal review applies to major unilateral decisions (taking systems offline permanently, engaging law enforcement) not routine containment.
- D is incorrect. Monitoring active exfiltration for 4 hours while 48 GB of data is transferred is not acceptable. Evidence gathering does not require allowing unlimited data loss.
