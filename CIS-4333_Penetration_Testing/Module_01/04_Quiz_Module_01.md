# Quiz: Module 01 - Planning & Scoping Pen Tests
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which document explicitly defines the boundaries, methods, and authorized targets of a penetration test?
*   A) Non-Disclosure Agreement (NDA)
*   B) Rules of Engagement (RoE)
*   C) Service Level Agreement (SLA)
*   D) Master Service Agreement (MSA)
*   **Correct Answer:** B) The RoE sets rules, exclusions, IP targets, and schedule guidelines for the team.
*   **Distractor Analysis:**
    *   *Why correct:* The RoE sets rules, exclusions, IP targets, and schedule guidelines for the team.
    *   NDA protects confidential data. SLA is service uptime. MSA is general commercial agreements.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **target classifications**?
B) A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.
C) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
D) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **target classifications**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **target classifications**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **target classifications**.
    * *Why A is correct:* This describes the exact role and function of **target classifications**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
B) wireshark
C) hydra -l admin -P passwords.txt ssh://target
D) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.


---

**Question 4**
While working on **Planning & Scoping Pen Tests** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Planning & Scoping Pen Tests**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

