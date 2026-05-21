# Quiz: Module 03 - Passive Reconnaissance (OSINT)
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which command-line tool is used for passive DNS gathering, specifically retrieving mail server configurations?
*   A) dig example.com MX
*   B) nmap example.com
*   C) ping example.com
*   D) traceroute example.com
*   **Correct Answer:** A) `dig` queries DNS name servers. Passing `MX` retrieves mail records passively without targeting the server directly.
*   **Distractor Analysis:**
    *   *Why correct:* `dig` queries DNS name servers. Passing `MX` retrieves mail records passively without targeting the server directly.
    *   Nmap is active scanning. Ping sends ICMP traffic. Traceroute routes packets.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **host)**?
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
B) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
C) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **host)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **host)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **host)**.
    * *Why A is correct:* This describes the exact role and function of **host)**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
B) nmap -sV -p 1-1024 target_ip
A) wireshark
C) openssl x509 -text -noout -in cert.pem
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Passive Reconnaissance (OSINT)** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Passive Reconnaissance (OSINT)**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

