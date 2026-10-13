# Lab Activity: Module 06 — Information Security Program Development

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Lab Overview

In this lab you will develop the foundational documents of an information security program for a fictional mid-size organization. You will draft a security program charter, construct a policy hierarchy sample, align security objectives to business goals, and calculate ALE to support a resource justification.

This lab is intentionally document-focused rather than technical-tool-focused because CISM Domain 3 competencies are governance and management skills. Your deliverables should reflect professional-quality content that would be usable in a real organization.

**Estimated Time:** 90–120 minutes

**Submission:** Upload all deliverables as a single PDF or Word document to the Canvas LMS assignment portal.

---

## Scenario

You have been hired as the Information Security Manager at **Meridian Financial Services**, a fictional regional bank with 850 employees, two data centers, and a growing online banking platform. The company processes approximately $2 billion in transactions annually and is subject to GLBA (Gramm-Leach-Bliley Act), PCI DSS, and SOX compliance requirements.

The previous security manager left 8 months ago. There is currently no formal security program charter, the policy documentation is outdated and inconsistent, and the security team of four analysts reports to the CTO with no formal authority grant.

The CEO has asked you to build the foundation of a credible security program within 90 days. This lab simulates your first deliverable.

---

## Part A: Security Program Charter (40 points)

### Task Description

Draft a security program charter for Meridian Financial Services. Your charter must address all six required components. Write in professional business language as if this document will be presented to the board of directors.

### Required Charter Components

**Component 1 — Purpose and Scope**

Write 3–5 sentences defining the purpose of the Meridian information security program. Include an explicit scope statement that identifies what systems, data, and business processes are in scope. State at least one item that is explicitly out of scope.

**Component 2 — Authority Grant**

Write 2–4 sentences naming who grants security authority, what that authority includes (policy enforcement, audit rights, incident response authority), and to whom it is granted. The authority grant should trace to the Board or CEO.

**Component 3 — Roles and Responsibilities**

Create a table with three columns: Role, Responsibility, and Accountability Level. Include at minimum these five roles: Chief Information Security Officer, IT Operations, Business Unit Managers, All Employees, and Third-Party Vendors.

**Component 4 — Alignment to Business Objectives**

Write a paragraph of 4–6 sentences explaining how the security program supports Meridian's business mission. Reference at least two specific regulatory requirements (GLBA, PCI DSS, or SOX) and explain how compliance supports customer trust and business continuity.

**Component 5 — Reporting Structure**

Write 2–3 sentences describing where the CISO position reports in the Meridian organizational hierarchy. Justify this reporting structure from a program independence and board access perspective.

**Component 6 — Review Cycle**

Write 2 sentences specifying how frequently the charter will be reviewed and what triggers an unscheduled review.

### Grading Criteria — Part A

| Criteria | Points |
|---|---|
| All six components present and substantively addressed | 12 |
| Professional, business-appropriate tone and language | 8 |
| Scope statement is specific and includes an out-of-scope item | 6 |
| Roles and responsibilities table is complete and logical | 8 |
| Business alignment references regulatory requirements accurately | 6 |

---

## Part B: Policy Hierarchy Sample (30 points)

### Task Description

Meridian currently has no documented multi-factor authentication requirement despite operating an online banking platform. Construct a complete four-tier policy hierarchy document set addressing remote access and MFA requirements.

You will write one document at each tier. Each document should be realistic and professionally written.

### Tier 1: Remote Access Policy Statement

Write a policy statement (8–12 sentences) covering remote access to Meridian systems. The policy must be technology-neutral, reference the applicable regulatory driver, state the consequence of non-compliance, and define the scope of who is covered.

### Tier 2: Multi-Factor Authentication Standard

Write a technical standard (10–15 sentences or a structured list) specifying the approved MFA methods for Meridian. Include at minimum: approved authentication factors, prohibited methods (e.g., SMS OTP), applicable systems and user categories, and the exception approval process.

### Tier 3: VPN Access Setup Procedure

Write a numbered step-by-step procedure (minimum 8 steps) for an employee to set up their authenticator app for VPN access. The procedure should be specific enough that an employee without prior IT knowledge could follow it.

### Tier 4: Remote Work Security Guideline

Write a short guideline (6–10 bullet points) with recommended best practices for employees working remotely. This document is non-mandatory — frame the language accordingly using "should" rather than "must."

### Grading Criteria — Part B

| Criteria | Points |
|---|---|
| All four tiers present and correctly distinguished | 8 |
| Policy is technology-neutral and references regulation | 7 |
| Standard specifies approved/prohibited methods explicitly | 7 |
| Procedure is sequential and actionable | 8 |

---

## Part C: Security Strategy Alignment (20 points)

### Task Description

Meridian's CEO has shared the following two business objectives for the next fiscal year:

1. Launch a mobile banking application for retail customers by Q3
2. Acquire Westgate Community Bank and integrate operations within 18 months

For each business objective, identify two supporting security objectives. Then for one of the four security objectives, write a brief strategy statement (3–5 sentences) that includes current state, target state, and a high-level initiative to close the gap.

### Deliverable Format

Present your answer as a table with three columns: Business Objective, Security Objective, and Notes. Below the table, write your strategy statement for the one security objective you selected.

### Grading Criteria — Part C

| Criteria | Points |
|---|---|
| Two security objectives per business objective, all four are logical and relevant | 12 |
| Strategy statement includes current state, target state, and initiative | 8 |

---

## Part D: ALE Calculation and Business Case (10 points)

### Task Description

Meridian's security team has identified that the online banking platform is vulnerable to credential stuffing attacks. Research suggests that a successful attack would result in fraudulent transaction losses, customer notification costs, and regulatory fines totaling approximately $1.8 million. Your threat intelligence indicates this type of attack succeeds against similar institutions approximately twice every five years.

**Calculate the following:**

1. The Annual Rate of Occurrence (ARO)
2. The Single Loss Expectancy (SLE) — assume 100% exposure factor for this scenario
3. The current Annualized Loss Expectancy (ALE)
4. The new ALE if a bot detection and rate-limiting solution reduces the probability to one success every 20 years
5. The net benefit if the bot detection solution costs $85,000 per year

**Show your calculations with labeled formulas.**

Then write a two-sentence business case recommendation to the CEO based on your ALE analysis.

### Grading Criteria — Part D

| Criteria | Points |
|---|---|
| All five calculations correct with labeled formulas | 7 |
| Business case recommendation is clear and grounded in the ALE analysis | 3 |

---

## Submission Requirements

Your submission must be a single document (PDF or Word) containing all four parts. Use clear section headers matching the Part labels above. Include your name and student ID in the document header.

Late submissions lose 10 points per day per the course late policy.

---

## Lab Rubric Summary

| Part | Topic | Points |
|---|---|---|
| A | Security Program Charter | 40 |
| B | Policy Hierarchy Sample | 30 |
| C | Security Strategy Alignment | 20 |
| D | ALE Calculation and Business Case | 10 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

These challenges extend the Module 06 lab into advanced program development scenarios. Complete both challenges and the reflection questions for up to 15 bonus points.

---

### Challenge 1: Security Program Charter Gap Analysis

You have been hired as a consultant to assess the information security program at Meridian Credit Union, a 220-employee financial institution with 14 branch locations. The CISO provides you with the organization's existing "IT Security Policy" document, which functions as the de facto security program governing document. Review the excerpted characteristics below and conduct a gap analysis against the elements required in a proper security program charter.

**Existing Document Characteristics:**
- Approved by the IT Director (not executive leadership or the board)
- Covers acceptable use, password requirements, and clean desk standards
- Does not define the CISO's authority or reporting line
- Does not reference the organization's risk appetite or tolerance
- States that all employees "must follow IT security guidelines" without specifying consequences
- Has not been reviewed or updated in three years
- Is stored on the internal wiki accessible only to IT staff

**Step 1**: Identify at least five specific gaps between the existing document and what a properly constructed security program charter should contain. For each gap, explain the operational or governance risk created by the deficiency.

**Step 2**: Draft the Authority and Scope section of a new security program charter for Meridian Credit Union. Your draft must include: the authority granted to the CISO, the scope of the program (people, systems, and locations covered), the CISO's reporting relationship, and the consequences of non-compliance with program requirements. Write approximately 200 words.

**Step 3**: Develop a one-page rollout plan for transitioning Meridian from the existing document to the new charter. Your plan must address: who must approve the charter, how existing staff will be notified, how the old document will be retired, and what the first 90-day program priorities will be after charter approval.

---

### Challenge 2: Policy Hierarchy Construction for a New Business Unit

Meridian Credit Union is launching a digital banking division that will offer mobile banking services to customers in five states. The CISO must develop the policy hierarchy for this new business unit, which will process payment card data, store customer PII, and operate a 24/7 customer support function.

**Step 1**: Identify the regulatory requirements that will govern the digital banking division's security program (consider PCI DSS, GLBA, state consumer protection laws, and any applicable federal banking regulations). For each regulatory requirement, identify the corresponding policy tier (Tier 1 through Tier 4) where compliance obligations would primarily be documented.

**Step 2**: Construct a complete policy hierarchy inventory for the digital banking division. For each tier, list at least three specific documents that must exist, provide a one-sentence description of each document's purpose, and identify the approval authority (who must sign it).

**Step 3**: Two of your Tier 1 policies conflict: the Data Retention Policy requires that transaction logs be retained for seven years, while the Customer Privacy Policy states that personal data will be deleted upon customer account closure. Write a 150-200 word conflict resolution memo to the CISO explaining the conflict, identifying the applicable regulatory requirement that governs the resolution (GLBA Safeguards Rule record retention), and recommending how the two policies should be reconciled.

---

### Reflection Questions

Answer each reflection question in four to six sentences.

1. A new CISO argues that the organization already has adequate security controls in place and that developing a formal program charter is unnecessary overhead that consumes time better spent on technical improvements. Construct a response that explains the specific governance functions a charter serves that cannot be provided by technical controls alone, and describe a realistic scenario where the absence of a charter would directly harm the organization.

2. Information security policies are commonly described as "technology-neutral" — they should describe what must be achieved rather than how specific technologies must be configured. Explain the governance rationale for this principle and describe a scenario where a technology-specific policy created a significant organizational problem when the technology changed or was replaced.
