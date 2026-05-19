# Quiz: Module 08 - Exploiting Windows & Active Directory
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which Active Directory attack involves requesting service tickets and attempting to crack the service account password hashes offline?
*   A) Pass-the-Hash
*   B) Kerberoasting
*   C) AS-REP Roasting
*   D) SMB Relay
*   **Correct Answer:** B) Kerberoasting allows standard AD users to request tickets for service principal names (SPNs) and attempt offline brute-forcing.
*   **Distractor Analysis:**
    *   *Why correct:* Kerberoasting allows standard AD users to request tickets for service principal names (SPNs) and attempt offline brute-forcing.
    *   Pass-the-hash uses existing hashes to authenticate without cracking them.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **SMB exploitation.**?
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
D) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **SMB exploitation.**.
    * *Why A is correct:* This describes the exact role and function of **SMB exploitation.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **SMB exploitation.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **SMB exploitation.**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) openssl x509 -text -noout -in cert.pem
C) wireshark
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
While working on **Exploiting Windows & Active Directory** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Exploiting Windows & Active Directory**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

