# Lab Activity: Module 09 — Problem and Change Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Total Points: 100

---

## Lab Overview

This lab places you in the role of IT Service Manager at Crestwood Community College,
a regional institution with 8,000 students and 600 staff. You will conduct a root cause
analysis using the 5 Whys technique, design a change management workflow, and classify
a set of change scenarios.

**Estimated time:** 90–120 minutes

**Submission format:** PDF or Word document uploaded to the course LMS

**Learning objectives:**

- Conduct a structured root cause analysis using the 5 Whys technique
- Create a known error database entry from an RCA outcome
- Classify changes as standard, normal, or emergency with justification
- Design a change request template that meets CAB review requirements
- Evaluate the integration of Problem Management and Change Enablement

---

## Part A: Root Cause Analysis — 5 Whys (30 points)

### Part A Background

Crestwood Community College has experienced the following recurring incident pattern
over the past eight weeks:

- **Week 1:** Student registration portal unavailable for 47 minutes on Monday morning
- **Week 3:** Student registration portal unavailable for 1 hour 12 minutes on Tuesday
- **Week 5:** Student registration portal slow/unresponsive for 3 hours on Monday
- **Week 7:** Student registration portal unavailable for 2 hours on Monday morning

Each time, the service desk restores the portal by restarting the application server.
The issue always occurs on Monday mornings between 8:00 AM and 10:00 AM. No problem
record has been raised until now.

Investigation notes gathered so far:

- The portal uses a shared application server (AppSrv-01) that hosts six other
  applications in addition to the registration portal
- A weekly database maintenance job runs every Sunday night at 11:00 PM
- AppSrv-01 logs show memory utilization above 95% at the time of each incident
- The maintenance job is configured to run for "up to 8 hours"
- No changes to AppSrv-01 have been logged in the change schedule

### Part A Instructions

#### Task 1: Conduct the 5 Whys (15 points)

Using the investigation notes above, perform a 5 Whys root cause analysis for the
registration portal outages. Present your analysis in a table with three columns:

- Why Number (1–5)
- The "Why?" question asked
- The answer derived from the investigation notes

Your fifth "why" should arrive at a systemic or process-level root cause — not just a
technical symptom.

#### Task 2: Document a Known Error Record (15 points)

Based on your RCA, create a Known Error Database (KEDB) entry for this problem. Your
entry must include all seven fields:

1. Problem ID (assign one: KE-2024-001)
2. Affected service (name it)
3. Description (what is the known error?)
4. Root cause (from your 5 Whys)
5. Workaround (what can the service desk do right now to restore service when this
   recurs, before the permanent fix is deployed?)
6. Status (use: "Permanent fix pending — Change record CR-2024-047 raised")
7. Linked change record (reference CR-2024-047)

### Part A Scoring Rubric

| Criterion | Points |
|---|---|
| 5 Whys table is logically consistent with investigation notes | 10 |
| Fifth why reaches a systemic or process-level root cause | 5 |
| KEDB entry includes all seven required fields | 10 |
| Workaround is practical and specific to the incident pattern | 5 |
| **Total Part A** | **30** |

---

## Part B: Change Classification and CAB Review (40 points)

### Part B Instructions

Crestwood IT has a queue of ten proposed changes. For each change:

1. Classify it as Standard, Normal, or Emergency
2. Provide a two-sentence justification citing the characteristics that determine the
   classification
3. Identify the appropriate change authority (pre-approved process / CAB / ECAB)

### Changes to Classify

1. Restart the registration portal application server (AppSrv-01) during the next
   Monday outage using the documented restart procedure.

2. Resize the memory allocation on AppSrv-01 from 16 GB to 32 GB to address the
   root cause identified in Part A. This requires a 30-minute maintenance window and
   has been tested in the staging environment.

3. Apply an emergency security patch to the student email system after a vendor
   advisory confirms an active exploit is being used in the wild. The patch has not
   been tested internally.

4. Add three new faculty members to the existing Faculty Distribution List in
   Microsoft 365. This is done weekly using a documented, pre-approved process.

5. Migrate the registration portal from AppSrv-01 to a new dedicated application
   server (AppSrv-07) with load balancing. The project has been in design for two
   months and is ready for production deployment.

6. Roll back a software update deployed last night that broke the financial aid
   calculator for all students. The rollback script has been tested and is ready.
   Financial aid applications are due in 48 hours.

7. Update the DNS record for the student Wi-Fi captive portal to point to a new
   authentication server. This has been done previously following a standard procedure
   that requires only a 5-minute outage.

8. Decommission a legacy server (LegacySrv-03) that hosts a retired application.
   No active users. IT must coordinate with the vendor to confirm no hidden dependencies.

9. Reset the password for the shared IT monitoring service account after it was
   accidentally changed by a new employee, causing monitoring alerts to fail.

10. Deploy a new Learning Management System (LMS) version upgrade across all 8,000
    student accounts. This involves database migration, third-party integration updates,
    and a 4-hour maintenance window during spring break.

### Part B Deliverable

A table with four columns: Change Number, Classification, Change Authority, Justification.

### Part B Scoring Rubric

| Criterion | Points |
|---|---|
| Correct classification assigned (3 pts each × 10) | 30 |
| Correct change authority identified for each (0.5 pts each) | 5 |
| Justifications cite specific classification criteria | 5 |
| **Total Part B** | **40** |

---

## Part C: Change Request Design (30 points)

### Part C Scenario

Change CR-2024-047 has been raised to permanently fix the AppSrv-01 memory issue
identified in Part A. The proposed change is to increase AppSrv-01 memory from 16 GB
to 32 GB and reconfigure the Sunday maintenance job to complete before 6:00 AM.

This is a Normal change requiring CAB review.

### Part C Instructions

Design a complete change request document for CR-2024-047. Your change request must
include all nine sections below.

#### Section 1: Change Identification

- Change ID: CR-2024-047
- Change title (write a descriptive title)
- Requestor name and role
- Date submitted
- Target implementation date (choose a realistic date and justify it)

#### Section 2: Description of Change

Two to three sentences describing exactly what is being changed, why, and what the
desired outcome is. Reference the linked problem record (KE-2024-001).

#### Section 3: Business Justification

Two to three sentences explaining the business impact of NOT making this change, and
the business benefit of proceeding.

#### Section 4: Technical Scope

List the specific systems, services, applications, and configuration items affected
by this change.

#### Section 5: Risk Assessment

Identify at least three risks associated with this change and rate each as High, Medium,
or Low. For each risk, describe a mitigation step.

#### Section 6: Testing Evidence

Describe what testing has been done in the staging environment and what the results were.

#### Section 7: Implementation Plan

A step-by-step numbered list of the implementation actions (minimum five steps).

#### Section 8: Rollback Plan

A step-by-step numbered list of the rollback actions if the change fails (minimum
three steps). Include the trigger condition that would initiate rollback.

#### Section 9: CAB Review Summary

Write three to four sentences summarizing what you would present to the CAB: the key
risk, the key mitigation, the proposed maintenance window, and your confidence level
based on staging test results.

### Part C Scoring Rubric

| Criterion | Points |
|---|---|
| All nine sections are present and complete | 9 |
| Risk assessment includes 3+ risks with mitigations | 6 |
| Implementation plan has 5+ logical, ordered steps | 6 |
| Rollback plan includes trigger condition and 3+ steps | 6 |
| CAB summary is persuasive and references testing evidence | 3 |
| **Total Part C** | **30** |

---

## Submission Checklist

Before submitting, verify:

- [ ] Part A: 5 Whys table with five rows and three columns
- [ ] Part A: KEDB entry with all seven fields
- [ ] Part B: Classification table with all 10 changes and justifications
- [ ] Part C: Change request with all nine sections
- [ ] Document includes your name, student ID, and submission date
- [ ] File saved as PDF or Word and uploaded to the LMS before the deadline

---

## Grading Summary

| Part | Points |
|---|---|
| Part A: Root Cause Analysis and KEDB Entry | 30 |
| Part B: Change Classification and CAB Review | 40 |
| Part C: Change Request Design | 30 |
| **Total** | **100** |

---

Module 09 Lab | CIS-4335 IT Service Management | Texas Wesleyan University
