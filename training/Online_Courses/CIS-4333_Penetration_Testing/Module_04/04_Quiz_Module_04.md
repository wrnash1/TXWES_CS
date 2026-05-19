# Quiz: Module 04 - Active Reconnaissance (Nmap)
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which Nmap scan type is known as 'stealth' or 'half-open' scanning because it does not complete the 3-way handshake?
*   A) TCP Connect Scan (-sT)
*   B) TCP SYN Scan (-sS)
*   C) UDP Scan (-sU)
*   D) Ping Sweep (-sn)
*   **Correct Answer:** B) SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK to keep connections half-open.
*   **Distractor Analysis:**
    *   *Why correct:* SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK to keep connections half-open.
    *   Connect scans complete the handshake, leaving log footprints on target sockets.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **OS detection (-O)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
B) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
D) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **OS detection (-O)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **OS detection (-O)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **OS detection (-O)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **OS detection (-O)**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
C) nmap -sV -p 1-1024 target_ip
D) wireshark
B) hydra -l admin -P passwords.txt ssh://target
A) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.


---

**Question 4**
While working on **Active Reconnaissance (Nmap)** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Active Reconnaissance (Nmap)**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
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

