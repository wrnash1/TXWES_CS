# Quiz: Module 15 - Security Controls & Architecture
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which control type is a security awareness training program classified as?
*   A) Technical control
*   B) Administrative (Managerial) control
*   C) Physical control
*   D) Deterrent control
*   **Correct Answer:** B) Administrative controls are written policies, guidelines, and training implemented by management.
*   **Distractor Analysis:**
    *   *Why correct:* Administrative controls are written policies, guidelines, and training implemented by management.
    *   Technical controls are software/hardware locks. Physical controls are fences/badges.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **security logging topologies.**?
B) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
D) The core model of cybersecurity representing three objectives: Confidentiality, Integrity, and Availability.
C) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **security logging topologies.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **security logging topologies.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **security logging topologies.**.
    * *Why A is correct:* This describes the exact role and function of **security logging topologies.**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
A) hydra -l admin -P passwords.txt ssh://target
C) nmap -sV -p 1-1024 target_ip
D) openssl x509 -text -noout -in cert.pem
B) wireshark
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Security Controls & Architecture** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..


---

**Question 5**
When designing a system for **Security Controls & Architecture**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

