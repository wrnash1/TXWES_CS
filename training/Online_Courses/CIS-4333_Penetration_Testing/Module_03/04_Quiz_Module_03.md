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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **DNS interrogation (dig**?
C) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) The security rule that users and systems should only be granted the minimum necessary permissions required to perform their tasks.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **DNS interrogation (dig**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **DNS interrogation (dig**.
    * *Why A is correct:* This describes the exact role and function of **DNS interrogation (dig**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **DNS interrogation (dig**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) wireshark
C) nmap -sV -p 1-1024 target_ip
A) hydra -l admin -P passwords.txt ssh://target
B) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Passive Reconnaissance (OSINT)** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Passive Reconnaissance (OSINT)**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

