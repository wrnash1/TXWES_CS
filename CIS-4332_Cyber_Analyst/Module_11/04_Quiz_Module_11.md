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
