# Quiz: Module 15 — Security Operations

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. This quiz is aligned to SY0-701 Domain 4 — Security Operations (28%).

---

### Question 1

A SOC analyst notices that 92% of daily alerts are automatically closed without investigation because they match known false positive patterns. The remaining 8% are routed to analysts. Which term best describes the technology performing this automated triage and routing?

- A) SIEM
- B) SOAR
- C) EDR
- D) CASB

Correct Answer: B

Explanation: SOAR executes automated playbooks that triage, enrich, and route alerts without human intervention. The SIEM generates the alerts; the SOAR acts on them. EDR focuses on endpoint detection; CASB governs cloud application access.

---

### Question 2

A production database server has a critical CVSS 9.8 vulnerability. The vendor patch requires a four-hour maintenance window unavailable for 12 days. Which is the BEST immediate action?

- A) Accept the risk and schedule the patch for the next available window
- B) Take the server offline until the patch can be applied
- C) Implement compensating controls such as network segmentation and enhanced monitoring
- D) Escalate to the vendor and wait for an emergency patch

Correct Answer: C

Explanation: When patching cannot occur immediately, compensating controls reduce exposure. Network segmentation limits lateral movement; IPS signatures can detect exploitation attempts. Accepting risk without mitigation (A) is inappropriate for CVSS 9.8. Taking the server offline (B) may not be feasible for a production system.

---

### Question 3

Which of the following BEST describes the difference between a credentialed and an uncredentialed vulnerability scan?

- A) Credentialed scans run from inside the network; uncredentialed scans run from outside
- B) Credentialed scans authenticate to each target and inspect local configuration; uncredentialed scans test only network-accessible services
- C) Credentialed scans use active probing; uncredentialed scans use passive traffic analysis
- D) Credentialed scans are faster because they skip port discovery

Correct Answer: B

Explanation: The key distinction is authentication. A credentialed scan logs into the target and inspects installed software, patch levels, and local configuration. An uncredentialed scan can only probe network-accessible services, producing more false negatives.

---

### Question 4

Which metric measures the elapsed time between when an attack begins and when the SOC first identifies it as a real incident?

- A) MTTR
- B) False positive rate
- C) MTTD
- D) Patch compliance rate

Correct Answer: C

Explanation: Mean Time to Detect (MTTD) measures the time from incident occurrence to SOC detection. MTTR measures time from detection to containment — that clock starts after MTTD ends.

---

### Question 5

An organization wants a free, publicly available standard to define minimum security configurations for every new Windows Server before production deployment. Which resource is MOST appropriate?

- A) DISA STIG for Windows Server
- B) CIS Benchmark for Windows Server
- C) NIST SP 800-53 control catalog
- D) ISO/IEC 27001 Annex A

Correct Answer: B

Explanation: CIS Benchmarks are free, publicly downloadable hardening guides for commercial organizations. DISA STIGs are valid but intended for DoD environments. NIST SP 800-53 and ISO 27001 Annex A are control frameworks, not system-specific hardening guides.

---

### Question 6

An investigation reveals a production server was modified outside change control three weeks ago, disabling a key log source. Which control would have MOST effectively prevented this?

- A) Mandatory CAB approval for all production changes
- B) Automated patch deployment using WSUS
- C) Weekly vulnerability scanning
- D) SIEM alert correlation rules

Correct Answer: A

Explanation: The Change Advisory Board (CAB) review requires all production changes to be formally requested, reviewed, and approved before implementation. Vulnerability scanning detects weaknesses but would not block an unauthorized administrative change.

---

### Question 7

A security manager reports a 97% critical patch compliance rate within 72 hours and a 94% security awareness training completion rate. What type of metrics are these?

- A) Key Risk Indicators (KRIs)
- B) Key Performance Indicators (KPIs)
- C) Vulnerability metrics
- D) Incident metrics

Correct Answer: B

Explanation: KPIs measure how well the security program performs its intended functions. KRIs measure current risk exposure — for example, number of unpatched critical CVEs open right now.

---

### Question 8

A SIEM collects logs from 47 systems using different date formats, field names, and severity labels. Before correlation rules can be applied, the SIEM must perform which process?

- A) Log compression
- B) Log encryption
- C) Log normalization
- D) Log archiving

Correct Answer: C

Explanation: Log normalization converts heterogeneous log data into a consistent format so the SIEM can compare and correlate events across sources. Without normalization, a firewall deny event cannot be meaningfully correlated with a Windows failed login event.

---

### Question 9

Critical patches must be deployed within 72 hours per policy. A critical Apache vulnerability published 96 hours ago is still unpatched because CAB approval took too long. What is the BEST resolution to prevent this conflict in the future?

- A) Eliminate change control for security patches entirely
- B) Define critical security patches as a pre-approved standard change type
- C) Extend the critical patch SLA to 14 days
- D) Deploy patches directly to production without testing

Correct Answer: B

Explanation: Standard changes are pre-approved for well-understood, low-risk procedures. Classifying critical patch deployment as a standard change eliminates individual CAB review bottlenecks while maintaining documentation. Eliminating change control entirely (A) removes the audit trail. Extending the SLA (C) increases exposure.

---

### Question 10

A SOC team's MTTD has remained at 18 hours despite new SIEM hardware. Investigation reveals correlation rules are 14 months old and alerts from critical systems are suppressed by an outdated filter. Which action MOST directly reduces MTTD?

- A) Purchase a SOAR platform to automate response
- B) Hire additional Tier 1 analysts
- C) Update SIEM correlation rules and remove outdated suppression filters
- D) Increase vulnerability scanning frequency to daily

Correct Answer: C

Explanation: MTTD reflects detection speed. Outdated rules and suppressed alerts mean the SIEM cannot detect modern attack patterns promptly. Updating rules and removing filters directly improves detection coverage. SOAR reduces MTTR, not MTTD. More analysts cannot detect incidents the SIEM never alerts on.

---

---

### Question 11 (5 points)

A SOC analyst reviews SIEM logs and finds the following sequence on a single workstation within a 12-minute window: 847 failed authentication events against the domain controller, followed by one successful authentication, followed by the execution of `net user /add` and `net localgroup administrators` commands. Which kill chain stage does the successful authentication and command execution represent?

- A) Reconnaissance
- B) Delivery
- C) Exploitation
- D) Actions on Objectives

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Reconnaissance is the pre-attack information gathering phase (scanning for open ports, identifying targets, researching employees). The attacker has already moved well past reconnaissance by the time they are executing commands inside a compromised system.
- Why B is incorrect: Delivery is the stage where the attacker transmits a weapon to the target environment (phishing email, malicious USB, drive-by download). Command execution on an already-compromised workstation is not the delivery stage.
- Why C is incorrect: Exploitation refers to triggering the vulnerability — in this case, the brute-force attack succeeding and achieving the initial foothold. The subsequent commands creating a new admin account represent the attacker using that foothold to achieve their objective (persistence and privilege escalation), which is Actions on Objectives.

---

### Question 12 (5 points)

A vulnerability scanner reports a finding: "SSL/TLS server supports 3DES cipher suite (CVE-2016-2183, CVSS 7.5)." The system is a legacy inventory management application that cannot be patched because the vendor went out of business three years ago. The application runs on an isolated internal VLAN with no internet connectivity. Which is the MOST appropriate risk response?

- A) Accept the risk and document the decision, noting the compensating controls (network isolation) already in place and the absence of internet exposure
- B) Immediately take the application offline until 3DES is disabled
- C) Upgrade the server's TLS library and disable 3DES
- D) Escalate to the vendor for an emergency patch

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: Taking the application offline eliminates a business function when the risk is already substantially reduced by compensating controls. Risk avoidance is appropriate when no treatment can reduce residual risk to tolerance — but network isolation of an internal legacy application with no internet exposure is a legitimate compensating control that may bring residual risk within acceptance threshold.
- Why C is incorrect: The question states the vendor went out of business and patching is not possible. Attempting to modify the TLS library of an unsupported legacy application without vendor support risks breaking the application entirely.
- Why D is incorrect: The vendor no longer exists. Escalating to a non-existent vendor is not a viable risk treatment action.

---

### Question 13 (5 points)

A security team implements a configuration baseline for all new Windows Server deployments using a CIS Benchmark Level 1 profile. Six months later, a routine integrity check finds that 23 servers have configurations that no longer match the approved baseline. What is the term for this condition, and what tool category is specifically designed to detect it?

- A) Configuration drift; detected by a file integrity monitoring or security configuration management tool
- B) Vulnerability regression; detected by a web application firewall
- C) Patch gap; detected by a vulnerability scanner
- D) Compliance deviation; detected by a SOAR playbook

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: Vulnerability regression refers to a previously remediated vulnerability reappearing after a change. Drift is the broader term for any deviation from an approved baseline state, regardless of whether a specific vulnerability is introduced.
- Why C is incorrect: A patch gap is specifically the absence of a required software patch. Configuration drift includes patch gaps but also covers unauthorized settings changes, disabled controls, and added software — it is a broader concept than patching alone.
- Why D is incorrect: SOAR is an orchestration and automation platform that responds to alerts — it does not perform configuration state comparison against baselines. Security configuration management (SCM) tools such as CIS-CAT, Tripwire, or Chef InSpec are designed for baseline compliance checking.

---

### Question 14 (5 points)

During a change advisory board meeting, the infrastructure team requests approval to upgrade a core authentication server from Windows Server 2016 to Windows Server 2022. The CAB chair asks what documentation is required before the change can be approved. Which documents are required as part of a properly controlled change request?

- A) An approved change ticket, a tested rollback plan, and evidence of successful testing in a non-production environment
- B) A signed exception form from the CISO and a compensating control plan
- C) A vulnerability scan report showing no critical findings on the current server
- D) A business case document approved by the CFO

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: Exception forms and compensating controls are used when a standard cannot be met, not when a planned upgrade is proceeding through normal channels. The CAB process requires evidence that the change is safe to implement, not documentation that a policy exception has been granted.
- Why C is incorrect: A vulnerability scan of the current server addresses the current risk posture but is not a required change control document. The required documents address the change itself — the implementation plan, test results, and rollback procedure.
- Why D is incorrect: A CFO business case may be required for capital expenditures but is not a standard change control artifact. The CAB process focuses on technical safety, testing, and reversibility of the change, not financial authorization.

---

### Question 15 (5 points)

A SOC manager presents the following metrics to the CISO: patch compliance rate for critical vulnerabilities is 94% within the 72-hour SLA; security awareness training completion is 97%; mean time to detect is 3.1 hours; and 14 critical CVEs are currently open with no assigned patch window. Which metric is a Key Risk Indicator rather than a Key Performance Indicator?

- A) Patch compliance rate of 94%
- B) Security awareness training completion of 97%
- C) Mean time to detect of 3.1 hours
- D) 14 critical CVEs open with no assigned patch window

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Patch compliance rate measures how well the patching process is performing — it reflects program effectiveness, which is the definition of a KPI. A KRI would describe the current exposure level, such as how many systems remain unpatched.
- Why B is incorrect: Training completion rate measures how well the security awareness program is being executed — again, this is a program performance metric (KPI). A KRI related to training would be the percentage of employees who have not completed training and therefore remain at elevated phishing risk.
- Why C is incorrect: MTTD measures how quickly the SOC detects incidents — it describes the performance of the detection capability (KPI). A KRI related to detection would be the number of endpoints not covered by EDR or SIEM collection.

---

### Question 16 (5 points)

A SIEM correlation rule fires when more than 10 failed logins occur for any single account within 5 minutes. A SOC analyst investigates and finds the account belongs to an automated service account that runs scheduled jobs. The jobs authenticate simultaneously when servers restart after a maintenance window, producing bursts of authentication events that trigger the rule. What is the correct term for this type of alert and what is the recommended remediation?

- A) True positive; the service account should be disabled immediately
- B) False positive; the SIEM rule should be tuned to exclude the known service account or adjusted to account for legitimate maintenance window behavior
- C) False negative; the rule failed to detect a real attack against the service account
- D) True negative; the SIEM is correctly ignoring benign authentication activity

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A true positive is an alert for a real security incident. This scenario describes a legitimate maintenance process that triggers the rule due to its normal behavior — there is no malicious activity occurring. Disabling the service account would cause business disruption without any security benefit.
- Why C is incorrect: A false negative occurs when a real attack happens and the SIEM fails to alert on it. The alert fired — there is no missed detection. The alert fired incorrectly on benign activity, which is a false positive.
- Why D is incorrect: A true negative is when no alert fires and no attack occurred — the system correctly identified a benign event as benign. In this scenario, the SIEM did alert (incorrectly), so it is not a true negative.

---

### Question 17 (5 points)

An organization wants to ensure that every new endpoint joining the network meets a minimum security posture before being granted access — including verified OS patch level, enabled disk encryption, and active endpoint detection software. If the endpoint does not meet the minimum posture, it is placed in a quarantine VLAN with access only to a remediation server. Which security architecture concept is this?

- A) Network Access Control (NAC)
- B) Security Information and Event Management (SIEM)
- C) Endpoint Detection and Response (EDR)
- D) Data Loss Prevention (DLP)

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: SIEM collects and correlates logs from across the environment to generate security alerts. It does not evaluate endpoint health posture at network connection time or enforce quarantine based on posture findings.
- Why C is incorrect: EDR monitors endpoints for malicious activity, records telemetry, and enables response actions. It is deployed on an endpoint and does not make network admission decisions based on posture checks at join time.
- Why D is incorrect: DLP identifies and prevents unauthorized transfer of sensitive data. It does not assess OS patch level, encryption status, or AV software at network admission time.

---

### Question 18 (5 points)

A security engineer is implementing a SIEM for a hospital network. The SIEM needs to ingest logs from Windows domain controllers (Windows Event Log), Linux application servers (syslog), a Cisco ASA firewall (ASA syslog format), and a Palo Alto NGFW (PAN-OS log format). Each source uses different timestamp formats, field names, and severity labels. What must the SIEM perform before it can apply cross-source correlation rules?

- A) Log compression to reduce storage costs
- B) Log encryption to protect sensitive event data
- C) Log normalization to convert all sources into a common schema
- D) Log archiving to meet HIPAA retention requirements

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Log compression reduces storage volume and is a useful operational feature, but it does not enable correlation. Correlation requires consistent field structures across sources — compressed logs with inconsistent field names are still uncorrelatable.
- Why B is incorrect: Log encryption protects confidentiality of log data in transit and at rest, which is a compliance requirement, but encrypted logs that cannot be normalized are still not correlatable by the SIEM rules engine.
- Why D is incorrect: Log archiving addresses retention policy (HIPAA requires audit logs for 6 years), but archiving does not transform heterogeneous log formats into a consistent schema for real-time correlation.

---

### Question 19 (5 points)

A security analyst examines Nessus scan results for a web server and finds the following finding: "Plugin 56984 — SSL/TLS Diffie-Hellman Modulus <= 1024 Bits (Logjam). CVSS: 4.3. The remote host allows SSL/TLS connections with one or more Diffie-Hellman moduli less than or equal to 1024 bits. Solution: Reconfigure the service to use a modulus of at least 2048 bits." The server is internet-facing and hosts a customer portal. How should this finding be prioritized?

- A) Critical priority — CVSS 4.3 means the vulnerability is critical and must be patched within 24 hours
- B) Medium priority based on the CVSS score, but the internet-facing exposure and customer data context elevate the business risk above the CVSS score alone
- C) Low priority — CVSS 4.3 is below the high threshold and can wait until the next quarterly patch cycle
- D) No action required — Diffie-Hellman key exchange weaknesses are theoretical and not exploitable in practice

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: CVSS 4.3 falls in the Medium range (4.0–6.9), not Critical. Critical CVSS scores are 9.0–10.0. The word "critical" in answer A misrepresents what the CVSS score means.
- Why C is incorrect: While the CVSS score alone suggests medium priority, the vulnerability is on an internet-facing customer portal. Context factors — internet exposure, customer data, potential for downgrade attacks enabling traffic decryption — elevate the actual risk above what the base CVSS score captures. Waiting until quarterly patching ignores business risk context.
- Why D is incorrect: The Logjam vulnerability (CVE-2015-4000) was demonstrated to be practically exploitable in 2015 by academic researchers who showed nation-state-level actors could precompute discrete log tables for 1024-bit primes. It is a real, documented, exploitable vulnerability, not a theoretical one.

---

### Question 20 (5 points)

A mid-size company has a single security analyst who manages all vulnerability scanning, patch coordination, incident triage, and change management documentation. The analyst reports that 60% of her time is spent on manual, repetitive tasks: opening tickets for each new vulnerability, sending patch notifications, closing resolved vulnerability tickets, and updating asset inventory records. Which technology investment would most directly reduce this manual workload without replacing the analyst?

- A) Deploying a second Nessus scanner to double scanning coverage
- B) Implementing a SOAR platform to automate the routine ticket creation, notification, and status update workflows
- C) Migrating from qualitative to quantitative risk analysis to better prioritize the analyst's work
- D) Increasing the vulnerability scan frequency from weekly to daily

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: A second scanner increases scanning capacity and coverage but does not reduce the manual workload for processing and acting on findings. More scan results would likely increase the analyst's workload, not reduce it.
- Why C is incorrect: Switching from qualitative to quantitative risk analysis changes how risks are measured and prioritized. It does not automate ticket creation, patch notifications, or status updates — it may actually increase analysis workload.
- Why D is incorrect: Daily scanning generates more findings and more alert volume. Without automation to process the results, increasing scan frequency increases analyst workload. The problem is the manual downstream processing, not the scanning frequency.

---

End of Quiz — Module 15
