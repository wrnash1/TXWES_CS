# Discussion Forum: Module 03 - Vulnerability Management: Scanning and Prioritization

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 2 - Vulnerability Management (30%)

---

## Overview

Vulnerability management is where technical knowledge meets organizational reality. The best patch strategy in the world fails when business constraints, limited staffing, and competing priorities interfere. This week's discussion asks you to reason through realistic prioritization and communication challenges that every vulnerability management analyst encounters. Strong posts demonstrate technical accuracy and the practical judgment that distinguishes an effective analyst from one who can only quote CVSS numbers.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A: The Prioritization Disagreement

Your vulnerability scanner returns results showing 847 open findings across the organization's environment. Among them are a Critical CVSS 9.8 finding on the payroll processing server and a High CVSS 7.5 finding on the public-facing customer login portal. The payroll server is critical to business operations but is entirely internal with no external network exposure. The login portal handles authentication for 2.4 million customers.

Your manager says: "We should fix the Critical finding first — it's a 9.8 and regulations say Critical findings must be remediated within 30 days." You believe the High finding on the login portal is actually higher priority.

In 175-225 words, address all three of the following points:

1. Make the case to your manager for prioritizing the login portal's High finding over the payroll server's Critical finding. Reference specific prioritization factors from the Reading Guide.
2. Identify what additional information you would need to make a fully defensible prioritization decision for both findings (for example: exploit availability, compensating controls already in place, compliance scope).
3. Explain how the CISA Known Exploited Vulnerabilities catalog could resolve the disagreement if either CVE appeared in it.

---

## Scenario B: The Risk Acceptance Problem

A system owner submits a formal risk acceptance request for a High-severity vulnerability in a legacy application. The application cannot be patched because the vendor is out of business and no patch exists. Replacing the application would require a full business process redesign estimated at 18 months and $2 million. The system owner proposes accepting the risk indefinitely with no compensating controls.

Your job as the vulnerability analyst is to evaluate this risk acceptance request before it goes to the CISO for approval.

In 175-225 words, address all three of the following points:

1. Identify at least two reasons why accepting the risk indefinitely with no compensating controls is problematic from a security and governance standpoint.
2. Recommend two specific compensating controls that could reduce the risk without replacing or patching the legacy application.
3. Explain what the risk acceptance document should contain at a minimum before it is presented to the CISO for approval.

---

## Scenario C: Scan Coverage Gap Discovery

During a routine audit, you discover that the vulnerability management program has been scanning 85% of the organization's IP address space for the past year. The missing 15% is a manufacturing floor network segment containing legacy Windows XP and Windows 7 systems that run industrial automation software. The network team excluded this segment from scanning because "the systems are fragile and scans might crash them."

In 175-225 words, address all three of the following points:

1. Explain the security risk created by this scan exclusion. What type of vulnerability program gap does this represent, and which classification in the alert classification matrix does it most closely resemble (TP, FP, TN, FN)?
2. Propose a practical approach to gaining vulnerability visibility into this segment without risking system crashes. Consider scan configuration options discussed in the Reading Guide.
3. Identify what additional security controls should be applied to this segment if credentialed or active scanning cannot be performed safely, and explain how those controls mitigate the visibility gap.

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify a compensating control or scanning configuration option the original post did not mention
- Challenge the prioritization reasoning with a specific counter-scenario or edge case
- Reference a specific CVSS metric or prioritization factor that changes the analysis
- Connect the scenario to a real-world breach pattern or regulatory requirement

Responses that only agree with or restate the original post will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5-6 points: All three prompt points addressed with technical precision. Correct use of CVSS, KEV, risk acceptance, and compensating control terminology. Meets 175-225 word count. Demonstrates original analytical reasoning.
- 3-4 points: Most prompt points addressed with some technical accuracy. One or more key terms used imprecisely. Meets minimum word count.
- 1-2 points: Fewer than two prompt points addressed, significant technical errors, or below minimum word count.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more substantive responses of 75 words each that add technical value — new control recommendations, specific counter-arguments, or relevant regulatory/compliance context.
- 2 points: Only one qualifying response, or both replies are superficial.
- 0 points: No peer responses submitted.

---

## A Note from Professor Nash

The scenarios in this discussion reflect real decisions that vulnerability management analysts make every week. The CVSS score is a tool, not an answer. The best analysts understand that a number means nothing without context — what is the asset, who can reach it, is there an exploit, and what does the business need? Practice translating that context-aware thinking into clear, defensible written recommendations. That skill is what the CySA+ exam tests, and it is what your future employer will expect from day one.
