# Discussion: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This discussion focuses on real-world application security failures and the organizational decisions that produce them. Application security is not purely a technical problem — it is shaped by development culture, release pressure, budget constraints, and awareness. Engaging with your peers on these questions will deepen your understanding of why vulnerabilities persist despite decades of known solutions.

---

## Discussion Prompt

Read the following scenario, then respond to all three parts.

### Scenario

A mid-sized e-commerce company launches a new customer portal. Under schedule pressure, the security team's review is moved to post-launch rather than pre-launch. Three weeks after go-live, a security researcher contacts the company to report that:

- Customer account pages are accessible by modifying the account ID in the URL (IDOR).
- The login endpoint has no rate limiting, enabling automated credential stuffing attacks.
- Customer passwords are stored as unsalted MD5 hashes.
- HTTP is accepted on all pages (no redirect to HTTPS).

The company patches all four issues over the following two weeks. No customer data is confirmed stolen, but the CISO is required to brief the board.

---

## Part 1 — Root Cause Analysis (Required)

For each of the four vulnerabilities reported:

1. Identify the OWASP Top 10 category it falls under.
2. State at which phase of the Secure SDLC this vulnerability should have been caught.
3. Identify the specific control (e.g., SAST, DAST, threat modeling, code review) that would have detected or prevented it.

Organize your response in a table or numbered list.

---

## Part 2 — The "Shift Right" Problem (Required)

The CISO tells the board: "We moved security review to after launch to meet our deadline. We now understand this was the wrong trade-off."

In your post, argue one side of the following position: **"Meeting a software release deadline justifies deferring security testing to post-launch."**

You do not have to agree with the position — choose whichever side produces the stronger argument. Defend your position using at least two specific examples, costs, or principles from this module.

Your response should be 150 to 200 words.

---

## Part 3 — Peer Response (Required)

Read at least two classmates' responses to Part 2. For each:

- Identify the strongest point they made.
- Identify one counter-argument or limitation they did not address.
- Your reply to each classmate should be 75 to 100 words.

---

## Initial Post Guidelines

- Post your initial response (Parts 1 and 2) by the date listed in the course schedule.
- Peer responses (Part 3) are due 48 hours after the initial post deadline.
- Your initial post should be 400 to 500 words total.
- Cite at least one source beyond course materials (OWASP documentation, a published breach report, or a security research article).

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part 1 — Correct OWASP mapping and SDLC phase for all 4 vulnerabilities | 30 |
| Part 2 — Clear position, supported by specific evidence from module content | 40 |
| Part 3 — Two substantive peer replies with counter-argument | 30 |
| **Total** | **100** |

---

## Instructor Note

The four vulnerabilities in this scenario are all preventable with well-known, freely available tools and practices. The goal of this discussion is to understand why they occur despite being preventable — and what organizational or cultural changes would be most impactful. There is no single correct answer for Part 2; your reasoning and evidence matter more than the position you take.

---

*End of Discussion — Module 10*
