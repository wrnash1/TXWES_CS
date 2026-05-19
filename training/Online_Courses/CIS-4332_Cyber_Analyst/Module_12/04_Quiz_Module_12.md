# Quiz: Module 12 - Incident Response Frameworks
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
During which phase of the NIST incident response lifecycle do you isolate a system to prevent further damage?
*   A) Detection and Analysis
*   B) Containment, Eradication, and Recovery
*   C) Post-Incident Activity
*   D) Preparation
*   **Correct Answer:** B) Containment limits the scope of the breach (e.g. shutting down ports, isolating subnets).
*   **Distractor Analysis:**
    *   *Why correct:* Containment limits the scope of the breach (e.g. shutting down ports, isolating subnets).
    *   Detection comes before containment. Eradication is removing the threat.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Containment/Eradication**?
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
C) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Containment/Eradication**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Containment/Eradication**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Containment/Eradication**.
    * *Why A is correct:* This describes the exact role and function of **Containment/Eradication**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
D) hydra -l admin -P passwords.txt ssh://target
A) openssl x509 -text -noout -in cert.pem
C) wireshark
B) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Incident Response Frameworks** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Incident Response Frameworks**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..

