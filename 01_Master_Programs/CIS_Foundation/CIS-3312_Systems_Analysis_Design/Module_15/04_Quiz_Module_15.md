# Quiz: Module 15 — Implementation, Change Management, and Transition

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Quiz Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided after each question to support your learning.

**Time limit:** 30 minutes

---

## Question 1

A hospital is replacing its legacy billing system with a new platform. The hospital processes thousands of insurance claims daily and cannot afford incorrect billing even during transition. The IT director recommends running both systems simultaneously for sixty days, comparing output from each to verify the new system produces correct results. This deployment strategy is best described as which of the following?

A. Phased rollout, because two departments are using different systems during the transition
B. Pilot deployment, because a limited group of users is testing the new system before full rollout
C. Parallel operation, because both systems run simultaneously with output comparison for verification
D. Big bang deployment, because a specific sixty-day cutover date has been defined

### Distractor Analysis — Question 1

**Correct answer: C**

Running both systems simultaneously and comparing outputs to verify correctness is the defining characteristic of parallel operation. It is specifically used when data accuracy is too critical to rely on testing alone.

**Why A is wrong:** Phased rollout deploys to different groups at different times — it does not involve running two systems doing the same work with output comparison.

**Why B is wrong:** Pilot deployment tests with a limited user subset before full rollout. The scenario describes all users working in both systems, not a limited subset.

**Why D is wrong:** Big bang deployment switches all users at once to the new system, retiring the old one on the cutover date. The scenario explicitly keeps both systems running — the opposite of big bang.

---

## Question 2

A BA discovers that front-line customer service representatives at a utility company do not understand why the company is replacing its customer account management system. The reps know the project is happening but cannot explain what problem the new system solves or why the old system is being retired. According to the ADKAR model, which stage is this group currently blocked at?

A. Desire — they are unwilling to support the change
B. Knowledge — they have not received training on the new system
C. Awareness — they do not understand the reason for the change
D. Reinforcement — they have reverted to old behaviors after initial training

### Distractor Analysis — Question 2

**Correct answer: C**

Awareness is the ADKAR stage where individuals understand why the change is necessary. The description says they know the project is happening but cannot explain what problem it solves. That is an Awareness gap — they lack the why, not the how.

**Why A is wrong:** Desire requires Awareness first. The reps have not expressed opposition — they simply lack understanding of the rationale. This is pre-Desire; the issue is at Awareness.

**Why B is wrong:** Knowledge is about how to use the new system. The reps' inability to explain the business reason for the change is an Awareness issue, not a training issue.

**Why D is wrong:** Reinforcement applies after adoption has occurred and the change is at risk of reverting. This group has not yet adopted anything — the system has not launched.

---

## Question 3

A training coordinator schedules all ERP system training eight weeks before the go-live date to ensure users have maximum preparation time. On go-live day, help desk call volume is unexpectedly high and many users report being unable to perform basic tasks. What is the most likely root cause of this outcome?

A. The training content was inaccurate and did not reflect the final system configuration.
B. Training was delivered too early, and the knowledge was not retained by go-live day.
C. The help desk staffing plan was inadequate and unrelated to training effectiveness.
D. Users did not complete the required training and were unprepared at go-live.

### Distractor Analysis — Question 3

**Correct answer: B**

Training delivered eight weeks before go-live is too early. Research on learning retention consistently shows that knowledge decays significantly over weeks without reinforcement or practice. The standard recommendation is to complete core training within two weeks of go-live.

**Why A is wrong:** While training accuracy is always a concern, the scenario does not indicate a system configuration change occurred. The timing issue is the most likely root cause given the information provided.

**Why C is wrong:** High help desk volume is a symptom, not a root cause. The question asks for the root cause of the outcome, which is the training timing problem.

**Why D is wrong:** The scenario says the training coordinator scheduled the training, implying it was conducted. There is no indication users skipped training. Non-retention due to timing is a more direct explanation.

---

## Question 4

A large retail chain is rolling out a new point-of-sale system to 1,200 store locations nationwide. The implementation team deploys the system to fifteen stores in one region first, observes results for four weeks, and then uses the lessons learned to improve the training program before deploying to the remaining 1,185 locations. This approach is best described as which of the following?

A. Parallel operation followed by big bang cutover
B. Phased rollout beginning with a pilot group
C. Big bang deployment with a four-week stabilization period
D. Throwaway prototyping applied to an operational deployment

### Distractor Analysis — Question 4

**Correct answer: B**

The initial fifteen-store deployment is a pilot — a limited, representative deployment designed to validate the approach and generate lessons learned. Using those lessons to improve the subsequent full rollout makes the overall strategy a phased rollout starting with a pilot.

**Why A is wrong:** Parallel operation involves running two systems simultaneously with output comparison. The scenario involves deploying to a subset of locations, not running two systems in the same locations at once.

**Why C is wrong:** A big bang deployment deploys to all users simultaneously. Deploying to fifteen stores first is explicitly not big bang.

**Why D is wrong:** Throwaway prototyping is a software development technique, not a deployment strategy. Deploying a real, production system to live stores is not prototyping.

---

## Question 5

After a new HR system goes live, the BA discovers that payroll administrators are still printing reports and manually re-entering data into a spreadsheet — the same process they used before the new system launched. According to the ADKAR model, what is the most appropriate diagnosis?

A. Knowledge gap — the payroll administrators were not trained on the new reporting feature
B. Awareness gap — the payroll administrators do not know the new system has a reporting feature
C. Reinforcement failure — the change was not sustained and reversion to old behaviors has occurred
D. Desire gap — the payroll administrators do not want to use the new system's reporting feature

### Distractor Analysis — Question 5

**Correct answer: C**

Reversion to old behaviors after initial adoption is a Reinforcement failure. The payroll administrators presumably went through go-live and were using the system, but without reinforcement mechanisms they have drifted back to familiar patterns.

**Why A is wrong:** A Knowledge gap would mean administrators never knew how to use the reporting feature. The scenario implies they went through go-live, suggesting they had some knowledge. The reversion pattern points to Reinforcement.

**Why B is wrong:** Awareness gap occurs when individuals do not understand why the change is happening. The administrators clearly know about the new system — they are just not using one of its features.

**Why D is wrong:** Desire gap occurs when individuals understand the change but actively oppose it. Active resistance is different from passive reversion to comfortable old habits.

---

## Question 6

A transition plan for a new claims processing system specifies that all technical documentation, configuration records, and source code will be stored in a shared drive accessible to the operations team. The transition plan also defines the help desk procedures, SLAs, and vendor contacts. What critical transition element is missing from this description?

A. Deployment strategy selection
B. A formal knowledge transfer process from the project team to the operations team
C. User acceptance testing sign-off documentation
D. The requirements traceability matrix

### Distractor Analysis — Question 6

**Correct answer: B**

Storing documentation is necessary but not sufficient. A formal knowledge transfer process ensures that operations team members actually understand and can act on the documentation — through structured briefings, shadow periods, walkthroughs, or handover meetings. Documents alone do not transfer expertise.

**Why A is wrong:** Deployment strategy is determined before go-live, not documented in the post-go-live transition plan.

**Why C is wrong:** UAT sign-off is a testing artifact, not a transition plan element. It precedes the transition phase.

**Why D is wrong:** The RTM is a requirements and testing artifact. While it should be preserved, its absence from the transition plan description is not the most critical gap compared to the knowledge transfer process.

---

## Question 7

A post-implementation review conducted thirty days after go-live finds that the average loan processing time has decreased from 18 minutes to 14 minutes — an improvement of 22%. The business case projected a 40% reduction to 11 minutes. What is the most appropriate BA action based on this finding?

A. Accept the result as a success since processing time did decrease.
B. Document the shortfall, identify contributing factors, and recommend specific corrective actions.
C. Reopen the project and conduct additional testing to find the root cause.
D. Recommend that the system be rolled back since it did not achieve its projected outcomes.

### Distractor Analysis — Question 7

**Correct answer: B**

A PIR is a forward-looking activity. When actual outcomes fall short of projections, the BA documents the gap, investigates contributing factors (inadequate training, process issues, system configuration), and recommends specific corrective actions. This is the professional standard for PIR findings.

**Why A is wrong:** Accepting a 22% improvement when 40% was projected without investigation ignores a significant business value gap. The PIR exists precisely to identify and address such gaps.

**Why C is wrong:** Reopening the project for additional testing is not the correct response to an operational performance finding. The PIR investigates operational factors, not technical defects.

**Why D is wrong:** Rolling back a system that shows improvement — even below target — is disproportionate. The appropriate response is investigation and corrective action, not abandonment.

---

## Question 8

During ADKAR analysis, a BA finds that a group of warehouse managers has both Awareness and Desire for a new inventory system but continues to make frequent errors when using it two weeks after go-live. The managers say they understand the system conceptually but struggle with the actual screens under time pressure. Which ADKAR stage should the BA target with an intervention?

A. Awareness — additional communication about the business case is needed
B. Knowledge — more classroom training will resolve the problem
C. Ability — supervised practice under realistic conditions will bridge the gap
D. Reinforcement — recognition for correct system use will sustain the change

### Distractor Analysis — Question 8

**Correct answer: C**

The managers have Awareness and Desire. They say they understand conceptually — suggesting Knowledge exists — but they struggle under real conditions. The gap between knowing how (Knowledge) and performing correctly under pressure (Ability) is the Ability stage. The intervention is supervised real-conditions practice.

**Why A is wrong:** The managers already have Awareness. Additional business-case communication would not address the real-world performance gap.

**Why B is wrong:** Classroom training addresses Knowledge. The scenario explicitly states the managers understand conceptually — the issue is performance under real conditions, not conceptual understanding.

**Why D is wrong:** Reinforcement applies when the change was adopted and then reverted. Two weeks post-go-live with frequent errors is an Ability issue, not a reversion issue.

---

## Question 9

A BA is creating a training plan for a financial services firm implementing a new trading platform. The compliance team needs to use six advanced functions that front-line traders will never touch. Which training plan principle does this scenario most directly call for?

A. Parallel operation, to allow compliance staff to verify results against the legacy platform
B. Audience segmentation, to ensure compliance staff receive a specialized training track distinct from the trader track
C. Competency verification, to confirm that all staff can perform all system functions before go-live
D. Phased deployment, to allow compliance staff to go live after traders have stabilized

### Distractor Analysis — Question 9

**Correct answer: B**

Different user groups with different functional needs require different training tracks — this is audience segmentation. Sending compliance staff to the same training as traders, or vice versa, wastes time and leaves role-specific needs unmet.

**Why A is wrong:** Parallel operation is a deployment strategy, not a training plan principle. It is unrelated to the different training needs of compliance staff vs. traders.

**Why C is wrong:** Competency verification confirms that training worked — it is a training plan component. But requiring all staff to be verified on all functions, including ones they will never use, is inefficient and defeats the purpose of segmentation.

**Why D is wrong:** Phased deployment is a go-live strategy, not a training design principle. Whether compliance staff go live before or after traders is separate from whether they receive appropriate training.

---

## Question 10

According to the BABOK Guide, the BA knowledge area most closely associated with post-implementation review and assessing whether a deployed solution delivers intended business value is which of the following?

A. Requirements Life Cycle Management
B. Strategy Analysis
C. Solution Evaluation
D. Business Analysis Planning and Monitoring

### Distractor Analysis — Question 10

**Correct answer: C**

Solution Evaluation is the BABOK knowledge area that covers assessing the performance of a deployed solution against business objectives, measuring realized value, and recommending improvements or corrective actions. The post-implementation review is a Solution Evaluation activity.

**Why A is wrong:** Requirements Life Cycle Management covers tracing, maintaining, and approving requirements through the project lifecycle. It focuses on requirements documents, not post-deployment value measurement.

**Why B is wrong:** Strategy Analysis covers understanding the business need, current state, and desired future state before solution design begins. It is an upstream activity, not a post-deployment assessment.

**Why D is wrong:** Business Analysis Planning and Monitoring covers how BA work is planned, governed, and assessed during a project. It does not encompass evaluating whether a deployed solution delivered business value.

---

*Module 15 Quiz | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

---

## Question 11

A regional bank is replacing its mortgage origination system. The system processes
mortgage applications that involve multiple regulatory hold periods, third-party
appraisals, and title searches. A project manager suggests big bang deployment because
it is the simplest to coordinate. What is the strongest argument against big bang in
this specific scenario?

A. Big bang is not permitted for financial services systems under federal banking
   regulations

B. Big bang exposes the entire mortgage portfolio to risk simultaneously — any critical
   defect discovered post-cutover will affect all in-flight applications with no fallback,
   potentially delaying closings and creating regulatory and customer service risk

C. Big bang requires running both systems simultaneously, which doubles staff workload
   during the transition period

D. Big bang is only appropriate for systems with fewer than 100 users

### Distractor Analysis — Question 11

**Correct answer: B**

The core argument against big bang in high-consequence transactional systems is that
a post-cutover critical defect immediately affects all users and all transactions with
no fallback. In mortgage processing, where regulatory timelines and customer commitments
exist, this risk is material. A phased or pilot strategy limits blast radius.

**Why A is wrong:** Big bang is not prohibited by federal banking regulations as a
category. The argument against it is operational and risk-based, not regulatory in the
sense of a blanket prohibition.

**Why C is wrong:** Running both systems simultaneously describes parallel operation, not
big bang. Big bang retires the old system on cutover day.

**Why D is wrong:** Big bang is used across organizations of all sizes. The selection
criterion is risk tolerance and rollback feasibility, not user count.

---

## Question 12

A change manager at a manufacturing company reports that a group of shop floor workers
completed ERP training three months ago and scored well on the post-training assessment.
However, two weeks after go-live, the workers are entering data incorrectly, requiring
supervisors to make frequent corrections. Using the ADKAR model, what is the most
likely barrier?

A. Awareness — the workers do not understand why the ERP system was implemented

B. Knowledge — the workers' training assessment scores were falsely high and they do
   not actually know how to use the system

C. Ability — the workers have the knowledge from training but cannot perform correctly
   under real production pressure with live data and time constraints

D. Desire — the workers do not want to use the new system and are deliberately entering
   data incorrectly

### Distractor Analysis — Question 12

**Correct answer: C**

The workers passed the training assessment (Knowledge exists) but struggle in production
(Ability gap). The ADKAR model distinguishes between knowing how to do something in a
controlled training environment (Knowledge) and being able to perform it correctly under
real conditions (Ability). The appropriate intervention is supervised practice in a
realistic environment.

**Why A is wrong:** The workers went through training and are using the system — both
indicate Awareness and Desire have been achieved. The issue is performance quality, not
motivation or understanding of the change rationale.

**Why B is wrong:** The training assessment was conducted and produced high scores. While
assessments can be imperfect, the scenario's most direct diagnosis is the Knowledge-to-
Ability gap, not invalid assessment results.

**Why D is wrong:** Deliberate sabotage would suggest a Desire problem. The scenario
describes errors requiring correction, not intentional resistance. Misattributing an
Ability problem to Desire would lead to the wrong intervention.

---

## Question 13

A transition plan for a new procurement system includes detailed technical documentation,
a help desk contact list, and SLA commitments from the software vendor. Three months
after go-live, the operations team is unable to make a minor configuration change because
the only person who knows the system architecture left the project six months ago. What
critical element was missing from the transition plan?

A. A parallel operation period to verify the new system before project team disbandment

B. A formal knowledge transfer process that ensured operations team members understood
   and could act on the system architecture — not just that documentation existed

C. Vendor support escalation procedures for configuration changes

D. A post-implementation review conducted before the project team disbanded

### Distractor Analysis — Question 13

**Correct answer: B**

The scenario is a classic knowledge-in-one-person failure. Documentation existed but the
operations team could not use it independently. A formal knowledge transfer process —
structured walkthroughs, shadow periods, hands-on configuration practice — would have
ensured the operations team had working capability, not just access to documents.

**Why A is wrong:** Parallel operation addresses deployment risk, not post-go-live
operational capability. The problem occurred three months post-go-live — a parallel
period would not have addressed the knowledge transfer gap.

**Why C is wrong:** Vendor escalation procedures are useful but would not resolve an
internal configuration capability gap. Configuration knowledge must reside within the
organization, not solely with the vendor.

**Why D is wrong:** A PIR evaluates whether the solution delivered business value. It
does not directly ensure that the operations team has the capability to maintain the
system architecture.

---

## Question 14

The ADKAR Desire stage is best addressed by which type of intervention?

A. Distributing a detailed FAQ document explaining the business case for the change

B. Scheduling additional training sessions on system features the group has not yet used

C. One-on-one conversations that acknowledge personal concerns, address the "what's in it
   for me" question, and involve individuals in solution design where possible

D. Assigning a floor walker to sit with the group during their first week on the new
   system

### Distractor Analysis — Question 14

**Correct answer: C**

Desire is a motivational and emotional milestone — it requires individual engagement,
not information delivery. One-on-one conversations that acknowledge specific concerns
and create personal stakes in success address Desire directly. Involving individuals in
design also builds ownership, which generates Desire.

**Why A is wrong:** A FAQ document addresses Awareness by explaining the rationale. It
does not address Desire, which requires emotional engagement and personal motivation —
not more information.

**Why B is wrong:** Additional training addresses Knowledge. Desire must be present
before Knowledge investments will be effective — training a resistant group produces
Knowledge without commitment.

**Why D is wrong:** Floor walker support addresses Ability — the gap between knowing how
and performing correctly under pressure. It is a post-Desire, post-Knowledge intervention.

---

## Question 15

A post-implementation review for a new CRM system finds that the projected 30% reduction
in average call handling time has not materialized — average handling time is unchanged
at 8.5 minutes. The business case projected 5.9 minutes. Which PIR action most directly
addresses this finding?

A. Declare the project a failure and recommend a system replacement

B. Document the gap, investigate whether the cause is system configuration, process
   non-compliance, inadequate training, or missing features, and recommend specific
   corrective actions with owners and timelines

C. Close the PIR with a note that call handling time improvement will occur naturally
   as users gain experience over the next twelve months

D. Reopen the UAT phase and re-execute all call handling test cases

### Distractor Analysis — Question 15

**Correct answer: B**

A PIR finding of unmet business outcomes requires root cause investigation and corrective
action, not project condemnation. The gap may be solvable through process coaching, a
configuration change, or targeted retraining — all lower-cost interventions than system
replacement or UAT repetition.

**Why A is wrong:** Declaring failure and recommending replacement based on one metric
at one PIR measurement point is premature. The PIR exists to identify and address gaps,
not to terminate solutions that show partial success.

**Why C is wrong:** Passively waiting for organic improvement is not a professional PIR
response. If the expected improvement has not occurred, the BA must investigate why and
recommend action.

**Why D is wrong:** Repeating UAT is a testing activity for pre-deployment verification.
Operational performance issues post-go-live are investigated through operational analysis,
process observation, and user interviews — not by re-executing UAT test cases.

---

## Question 16

A BA is planning a pilot deployment for a new expense reporting system at a company
with 2,400 employees across eight regional offices. The pilot will include one regional
office of 300 employees. Which characteristic of the pilot group selection is most
important for the pilot to be useful?

A. The pilot group should be the most technically proficient office so the system is
   validated by the most capable users first

B. The pilot group should be representative of the full population in technology comfort
   level, role variety, and workflow complexity so that findings from the pilot predict
   the full rollout experience accurately

C. The pilot group should be geographically closest to headquarters to minimize support
   travel costs

D. The pilot group should be the smallest office available to minimize the impact of
   any defects discovered during the pilot

### Distractor Analysis — Question 16

**Correct answer: B**

Representativeness is the most critical pilot group characteristic. A pilot conducted
with atypically skilled or cooperative users produces overly optimistic results and
fails to surface problems that will emerge during full rollout. The pilot's purpose is
to predict and prepare — which requires a group that mirrors the full population.

**Why A is wrong:** Selecting the most technically proficient group will produce an
artificially smooth pilot. Problems experienced by average users will not surface,
and training approaches designed for expert users will fail when applied to the broader
population.

**Why C is wrong:** Geographic proximity to headquarters may reduce support costs but
does not make the pilot representative. Cost optimization is a secondary concern to
validity.

**Why D is wrong:** Using the smallest office minimizes exposure but may not be
representative of the diversity of roles and workflows in the larger population. Pilot
size should be driven by representativeness, not defect containment alone.

---

## Question 17

An EHR implementation project has a go-live date in five days. The training coordinator
reports that the Emergency Department nursing staff completed training three weeks ago
but has not had access to the practice sandbox since training ended. Which risk does
this situation most directly create?

A. Awareness risk — nurses may not remember why the system is being implemented

B. Ability risk — nurses have Knowledge from training but have not practiced under
   realistic conditions, increasing the probability of performance errors during
   critical patient care activities at go-live

C. Desire risk — nurses who have not used the system recently may lose motivation to
   adopt it

D. Reinforcement risk — nurses will revert to old behaviors because there are no
   accountability measures in place

### Distractor Analysis — Question 17

**Correct answer: B**

The three-week gap between training and go-live without sandbox access creates an Ability
risk. Knowledge from training decays without practice. Nurses who knew how to perform
tasks in training may struggle under real production conditions — particularly in a high-
stakes environment like the ED where errors have patient safety implications.

**Why A is wrong:** Awareness is about understanding why the change is happening. A
three-week training gap does not affect the nurses' understanding of the business
rationale.

**Why C is wrong:** Desire concerns motivation to support the change. A training gap
affects retention and performance capability, not motivational state.

**Why D is wrong:** Reinforcement applies after adoption has occurred and behavior is
at risk of reverting. The nurses have not yet gone live — this is a pre-go-live
Knowledge-to-Ability bridge issue, not a post-adoption reinforcement issue.

---

## Question 18

Which of the following scenarios describes an appropriate use of the lessons-learned
process?

A. The project manager distributes the lessons-learned report to the project team
   immediately after the PIR meeting, files it in the project archive, and considers
   the project closed

B. The BA facilitates a lessons-learned session at project close, documents findings
   categorized by process area, ensures the report is shared with the PMO and BA
   practice lead, and requests that two specific process improvements be incorporated
   into the organization's project methodology before the next ERP implementation begins

C. The BA writes a lessons-learned report and stores it in a personal folder for
   future reference

D. Lessons learned are collected only when the project was a failure, not when it was
   a success, since successful projects do not produce actionable insights

### Distractor Analysis — Question 18

**Correct answer: B**

Effective lessons-learned practice requires documentation, distribution to appropriate
stakeholders, and — critically — action. Requesting that specific improvements be
incorporated into methodology closes the loop between findings and organizational
learning. This is the professional standard.

**Why A is wrong:** Filing the report and closing the project without ensuring follow-up
action produces documents that are read once and forgotten. This is the most common
failure mode of lessons-learned processes.

**Why C is wrong:** Storing lessons learned in a personal folder makes them inaccessible
to the organization. Lessons learned must be shared and institutionalized to deliver
value.

**Why D is wrong:** Successful projects generate equally valuable lessons — what worked
well and should be repeated, what could be improved even though the outcome was
acceptable. Limiting lessons-learned to failures misses half the organizational learning
opportunity.

---

## Question 19

A BA is developing go-live support for a new patient scheduling system at a medical
clinic. Receptionists will use the system to book appointments — a task they currently
perform via phone and paper. Which go-live support resource is most important for this
user group on day one?

A. A vendor support hotline for technical issues requiring system patches

B. Floor walkers stationed at reception desks during patient-facing hours who can answer
   questions in real time without requiring receptionists to leave their workstation

C. A fifty-page user manual stored on the shared drive

D. A scheduled group training refresher session in week two of go-live

### Distractor Analysis — Question 19

**Correct answer: B**

Receptionists interact with patients in real time — any delay caused by system confusion
directly affects the patient experience. Floor walkers at the workstation provide
immediate, in-context support without requiring the receptionist to leave a patient or
wait for a callback. This is the highest-value go-live support resource for this role.

**Why A is wrong:** A vendor support hotline addresses technical system issues that
require development-level intervention. Day-one receptionist questions will be workflow
and usability questions, not patch-level technical issues.

**Why C is wrong:** A fifty-page manual is inaccessible during a patient-facing
interaction. No receptionist can search a manual while a patient is standing at the
desk. Quick reference cards are far more useful than comprehensive manuals for point-
of-use support.

**Why D is wrong:** A week-two refresher is valuable for addressing issues that emerge
after the initial go-live period, but it does not help receptionists on day one when
confidence and task accuracy are lowest.

---

## Question 20

The BABOK Guide places post-implementation review and solution value assessment in which
knowledge area, and what is the primary output of that knowledge area from a BA perspective?

A. Requirements Life Cycle Management — the primary output is an updated requirements
   baseline reflecting post-deployment changes

B. Solution Evaluation — the primary output is an assessment of solution performance
   against business objectives, including recommendations for enhancement or corrective
   action

C. Business Analysis Planning and Monitoring — the primary output is a revised BA plan
   for the next project phase

D. Strategy Analysis — the primary output is a future-state architecture incorporating
   lessons from the deployed solution

### Distractor Analysis — Question 20

**Correct answer: B**

Solution Evaluation is the BABOK knowledge area that covers assessing whether a deployed
solution delivers intended value, measuring performance against business objectives, and
recommending improvements. The primary output is the solution performance assessment with
actionable recommendations.

**Why A is wrong:** Requirements Life Cycle Management covers tracing and maintaining
requirements during the project lifecycle. While requirements may be updated post-
deployment through change control, RLCM is not the knowledge area for evaluating
whether the solution delivered business value.

**Why C is wrong:** Business Analysis Planning and Monitoring covers how BA work is
governed during a project. It does not produce post-deployment value assessments.

**Why D is wrong:** Strategy Analysis focuses on defining the business need and current/
future state before solution design. It is an upstream activity. Incorporating lessons
into a future-state architecture would involve a new Strategy Analysis effort, not the
Solution Evaluation of the current deployment.

---

*Module 15 Quiz (extended) | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
