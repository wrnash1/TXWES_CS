# Reading Guide: Module 13 — Penetration Test Report Writing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

The penetration test report is the primary deliverable of any engagement. Technical skill without effective communication produces limited value for the client. This reading guide covers report structure, CVSS scoring, finding writing standards, executive communication, and professional delivery practices aligned with PT0-002 Domain 4.

---

## Learning Objectives

After completing this module, students will be able to:

1. Identify the standard sections of a penetration test report and explain their purpose.
2. Write an executive summary that communicates risk to non-technical stakeholders.
3. Write complete technical findings including all required components.
4. Calculate CVSS 3.1 Base Scores using the metric framework.
5. Apply temporal and environmental CVSS metrics to adjust for client context.
6. Develop tiered remediation recommendations with realistic timelines.
7. Communicate findings professionally in written and verbal formats.

---

## Section 1: Report Architecture

### 1.1 Standard Report Components

A professional penetration test report contains the following sections in order:

**Cover Page:** Client name, report title, date, classification marking, testing firm logo and contact.

**Document Control:** Version history, distribution list with delivery dates, revision notes. Each distribution copy should be numbered or tracked.

**Confidentiality Notice:** Legal language asserting the report's confidential status and limiting distribution to authorized personnel. This language protects both the client (vulnerabilities are not disclosed) and the tester (professional liability).

**Table of Contents:** Navigational aid. Long reports (50+ pages) benefit from section bookmarks in PDF format.

**Executive Summary:** 1–3 pages maximum. Primary audience: executives and board members. Scope, overall posture, key findings (plain language), and priority actions.

**Assessment Scope and Methodology:** Technical description of what was tested, testing period, tools used, methodologies followed, and limitations.

**Findings Summary:** A table or matrix showing all findings with severity and affected systems at a glance. Readers can see the full picture before diving into individual findings.

**Detailed Findings:** The core technical section. One finding per page (minimum) or more. Each finding follows the standard structure.

**Appendices:** Raw tool output, full port scan results, testing timeline, acronym glossary, references.

### 1.2 Document Control and Handling

The document control section establishes the report's chain of custody. Each version should be identified:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Author] | Initial draft |
| 1.0 | [Date] | [Author] | Final release |

The distribution list documents who received the report and when. This matters if the report is later involved in a legal proceeding — demonstrating that only appropriate personnel received the document.

Classification markings should appear in the header or footer of every page: "CONFIDENTIAL — [Client Name] — Not for Public Distribution."

### 1.3 Report Classification and Handling

Penetration test reports contain highly sensitive information — specifically, a roadmap of exploitable vulnerabilities with evidence of exploitation. Handling requirements:

- Store in encrypted format (password-protected PDF with AES-256, or encrypted file container)
- Transmit via encrypted channel (PGP email, secure file portal)
- Do not email unencrypted reports even to the client
- Implement a retention and destruction policy in the contract
- Never include client reports in personal portfolios without explicit, written client permission

---

## Section 2: Executive Summary Writing

### 2.1 Audience Analysis

The executive summary serves readers who:

- May have limited technical background
- Are making business decisions about security investment
- Have limited time to read the full report
- Are accountable to boards, regulators, and shareholders for security posture

These readers need: What is the overall situation? What is at risk? What do we need to do immediately? What will it cost if we do not act?

They do not need: Technical vulnerability mechanics, CVE numbers (without explanation), protocol details, or tool names.

### 2.2 Writing the Overall Posture Assessment

The overall security posture assessment is a qualitative summary statement supported by the finding distribution. Options:

**Qualitative descriptions:** "The organization's security posture is assessed as High Risk, with multiple critical and high-severity vulnerabilities presenting immediate exploitation risk."

**Risk matrix summary:** "The assessment identified 2 Critical, 5 High, 8 Medium, and 4 Low findings across web applications, internal infrastructure, and network configuration."

**Comparison to maturity model:** "The organization's current security controls represent an early-stage security program (NIST CSF Tier 1 — Partial). Core capabilities in Detection and Response require significant investment."

### 2.3 Key Findings in Executive Language

Translate each top finding using this framework:

1. What is vulnerable? (Business asset, not technical artifact)
2. What can an attacker do? (Business outcome, not technical action)
3. How difficult is it? (Skill required, time required)
4. What should be done? (Specific action, realistic timeline)

Example transformation:

**Technical:** "Unauthenticated SSRF in the internal request proxy at port 8080 enables reading of AWS EC2 instance metadata including IAM role credentials."

**Executive:** "An attacker can access the company's cloud infrastructure management system without a password by exploiting a flaw in the internal server. This could allow them to access or delete data stored in the company's cloud environment, including customer records."

### 2.4 Priority Action Items

The executive summary should conclude with 3–5 prioritized actions:

- Use active verbs: "Apply the available patch to the web application server."
- Specify timeline: "Immediately (within 48 hours)"
- Reference business impact: "to prevent unauthorized access to the customer database"

---

## Section 3: Technical Finding Structure

### 3.1 Required Finding Components

Every technical finding must include all of the following:

**Title:** Descriptive, consistent naming convention. Reference the vulnerability type and affected component.

**Risk Rating:** Critical / High / Medium / Low / Informational. Include the basis for the rating.

**CVSS Score:** Version 3.1 Base Score with full vector string. Include temporal score if relevant.

**Description:** 3–5 sentences. What is the vulnerability? Where does it exist? How was it confirmed?

**Evidence:** Minimum one screenshot or command output per finding. Evidence must show the testing system's identifier (IP, hostname) and a timestamp.

**Impact:** What can an attacker accomplish? State the worst plausible outcome.

**Affected Assets:** Specific host, URL, service, or system identifier.

**Remediation (Immediate):** 0–30 day action. Configuration change, patch, disable.

**Remediation (Long-term):** 30–90+ day action. Code fix, architecture change, vendor upgrade.

**References:** CVE identifier, NVD link, vendor advisory, relevant security standard.

### 3.2 Evidence Documentation Standards

Evidence quality directly affects report credibility:

**Screenshots:** Use full-screen or browser-window captures, never cropped to show only the "interesting" part. Context around the key finding is critical. Include browser address bar, response code, and timestamp.

**Command output:** Include the exact command issued, the system it was run from (hostname or IP), and the full output (not just the interesting lines). Truncated output raises reproducibility questions.

**Video evidence:** Screen recordings can document complex attack chains that screenshots miss. Include these in appendices or reference them as supplemental evidence.

**Timestamps:** All evidence should be timestampable to the engagement period. If a screenshot lacks a timestamp, annotate it with the date and time from your testing log.

### 3.3 Finding Writing Anti-Patterns

Avoid these common errors:

**Vague descriptions:** "The system has a vulnerability." Specific descriptions of affected parameters, versions, and conditions are required.

**Overstated impact:** "An attacker can compromise the entire organization." State the actual demonstrated impact with evidence.

**Unsupported ratings:** A Critical rating without evidence of actual exploitation or a specific high-impact scenario is not credible.

**Missing remediation:** A finding without remediation guidance is an incomplete finding.

**Template language:** "This vulnerability is commonly exploited in the wild" without specific references is padding. Support assertions with references.

---

## Section 4: CVSS 3.1 Reference

### 4.1 Base Metric Group

| Metric | Values | Notes |
|--------|--------|-------|
| Attack Vector (AV) | N/A/L/P | Network is highest severity |
| Attack Complexity (AC) | L/H | Low = no special conditions required |
| Privileges Required (PR) | N/L/H | None = no authentication required |
| User Interaction (UI) | N/R | None = no victim action required |
| Scope (S) | U/C | Changed = impacts beyond vulnerable component |
| Confidentiality (C) | N/L/H | High = complete information disclosure |
| Integrity (I) | N/L/H | High = complete data modification |
| Availability (A) | N/L/H | High = complete resource unavailability |

### 4.2 Common Scoring Patterns

**Remote unauthenticated code execution:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H = 10.0 Critical

**Authenticated privilege escalation (local):** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H = 7.8 High

**Reflected XSS (user interaction required):** AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N = 6.1 Medium

**Information disclosure (internal only):** AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N = 4.0 Medium

**Default credentials on administrative interface:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H = 9.8 Critical

### 4.3 Environmental Metric Adjustment

Environmental adjustments reflect the specific deployment. Key adjustments:

If a Critical finding affects a DMZ server with no access to sensitive data, the environmental Confidentiality Requirement might be Low (CR:L), reducing the effective score.

If a High finding affects a system processing regulated financial data, increasing the environmental Integrity and Availability Requirements to High may increase the effective score.

Document the basis for environmental adjustments in the finding's narrative.

---

## Section 5: Remediation Framework

### 5.1 Tiered Remediation Timelines

| Severity | Short-term (Emergency) | Long-term (Permanent) |
|----------|----------------------|----------------------|
| Critical | 0–48 hours | 30 days |
| High | 7 days | 60 days |
| Medium | 30 days | 90 days |
| Low | 90 days | As resources permit |

These timelines are guidelines, not hard rules. Document reasoning when deviating.

### 5.2 Remediation Types

**Patch application:** Vendor-supplied fix. Specify the vendor advisory, the patch version, and the testing recommendation before production deployment.

**Configuration change:** Disable a feature, change a setting, restrict permissions. Highly actionable and often immediate.

**Architecture change:** Redesign a network segment, implement network segmentation, deploy additional security controls. Longer timeline but addresses root cause.

**Code remediation:** Fix a custom application's vulnerable code. Requires development resources and testing.

**Process change:** Update a security policy, implement training, change operational procedures. Necessary but slower to take effect.

**Compensating control:** When the vulnerable component cannot be immediately fixed, a compensating control reduces risk: WAF rule, network ACL, enhanced monitoring.

---

## Section 6: PT0-002 Exam Alignment

### 6.1 Report Component Knowledge

The PT0-002 exam tests whether students know the components and purpose of each report section. Be able to identify:

- Which section a specific type of content belongs in
- The difference between executive summary and technical findings audience and tone
- The required components of a complete technical finding
- The purpose of a findings summary matrix

### 6.2 CVSS Scoring on the Exam

The exam presents scenarios and asks students to identify the correct CVSS metric values. Practice scenarios:

"A vulnerability requires no authentication, can be exploited remotely, and gives the attacker full control of the server." — AV:N, AC:L, PR:N, UI:N, S:C, C:H, I:H, A:H

"A bug in the company's internal HR application requires an authenticated low-privilege user and only affects the HR system." — AV:N, AC:L, PR:L, UI:N, S:U, with impacts dependent on data sensitivity.

---

## Key Terms

**CVSS:** Common Vulnerability Scoring System — quantitative vulnerability severity framework.

**Base Score:** The CVSS score reflecting intrinsic vulnerability characteristics, independent of temporal and environmental factors.

**Vector string:** The compact notation encoding all CVSS metric values: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Executive summary:** The report section written for non-technical decision-makers.

**Finding:** A documented vulnerability including all required components.

**Evidence:** Captured proof of a finding's existence — screenshots, command output, network captures.

**Remediation:** Specific, actionable guidance for eliminating or mitigating a finding.

**Risk acceptance:** Client documentation of a decision to acknowledge and accept a finding without immediate remediation.

---

## Review Questions

1. What is the difference between the CVSS Base Score and the Environmental Score? When should a penetration tester apply environmental adjustments?

2. Write an executive-level description (3 sentences maximum) of the following finding: "The SMTP server at mail.corp.internal allows NTLM authentication in cleartext over port 587, enabling passive capture of domain credentials."

3. A client argues that a Critical-rated finding should be downgraded to High because they have a WAF deployed that blocks the attack vector. How should the tester respond, and where in the report is this disagreement documented?

4. What is the minimum evidence required to document a finding that the tester believes is present but cannot fully confirm? How does the uncertainty affect the CVSS temporal score?

5. List the five required elements of an executive summary and explain why each matters to a non-technical decision-maker.

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives, Domain 4.1, 4.2
- CVSS 3.1 Specification Document: https://www.first.org/cvss/specification-document
- NIST NVD CVSS Calculator: https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator
- PTES (Penetration Testing Execution Standard): http://www.pentest-standard.org/index.php/Reporting
- Weidman, G. (2014). *Penetration Testing.* No Starch Press. Chapter 16: Working with the Report.
