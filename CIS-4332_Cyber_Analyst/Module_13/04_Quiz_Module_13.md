# Quiz: Module 13 - Forensics & Evidence Collection
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which data source should be collected FIRST during forensic collection due to its volatility?
*   A) HDD storage
*   B) CPU Registers and RAM
*   C) Log files on disk
*   D) Print server spool queue
*   **Correct Answer:** B) Memory and processor state volatile data is lost immediately on shutdown, placing them first in the order of volatility.
*   **Distractor Analysis:**
    *   *Why correct:* Memory and processor state volatile data is lost immediately on shutdown, placing them first in the order of volatility.
    *   Disk storage can survive power loss.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **write blockers**?
D) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
B) A social engineering attack where malicious actors send fraudulent messages designed to trick victims into revealing sensitive information.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **write blockers**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **write blockers**.
    * *Why A is correct:* This describes the exact role and function of **write blockers**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **write blockers**.


---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
D) hydra -l admin -P passwords.txt ssh://target
B) nmap -sV -p 1-1024 target_ip
C) openssl x509 -text -noout -in cert.pem
A) wireshark
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.


---

**Question 4**
While working on **Forensics & Evidence Collection** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..


---

**Question 5**
When designing a system for **Forensics & Evidence Collection**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
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

