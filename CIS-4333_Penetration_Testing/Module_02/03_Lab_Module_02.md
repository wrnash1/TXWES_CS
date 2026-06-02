# Lab Activity: Module 02 - Rules of Engagement and Legal Considerations

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash
**Total Points:** 100

---

## Authorization and Context Notice

This lab is a document analysis and written-response exercise. No technical scanning or network interaction is performed. All scenarios, organizations, and documents referenced are fictional. This activity simulates professional legal and ethical judgment tasks performed by penetration testers in authorized educational contexts.

---

## Lab Overview

In this lab you will analyze three fictional pre-engagement documents, identify deficiencies, apply regulatory compliance knowledge, and respond to ethical judgment scenarios. These tasks directly mirror real-world situations tested on the CompTIA PenTest+ PT0-002 exam.

---

## Part 1: Authorization Letter Analysis (25 Points)

Read the following fictional authorization letter and answer the questions that follow.

---

### Sample Authorization Letter (Fictional)

To Whom It May Concern:

This letter confirms that ClearPath Security Consulting has been retained to perform security testing on our systems. Testing will occur sometime next month. Please cooperate with their team.

Sincerely,
J. Smith
IT Manager, Westbridge Healthcare Group

---

### Question 1.1 — Missing Components (10 Points)

A professional authorization letter must contain specific components to be legally effective. Identify five components that are missing or inadequate in the letter above. For each missing component, explain why its absence creates a professional or legal problem.

Use this format for each item:

Missing Component: (name the component)

Problem Created: (explain the legal or professional risk)

### Question 1.2 — Rewrite (15 Points)

Rewrite the authorization letter above so that it is professionally complete. Your rewritten letter must include all required components. Use fictional but realistic names, dates, and system details consistent with a healthcare organization. The letter must be signed by someone with appropriate organizational authority.

---

## Part 2: Regulatory Compliance Mapping (30 Points)

For each of the following three client scenarios, identify the applicable compliance framework(s), the specific requirement that drives the penetration testing obligation, and any special data handling considerations the penetration tester must address.

Write a minimum of 3 to 4 sentences per scenario.

### Scenario 2.1 — Regional Bank (10 Points)

First National Savings Bank (fictional) processes credit card transactions for small business customers. They have approximately 500 merchant clients. Their technical environment includes a cardholder data environment (CDE) hosted on-premises, a web portal for merchant account management, and a customer-facing mobile application.

Identify: Which compliance framework(s) apply? What specific requirement mandates penetration testing? What special scope considerations apply to the CDE? What must the RoE address regarding cardholder data discovered during testing?

### Scenario 2.2 — Medical Practice (10 Points)

Sunrise Family Medicine (fictional) is a group medical practice with 12 physicians and approximately 8,000 active patients. They use an electronic health records system hosted by a cloud vendor. Their on-premises network connects physician workstations to the EHR system via a local server. They have never had a formal security assessment performed.

Identify: Which compliance framework(s) apply? Does that framework explicitly mandate penetration testing? How should the RoE address Protected Health Information? What must the tester do if PHI is encountered during testing?

### Scenario 2.3 — EU-Facing Software Company (10 Points)

CodeBridge Solutions (fictional) is a US-based software company that provides project management software to enterprise customers in Germany, France, and the Netherlands. Personal data of EU-resident users including names, email addresses, and work activity logs is stored on US-based servers. The company's CTO wants a penetration test before their next major product release.

Identify: Which regulation applies to this company's data? What does that regulation require regarding technical security measures? What data handling obligations apply to the penetration tester? What would the company need to do within 72 hours if the penetration test accidentally caused a data incident affecting EU residents?

---

## Part 3: Ethical Judgment Scenarios (25 Points)

Answer each of the following scenarios in complete sentences. Write 4 to 6 sentences per response. Apply the ethical principles covered in Module 02.

### Scenario 3.1 — The Interesting System (8 Points)

You are conducting a gray box internal network penetration test for a manufacturing firm. Your authorized scope is the 10.20.0.0/24 subnet. While enumerating services on an authorized host, you notice it has an open connection to 172.16.5.10 — a subnet that is not in your RoE. Further passive observation suggests the 172.16.5.0/24 subnet contains the company's industrial control systems (ICS). Compromising those systems would likely be a critical finding that would add significant value to the report.

What do you do? Be specific about each step you take and the order you take them in.

### Scenario 3.2 — The Active Breach (9 Points)

You are four days into an authorized external network penetration test. While reviewing logs from your exploitation of a confirmed vulnerable web application, you notice file system artifacts you did not create — specifically a webshell planted three weeks ago with an external IP address you do not control in the access logs. The webshell has had regular external connections for 21 days. You check the RoE — it says nothing specific about this scenario.

What do you do? Address: testing activity, client notification timing, evidence handling, your obligations under the RoE, and whether you continue the penetration test after the situation is reported.

### Scenario 3.3 — The Scope Expansion Request (8 Points)

Your firm is two days from the end of a two-week authorized penetration test for a regional retailer. The client's IT director calls and verbally asks you to also test their new e-commerce platform, which was not in the original RoE. He says "just add it, we're all friends here, no need for paperwork." The e-commerce platform is hosted by a third-party managed services provider on shared infrastructure.

What do you do? Address: verbal authorization, formal RoE amendment requirements, third-party authorization, and how you communicate your position professionally without damaging the client relationship.

---

## Part 4: RoE Gap Analysis (20 Points)

Review the following abbreviated Rules of Engagement document excerpt and identify all gaps, ambiguities, or missing required sections. For each issue found, explain what the problem is and how it should be corrected.

---

### Sample RoE Excerpt (Fictional — Contains Intentional Deficiencies)

Engagement: Network Security Assessment
Client: Meridian Logistics Group
Testing Firm: ClearPath Security Consulting

Authorized Targets: Meridian's internal network
Testing Methods: All standard penetration testing techniques
Schedule: During business hours, this month
Contact: Email the IT department

---

### Instructions

Identify at least six specific problems with this RoE excerpt. For each problem, write:

Problem: (describe the specific deficiency)

Risk Created: (explain what could go wrong because of this deficiency)

Correction: (describe what the corrected language should say)

---

## Submission Instructions

Submit the following to the Canvas LMS assignment portal:

- One PDF or Word document containing all four parts of this lab
- File naming convention: `CIS4333_Lab02_LastName_FirstName.pdf`
- Due date: as listed in the course calendar

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part 1.1 — Missing Components | 10 | Five components identified; legal or professional risk clearly explained for each |
| Part 1.2 — Rewritten Letter | 15 | All required components present; language is professional and specific; appropriate signatory |
| Part 2.1 — Bank Scenario | 10 | PCI DSS identified; Requirement 11.3 cited; CDE scope and data handling addressed |
| Part 2.2 — Medical Scenario | 10 | HIPAA identified; risk analysis context explained; PHI handling procedure described |
| Part 2.3 — EU Scenario | 10 | GDPR identified; Article 32 cited; data handling and 72-hour notification obligation addressed |
| Part 3.1 — Interesting System | 8 | Correct steps in correct order: stop, document, notify, await authorization |
| Part 3.2 — Active Breach | 9 | Testing stopped; client notified immediately; evidence preserved; correct continuation decision |
| Part 3.3 — Scope Expansion | 8 | Verbal authorization refused; RoE amendment process explained; third-party issue identified |
| Part 4 — RoE Gap Analysis | 20 | Six or more problems identified; risk explained clearly; corrective language specific and professional |
| **Total** | **100** | |

---

*This lab is for authorized educational purposes only. All scenarios, organizations, and documents are fictional. No actual systems are tested.*
