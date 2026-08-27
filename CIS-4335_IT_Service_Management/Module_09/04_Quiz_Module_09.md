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

---

### Question 11 (5 points)

A problem record has been open for three weeks. The root cause has been identified — a buggy third-party library — but the vendor has not yet released a patch. The team has documented a workaround that temporarily mitigates the impact. What is the correct ITIL 4 status for this problem record?

- A) Closed — because a workaround exists
- B) Known error — root cause identified, workaround documented, permanent fix pending
- C) Incident — the service is still impaired
- D) Emergency change — the vendor must be compelled to release the patch immediately

#### Q11 Correct Answer: B — Known error

#### Q11 Distractor Analysis

- A is incorrect. A problem record is not closed when a workaround is found — it becomes a known error and remains open until the permanent fix is deployed and verified.
- C is incorrect. The situation has progressed beyond incident management into problem management. The problem record, not an incident record, is the correct tracking vehicle.
- D is incorrect. An emergency change is raised to implement a specific technical fix, not to compel a vendor. The problem state here is known error, and a change would be raised once a fix is available.

---

### Question 12 (5 points)

An IT organization uses the fishbone (Ishikawa) diagram during root cause analysis. In this technique, which of the following correctly describes the "spine" of the fishbone?

- A) The documented workaround that enables service to continue
- B) The effect or problem statement being investigated
- C) The list of all known errors in the KEDB
- D) The change request raised to fix the underlying cause

#### Q12 Correct Answer: B

#### Q12 Distractor Analysis

- A is incorrect. The workaround is an operational response, not part of the fishbone diagram structure.
- C is incorrect. The KEDB is a separate database, not a component of the fishbone diagram.
- D is incorrect. A change request is raised after root cause is identified; it is not part of the analysis tool itself.

---

### Question 13 (5 points)

A software development team uses continuous delivery and deploys small code changes to production multiple times per day. Which change enablement approach would ITIL 4 recommend for these deployments?

- A) Each deployment should be submitted as a normal change and reviewed by the full CAB.
- B) Each deployment should be classified as an emergency change due to the speed of delivery.
- C) Deployments should be designed as pre-authorized standard changes with automated testing gates, enabling fast delivery without full CAB review each time.
- D) Continuous delivery is incompatible with ITIL 4 change enablement and should be discontinued.

#### Q13 Correct Answer: C

#### Q13 Distractor Analysis

- A is incorrect. Requiring full CAB review for every continuous delivery deployment would create a bottleneck that makes the practice unworkable. ITIL 4 supports standard change pre-authorization for well-understood, repeatable processes.
- B is incorrect. Emergency changes are for urgent unplanned situations. Routine continuous delivery deployments are planned and repeatable — emergency classification is inappropriate.
- D is incorrect. ITIL 4 explicitly supports continuous delivery through flexible change enablement models. Continuous delivery is a recognized and compatible engineering practice.

---

### Question 14 (5 points)

During a normal change review, the CAB raises concerns about the proposed implementation window (Friday at 5 PM during month-end financial close). The change owner is asked to reschedule. Which function of the Change Schedule is being applied?

- A) Documenting completed changes for audit purposes
- B) Identifying conflicts between proposed changes and business-sensitive periods to prevent disruption
- C) Authorizing emergency changes during business-critical events
- D) Recording known errors associated with recent changes

#### Q14 Correct Answer: B

#### Q14 Distractor Analysis

- A is incorrect. Documenting completed changes is a historical record function, not the scheduling conflict identification function being applied here.
- C is incorrect. Emergency changes follow an accelerated path; the Change Schedule is used to coordinate timing, not to authorize emergency changes.
- D is incorrect. Known error recording is a Problem Management function using the KEDB, not the Change Schedule.

---

### Question 15 (5 points)

An organization's change enablement process requires that all changes — including adding a user to a distribution list — go through full CAB review, causing an average 12-day wait time. Which ITIL 4 Guiding Principle is most being violated?

- A) Focus on Value
- B) Think and Work Holistically
- C) Collaborate and Promote Visibility
- D) Keep It Simple and Practical

#### Q15 Correct Answer: D — Keep It Simple and Practical

#### Q15 Distractor Analysis

- A is incorrect. Focus on Value is about ensuring work contributes to stakeholder outcomes. While value is affected, the specific violation described — unnecessary complexity in the approval process — is best described by Keep It Simple and Practical.
- B is incorrect. Think and Work Holistically concerns considering system-wide impacts. The issue here is bureaucratic over-engineering, not a lack of holistic thinking.
- C is incorrect. Collaborate and Promote Visibility is about stakeholder involvement and transparency. The problem is not a lack of collaboration but an excessively complex process.

---

### Question 16 (5 points)

Which of the following scenarios should result in a problem record being raised proactively — before any incident has occurred?

- A) A service desk agent resolves a password reset call in under two minutes.
- B) A configuration audit reveals that 40% of servers are running end-of-life operating systems with known critical vulnerabilities.
- C) A monitoring tool generates an informational event confirming a successful nightly backup.
- D) A user reports that a web application is loading slowly but still functional.

#### Q16 Correct Answer: B

#### Q16 Distractor Analysis

- A is incorrect. A fast resolution of a routine service request does not indicate a systemic problem requiring investigation.
- C is incorrect. An informational event confirming successful operation requires no action and would not trigger a problem record.
- D is incorrect. A slow but functional application represents a degraded service that might generate an incident record, but a single user-reported performance observation alone does not trigger proactive problem investigation. The scenario of end-of-life OSes with known vulnerabilities is the clear proactive problem trigger.

---

### Question 17 (5 points)

An IT team discovers that a critical database configuration file was modified without a corresponding change record. When questioned, the engineer says they made a "quick fix" because it seemed low-risk. Two hours later, a related service goes down. Which ITIL 4 concept does this scenario illustrate?

- A) The value of proactive problem management
- B) The risk of unauthorized changes circumventing change enablement controls
- C) The need for a larger CAB to review all configuration changes
- D) The limitation of the Known Error Database in preventing outages

#### Q17 Correct Answer: B

#### Q17 Distractor Analysis

- A is incorrect. Proactive problem management identifies vulnerabilities before incidents occur. This scenario describes an unauthorized change that caused an incident — a change enablement failure.
- C is incorrect. The problem is not that the CAB is too small; the problem is that the change bypassed the change enablement process entirely.
- D is incorrect. The KEDB stores documented workarounds for known errors. It plays no role in preventing unauthorized changes.

---

### Question 18 (5 points)

A problem record is raised after three separate incidents affecting the same application in one month. The problem manager assigns the investigation to a senior engineer who performs a 5 Whys analysis. At which point in the problem lifecycle does the problem become a known error?

- A) When the problem record is first created
- B) When the first incident linked to the problem is resolved
- C) When the root cause is identified and a workaround is documented
- D) When the permanent fix is deployed and verified

#### Q18 Correct Answer: C

#### Q18 Distractor Analysis

- A is incorrect. When a problem record is created, the cause is still unknown — it is an open problem, not yet a known error.
- B is incorrect. Incident resolution does not change the problem's status. The problem record remains open and has not yet identified the cause.
- D is incorrect. When the permanent fix is deployed and verified, the known error is resolved and the problem record can be closed. The known error state precedes this final resolution step.

---

### Question 19 (5 points)

A change manager reviews a proposed emergency change to disable a firewall rule that is blocking critical payroll processing with the payroll run scheduled in four hours. The ECAB convenes and approves the change with conditions. Which condition would be most appropriate to include?

- A) Require that the permanent firewall rule fix be submitted as a standard change within 30 days
- B) Require that the firewall rule remain permanently disabled after the emergency is resolved
- C) Require that the change be re-submitted as a normal change before it is implemented
- D) Require the change owner to obtain unanimous CAB approval from all 15 board members

#### Q19 Correct Answer: A

#### Q19 Distractor Analysis

- A is correct because emergency changes are designed to be temporary resolutions — ITIL 4 best practice requires that emergency changes be followed up with a permanent solution through the normal change process.
- B is incorrect. Permanently disabling a firewall rule as a result of an emergency change would introduce a lasting security risk — emergency changes should be minimal and followed by a proper permanent fix.
- C is incorrect. Re-submitting as a normal change before implementation defeats the purpose of emergency change authorization; the urgency prevents a normal review cycle.
- D is incorrect. The ECAB is a small, fast-moving body specifically designed to avoid requiring full board consensus for urgent decisions.

---

### Question 20 (5 points)

Which of the following best describes the relationship between Problem Management and Change Enablement?

- A) They are the same practice and use the same records.
- B) Problem Management identifies root causes and designs fixes; Change Enablement provides the controlled process for implementing those fixes.
- C) Change Enablement manages the KEDB; Problem Management reviews the Change Schedule.
- D) Problem Management approves changes; Change Enablement investigates root causes.

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

- A is incorrect. Problem Management and Change Enablement are distinct ITIL 4 practices with different purposes, records, and roles.
- C is incorrect. The KEDB is maintained by Problem Management, not Change Enablement. The Change Schedule is maintained by Change Enablement.
- D is incorrect. The relationship is the reverse — Problem Management investigates root causes and designs fixes; Change Enablement provides the authorization process for implementing them. Problem Management does not approve changes.

---

Module 09 Quiz | CIS-4335 IT Service Management | Texas Wesleyan University
