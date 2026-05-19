# Quiz: Module 06 - IDS/IPS Tools & Monitoring
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the main operational difference between an IDS and an IPS?
*   A) IDS is active, IPS is passive
*   B) IDS only detects and alerts, while IPS actively blocks traffic
*   C) IDS works at Layer 2, IPS works at Layer 7
*   D) IDS does not require rules
*   **Correct Answer:** B) Intrusion Detection Systems (IDS) detect/log. Intrusion Prevention Systems (IPS) sit inline and can block traffic.
*   **Distractor Analysis:**
    *   *Why correct:* Intrusion Detection Systems (IDS) detect/log. Intrusion Prevention Systems (IPS) sit inline and can block traffic.
    *   IDS is passive. IPS is active.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Signature-based vs anomaly-based detection**?
B) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Signature-based vs anomaly-based detection**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Signature-based vs anomaly-based detection**.
    * *Why A is correct:* This describes the exact role and function of **Signature-based vs anomaly-based detection**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Signature-based vs anomaly-based detection**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
A) wireshark
D) openssl x509 -text -noout -in cert.pem
C) nmap -sV -p 1-1024 target_ip
B) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IDS/IPS Tools & Monitoring** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **IDS/IPS Tools & Monitoring**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

