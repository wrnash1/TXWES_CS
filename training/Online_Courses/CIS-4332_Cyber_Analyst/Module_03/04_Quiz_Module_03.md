# Quiz: Module 03 - Infrastructure Scanning Tools
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which type of scan provides the most accurate view of patch levels and installed software on a target host?
*   A) Non-credentialed scan
*   B) Credentialed scan
*   C) Passive network sniff
*   D) Stealth SYN scan
*   **Correct Answer:** B) Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.
*   **Distractor Analysis:**
    *   *Why correct:* Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.
    *   Non-credentialed scans can only analyze open network ports and banners.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Network vulnerability scanners**?
B) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
D) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Network vulnerability scanners**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Network vulnerability scanners**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Network vulnerability scanners**.
    * *Why A is correct:* This describes the exact role and function of **Network vulnerability scanners**.


---

**Question 3**
A systems administrator or developer needs to **run a dictionary brute-force attack against the target SSH service to test credential strength**. Which of the following commands is the most appropriate to execute?
D) openssl x509 -text -noout -in cert.pem
C) wireshark
B) nmap -sV -p 1-1024 target_ip
A) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `hydra -l admin -P passwords.txt ssh://target` command is directly designed to run a dictionary brute-force attack against the target SSH service to test credential strength.


---

**Question 4**
While working on **Infrastructure Scanning Tools** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Infrastructure Scanning Tools**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.

