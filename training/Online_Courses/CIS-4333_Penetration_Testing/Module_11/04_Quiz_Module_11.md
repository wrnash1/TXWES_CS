# Quiz: Module 11 - Wireless Network Assessment
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which wireless security standard is vulnerable to offline dictionary attacks on its 4-way handshake?
*   A) WPA3
*   B) WPA2-Personal (PSK)
*   C) WPA2-Enterprise
*   D) WEP
*   **Correct Answer:** B) WPA2-Personal uses a 4-way handshake that can be captured and brute-forced offline. WPA3 replaces this with SAE.
*   **Distractor Analysis:**
    *   *Why correct:* WPA2-Personal uses a 4-way handshake that can be captured and brute-forced offline. WPA3 replaces this with SAE.
    *   WEP uses RC4 cracking methods, not handshake brute-forcing. Enterprise uses RADIUS.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **packet capture (airodump-ng)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **packet capture (airodump-ng)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **packet capture (airodump-ng)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **packet capture (airodump-ng)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **packet capture (airodump-ng)**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
B) wireshark
D) nmap -sV -p 1-1024 target_ip
C) hydra -l admin -P passwords.txt ssh://target
A) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.


---

**Question 4**
While working on **Wireless Network Assessment** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Wireless Network Assessment**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

