# Quiz: Module 02 - Threat Intelligence – MITRE ATT&CK and CTI
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
    *   Identification is the initial step; the remaining options represent later phases of the lifecycle.

---

**Question 2**
In a SOC context, which of the following most accurately defines the **MITRE ATT&CK framework**?
*   A) A vendor-specific endpoint detection product that automatically blocks known malware signatures on Windows hosts
*   B) A community-maintained knowledge base of adversary tactics, techniques, and procedures (TTPs) used to map attacker behaviors and guide detection engineering
*   C) A cryptographic protocol that authenticates email senders using public key infrastructure and DNS records
*   D) A regulatory compliance framework that specifies annual penetration testing requirements for financial institutions
*   **Correct Answer:** B) A community-maintained knowledge base of adversary tactics, techniques, and procedures (TTPs) used to map attacker behaviors and guide detection engineering.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ATT&CK is a knowledge base and mapping framework, not a product — it does not block malware or run on endpoints.
    *   *Why B is correct:* MITRE ATT&CK catalogs real-world adversary behaviors organized by tactic (the goal) and technique (the method), enabling analysts to identify detection gaps and map alerts to specific attacker actions.
    *   *Why C is incorrect:* This describes DKIM (DomainKeys Identified Mail), an email authentication technology.
    *   *Why D is incorrect:* ATT&CK is not a compliance standard; it has no mandatory requirements and is used operationally, not for regulatory audits.

---

**Question 3**
A threat analyst is reviewing an alert showing that an attacker used PowerShell to download and execute a payload from a remote server. Which MITRE ATT&CK tactic does this behavior most directly represent?
*   A) Initial Access — the attacker is gaining first entry to the environment
*   B) Exfiltration — the attacker is transferring data out of the network
*   C) Execution — the attacker is running malicious code on a compromised system
*   D) Discovery — the attacker is enumerating network resources and user accounts
*   **Correct Answer:** C) Execution — the attacker is running malicious code on a compromised system.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Initial Access covers techniques used to gain the first foothold (e.g., phishing, exploiting public-facing applications); PowerShell execution occurs after access is established.
    *   *Why B is incorrect:* Exfiltration involves transferring collected data outside the network; downloading and running a payload is not data theft.
    *   *Why C is correct:* Execution (TA0002) covers techniques that result in attacker-controlled code running on a local or remote system; PowerShell scripting (T1059.001) is a canonical Execution technique.
    *   *Why D is incorrect:* Discovery techniques involve the attacker learning about the environment (e.g., account enumeration, network scanning); downloading a payload is an Execution action.

---

**Question 4**
An analyst receives a threat intelligence report containing a JSON object with type "indicator" and a pattern field containing an IP address. The report was delivered automatically over HTTPS from a partner organization's sharing server. Which two standards are being used?
*   A) OpenIOC for the data format and Syslog for the transport
*   B) STIX for the data format and TAXII for the transport
*   C) CVSS for the data format and REST API for the transport
*   D) YARA for the data format and TLP for the transport
*   **Correct Answer:** B) STIX for the data format and TAXII for the transport.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* OpenIOC is an older XML-based format and Syslog is a log forwarding protocol; neither is the current standard for structured CTI sharing.
    *   *Why B is correct:* STIX 2.1 defines the JSON schema for CTI objects (indicators, attack-patterns, threat-actors), and TAXII is the HTTPS-based server/client protocol used to deliver those objects between organizations.
    *   *Why C is incorrect:* CVSS measures vulnerability severity and is unrelated to threat intelligence object formatting or transport.
    *   *Why D is incorrect:* YARA is a pattern-matching rule language for malware detection; TLP (Traffic Light Protocol) is a data-sharing classification scheme, not a transport protocol.

---

**Question 5**
A SOC team wants to ensure that if an attacker compromises a host and deletes local Windows Event Logs, the evidence is still available for investigation. Which control best addresses this risk?
*   A) Deploy application whitelisting on all endpoints to prevent unauthorized processes from running
*   B) Forward Windows Event Logs in real time to a centralized, tamper-protected SIEM platform
*   C) Enable full-disk encryption on all endpoint systems using BitLocker
*   D) Require multi-factor authentication for all remote desktop protocol (RDP) connections
*   **Correct Answer:** B) Forward Windows Event Logs in real time to a centralized, tamper-protected SIEM platform.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Application whitelisting restricts execution but does not protect log data from deletion by an already-running privileged process.
    *   *Why B is correct:* Centralizing logs to a write-protected SIEM ensures log integrity even if local copies are wiped; the attacker cannot reach the off-host copy.
    *   *Why C is incorrect:* Disk encryption protects data confidentiality at rest but does not prevent an authenticated attacker from deleting log files on a running system.
    *   *Why D is incorrect:* MFA on RDP reduces unauthorized remote access but does not protect log integrity after a host is already compromised.

