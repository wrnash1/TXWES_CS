# Quiz: Module 01 - Threats, Attacks, and Vulnerabilities
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
An organization implements an automated system that checks the hash of system files every hour. If a hash mismatch is detected, an alert is sent to the security operations center. Which pillar of the CIA triad is this control primarily enforcing?
A) Confidentiality
B) Integrity
C) Availability
D) Non-repudiation
*   **Correct Answer:** B) Integrity
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Confidentiality is maintained by encryption and access controls that hide data from unauthorized parties — hashing does not conceal data, it verifies whether data has changed.
    *   *Why C is incorrect:* Availability ensures systems remain accessible through redundancy and backups; it does not address unauthorized file modification.
    *   *Why D is incorrect:* Non-repudiation proves who performed an action using digital signatures — hashing only proves whether a file was altered, not who altered it.

---

---

**Question 2**
A security analyst reviews a report listing four threat actors. Which of the following actors represents the HIGHEST level of sophistication, resources, and long-term persistence?
A) Script Kiddie
B) Hacktivist
C) Nation-State Actor
D) Insider Threat
*   **Correct Answer:** C) Nation-State Actor
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Script kiddies have low technical skill and rely on pre-built tools; they typically launch opportunistic, short-duration attacks rather than sustained campaigns.
    *   *Why B is incorrect:* Hacktivists are motivated by ideology or political agendas and may have moderate technical ability, but they lack the state-level funding and infrastructure of nation-state actors.
    *   *Why D is incorrect:* Insider threats are dangerous because of their authorized access, but they do not inherently possess nation-state-level resources or advanced persistent threat (APT) capabilities.

---

---

**Question 3**
An attacker exploits a vulnerability in a web application that the vendor has not yet discovered or patched. Which type of attack does this describe?
A) Replay attack
B) Zero-day exploit
C) SQL injection
D) Pass-the-hash attack
*   **Correct Answer:** B) Zero-day exploit
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A replay attack intercepts and retransmits valid authentication tokens to gain unauthorized access — it targets known protocol weaknesses, not undiscovered vulnerabilities.
    *   *Why C is incorrect:* SQL injection is a well-known, documented attack class against web applications; it is not a zero-day because defenders can apply input validation and parameterized queries as known mitigations.
    *   *Why D is incorrect:* Pass-the-hash captures hashed credentials from memory and reuses them without cracking — it exploits known Windows authentication weaknesses, not an undiscovered vulnerability.

---

**Question 4**
A company requires all employees to sign an Acceptable Use Policy (AUP) before being granted network access. How should this security control be classified?
A) Physical / Corrective
B) Logical / Detective
C) Administrative / Preventive
D) Technical / Compensating
*   **Correct Answer:** C) Administrative / Preventive
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An AUP is a written policy document (Administrative), not a physical barrier such as a lock or fence. It aims to prevent violations by setting expectations before bad behavior occurs (Preventive), not to correct harm after the fact.
    *   *Why B is incorrect:* Logical (Technical) controls use software or hardware mechanisms to enforce rules automatically; an AUP is a human-process control, not an automated enforcement mechanism. Detective controls identify incidents after they occur.
    *   *Why D is incorrect:* Technical controls include firewalls, encryption, and access control lists. A compensating control substitutes for a primary control when the primary cannot be implemented — an AUP is a standard preventive administrative control, not a compensating one.

---

**Question 5**
When designing a security architecture, you need to prevent attackers from deleting local system event logs after a breach to hide their tracks. Which of the following controls best mitigates this risk?
A) Forward all system logs to a remote, write-protected SIEM platform in real time.
B) Enforce full disk encryption on all endpoints to prevent unauthorized file deletion.
C) Require multi-factor authentication for all administrative console logins.
D) Deploy a host-based intrusion detection system (HIDS) on every endpoint.
*   **Correct Answer:** A) Forward all system logs to a remote, write-protected SIEM platform in real time.
*   **Distractor Analysis:**
    *   *Why A is correct:* Centralizing logs on a remote, write-once SIEM means that even if an attacker gains local admin access and wipes local logs, the offsite copies remain intact and admissible for forensic investigation.
    *   *Why B is incorrect:* Full disk encryption protects data confidentiality at rest — it does not prevent a logged-in attacker with admin privileges from deleting files, including log files.
    *   *Why C is incorrect:* MFA hardens the authentication step but does not address the threat of log deletion after an attacker has already gained access through a compromised account.
    *   *Why D is incorrect:* A HIDS can detect suspicious file activity, but it does not prevent log deletion the way remote log forwarding does; if the attacker disables the HIDS first, the logs are still gone.
