# Quiz: Module 07 - Exploiting Network Vulnerabilities
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which type of shell payload instructs the target machine to connect back to the attacker's listening machine?
*   A) Bind Shell
*   B) Reverse Shell
*   C) SSH Shell
*   D) Interactive Shell
*   **Correct Answer:** B) Reverse shells initiate connections outwards from the target, bypassing inbound firewall blocks.
*   **Distractor Analysis:**
    *   *Why correct:* Reverse shells initiate connections outwards from the target, bypassing inbound firewall blocks.
    *   Bind shells open a port on target and listen for attacker connections.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **reverse vs bind shells.**?
C) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **reverse vs bind shells.**.
    * *Why A is correct:* This describes the exact role and function of **reverse vs bind shells.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **reverse vs bind shells.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **reverse vs bind shells.**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
A) nmap -sV -p 1-1024 target_ip
C) openssl x509 -text -noout -in cert.pem
B) wireshark
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Exploiting Network Vulnerabilities** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..


---

**Question 5**
When designing a system for **Exploiting Network Vulnerabilities**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

