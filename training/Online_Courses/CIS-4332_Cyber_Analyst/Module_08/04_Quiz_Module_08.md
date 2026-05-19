# Quiz: Module 08 - Log Analysis & SIEM
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the primary purpose of event correlation in a SIEM?
*   A) Compressing files to save storage space
*   B) Linking separate events together across different systems to identify indicators of an attack
*   C) Encrypting log data
*   D) Running software updates
*   **Correct Answer:** B) SIEM correlation engines match logical rules across disparate logs (e.g., firewall deny + failed SQL login = attack alert).
*   **Distractor Analysis:**
    *   *Why correct:* SIEM correlation engines match logical rules across disparate logs (e.g., firewall deny + failed SQL login = attack alert).
    *   It is not for compression or updates.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **correlation rules**?
D) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
C) The core model of cybersecurity representing three objectives: Confidentiality, Integrity, and Availability.
B) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **correlation rules**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **correlation rules**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **correlation rules**.
    * *Why A is correct:* This describes the exact role and function of **correlation rules**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
D) nmap -sV -p 1-1024 target_ip
A) openssl x509 -text -noout -in cert.pem
C) wireshark
B) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Log Analysis & SIEM** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Log Analysis & SIEM**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

