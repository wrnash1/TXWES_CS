# Quiz: Module 13 - Maintaining Access & Pivoting
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which technique allows a tester to route traffic through a compromised host to access a internal network subnet?
*   A) Privilege Escalation
*   B) Pivoting
*   C) Vulnerability Scanning
*   D) Social Engineering
*   **Correct Answer:** B) Pivoting uses a compromised dual-homed host as a bridge to send traffic into internal systems.
*   **Distractor Analysis:**
    *   *Why correct:* Pivoting uses a compromised dual-homed host as a bridge to send traffic into internal systems.
    *   Escalation increases local permission level.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **registry runs)**?
C) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
D) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **registry runs)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **registry runs)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **registry runs)**.
    * *Why A is correct:* This describes the exact role and function of **registry runs)**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
A) nmap -sV -p 1-1024 target_ip
C) hydra -l admin -P passwords.txt ssh://target
B) openssl x509 -text -noout -in cert.pem
D) wireshark
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Maintaining Access & Pivoting** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..


---

**Question 5**
When designing a system for **Maintaining Access & Pivoting**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

