# Quiz: Module 13 - Forensics & Evidence Collection
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which data source should be collected FIRST during forensic collection due to its volatility?
*   A) HDD storage
*   B) CPU Registers and RAM
*   C) Log files on disk
*   D) Print server spool queue
*   **Correct Answer:** B) Memory and processor state volatile data is lost immediately on shutdown, placing them first in the order of volatility.
*   **Distractor Analysis:**
    *   *Why correct:* Memory and processor state volatile data is lost immediately on shutdown, placing them first in the order of volatility.
    *   Disk storage can survive power loss.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **chain of custody**?
D) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **chain of custody**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **chain of custody**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **chain of custody**.
    * *Why A is correct:* This describes the exact role and function of **chain of custody**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
C) hydra -l admin -P passwords.txt ssh://target
D) nmap -sV -p 1-1024 target_ip
A) wireshark
B) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Forensics & Evidence Collection** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.


---

**Question 5**
When designing a system for **Forensics & Evidence Collection**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

