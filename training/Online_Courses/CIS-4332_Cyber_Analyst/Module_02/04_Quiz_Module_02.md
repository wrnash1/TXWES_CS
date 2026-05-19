# Quiz: Module 02 - Vulnerability Management Lifecycle
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the first phase of the vulnerability management lifecycle?
*   A) Remediation
*   B) Prioritization
*   C) Identification
*   D) Verification
*   **Correct Answer:** C) You must identify vulnerabilities first (via scanning or assessment) before you can analyze or remediate them.
*   **Distractor Analysis:**
    *   *Why correct:* You must identify vulnerabilities first (via scanning or assessment) before you can analyze or remediate them.
    *   Identification is the initial step.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Analyze**?
B) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Analyze**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Analyze**.
    * *Why A is correct:* This describes the exact role and function of **Analyze**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Analyze**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
A) hydra -l admin -P passwords.txt ssh://target
B) nmap -sV -p 1-1024 target_ip
D) wireshark
C) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Vulnerability Management Lifecycle** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..


---

**Question 5**
When designing a system for **Vulnerability Management Lifecycle**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

