# Lab Activity: Module 02 - Business Process Management

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab develops your BPMN process modeling skills and your ability to design TO-BE process improvements for ERP implementation. You will analyze a described business scenario, draw BPMN diagrams, perform a gap analysis, and propose automation solutions using both SAP and Salesforce concepts.

**Estimated Time:** 90 minutes

**Submission:** Upload your completed lab document to Canvas under "Lab 02 — Business Process Management."

---

## Learning Objectives

By completing this lab you will be able to:

- Read a business scenario and extract the sequence of process steps, actors, and decision points
- Draw a valid BPMN 2.0 AS-IS process diagram with correct element types and swimlane assignments
- Identify bottlenecks and inefficiencies in a current-state process
- Design a TO-BE BPMN diagram that incorporates ERP automation, escalation rules, and workflow routing
- Map BPMN gateway types to their Salesforce Flow or SAP workflow equivalents
- Perform a structured gap analysis and classify each gap as process change, configuration, or customization

---

## Scenario Background

**Company:** Pinnacle Health Services
**Industry:** Healthcare administration
**Size:** 800 employees across four clinics
**Finance and HR system:** QuickBooks + manual HR folder

Pinnacle processes employee expense reports submitted by clinical and administrative staff. The current process operates as follows:

1. An employee fills out a paper expense form and hands it to their department supervisor.
2. The supervisor reviews the form, signs it if approved, and places it in the out-box on their desk.
3. The HR coordinator picks up the out-box daily at 4:00 PM and manually enters approved amounts into QuickBooks.
4. The HR coordinator also checks whether any required receipts are attached. If missing, the form is returned to the employee — by internal mail.
5. QuickBooks generates a check on Fridays for all approved expenses.
6. If an expense is over $500, it requires additional approval from the Finance Director. The supervisor must email the Finance Director separately, attaching a scanned copy of the form.
7. The Finance Director responds by email. If approved, the email is printed, attached to the paper form, and the cycle continues. If denied, the employee is notified by phone.
8. There is no tracking system. Neither employees nor supervisors know the status of submitted forms until a check arrives — or does not.

---

## Part A: AS-IS Process Analysis (25 points)

### A-1: Process Step Inventory

List every distinct step in Pinnacle's current expense process. For each step, identify:

- The step description
- The actor responsible
- Whether the step is manual or automated
- The average cycle time if estimable from the scenario
- Whether the step creates or relies on a physical document

Present your answer in a table with these five columns.

### A-2: AS-IS BPMN Diagram

Draw the complete AS-IS process using BPMN 2.0 notation. Your diagram must include:

- A start event and at least one end event
- All tasks from your Step Inventory in A-1
- Swimlanes for each actor: Employee, Supervisor, HR Coordinator, Finance Director
- Correct gateway types at each decision point (identify whether each decision is XOR, AND, or OR and justify your choice)
- Sequence flows connecting all elements in the correct order

You may draw by hand (photograph and attach) or use a diagramming tool. Label all elements clearly.

### A-3: Bottleneck Identification

Identify at least three specific bottlenecks in the current process. For each, state:

- Where in the process it occurs (which step)
- What type of bottleneck it is (resource constraint, time-gated step, information gap, or handoff delay)
- The estimated business impact (cost, delay, employee frustration, compliance risk)

---

## Part B: Gap Analysis (25 points)

### B-1: Fit-to-Standard Assessment

Pinnacle is evaluating two options for replacing their paper expense process:

- **Option A:** SAP SuccessFactors Employee Central with integrated expense workflow
- **Option B:** A Salesforce-based custom expense process using Salesforce Flow and Approval Processes

For each of the following requirements, indicate whether the standard tool meets the requirement, requires configuration, or would require customization. Briefly explain each classification.

| Requirement | SAP SuccessFactors | Salesforce Flow/Approvals | Classification Justification |
|---|---|---|---|
| Employee submits expense request digitally | | | |
| Supervisor receives immediate notification | | | |
| Automatic escalation to Finance Director over $500 | | | |
| Employee can check status in real time | | | |
| Receipts attached digitally at submission | | | |
| System generates payment on Friday automatically | | | |
| Full audit trail of all approvals with timestamps | | | |

### B-2: Gap Decision Matrix

For each gap you identified (where the standard system does not meet the requirement out of the box), complete the following decision:

- Recommended action: adapt the process, configure the system, or customize with code
- Reasoning for your recommendation
- Risk if customization is chosen instead of process adaptation

---

## Part C: TO-BE Process Design (35 points)

### C-1: TO-BE BPMN Diagram

Design the TO-BE process for Pinnacle's expense management after ERP implementation. Your TO-BE diagram must:

- Reduce the number of manual steps by at least 50% compared to AS-IS
- Eliminate the paper form entirely
- Include automated notifications at appropriate steps
- Include an escalation path for expenses over $500 using an event-based or timer intermediate event
- Use at least one parallel gateway where multiple actions should fire simultaneously
- Show the correct gateway types for all decision points

Label your diagram with the platform tool used at each automated step (e.g., "SAP Workflow Notification" or "Salesforce Flow Email Action").

### C-2: Bottleneck Resolution Summary

For each of the three bottlenecks you identified in A-3, describe specifically how the TO-BE process eliminates or reduces it. Reference the specific ERP feature (workflow automation, escalation rule, delegation rule, real-time notification, or system validation) that resolves each bottleneck.

### C-3: Time-Savings Estimate

Based on your AS-IS and TO-BE analysis:

- Estimate the current average total cycle time for a standard expense report (no escalation needed) from submission to payment
- Estimate the TO-BE cycle time with automation
- Calculate the reduction in days
- Multiply by 800 employees submitting an average of 1 expense per month to estimate the annual hours saved across the organization

Show your work and state your assumptions.

---

## Part D: Reflection (15 points)

### D-1: Certification Connection

In 100-150 words, explain how the tasks in this lab connect to at least one specific concept tested on either the Salesforce Certified Associate or SAP Certified Associate exam. Name the concept and describe why a certification candidate needs to understand it.

### D-2: Real-World Process Challenge

In 100-150 words, describe a real or hypothetical business process from a field you are interested in (healthcare, retail, finance, technology, education) that has at least one significant bottleneck. Explain what type of bottleneck it is and what ERP feature could resolve it.

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Step inventory table | 8 | All steps listed with actor, manual/auto, timing, document fields |
| A-2: AS-IS BPMN diagram | 10 | Correct element types, swimlanes, gateways, sequence flows |
| A-3: Bottleneck identification | 7 | 3 bottlenecks identified with type, location, and business impact |
| B-1: Fit-to-standard assessment | 12 | All 7 requirements assessed for both platforms with justification |
| B-2: Gap decision matrix | 13 | Each gap has recommended action, reasoning, and customization risk |
| C-1: TO-BE BPMN diagram | 15 | Reduces manual steps 50%+, includes escalation, parallel gateway, platform labels |
| C-2: Bottleneck resolution | 10 | Each bottleneck addressed with specific ERP feature |
| C-3: Time-savings estimate | 10 | Calculation shown, assumptions stated, result reasonable |
| D-1: Certification connection | 8 | Named concept, exam context, clear reasoning |
| D-2: Real-world challenge | 7 | Industry-specific bottleneck with ERP resolution |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile responses into a single document. Include both BPMN diagrams as embedded images or clearly labeled sketches.
2. Name your file: `Lab02_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 02 — Business Process Management."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day unless an extension is approved by Professor Nash in advance.

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Department BPMN with Exception Handling

A regional bank's loan origination process involves four departments: Customer Service, Credit Analysis, Legal, and Finance. The process must handle three exception paths: (1) incomplete application → return to customer, (2) credit score below threshold → automatic rejection, (3) legal review flags a compliance issue → escalate to VP.

1. Draw a complete BPMN 2.0 diagram with four swimlanes, at least two exclusive gateways (one for credit score routing, one for legal review outcome), one timer intermediate event (legal review must complete within 3 business days or escalate automatically), and clearly labeled start and end events.
2. Identify two places in the diagram where a parallel gateway could reduce total cycle time by running steps concurrently, and explain the tradeoff of doing so.
3. Annotate the diagram with estimated cycle times for each step. Calculate total cycle time for the "happy path" (no exceptions) and the longest exception path.
4. List three data fields that must be passed between swimlane handoffs and identify which ERP or CRM system would own each field as its system of record.

### Challenge 2: Process KPI Dashboard Design

You have been asked to build a process performance measurement framework for the purchase order approval process studied in Lab 02.

1. Define five KPIs for the PO approval process. For each KPI, specify: the metric name, how it is calculated, the data source (which SAP transaction or table), the target value, and the alert threshold that should trigger an escalation.
2. Identify which two KPIs are leading indicators (predict future problems) versus lagging indicators (report past outcomes), and explain why the distinction matters for process management.
3. Describe how a Salesforce dashboard or SAP Analytics Cloud report could visualize each KPI, specifying the chart type most appropriate for each metric.

### Reflection Questions

1. In the bank loan process, the timer escalation after 3 days adds complexity to the BPMN diagram. Under what circumstances is it worth this added complexity, and when might a simpler manual follow-up be preferable?
2. Which of the five KPIs you designed in Challenge 2 would be most difficult to collect from existing systems, and what data quality or integration work would be required to make it measurable?
