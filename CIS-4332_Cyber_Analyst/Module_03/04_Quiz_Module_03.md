# Quiz: Module 03 - Infrastructure Scanning Tools
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which type of scan provides the most accurate view of patch levels and installed software on a target host?
*   A) Non-credentialed scan
*   B) Credentialed scan
*   C) Passive network sniff
*   D) Stealth SYN scan
*   **Correct Answer:** B) Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.
*   **Distractor Analysis:**
    *   *Why correct:* Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.
    *   Non-credentialed scans can only analyze open network ports and banners.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **credentialed vs non-credentialed scans**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
B) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
C) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **credentialed vs non-credentialed scans**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **credentialed vs non-credentialed scans**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **credentialed vs non-credentialed scans**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **credentialed vs non-credentialed scans**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
D) wireshark
C) nmap -sV -p 1-1024 target_ip
B) hydra -l admin -P passwords.txt ssh://target
A) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.


---

**Question 4**
While working on **Infrastructure Scanning Tools** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Infrastructure Scanning Tools**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

