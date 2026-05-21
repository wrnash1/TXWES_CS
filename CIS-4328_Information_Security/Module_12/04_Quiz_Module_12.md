# Quiz: Module 12 - Incident Response
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A security analyst receives a SIEM alert at 2:00 AM indicating that a workstation is making outbound connections to a known command-and-control server IP address. The analyst confirms the connection is real and that the workstation is likely compromised. The analyst immediately disconnects the workstation from the network. Which phase of the NIST incident response lifecycle does this action belong to?
A) Preparation
B) Detection and Analysis
C) Containment, Eradication, and Recovery
D) Post-Incident Activity
*   **Correct Answer:** C) Containment, Eradication, and Recovery
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Preparation occurs before any incident — it encompasses building IR policies, playbooks, and tools. Once an incident is confirmed and active, the team has moved past the Preparation phase.
    *   *Why B is incorrect:* Detection and Analysis is the phase where the analyst reviews the SIEM alert and determines whether the event is a genuine incident. Disconnecting the workstation is the response action that follows confirmation — it is a containment action, not an analysis action.
    *   *Why D is incorrect:* Post-Incident Activity occurs after the incident is fully resolved — it involves lessons-learned reviews and updating controls. The incident is still active in this scenario.

---

---

**Question 2**
After containing a ransomware infection on three servers, the IR team is preparing to wipe and rebuild the affected systems. Before performing the rebuild, the team lead insists on creating forensic disk images of the infected servers. What is the PRIMARY reason for imaging the systems before eradication?
A) To save time by avoiding the need to reconfigure the servers from scratch after the rebuild.
B) To preserve evidence for forensic investigation, legal proceedings, and root-cause analysis before destroying the affected systems.
C) To transfer the ransomware to an isolated lab environment for malware analysis using the live infected images.
D) To satisfy the backup retention policy, which requires a snapshot before any system changes are made.
*   **Correct Answer:** B) To preserve evidence for forensic investigation, legal proceedings, and root-cause analysis before destroying the affected systems.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Forensic imaging captures the infected disk state — it is not a configuration backup and cannot be used to restore a clean system. Rebuilding still requires clean installation media and configuration management, not the forensic image.
    *   *Why C is incorrect:* While malware analysis in an isolated lab is a valid technique, it is performed using a copy of the image in a controlled environment — it is not the primary reason for imaging before eradication. The primary reason is evidence preservation.
    *   *Why D is incorrect:* Backup retention policies govern recovery-oriented snapshots of clean system states — forensic imaging of an actively infected system is a security investigation procedure, not a backup compliance action.

---

---

**Question 3**
A threat hunter reviewing network logs identifies the following pattern: a single endpoint has made 47 outbound DNS queries for randomly generated domain names (e.g., x7k2m.attacker.com, p9q3n.attacker.com) over the past hour. No user was active on the workstation during this time. Which type of malicious activity does this traffic pattern most likely indicate?
A) A password spraying attack against the domain controller
B) Domain generation algorithm (DGA) beaconing by malware communicating with a command-and-control server
C) A DNS amplification DDoS attack originating from the endpoint
D) A port scan being conducted by a network discovery tool
*   **Correct Answer:** B) Domain generation algorithm (DGA) beaconing by malware communicating with a command-and-control server
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Password spraying involves authentication attempts against login services (LDAP, Kerberos, web forms) — it does not generate DNS queries for randomly generated external domain names.
    *   *Why C is incorrect:* A DNS amplification attack sends small DNS queries with a spoofed victim IP to open DNS resolvers to generate large response traffic toward the victim — the attacker's endpoint would be the source of spoofed requests, not the endpoint making sequential queries for unique random subdomains.
    *   *Why D is incorrect:* Port scanning (e.g., nmap) generates TCP/UDP connection attempts to target IP addresses across many ports — it does not produce a pattern of sequential DNS queries for algorithmically generated domain names.

---

**Question 4**
An organization's incident response team has successfully removed ransomware from infected systems, restored data from clean backups, and returned all systems to normal operation. The CISO asks the team to document what happened, identify how the attacker gained initial access, and recommend three specific control improvements to prevent recurrence. Which NIST IR phase does this task represent?
A) Preparation
B) Detection and Analysis
C) Containment, Eradication, and Recovery
D) Post-Incident Activity (Lessons Learned)
*   **Correct Answer:** D) Post-Incident Activity (Lessons Learned)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Preparation is the phase before incidents occur — it involves building IR capability. The task described occurs after the incident is fully resolved, making it a post-incident activity, not preparation.
    *   *Why B is incorrect:* Detection and Analysis involves identifying and confirming the incident during its active phase — the incident is already resolved in this scenario.
    *   *Why C is incorrect:* Containment, Eradication, and Recovery are the active response actions during the incident — removing the ransomware and restoring backups was this phase. The CISO's request for documentation and control improvement recommendations comes after recovery is complete.

---

**Question 5**
A security operations center (SOC) team wants to automate their response to phishing alerts. When the SIEM generates a phishing alert, they want the system to automatically pull the email headers, query threat intelligence feeds for the sender IP, sandbox any attachments, and isolate the affected user's mailbox — all without requiring manual analyst intervention for each alert. Which technology category is designed to enable this type of automated IR workflow?
A) Security Information and Event Management (SIEM)
B) Security Orchestration, Automation, and Response (SOAR)
C) Endpoint Detection and Response (EDR)
D) Data Loss Prevention (DLP)
*   **Correct Answer:** B) Security Orchestration, Automation, and Response (SOAR)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A SIEM aggregates logs and generates alerts based on correlation rules — it detects the phishing event and triggers the alert, but it does not execute automated multi-step response workflows across different security tools. That orchestration capability is provided by SOAR.
    *   *Why C is incorrect:* EDR monitors endpoint activity, detects malicious behavior on devices, and can isolate individual endpoints — it is an endpoint-focused tool and does not orchestrate cross-tool workflows involving email analysis, threat intelligence lookups, and mailbox isolation.
    *   *Why D is incorrect:* DLP monitors and prevents the unauthorized transfer of sensitive data — it enforces data handling policies but does not perform incident response automation or coordinate actions across multiple security tools in response to an alert.
