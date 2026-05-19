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
C) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
D) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The security rule that users and systems should only be granted the minimum necessary permissions required to perform their tasks.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **local system audits.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **local system audits.**.
    * *Why A is correct:* This describes the exact role and function of **local system audits.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **local system audits.**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
A) wireshark
C) hydra -l admin -P passwords.txt ssh://target
D) openssl x509 -text -noout -in cert.pem
B) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Host-Based Security & EDR** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Host-Based Security & EDR**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

