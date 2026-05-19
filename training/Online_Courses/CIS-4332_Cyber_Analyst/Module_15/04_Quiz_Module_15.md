# Quiz: Module 15 - Security Controls & Architecture
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which control type is a security awareness training program classified as?
*   A) Technical control
*   B) Administrative (Managerial) control
*   C) Physical control
*   D) Deterrent control
*   **Correct Answer:** B) Administrative controls are written policies, guidelines, and training implemented by management.
*   **Distractor Analysis:**
    *   *Why correct:* Administrative controls are written policies, guidelines, and training implemented by management.
    *   Technical controls are software/hardware locks. Physical controls are fences/badges.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **defense-in-depth**?
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
C) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **defense-in-depth**.
    * *Why A is correct:* This describes the exact role and function of **defense-in-depth**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **defense-in-depth**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **defense-in-depth**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) wireshark
C) openssl x509 -text -noout -in cert.pem
B) nmap -sV -p 1-1024 target_ip
A) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.


---

**Question 4**
While working on **Security Controls & Architecture** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Security Controls & Architecture**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

