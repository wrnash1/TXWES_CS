# Quiz: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is open-note but must reflect your own work. Questions are written to match the difficulty and style of the CompTIA Security+ SY0-701 exam.

---

## Question 1

A security analyst is reviewing SIEM alerts. One alert indicates that a single workstation generated 1,200 failed authentication attempts against a domain controller in a five-minute window. The analyst confirms the alerts are genuine. According to NIST SP 800-61, which phase of the incident response lifecycle is the analyst performing?

A) Preparation

B) Containment

C) Detection and Analysis

D) Post-Incident Activity

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Preparation occurs before any incident. It includes building the IR plan, training the team, and deploying tools. Reviewing and analyzing alerts is not preparation — it is an active investigation activity.
- Why B is incorrect: Containment applies after a decision has been made that an incident is occurring. The analyst is still in the process of determining what the event means and whether it constitutes an incident.
- Why D is incorrect: Post-Incident Activity (lessons learned) occurs after the incident has been fully resolved. Reviewing live SIEM alerts during an active event is detection and analysis.

---

## Question 2

A forensic investigator arrives at a scene to image a suspect workstation. Before touching the keyboard or attaching any equipment, she connects a hardware device between the suspect hard drive and her forensic laptop. What is this device and what does it do?

A) A network tap that captures all traffic from the workstation

B) A write blocker that allows the drive to be read without allowing any writes

C) A cryptographic accelerator that speeds up hash verification

D) A Faraday cage adapter that prevents wireless signals from the drive

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A network tap captures network traffic — it is a passive monitoring device placed inline on a network connection. It does not interface between a storage drive and a forensic workstation.
- Why C is incorrect: Cryptographic accelerators are hardware devices that offload cryptographic computation. They are used in high-volume server environments, not in forensic disk imaging workflows to protect evidence integrity.
- Why D is incorrect: Faraday cages block electromagnetic signals and are used to isolate wireless devices (phones, laptops) from cellular or Wi-Fi networks. Hard drives do not transmit wireless signals requiring this type of isolation.

---

## Question 3

An organization discovers an attacker has had persistent access to their network for six weeks. The IR team wants to observe the attacker's behavior to map their full infrastructure before ejecting them. Which containment approach does this represent?

A) Isolation

B) Black-holing

C) Controlled observation / sinkholing

D) Eradication

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Isolation immediately disconnects the affected system from the network. This would alert the attacker and end the observation opportunity described in the scenario.
- Why B is incorrect: Black-holing routes traffic to a dead-end, effectively cutting off the attacker's communications. This stops the attacker but does not allow observation of their behavior.
- Why D is incorrect: Eradication removes the attacker's presence and closes the vulnerability. It is the phase after containment — the scenario explicitly describes a decision to delay eradication in order to observe.

---

## Question 4

An IR team has completed containment and removed malware from 12 infected workstations. They plan to restore the systems to production by applying the most recent system backup from the previous night. The IR manager stops the team and says the previous night's backup cannot be trusted. Why is the IR manager correct?

A) Backups cannot be verified with cryptographic hashes

B) The backup was created after the compromise began and may contain the malware

C) Restoring from backup is not part of the NIST IR lifecycle

D) The backup must be reviewed by legal counsel before it can be used in recovery

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Backups can and should be verified with cryptographic hashes. Many backup systems include hash verification. The problem is not about hash verification capability.
- Why C is incorrect: Recovery, including restoration from backups, is explicitly part of Phase 3 of the NIST IR lifecycle. The concern is not about whether backups should be used, but which backup is safe to use.
- Why D is incorrect: Legal counsel reviews evidence and notification obligations, not backup files used for recovery. There is no general requirement for legal review before restoring a backup.

---

## Question 5

An analyst lists the following evidence sources in order of collection priority for a live compromised system: disk image, RAM capture, network state, swap file. Which ordering correctly reflects the order of volatility?

A) RAM capture, network state, swap file, disk image

B) Disk image, swap file, network state, RAM capture

C) Network state, RAM capture, disk image, swap file

D) Swap file, disk image, RAM capture, network state

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: This is essentially the reverse of the correct order of volatility. Disk images persist indefinitely and should be collected last among these four. RAM is the most volatile and disappears on power-off.
- Why C is incorrect: Network state (ARP cache, active connections) is volatile but less volatile than RAM. RAM should always be captured before network state because RAM data is immediately lost at shutdown.
- Why D is incorrect: Swap file is more persistent than RAM because it resides on disk, but RAM captures in-use process data not yet written to swap. This ordering incorrectly places swap before RAM and RAM before network state.

---

## Question 6

A healthcare organization experiences a ransomware attack that encrypts patient records. The organization determines that 62,000 patient records were accessible by the ransomware. According to HIPAA, what notification action is required?

A) No notification is required if the organization pays the ransom and decrypts the data

B) Notification to affected individuals is required within 60 days; HHS must be notified immediately for breaches affecting 500 or more individuals

C) Notification to the FBI must occur within 24 hours before any other action

D) Notification is only required if the encrypted data was exfiltrated outside the organization

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: HIPAA breach notification obligations are not contingent on whether the organization recovers the data. If protected health information was accessed or potentially accessed by an unauthorized party, the breach notification requirement applies regardless of recovery.
- Why C is incorrect: HIPAA does not require FBI notification. Law enforcement notification is discretionary based on the organization's legal and operational decisions, not a HIPAA mandate.
- Why D is incorrect: HIPAA breach notification applies when PHI was acquired or accessed by an unauthorized person. Encryption of data in place — even without confirmed exfiltration — can still constitute a breach that triggers notification obligations under HIPAA's risk assessment framework.

---

## Question 7

During a post-incident review, the IR manager asks: "We first detected this incident on Day 14. The earliest evidence in our logs shows the attacker was present on Day 1. What does the gap between Day 1 and Day 14 represent?"

A) The recovery window

B) The dwell time

C) The mean time to respond

D) The attack surface exposure period

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The recovery window is the period after incident confirmation during which systems are restored to normal operation. It begins after containment and eradication.
- Why C is incorrect: Mean time to respond (MTTR) measures the average time from alert generation to initiating a response action. It does not specifically refer to the gap between compromise and detection.
- Why D is incorrect: Attack surface exposure period is not a standard incident response metric. Dwell time is the specific, widely-used term for the period between initial compromise and detection.

---

## Question 8

A chain of custody log for a hard drive shows the following sequence: Analyst A collected the drive → Analyst B signed for it to perform imaging → Analyst A signed for it back → Drive was placed in evidence storage. Three weeks later, a defense attorney argues that the chain of custody is broken. Which scenario would BEST support the attorney's argument?

A) Two different analysts handled the evidence at different times

B) There is a two-hour gap in the log between Analyst B returning the drive and its placement in evidence storage with no entry explaining the gap

C) The drive was stored in a locked evidence cabinet rather than a vault

D) The chain of custody log was kept in digital form rather than paper

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Multiple analysts handling evidence is normal and expected in a proper chain of custody. What matters is that each handoff is documented, not that only one person handles the evidence.
- Why C is incorrect: A locked evidence cabinet is an acceptable form of evidence storage. The type of storage container does not inherently break chain of custody as long as access is logged.
- Why D is incorrect: Digital chain of custody records are widely accepted and used. The format of the log does not determine whether chain of custody is intact; the completeness and accuracy of the entries does.

---

## Question 9

A company's IR playbook specifies that after an incident is confirmed, the communications lead must notify external customers within 48 hours of confirmation. During a real incident, the communications lead sent a notification 24 hours after confirmation. Three months later, in the lessons learned review, a team member says the 24-hour notification was a mistake. What is the most likely concern?

A) The notification was sent too slowly relative to industry best practice

B) The notification may have been premature, disclosing information before the investigation was complete, potentially alerting the attacker or creating legal liability

C) External notifications should always be handled by legal counsel, not the communications lead

D) The 48-hour policy is too slow to comply with GDPR and should be shortened to 24 hours

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The notification was faster, not slower, than the plan specified. The concern is not about speed relative to best practice — it is about whether notifying before the investigation is complete creates new risks.
- Why C is incorrect: Legal counsel advises on notification content and timing, but communications leads are typically authorized to issue notifications. The concern is about timing and completeness of the investigation, not who sent the notification.
- Why D is incorrect: GDPR's 72-hour notification requirement applies to the supervisory authority, not directly to customers. Even if the policy should be aligned with GDPR, the question focuses on a specific early notification during investigation, not policy adequacy.

---

## Question 10

An organization's tabletop exercise reveals that the IR plan does not specify who is authorized to approve disconnecting a compromised system from the production network — a decision that would cause approximately 30 minutes of downtime. Which IR lifecycle phase should the finding be addressed in, and how?

A) Detection and Analysis — by training analysts to make autonomous containment decisions

B) Containment — by documenting the specific decision in the playbook during the current exercise

C) Preparation — by updating the IR plan and escalation matrix before the next incident

D) Post-Incident Activity — by documenting the gap in the lessons learned report after an actual incident

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Detection and analysis is about identifying and classifying incidents, not about authority structures for containment decisions. Making analysts autonomous for business-impacting decisions without executive authorization creates governance and liability risks.
- Why B is incorrect: While the tabletop exercise can surface the issue, documenting the fix "during the current exercise" means the change would only exist in exercise notes and not be formalized. The fix belongs in the IR plan, which is a Preparation-phase artifact.
- Why D is incorrect: Post-Incident Activity addresses findings after a real incident occurs. The tabletop exercise has already revealed the gap. Waiting for a real incident to formally address it means the organization will face the same decision ambiguity under actual pressure.

---

---

## Question 11

A forensic analyst is investigating a compromised Linux server. The analyst needs to determine what processes were running at the time of compromise and what network connections they had established. The server has since been rebooted for operational reasons. Which evidence source is no longer available due to the reboot?

A) The system's disk image, because rebooting overwrites the file system

B) The contents of RAM, because RAM is volatile and cleared on power-off

C) The server's event logs, because log rotation occurs on reboot

D) The firewall's NetFlow records, which are deleted on reboot

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Rebooting a system does not overwrite the file system. Disk contents including files, logs, and registry entries persist across reboots. The disk image remains collectable and valid after a reboot.
- Why C is incorrect: System event logs are written to disk and persist across reboots. Log rotation is a scheduled process based on size or time, not triggered by reboots in standard configurations.
- Why D is incorrect: NetFlow records are collected by network devices (routers, firewalls) and stored on those devices or a central collector — they are not stored in the server's RAM and are not affected by the server's reboot state.

---

## Question 12

An organization's IR plan classifies incidents by severity using four tiers: P1 (critical — all hands), P2 (high — senior analyst response), P3 (medium — standard response), P4 (low — next business day). A ransomware attack encrypts the organization's active directory domain controllers, taking down authentication for all 4,000 employees. Which tier applies, and what is the FIRST action the IR team lead should take?

A) P2 — Assign a senior analyst and begin investigation per standard playbook

B) P1 — Invoke the all-hands response and activate the IR plan's major incident procedures, including executive notification

C) P3 — Restore domain controllers from backup and document as a standard recovery event

D) P4 — Log the ticket and schedule remediation for the next business day since ransomware is a known threat type

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: An attack rendering authentication unavailable for 4,000 employees meets any reasonable definition of a critical P1 incident. A senior analyst response without executive notification and all-hands mobilization is insufficient for an enterprise-wide authentication outage.
- Why C is incorrect: Ransomware on domain controllers is not a standard recovery event. The scope (all users impacted), the attacker's persistence in the environment, and potential lateral movement require the full IR lifecycle — not a simple restore.
- Why D is incorrect: An active ransomware attack affecting the entire organization cannot wait until the next business day. Deferring the response allows the attacker to establish additional persistence, exfiltrate data, or extend encryption.

---

## Question 13

During eradication following a breach, the IR team removes all identified malware and patches the exploited vulnerability. Two weeks later, the same attacker regains access through the same system. Which eradication failure is MOST likely responsible?

A) The team did not update the IDS signatures after eradication

B) A backdoor or secondary persistence mechanism was not identified and removed during eradication

C) The lessons learned review was not completed before recovery

D) The team restored from a backup that predated the initial compromise

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Updating IDS signatures improves detection but does not prevent re-entry if the attacker's persistence mechanism was not removed. A missed backdoor allows re-access regardless of detection capability.
- Why C is incorrect: The lessons learned review is a post-incident improvement process. Completing or skipping it does not affect whether the attacker can re-access the system — eradication completeness is what determines re-compromise risk.
- Why D is incorrect: Restoring from a backup predating the compromise would be a recovery best practice, not a failure. If the team restored from a clean pre-compromise backup, the system should not contain malware. The failure is missing a persistence mechanism during eradication, not the backup selection.

---

## Question 14

An organization is subject to GDPR and experiences a data breach affecting personal data of 3,200 EU residents. The breach occurred on a Tuesday. When must the organization notify the supervisory authority?

A) Within 72 hours of becoming aware of the breach — by Friday at the latest

B) Within 30 days of discovery to allow time for a complete investigation

C) Only if the individuals affected formally request notification

D) Within 24 hours of discovery, as GDPR requires same-day notification for personal data

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: GDPR Article 33 requires notification to the supervisory authority within 72 hours of becoming aware of a breach — not 30 days. A 30-day window is found in some US state breach notification laws, not GDPR.
- Why C is incorrect: GDPR breach notification to the supervisory authority is mandatory — it is not contingent on individual requests. Notification to affected individuals (Article 34) may also be required if the breach poses a high risk, but it is separate from the supervisory authority notification.
- Why D is incorrect: GDPR specifies 72 hours, not 24 hours, for supervisory authority notification. If 72 hours cannot be met, the notification must still be submitted with a reasoned explanation for the delay.

---

## Question 15

A junior analyst is performing memory forensics on a live system and uses the `strings` command to extract readable text from a RAM dump. The analyst finds what appears to be a plaintext encryption key in the output. Which property of volatile memory does this finding demonstrate?

A) RAM stores only program executables; the key must have been loaded from disk

B) Memory encryption prevents readable strings from appearing in RAM dumps

C) Cryptographic keys, passwords, and other secrets exist in plaintext in RAM during active use, making memory acquisition a high-value forensic target

D) The `strings` command only retrieves data from the swap file, not from RAM

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: RAM stores all running process data — not just executables — including heap memory, stack variables, network buffers, and cryptographic material. The observation is correct: encryption keys appear in RAM during use.
- Why B is incorrect: Standard RAM on most systems is not encrypted at rest. Memory encryption technologies (AMD SME, Intel TME) exist but are not universally deployed, and even encrypted-in-transit keys are decrypted in CPU registers and memory regions during active operations.
- Why D is incorrect: The `strings` command, when applied to a raw memory dump file, extracts readable ASCII/Unicode strings from that dump. It operates on whatever file is provided as input — including raw RAM dumps, not just swap files.

---

## Question 16

An organization's IR team uses a SIEM to correlate log data. During an incident, analysts observe that log entries from a critical server stop appearing in the SIEM at 11:47 PM on the night of a suspected compromise. Which explanation MOST warrants investigation?

A) The server's time zone was changed, causing a timestamp offset in the SIEM

B) An attacker may have disabled or cleared the logging agent on the server to reduce their forensic footprint

C) SIEM log ingestion pipelines routinely pause at midnight for maintenance

D) The server's disk filled up, and the OS automatically paused log writing

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A time zone change would shift timestamps, not stop log entries entirely. Logs would still appear in the SIEM but with offset times.
- Why C is incorrect: SIEM log ingestion pipelines are designed for high availability. Scheduled maintenance pauses are typically pre-announced and affect all log sources simultaneously, not a single server.
- Why D is incorrect: While a full disk can pause OS logging, the timing — precisely during a suspected compromise — makes attacker action the higher-priority hypothesis to investigate. Full disk conditions also typically generate system alerts through other channels.

---

## Question 17

A company's tabletop exercise simulates a ransomware attack on their file servers. During the exercise, the team discovers that IT only has the personal cell phone numbers of two executives — neither of whom is available. The primary communication channel (corporate email) would be encrypted by the ransomware in the scenario. Which gap does this reveal, and in which IR phase should it be addressed?

A) Detection gap — the SIEM should detect ransomware before it encrypts the email server; address in Detection and Analysis

B) Eradication gap — executives should be involved in eradication decisions; address in Containment/Eradication/Recovery

C) Communication gap — the IR plan lacks an out-of-band communication method and complete emergency contact list; address in Preparation

D) Recovery gap — the organization should back up executive contact information; address in Post-Incident Activity

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: The gap described is not about detection capability. The SIEM may detect the attack but cannot fix the inability to reach executives when email is down.
- Why B is incorrect: The lack of communication channels is a pre-incident planning failure, not an eradication phase gap. Eradication focuses on removing attacker presence — executive contact methods are needed much earlier.
- Why D is incorrect: Post-Incident Activity addresses improvements after a real incident. The tabletop exercise has identified the gap while still in Preparation. The appropriate action is to fix the IR plan now, before an actual incident forces the team to work around the gap.

---

## Question 18

A forensic investigator hashes a seized hard drive immediately upon collection and records SHA-256: `a7f3...`. After imaging, the investigator hashes the forensic image and records SHA-256: `a7f3...`. Three weeks later, during trial, the investigator hashes the original drive again and records SHA-256: `a7f3...`. What does this consistent hash value across all three points in time prove?

A) The hard drive contains no deleted files, because deleted files would change the hash

B) The hash algorithm SHA-256 has no known collisions, proving the drive is authentic

C) The bit-level content of the drive has not changed since original collection, establishing integrity for the chain of custody

D) The original drive and the forensic image are the same physical device

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Deleted files occupy space in the unallocated clusters of the drive. A forensic image captures the full disk including unallocated space. The presence or absence of deleted files does not affect whether the hash is consistent — what matters is that nothing changed.
- Why B is incorrect: SHA-256 having no known practical collisions strengthens confidence, but the hash value's purpose in chain of custody is to detect any modification — even a single bit change would produce a different hash. The statement that it "proves authenticity" conflates integrity with provenance.
- Why D is incorrect: A forensic image is a copy, not the same physical device. The identical SHA-256 hash proves the image is an exact bit-for-bit copy of the original, but they remain distinct objects.

---

## Question 19

A security analyst is asked to categorize a collection of observations from a compromised endpoint. Which observation is BEST classified as an Indicator of Attack (IOA) rather than an Indicator of Compromise (IOC)?

A) A file hash matching a known ransomware sample in the NIST National Software Reference Library

B) An IP address listed on multiple threat intelligence feeds as a known C2 server

C) A process spawning `cmd.exe` as a child process via a Microsoft Office document immediately after the document is opened

D) A registry key value matching a known malware persistence entry

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A file hash matching a known malware sample is an artifact-based Indicator of Compromise — it identifies a specific known-malicious file. It is retrospective and signature-based.
- Why B is incorrect: A threat intelligence feed entry for a known C2 IP is an Indicator of Compromise — a specific artifact known to be associated with malicious activity.
- Why D is incorrect: A registry key matching a known persistence entry is also an Indicator of Compromise — a specific artifact of a known persistence technique.

---

## Question 20

An organization recovers from a ransomware incident and holds a lessons learned meeting two months later. An attendee argues that two months is too long to wait and that the review should have been held sooner. According to NIST SP 800-61 guidance, what is the recommended timing, and why does it matter?

A) NIST recommends waiting at least 90 days to allow all legal matters to be resolved before discussing the incident internally

B) NIST recommends holding the lessons learned meeting within one to two weeks of incident closure while details are fresh and improvement actions can be implemented before the next incident

C) NIST does not specify a timeframe — any timing is acceptable as long as the meeting occurs eventually

D) NIST recommends holding the lessons learned meeting simultaneously with eradication so improvements are applied immediately

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: NIST SP 800-61 does not recommend waiting for legal resolution before holding an internal lessons learned review. Legal counsel participation is appropriate, but legal proceedings do not delay the internal improvement process.
- Why C is incorrect: NIST SP 800-61 Section 3.4 specifically recommends holding the lessons learned meeting as soon as possible after the incident — ideally within one to two weeks. Vague timing guidance is not what NIST provides.
- Why D is incorrect: Eradication occurs while the incident is still active. Holding a lessons learned meeting during active eradication would be premature and would not have the full incident scope needed for meaningful analysis.

---

*End of Quiz — Module 11*
