# Quiz: Module 09 — Problem and Change Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

## Total Questions: 10 | Points: 10 (1 pt each)

## Certification Alignment: ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Questions are scenario-based and aligned
to the ITIL 4 Foundation exam style. Each question is followed by the correct answer and
a distractor analysis explaining why the other options are incorrect.

---

### Question 1

An IT team has experienced the same application error four times in three weeks. Each
time the application crashes, they restart it and service is restored. They have not
investigated why the crashes occur.

According to ITIL 4, what should the team do now?

- A) Increase the priority of the incident each time it recurs
- B) Raise a problem record and conduct a root cause analysis
- C) Declare a major incident and activate the war room
- D) Submit an emergency change request to patch the application

#### Q1 Correct Answer: B

#### Q1 Distractor Analysis

- A is incorrect. Changing incident priority addresses response urgency, not the
  underlying cause. The correct response to a recurring incident pattern is Problem
  Management.
- C is incorrect. Major incident declaration is triggered by current high-severity
  business impact, not by recurrence history. The appropriate response here is raising
  a problem record.
- D is incorrect. An emergency change cannot be raised without first identifying what
  needs to change. Problem Management must first identify the root cause before a fix
  can be designed and a change raised.

---

### Question 2

A problem has been analyzed. The root cause has been identified — a misconfigured load
balancer — and a temporary workaround has been documented that allows services to
continue with reduced performance. A permanent fix has been designed but not yet
deployed.

According to ITIL 4, what is the correct term for the current state of this problem?

- A) Open incident
- B) Known error
- C) Resolved problem
- D) Emergency change

#### Q2 Correct Answer: B — Known Error

#### Q2 Distractor Analysis

- A (Open incident) is incorrect. An incident is an unplanned service interruption. This
  situation involves a documented root cause and workaround — it has progressed beyond
  incident status into Problem Management.
- C (Resolved problem) is incorrect. A problem is only resolved when the permanent fix
  has been deployed and verified. With the fix pending, the problem remains open as a
  known error.
- D (Emergency change) is incorrect. An emergency change is a type of change request, not
  a problem state. The problem becomes a known error; a change record is what gets raised
  to deploy the fix.

---

### Question 3

Which of the following BEST distinguishes proactive problem management from reactive
problem management?

- A) Proactive problem management is performed by senior staff; reactive is performed by
  the service desk
- B) Reactive problem management is triggered by incidents; proactive problem management
  identifies potential causes before incidents occur
- C) Proactive problem management involves the CAB; reactive problem management does not
- D) Reactive problem management uses the 5 Whys; proactive uses the fishbone diagram

#### Q3 Correct Answer: B

#### Q3 Distractor Analysis

- A is incorrect. ITIL 4 does not distinguish problem management types by staff level.
  Both types can involve any appropriate technical staff.
- C is incorrect. The CAB is a Change Enablement body, not a Problem Management one.
  Neither type of problem management inherently involves the CAB.
- D is incorrect. Both RCA techniques can be used for either type of problem management.
  The choice of technique depends on the problem's complexity, not whether it is reactive
  or proactive.

---

### Question 4

During a 5 Whys analysis, an IT team asks: "Why did the server run out of disk space?"
and answers "Because log files were never purged." They then ask why log files were never
purged and discover the automated cleanup job was disabled during a maintenance window
six months ago and was never re-enabled.

Which ITIL 4 practice's absence contributed most directly to this root cause?

- A) Incident Management
- B) Service Level Management
- C) Change Enablement
- D) Service Desk

#### Q4 Correct Answer: C — Change Enablement

#### Q4 Distractor Analysis

- A (Incident Management) is incorrect. Incident Management would have responded to the
  disk-full symptom, not prevented the root cause. The root cause is a configuration
  change made during maintenance that was never properly tracked or reversed.
- B (Service Level Management) is incorrect. SLM governs service quality agreements and
  reviews, not the operational execution of maintenance tasks and configuration tracking.
- D (Service Desk) is incorrect. The service desk handles user contacts and incident
  logging. The root cause here is an untracked configuration modification — a Change
  Enablement gap.

---

### Question 5

A financial services firm needs to apply a critical security patch to their trading
platform. A zero-day vulnerability has been publicly disclosed and is being actively
exploited. The patch has not been tested internally, and the trading platform is live
with active users.

Which change type BEST applies to this situation?

- A) Standard change
- B) Normal change
- C) Emergency change
- D) Authorized change

#### Q5 Correct Answer: C — Emergency Change

#### Q5 Distractor Analysis

- A (Standard change) is incorrect. Standard changes are pre-authorized, low-risk, and
  follow documented repeatable procedures. An untested patch during an active exploit
  does not qualify as standard.
- B (Normal change) is incorrect. Normal changes require full CAB review and scheduling.
  The urgency of an active exploit does not allow the time required for normal change
  process.
- D (Authorized change) is incorrect. "Authorized change" is not a recognized ITIL 4
  change type. The three types are standard, normal, and emergency.

---

### Question 6

Which of the following is the PRIMARY purpose of the Known Error Database (KEDB)?

- A) To store all closed problem records for historical reference
- B) To track the status of all in-progress change requests
- C) To provide documented workarounds that enable faster incident resolution while
  permanent fixes are pending
- D) To record all incidents by category and resolution time

#### Q6 Correct Answer: C

#### Q6 Distractor Analysis

- A is incorrect. The KEDB stores known errors — problems with identified root causes and
  documented workarounds — not all closed problem records. Closed problems where the fix
  has been deployed are removed or archived from the active KEDB.
- B is incorrect. Change request tracking is a Change Enablement function, not the
  purpose of the KEDB.
- D is incorrect. Incident records are maintained in the IT service management tool's
  incident module, not in the KEDB.

---

### Question 7

A systems administrator wants to add a new DNS record following a standard procedure
that has been used dozens of times without incident. The procedure is fully documented,
tested, and has pre-authorization from the Change Manager.

Which change type and process applies?

- A) Normal change — must be submitted to the CAB for review
- B) Emergency change — DNS changes always require urgent handling
- C) Standard change — pre-authorized, low-risk, follows documented procedure
- D) Standard change — but a rollback plan must first be approved by the CAB

#### Q7 Correct Answer: C

#### Q7 Distractor Analysis

- A is incorrect. Standard changes do not require CAB review — they are pre-authorized
  precisely because they are well understood, low-risk, and repeatable.
- B is incorrect. The emergency change type is for urgent, unplanned situations. A
  routine DNS record addition following a known procedure is not an emergency.
- D is incorrect. Standard changes do not require CAB approval of rollback plans.
  The pre-authorization covers the procedure including its rollback steps.

---

### Question 8

Which of the following BEST describes the purpose of the Change Schedule?

- A) A list of all incidents and their resolution times for the current month
- B) An authorized timeline of all approved changes, used to prevent conflicts and
  support business planning
- C) A prioritized backlog of change requests awaiting CAB review
- D) A project plan for major IT initiatives approved by the executive steering committee

#### Q8 Correct Answer: B

#### Q8 Distractor Analysis

- A is incorrect. The Change Schedule tracks approved changes, not incident records.
  Incident records are managed in the incident management module.
- C is incorrect. Change requests awaiting CAB review are in the change pipeline or
  change queue, not the Change Schedule. The Change Schedule contains only authorized,
  approved changes.
- D is incorrect. The Change Schedule is an operational tool for managing IT changes, not
  a strategic project plan. Major projects may have entries in the Change Schedule but
  the schedule itself is not a project management artifact.

---

### Question 9

After a major incident is resolved, the post-incident review identifies three systemic
factors that contributed to the outage. Which practice takes primary responsibility for
investigating these factors and preventing recurrence?

- A) Incident Management
- B) Change Enablement
- C) Problem Management
- D) Monitoring and Event Management

#### Q9 Correct Answer: C — Problem Management

#### Q9 Distractor Analysis

- A (Incident Management) is incorrect. Incident Management's goal is restoration.
  After restoration, the baton passes to Problem Management for root cause investigation.
- B (Change Enablement) is incorrect. Change Enablement may be involved later to
  implement the fix, but it does not perform root cause analysis.
- D (Monitoring and Event Management) is incorrect. Monitoring detects and categorizes
  events. It feeds information into incident and problem management but does not itself
  conduct root cause analysis or manage the problem lifecycle.

---

### Question 10

An organization's IT team is conducting a quarterly architecture review. They identify
that their primary database server has no redundancy — if it fails, the entire ERP system
goes down. No incident has occurred yet.

Which type of problem management activity is this?

- A) Reactive problem management — triggered by an existing incident
- B) Proactive problem management — identifying a potential cause of future incidents
- C) Change Enablement — assessing risk of a proposed modification
- D) Service Level Management — reviewing compliance with SLA targets

#### Q10 Correct Answer: B — Proactive Problem Management

#### Q10 Distractor Analysis

- A (Reactive problem management) is incorrect. Reactive problem management is triggered
  by existing incidents. No incident has occurred here — the team is identifying a
  vulnerability before it causes a problem.
- C (Change Enablement) is incorrect. No change is being proposed or assessed. The team
  is identifying a risk through an architecture review — a proactive Problem Management
  activity.
- D (Service Level Management) is incorrect. SLM focuses on agreed service targets and
  their measurement. Identifying a redundancy gap is a technical risk identification
  activity within Problem Management.

---

Module 09 Quiz | CIS-4335 IT Service Management | Texas Wesleyan University
