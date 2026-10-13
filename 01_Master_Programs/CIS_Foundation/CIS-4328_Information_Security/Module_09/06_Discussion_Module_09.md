# Discussion: Module 09 — Cloud Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Discussion Overview

**Forum Title:** The Shared Responsibility Model in Practice — Who Really Owns Cloud Security?

**Points:** 50 points total (Initial post: 30 points | Two peer responses: 10 points each)

**Deadline:** Initial post due by Day 4 of the module week; peer responses due by Day 7

---

## Background

In 2019, Capital One suffered a breach affecting over 100 million customers. The attacker exploited a misconfigured AWS Web Application Firewall and used Server-Side Request Forgery (SSRF) to steal AWS credentials from the EC2 instance metadata service. AWS infrastructure was not compromised — Capital One's application configuration was. AWS later introduced IMDSv2 (Instance Metadata Service version 2) to mitigate this class of attack, but the breach occurred because of a customer-side misconfiguration.

In 2021, researchers discovered thousands of publicly accessible S3 buckets containing sensitive data from various organizations. In most cases, the buckets were set to public by developers who misunderstood the default settings or prioritized speed over security.

Both incidents reflect the same underlying tension: cloud providers build secure infrastructure, but customers make insecure decisions within it.

---

## Initial Post Prompt

Choose ONE of the following two scenarios and respond to the questions. Identify which scenario you chose at the top of your post.

### Scenario A — Healthcare SaaS Misconfiguration

A regional hospital network uses a SaaS electronic health record (EHR) system hosted by a third-party vendor. The vendor is HIPAA-compliant and holds a SOC 2 Type II report. The hospital's IT team configures the EHR system and grants all 500 employees the same administrator-level access for convenience during the initial rollout. Six months later, a nurse's account is compromised via a phishing attack, and the attacker exfiltrates records for 45,000 patients using the nurse's administrator privileges.

Address all of the following in your post:

1. Under the shared responsibility model, which security failures are attributable to the hospital and which (if any) are attributable to the EHR vendor? Be specific about what each party controlled.

2. Which specific security control, if implemented at the time of rollout, would have most likely prevented the breach? Justify your choice with a two- to three-sentence explanation.

3. The hospital's CISO argues that because the vendor is HIPAA-compliant and has a SOC 2 Type II report, the vendor should share liability for the breach. Evaluate this argument — is it valid? Why or why not?

4. How does this incident relate to at least ONE concept from the Security+ SY0-701 exam objectives covered in this module?

### Scenario B — Multi-Cloud Container Deployment

A financial services company operates containers across AWS EKS and Azure AKS. During a routine vulnerability scan, the security team discovers that 40% of container images in production were built from a base image that has not been updated in 14 months and contains 23 critical CVEs. Additionally, several containers are running as root with no resource limits or security profiles applied. The containers process real-time financial transaction data.

Address all of the following in your post:

1. Identify the full attack surface exposed by these findings. Consider image-level risks, runtime risks, and data-level risks in your analysis.

2. The organization argues that because AWS and Azure provide container orchestration as managed services, the cloud providers should have flagged these vulnerabilities through their native security tools. Evaluate this argument using the shared responsibility model.

3. Design a remediation plan that addresses the findings in priority order. For each action item, state the finding it addresses, the control applied, and the timeline (immediate / short-term within 30 days / medium-term within 90 days).

4. How does this incident relate to at least ONE concept from the Security+ SY0-701 exam objectives covered in this module?

---

## Initial Post Requirements

- Minimum length: 400 words
- Maximum length: 700 words (practice the professional skill of being concise)
- Use proper paragraph structure — bullet lists alone do not earn full credit
- Reference at least one assigned reading from the Module 09 Reading Guide
- No outside sources required, but college-level writing is expected

---

## Peer Response Requirements

Respond substantively to two classmates who chose DIFFERENT scenarios from each other (you may respond to students who chose the same scenario as you only if no other posts are available). Each response must:

- Minimum length: 150 words
- Either (a) extend the analysis with a point the original poster did not address, OR (b) respectfully challenge an argument the poster made and explain why
- Be constructive — "great post" without substance earns zero points

---

## Grading Rubric

### Initial Post (30 points)

| Criterion | Excellent (Full Credit) | Satisfactory (Partial) | Insufficient (Minimal) |
|---|---|---|---|
| Shared responsibility analysis (Q1) | Precisely identifies customer vs. vendor responsibilities with specific controls (8 pts) | General description without specific controls (5 pts) | Vague or incorrect attribution (0–2 pts) |
| Security control recommendation (Q2) | Specific, justified control aligned to the facts (7 pts) | Correct control without adequate justification (4 pts) | Generic or irrelevant recommendation (0–2 pts) |
| Critical evaluation (Q3/Q2B) | Engages the argument analytically with evidence from course content (8 pts) | Agrees or disagrees without reasoning (4 pts) | Avoids the question (0–2 pts) |
| Security+ objective connection (Q4) | Names specific exam objective and connects it meaningfully (7 pts) | Names a topic without connecting it (4 pts) | Missing or superficial (0–2 pts) |

### Peer Responses (10 points each)

| Criterion | Full Credit | Partial | Minimal |
|---|---|---|---|
| Extends or challenges analysis substantively | Adds a new point or a reasoned challenge (7 pts) | Restates what the poster said (4 pts) | Compliment only (0 pts) |
| Minimum length and professional tone | 150+ words, respectful, clear (3 pts) | Under 150 words or informal (1 pt) | Under 75 words (0 pts) |

---

## Instructor Notes

This discussion is designed to develop the applied analytical skills that Security+ performance-based questions require. Students who struggle with scenario Q1 (shared responsibility attribution) likely need to re-review the shared responsibility table in the Reading Guide. Common errors include blaming the cloud provider for application-layer decisions and overstating the protection conferred by compliance certifications. The Capital One breach is an excellent real-world anchor for both scenarios.

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 09*
