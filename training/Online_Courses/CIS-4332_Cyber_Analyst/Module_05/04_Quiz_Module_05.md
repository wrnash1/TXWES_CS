# Quiz: Module 05 - Threat Intelligence & Hunting
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which protocol is the standard carrier for exchanging structured cyber threat intelligence data over HTTP?
*   A) STIX
*   B) TAXII
*   C) JSON-RPC
*   D) Syslog
*   **Correct Answer:** B) TAXII (Trusted Automated Exchange of Intelligence Information) is the transport mechanism. STIX is the language format.
*   **Distractor Analysis:**
    *   *Why correct:* TAXII (Trusted Automated Exchange of Intelligence Information) is the transport mechanism. STIX is the language format.
    *   STIX defines the data schema, TAXII carries it.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **threat intelligence feeds (STIX/TAXII).**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
D) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
B) A social engineering attack where malicious actors send fraudulent messages designed to trick victims into revealing sensitive information.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **threat intelligence feeds (STIX/TAXII).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **threat intelligence feeds (STIX/TAXII).**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **threat intelligence feeds (STIX/TAXII).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **threat intelligence feeds (STIX/TAXII).**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
D) hydra -l admin -P passwords.txt ssh://target
B) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
C) wireshark
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Threat Intelligence & Hunting** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..


---

**Question 5**
When designing a system for **Threat Intelligence & Hunting**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..

