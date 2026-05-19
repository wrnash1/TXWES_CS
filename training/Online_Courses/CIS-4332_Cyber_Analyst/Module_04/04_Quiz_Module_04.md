# Quiz: Module 04 - Analyzing Vulnerability Reports
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which CVSS metric group represents the characteristics of a vulnerability that constant over time and across environments?
*   A) Base Metric Group
*   B) Temporal Metric Group
*   C) Environmental Metric Group
*   D) Local Metric Group
*   **Correct Answer:** A) Base metrics represent the core qualities of the vulnerability that do not change.
*   **Distractor Analysis:**
    *   *Why correct:* Base metrics represent the core qualities of the vulnerability that do not change.
    *   Temporal metrics reflect threat activity. Environmental metrics reflect local network importance.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **base/temporal/environmental metrics**?
B) The security rule that users and systems should only be granted the minimum necessary permissions required to perform their tasks.
C) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
D) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **base/temporal/environmental metrics**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **base/temporal/environmental metrics**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **base/temporal/environmental metrics**.
    * *Why A is correct:* This describes the exact role and function of **base/temporal/environmental metrics**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
A) wireshark
B) openssl x509 -text -noout -in cert.pem
C) nmap -sV -p 1-1024 target_ip
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Analyzing Vulnerability Reports** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Analyzing Vulnerability Reports**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

