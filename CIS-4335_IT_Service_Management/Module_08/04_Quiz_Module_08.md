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

---

### Question 11 (5 points)

An IT organization's service desk receives a ticket from a user who cannot access the company VPN. The agent verifies the user's credentials are correct, confirms the VPN service is operational, and discovers the user's device certificate has expired. The agent renews the certificate and the user connects successfully in under ten minutes.

Which ITIL 4 term best describes this ticket?

- A) Problem
- B) Change
- C) Event
- D) Incident

#### Q11 Correct Answer: D — Incident

#### Q11 Distractor Analysis

- A (Problem) is incorrect. A problem is the cause of one or more incidents under investigation. This is a single user-reported interruption that was resolved without root cause investigation.
- B (Change) is incorrect. A change involves adding, modifying, or removing a service component in a controlled manner. Renewing an expired certificate as part of incident resolution is a restoration action, not a planned change.
- C (Event) is incorrect. An event is a change of state detected by monitoring tools. This situation was reported by a user, not detected by monitoring, and it represents an unplanned service interruption.

---

### Question 12 (5 points)

A financial services firm's monitoring platform generates 4,200 alerts per day. Analysis shows that 3,100 of these alerts require no action because they are generated by routine system behavior that is within acceptable operating ranges. Which monitoring strategy would most directly reduce alert noise?

- A) Increase alert thresholds so that fewer alerts are generated for the same events
- B) Tune event thresholds and apply AIOps correlation to suppress repetitive, non-actionable alerts
- C) Disable monitoring on non-critical systems to reduce the volume
- D) Route all alerts directly to the service desk for manual triage

#### Q12 Correct Answer: B

#### Q12 Distractor Analysis

- A is incorrect. Blindly raising thresholds without tuning correlation risks missing genuine warning events before they become incidents. Threshold tuning must be paired with intelligent correlation.
- C is incorrect. Disabling monitoring on non-critical systems reduces visibility and increases the risk of undetected failures. The goal is to reduce noise while preserving coverage.
- D is incorrect. Routing all alerts to the service desk for manual triage is the opposite of efficient event management — it overwhelms human capacity and defeats the purpose of monitoring automation.

---

### Question 13 (5 points)

After resolving a P1 incident affecting the company's e-commerce platform for 3 hours on a Friday evening, the incident manager schedules a Post-Incident Review for the following Tuesday. Which of the following is NOT a primary output of the PIR?

- A) A timeline documenting the sequence of events from first detection to resolution
- B) An updated price list for the services affected during the outage
- C) A list of contributing factors that made the incident worse or harder to resolve
- D) Action items with owners and due dates to prevent recurrence

#### Q13 Correct Answer: B

#### Q13 Distractor Analysis

- A is incorrect — this is a legitimate PIR output. A timeline of the incident sequence is a standard PIR deliverable that supports root cause analysis and future training.
- C is incorrect — this is a legitimate PIR output. Identifying contributing factors is a core PIR objective.
- D is incorrect — this is a legitimate PIR output. Action items with owners and due dates are the primary mechanism for translating PIR findings into improvements.
- B is correct as the answer because an updated price list has no relationship to incident management or post-incident review. PIRs focus on technical and process improvement, not commercial pricing.

---

### Question 14 (5 points)

According to ITIL 4 Incident Management, what is the difference between functional escalation and hierarchical escalation?

- A) Functional escalation increases the incident's priority; hierarchical escalation increases the response team size.
- B) Functional escalation transfers the incident to a more technically capable team; hierarchical escalation involves notifying management for authority or visibility.
- C) Functional escalation is used only for P1 incidents; hierarchical escalation is used for P2 and below.
- D) Functional escalation requires Change Advisory Board approval; hierarchical escalation does not.

#### Q14 Correct Answer: B

#### Q14 Distractor Analysis

- A is incorrect. Priority changes are a separate action from escalation type. Functional escalation routes to specialist capability, not higher priority; hierarchical escalation adds management visibility, not team size.
- C is incorrect. Both types of escalation can be applied to any priority level depending on the specific situation.
- D is incorrect. Change Advisory Board approval relates to Change Enablement, not to incident escalation types.

---

### Question 15 (5 points)

A service desk team tracks the following metrics monthly: first-contact resolution rate, average handle time, customer satisfaction score, and SLA compliance percentage. Which of these metrics most directly indicates whether the shift-left strategy is succeeding?

- A) Average handle time
- B) SLA compliance percentage
- C) Customer satisfaction score
- D) First-contact resolution rate

#### Q15 Correct Answer: D — First-contact resolution rate

#### Q15 Distractor Analysis

- A is incorrect. Average handle time measures efficiency per call but does not indicate whether issues are being resolved at the earliest support tier rather than escalated.
- B is incorrect. SLA compliance measures whether resolution targets are met within agreed timeframes but does not specifically reflect the shift-left strategy's goal of resolving more issues at Level 0 or Level 1.
- C is incorrect. Customer satisfaction measures user experience quality but does not specifically measure whether resolution is happening at the earliest possible point.

---

### Question 16 (5 points)

An IT organization's incident management process has an SLA requiring P2 incidents to be resolved within 4 hours. A P2 incident is opened at 9:00 AM. At 12:30 PM, the resolution has not been found and the SLA will breach in 30 minutes. What ITIL 4 concept applies to this situation?

- A) Event management threshold
- B) SLA breach — triggers automatic ticket closure
- C) SLA jeopardy — should trigger a management notification and possible priority re-evaluation
- D) Known error — the incident should be transferred to the Known Error Database

#### Q16 Correct Answer: C

#### Q16 Distractor Analysis

- A is incorrect. An event management threshold applies to monitoring alerts, not to incident SLA timers.
- B is incorrect. SLA breach does not trigger automatic ticket closure. A breach triggers escalation, notification, and management review — not closure of the unresolved incident.
- D is incorrect. A Known Error record is created when Problem Management identifies a root cause and workaround for a recurring issue. A single unresolved incident approaching SLA breach does not constitute a known error.

---

### Question 17 (5 points)

Which statement best describes the relationship between Incident Management and Problem Management in ITIL 4?

- A) They are the same practice — ITIL 4 merged them to reduce complexity.
- B) Incident Management resolves service interruptions; Problem Management investigates root causes of incidents to prevent recurrence. They operate concurrently and share data.
- C) Problem Management must be completed before Incident Management can begin.
- D) Incident Management produces changes; Problem Management produces incidents.

#### Q17 Correct Answer: B

#### Q17 Distractor Analysis

- A is incorrect. ITIL 4 defines Incident Management and Problem Management as separate practices with different purposes, inputs, and outputs.
- C is incorrect. Incident Management begins immediately when an interruption is detected, regardless of whether Problem Management has investigated the underlying cause. They operate in parallel.
- D is incorrect. Incident Management restores service; it may trigger a change to implement a permanent fix, but it does not "produce" changes as its primary output. Problem Management investigates root causes and may produce known errors or change requests — not incidents.

---

### Question 18 (5 points)

A university service desk uses a tiered support model. Tier 0 is a self-service portal. Tier 1 is the service desk. Tier 2 is desktop support. Tier 3 is infrastructure engineering. A student submits a password reset via the self-service portal successfully. Which tier handled the interaction?

- A) Tier 1
- B) Tier 2
- C) Tier 3
- D) Tier 0

#### Q18 Correct Answer: D — Tier 0

#### Q18 Distractor Analysis

- A is incorrect. Tier 1 is the human service desk. The student resolved the issue without contacting a service desk agent.
- B is incorrect. Tier 2 is desktop support, which handles issues requiring physical or remote technical intervention beyond the service desk's capability.
- C is incorrect. Tier 3 is infrastructure engineering, which handles deep technical and platform-level work. A self-service password reset does not involve this tier.

---

### Question 19 (5 points)

An event management tool is configured to automatically create a P3 incident ticket when a server's memory utilization exceeds 90% for more than five consecutive minutes. This configuration is an example of which event management concept?

- A) AIOps noise suppression
- B) Informational event logging
- C) Automated event-to-incident escalation based on an exception threshold
- D) Warning event correlation

#### Q19 Correct Answer: C

#### Q19 Distractor Analysis

- A is incorrect. AIOps noise suppression reduces alert volume by correlating and filtering events. This configuration is creating incidents from specific threshold breaches, not suppressing noise.
- B is incorrect. Informational events are logged for reference during normal operations and require no action. A 90% memory threshold breach requires a response and triggers an incident.
- D is incorrect. The scenario describes a clear exception threshold breach (above 90%) that triggers incident creation, not a warning event approaching a threshold.

---

### Question 20 (5 points)

A service desk manager reviews monthly data and finds that 38% of incidents are resolved at Tier 1, 41% require escalation to Tier 2, and 21% require escalation to Tier 3. The manager's goal is to increase the Tier 1 resolution rate to 60% within six months. Which combination of improvements would most directly achieve this goal?

- A) Hire more Tier 2 engineers and expand the Tier 3 team's capacity
- B) Expand the service desk's knowledge base, provide additional training to Tier 1 agents, and implement guided diagnostic scripts for common incident types
- C) Implement stricter SLA targets for Tier 2 and Tier 3 escalation resolution times
- D) Reduce the number of incident categories so fewer tickets require specialist routing

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

- A is incorrect. Expanding Tier 2 and Tier 3 capacity addresses escalated volume but does not help Tier 1 agents resolve more issues themselves.
- C is incorrect. Tightening SLA targets for Tier 2 and Tier 3 may improve their responsiveness but does not directly increase Tier 1's capability to resolve incidents without escalation.
- D is incorrect. Reducing category count simplifies routing but does not equip Tier 1 agents with the knowledge and tools to resolve a broader range of incidents.

---

Module 08 Quiz | CIS-4335 IT Service Management | Texas Wesleyan University
