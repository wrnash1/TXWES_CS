# Discussion: Module 01 - Penetration Testing Methodology and Scoping

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash

---

## Instructions

Post your initial response to one of the three scenarios below by Wednesday at 11:59 PM. Then reply to at least two classmates by Sunday at 11:59 PM. Your initial post should be 175 to 225 words. Each peer reply should be at least 75 words and contribute new analysis, a counterpoint, or a real-world connection.

Professor Nash will participate in the discussion thread mid-week to ask follow-up questions. Be prepared to defend your reasoning.

---

## Scenario A — The Rushed Client

A startup CTO contacts your penetration testing firm on a Friday afternoon. She says the company's board requires proof of a security assessment before Monday's investor meeting. She offers to pay double your normal rate and says she will send you a "quick email authorization" so you can begin scanning their web application over the weekend. She is clearly authorized to make decisions for the company.

Discuss: What are the specific risks of proceeding based on an email authorization rather than a fully executed Rules of Engagement? What documents must be signed before testing begins, and why does urgency not change those requirements? How would you handle this client professionally without losing the business?

---

## Scenario B — The Scope Creep Discovery

You are two days into an authorized internal network penetration test. Your authorized scope is 10.10.0.0/24. While enumerating services on an in-scope host, you discover it has an active SMB connection to a server at 10.10.1.50, which is in a subnet not listed in your RoE. A quick passive observation suggests the server may be a domain controller. Exploiting it would likely yield domain administrator credentials and demonstrate a critical finding.

Discuss: What is the correct professional and legal response to this discovery? Why does the potential severity of the finding not justify proceeding without updated authorization? What specific steps do you take, and how do you document this situation in your final report?

---

## Scenario C — The Compliance-Driven Test

A healthcare organization asks you to perform a penetration test to satisfy their HIPAA risk analysis requirement. During the scoping call, their IT manager says they want a "full test of everything" but has not provided any network documentation. When you ask about Protected Health Information (PHI) systems, the IT manager says "just avoid those, everyone knows which servers they are."

Discuss: Why is "just avoid those systems" insufficient as a scope exclusion? What specific information must be documented in the scoping document before testing begins? How do data handling obligations under HIPAA affect what you include in your RoE, and what happens if you accidentally access a PHI system during testing?

---

## Grading Rubric (10 Points)

| Component | Points | Criteria |
|---|---|---|
| Initial Post — Content | 4 | Directly addresses the scenario; applies correct module concepts (RoE, CFAA, scope, authorization) accurately |
| Initial Post — Depth | 2 | Goes beyond surface-level summary; includes specific reasoning, professional context, or consequences |
| Word Count | 0 or -1 | Posts under 175 words or over 225 words receive a one-point deduction |
| Peer Reply 1 | 2 | At least 75 words; adds new analysis, a counterpoint, or a real-world connection — not just agreement |
| Peer Reply 2 | 2 | At least 75 words; same standard as Peer Reply 1 |
| **Total** | **10** | |
