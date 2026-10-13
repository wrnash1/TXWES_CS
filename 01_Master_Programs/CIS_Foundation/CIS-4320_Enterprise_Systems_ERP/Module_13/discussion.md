# Discussion: Module 13 — ERP Security and Access Control

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be 175–225 words and address all embedded questions. After posting, reply substantively to **two classmates** who chose different scenarios. Peer replies must be at least 75 words and contribute new analysis. Initial posts are due Thursday 11:59 PM; peer replies are due Sunday 11:59 PM.

---

## Scenario 1: The Over-Privileged Administrator

Meridian Healthcare uses Salesforce to manage patient referrals and insurance authorizations. During a routine annual access review, the security team discovers that six employees who left the company in the past year still have active Salesforce user accounts. Three of those accounts were accessed after the employees' departure dates.

Additionally, the IT team learns that the previous Salesforce Administrator granted herself — before resigning — the ability to export all patient data from every report, with no restriction on what she could take with her.

Address the following in your post:

- What specific Salesforce security controls should have prevented both the active-account issue and the unrestricted data export?
- What does HIPAA (healthcare privacy law) require when a breach of this type is suspected, and how does that change the company's immediate priorities?
- What is "privilege creep," and how did it likely contribute to the administrator's ability to grant herself excessive permissions?
- What process changes would you implement immediately to prevent recurrence?

Your response should demonstrate understanding of Salesforce user management, Field-Level Security, Event Monitoring, and access review processes covered in Module 13.

---

## Scenario 2: The SAP Role Redesign

Atlas Chemicals is a manufacturing company whose SAP system was configured by a consultant fifteen years ago. The security model was never updated, and over time roles have accumulated so many authorizations that most plant managers have what amounts to system-wide access to all financial posting, material management, and vendor management transactions simultaneously.

The internal audit team has just flagged eleven critical SoD conflicts affecting twelve users. The CISO wants the conflicts remediated before the external audit in 90 days. The operations team is pushing back, saying any access changes will disrupt day-to-day work.

Address the following in your post:

- Explain why the legacy "super-role" model is both a security failure and a compliance risk.
- How would you use SAP GRC's Access Risk Analysis to prioritize which conflicts to remediate first?
- What is a compensating control, and why might one be necessary for conflicts that cannot be fully remediated within 90 days?
- How would you handle the operations team's resistance while still meeting the audit deadline?

Your response should demonstrate understanding of SAP role design, SoD concepts, SAP GRC, and compensating controls from Module 13.

---

## Scenario 3: Designing the Security Model from Scratch

You have just been hired as the Salesforce Administrator for a new 50-person B2B SaaS startup. The company is about to go live with Salesforce Sales Cloud. Nobody has configured security yet — you have a blank slate.

The company has five sales reps, two sales managers, one VP of Sales, a finance analyst, a marketing coordinator, and the rest are engineers and executives with read-only needs.

Address the following in your post:

- How many profiles would you create, and what would each one be? Justify your answer using the principle of minimizing profile proliferation.
- What OWD settings would you apply to Opportunity, Account, and Lead, and why?
- What permission sets would you create to handle exceptions and specialty access?
- What is one security decision you would make differently at a 500-person company versus a 50-person startup, and why does organization size matter?

Your response should demonstrate understanding of Salesforce profile design, OWD strategy, permission set best practices, and scalability considerations.

---

## Peer Response Guidelines

When replying to a classmate's post:

- Identify one specific recommendation they made and either reinforce it with an additional reason or respectfully challenge it with a counter-argument
- Reference content from the Module 13 reading or video to support your point
- Avoid generic agreement — every word should add analytical value

---

## 10-Point Grading Rubric

| Criterion | 2 Points | 1 Point | 0 Points |
|-----------|----------|---------|----------|
| **Addresses all scenario questions** | All embedded questions substantively answered | Most questions answered; one is missing or very brief | Multiple questions unanswered; response is off-topic |
| **Demonstrates module content mastery** | Accurately applies at least two specific Module 13 concepts with correct terminology | Uses module vocabulary but imprecisely or without clear connection to the scenario | Little to no use of module-specific concepts |
| **Analysis depth and specificity** | Gives concrete, specific recommendations with clear reasoning; acknowledges trade-offs | Makes recommendations without specific reasoning; does not address trade-offs | States opinions without analysis or specificity |
| **Writing quality** | Well organized, 175–225 words, clear and professional; minimal grammatical errors | Mostly clear; minor organizational issues; length within 10% of target range | Unclear, significantly off word count, or major grammatical issues impede comprehension |
| **Peer responses (two required)** | Both replies are 75+ words, directly engage the classmate's argument, and add new analysis | One strong reply; second reply is brief or generic | Zero or one reply; replies do not engage with classmate's specific points |

**Total: 10 points**

---

## Sample Strong Opening Lines (to inspire, not copy)

For Scenario 1: "The core failure here is not a technology gap — Salesforce has the tools to prevent every incident described — but a process failure: no one was enforcing the controls that were available..."

For Scenario 2: "The fifteen-year-old 'super-role' model is a product of good intentions and accumulated technical debt: each time a manager needed one additional transaction, it was easier to add it to an existing role than to redesign the role model properly..."

For Scenario 3: "At 50 people, the temptation is to keep security simple by creating as few profiles as possible and using OWD settings that are permissive enough to avoid constant sharing rule maintenance — but getting this wrong at the start is significantly harder to fix later..."

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
