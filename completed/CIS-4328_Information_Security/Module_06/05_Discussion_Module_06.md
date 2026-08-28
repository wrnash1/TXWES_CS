# Discussion Forum — Module 06: Identity and Access Management

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This discussion applies Module 06's IAM concepts to real-world identity security failures and the evolving debate around passwordless authentication. Identity-related failures are the leading root cause of data breaches — understanding why they persist and what can be done about them is a core professional competency.

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM

**Minimum Participation:** One original post (250–350 words) and two substantive replies (100+ words each).

---

## Scenario A — The Credential Stuffing Epidemic

Credential stuffing attacks use lists of username/password combinations from previous data breaches to attempt login at other services. These attacks succeed because users reuse passwords across multiple sites. A 2023 analysis found that credential stuffing attacks account for billions of login attempts per day across the internet.

Many organizations respond by implementing multi-factor authentication. However, MFA adoption rates remain uneven — some studies show fewer than 30% of enterprise users have MFA enabled on all their accounts.

In 250–350 words, respond to all three of the following:

1. Explain why credential stuffing specifically exploits the intersection of a data breach at one organization and an IAM weakness at a different organization. What IAM principle would directly reduce credential stuffing success rates even without MFA?

2. Organizations often cite user friction as the reason MFA adoption is low. Evaluate this tradeoff: how do you weigh the security benefit of MFA against the usability cost? Are there MFA implementations that reduce friction while maintaining strong security? Reference specific methods covered in Module 06.

3. NIST SP 800-63B (from the reading guide) identifies phishing-resistant authenticators as the highest assurance level. What specific authenticator types achieve AAL3, and why are they phishing-resistant in a way that TOTP codes are not?

---

## Scenario B — Least Privilege at Scale

A rapidly growing startup has 200 employees. In the early days, everyone had admin access to the cloud environment "to move fast." The company now processes healthcare data and must comply with HIPAA. An audit has found that 140 of 200 employees have some form of elevated cloud access that they likely do not need.

The CISO has been tasked with implementing least-privilege access across the cloud environment within 90 days, without disrupting ongoing product development.

In 250–350 words, respond to all three of the following:

1. Design a phased approach to implementing least-privilege access in this environment. What would you do in the first 30 days, the next 30 days, and the final 30 days? Use IAM terminology from Module 06 to describe the specific actions at each phase.

2. The engineering team warns that removing admin access will slow down developers who legitimately need elevated permissions to deploy code and manage infrastructure. How would you address this concern using PAM concepts from Module 06? What specific control allows developers to have elevated access when genuinely needed without maintaining persistent admin rights?

3. HIPAA requires individual accountability for access to protected health information (PHI). Which specific IAM conditions in the current state violate this requirement? What controls must be in place to satisfy individual accountability under HIPAA?

---

## Peer Reply Guidance

When replying to classmates, engage with one of these angles:

- If your classmate proposed a specific MFA implementation to address user friction, challenge them to consider scenarios where that implementation would fail (SIM-swapping for SMS, real-time phishing proxies for TOTP).

- If your classmate's phased least-privilege plan involves removing access first, challenge them to consider the business impact and what discovery/inventory steps should precede removal.

- If your classmate addressed the HIPAA individual accountability requirement, ask them to specify exactly which technical controls (logging, unique accounts, session recording) satisfy the audit trail requirement.

---

## Research Starting Points

- CISA MFA Fact Sheet: [https://www.cisa.gov/sites/default/files/publications/MFA-Fact-Sheet-Jan22-508.pdf](https://www.cisa.gov/sites/default/files/publications/MFA-Fact-Sheet-Jan22-508.pdf)

- NIST SP 800-63B Digital Identity Guidelines: [https://pages.nist.gov/800-63-3/sp800-63b.html](https://pages.nist.gov/800-63-3/sp800-63b.html)

- CISA Zero Trust Maturity Model: [https://www.cisa.gov/zero-trust-maturity-model](https://www.cisa.gov/zero-trust-maturity-model)

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Original post addresses all prompt questions | 40 |
| Demonstrates correct use of Module 06 IAM terminology | 25 |
| Arguments are specific and technically grounded | 15 |
| Two substantive replies that add new reasoning | 20 |
| **Total** | **100** |

---

Module 06 Discussion — End
