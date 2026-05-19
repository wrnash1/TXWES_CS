# Quiz: Module 09 - AppSec (OWASP)
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Exam Tip**?
B) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
C) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Exam Tip**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Exam Tip**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Exam Tip**.
    * *Why A is correct:* This describes the exact role and function of **Exam Tip**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
D) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
C) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
B) openssl x509 -text -noout -in cert.pem
C) wireshark
D) hydra -l admin -P passwords.txt ssh://target
A) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.


---

**Question 4**
While working on **AppSec (OWASP)** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **AppSec (OWASP)**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
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

