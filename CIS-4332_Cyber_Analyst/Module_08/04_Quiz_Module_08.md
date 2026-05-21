# Quiz: Module 08 - Incident Response – Detection and Triage
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the primary purpose of event correlation in a SIEM during the detection and triage phase of incident response?

*   A) Compressing and archiving log files to reduce storage costs on the SIEM appliance
*   B) Linking related events across multiple log sources to identify patterns that individually appear benign but together indicate an attack
*   C) Encrypting log data in transit between log sources and the central SIEM collector
*   D) Automatically patching vulnerabilities identified in endpoint scan results
*   **Correct Answer:** B) Linking related events across multiple log sources to identify patterns that individually appear benign but together indicate an attack.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Log compression and archiving are storage management functions; they are unrelated to the analytic purpose of event correlation, which is attack pattern detection.
    *   *Why B is correct:* SIEM correlation engines apply logical rules across disparate event streams — for example, five failed authentications followed by a successful login from the same IP is a brute-force success pattern that only becomes visible by correlating authentication log events over time. Correlation is the mechanism that transforms raw log noise into actionable security alerts.
    *   *Why C is incorrect:* Encrypting log data in transit (e.g., syslog over TLS) is a data-in-transit security control; it protects log confidentiality but is not what event correlation does.
    *   *Why D is incorrect:* Automated patching based on scan results is a vulnerability management function; it is separate from SIEM event correlation in the incident detection workflow.

---

**Question 2**
During alert triage, a SOC analyst reviews a SIEM alert for a port scan originating from an internal IP address. After investigation, the analyst determines the source is the authorized vulnerability scanner operated by the network security team, running on its scheduled weekly window. How should the analyst classify this alert?

*   A) True positive — the scan traffic is real and the alert correctly identifies scanning behavior, so it must be escalated as an active attack
*   B) False positive — the alert fired on legitimate, authorized activity; the detection is technically correct but the event is not malicious
*   C) False negative — the SIEM missed the detection entirely and the alert should be reviewed for detection gaps
*   D) True negative — no alert was generated and no malicious activity occurred, confirming the SIEM is working correctly
*   **Correct Answer:** B) False positive — the alert fired on legitimate, authorized activity; the detection is technically correct but the event is not malicious.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Classifying an authorized scanner as an active attack (true positive) would incorrectly escalate benign activity and waste analyst resources. The key distinction is whether the activity is malicious — authorized scans are not malicious even though they generate scan-like traffic.
    *   *Why B is correct:* A false positive occurs when an alert fires on real traffic but the underlying activity is not malicious. The SIEM rule correctly detected scanning behavior, but because the source is an authorized, scheduled scanner, it is a false positive that should be resolved by adding an exception for the scanner's IP address.
    *   *Why C is incorrect:* A false negative means detection was missed entirely — the opposite of the described scenario, where an alert was generated.
    *   *Why D is incorrect:* A true negative means no alert was generated and no attack occurred; the scenario describes a generated alert, which eliminates the true negative category.

---

**Question 3**
A Tier 1 SOC analyst is reviewing a SIEM alert: an internal workstation made three successful outbound connections to a known-malicious IP address listed in a current threat intelligence feed. The analyst confirms the destination IP is flagged as active C2 infrastructure. Which action should the analyst take next?

*   A) Close the alert as a false positive because the threat intelligence feed may contain outdated entries
*   B) Wait 24 hours to observe whether additional connections occur before taking any action
*   C) Escalate to Tier 2 with a structured escalation note documenting the affected host, IOC, connection timestamps, and recommended containment action
*   D) Reboot the affected workstation to terminate the active connections and clear any malicious processes from memory
*   **Correct Answer:** C) Escalate to Tier 2 with a structured escalation note documenting the affected host, IOC, connection timestamps, and recommended containment action.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Confirmed connections to known-malicious C2 infrastructure from a current threat feed represent a high-confidence true positive; closing it as a false positive without investigation would be a critical missed detection.
    *   *Why B is incorrect:* Waiting 24 hours while an active C2 connection is confirmed allows the attacker continued access; the incident response lifecycle requires prompt detection-to-containment action, not delayed observation.
    *   *Why C is correct:* An active confirmed C2 connection exceeds Tier 1 response authority. The correct action is immediate escalation to Tier 2 with a complete structured handoff note so that Tier 2 can take the appropriate containment action (EDR network isolation) without delay. This follows the NIST IR Detection and Analysis → Containment transition.
    *   *Why D is incorrect:* Rebooting the workstation destroys volatile memory evidence (running processes, open network connections, encryption keys) — this is the same shutdown trap tested across multiple CySA+ domains. The correct containment is EDR network isolation, not reboot.

---

**Question 4**
An organization's IR runbook requires that a Tier 1 analyst document the scope of a potential incident before escalation. A confirmed ransomware infection is found on a single workstation. The analyst checks lateral movement indicators and finds the ransomware's C2 domain was also queried by two servers and four other workstations in the past 48 hours. How should the analyst document the scope?

*   A) Scope: one workstation — only the initially confirmed infected system should be listed; additional systems require separate confirmed alerts before being included
*   B) Scope: seven systems (one confirmed infected workstation plus two servers and four workstations showing C2 domain queries) — all systems with IOC overlap should be included in the preliminary scope
*   C) Scope: the entire network — once ransomware is detected, all systems must be assumed compromised and listed in the scope until cleared
*   D) Scope: zero systems — the C2 domain queries may be false positives and scope should not be documented until every system is individually forensically confirmed
*   **Correct Answer:** B) Scope: seven systems (one confirmed infected workstation plus two servers and four workstations showing C2 domain queries) — all systems with IOC overlap should be included in the preliminary scope.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Limiting scope to only the initially confirmed system ignores the IOC pivot data already available. The C2 domain queries from the additional six systems are strong indicators of compromise that must be included in the preliminary scope for the Tier 2 investigation.
    *   *Why B is correct:* Effective IR scoping uses IOC pivoting — when the same C2 domain appears in DNS query logs across multiple systems, those systems are in-scope for the investigation even before full forensic confirmation. Including them in the preliminary scope ensures Tier 2 investigators check all potentially affected assets immediately.
    *   *Why C is incorrect:* Declaring the entire network in scope is operationally unworkable and unsupported by the available evidence. Scope should be evidence-driven, not assumed worst-case without data.
    *   *Why D is incorrect:* Refusing to document scope until full forensic confirmation of each system would delay containment of active ransomware propagation. Preliminary scope based on available IOC evidence is required; it is labeled as preliminary and updated as investigation proceeds.

---

**Question 5**
An organization wants to ensure its IR team can detect active intrusions within one hour of the initial compromise and classify them correctly during the triage phase. Which two controls together best achieve this goal?

*   A) Deploy full-disk encryption on all endpoints and require pre-boot authentication to prevent unauthorized access to system drives
*   B) Configure the SIEM with correlation rules for high-confidence IOC patterns (C2 beaconing, lateral movement, privilege escalation) and conduct quarterly tabletop exercises so analysts practice applying IR triage classification under realistic scenarios
*   C) Enforce application whitelisting on all endpoints and maintain a software inventory to track authorized applications
*   D) Implement a network access control (NAC) solution that blocks unmanaged devices from connecting to the corporate LAN
*   **Correct Answer:** B) Configure the SIEM with correlation rules for high-confidence IOC patterns (C2 beaconing, lateral movement, privilege escalation) and conduct quarterly tabletop exercises so analysts practice applying IR triage classification under realistic scenarios.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full-disk encryption and pre-boot authentication protect data confidentiality on stolen or powered-off devices; they do not contribute to real-time intrusion detection speed or analyst triage skill.
    *   *Why B is correct:* Detection speed depends on the SIEM having tuned correlation rules that surface high-confidence alerts quickly (reducing time-to-alert), and triage accuracy depends on analyst proficiency developed through regular tabletop exercises. Together these directly address both the detection timeline and classification accuracy objectives.
    *   *Why C is incorrect:* Application whitelisting reduces attack surface by limiting what can execute, but it does not improve the speed of detecting active intrusions already in progress or the analyst's ability to classify triage findings.
    *   *Why D is incorrect:* NAC prevents unauthorized devices from connecting but does not improve intrusion detection speed for attacks originating from already-connected managed endpoints — the most common attack vector.
