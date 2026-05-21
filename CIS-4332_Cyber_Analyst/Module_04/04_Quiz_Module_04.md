# Quiz: Module 04 - Log Analysis and SIEM Operations
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which CVSS metric group represents the characteristics of a vulnerability that are constant over time and across environments?
*   A) Base Metric Group
*   B) Temporal Metric Group
*   C) Environmental Metric Group
*   D) Local Metric Group
*   **Correct Answer:** A) Base metrics represent the core qualities of the vulnerability that do not change.
*   **Distractor Analysis:**
    *   *Why correct:* Base metrics represent intrinsic, unchanging characteristics of a vulnerability such as attack vector, attack complexity, and impact scope.
    *   Temporal metrics change over time as exploits and patches emerge. Environmental metrics reflect the specific local context of the organization.

---

**Question 2**
In a SIEM context, which of the following most accurately defines **SIEM dashboards**?
*   A) Firewall rule sets that automatically block traffic matching known malicious signatures in real time
*   B) Visual interfaces in a SIEM platform that aggregate security metrics, alert trends, and event data to give analysts situational awareness across monitored systems
*   C) Encrypted tunnels that forward raw log data from endpoints to a centralized log aggregation server
*   D) Automated playbooks that execute containment actions such as account lockouts when a correlation rule fires
*   **Correct Answer:** B) Visual interfaces in a SIEM platform that aggregate security metrics, alert trends, and event data to give analysts situational awareness across monitored systems.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Blocking traffic based on signatures is the function of an IPS, not a SIEM dashboard; a SIEM detects and alerts but does not block.
    *   *Why B is correct:* SIEM dashboards provide real-time visual summaries of alert volumes, top event sources, geographic activity, and severity breakdowns — enabling analysts to prioritize investigations during a shift.
    *   *Why C is incorrect:* Encrypted log forwarding describes a log transport mechanism (e.g., syslog-ng with TLS), not a SIEM dashboard function.
    *   *Why D is incorrect:* Automated playbooks that take containment actions describe SOAR (Security Orchestration, Automation, and Response) functionality, which is separate from SIEM dashboards.

---

**Question 3**
A SOC analyst is investigating a potential brute-force attack on a Linux SSH server. Which log file and command should the analyst query first to identify failed authentication attempts?
*   A) `grep 'Failed password' /var/log/auth.log` — searches the Linux authentication log for failed SSH login entries
*   B) `cat /var/log/syslog | grep ERROR` — searches the general system log for error-level messages
*   C) `tail -f /var/log/apache2/access.log` — streams the latest entries from the Apache web server access log
*   D) `journalctl -u nginx` — retrieves log entries for the nginx web service from systemd journal
*   **Correct Answer:** A) `grep 'Failed password' /var/log/auth.log` — searches the Linux authentication log for failed SSH login entries.
*   **Distractor Analysis:**
    *   *Why A is correct:* `/var/log/auth.log` records all authentication events on Linux systems including SSH login attempts; the string "Failed password" appears for each unsuccessful credential submission, making this the direct data source for brute-force investigation.
    *   *Why B is incorrect:* `/var/log/syslog` is a general system log that captures many event types; while SSH events may appear there on some distributions, `auth.log` is the authoritative source for authentication-specific events.
    *   *Why C is incorrect:* The Apache access log records HTTP web requests, not SSH authentication events.
    *   *Why D is incorrect:* `journalctl -u nginx` retrieves nginx web server logs; these are unrelated to SSH authentication failures.

---

**Question 4**
A SIEM correlation rule is generating hundreds of alerts per day for a known administrative scanning tool used by the network team. Which action best resolves this without reducing overall detection coverage?
*   A) Delete the correlation rule entirely to eliminate the false positives
*   B) Add an exception to the rule that excludes the network team's authorized scanner IP addresses and document the change
*   C) Increase the correlation rule threshold to require 10,000 events before firing instead of the current setting
*   D) Disable all network scanning across the organization to prevent the alerts from occurring
*   **Correct Answer:** B) Add an exception to the rule that excludes the network team's authorized scanner IP addresses and document the change.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting the rule removes detection coverage for genuine attacks using the same pattern; tuning is always preferable to removal.
    *   *Why B is correct:* Adding an IP-based exception for authorized scanners suppresses known-good activity while preserving the rule's ability to fire on identical behavior from unauthorized sources — this is standard SIEM tuning practice.
    *   *Why C is incorrect:* Raising the threshold to an unrealistic value effectively disables the rule for real attack scenarios and does not address the root cause of authorized scanner noise.
    *   *Why D is incorrect:* Disabling authorized scanning removes a critical security monitoring capability; the SIEM rule should be tuned, not the business process removed.

---

**Question 5**
An organization wants to ensure that if an attacker compromises a server and attempts to clear the local event logs, the activity is still detectable. Which two controls together best achieve this goal?
*   A) Enable full-disk encryption and require smart card authentication for all administrators
*   B) Forward logs in real time to a centralized write-protected SIEM, and create a correlation rule that alerts when the Windows Security Event Log is cleared (Event ID 1102)
*   C) Deploy an antivirus solution and run daily vulnerability scans against all servers
*   D) Implement network segmentation and restrict outbound traffic using firewall ACLs
*   **Correct Answer:** B) Forward logs in real time to a centralized write-protected SIEM, and create a correlation rule that alerts when the Windows Security Event Log is cleared (Event ID 1102).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disk encryption and smart card auth address access control and data-at-rest confidentiality; neither preserves log integrity after a system is already compromised.
    *   *Why B is correct:* Real-time log forwarding to an immutable SIEM preserves evidence even if local logs are deleted, and a correlation rule on Event ID 1102 (audit log cleared) provides an immediate alert when the deletion occurs — combining prevention of evidence loss with active detection.
    *   *Why C is incorrect:* Antivirus and vulnerability scanning address malware and patch management; they do not preserve or protect log data from deletion.
    *   *Why D is incorrect:* Network segmentation and firewall ACLs limit lateral movement and exfiltration; they do not protect local log integrity after host compromise.

