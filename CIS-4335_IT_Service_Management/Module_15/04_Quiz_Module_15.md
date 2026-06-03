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
