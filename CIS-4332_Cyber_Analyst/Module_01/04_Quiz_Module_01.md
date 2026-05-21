# Quiz: Module 01 - Security Operations & Analyst Role
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What does IOC stand for in security operations?
*   A) Index of Controls
*   B) Indicator of Compromise
*   C) Institution of Cybersecurity
*   D) Internal Operational Check
*   **Correct Answer:** B) Indicators of Compromise (IOCs) are forensic clues (file hashes, IPs, domains) that indicate a security breach.
*   **Distractor Analysis:**
    *   *Why correct:* Indicators of Compromise (IOCs) are forensic clues (file hashes, IPs, domains) that indicate a security breach.
    *   The other options are fabricated acronyms not used in security operations.

---

**Question 2**
In a SOC, which of the following best defines the **threat landscape**?
*   A) A SIEM dashboard view showing real-time firewall throughput statistics
*   B) The complete set of threat actors, attack vectors, and vulnerabilities relevant to an organization at a given time
*   C) A cryptographic method that uses a public key to encrypt data and a private key to decrypt it
*   D) The maximum acceptable downtime before business operations are critically impacted
*   **Correct Answer:** B) The complete set of threat actors, attack vectors, and vulnerabilities relevant to an organization at a given time.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A SIEM dashboard displays log data and alerts; it is a tool used to observe part of the threat landscape, not the landscape itself.
    *   *Why B is correct:* The threat landscape is the holistic picture of adversaries, techniques, and weaknesses facing an organization, which SOC analysts must continuously monitor.
    *   *Why C is incorrect:* This describes asymmetric (public-key) encryption, an unrelated cryptographic concept.
    *   *Why D is incorrect:* This describes Recovery Time Objective (RTO), a business continuity metric unrelated to threat landscape.

---

**Question 3**
A SOC analyst receives an alert showing multiple failed SSH login attempts from a single external IP address followed by a successful login. Which SOC analyst action is the most appropriate first step?
*   A) Immediately block the external IP address at the perimeter firewall
*   B) Verify whether the successful login matches an authorized user and correlate the source IP against threat intelligence feeds
*   C) Reimage the target system to ensure no persistent malware was installed
*   D) Close the alert as a false positive since the login eventually succeeded
*   **Correct Answer:** B) Verify whether the successful login matches an authorized user and correlate the source IP against threat intelligence feeds.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Blocking before verifying may interrupt legitimate business activity and skips the required triage step.
    *   *Why B is correct:* Triage requires confirming the alert is a true positive by checking user authorization and threat intelligence context before taking containment action.
    *   *Why C is incorrect:* Reimaging is a remediation action performed after confirmation and approval — not a first triage step.
    *   *Why D is incorrect:* A successful login after repeated failures is a classic brute-force success pattern and should never be dismissed without investigation.

---

**Question 4**
Which of the following best describes the role of a Tier 1 SOC analyst?
*   A) Leading threat hunting operations and developing custom SIEM detection rules
*   B) Performing initial alert triage, filtering false positives, and escalating confirmed incidents to Tier 2
*   C) Conducting post-incident forensic analysis and producing executive-level reports
*   D) Managing network infrastructure and applying security patches to production systems
*   **Correct Answer:** B) Performing initial alert triage, filtering false positives, and escalating confirmed incidents to Tier 2.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Threat hunting and custom rule development are Tier 3 or senior analyst responsibilities requiring deeper expertise.
    *   *Why B is correct:* Tier 1 analysts are the first responders — they monitor the alert queue, apply playbooks, determine if an alert is real, and hand off confirmed incidents.
    *   *Why C is incorrect:* Forensic analysis and executive reporting are Tier 2/3 and management responsibilities.
    *   *Why D is incorrect:* Infrastructure management and patching are IT operations roles, not SOC analyst duties.

---

**Question 5**
When designing a monitoring strategy for a SOC, which control best mitigates the risk of an attacker deleting local system logs after a breach to conceal their activity?
*   A) Enforce multi-factor authentication on all privileged accounts
*   B) Forward all system logs in real time to a centralized, write-protected SIEM platform
*   C) Enable full-disk encryption on all endpoint systems
*   D) Deploy a host-based intrusion prevention system on every workstation
*   **Correct Answer:** B) Forward all system logs in real time to a centralized, write-protected SIEM platform.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* MFA protects against unauthorized account access but does not prevent an already-authenticated attacker from deleting local logs.
    *   *Why B is correct:* Centralizing logs to an immutable SIEM ensures that even if local logs are deleted, the off-system copy remains intact for investigation.
    *   *Why C is incorrect:* Full-disk encryption protects data confidentiality at rest but does not prevent a logged-in user or attacker from deleting log files.
    *   *Why D is incorrect:* HIPS can block some malicious actions but does not guarantee log preservation; a privileged attacker can often disable or bypass host-based controls.

