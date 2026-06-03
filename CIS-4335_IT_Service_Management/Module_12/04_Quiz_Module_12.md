# Quiz: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

### Question 1

What is the defined purpose of Release and Deployment Management in ITIL 4?

- A) To assess the risk of proposed changes and authorize them to proceed to production.
- B) To make new and changed services and features available for use.
- C) To monitor production environments for events that may indicate service degradation.
- D) To package sets of changes into releases and manage the release schedule.

**Correct Answer:** B) The purpose of Release and Deployment Management is to make new and changed services and features available for use.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 explicitly defines the purpose of Release and Deployment Management as making new and changed services and features available for use. This encompasses release planning, deployment execution, rollback planning, and post-implementation review — the full lifecycle of bringing a change into active use.
- *Why A is incorrect:* Assessing risk and authorizing changes is the purpose of Change Enablement. Release and Deployment Management operates after authorization has been granted — it does not perform the authorization itself.
- *Why C is incorrect:* Monitoring production environments for events is the purpose of Monitoring and Event Management. Release and Deployment Management is concerned with deploying changes, not with ongoing environmental surveillance.
- *Why D is incorrect:* Packaging changes into releases and managing the release schedule is part of release planning within Release and Deployment Management, but the defined purpose is broader — making services available for use, which includes the entire deployment lifecycle.

---

### Question 2

A company needs to deploy a new version of its customer-facing mobile banking application. The deployment team wants the ability to instantly redirect all traffic back to the previous version if critical problems are detected within minutes of the switch. Which deployment approach best meets this requirement?

- A) Big bang deployment — replace the old version entirely in a single operation for all users.
- B) Phased deployment — roll out to 10% of users, validate, then expand to the full base.
- C) Blue-green deployment — maintain two identical production environments and switch traffic via load balancer.
- D) Canary deployment — route 1% of users to the new version and monitor error rates.

**Correct Answer:** C) Blue-green deployment provides near-instantaneous rollback by redirecting traffic back to the inactive prior-version environment.

**Distractor Analysis:**

- *Why C is correct:* Blue-green deployment maintains two identical production environments. The new version is deployed and validated in the inactive environment before any traffic is switched. The cutover is a load balancer or DNS redirect — a near-instantaneous operation. Rollback is the same operation in reverse, taking seconds. No other deployment approach provides comparable rollback speed.
- *Why A is incorrect:* Big bang deployment replaces the old version entirely. Rolling back requires re-deploying the old version — a process that takes minutes to hours and may involve database state complications. Instant rollback is not available.
- *Why B is incorrect:* Phased deployment limits blast radius but does not provide instant rollback. Rolling back a phased deployment requires rolling back each completed phase, which is a multi-step operation, not an instant one.
- *Why D is incorrect:* Canary deployment reduces the affected population to a small percentage, which is excellent for early signal detection, but rollback still requires redirecting that canary population — faster than big bang, but not instantaneous in the way a pre-positioned blue-green environment is.

---

### Question 3

An IT team completed a deployment at 11 PM and immediately observed that 4% of transactions were generating errors. The deployment plan included a rollback procedure. What is the primary reason rollback planning is considered a mandatory component of any deployment plan in ITIL 4?

- A) Rollback planning is required by law under most data protection regulations.
- B) Rollback planning ensures that a tested, documented procedure exists to restore the previous service state quickly when a deployment causes unacceptable problems.
- C) Rollback planning reduces the time required to develop the original deployment — shorter deployments are safer.
- D) Rollback planning eliminates the need for post-deployment monitoring because rollbacks happen automatically.

**Correct Answer:** B) Rollback planning ensures a tested, documented procedure exists to restore the previous service state quickly when a deployment causes unacceptable problems.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 treats rollback planning as a required element of deployment management because deployments can fail in production despite thorough testing. When failure occurs, the fastest path to restoring service is executing a pre-planned, pre-tested rollback. Without a rollback plan, teams must improvise under pressure — which increases both the time to restore service and the risk of causing additional damage.
- *Why A is incorrect:* While regulatory frameworks may address change management in regulated industries, rollback planning is an ITIL 4 best practice based on service continuity principles, not a legal mandate in general.
- *Why C is incorrect:* Rollback planning has no relationship to deployment development time. The two are independent activities — a simple deployment can have a complex rollback, and a complex deployment may have a straightforward rollback.
- *Why D is incorrect:* Rollback planning does not eliminate the need for post-deployment monitoring. Monitoring is how teams detect that a rollback is needed in the first place. Without monitoring, the conditions that should trigger a rollback may go undetected.

---

### Question 4

A release manager is planning the deployment of a database-backed application update. The release includes a schema migration that adds three new columns and removes one deprecated column from the orders table. Why does the schema change require special rollback planning compared to the application code change?

- A) Database schema changes are simpler to roll back because databases have built-in undo functionality.
- B) Removing a column permanently deletes any data stored in that column — this data cannot be recovered from the schema rollback itself if transactions were written after deployment.
- C) Schema changes do not need rollback planning because they only affect internal database structure, not users.
- D) Application code rollback automatically includes the schema rollback — no separate plan is needed.

**Correct Answer:** B) Removing a column permanently deletes data stored in it — if transactions populated that column after deployment, a schema rollback cannot recover that data without a separate backup restore.

**Distractor Analysis:**

- *Why B is correct:* Database schema rollbacks are complex because schema changes can result in data being written to new structures during the deployment window. If a column is dropped and then the schema is rolled back by re-adding the column, the data that was written to that column during the window is gone — the column structure returns, but the data that was in it is lost unless a point-in-time backup is restored. This is why schema changes require careful rollback planning separate from code deployment.
- *Why A is incorrect:* Databases do not have universal automatic undo for schema changes. While some platforms support transactional DDL, many production environments require explicit scripts to reverse schema migrations, and data written between the forward and reverse migrations complicates recovery.
- *Why C is incorrect:* Schema changes directly affect application functionality. An application coded to expect a certain column that no longer exists — or that has changed data type — will fail in ways that are immediately visible to users.
- *Why D is incorrect:* Application code rollback and database schema rollback are independent operations. Rolling back the application binary does not reverse schema changes. Both must be planned and executed separately.

---

### Question 5

Following a deployment, the operations team discovers a session-cache warm-up step was missing from both the deployment plan and the release notes. As a result, 200 users experienced an 18-minute login failure while the engineer diagnosed the undocumented dependency. Which ITIL 4 activity most directly addresses preventing this from recurring?

- A) Change the deployment approach from phased to blue-green so that future deployments can be rolled back faster.
- B) Conduct a post-implementation review, document the missing step as a lesson learned, and update the deployment plan template and release note standards.
- C) Increase the deployment testing cycle from two weeks to four weeks so that all dependencies are discovered before production.
- D) Assign a dedicated on-call engineer whose only job is to monitor for undocumented dependencies during all future deployments.

**Correct Answer:** B) The post-implementation review captures lessons learned and drives improvements to deployment plan templates and release note standards.

**Distractor Analysis:**

- *Why B is correct:* The post-implementation review is ITIL 4's mechanism for turning deployment experience into organizational learning. Documenting the missing session-cache step as a lesson learned, then updating the deployment plan template to include it as a standard checklist item, directly prevents the same error in future releases. This also feeds the Continual Improvement Register.
- *Why A is incorrect:* Changing the deployment approach addresses rollback speed, not the root cause — an undocumented dependency. The session-cache issue would recur in a blue-green deployment as well unless the dependency is documented and planned for.
- *Why C is incorrect:* Extending the testing cycle may help discover some dependencies but does not guarantee discovery of all operational dependencies. A session-cache warm-up issue may not surface in a test environment at all. Documentation and checklist improvement is a more targeted solution.
- *Why D is incorrect:* Assigning a dedicated monitoring engineer treats the symptom (delayed diagnosis) rather than the cause (missing documentation). Future deployments with the same undocumented dependency would still take time to diagnose — just with a dedicated resource doing the diagnosing.

---

### Question 6

A canary deployment is currently routing 5% of production traffic to a new application version. Automated monitoring shows that the error rate for the canary population is 0.3%, compared to 0.1% for the stable population. The release manager must decide whether to proceed with expanding the rollout or roll back the canary. Which factor is most important for making this decision?

- A) The 0.2% error rate difference is statistically insignificant and the rollout should always proceed on schedule.
- B) The absolute number of errors in the canary population and their business impact — a 0.2% increase in errors on a payment processing endpoint is more significant than the same rate on a help page.
- C) The deployment approach should be changed to big bang to reduce the complexity of the monitoring decision.
- D) The canary should be rolled back immediately any time the error rate exceeds 0.1% regardless of business context.

**Correct Answer:** B) The business impact of the errors — not just their statistical rate — determines whether the difference is acceptable.

**Distractor Analysis:**

- *Why B is correct:* A 0.2% error rate increase must be evaluated in its business context. On a payment processing endpoint with millions of transactions, 0.2% represents thousands of failed payments — an unacceptable business impact that warrants rollback. On a low-traffic informational page, the same rate increase may be within acceptable noise. ITIL 4's focus on value and business outcomes means technical metrics must always be interpreted in business terms.
- *Why A is incorrect:* Statistical significance depends on sample size and business stakes. A rate difference that appears small in percentage terms may represent significant user harm at scale. Proceeding purely on schedule without evaluating business impact contradicts ITIL 4 value-focused principles.
- *Why C is incorrect:* Switching to big bang would eliminate the risk-limiting benefit of the canary approach and expose all users to the elevated error rate. Canary deployments exist precisely to enable this kind of monitored, incremental rollout decision.
- *Why D is incorrect:* Rigid thresholds divorced from business context lead to unnecessary rollbacks of safe releases. A 0.1% baseline and 0.1% threshold cannot meaningfully distinguish acceptable variance from a real problem without knowing what those errors represent to customers and the business.

---

### Question 7

The ITIL 4 guiding principle "Optimize and Automate" is applied to a company's deployment pipeline. The pipeline currently has eight manual approval steps, three of which serve no practical purpose and have never blocked a deployment in the past two years. What does this guiding principle say should be done first before automating the pipeline?

- A) Automate all eight steps immediately — automation is always the priority under this principle.
- B) First optimize the process by removing or consolidating the unnecessary manual steps, then automate the streamlined process.
- C) Add additional manual steps to ensure more oversight before automation is introduced.
- D) The principle does not apply to deployment pipelines — it only covers infrastructure provisioning.

**Correct Answer:** B) The principle advises optimizing first — removing waste — then automating the optimized process.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4's "Optimize and Automate" principle explicitly states that organizations should optimize processes first and then automate them. Automating a process with unnecessary steps embeds those steps into the automation — making them faster but not removing the waste. Removing the three unnecessary approval steps first, then automating, produces a faster and cleaner pipeline.
- *Why A is incorrect:* Automating all steps including unnecessary ones would make the process faster but would still include the waste. The principle's insight is that automation without optimization does not fully realize the benefits of automation.
- *Why C is incorrect:* Adding more manual steps contradicts both halves of the principle — neither optimization (which seeks to remove waste) nor automation (which seeks to reduce manual intervention) calls for more manual steps.
- *Why D is incorrect:* The "Optimize and Automate" principle applies across all ITIL 4 practices, including deployment pipelines, change management workflows, incident triage, and any other repeatable process. It is not limited to infrastructure provisioning.

---

### Question 8

Which of the following best describes a "watermelon release" in the context of post-implementation review?

- A) A release that is delayed multiple times but ultimately succeeds when deployed.
- B) A release where all deployment metrics show green (on time, no incidents) but post-deployment monitoring reveals hidden service degradation that was not measured during deployment.
- C) A release that includes both front-end and back-end changes bundled together.
- D) A release that uses both blue-green and canary deployment approaches simultaneously.

**Correct Answer:** B) A watermelon release appears green on the surface but conceals hidden problems — analogous to the ITIL 4 watermelon SLA concept applied to release outcomes.

**Distractor Analysis:**

- *Why B is correct:* Borrowing from the "watermelon SLA" concept in ITIL 4's Service Level Management practice, a watermelon release shows green deployment metrics (on schedule, no deployment incidents, release notes complete) while masking service quality problems — elevated error rates, degraded performance, or user experience issues — that only become visible through post-deployment monitoring and user feedback. The PIR is designed to surface these hidden outcomes.
- *Why A is incorrect:* A delayed release that ultimately succeeds is simply a late release. It does not have the specific characteristic of appearing green while concealing quality issues.
- *Why C is incorrect:* Bundling front-end and back-end changes is a release scoping decision — it has no connection to the watermelon concept.
- *Why D is incorrect:* Combining deployment approaches is a deployment architecture decision. The watermelon concept refers to the mismatch between visible metrics and actual outcomes, not deployment approach combination.

---

### Question 9

Release notes are described as serving multiple audiences simultaneously. Which combination correctly matches the audience to what they need from release notes?

- A) End users need rollback instructions; operations staff need a summary of new features; the change record needs escalation contact information.
- B) End users need to know what changed in the service they use; operations staff need deployment steps, configuration changes, and rollback instructions; the change record needs version, date, and a complete list of changes for future investigation.
- C) End users need database schema diagrams; operations staff need marketing materials; the change record needs customer satisfaction surveys.
- D) All audiences need identical information — release notes should not be segmented by audience.

**Correct Answer:** B) Each audience has distinct information needs from release notes.

**Distractor Analysis:**

- *Why B is correct:* Release notes serve three distinct audiences with different needs. End users want to know what changed in the service they rely on — new features, known limitations, anything that affects their daily work. Operations staff need technical detail — what was deployed, what changed in configuration, what to do if something breaks, and the rollback procedure. The change record needs a permanent, auditable record — version, date, components changed — to support incident investigation and compliance audits months or years later.
- *Why A is incorrect:* This scrambles the audience-content mapping. Rollback instructions belong to operations staff, not end users. New feature summaries belong to end users, not just operations. This mismatch would result in unusable release notes for all three audiences.
- *Why C is incorrect:* Database schema diagrams, marketing materials, and customer satisfaction surveys are not components of release notes. This answer describes completely different document types.
- *Why D is incorrect:* ITIL 4 emphasizes fit-for-purpose communication. Identical release notes for all audiences would either overwhelm end users with technical detail or deprive operations staff of the information they need. Audience segmentation is a quality characteristic of good release notes.

---

### Question 10

A post-implementation review conducted two weeks after a major release identifies three recurring patterns across the last four releases: deployment plans consistently underestimate database migration time, rollback procedures are written but never tested before deployment, and release notes regularly omit post-deployment verification steps. According to ITIL 4, what is the appropriate next step for these findings?

- A) Dismiss the findings as minor operational issues that do not warrant formal action.
- B) Document the findings in the Continual Improvement Register and assign owners to develop specific improvements to the deployment planning template, rollback testing procedure, and release note standard.
- C) Immediately cancel all pending releases until a complete deployment process audit is conducted.
- D) Assign blame to the release managers responsible for the last four releases and require remedial training.

**Correct Answer:** B) PIR findings feed the Continual Improvement Register with specific, actionable improvement items assigned to owners.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4's Continual Improvement practice uses the Continual Improvement Register to track improvement opportunities identified across all practices. PIR findings are a primary input. Each recurring pattern identified — underestimated database migration time, untested rollback procedures, incomplete release notes — becomes a named improvement item with a specific action, an owner, and a target date. This is how organizations systematically improve rather than repeating the same mistakes.
- *Why A is incorrect:* Three recurring patterns across four consecutive releases are systemic issues, not minor anomalies. Dismissing them means accepting continued risk to every future deployment. ITIL 4's Continual Improvement philosophy explicitly rejects this approach.
- *Why C is incorrect:* Canceling all pending releases is disproportionate and harmful to the business. The findings describe process quality issues, not evidence of imminent catastrophic failure. The appropriate response is targeted improvement, not suspension of all activity.
- *Why D is incorrect:* ITIL 4 emphasizes blameless improvement. The identified patterns are process failures, not individual failures. Assigning blame to individual release managers without addressing the underlying process deficiencies would not prevent recurrence and would harm the culture needed for honest PIR participation.
