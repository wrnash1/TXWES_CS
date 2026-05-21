# Quiz: Module 16 - Final Exam Prep and CompTIA Security+ SY0-701 Certification
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

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
