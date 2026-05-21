# Quiz: Module 14 - Threat Hunting Methodologies
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the primary purpose of DNS sinkholing in threat hunting and incident containment?

*   A) Speeding up DNS resolution for internal hosts by caching frequently requested domain records on a local resolver
*   B) Redirecting queries for known-malicious domains to a controlled internal IP address — severing C2 communication and identifying which internal hosts are infected by observing which systems query the sinkholed domain
*   C) Encrypting all DNS query traffic between internal resolvers and external root servers to prevent DNS eavesdropping
*   D) Shutting down the organization's primary DNS server to prevent all external name resolution during an active incident
*   **Correct Answer:** B) Redirecting queries for known-malicious domains to a controlled internal IP address — severing C2 communication and identifying which internal hosts are infected by observing which systems query the sinkholed domain.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Caching for performance is a standard DNS resolver function; it has nothing to do with threat containment or malicious domain redirection. DNS sinkholing is a security control, not a performance optimization.
    *   *Why B is correct:* A DNS sinkhole resolves blacklisted C2 domains to an internal controlled IP (e.g., `127.0.0.1` or a monitored sensor). This simultaneously cuts the infected host's communication path to the C2 server (containment) and generates observable traffic to the sinkhole address that reveals exactly which internal hosts are compromised (threat identification). Both capabilities make it a high-value threat hunting and IR tool.
    *   *Why C is incorrect:* Encrypting DNS traffic between resolvers and root servers describes DNS over HTTPS (DoH) or DNS over TLS (DoT) — privacy and integrity controls, not containment techniques.
    *   *Why D is incorrect:* Shutting down the DNS server would cause complete internal name resolution failure — a self-inflicted denial of service. DNS sinkholing targets specific malicious domains, not all DNS service.

---

**Question 2**
In threat hunting, which of the following most accurately defines **hypothesis-driven hunting**?

*   A) Responding to a SIEM alert that has fired on a known-malicious IP address by investigating the affected host and escalating if the alert is confirmed as a true positive
*   B) A structured approach in which the hunter formulates a specific, testable assumption about attacker behavior — typically based on threat intelligence or ATT&CK techniques — then queries available data sources to confirm or refute it
*   C) Running automated vulnerability scans against all production systems on a weekly schedule to identify new CVEs before attackers can exploit them
*   D) Reviewing threat intelligence reports from external feeds and ingesting the listed IOCs into the SIEM for automated correlation against future log events
*   **Correct Answer:** B) A structured approach in which the hunter formulates a specific, testable assumption about attacker behavior — typically based on threat intelligence or ATT&CK techniques — then queries available data sources to confirm or refute it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Responding to a fired SIEM alert is reactive alert triage — it begins with a detection event, not a proactive hypothesis. Hypothesis-driven hunting begins before any alert fires, under the assumption that adversaries may already be present.
    *   *Why B is correct:* Hypothesis-driven hunting starts with a structured question such as "Based on recent threat intelligence about this threat actor group, they may be using T1059.001 PowerShell execution in our environment — let me hunt for encoded PowerShell commands in endpoint logs from the past 30 days." The hunt produces a documented result regardless of outcome, improving future detection capability even when nothing is found.
    *   *Why C is incorrect:* Automated vulnerability scanning is a vulnerability management activity; it looks for exploitable weaknesses in systems, not for adversary activity already present in the environment.
    *   *Why D is incorrect:* Ingesting IOCs into the SIEM for automated correlation is a reactive threat intelligence integration task; it depends on future alerts firing when IOCs match, rather than proactively searching for existing adversary activity.

---

**Question 3**
A threat hunter forms the following hypothesis: "Based on recent threat actor TTPs for our industry, attackers may have established persistence using scheduled tasks created outside business hours." Which MITRE ATT&CK technique and Windows event log data source should the hunter use to test this hypothesis?

*   A) ATT&CK T1078 (Valid Accounts) — query Windows Security Event Log for Event ID 4624 (successful logon) events outside business hours
*   B) ATT&CK T1053.005 (Scheduled Task/Job) — query Windows Security Event Log for Event ID 4698 (scheduled task created) events filtered to after-hours timestamps and non-standard task names
*   C) ATT&CK T1071 (Application Layer Protocol) — query network proxy logs for outbound HTTP/HTTPS connections to domains with high entropy names
*   D) ATT&CK T1003 (OS Credential Dumping) — query Windows Security Event Log for Event ID 4688 (process creation) events involving lsass.exe as the target process
*   **Correct Answer:** B) ATT&CK T1053.005 (Scheduled Task/Job) — query Windows Security Event Log for Event ID 4698 (scheduled task created) events filtered to after-hours timestamps and non-standard task names.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* T1078 (Valid Accounts) addresses credential reuse and account compromise; Event ID 4624 (logon events) would test for unauthorized logins, not for scheduled task persistence. The hypothesis is specifically about persistence via scheduled tasks.
    *   *Why B is correct:* T1053.005 is the ATT&CK sub-technique for Windows Scheduled Task persistence. Event ID 4698 records the creation of a new scheduled task, including the task name, command, creator, and timestamp. Filtering to after-hours creation timestamps and excluding known legitimate task names directly tests whether the persistence hypothesis is true.
    *   *Why C is incorrect:* T1071 (Application Layer Protocol) is a C2 communication technique; querying proxy logs for high-entropy domain names tests for C2 beaconing, not scheduled task persistence.
    *   *Why D is incorrect:* T1003 (OS Credential Dumping) targets lsass.exe process access for credential extraction; it is a different ATT&CK technique and data source unrelated to the scheduled task persistence hypothesis.

---

**Question 4**
During a threat hunt, an analyst queries DNS query logs and finds that 14 internal workstations have queried a domain that was registered three days ago, uses a DGA-like name pattern, and resolves to an IP address flagged in a current threat intelligence feed. No SIEM alerts have fired for any of these hosts. What does the absence of SIEM alerts indicate, and what should the analyst do next?

*   A) The absence of alerts confirms these are false positives — the threat intelligence feed must be outdated and the domains are legitimate; no further action is needed
*   B) The absence of alerts indicates the automated detection rules did not cover this specific C2 domain, demonstrating the value of proactive threat hunting; the analyst should escalate all 14 hosts as potentially compromised for Tier 2 investigation and EDR isolation
*   C) The absence of alerts means the workstations are protected and the threat hunting query returned an incorrect result; the query should be re-run against a different data source to confirm
*   D) The absence of SIEM alerts indicates the 14 workstations are honeypots intentionally configured to attract attacker traffic; no incident response action is required
*   **Correct Answer:** B) The absence of alerts indicates the automated detection rules did not cover this specific C2 domain, demonstrating the value of proactive threat hunting; the analyst should escalate all 14 hosts as potentially compromised for Tier 2 investigation and EDR isolation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The absence of SIEM alerts does not indicate the activity is benign — it indicates the detection rules missed it. A recently registered domain with a DGA-like name pattern resolving to a threat-intel-flagged IP is a high-confidence compromise indicator regardless of whether a SIEM rule fired.
    *   *Why B is correct:* This scenario perfectly illustrates the value of threat hunting: 14 hosts are exhibiting C2-like behavior that no automated rule detected. The hunter's proactive DNS log query surfaced the activity. The correct next step is immediate escalation — all 14 hosts are in scope for investigation and isolation — and the hunt finding should be used to create a new SIEM detection rule for this domain pattern going forward.
    *   *Why C is incorrect:* The query result is consistent and supported by threat intelligence correlation; there is no basis for assuming the query is incorrect. Dismissing valid hunt findings because no alert fired would negate the entire value of threat hunting.
    *   *Why D is incorrect:* There is no indication these workstations are honeypots; treating real compromised production hosts as honeypots would leave 14 active C2-connected systems uncontained.

---

**Question 5**
An organization wants to improve its ability to detect adversary activity that bypasses signature-based SIEM rules. Which two controls together best address this capability gap?

*   A) Deploy full-disk encryption on all endpoints and require pre-boot authentication to prevent unauthorized access to powered-off systems
*   B) Establish a dedicated threat hunting program where analysts use MITRE ATT&CK as a hypothesis framework to proactively hunt through endpoint, DNS, and network logs weekly — and implement DNS sinkholing for all known-malicious C2 domains in current threat intelligence feeds to identify infected hosts that have not triggered alerts
*   C) Increase the SIEM storage retention period from 90 days to 365 days to enable longer historical lookback for retrospective investigations
*   D) Enforce application whitelisting on all endpoints using AppLocker to block execution of any binary not in the approved software inventory
*   **Correct Answer:** B) Establish a dedicated threat hunting program using ATT&CK hypotheses to proactively hunt through endpoint, DNS, and network logs — and implement DNS sinkholing for known-malicious C2 domains to identify infected hosts that have not triggered alerts.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full-disk encryption and pre-boot authentication protect offline data confidentiality; they have no effect on detecting active adversary activity already present on running, authenticated systems.
    *   *Why B is correct:* Signature-based SIEM rules only detect what they are programmed to detect — novel or slightly modified attack techniques evade them. A threat hunting program proactively searches for attacker behaviors that rules miss, using ATT&CK as a guide for what to hunt. DNS sinkholing adds a passive identification layer that surfaces C2-connected hosts without requiring a detection rule for each specific domain. Together these directly address the gap between automated detection capability and real adversary activity.
    *   *Why C is incorrect:* Extended log retention improves retrospective investigation capability after a compromise is discovered — it is a forensic lookback enabler, not a real-time detection improvement for evading adversaries.
    *   *Why D is incorrect:* Application whitelisting reduces the attack surface by limiting what can execute, which is valuable — but it is a preventive control, not a detection control. It does not find adversaries already operating inside the environment using whitelisted LOLBins.
