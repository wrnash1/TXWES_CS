# Quiz: Module 07 — Service Management Practices: Change Enablement

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Total Questions:** 10
**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Review the distractor analysis after submitting to reinforce exam-ready reasoning.

---

## Question 1

What is the primary purpose of the Change Enablement practice in ITIL 4?

* A) To deploy all approved changes into the live environment as quickly as possible
* B) To maximize the number of successful IT and service changes by ensuring that risks are properly assessed, authorizing changes to proceed, and managing the change schedule
* C) To document all configuration items and maintain an accurate record of the current IT infrastructure
* D) To restore normal service operation as quickly as possible following a disruption

Correct answer: B

Distractor analysis: B is correct because ITIL 4 defines the purpose of Change Enablement as maximizing successful changes through risk assessment, authorization, and change schedule management. A is incorrect because deploying changes into the live environment is the responsibility of Deployment Management, not Change Enablement. C is incorrect because documenting configuration items is the purpose of Service Configuration Management. D is incorrect because restoring service after a disruption is the purpose of Incident Management.

---

## Question 2

Which of the following most accurately describes a standard change in ITIL 4?

* A) A change requiring full risk assessment and CAB approval before implementation
* B) A change that must be implemented immediately to resolve a critical service failure, bypassing the normal authorization process
* C) A pre-authorized, low-risk, well-understood change that follows a documented procedure and does not require individual authorization per occurrence
* D) A customer-requested change that must be tracked through Service Request Management before authorization

Correct answer: C

Distractor analysis: C is correct because standard changes are pre-authorized as a class — the risk and procedure were assessed and approved when the change type was established, so individual occurrences do not require new authorization. A is incorrect because that describes a normal change. B is incorrect because that describes an emergency change, which still requires expedited authorization. D is incorrect because that describes a service request, which is a different practice.

---

## Question 3

A company is planning to migrate its entire customer relationship management system from on-premises servers to a cloud platform. The migration affects 12 business units, carries significant risk of data loss if not executed correctly, and has never been performed in this organization. Which change type applies?

* A) Standard change — cloud migrations are routine in modern IT and can be pre-authorized
* B) Emergency change — the urgency of moving to cloud requires fast-tracking through an Emergency CAB
* C) Normal change — the migration requires individual risk assessment and authorization, with CAB advisory input appropriate given the risk and scope
* D) Normal change — the service owner submits it and the change is automatically approved after 72 hours with no response

Correct answer: C

Distractor analysis: C is correct because a high-risk, high-impact change that has never been performed in this organization is a normal change requiring individual risk assessment and authorization. Given the scope and risk, CAB advisory input is appropriate. A is incorrect because cloud migrations at this scale and complexity are not pre-authorized standard changes. B is incorrect because emergency changes require an active incident or imminent critical failure — a planned migration does not qualify. D is incorrect because normal changes are never automatically approved by elapsed time.

---

## Question 4

What is the role of the Change Advisory Board (CAB) in ITIL 4?

* A) The CAB holds final authorization authority over all normal changes and must approve every change before it can proceed
* B) The CAB provides advisory support to the change authority by reviewing and making recommendations on high-risk or high-impact normal changes
* C) The CAB is responsible for deploying approved changes and verifying that they succeeded
* D) The CAB manages the change schedule and owns the coordination of all implementation windows

Correct answer: B

Distractor analysis: B is correct because ITIL 4 defines the CAB as an advisory body. It reviews high-risk or high-impact normal changes and makes recommendations to the change authority, which holds the actual authorization power. A is incorrect because the CAB does not authorize — this is the most common exam trap related to the CAB. C is incorrect because deploying and verifying changes is the responsibility of Deployment Management. D is incorrect because managing the change schedule is a Change Enablement activity broadly, not a specific CAB responsibility.

---

## Question 5

A zero-day vulnerability is being actively exploited in a production web server. A vendor-supplied patch is available. There is no time for a standard weekly CAB meeting. What is the correct approach under ITIL 4 Change Enablement?

* A) Implement the patch immediately without authorization, then document and report it afterward
* B) Wait for the next scheduled CAB meeting to ensure proper review before applying any patch
* C) Classify this as an emergency change and obtain expedited authorization from an Emergency CAB or designated senior authority before or as close to implementation as possible
* D) Classify this as a standard change because security patching is a routine pre-authorized activity

Correct answer: C

Distractor analysis: C is correct because ITIL 4 requires that emergency changes be authorized, even when the process is expedited. The Emergency CAB or a designated senior authority provides that authorization quickly. A is incorrect because implementing without any authorization violates Change Enablement principles — expedited authorization is not the same as no authorization. B is incorrect because waiting for a regular CAB cycle while active exploitation is occurring would cause ongoing harm. D is incorrect because a patch responding to active exploitation is not a routine pre-authorized activity — it is a response to an active security incident.

---

## Question 6

How does Change Enablement relate to Deployment Management in ITIL 4?

* A) They are the same practice with different names — both handle authorization and deployment of changes
* B) Change Enablement assesses and authorizes the change; Deployment Management physically moves the change into the live environment
* C) Deployment Management assesses and authorizes the change; Change Enablement executes the physical deployment
* D) Change Enablement is used for software changes; Deployment Management is used for hardware changes

Correct answer: B

Distractor analysis: B is correct because ITIL 4 distinguishes these as separate practices with complementary roles. Change Enablement is the governance layer — it assesses risk and authorizes changes. Deployment Management is the execution layer — it physically deploys the authorized change into production. A is incorrect because they are explicitly separate practices. C is incorrect because the roles are reversed — Change Enablement governs and Deployment Management executes. D is incorrect because the distinction is about governance versus execution, not about software versus hardware.

---

## Question 7

An IT team has a category of change they perform several times each week: applying approved security patches from the vendor's monthly patch list. The risk is well understood and a documented rollout procedure has been tested and validated. Which approach best reflects Change Enablement best practice for this change category?

* A) Require a full CAB review for each patch application, since security patches always carry some risk
* B) Establish this category as a standard change with pre-authorization, documented procedure, and periodic review to ensure the pre-authorization remains appropriate
* C) Skip Change Enablement for routine patches since they are too frequent to go through any governance process
* D) Classify each patch as an emergency change to expedite implementation and avoid bureaucratic delays

Correct answer: B

Distractor analysis: B is correct because the scenario describes a change type that meets the criteria for a standard change — well understood, documented procedure, validated, and recurring. Pre-authorizing it as a standard change allows efficient execution without bypassing governance. A is incorrect because requiring CAB review for every pre-tested patch application applies unnecessary governance overhead — this would violate Keep It Simple and Practical. C is incorrect because skipping Change Enablement entirely eliminates governance, which is not acceptable even for routine changes. D is incorrect because emergency changes are reserved for actual emergencies — routine patching is not an emergency.

---

## Question 8

What is the purpose of the change schedule in Change Enablement?

* A) To document the risk assessment and rollback plan for each individual change
* B) To record the results of the CAB advisory review for each change submitted
* C) To list all authorized changes and their planned implementation dates, coordinating timing to prevent conflicts and communicate plans to stakeholders
* D) To track the number of successful versus failed changes over a defined reporting period

Correct answer: C

Distractor analysis: C is correct because ITIL 4 defines the change schedule as a document listing authorized changes and planned dates, used to coordinate timing, prevent conflicts, and communicate to stakeholders. A is incorrect because risk assessments and rollback plans are part of the individual change record, not the change schedule. B is incorrect because CAB review recommendations are documented in the change record, not the change schedule. D is incorrect because tracking success rates is a metrics and reporting activity, not the purpose of the change schedule.

---

## Question 9

Which of the following scenarios most accurately illustrates the application of the Progress Iteratively with Feedback Guiding Principle to a large-scale normal change?

* A) Deploying all components of a new enterprise resource planning system in a single weekend cutover to minimize total disruption time
* B) Requiring CAB review for every individual change within a large program, regardless of risk level
* C) Breaking the ERP deployment into phases — deploying one module at a time, measuring results, and using feedback to adjust the approach before deploying the next module
* D) Submitting a single consolidated change request for all planned ERP changes to reduce administrative overhead

Correct answer: C

Distractor analysis: C is correct because Progress Iteratively with Feedback specifically directs organizations to organize work into manageable increments, measure results, and use feedback to improve subsequent iterations. Phased deployment with measurement between phases is a direct application of this principle. A is incorrect because a single all-at-once deployment has no feedback checkpoints and concentrates risk. B is incorrect because requiring maximum governance for every component regardless of risk violates Keep It Simple and Practical. D is incorrect because consolidating everything into one change request addresses administrative convenience, not iterative delivery.

---

## Question 10

An organization has a documented change procedure for network switch replacements at branch offices. The procedure has been tested, the risk has been formally assessed and accepted, and the change authority has formally pre-approved the procedure. A branch experiences a switch failure and needs an immediate replacement. How should this change be handled?

* A) As an emergency change, because the branch is currently experiencing a service disruption and urgency is high
* B) As a standard change, because the procedure is pre-authorized, well-understood, and documented — individual authorization is not required
* C) As a normal change, because any change affecting live infrastructure requires individual risk assessment and CAB review
* D) No change type applies because the switch replacement is a hardware repair, not a service change

Correct answer: B

Distractor analysis: B is correct because the scenario describes a change type that has been formally pre-authorized — the procedure is documented, risk has been assessed and accepted, and the change authority has approved the category. This is the definition of a standard change. A is incorrect because the fact that there is urgency does not automatically make a change an emergency change if an appropriate pre-authorized procedure already exists for this situation. C is incorrect because pre-authorization means standard changes do not require individual CAB review per occurrence. D is incorrect because replacing a failed switch affects service continuity and is clearly within the scope of Change Enablement.
