# Quiz: Module 02 - Legal & Ethical Considerations
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What must a penetration tester secure before executing any port scanning or exploit tools against a client network?
*   A) Public IP certificate
*   B) Written authorization from key stakeholders
*   C) Insurance coverage
*   D) A server license
*   **Correct Answer:** B) Without written, authorized consent, performing scanning or exploits is considered illegal hacking.
*   **Distractor Analysis:**
    *   *Why correct:* Without written, authorized consent, performing scanning or exploits is considered illegal hacking.
    *   Authorization is legally required.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **HIPAA).**?
D) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
B) A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **HIPAA).**.
    * *Why A is correct:* This describes the exact role and function of **HIPAA).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **HIPAA).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **HIPAA).**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) wireshark
B) nmap -sV -p 1-1024 target_ip
A) hydra -l admin -P passwords.txt ssh://target
C) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Legal & Ethical Considerations** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
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
When designing a system for **Legal & Ethical Considerations**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..

