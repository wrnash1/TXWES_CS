# Quiz: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

This quiz contains 20 questions aligned to Security+ SY0-701 exam objectives. Time limit: 30 minutes. Each question is worth 5 points. A score of 75 or higher (15/20) is required to pass.

---

## Questions

**Question 1**

An organization has just completed drafting an incident response plan, identified team members, deployed SIEM and EDR tools, and conducted a tabletop exercise. Which phase of the NIST SP 800-61 incident response lifecycle do all of these activities belong to?

- A. Detection and Analysis
- B. Containment, Eradication, and Recovery
- C. Preparation
- D. Post-Incident Activity

---

**Question 2**

A security analyst receives an EDR alert indicating that a process on a workstation is attempting to encrypt files and delete shadow copies. The analyst validates the alert is a true positive. Which phase of the NIST IR lifecycle are these activities — receiving and validating the alert — part of?

- A. Preparation
- B. Detection and Analysis
- C. Containment
- D. Post-Incident Activity

---

**Question 3**

During an incident involving ransomware, a responder needs to collect evidence from an infected Windows workstation that is still powered on. Which evidence source should be collected FIRST based on the order of volatility?

- A. The contents of the hard drive
- B. The Windows Event Logs stored on disk
- C. The contents of system RAM
- D. The ransom note file on the desktop

---

**Question 4**

An incident responder follows these steps: disconnects the affected server from the network, blocks the attacker's known IP addresses at the firewall, and applies emergency access restrictions on affected accounts. Which sub-phase of the NIST IR lifecycle do these actions represent?

- A. Eradication
- B. Recovery
- C. Short-term containment
- D. Detection

---

**Question 5**

After containing an incident, the IR team removes all malware artifacts, deletes unauthorized accounts the attacker created, resets all compromised credentials, and patches the exploited vulnerability. Which sub-phase does this describe?

- A. Containment
- B. Eradication
- C. Recovery
- D. Post-Incident Activity

---

**Question 6**

A forensic investigator collects a hard drive from a compromised server. The investigator documents the drive's make, model, and serial number; records the SHA-256 hash; seals it in a tamper-evident bag; and logs their name, the date/time, and the collection location. The investigator then hands the drive to a colleague for analysis and records this transfer. What does this documentation practice establish?

- A. Non-repudiation for the attacker
- B. Chain of custody
- C. Order of volatility compliance
- D. Evidence classification level

---

**Question 7**

An organization's security team discovers an active data exfiltration event. The team wants to observe the attacker to gather threat intelligence about their tools and targets before intervening. Which containment approach does this describe?

- A. Aggressive short-term containment
- B. Long-term containment
- C. Delayed containment for intelligence gathering
- D. Eradication without prior containment

---

**Question 8**

A CISO reports that the organization's Mean Time to Detect (MTTD) for the previous year was 210 days. What does this metric indicate about the organization's security posture?

- A. The organization responds to incidents in 210 days on average
- B. Attackers were present in the environment for an average of 210 days before detection
- C. The organization takes 210 days to fully recover from incidents
- D. The organization has had no incidents detected in 210 days

---

**Question 9**

During an incident, the security team communicates exclusively via the company's normal Microsoft Teams environment. The IR manager is later concerned that the attacker may have had access to Teams and monitored the response. What specific control should the IR plan have required?

- A. Encrypted email for all communications
- B. An out-of-band communication channel separate from potentially compromised systems
- C. All communications routed through legal counsel
- D. Verbal-only communications with no electronic records

---

**Question 10**

An incident responder is analyzing a compromised endpoint. Which item in the following list is classified as volatile evidence that must be collected before the system is powered off?

- A. Files stored in the Documents folder
- B. The Windows Registry hive files on disk
- C. The list of currently active network connections
- D. Log files archived to a SIEM two weeks ago

---

**Question 11**

Following a security incident, the organization holds a meeting to review the timeline, identify what worked and what failed, and assign improvement actions. Which phase of the NIST IR lifecycle does this meeting occur in?

- A. Preparation
- B. Detection and Analysis
- C. Containment, Eradication, and Recovery
- D. Post-Incident Activity

---

**Question 12**

A company experiences a data breach involving customer PII. The company's breach notification legal obligation requires informing affected individuals within 30 days. On day 29, legal counsel has not yet approved the draft notification. Who bears responsibility for ensuring the notification is sent on time?

- A. Legal counsel, as they control the approval process
- B. The incident commander and legal counsel jointly, as notifications require both technical accuracy and legal review
- C. The PR team, as customer communications are their responsibility
- D. The CISO, as the most senior security official

---

**Question 13**

An IR team collects a forensic image of a compromised hard drive. They verify the SHA-256 hash matches the value recorded at collection after the image is copied to the analysis workstation. What does a matching hash confirm?

- A. The drive was not involved in the incident
- B. The forensic image has not been modified since collection
- C. The drive contains no malware
- D. The chain of custody is complete

---

**Question 14**

The playbook for responding to phishing incidents includes specific steps for: identifying affected accounts, resetting compromised passwords, reviewing mail server logs, and notifying potentially affected users. What is the PRIMARY purpose of documenting playbooks in advance?

- A. To satisfy audit requirements for ISO 27001 certification
- B. To ensure responders can execute consistent, tested procedures under pressure during an actual incident
- C. To document the organization's legal obligations during incidents
- D. To demonstrate IR capability to cyber insurance underwriters

---

**Question 15**

During an incident, the CISO instructs the IT team to rebuild compromised servers from clean OS images and restore data from the last known-good backup. Which IR phase does rebuilding systems from backups represent?

- A. Containment
- B. Eradication
- C. Recovery
- D. Post-Incident Activity

---

**Question 16**

An organization's incident response team is composed of members from IT security, legal, HR, PR, and business operations. These individuals work their normal jobs between incidents and assemble when an incident is declared. What is this team structure called?

- A. Dedicated CSIRT
- B. Virtual CSIRT
- C. External IR retainer
- D. Managed Security Service Provider (MSSP)

---

**Question 17**

A security analyst discovers an attacker has been present in the network for 45 days. During that time, the attacker moved laterally to 12 systems and accessed a file server containing sensitive contracts. The incident is now contained. Which IR metric does the "45 days" represent?

- A. MTTR
- B. MTTD
- C. RPO (Recovery Point Objective)
- D. RTO (Recovery Time Objective)

---

**Question 18**

An IR team member discovers that a compromised server stores customer health records. HIPAA requires covered entities to notify the Department of Health and Human Services of breaches affecting more than 500 individuals. At what point in the IR process should legal counsel be engaged regarding this notification?

- A. Only after full eradication is complete
- B. Only during post-incident activity
- C. As early as Detection and Analysis when a breach is suspected
- D. Only when HHS proactively contacts the organization

---

**Question 19**

During a lessons learned meeting, the team discovers that the IR plan did not include a procedure for notifying the cyber insurance carrier during an incident. As a result, the carrier is denying coverage because they were not notified within their required timeframe. What type of improvement action should result from this finding?

- A. Replace the SIEM with a tool that automatically notifies the insurer
- B. Update the IR plan and notification procedures to include cyber insurance carrier notification as a required step with a defined timeline
- C. Remove cyber insurance from the organization's risk management strategy
- D. Require all analysts to take additional training in legal compliance

---

**Question 20**

A security analyst collects the following items during an incident response. Arrange them from most volatile to least volatile: (A) a backup tape, (B) a running process list, (C) a file on a USB drive found near a workstation, (D) the contents of the workstation's RAM.

- A. D → B → C → A
- B. B → D → A → C
- C. A → C → B → D
- D. D → B → A → C

---

## Answer Key

*For instructor use only — do not distribute to students*

| Question | Answer | Objective |
|---|---|---|
| 1 | C | 4.2 — IR phases / Preparation |
| 2 | B | 4.2 — Detection and Analysis |
| 3 | C | 4.3 — Order of volatility |
| 4 | C | 4.2 — Short-term containment |
| 5 | B | 4.2 — Eradication |
| 6 | B | 4.3 — Chain of custody |
| 7 | C | 4.4 — Containment strategy |
| 8 | B | 4.2 — MTTD interpretation |
| 9 | B | 4.2 — Out-of-band communication |
| 10 | C | 4.3 — Volatile evidence |
| 11 | D | 4.2 — Post-incident / lessons learned |
| 12 | B | 4.2 — Notification responsibility |
| 13 | B | 4.3 — Hash verification / integrity |
| 14 | B | 4.2 — Playbook purpose |
| 15 | C | 4.2 — Recovery phase |
| 16 | B | 4.2 — Virtual CSIRT |
| 17 | B | 4.2 — MTTD definition |
| 18 | C | 4.2 — Legal involvement timing |
| 19 | B | 4.2 — Lessons learned improvement |
| 20 | A | 4.3 — Order of volatility sequence |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 11*
