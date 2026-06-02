# Quiz: Module 03 - Vulnerability Management: Scanning and Prioritization

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 2 - Vulnerability Management (30%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer. Review the distractor analysis after completing the quiz.

---

## Question 1

A vulnerability scanner reports a Critical vulnerability (CVSS 9.8) on a system. The system is an isolated development server with no external network access, no production data, and no connectivity to production systems. At the same time, the scanner reports a High vulnerability (CVSS 7.5) on the organization's public-facing authentication portal. Which vulnerability should be remediated first?

- A) The Critical finding on the isolated development server because CVSS 9.8 is a higher score
- B) The High finding on the authentication portal because asset criticality and exposure elevate its effective priority
- C) Both findings must be remediated simultaneously because any Critical finding is immediately actionable
- D) Neither finding; both should be submitted to a risk acceptance process since neither affects production data

Correct Answer: B

Distractor Analysis:

- A is incorrect. CVSS score alone does not determine remediation priority. The isolated development server has no external exposure and no path to production data, which significantly reduces the effective risk despite the high score.
- B is correct. Risk-based prioritization requires weighing CVSS score alongside asset criticality, exposure, and exploitability. The authentication portal is internet-facing and business-critical — a successful exploit has immediate, high-impact consequences. This elevates the High-severity finding above the Critical finding on an isolated server.
- C is incorrect. Simultaneous remediation of all findings is impractical in most organizations; prioritization exists precisely because resources are limited.
- D is incorrect. Risk acceptance is appropriate only for genuinely low-risk findings after a formal analysis. Dismissing a finding on a critical authentication portal without analysis is not risk acceptance — it is negligence.

---

## Question 2

Which of the following CVSS v3.1 Base metrics describes whether an attacker needs a valid account on the target system before exploiting the vulnerability?

- A) Attack Vector
- B) Attack Complexity
- C) Privileges Required
- D) User Interaction

Correct Answer: C

Distractor Analysis:

- A is incorrect. Attack Vector describes how the attacker accesses the vulnerable component — via the network, an adjacent network, locally, or physically.
- B is incorrect. Attack Complexity describes whether special conditions beyond the attacker's control must exist for exploitation to succeed.
- C is correct. Privileges Required describes the level of authentication or privilege the attacker must already possess before exploiting the vulnerability. Options are None (no login required), Low (standard user access), and High (administrative access required).
- D is incorrect. User Interaction describes whether a human user must take an action (clicking a link, opening a file) for exploitation to succeed.

---

## Question 3

A SOC analyst receives vulnerability scan results showing a Critical finding for OpenSSL 1.0.2k on a Linux server. The server's system administrator states that the installed distribution has backported the security fix into the 1.0.2k version string, and the vulnerability is not actually present. What type of scan finding does this represent?

- A) True positive
- B) False positive
- C) True negative
- D) False negative

Correct Answer: B

Distractor Analysis:

- A is incorrect. A true positive means the vulnerability exists and was correctly detected. In this case, the vulnerability does not actually exist on the system.
- B is correct. A false positive is a vulnerability that the scanner reports but that does not actually exist. Version-based detection without confirming backported patches is a common cause of false positives on Linux systems where distributions apply security fixes without incrementing the upstream version string.
- C is incorrect. A true negative means no vulnerability exists and no finding was reported — not applicable here since the scanner did report a finding.
- D is incorrect. A false negative means a real vulnerability exists but the scanner did not detect it — the opposite of this scenario.

---

## Question 4

An analyst is reviewing scan findings and identifies a vulnerability on the organization's VPN appliance. The CVE has a CVSS Base Score of 7.2 (High). The analyst checks the CISA Known Exploited Vulnerabilities catalog and finds this CVE is listed. How should this information affect the analyst's prioritization decision?

- A) The KEV listing has no impact because the CVSS Base Score is only 7.2, which is not Critical
- B) The KEV listing confirms active exploitation in the wild and elevates this vulnerability to immediate remediation priority regardless of its CVSS score
- C) The KEV listing means the patch has already been applied by the vendor and no action is needed
- D) The KEV listing only applies to federal government agencies; private organizations do not need to consider it

Correct Answer: B

Distractor Analysis:

- A is incorrect. The CISA KEV catalog is not limited to Critical CVSS scores. Any CVE on the list has been confirmed as actively exploited, which makes it immediately actionable regardless of CVSS score.
- B is correct. CISA KEV listing confirms that threat actors have actively exploited this vulnerability in real attacks. This is the highest-priority signal in vulnerability management — active exploitation overrides CVSS score thresholds.
- C is incorrect. The KEV catalog tracks confirmed exploitation; it provides no information about vendor patch availability. Patch status must be checked separately.
- D is incorrect. While the KEV remediation deadlines are mandatory only for federal civilian agencies, the catalog is a public best-practice resource widely used by private sector organizations as a prioritization tool.

---

## Question 5

Which vulnerability scanning mode produces the most accurate and complete results for assessing the true patch state of an internal Windows server fleet?

- A) Unauthenticated external scanning from a DMZ-based scanner
- B) Credentialed internal scanning using a service account with read access to system configuration
- C) Passive network monitoring of traffic between servers to infer software versions
- D) Manual review of change management records to verify applied patches

Correct Answer: B

Distractor Analysis:

- A is incorrect. An unauthenticated external scan from the DMZ cannot enumerate the actual patch state of internal systems; it can only see network-visible services and infer software versions, producing more false positives and missing many internal vulnerabilities.
- B is correct. Credentialed internal scanning authenticates to each target system, reads installed software versions, checks applied patches, and audits configuration settings directly. This produces the most accurate patch state assessment with the fewest false positives.
- C is incorrect. Passive network monitoring can identify software version banners in traffic but cannot reliably determine patch state and misses vulnerabilities in services that don't advertise versions in traffic.
- D is incorrect. Change management records document planned and approved changes but may not reflect emergency patches, failed patch deployments, or configuration drift. Manual record review is not a substitute for automated scanning.

---

## Question 6

A vulnerability scan finds a High-severity finding on a database server that contains the organization's primary customer PII database. The finding indicates that the database service is running on a default port and responding to unauthenticated status queries. The recommended remediation is to disable the unauthenticated status endpoint through configuration. Which remediation type is most appropriate?

- A) Patch
- B) Risk acceptance
- C) Configuration change
- D) System decommission

Correct Answer: C

Distractor Analysis:

- A is incorrect. Patching applies when a software vulnerability requires a vendor-supplied update. This finding results from a default configuration setting, not a software flaw requiring a patch.
- B is incorrect. Risk acceptance is appropriate only for low-risk findings where remediation cost exceeds risk. A High-severity finding on a PII database server does not meet this threshold.
- C is correct. The recommended remediation is to disable the unauthenticated status endpoint — a configuration change. Vulnerabilities caused by default or misconfigured settings are remediated through configuration changes, not patches.
- D is incorrect. Decommissioning is reserved for end-of-life systems that cannot be patched or secured. This database server hosts critical production data and has a straightforward configuration fix available.

---

## Question 7

An organization's vulnerability management policy requires remediation of High-severity findings within 30 days. A system owner states that a High-severity finding cannot be patched because the vendor patch breaks a critical business application that has no replacement for at least six months. What is the most appropriate course of action?

- A) Extend the remediation deadline to six months with no additional action required
- B) Immediately decommission the affected system until a compatible patch is available
- C) Implement a compensating control to reduce risk and document a formal risk acceptance with management sign-off for the interim period
- D) Close the finding in the vulnerability management system since the patch cannot be applied

Correct Answer: C

Distractor Analysis:

- A is incorrect. Simply extending the deadline without additional protective action leaves the organization exposed for six months with no risk reduction.
- B is incorrect. Decommissioning a system running a critical business application is disproportionate and would cause business disruption. Compensating controls should be explored first.
- C is correct. When a patch cannot be applied, the correct approach is to implement compensating controls (network segmentation, enhanced monitoring, WAF rules, additional authentication) to reduce risk, and document formal risk acceptance with management approval for the period until the patch can be applied.
- D is incorrect. Closing a finding that has not been remediated is improper. Open findings must remain open until they are either remediated, have a documented compensating control, or are formally accepted as risk with management sign-off.

---

## Question 8

During a vulnerability scan review, an analyst notices that no findings were returned for a network segment hosting 15 servers. The scanner configuration log shows that the scanner is positioned in the corporate office network and the 15 servers are in a dedicated manufacturing floor network segment separated by an internal firewall with no rules permitting traffic from the scanner's network. What does this situation represent?

- A) A true negative — the manufacturing floor servers have no vulnerabilities
- B) A false negative — the scanner may have missed real vulnerabilities because it could not reach the segment
- C) A false positive — the scanner incorrectly reported no findings for a network segment it did not scan
- D) A scan anomaly that requires no corrective action since internal segments are lower risk

Correct Answer: B

Distractor Analysis:

- A is incorrect. The absence of findings does not mean there are no vulnerabilities. In this case, the scanner never reached the segment, so it produced no findings — but the servers may have many vulnerabilities.
- B is correct. This is a false negative scenario — real vulnerabilities may exist but were not detected because the scanner lacked network access to the target segment. The firewall blocked the scanner's probe traffic. The correct fix is to provision scanner access to all target segments or deploy a scanner within the manufacturing segment.
- C is incorrect. A false positive is an incorrectly reported vulnerability. Reporting no findings for an unreachable segment is not a false positive — it is a scan gap.
- D is incorrect. Internal network segments, including manufacturing floor OT/IT systems, often contain high-value targets and may run legacy, unpatched software. Assuming they are lower risk because they are internal is a dangerous assumption.

---

## Question 9

A vulnerability management analyst is preparing a monthly report for the CISO. Which metric would most directly communicate the efficiency of the organization's vulnerability remediation program over time?

- A) Total number of vulnerability scans performed in the reporting period
- B) Number of new CVEs published by NVD during the reporting period
- C) Percentage of Critical and High findings remediated within SLA timeframes
- D) Total number of assets scanned during the reporting period

Correct Answer: C

Distractor Analysis:

- A is incorrect. The number of scans performed indicates scanning activity but says nothing about whether findings are actually being remediated. More scans that produce unaddressed findings do not improve security.
- B is incorrect. The total number of CVEs published by NVD is an industry-wide number outside the organization's control. It does not measure the organization's remediation performance.
- C is correct. SLA compliance for Critical and High findings directly measures whether the vulnerability management program is achieving its core objective: remediating high-risk findings within defined timeframes. This is the most meaningful efficiency metric for executive reporting.
- D is incorrect. Asset scan coverage is an important metric for measuring scan completeness but does not measure whether findings are being remediated.

---

## Question 10

Which of the following correctly describes the relationship between a vulnerability's CVSS Base Score and its Temporal Score?

- A) The Temporal Score is always higher than the Base Score because it adds exploit availability data
- B) The Temporal Score modifies the Base Score downward over time as patches become available and exploit maturity decreases
- C) The Temporal Score replaces the Base Score once an exploit is publicly released
- D) The Temporal Score only applies to Critical CVSS findings and has no effect on High, Medium, or Low findings

Correct Answer: B

Distractor Analysis:

- A is incorrect. The Temporal Score modifies the Base Score; it can reduce the effective score as remediation becomes available. It does not universally increase the score.
- B is correct. The CVSS Temporal Score accounts for factors that change over time. The Exploit Code Maturity (E) metric reduces the score if no exploit is available and increases urgency if a weaponized exploit exists. As the vendor releases a patch and the vulnerability ages, the Temporal Score typically decreases relative to the Base Score.
- C is incorrect. The Temporal Score modifies the Base Score; it does not replace it. The Base Score remains the foundational measure.
- D is incorrect. CVSS Temporal Score applies to vulnerabilities at any severity level. It is not restricted to Critical findings.
