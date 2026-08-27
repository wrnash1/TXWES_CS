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

---

### Question 11 (5 points)

A threat hunter reviewing SIEM logs notices that a workstation has been executing PowerShell commands that spawn encoded base64 strings every four hours for the past six days. No antivirus alert has fired. Which detection concept best describes why the AV has not alerted, and which detection technology is most suited to identifying this behavior?

- A) The AV has not alerted because it is misconfigured; signature-based IDS would detect this pattern.
- B) The attacker is using a living-off-the-land technique that abuses a legitimate tool, producing no malware file signature; UEBA or EDR with behavioral detection rules is most suited to identify this pattern.
- C) The AV has not alerted because PowerShell is whitelisted; a firewall ACL should be updated to block PowerShell execution.
- D) This is likely a false positive caused by a legitimate scheduled task; no further investigation is needed.

### Answer and Analysis — Question 11

**Correct Answer: B**

**Why B is correct**: Living-off-the-land (LotL) techniques use legitimate operating system tools — PowerShell, WMI, certutil — to execute malicious actions without dropping a malware file. Signature-based antivirus detects known malicious files; a LotL attack produces no new file to signature. EDR platforms with behavioral detection rules and UEBA can identify abnormal PowerShell usage patterns — such as periodic encoded command execution — that deviate from normal workstation behavior baselines.

**Why A is wrong**: Signature-based IDS detects known attack traffic patterns, not process behavior on endpoints. It would not detect encoded PowerShell execution on a workstation.

**Why C is wrong**: Blocking PowerShell via firewall ACL is architecturally incorrect. Firewalls operate at the network layer and do not control local process execution. Application control or AppLocker policies would be the correct technical response, but the question asks about detection, not prevention.

**Why D is wrong**: Dismissing periodic encoded PowerShell execution as a likely false positive is exactly the kind of alert fatigue behavior that allows attackers to maintain dwell time for months. Encoded PowerShell is a high-fidelity indicator that warrants investigation.

---

### Question 12 (5 points)

An EDR platform generates an alert: "Process lsass.exe accessed by mimikatz.exe." The SOC analyst confirms the process names in the alert are accurate. What does this finding most likely indicate, and what is the appropriate immediate response?

- A) This is a false positive — lsass.exe routinely interacts with other processes; no action needed.
- B) This is an Indicator of Compromise confirming credential harvesting is in progress; the affected system should be immediately isolated and escalated per the IRP severity criteria.
- C) This indicates a software deployment conflict; the IT help desk should be notified.
- D) This is an Indicator of Attack suggesting an attack may occur in the future; continue monitoring without containment.

### Answer and Analysis — Question 12

**Correct Answer: B**

**Why B is correct**: Mimikatz is a well-known credential harvesting tool that accesses the Local Security Authority Subsystem Service (lsass.exe) to extract password hashes and Kerberos tickets from memory. A confirmed process interaction between mimikatz.exe and lsass.exe is an unambiguous Indicator of Compromise indicating active credential theft in progress. Immediate isolation and escalation are required.

**Why A is wrong**: While lsass.exe does interact with many processes legitimately, interaction specifically from mimikatz.exe is not legitimate. Mimikatz is a post-exploitation tool with no legitimate business use case.

**Why C is wrong**: Mimikatz is not a software deployment tool. This alert indicates attacker activity, not an IT configuration issue.

**Why D is wrong**: This is not a future-oriented IoA — the attack is actively in progress. Mimikatz accessing lsass.exe is evidence of an ongoing credential compromise, not a precursor to a future event. Continuing to monitor without containment allows the attacker to collect credentials and move laterally.

---

### Question 13 (5 points)

An organization's security operations team has deployed a honeypot — a fake server configured to appear as a production database — on the internal network. The honeypot generates an alert when any internal host connects to it. During a regular Monday morning review, the analyst sees that a connection was made to the honeypot from a finance workstation at 3:17 AM Saturday. Which statement best characterizes the significance of this alert?

- A) Low significance — the finance workstation may have been running a scheduled backup that contacted the wrong server.
- B) High significance — any connection to a honeypot from an internal host is a high-fidelity indicator of attacker lateral movement or unauthorized internal reconnaissance because no legitimate user or process should ever contact this server.
- C) Medium significance — honeypot alerts are frequently triggered by network scanning tools used by IT and require correlation before escalation.
- D) No significance — the connection was made outside business hours and therefore cannot be from an active attacker.

### Answer and Analysis — Question 13

**Correct Answer: B**

**Why B is correct**: A honeypot generates almost no false positives because it serves no legitimate function. No authorized user, process, or scheduled task should ever connect to it. A connection from an internal workstation to a honeypot is a near-certain indicator of attacker reconnaissance or lateral movement. The after-hours timing adds further suspicion. This alert deserves immediate high-priority investigation.

**Why A is wrong**: Backup processes are configured to target specific known systems. A finance workstation connecting to an unlisted fake database at 3 AM is not a plausible backup scenario. The honeypot's value is that it eliminates almost all legitimate connection explanations.

**Why C is wrong**: Honeypots are specifically not IT scanning targets — they are hidden from authorized IT tools by design. A connection from a finance workstation cannot be attributed to authorized IT scanning.

**Why D is wrong**: Attackers operate at all hours, including weekends and after hours. After-hours activity by an internal host connecting to a honeypot is more suspicious, not less. The timing is an additional indicator, not an exonerating factor.

---

### Question 14 (5 points)

During the long-term containment phase of an advanced persistent threat investigation, the IR team discovers that the attacker has been using a compromised IT administrator account to access systems. The team is considering whether to immediately lock the account or to continue monitoring the account's activity to understand the attacker's full objectives. Which factor most strongly supports continued monitoring before lockout?

- A) The organization's IT administrator requires continuous access and cannot tolerate any account disruption.
- B) Immediately locking the account may alert the attacker that they have been discovered, causing them to accelerate their objectives, destroy evidence, or activate additional persistence mechanisms before the team can identify the full scope of the compromise.
- C) Monitoring is required by law before any account lockout action can be taken.
- D) The IR team cannot lock administrator accounts without a signed court order.

### Answer and Analysis — Question 14

**Correct Answer: B**

**Why B is correct**: For APT and espionage-type incidents, the containment decision matrix (Module 11 Reading Guide, Section 3.2) notes that the appropriate strategy is covert monitoring before gradual containment to avoid tipping off the actor. If the attacker detects account lockout, they may trigger destructive payloads, exfiltrate remaining target data at high speed, or activate backup persistence mechanisms before the team can identify and remove them. Understanding the full scope before acting is a legitimate and important tactical consideration.

**Why A is wrong**: The legitimate administrator's access needs are a real consideration, but the actual reason to delay lockout in this scenario is the investigative and tactical value of continued monitoring — not the administrator's convenience.

**Why C is wrong**: There is no general legal requirement to monitor before account lockout. This is a tactical incident response decision based on investigation objectives.

**Why D is wrong**: Internal account lockout for security purposes is within the authority of the IR team under the IRP's executive authorization. Court orders are not required for internal security response actions.

---

### Question 15 (5 points)

Following eradication of a ransomware attack, the recovery team restores systems from the most recent backup. Two days after restoration, users report that files appear to be missing and that system performance has degraded. The IR team investigates and finds that the same ransomware encryption process has begun again. Which eradication failure most likely explains this outcome?

- A) The backup storage system was corrupted during the original ransomware attack.
- B) The ransomware used a zero-day vulnerability that cannot be patched.
- C) Eradication failed to identify and remove a persistence mechanism — such as a scheduled task or service — that reactivated the ransomware after recovery.
- D) The recovery team restored to the wrong system tier, causing the ransomware to spread from a Tier-3 system.

### Answer and Analysis — Question 15

**Correct Answer: C**

**Why C is correct**: Re-encryption after a successful-seeming recovery is a classic sign of incomplete eradication. Ransomware operators frequently install persistence mechanisms — scheduled tasks, services, WMI subscriptions, registry Run key entries — that survive the visible malware removal and reactivate after recovery. The recovery restored the system to operational status, but the persistence mechanism reactivated the ransomware payload. Thorough persistence hunting is a required eradication step.

**Why A is wrong**: A corrupted backup would cause restoration failures, not successful restoration followed by re-encryption two days later.

**Why B is wrong**: A zero-day vulnerability would explain initial access or initial failure to detect, but not re-encryption after recovery. The vulnerability must have been the entry vector, but the re-encryption after restoration indicates a persistence mechanism — not a new exploitation event.

**Why D is wrong**: Restoring to the wrong tier would cause functional issues with business applications, not a re-encryption event. The ransomware's re-activation is due to a missed persistence mechanism, not a tier classification error.

---

### Question 16 (5 points)

An organization's incident response team completes eradication of a supply chain compromise in which an attacker gained access through a backdoored software update from a third-party vendor. Before beginning recovery, which action is MOST critical to prevent reinfection during the restoration process itself?

- A) Notify the vendor that their software was compromised and request a credit.
- B) Verify that the vendor has issued a clean software version, confirm its integrity with a cryptographic hash from an independent source, and ensure the backdoored version is removed from all update channels and endpoints before recovery begins.
- C) Restore all systems from the most recent backup, which predates the compromised update.
- D) Block the vendor's software update server at the perimeter firewall until the next scheduled maintenance window.

### Answer and Analysis — Question 16

**Correct Answer: B**

**Why B is correct**: A supply chain compromise is reintroduced if the compromised software update is still present in the update infrastructure or is applied during recovery. Before recovery begins, the team must confirm that a clean version of the software exists, verify its integrity using a hash from a trusted independent source (not the vendor's own website, which may also be compromised), and ensure the backdoored version cannot be re-deployed during recovery.

**Why A is wrong**: Notifying the vendor is an appropriate notification action but is not the critical pre-recovery technical step. The vendor notification does not itself prevent reinfection during recovery.

**Why C is wrong**: Restoring from a backup that predates the compromised update restores the clean system state, but if the recovery process then applies the compromised software update as part of patching or configuration management, the attack reintroduces itself. The backup alone does not address the update channel risk.

**Why D is wrong**: Blocking the update server at the perimeter is a useful short-term containment step but is not the most critical recovery preparation action. Internal systems that already have the backdoored version installed will not be remediated by a perimeter block.

---

### Question 17 (5 points)

An IR team is preparing their lessons-learned report following a significant data breach. The report will be shared with the board of directors and may be reviewed by external auditors. Legal counsel advises that the report should be prepared under attorney-client privilege. Which statement best describes the practical implication of this advice for the report's content and distribution?

- A) The report cannot be shared with the board of directors if it is under attorney-client privilege.
- B) Preparing the report under attorney-client privilege means its candid findings may be legally protected from compelled disclosure, but the team must be careful about distribution — sharing the report beyond the privileged group may waive the privilege.
- C) Attorney-client privilege has no practical effect on incident report content; it is a formality with no operational consequences.
- D) The report must be destroyed after review if it contains findings that could be used against the organization in litigation.

### Answer and Analysis — Question 17

**Correct Answer: B**

**Why B is correct**: Preparing post-incident reports under attorney-client privilege can protect candid root cause findings and identified vulnerabilities from compelled disclosure in litigation. However, attorney-client privilege can be waived if the privileged document is shared beyond the protected group without appropriate controls. The legal team typically provides specific distribution guidance when privilege is intended to apply.

**Why A is wrong**: Attorney-client privilege does not prevent sharing with the board, which is within the privileged group for this purpose. Legal counsel typically structures board presentations of privileged reports appropriately.

**Why C is wrong**: Attorney-client privilege has significant practical consequences. It determines whether the report's candid findings can be compelled in discovery during litigation. Treating it as a formality ignores its legal function.

**Why D is wrong**: Destroying documents to avoid litigation exposure is spoliation, which creates far greater legal risk than the document itself. Documents are preserved, not destroyed, when litigation is anticipated.

---

### Question 18 (5 points)

A security analyst is performing triage on a SIEM alert at 2 AM. The alert indicates that a privileged service account used to run database backups has authenticated to three additional servers that it has never previously accessed. The analyst consults threat intelligence and finds no match to known threat actor indicators. Which triage decision is most consistent with CISM Domain 4 principles?

- A) Close the alert as a false positive because there is no threat intelligence match.
- B) Escalate the alert as a genuine anomalous activity indicator, classify severity based on IRP criteria for privileged account abuse, and begin investigation regardless of the absence of a threat intelligence match.
- C) Defer the investigation until the next business day when the system owner can be consulted.
- D) Reset the service account password immediately without any further investigation.

### Answer and Analysis — Question 18

**Correct Answer: B**

**Why B is correct**: The absence of a threat intelligence match does not make an alert a false positive. UEBA-type alerts based on behavioral deviation — a service account accessing servers outside its defined scope — are significant anomalies that warrant investigation regardless of threat intel correlation. The IRP severity criteria should be applied based on the observable behavior (privileged account lateral movement potential) and escalated appropriately.

**Why A is wrong**: Relying solely on threat intelligence absence to dismiss anomalous behavior is a critical analytical failure. Novel attacks, insider threats, and zero-day exploits will not match existing threat intelligence. Behavioral anomalies from privileged accounts are high-fidelity indicators.

**Why C is wrong**: Privileged account abuse does not wait for business hours. A 2 AM investigation of a service account accessing unusual servers is exactly the scenario that on-call coverage exists to address. Deferring until business hours could allow hours of additional damage.

**Why D is wrong**: Resetting the service account password without investigation destroys the forensic opportunity to understand what accessed the additional servers, whether lateral movement occurred, and whether the compromise has spread. Investigation precedes remediation.

---

### Question 19 (5 points)

The NIST SP 800-61 framework describes "short-term containment" and "long-term containment" as distinct strategies applied during the Containment phase. Which of the following scenarios correctly applies the appropriate strategy?

- A) Short-term containment: placing enhanced monitoring on a compromised segment while maintaining attacker access to observe objectives. Long-term containment: immediately isolating all affected systems from the network.
- B) Short-term containment: immediately isolating a ransomware-infected server to stop active encryption and spread. Long-term containment: deploying temporary network access controls and enhanced monitoring across affected segments while investigation continues.
- C) Short-term containment: waiting 24 hours to gather all evidence before acting. Long-term containment: restoring all systems from backup within the same 24-hour period.
- D) Short-term containment and long-term containment are synonymous terms for the same activity performed at different times of day.

### Answer and Analysis — Question 19

**Correct Answer: B**

**Why B is correct**: Short-term containment prioritizes speed to stop active and immediate harm — isolating an actively encrypting ransomware server is the correct short-term action. Long-term containment maintains sustained controls that allow investigation to continue without allowing the attacker to operate freely — enhanced monitoring and temporary access controls on the broader affected segment describe long-term containment correctly.

**Why A is wrong**: This reverses the two strategies. Covert monitoring while maintaining attacker access is a long-term containment approach used for APT investigations. Immediate isolation is the short-term strategy.

**Why C is wrong**: Waiting 24 hours to act is not short-term containment — it is a delay in containment. Recovery from backup is a recovery activity, not a containment strategy.

**Why D is wrong**: Short-term and long-term containment are distinct strategies with different purposes, objectives, and operational profiles. They are not synonymous.

---

### Question 20 (5 points)

An organization's IR team discovers that the attacker's initial access occurred through an unpatched vulnerability in a public-facing web application. The vulnerability has been patched by the vendor. The organization has not applied the patch because the change management process requires a 30-day testing period before any production patch can be deployed. Which CISM-aligned recommendation best addresses this systemic gap?

- A) Bypass the change management process for all security patches going forward to ensure faster deployment.
- B) Work with change management leadership to establish a risk-tiered patch process that allows critical and actively exploited vulnerabilities to follow an expedited approval track while maintaining appropriate testing controls.
- C) Accept the risk of delayed patching as an inherent limitation of enterprise change management processes.
- D) Replace the change management team with the security team to give security unilateral control over patch deployment.

### Answer and Analysis — Question 20

**Correct Answer: B**

**Why B is correct**: CISM Domain 3 principles require security controls to be integrated with organizational processes, not to bypass them. The correct governance solution is to work within the change management framework to create a risk-tiered track — a documented, approved process for expedited deployment of critical patches — that satisfies both security urgency and change management risk controls. This is a program management improvement, not a process bypass.

**Why A is wrong**: Bypassing change management entirely creates uncontrolled production risk. Unauthorized changes to production systems have caused significant outages and are prohibited by SOX IT General Controls for organizations with financial reporting obligations.

**Why C is wrong**: Accepting delayed patching as inherent is not consistent with CISM risk management principles. The 30-day blanket delay creates foreseeable, unmitigated risk. The correct approach is to address the systemic gap through program design.

**Why D is wrong**: Giving security unilateral control over change management creates a separation of duties failure and undermines the operational stability that change management exists to protect. Governance requires collaboration between functions, not unilateral control by any single function.

---

## End of Quiz

**Total: 20 questions | 10 questions at 10 points each (original) + 10 questions at 5 points each (supplemental) = 150 points**

Review your answers using the distractor analysis provided. For any question you answered incorrectly, revisit the corresponding section in the Module 11 Reading Guide before proceeding to the lab.
