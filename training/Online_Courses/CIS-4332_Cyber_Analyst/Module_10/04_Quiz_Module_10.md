# Quiz: Module 10 - IAM Risks and Audit
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the risk associated with orphan accounts?
*   A) They waste disk space
*   B) They remain active after employees leave, providing unmonitored access points
*   C) They cannot be backed up
*   D) They cause IP address conflicts
*   **Correct Answer:** B) Orphan accounts are active accounts belonging to ex-employees that can be hijacked by attackers.
*   **Distractor Analysis:**
    *   *Why correct:* Orphan accounts are active accounts belonging to ex-employees that can be hijacked by attackers.
    *   They represent access risks rather than resource constraints.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **access reviews**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
B) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
C) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **access reviews**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **access reviews**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **access reviews**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **access reviews**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
C) hydra -l admin -P passwords.txt ssh://target
B) wireshark
D) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.


---

**Question 4**
While working on **IAM Risks and Audit** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **IAM Risks and Audit**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.

