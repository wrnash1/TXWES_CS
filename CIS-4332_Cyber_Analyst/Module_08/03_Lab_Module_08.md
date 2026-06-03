# Lab Activity: Module 08 — Vulnerability Management

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Lab Overview

In this lab you will apply vulnerability management skills to a realistic set of scanner findings. You will perform CVSS score interpretation, apply risk-based prioritization logic, research CVEs using the NVD and CISA KEV catalog, and produce a prioritized remediation plan with SLA targets. You will also evaluate two remediation options for a critical finding and justify your recommendation.

- Total Points: 100
- Estimated Completion Time: 75–90 minutes
- Submission: Upload your completed Lab Report to Canvas, Module 08 Lab assignment

---

## Learning Objectives

By completing this lab you will be able to:

- Interpret CVSS v3.1 vector strings and calculate implied severity factors
- Apply CISA KEV status, EPSS context, and asset criticality to vulnerability prioritization
- Use the NVD to research CVE details and identify remediation information
- Produce a risk-based prioritized remediation plan with SLA assignments
- Evaluate remediation options and justify the appropriate choice

---

## Tools and Resources

All tools are free and browser-based:

- NVD (National Vulnerability Database): `https://nvd.nist.gov`
- CISA KEV Catalog: `https://www.cisa.gov/known-exploited-vulnerabilities-catalog`
- CVSS v3.1 Calculator: `https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator`
- EPSS Data: `https://www.first.org/epss`
- CVE Details: `https://cvedetails.com` (supplemental)

---

## Exercise 1 — CVSS Interpretation and Scoring (30 points)

### Exercise 1 Background

The following five vulnerabilities were identified in a recent authenticated vulnerability scan. Each is presented with its CVE identifier and CVSS v3.1 vector string. You must interpret the vector, identify the severity factors, and research each CVE using the NVD.

### Vulnerability Dataset

```text
Finding 1:
  CVE: CVE-2021-44228 (Log4Shell)
  Affected Asset: APP-SERVER-03 (Java application server, internet-facing)
  CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
  CISA KEV: YES (added 2021-12-10)

Finding 2:
  CVE: CVE-2020-1472 (Zerologon)
  Affected Asset: CORP-DC-01 (Primary domain controller, internal only)
  CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
  CISA KEV: YES (added 2021-11-03)

Finding 3:
  CVE: CVE-2022-30190 (Follina / MSDT)
  Affected Asset: 47 Windows workstations (standard user accounts)
  CVSS Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
  CISA KEV: YES (added 2022-06-14)

Finding 4:
  CVE: CVE-2019-11510 (Pulse Secure VPN)
  Affected Asset: VPN-GW-01 (internet-facing VPN gateway)
  CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
  CISA KEV: YES (added 2021-11-03)

Finding 5:
  CVE: CVE-2018-13379 (Fortinet FortiOS SSL VPN)
  Affected Asset: LEGACY-VPN-02 (secondary VPN gateway, not internet-facing)
  CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
  CISA KEV: YES (added 2021-11-03)
```

### Task 1A — CVSS Vector Analysis (20 points)

For each of the five vulnerabilities, complete the following analysis (4 points each):

1. Decode the CVSS vector string — for each metric in the vector, state the metric name, its value abbreviation, and what that value means in plain language.
2. Identify which two metrics in this vector contribute most significantly to the high score and explain why.
3. Use the NVD to look up the CVE. In 2–3 sentences, describe what the vulnerability is and what an attacker could do if they exploited it.

### Task 1B — CVSS Score Comparison (10 points)

Findings 1 and 2 (Log4Shell and Zerologon) share identical CVSS vector strings and identical scores of 10.0. Yet a security professional would likely prioritize them differently in practice.

In 5–7 sentences, explain:

1. Why two vulnerabilities with identical CVSS v3.1 Base Scores may require different prioritization
2. Specifically, what contextual factors make CVE-2021-44228 (Finding 1) potentially higher urgency for the organization described
3. What Environmental Score adjustment you might apply to Finding 2 based on the asset context described (domain controller, internal only, no external access)

---

## Exercise 2 — Risk-Based Prioritization (35 points)

### Exercise 2 Background

In addition to the five CVEs above, your organization's vulnerability scan also returned the following four findings from a broader scan of internal systems:

```text
Finding 6:
  CVE: CVE-2023-44487 (HTTP/2 Rapid Reset — DDoS)
  Affected Asset: PUBLIC-WEB-01 (public-facing web server)
  CVSS Base Score: 7.5 (High)
  CISA KEV: YES
  EPSS Score: 0.73 (73% probability of exploitation within 30 days)
  Asset Criticality: HIGH — customer-facing revenue application

Finding 7:
  CVE: CVE-2023-20198 (Cisco IOS XE Web UI RCE)
  Affected Asset: CORE-SWITCH-01 (core network switch)
  CVSS Base Score: 10.0 (Critical)
  CISA KEV: YES
  EPSS Score: 0.91
  Asset Criticality: CRITICAL — loss would disrupt all network connectivity

Finding 8:
  CVE: CVE-2022-41082 (ProxyNotShell — Exchange RCE)
  Affected Asset: MAIL-SRV-01 (on-premises Exchange email server)
  CVSS Base Score: 8.8 (High)
  CISA KEV: YES
  EPSS Score: 0.45
  Asset Criticality: HIGH — organization-wide email system

Finding 9:
  CVE: CVE-2015-10049 (Hypothetical legacy app — local privilege escalation)
  Affected Asset: DEV-VM-07 (developer sandbox VM, no production data,
                              no external network access)
  CVSS Base Score: 7.2 (High)
  CISA KEV: NO
  EPSS Score: 0.02
  Asset Criticality: LOW — isolated development environment
```

### Task 2A — Comprehensive Prioritization (20 points)

Using all nine findings (Findings 1–9), produce a complete prioritized remediation list. Your list must:

1. Rank all nine findings from highest to lowest priority
2. Assign a remediation SLA (Emergency/7 days, High/15 days, Standard/30 days, Routine/90 days, or Acceptance) to each finding
3. Provide a 2–3 sentence justification for the ranking of each of the top four findings

Your justification must reference at least three of the following factors for each top-four finding: CVSS score, KEV status, EPSS score, asset criticality, external exposure.

### Task 2B — Prioritization Framework Justification (15 points)

In 6–8 sentences, answer the following:

1. Compare the prioritization of Finding 7 (Cisco IOS XE, CVSS 10.0, KEV, critical asset) versus Finding 2 (Zerologon, CVSS 10.0, KEV, domain controller, internal only). Both have identical CVSS scores and KEV status. What factors differentiate their priority ranking, and which do you prioritize first?

2. Finding 9 (CVE-2015-10049) has a CVSS 7.2 High score but you likely ranked it near the bottom. Explain how you justified this placement to a manager who argues that "High severity vulnerabilities must be patched within 30 days per policy."

3. What risk does the low-CVSS-but-high-EPSS pattern (Finding 6 — CVSS 7.5, EPSS 0.73) illustrate about relying solely on CVSS for prioritization?

---

## Exercise 3 — NVD Research and Remediation Planning (25 points)

### Exercise 3 Background

Select any two of the nine findings from Exercises 1 and 2. For each selected finding, perform a full NVD research exercise.

### Task 3A — NVD Research (15 points)

For each of your two selected CVEs, complete the following (7.5 points each):

1. Navigate to `https://nvd.nist.gov` and look up the CVE. Screenshot or transcribe:
   - The full CVE description
   - The CVSS v3.1 Base Score and vector string as listed by NVD
   - The CWE (Common Weakness Enumeration) classification
   - The vendor advisory or patch link from the References section

2. In 3–4 sentences, describe the remediation action — what specific patch or version update resolves this vulnerability? Is there a workaround documented?

3. In 2–3 sentences, explain what CWE classification means and what category of software weakness this vulnerability represents.

### Task 3B — Remediation Plan for One Critical Finding (10 points)

Select one of your two researched CVEs — it must be rated Critical or High. Write a structured remediation plan for this finding that includes:

- Finding Summary: CVE ID, affected asset, CVSS score, KEV status
- Business Impact: What would happen if this vulnerability were exploited? (3–4 sentences)
- Immediate Mitigation: What can be done right now to reduce risk while the full patch is prepared? (3–4 sentences)
- Patch Plan: What is the specific patch to apply, what testing is required, and what is the deployment timeline? (3–4 sentences)
- Verification: How will you confirm successful remediation? (2–3 sentences)
- Risk Acceptance Fallback: If the patch cannot be applied within the SLA, what compensating controls and documentation are required? (2–3 sentences)

---

## Exercise 4 — Remediation Option Analysis (10 points)

### Exercise 4 Background

Your organization has identified CVE-2022-30190 (Follina/MSDT — Finding 3) on 47 Windows workstations. The vulnerability requires user interaction (UI:R) — specifically, a user must open or preview a specially crafted Office document. Your organization has three workstations that process sensitive documents from external vendors and cannot have standard document-preview disabled without business impact.

Your security team has three remediation options:

- Option A: Apply the official Microsoft security update to all 47 workstations. Testing required — pilot group deployment first due to known compatibility issue with legacy accounting software on 8 of the 47 workstations.

- Option B: Apply the official workaround from Microsoft Security Advisory (disable MSDT URL handler via registry) to all 47 workstations immediately, then follow with the official patch when compatibility is confirmed.

- Option C: Deploy a compensating control — update email filtering rules to block .docx and .rtf attachments from external senders on the 3 sensitive-document workstations only; accept residual risk on the remaining 44 workstations.

### Task 4A — Remediation Option Recommendation (10 points)

In 6–8 sentences, recommend one of the three options and justify your choice. Your answer must:

1. Explain why you selected your recommended option over the other two
2. Explain what risk remains after your recommended option is implemented
3. Describe what verification step you would take to confirm the chosen option is effective
4. Identify any exception or risk acceptance documentation that would be required

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| 1A — CVSS Vector Analysis (5 CVEs) | 20 | 4 pts each: full decode, key metric identification, NVD description |
| 1B — CVSS Score Comparison | 10 | Contextual factors identified; environmental score adjustment explained |
| 2A — Prioritization List | 20 | 9 findings ranked; SLAs assigned; top-4 justified with 3+ factors |
| 2B — Framework Justification | 15 | CVSS vs. context; policy vs. risk arguments; CVSS/EPSS gap explained |
| 3A — NVD Research (2 CVEs) | 15 | Full NVD data; remediation action; CWE classification explained |
| 3B — Remediation Plan | 10 | All six sections complete; specific patch referenced; verification described |
| 4A — Option Recommendation | 10 | Option justified; residual risk acknowledged; verification step; documentation |
| Total | 100 | |

---

## Submission Instructions

1. Use a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Include NVD screenshots or transcribed data for Task 3A.
4. Present prioritization rankings in a clearly formatted table.
5. Submit to the Canvas Module 08 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

CVE data used in this lab is real and publicly available. Research must be performed independently. Do not share NVD research findings or prioritization lists with classmates before submission. All analysis and written justifications must be your own work.
