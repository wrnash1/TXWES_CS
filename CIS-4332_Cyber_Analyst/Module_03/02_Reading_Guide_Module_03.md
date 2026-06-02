# Reading Guide: Module 03 - Vulnerability Management: Scanning and Prioritization

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 2 - Vulnerability Management (30%)

---

## Introduction

Vulnerability Management is the second-largest domain on the CySA+ CS0-003 exam at 30% of the total score. It tests your ability to understand the vulnerability lifecycle, interpret scanner output, apply CVSS scoring, prioritize findings using risk-based criteria, and recommend appropriate remediation actions. This guide provides the reference material you need to complete the Module 03 lab and succeed on exam questions drawn from this domain.

---

## Section 1: Vulnerability Management Lifecycle

### 1.1 Five-Phase Lifecycle

| Phase | Description | Key Activities |
|---|---|---|
| Identify | Discover vulnerabilities in the environment | Vulnerability scanning, asset inventory review, penetration test findings, CVE monitoring |
| Analyze | Evaluate each finding for severity and context | CVSS scoring, asset criticality assessment, exploitability research |
| Prioritize | Rank vulnerabilities for remediation order | Risk-based scoring, KEV catalog check, threat intelligence correlation |
| Remediate | Apply fixes or compensating controls | Patching, configuration hardening, network segmentation, risk acceptance |
| Verify | Confirm remediation was effective | Rescan, compliance check, penetration test re-test |

The cycle is continuous. New assets are discovered, new CVEs are published daily, and the program runs without stopping.

### 1.2 Key Concepts

| Term | Definition |
|---|---|
| Vulnerability | A weakness in software, hardware, or configuration that can be exploited |
| Threat | An actor or event capable of exploiting a vulnerability |
| Exposure | A condition that allows a threat to reach a vulnerability |
| Risk | The probability and impact of a threat exploiting a vulnerability through an exposure |
| CVE | Common Vulnerabilities and Exposures; unique identifier for a specific vulnerability |
| NVD | National Vulnerability Database; NIST-maintained repository of CVE data with CVSS scores |
| KEV | Known Exploited Vulnerabilities catalog; CISA-maintained list of CVEs actively exploited in the wild |

---

## Section 2: Vulnerability Scanning

### 2.1 Scanning Modes

| Mode | Also Called | Description | Advantages | Limitations |
|---|---|---|---|---|
| Credentialed | Authenticated | Scanner logs into target system with provided credentials | Highly accurate, low false positives, detects patch state and configuration | Requires credential management; may be intrusive if credentials are over-privileged |
| Uncredentialed | Unauthenticated | Scanner probes target from outside without logging in | Fast, no credential management, simulates attacker view | More false positives, misses patch-level details, limited internal visibility |

Exam note: Credentialed scanning is more thorough and accurate. If asked which type produces more reliable results, the answer is credentialed.

### 2.2 Scanning Perspectives

| Perspective | Description | What It Reveals |
|---|---|---|
| Internal scan | Scanner positioned inside the network perimeter | Services not visible externally, internal management interfaces, backend systems, lateral movement paths |
| External scan | Scanner positioned outside the network perimeter | Internet-facing attack surface, services exposed to the public internet, externally exploitable vulnerabilities |

Best practice: run both internal credentialed scans and external uncredentialed scans regularly.

### 2.3 Scan Frequency Considerations

| Frequency | Use Case | Limitation |
|---|---|---|
| Continuous | High-security environments, compliance-required | Resource-intensive; requires robust infrastructure |
| Weekly | Mid-to-large enterprises | Reasonable balance of coverage and resource use |
| Monthly | Small organizations | Acceptable baseline; misses rapidly emerging CVEs |
| Quarterly | Legacy practice | Insufficient for modern threat environment; not recommended |

### 2.4 Scanning Constraints and Considerations

- Change windows: Scans should align with approved change management windows to avoid unexpected disruptions
- Scan exclusions: Some systems (ICS/OT, medical devices) may require exclusions or specialized scan profiles due to fragility
- Credentialed scan credential hygiene: Scanner credentials should be dedicated service accounts with minimum necessary privileges
- Network segmentation: Scanners must have network access to target segments; a scanner that cannot reach a segment produces no results for that segment

---

## Section 3: CVSS Scoring

### 3.1 CVSS v3.1 Score Ranges

| Score | Severity Label |
|---|---|
| 0.0 | None |
| 0.1 - 3.9 | Low |
| 4.0 - 6.9 | Medium |
| 7.0 - 8.9 | High |
| 9.0 - 10.0 | Critical |

### 3.2 CVSS Base Metrics

| Metric | Options | Description |
|---|---|---|
| Attack Vector (AV) | Network (N), Adjacent (A), Local (L), Physical (P) | How the attacker reaches the vulnerable component |
| Attack Complexity (AC) | Low (L), High (H) | Conditions beyond attacker control required to exploit |
| Privileges Required (PR) | None (N), Low (L), High (H) | Privilege level attacker must possess before exploiting |
| User Interaction (UI) | None (N), Required (R) | Whether a human user must take action for exploitation |
| Scope (S) | Unchanged (U), Changed (C) | Whether exploitation impacts only the vulnerable component or crosses a security boundary |
| Confidentiality Impact (C) | None (N), Low (L), High (H) | Impact on confidentiality of information |
| Integrity Impact (I) | None (N), Low (L), High (H) | Impact on integrity of information |
| Availability Impact (A) | None (N), Low (L), High (H) | Impact on availability of the affected component |

### 3.3 CVSS Metric Groups

| Group | Description | Key Point |
|---|---|---|
| Base Score | Intrinsic vulnerability characteristics; does not change with environment or time | Calculated from the eight Base metrics above |
| Temporal Score | Characteristics that change over time (exploit availability, patch status) | Lowers over time as patches become available and CVE ages |
| Environmental Score | Organization-specific adjustments (asset criticality, mitigations in place) | Customizes base score for specific deployment context |

### 3.4 Interpreting CVSS Scores

A CVSS 9.8 (Critical) score does not mean this vulnerability is the first one you fix. CVSS measures intrinsic severity — how bad the vulnerability is by design. Prioritization must also consider:

- Is there a publicly available exploit?
- Is the vulnerable system internet-facing?
- How critical is the business function this system supports?
- Does any compensating control reduce the effective exposure?

---

## Section 4: Risk-Based Prioritization

### 4.1 Prioritization Factors

| Factor | High Priority Indicators | Low Priority Indicators |
|---|---|---|
| CVSS Score | 7.0 or higher (High/Critical) | 3.9 or lower (Low) |
| Exploitability | Public exploit available; in Metasploit; actively exploited in wild | No known public exploit |
| KEV Catalog | Vulnerability appears on CISA KEV list | Vulnerability not on KEV list |
| Asset Criticality | Crown-jewel systems; PII data stores; auth systems; production | Non-critical; isolated; dev/test |
| Exposure | Internet-facing; externally reachable service | Internally isolated; no external access |
| Compensating Controls | None in place | Existing controls reduce likelihood or impact |

### 4.2 CISA Known Exploited Vulnerabilities Catalog

The CISA KEV catalog is a list of CVEs that have been confirmed as actively exploited in real attacks. Key exam points:

- Federal agencies are required to remediate KEV vulnerabilities within defined timeframes (typically 2 weeks for critical, 6 months for others)
- For private sector organizations, KEV is a best-practice prioritization tool
- A vulnerability's presence on the KEV list makes it immediate remediation priority regardless of CVSS score
- KEV is publicly available and updated regularly

### 4.3 Prioritization Framework Decision Tree

When evaluating a vulnerability for prioritization:

1. Is it on the CISA KEV list? If yes — highest priority; remediate immediately.
2. Is there a public exploit available? If yes — elevate to top of queue.
3. Is the affected system internet-facing? If yes — elevate priority.
4. What is the asset criticality? Crown-jewel systems always elevate priority.
5. What is the CVSS score? Use as a baseline but not the sole determinant.
6. Are compensating controls in place that meaningfully reduce risk? If yes — document and deprioritize appropriately, but do not deprioritize to zero.

---

## Section 5: Remediation Options

### 5.1 Remediation Types

| Option | Description | When to Use |
|---|---|---|
| Patch | Apply vendor-supplied software update | Standard remedy for most software vulnerabilities |
| Configuration Change | Disable service, change settings, remove default credentials | Vulnerabilities caused by misconfiguration |
| Compensating Control | Network segmentation, WAF, additional authentication layer | When patch unavailable or cannot be deployed safely |
| Risk Acceptance | Formally document and accept residual risk | Low-risk findings or when remediation cost exceeds risk |
| System Decommission | Remove the vulnerable system from service | When system is end-of-life and cannot be patched |

### 5.2 Remediation SLAs

Industry best practices and compliance frameworks typically specify remediation SLAs by severity:

| Severity | Recommended Remediation Timeframe |
|---|---|
| Critical | 24-72 hours for actively exploited; 15-30 days standard |
| High | 30 days |
| Medium | 60-90 days |
| Low | 90-180 days |
| Informational | Next scheduled maintenance cycle |

### 5.3 Verification Scanning

After remediation, the vulnerability management program requires a rescan to confirm:

- The specific CVE no longer appears in results for the patched system
- The patch did not introduce new vulnerabilities
- The compensating control effectively prevents exploitation

Verification closes the lifecycle loop and provides documentation for compliance and audit purposes.

---

## Section 6: Vulnerability Report Interpretation

### 6.1 Scan Output Fields

| Field | Description |
|---|---|
| CVE ID | Common Vulnerabilities and Exposures identifier (e.g., CVE-2024-12345) |
| CVSS Score | Numeric severity score from NVD or scanner database |
| Severity Label | None / Low / Medium / High / Critical |
| Plugin/Check ID | Scanner-specific identifier for the detection check |
| Host | Target system IP or hostname |
| Port/Protocol | Network service where the vulnerability was detected |
| Description | Technical description of the vulnerability |
| Solution | Recommended remediation action |
| References | Links to CVE, vendor advisory, NVD entry |

### 6.2 False Positives in Scan Results

False positives occur when the scanner reports a vulnerability that does not actually exist. Common causes:

- Version-based detection without confirming backported patches (common on Linux distributions)
- Outdated scanner signature database
- Incorrect banner grabbing from custom software
- Configuration that resembles a vulnerable state but is actually mitigated

Credentialed scanning significantly reduces false positives by verifying the actual patch state rather than inferring from version numbers.

---

## Section 7: Compliance and Regulatory Context

### 7.1 Vulnerability Scanning in Compliance Frameworks

| Framework | Vulnerability Management Requirement |
|---|---|
| PCI DSS | Quarterly internal and external vulnerability scans; scans after significant changes |
| HIPAA | No explicit scan frequency; requires risk analysis covering technical vulnerabilities |
| NIST SP 800-53 | Continuous monitoring; RA-5 requires scanning at defined frequency |
| ISO 27001 | Risk assessment process must include vulnerability identification |
| SOC 2 | CC7.1 — monitoring for new vulnerabilities; evidence of remediation tracking required |

---

## CySA+ Exam Tips

Exam Tip 1: Know the five vulnerability management lifecycle phases in order. Exam questions describe a phase and ask you to identify it, or give you a phase and ask what happens next.

Exam Tip 2: Credentialed scanning is more accurate than uncredentialed scanning. This appears as a direct question and as a scenario where you must choose the better scan type for a specific goal.

Exam Tip 3: CVSS scores do not determine remediation priority alone. Asset criticality, exploitability, exposure, and KEV status all factor in. Exam scenario questions will present a high CVSS score for a low-criticality system alongside a medium CVSS on a critical internet-facing system and ask which to fix first.

Exam Tip 4: The CISA KEV catalog is tested by name. Know what it is, who maintains it, and why a KEV-listed vulnerability gets immediate priority.

Exam Tip 5: Know all four remediation types: patch, configuration change, compensating control, risk acceptance. Exam questions describe a scenario and ask which remediation type is most appropriate.

Exam Tip 6: Risk acceptance requires documented management sign-off. It is not the same as ignoring a vulnerability. Exam questions may ask what distinguishes risk acceptance from negligence.

Exam Tip 7: False positives in scan results are reduced by credentialed scanning. If asked how to improve scan accuracy, the answer involves credentials.

Exam Tip 8: Scan frequency: continuous is the gold standard. Quarterly is insufficient in modern environments. If asked which frequency is considered best practice, select the most frequent option available.

---

## Glossary

- Attack Vector: CVSS metric describing how an attacker reaches the vulnerable component (Network, Adjacent, Local, Physical)
- Compensating Control: A control that reduces risk when the primary remedy cannot be applied
- CVSS: Common Vulnerability Scoring System; standard for rating vulnerability severity
- CVE: Common Vulnerabilities and Exposures; unique identifier for a specific published vulnerability
- Credentialed Scan: Vulnerability scan where the scanner authenticates to target systems for deeper inspection
- False Positive: Scanner-reported vulnerability that does not actually exist on the system
- KEV: Known Exploited Vulnerabilities catalog; CISA list of CVEs confirmed as actively exploited
- NVD: National Vulnerability Database; NIST-maintained CVE repository with CVSS scores
- Risk Acceptance: Formal management decision to accept residual risk rather than remediate
- Temporal Score: CVSS modifier reflecting exploit availability and patch status
- Uncredentialed Scan: Vulnerability scan without system credentials; simulates external attacker view
- Verification Scan: Rescan performed after remediation to confirm vulnerability no longer present
- Vulnerability: A weakness in software, hardware, or configuration that can be exploited

---

## Required Resources

- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com
- CISA Known Exploited Vulnerabilities catalog: cisa.gov/known-exploited-vulnerabilities-catalog
- NIST National Vulnerability Database: nvd.nist.gov

---

## Study Checklist

- [ ] List the five vulnerability management lifecycle phases without notes
- [ ] Explain the difference between credentialed and uncredentialed scanning and when to use each
- [ ] State the CVSS v3.1 score ranges for all five severity labels
- [ ] Name all eight CVSS Base metrics and their option sets from memory
- [ ] Explain why CVSS score alone is insufficient for prioritization
- [ ] Name the CISA KEV catalog and explain its role in prioritization decisions
- [ ] Describe the four remediation types and give an example of when each is appropriate
- [ ] Explain what constitutes a false positive in scan results and how to reduce them
- [ ] Review all eight exam tips
- [ ] Complete the Module 03 Lab
- [ ] Complete the Module 03 Quiz
- [ ] Post initial response to the Module 03 Discussion board by Wednesday at 11:59 PM
