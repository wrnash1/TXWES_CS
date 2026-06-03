# Discussion Forum: Module 08 — Vulnerability Management

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Overview

Vulnerability management is where technical analysis meets organizational politics. Identifying vulnerabilities is the easy part. Convincing system owners to patch, navigating change management, and making defensible prioritization decisions when everything is marked Critical — that is the work. This week's scenarios put you in that position. The goal is to reason through the competing pressures and produce defensible, technically sound decisions.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A — The CVSS Score Debate

Your vulnerability management platform has completed its quarterly scan. The report shows 143 Critical findings, 412 High findings, and 1,847 Medium findings. Your IT operations manager pushes back: "This is the same CVSS-based report we got last quarter. Nothing is actually different. We're going to work our way through the list in score order — Critical first, then High."

You know that three of the 143 Critical findings are in the CISA KEV catalog and appear on internet-facing systems. You also know that 22 of the 412 High findings have EPSS scores above 0.60, and two of those have been actively discussed in threat intelligence reports as being exploited by the threat actor group most commonly targeting your industry sector.

In 175–225 words, address all three of the following points:

1. Explain specifically why "work through the list in score order" is an inadequate prioritization methodology. Use the KEV and EPSS data provided to illustrate the risk of CVSS-only ordering.

2. Propose a prioritization framework that uses at least four inputs beyond CVSS Base Score. Describe the practical steps your team would take to apply this framework to the 143 Critical findings.

3. Explain how you would communicate this prioritization argument to the IT operations manager without creating conflict. What language — risk, business impact, compliance — would you use to make the case for context-aware prioritization?

---

## Scenario B — The Patch That Breaks Things

A Critical vulnerability (CVE-2023-XXXX, CVSS 9.8, CISA KEV) is identified on the organization's primary order management application server. The vendor patch is available. Your patch management team tests the patch in a staging environment and discovers it breaks a critical integration with the ERP system, causing order processing to fail. The application owner says: "We cannot deploy this patch until the vendor provides a compatibility fix — that could be four to six weeks."

The CISO asks you to propose a solution.

In 175–225 words, address all three of the following points:

1. Identify at least three compensating controls that could reduce the organization's exposure to this vulnerability while the compatible patch is developed. For each control, explain what risk it reduces and what residual risk remains.

2. Describe what formal documentation should be produced during this exception period. Who should sign the risk acceptance, what should it contain, and how often should it be reviewed?

3. Explain what the CISO should communicate to the board about this situation if asked — specifically, how should she characterize the risk level, the compensating measures in place, and the timeline for full remediation?

---

## Scenario C — The Legacy System Problem

A security audit reveals that a financial organization's core transaction processing system — a mainframe running software last patched five years ago — has 34 outstanding Critical and High vulnerabilities. The system vendor went out of business three years ago. No patches exist. The system cannot be replaced within 18 months due to cost and regulatory approval timelines. It processes millions of transactions per day, has no alternate system, and is directly connected to the payment processing network.

In 175–225 words, address all three of the following points:

1. Identify and describe at least four network architecture or access control compensating controls that could reduce the exposure of this system to exploitation, even though patching is not possible.

2. Explain what risk acceptance documentation an organization in a regulated industry (financial services, for example subject to PCI DSS) would need to produce for this situation. What regulatory reporting obligations might apply?

3. Discuss the long-term vulnerability management strategy the organization should implement — what planning, testing, and migration activities should begin immediately to address the 18-month replacement timeline?

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify a compensating control the original post missed
- Challenge a prioritization argument with a competing risk factor or regulatory consideration
- Reference a specific CVSS metric or Environmental Score adjustment concept from the Reading Guide
- Connect the scenario to a documented real-world breach caused by unpatched vulnerabilities

Responses consisting only of agreement without technical content will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5–6 points: All three prompt points addressed with technical precision. CVSS concepts, KEV, EPSS, and compensating controls applied accurately. Meets 175–225 word count.
- 3–4 points: Most prompt points addressed with reasonable accuracy. Meets minimum word count.
- 1–2 points: Fewer than two points addressed or significant technical errors present.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more responses of 75+ words with specific technical additions or challenges.
- 2 points: One qualifying response or both are superficial.
- 0 points: No peer responses submitted.

---

## A Note from Professor Nash

Scenario C is the scenario most organizations quietly live with. Perfect patch coverage is a myth in large, complex environments — especially in healthcare, finance, and manufacturing where legacy systems run business-critical processes for decades. The analyst who can identify the right compensating controls, produce defensible risk acceptance documentation, and build a credible migration plan is far more valuable than one who simply says "patch it." The regulatory pressure — PCI DSS, HIPAA, SOX — gives you leverage to accelerate decisions that would otherwise stall in budget discussions. Know how to use it.
