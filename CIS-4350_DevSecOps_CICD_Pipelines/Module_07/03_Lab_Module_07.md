# Lab Activity: Module 07 - DAST: Dynamic Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Explain the operational difference between SAST and DAST in a CI/CD pipeline context.
- Configure a GitHub Actions workflow step that runs an OWASP ZAP baseline scan against a staging URL.
- Interpret a DAST finding report, identifying vulnerability class, severity, and remediation.
- Describe the authenticated scanning requirement and when it is necessary.

---

## Prerequisites

Before beginning this lab, confirm the following:

- Docker is installed and running (`docker --version`).
- You have completed Module 07 video and reading guide.
- You have access to the GitHub repository from previous modules.

Note: For Parts 1 and 2, you will analyze provided DAST output rather than running a live scan against a real application, so a staging environment is not required for these parts. Part 3 requires Docker for a local scan against a public test application.

---

## Part 1: DAST vs. SAST Comparison Analysis (25 points)

### Part 1 Background

Understanding when DAST is required versus when SAST is sufficient is a core DevSecOps Professional exam skill.

### Part 1 Scenario

A security engineer joins a team that has SAST integrated into every pull request via Semgrep. The team claims their pipeline is "secure" and asks whether DAST is necessary given that SAST already runs on every commit.

### Part 1 Instructions

**Step 1: Identify five vulnerabilities DAST would find that SAST would miss.**

For each vulnerability, provide: the vulnerability name and CWE number, a 2-sentence explanation of why SAST cannot detect it at code analysis time, and a concrete example HTTP request or scenario that DAST would use to detect it.

**Step 2: Write a one-page recommendation memo.**

Write a 200-250 word memo to the security engineer explaining why DAST is a necessary complement to SAST, not a redundant tool. Address: what SAST finds, what DAST finds, where each runs in the pipeline, and the defense-in-depth argument for running both.

### Part 1 Deliverable

Submit your five-vulnerability analysis and the recommendation memo.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Five vulnerabilities identified with correct CWE numbers | 10 |
| Each vulnerability has accurate explanation of why SAST misses it | 10 |
| Recommendation memo is technically accurate and within word count | 5 |

---

## Part 2: DAST Finding Report Analysis (30 points)

### Part 2 Background

Interpreting DAST findings is a required skill for DevSecOps practitioners and is tested on the exam.

### Part 2 Finding Report

The following ZAP baseline scan findings were produced against a staging web application:

```text
WARN-NEW: Cookie Without Secure Flag [10011]
  URL: https://staging.myapp.com/login
  Evidence: Set-Cookie: session=abc123; HttpOnly; Path=/
  Description: A cookie has been set without the secure flag.
  An attacker may be able to read the cookie's value by snooping
  the traffic between the browser and server.
  CWE: 614
  OWASP: A05:2021 - Security Misconfiguration

WARN-NEW: Missing Anti-clickjacking Header [10020]
  URL: https://staging.myapp.com/
  Evidence: No X-Frame-Options or Content-Security-Policy frame-ancestors header found.
  Description: The response does not include either Content-Security-Policy with 'frame-ancestors'
  directive or X-Frame-Options to protect against Clickjacking attacks.
  CWE: 1021
  OWASP: A05:2021 - Security Misconfiguration

FAIL-NEW: SQL Injection [40018]
  URL: https://staging.myapp.com/search?q=test
  Parameter: q
  Evidence: 1 AND 1=1 -- injection string returned database error: syntax error near "1=1"
  CWE: 89
  OWASP: A03:2021 - Injection
```

### Part 2 Instructions

**Step 1: Analyze Finding 1 — Cookie Without Secure Flag.**

Write a structured analysis: vulnerability name and CWE, what the finding means (what is missing and why it matters), attack scenario (how could an attacker exploit this?), and the specific remediation — write the corrected `Set-Cookie` header value.

**Step 2: Analyze Finding 2 — Missing Anti-clickjacking Header.**

Write a structured analysis covering the same four elements. Include two valid HTTP response header solutions (X-Frame-Options and Content-Security-Policy with frame-ancestors).

**Step 3: Analyze Finding 3 — SQL Injection.**

Write a structured analysis covering the same four elements. This finding was detected by both SAST (Module 06) and now DAST — explain what additional information DAST provides that SAST could not.

**Step 4: Classify the findings by scan mode.**

For each of the three findings, state whether it would be detected by passive scanning, active scanning, or both. Explain your reasoning.

### Part 2 Deliverable

Submit your structured analysis for each finding and the scan mode classification.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Finding 1 analysis covers all four elements accurately | 8 |
| Finding 2 analysis covers all four elements accurately | 8 |
| Finding 3 analysis covers all four elements and explains the SAST/DAST difference | 10 |
| Scan mode classification for all three findings is correct with explanation | 4 |

---

## Part 3: DAST Local Scan Exercise (30 points)

### Part 3 Background

OWASP maintains a deliberately vulnerable web application — WebGoat — specifically for DAST practice. In this part you run a ZAP baseline scan against the publicly available demo instance.

### Part 3 Instructions

**Step 1: Run a ZAP baseline scan using Docker.**

Note: The OWASP WebGoat demo instance is available at the URL shown below for educational purposes. Run the ZAP baseline scan:

```bash
docker run --rm ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py \
  -t https://webgoat.org \
  -r zap-baseline-report.html \
  -l WARN \
  2>&1 | tee zap-output.txt
```

Record the complete output.

**Step 2: Count and categorize findings.**

From the ZAP output, count the number of WARN and FAIL findings. Create a summary table with columns: Rule ID, Rule Name, Severity, Count of Alerts.

**Step 3: Select the highest-severity finding and analyze it.**

For the highest-severity finding in your results, write a structured analysis covering: finding name, CWE, attack scenario, and remediation steps.

**Step 4: Interpret the exit code.**

Record the exit code of the ZAP scan command. Explain what this exit code indicates for a CI/CD pipeline job and whether the pipeline would pass or fail with this exit code.

### Part 3 Deliverable

Submit: the ZAP scan output, your finding summary table, the structured analysis of the highest-severity finding, and the exit code interpretation.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| ZAP scan output is shown and demonstrates successful execution | 8 |
| Finding summary table is complete and accurate | 8 |
| Highest-severity finding analysis covers all four elements | 10 |
| Exit code interpretation is technically accurate | 4 |

---

## Part 4: DAST Pipeline Integration Design (15 points)

### Part 4 Instructions

Write a 200-250 word technical design document for integrating DAST into the CI/CD pipeline you built in Module 03.

Address all four points below:

1. Where in the pipeline does the DAST job run? What job does it need to wait for (`needs:`)? Why must it run after that job and not before?
2. Should the DAST job use `zap-baseline.py` or `zap-full-scan.py` for a pipeline that runs on every PR merge? Justify your choice.
3. How do you handle the health check problem — ensuring the staging environment is ready before ZAP begins scanning?
4. Should the DAST job use `fail_action: true`? Explain the trade-off between blocking the pipeline on WARN findings versus HIGH/CRITICAL findings only.

### Part 4 Deliverable

Submit your written design document (200-250 words) addressing all four points.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Pipeline placement is correctly justified | 4 |
| Scan type choice is correctly justified for the use case | 4 |
| Health check strategy is technically valid | 4 |
| fail_action discussion correctly identifies the trade-off | 3 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (07) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
