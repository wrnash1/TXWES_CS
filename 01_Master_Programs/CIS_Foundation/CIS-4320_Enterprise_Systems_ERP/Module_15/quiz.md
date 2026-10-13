# Quiz: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

This quiz contains 10 multiple-choice questions worth 10 points each. Select the single best answer. Distractor analysis is provided for instructor and student review.

---

## Question 1

During which ASAP phase are the to-be business processes documented in formal workshops with business stakeholders, producing the primary reference document for the entire configuration phase?

A. Phase 1 — Project Preparation

B. Phase 2 — Business Blueprint

C. Phase 3 — Realization

D. Phase 4 — Final Preparation

**Correct Answer: B**

**Distractor Analysis:**

- **A — Project Preparation:** Project Preparation focuses on organizational setup — project charter, system landscape design, project organization. Business process workshops are not conducted in this phase.
- **B — Business Blueprint (Correct):** Business Blueprint is specifically designed to document the to-be business processes. The Q&A database guides structured workshops with business stakeholders; the output is the Business Blueprint document, which serves as the contract between business and project team for the Realization phase.
- **C — Realization:** Realization is the configuration and build phase — the team implements the processes documented in the Blueprint. Discovery and documentation of processes happens before Realization begins.
- **D — Final Preparation:** Final Preparation focuses on training, data migration rehearsals, and the Go/No-Go decision. Business process documentation is complete long before this phase.

---

## Question 2

A Salesforce implementation project is three months from go-live when the VP of Marketing requests that the project team also configure Salesforce Pardot (Marketing Cloud Account Engagement) for email campaigns — something that was not in the original scope. What project management phenomenon does this represent, and what should the project manager do?

A. This is a best practice enhancement; it should be added immediately at no additional cost.

B. This is scope creep; the project manager should evaluate the request through a formal change control process.

C. This is a hypercare activity; it should be deferred to after go-live.

D. This is a Business Blueprint gap; it should have been identified in Phase 2.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Adding an unplanned module three months before go-live is not a best practice enhancement — it is a significant scope change that would require additional configuration, testing, and training time, and would almost certainly delay the go-live date. There is no such thing as "no additional cost" for a module addition at this stage.
- **B — Scope creep through formal change control (Correct):** When a stakeholder requests something outside the original defined scope, the project manager must route it through a formal change control process. This involves: documenting the request, estimating the impact on schedule and budget, getting approval from the steering committee or project sponsor, and deciding whether to include it in the current project or defer to a Phase 2.
- **C:** Hypercare is the post-go-live intensive support period for the existing scope. Adding a new module is not a hypercare activity.
- **D:** A Business Blueprint gap is a process requirement that was missed during the Blueprint phase and discovered during Realization. This is a new requirement being added by an executive — it is scope creep, not a Blueprint gap.

---

## Question 3

In SAP's three-tier system landscape, what is the purpose of the Quality/Test (QAS) system?

A. To hold a backup copy of production data for disaster recovery

B. To allow developers to build and test configurations before they affect users

C. To provide a staging environment where integration testing, UAT, and regression testing are performed before changes move to production

D. To store archival data from closed fiscal years that is no longer needed in the production system

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Disaster recovery backups are maintained separately from the three-tier development landscape. The QAS system is not a backup system.
- **B:** Development and initial testing by developers is done in the DEV (Development) system, not QAS. QAS is downstream of DEV.
- **C — Staging for testing before production (Correct):** QAS is the middle tier between DEV and PRD. After configuration changes are developed and unit-tested in DEV, transport requests carry them to QAS. QAS is where integration testing, user acceptance testing (UAT), and regression testing are performed. The goal is to validate that changes work correctly in an environment that closely mirrors production before they go to PRD.
- **D:** Archival storage for historical data is handled through SAP's archiving tools (SAP ILM, ArchiveLink) against the production system — not through the QAS landscape system.

---

## Question 4

Using the ADKAR change management model, a change management analyst finds that employees know how to use the new ERP system (Knowledge = high) and want to succeed with it (Desire = high), but they are still performing their jobs incorrectly in the system two months after go-live. Which ADKAR stage is most likely the barrier?

A. Awareness

B. Desire

C. Ability

D. Reinforcement

**Correct Answer: C**

**Distractor Analysis:**

- **A — Awareness:** The scenario states that employees want to succeed (Desire is high), which implies they understand why the change was made (Awareness is sufficient). Low Awareness would manifest as employees not understanding why the change is happening at all.
- **B — Desire:** Desire is explicitly stated to be high. This is not the barrier.
- **C — Ability (Correct):** The gap between Knowledge (knowing what to do) and actual performance is the Ability stage. Employees may have learned the correct steps in training but cannot reliably perform them in the real work environment — especially under time pressure, with edge cases, or with the additional cognitive load of serving customers simultaneously. This requires hands-on practice, job aids at the point of need, and coaching support.
- **D — Reinforcement:** Reinforcement is about sustaining the change over time after it has been successfully adopted. The scenario describes employees who are still not performing correctly — which is a pre-adoption problem (Ability), not a post-adoption relapse problem (Reinforcement).

---

## Question 5

A Salesforce implementation team is preparing to deploy a major configuration update to production. The project uses Change Sets. A team member raises a concern that after deployment, they will not be able to tell which sandbox version of each component was deployed. Which Salesforce development approach addresses this limitation?

A. Using a Full Sandbox instead of a Developer Sandbox

B. Adopting Salesforce DX with metadata stored in a Git repository

C. Creating multiple outbound change sets for each component type

D. Exporting the deployment manifest from the Change Set to a CSV file

**Correct Answer: B**

**Distractor Analysis:**

- **A:** The sandbox type does not affect whether changes are tracked in version control. A Full Sandbox is used for testing fidelity, not for change history and deployment lineage.
- **B — Salesforce DX with Git (Correct):** Salesforce DX stores all metadata as source code in a version control repository (typically Git). Every change is committed with a message, timestamp, and author. Branches represent different development streams. The exact state deployed to production is traceable to a specific Git commit. This directly addresses the concern about not knowing which version was deployed.
- **C:** Creating multiple change sets does not provide version history or deployment lineage. It adds administrative complexity without solving the tracking problem.
- **D:** Exporting a deployment manifest to CSV provides a snapshot of what was deployed in a given change set, but it is a manual, point-in-time record. It does not provide true version control, branching, or the ability to compare configurations across environments.

---

## Question 6

A Crestwood Medical Group cutover plan specifies that the final production data migration must be complete by 4:00 AM for a 7:00 AM go-live. At 3:30 AM, the data migration is at 72% complete and running 30 minutes behind schedule. What should the cutover command team do first?

A. Immediately initiate the rollback procedure.

B. Announce a delayed go-live time of 10:00 AM to all stakeholders.

C. Assess whether the migration can be completed in time, check the rollback decision point criteria, and convene a rapid decision with the executive sponsor.

D. Allow the migration to continue and go live at 7:00 AM with only 72% of data loaded.

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Immediate rollback at 3:30 AM is premature. The rollback decision criteria should be assessed — there may be time to complete the migration, or there may be a planned buffer. Rollback is not the automatic first response to a delay.
- **B:** Announcing a delayed go-live without consulting the executive sponsor and assessing the full situation is premature. The decision to delay requires executive authorization and a revised plan.
- **C — Assess and convene decision (Correct):** The correct response is structured decision-making. First, assess the situation: is the migration accelerating or decelerating? Can it finish in time? Are there high-priority record sets that can be migrated first to allow a partial go-live? Check the rollback decision point: is the team still within the rollback window, or has that passed? Then bring the executive sponsor into a rapid decision conversation with the facts. This is what a rollback decision point and a cutover command structure are designed for.
- **D:** Going live with only 72% of data loaded could mean that 28% of patients, referrals, or contacts are not accessible on day one — causing significant operational disruption and potentially patient safety issues in a medical context.

---

## Question 7

What is the primary purpose of a hypercare period following an ERP go-live?

A. To complete the Business Blueprint documentation that was not finished before go-live

B. To provide intensive, rapid-response support during the highest-risk period immediately after production launch

C. To conduct additional user training for employees who were not present during the pre-go-live training

D. To perform the final data migration for records that were skipped during the cutover

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Business Blueprint documentation is a Phase 2 deliverable. If it is not complete by go-live, the project has a serious process gap. The hypercare period is not a documentation catch-up period.
- **B — Intensive post-launch support (Correct):** Hypercare acknowledges that the weeks immediately after go-live are when the system faces its most unpredictable conditions: real users, real data, real transaction volumes, and real edge cases that were not covered in testing. The hypercare structure keeps the project team engaged and available to resolve issues rapidly — before they escalate into business-disrupting problems.
- **C:** While additional training may be delivered during or after hypercare, that is a separate activity. The primary purpose of hypercare is issue resolution and system stabilization, not training delivery.
- **D:** Records skipped during cutover would be a data migration remediation activity, which might occur in the early post-go-live period, but it is not the primary purpose or definition of hypercare.

---

## Question 8

Total Cost of Ownership (TCO) for a Salesforce implementation over five years is best described as:

A. The sum of the Year 1 implementation consulting fees only

B. The annual Salesforce license fee multiplied by five

C. The complete lifecycle cost including licensing, implementation, integration maintenance, enhancements, and support over the full ownership period

D. The cost that appears on the Salesforce order form

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Year 1 consulting fees represent only a portion of Year 1 costs, which are themselves only a fraction of the five-year TCO. This dramatically understates the total investment.
- **B:** License fees are the most visible recurring cost, but TCO includes implementation services, integration maintenance, enhancement consulting, internal support staff, training, and potentially third-party app subscriptions. Multiplying the license fee by five significantly underestimates TCO.
- **C — Complete lifecycle cost (Correct):** TCO captures every cost associated with owning and operating the system — not just the license fee and implementation invoice. The implementation fee is often the highest single-year cost, but recurring annual costs (licensing, support staff, ongoing enhancements) accumulate significantly over a five-year period. A complete TCO model is essential for executive decision-making and for comparing different platform options.
- **D:** The Salesforce order form shows the agreed license pricing. It does not include internal implementation labor, integration costs, training, ongoing support staffing, or third-party AppExchange subscriptions.

---

## Question 9

SAP Activate differs from ASAP primarily because:

A. SAP Activate eliminates the need for user training

B. SAP Activate uses Agile sprints and a fit-to-standard philosophy, starting from pre-configured SAP Best Practices content

C. SAP Activate does not include a Go/No-Go decision before go-live

D. SAP Activate is only used for cloud implementations; ASAP is used for all on-premises implementations

**Correct Answer: B**

**Distractor Analysis:**

- **A:** User training remains a critical activity in SAP Activate — it is addressed in the Deploy phase. No methodology eliminates the need for training.
- **B — Agile sprints and fit-to-standard (Correct):** SAP Activate introduces two major changes. First, it uses an Agile sprint-based approach for the Realize phase, delivering working functionality incrementally rather than in one big bang. Second, it promotes a fit-to-standard philosophy: instead of designing custom processes and then configuring SAP to match, organizations are encouraged to review SAP's pre-configured Best Practices content and adopt SAP's standard processes wherever possible. This reduces customization costs and accelerates timelines.
- **C:** Go/No-Go decisions are included in SAP Activate's Deploy phase. Readiness assessment before production go-live is a universal best practice that neither ASAP nor Activate eliminates.
- **D:** SAP Activate is SAP's current recommended methodology for both cloud (S/4HANA Cloud) and on-premises (S/4HANA on-premises) implementations. ASAP predates cloud computing and was used for on-premises implementations. The cloud/on-premises distinction is not the primary differentiator between the two methodologies.

---

## Question 10

A company's end-users have completed all Salesforce training before go-live, but employee surveys show that most respondents "strongly agree" with the statement: "I don't understand why we're replacing our current system." According to the ADKAR model, which stage is the primary barrier?

A. Knowledge

B. Ability

C. Awareness

D. Reinforcement

**Correct Answer: C**

**Distractor Analysis:**

- **A — Knowledge:** Low Knowledge would manifest as "I don't know how to use the new system" — employees lack training or skill. The scenario states training is complete, so Knowledge is not the primary barrier.
- **B — Ability:** Ability is the gap between knowing how to do something and being able to do it under real-world conditions. The survey statement does not mention difficulty performing tasks — it expresses confusion about the purpose of the change.
- **C — Awareness (Correct):** The statement "I don't understand why we're replacing our current system" is a direct indicator of low Awareness. ADKAR's Awareness stage addresses whether people understand the business reasons for the change — the rationale, the problem being solved, and why the organization cannot continue with the status quo. If Awareness is low, employees will not engage with training meaningfully (even if they attend), and Desire will likely also be low. The communication program needs immediate strengthening.
- **D — Reinforcement:** Reinforcement addresses sustaining change after initial adoption. The scenario describes pre-go-live conditions — the system has not gone live yet — so there is no adopted behavior to reinforce or risk of relapse.

---

## Quiz Summary

| Question | Topic | Correct Answer |
|----------|-------|----------------|
| 1 | Business Blueprint is Phase 2 of ASAP | B |
| 2 | Scope creep managed through change control | B |
| 3 | QAS system purpose — staging for testing | C |
| 4 | ADKAR barrier — Ability gap | C |
| 5 | Salesforce DX solves change tracking limitation | B |
| 6 | Cutover delay — assess and convene decision | C |
| 7 | Hypercare purpose — intensive post-launch support | B |
| 8 | TCO definition — complete lifecycle cost | C |
| 9 | SAP Activate — Agile and fit-to-standard | B |
| 10 | ADKAR barrier — Awareness for "why" confusion | C |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
