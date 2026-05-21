# Quiz: Module 13 - Digital Forensics and Threat Intelligence
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A forensic investigator arrives at the scene of a suspected insider threat incident. The suspect's workstation is still powered on and running. The investigator needs to collect evidence before shutting down the machine. According to the order of volatility, which data source should be collected FIRST?
A) The contents of the local hard drive, including deleted files and unallocated space.
B) The contents of system RAM, including running processes, open network connections, and decryption keys loaded in memory.
C) The system's event logs stored in the Windows Event Viewer on disk.
D) Archived backup tapes held in the organization's offsite storage facility.
*   **Correct Answer:** B) The contents of system RAM, including running processes, open network connections, and decryption keys loaded in memory.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hard drive data is persistent — it survives a system shutdown and can be collected after RAM is captured. Collecting disk before RAM wastes the opportunity to recover highly volatile in-memory evidence that will be permanently lost when the machine is powered off.
    *   *Why C is incorrect:* Event logs stored on disk are non-volatile — they persist after shutdown. While important evidence, they are significantly less volatile than RAM contents and should be collected after memory acquisition.
    *   *Why D is incorrect:* Offsite backup tapes are the least volatile evidence source in the order of volatility — they are durable, persistent, and will not be lost regardless of what happens to the live system. They should be collected last.

---

---

**Question 2**
A forensic analyst is preparing to image the hard drive from a compromised server for legal proceedings. Before connecting the drive to the forensic workstation, the analyst attaches a hardware device between the drive and the workstation. After imaging is complete, the analyst computes SHA-256 hashes of both the original drive and the forensic image and confirms they match. What is the purpose of the hardware device used during imaging?
A) To accelerate the imaging process by providing a dedicated processing channel between the drive and the workstation.
B) To prevent the forensic workstation from writing any data to the original evidence drive, preserving its integrity.
C) To encrypt the forensic image as it is created, protecting evidence confidentiality during transfer.
D) To automatically verify the hash of each sector as it is copied to detect read errors during acquisition.
*   **Correct Answer:** B) To prevent the forensic workstation from writing any data to the original evidence drive, preserving its integrity.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A write blocker does not accelerate the imaging process — it is a passive or active hardware device that intercepts write commands and discards them, leaving only read operations to proceed. Speed is not its function.
    *   *Why C is incorrect:* Write blockers do not perform encryption — they are evidence integrity tools, not confidentiality tools. Encryption of the forensic image is handled separately by the imaging software or storage solution.
    *   *Why D is incorrect:* While some forensic imaging tools do perform sector-level hash verification, that is a software function of the imaging application — not the function of the write blocker hardware device. The write blocker's sole purpose is preventing writes to the original media.

---

---

**Question 3**
A threat intelligence analyst is reviewing a report from a commercial feed that describes a nation-state group's attack campaign. The report includes details about the group's initial access techniques (spear phishing with malicious attachments), persistence mechanisms (registry run key modifications), and lateral movement methods (Pass-the-Hash). The analyst wants to map these behaviors to a standardized framework to identify which defensive controls are missing. Which framework is designed for this purpose?
A) NIST Cybersecurity Framework (CSF)
B) MITRE ATT&CK Framework
C) ISO/IEC 27001
D) OWASP Top 10
*   **Correct Answer:** B) MITRE ATT&CK Framework
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The NIST Cybersecurity Framework provides a high-level organizational structure for managing cybersecurity risk across five functions (Identify, Protect, Detect, Respond, Recover) — it does not catalog specific adversary tactics and techniques that can be mapped to observed attack behaviors.
    *   *Why C is incorrect:* ISO/IEC 27001 is an international standard for information security management systems (ISMS) — it defines requirements for establishing and maintaining an ISMS program but does not provide a technique-level catalog of adversary behaviors for threat mapping.
    *   *Why D is incorrect:* The OWASP Top 10 lists the most critical web application security risks (SQL injection, XSS, insecure deserialization, etc.) — it is scoped to web application vulnerabilities and does not cover the full range of adversary TTPs described in the scenario.

---

**Question 4**
An organization wants to automatically receive and ingest structured threat intelligence from multiple external partners and government sharing programs in a machine-readable format. The security team specifies that the intelligence must be described in a standardized language and delivered via a standardized transport protocol so their SIEM can consume it automatically. Which combination of standards meets this requirement?
A) STIX for describing the threat intelligence data; TAXII for transporting it between organizations.
B) TAXII for describing the threat intelligence data; STIX for transporting it between organizations.
C) MITRE ATT&CK for describing threat data; CVSS for scoring and transporting vulnerability severity.
D) OpenIOC for describing indicators; SMTP for delivering threat reports via email.
*   **Correct Answer:** A) STIX for describing the threat intelligence data; TAXII for transporting it between organizations.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* This reverses the roles. STIX (Structured Threat Information eXpression) is the data format/language used to describe threat intelligence. TAXII (Trusted Automated eXchange of Intelligence Information) is the transport protocol used to share that data. Swapping them is a common exam trap.
    *   *Why C is incorrect:* MITRE ATT&CK is a knowledge base for mapping adversary behaviors to techniques — it is not a machine-readable transport format for automated intelligence ingestion. CVSS (Common Vulnerability Scoring System) scores software vulnerability severity and does not transport threat intelligence.
    *   *Why D is incorrect:* OpenIOC is a legacy indicator format developed by Mandiant that is not the current standard for automated SIEM ingestion. SMTP is an email delivery protocol — it is not a structured, automated machine-to-machine threat intelligence transport mechanism.

---

**Question 5**
A security analyst is performing proactive threat hunting in the enterprise environment. The analyst hypothesizes that an attacker may have established persistence using a scheduled task that runs a PowerShell script from an unusual directory. The analyst queries the EDR platform for scheduled tasks created in the past 30 days that execute PowerShell from non-standard paths. No SIEM alert was triggered for this activity. What distinguishes threat hunting from standard security monitoring in this scenario?
A) Threat hunting uses different tools than SIEM-based monitoring, so it can detect attacks that SIEM cannot.
B) Threat hunting is a reactive process triggered by a security alert, while monitoring is proactive.
C) Threat hunting is a proactive, hypothesis-driven search for adversary activity that has evaded automated detection, rather than waiting for an alert to be generated.
D) Threat hunting only applies to nation-state attacks; standard monitoring handles commodity malware.
*   **Correct Answer:** C) Threat hunting is a proactive, hypothesis-driven search for adversary activity that has evaded automated detection, rather than waiting for an alert to be generated.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Threat hunters often use the same platforms (EDR, SIEM, packet capture) as standard monitoring — the distinction is not the toolset but the approach. Hunters query and pivot through data guided by a hypothesis rather than waiting for automated rules to fire.
    *   *Why B is incorrect:* This reverses the definitions. Standard monitoring (SIEM alerting) is reactive — it responds to triggered alerts. Threat hunting is proactive — the analyst initiates the search based on intelligence and hypotheses before any alert exists.
    *   *Why D is incorrect:* Threat hunting is applied across all threat categories — commodity malware, insider threats, and nation-state actors. The defining characteristic is the proactive, hypothesis-driven methodology, not the threat actor classification.
