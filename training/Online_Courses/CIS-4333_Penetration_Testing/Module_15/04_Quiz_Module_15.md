# Quiz: Module 15 - Post-Report Cleanup & Debriefing
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Why is cleanup critical after completing a penetration test?
*   A) To speed up network performance
*   B) To ensure no backdoors, shells, or mock payloads are left behind for real attackers to exploit
*   C) Because the contract requires it
*   D) None of the above
*   **Correct Answer:** B) Leftover backdoors created during tests represent serious security risks that actual hackers can compromise.
*   **Distractor Analysis:**
    *   *Why correct:* Leftover backdoors created during tests represent serious security risks that actual hackers can compromise.
    *   Performance impact is minimal, and cleanup is first and foremost a security requirement.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Removing shells/backdoors**?
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
C) The security rule that users and systems should only be granted the minimum necessary permissions required to perform their tasks.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Removing shells/backdoors**.
    * *Why A is correct:* This describes the exact role and function of **Removing shells/backdoors**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Removing shells/backdoors**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Removing shells/backdoors**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
A) nmap -sV -p 1-1024 target_ip
D) openssl x509 -text -noout -in cert.pem
B) hydra -l admin -P passwords.txt ssh://target
C) wireshark
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Post-Report Cleanup & Debriefing** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Post-Report Cleanup & Debriefing**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

