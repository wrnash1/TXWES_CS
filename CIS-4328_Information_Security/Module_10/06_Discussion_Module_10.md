# Discussion: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Discussion Overview

**Forum Title:** When Software Ships Broken — Responsibility, Culture, and the Secure SDLC

**Points:** 50 points total (Initial post: 30 points | Two peer responses: 10 points each)

**Deadline:** Initial post due by Day 4 of the module week; peer responses due by Day 7

---

## Background

In 2017, Equifax disclosed a breach affecting approximately 147 million people. The root cause was an unpatched Apache Struts vulnerability (CVE-2017-5638) in a web application. The vulnerability had been publicly disclosed and a patch had been available for two months before the breach. Equifax's security team had sent an internal notification to patch the system, but the patch was never applied. The attacker exploited the vulnerability using a simple HTTP request.

The same year, Uber disclosed a breach of 57 million driver and rider records caused by attackers who found AWS credentials hardcoded in a GitHub repository. Instead of disclosing the breach, Uber paid the attackers $100,000 through its bug bounty program to delete the data and keep it quiet — a decision that resulted in the company's Chief Security Officer being criminally charged.

Both breaches were preventable with basic secure development and patch management practices covered in this module. Both breaches resulted from organizational and cultural failures, not just technical ones.

---

## Initial Post Prompt

Choose ONE of the two scenarios below. Identify your choice at the top of your post.

### Scenario A — The Equifax Breach and Secure SDLC Failure

The Equifax breach stemmed from a vulnerable third-party library that was never patched. Had a mature Secure SDLC been in place, the organization would have had processes to detect and remediate this vulnerability before exploitation.

Address all of the following in your post:

1. At which phase(s) of the Secure SDLC could this breach have been prevented? Identify at least two phases and explain specifically what activity at each phase would have caught or mitigated the risk.

2. The Equifax breach involved a third-party library (Apache Struts), not code written by Equifax developers. Which tool category — SAST, DAST, or SCA — is most specifically designed to detect this category of risk? Explain why the others are less suited.

3. Imagine you are the CISO presenting a post-breach analysis to the board. The board asks: "Was this a technology failure or a people/process failure?" Construct a two- to three-sentence answer that accurately captures the nature of the failure. Use concepts from this module's content.

4. How does this scenario illustrate one or more of the OWASP Top 10 categories from the 2021 list? Name the specific category and explain the connection.

### Scenario B — The Uber Credential Breach and Secrets Management Failure

The Uber breach was caused by hardcoded AWS credentials in a GitHub repository — a violation of one of the most fundamental secure coding principles. This type of credential exposure is so common that there are automated tools (like truffleHog and GitGuardian) that scan GitHub repositories continuously looking for accidentally committed secrets.

Address all of the following in your post:

1. Explain how this breach could have been prevented at three different points in the development process: before the commit, at the commit, and after the commit. For each point, name a specific control or tool.

2. After finding the exposed credentials, Uber chose to pay the attackers rather than disclose. Evaluate this decision from a security and legal standpoint. Consider: what security principle does paying attackers undermine? What legal obligations does a company have when a breach occurs?

3. The attackers in the Uber breach did not exploit a zero-day or use sophisticated malware — they simply found credentials on a public code repository. What does this tell you about the relative prevalence of basic security failures versus sophisticated attacks? Use statistics or evidence from any assigned reading in this module or any prior module.

4. How does this scenario illustrate one or more of the OWASP Top 10 categories from the 2021 list? Name the specific category and explain the connection.

---

## Initial Post Requirements

- Minimum length: 400 words
- Maximum length: 700 words
- Use proper paragraph structure — bullet lists alone do not earn full credit
- Reference at least one assigned reading from the Module 10 Reading Guide
- No outside sources required, but factual accuracy about the breach scenarios is expected

---

## Peer Response Requirements

Respond substantively to two classmates. Each response must:

- Minimum length: 150 words
- Either (a) extend the analysis with a point the original poster did not address, OR (b) respectfully challenge an argument the poster made and support your counterargument
- Responses that merely agree ("great analysis") without adding substance earn zero points

---

## Grading Rubric

### Initial Post (30 points)

| Criterion | Excellent (Full Credit) | Satisfactory (Partial) | Insufficient |
|---|---|---|---|
| SDLC / tool analysis (Q1 + Q2 / Q1) | Phase-specific activities named accurately; tool category correctly selected with reasoning (8 pts) | Phases mentioned without specific activities; tool category correct without explanation (5 pts) | Vague or incorrect (0–2 pts) |
| Board/legal analysis (Q3 / Q2) | Accurately characterizes failure type; uses module vocabulary (7 pts) | Correct conclusion without supporting reasoning (4 pts) | Missing or incorrect (0–2 pts) |
| Strategic/ethical analysis (Q4 / Q3) | Demonstrates critical thinking; uses evidence from readings (8 pts) | Opinion without evidence (4 pts) | Avoids the question (0–2 pts) |
| OWASP connection (Q4) | Correct category identified with specific connection to scenario (7 pts) | Category named but connection is vague (4 pts) | Missing or wrong category (0–2 pts) |

### Peer Responses (10 points each)

| Criterion | Full Credit | Partial | Minimal |
|---|---|---|---|
| Substantive extension or challenge | Adds a new point or a reasoned challenge with supporting argument (7 pts) | Restates original post or adds a minor observation (4 pts) | Compliment only or under 50 words (0 pts) |
| Length and professionalism | 150+ words, respectful, clear (3 pts) | Under 150 words or informal tone (1 pt) | Under 75 words (0 pts) |

---

## Instructor Notes

The Equifax and Uber scenarios work together to illustrate two ends of the application security spectrum: patching failures (Equifax, addressed by SCA and patch management) and secrets management failures (Uber, addressed by secrets scanning and secure coding). Students often conflate "third-party library" vulnerabilities with something beyond the organization's control — this discussion explicitly challenges that assumption. The Uber scenario raises ethics and law, which surfaces well in peer responses. Encourage the class to discuss whether the $100,000 payment constitutes an admission of liability.

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 10*
