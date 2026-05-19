# Quiz: Module 11 - Software Security & OWASP
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which vulnerability class allows an attacker to inject client-side scripts into web pages viewed by other users?
*   A) SQL Injection
*   B) Cross-Site Scripting (XSS)
*   C) Server-Side Request Forgery
*   D) Command Injection
*   **Correct Answer:** B) XSS vulnerabilities occur when web applications execute malicious script in the browser of another user.
*   **Distractor Analysis:**
    *   *Why correct:* XSS vulnerabilities occur when web applications execute malicious script in the browser of another user.
    *   SQLi targets databases. SSRF targets backend server requests.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **secure code reviews**?
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
D) Intrusion Detection/Prevention Systems that monitor network traffic for suspicious activity or policy violations.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The security rule that users and systems should only be granted the minimum necessary permissions required to perform their tasks.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **secure code reviews**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **secure code reviews**.
    * *Why A is correct:* This describes the exact role and function of **secure code reviews**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **secure code reviews**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
B) wireshark
A) hydra -l admin -P passwords.txt ssh://target
C) nmap -sV -p 1-1024 target_ip
D) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Software Security & OWASP** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Software Security & OWASP**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

