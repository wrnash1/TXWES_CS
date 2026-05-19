# Quiz: Module 16 - Final Prep
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
C) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
B) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
B) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
C) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) wireshark
C) nmap -sV -p 1-1024 target_ip
B) openssl x509 -text -noout -in cert.pem
A) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.


---

**Question 4**
While working on **Final Prep** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Final Prep**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.

