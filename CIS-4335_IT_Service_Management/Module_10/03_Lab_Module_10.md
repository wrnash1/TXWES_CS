# Lab Activity: Module 10 — Service Level Management and SLAs

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Total Points: 100

---

## Lab Overview

You are the IT Service Manager at Pinnacle Property Management, a real estate services
firm with 900 employees across twelve offices. Pinnacle's IT department provides services
to internal staff and manages a tenant-facing web portal used by 15,000 active tenants.

Your tasks in this lab involve designing an SLA, analyzing a breach scenario, and
preparing a service review meeting report.

**Estimated time:** 90–120 minutes

**Submission format:** PDF or Word document uploaded to the course LMS

**Learning objectives:**

- Design a complete, business-aligned SLA for a realistic service
- Identify and align OLA and UC commitments with SLA targets
- Conduct SLA breach analysis and design corrective actions
- Prepare a service review meeting report with accurate, honest metrics

---

## Part A: SLA Design (40 points)

### Part A Scenario

Pinnacle's tenant-facing web portal — TenantConnect — allows tenants to pay rent, submit
maintenance requests, communicate with property managers, and access lease documents.
The portal is hosted on a cloud provider (CloudBase Inc.) under an existing contract.
Internal support is provided by the Application Support team and the Infrastructure team.

You have been asked to draft the initial SLA for TenantConnect. The following business
requirements were gathered in stakeholder interviews:

- Tenants expect the portal to be available 24 hours a day, 7 days a week
- The VP of Property Management considers 99.5% monthly availability to be the minimum
  acceptable level
- Maintenance requests submitted through the portal must be acknowledged within 4 hours
  (this is a legal requirement in the firm's lease agreements)
- The portal currently experiences an average of 3.2 hours of unplanned downtime per month
- The peak usage period is the 1st–5th of each month when rent payments are due
- The Infrastructure team currently has no documented response time commitment to the
  Application Support team
- CloudBase Inc. currently guarantees 99.7% availability in their contract

### Part A Instructions

Design a complete SLA for the TenantConnect portal. Your SLA must include all ten
required components from the Module 10 reading guide:

1. Service description (include scope and explicit exclusions)
2. Service hours
3. Availability target (calculate whether the current 3.2 hours downtime meets the
   proposed target and state your finding)
4. Performance targets (at least three measurable targets beyond availability)
5. Priority-based resolution targets (define P1–P4 with acknowledgment and resolution
   times appropriate to this service)
6. Support model (how tenants and staff contact IT; escalation path)
7. Measurement and reporting (how availability is calculated; report frequency)
8. Breach notification (timeline and method for notifying the VP of Property Management)
9. Review schedule
10. Exceptions (list at least three specific exception conditions)

Additionally, design:

- One OLA between the Infrastructure team and the Application Support team (include at
  least two specific targets)
- A brief UC assessment: does the CloudBase Inc. guarantee of 99.7% adequately underpin
  a 99.5% SLA target? Explain why or why not.

### Part A Scoring Rubric

| Criterion | Points |
|---|---|
| All ten SLA components present and complete | 20 |
| Availability calculation performed and conclusion stated | 4 |
| OLA includes at least two specific, aligned targets | 6 |
| UC assessment correctly evaluates alignment | 4 |
| SLA targets are business-based (not provider-centered) | 6 |
| **Total Part A** | **40** |

---

## Part B: SLA Breach Analysis (35 points)

### Part B Scenario

During the month of October, the following events occurred at Pinnacle:

- **Oct 1, 11:47 PM:** TenantConnect portal becomes unavailable. Rent payment transactions
  fail for all tenants. Service restored at Oct 2, 2:14 AM. Total downtime: 2 hours 27 minutes.

- **Oct 3, 9:30 AM:** The portal is accessible but maintenance request submissions are
  failing silently — tenants receive no error message but requests are not recorded.
  Issue discovered by staff at 11:15 AM when tenants begin calling. Resolved at 2:40 PM.
  Total affected window: approximately 5 hours 10 minutes.

- **Oct 14, 3:00 PM–3:45 PM:** Planned maintenance window conducted by the Infrastructure
  team (45 minutes). Advance notice was sent to the VP of Property Management 24 hours
  prior.

- **Oct 22, 8:15 AM:** Three tenants report intermittent slow response times. Investigation
  finds a background database optimization job is consuming resources. Resolved at 9:00 AM
  (45 minutes).

Assume the SLA you designed in Part A is in effect. October has 744 hours of service time.

### Part B Instructions

#### Task 1: Breach Assessment (15 points)

For each of the four October events:

1. Determine whether it constitutes an SLA breach under your Part A SLA
2. If a breach: identify the breach type (technical, process, OLA, or UC)
3. State the specific SLA target that was or was not breached
4. Calculate the impact on October's availability percentage

Show your availability calculation for October including all applicable downtime.

#### Task 2: Breach Communication (10 points)

For the Oct 1–2 portal outage, draft the proactive breach notification that should be
sent to the VP of Property Management once the breach is confirmed. Your notification
must follow the communication template from the Module 08 reading guide and include:

- The time the breach is being communicated (choose a realistic time)
- The nature of the breach (what SLA target was missed and by how much)
- The cause (as known at time of communication)
- The actions taken and completed
- The next steps

#### Task 3: Corrective Action Plan (10 points)

For any confirmed breaches from Task 1, create a corrective action plan. For each breach:

- Identify the root cause category (technology, process, OLA gap, UC gap)
- Propose one specific corrective action
- Assign an owner (by role, not name)
- Set a due date (relative, e.g., "within 30 days")
- Identify which improvement register the action belongs in (Problem Management,
  Change Enablement, SLM review, OLA renegotiation, UC renegotiation)

### Part B Scoring Rubric

| Criterion | Points |
|---|---|
| Each event correctly assessed as breach or non-breach with justification | 8 |
| Availability calculation is arithmetically correct | 4 |
| Breach types correctly identified for each breach | 3 |
| Breach notification follows required format and is appropriately timed | 10 |
| Corrective actions are specific, have owners, and are linked to the right register | 10 |
| **Total Part B** | **35** |

---

## Part C: Service Review Meeting Preparation (25 points)

### Part C Instructions

Prepare the October service review meeting package for the VP of Property Management.
Your package must include:

#### Section 1: Executive Summary (5 points)

A 150–200 word summary written for a non-technical executive. Cover:

- Overall service performance for October (good news and bad news)
- The two incidents and their status
- One key improvement action underway
- Your overall assessment: is TenantConnect trending better or worse?

Write this section as if you are the IT Service Manager presenting to the VP. Be honest.

#### Section 2: Performance Dashboard (10 points)

Create a performance table covering October with the following rows:

- Availability: target, actual, status (met/breached)
- P1 incident count and SLA compliance rate
- P2 incident count and SLA compliance rate
- Maintenance request acknowledgment rate: target, actual, status
- Planned maintenance events: count, advance notice provided (yes/no)
- Customer satisfaction score (make up a plausible survey result between 3.2 and 4.1
  out of 5.0 and note it is based on a 47-response survey)

Use a simple table format with clear status indicators (Met / Breached / N/A).

#### Section 3: Action Items Register (10 points)

Create a formal action items register for the meeting with at least five items. For each
item include:

- Action item number
- Description (specific and actionable)
- Owner (by role)
- Due date (relative)
- Status (New / In Progress / Complete)
- Source (e.g., "Oct 1 breach PIR," "OLA gap identified," "customer feedback")

### Part C Scoring Rubric

| Criterion | Points |
|---|---|
| Executive summary is honest, business-appropriate, and 150–200 words | 5 |
| Performance dashboard includes all six required rows with correct status | 6 |
| Dashboard data is consistent with Part B breach analysis | 4 |
| Action items register has 5+ items with all required fields | 10 |
| **Total Part C** | **25** |

---

## Submission Checklist

Before submitting, verify:

- [ ] Part A: SLA with all ten components, OLA, and UC assessment
- [ ] Part B: Breach assessment table, availability calculation, breach notification,
  and corrective action plan
- [ ] Part C: Executive summary, performance dashboard, and action items register
- [ ] Document includes your name, student ID, and submission date
- [ ] File saved as PDF or Word and uploaded to the LMS before the deadline

---

## Grading Summary

| Part | Points |
|---|---|
| Part A: SLA Design | 40 |
| Part B: SLA Breach Analysis | 35 |
| Part C: Service Review Meeting Preparation | 25 |
| **Total** | **100** |

---

Module 10 Lab | CIS-4335 IT Service Management | Texas Wesleyan University
