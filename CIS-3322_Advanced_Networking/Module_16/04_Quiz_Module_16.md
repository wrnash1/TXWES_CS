# Quiz: Module 16 - Final Exam Prep & Cisco CCNA 200-301 Certification
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which CCNA 200-301 exam domain carries the highest percentage weighting?
*   A) Network Fundamentals (20%)
*   B) Security Fundamentals (15%)
*   C) IP Connectivity (25%)
*   D) Network Access (20%)
*   **Correct Answer:** C) IP Connectivity (25%) is the highest-weighted domain, covering static routing, OSPFv2, and IPv6 routing.
*   **Distractor Analysis:**
    *   *Why correct:* IP Connectivity covers static routing, OSPF, and IPv6 routing — the largest single domain at 25%.
    *   Network Fundamentals and Network Access are each 20%. Security Fundamentals is 15%.

---

**Question 2**
Which of the following most accurately describes the **CCNA 200-301 exam format**?
*   A) A 120-minute exam with approximately 100–120 questions in multiple-choice, drag-and-drop, fill-in-the-blank, and simulation formats, requiring a score of 825/1000 to pass.
*   B) A two-part exam requiring separate written and hands-on lab components — the written exam tests theory while the lab exam requires configuring a live Cisco network at a Cisco testing facility.
*   C) An open-book exam allowing candidates to reference Cisco documentation and IOS command references during the test, with a 180-minute time limit and 50 scenario-based questions.
*   D) A 90-minute adaptive exam where correct answers unlock progressively harder questions, and each candidate must score above 700 on three consecutive attempts to receive certification.
*   **Correct Answer:** A) A 120-minute exam with approximately 100–120 questions in multiple-choice, drag-and-drop, fill-in-the-blank, and simulation formats, requiring a score of 825/1000 to pass.
*   **Distractor Analysis:**
    * *Why A is correct:* These are the accurate CCNA 200-301 exam parameters. The 825/1000 passing threshold and 120-minute duration are official Cisco values.
    * *Why B is incorrect:* The CCNA 200-301 is a single exam — it does not have a separate hands-on lab component (unlike higher-level certifications such as CCIE).
    * *Why C is incorrect:* The CCNA exam is closed-book — no external references are permitted. The time limit is 120, not 180 minutes.
    * *Why D is incorrect:* While the CCNA uses computer-adaptive testing elements, there is no multi-attempt passing threshold or "700 on three attempts" requirement.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
B) traceroute
D) nslookup
C) ping
A) netstat -ano
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.


---

**Question 4**
While reviewing for the **CCNA 200-301 Final Exam**, you encounter a scenario indicating a **DNS Failure** error on a network host. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
For the **CCNA 200-301 Final Exam**, you must demonstrate knowledge of mitigating the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Configure SNMPv3 with authentication and privacy (authPriv) to ensure all SNMP network management polling is encrypted.
D) Enable AAA (Authentication, Authorization, and Accounting) with RADIUS to centralize credential management and audit all management access attempts.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH and HTTPS directly encrypt management session credentials in transit, preventing their capture by a packet sniffer — the most direct defense against the described threat.
    * *Why B is incorrect:* Port Security restricts physical switch port access by MAC address — it does not encrypt management credentials transmitted over the network.
    * *Why C is incorrect:* SNMPv3 authPriv encrypts SNMP polling traffic specifically, but does not address Telnet or HTTP credential exposure during interactive management sessions.
    * *Why D is incorrect:* AAA with RADIUS centralizes authentication and adds auditing, but if Telnet is still permitted, credentials are still transmitted in plaintext before reaching the RADIUS server.
