# Quiz: Module 10 - Web Application Exploit Methods
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What web vulnerability allows an attacker to append file paths to a URL parameter to retrieve unauthorized server files?
*   A) Directory Traversal
*   B) SQL Injection
*   C) Cross-Site Scripting
*   D) Buffer Overflow
*   **Correct Answer:** A) Directory Traversal uses dot-dot-slash (`../`) parameters to escape web document roots.
*   **Distractor Analysis:**
    *   *Why correct:* Directory Traversal uses dot-dot-slash (`../`) parameters to escape web document roots.
    *   SQLi targets sql queries. XSS targets client scripts.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **SQL Injection (SQLi)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) A security control requiring users to provide two or more verification factors to gain access to resources.
B) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
C) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **SQL Injection (SQLi)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **SQL Injection (SQLi)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **SQL Injection (SQLi)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **SQL Injection (SQLi)**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
B) wireshark
C) openssl x509 -text -noout -in cert.pem
D) nmap -sV -p 1-1024 target_ip
A) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.


---

**Question 4**
While working on **Web Application Exploit Methods** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Web Application Exploit Methods**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.

