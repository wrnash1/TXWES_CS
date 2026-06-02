# Discussion Forum: Module 07 - DAST: Dynamic Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 07 concepts — DAST mechanics, OWASP ZAP, passive vs. active scanning, pipeline placement, and the SAST/DAST/SCA triad — to realistic operational scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Production Active Scan Incident

A junior DevSecOps engineer, trying to demonstrate security value to management, configures OWASP ZAP's full active scan to run against the production URL `https://app.company.com` on a daily schedule. Two days after deployment, customer service receives calls from users who cannot log in. Investigation reveals that ZAP's brute-force detection testing has triggered account lockout for thousands of user accounts, and a ZAP SQL injection payload in a search field has corrupted a subset of production database records.

In 175-225 words, address the following: Identify the specific technical errors the engineer made in this configuration — name the ZAP scan mode, the target environment, and the missing control that would have prevented each incident. Describe the correct DAST pipeline architecture that provides equivalent security coverage without the production risk: which environment, which scan mode, and which schedule. Finally, explain what the engineer should have done instead of running active scans against production — what monitoring-oriented DAST capability is appropriate for a production environment?

---

## Scenario B: The SAST-Only Argument

A startup CTO argues: "We run Semgrep on every PR. It catches SQL injection, XSS, and hardcoded credentials. Adding DAST would just be redundant testing that slows down our pipeline. We are a five-person team and cannot afford 45-minute pipeline runs."

A security engineer responds: "SAST and DAST are not redundant — they find completely different vulnerability classes."

In 175-225 words, address the following: Support the security engineer's position by identifying three specific vulnerability classes that their SAST-covered Semgrep scan would miss that DAST would catch. For each, explain precisely why the vulnerability is only detectable at runtime. Then address the CTO's velocity concern directly: propose a DAST integration approach that adds meaningful security coverage without the 45-minute pipeline duration problem, citing the specific ZAP tool and configuration that makes this achievable.

---

## Scenario C: The Authenticated DAST Gap

A healthcare application processes patient records accessible only after login. A DevSecOps team integrates ZAP baseline scan into their CI/CD pipeline targeting the staging URL. After six months of weekly scans, a penetration tester discovers an IDOR vulnerability: any authenticated user can access any other patient's records by modifying the patient ID in the URL. The ZAP scans never flagged this vulnerability.

In 175-225 words, address the following: Explain precisely why the ZAP scans missed the IDOR vulnerability — what configuration gap caused this? Describe the specific DAST configuration change required to detect IDOR vulnerabilities: what does authenticated DAST mean technically, what does ZAP need to be provided to perform authenticated scanning, and what scan capability specifically tests IDOR patterns? Discuss whether automated DAST alone is sufficient for discovering all IDOR vulnerabilities in a complex healthcare application, or whether supplementary testing is required.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise DAST and DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most elements but lacks technical depth in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios.

- 4 pts: Two substantive responses (at least 50 words each) that add technical depth, propose an alternative approach, or cite a specific reading guide concept.
- 2 pts: Only one substantive response, or both are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

Scenario A involves a common error made by engineers who understand DAST tools but not the operational constraints of their deployment. When discussing Scenario A, do not just say "don't scan production" — explain specifically what each ZAP mode does that caused each specific incident (account lockouts and database corruption are two distinct problems with two distinct causes). Precision in incident analysis is a skill the exam and real-world DevSecOps practice both require.
