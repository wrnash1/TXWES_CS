# Quiz: Module 01 - Security Operations & Analyst Role

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer. Review the distractor analysis after completing the quiz to reinforce your understanding of why each wrong answer is incorrect.

---

## Question 1

What does the acronym IOC stand for in security operations?

- A) Index of Controls
- B) Indicator of Compromise
- C) Institution of Cybersecurity
- D) Internal Operational Check

Correct Answer: B

Distractor Analysis:

- A is incorrect. "Index of Controls" is not a recognized security term.
- B is correct. An Indicator of Compromise is an observable artifact — such as a file hash, IP address, or domain name — that provides evidence a system has been compromised or is under attack.
- C is incorrect. "Institution of Cybersecurity" is not a recognized term in the field.
- D is incorrect. "Internal Operational Check" is fabricated and has no meaning in security operations.

---

## Question 2

In a SOC, which of the following best defines the threat landscape?

- A) A SIEM dashboard view showing real-time firewall throughput statistics
- B) The complete set of threat actors, attack vectors, and vulnerabilities relevant to an organization at a given time
- C) A cryptographic method that uses a public key to encrypt data and a private key to decrypt it
- D) The maximum acceptable downtime before business operations are critically impacted

Correct Answer: B

Distractor Analysis:

- A is incorrect. A SIEM dashboard is a tool used to observe part of the threat landscape; it is not the landscape itself.
- B is correct. The threat landscape is the holistic picture of adversaries, techniques, and weaknesses facing an organization, which SOC analysts must continuously monitor and assess.
- C is incorrect. This describes asymmetric (public-key) encryption, which is a cryptographic concept unrelated to threat landscape.
- D is incorrect. This describes Recovery Time Objective (RTO), a business continuity metric unrelated to the threat landscape.

---

## Question 3

A SOC analyst receives an alert showing multiple failed SSH login attempts from a single external IP address followed by a successful login. Which action is the most appropriate first step?

- A) Immediately block the external IP address at the perimeter firewall
- B) Verify whether the successful login matches an authorized user and correlate the source IP against threat intelligence feeds
- C) Reimage the target system to ensure no persistent malware was installed
- D) Close the alert as a false positive since the login eventually succeeded

Correct Answer: B

Distractor Analysis:

- A is incorrect. Blocking before verifying may interrupt legitimate business activity and skips the required triage step; the exam consistently marks premature containment as wrong.
- B is correct. Triage requires confirming the alert is a true positive by checking user authorization and threat intelligence context before taking any containment action.
- C is incorrect. Reimaging is a remediation action performed after confirmation and management approval — not a first triage step.
- D is incorrect. A successful login after repeated failures is a classic brute-force success pattern and must never be dismissed without thorough investigation.

---

## Question 4

Which of the following best describes the primary role of a Tier 1 SOC analyst?

- A) Leading threat hunting operations and developing custom SIEM detection rules
- B) Performing initial alert triage, filtering false positives, and escalating confirmed incidents to Tier 2
- C) Conducting post-incident forensic analysis and producing executive-level reports
- D) Managing network infrastructure and applying security patches to production systems

Correct Answer: B

Distractor Analysis:

- A is incorrect. Threat hunting and custom rule development are Tier 3 or senior analyst responsibilities that require significantly deeper expertise and experience.
- B is correct. Tier 1 analysts are the first responders — they monitor the alert queue, apply playbooks, determine whether an alert is real, and hand off confirmed incidents to Tier 2.
- C is incorrect. Forensic analysis and executive reporting are Tier 2/3 and management responsibilities.
- D is incorrect. Infrastructure management and patching are IT operations roles; they fall outside the SOC analyst's job function.

---

## Question 5

When designing a monitoring strategy for a SOC, which control best mitigates the risk of an attacker deleting local system logs after a breach to conceal their activity?

- A) Enforce multi-factor authentication on all privileged accounts
- B) Forward all system logs in real time to a centralized, write-protected SIEM platform
- C) Enable full-disk encryption on all endpoint systems
- D) Deploy a host-based intrusion prevention system on every workstation

Correct Answer: B

Distractor Analysis:

- A is incorrect. MFA protects against unauthorized account access but does not prevent an already-authenticated attacker from deleting local logs on a compromised system.
- B is correct. Centralizing logs to an immutable or write-protected SIEM ensures that even if local logs are deleted, the off-system copy remains intact for investigation and legal proceedings.
- C is incorrect. Full-disk encryption protects data confidentiality at rest but does not prevent a logged-in user or attacker from deleting log files.
- D is incorrect. HIPS can block some malicious actions but does not guarantee log preservation; a privileged attacker can often disable or bypass host-based controls.

---

## Question 6

An organization experiences a ransomware attack that encrypts all files on its file servers, making them inaccessible to employees for three days. Which pillar of the CIA Triad is most directly violated?

- A) Confidentiality
- B) Integrity
- C) Availability
- D) Authentication

Correct Answer: C

Distractor Analysis:

- A is incorrect. Confidentiality is violated when data is accessed by unauthorized parties. Ransomware encrypts data to prevent access but does not necessarily exfiltrate it.
- B is incorrect. Integrity is violated when data is modified without authorization. Encryption changes data, but the primary harm here is that users cannot access their files.
- C is correct. Availability is violated when legitimate users cannot access systems or data. Ransomware that makes files inaccessible for three days is a direct Availability attack.
- D is incorrect. Authentication is a security mechanism, not a pillar of the CIA Triad.

---

## Question 7

Which of the following best describes the difference between a false negative and a false positive in the context of SIEM alerts?

- A) A false negative is a blocked threat; a false positive is an allowed threat
- B) A false negative is an undetected real attack; a false positive is a detected non-attack
- C) A false negative is a Tier 1 error; a false positive is a Tier 2 error
- D) A false negative requires escalation; a false positive requires remediation

Correct Answer: B

Distractor Analysis:

- A is incorrect. This confuses the alert classification terminology with firewall allow/deny actions.
- B is correct. A false negative means a real attack occurred but the SIEM did not fire an alert — this is the most dangerous scenario. A false positive means the SIEM fired an alert but no real threat exists — this creates unnecessary work.
- C is incorrect. Both false negatives and false positives can be identified or created at any analyst tier; the terms are not tier-specific.
- D is incorrect. False negatives indicate detection gaps and require rule improvement; false positives require tuning, not remediation.

---

## Question 8

According to the Pyramid of Pain, which category of indicator is the most difficult for an attacker to change after it has been identified and blocked by defenders?

- A) File hash values
- B) IP addresses
- C) Domain names
- D) Tactics, Techniques, and Procedures

Correct Answer: D

Distractor Analysis:

- A is incorrect. Hash values are at the base of the Pyramid of Pain — they are trivially easy for an attacker to change by recompiling or slightly modifying the malicious file.
- B is incorrect. IP addresses are low on the Pyramid of Pain; an attacker can switch to new infrastructure with minimal effort.
- C is incorrect. Domain names require slightly more effort than IPs but can be registered quickly and cheaply, placing them in the middle of the pyramid.
- D is correct. TTPs represent how an adversary thinks and operates. Changing TTPs requires fundamentally altering tradecraft, which is costly and difficult. Blocking at the TTP level maximizes disruption to the attacker.

---

## Question 9

A Tier 1 analyst receives 200 alerts during an 8-hour shift and confirms that 196 of them are false positives. Which operational problem does this most directly indicate?

- A) The organization lacks a threat hunting program
- B) The SIEM correlation rules are too broadly tuned, generating excessive noise
- C) The Tier 1 analysts are not following the correct escalation procedures
- D) The organization needs to deploy additional endpoint detection and response tools

Correct Answer: B

Distractor Analysis:

- A is incorrect. A lack of threat hunting would manifest as high dwell time or missed intrusions, not a high false positive rate.
- B is correct. A 98% false positive rate (196 out of 200) indicates that SIEM correlation rules are over-sensitive — they are matching normal business activity as suspicious. The solution is rule tuning.
- C is incorrect. Escalation procedure failures would affect true positive handling, not the ratio of false to true positives.
- D is incorrect. Additional EDR tools would increase visibility and potentially generate more alerts, but would not address the root cause of poorly tuned correlation rules.

---

## Question 10

A SOC manager reports that the organization's Mean Time to Detect has increased from 4 hours to 72 hours over the past quarter. Which action would most directly address this increase?

- A) Increase the number of Tier 2 analysts to handle incident investigation
- B) Review and update SIEM correlation rules and add threat hunting activities to find threats before they trigger alerts
- C) Implement a change management program to control software updates
- D) Expand the organization's backup and disaster recovery capabilities

Correct Answer: B

Distractor Analysis:

- A is incorrect. Adding Tier 2 analysts improves MTTR (response time) but does not directly address MTTD (detection time), which depends on the quality of detection rules and hunting activities.
- B is correct. High MTTD indicates that threats are entering the environment and remaining undetected for extended periods. Improving detection rules and adding proactive threat hunting directly targets this gap.
- C is incorrect. Change management reduces the risk of misconfigurations and unauthorized changes, but does not improve the speed at which existing threats are detected.
- D is incorrect. Backup and disaster recovery capabilities support Availability and recovery objectives; they do not affect how quickly threats are detected.
