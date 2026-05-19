# Quiz: Module 06 - Social Engineering Attacks
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What is a phishing attack that specifically targets high-profile corporate executives (such as CEOs or CFOs) called?
*   A) Spear-phishing
*   B) Whaling
*   C) Vishing
*   D) Smishing
*   **Correct Answer:** B) Whaling is a sub-class of phishing designed specifically to target high-ranking executive personnel.
*   **Distractor Analysis:**
    *   *Why correct:* Whaling is a sub-class of phishing designed specifically to target high-ranking executive personnel.
    *   Spear-phishing targets any specific individual. Vishing is voice. Smishing is SMS.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **spear-phishing vs whaling.**?
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
C) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
D) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within security operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **spear-phishing vs whaling.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **spear-phishing vs whaling.**.
    * *Why A is correct:* This describes the exact role and function of **spear-phishing vs whaling.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **spear-phishing vs whaling.**.


---

**Question 3**
A systems administrator or developer needs to **scan ports on a target host to identify active services and their version numbers**. Which of the following commands is the most appropriate to execute?
B) wireshark
D) hydra -l admin -P passwords.txt ssh://target
A) nmap -sV -p 1-1024 target_ip
C) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) nmap -sV -p 1-1024 target_ip
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nmap -sV -p 1-1024 target_ip` command is directly designed to scan ports on a target host to identify active services and their version numbers.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Social Engineering Attacks** in a production environment, you encounter a system alert indicating a **Firewall Blocking Valid Traffic** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Tune the detection signatures and define exceptions for authorized administrative activities.
A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
C) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
*   **Correct Answer:** A) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why A is correct:* Because The default-deny firewall rule is blocking a newly deployed service that has not been whitelisted. The appropriate fix is to Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port..
    * *Why D is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.
    * *Why C is incorrect:* This action does not resolve the root cause of Firewall Blocking Valid Traffic.


---

**Question 5**
When designing a system for **Social Engineering Attacks**, you must mitigate the risk of **Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why A is correct:* Implementing Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform. mitigates the risk of Intruders deleting local system event logs after a breach to hide their tracks and prevent investigation..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Centralized Logs.

