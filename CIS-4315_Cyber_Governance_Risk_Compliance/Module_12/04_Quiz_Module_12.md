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
