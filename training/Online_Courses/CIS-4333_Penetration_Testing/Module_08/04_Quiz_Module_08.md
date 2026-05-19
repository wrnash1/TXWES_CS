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
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
D) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
B) Intrusion Detection/Prevention Systems that monitor network traffic for suspicious activity or policy violations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **SMB exploitation.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **SMB exploitation.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **SMB exploitation.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **SMB exploitation.**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
A) nmap -sV -p 1-1024 target_ip
B) wireshark
C) openssl x509 -text -noout -in cert.pem
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Exploiting Windows & Active Directory** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Exploiting Windows & Active Directory**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

