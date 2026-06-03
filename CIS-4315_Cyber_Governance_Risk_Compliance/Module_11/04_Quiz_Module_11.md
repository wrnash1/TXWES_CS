# Quiz: Module 11 — Incident Detection and Response Procedures

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question has exactly four answer options. Select the single best answer for each question. Each question is worth 10 points for a total of 100 points.

These questions are written in the CISM exam style. Read each question carefully and identify what is specifically being asked before reviewing the options.

---

## Question 1

A security analyst discovers that a user account logged into the corporate VPN at 2 AM and accessed 847 files in the HR document repository — behavior that is completely outside this user's normal pattern. Which of the following detection technologies is MOST specifically designed to identify this type of anomaly?

A. Signature-based IDS, which matches known attack patterns against network traffic.

B. User and Entity Behavior Analytics (UEBA), which detects deviations from established behavioral baselines.

C. Network Detection and Response (NDR), which analyzes aggregate network traffic patterns.

D. A firewall access control list, which blocks unauthorized network connections.

### Answer and Analysis — Question 1

**Correct Answer: B**

**Why B is correct**: UEBA is specifically designed to establish behavioral baselines for users and entities and detect anomalous deviations from those baselines. An account accessing 847 HR files at 2 AM when the user's baseline shows no after-hours access and no HR data access is a prototypical UEBA detection use case. UEBA is particularly effective for insider threats and compromised accounts that use legitimate credentials.

**Why A is wrong**: Signature-based IDS detects known attack patterns encoded as signatures — specific exploit code, malware communication patterns, and other defined fingerprints. Unusual legitimate file access by a valid account user does not match any attack signature.

**Why C is wrong**: NDR analyzes network traffic patterns at the aggregate level — connection volumes, geographic anomalies, protocol behaviors. While NDR might flag the 847-file access as unusual data movement, it is not specifically designed for user behavioral analysis.

**Why D is wrong**: A firewall ACL is a preventive control that enforces network access rules. The user in this scenario has legitimate VPN access. An ACL would not detect or prevent this anomalous behavior by an authorized user.

---

## Question 2

During triage of a security alert, an analyst determines that an endpoint has established a persistent outbound connection to an IP address listed in multiple threat intelligence feeds as active command-and-control infrastructure. The connection was first established 18 days ago. Which of the following BEST describes the nature of this finding?

A. An Indicator of Attack (IoA) suggesting that an attack may be in planning stages.

B. A false positive resulting from a misconfigured threat intelligence feed.

C. An Indicator of Compromise (IoC) providing strong evidence of an existing compromise.

D. A routine event that requires no further investigation until a user reports unusual behavior.

### Answer and Analysis — Question 2

**Correct Answer: C**

**Why C is correct**: A confirmed connection to known command-and-control infrastructure is a classic Indicator of Compromise (IoC) — specifically an IP address IoC. The fact that the connection has persisted for 18 days is additional evidence that this is not an accidental or one-time connection. The 18-day connection duration is the dwell time and indicates an established compromise.

**Why A is wrong**: An Indicator of Attack (IoA) is evidence that an attack is in progress based on behavioral patterns — such as credential dumping behavior or lateral movement techniques. An IoA is more forward-looking. An established 18-day C2 connection is evidence of an existing compromise, not planning stages.

**Why B is wrong**: Dismissing a confirmed C2 connection as a likely false positive is a dangerous default assumption. Threat intelligence feeds identify known malicious infrastructure. An analyst who reflexively treats C2 connection alerts as false positives is exhibiting the behavior pattern that leads to prolonged dwell times.

**Why D is wrong**: Waiting for a user to report unusual behavior before investigating a confirmed C2 connection would allow an attacker to operate for an indeterminate additional period. Security alerts require analyst-driven investigation, not user-reported triggers.

---

## Question 3

An IR team discovers active ransomware spreading across a file server cluster. The team lead must decide whether to immediately isolate all affected servers or to capture forensic memory images first before isolating. Which of the following factors MOST strongly supports immediate isolation without prior memory capture?

A. The organization has a regulatory obligation to preserve all forensic evidence.

B. The ransomware is actively encrypting files and spreading to additional servers with each minute of delay.

C. The organization has cyber insurance that requires forensic evidence collection before any containment action.

D. The affected servers are Tier-3 systems with no impact on critical business operations.

### Answer and Analysis — Question 3

**Correct Answer: B**

**Why B is correct**: The evidence-versus-speed trade-off is explicitly resolved in favor of speed when active damage is occurring and spreading. Ransomware actively encrypting and propagating represents escalating and irreversible harm. Each minute of delay allows more files to be encrypted and more systems to be infected. In this scenario, the cost of evidence loss is lower than the cost of additional encryption and spread.

**Why A is wrong**: Regulatory obligations to preserve evidence do not require allowing active damage to continue. Courts and regulators recognize that operational necessity may require immediate containment before ideal forensic conditions can be established. The response must document that the situation required immediate action.

**Why C is wrong**: Cyber insurance policies do not typically require forensic collection before containment. Policies require timely notification and cooperation with investigation after containment. An insurer that denied coverage because a company isolated ransomware before capturing memory images would face significant legal challenge.

**Why D is wrong**: The tier classification of the affected systems is relevant to recovery prioritization, not to the containment decision during an active spreading attack. Even Tier-3 systems used as pivot points can spread ransomware to Tier-1 systems. The active spreading risk justifies immediate isolation regardless of tier.

---

## Question 4

An organization completes ransomware containment on Tuesday and begins recovery on Wednesday by restoring systems from the most recent backup — which was taken the previous Sunday. It is later discovered that the initial compromise occurred the previous Friday. Which of the following BEST describes the risk created by this recovery approach?

A. No risk — Sunday's backup postdates the Friday compromise, so it contains clean data.

B. The Sunday backup was taken after the initial compromise and may have captured the attacker's persistence mechanisms, potentially re-introducing the threat upon restoration.

C. The Sunday backup may contain encrypted data from the ransomware, making it unusable.

D. The recovery is valid because ransomware does not typically establish persistence before encrypting files.

### Answer and Analysis — Question 4

**Correct Answer: B**

**Why B is correct**: If the initial compromise occurred Friday and the backup was taken Sunday — two days after the attacker's initial access — the backup may contain web shells, backdoors, scheduled task modifications, or other persistence mechanisms the attacker established during those two days. Restoring from this backup would reinstall the attacker's foothold along with the legitimate data. The correct approach is to restore from the last known-clean backup, which would be the most recent backup taken before Friday's compromise.

**Why A is wrong**: A backup taken Sunday does NOT postdate the Friday compromise — it was taken during the attacker's active dwell period. The backup was created while the attacker was already in the environment, meaning it may contain compromised artifacts.

**Why C is wrong**: Ransomware encrypted files after Sunday's backup was taken (the encryption was the visible symptom discovered Tuesday). The Sunday backup itself was not subject to encryption. The risk is not encrypted data in the backup but rather attacker-placed persistence mechanisms that were present when the backup was created.

**Why D is wrong**: Modern ransomware operations — particularly ransomware-as-a-service operations — frequently involve an extended pre-encryption period in which the attacker establishes persistence, moves laterally, and exfiltrates data before triggering encryption. Assuming no pre-encryption activity is a dangerous misconception.

---

## Question 5

Which of the following MOST accurately describes the primary purpose of conducting a lessons-learned review within two weeks of incident closure?

A. To satisfy regulatory requirements for post-incident documentation of security events.

B. To identify process improvements, update the IRP, and capture institutional knowledge while the incident is fresh in participants' memories.

C. To determine which team members should be disciplined for failing to follow incident response procedures.

D. To provide the board of directors with a detailed technical account of the incident for their quarterly briefing.

### Answer and Analysis — Question 5

**Correct Answer: B**

**Why B is correct**: The lessons-learned review is a structured improvement process. Its primary purposes are to identify what worked and what failed in the response, to extract actionable improvements, and to update the IRP while the experience is recent. NIST SP 800-61 specifically notes the two-week timing as optimal for memory accuracy. The organizational learning value is the primary purpose.

**Why A is wrong**: While incident documentation is a compliance activity and may satisfy regulatory requirements, the lessons-learned review specifically is designed for organizational improvement, not regulatory compliance. A compliance-only incident report would not require the participatory, structured improvement agenda of a true lessons-learned review.

**Why C is wrong**: A lessons-learned review is a blameless improvement process. Assigning individual blame in a lessons-learned forum destroys the psychological safety needed for honest retrospection. Disciplinary decisions, if warranted, are handled separately through HR processes.

**Why D is wrong**: Board briefings use executive-level summaries, not detailed technical accounts. The lessons-learned review produces internal process improvement documentation, not board-level reporting. Board reporting is a separate governance communication activity.

---

## Question 6

An incident responder is analyzing a compromised Windows server. Which of the following evidence types should be collected FIRST, before any other collection activity, to preserve the most perishable forensic artifacts?

A. Windows Event Logs stored in the C:\Windows\System32\winevt\Logs directory.

B. The file system contents of the server's local disk.

C. RAM contents, active network connections, and running process list.

D. Registry hive files exported from the HKLM\SOFTWARE key.

### Answer and Analysis — Question 6

**Correct Answer: C**

**Why C is correct**: The order of volatility principle in forensic evidence collection requires collecting the most perishable evidence first. RAM contents, active network connections, and the running process list are volatile — they exist only while the system is running and are lost on shutdown, isolation, or crash. RAM may contain encryption keys, attacker tools loaded only in memory, and active C2 session data that exists nowhere else. Collect volatile evidence before any action that could change system state.

**Why A is wrong**: Windows Event Logs are stored on disk as persistent files. While they should be collected, they will still exist after a system isolation or even a controlled shutdown. They are less perishable than RAM contents and should be collected after volatile evidence.

**Why B is wrong**: Full disk contents are the least perishable category — they persist through system shutdown and isolation. Disk collection is correct but is performed after all volatile evidence is secured.

**Why D is wrong**: Registry hive files, like Event Logs, are persistent disk artifacts. They will be preserved through system shutdown. Their collection is valuable but follows volatile evidence collection in the order of volatility framework.

---

## Question 7

After completing containment of a sophisticated network intrusion, an organization's IR team begins eradication. They remove the identified malware and patch the vulnerability used for initial access. Three days later, the attacker re-establishes access through the same environment. Which of the following MOST likely explains this outcome?

A. The patch applied during eradication was not compatible with the operating system version.

B. The attacker used a zero-day exploit that was not yet patchable.

C. Eradication was incomplete — the attacker's secondary persistence mechanisms were not identified and removed.

D. The organization's firewall rules were not updated after the initial incident.

### Answer and Analysis — Question 7

**Correct Answer: C**

**Why C is correct**: Sophisticated attackers — particularly APT actors — routinely establish multiple persistence mechanisms as redundancy against exactly this scenario: having one entry point discovered and closed. If eradication only addressed the initially detected malware and the known attack vector without comprehensively hunting for secondary web shells, scheduled tasks, service installations, or credential implants, the attacker retains access through an undiscovered path.

**Why A is wrong**: Patch compatibility failure would prevent the patch from applying, which would be detected during eradication validation. A failed patch does not explain re-entry through what appears to be a new pathway three days later.

**Why B is wrong**: Zero-day exploits are possible but statistically uncommon. The more likely explanation for rapid re-entry following eradication is incomplete eradication — a missed persistence mechanism — rather than an entirely new zero-day attack. The CISM exam generally expects you to choose the most likely explanation.

**Why D is wrong**: Firewall rule updates are a legitimate eradication activity, but if the attacker's persistence is within the network — a web shell on an internal server, a scheduled task, or harvested credentials — updated firewall rules blocking external traffic would not prevent re-entry through an internal persistence mechanism.

---

## Question 8

During the post-incident review for a major data breach, the IR team discovers that the attacker had access to the environment for 34 days before detection. The team also finds that the SIEM generated an alert on Day 6 of the attacker's presence that matched the initial compromise pattern. The alert was closed without investigation because the analyst's queue contained 2,800 alerts that day. Which of the following BEST describes the root cause of the extended dwell time?

A. The SIEM detection rules were insufficient to identify the compromise pattern.

B. Alert fatigue from an overwhelming false positive volume caused the genuine alert to be dismissed.

C. The incident response plan did not include procedures for this type of attack.

D. The attacker used advanced obfuscation techniques that evaded standard detection.

### Answer and Analysis — Question 8

**Correct Answer: B**

**Why B is correct**: The scenario explicitly states that the SIEM did generate the correct alert on Day 6 — detection was not the failure. The failure was that the analyst dismissed the alert without investigation due to a queue of 2,800 alerts. This is a textbook description of alert fatigue: the genuine alert was present but lost in a sea of alerts that the analyst could not meaningfully investigate. The root cause is the operational failure of alert fatigue, which is caused by poorly tuned SIEM correlation rules generating excessive false positives.

**Why A is wrong**: The SIEM detection rules did identify the compromise pattern — an alert was fired on Day 6. The detection technology worked. The failure was in the human response to the detection, not in the detection capability itself.

**Why C is wrong**: The incident response plan's procedure coverage is a separate concern from why the Day 6 alert was dismissed. Inadequate procedures would affect how the team responded after incident declaration, not whether the analyst investigated the initial alert.

**Why D is wrong**: If the attacker had successfully evaded detection, the SIEM would not have generated an alert on Day 6. The scenario states that the alert was generated and dismissed — obfuscation is not the explanation.

---

## Question 9

An organization is developing containment playbooks for its top five incident types. Which of the following incident types requires the MOST careful coordination with Human Resources and Legal counsel before executing containment actions?

A. External ransomware attack spreading across a file server cluster.

B. DDoS attack affecting the public-facing website.

C. Suspected insider threat — an employee is believed to be exfiltrating confidential data.

D. Phishing campaign with multiple employees reporting suspicious emails.

### Answer and Analysis — Question 9

**Correct Answer: C**

**Why C is correct**: Insider threat investigations require HR and Legal involvement from the earliest stages because the containment actions — account lockout, device seizure, access revocation — affect an employee's employment status and rights. Executing containment without HR coordination can expose the organization to wrongful termination claims. Legal must be involved to ensure evidence is preserved in a manner that supports potential employment action or criminal referral. The IRP must specify HR and Legal notification as prerequisites to executing insider threat containment.

**Why A is wrong**: Ransomware containment — network isolation, system lockout — is primarily a technical response that can proceed on IR team authority under the IRP. HR involvement is not typically required before isolating infected servers.

**Why B is wrong**: DDoS containment involves network controls — traffic scrubbing, rate limiting, upstream mitigation — with no employee action implications. HR is not relevant to DDoS containment.

**Why D is wrong**: Phishing response — quarantining suspicious emails, isolating clicked endpoints — is a technical response. HR notification may be appropriate if the phishing resulted in credential compromise, but the initial containment does not require HR coordination.

---

## Question 10

An organization's IR team has completed eradication of a sophisticated attack and is preparing to begin recovery. The security manager wants to restore systems from backup as quickly as possible to meet the 8-hour RTO in the DRP. The forensic investigator argues that the recovery should be delayed until a full forensic review of all affected systems is complete. Which of the following BEST describes the appropriate resolution?

A. Always prioritize the RTO — business recovery is the primary objective of incident response.

B. Always prioritize forensic completeness — evidence preservation is required by law in all incidents.

C. Apply the pre-negotiated decision authority in the IRP, which should specify recovery criteria for each system tier and whether forensic imaging (rather than delayed recovery) satisfies the evidence requirement.

D. Escalate to the board of directors for a decision on whether business continuity or forensic completeness takes priority.

### Answer and Analysis — Question 10

**Correct Answer: C**

**Why C is correct**: The IRP-DRP conflict between forensic needs and recovery speed is a known, predictable tension that must be resolved in the plan before an incident occurs — not during the response. A mature IRP specifies the pre-negotiated approach for each system tier: for critical Tier-1 systems, forensic imaging may satisfy evidence requirements while allowing recovery to proceed (the image is the evidence; the original can be rebuilt). The IRP should specify who has authority to make this trade-off decision and what criteria apply. Applying the pre-negotiated authority avoids delay and inconsistency.

**Why A is wrong**: Always prioritizing RTO without forensic consideration risks recovering from a backup that contains attacker persistence (as covered in Question 4) and destroying evidence that may be needed for regulatory proceedings, litigation, or insurance claims. Blind prioritization of RTO is not a mature incident management approach.

**Why B is wrong**: Forensic evidence preservation is not legally required in all incidents. Most organizations are not under a legal hold at the time of the incident. Forensic imaging rather than system preservation often satisfies evidence needs while allowing recovery. Treating all incidents as if a full forensic hold is legally required is operationally untenable.

**Why D is wrong**: Escalating an operational recovery timing decision to the board is inappropriate. The board has neither the operational knowledge to make this decision nor the time to do so during an active recovery window. This decision should be pre-authorized in the IRP and executed by the CISO and IR Manager.

---

## End of Quiz

**Total: 10 questions | 100 points**

Review your answers using the distractor analysis provided. For any question you answered incorrectly, revisit the corresponding section in the Module 11 Reading Guide before proceeding to the lab.
