# Quiz: Module 08 - Incident Response
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **OSINT**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
D) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **OSINT**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **OSINT**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **OSINT**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **OSINT**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **MITRE ATT&CK Framework**?
D) A security control requiring users to provide two or more verification factors to gain access to resources.
B) Intrusion Detection/Prevention Systems that monitor network traffic for suspicious activity or policy violations.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **MITRE ATT&CK Framework**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **MITRE ATT&CK Framework**.
    * *Why A is correct:* This describes the exact role and function of **MITRE ATT&CK Framework**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **MITRE ATT&CK Framework**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
C) nmap -sV -p 1-1024 target_ip
B) openssl x509 -text -noout -in cert.pem
A) wireshark
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Incident Response** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Incident Response**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

