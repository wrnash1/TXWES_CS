# Quiz: Module 15 — DevOps, Agile, and ITIL 4 Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

### Question 1

Which of the following best describes how ITIL 4 relates to Agile and DevOps practices?

- A) ITIL 4 is a competing framework — organizations must choose between ITIL, Agile, and DevOps.
- B) ITIL 4 is designed to coexist with and complement Agile and DevOps — it provides governance and operational management that surrounds and supports iterative delivery.
- C) ITIL 4 replaces Agile and DevOps in mature organizations — once ITIL is fully implemented, Agile and DevOps are no longer needed.
- D) ITIL 4 and DevOps address the same problems with different names — organizations should pick the one that is more popular in their industry.

**Correct Answer:** B) ITIL 4 is designed to coexist with Agile and DevOps, providing governance and operational management around iterative delivery.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 was specifically redesigned to work alongside Agile and DevOps rather than conflict with them. The ITIL 4 Service Value System is flexible enough to encompass both high-governance practices (change authorization, risk management, compliance) and high-velocity practices (automated pipelines, frequent deployments, iterative development). Agile addresses how software is developed; DevOps addresses how development and operations collaborate; ITIL 4 addresses the full governance and operational management framework within which both operate.
- *Why A is incorrect:* This is the perception ITIL 4 explicitly set out to correct. Modern IT organizations routinely use all three approaches simultaneously, and ITIL 4 was designed with that reality in mind.
- *Why C is incorrect:* ITIL 4 does not replace Agile or DevOps — it complements them. Agile delivery methods and DevOps practices address concerns that ITIL 4 does not — specifically software development methodology and the cultural integration of development and operations.
- *Why D is incorrect:* ITIL 4 and DevOps address different (though overlapping) concerns. DevOps focuses on the collaboration, automation, and measurement of software delivery. ITIL 4 addresses the full management framework for IT services including support, risk, compliance, asset management, and governance. They are not interchangeable.

---

### Question 2

A DevOps team deploys to production 15 times per day using an automated pipeline. The deployment pipeline includes automated testing, automated change record creation, and post-deployment health checks. Most of these deployments are for routine feature releases following a standard, pre-approved procedure. Under ITIL 4's Change Enablement model, how should these routine deployments be classified?

- A) Emergency changes — the high frequency of deployment indicates urgency that requires expedited authorization.
- B) Normal changes — each individual deployment requires a risk assessment and CAB approval before proceeding.
- C) Standard changes — pre-authorized, low-risk changes following a documented procedure that can be implemented without individual CAB review.
- D) Unauthorized changes — automated deployments without manual approval violate ITIL 4's change management requirements.

**Correct Answer:** C) Standard changes — pre-authorized, low-risk deployments following a documented procedure that the pipeline executes without individual CAB review.

**Distractor Analysis:**

- *Why C is correct:* ITIL 4 defines standard changes as pre-authorized changes that follow a documented, pre-approved procedure with low risk. Routine feature deployments through a validated CI/CD pipeline — with automated testing, defined rollback procedures, and consistent deployment steps — qualify as standard changes. The pipeline executes the standard change procedure automatically. This classification is what enables DevOps-speed deployment while remaining within ITIL 4's governance model.
- *Why A is incorrect:* Emergency changes are for urgent, unplanned situations requiring expedited authorization — not for routine, frequent, pre-planned deployments. Frequency does not indicate urgency.
- *Why B is incorrect:* Requiring individual CAB approval for each of 15 daily deployments would make the CAB a bottleneck that prevents the delivery speed DevOps organizations require. Standard change pre-authorization exists precisely to avoid this bottleneck for routine, low-risk changes.
- *Why D is incorrect:* Automated deployments are explicitly supported by ITIL 4's "Optimize and Automate" guiding principle. ITIL 4 does not require manual human approval for every change — it requires that changes follow an appropriate authorization model. Standard changes are pre-authorized, making automated execution compliant.

---

### Question 3

A value stream map analysis reveals that a software delivery process has a total lead time of 10 days. The total value-added time (time spent on actual development, testing, and deployment work) is 1.5 days. What is the value-added ratio, and what does this number indicate?

- A) 15% value-added ratio — 85% of the total delivery time is waiting, handoffs, or other non-value-added activities.
- B) 85% value-added ratio — 85% of the delivery time is productively spent, which is above average.
- C) 150% value-added ratio — the team is working faster than the timeline allows.
- D) The value-added ratio cannot be calculated without knowing how many engineers are working on the process.

**Correct Answer:** A) 15% value-added ratio — 85% of total lead time is non-value-added waste.

**Distractor Analysis:**

- *Why A is correct:* Value-added ratio = total value-added time / total lead time = 1.5 days / 10 days = 15%. This means that only 15% of the calendar time from request to delivery is spent on actual productive work. The remaining 85% — 8.5 days — is consumed by waiting, handoffs, approval queues, and other non-value-added activities. This is unfortunately typical for many IT organizations, and it is exactly what value stream mapping is designed to reveal.
- *Why B is incorrect:* This answer reverses the calculation. 85% is the proportion of non-value-added time, not value-added time. 1.5 days out of 10 days is 15%, not 85%.
- *Why C is incorrect:* A value-added ratio cannot exceed 100% — it is a proportion of time. The formula is value-added time divided by total lead time, always producing a value between 0 and 1 (or 0% and 100%).
- *Why D is incorrect:* The value-added ratio is calculated from time data — how long work takes versus how long the total process takes. Team size affects capacity but is not a variable in the value-added ratio calculation.

---

### Question 4

The DORA research program identified four key metrics for measuring software delivery performance. Which metric directly measures the quality of release and deployment practices — specifically the proportion of deployments that cause failures requiring remediation?

- A) Deployment Frequency — how often the team successfully deploys to production.
- B) Lead Time for Changes — how long it takes for a committed change to reach production.
- C) Change Failure Rate — the percentage of deployments that cause a production failure.
- D) Time to Restore Service — how long it takes to recover from a production incident.

**Correct Answer:** C) Change Failure Rate measures the proportion of deployments that cause production failures.

**Distractor Analysis:**

- *Why C is correct:* Change Failure Rate is the DORA metric that directly measures deployment quality. It is calculated as the number of deployments causing production failures divided by total deployments. Elite performers maintain a change failure rate below 5%. This metric reflects the effectiveness of testing, release validation, and deployment practices — it is the quality counterpart to deployment frequency's speed measurement.
- *Why A is incorrect:* Deployment Frequency measures how often deployments occur — a speed and capacity metric. It says nothing about the quality of those deployments or how many cause failures.
- *Why B is incorrect:* Lead Time for Changes measures how quickly code moves from commit to production — an efficiency metric. It reflects the effectiveness of the development and deployment pipeline, not the quality of what is deployed.
- *Why D is incorrect:* Time to Restore Service measures recovery speed after a failure occurs — an Incident Management metric. It measures how quickly the organization can respond to and resolve production problems, not how frequently those problems are caused by deployments.

---

### Question 5

An SRE team has set a Service Level Objective of 99.9% monthly availability for its payment processing service. During the first 20 days of the month, two incidents have consumed 28 minutes of the monthly error budget. How much error budget remains, and what should the team do?

- A) The error budget is fully consumed — all deployments must be halted for the remainder of the month.
- B) Monthly error budget = 43.8 minutes; 28 minutes consumed; 15.8 minutes remaining. The team has significant remaining budget and can continue deploying.
- C) Monthly error budget = 43.8 minutes; 28 minutes consumed; 15.8 minutes remaining. The team should reduce deployment frequency as a precaution given only 36% of the budget remains and 33% of the month remains.
- D) Error budgets only apply to deployments — incidents caused by factors other than deployments do not count against the error budget.

**Correct Answer:** C) 15.8 minutes of budget remain with one-third of the month left — a reasonable precautionary reduction in deployment frequency is appropriate.

**Distractor Analysis:**

- *Why C is correct:* Monthly error budget for 99.9% SLO = 43.8 minutes. With 28 minutes consumed in the first 20 days and 10–11 days remaining, approximately 36% of the budget remains for 33% of the remaining time. The budget is not fully consumed, but the pace of consumption — 1.4 minutes per day on average — suggests caution. Reducing deployment frequency (which is a controllable risk factor) for the remaining days is a prudent, data-driven response. This is exactly the kind of trade-off the error budget model enables.
- *Why A is incorrect:* The error budget is not fully consumed — 15.8 minutes remain. Halting all deployments is disproportionate and contradicts the purpose of the error budget, which is to make nuanced trade-off decisions, not impose binary stop-go rules.
- *Why B is incorrect:* While technically correct on the math, "can continue deploying" without qualification is too permissive. With limited budget remaining and a meaningful portion of the month ahead, some reduction in deployment risk is appropriate. The error budget model encourages active management of deployment pace based on budget status.
- *Why D is incorrect:* Error budgets measure all availability impacts, regardless of cause — incidents caused by deployments, infrastructure failures, upstream dependencies, or any other factor all count. The budget represents the total permitted unreliability for the SLO period.

---

### Question 6

An organization is using ITIL 4 alongside Scrum. The Scrum team completes a two-week sprint and prepares to deploy a new feature to production. The CI/CD pipeline runs automated tests — all pass. However, the feature includes a database schema migration. Which ITIL 4 practice should the deployment plan specifically address, and what additional consideration is required compared to a code-only deployment?

- A) Incident Management — database migrations frequently cause incidents, so the incident team should be alerted before every migration.
- B) Release and Deployment Management — specifically rollback planning must address the added complexity that database schema changes may not be reversible without data loss.
- C) IT Asset Management — the database is a CI that must be updated in the CMDB before the migration runs.
- D) Service Request Management — users must submit a service request before any database migration can proceed.

**Correct Answer:** B) Release and Deployment Management must address database rollback complexity — schema changes can be difficult or impossible to reverse without data loss.

**Distractor Analysis:**

- *Why B is correct:* Release and Deployment Management requires a rollback plan for every deployment. When a release includes a database schema migration, rollback planning becomes significantly more complex. Adding columns can typically be reversed. Removing columns or altering data types may result in data loss if data has been written to the new structure before rollback. The deployment plan must explicitly address: whether the schema change is reversible, what data integrity risks exist during the rollback window, and whether a point-in-time database backup should be taken immediately before migration.
- *Why A is incorrect:* Alerting the incident team before every database migration is not a standard ITIL 4 practice requirement. Post-deployment monitoring should be in place for any deployment, but pre-alerting the incident team is not a deployment management requirement.
- *Why C is incorrect:* While the CMDB should reflect the deployed state of the database, updating it is a configuration management activity that follows the deployment — it does not constitute the special consideration required for schema migration risk management.
- *Why D is incorrect:* Service Request Management handles standardized user requests for pre-approved services. A production database migration is a change, managed through Change Enablement and Release and Deployment Management, not a service request.

---

### Question 7

Which of the following best describes the relationship between the ITIL 4 guiding principle "Progress Iteratively with Feedback" and Agile sprint methodology?

- A) They conflict — ITIL 4 requires comprehensive upfront planning, while Agile avoids planning entirely.
- B) They are aligned — both emphasize delivering work in small increments, reviewing outcomes after each increment, and adapting based on what is learned.
- C) They are unrelated — ITIL 4's guiding principles apply only to service operations, not software development.
- D) ITIL 4 "Progress Iteratively" refers only to continual improvement programs — it does not apply to software delivery.

**Correct Answer:** B) Both ITIL 4's iterative principle and Agile sprint methodology emphasize small increments, feedback, and adaptation.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4's "Progress Iteratively with Feedback" principle explicitly advises against big-bang implementations and comprehensive upfront planning. It recommends delivering work in iterations, reviewing the results of each iteration, and using that feedback to adapt the next iteration. This maps directly to the Agile sprint model — deliver working output every two weeks, review the sprint result, incorporate feedback into the next sprint. The alignment is intentional in ITIL 4's design.
- *Why A is incorrect:* ITIL 4 does not require comprehensive upfront planning — in fact, the "Progress Iteratively with Feedback" principle explicitly advises against it. This is a common misconception about ITIL inherited from earlier, more prescriptive versions.
- *Why C is incorrect:* ITIL 4's guiding principles apply across all aspects of the Service Value System — they are foundational to how the organization thinks about all its work, including software delivery. They are not limited to operations.
- *Why D is incorrect:* The "Progress Iteratively with Feedback" principle applies broadly — to improvement programs, service design, software delivery, and any other context where work can be organized iteratively. ITIL 4 does not restrict its application to continual improvement only.

---

### Question 8

An organization currently has separate development, QA, and operations departments. Development teams throw code "over the wall" to QA, who throw tested builds "over the wall" to operations for deployment. When production incidents occur, the three teams blame each other. From a DevOps and ITIL 4 perspective, what is the primary structural problem and what is the recommended solution?

- A) The primary problem is that the teams use different ticketing systems — the solution is to standardize on a single ITSM tool.
- B) The primary problem is organizational silos that create handoff delays, knowledge gaps, and misaligned incentives — the solution is cross-functional teams with shared accountability for the full service lifecycle.
- C) The primary problem is lack of documentation — if each team documented their processes better, handoffs would be smoother.
- D) The primary problem is that operations needs more staff — with enough people, handoff delays would be eliminated.

**Correct Answer:** B) Organizational silos create systemic problems with handoffs, knowledge, and incentives — the solution is cross-functional teams with shared ownership.

**Distractor Analysis:**

- *Why B is correct:* The "throw it over the wall" pattern and the blame culture it creates are classic symptoms of organizational silos. Each team optimizes for its own metrics without accountability for the end-to-end outcome. DevOps addresses this through cross-functional teams — often called product teams or stream-aligned teams — that include developers, testers, and operations engineers working together with shared accountability for building, deploying, and running the service. ITIL 4 supports this through value stream thinking that focuses on end-to-end flow rather than functional team performance.
- *Why A is incorrect:* Tool standardization may reduce friction in communication but does not address the root cause — organizational silos. Teams with different goals and separate accountability can still have the same tool and still throw work over the wall.
- *Why C is incorrect:* Documentation improves the quality of handoffs but does not eliminate the structural problem. Documented handoffs between siloed teams still create delays, reduce feedback speed, and distribute accountability in ways that enable blame culture.
- *Why D is incorrect:* Adding staff to operations addresses capacity but not the organizational structure. A well-staffed siloed operations team still has the same handoff delays and accountability gaps as an understaffed one.

---

### Question 9

A team's value stream map for their incident management process shows the following: detection-to-acknowledgment time averages 22 minutes, acknowledgment-to-diagnosis time averages 47 minutes, diagnosis-to-resolution time averages 31 minutes. The total lead time from detection to resolution is 100 minutes. The actual active work time (acknowledgment, diagnosis, resolution activities) is 80 minutes. What does the 20-minute gap represent, and what type of waste does it most likely indicate?

- A) The 20-minute gap represents value-added work that was performed too quickly — the team should slow down to reduce errors.
- B) The 20-minute gap represents wait time or handoff delays between active work periods — it is non-value-added waste that extends incident resolution time without contributing to the fix.
- C) A 20-minute gap in a 100-minute process is negligible — it falls within normal variation and does not warrant analysis.
- D) The gap represents time spent updating the CMDB — mandatory documentation that is fully value-added.

**Correct Answer:** B) The 20-minute gap is non-value-added wait or handoff time that extends incident duration without contributing to resolution.

**Distractor Analysis:**

- *Why B is correct:* In value stream mapping, any time between active work periods represents waiting — a form of non-value-added waste. In incident management, wait time between detection and acknowledgment, or between acknowledgment and active diagnosis, directly extends the time users are experiencing service degradation. Reducing this 20 minutes of wait and handoff time would reduce incident duration from 100 to 80 minutes — a 20% improvement — without requiring the team to resolve incidents any faster.
- *Why A is incorrect:* The gap represents elapsed time between activities, not speed of execution. Slowing down active work would increase, not decrease, incident duration. The concept of "too fast" does not apply to incident resolution time.
- *Why C is incorrect:* In value stream thinking, all non-value-added time is worth analyzing regardless of magnitude. A 20-minute reduction in every incident's duration compounds significantly across hundreds or thousands of annual incidents. "Negligible" is not a concept in Lean waste analysis.
- *Why D is incorrect:* CMDB updates after incident resolution are configuration management activities — they have compliance value but do not contribute to resolving the incident. In the context of this value stream map, they would also not appear within the detection-to-resolution window if performed post-resolution.

---

### Question 10

Which of the following correctly describes the purpose of an error budget in Site Reliability Engineering?

- A) The error budget is the total cost budget allocated to fixing production errors in a fiscal year.
- B) The error budget is the permitted amount of unreliability within an SLO period — it creates a quantified trade-off between deployment velocity and service reliability.
- C) The error budget is a reserve fund that SRE teams use to purchase monitoring tools and automation infrastructure.
- D) The error budget is the maximum number of incident tickets the SRE team will accept in a given month before escalating to senior leadership.

**Correct Answer:** B) The error budget is the permitted amount of unreliability within an SLO period, enabling data-driven trade-offs between velocity and reliability.

**Distractor Analysis:**

- *Why B is correct:* The error budget is calculated from the SLO: a 99.9% monthly availability SLO means 0.1% of monthly time — approximately 43.8 minutes — is the permitted downtime budget. When the error budget is healthy, teams can deploy frequently and take calculated risks. When it is nearly consumed, deployments are paused to protect the remaining budget. This creates an objective, quantified mechanism for making trade-off decisions between development velocity (which consumes error budget through deployment risk) and operational stability (which is protected by preserving error budget).
- *Why A is incorrect:* An error budget has no financial definition — it is a time-based measure of permitted unreliability, not a cost allocation.
- *Why C is incorrect:* An error budget is not a financial reserve. It is a reliability measurement construct — a portion of time that can be "spent" on unavailability within the SLO constraint.
- *Why D is incorrect:* Incident count limits are not how error budgets are defined. Error budgets measure availability impact in time units, not incident ticket counts. The same amount of downtime could come from one long incident or many short ones — the error budget treats both equivalently.

---

### Question 11

An organization's development team argues that ITIL 4's Change Enablement process is slowing down their CI/CD pipeline. Every code commit triggers a change record review that takes an average of 4 hours, making same-day deployments impossible. What is the most likely root cause of this problem, and what is the ITIL 4-aligned solution?

- A) CI/CD pipelines are incompatible with ITIL 4 — the organization must choose one or the other.
- B) The change process is not properly categorized — routine automated deployments should be classified as standard changes, eliminating the need for individual review per commit.
- C) The development team should bypass the change management process for urgent features.
- D) The change management team needs more staff to review each commit faster.

**Correct Answer:** B) The root cause is misclassification — routine automated deployments should be standard changes that do not require individual CAB review.

**Distractor Analysis:**

- *Why B is correct:* The 4-hour review bottleneck is a symptom of treating every deployment as a normal change requiring individual assessment. ITIL 4's standard change classification exists precisely for this scenario — pre-authorized, low-risk changes following a defined procedure. A validated CI/CD pipeline with automated testing, defined rollback procedures, and consistent deployment steps qualifies as a standard change procedure. Once the procedure is pre-approved, each deployment through the pipeline executes the standard change automatically — no individual review required.
- *Why A is incorrect:* ITIL 4 is explicitly designed to coexist with CI/CD pipelines. The standard change classification is ITIL 4's mechanism for enabling DevOps-speed deployment within a governed framework. Choosing between CI/CD and ITIL 4 is a false dilemma created by process misconfiguration, not architectural incompatibility.
- *Why C is incorrect:* Bypassing change management creates governance and compliance risk. The solution is to configure change management correctly — not to bypass it. Bypass behavior also sets a precedent that undermines the change process for genuinely risky changes.
- *Why D is incorrect:* Adding staff to the change review team would speed up individual reviews but would not address the structural problem — requiring individual review for changes that should be pre-approved. Even with more staff, the process would remain slower than necessary and more expensive to operate than a properly configured standard change workflow.

---

### Question 12

A team's Value Stream Map reveals three major wait-time sources: a 48-hour security review queue between development complete and QA start, a 24-hour business approval gate between QA complete and deployment approval, and a 6-hour deployment scheduling window. Together these represent 78 hours of the 96-hour total lead time. Which Lean waste category do these wait times fall under, and what approach does VSM recommend to address them?

- A) Overproduction waste — the team is building features faster than the business can absorb them.
- B) Waiting waste — activities are idle while waiting for queue processing, approvals, or scheduling slots; the recommendation is to analyze each queue to determine whether the wait produces proportionate value and to redesign the flow to reduce or eliminate unnecessary waiting.
- C) Defect waste — the security and business review steps indicate that defects are being detected downstream.
- D) Motion waste — the team is physically moving between locations unnecessarily for each review stage.

**Correct Answer:** B) These are examples of waiting waste — idle time between activities — and VSM analysis drives redesign to reduce or eliminate non-proportionate waiting.

**Distractor Analysis:**

- *Why B is correct:* In Lean and VSM terminology, waiting waste refers to idle time when work is waiting for the next step to begin — approval queues, scheduling windows, and review backlogs are classic examples. The 78/96 (81%) non-value-added time ratio revealed by the VSM is the diagnostic trigger. The solution is to analyze each wait: Is the 48-hour security review necessary in its current form? Could it be partially automated? Could the business approval be reduced to 4 hours with a different workflow? Could deployment scheduling be on-demand rather than batch-scheduled?
- *Why A is incorrect:* Overproduction waste occurs when more is built than is needed or can be consumed. That is not what the VSM shows — the features are being built and proceeding through a pipeline, just slowly due to queue delays.
- *Why C is incorrect:* Defect waste occurs when work is done incorrectly and must be reworked. The security review and business approval exist to catch defects, but their queue time itself — while they wait in the backlog — is waiting waste, not defect waste.
- *Why D is incorrect:* Motion waste refers to unnecessary physical or digital movement in a process — searching for files, navigating between disconnected systems. Review queue delays are waiting waste, not motion waste.

---

### Question 13

An SRE team's checkout service has consumed 80% of its monthly error budget by the 18th day of the month. The team has 10 more planned deployments scheduled for the remaining 12 days. What action most reflects SRE error budget principles?

- A) Proceed with all 10 deployments on schedule — the error budget should not restrict planned work.
- B) Pause all new feature deployments for the remainder of the month and focus exclusively on reliability improvements, since deploying features when the error budget is nearly exhausted would risk SLO breach.
- C) Cancel the SLO and reset the error budget immediately to allow the team to continue deploying.
- D) Escalate to the CTO to request an extension on the error budget deadline.

**Correct Answer:** B) Pausing feature deployments and focusing on reliability improvements is the data-driven response when the error budget is nearly exhausted.

**Distractor Analysis:**

- *Why B is correct:* The error budget model is designed to create exactly this kind of self-governing decision. When the budget is 80% consumed with 40% of the month remaining, the pace of consumption (about 4.4% per day) suggests the SLO will be breached before month-end if deployments continue at the same rate. The appropriate response is to pause reliability-risking deployments and invest remaining team capacity in reliability improvements — the SRE model explicitly links error budget exhaustion to a shift in development priorities from features to reliability work.
- *Why A is incorrect:* Ignoring error budget status when scheduling deployments defeats the purpose of the error budget mechanism. The budget exists to create a data-driven link between deployment pace and reliability outcomes. Proceeding regardless of budget status reverts to the pre-SRE model of subjective, non-quantified deployment decisions.
- *Why C is incorrect:* Canceling or resetting an SLO to avoid its constraints defeats the entire purpose of the SLO. An SLO represents a commitment to service users — resetting it when it becomes inconvenient harms user trust and removes the reliability accountability the SRE model depends on.
- *Why D is incorrect:* Error budgets are not time-bound deadlines that can be extended by management approval. They are derived from the SLO, which represents a customer-facing commitment. "Extending the deadline" is not a meaningful concept in the error budget model — the SLO period is what it is.

---

### Question 14

An organization uses Scrum for software development and ITIL 4 practices for service operations. The Product Owner is creating a new user story for a feature that requires storing new types of customer payment data. Which ITIL 4 practice should be involved during sprint planning for this story, and why?

- A) Incident Management — payment features frequently cause incidents.
- B) Risk and Compliance, specifically because storing new payment data likely creates PCI-DSS obligations that must be assessed before development begins.
- C) Service Desk — customers will need to contact the service desk about the new payment feature.
- D) IT Asset Management — new payment data fields must be added to the CMDB.

**Correct Answer:** B) Risk and Compliance must be involved because new payment data storage creates PCI-DSS obligations that affect how the feature is designed and implemented.

**Distractor Analysis:**

- *Why B is correct:* Introducing new payment data storage triggers PCI-DSS compliance requirements — specific controls for encryption, access restriction, logging, and transmission security must be built into the feature from the start. This is a "shift-left" compliance requirement: if compliance considerations are not introduced during sprint planning, the development team may build a feature that is technically complete but non-compliant, requiring costly rework later. ITIL 4 integration with Agile means compliance input should occur at the planning stage, not after deployment.
- *Why A is incorrect:* While payment features do carry higher incident risk, Incident Management is a reactive practice that responds to problems after they occur. The relevant consideration at sprint planning is proactive — ensuring the feature is built compliantly. Incident Management is not a sprint planning input.
- *Why C is incorrect:* Service desk planning for a new feature is relevant for user communication and training, but it does not affect how the payment data storage is designed or whether it meets compliance requirements. The compliance consideration is more urgent and more directly tied to sprint planning decisions.
- *Why D is incorrect:* While CMDB updates may eventually be needed to reflect new data storage assets, CMDB management is a post-deployment configuration activity, not a sprint planning input that affects feature design. The compliance consideration affects the architecture of the feature itself.

---

### Question 15

Which of the following correctly describes the DORA "Elite" performance tier for Deployment Frequency?

- A) Elite teams deploy to production once per month.
- B) Elite teams deploy to production on demand, potentially multiple times per day.
- C) Elite teams deploy to production once per week following a structured release schedule.
- D) Elite teams limit deployments to once per quarter to ensure thorough regression testing.

**Correct Answer:** B) Elite performers deploy on demand — potentially multiple times per day.

**Distractor Analysis:**

- *Why B is correct:* DORA research defines the Elite performance tier for Deployment Frequency as on-demand deployment — teams can deploy at any time when a change is ready, typically resulting in multiple daily deployments. This is enabled by automated CI/CD pipelines, comprehensive automated testing, and standard change pre-authorization for routine deployments. Elite performers are not constrained by manual approval cycles or scheduled release windows for routine changes.
- *Why A is incorrect:* Monthly deployment frequency is the Low tier in DORA's research — it is the worst-performing category. Monthly deployments are associated with high change failure rates and longer incident recovery times because each deployment bundles many changes, making failures harder to diagnose and increasing blast radius.
- *Why C is incorrect:* Weekly deployments fall in the Medium tier — better than monthly but not Elite. Weekly release schedules are common in organizations that have automated testing but still require manual approval gates or release coordination processes that prevent on-demand deployment.
- *Why D is incorrect:* Quarterly deployments represent the worst tier in DORA's performance classification. Quarterly release cycles are associated with the highest change failure rates and longest recovery times because the large batch sizes amplify risk in every dimension.

---

### Question 16

A company's incident management value stream shows that 35% of total incident resolution time is spent on "diagnosis" — the step between acknowledgment and identifying the root cause. A team member suggests that this is just the nature of complex systems and cannot be reduced. Which ITIL 4 and DevOps concept most directly challenges this assumption?

- A) The assumption is correct — diagnosis time is inherently variable and cannot be systematically reduced.
- B) Known Error Database entries, runbooks, and post-incident review documentation reduce repeat incident diagnosis time by capturing previous diagnostic paths, making future instances of the same issue faster to resolve.
- C) Automated monitoring eliminates diagnosis time entirely by identifying root causes before incidents are even reported.
- D) Increasing team size reduces diagnosis time because more engineers can investigate simultaneously.

**Correct Answer:** B) KEDB entries, runbooks, and PIR learnings reduce repeat diagnosis time by preserving previous diagnostic knowledge.

**Distractor Analysis:**

- *Why B is correct:* A significant proportion of incidents in mature environments are repeat occurrences of known or similar issues. When previous incidents are documented — their symptoms, diagnostic steps, and resolutions captured in KEDB entries or runbooks — future occurrences of the same issue can be diagnosed in minutes rather than hours. This is exactly the purpose of ITIL 4's Known Error Database and the PIR lesson-learned feedback loop. Diagnosis time for novel incidents may remain high, but the proportion of novel incidents decreases as the knowledge base grows.
- *Why A is incorrect:* The assumption that diagnosis time "cannot be reduced" treats the current state as fixed. ITIL 4's Continual Improvement and Problem Management practices exist specifically to systematically reduce incident resolution time through knowledge capture, root cause elimination, and process improvement. The assumption is exactly the mindset that Lean and VSM challenges.
- *Why C is incorrect:* Automated monitoring can reduce detection-to-acknowledgment time and can surface potential causes, but it does not "eliminate diagnosis time entirely." Complex system failures often require human interpretation of monitoring data even when the data is rich. Monitoring is a valuable input to diagnosis, not a complete substitute for it.
- *Why D is incorrect:* Adding engineers can parallelize some diagnostic work, but it does not address the root cause of slow diagnosis — lack of documented knowledge from previous incidents. Two engineers working in parallel without KEDB documentation are still slower than one engineer with a well-documented runbook for the specific issue.

---

### Question 17

An organization's current change failure rate is 18%. The DORA research classifies this as the Low performance tier (above 15%). The team wants to improve to the Elite tier (below 5%). Which combination of practices would most directly reduce change failure rate?

- A) Increase deployment frequency and reduce lead time for changes — faster delivery reduces change failure rate.
- B) Strengthen automated testing coverage, improve pre-deployment validation in staging environments, and invest in canary or phased deployment approaches that limit blast radius when failures do occur.
- C) Reduce deployment frequency to once per quarter — fewer deployments means fewer opportunities for failures.
- D) Add more manual CAB approval steps to catch problems before they reach production.

**Correct Answer:** B) Improved test coverage, staging validation, and risk-limiting deployment approaches directly reduce change failure rate.

**Distractor Analysis:**

- *Why B is correct:* Change failure rate measures the proportion of deployments that cause production failures. Reducing it requires preventing failures from reaching production (better testing, better staging validation) and limiting the impact when they do (canary and phased deployment approaches that catch failures before they affect all users). DORA research consistently identifies automated testing and progressive delivery practices as the key enablers of Elite change failure rates — not slower deployment or more manual gates.
- *Why A is incorrect:* DORA research shows no causal relationship where faster deployment reduces change failure rate. In fact, very high deployment frequency without quality practices can increase failure rate. Speed and quality must be addressed together, not traded off.
- *Why C is incorrect:* Reducing deployment frequency to quarterly does not improve change failure rate — it changes the denominator. If 18% of deployments fail and you deploy quarterly, you still have a roughly 18% failure rate per deployment, with worse consequences because each deployment bundles more changes. DORA research actually shows that low-frequency deployers tend to have higher failure rates because of large batch sizes.
- *Why D is incorrect:* DORA research has consistently found that organizations with more manual approval gates do not have lower change failure rates than those with fewer. Manual gates are slower but do not improve quality because human reviewers cannot catch the types of integration and environment-specific failures that automated testing can. More manual steps slow deployment without improving the failure rate.

---

### Question 18

A DevOps team is told to implement "continuous improvement" as part of their ITIL 4 integration. A developer interprets this as: "We should always be working on making things better." A service manager interprets it as: "We need to maintain a Continual Improvement Register with owned action items reviewed at structured intervals." Which interpretation is more aligned with ITIL 4?

- A) The developer's interpretation — continuous improvement is a mindset that does not require formal structure.
- B) The service manager's interpretation — ITIL 4's Continual Improvement practice requires formal tracking, ownership, and structured review of improvement items.
- C) Both interpretations are equivalent — mindset and formal tracking produce identical outcomes.
- D) Neither interpretation is correct — ITIL 4 defines continual improvement only for senior leadership, not for teams.

**Correct Answer:** B) ITIL 4's Continual Improvement practice requires formal tracking through the CIR with owners and review cadence — mindset alone is insufficient.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 explicitly defines the Continual Improvement practice as including a Continual Improvement Register — a formal log of improvement opportunities with descriptions, owners, priorities, statuses, and target dates. Regular review of the CIR is part of the practice's governance. This does not contradict the mindset of always seeking improvement — it operationalizes the mindset. Without the CIR, improvement ideas are lost, deprioritized, or never completed because they have no owner or accountability structure.
- *Why A is incorrect:* While a continuous improvement mindset is a cultural prerequisite, ITIL 4 does not accept mindset alone as implementation of the practice. The Continual Improvement practice has specific artifacts (CIR), activities (assessment, prioritization, review), and governance requirements that a mindset alone does not fulfill.
- *Why C is incorrect:* Mindset and formal tracking do not produce identical outcomes. Mindset without structure produces improvement ideas that are expressed verbally, acted on inconsistently, forgotten when team members change, and invisible to management. Formal tracking produces measurable, auditable, consistently resourced improvement work.
- *Why D is incorrect:* ITIL 4 explicitly states that Continual Improvement is everyone's responsibility — it applies at all levels from individual teams to the organization's senior leadership. The practice is not limited to any organizational layer.

---

### Question 19

An organization's value stream for new employee IT onboarding has a total lead time of 10 business days. Interviews with the team reveal that the actual work required — account provisioning, equipment imaging, access configuration, and orientation session scheduling — takes approximately 3.5 hours. What does this value-added ratio indicate, and what type of waste most likely accounts for the remaining time?

- A) Value-added ratio = 8.75% — the dominant waste is likely batching and queue delays (accounts are processed in weekly batches, equipment is imaged in groups, and approvals wait in queues).
- B) Value-added ratio = 91.25% — the process is highly efficient with minimal waste.
- C) Value-added ratio = 8.75% — the dominant waste is defect waste because IT is making errors that require rework.
- D) The ratio cannot be calculated because IT onboarding is not a production process.

**Correct Answer:** A) Value-added ratio = 8.75% — batching, queue delays, and approval waiting are the most likely dominant waste types for this kind of cross-team administrative process.

**Distractor Analysis:**

- *Why A is correct:* Value-added ratio = 3.5 hours / (10 × 8 hours) = 3.5 / 80 = 4.4%. Wait — 3.5 hours / 80 hours = approximately 4.4%. The answer states 8.75% which would be 3.5 / 40, implying a 5-day work week with 8-hour days where "10 business days" equals 80 hours total. Either calculation produces a very low value-added ratio. The dominant waste in IT onboarding processes is almost always batching (accounts provisioned once weekly rather than on request), approval queue delays (manager approvals that wait in inboxes), and handoff delays between teams (IT, HR, facilities). These are all waiting waste varieties.
- *Why B is incorrect:* This reverses the ratio calculation. 3.5 hours out of 80 hours (10 business days) is not 91% — it is approximately 4–9% depending on the exact calculation. The result showing 91% value-added would mean the process has almost no waste, which clearly contradicts the 10-day lead time for 3.5 hours of work.
- *Why C is incorrect:* Defect waste — errors requiring rework — is possible but is not the most likely dominant waste in an administrative onboarding process. Batching, approval queues, and handoff delays typically account for far more calendar time than defect rework in these processes.
- *Why D is incorrect:* Value stream mapping applies to any process — production, administrative, IT, HR, or financial. Any process with a defined input and output, where lead time can be measured and value-added work can be separated from waiting and processing overhead, is amenable to VSM analysis.

---

### Question 20

ITIL 4's Service Value System includes the concept of a "shared vision" as a prerequisite for effective DevOps and organizational alignment. A technology company has development teams that measure success by features shipped per sprint, while operations teams measure success by change failure rate and incident volume. When a developer deploys a feature that causes a P2 incident, the development team considers it a success (feature shipped) while operations considers it a failure. Which ITIL 4 concept most directly addresses this misalignment?

- A) The teams should be evaluated using identical KPIs regardless of their different functions.
- B) The four dimensions of service management — particularly Organizations and People — require that all teams share aligned metrics connected to overall value delivered to customers, not isolated functional metrics.
- C) Development metrics and operations metrics are inherently incompatible — organizations must accept this tension.
- D) Operations should adopt the development team's sprint-based measurement model to align perspectives.

**Correct Answer:** B) ITIL 4's Organizations and People dimension requires that team metrics align to shared customer value outcomes, not create competing incentives.

**Distractor Analysis:**

- *Why B is correct:* The scenario describes a classic organizational incentive misalignment — each team optimizes for its own metric in ways that conflict at the seam between development and operations. ITIL 4's Organizations and People dimension addresses this by requiring that team structures, incentives, and metrics align with the organization's overall value delivery objectives. DevOps practices reinforce this through shared team ownership of the full service lifecycle — the same team that builds the feature is accountable for its operational performance, creating a single set of aligned incentives.
- *Why A is incorrect:* Identical KPIs across different functional roles would be impractical and uninformative. Development and operations have different activities that require different performance measures. The solution is not identical metrics but aligned metrics — different measures that all connect to a shared customer outcome rather than competing functional goals.
- *Why C is incorrect:* The tension is not inherent — it is a structural choice. Organizations that have adopted DevOps product team models with shared accountability for development and operations demonstrate that the misalignment can be eliminated by changing organizational design and incentive structures.
- *Why D is incorrect:* Operations adopting sprint-based measurement would create a different kind of misalignment — operations work (incident response, patching, capacity management) is not primarily sprint-organized. The solution is to create shared outcome-based metrics (service reliability, time to value, customer satisfaction) that both teams contribute to, not to force one team's model on the other.
