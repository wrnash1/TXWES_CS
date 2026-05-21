# Quiz: Module 01 - Security Operations & Analyst Role
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What does IOC stand for in security operations?
*   A) Index of Controls
*   B) Indicator of Compromise
*   C) Institution of Cybersecurity
*   D) Internal Operational Check
*   **Correct Answer:** B) Indicators of Compromise (IOCs) are forensic clues (file hashes, IPs, domains) that indicate a security breach.
*   **Distractor Analysis:**
    *   *Why correct:* Indicators of Compromise (IOCs) are forensic clues (file hashes, IPs, domains) that indicate a security breach.
    *   The other options are made up acronyms.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **threat landscape**?
C) A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
D) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **threat landscape**.
    * *Why A is correct:* This describes the exact role and function of **threat landscape**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **threat landscape**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **threat landscape**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
D) openssl x509 -text -noout -in cert.pem
B) wireshark
A) nmap -sV -p 1-1024 target_ip
C) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Security Operations & Analyst Role** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Security Operations & Analyst Role**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

