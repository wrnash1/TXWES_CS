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

---

### Question 11 (5 points)

An attacker gains access to a company's web server and modifies the displayed prices in the public product catalog so that high-value items show a price of $0.01. Customers begin placing orders at the fraudulent prices. Which CIA Triad property has been violated, and what technical control would best detect this type of change?

- A) Availability — a load balancer would detect the unauthorized price changes
- B) Integrity — a file integrity monitoring system that alerts on unauthorized changes to application data would detect this
- C) Confidentiality — encryption at rest would prevent attackers from reading and modifying the price database
- D) Non-repudiation — a digital signature on each price record would prevent changes

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Availability refers to system uptime and access continuity. The web server is still functioning and accessible — customers can place orders. The violation is the unauthorized modification of data, which is an integrity issue.
  - Why C is incorrect: Confidentiality controls prevent unauthorized reading of data. Encryption at rest protects data if storage media is stolen but does not prevent an attacker who already has access from modifying the live database.
  - Why D is incorrect: Digital signatures provide non-repudiation by proving who created or approved a record. They can detect tampering but are not typically used on every database price row. File integrity monitoring is the direct, operational answer for detecting unauthorized changes to application data.

---

### Question 12 (5 points)

A security team deploys warning banners on all company computers that state: "Unauthorized use of this system is prohibited and subject to monitoring." Users must click "Agree" before logging in. How should this control be classified?

- A) Technical / Preventive
- B) Physical / Deterrent
- C) Administrative / Directive
- D) Technical / Detective

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: A technical control uses hardware or software mechanisms. A login banner is displayed by software, but its purpose is to communicate a policy and create a legal acknowledgment record — it does not block or technically prevent unauthorized access.
  - Why B is incorrect: Physical controls involve tangible barriers. A software-displayed banner on a screen is not a physical control.
  - Why D is incorrect: A detective control identifies incidents after or as they occur. A login warning banner is displayed before any action — it establishes behavioral expectations and legal acknowledgment, which defines a directive control.

---

### Question 13 (5 points)

A threat intelligence analyst describes a threat actor as follows: "Low technical sophistication, uses publicly available scanning tools and known exploit frameworks, motivated primarily by curiosity and notoriety, and typically attacks without a specific target in mind." Which threat actor type matches this description?

- A) Nation-State Actor
- B) Hacktivist
- C) Organized Crime
- D) Script Kiddie

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: Nation-state actors have advanced technical capabilities, significant financial resources, and pursue strategic geopolitical objectives. They do not rely on publicly available tools and are highly targeted in their operations.
  - Why B is incorrect: Hacktivists are motivated by ideology or political causes and often target specific organizations for public embarrassment. The described actor has no specific ideological motivation and attacks without a target in mind.
  - Why C is incorrect: Organized crime is financially motivated and operates with well-funded criminal networks using sophisticated tools such as ransomware-as-a-service. The description does not fit a financially motivated, sophisticated criminal operation.

---

### Question 14 (5 points)

A network administrator discovers that a developer's test database is publicly accessible via the internet using the vendor's default username and password combination (admin/admin). No data has been stolen yet, but the database contains thousands of customer records. Which vulnerability class does this represent?

- A) Zero-day exploit
- B) Configuration vulnerability — default credentials
- C) Software vulnerability — buffer overflow
- D) Operational vulnerability — missing patch

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A zero-day exploit targets an undiscovered or unpatched software vulnerability. Default credentials are a well-known, documented configuration issue that requires no exploitation of software flaws — the credentials are publicly listed in vendor documentation.
  - Why C is incorrect: A buffer overflow is a memory-level software vulnerability where a program writes past the boundary of a buffer. Default credentials involve no memory corruption.
  - Why D is incorrect: Missing patches describe software that has available security updates not yet applied. The database software itself may be fully patched — the vulnerability is the unchanged default credential configuration, not a software version issue.

---

### Question 15 (5 points)

An organization classifies its data into four levels: Public, Internal, Confidential, and Restricted. Restricted data requires encryption at rest, multi-factor authentication for access, and logging of every access event. Which security principle does this tiered classification system most directly support?

- A) Defense in depth
- B) Non-repudiation
- C) Data classification driving proportional controls
- D) Availability through redundancy

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Defense in depth refers to the use of multiple, layered security controls so no single failure is catastrophic. A data classification scheme itself does not describe layered controls — it describes the assignment of different protection requirements to different data types.
  - Why B is incorrect: Non-repudiation proves that a specific party performed a specific action. Access logging supports non-repudiation for Restricted data, but the purpose of the classification system is broader than establishing non-repudiation.
  - Why D is incorrect: Availability through redundancy involves backup systems, failover, and uptime controls. The classification system described is focused on confidentiality and integrity controls, not availability or redundancy.

---

### Question 16 (5 points)

A security awareness trainer explains to employees that they should never read sensitive documents on a laptop in a crowded airport terminal without a physical privacy screen. Which attack does the privacy screen primarily defend against?

- A) Man-in-the-Middle
- B) Shoulder surfing
- C) Eavesdropping
- D) Replay attack

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A man-in-the-middle attack involves an attacker intercepting and potentially modifying network communications between two parties. A crowded airport visual observation attack does not involve network interception.
  - Why C is incorrect: Eavesdropping in security contexts refers to capturing network traffic — passively intercepting data in transit on a network. Visually observing a screen is not network eavesdropping.
  - Why D is incorrect: A replay attack captures and retransmits authentication tokens. It is a network-level attack and does not involve visual observation of a screen.

---

### Question 17 (5 points)

A company's risk assessment identifies the following: its primary web application is publicly accessible, there is a known unpatched SQL injection vulnerability, and exploitation would expose the personal data of 500,000 customers. No attack has occurred yet. Using formal risk vocabulary, which statement correctly applies all three concepts?

- A) The SQL injection flaw is a threat; the attacker is a vulnerability; the exposed customers represent risk
- B) The unpatched SQL injection flaw is a vulnerability; an attacker who exploits web applications is a threat; the potential harm to customers represents risk
- C) The exposed customer data is a vulnerability; the SQL injection flaw is a threat; the attacker represents risk
- D) The SQL injection flaw is both a threat and a vulnerability because it can be exploited by any actor

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This inverts the definitions. A vulnerability is the weakness (the SQL injection flaw), not the attacker. An attacker is a threat actor.
  - Why C is incorrect: The exposed customer data is an asset at risk, not a vulnerability. A vulnerability is a weakness in a system or control.
  - Why D is incorrect: A single condition cannot be both a threat and a vulnerability. A vulnerability is a weakness that can be exploited; a threat is an actor or event that could exploit that weakness.

---

### Question 18 (5 points)

A SIEM alert fires when a user account successfully authenticates from New York at 8:00 AM and then successfully authenticates from Tokyo at 8:47 AM the same morning. The SIEM correlation rule that triggered the alert is based on geographic impossibility. Which type of IOC does this represent?

- A) Host IOC — a new process was launched on the user's workstation
- B) Network IOC — traffic was observed on a non-standard port
- C) Account IOC — a login occurred from a location that is geographically impossible given prior activity
- D) File IOC — a known malicious file hash was detected on the system

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: A host IOC involves file system, registry, or process anomalies on a specific endpoint. The alert describes an authentication event tied to geographic location, not a host-side artifact.
  - Why B is incorrect: A network IOC involves suspicious traffic patterns, IP addresses, or port usage. An authentication event with an impossible travel pattern is an account-based IOC, not a network IOC — it involves identity, not network traffic characteristics.
  - Why D is incorrect: A file IOC involves matching a file hash or filename against known malicious indicators. No file activity is described in this scenario.

---

### Question 19 (5 points)

An organization's IT policy requires all employees to use unique, complex passwords and prohibits password reuse for the last 12 passwords. An employee who has used the same password for five years finally changes it to comply with the policy. Security researchers have recently found this five-year-old password in a publicly leaked credential database. Which threat does the policy change primarily address?

- A) Zero-day exploit using the password as an attack vector
- B) Credential stuffing using the leaked password against other accounts
- C) Brute-force attack guessing all possible character combinations
- D) SQL injection using the password field as the injection point

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A zero-day exploit targets an undiscovered software vulnerability. Passwords are credentials, not software vulnerabilities. An exposed password is not a zero-day.
  - Why C is incorrect: Brute-force attacks try all possible combinations and do not rely on a leaked password database. The scenario specifically describes a leaked credential — credential stuffing is the attack that uses known leaked credentials.
  - Why D is incorrect: SQL injection inserts malicious SQL syntax into input fields. A password field can be a vector for injection attacks, but the threat described — using a known leaked password — is credential stuffing, not injection.

---

### Question 20 (5 points)

A financial institution sends all security events to a centralized SIEM. A threat intelligence team uses the SIEM data alongside subscriptions to commercial threat intelligence feeds and government advisories from CISA to identify threats specific to the financial sector. Which threat intelligence source type do the CISA advisories represent?

- A) OSINT (Open-Source Intelligence)
- B) Dark web monitoring
- C) Internal telemetry
- D) Government / authoritative advisory

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: OSINT is intelligence gathered from publicly available, non-governmental internet sources including news, social media, and research publications. CISA advisories are official government publications from a federal cybersecurity agency — they represent authoritative government intelligence, not generic open-source intelligence.
  - Why B is incorrect: Dark web monitoring involves analyzing criminal forums and underground marketplaces for stolen data or planned attacks. CISA advisories are published on the open internet by a US government agency and have no connection to dark web sources.
  - Why C is incorrect: Internal telemetry refers to SIEM data, firewall logs, and EDR alerts generated within the organization's own environment. CISA advisories are an external intelligence source, not internally generated data.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 01 Quiz

Proprietary and Confidential. Not for disclosure outside of authorized course use.
