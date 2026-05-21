# Quiz: Module 10 - Web Application Exploit Methods
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What web vulnerability allows an attacker to append file paths to a URL parameter to retrieve unauthorized server files?
*   A) Directory Traversal
*   B) SQL Injection
*   C) Cross-Site Scripting
*   D) Buffer Overflow
*   **Correct Answer:** A) Directory Traversal uses dot-dot-slash (`../`) parameters to escape web document roots.
*   **Distractor Analysis:**
    *   *Why correct:* Directory Traversal uses dot-dot-slash (`../`) parameters to escape web document roots.
    *   SQLi targets sql queries. XSS targets client scripts.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Cross-Site Scripting (XSS)**?
B) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
D) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Cross-Site Scripting (XSS)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Cross-Site Scripting (XSS)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Cross-Site Scripting (XSS)**.
    * *Why A is correct:* This describes the exact role and function of **Cross-Site Scripting (XSS)**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
B) openssl x509 -text -noout -in cert.pem
C) nmap -sV -p 1-1024 target_ip
D) wireshark
A) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.


---

**Question 4**
While working on **Web Application Exploit Methods** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Web Application Exploit Methods**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
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

