# Quiz — Module 01: Threats, Attacks, and Vulnerabilities

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | 10 Questions | 100 Points

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is open-note but must reflect your own work. Questions are written to match the difficulty and style of the CompTIA Security+ SY0-701 exam.

---

## Question 1

An organization implements an automated system that checks the hash of system files every hour. If a hash mismatch is detected, an alert is sent to the security operations center. Which pillar of the CIA triad is this control primarily enforcing?

A) Confidentiality

B) Integrity

C) Availability

D) Non-repudiation

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Confidentiality is maintained by encryption and access controls that restrict who can read data. Hashing does not conceal data from unauthorized parties — it detects whether data has been altered.
- Why C is incorrect: Availability ensures systems remain accessible through redundancy and backups. Hashing does not address system uptime or access continuity.
- Why D is incorrect: Non-repudiation proves who performed an action and is enforced by digital signatures. Hashing only proves whether a file was altered, not who altered it.

---

## Question 2

A security analyst reviews a report listing four threat actors involved in separate incidents. Which of the following actors represents the HIGHEST level of sophistication, available resources, and long-term persistence?

A) Script Kiddie

B) Hacktivist

C) Nation-State Actor

D) Insider Threat

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Script kiddies have low technical skill and rely on pre-built tools. They launch opportunistic, short-duration attacks rather than sustained strategic campaigns.
- Why B is incorrect: Hacktivists are motivated by ideology and may have moderate technical ability, but they lack the state-level funding and infrastructure that enables advanced persistent threats.
- Why D is incorrect: Insider threats are dangerous because of their authorized access, but they do not inherently possess nation-state-level resources or advanced persistent threat capabilities.

---

## Question 3

An attacker exploits a vulnerability in a web application that the vendor has not yet discovered or patched. Which type of attack does this describe?

A) Replay attack

B) Zero-day exploit

C) SQL injection

D) Pass-the-hash attack

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A replay attack intercepts and retransmits valid authentication tokens to gain unauthorized access. It targets known protocol weaknesses, not undiscovered vulnerabilities.
- Why C is incorrect: SQL injection is a well-known, documented attack class against web applications. It is not a zero-day because defenders can apply input validation and parameterized queries as documented mitigations.
- Why D is incorrect: Pass-the-hash captures hashed credentials from memory and reuses them without cracking. It exploits known Windows authentication weaknesses, not an undiscovered vulnerability.

---

## Question 4

A company requires all employees to sign an Acceptable Use Policy before being granted network access. How should this security control be classified?

A) Physical / Corrective

B) Logical / Detective

C) Administrative / Preventive

D) Technical / Compensating

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: An Acceptable Use Policy is a written document, not a physical barrier such as a lock or fence. It aims to prevent violations by setting behavioral expectations before bad behavior occurs, not to correct harm after the fact.
- Why B is incorrect: Logical (Technical) controls use software or hardware mechanisms to enforce rules automatically. An AUP is a human-process control. Detective controls identify incidents after they occur, not before.
- Why D is incorrect: Technical controls include firewalls, encryption, and access control lists. A compensating control substitutes for a primary control when the primary cannot be implemented. An AUP is a standard preventive administrative control.

---

## Question 5

When designing a security architecture, you need to prevent attackers from deleting local system event logs after a breach to cover their tracks. Which of the following controls best mitigates this risk?

A) Forward all system logs to a remote, write-protected SIEM platform in real time.

B) Enforce full disk encryption on all endpoints to prevent unauthorized file deletion.

C) Require multi-factor authentication for all administrative console logins.

D) Deploy a host-based intrusion detection system on every endpoint.

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct: Centralizing logs on a remote, write-once SIEM means that even if an attacker gains local admin access and wipes local logs, the offsite copies remain intact and available for forensic investigation.
- Why B is incorrect: Full disk encryption protects data confidentiality at rest. It does not prevent a logged-in attacker with admin privileges from deleting files, including log files.
- Why C is incorrect: MFA hardens the authentication step but does not address the threat of log deletion after an attacker has already gained access through a compromised account.
- Why D is incorrect: A HIDS can detect suspicious file activity, but it does not prevent log deletion the way remote log forwarding does. If the attacker disables the HIDS first, the local logs are still gone.

---

## Question 6

A penetration tester connects to a coffee shop wireless network and uses a tool to silently capture all traffic flowing between other patrons and the access point. The tester does not modify any packets or inject any data. Which attack category best describes this activity?

A) Man-in-the-Middle

B) Replay attack

C) Eavesdropping

D) Injection

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A man-in-the-middle attack requires the attacker to position themselves in the communication path and intercept traffic between two specific parties. Passive packet capture without injection or interception is not a MITM attack.
- Why B is incorrect: A replay attack requires the attacker to capture a specific valid token or packet and retransmit it to impersonate a legitimate session. No retransmission occurs here.
- Why D is incorrect: Injection attacks insert malicious data into a data stream or input field. The tester is only observing traffic without modifying or injecting anything.

---

## Question 7

An organization's risk assessment identifies an unpatched operating system vulnerability (CVE-2023-XXXX) on a critical server. The security team cannot apply the patch because the server runs a legacy application that is not compatible with the updated OS version. The team decides to place the server in an isolated network segment with strict firewall rules. What type of control is the network segmentation in this context?

A) Corrective / Technical

B) Preventive / Administrative

C) Compensating / Technical

D) Detective / Physical

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: A corrective control restores a system to a secure state after an incident has already occurred. Network segmentation is applied proactively before exploitation occurs.
- Why B is incorrect: Network segmentation uses routing and firewall rules — software and hardware mechanisms — making it a Technical control, not Administrative.
- Why D is incorrect: A detective control identifies attacks that are in progress or have occurred. Network segmentation actively blocks attack paths, making it Preventive, not Detective.

---

## Question 8

A threat actor sends thousands of automated login requests to a cloud-based application using username and password pairs obtained from a publicly leaked credential database belonging to a different company. The attacker assumes that many users reuse passwords across services. What attack technique is this?

A) Brute force

B) Credential stuffing

C) Password spraying

D) Rainbow table attack

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Brute force systematically tries all possible character combinations for a given username. Credential stuffing uses known username/password pairs from previous breaches — it does not try all combinations.
- Why C is incorrect: Password spraying tries a single common password against many different accounts to avoid lockout thresholds. Credential stuffing uses specific credential pairs from a leak, not a single common password.
- Why D is incorrect: A rainbow table attack uses precomputed hash chains to reverse password hashes offline. It requires access to a stolen password hash database, not live login attempts against a cloud application.

---

## Question 9

During a threat hunt, an analyst finds that a standard user account on a file server has been granted Domain Admin privileges. The change was made at 11:47 PM on a Saturday. No IT change ticket exists for this modification. Which type of Indicator of Compromise does this represent, and what is the most likely explanation?

A) Network IOC — the account was accessed from an unusual IP address.

B) Account-based IOC — the attacker created or elevated a privileged account to maintain persistence.

C) Host-based IOC — a new service was installed on the server that requires elevated privileges.

D) Log-based IOC — the security event log was cleared to hide the privilege escalation.

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The finding is about unauthorized privilege escalation, not about the geographic or network location of the access. An unusual IP address would be a network IOC — this finding is account-based.
- Why C is incorrect: The finding describes account privilege modification, not service installation. A new service would be a host-based IOC, but the scenario specifically describes an account change.
- Why D is incorrect: The scenario states that the change was found in the logs, which means the logs were not cleared. Log clearing would be a separate, additional IOC if it had occurred.

---

## Question 10

An organization is building a new security awareness program. The CISO wants to ensure employees understand that receiving an email that appears to come from the CEO asking for an immediate wire transfer is a known attack technique, even if the email address looks legitimate. Which threat actor type most commonly uses this technique, and what is the correct term for this specific attack?

A) Script Kiddie — phishing

B) Nation-State Actor — spear phishing

C) Organized Crime — business email compromise (BEC)

D) Hacktivist — whaling

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Script kiddies use automated, opportunistic tools. Crafting targeted financial fraud emails impersonating executives requires deliberate social engineering effort. Phishing is generic; this scenario is targeted.
- Why B is incorrect: While nation-state actors do use spear phishing, the specific technique of impersonating executives to request wire transfers is the defining characteristic of business email compromise, which is financially motivated and strongly associated with organized crime.
- Why D is incorrect: Whaling is a type of phishing that targets high-value individuals (executives — the "big fish"). In this scenario the CEO is the impersonated party, not the target. The employees are the targets. This is BEC, not whaling.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 01 Quiz

Proprietary and Confidential. Not for disclosure outside of authorized course use.
