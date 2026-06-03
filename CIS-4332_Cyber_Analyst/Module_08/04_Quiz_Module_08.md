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
