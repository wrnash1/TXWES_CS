# Quiz: Module 02 - Network Sec
## Course: CIS-4328_Information_Security (4328_Information_Security - CompTIA Security+ (SY0-701))

---

**Question 1**
An attacker sends a highly customized email specifically to the Chief Financial Officer (CFO) of a company, referencing a recent board meeting and asking them to click a link to review an urgent invoice. What type of social engineering attack is this?
A) Vishing
B) Whaling
C) Smishing
D) Pharming
*   **Correct Answer:** B) Whaling
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Vishing (Voice Phishing) relies on telephone calls, not email.
    *   *Why C is incorrect:* Smishing (SMS Phishing) relies on text messages, not email.
    *   *Why D is incorrect:* Pharming involves poisoning a DNS server to redirect legitimate traffic to a fake website; it is not a targeted email attack. Whaling is a form of spear-phishing specifically targeting high-level executives (the "big fish" or whales).

---

---

**Question 2**
A system administrator runs a tool against the corporate network. The tool actively attempts to bypass security controls, steal hashed passwords, and gain shell access to servers to prove that the network is insecure. Which of the following best describes this activity?
A) Vulnerability Scanning
B) Penetration Testing
C) Risk Assessment
D) Threat Hunting
*   **Correct Answer:** B) Penetration Testing
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Vulnerability scanning is passive and automated; it identifies potential weaknesses (like missing patches) but does *not* actively exploit them to steal data or gain access.
    *   *Why C is incorrect:* A risk assessment is an administrative process of identifying assets, threats, and risks on paper, not a technical exploitation of a network.
    *   *Why D is incorrect:* Threat hunting is the proactive searching through logs and systems to find hidden attackers that have already bypassed defenses; it is not the act of exploiting the network yourself.

---

---

**Question 3**
A systems administrator or developer needs to **launch the graphical packet analyzer to capture and dissect network frames in real-time**. Which of the following commands is the most appropriate to execute?
C) hydra -l admin -P passwords.txt ssh://target
B) openssl x509 -text -noout -in cert.pem
A) wireshark
D) nmap -sV -p 1-1024 target_ip
*   **Correct Answer:** A) wireshark
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `wireshark` command is directly designed to launch the graphical packet analyzer to capture and dissect network frames in real-time.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Network Sec** in a production environment, you encounter a system alert indicating a **IDS False Positives** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Generate a new Certificate Signing Request (CSR) and obtain an updated certificate from a trusted CA.
A) Tune the detection signatures and define exceptions for authorized administrative activities.
C) Review active security rules and add a permissive firewall rule allowing the specific source IP and destination port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Tune the detection signatures and define exceptions for authorized administrative activities.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why A is correct:* Because The network security system flags benign administrative scans or regular traffic patterns as malicious exploits. The appropriate fix is to Tune the detection signatures and define exceptions for authorized administrative activities..
    * *Why C is incorrect:* This action does not resolve the root cause of IDS False Positives.
    * *Why D is incorrect:* This action does not resolve the root cause of IDS False Positives.


---

**Question 5**
When designing a system for **Network Sec**, you must mitigate the risk of **Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Forward all system logs to a secure, write-once SIEM (Security Information and Event Management) platform.
A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Correct Answer:** A) Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC).
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why C is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why B is incorrect:* This does not address the security vulnerability of Weak Key Strength.
    * *Why A is correct:* Implementing Enforce RSA keys with a minimum length of 2048/4096 bits or switch to Elliptic Curve Cryptography (ECC). mitigates the risk of Attackers cracking weak encryption keys using commodity hardware, compromises confidentiality..

