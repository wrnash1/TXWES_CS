# Quiz: Module 12 - Post-Exploitation & Privilege Escalation
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is the primary goal of privilege escalation during post-exploitation?
*   A) Scanning the local subnet
*   B) Elevating privileges from a standard user to administrator/root
*   C) Deleting logs
*   D) Installing backdoors
*   **Correct Answer:** B) Privilege escalation focuses on finding paths to gain administrative control after initial access.
*   **Distractor Analysis:**
    *   *Why correct:* Privilege escalation focuses on finding paths to gain administrative control after initial access.
    *   Lateral movement is moving networks. Escalation is increasing privileges.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Linux cron jobs)**?
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
C) The core model of cybersecurity representing three objectives: Confidentiality, Integrity, and Availability.
D) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Linux cron jobs)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Linux cron jobs)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Linux cron jobs)**.
    * *Why A is correct:* This describes the exact role and function of **Linux cron jobs)**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
C) nmap -sV -p 1-1024 target_ip
D) openssl x509 -text -noout -in cert.pem
B) hydra -l admin -P passwords.txt ssh://target
A) wireshark
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.


---

**Question 4**
While working on **Post-Exploitation & Privilege Escalation** in a production environment, you encounter a system alert indicating a **Certificate Expired Error** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why C is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why D is incorrect:* This action does not resolve the root cause of Certificate Expired Error.
    * *Why A is correct:* Because The SSL/TLS digital certificate presented by the server has passed its validity end date, causing clients to block connections. The appropriate fix is to Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA..


---

**Question 5**
When designing a system for **Post-Exploitation & Privilege Escalation**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.

