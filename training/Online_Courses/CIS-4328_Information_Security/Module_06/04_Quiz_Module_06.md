# Quiz: Module 06 - PKI
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **CSR (Certificate Signing Request)**?
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
C) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **CSR (Certificate Signing Request)**.
    * *Why A is correct:* This describes the exact role and function of **CSR (Certificate Signing Request)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **CSR (Certificate Signing Request)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **CSR (Certificate Signing Request)**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **CSR (Certificate Signing Request)**?
C) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
D) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
B) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **CSR (Certificate Signing Request)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **CSR (Certificate Signing Request)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **CSR (Certificate Signing Request)**.
    * *Why A is correct:* This describes the exact role and function of **CSR (Certificate Signing Request)**.


---

**Question 3**
A systems administrator or developer needs to **display the detailed metadata and validation parameters of an SSL/TLS digital certificate**. Which of the following commands is the most appropriate to execute?
A) openssl x509 -text -noout -in cert.pem
B) nmap -sV -p 1-1024 target_ip
C) hydra -l admin -P passwords.txt ssh://target
D) wireshark
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    * *Why A is correct:* The `openssl x509 -text -noout -in cert.pem` command is directly designed to display the detailed metadata and validation parameters of an SSL/TLS digital certificate.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **PKI** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
C) Tune the detection signatures and define exceptions for authorized administrative activities.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **PKI**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

