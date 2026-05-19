# Quiz: Module 06 - Social Engineering Attacks
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is a phishing attack that specifically targets high-profile corporate executives (such as CEOs or CFOs) called?
*   A) Spear-phishing
*   B) Whaling
*   C) Vishing
*   D) Smishing
*   **Correct Answer:** B) Whaling is a sub-class of phishing designed specifically to target high-ranking executive personnel.
*   **Distractor Analysis:**
    *   *Why correct:* Whaling is a sub-class of phishing designed specifically to target high-ranking executive personnel.
    *   Spear-phishing targets any specific individual. Vishing is voice. Smishing is SMS.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **tailgating**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
D) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
C) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **tailgating**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **tailgating**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **tailgating**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **tailgating**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
A) nmap -sV -p 1-1024 target_ip
D) openssl x509 -text -noout -in cert.pem
C) wireshark
B) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Social Engineering Attacks** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..


---

**Question 5**
When designing a system for **Social Engineering Attacks**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

