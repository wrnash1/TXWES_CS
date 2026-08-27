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

---

## Question 11 (5 points)

A SOC analyst reviewing logs notices that a service account authenticated successfully to a database server at 3:14 AM on a Saturday — outside its documented operating window. Which of the following actions best follows the principle of verifying before acting?

- A) Immediately disable the service account to prevent further unauthorized access
- B) Correlate the login with scheduled job records, change management logs, and the account's documented operating window before taking action
- C) Reimage the database server to eliminate any potential persistence mechanisms
- D) File an incident report and wait for Tier 3 to investigate before doing anything

Correct Answer: B

Distractor Analysis:

- A is incorrect. Disabling a service account without verification could break an authorized maintenance job running outside business hours, causing an outage. Verification must precede containment.
- B is correct. Cross-referencing the activity against change management records and the account's documented schedule is proper triage — it determines whether this is authorized activity or a true compromise before any action is taken.
- C is incorrect. Reimaging is a remediation step that requires confirmed compromise and management authorization. Performing it prematurely destroys forensic evidence and disrupts operations.
- D is incorrect. A Tier 1 analyst is expected to triage actively, not passively wait. Waiting without performing triage violates the SOC's detection and response mission.

---

## Question 12 (5 points)

Which of the following most accurately describes the difference between a SOC and a CERT (Computer Emergency Response Team)?

- A) A SOC focuses on reactive incident response after a breach; a CERT focuses on continuous monitoring
- B) A SOC performs continuous 24/7 monitoring and triage; a CERT is typically activated to coordinate response to declared cyber incidents or emergencies
- C) A SOC manages firewall and IPS rules; a CERT manages endpoint detection and response tools
- D) A SOC is a government entity; a CERT is always a private sector function

Correct Answer: B

Distractor Analysis:

- A is incorrect. This reverses the functions. The SOC monitors continuously and often handles both detection and initial response. CERTs are not passive monitoring entities.
- B is correct. The SOC is the ongoing operational security capability running 24/7. A CERT or CSIRT is typically a designated team — sometimes overlapping with SOC personnel — that manages formal incident coordination, communication, and recovery during a declared incident.
- C is incorrect. Neither the SOC nor a CERT is defined by ownership of specific tools like firewalls or EDR. Both use multiple tools across their functions.
- D is incorrect. Both SOCs and CERTs exist in government and private sector organizations. The distinction is functional, not organizational ownership.

---

## Question 13 (5 points)

An analyst discovers that an internal host has made DNS queries to a domain registered 48 hours ago that shares a naming pattern with known command-and-control infrastructure. The host has no associated SIEM alerts. What type of SOC activity does investigating this represent?

- A) Alert triage
- B) Vulnerability management
- C) Threat hunting
- D) Incident management

Correct Answer: C

Distractor Analysis:

- A is incorrect. Alert triage is the process of evaluating alerts the SIEM has already generated. No SIEM alert exists in this scenario — the analyst identified the suspicious activity proactively.
- B is incorrect. Vulnerability management involves identifying and remediating software weaknesses, not investigating suspicious network communication patterns.
- C is correct. Threat hunting is the proactive search for threats that have not yet triggered automated alerts. Investigating suspicious DNS queries without a preceding SIEM alert is a textbook threat hunting activity.
- D is incorrect. Incident management begins after an event has been classified as an incident. This activity is still in the hypothesis-investigation phase.

---

## Question 14 (5 points)

A SOC analyst receives a phishing email report from a user. The email contains a link. The analyst pastes the URL into a threat intelligence lookup platform and finds it is classified as malicious. What type of IOC is this URL?

- A) Network-based IOC
- B) Host-based IOC
- C) Behavioral IOC
- D) Email-based IOC

Correct Answer: A

Distractor Analysis:

- A is correct. URLs, domain names, and IP addresses are network-based IOCs because they describe malicious network infrastructure — not activity on a specific host or a behavioral pattern over time.
- B is incorrect. Host-based IOCs describe artifacts found on a compromised system such as registry keys, scheduled tasks, or file paths — not network addresses or links.
- C is incorrect. Behavioral IOCs describe patterns of activity over time such as beaconing at regular intervals. A single URL is not a behavioral pattern.
- D is incorrect. Email-based IOCs describe characteristics of malicious email messages themselves — sender address, subject line, attachment hash. Once extracted from the email, the URL is classified as a network-based indicator.

---

## Question 15 (5 points)

An organization's SOC manager wants to measure how effective the team is at containing confirmed incidents. Which metric most directly measures this capability?

- A) Mean Time to Detect (MTTD)
- B) False Positive Rate
- C) Mean Time to Respond (MTTR)
- D) Alert Volume

Correct Answer: C

Distractor Analysis:

- A is incorrect. MTTD measures detection speed — how quickly a threat is identified from the time of intrusion. It does not measure containment capability.
- B is incorrect. False Positive Rate measures detection accuracy (alert noise), not containment speed or effectiveness after confirmation.
- C is correct. MTTR (Mean Time to Respond) measures the average time from alert confirmation to containment or remediation. A high MTTR indicates that confirmed incidents are not being contained quickly enough.
- D is incorrect. Alert Volume measures how many alerts are generated per period, not how effectively the team handles them after confirmation.

---

## Question 16 (5 points)

During an investigation, an analyst finds that an attacker used a legitimate Windows administration tool — PsExec — to move laterally across the network instead of deploying custom malware. This technique is most commonly described as what?

- A) Fileless malware execution
- B) Living off the land (LotL)
- C) Zero-day exploitation
- D) Privilege escalation

Correct Answer: B

Distractor Analysis:

- A is incorrect. Fileless malware refers to malicious code that executes in memory without writing files to disk. While PsExec-based lateral movement may leave few artifacts, the defining characteristic here is abuse of a legitimate system tool — not memory-only execution.
- B is correct. Living off the land (LotL) describes adversaries who use legitimate, pre-installed tools and system utilities to carry out malicious actions. This makes detection harder because the activity blends with normal administrative operations.
- C is incorrect. A zero-day is an unpatched software vulnerability. Using PsExec does not exploit a vulnerability — it abuses a legitimate administrative function.
- D is incorrect. Privilege escalation describes gaining elevated permissions. Lateral movement describes moving to additional systems. These are distinct phases of the attack lifecycle.

---

## Question 17 (5 points)

A SIEM correlation rule fires when more than 10 authentication failures occur for the same username within 5 minutes. An attacker performs only 3 failed attempts every 10 minutes across multiple different usernames. What does this attacker technique illustrate?

- A) SQL injection
- B) Credential stuffing with threshold evasion
- C) Pass-the-hash attack
- D) Kerberoasting

Correct Answer: B

Distractor Analysis:

- A is incorrect. SQL injection exploits vulnerable database query inputs to execute unauthorized commands. It has no relationship to authentication attempt thresholds or credential testing.
- B is correct. The attacker is conducting credential stuffing (testing many username/password combinations) while deliberately staying below the per-account, per-time-window detection threshold. This threshold evasion behavior requires cross-account and velocity-based correlation rules to detect.
- C is incorrect. Pass-the-hash uses captured NTLM credential hashes to authenticate without knowing the plaintext password. It does not involve repeated authentication failures.
- D is incorrect. Kerberoasting targets Kerberos service tickets to crack service account passwords offline. It generates different artifacts and does not involve repeated failed logins.

---

## Question 18 (5 points)

In the Cyber Kill Chain model, which phase occurs immediately before the attacker installs malware on the victim's system?

- A) Reconnaissance
- B) Weaponization
- C) Delivery
- D) Command and Control

Correct Answer: C

Distractor Analysis:

- A is incorrect. Reconnaissance is the first phase — the attacker researches the target. It occurs several phases before installation.
- B is incorrect. Weaponization is the second phase — the attacker pairs an exploit with a payload. It precedes delivery, not installation.
- C is correct. The Cyber Kill Chain sequence is: Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives. Delivery (transmitting the weaponized payload to the victim) immediately precedes the installation phase.
- D is incorrect. Command and Control occurs after installation. Once the malware is installed, it establishes a communication channel back to the attacker's infrastructure.

---

## Question 19 (5 points)

An analyst is documenting an incident that may be used in a legal proceeding. Which documentation practice is most critical in this context?

- A) Use informal shorthand and abbreviations to document findings quickly before memory fades
- B) Maintain a timestamped, detailed chain of custody and write findings in clear, unambiguous language
- C) Document only the final determination — whether it was a true positive or false positive
- D) Provide a verbal summary to the Tier 2 analyst and have them create the formal documentation

Correct Answer: B

Distractor Analysis:

- A is incorrect. Informal shorthand may be misinterpreted in legal proceedings. Documentation intended for potential legal use must be clear, precise, and follow accepted evidence handling standards.
- B is correct. Legal proceedings require a clear chain of custody documenting who collected each piece of evidence, when, and how it was preserved. Timestamped, detailed, unambiguous documentation is the professional and legally defensible standard for incident records.
- C is incorrect. Documenting only the final determination eliminates the evidentiary trail. Courts and investigators need to see how the conclusion was reached, not just what the conclusion was.
- D is incorrect. Verbal handoffs are not a substitute for written documentation. The analyst who performed triage is responsible for their own documented findings regardless of escalation.

---

## Question 20 (5 points)

Which scenario best demonstrates a violation of the Integrity pillar of the CIA Triad?

- A) A ransomware attack encrypts all files on a file server, making them inaccessible to staff for three days
- B) An attacker exfiltrates a database of customer credit card numbers to an external server
- C) A malicious insider modifies financial transaction records to redirect funds to an unauthorized account
- D) A DDoS attack floods a public-facing web server with traffic, causing it to become unresponsive

Correct Answer: C

Distractor Analysis:

- A is incorrect. Encrypting files and making them inaccessible is an Availability violation — authorized users cannot reach data they are entitled to access.
- B is incorrect. Exfiltrating data is a Confidentiality violation — unauthorized parties gain access to information they should not see.
- C is correct. Modifying financial records without authorization is an Integrity violation — the data was changed in an unauthorized way and no longer accurately reflects reality. Unauthorized modification is the defining characteristic of an Integrity attack.
- D is incorrect. Flooding a server to make it unresponsive is an Availability violation — legitimate users are prevented from accessing the service they depend on.
