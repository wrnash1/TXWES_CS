# Quiz: Module 12 - Technical Management Practices - Deployment Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the Deployment Management practice in ITIL 4?
*   A) To assess the risk of proposed changes and authorize them to proceed through the change schedule.
*   B) To move new or changed hardware, software, documentation, processes, or any other component to live environments.
*   C) To package a set of changes into a release and manage the release schedule across the organization.
*   D) To monitor live environments for events that may indicate a degradation in service quality or a potential failure.
*   **Correct Answer:** B) The purpose of Deployment Management is to move new or changed components to live environments.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of Deployment Management as moving new or changed hardware, software, documentation, processes, or any other component to live environments. It is the execution arm of the change-release-deployment workflow — responsible for the physical or logical movement of components.
    *   *Why A is incorrect:* Assessing risk and authorizing changes is the purpose of Change Enablement. Deployment Management executes after authorization has been granted — it does not perform the authorization itself.
    *   *Why C is incorrect:* Packaging changes into a release and managing the release schedule is the purpose of Release Management. Deployment Management moves the release into the live environment after Release Management has prepared it.
    *   *Why D is incorrect:* Monitoring live environments for events and potential failures is the purpose of Monitoring and Event Management, not Deployment Management.

---

**Question 2**
Which of the following most accurately describes the distinction between Deployment Management and Change Enablement in ITIL 4?
*   A) Change Enablement and Deployment Management are two names for the same practice — ITIL 4 uses them interchangeably.
*   B) Change Enablement assesses risk and authorizes whether a change may proceed; Deployment Management physically moves the authorized change into the live environment.
*   C) Deployment Management authorizes the change, and Change Enablement executes the deployment in the live environment.
*   D) Change Enablement handles software deployments; Deployment Management handles hardware installations.
*   **Correct Answer:** B) Change Enablement governs authorization; Deployment Management executes the physical movement of components to live.
*   **Distractor Analysis:**
    *   *Why B is correct:* These are two distinct ITIL 4 practices with complementary but separate responsibilities. Change Enablement is the governance practice — it assesses risk, consults the CAB where needed, and authorizes the change. Deployment Management is the execution practice — it moves the authorized component to the live environment. One authorizes; the other delivers.
    *   *Why A is incorrect:* ITIL 4 defines these as distinct practices with different purposes, activities, and scope. Treating them as interchangeable would cause authorization and execution responsibilities to be confused.
    *   *Why C is incorrect:* This reverses the roles. Change Enablement holds the authorization function; Deployment Management holds the execution function. Deployment Management does not authorize changes.
    *   *Why D is incorrect:* Both Change Enablement and Deployment Management apply to all types of components — hardware, software, documentation, and processes. The distinction is not by component type but by function (authorization vs. execution).

---

**Question 3**
A financial services company is deploying a critical update to its core banking platform. The update is complex, has never been deployed to this scale before, and affects all 50,000 customers. The deployment team wants to minimize risk. Which deployment approach is most appropriate?
*   A) Big bang deployment — deploy the update to all 50,000 customers simultaneously to minimize the deployment window and reduce complexity.
*   B) Phased deployment — roll out the update to a small subset of customers first, validate the deployment, then progressively expand to the full customer base.
*   C) Continuous deployment — use a CI/CD pipeline to push small code changes to all customers automatically as soon as each change passes testing.
*   D) No formal approach is needed — the development team should deploy directly to production without a deployment plan.
*   **Correct Answer:** B) Phased deployment limits the blast radius of any issues and allows validation in production conditions before full rollout to all customers.
*   **Distractor Analysis:**
    *   *Why B is correct:* For a complex, high-impact deployment to 50,000 customers, phased deployment is the appropriate risk mitigation strategy. Starting with a small subset allows the team to detect issues in production conditions — performance problems, integration failures, data issues — before they affect all customers. The rollout can be paused or rolled back at any phase if problems emerge.
    *   *Why A is incorrect:* Big bang deployment simultaneously affects all customers, meaning any deployment failure immediately impacts everyone. For a complex, high-stakes update, this maximizes exposure and recovery cost if issues occur.
    *   *Why C is incorrect:* Continuous deployment via CI/CD is designed for small, frequent incremental changes — not for large, complex releases. This approach is inappropriate for a single complex update affecting core banking functionality.
    *   *Why D is incorrect:* An unplanned deployment to production for a change of this scale and complexity would violate Change Enablement principles and expose the organization to unacceptable risk without authorization, testing, or a rollback plan.

---

**Question 4**
During a deployment of a new version of a company's HR application, the deployment team discovers that a critical integration with the payroll system has broken in the live environment. The issue cannot be fixed quickly. What should the deployment team do according to Deployment Management best practices?
*   A) Continue the deployment and file an incident report — the payroll integration issue will be resolved as a separate incident after the deployment is complete.
*   B) Execute the pre-tested rollback procedure to revert to the previous working version, minimizing the impact on the payroll system and users.
*   C) Escalate the issue to the Change Advisory Board and wait for a new change authorization before taking any further action.
*   D) Rebuild the deployment from scratch using the original source code, since the current deployment package is corrupt.
*   **Correct Answer:** B) Executing the pre-tested rollback procedure restores service and minimizes business impact — this is the purpose of having a rollback plan.
*   **Distractor Analysis:**
    *   *Why B is correct:* A tested rollback procedure is a required component of any deployment plan for high-risk changes. When a deployment causes a critical integration failure that cannot be fixed quickly, the fastest path to restoring normal service is to execute the rollback — reverting to the last known working state. This is precisely why rollback planning is part of Deployment Management best practices.
    *   *Why A is incorrect:* Completing a deployment that has broken a critical system integration and then treating the broken integration as a separate incident is not appropriate — the deployment itself is the cause. The deployment should be halted and reversed, not completed.
    *   *Why C is incorrect:* While Change Enablement may need to be informed, waiting for a new CAB authorization before taking action would prolong the impact on the payroll system. The rollback plan was part of the original authorized deployment and does not require a new authorization to execute.
    *   *Why D is incorrect:* Rebuilding from source code would take significantly longer than executing a rollback and is not a standard Deployment Management response. A pre-tested rollback package should already exist.

---

**Question 5**
Which of the following correctly describes the relationship between Release Management and Deployment Management in ITIL 4?
*   A) Release Management and Deployment Management are the same practice — ITIL 4 combined them into a single unified practice in version 4.
*   B) Release Management packages and schedules changes into releases for deployment; Deployment Management moves those releases into the live environment.
*   C) Deployment Management packages releases for testing and staging; Release Management deploys the tested releases to the live environment.
*   D) Release Management only applies to software releases; Deployment Management only applies to hardware installations.
*   **Correct Answer:** B) Release Management prepares and schedules releases; Deployment Management moves them into live.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines these as distinct but complementary practices. Release Management determines what changes are bundled together into a release, manages the release schedule, and ensures readiness for deployment. Deployment Management then takes that release and physically or logically moves it into the live environment. Release Management prepares the package; Deployment Management delivers it.
    *   *Why A is incorrect:* ITIL 4 defines Release Management and Deployment Management as separate practices with distinct purposes. They were not merged in ITIL 4 — each retains its own defined scope.
    *   *Why C is incorrect:* This reverses the responsibilities. Deployment Management moves to live; Release Management packages and schedules — not the other way around. Release Management does not deploy to live.
    *   *Why D is incorrect:* Both practices apply to all types of components — software, hardware, documentation, and processes. The scope distinction is based on function (packaging/scheduling vs. moving to live), not component type.
