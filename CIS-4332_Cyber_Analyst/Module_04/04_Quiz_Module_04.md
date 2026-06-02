# Quiz: Module 04 - Log Analysis and SIEM Operations

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer. Review distractor analysis to reinforce understanding.

---

## Question 1

A SOC analyst observes the following Windows Security log pattern: 47 instances of Event ID 4625 for user "admin" from the same source IP address within a 3-minute window, followed immediately by one instance of Event ID 4624 for the same user from the same IP. What attack does this sequence most likely represent?

- A) A Pass-the-Hash attack using an NTLM credential hash
- B) A successful brute-force authentication attack
- C) A privilege escalation using a stolen Kerberos ticket
- D) An account enumeration scan with no successful compromise

Correct Answer: B

Distractor Analysis:

- A is incorrect. Pass-the-Hash involves using a stolen NTLM hash to authenticate without the plaintext password. It typically does not produce dozens of 4625 failures before success — hash authentication either works immediately or fails. The multiple 4625 failures before 4624 success is characteristic of brute-force, not PtH.
- B is correct. Multiple rapid 4625 (failed logon) events followed by a 4624 (successful logon) from the same source IP for the same user is the textbook signature of a brute-force attack that eventually succeeded.
- C is incorrect. Privilege escalation using a Kerberos ticket would appear in different event types (4768, 4769 for Kerberos ticket requests) and would not produce dozens of password failures.
- D is incorrect. Account enumeration would produce failures across multiple different usernames from one IP — not repeated failures for the same single username.

---

## Question 2

An analyst reviews Windows Event Log entries and finds multiple instances of Event ID 4648 from a workstation, with the TargetUser field showing a service account and the TargetHost field showing a financial database server. Which Windows Logon Type and ATT&CK technique does this pattern most directly suggest?

- A) Logon Type 2 (Interactive) — T1078 Valid Accounts
- B) Logon Type 3 (Network) — T1021 Remote Services
- C) Logon Type 10 (RemoteInteractive) — T1021.001 Remote Desktop Protocol
- D) Logon Type 3 (Network) using explicit credentials passed to a remote host — T1550.002 Pass the Hash

Correct Answer: D

Distractor Analysis:

- A is incorrect. Event ID 4648 (logon using explicit credentials) does not correspond to interactive local logons and would not produce Logon Type 2 events as a lateral movement indicator.
- B is incorrect. While lateral movement involves network logons (Type 3), Event ID 4648 specifically fires when explicit credentials are passed — distinct from normal network authentication. This specificity points toward credential abuse.
- C is incorrect. Logon Type 10 is RDP; Event ID 4648 is not the primary RDP indicator.
- D is correct. Event ID 4648 fires when a process or user presents explicit credentials (a specific username/password or hash) to authenticate to another system. Combined with network logon type and targeting a specific service account on a financial server, this pattern indicates credential-based lateral movement consistent with T1550.002 Pass the Hash.

---

## Question 3

An analyst is reviewing Apache web server access logs and observes the following pattern: 312 requests from a single IP address within 2 minutes, all returning HTTP 404 status codes, with the requested URLs appearing to be common CMS paths, backup file names, and configuration file names. What does this pattern indicate?

- A) A successful SQL injection attack exploiting the web application
- B) A denial-of-service attack targeting the web server's processing capacity
- C) Directory enumeration or web application scanning for accessible files and paths
- D) A cross-site scripting attack using malformed URL parameters

Correct Answer: C

Distractor Analysis:

- A is incorrect. SQL injection would manifest as requests with SQL syntax in parameters and would likely produce 500 errors (server errors from failed injection) rather than uniform 404s for non-existent paths.
- B is incorrect. A DoS attack would use high-volume requests causing service unavailability, typically producing 503 errors or connection failures. The pattern here is targeted path enumeration, not volume flooding.
- C is correct. Rapid requests to many different file and directory paths, all returning 404 (Not Found), is the signature of automated directory enumeration or vulnerability scanning. The scanner is probing for misconfigured files, backup archives, and CMS management interfaces that may be unintentionally accessible.
- D is incorrect. XSS attacks would appear as requests with JavaScript or HTML in URL parameters, not as 404 responses for distinct file paths.

---

## Question 4

A Sysmon Event ID 10 is logged on a Windows workstation. The TargetImage field contains "C:\Windows\System32\lsass.exe" and the SourceImage field contains "C:\Users\analyst\AppData\Temp\report_gen.exe". The GrantedAccess field shows 0x1010. What does this event most likely indicate?

- A) A legitimate antivirus process performing scheduled memory scanning
- B) An attempt to read LSASS process memory, likely to extract credential hashes
- C) Normal Windows Defender activity accessing the LSASS process for integrity checking
- D) A standard Windows update process accessing system security services

Correct Answer: B

Distractor Analysis:

- A is incorrect. Legitimate AV processes are typically signed, reside in Program Files directories, and are identifiable by their vendor name. A file in a user's AppData Temp directory is not a standard AV binary location.
- B is correct. Sysmon Event ID 10 logs process access requests. When an unknown process accesses lsass.exe (the Local Security Authority Subsystem Service) and requests memory-read access rights (0x1010 includes PROCESS_VM_READ), this is the signature of credential dumping tools like Mimikatz attempting to read credential material from LSASS memory. This maps to ATT&CK T1003.001.
- C is incorrect. Windows Defender uses its own signed binaries and does not access LSASS from user AppData directories.
- D is incorrect. Windows Update processes are signed Microsoft binaries in known system directories; they do not access LSASS memory from temp directories.

---

## Question 5

Which SIEM function converts log entries from diverse formats — Windows XML event logs, syslog text messages, JSON API events — into a unified schema with standardized field names?

- A) Correlation
- B) Normalization
- C) Enrichment
- D) Aggregation

Correct Answer: B

Distractor Analysis:

- A is incorrect. Correlation is the process of comparing multiple events according to defined rules to identify suspicious patterns. It operates on already-normalized data.
- B is correct. Normalization maps the varying field names and formats from different log sources to a common schema. For example, "src" from a firewall, "IpAddress" from Active Directory, and "client_ip" from a web server all become the same standardized field in the SIEM.
- C is incorrect. Enrichment adds additional context to log events — such as geolocation data for an IP address or asset information from the CMDB — but does not convert formats.
- D is incorrect. Aggregation combines multiple similar events into a single summary record (e.g., grouping 1,000 identical events into one record with a count). This reduces storage but is distinct from normalization.

---

## Question 6

An organization's SOC discovers that an attacker deleted all Windows Event Logs on a compromised server approximately 30 days before the breach was discovered. The SOC had been forwarding logs in real time to a centralized SIEM with a 90-day retention policy. What is the most accurate statement about the investigation?

- A) The investigation is impossible because the logs were deleted before discovery
- B) Logs for the 30 days after deletion are recoverable from the SIEM; logs for the period before deletion are lost
- C) All log evidence is preserved in the SIEM because real-time forwarding captured events before the attacker deleted local copies
- D) The SIEM only retains logs for the most recent 7 days regardless of policy settings

Correct Answer: C

Distractor Analysis:

- A is incorrect. This would be true if logs were stored only locally. Real-time forwarding to a SIEM means a remote copy was made before deletion occurred.
- B is incorrect. This reverses the situation. Events that occurred before the deletion were already forwarded to the SIEM. The SIEM copy persists regardless of what happens to local logs.
- C is correct. Real-time forwarding means each event is transmitted to the SIEM as it is generated. An attacker who deletes local log files removes only the local copy; the SIEM already has the forwarded events stored in its repository. With a 90-day retention policy, all events from the prior 90 days are available for investigation.
- D is incorrect. SIEM retention is configurable by the organization; 7-day retention is not a universal default.

---

## Question 7

A SOC analyst configures a SIEM correlation rule to fire an alert when a single source IP generates more than 15 failed SSH authentication events against any host within a 10-minute window. Under what circumstances would this rule produce a false positive?

- A) When an attacker successfully brutes-force a root password after 17 failed attempts
- B) When a legitimate monitoring agent performs scripted SSH health checks that occasionally fail due to timeout, generating 20 error events in a 10-minute window
- C) When an attacker uses a single IP to scan multiple SSH ports looking for open services
- D) When an internal backup server makes 8 failed SSH connection attempts

Correct Answer: B

Distractor Analysis:

- A is incorrect. An attacker successfully brute-forcing after 17 failures followed by a success is a true positive — the rule correctly detected malicious activity.
- B is correct. A false positive is a rule that fires on legitimate, authorized activity. A monitoring agent that generates error events during scripted health checks is not malicious, but if its error rate occasionally exceeds the threshold, the rule fires. This is legitimate activity incorrectly flagged — a false positive. The fix is to add an exception for the monitoring agent's IP or hostname.
- C is incorrect. A port scan for SSH services would not generate authentication events — it would generate connection attempts and possibly refused connections, not authentication failures. Even if it did, scanning activity is malicious and would represent a true positive.
- D is incorrect. 8 failed connections is below the 15-event threshold, so no alert would fire. This is a true negative — no malicious activity, no alert.

---

## Question 8

An analyst observes a pattern in the network log where an internal host (10.0.5.14) makes outbound HTTPS connections to the same external IP address (203.0.113.99) at intervals of exactly 300 seconds, repeated 48 times over the past four hours. What does this pattern indicate?

- A) A user browsing a frequently visited secure website
- B) Automated software update traffic from a patch management agent
- C) Beaconing behavior consistent with malware communicating with a command-and-control server
- D) A misconfigured NTP synchronization client sending repeated time requests

Correct Answer: C

Distractor Analysis:

- A is incorrect. Human browsing behavior is irregular — page loads happen at varying intervals based on user activity. Precisely regular 300-second intervals are not characteristic of human-driven traffic.
- B is incorrect. Legitimate patch management agents check for updates periodically but typically do not communicate at precise 300-second intervals and would connect to known vendor domains, not generic external IPs.
- C is correct. Malware that communicates with a C2 server typically uses a sleep timer between check-ins, producing highly regular connection intervals. Exactly 300 seconds (5 minutes) repeated 48 times over 4 hours is a textbook beaconing signature. This maps to ATT&CK T1071 Command and Control.
- D is incorrect. NTP uses UDP port 123, not HTTPS (TCP 443), and produces very brief, infrequent traffic — not 48 connections over 4 hours.

---

## Question 9

Which of the following log sources would provide the MOST useful evidence for reconstructing the specific commands an attacker executed on a compromised Windows workstation after gaining access?

- A) Windows Firewall log with connection details
- B) Active Directory authentication log with Event ID 4624 entries
- C) Windows Security Event Log Event ID 4688 with command-line auditing enabled, or Sysmon Event ID 1
- D) DHCP server lease log showing IP address assignments

Correct Answer: C

Distractor Analysis:

- A is incorrect. The Windows Firewall log records network connections (source/destination IPs and ports) but does not capture what commands were executed on the system.
- B is incorrect. Event ID 4624 records successful logon events and includes the logon type and source, but contains no information about what the authenticated user actually did after logging in.
- C is correct. Windows Security Event ID 4688 (when command-line auditing is enabled via Group Policy) records the full process command line for every process created. Sysmon Event ID 1 provides the same information with additional detail including the parent process. These are the primary sources for post-compromise command execution reconstruction.
- D is incorrect. DHCP logs record IP address assignments by MAC address and hostname. They provide no information about commands executed on a system.

---

## Question 10

An organization subject to PCI DSS is reviewing its log retention policy. The security manager proposes keeping all logs for 7 days online (immediately accessible) and deleting them after that. Which statement correctly identifies the compliance problem with this policy?

- A) PCI DSS does not regulate log retention; the policy is compliant as long as logs are encrypted
- B) PCI DSS requires a minimum of 12 months of log retention with at least the most recent 3 months immediately available
- C) PCI DSS requires logs to be kept for 7 years to align with financial record-keeping requirements
- D) PCI DSS only requires log retention for cardholder data environment systems, not all systems

Correct Answer: B

Distractor Analysis:

- A is incorrect. PCI DSS Requirement 10.5.1 specifically mandates log retention duration. Encryption is a separate requirement and does not substitute for retention duration compliance.
- B is correct. PCI DSS Requirement 10.5.1 requires that audit log history be retained for at least 12 months with a minimum of 3 months available for immediate analysis. A 7-day online retention policy with deletion after 7 days would fail both the 12-month total requirement and the 3-month immediate availability requirement.
- C is incorrect. Seven-year retention is associated with some financial accounting records (Sarbanes-Oxley) but is not the PCI DSS log retention standard.
- D is incorrect. PCI DSS log requirements apply across the cardholder data environment and systems that could impact CDE security. Limiting log retention only to specific systems may still fail the full scope of PCI DSS requirements.
