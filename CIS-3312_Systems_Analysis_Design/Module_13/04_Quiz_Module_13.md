# Quiz: Module 13 - Implementation and Change Management
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
A hospital is replacing its patient records system. Because patient care cannot be interrupted, the hospital plans to run both the old and the new systems simultaneously for 90 days, with staff entering data in both, before switching off the legacy system. Which deployment strategy is this?
*   A) Direct cutover (big bang) — all users switch to the new system on a single go-live date
*   B) Pilot rollout — a small representative group tests the new system before full deployment
*   C) Phased rollout — one department or ward at a time transitions to the new system
*   D) Parallel operation — both systems run simultaneously until confidence is established to decommission the old one
*   **Correct Answer:** D) Parallel operation — both systems run simultaneously until confidence is established to decommission the old one
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Direct cutover decommissions the old system the moment the new one goes live; no simultaneous operation occurs.
    *   *Why B is incorrect:* A pilot deploys to a small group for validation before broader rollout; the scenario describes all staff in both systems simultaneously.
    *   *Why C is incorrect:* Phased rollout deploys sequentially to one group at a time; the scenario describes all users in both systems at the same time.
    *   *Why D is correct:* Running both systems simultaneously until the organization is confident enough to decommission the old one is the defining characteristic of parallel operation — high cost and effort, but lowest risk for critical systems where errors cannot be tolerated.

---

**Question 2**
In the context of systems implementation, which of the following is the most accurate definition of **transition requirements**?
*   A) Requirements that define the ongoing operational capabilities the system must provide to users after full deployment
*   B) Requirements describing capabilities needed only during the transition from the current state to the future state, which are no longer needed after cutover
*   C) Requirements that specify how stakeholders should be trained to use the new system during the go-live phase
*   D) Requirements for the backup and disaster recovery processes that protect the system after it goes live in production
*   **Correct Answer:** B) Requirements describing capabilities needed only during the transition from the current state to the future state, which are no longer needed after cutover
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Requirements for ongoing operational capabilities after full deployment are solution requirements (persistent), not transition requirements (temporary).
    *   *Why C is incorrect:* Training plans and materials are part of the OCM and training plan activities; while training may be described in transition requirements, the definition of transition requirements is broader and specifically about temporary capabilities.
    *   *Why D is incorrect:* Backup and disaster recovery requirements are non-functional solution requirements (availability/resilience) that persist after go-live; they are not temporary transition requirements.
    *   *Why B is correct:* BABOK® KA 3 defines transition requirements as a specific, temporary category of requirements — needed to support the changeover (e.g., data migration scripts, bulk import tools, parallel reporting) but with no value after the transition is complete.

---

**Question 3**
According to the Prosci ADKAR model, a BA discovers through stakeholder feedback that users understand the new system is being deployed (Awareness) and want to use it (Desire), but they make repeated errors because they do not know how to perform key tasks in the new interface. Which ADKAR element is the gap?
*   A) Awareness — users need more information about why the change is happening
*   B) Desire — users need stronger motivation to engage with the change
*   C) Knowledge — users need training on how to perform tasks in the new system
*   D) Reinforcement — users need incentives and recognition to sustain their new behaviors
*   **Correct Answer:** C) Knowledge — users need training on how to perform tasks in the new system
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The scenario confirms users have Awareness; they know the system is being deployed. The gap is not at the Awareness stage.
    *   *Why B is incorrect:* The scenario confirms users have Desire; they want to use the system. The gap is not motivation.
    *   *Why D is incorrect:* Reinforcement addresses sustaining change after users have already demonstrated the new behaviors; users in this scenario cannot yet perform the tasks correctly, so reinforcement is premature.
    *   *Why C is correct:* In the ADKAR model, Knowledge is the element that addresses knowing *how* to change — the skills, procedures, and behaviors required in the new state. Users making errors because they don't know how to use the new interface have a clear Knowledge gap, addressed by targeted role-specific training.

---

**Question 4**
A BA is conducting a go-live readiness assessment two days before a planned system launch. The assessment reveals that the data migration validation tests have not been completed and 15% of migrated customer records have unresolved data quality errors. What is the most appropriate action?
*   A) Proceed with go-live and address the data quality errors through customer service tickets after launch
*   B) Delay go-live until data migration is completed and validated, and present the risk to the project sponsor for a go/delay decision
*   C) Launch the system without the affected customer records and migrate the remaining 15% in the following week
*   D) Cancel the project and restart data migration from the beginning with a new vendor
*   **Correct Answer:** B) Delay go-live until data migration is completed and validated, and present the risk to the project sponsor for a go/delay decision
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Launching with known data quality errors forces customers to experience system failures and erodes trust; addressing critical data errors post-launch is more expensive and disruptive than delaying.
    *   *Why C is incorrect:* Launching without 15% of customer records creates an incomplete system that cannot serve all users from day one, violating operational requirements and potentially causing contractual issues.
    *   *Why D is incorrect:* A complete project cancellation and vendor restart is a disproportionate response to a data quality issue that is resolvable with additional remediation time.
    *   *Why B is correct:* The purpose of a go-live readiness assessment is precisely to surface blockers like this before launch. The appropriate action is to escalate the validated risk to the decision authority (sponsor), recommend a delay, and provide options — not to proceed with known critical failures.

---

**Question 5**
A BA is developing the implementation plan for a new finance system. The team has identified a requirement for a bulk data import utility that will load five years of historical invoice data from the legacy system's export files into the new database schema. This utility will be used only during the cutover weekend and will be decommissioned immediately afterward. How should this requirement be classified?
*   A) A functional requirement — because it describes a specific system behavior (importing data) that the system must perform
*   B) A non-functional requirement — because it describes a performance characteristic (importing five years of data in a limited window)
*   C) A transition requirement — because it is needed only to support the cutover from the legacy system and has no value after the transition
*   D) A business rule — because it defines a constraint (five years of data must be retained) that governs the organization's data management policy
*   **Correct Answer:** C) A transition requirement — because it is needed only to support the cutover from the legacy system and has no value after the transition
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While the import utility does perform a function, classifying it as a standard functional requirement (permanent system capability) misses the critical characteristic: it is temporary and will be decommissioned.
    *   *Why B is incorrect:* A non-functional requirement (quality attribute) describes how the system performs ongoing operations; the import utility is not an ongoing system capability.
    *   *Why D is incorrect:* A business rule defines a policy constraint that the system enforces continuously; the import utility is a one-time technical activity, not a persistent business rule.
    *   *Why C is correct:* BABOK® KA 3 defines transition requirements as capabilities needed only during the change from current to future state. A one-time data migration utility used only during cutover weekend — with no post-go-live value — is the textbook definition of a transition requirement.
