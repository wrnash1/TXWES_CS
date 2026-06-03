# Lab Activity: Module 14 — Penetration Testing Reports

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication

---

## Objective

In this lab you will draft a structured penetration testing report section covering two
confirmed vulnerability findings from a provided scenario. You will practice all six
required finding components, apply CVSS 3.1 scoring, write executive-appropriate impact
statements, and produce a properly classified report header and attestation block. By
completing this lab you will be prepared for both exam scenario questions and real-world
reporting deliverables.

---

## Prerequisites

- Complete the Module 14 video lecture and reading guide before beginning
- Have access to a word processor or Markdown editor (VS Code, Obsidian, or Google Docs
  are all acceptable)
- Optional but recommended: open the
  [NIST CVSS Calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator) in a browser
  tab to assist with scoring

---

## Scenario Background

You are a penetration tester who has completed a two-week external and internal assessment
for Meridian Financial Services, a fictional mid-size financial institution. The authorized
scope included one external IP range (`203.0.113.0/28`) and one internal subnet
(`10.10.5.0/24`). Testing occurred from 2026-05-19 through 2026-05-30.

During the engagement, you confirmed the following two vulnerabilities:

**Vulnerability A**: The external-facing web application login page at
`https://203.0.113.10/login` is vulnerable to SQL injection. Using sqlmap with default
settings, you extracted the `users` table from the `meridian_app` database, which contained
4,200 records including usernames, bcrypt password hashes, and email addresses. The
application runs Apache Tomcat 9.0.41 on a Linux host. No authentication was required to
reach the login page. The database server is Microsoft SQL Server 2017.

**Vulnerability B**: An internal Windows Server 2016 host at `10.10.5.22` is running SMB
v1 and has not been patched against MS17-010 (EternalBlue). Using the Metasploit module
`exploit/windows/smb/ms17_010_eternalblue`, you obtained a SYSTEM-level Meterpreter session.
The host is the domain file server storing accounting documents. It is reachable only from
within the internal network — not from the internet.

---

## Step-by-Step Instructions

### Part 1 — Report Header and Classification Block (15 minutes)

Create a report cover page block containing the following elements. Format it as you would
the first page of a professional report document.

1. Report title: "Penetration Test Assessment Report — Meridian Financial Services"
2. Classification marking: CONFIDENTIAL
3. Engagement dates: 2026-05-19 through 2026-05-30
4. Scope summary: One sentence describing the authorized scope
5. Prepared by: Your name and course section
6. Handling statement: A two-sentence statement restricting unauthorized distribution

Verify that your classification marking appears at both the top and bottom of the page.

### Part 2 — Executive Summary Section (20 minutes)

Write a 150–200 word executive summary for the Meridian Financial Services engagement.

Your executive summary must include:

1. Overall risk posture (use one of: Critical / High / Medium / Low and justify briefly)
2. A two-to-three sentence narrative describing the most significant findings in business
   terms — no tool names, no CVE numbers, no technical jargon
3. A prioritized remediation list with three action items ranked by urgency
4. A one-sentence attestation statement

Write this section as if the reader is the Chief Information Officer. They understand
business risk but not exploit techniques.

### Part 3 — CVSS Scoring Exercise (20 minutes)

Score both vulnerabilities using CVSS 3.1. For each vulnerability, document all eight Base
metrics and calculate the Base Score using the NIST CVSS Calculator.

**Vulnerability A — SQL Injection scoring worksheet:**

Complete the table below by filling in the value (and your justification) for each metric:

| Metric | Your Value | Justification |
|--------|------------|---------------|
| Attack Vector (AV) | | |
| Attack Complexity (AC) | | |
| Privileges Required (PR) | | |
| User Interaction (UI) | | |
| Scope (S) | | |
| Confidentiality (C) | | |
| Integrity (I) | | |
| Availability (A) | | |
| **Base Score** | | |
| **Severity** | | |

**Vulnerability B — MS17-010 scoring worksheet:**

Complete the same table for the EternalBlue finding. Note that this host is not
internet-accessible. After calculating the Base Score, determine whether your reported risk
rating should differ from the raw CVSS score, and if so, explain why.

### Part 4 — Full Finding Entries (40 minutes)

Write a complete technical finding entry for each vulnerability. Each entry must contain all
six required components.

**Finding FIND-001 (Vulnerability A):**

1. **Title** — Write a specific, descriptive title following the format:
   `[Vulnerability Class] in [Location] Allows [Consequence] ([CVE or CWE])`
2. **Description** — Three to five sentences explaining the vulnerability class, root cause,
   and how it manifests in this specific application. Reference the applicable CWE.
3. **Evidence** — Write the evidence summary as it would appear in a report. Include:
   - The sqlmap command used (as a code block)
   - A description of the screenshot or output you captured
   - The number of records extracted and data types confirmed
4. **Impact** — Two to three sentences describing the business consequence. Reference
   applicable regulations (this is a financial institution — consider PCI-DSS and GLBA).
5. **CVSS Score and Risk Rating** — Use your score from Part 3. Include the full vector
   string in this format: `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L`
6. **Remediation** — Provide both a short-term mitigation and a long-term fix. Reference
   OWASP A03:2021 (Injection) guidance.

**Finding FIND-002 (Vulnerability B):**

Complete all six components for the EternalBlue finding. For the remediation, provide
the specific Microsoft patch identifier and the Group Policy setting that disables SMBv1.

### Part 5 — Findings Summary Table (10 minutes)

Create a findings summary table listing both findings with the following columns:

| Finding ID | Title (short) | Affected Asset | Risk Rating | Remediation Priority |
|------------|---------------|----------------|-------------|----------------------|

Remediation Priority should be: Immediate (24–48 hrs), Short-term (1–2 weeks), or
Medium-term (30 days).

---

## Deliverables

Submit a single document to the Canvas assignment portal containing:

1. Report header and classification block (Part 1)
2. Executive summary section (Part 2)
3. CVSS scoring worksheets for both vulnerabilities (Part 3)
4. Two complete finding entries, FIND-001 and FIND-002 (Part 4)
5. Findings summary table (Part 5)
6. A brief reflection (100–150 words) answering: What was the most challenging component
   to write, and why does that component matter to the client?

---

## Grading Criteria

| Component | Points |
|-----------|--------|
| Report header with correct classification | 10 |
| Executive summary — appropriate audience and tone | 15 |
| CVSS worksheets — accurate metric selection with justification | 20 |
| FIND-001 — all six components present and complete | 20 |
| FIND-002 — all six components present and complete | 20 |
| Findings summary table | 10 |
| Reflection response | 5 |
| **Total** | **100** |

---

## Troubleshooting Guide

- **Unsure about CVSS metric values**: Use the NIST CVSS 3.1 calculator at
  `nvd.nist.gov/vuln-metrics/cvss/v3-calculator`. Each metric has a built-in description
  of what each value means.
- **Not sure if impact statement is too technical**: Read it aloud and ask: "Would a
  non-security business executive understand this sentence?" If the answer is no, revise.
- **Remediation too vague**: Every remediation should answer: "What exactly does the
  system administrator click, type, or configure to fix this?" Generic statements like
  "update the software" are insufficient.
