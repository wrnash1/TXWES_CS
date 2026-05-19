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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Snort rule configuration**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
B) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Snort rule configuration**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Snort rule configuration**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Snort rule configuration**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Snort rule configuration**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) nmap -sV -p 1-1024 target_ip
B) wireshark
A) hydra -l admin -P passwords.txt ssh://target
C) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IDS/IPS Tools & Monitoring** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **IDS/IPS Tools & Monitoring**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

