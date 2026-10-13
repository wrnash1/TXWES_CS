# Quiz: Module 08 — Vulnerability Management

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer.

---

## Question 1

A vulnerability scanner is configured to scan an organization's server fleet using only a network-level scan with no credentials provided. The scanner reports 12 Critical and 34 High findings. A subsequent authenticated scan of the same servers returns 47 Critical and 112 High findings. What is the most accurate explanation for the significant difference in findings?

- A) The authenticated scan ran a more comprehensive plugin set that the unauthenticated scan was not licensed for
- B) Unauthenticated scanning relies on version banners and service fingerprinting, which may not reflect actual installed patch levels — authenticated scanning reads actual patch state directly from the OS, producing more accurate and complete results
- C) The unauthenticated scan was run against a different network segment, explaining the lower finding count
- D) Authenticated scanning generates false positives by over-reporting vulnerabilities not actually present on the system

Correct Answer: B

Distractor Analysis:

- A is incorrect. While some scanner versions have plugin licensing differences, the primary reason for the disparity between authenticated and unauthenticated scans is the depth of data access — not plugin licensing. Authenticated scanning provides direct system access regardless of licensing tier.
- B is correct. Unauthenticated scanning guesses vulnerability state based on version strings reported by services. If a service reports version 2.4.49 but a patch has been applied that fixes the CVE without changing the version banner, the unauthenticated scan will report the vulnerability incorrectly. Authenticated scanning reads the actual installed patch registry, installed package database, or file version — dramatically improving accuracy in both directions (fewer false positives and false negatives).
- C is incorrect. The question states both scans targeted the same server fleet. Network segment difference is not a valid explanation for this scenario.
- D is incorrect. Authenticated scanning produces more accurate results overall — both more true positives (catching things unauthenticated scanning missed) and fewer false positives (confirming actual patch state). It does not systematically over-report.

---

## Question 2

A vulnerability assessment identifies CVE-2023-XXXX with the following CVSS v3.1 vector: `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Which statement most accurately describes the exploitability characteristics of this vulnerability?

- A) Exploitation requires local access to the system and a user to be tricked into opening a malicious file
- B) Exploitation is possible only by an authenticated user with high-level administrative privileges
- C) Exploitation can be performed by any unauthenticated remote attacker over the network without user interaction and without complex conditions
- D) Exploitation requires physical access to the device and user interaction with the target system

Correct Answer: C

Distractor Analysis:

- A is incorrect. The vector shows AV:N (Attack Vector: Network) — not local access. UI:N means no user interaction is required. AC:L means attack complexity is low — no complex conditions needed.
- B is incorrect. PR:N (Privileges Required: None) means no authentication or privileges are required. An authenticated high-privilege requirement would be PR:H.
- C is correct. This vector decodes as: AV:N (network-accessible), AC:L (low complexity — easy to exploit reliably), PR:N (no privileges required — unauthenticated), UI:N (no user interaction required), S:U (scope unchanged), C:H/I:H/A:H (high impact on confidentiality, integrity, and availability). This is a worst-case exploitability profile — any attacker on the internet can attempt exploitation without credentials or victim action.
- D is incorrect. AV:P (Physical) would indicate physical access required. AV:N explicitly means network access is sufficient. UI:N means no user interaction.

---

## Question 3

The CISA Known Exploited Vulnerabilities (KEV) catalog is updated to include a CVE that affects a web server running in your organization's DMZ. The CVE has a CVSS v3.1 Base Score of 6.8 (Medium). Your organization's vulnerability management policy requires Medium vulnerabilities to be patched within 90 days. How should you handle this finding?

- A) Follow the standard policy — patch within 90 days because the CVSS Medium score defines the timeline
- B) Escalate immediately and treat this as a higher priority than the CVSS score suggests, because KEV status indicates active exploitation in the wild regardless of CVSS score
- C) Downgrade the finding to Low priority because CVSS 6.8 is borderline Medium and KEV listings are only mandatory for federal agencies
- D) Wait for the CVSS Temporal Score to update with the exploitation data before deciding on priority

Correct Answer: B

Distractor Analysis:

- A is incorrect. CVSS score alone is an incomplete prioritization input. A KEV listing means attackers are actively exploiting this vulnerability today. Applying a 90-day SLA to a CVE being actively weaponized in the wild creates a 90-day window of exposure to known active exploitation.
- B is correct. CISA KEV status overrides the CVSS-based SLA policy for rational risk-based prioritization. The KEV catalog specifically identifies vulnerabilities being exploited in the wild — if attackers are using it today, organizational exposure exists today. Security programs should treat KEV entries as "patch immediately" or "apply workaround now," regardless of the CVSS score. A CVSS 6.8 in active exploitation is more dangerous than a CVSS 9.0 with no known exploitation.
- C is incorrect. While federal agencies have compliance mandates tied to KEV, private organizations face the same real-world exploitation risk. KEV listings are relevant to any organization regardless of sector. Downgrading priority based on non-federal status ignores the actual threat.
- D is incorrect. The Temporal Score may eventually update, but waiting for a score update before acting on an actively exploited vulnerability creates unnecessary delay. KEV status is already the definitive exploitation signal — no score calculation needed to justify action.

---

## Question 4

A security analyst calculates an Environmental Score for a Critical vulnerability (CVSS Base Score 9.8) affecting an internal database server that contains no sensitive data, has no external network access, and is physically isolated from production systems. After applying Modified Attack Vector (from Network to Local) and lowering the Confidentiality Requirement, the adjusted score becomes 4.2 (Medium). Which statement best evaluates this approach?

- A) This approach is inappropriate — CVSS Base Scores are fixed and cannot be modified by individual organizations
- B) This approach correctly demonstrates how Environmental Score customization allows organizations to apply context-specific risk assessment rather than treating all Critical findings identically
- C) The analyst should not lower the score below 7.0 (High) for any Critical vulnerability, as this creates compliance violations
- D) The Environmental Score adjustment is only valid if the vulnerability has been verified as not exploitable in the current environment through active penetration testing

Correct Answer: B

Distractor Analysis:

- A is incorrect. Environmental Scores are a defined component of the CVSS standard specifically designed for organizations to customize scoring based on their environment. CVSS explicitly supports Modified Base Metrics (MAV, MAC, MPR, MUI, MS) and CIA Requirement weights for this purpose.
- B is correct. The CVSS Environmental Score exists precisely to enable this kind of risk-based adjustment. A vulnerability that requires network access but is only accessible locally, affects a system with no sensitive data, and is isolated from production systems has significantly lower actual risk than the base score implies. Environmental Score customization produces a more accurate representation of organizational risk and prevents resource misallocation to low-actual-risk findings.
- C is incorrect. There is no CVSS standard or universal compliance mandate that prohibits adjusting Environmental Scores below specific thresholds. Environmental Score adjustment is standard practice. Individual compliance frameworks (PCI DSS, HIPAA) set their own patch requirements, but these are separate from CVSS scoring methodology.
- D is incorrect. Environmental Score adjustments are not contingent on penetration test verification. They are based on documented environmental characteristics — network architecture, asset classification, data classification — that can be verified through configuration review and asset inventory, not exclusively through active exploitation testing.

---

## Question 5

Which of the following best describes what the EPSS (Exploit Prediction Scoring System) measures and how it should be used alongside CVSS?

- A) EPSS measures the potential business impact of a vulnerability and replaces CVSS for organizational risk prioritization
- B) EPSS measures the technical severity of a vulnerability's exploitable characteristics and duplicates information already in the CVSS Base Score
- C) EPSS predicts the probability that a given CVE will be exploited in the wild within 30 days, providing exploitation likelihood context that CVSS Base Score does not include
- D) EPSS measures how many organizations have already been compromised through a specific vulnerability, serving as a historical exploitation count

Correct Answer: C

Distractor Analysis:

- A is incorrect. EPSS does not measure business impact. It is a probability model for exploitation likelihood. It is designed to complement CVSS, not replace it — CVSS measures technical severity while EPSS measures exploitation probability.
- B is incorrect. EPSS and CVSS measure fundamentally different things. CVSS Base Score measures inherent technical severity (how bad could this be?). EPSS measures exploitation probability (how likely is this to be exploited?). A vulnerability can have low CVSS but high EPSS — for example, a medium-complexity vulnerability in a widely deployed product that has a working public exploit.
- C is correct. EPSS uses a machine learning model fed by threat intelligence, exploitation feeds, and vulnerability characteristics to produce a daily-updated probability score (0–1) for each CVE. A score of 0.85 means 85% of CVEs with similar characteristics are exploited within 30 days. Used alongside CVSS, EPSS helps analysts identify high-probability-of-exploitation vulnerabilities that might have moderate CVSS scores but deserve urgent attention.
- D is incorrect. EPSS is a predictive model, not a historical count. It predicts future exploitation probability, not the count of past compromises. Historical exploitation data is one input into the model, but the output is a probability score, not a victim count.

---

## Question 6

After a vulnerability scanner identifies a critical RCE vulnerability on an internet-facing web application server, the application owner informs the security team that the official vendor patch cannot be deployed for three weeks due to a regression that would break a critical business process. What is the most appropriate immediate response?

- A) Accept the risk and schedule the patch for the vendor's next release cycle, which is six months away
- B) Decommission the application until the vendor patch is available
- C) Apply a virtual patch via a Web Application Firewall rule or IPS signature to block known exploit traffic while the official patch is tested and prepared for deployment
- D) Rerun the vulnerability scan to verify the finding is accurate before taking any action

Correct Answer: C

Distractor Analysis:

- A is incorrect. A six-month delay on a critical RCE affecting an internet-facing server creates an unacceptable exploitation window, especially given KEV-level exposure risk for many RCE vulnerabilities. Risk acceptance without compensating controls is inappropriate here.
- B is incorrect. Decommissioning a critical business application is likely to cause significant operational impact and is typically not within the security team's authority to decide unilaterally. Virtual patching provides risk reduction without application downtime.
- C is correct. Virtual patching — deploying a WAF or IPS rule that blocks known exploitation patterns for the specific CVE — is the standard compensating control when a vendor patch cannot be immediately applied. It reduces exposure while the official patch is tested and staged for production deployment. This approach is documented in the CVSS remediation options framework and is widely practiced in enterprise vulnerability management programs.
- D is incorrect. Rerunning the scan adds no value when the application owner has already confirmed the vulnerability exists and the business constraint has been identified. The priority is reducing exposure, not re-confirming what is already known.

---

## Question 7

A vulnerability management analyst is reviewing scan results and notices that a Linux server running Apache 2.4.51 shows a finding for CVE-2021-41773 (Apache Path Traversal/RCE). However, the sysadmin confirms that the mod_cgi module is disabled on this server, which is required for the RCE portion of the exploit. What is the correct classification for this finding?

- A) True positive — CVE-2021-41773 affects Apache 2.4.51 regardless of module configuration, and the finding should be escalated as Critical
- B) Partial false positive — the path traversal component may still be exploitable, but the RCE impact is mitigated by the disabled mod_cgi module; severity should be reassessed with the Environmental Score
- C) False positive — since mod_cgi is disabled, the vulnerability is completely non-exploitable and should be closed without action
- D) True negative — the scanner correctly detected that the vulnerability is not exploitable and the finding should be deleted

Correct Answer: B

Distractor Analysis:

- A is incorrect. While the vulnerability does affect Apache 2.4.51, the compensating control (disabled mod_cgi) materially reduces the actual impact. Treating this identically to a fully exploitable instance ignores relevant context and misallocates remediation resources.
- B is correct. CVE-2021-41773 has two components: a path traversal vulnerability and, if mod_cgi is enabled, remote code execution. With mod_cgi disabled, the RCE component is neutralized but the path traversal may remain exploitable — depending on the target resource. This is a classic Environmental Score adjustment scenario: the Modified Integrity and Availability impact should be lowered, but the finding should not be dismissed. The system still needs patching to Apache 2.4.50+ to resolve both components.
- C is incorrect. A disabled mod_cgi module eliminates RCE but does not necessarily eliminate path traversal exploitation entirely. Closing the finding without patching leaves residual exposure. The correct action is adjusted prioritization, not elimination.
- D is incorrect. A true negative means no vulnerability exists and no finding was generated. The scanner did detect a finding — the discussion is about severity interpretation and compensating controls, not about whether the scanner made an error.

---

## Question 8

A security analyst is presenting vulnerability management metrics to the CISO. Which metric most directly measures whether the vulnerability management program is keeping pace with new vulnerabilities being discovered and whether the organization's risk posture is improving over time?

- A) Total number of vulnerability scan plugins installed in the scanner
- B) Number of vulnerability scan scans performed per quarter
- C) Vulnerability backlog trend — whether the number of open, unpatched vulnerabilities is growing, stable, or shrinking over time
- D) Percentage of vulnerability findings that were discovered through authenticated versus unauthenticated scanning

Correct Answer: C

Distractor Analysis:

- A is incorrect. The number of installed scanner plugins measures scanner capability, not program effectiveness. Having more plugins does not mean vulnerabilities are being remediated faster or that risk is decreasing.
- B is incorrect. The number of scans performed measures activity, not outcomes. Running more scans without remediating findings does not improve security posture. Scan frequency is an input metric, not an outcome metric.
- C is correct. Vulnerability backlog trend directly measures program effectiveness. A growing backlog indicates that new vulnerabilities are being discovered faster than they are being remediated — the program is falling behind. A shrinking backlog indicates remediation is outpacing discovery — the program is improving posture. This trend metric, combined with SLA compliance rate, is the most meaningful indicator of vulnerability management program health for CISO-level reporting.
- D is incorrect. The ratio of authenticated to unauthenticated scanning measures data quality and methodology, not program effectiveness or risk posture improvement. It is a useful operational metric but not a board-level risk posture metric.

---

## Question 9

Which of the following correctly describes the relationship between the CVE database maintained by MITRE and the National Vulnerability Database (NVD) maintained by NIST?

- A) They are competing databases — organizations should choose one and use it exclusively to avoid confusion from different scoring
- B) CVE provides the unique identifier and basic description for each vulnerability; NVD enriches CVE data with CVSS scores, CPE applicability, and reference links to patches and advisories
- C) NVD assigns CVE identifiers to newly discovered vulnerabilities; MITRE enriches them with CVSS scores and exploitation information
- D) CVE is the commercial, paid version of vulnerability data; NVD is the free government version for organizations that cannot afford commercial feeds

Correct Answer: B

Distractor Analysis:

- A is incorrect. CVE and NVD are complementary, not competing. Both are free, authoritative, and used together. CVE is the naming registry; NVD is the enrichment database. Security practitioners use both in their workflows.
- B is correct. The CVE Program (MITRE) assigns CVE identifiers and provides minimal descriptions for publicly disclosed vulnerabilities. NIST's NVD then enriches each CVE with CVSS v3.1 Base Scores, vector strings, CWE weakness classifications, CPE applicability statements identifying affected products and versions, and references to vendor advisories and patches. The NVD is the analyst's primary research resource; CVE provides the canonical identifier.
- C is incorrect. MITRE assigns CVE identifiers, not NIST/NVD. This answer reverses the roles of the two organizations.
- D is incorrect. Both the CVE List and the NVD are completely free, public, government-sponsored resources. There is no commercial/free distinction between them.

---

## Question 10

A vulnerability management analyst must choose between patching a server now versus implementing a network segmentation control as a temporary compensating measure. The server hosts a legacy application that cannot be easily patched due to vendor support constraints. The vulnerability is a CVSS 8.1 network-accessible authentication bypass. Which response option is most appropriate given the constraint?

- A) Implement the network segmentation immediately to restrict access to only authorized hosts and document the residual risk as a formal risk acceptance while planning a longer-term remediation path
- B) Delay any action until the vendor is able to provide an official patch, and document that the vulnerability was identified but not addressable
- C) Disable the server completely until a patch is available, regardless of business impact
- D) Modify the CVSS Base Score in the vulnerability management platform to reduce the severity of the finding to avoid SLA breach documentation

Correct Answer: A

Distractor Analysis:

- A is correct. When patching is not immediately feasible due to vendor constraints, the appropriate response is to implement the strongest available compensating control (network segmentation limiting access to the vulnerable service to only authorized hosts reduces the attack surface substantially) and document the residual risk through a formal risk acceptance process signed by the appropriate business owner. This follows the CVSS remediation framework — applying compensating controls reduces effective exposure, and formal risk acceptance ensures accountability for the remaining risk.
- B is incorrect. Delaying all action and merely documenting the finding is not an acceptable response for a CVSS 8.1 authentication bypass. This leaves the vulnerability fully exposed with no compensating control while waiting indefinitely for vendor support.
- C is incorrect. Disabling a production server without business impact assessment and executive approval is not a unilateral security team decision. Business continuity must be weighed against security risk. Compensating controls are the standard approach when disabling a service is not feasible.
- D is incorrect. Modifying scores in the vulnerability management platform to avoid SLA breach documentation is a form of metric manipulation. It does not reduce actual risk, violates the integrity of the vulnerability program, and could expose the organization to compliance and audit findings if discovered. SLA breaches with documented justified exceptions are the correct handling path.

---

## Question 11 (5 points)

The EPSS (Exploit Prediction Scoring System) assigns a probability score from 0 to 1 representing the likelihood a vulnerability will be exploited in the wild within 30 days. A vulnerability has a CVSS Base Score of 9.8 but an EPSS score of 0.0041 (0.41%). A second vulnerability has a CVSS Base Score of 6.5 but an EPSS score of 0.9310 (93.1%). Which should be remediated first?

- A) The CVSS 9.8 vulnerability because severity always takes precedence over exploitation probability
- B) The CVSS 6.5 vulnerability because the 93.1% EPSS score indicates active exploitation is extremely likely in the near term
- C) Both must be remediated in the same patch cycle regardless of EPSS scores
- D) Neither — the CVSS 9.8 vulnerability should be accepted since no exploit is currently known, and the CVSS 6.5 finding should be deferred since it is below the Critical threshold

Correct Answer: B

Distractor Analysis:

- A is incorrect. CVSS score represents theoretical severity of a successfully exploited vulnerability. EPSS complements CVSS by measuring likelihood of actual exploitation based on threat intelligence. A vulnerability that is almost certain to be exploited in the next 30 days poses more immediate practical risk than a theoretically worse vulnerability that is rarely targeted.
- B is correct. The EPSS 6.5 vulnerability is actively targeted — a 93% probability of exploitation in 30 days is an extremely high likelihood signal. Prioritizing it over the rarely-exploited CVSS 9.8 finding is the modern risk-based approach endorsed by frameworks like SSVC and threat-informed vulnerability management.
- C is incorrect. Treating all findings equally regardless of exploitation data defeats the purpose of prioritization frameworks. Remediation capacity is finite; risk-based ordering is required.
- D is incorrect. Risk acceptance requires formal approval and documentation of business justification. Deferring a 93.1% EPSS finding without compensating controls based on severity threshold alone is not sound vulnerability management.

---

## Question 12 (5 points)

An organization uses a software bill of materials (SBOM) as part of its vulnerability management program. Which capability does an SBOM most directly enable?

- A) Blocking all software updates from untrusted vendors
- B) Automatically patching all software components without analyst involvement
- C) Identifying which applications in the environment contain a specific vulnerable open-source component when a new CVE is disclosed for that component
- D) Replacing the vulnerability scanner for all internal application assessments

Correct Answer: C

Distractor Analysis:

- A is incorrect. An SBOM documents software components; it does not block updates. Update blocking is a policy enforced by application whitelisting or change management controls.
- B is incorrect. An SBOM is a passive inventory document — it enables impact analysis, not automated patching. Patching requires separate tools and processes.
- C is correct. An SBOM is a formal record of every software component (libraries, packages, dependencies) included in an application. When a new CVE is disclosed for a common library (e.g., Log4j), an organization with SBOMs can immediately query them to find every application that includes the vulnerable library version, enabling rapid scope identification.
- D is incorrect. An SBOM documents known components at build time. A vulnerability scanner actively probes running systems for weaknesses including misconfigurations and version-state issues that SBOM records alone cannot detect.

---

## Question 13 (5 points)

A vulnerability assessment report identifies a finding with the following characteristics: exploitable from the network, no privileges required, no user interaction, scope changed, high confidentiality/integrity/availability impact. What is the correct CVSS v3.1 Base Score range for this vulnerability?

- A) 4.0 – 6.9 (Medium)
- B) 7.0 – 8.9 (High)
- C) 9.0 – 10.0 (Critical)
- D) 0.1 – 3.9 (Low)

Correct Answer: C

Distractor Analysis:

- A is incorrect. A Medium score requires lower exploitability or impact values. Network exploitability with no authentication, no user interaction, and full CIA impact is the highest-severity combination.
- B is incorrect. High severity would require some mitigating factor such as requiring privileges, user interaction, or reduced impact. The parameters described maximize all exploitability metrics.
- C is correct. The CVSS vector `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` produces a score of 10.0. Network-accessible (`AV:N`), low complexity (`AC:L`), no privileges (`PR:N`), no user interaction (`UI:N`), scope change (`S:C`), and full impact on all three CIA pillars maximizes the score to the Critical ceiling.
- D is incorrect. Low severity describes findings with significant mitigating factors (local access only, high complexity, or minimal impact). None of those apply here.

---

## Question 14 (5 points)

A vulnerability scanner finds 14 open findings on a critical database server that has not been patched in 18 months. The DBA states: "We cannot patch the database server because patching requires a 4-hour maintenance window and the business will not approve downtime." What is the correct vulnerability management response to this situation?

- A) Accept the situation as-is since patching requires business approval and the business has declined
- B) Escalate to the CISO or risk committee: document the unpatched findings with a formal risk acceptance request requiring executive sign-off, implement compensating controls (network isolation, enhanced monitoring), and schedule the next available maintenance window
- C) Modify the severity ratings in the scanner to Low so the findings no longer trigger SLA requirements
- D) Delete the 14 findings from the vulnerability tracking system to avoid an audit finding

Correct Answer: B

Distractor Analysis:

- A is incorrect. Silently accepting the situation without documentation, compensating controls, or executive awareness is not sound vulnerability management. It creates unacknowledged organizational risk and audit exposure.
- B is correct. The correct response involves three parallel actions: (1) documenting the risk formally through the risk acceptance process with CISO or risk committee approval, (2) implementing compensating controls that reduce the attack surface while patching is pending, and (3) scheduling remediation through the change management process for the next available window.
- C is incorrect. Modifying severity scores to avoid SLA triggers is data manipulation and program integrity violation — it does not reduce actual risk and creates compliance liability.
- D is incorrect. Deleting vulnerability findings from tracking systems is worse than severity manipulation — it destroys the record of known risk, which is a serious audit and compliance violation.

---

## Question 15 (5 points)

An organization's vulnerability management team discovers a critical zero-day vulnerability affecting their web application framework. No vendor patch exists. Which sequence of actions represents the correct initial response?

- A) Wait for the vendor to release a patch before taking any action to avoid making unauthorized configuration changes
- B) Immediately shut down all affected systems permanently until a patch is available
- C) Apply available workarounds or compensating controls (WAF rules, input validation, network segmentation), increase monitoring and logging on affected systems, and register for vendor security advisories to receive patch notification
- D) Exploit the vulnerability internally to understand its impact before determining whether to mitigate

Correct Answer: C

Distractor Analysis:

- A is incorrect. Waiting for a patch without taking compensating action leaves the organization fully exposed. Zero-day vulnerabilities are actively exploited before patches exist — delay is not acceptable.
- B is incorrect. Permanently shutting down affected systems is a disproportionate response that ignores compensating controls. Production systems cannot be shut down indefinitely without severe business impact.
- C is correct. When no patch exists, the response framework calls for: (1) applying vendor-recommended workarounds and security controls (WAF rules, configuration hardening), (2) increasing visibility by enhancing logging and monitoring on affected systems, and (3) tracking the vendor advisory channel for patch availability. This reduces attack surface while maintaining business continuity.
- D is incorrect. Internally exploiting a production vulnerability to understand its impact could cause unintended damage, violate change management policies, and introduce additional risk. Impact assessment should use lab environments or vendor documentation.

---

## Question 16 (5 points)

A vulnerability management team wants to measure the program's overall risk reduction performance. Which combination of metrics provides the most complete picture of program effectiveness?

- A) Total scans run per quarter and total agents deployed
- B) Patch SLA compliance rate, mean time to remediate by severity, percentage of assets with current scan coverage, and open KEV findings outstanding
- C) CVSS average score across all open findings and total CVEs published by NVD per quarter
- D) Number of vulnerability management team members and budget spent on scanner licenses

Correct Answer: B

Distractor Analysis:

- A is incorrect. Counting scans and deployed agents measures operational activity, not risk reduction outcomes. A team could run many scans without remediating any findings.
- B is correct. This combination measures what matters: SLA compliance (are findings being closed on time?), speed of remediation by severity (are Critical findings prioritized?), coverage (are all assets being scanned?), and KEV closure (are actively exploited vulnerabilities being addressed?). Together these metrics provide a risk-reduction performance dashboard.
- C is incorrect. Average CVSS score across all open findings is a risk density metric but does not measure remediation velocity. Total NVD CVE publications are industry-wide statistics outside the organization's control.
- D is incorrect. Headcount and license budget are input metrics — they measure resource investment, not security outcomes.

---

## Question 17 (5 points)

During vulnerability remediation, a system administrator applies a security patch to a production server. Within 2 hours, a critical application begins returning errors. Which vulnerability management process was most likely skipped or inadequate?

- A) The vulnerability scanner was not updated with the latest plugin feed
- B) Patch testing in a staging environment before production deployment
- C) CVSS environmental score calculation for the finding
- D) The post-patch vulnerability rescan

Correct Answer: B

Distractor Analysis:

- A is incorrect. Scanner plugin updates affect detection, not patch behavior. An outdated scanner plugin has no relationship to application errors caused by a patch.
- B is correct. A patch that causes application failures in production should have been tested in a staging or QA environment first. Standard change management and patching procedures require pre-production testing specifically to identify patch-caused regressions before they affect production workloads.
- C is incorrect. CVSS environmental scoring helps prioritize findings — it is a prioritization calculation, not a deployment testing activity. Not calculating an environmental score does not cause application failures.
- D is incorrect. A post-patch rescan verifies the vulnerability is remediated — it occurs after deployment and does not prevent application failures. The failure prevention step is pre-deployment testing.

---

## Question 18 (5 points)

Which of the following most accurately describes the relationship between vulnerability scanning and penetration testing in a comprehensive security program?

- A) They are interchangeable — organizations should choose one or the other based on budget
- B) Vulnerability scanning provides broad automated identification of known weaknesses across all assets; penetration testing provides deep manual validation of whether identified or unknown weaknesses are actually exploitable in the context of the organization's specific environment
- C) Penetration testing replaced vulnerability scanning when CVSS v3.1 was released
- D) Vulnerability scanning is only used for external networks; penetration testing is only used for internal networks

Correct Answer: B

Distractor Analysis:

- A is incorrect. Vulnerability scanning and penetration testing are complementary, not interchangeable. Eliminating one creates significant gaps: no scanning means no systematic coverage of the full asset inventory; no pen testing means no validation that findings are actually exploitable or that unknown issues exist.
- B is correct. Vulnerability scanning provides automated, high-coverage identification of known CVEs and misconfigurations across thousands of assets. Pen testing provides human-driven, context-aware exploitation attempts that validate exploitability, chain vulnerabilities together, and identify weaknesses that automated scanners cannot detect. Both are required for a mature program.
- C is incorrect. CVSS is a severity scoring standard with no relationship to the scope of penetration testing as a practice.
- D is incorrect. Both vulnerability scanning and penetration testing are applied to internal and external network segments. The distinction is methodology and depth, not network location.

---

## Question 19 (5 points)

A vulnerability assessment identifies that a web server is running TLS 1.0, which is a deprecated protocol version with known cryptographic weaknesses. This finding does not have a CVE assigned. How should it be handled in the vulnerability management program?

- A) Ignore the finding entirely since there is no CVE and it cannot be tracked in the vulnerability database
- B) Create a configuration finding in the vulnerability management platform, assign appropriate severity based on the protocol weakness and asset exposure, and schedule remediation to upgrade the server to TLS 1.2 or 1.3
- C) Accept the risk permanently since deprecated protocols are legacy issues that do not represent current threats
- D) Report the issue only to the network team and exclude it from vulnerability management tracking

Correct Answer: B

Distractor Analysis:

- A is incorrect. Vulnerability management programs should track configuration weaknesses and misconfigurations even when no CVE exists. Many high-impact security issues — weak protocol support, default credentials, excessive permissions — are not CVE-tracked but represent significant risk.
- B is correct. A TLS 1.0 implementation on an exposed web server is a meaningful security finding regardless of CVE assignment. It should be documented, risk-rated (considering that TLS 1.0 has exploitable cryptographic weaknesses including POODLE and BEAST), and scheduled for remediation. TLS 1.2 or 1.3 should replace it.
- C is incorrect. TLS 1.0 weaknesses are not merely theoretical legacy concerns. They have been actively exploited. Permanent risk acceptance for an exploitable protocol on an internet-facing server without compensating controls is not defensible.
- D is incorrect. Vulnerability findings affecting security posture should be tracked centrally regardless of which team owns the remediation. Excluding them from the vulnerability program creates visibility gaps and audit exposure.

---

## Question 20 (5 points)

An organization's vulnerability management program uses a risk score formula: `Risk = CVSS_Base × Asset_Criticality × Exploitability_Factor`. The Exploitability_Factor is 2.0 if the CVE appears in CISA KEV and 1.0 if not. A CVSS 7.5 finding on a Critical asset (factor 3) in the KEV catalog produces what effective risk score, and how does it compare to a CVSS 9.8 finding on a Low-criticality asset (factor 1) not in the KEV catalog?

- A) CVSS 7.5 finding: 45; CVSS 9.8 finding: 9.8 — the KEV finding ranks significantly higher despite lower CVSS score
- B) CVSS 7.5 finding: 15; CVSS 9.8 finding: 9.8 — they are roughly equivalent
- C) CVSS 7.5 finding: 7.5; CVSS 9.8 finding: 9.8 — the higher CVSS score always wins in any risk formula
- D) Risk formulas should never be used for prioritization — CVSS Base Score is the only valid prioritization metric

Correct Answer: A

Distractor Analysis:

- A is correct. Applying the formula: CVSS 7.5 × 3 (Critical asset) × 2.0 (KEV) = 45. CVSS 9.8 × 1 (Low asset) × 1.0 (not KEV) = 9.8. The risk formula produces a significantly higher score for the KEV-listed finding on the critical asset, demonstrating how asset criticality and exploitation context can outweigh raw CVSS severity in risk-based prioritization.
- B is incorrect. 7.5 × 3 × 2.0 = 45, not 15. The calculation in this option drops the KEV multiplier.
- C is incorrect. This option ignores the formula entirely. The entire point of risk-based scoring is to incorporate factors beyond CVSS Base Score alone.
- D is incorrect. Risk formulas incorporating asset criticality, exploitability evidence, and environmental context are standard practice in mature vulnerability management programs (SSVC, RBVM frameworks). CVSS Base Score alone is widely recognized as insufficient for prioritization.
