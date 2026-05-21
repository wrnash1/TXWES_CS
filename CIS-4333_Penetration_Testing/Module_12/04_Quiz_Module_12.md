# Quiz: Module 12 - Post-Exploitation & Privilege Escalation
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is the primary goal of privilege escalation during post-exploitation?
*   A) Scanning the local subnet
*   B) Elevating privileges from a standard user to administrator/root
*   C) Deleting logs
*   D) Installing backdoors
*   **Correct Answer:** B) Privilege escalation focuses on finding paths to gain administrative control after initial access.
*   **Distractor Analysis:**
    *   *Why correct:* Privilege escalation focuses on finding paths to gain administrative control after initial access.
    *   Lateral movement is moving networks. Escalation is increasing privileges.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Privilege escalation (Windows UAC bypass**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
D) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
B) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Privilege escalation (Windows UAC bypass**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Privilege escalation (Windows UAC bypass**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Privilege escalation (Windows UAC bypass**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Privilege escalation (Windows UAC bypass**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
B) wireshark
A) hydra -l admin -P passwords.txt ssh://target
D) nmap -sV -p 1-1024 target_ip
C) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Post-Exploitation & Privilege Escalation** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Post-Exploitation & Privilege Escalation**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

