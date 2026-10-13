# Quiz: Module 12 — Digital Forensics and Post-Incident Analysis

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Instructions

This quiz contains 10 multiple-choice questions. Select the single best answer for each question. Each question is worth 10 points for a total of 100 points.

---

## Question 1

An investigator connects a suspect hard drive directly to a forensic workstation without any intervening hardware and begins copying files. Which forensic principle has been violated?

A) Chain of custody
B) Evidence preservation
C) Evidence identification
D) Legal hold compliance

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Chain of custody refers to documenting the handling of evidence over time. While connecting the drive without a write blocker may ultimately affect the chain of custody record, the immediate violation is to the preservation principle, which requires that evidence not be altered during acquisition.

B) Correct. The preservation principle requires that evidence be acquired in a manner that prevents alteration. Connecting a drive without a write blocker allows the forensic workstation's operating system to write to the drive — modifying access timestamps and potentially overwriting data — which corrupts the integrity of the evidence.

C) Incorrect. Evidence identification is the phase in which the investigator determines what constitutes evidence. That phase occurred prior to physical acquisition and is not the principle violated by connecting the drive without a write blocker.

D) Incorrect. Legal hold compliance relates to preserving evidence in response to anticipated litigation. It is a governance and legal concept, not the specific forensic principle violated by the physical handling described in this question.

---

## Question 2

A security investigator must collect evidence from five systems following a network intrusion. The systems include a running web server with an active memory dump tool, a powered-off workstation, a SIEM with 12 months of logs, a firewall with 30-day NetFlow records, and an email server. According to the order of volatility, which system should be addressed first?

A) The SIEM with 12 months of logs
B) The powered-off workstation
C) The running web server with active memory
D) The firewall with 30-day NetFlow records

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. SIEM logs stored on disk are persistent evidence with a known retention period. They are not at immediate risk of loss and should be collected after volatile evidence sources have been secured.

B) Incorrect. A powered-off workstation's disk contents are non-volatile. While the drive should be imaged with a write blocker, it is not at risk of imminent data loss. It correctly ranks lower in the collection order than active memory.

C) Correct. The order of volatility principle requires that investigators collect the most transient evidence first. Memory (RAM) is lost the moment a system is powered down or rebooted. The running web server's active memory contains evidence — running processes, open connections, encryption keys — that cannot be recovered from any other source once it is gone.

D) Incorrect. NetFlow records stored on the firewall are disk-based or database-resident with a 30-day rolling window. While investigators should note the expiration date and plan collection accordingly, this evidence is significantly less volatile than RAM on a running system.

---

## Question 3

During a post-incident review, the security team discovers that an attacker maintained persistent access for 63 days before detection. The SIEM had been deployed 8 months earlier but no lateral movement detection rules had ever been configured. Applying the Five Whys technique, which statement best represents the root cause?

A) The attacker was highly skilled and used sophisticated evasion techniques
B) The SIEM lacked lateral movement detection rules
C) The organization had no standard defining required detection coverage for SIEM deployments
D) The security operations team did not review alerts frequently enough

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. Attacker sophistication is a threat characteristic, not an organizational root cause. The Five Whys technique focuses on internal organizational causes that the organization can control and remediate. Attacker skill level is not something the organization can address through internal process improvement.

B) Incorrect. The absence of lateral movement detection rules is a symptom — it is the first "why" answer, not the root cause. Applying additional why iterations would ask why the rules were never configured, eventually revealing the deeper governance gap.

C) Correct. Applying Five Whys to this scenario: The SIEM lacked detection rules (Why 1) because no one configured them after deployment (Why 2) because the deployment project was closed without a detection engineering phase (Why 3) because no project standard required detection engineering (Why 4) because the organization had no SIEM deployment standard at all (root cause). The missing standard is the fundamental governance gap that would prevent recurrence if addressed.

D) Incorrect. Alert review frequency is a process symptom, not a root cause, and this answer is factually incomplete — the issue is not that alerts were missed but that no alerts were ever generated due to unconfigured rules.

---

## Question 4

A forensic examiner images a suspect hard drive and records the following SHA-256 hash at the time of imaging: `a3f2...9c41`. Three weeks later during analysis, the examiner re-hashes the forensic image and obtains `a3f2...9c41`. What does this confirm?

A) The original drive has not been accessed since imaging
B) The forensic image is an exact copy of the original drive
C) The forensic image has not been altered since it was created
D) The chain of custody was maintained without interruption

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. The hash comparison verifies the integrity of the forensic image copy, not the original drive. The original drive's access status is controlled separately through physical evidence storage and chain of custody documentation.

B) Incorrect. While a matching hash strongly implies the image is an accurate copy of the original, the comparison described here is between the image at creation time and the image at analysis time — not between the image and the original drive. A separate hash comparison at the time of imaging would verify accuracy against the original.

C) Correct. When the SHA-256 hash computed at analysis time matches the hash recorded at the time of imaging, it proves that not a single bit of the forensic image file has changed in the intervening period. SHA-256 produces a unique fingerprint; any modification — even changing one bit — would produce an entirely different hash value.

D) Incorrect. Chain of custody is documented through written records of transfers and storage, not through hash verification. Hash matching confirms data integrity; the chain of custody form confirms proper handling procedures were followed. Both are required, but they serve different purposes.

---

## Question 5

Legal counsel notifies the CISO that litigation is reasonably anticipated following a data breach. Which action should the CISO take immediately?

A) Delete all logs older than 90 days to limit discoverable evidence
B) Suspend the organization's data retention and deletion schedules for relevant systems
C) Transfer all evidence to external counsel's servers to protect attorney-client privilege
D) Conduct a full forensic investigation and publish findings to stakeholders

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Deleting logs after litigation is reasonably anticipated constitutes spoliation of evidence — the intentional or negligent destruction of relevant evidence. This can result in severe legal sanctions including adverse inference instructions, evidence exclusion, and financial penalties. This is the opposite of the correct action.

B) Correct. When legal counsel notifies the organization that litigation is reasonably anticipated, the CISO must immediately implement a legal hold, which suspends normal data retention and deletion schedules for all potentially relevant systems and data. This preserves evidence that might otherwise be routinely deleted.

C) Incorrect. Transferring evidence to external counsel's servers is not the standard response to a legal hold notification and is not a recognized practice for implementing a legal hold. The legal hold applies to the organization's own systems and custodians, not to evidence transfer.

D) Incorrect. Publishing investigation findings publicly before legal proceedings are resolved would be inappropriate and potentially harmful to the organization's legal position. Investigation findings must be handled with strict confidentiality in coordination with legal counsel during active litigation.

---

## Question 6

Which forensic tool is specifically designed for the analysis of volatile memory images and is considered the gold standard open-source solution for this purpose?

A) Autopsy
B) EnCase
C) Volatility
D) Wireshark

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. Autopsy is a graphical interface built on The Sleuth Kit and is designed for disk forensics — file system analysis, timeline generation, and artifact extraction from disk images. It does not analyze memory images.

B) Incorrect. EnCase is a commercial disk forensics platform used for disk imaging, file analysis, and report generation. While it is widely used in law enforcement and enterprise investigations, it is not the primary tool for memory forensics.

C) Correct. Volatility is the gold standard open-source framework for memory forensics. It supports analysis of Windows, Linux, and macOS memory images and provides hundreds of plugins to extract running processes, network connections, injected code, registry keys loaded in memory, and credentials.

D) Incorrect. Wireshark is a network packet capture analysis tool. It examines network traffic, not memory images. While Wireshark is invaluable in network forensics, it has no capability to analyze RAM dumps.

---

## Question 7

An organization's after-action report following a ransomware incident contains a detailed timeline, a thorough root cause analysis, and 12 specific findings. However, none of the findings include assigned owners or target completion dates. From a CISM governance perspective, what is the primary deficiency of this report?

A) The timeline is too detailed and should be summarized for executive audiences
B) The report lacks an executive summary section
C) The findings without owners and due dates cannot drive accountability or improvement
D) Root cause analysis should not appear in documents shared with executives

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. A detailed timeline is a valuable component of an after-action report and is typically maintained in full in appendices even when a summary is provided elsewhere. Timeline detail is not a deficiency.

B) Incorrect. The absence of an executive summary is a presentation gap but not the primary governance deficiency described in the scenario. The scenario specifically asks about the impact of findings without owners and due dates.

C) Correct. From a CISM governance perspective, findings without assigned owners and target completion dates are unactionable. They create a record of known deficiencies with no mechanism for accountability or improvement. An after-action report that documents what is broken without establishing who will fix it and by when is a governance failure — it creates legal and regulatory liability without producing organizational benefit.

D) Incorrect. Root cause analysis is an appropriate and valuable component of after-action reports at all levels. Executives need to understand root causes to make informed resource and risk decisions.

---

## Question 8

An investigator is using the fishbone (Ishikawa) diagram method to analyze a security incident where an insider threat actor exfiltrated sensitive data over six months. Which of the following correctly represents the "Process" category contribution in a fishbone diagram?

A) The insider used an unmonitored USB port to copy data
B) No data loss prevention solution was deployed on workstations
C) The organization had no formal offboarding procedure to revoke access for departing employees
D) The insider's manager had not received security awareness training

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. An unmonitored USB port is a Technology gap — it represents a missing or misconfigured technical control. In fishbone analysis, physical and logical security control deficiencies belong in the Technology or Environment category, not Process.

B) Incorrect. The absence of a data loss prevention solution is a Technology gap — specifically a missing technical safeguard. Technology category items describe tools, systems, and technical controls that are missing or misconfigured.

C) Correct. The absence of a formal offboarding procedure is a Process deficiency. Processes are documented, repeatable workflows that define how organizational activities are conducted. A missing offboarding procedure means there is no defined sequence of steps to revoke access when employment ends — this is squarely within the Process category of a fishbone diagram.

D) Incorrect. Manager training is a People category issue. People category items address human factors including skills, knowledge, training, awareness, behavior, and role clarity. A manager who has not received security awareness training represents a gap in the People dimension.

---

## Question 9

Which of the following statements most accurately describes the concept of forensic readiness?

A) The ability to respond to a forensic investigation request within 24 hours of an incident
B) Organizational capability to collect and preserve digital evidence before an incident occurs
C) The possession of licensed forensic software such as EnCase or FTK
D) Compliance with law enforcement evidence handling standards for criminal investigations

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. A 24-hour response capability is a response time objective, not a definition of forensic readiness. Forensic readiness is not primarily about response speed; it is about having the capability, infrastructure, and procedures in place before they are needed.

B) Correct. Forensic readiness is defined by ISACA as the organizational state of maximizing the ability to use digital evidence while minimizing the cost of an investigation. It is a proactive capability — establishing logging, retention policies, trained personnel, defined procedures, and legal frameworks before an incident occurs, so that evidence collection can begin immediately and effectively when needed.

C) Incorrect. Software licensing is one component of forensic readiness, but owning tools does not constitute readiness. An organization with licensed tools but no trained staff, no retention policies, and no evidence handling procedures is not forensically ready.

D) Incorrect. Forensic readiness is not limited to criminal investigations or law enforcement standards. It applies to any situation where digital evidence may be needed — including regulatory inquiries, civil litigation, insurance claims, and internal investigations.

---

## Question 10

During a forensic investigation, an examiner discovers that a critical server's Windows Security event log was cleared at 3:12 AM on the night of the incident. The event log clearing event itself (Event ID 1102) was captured in the SIEM before the local log was deleted. What is the most appropriate characterization of this finding from a CISM perspective?

A) The SIEM data is inadmissible because it is a secondary source
B) The log clearing is evidence of anti-forensic activity and should be documented in the after-action report
C) The investigator should power down the server immediately to preserve remaining evidence
D) The investigation cannot proceed without the original Windows Security event log

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. SIEM data is legitimate and routinely admissible evidence in both legal proceedings and regulatory inquiries. Secondary sources captured in a centralized, tamper-resistant logging system can be highly credible, especially when the original source was deliberately destroyed.

B) Correct. Log clearing, particularly when it coincides with the timing of a security incident, is a classic anti-forensic technique used by attackers to destroy evidence of their activities. The CISM candidate must recognize this as a significant finding — it indicates intent to conceal, it informs the investigation's scope, and it must be prominently documented in the after-action report as evidence of deliberate attacker action.

C) Incorrect. Powering down the server would destroy volatile memory evidence including running processes and open network connections that may contain attacker artifacts. Powering down is generally contraindicated for running systems unless it is necessary to prevent ongoing harm.

D) Incorrect. The SIEM captured Event ID 1102 (the log clearing event itself) before the local log was cleared, which confirms the clearing occurred. The investigation can and should proceed using SIEM data, other log sources, memory forensics, and network evidence to reconstruct the timeline.

---

## Question 11

(5 points) A forensic investigator is acquiring a disk image from a Windows workstation using FTK Imager. After the acquisition completes, the investigator computes an MD5 hash of the image file on the forensic workstation and records it on the chain of custody form. Three days later, a second investigator re-hashes the image before beginning analysis and finds that the MD5 value matches. What does this comparison confirm, and what does it NOT confirm?

A) It confirms the image is identical to the original drive and that the chain of custody was unbroken.
B) It confirms the image has not been altered since the first hash was recorded, but it does not confirm that the image is an accurate copy of the original drive at the time of acquisition.
C) It confirms the chain of custody was properly maintained but does not confirm data integrity.
D) It confirms that SHA-256 verification is unnecessary if MD5 hashes match.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. The matching hashes confirm that the image file has not changed between the two measurement points. They do not confirm that the original acquisition was accurate — that comparison requires a hash taken of both the original drive and the image at the time of acquisition and recording that pair on the chain of custody form.

B) Correct. Hash matching between two points in time proves that the file has not been altered in between. However, this comparison is between the image at creation time and the image at analysis time — not between the original drive and the image. To confirm forensic accuracy, the investigator must have recorded the hash of the original drive at acquisition time and verified it matched the image hash then.

C) Incorrect. Hash matching is precisely how data integrity is confirmed. Chain of custody documentation is the separate process that confirms handling procedures were followed; both are required and serve different purposes.

D) Incorrect. SHA-256 is the recommended standard for forensic work due to its stronger collision resistance. MD5 is still useful for integrity verification in a forensic context, but this answer incorrectly dismisses SHA-256 as unnecessary. The comparison described does not speak to which algorithm should be used.

---

## Question 12

(5 points) During a forensic investigation of a Linux server, an investigator uses the `dd` command to create a bit-for-bit image of the server's hard drive. After imaging, the investigator runs `md5sum` on both the original device and the image file and receives matching hash values. What does this simultaneous comparison confirm?

A) The server's operating system has not been modified by the attacker.
B) The forensic image is a complete and accurate bit-for-bit copy of the original device at the time of acquisition.
C) The evidence has been preserved in accordance with legal hold requirements.
D) The chain of custody documentation is complete and admissible in court.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Hashing an entire disk image confirms data integrity of the copy — it does not analyze whether any specific files or operating system components were modified by an attacker. That analysis requires examination tools applied to the image content.

B) Correct. When the MD5 hash of the source device matches the MD5 hash of the image file immediately after acquisition, this confirms that the `dd` imaging process produced a bit-for-bit accurate copy with no data loss or alteration during the transfer. This is the standard forensic acquisition verification step.

C) Incorrect. Hash verification confirms data integrity. Legal hold compliance is a separate governance process involving retention of evidence in response to legal counsel's directive. Hash matching does not demonstrate legal hold compliance.

D) Incorrect. Chain of custody documentation is maintained through written transfer records and procedural compliance — not through hash comparison. Hash matching provides technical integrity verification; the chain of custody form provides legal admissibility documentation. Both are required, and neither alone is sufficient.

---

## Question 13

(5 points) An organization's CISO is asked by the board whether the organization is "forensically ready." Which combination of capabilities most accurately demonstrates forensic readiness?

A) Possession of licensed forensic software such as FTK and Volatility, and a trained forensic investigator on staff.
B) An ability to activate the incident response plan within one hour of detection, supported by documented escalation procedures.
C) Comprehensive logging with defined retention periods, documented evidence handling procedures, trained personnel, a legal hold process, and secure evidence storage — all established before any incident occurs.
D) Membership in an industry information sharing and analysis center (ISAC) providing access to threat intelligence and forensic support on demand.

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. Tool possession and a trained investigator are components of forensic readiness, but they alone do not constitute full readiness. Without logging infrastructure, retention policies, legal hold processes, and documented procedures, the tools cannot be used effectively when needed.

B) Incorrect. Rapid incident response activation describes incident response readiness, not forensic readiness specifically. Forensic readiness focuses on the ability to collect and preserve legally defensible evidence — which requires infrastructure, policy, and process established proactively.

C) Correct. ISACA's definition of forensic readiness encompasses the organizational state of being prepared to conduct digital investigations before incidents occur. The complete combination — logging, retention, procedures, trained people, legal hold process, and secure storage — is the recognized comprehensive definition.

D) Incorrect. ISAC membership provides threat intelligence and peer support, which are valuable security capabilities, but ISAC membership does not constitute forensic readiness. Forensic readiness requires internal organizational capabilities, not external membership.

---

## Question 14

(5 points) A security analyst is reviewing an after-action report from a phishing-triggered malware incident. The report contains an executive summary, a detailed timeline, and a root cause analysis. The analyst notes that the root cause section identifies three contributing factors but the report does not include any recommendations. From a CISM governance perspective, what is the primary problem with this finding?

A) Three contributing factors are insufficient; the root cause section must identify at least five factors to be acceptable.
B) Without recommendations, the documented root causes cannot produce organizational improvement or risk register updates, defeating the purpose of the after-action process.
C) Contributing factors should not be documented without evidence — the root cause section needs citations to be acceptable.
D) The executive summary section should contain the recommendations; a separate recommendations section is redundant.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. There is no prescribed minimum number of contributing factors in an after-action report. The quality of the analysis matters more than the quantity. This answer focuses on a nonexistent requirement and misses the actual governance deficiency.

B) Correct. The governance purpose of an after-action report is to convert incident experience into organizational improvement. If root causes are identified but no recommendations are generated, the organization has documented what is broken without establishing what will be done to fix it. This is a fundamental governance failure — findings without recommendations create no accountability and produce no change.

C) Incorrect. While evidence-based analysis is best practice, the absence of citations is a quality issue, not the primary governance deficiency. The absence of any recommendations is a more fundamental failure than citation practices.

D) Incorrect. Recommendations typically appear in their own section and are often referenced in the executive summary, but the two sections serve different audiences and levels of detail. The primary problem in this scenario is the complete absence of recommendations, not their placement.

---

## Question 15

(5 points) An organization suspects that an employee has been exfiltrating intellectual property via personal email. Legal counsel authorizes a forensic investigation of the employee's company-issued laptop. The forensic investigator finds a deleted folder containing hundreds of proprietary design documents in the unallocated space of the drive. What forensic technique was used to locate these files, and what does this finding demonstrate about deleted data on Windows systems?

A) Log correlation; deleted files are permanently removed from the drive but their names remain visible in event logs.
B) File carving applied to unallocated disk space; deletion on Windows typically removes file system pointers but does not immediately overwrite the data, leaving recoverable file content in unallocated space.
C) Memory forensics; the deleted files were recovered from the RAM of the powered-on laptop.
D) Network forensics; the files were intercepted before being deleted from the email server.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Event logs record file system activity metadata but do not contain recoverable file content. Log correlation is a detection and timeline reconstruction technique, not a method for recovering deleted file contents from disk.

B) Correct. When a file is deleted in Windows, the operating system marks the clusters as available for reuse but does not immediately zero out the data. File carving tools scan unallocated disk space for file headers and footers matching known file formats, recovering file content even without intact file system metadata. This is a fundamental concept in disk forensics and directly relevant to insider threat investigations.

C) Incorrect. Memory forensics analyzes RAM contents, which would contain currently running processes and recently accessed data — not historically deleted files. Recovering deleted files from disk unallocated space requires disk forensic techniques, not memory analysis.

D) Incorrect. Network forensics involves capturing and analyzing network traffic. While network forensics might reveal exfiltration attempts, the scenario describes recovering deleted files from the physical hard drive — a disk forensics operation, not a network investigation.

---

## Question 16

(5 points) During a post-incident review, the team uses the fault tree analysis method to analyze a ransomware outbreak that encrypted 200 servers. The analysis reveals that the outbreak required three simultaneous failures: a user clicking a malicious link, the email gateway failing to quarantine the attachment, and EDR software not detecting the payload. Which statement best describes the value of fault tree analysis compared to the Five Whys technique for this scenario?

A) Fault tree analysis is less appropriate because it requires specialized software that most organizations do not own.
B) Fault tree analysis is more appropriate because it models how multiple simultaneous contributing failures combine using Boolean logic, revealing that all three failures were required for the outbreak — something the Five Whys linear approach cannot capture.
C) The Five Whys is more appropriate because ransomware incidents always have a single root cause.
D) Fault tree analysis applies only to hardware failures; the Five Whys is always preferred for cybersecurity incidents.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Fault tree analysis can be performed using diagramming tools, whiteboards, or even paper — specialized software is useful but not required. The appropriateness of the method depends on the nature of the incident, not on tool availability.

B) Correct. Fault tree analysis uses AND gates and OR gates to model how combinations of failures must coexist to produce an outcome. In this scenario, the ransomware required all three failures simultaneously — an AND gate condition. The Five Whys is a linear technique that follows a single causal chain; it may miss contributing factor combinations. Fault tree analysis is specifically designed for multi-factor incident scenarios.

C) Incorrect. Ransomware incidents rarely have a single root cause — they typically involve a combination of technical, process, and human factors. Assuming a single cause leads to incomplete remediation and future recurrence.

D) Incorrect. Fault tree analysis is applicable to any complex system failure, including cybersecurity incidents. It originated in safety engineering but has been widely adopted in information security risk and incident analysis. There is no domain restriction to hardware failures.

---

## Question 17

(5 points) An insider threat investigator must acquire email evidence from a Microsoft Exchange server without alerting the suspect employee. The investigator requests that IT perform a targeted mailbox export and deliver the PST file via USB to the investigation team. Which forensic principle is most at risk if the IT administrator accesses the mailbox content during the export?

A) Order of volatility — accessing the mailbox modifies its volatility level.
B) Confidentiality of investigation — unauthorized review of mailbox content during export may constitute a separate legal exposure.
C) Chain of custody — any access to evidence by an unauthorized party without documentation breaks the chain of custody.
D) Hash verification — the PST file hash will be invalidated if the administrator reads the email content.

**Correct Answer: C**

**Distractor Analysis:**

A) Incorrect. Order of volatility refers to the sequence in which evidence should be collected based on how quickly it may be lost. Email stored on an Exchange server is persistent evidence; the administrator accessing the mailbox does not change its volatility classification.

B) Incorrect. While confidentiality of the investigation is an important operational concern, the primary forensic principle at risk from an undocumented access is chain of custody integrity. Investigation confidentiality is a process concern; chain of custody is the legal admissibility concern.

C) Correct. Chain of custody requires that every access to evidence be documented, authorized, and recorded. If the IT administrator accesses mailbox content beyond the scope of their authorized role — and that access is not documented — it creates a gap in the chain of custody that opposing counsel can use to challenge admissibility. All access to evidence must be recorded regardless of who performs it.

D) Incorrect. The hash of a PST export file would be computed after the export is complete. Reading an email client does not alter the underlying PST file bytes. Hash verification confirms that the file itself has not changed — it is not affected by whether someone views the content through an email client interface.

---

## Question 18

(5 points) An organization's legal counsel issues a litigation hold covering all email, network logs, and files related to a specific project. Six months later, the records management system automatically deleted 90 days' worth of network logs covered by the hold because the records management team was not notified of the hold's scope. What is the correct characterization of this event?

A) This is a minor administrative error with no legal consequence because automated deletions are system-generated, not intentional.
B) This constitutes potential spoliation of evidence — the destruction of information covered by a legal hold, regardless of intent, may result in adverse court sanctions.
C) This is acceptable because network logs have a 90-day retention period and retention schedules always override legal holds.
D) This event only creates legal risk if the deleted logs contained evidence material to the litigation — no risk exists if the logs were irrelevant.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Courts have held that spoliation can occur through negligence as well as intentional destruction. The fact that an automated process caused the deletion does not eliminate the organization's culpability if it failed to properly communicate and enforce the legal hold across all relevant systems and custodians.

B) Correct. A legal hold suspends all normal retention and deletion schedules for covered data. Failing to communicate the hold to all relevant parties — including records management — is an organizational failure that can result in spoliation findings. Courts may impose adverse inference instructions, evidence exclusion, or financial sanctions even when destruction was unintentional, if the organization failed to take reasonable steps to preserve evidence.

C) Incorrect. Legal holds explicitly override normal retention schedules. This is the entire purpose of a legal hold — to preserve data that would otherwise be routinely deleted. Retention schedules do not supersede a valid litigation hold.

D) Incorrect. Materiality is typically assessed after the fact, but organizations cannot unilaterally decide that covered evidence is irrelevant as a basis for not preserving it. The opposing party and the court determine materiality. Allowing covered data to be destroyed based on the holder's own materiality judgment creates serious legal risk regardless of the eventual determination.

---

## Question 19

(5 points) A security operations team is preparing for a forensic investigation and must decide between using Autopsy and Volatility as the primary analysis tool. The investigation involves a suspected compromise where the attacker may have injected malicious code into a legitimate running process. Which tool selection is correct, and why?

A) Autopsy, because it is the gold standard for all forensic investigations and can analyze any evidence type.
B) Volatility, because detecting injected code in a running process requires memory forensics — analysis of a RAM image in which the process's memory space can be inspected for indicators of code injection.
C) Wireshark, because injected code communicates over the network, and packet capture will reveal the malicious activity.
D) EnCase, because it is the only commercial tool approved for use in legal proceedings.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Autopsy is a disk forensics platform built on The Sleuth Kit. While it is excellent for file system analysis, artifact extraction, and timeline reconstruction, it cannot analyze running process memory or detect code injection in RAM. It is not a universal tool for all forensic evidence types.

B) Correct. Code injection — techniques such as process hollowing, DLL injection, and reflective DLL loading — leaves evidence primarily in memory. The injected code typically resides in the process's memory space without being written to disk. Volatility's `malfind`, `dlllist`, and `pslist` plugins can identify anomalous memory regions, unsigned executable segments in process memory, and discrepancies between on-disk and in-memory process images that indicate injection.

C) Incorrect. While injected code may generate network traffic, network forensics via Wireshark captures packets at the network layer and cannot inspect the internal memory structure of a process to identify code injection. Network evidence is complementary to memory forensics, not a substitute.

D) Incorrect. EnCase is a reputable commercial disk forensics platform, but it is not the only tool approved for legal proceedings. Properly documented open-source tools including Volatility, Autopsy, and dd are routinely accepted in legal and regulatory proceedings when evidence handling procedures are followed correctly.

---

## Question 20

(5 points) An organization's security incident response policy requires that all post-incident after-action reports for severity-1 incidents be completed and distributed to the board within ten business days. Following a major ransomware incident, the security team delivers the after-action report on day fifteen, citing the complexity of the root cause analysis. From a CISM governance perspective, what is the most significant concern?

A) The root cause analysis was too thorough; it should be abbreviated to meet the timeline requirement.
B) The after-action report delivery exceeded the policy-mandated timeline, creating a governance gap and potentially delaying board-level risk response decisions.
C) The board does not need to review after-action reports; the CISO is the appropriate final recipient.
D) The ten-business-day policy is unrealistic for ransomware incidents and should be revised to thirty days.

**Correct Answer: B**

**Distractor Analysis:**

A) Incorrect. Abbreviating root cause analysis to meet a timeline is counterproductive — a superficial root cause analysis produces poor findings and ineffective remediation. The solution is policy compliance or a documented policy exception, not reduced analytical quality.

B) Correct. The CISM governance principle is that incident response policies — including reporting timelines — exist to ensure timely governance oversight and accountability. A fifteen-day delivery for a ten-day policy requirement means the board received critical risk information five days late, potentially delaying risk-informed decisions about additional investment, regulatory notification timing, or stakeholder communication. The delay is a policy compliance failure and should be documented and addressed.

C) Incorrect. Board oversight of significant incidents is a core governance responsibility. Major incidents — particularly those with financial, regulatory, or reputational impact — require board-level visibility because they affect organizational risk posture at a strategic level. The CISO cannot be the final recipient for severity-1 incidents in a well-governed organization.

D) Incorrect. While policy revision may ultimately be appropriate if the timeline is consistently unachievable, the correct immediate response is to document the deviation, understand why it occurred, and address the root cause. Retroactively revising policies to match actual performance without analysis converts compliance failures into the new standard and undermines governance accountability.

---

## Quiz Answer Key

| Question | Correct Answer | Topic |
|---|---|---|
| 1 | B | Evidence preservation and write blockers |
| 2 | C | Order of volatility |
| 3 | C | Five Whys and root cause analysis |
| 4 | C | Hash integrity verification |
| 5 | B | Legal hold |
| 6 | C | Memory forensics tools |
| 7 | C | After-action report governance |
| 8 | C | Fishbone diagram categories |
| 9 | B | Forensic readiness |
| 10 | B | Anti-forensic activity recognition |
| 11 | B | Hash comparison scope and limitations |
| 12 | B | Forensic acquisition verification |
| 13 | C | Forensic readiness components |
| 14 | B | After-action report recommendations |
| 15 | B | File carving and deleted data recovery |
| 16 | B | Fault tree analysis vs Five Whys |
| 17 | C | Chain of custody in insider investigations |
| 18 | B | Spoliation and litigation hold compliance |
| 19 | B | Memory forensics tool selection |
| 20 | B | After-action report governance timeline |
