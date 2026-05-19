# Quiz: Module 05 - Vulnerability Scanning
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is it called when a vulnerability scanner reports a security issue that does not actually exist on the target system?
*   A) False Negative
*   B) False Positive
*   C) True Positive
*   D) Null Match
*   **Correct Answer:** B) False Positives occur when scanning rules mismatch background states and assume a vulnerability is present.
*   **Distractor Analysis:**
    *   *Why correct:* False Positives occur when scanning rules mismatch background states and assume a vulnerability is present.
    *   False Negatives are when real issues are missed by the scanner.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **analyzing severity levels.**?
B) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
C) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **analyzing severity levels.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **analyzing severity levels.**.
    * *Why A is correct:* This describes the exact role and function of **analyzing severity levels.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **analyzing severity levels.**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
C) hydra -l admin -P passwords.txt ssh://target
A) nmap -sV -p 1-1024 target_ip
B) wireshark
D) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Vulnerability Scanning** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Vulnerability Scanning**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
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

