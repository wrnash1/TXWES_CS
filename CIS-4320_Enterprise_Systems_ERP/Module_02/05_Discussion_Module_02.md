# Discussion Forum: Module 02 - Business Process Management

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

---

## Overview

This forum asks you to apply BPMN concepts and process analysis to real business scenarios. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175-225 words** that directly addresses the questions for your chosen scenario. Begin your post by identifying which scenario you selected.

Your post must:

- Name and correctly apply at least one BPMN element (gateway type, swimlane, event, or task) to the scenario
- Identify at least one specific bottleneck in the current process and name its type (resource constraint, time-gated step, information gap, or handoff delay)
- Propose a concrete TO-BE improvement using a named ERP feature (workflow automation, escalation rule, Flow Builder, etc.)

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Extend your classmate's bottleneck analysis with an additional bottleneck they may have missed
- Challenge whether the BPMN element they applied was the most appropriate choice and explain your alternative
- Describe how the improvement your classmate proposed would look specifically in either Salesforce Flow Builder or an SAP workflow, with one concrete detail

---

## Scenarios

### Scenario A: The Hiring Bottleneck

A regional hospital system uses paper job applications and a multi-stage interview process. Applications are received by HR and sorted manually. Qualified resumes are emailed to the hiring manager. The hiring manager reviews resumes when time allows and replies by email with a short list. HR then individually calls each short-listed candidate to schedule phone screens. After phone screens, the hiring manager selects two finalists, who are scheduled for in-person panel interviews by emailing three department heads to find a common available time. The average time from job posting to offer letter is 47 business days.

**Your task:** Identify the primary bottleneck type (with evidence from the scenario). Using BPMN notation, describe what type of gateway would control the transition from resume review to phone screen scheduling, and justify your choice. Propose one specific ERP or workflow automation improvement that would reduce the average time-to-hire, and estimate how much time it could save.

### Scenario B: The Invoice Approval Loop

A construction company's subcontractor invoices go through a five-step approval process: project manager approves the hours, accounting verifies the rate, the VP of Operations approves invoices over $50,000, the accounting manager enters the invoice into QuickBooks, and the check is issued on the 15th and last day of each month. Currently, 35% of invoices are returned for corrections after step 1 because the subcontractor's invoice format does not match the company's requirements. Each correction cycle takes an average of 4 business days and requires re-entry at step 1.

**Your task:** What BPMN element would you use to model the correction rework loop? What type of bottleneck does the 35% rejection rate represent? Design a TO-BE process improvement that reduces the rework rate, and explain whether the solution would be classified as process change, configuration, or customization in a gap analysis.

### Scenario C: The Disconnected Sales Handoff

A software company's sales team uses Salesforce to manage opportunities. When a deal closes, a salesperson emails the implementation team with a PDF summary of what was sold. The implementation team creates a project in their separate project management tool by re-entering data from the PDF. Three months after an ERP audit, the company discovers that 22% of closed deals have never had an implementation project created — the emails were missed, lost, or assigned to the wrong person.

**Your task:** What BPMN element (specifically which gateway or event type) would you use to trigger the implementation project creation automatically when a deal closes in Salesforce? Describe the specific Salesforce automation tool you would use and how it would eliminate the 22% loss rate. What swimlane change in the TO-BE process diagram reflects the automation replacing the manual email step?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Post clearly states which scenario was chosen |
| BPMN element applied correctly and by name | 1 | Named element (gateway type, swimlane, event) correctly applied to scenario |
| Bottleneck identified with type and evidence | 2 | Type named (resource, time-gated, information gap, handoff), evidence from scenario cited |
| Concrete TO-BE improvement with ERP feature named | 1 | Specific feature (escalation rule, Flow, workflow automation) named and applied |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive contribution | 2 | Extends, challenges, or concretely adds platform detail |
| Peer response 2: 60+ words, substantive contribution | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

The most common mistake in process analysis is jumping to the TO-BE solution before fully understanding the AS-IS problem. When you write your post, spend at least half your word count describing the current-state problem clearly before proposing the improvement. Certification exam questions that test BPM present scenarios first — your ability to analyze the scenario before selecting an answer is exactly what they are measuring.
