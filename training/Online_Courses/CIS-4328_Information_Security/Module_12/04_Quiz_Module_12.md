# Quiz: Module 12 - IoT Security
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
C) The core model of cybersecurity representing three objectives: Confidentiality, Integrity, and Availability.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
B) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
C) The core model of cybersecurity representing three objectives: Confidentiality, Integrity, and Availability.
B) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
B) wireshark
A) openssl x509 -text -noout -in cert.pem
C) hydra -l admin -P passwords.txt ssh://target
D) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IoT Security** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **IoT Security**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

