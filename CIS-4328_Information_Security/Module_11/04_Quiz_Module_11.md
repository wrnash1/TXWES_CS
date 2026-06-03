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

*End of Quiz — Module 11*
