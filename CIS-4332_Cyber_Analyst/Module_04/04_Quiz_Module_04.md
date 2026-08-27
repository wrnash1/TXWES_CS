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

---

## Question 11 (5 points)

An analyst reviewing Windows Security Event logs sees Event ID 4625 (failed logon) entries for the same username appearing 200 times in 3 minutes, all from the same source IP, with Logon Type 3 (network). What attack pattern does this most likely indicate?

- A) Pass-the-hash
- B) Remote brute-force or credential stuffing against a network share or service
- C) Local privilege escalation
- D) Kerberoasting

Correct Answer: B

Distractor Analysis:

- A is incorrect. Pass-the-hash uses a captured NTLM hash to authenticate without a password. It typically produces a single successful authentication event, not hundreds of failures. Pass-the-hash attacks do not generate high-volume 4625 events.
- B is correct. Logon Type 3 indicates a network logon (e.g., to a file share or network service). Two hundred failed attempts in 3 minutes from one source IP against one username is a clear brute-force or credential stuffing pattern over the network.
- C is incorrect. Local privilege escalation would produce Event IDs related to token manipulation, privilege use, or service installation — not high-volume remote network logon failures.
- D is incorrect. Kerberoasting involves requesting service tickets for service principal names and cracking them offline. It does not generate large numbers of 4625 failures against a single username from a single IP.

---

## Question 12 (5 points)

An analyst reads the following Linux syslog entry: `Nov 14 03:22:11 webserver sshd[2847]: Accepted publickey for deploy from 10.10.1.5 port 52341 ssh2`. Which field confirms this was a successful authentication using a cryptographic key rather than a password?

- A) The port number 52341
- B) The word "Accepted" combined with the method "publickey"
- C) The timestamp 03:22:11
- D) The process ID 2847

Correct Answer: B

Distractor Analysis:

- A is incorrect. Port 52341 is the source (ephemeral) port on the connecting client — it identifies the connection but provides no information about the authentication method used.
- B is correct. The keyword "Accepted" confirms the authentication was successful. The method "publickey" identifies that SSH public key authentication was used rather than password-based authentication. These two fields together answer both whether authentication succeeded and how.
- C is incorrect. The timestamp records when the event occurred. It contains no information about authentication method or success/failure status.
- D is incorrect. The process ID identifies which sshd process handled the connection — it is a system artifact, not an authentication outcome indicator.

---

## Question 13 (5 points)

A SIEM correlation rule generates an alert when a user account produces more than 5 failed logins within 10 minutes followed by a successful login. The rule uses a time window of 10 minutes and groups events by username. An analyst reviews the alert and finds 8 failed logins and 1 successful login for user jsmith between 14:02 and 14:09. What should the analyst examine next to determine if this is a true positive?

- A) The SIEM's disk usage to verify log storage capacity
- B) The source IP addresses of the failed and successful logins to determine whether they are the same or different, and whether the successful login source is authorized
- C) The total number of other users who triggered the same rule in the same time window
- D) The SIEM vendor's documentation to confirm the correlation rule syntax is correct

Correct Answer: B

Distractor Analysis:

- A is incorrect. Disk usage is an infrastructure concern unrelated to determining whether this specific alert represents a real attack.
- B is correct. The critical investigative question is whether the successful login came from the same IP as the failed attempts (suggesting the attacker succeeded) or a different IP (potentially a coincidental user lockout followed by legitimate access). The source IP of the successful login and whether it is an authorized address are the most important next investigative steps.
- C is incorrect. How many other users triggered the rule is relevant for understanding potential noise levels but does not help classify this specific alert as real or false.
- D is incorrect. Rule syntax verification is a rule development activity, not an alert investigation step. The rule fired correctly — the investigation is about the underlying event, not the rule.

---

## Question 14 (5 points)

Which Windows Event ID records a user or process requesting the use of a sensitive privilege such as SeDebugPrivilege or SeBackupPrivilege?

- A) Event ID 4648
- B) Event ID 4672
- C) Event ID 4698
- D) Event ID 4776

Correct Answer: B

Distractor Analysis:

- A is incorrect. Event ID 4648 records an explicit credential logon — a process authenticating using different credentials than the currently logged-in user. It is relevant for detecting pass-the-hash and lateral movement but not privilege use.
- B is correct. Event ID 4672 (Special Logon) is generated when an account with one or more sensitive or administrator-equivalent privileges logs on. Security analysts monitor this event to detect accounts using high-value privileges that could indicate privilege escalation or abuse.
- C is incorrect. Event ID 4698 records the creation of a scheduled task — an important persistence detection event but unrelated to privilege use.
- D is incorrect. Event ID 4776 records NTLM credential validation attempts against the local SAM database — an authentication event, not a privilege use event.

---

## Question 15 (5 points)

An analyst is writing a Splunk SPL query to find DNS queries for newly registered domains (registered within the last 7 days) from internal hosts. Which Splunk command extracts the queried domain from DNS log events and counts how many unique internal hosts queried each domain?

- A) `index=dns | stats count by src_ip | sort -count`
- B) `index=dns | rex field=query "(?P<domain>[^.]+\.[^.]+$)" | stats dc(src_ip) as unique_hosts by domain | where unique_hosts > 1`
- C) `index=dns | table _time, src_ip, query, response_ip`
- D) `index=dns | eval domain=lower(query) | dedup domain`

Correct Answer: B

Distractor Analysis:

- A is incorrect. This query counts events per source IP — it does not extract domain names or count unique hosts per domain. It answers a different question (which host generated the most DNS queries).
- B is correct. This query uses `rex` to extract the registered domain from the query field, then uses `stats dc(src_ip)` (distinct count) to count how many unique internal hosts queried each domain. The `where` clause filters to domains queried by more than one host, which is relevant for detecting spreading malware communicating with a C2 domain.
- C is incorrect. `table` returns raw rows formatted as a readable table — it does not aggregate, count, or filter for suspicious patterns. It is useful for manual review but is not a detection query.
- D is incorrect. `dedup domain` returns one row per unique domain but does not aggregate host counts. `eval domain=lower(query)` normalizes case but does not produce a meaningful detection output on its own.

---

## Question 16 (5 points)

A SOC analyst notices that the SIEM has not received any logs from WEBSERVER-PROD-01 for the past 4 hours. The server is confirmed to be online and accessible. What is the most security-relevant interpretation of this log gap?

- A) The server is operating normally; log collection gaps of several hours are expected and do not require investigation
- B) A log forwarding agent failure, network configuration change, or attacker action (such as stopping the log agent) may be causing the gap — this should be treated as a potential security event requiring immediate investigation
- C) The SIEM is malfunctioning and all alerts from the past 4 hours should be discarded
- D) The server's security posture has improved because fewer log events means fewer suspicious activities

Correct Answer: B

Distractor Analysis:

- A is incorrect. Log collection gaps are not normal expected behavior and should never be ignored. An unexplained gap on a production server is a potential indicator of attacker activity, misconfigurations, or agent tampering.
- B is correct. A 4-hour log gap on an online server is a high-priority investigation item. Attackers frequently disable or stop log forwarding agents as part of defense evasion. The gap should be investigated immediately by checking the log agent status, network connectivity, and local log files on the server for signs of tampering.
- C is incorrect. A gap in one server's logs does not indicate SIEM malfunction — other sources continue logging normally. Discarding alerts would be dangerous.
- D is incorrect. Fewer log events do not indicate improved security posture. They indicate reduced visibility, which is dangerous.

---

## Question 17 (5 points)

Which Sysmon Event ID is most useful for detecting process injection — the technique where an attacker writes and executes code inside another process's memory space?

- A) Event ID 1 (Process Create)
- B) Event ID 3 (Network Connection)
- C) Event ID 8 (CreateRemoteThread)
- D) Event ID 11 (File Create)

Correct Answer: C

Distractor Analysis:

- A is incorrect. Sysmon Event ID 1 (Process Create) records when a new process is started. Process injection does not create a new process — it runs code inside an existing one. Event ID 1 will not capture the injection itself.
- B is incorrect. Sysmon Event ID 3 (Network Connection) records outbound network connections from processes. It can help identify post-injection C2 communication but does not detect the injection act itself.
- C is correct. Sysmon Event ID 8 (CreateRemoteThread) fires when a thread is created in another process's memory space. CreateRemoteThread is the primary Windows API call used in classic process injection techniques. Monitoring for Event ID 8 with unexpected source/target process combinations is a high-value detection approach.
- D is incorrect. Sysmon Event ID 11 (File Create) records file system write operations. It is useful for detecting file drops but does not capture in-memory injection activity.

---

## Question 18 (5 points)

A web server access log shows a series of HTTP GET requests to `/admin/config.php?cmd=cat+/etc/passwd`. What type of attack does this log entry most likely indicate?

- A) SQL injection
- B) Remote code execution via command injection through a URL parameter
- C) Cross-site scripting (XSS)
- D) Directory traversal

Correct Answer: B

Distractor Analysis:

- A is incorrect. SQL injection injects SQL syntax (e.g., `' OR 1=1--`) into database query inputs. The `cmd=cat+/etc/passwd` pattern uses OS shell command syntax, not SQL.
- B is correct. The `cmd=` parameter attempts to pass a shell command (`cat /etc/passwd`) to a PHP script that appears to be executing system commands from URL parameters. This is a command injection attack — the attacker is attempting to execute OS commands through a vulnerable web application parameter.
- C is incorrect. XSS injects JavaScript into pages rendered in other users' browsers. The pattern here does not include JavaScript syntax and targets server-side command execution, not client-side script injection.
- D is incorrect. Directory traversal uses path sequences (`../`) to navigate outside the web root to access restricted files. This request uses a command parameter, not path traversal sequences.

---

## Question 19 (5 points)

An analyst is reviewing firewall logs and finds repeated outbound connections from an internal host to an external IP on port 4444 every 60 seconds for the past 8 hours. No legitimate business application uses port 4444 and the external IP is not in approved network documentation. What does this traffic pattern most likely indicate?

- A) Normal Windows Update traffic that uses dynamic port assignments
- B) A beacon — automated, regularly timed callback from malware on the internal host to a command-and-control server
- C) A legitimate load-balancing heartbeat between internal servers
- D) Outbound DNS resolution queries that happen to use a non-standard port

Correct Answer: B

Distractor Analysis:

- A is incorrect. Windows Update uses HTTP/HTTPS on ports 80 and 443 to Microsoft-owned infrastructure. It does not use port 4444 or contact unknown external IPs at regular 60-second intervals.
- B is correct. Regularly timed, periodic outbound connections to an unknown external IP on a non-standard port over an 8-hour period is the textbook signature of C2 beaconing. The 60-second interval suggests the malware's callback timer. Port 4444 is commonly associated with Meterpreter and other post-exploitation frameworks.
- C is incorrect. Load-balancing heartbeats are internal traffic between known infrastructure components. They do not originate from endpoints and do not traverse the perimeter to external IPs.
- D is incorrect. DNS uses UDP/TCP port 53. DNS over non-standard ports does exist (DNS-over-HTTPS uses 443) but the 60-second exact interval and unknown external IP make DNS resolution an implausible explanation.

---

## Question 20 (5 points)

A SIEM analyst wants to reduce alert fatigue caused by a correlation rule that fires too often on legitimate activity. Which approach is the most appropriate and professionally sound tuning action?

- A) Delete the correlation rule entirely to stop the false positives
- B) Add an exception for known legitimate source IPs, asset groups, or user accounts that consistently trigger the rule for authorized reasons, and document the exception with a business justification
- C) Raise the alert severity from Medium to Low so analysts can ignore it more easily
- D) Increase the detection threshold so high that the rule only fires on statistically impossible event volumes

Correct Answer: B

Distractor Analysis:

- A is incorrect. Deleting a correlation rule eliminates both the false positives and all true positive detections the rule would have generated. Deletion is only appropriate if the rule provides zero detection value and cannot be tuned.
- B is correct. Adding documented exceptions for known-good sources (specific authorized IPs, service accounts, maintenance windows) reduces false positive volume while preserving the rule's ability to detect the same activity from unknown or unauthorized sources. Documentation provides an audit trail for the tuning decision.
- C is incorrect. Changing severity does not reduce alert volume — analysts still see the same number of alerts. It trains analysts to ignore a category of alerts, which creates blind spots and analyst complacency.
- D is incorrect. Setting the threshold so high that the rule only fires on impossible event volumes effectively disables the rule's detection capability for realistic attack scenarios.
