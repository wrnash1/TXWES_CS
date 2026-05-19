# Quiz: Module 14 - Penetration Testing Reports
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What section of a penetration testing report is written specifically for non-technical stakeholders?
*   A) Technical Findings List
*   B) Executive Summary
*   C) Remediation Timeline
*   D) IP Address Scope List
*   **Correct Answer:** B) The Executive Summary translates technical security risks into business impact, costs, and high-level summaries.
*   **Distractor Analysis:**
    *   *Why correct:* The Executive Summary translates technical security risks into business impact, costs, and high-level summaries.
    *   Technical findings detail raw exploit steps.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **technical findings**?
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
D) The descendant node connected to the left branch of a parent node in a binary tree structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **technical findings**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **technical findings**.
    * *Why A is correct:* This describes the exact role and function of **technical findings**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **technical findings**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
D) openssl x509 -text -noout -in cert.pem
B) wireshark
C) hydra -l admin -P passwords.txt ssh://target
A) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.


---

**Question 4**
While working on **Penetration Testing Reports** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Penetration Testing Reports**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

