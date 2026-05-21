# Quiz: Module 09 - Exploiting Linux Systems
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which file permission bit configuration allows an executable to run with the permissions of the file owner (often root)?
*   A) Write Permission
*   B) Sticky Bit
*   C) SUID (Set Owner User ID)
*   D) Execute Bit
*   **Correct Answer:** C) SUID allows binaries to execute using root privileges, creating potential escalation targets if misconfigured.
*   **Distractor Analysis:**
    *   *Why correct:* SUID allows binaries to execute using root privileges, creating potential escalation targets if misconfigured.
    *   Sticky bit limits deletions. SGID sets group execution permissions.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **exploiting SUID binaries**?
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
D) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **exploiting SUID binaries**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **exploiting SUID binaries**.
    * *Why A is correct:* This describes the exact role and function of **exploiting SUID binaries**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **exploiting SUID binaries**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
A) openssl x509 -text -noout -in cert.pem
C) hydra -l admin -P passwords.txt ssh://target
B) wireshark
D) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Exploiting Linux Systems** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Exploiting Linux Systems**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

