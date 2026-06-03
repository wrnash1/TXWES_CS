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
