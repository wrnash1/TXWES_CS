# Quiz: Module 09 - Exploiting Linux Systems
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which file permission bit configuration allows an executable to run with the permissions of the file owner (often root)?
*   A) Write Permission
*   B) Sticky Bit
*   C) SUID (Set Owner User ID)
*   D) Execute Bit
*   **Correct Answer:** C) SUID allows binaries to execute using root privileges, creating potential escalation targets if misconfigured.
*   **Distractor Analysis:**
    *   *Why correct:* SUID allows binaries to execute using root privileges, creating potential escalation targets if misconfigured.
    *   Sticky bit limits deletions. SGID sets group execution permissions.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **exploiting SUID binaries**?
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
D) A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **exploiting SUID binaries**.
    * *Why A is correct:* This describes the exact role and function of **exploiting SUID binaries**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **exploiting SUID binaries**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **exploiting SUID binaries**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
D) hydra -l admin -P passwords.txt ssh://target
B) openssl x509 -text -noout -in cert.pem
A) nmap -sV -p 1-1024 target_ip
C) wireshark
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Exploiting Linux Systems** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Exploiting Linux Systems**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

