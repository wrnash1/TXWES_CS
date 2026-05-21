# Quiz: Module 01 - Threats
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 1**
An organization implements an automated system that checks the hash of system files every hour. If a hash mismatch is detected, an alert is sent to the security operations center. Which pillar of the CIA triad is this control primarily enforcing?
A) Confidentiality
B) Integrity
C) Availability
D) Non-repudiation
*   **Correct Answer:** B) Integrity
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Confidentiality is maintained by encryption (hiding data), not by hashing (checking if data changed).
    *   *Why C is incorrect:* Availability ensures systems are up (like clustering or backups), not checking for unauthorized alterations.
    *   *Why D is incorrect:* Non-repudiation proves *who* took an action (using digital signatures), while hashing only proves *if* the file changed.

---

---

**Question 2**
A company requires all employees to sign an Acceptable Use Policy (AUP) before being granted network access. How should this security control be classified?
A) Physical / Corrective
B) Logical / Detective
C) Administrative / Preventive
D) Technical / Corrective
*   **Correct Answer:** C) Administrative / Preventive
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An AUP is a written document (Administrative), not a physical barrier (Physical), and it aims to set rules before bad things happen (Preventive), not fix them after (Corrective).
    *   *Why B is incorrect:* It does not use software to enforce rules automatically (Logical), nor does it alert after the fact (Detective).
    *   *Why D is incorrect:* Technical is synonymous with Logical. An AUP is a managerial policy.

---

---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
C) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
B) wireshark
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Threats** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Threats**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

