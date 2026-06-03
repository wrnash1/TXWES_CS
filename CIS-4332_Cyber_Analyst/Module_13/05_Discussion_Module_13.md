# Discussion Forum: Module 13 — Compliance and Security Controls Validation

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Overview

This discussion explores the practical tensions that arise in compliance and security controls validation work. Security frameworks provide ideal targets, but real organizations operate with budget constraints, legacy systems, and competing priorities. Each scenario below presents a situation where analysts must balance compliance requirements against operational realities. Select one scenario, post your analysis, and respond to two peers on different scenarios.

---

## Scenario A — The Compliance vs. Security Paradox

Your organization recently completed a SOC 2 Type II audit and passed with no significant findings. Two weeks after receiving the clean audit report, your threat hunting team discovers evidence that an attacker had persistent access to a development server for approximately six weeks during the audit period. The server hosted test data with synthetic (non-production) customer records. The attacker's activity was within the scope of several monitoring controls that were listed as "fully implemented" in the audit evidence package.

In 175–225 words, address the following: How is it possible to pass a compliance audit and still have an active attacker in your environment? What does this scenario reveal about the limitations of point-in-time compliance audits? Should the organization disclose the breach to its auditors retroactively, and what are the professional and legal implications of not doing so? What change to the compliance program would provide more meaningful assurance that controls are actually working?

---

## Scenario B — The Unpatched Legacy System

You are an analyst at a manufacturing company. A gap analysis reveals that a critical industrial control system (ICS) that manages production line equipment has not been patched in four years because the vendor states that patching will void the warranty and could cause production line failures. The system runs an unpatched OS version with 23 known critical CVEs, two of which are actively exploited in the wild. The production line generates $4.2 million per day in revenue and cannot tolerate unplanned downtime.

In 175–225 words, address the following: How would you document this gap in the formal gap report? What compensating controls would you recommend to reduce the risk without patching the system? Who should sign off on the formal risk acceptance for this exception, and what information do they need to make an informed decision? If a ransomware attack successfully exploits one of the unpatched CVEs and shuts down the production line, what documentation from your gap analysis process would be most important to have on record?

---

## Scenario C — The Compliance Dashboard Disconnect

You maintain the organization's compliance dashboard, which shows 94% compliance across all CIS IG1 safeguards. The CISO presents this dashboard to the board monthly and uses it to justify deferring additional security investment. However, you have growing concerns about the data quality behind the dashboard. The hardware inventory feeding the dashboard is maintained manually by IT staff, the vulnerability scan coverage is calculated based on the number of scan reports submitted rather than verified asset coverage, and the MFA adoption metric is derived from license counts rather than verified enforcement logs.

In 175–225 words, address the following: What specific risks does metric methodology quality create for a compliance dashboard? If the dashboard is inflating the apparent compliance posture, what obligation does the analyst have to raise this concern — even if it conflicts with the CISO's narrative to the board? What technical improvements would make each of the three metrics (hardware inventory, scan coverage, MFA adoption) more accurate and defensible? How would you present the concern about data quality to your manager without undermining the credibility of the security program?

---

## Posting Instructions

**Initial Post:** Due Wednesday at 11:59 PM. Select one scenario. Write 175–225 words directly addressing all questions. Use correct compliance and controls terminology. Reference NIST CSF, CIS Controls, or CySA+ concepts where applicable.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who chose different scenarios from yours. Each reply must be at least 75 words and add substantive analysis — extend the argument, challenge an assumption, or offer an alternative framework for the problem.

---

## Discussion Rubric — 10 Points Total

### Initial Post — 6 Points

- 5–6 pts: Addresses all scenario questions with technical accuracy, correct compliance terminology, and clear reasoning. Word count within range. References course frameworks.
- 3–4 pts: Addresses most questions but lacks depth or technical precision.
- 1–2 pts: Superficial treatment or misses key questions.
- 0 pts: No initial post submitted.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies (75+ words each) to classmates on different scenarios. Replies add analysis, challenge assumptions, or offer alternative approaches grounded in course content.
- 2–3 pts: One substantive reply, or two replies that are superficial.
- 1 pt: Replies present but below length or quality threshold.
- 0 pts: No peer responses submitted.
