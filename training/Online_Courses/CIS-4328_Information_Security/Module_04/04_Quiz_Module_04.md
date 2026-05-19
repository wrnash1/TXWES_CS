# Quiz: Module 04 - Operations
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 1**
During an active malware outbreak, the incident response team decides to physically disconnect the infected web server from the corporate network switch, but leaves the server powered on to preserve memory artifacts. Which phase of the Incident Response Lifecycle does this action represent?
A) Identification
B) Containment
C) Eradication
D) Recovery
*   **Correct Answer:** B) Containment
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Identification is the phase where the team confirms an incident is actually occurring. Disconnecting the server is an action taken *after* it has been identified.
    *   *Why C is incorrect:* Eradication involves removing the malware (e.g., wiping the drive, running antivirus). Disconnecting the cable stops the spread, but the malware is still on the machine.
    *   *Why D is incorrect:* Recovery is the process of restoring the server to normal business operations, which cannot happen until the threat is eradicated.

---

**Question 2**
A security analyst needs to collect forensic evidence from a compromised workstation. According to the standard order of volatility, which of the following data sources should the analyst collect FIRST?
A) The local hard drive (HDD/SSD)
B) The routing tables and ARP cache
C) System Memory (RAM)
D) Archival backup tapes
*   **Correct Answer:** C) System Memory (RAM)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hard drives represent non-volatile storage. Data on a hard drive will survive a reboot, so it is collected *after* highly volatile sources.
    *   *Why B is incorrect:* While routing tables are volatile, RAM (which includes CPU registers and cache in broader definitions) is generally prioritized as the primary source of volatile running processes and encryption keys. (Note: CPU registers are technically higher than RAM, but among these options, RAM is the highest).
    *   *Why D is incorrect:* Backup tapes are the least volatile form of storage and can be collected at any time.

---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
C) hydra -l admin -P passwords.txt ssh://target
B) wireshark
D) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.


---

**Question 4**
While working on **Operations** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Operations**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..

