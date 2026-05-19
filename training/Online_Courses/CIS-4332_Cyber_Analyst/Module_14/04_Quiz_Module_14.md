# Quiz: Module 14 - Threat Detection & Containment
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the purpose of DNS sinkholing in incident containment?
*   A) Speeding up DNS requests
*   B) Redirecting malicious outbound traffic to a secure internal IP address
*   C) Encrypting domain records
*   D) Shutting down the DNS server
*   **Correct Answer:** B) DNS sinkholing resolves blacklisted domains to a controlled IP, preventing communication with C2 servers.
*   **Distractor Analysis:**
    *   *Why correct:* DNS sinkholing resolves blacklisted domains to a controlled IP, preventing communication with C2 servers.
    *   It is a containment mechanism, not an optimization tool.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **firewall IP blocks**?
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
D) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **firewall IP blocks**.
    * *Why A is correct:* This describes the exact role and function of **firewall IP blocks**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **firewall IP blocks**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **firewall IP blocks**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
B) wireshark
A) openssl x509 -text -noout -in cert.pem
D) hydra -l admin -P passwords.txt ssh://target
C) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Threat Detection & Containment** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
D) Reboot the physical machine and wait for services to reload.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Threat Detection & Containment**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

