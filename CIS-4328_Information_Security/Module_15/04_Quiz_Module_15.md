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

End of Quiz — Module 15
