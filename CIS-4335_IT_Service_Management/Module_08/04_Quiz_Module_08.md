# Quiz: Module 08 — Service Desk, Incident Management, and Monitoring

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

A user contacts IT because they cannot log in to the payroll application. Their account
credentials are correct but the application is returning an authentication error. This is
the only reported case.

Which ITIL 4 term BEST describes this situation?

- A) Problem
- B) Event
- C) Incident
- D) Change

#### Q1 Correct Answer: C — Incident

#### Q1 Distractor Analysis

- A (Problem) is incorrect. A problem is the cause of one or more incidents. At this
  stage there is only one reported case and no investigation into root cause has begun.
- B (Event) is incorrect. An event is a change of state detected by monitoring tools.
  The user's experience is an unplanned service interruption — an incident.
- D (Change) is incorrect. A change involves adding, modifying, or removing something.
  This is an unplanned interruption, not a planned modification.

---

### Question 2

A monitoring system detects that a web server's CPU utilization has reached 91%, exceeding
the 85% configured threshold. No user-facing impact has been reported yet, but application
response times are beginning to degrade slightly.

Which event category BEST describes this alert?

- A) Informational
- B) Warning
- C) Exception
- D) Critical

#### Q2 Correct Answer: C — Exception

#### Q2 Distractor Analysis

- A (Informational) is incorrect. Informational events represent normal operation with no
  threshold breached. The 85% threshold has been exceeded here.
- B (Warning) is incorrect. A warning event approaches a threshold but has not yet
  breached it. The threshold has already been exceeded — this is an exception.
- D (Critical) is incorrect. "Critical" is not an ITIL 4 event category. The three
  categories are informational, warning, and exception.

---

### Question 3

The primary purpose of Incident Management is best described as which of the following?

- A) To identify the root cause of service failures and prevent recurrence
- B) To restore normal service operation as quickly as possible and minimize negative impact
- C) To authorize and implement changes that fix service defects
- D) To maintain a database of known errors and approved workarounds

#### Q3 Correct Answer: B

#### Q3 Distractor Analysis

- A is incorrect. Identifying root cause and preventing recurrence is the purpose of
  Problem Management, not Incident Management.
- C is incorrect. Authorizing and implementing fixes is the purpose of Change Enablement.
  Incident Management focuses on restoration, not controlled modification.
- D is incorrect. Maintaining a known error database is an output of Problem Management.
  Incident Management may reference it but does not maintain it.

---

### Question 4

During a P1 major incident, a designated team member is responsible for drafting and
sending stakeholder status updates every 30 minutes, managing the outage communication
page, and coordinating messaging to executive leadership.

Which war room role does this person hold?

- A) Incident Commander
- B) Technical Lead
- C) Scribe / Recorder
- D) Communications Lead

#### Q4 Correct Answer: D — Communications Lead

#### Q4 Distractor Analysis

- A (Incident Commander) is incorrect. The Incident Commander holds overall ownership
  and decision authority but delegates communications to the Communications Lead.
- B (Technical Lead) is incorrect. The Technical Lead directs the technical investigation
  and coordinates resolver teams, not external stakeholder communication.
- C (Scribe / Recorder) is incorrect. The Scribe documents internal actions and decisions
  in real time. External communication is the Communications Lead's responsibility.

---

### Question 5

A service desk has implemented a self-service portal where users can reset their own
passwords, check ticket status, and access a knowledge base. Password reset calls to the
service desk have dropped by 45% since the portal launched.

Which service desk concept does this BEST illustrate?

- A) Hierarchical escalation
- B) Functional escalation
- C) Shift-left strategy
- D) Post-incident review

#### Q5 Correct Answer: C — Shift-Left Strategy

#### Q5 Distractor Analysis

- A (Hierarchical escalation) is incorrect. Hierarchical escalation routes issues to
  management for authority or visibility — not related to self-service adoption.
- B (Functional escalation) is incorrect. Functional escalation transfers tickets to
  more capable teams. Moving resolution to the user is the opposite direction.
- D (Post-incident review) is incorrect. A PIR is a structured lessons-learned session
  after a major incident, unrelated to self-service portal implementation.

---

### Question 6

A monitoring tool detects normal backup job completion at 2:00 AM. No threshold has been
breached. No action is required. The event is logged automatically.

Which event category does this represent?

- A) Exception
- B) Warning
- C) Informational
- D) Alert

#### Q6 Correct Answer: C — Informational

#### Q6 Distractor Analysis

- A (Exception) is incorrect. Exception events indicate a threshold breach or failure
  requiring action. Normal backup completion is successful, expected operation.
- B (Warning) is incorrect. Warning events indicate approach toward a threshold. A
  successful backup job is not approaching any threshold.
- D (Alert) is incorrect. An alert is a notification triggered by an exception event,
  not itself an event category. The three categories are informational, warning, exception.

---

### Question 7

An IT organization has experienced the same P2 incident three times in six weeks, each
time caused by a memory leak in a core middleware component. The team restores service
each time but has not addressed the underlying cause.

What should happen next according to ITIL 4 best practice?

- A) The service desk should assign a higher priority to future occurrences
- B) The team should raise a problem record to investigate and address the root cause
- C) The Incident Commander should declare a major incident for the next occurrence
- D) The Change Advisory Board should immediately approve an emergency change

#### Q7 Correct Answer: B

#### Q7 Distractor Analysis

- A is incorrect. Changing priority does not address the underlying cause. Priority
  governs response urgency, not root cause investigation.
- C is incorrect. Declaring a major incident is triggered by severity and current business
  impact, not recurrence history alone. Problem Management is the correct response.
- D is incorrect. An emergency change might be needed once a fix is identified, but the
  first step is Problem Management to identify and validate the root cause.

---

### Question 8

Which of the following BEST describes the service desk's role as the single point of contact?

- A) The service desk resolves all incidents without escalation to other teams
- B) The service desk is the one consistent entry point for all user IT interactions,
  regardless of issue type or resolution path
- C) The service desk is the only team authorized to create incident tickets
- D) The service desk manages all IT projects and change requests on behalf of users

#### Q8 Correct Answer: B

#### Q8 Distractor Analysis

- A is incorrect. The service desk does not resolve all incidents — many require
  escalation to L2 and L3 teams. The SPOC concept is about the entry point, not
  resolution ownership.
- C is incorrect. Monitoring tools, automated systems, and other teams can all create
  incident tickets. The service desk is the human SPOC, not the exclusive ticket creator.
- D is incorrect. The service desk handles incident and service request intake. Change
  requests and project management are separate functions.

---

### Question 9

An incident is classified with High Impact and Low Urgency. According to ITIL 4 priority
principles, which statement is most accurate?

- A) This incident must be treated as P1 because impact is high
- B) This incident will receive a moderate priority because urgency moderates the impact
- C) Impact and urgency cannot conflict — all high-impact incidents are automatically high urgency
- D) Low urgency automatically makes this a P5 informational incident

#### Q9 Correct Answer: B

#### Q9 Distractor Analysis

- A is incorrect. Priority is a function of both impact AND urgency. High impact alone
  does not automatically produce P1 — low urgency moderates the final priority.
- C is incorrect. Impact and urgency are independent dimensions. A service affecting
  many users (high impact) may still have a workaround making resolution timing less
  critical (low urgency).
- D is incorrect. Low urgency does not default to P5. P5 is for informational situations
  with no current impact. This incident has high impact and cannot be P5.

---

### Question 10

A server monitoring tool detects that disk utilization has reached 79% against a defined
threshold of 80%. No service impact has occurred. The operations team receives a
notification to investigate proactively.

Which event category and appropriate response BEST match this scenario?

- A) Informational — log the event and take no action
- B) Warning — investigate proactively before the threshold is breached
- C) Exception — create a P1 incident immediately
- D) Exception — activate the war room and notify all stakeholders

#### Q10 Correct Answer: B — Warning

#### Q10 Distractor Analysis

- A (Informational) is incorrect. Informational events represent normal operations.
  At 79% — one point below threshold — this requires proactive attention, not just logging.
- C is incorrect. An exception event triggers incident creation when a threshold is
  breached. At 79%, the threshold has not been breached; this is a warning. P1 would
  be a grossly disproportionate response.
- D is incorrect. War room activation is reserved for declared P1 major incidents. A
  near-threshold disk warning does not meet that criterion.

---

Module 08 Quiz | CIS-4335 IT Service Management | Texas Wesleyan University
