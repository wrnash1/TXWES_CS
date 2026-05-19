# Quiz: Module 05 - Vulnerability Scanning
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is it called when a vulnerability scanner reports a security issue that does not actually exist on the target system?
*   A) False Negative
*   B) False Positive
*   C) True Positive
*   D) Null Match
*   **Correct Answer:** B) False Positives occur when scanning rules mismatch background states and assume a vulnerability is present.
*   **Distractor Analysis:**
    *   *Why correct:* False Positives occur when scanning rules mismatch background states and assume a vulnerability is present.
    *   False Negatives are when real issues are missed by the scanner.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **false positives vs false negatives**?
D) A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.
B) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **false positives vs false negatives**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **false positives vs false negatives**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **false positives vs false negatives**.
    * *Why A is correct:* This describes the exact role and function of **false positives vs false negatives**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
D) hydra -l admin -P passwords.txt ssh://target
B) openssl x509 -text -noout -in cert.pem
A) wireshark
C) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Vulnerability Scanning** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Tune the detection signatures and define exceptions for authorized administrative activities.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Vulnerability Scanning**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

