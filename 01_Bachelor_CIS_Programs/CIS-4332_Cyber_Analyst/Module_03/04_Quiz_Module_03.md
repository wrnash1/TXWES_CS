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

---

## Question 11 (5 points)

A vulnerability scanner returns a finding for a web application on an internal development server that is not reachable from the internet and holds no production data. The CVSS Base Score is 9.1 (Critical). The CISA KEV catalog does not list this vulnerability. What is the most appropriate remediation priority decision?

- A) Immediately patch within 24 hours because all Critical CVSS findings require emergency response
- B) Accept the risk permanently since the server is internal
- C) Apply normal business-priority patching within the standard patch cycle, documenting the rationale that low exposure and absence from KEV reduce effective risk
- D) Remove the server from the network until the patch is applied

Correct Answer: C

Distractor Analysis:

- A is incorrect. CVSS score alone does not determine patching urgency. The absence of external exposure, production data, and a KEV listing significantly reduces the actual risk. A flat "patch all Critical in 24 hours" policy fails to account for business context and would overwhelm patching teams with low-actual-risk items.
- B is incorrect. Risk acceptance without documentation and context analysis is not a proper vulnerability management procedure. Internal servers can still be attack pivot points, so permanent risk acceptance without review is inappropriate.
- C is correct. The combination of no external exposure, no production data, and no KEV listing justifies scheduling the patch within the standard cycle. Documenting the risk rationale is the professional approach and satisfies audit requirements.
- D is incorrect. Taking the server offline is a disproportionate response given the low actual risk. Containment actions of this severity require confirmed exploitation evidence or critical asset exposure that is not present here.

---

## Question 12 (5 points)

A credentialed vulnerability scan identifies 47 findings on a Windows server. An uncredentialed scan of the same server returns only 12 findings. What best explains the difference?

- A) The credentialed scan misconfigured itself and generated false positives
- B) The uncredentialed scan only tests for network-layer vulnerabilities; it cannot inspect installed software versions, registry settings, or local configurations that require authentication
- C) Windows servers have fewer vulnerabilities when scanned without credentials because the scanner cannot trigger them
- D) Credentialed scanning always returns more findings because it tests a broader IP range

Correct Answer: B

Distractor Analysis:

- A is incorrect. The credentialed scan is more likely to produce accurate results, not more false positives. The difference in count is expected behavior, not misconfiguration.
- B is correct. Credentialed scanning authenticates to the target system and can directly inspect installed software versions, patch levels, registry keys, and local configuration files. Uncredentialed scanning can only observe what is visible from the network — open ports, service banners, and externally reachable vulnerabilities. The 35-finding gap is a typical illustration of this difference.
- C is incorrect. Vulnerabilities exist independent of scanning method. The scanner not being able to see them does not mean they are not present — it means the uncredentialed scan has a visibility gap.
- D is incorrect. Credentialed scanning is not about scanning a broader IP range. It authenticates to a single target to gain deeper visibility into that target's configuration.

---

## Question 13 (5 points)

An organization's remediation SLA requires Critical vulnerabilities to be patched within 15 days. A Critical finding was discovered on day 1 and is not yet patched on day 18. Which term describes this finding's status?

- A) Risk accepted
- B) False positive
- C) SLA breach
- D) Compensating control applied

Correct Answer: C

Distractor Analysis:

- A is incorrect. Risk acceptance is a formal decision documented by authorized stakeholders that a finding will not be remediated. There is no indication that a formal risk acceptance decision was made — the patch is simply overdue.
- B is incorrect. A false positive is a finding that the scanner reported but does not actually exist on the system. The scenario does not question whether the finding is real.
- C is correct. The vulnerability was not remediated within the defined 15-day SLA window. This is a SLA breach — a measurable operational failure that should be tracked, escalated, and reported.
- D is incorrect. A compensating control is a mitigation applied when a direct patch is not possible, accompanied by documentation. No such control is described in the scenario.

---

## Question 14 (5 points)

Which CVSS v3.1 Base metric describes whether the attacker needs to be on the same network segment as the vulnerable component or can attack it remotely across the internet?

- A) User Interaction (UI)
- B) Privileges Required (PR)
- C) Attack Vector (AV)
- D) Scope (S)

Correct Answer: C

Distractor Analysis:

- A is incorrect. User Interaction describes whether the attack requires a human user to take an action (e.g., click a link, open a file). It does not describe network positioning.
- B is incorrect. Privileges Required describes whether the attacker needs to be authenticated and what privilege level is required before the attack can be executed.
- C is correct. Attack Vector (AV) describes the context from which exploitation is possible. The values are Network (remotely exploitable across the internet), Adjacent (requires same network), Local (requires local access), and Physical (requires physical hardware access).
- D is incorrect. Scope describes whether a successful exploit can affect components beyond the vulnerable component itself. It does not describe attacker positioning.

---

## Question 15 (5 points)

The CISA Known Exploited Vulnerabilities (KEV) catalog was established to serve which primary purpose?

- A) To replace CVSS as the standard vulnerability scoring system
- B) To provide a government-mandated list of vulnerabilities that federal agencies must remediate within specified deadlines, serving as a practical exploitation-confirmed prioritization resource
- C) To list all vulnerabilities discovered by CISA researchers regardless of exploitation status
- D) To assign legal liability to vendors whose software appears in the catalog

Correct Answer: B

Distractor Analysis:

- A is incorrect. The KEV catalog does not replace CVSS. They serve different purposes: CVSS measures theoretical severity; KEV confirms actual exploitation in the wild. Organizations use both together for prioritization.
- B is correct. The KEV catalog was created by CISA under Binding Operational Directive 22-01. It lists vulnerabilities with confirmed evidence of active exploitation in the wild and mandates remediation deadlines for federal civilian agencies. Private sector organizations widely use it as a high-confidence exploitation-confirmed prioritization signal.
- C is incorrect. The KEV catalog specifically requires evidence of active exploitation. It does not list all discovered vulnerabilities — that is the role of the NVD.
- D is incorrect. The KEV catalog does not assign legal liability. Vendors are not penalized for appearing in the catalog — it is an informational resource for defenders.

---

## Question 16 (5 points)

Which of the following best describes the difference between a patch and a compensating control in the context of vulnerability remediation?

- A) A patch is applied by the vendor; a compensating control is applied by the operating system
- B) A patch directly fixes the vulnerable code or configuration; a compensating control reduces the likelihood or impact of exploitation without fixing the underlying vulnerability
- C) A patch is used for Critical findings; a compensating control is used for Low findings only
- D) A patch and a compensating control are equivalent remediation actions that provide identical protection

Correct Answer: B

Distractor Analysis:

- A is incorrect. Patches are distributed by vendors but applied by system administrators. Compensating controls are implemented by the defending organization and can include configuration changes, network segmentation, or additional monitoring — not operating system actions specifically.
- B is correct. A patch modifies the software or configuration to eliminate the vulnerability entirely. A compensating control reduces risk through indirect means — for example, blocking network access to a vulnerable service as a workaround when the patch cannot be applied immediately — but the underlying vulnerability remains.
- C is incorrect. Compensating controls are used across all severity levels when direct patching is not feasible, not only for Low severity findings.
- D is incorrect. Compensating controls do not provide equivalent protection to direct patching. They are interim risk reduction measures, not permanent fixes.

---

## Question 17 (5 points)

An analyst runs a vulnerability scan and finds a reported Critical vulnerability in Apache Struts on a production web server. The analyst verifies manually that the server actually runs Nginx, not Apache Struts. How should the analyst classify this finding?

- A) True positive — the scanner correctly identified a real vulnerability
- B) False positive — the scanner reported a vulnerability that does not exist on this system
- C) False negative — the scanner missed a vulnerability that actually exists
- D) True negative — the scanner correctly determined no vulnerability was present

Correct Answer: B

Distractor Analysis:

- A is incorrect. A true positive requires that both the alert fired and the vulnerability actually exists. Since the server runs Nginx, not Apache Struts, the vulnerability cannot exist on this system.
- B is correct. A false positive in vulnerability scanning occurs when the scanner reports a vulnerability on a system where the vulnerable component is not actually present. The scanner incorrectly fingerprinted the web server and produced an inaccurate result.
- C is incorrect. A false negative means the scanner missed a vulnerability that does exist. In this case, the scanner reported something that does not exist — the opposite scenario.
- D is incorrect. A true negative means no alert fired and no vulnerability exists. The scanner did fire an alert in this scenario — it just fired incorrectly.

---

## Question 18 (5 points)

Which of the following is the correct order of the vulnerability management lifecycle phases?

- A) Remediate → Scan → Prioritize → Discover → Report
- B) Discover → Scan → Prioritize → Remediate → Report
- C) Report → Discover → Scan → Remediate → Prioritize
- D) Scan → Discover → Report → Prioritize → Remediate

Correct Answer: B

Distractor Analysis:

- A is incorrect. Remediation cannot occur before scanning and prioritization. This order reverses the process.
- B is correct. The vulnerability management lifecycle follows: Discover (identify assets in scope) → Scan (run the vulnerability scanner) → Prioritize (rank findings by risk) → Remediate (apply patches or controls) → Report (track metrics and communicate status). Some models use slightly different naming but this sequence is consistent across frameworks.
- C is incorrect. Reporting is the final phase, not the first. The process must produce findings before they can be reported.
- D is incorrect. Discovery of assets in scope precedes scanning. You cannot effectively scope a scan without knowing your asset inventory.

---

## Question 19 (5 points)

Which vulnerability management metric most directly measures the program's effectiveness at protecting the organization from actively exploited threats?

- A) Total number of vulnerabilities discovered per quarter
- B) Percentage of KEV catalog items patched within the defined SLA timeframe
- C) Average CVSS score across all open findings
- D) Number of new vulnerability scanner licenses purchased

Correct Answer: B

Distractor Analysis:

- A is incorrect. The number of discoveries is a coverage metric. Discovering many vulnerabilities without remediating them provides no protection.
- B is correct. The KEV catalog lists vulnerabilities with confirmed active exploitation. Tracking what percentage of KEV items are remediated within the SLA directly measures whether the program is protecting the organization from the threats most likely to cause real-world harm.
- C is incorrect. Average CVSS score across all open findings is a risk density metric, not a protection effectiveness metric. It does not indicate whether the most dangerous vulnerabilities are being addressed first.
- D is incorrect. License purchases measure budget spend, not security outcomes.

---

## Question 20 (5 points)

An organization wants to reduce the number of false positives in its credentialed vulnerability scan results. Which approach is most effective?

- A) Switch from credentialed to uncredentialed scanning to reduce the number of findings
- B) Tune the scanner's plugin configuration to match the actual operating systems, applications, and versions deployed, and maintain an accurate asset inventory
- C) Increase scan frequency from weekly to daily, which will cause false positives to self-correct over time
- D) Disable all plugins for operating system vulnerabilities and only scan application-layer components

Correct Answer: B

Distractor Analysis:

- A is incorrect. Switching to uncredentialed scanning reduces overall findings but also dramatically reduces true positives — it does not improve accuracy. You lose real findings along with false ones.
- B is correct. False positives in vulnerability scanning most commonly result from inaccurate asset inventory, incorrect OS/application fingerprinting, or overly broad plugin configurations. Tuning scanner plugins to reflect the actual environment and maintaining an accurate asset inventory are the most effective false positive reduction strategies.
- C is incorrect. Increasing scan frequency does not cause false positives to self-correct. The same inaccurate plugin will produce the same false positive on every scan.
- D is incorrect. Disabling OS vulnerability plugins would eliminate coverage for entire vulnerability categories, increasing false negatives (missed real vulnerabilities) far more than it reduces false positives.
