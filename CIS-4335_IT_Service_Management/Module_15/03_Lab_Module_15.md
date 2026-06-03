# Lab Activity: Module 15 — DevOps, Agile, and ITIL 4 Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Scenario: Brightway Commerce Platform

Brightway is an e-commerce company with 2.1 million active customers. The engineering team uses Scrum with two-week sprints. The operations team is a separate department. Development and operations use different ticketing systems, have different performance metrics, and rarely communicate outside of scheduled release meetings.

A post-incident review following a four-hour checkout outage (caused by a deployment made without notifying operations) has prompted the CTO to hire a DevOps transformation consultant. You are that consultant. You will analyze the current delivery process, identify waste, design a CI/CD pipeline with ITSM integration, and develop a flow measurement plan.

---

## Exercise 1: Value Stream Map — Current State (25 points)

The following process data was collected for Brightway's current feature delivery value stream — from when a product story is accepted into a sprint through to production deployment.

| Step | Activity | Value-Added? | Activity Duration | Wait Time Before Step |
|---|---|---|---|---|
| 1 | Developer writes code and unit tests | Yes | 8 hours | 0 hours (sprint start) |
| 2 | Developer submits pull request for code review | No (handoff) | 15 minutes | 4 hours (reviewer availability) |
| 3 | Peer code review and approval | Yes | 2 hours | 0 hours |
| 4 | Merge to integration branch; automated CI pipeline runs | Yes | 45 minutes | 0 hours |
| 5 | QA team picks up build for manual testing | No (handoff) | 10 minutes | 16 hours (QA queue wait) |
| 6 | QA manual functional testing | Yes | 3 hours | 0 hours |
| 7 | QA submits change request to Change Advisory Board | No (handoff) | 20 minutes | 0 hours |
| 8 | CAB meets and reviews change request | Yes | 30 minutes | 48 hours (next scheduled CAB) |
| 9 | Operations receives approved change; schedules deployment | No (handoff) | 15 minutes | 24 hours (operations scheduling lag) |
| 10 | Operations deploys to staging for validation | Yes | 2 hours | 0 hours |
| 11 | Operations deploys to production | Yes | 1 hour | 0 hours |

### Task 1a: Value-Added Ratio Calculation

Calculate the following:

- Total value-added time (sum of activity durations for value-added steps only): _______________
- Total non-value-added time (sum of wait times and handoff durations): _______________
- Total lead time (sum of all activity durations and wait times): _______________
- Value-added ratio (total value-added time / total lead time, expressed as percentage): _______________

### Task 1b: Waste Identification

Identify the three greatest sources of waste in the current state value stream. For each, describe:

- What the waste is
- Why it occurs (root cause)
- What category of waste it represents (wait, handoff, rework, or unnecessary process)

### Task 1c: Impact Statement

Write a 75–100 word statement explaining what the current value-added ratio means in practical terms for Brightway — specifically how it relates to the four-hour checkout outage and the organization's ability to respond to production incidents quickly.

---

## Exercise 2: Future-State Value Stream Design (25 points)

Design a future-state value stream for Brightway's feature delivery process that eliminates or significantly reduces the three wastes identified in Exercise 1. You do not need to eliminate all wait time — but you must demonstrate a meaningful improvement in the value-added ratio.

### Task 2a: Redesigned process table

Create a redesigned process table using the same format as the current-state table. You may combine, eliminate, or automate steps. You must retain at least one human approval gate (for normal changes) and demonstrate where ITSM practice integration points appear. Show the step number, activity name, value-added designation, estimated activity duration, and estimated wait time.

### Task 2b: Value-Added Ratio improvement

Calculate the new value-added ratio for your future-state design and state the improvement over the current state.

### Task 2c: Change type classification

In your future-state design, most routine feature deployments would flow through the pipeline as which type of change (standard, normal, or emergency)? Write 75–100 words justifying your classification and explaining what criteria Brightway would use to distinguish routine deployments from deployments that require a normal change process.

---

## Exercise 3: CI/CD Pipeline Design with ITSM Gates (25 points)

Design a CI/CD pipeline for Brightway that integrates ITSM practice touchpoints at appropriate stages. Your pipeline must cover the full path from code commit to production deployment.

### Task 3a: Pipeline stage map

Create a pipeline stage map with at least eight stages. For each stage, specify:

- Stage name
- What happens at this stage (one sentence)
- Whether this stage is automated or manual
- Which ITSM practice this stage connects to (if applicable)

Present as a table with those four columns.

### Task 3b: Approval gate design

Describe your approval gate design in 100–150 words. Address:

- What conditions allow a deployment to pass the approval gate automatically (standard change criteria)
- What conditions pause the pipeline for human approval (normal change criteria)
- How the emergency change path works — what logging and post-hoc review is required

### Task 3c: Failure handling

Describe the automated failure handling logic at two points in the pipeline: (1) when automated tests fail before deployment, and (2) when post-deployment smoke tests fail after production deployment. For each, specify what automated action is taken and what ITSM record is created.

---

## Exercise 4: Flow Measurement Plan (25 points)

Brightway's CTO wants to establish a DevOps performance baseline and measure improvement after the transformation. Design a flow measurement plan using the DORA Four Keys framework.

### Task 4a: Baseline measurement plan

For each of the four DORA metrics — Deployment Frequency, Lead Time for Changes, Change Failure Rate, and Time to Restore Service — specify:

- How Brightway would measure this metric (what data source, what formula)
- What Brightway's approximate current baseline is based on the current-state VSM and incident data
- What a realistic 12-month improvement target would be and why

Present as a table with those four columns.

### Task 4b: ITIL 4 practice mapping

Write a 100–150 word paragraph explaining which DORA metrics are most closely connected to ITIL 4 practices, and specifically which practices Brightway must mature to improve each of the four metrics. Reference at least three specific ITIL 4 practices.

### Task 4c: Error budget proposal

Brightway's most critical service is its checkout flow. The current availability, based on incident records, is approximately 99.5% monthly. The engineering team wants to increase deployment frequency. Propose an SLO and calculate the corresponding monthly error budget. Then write 75–100 words explaining how the error budget would govern the pace of deployment changes — specifically when deployments would be paused and when they would be permitted.

---

## Submission

Submit your completed lab document to the Canvas assignment portal by the due date. All calculations must show your work. All written responses must use specific terminology from the module — vague or generic answers will not receive full credit.

**Grading:** Each exercise is worth 25 points distributed across tasks based on accuracy, completeness, and quality of reasoning.
