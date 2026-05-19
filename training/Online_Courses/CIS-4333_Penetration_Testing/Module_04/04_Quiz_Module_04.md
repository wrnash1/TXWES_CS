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
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
B) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **OS detection (-O)**.
    * *Why A is correct:* This describes the exact role and function of **OS detection (-O)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **OS detection (-O)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **OS detection (-O)**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
D) hydra -l admin -P passwords.txt ssh://target
C) openssl x509 -text -noout -in cert.pem
B) wireshark
A) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.


---

**Question 4**
While working on **Active Reconnaissance (Nmap)** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Active Reconnaissance (Nmap)**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.

