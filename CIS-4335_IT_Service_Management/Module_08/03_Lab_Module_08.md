# Lab Activity: Module 08 — Service Desk, Incident Management, and Monitoring

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Total Points: 100

---

## Lab Overview

This lab puts you in the role of an IT Service Manager at Meridian Financial Services,
a mid-sized wealth management firm with 1,200 employees across four offices. Your lab
tasks involve designing incident priority criteria, documenting a major incident process
flow, and analyzing a monitoring event scenario.

**Estimated time:** 90–120 minutes

**Submission format:** PDF or Word document uploaded to the course LMS

**Learning objectives:**

- Apply the impact/urgency priority model to realistic incident scenarios
- Design a major incident response process with defined roles and communication steps
- Analyze a monitoring event scenario and identify process gaps
- Recommend shift-left improvements for a described service desk environment

---

## Part A: Incident Priority Classification (25 points)

### Part A Scenario

Meridian Financial Services operates the following critical systems:

- **TradeExec** — real-time trade execution platform (all 1,200 users depend on it)
- **ClientPortal** — client-facing web portal (used by approximately 8,000 external clients)
- **RiskCalc** — risk analytics tool (used by 15 analysts)
- **Email** — corporate email system (all 1,200 employees)
- **PrintServ** — print server for the downtown office (80 users)

### Part A Instructions

For each of the eight incidents below, assign:

1. An impact level (High / Medium / Low)
2. An urgency level (High / Medium / Low)
3. A priority (P1 / P2 / P3 / P4 / P5)
4. A one-sentence justification

### Incidents to Classify

1. TradeExec is completely unavailable. All trading activity has halted at 10:22 AM on a
   Tuesday during market hours.

2. ClientPortal is responding slowly — page loads take 12 seconds instead of the normal
   2 seconds. Some external clients are complaining but can still access their accounts.

3. A single analyst's RiskCalc instance crashes every time she runs a specific report.
   Other analysts are unaffected. She can use an alternative report format as a workaround.

4. The corporate email system is rejecting all inbound emails from external senders. No
   outbound issues. Impact discovered at 4:55 PM on a Friday.

5. PrintServ is offline. The 80 downtown office users cannot print. All work can continue
   via digital documents.

6. Three users report that their VPN client is not connecting from home. All three can use
   the web-based VPN alternative.

7. TradeExec is showing incorrect pricing data on one asset class (municipal bonds) for
   all users. Data is visibly wrong but the system remains accessible.

8. A single laptop in the accounting department will not connect to the wireless network.
   The user has a wired connection available.

### Part A Deliverable

A table with five columns: Incident Number, Impact, Urgency, Priority, Justification.

### Part A Scoring Rubric

| Criterion | Points |
|---|---|
| Correct priority assigned (2 pts each × 8 incidents) | 16 |
| Impact and urgency levels are consistent with priority | 5 |
| Justifications use ITIL 4 terminology correctly | 4 |
| **Total Part A** | **25** |

---

## Part B: Major Incident Process Design (45 points)

### Part B Scenario

Incident 1 from Part A — TradeExec complete outage during market hours — has been declared
a Major Incident (P1). You are the IT Service Manager. You have 12 staff available and
a vendor support contract with the TradeExec software vendor (4-hour response SLA).

### Part B Instructions

Design a Major Incident Response Plan for this specific scenario. Your plan must include
all five elements below.

#### Element 1: Role Assignments (10 points)

Define the four war room roles for this incident:

- Incident Commander
- Technical Lead
- Communications Lead
- Scribe / Recorder

For each role, write 2–3 sentences describing: who should fill this role (job title or
function), what their specific responsibilities are during this P1, and one decision
they are authorized to make without escalation.

#### Element 2: Communication Timeline (10 points)

Create a communication timeline for the first 90 minutes of the incident. Include:

- Time 0:00 — Incident declared; war room activated
- At least four additional communication touchpoints (what is communicated, to whom,
  by which role, through which channel)
- The 30-minute stakeholder update schedule with a template message

Your template message should follow this format:

> **[TIME] — Meridian IT Service Status Update**
> Service affected: [name]
> Current status: [what is known]
> User impact: [who is affected and how]
> Actions underway: [what the team is doing]
> Next update: [time of next scheduled communication]

#### Element 3: Escalation Decision Tree (10 points)

Create a simple escalation decision tree for this incident. The tree must answer the
following decision points:

1. If root cause is identified within 30 minutes — what happens?
2. If root cause is NOT identified within 30 minutes — what happens?
3. If the TradeExec vendor is engaged but does not respond within their 4-hour SLA —
   what happens?
4. If a workaround is available but requires taking a secondary system offline — who
   must authorize?

Present this as a numbered list with Yes/No branches or as a simple diagram with labels.

#### Element 4: Resolution and Closure Criteria (5 points)

Define specific, measurable criteria that must be met before this incident can be closed.
Provide at least four criteria. Example: "All TradeExec users confirm trade execution
is functioning normally" — but write your own four criteria appropriate to this scenario.

#### Element 5: Post-Incident Review Plan (10 points)

Design a Post-Incident Review (PIR) agenda for the review that should occur within 72
hours of resolution. Your agenda must include:

- Meeting duration and attendee list (by role)
- At least five agenda items with a time allocation for each
- A template for the three key outputs of the PIR:
  1. Timeline of the incident (what happened and when)
  2. Contributing factors (what made the incident worse or harder to resolve)
  3. Action items (what will change to prevent recurrence — each with an owner and
     a due date)

### Part B Scoring Rubric

| Criterion | Points |
|---|---|
| Role assignments are complete and specific (4 roles × 2.5 pts) | 10 |
| Communication timeline covers 90 minutes with template message | 10 |
| Escalation decision tree addresses all four decision points | 10 |
| Resolution criteria are specific and measurable (4+ criteria) | 5 |
| PIR agenda includes all required elements | 10 |
| **Total Part B** | **45** |

---

## Part C: Monitoring Gap Analysis (30 points)

### Part C Scenario

A review of the TradeExec P1 incident reveals the following timeline:

- **08:47 AM** — Monitoring tool records a warning event: TradeExec database connection
  pool utilization reaches 78% (threshold: 80%)
- **08:53 AM** — Monitoring tool records a second warning event: connection pool at 82%
  (now above threshold — should have triggered an exception alert)
- **09:10 AM** — No alert has been sent. No ticket has been created.
- **09:15 AM** — TradeExec becomes completely unresponsive
- **09:22 AM** — First user calls the service desk
- **10:22 AM** — After 60 minutes of user calls flooding the service desk, an L2 engineer
  is finally assigned and discovers the 08:53 warning event in the monitoring logs

### Part C Instructions

Answer each of the following analysis questions in 100–150 words each.

#### Analysis Question 1 (10 points)

Identify at least three specific failures in the Monitoring and Event Management process
based on the timeline above. For each failure, name the process step where it broke down
and explain the consequence of that failure.

#### Analysis Question 2 (10 points)

Design a corrected event-to-incident pipeline for this scenario. Starting from the 08:47
warning event, describe the steps that should have occurred to prevent or minimize the
outage. Use ITIL 4 event management terminology (warning, exception, alert, threshold,
automated response, incident creation) in your answer.

#### Analysis Question 3 (10 points)

Recommend two specific improvements to Meridian's monitoring configuration and two
improvements to their incident response process that would prevent a similar gap in the
future. Explain the expected impact of each recommendation.

### Part C Scoring Rubric

| Criterion | Points |
|---|---|
| Analysis Question 1 identifies 3+ failures with correct process step labels | 10 |
| Analysis Question 2 describes a correct corrected pipeline with proper ITIL terms | 10 |
| Analysis Question 3 provides 4 specific recommendations with expected impacts | 10 |
| **Total Part C** | **30** |

---

## Submission Checklist

Before submitting, verify:

- [ ] Part A table includes all 8 incidents with Impact, Urgency, Priority, and Justification
- [ ] Part B includes all five elements with required detail
- [ ] Part B communication template follows the required format
- [ ] Part C includes three analysis responses of 100–150 words each
- [ ] Document includes your name, student ID, and submission date
- [ ] File is saved as PDF or Word and uploaded to the LMS before the deadline

---

## Grading Summary

| Part | Points |
|---|---|
| Part A: Incident Priority Classification | 25 |
| Part B: Major Incident Process Design | 45 |
| Part C: Monitoring Gap Analysis | 30 |
| **Total** | **100** |

---

Module 08 Lab | CIS-4335 IT Service Management | Texas Wesleyan University
