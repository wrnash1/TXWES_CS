# Lab Activity: Module 07 - Customer Relationship Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab develops your ability to map customer-facing business scenarios to Salesforce CRM objects, trace the Lead-to-Opportunity conversion process, analyze Service Cloud case management, and describe CRM-ERP integration data flows. All work is analytical and scenario-based.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 07 — Customer Relationship Management Modules."

---

## Learning Objectives

By completing this lab you will be able to:

- Map business events to the correct Salesforce standard object (Lead, Account, Contact, Opportunity, Case)
- Trace the Lead conversion process and explain what each resulting record represents
- Analyze an Opportunity pipeline and calculate forecasted revenue
- Apply Service Cloud SLA concepts to a customer escalation scenario
- Describe the integration data flow between Salesforce CRM and an ERP system at the point of order creation

---

## Scenario Background

**Company:** Pinnacle Software Solutions

**Industry:** B2B SaaS -- enterprise workflow automation software

**Size:** 220 employees, $48 million ARR (annual recurring revenue)

**CRM:** Salesforce Sales Cloud and Service Cloud, implemented 2 years ago

**Revenue team:** 18 account executives, 4 sales managers, 12 customer success representatives

Pinnacle's VP of Sales has asked you to analyze several CRM process issues the team has encountered since the Salesforce implementation.

---

## Part A: Object Mapping and Lead Conversion (30 points)

### A-1: Business Event to Salesforce Object

For each business event at Pinnacle, identify the correct Salesforce object that should be created or updated, and explain in one sentence why that object is the correct choice.

| Business Event | Salesforce Object | One-Sentence Justification |
|---|---|---|
| A marketing team member enters information about a company that downloaded a whitepaper from Pinnacle's website -- the contact has not been qualified yet | | |
| A sales rep calls Marcus Webb, the IT Director at Bridgecross Financial, and has an exploratory conversation -- Marcus's company uses a competitor product and has no current buying signal | | |
| After three weeks of conversations, Marcus Webb confirms that Bridgecross has budget approval and is actively evaluating vendors; his company is now a real prospect | | |
| The sales rep wins the deal with Bridgecross and the contract is signed for $85,000/year | | |
| Six months after go-live, Bridgecross's system administrator reports that automated reports are generating errors -- she needs help from Pinnacle's support team | | |
| Pinnacle's support team resolves the reporting error and documents the fix for future reference | | |

### A-2: Lead Conversion Analysis

A Pinnacle sales rep has the following Lead record:

- Lead Name: Jennifer Roark
- Lead Company: Meridian Health Group
- Lead Source: Trade Show
- Lead Status: Qualified
- Estimated Deal Size: $120,000
- Notes: Jennifer is the VP of Operations; she confirmed budget authority and signed NDA; demo scheduled for next week

Answer the following questions:

1. What triggers the decision to convert this Lead? What criteria has this Lead met that makes conversion appropriate?

2. When the sales rep converts this Lead, what three records does Salesforce create? Name the object type and describe what information goes into each one from the Lead record above.

3. After conversion, what happens to the original Lead record? Why is it retained rather than deleted?

4. What stage should the new Opportunity be set to after conversion, given the information in the Lead notes? Justify your answer.

---

## Part B: Pipeline Analysis and Forecasting (25 points)

### B-1: Pipeline Report Construction

The Pinnacle sales manager provides the following open Opportunity data for her team. Complete the Forecasted Revenue column using the Stage Probability values from the Module 07 Reading Guide.

| Opportunity | Owner | Amount | Stage | Close Date | Probability | Forecasted Revenue |
|---|---|---|---|---|---|---|
| Bridgecross Financial -- Year 2 Renewal | M. Torres | $85,000 | Negotiation | 2026-07-31 | | |
| Meridian Health Group -- New Deal | K. Park | $120,000 | Proposal / Price Quote | 2026-08-15 | | |
| Oakdale Manufacturing -- Platform Upgrade | S. Reyes | $42,000 | Qualification | 2026-09-30 | | |
| Coastal Logistics -- Net New | M. Torres | $67,000 | Needs Analysis | 2026-08-01 | | |
| Summit Financial -- Pilot | K. Park | $18,000 | Prospecting | 2026-10-31 | | |

Show your calculations and state the total forecasted revenue for the team.

### B-2: Pipeline Health Assessment

Review the pipeline data in B-1 and answer the following questions in 2-3 sentences each:

1. Which opportunity represents the highest financial risk to the quarter? Explain your reasoning using both stage probability and close date.

2. Which sales representative has the strongest near-term forecast based on deal stage and timing?

3. The VP of Sales wants to know whether the team will hit the $200,000 quarterly revenue target. Based on the pipeline data, what is your assessment, and what caveat is required when using forecasted revenue to project actual bookings?

---

## Part C: Service Cloud Case Management (25 points)

### C-1: Case Lifecycle Tracing

Pinnacle's support team uses a three-tier SLA:

- Priority 1 (system down): First response within 1 hour, resolution within 4 hours
- Priority 2 (major feature broken): First response within 4 hours, resolution within 24 hours
- Priority 3 (general question): First response within 24 hours, resolution within 72 hours

For each customer contact below, assign the correct priority level and describe what SLA Milestones apply. Then state whether an escalation would be triggered given the scenario details.

**Contact 1:** Bridgecross Financial's system administrator reports that the entire Pinnacle platform is inaccessible for all 200 of their users. The Case is created at 9:00 AM Monday. The first response is sent at 9:45 AM. By 4:00 PM the issue is still unresolved.

**Contact 2:** Meridian Health Group's operations manager submits a web form question asking how to configure a specific report filter. The Case is created Friday at 3:00 PM. The first response is sent Monday at 8:30 AM.

**Contact 3:** Summit Financial's IT Director calls to report that automated email notifications from the system stopped working at some point over the weekend -- the exact time is unknown. The Case is created Tuesday at 10:00 AM. The first response is sent at 11:30 AM.

### C-2: Escalation Scenario

The Bridgecross Financial Case from Contact 1 above reaches 5:00 PM Monday without resolution. The assigned support agent has a daily hard stop at 5:00 PM. Write a 100-150 word description of the Salesforce Service Cloud mechanisms that should be configured to handle this escalation automatically, without requiring a manager to manually monitor the Case. Reference at least two specific Service Cloud features by name.

---

## Part D: CRM-ERP Integration Analysis (20 points)

### D-1: Integration Data Flow Mapping

Pinnacle has integrated Salesforce CRM with their SAP S/4HANA ERP system. When a Salesforce Opportunity is marked Closed Won, a series of events must occur across both systems. Complete the integration flow table below.

| Step | System | Action | Data Involved |
|---|---|---|---|
| 1 | Salesforce | Sales rep marks Opportunity Closed Won | |
| 2 | Salesforce | | Opportunity data converted to Order |
| 3 | Integration layer | Order record transmitted to SAP | |
| 4 | SAP SD | | Customer name, products, quantities, pricing |
| 5 | SAP MM | | Available inventory checked against order |
| 6 | SAP FI | | Revenue recognized; receivable created |
| 7 | SAP FI-AR | Invoice generated and sent to customer | |
| 8 | Salesforce | | Open invoice, amount, due date |

### D-2: Integration Failure Analysis

Three months after the Salesforce-SAP integration goes live, the implementation team discovers that 12 Orders created in Salesforce over the past two weeks did not create corresponding Sales Orders in SAP. The finance team has no record of these deals. In 100-150 words, describe three possible causes of this integration failure and explain what governance or monitoring mechanism should have caught the issue sooner.

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Object mapping | 12 | All 6 events mapped to correct object with valid justification |
| A-2: Lead conversion analysis | 18 | Four questions answered completely with specific record details and reasoning |
| B-1: Pipeline forecast calculation | 10 | All 5 forecasted revenues calculated correctly; total accurate |
| B-2: Pipeline health assessment | 15 | Three questions answered with reference to stage probability and timing |
| C-1: Case priority and SLA assignment | 15 | Correct priority for each contact; correct Milestones identified; escalation determination accurate |
| C-2: Escalation scenario | 10 | 100-150 words; two specific Service Cloud features named and described |
| D-1: Integration data flow mapping | 10 | All steps completed with accurate system, action, and data descriptions |
| D-2: Integration failure analysis | 10 | 100-150 words; three causes identified; monitoring mechanism described |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab07_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 07 -- Customer Relationship Management Modules."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.

---

## Part 9 — Challenge Exercise

### Challenge 1: Full Sales Process Configuration Design

You are the Salesforce administrator for a commercial real estate firm. The firm has two distinct sales processes: (1) Tenant Representation (helping businesses find office space — 9-month average cycle) and (2) Investment Sales (selling commercial properties — 18-month average cycle). Each requires different stages, required fields, and reporting.

1. Design the Stage picklist values for each Sales Process. Include at minimum 6 stages per process, with a probability percentage for each stage. Explain why the probabilities differ between the two processes at equivalent points in the cycle.
2. Define the Key Fields and Guidance for Success content (2-3 bullet points) for two stages in each Sales Process that would be configured in the Salesforce Path component.
3. Design the Record Types and Page Layouts required to support both processes simultaneously in one Salesforce org. Specify which fields appear on each layout and which are exclusive to each transaction type.
4. Build a Matrix Report specification (not the actual report — just the design) showing: rows = Stage, columns = Agent Name, values = SUM of Opportunity Amount. Describe how a sales manager would use this report in a weekly pipeline review call.

### Challenge 2: CRM-ERP Order-to-Cash Integration Failure Analysis

A manufacturing company has Salesforce Sales Cloud integrated with SAP S/4HANA via MuleSoft. When a rep marks an Opportunity as Closed Won in Salesforce, an SAP Sales Order should be automatically created within 5 minutes. Over the past two weeks, 15% of Closed Won Opportunities have failed to create an SAP Sales Order, causing order fulfillment delays of 2-5 days.

1. Identify five possible root causes for the integration failure, categorized as: Salesforce-side data quality issues, MuleSoft middleware failures, and SAP-side rejection reasons. For each cause, specify what data or log you would examine to confirm or rule it out.
2. Design a monitoring solution using Salesforce Reports and Dashboards that would detect this failure pattern within 1 hour of it occurring. Specify the report type, filters, grouping, and the alert mechanism.
3. Write the data mapping specification for the three most critical fields that must be correctly translated from Salesforce to SAP for the Sales Order to be created successfully: specify the Salesforce field name, the SAP field/table, the data type in each system, and a transformation rule if the formats differ.

### Reflection Questions

1. In the sales process design challenge, you created separate stages for Tenant Representation and Investment Sales. What happens to pipeline forecasting accuracy when salespeople skip stages in Salesforce versus when the stage sequence is enforced by the system — and what is the right balance between process enforcement and sales rep autonomy?
2. The integration failure analysis revealed that a 15% failure rate was going undetected for two weeks. What organizational process failure allowed this to persist, and what monitoring governance should have been in place at the time of the integration go-live?
