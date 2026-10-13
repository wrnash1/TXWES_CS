# Quiz: Module 16 — Security+ SY0-701 Exam Preparation and Capstone

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

Instructions: Select the single best answer for each question. All ten questions use the scenario-based format of the actual SY0-701 exam. Full distractor analysis is provided after each question.

---

---

**Question 1**
A penetration tester discovers that a web application constructs SQL queries by directly concatenating user input into the query string. By entering the value `' OR '1'='1` into the login field, the tester is able to bypass authentication and access all user accounts in the database. The development team asks the tester to recommend the single most effective remediation. Which control should the tester recommend?
A) Deploy a web application firewall (WAF) to detect and block SQL injection payloads at the network perimeter.
B) Rewrite all database queries to use parameterized queries (prepared statements) so that user input is never interpreted as SQL code.
C) Encrypt the database contents at rest using AES-256 so that stolen data cannot be read.
D) Require all users to authenticate with MFA before accessing the application.
*   **Correct Answer:** B) Rewrite all database queries to use parameterized queries (prepared statements) so that user input is never interpreted as SQL code.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A WAF provides a valuable defense-in-depth layer by filtering known attack patterns, but it does not fix the root cause — the application still constructs queries insecurely. A sufficiently obfuscated payload or novel variant can bypass WAF signatures. Parameterized queries eliminate the vulnerability at its source.
    *   *Why C is incorrect:* Encryption at rest protects data confidentiality if storage media is physically stolen or compromised, but it does not prevent an attacker from extracting data through a live SQL injection attack — the database decrypts data for legitimate (and injected) queries transparently.
    *   *Why D is incorrect:* MFA strengthens authentication but does not prevent SQL injection — the tester bypassed the login logic entirely by manipulating the SQL query, not by stealing credentials. An attacker can exploit SQLi before any authentication occurs.

---

---

**Question 2**
A CISO reviews a security incident report and notes the following timeline: Day 1 — security analysts deployed honeypots and updated incident response playbooks. Day 3 — SIEM alerts triggered on anomalous outbound traffic from a finance workstation. Day 4 — the workstation was isolated from the network. Day 6 — malware was removed and the OS was reimaged. Day 7 — the workstation was returned to service. Day 10 — the team held a meeting to document lessons learned and identify three new detection rules. Which NIST IR phase occurred on Day 10?
A) Preparation
B) Detection and Analysis
C) Containment, Eradication, and Recovery
D) Post-Incident Activity
*   **Correct Answer:** D) Post-Incident Activity
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Preparation (Day 1 — deploying honeypots and updating playbooks) occurred before the incident was detected. The Day 10 activity occurs after the incident is fully resolved, which is characteristic of Post-Incident Activity, not Preparation.
    *   *Why B is incorrect:* Detection and Analysis (Day 3 — SIEM alert on anomalous traffic) was the phase where analysts confirmed the incident. The Day 10 retrospective meeting occurs after all four active response phases are complete.
    *   *Why C is incorrect:* Containment (Day 4 — isolation), Eradication (Day 6 — malware removal and reimaging), and Recovery (Day 7 — return to service) were all completed before Day 10. The lessons-learned meeting is the defining activity of the Post-Incident Activity phase.

---

---

**Question 3**
An organization stores customer records containing names, Social Security Numbers, dates of birth, and credit card numbers in a cloud-based database. A security assessment identifies that the database is accessible via a publicly routable IP address with no firewall restrictions, the data is stored in plaintext, and access logs show three login attempts from foreign IP addresses last month. The security team must prioritize remediation. Which action addresses the MOST critical vulnerability first?
A) Implement IP allowlisting and a firewall rule restricting database access to the application servers only.
B) Encrypt the database at rest using AES-256 to protect the stored PII and financial data.
C) Enable multi-factor authentication on the database administrator accounts.
D) Review and investigate the three foreign login attempts to determine if a breach occurred.
*   **Correct Answer:** A) Implement IP allowlisting and a firewall rule restricting database access to the application servers only.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Encrypting data at rest is an important control, but if the database remains publicly accessible without authentication restrictions, an attacker can still query unencrypted data through the open connection before encryption is implemented. Closing the exposure surface is the higher-priority action.
    *   *Why C is incorrect:* MFA on admin accounts improves authentication strength but does not address the immediate risk of the database being reachable by anyone on the internet. An attacker does not need admin credentials to exploit a publicly accessible database with no network restrictions.
    *   *Why D is incorrect:* Investigating past login attempts is an important detective action, but it is reactive — the database remains publicly exposed and vulnerable to new attacks during the investigation. Closing the network exposure eliminates the ongoing risk while investigation proceeds.

---

**Question 4**
A company's legal team is reviewing contracts with a new SaaS vendor that will process employee payroll data including Social Security Numbers, bank account details, and salary information. The legal team asks the security team which compliance obligations are triggered and what contractual security requirements must be included. Which of the following responses correctly identifies the applicable obligation?
A) The company must comply with PCI-DSS because payroll data includes bank account numbers, which are financial data equivalent to cardholder data.
B) The company must include contractual data processing requirements and right-to-audit clauses, and the vendor must demonstrate adequate security controls for the PII being processed.
C) The company has no compliance obligations because SaaS vendors assume full responsibility for data security under the shared responsibility model.
D) The company must comply with HIPAA because employee benefit data may include health insurance information.
*   **Correct Answer:** B) The company must include contractual data processing requirements and right-to-audit clauses, and the vendor must demonstrate adequate security controls for the PII being processed.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* PCI-DSS applies specifically to payment card data (credit and debit card numbers, CVVs, PINs) — it does not apply to employee bank account numbers used for payroll direct deposit. Payroll bank account data is PII governed by general data protection principles, not PCI-DSS.
    *   *Why C is incorrect:* The shared responsibility model never transfers full security responsibility to the SaaS vendor — the customer always retains responsibility for data classification, access control configuration, and ensuring the vendor meets contractual security requirements. Outsourcing processing does not outsource compliance accountability.
    *   *Why D is incorrect:* HIPAA applies to protected health information (PHI) held by covered entities (healthcare providers and insurers) and their business associates — it does not apply to general employee PII such as SSNs, bank accounts, and salaries processed by a payroll system unless the data explicitly contains medical records or health insurance claims data.

---

**Question 5**
A security architect is designing the authentication system for a new enterprise application that will be used by 5,000 employees. The requirements state: employees must not need to remember separate credentials for this application; the system must use the existing Active Directory identity store; authentication must be phishing-resistant; and access must be revocable immediately when an employee leaves the organization. Which combination of controls best meets all four requirements?
A) Local application username and password with complexity requirements and a 90-day rotation policy.
B) SAML 2.0 SSO federated to Active Directory as the identity provider, combined with hardware security key (FIDO2) MFA.
C) Shared department passwords stored in a team password manager, with IP-based access restrictions.
D) OAuth 2.0 authorization with SMS-based OTP as the second factor and monthly access reviews.
*   **Correct Answer:** B) SAML 2.0 SSO federated to Active Directory as the identity provider, combined with hardware security key (FIDO2) MFA.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Separate application credentials with a 90-day rotation policy violates the "no separate credentials" requirement and does not federate to Active Directory — deprovisioning requires manual action in the application rather than an immediate AD account disable. Password-based authentication is also phishable.
    *   *Why C is incorrect:* Shared department passwords violate least privilege and make individual accountability impossible — there is no way to immediately revoke a departing employee's access without changing the shared password for the entire department. IP restrictions are security through obscurity, not authentication.
    *   *Why D is incorrect:* OAuth 2.0 is an authorization framework, not an authentication federation protocol — it does not fulfill the requirement of federating authentication to Active Directory as the single identity source. SMS-based OTP is also not phishing-resistant (it is vulnerable to SIM swapping and real-time phishing relay attacks), failing the phishing-resistant requirement.

---

**Question 6 (5 points)**
A digital forensics examiner responds to a workstation suspected of being used to exfiltrate sensitive data. The examiner must collect evidence in the correct order of volatility. Which sequence correctly lists these sources from MOST volatile to LEAST volatile: (1) Hard drive image, (2) CPU registers and cache, (3) Network connections, (4) Running processes, (5) Swap file / pagefile?
A) 2 → 4 → 3 → 5 → 1
B) 1 → 5 → 3 → 4 → 2
C) 3 → 2 → 4 → 5 → 1
D) 4 → 3 → 2 → 1 → 5
*   **Correct Answer:** A) 2 → 4 → 3 → 5 → 1
*   **Distractor Analysis:**
    *   *Why B is incorrect:* This order reverses the volatility hierarchy. The hard drive is the least volatile source and should be collected last. CPU registers and cache are the most volatile and disappear the instant power is lost — they must be collected first.
    *   *Why C is incorrect:* Network connections are volatile but less volatile than CPU registers and active process memory. The examiner must capture CPU/register state and running process memory before capturing network connection tables, which persist slightly longer in OS data structures.
    *   *Why D is incorrect:* Running processes are more volatile than network connections in the standard order of volatility (RFC 3227). Process memory includes loaded DLLs and injected code that can be modified or cleared before network connection entries are updated.

---

**Question 7 (5 points)**
A threat intelligence analyst reviews a SIEM alert: an internal HR application server is making a 47-minute outbound connection on port 4444 to 198.51.100.15, a known APT command-and-control IP, transferring 2.3 MB of data. What MITRE ATT&CK tactic is most consistent with this observed behavior?
A) Initial Access (TA0001) — the attacker is first establishing a foothold
B) Command and Control (TA0011) — the internal host is communicating with known C2 infrastructure
C) Exfiltration (TA0010) — data is being stolen from the HR application server
D) Discovery (TA0007) — the attacker is mapping the internal network
*   **Correct Answer:** B) Command and Control (TA0011) — the internal host is communicating with known C2 infrastructure
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Initial Access describes gaining an entry point into the network. A 47-minute outbound connection from an internal server to known C2 infrastructure indicates an already-established compromise — initial access has already occurred.
    *   *Why C is incorrect:* An outbound connection to a known C2 IP on port 4444 is the defining signature of Command and Control. Exfiltration would typically involve large data transfers to cloud storage, FTP servers, or email destinations, not a persistent callback channel.
    *   *Why D is incorrect:* Discovery techniques involve internal reconnaissance — querying Active Directory, running network scans, enumerating shares. An outbound connection to an external C2 IP is not a discovery technique.

---

**Question 8 (5 points)**
An organization uses AES-256 to encrypt sensitive files at rest and needs to securely transmit the AES key to external partners. Which approach correctly solves the symmetric key distribution problem?
A) Email the AES-256 key to the recipient in a separate message from the encrypted file.
B) Encrypt the AES-256 key with the recipient's RSA public key and transmit the encrypted key alongside the encrypted file.
C) Use a shared password that both parties already know to derive the AES key using a KDF.
D) Hash the AES-256 key with SHA-256 and send the hash to the recipient for decryption.
*   **Correct Answer:** B) Encrypt the AES-256 key with the recipient's RSA public key and transmit the encrypted key alongside the encrypted file.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Emailing the AES key in plaintext exposes it to interception. If an attacker captures both the encrypted file and the plaintext key, decryption is trivial — this creates two attack surfaces instead of solving the problem.
    *   *Why C is incorrect:* Using a pre-shared password with a KDF requires the parties to have already securely exchanged the password, which recreates the same key distribution problem. This approach is only valid when parties share a secret through an out-of-band channel, which is not described.
    *   *Why D is incorrect:* SHA-256 is a one-way hash function — hashing the key produces a digest the recipient cannot use to reconstruct the original AES key. The recipient needs the actual key, not a hash of it.

---

**Question 9 (5 points)**
A security analyst finds a process named `svchost32.exe` running from `C:\Users\jsmith\AppData\Roaming\` on an accounting workstation. The legitimate `svchost.exe` runs from `C:\Windows\System32\`. The process has run for 14 days and makes periodic outbound connections to an Eastern Europe IP. Which malware technique does the process name and location most likely represent?
A) SQL injection
B) Masquerading — using a name similar to a legitimate process to evade detection
C) Pass-the-hash — using the process to steal credential hashes from LSASS
D) Rootkit — hiding the process from the operating system process list
*   **Correct Answer:** B) Masquerading — using a name similar to a legitimate process to evade detection
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SQL injection is a web application attack against database query inputs. It is entirely unrelated to a Windows process running under a user's AppData directory.
    *   *Why C is incorrect:* Pass-the-hash captures NTLM credential hashes from LSASS memory and replays them for lateral movement. The question asks about the technique represented by the process name and location — masquerading is the defining characteristic described.
    *   *Why D is incorrect:* A rootkit hides itself by intercepting OS system calls and would typically not appear in the process list at all. The fact that the analyst can see `svchost32.exe` indicates it is not using rootkit techniques.

---

**Question 10 (5 points)**
A company migrates its web application to AWS EC2. The CISO asks who is responsible for patching the EC2 instance operating systems under the AWS shared responsibility model. Which answer is correct?
A) AWS is responsible for all patching because they own the infrastructure.
B) The customer is responsible for patching the OS and application on EC2 instances; AWS patches the physical infrastructure, hypervisor, and managed services.
C) Both AWS and the customer share equal responsibility for patching EC2 operating systems.
D) Patching responsibility depends on the AWS region where instances are deployed.
*   **Correct Answer:** B) The customer is responsible for patching the OS and application on EC2 instances; AWS patches the physical infrastructure, hypervisor, and managed services.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* EC2 is an IaaS service. AWS manages security of the cloud (hardware, hypervisor, network), but the customer is fully responsible for security in the cloud — including guest OS patches, application software, and security configurations.
    *   *Why C is incorrect:* There is no shared equal responsibility for EC2 OS patching. The boundary is clearly defined: AWS owns the hypervisor layer and below; the customer owns the guest OS layer and above.
    *   *Why D is incorrect:* Shared responsibility model boundaries are consistent across all AWS regions. The patching responsibility for EC2 is determined by the service type (IaaS), not geographic deployment location.

---

**Question 11 (5 points)**
A forensic investigator uses a hardware write blocker before attaching a compromised server's hard drive to the forensic workstation. What is the primary purpose of the write blocker?
A) To encrypt the drive image to protect its confidentiality during transit.
B) To prevent any write operations to the original evidence drive, preserving its integrity and admissibility.
C) To accelerate the imaging process by bypassing the drive's firmware.
D) To verify that the drive image hash matches the original drive hash after imaging.
*   **Correct Answer:** B) To prevent any write operations to the original evidence drive, preserving its integrity and admissibility.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A write blocker does not encrypt the drive or image. Encryption of the forensic image is a separate step performed after imaging. The write blocker's sole function is to intercept and block write commands directed at the source drive.
    *   *Why C is incorrect:* Write blockers are pass-through devices that allow reads while blocking writes — they do not accelerate imaging. Imaging speed is determined by the drive interface and imaging tool.
    *   *Why D is incorrect:* Hash verification is performed by the imaging tool after the image is created. The write blocker ensures the source drive is not modified during imaging so the hash comparison is valid, but it does not perform hash verification itself.

---

**Question 12 (5 points)**
An employee is terminated. The CA must immediately revoke their certificate before its expiration date so relying parties know it is no longer trustworthy. Which two PKI mechanisms communicate certificate revocation status to relying parties?
A) Re-issuing a replacement certificate with a shorter validity period and sending an email notification.
B) Publishing the revoked certificate's serial number in a Certificate Revocation List (CRL) and/or responding to OCSP queries with a revoked status.
C) Updating the certificate's expiration date field to yesterday via the CA administrative interface.
D) Sending a signed revocation message directly to every system that trusts the CA.
*   **Correct Answer:** B) Publishing the revoked certificate's serial number in a Certificate Revocation List (CRL) and/or responding to OCSP queries with a revoked status.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Email notification is not a PKI revocation mechanism. Relying parties check CRL or OCSP, not email, to verify certificate status. A new certificate would only be issued to a different user after proper vetting.
    *   *Why C is incorrect:* Certificates are signed by the CA — any modification to the certificate's fields would invalidate the CA's digital signature. Certificate fields cannot be modified after issuance; the certificate must be revoked and a new one issued.
    *   *Why D is incorrect:* PKI is designed to scale across large networks. Sending individual signed revocation messages to every relying party would require the CA to know every trusting system — architecturally impractical at enterprise scale.

---

**Question 13 (5 points)**
A company's secondary disaster recovery facility has all the same hardware pre-installed, connected to the network, and running with current data synchronized in real time. It can assume production load within minutes of a failover decision. Which DR site type does this describe?
A) Cold site
B) Warm site
C) Hot site
D) Mobile site
*   **Correct Answer:** C) Hot site
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A cold site has power, cooling, and physical space but no pre-installed hardware or data. It requires days to weeks of setup before operations can resume.
    *   *Why B is incorrect:* A warm site has hardware installed but typically lacks real-time data synchronization. Recovery requires restoring from recent backups, resulting in recovery times measured in hours rather than minutes.
    *   *Why D is incorrect:* A mobile site is a transportable, self-contained facility deployed to a disaster location. The scenario describes a fixed secondary facility with real-time synchronization and sub-minute failover capability, which is the defining characteristic of a hot site.

---

**Question 14 (5 points)**
An access control policy evaluates a user's department, current location, resource classification level, and time of day simultaneously at runtime to determine access rights. Which access control model is this?
A) Mandatory Access Control (MAC)
B) Discretionary Access Control (DAC)
C) Role-Based Access Control (RBAC)
D) Attribute-Based Access Control (ABAC)
*   **Correct Answer:** D) Attribute-Based Access Control (ABAC)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* MAC assigns access based on security labels and clearance levels such as Top Secret or Secret. Access decisions use classification labels, not dynamic combinations of department, location, time, and resource attributes evaluated at runtime.
    *   *Why B is incorrect:* DAC allows data owners to set permissions on their own resources at their discretion. It is owner-controlled, not a policy-driven multi-attribute evaluation engine.
    *   *Why C is incorrect:* RBAC assigns permissions to roles and users to roles. Access is determined by role membership, not by dynamically evaluating multiple contextual attributes simultaneously. ABAC is a generalization of RBAC that adds attribute-based policy evaluation.

---

**Question 15 (5 points)**
During incident response, ransomware is actively spreading via SMB across a flat network. The IR team lead decides to disable all switch ports on the affected segment. A business unit manager objects that this will halt afternoon production. How should the IR team lead respond?
A) Restore connectivity and use endpoint antivirus to clean infected systems in place to minimize disruption.
B) Accept the objection and limit containment to blocking only the confirmed-infected servers.
C) Maintain network isolation — stopping active spread is the correct priority, and partial containment will cause greater total disruption than full containment now.
D) Escalate to the CISO for permission before acting, since the IR team lacks authority to impact production.
*   **Correct Answer:** C) Maintain network isolation — stopping active spread is the correct priority, and partial containment will cause greater total disruption than full containment now.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Attempting to clean actively encrypting ransomware in place while it continues spreading via SMB results in more systems being encrypted during cleanup. The correct sequence is contain first, then eradicate.
    *   *Why B is incorrect:* Partial containment allows the malware to continue encrypting unaffected systems. The resulting recovery scope will be larger — and more disruptive — than a brief planned network outage for full containment.
    *   *Why D is incorrect:* IR plans should pre-authorize containment actions for active ransomware. Waiting for CISO approval while ransomware spreads to additional production systems is inconsistent with sound IR practice. The Preparation phase should define authority to isolate segments during active incidents.

---

**Question 16 (5 points)**
A developer validates only the `.jpg` file extension before saving user-uploaded profile photos to the web server's document root. An attacker uploads `shell.php.jpg`, which the server executes as a PHP script, granting remote code execution. Which vulnerability class does this represent?
A) Cross-site scripting (XSS)
B) SQL injection
C) Unrestricted file upload with insufficient validation
D) Server-side request forgery (SSRF)
*   **Correct Answer:** C) Unrestricted file upload with insufficient validation
*   **Distractor Analysis:**
    *   *Why A is incorrect:* XSS injects malicious scripts into web pages that execute in the victim's browser. File upload vulnerabilities place malicious files on the server — code executes server-side, not in a browser.
    *   *Why B is incorrect:* SQL injection inserts malicious SQL syntax into database query inputs. No database query is involved in this file upload scenario — the vulnerability is in the file handling and server execution logic.
    *   *Why D is incorrect:* SSRF tricks a server into making requests to internal or external resources on the attacker's behalf. This scenario involves uploading a malicious file that achieves server-side code execution, not forged server-initiated requests.

---

**Question 17 (5 points)**
A security architect places public-facing web servers, application servers, and database servers in three separate network segments with firewall rules permitting only specific necessary traffic between segments. Which network security architecture concept does this implement?
A) Air gap
B) Defense in depth through network segmentation and DMZ architecture
C) VPN tunneling
D) Network Access Control (NAC)
*   **Correct Answer:** B) Defense in depth through network segmentation and DMZ architecture
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An air gap is complete physical separation with no electronic connection between networks. The described architecture has multiple segments communicating via controlled firewall rules — there are deliberate controlled paths between tiers.
    *   *Why C is incorrect:* A VPN creates an encrypted tunnel for remote access or site-to-site connectivity. The described architecture uses internal firewall segmentation between application tiers, not encrypted tunneling.
    *   *Why D is incorrect:* NAC evaluates endpoint health posture before granting network admission. The three-tier segmentation design described addresses lateral movement between application tiers, not endpoint admission control.

---

**Question 18 (5 points)**
A threat actor sends an email appearing to come from the hospital CEO's legitimate address, instructing the CFO to wire $180,000 immediately for a confidential acquisition — and to tell no one. The CFO wires the money before IT can intervene. Which social engineering technique does this describe?
A) Phishing — a mass email campaign impersonating a trusted institution
B) Vishing — a voice call impersonating an executive
C) Business Email Compromise (BEC) — targeted financial fraud via executive impersonation
D) Pretexting — fabricating a false identity to extract information
*   **Correct Answer:** C) Business Email Compromise (BEC) — targeted financial fraud via executive impersonation
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Phishing is a mass campaign sent to many recipients impersonating banks or IT helpdesks to steal credentials. This is a single-recipient, targeted financial fraud email — BEC, not generic phishing.
    *   *Why B is incorrect:* Vishing uses voice calls, not email. The attack described is conducted entirely through email.
    *   *Why D is incorrect:* Pretexting fabricates a scenario to extract information, such as impersonating IT support to get a password. BEC is specifically defined by a spoofed or compromised executive email directing fraudulent wire transfers — the urgency, secrecy, and financial transfer instruction are the BEC markers.

---

**Question 19 (5 points)**
A SOC analyst is granted temporary write access to a threat intelligence platform for a 30-day project. The access is never removed. Three months later she still has write access she no longer needs. Which access control principle is being violated?
A) Separation of duties
B) Need to know
C) Least privilege — specifically, failure to revoke access when the business need ends
D) Mandatory Access Control
*   **Correct Answer:** C) Least privilege — specifically, failure to revoke access when the business need ends
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Separation of duties prevents one person from having conflicting privileges enabling fraud (e.g., both authorizing and executing a financial transaction). This scenario describes accumulated unnecessary access — a least privilege violation, not conflicting duties.
    *   *Why B is incorrect:* Need to know is closely related to least privilege but specifically addresses whether a person has a legitimate reason to access particular data. The violation here is about access not being revoked when the project ended — an access lifecycle management failure.
    *   *Why D is incorrect:* MAC assigns access based on clearance labels set by administrators. It is not related to the failure to revoke project-based access in an RBAC model.

---

**Question 20 (5 points)**
A company's current perimeter firewall grants implicit trust to all traffic from inside the corporate network. Under a zero trust architecture, which principle replaces implicit internal trust?
A) All internal traffic is encrypted using IPsec tunnel mode between every host pair.
B) Every access request is continuously verified against policy — no entity is trusted by default based on network location alone.
C) All employees must use VPN even when working inside the office building.
D) The perimeter firewall is replaced with host-based firewalls on every endpoint.
*   **Correct Answer:** B) Every access request is continuously verified against policy — no entity is trusted by default based on network location alone.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IPsec encryption provides confidentiality and integrity for network traffic but does not eliminate implicit trust. An encrypted connection from a compromised internal host is still a threat. Zero trust addresses trust decisions, not just encryption.
    *   *Why C is incorrect:* Requiring VPN for on-premises users may be one tactic in some zero trust implementations, but it is not the defining principle. The core principle is continuous policy-based verification of identity, device health, and context for every access request.
    *   *Why D is incorrect:* Host-based firewalls are a useful defense-in-depth control but do not implement zero trust policy verification. Zero trust requires a policy engine evaluating identity, device posture, resource sensitivity, and context — not just firewall placement.

---

End of Quiz — Module 16
