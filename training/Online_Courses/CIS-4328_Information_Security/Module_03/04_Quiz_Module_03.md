# Quiz: Module 03 - Cryptography
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 1**
An organization wants to deploy a new public-facing customer portal. The portal must communicate with a highly secure backend database that stores PII. Which network architectural design provides the most secure placement for these servers?
A) Place both the web server and the database server in the DMZ to ensure fast communication.
B) Place the web server in the DMZ and the database server on the internal secure network.
C) Place both servers on the internal secure network and forward port 80/443 directly from the internet router.
D) Place the database server in the DMZ and the web server on the internal network.
*   **Correct Answer:** B) Place the web server in the DMZ and the database server on the internal secure network.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Placing the database in the DMZ exposes sensitive PII to a less secure zone, violating defense-in-depth principles.
    *   *Why C is incorrect:* Port forwarding directly to the internal network bypasses the DMZ entirely, exposing the secure network to direct internet attacks.
    *   *Why D is incorrect:* The web server must face the public internet (DMZ), and the database must be hidden (Internal). Reversing them breaks functionality and security.

---

**Question 2**
Alice wants to send a highly confidential contract to Bob over an untrusted network. She wants to ensure that *only* Bob can read the contract. Using asymmetric cryptography, whose key should Alice use to encrypt the document?
A) Alice's Private Key
B) Alice's Public Key
C) Bob's Private Key
D) Bob's Public Key
*   **Correct Answer:** D) Bob's Public Key
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If Alice encrypts it with her private key, anyone with her public key (which is everyone) can decrypt it. This provides non-repudiation, not confidentiality.
    *   *Why B is incorrect:* You do not encrypt messages with your own public key.
    *   *Why C is incorrect:* Alice does not have access to Bob's private key; it must remain exclusively with Bob. Only Bob's private key can decrypt a message encrypted with Bob's public key.

---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
A) openssl x509 -text -noout -in cert.pem
D) nmap -sV -p 1-1024 target_ip
C) wireshark
B) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Cryptography** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Cryptography**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

