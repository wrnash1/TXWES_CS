# Quiz: Module 07 - Host-Based Security & EDR
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which technology monitors system files in real-time to detect unauthorized file alterations or registry edits?
*   A) Endpoint Detection and Response (EDR)
*   B) File Integrity Monitoring (FIM)
*   C) Antivirus signatures
*   D) Host-based firewall
*   **Correct Answer:** B) FIM compares cryptographic hashes of files against a baseline to detect modifications.
*   **Distractor Analysis:**
    *   *Why correct:* FIM compares cryptographic hashes of files against a baseline to detect modifications.
    *   EDR is broader. FIM is specific to file tampering.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **local system audits.**?
C) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
B) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **local system audits.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **local system audits.**.
    * *Why A is correct:* This describes the exact role and function of **local system audits.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **local system audits.**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
B) wireshark
C) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Host-Based Security & EDR** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..


---

**Question 5**
When designing a system for **Host-Based Security & EDR**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.

