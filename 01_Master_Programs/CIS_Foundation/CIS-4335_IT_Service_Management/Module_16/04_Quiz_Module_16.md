# Quiz: Module 16 — ITIL 4 Foundation Exam Preparation

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Note to Students

This is a 20-question practice quiz that simulates the ITIL 4 Foundation exam format. All questions use the same four-choice multiple-choice format as the actual exam. A score of 13 or higher (65%) indicates readiness. Review all distractor analyses carefully — understanding why wrong answers are wrong is as important as knowing the correct answers.

---

### Question 1

Which of the following correctly defines the purpose of the ITIL 4 Service Value System?

- A) To provide a prescriptive set of processes that all IT organizations must follow to achieve certification.
- B) To describe how all components and activities of an organization work together as a system to enable value creation.
- C) To replace existing IT frameworks — organizations that adopt the SVS should discontinue Agile and DevOps practices.
- D) To define the 34 ITIL 4 practices and specify how each must be implemented.

**Correct Answer:** B) The SVS describes how all components and activities work together as a system to enable value creation.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 defines the SVS as the model that describes how all components and activities of an organization work together as a system to enable value creation. The SVS is not prescriptive about specific processes — it is a flexible system that can accommodate different organizational contexts, including Agile and DevOps approaches.
- *Why A is incorrect:* The ITIL 4 SVS is explicitly not prescriptive in the traditional sense. ITIL 4 moved away from the rigid process prescriptions of earlier versions and toward principles-based guidance. The SVS provides a framework, not a mandatory process set.
- *Why C is incorrect:* ITIL 4 is designed to complement Agile, DevOps, and Lean — not replace them. This is one of the fundamental changes in ITIL 4 compared to earlier versions.
- *Why D is incorrect:* The SVS contains practices as one of its five components, but its purpose is broader than defining practices. The SVS describes the entire system of components that create value — guiding principles, governance, the service value chain, practices, and continual improvement.

---

### Question 2

A service provider delivers a cloud-based project management application. The application performs all required functions reliably and has never had unplanned downtime in six months of operation. However, response times average 8 seconds under peak load, which users find unacceptable. Which dimension of service quality is failing?

- A) Utility — the application does not meet the customer's functional need for project management.
- B) Warranty — the application does not meet agreed requirements for performance and availability.
- C) Value co-creation — the customer is not using the application correctly.
- D) Output — the application is not producing the required tangible deliverables.

**Correct Answer:** B) Warranty — the application fails the "fit for use" standard because performance under load is unacceptable.

**Distractor Analysis:**

- *Why B is correct:* Warranty is the assurance that a service will meet agreed requirements — it covers availability, capacity/performance, security, and continuity. "Fit for use" requires that the service performs adequately under real operating conditions. Eight-second response times under peak load represent a capacity and performance failure — the service is not fit for use even though its functional features work correctly.
- *Why A is incorrect:* Utility (fit for purpose) concerns whether the service has the right functionality to meet the customer's need. The scenario states the application "performs all required functions" — so utility is satisfied. The failure is in operational performance, not functional coverage.
- *Why C is incorrect:* Nothing in the scenario suggests the customer is misusing the application. User dissatisfaction with 8-second response times is a legitimate warranty issue, not a user behavior issue.
- *Why D is incorrect:* Output describes tangible or intangible deliverables of an activity. The application is producing outputs — the question is whether the service meets warranty requirements, not whether it produces outputs.

---

### Question 3

An IT service provider's helpdesk analyst receives a call from a user who cannot log into the company's HR system. The user says the login page is displaying an error message they have never seen before and the issue started 20 minutes ago. How should this be classified under ITIL 4?

- A) Service request — the user is requesting a service from the IT department.
- B) Incident — this is an unplanned interruption to the HR system service.
- C) Problem — the error message indicates an underlying cause that must be investigated.
- D) Change — the error message suggests that a recent change has broken the login functionality.

**Correct Answer:** B) Incident — an unplanned interruption to a service that a user is reporting for restoration.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 defines an incident as an unplanned interruption to or reduction in the quality of a service. This user is experiencing an unplanned inability to access the HR system. Incident Management's purpose is to restore normal service operation as quickly as possible. Classification as an incident triggers the incident response process immediately.
- *Why A is incorrect:* A service request is a pre-defined, planned request from a user for something to be provided — such as access provisioning, a password reset, or a software installation. An unexpected system error preventing login is not a pre-planned service request; it is an unplanned interruption.
- *Why C is incorrect:* Problem Management identifies root causes of incidents. The immediate priority when a user cannot log in is incident resolution — restoring access. Problem investigation may follow if the incident is part of a pattern, but the first classification is incident.
- *Why D is incorrect:* While the error could have been caused by a recent change, that is a hypothesis, not a confirmed classification. The ticket is classified based on what it is — an unplanned interruption — not based on its potential cause. Change investigation may occur within problem management if a change is found to be the root cause.

---

### Question 4

A Problem Manager has identified the root cause of a recurring database timeout issue and has developed a script that reduces timeout frequency by 85% while the permanent fix is being developed. The permanent fix requires a major change that will take eight weeks to complete. What term describes the current state of this problem?

- A) Incident — the problem is still causing service interruptions and must be managed as an active incident.
- B) Known error — the root cause has been identified and a workaround is available, but the permanent fix has not yet been implemented.
- C) Resolved problem — the workaround has reduced the impact sufficiently to close the problem record.
- D) Standard change — the script that reduces timeout frequency qualifies as a standard change to the problem.

**Correct Answer:** B) Known error — root cause identified, workaround available, permanent fix pending.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 defines a known error as a problem that has been analyzed and has a documented root cause and a workaround. The key characteristics are all present: root cause identified (database timeout mechanism), workaround in place (the script that reduces frequency by 85%), and permanent fix not yet implemented. The known error record is maintained and managed until the permanent fix is deployed.
- *Why A is incorrect:* Incidents and problems are separate records. The database timeout incidents may continue at reduced frequency, but the problem record has advanced beyond the investigation phase. Active incidents would be managed under Incident Management; this problem has been classified at the known error stage.
- *Why C is incorrect:* A problem is not resolved until the root cause is permanently addressed. Having a workaround does not close the problem — it advances it to known error status. Closing the problem record prematurely would eliminate the tracking mechanism for the permanent fix.
- *Why D is incorrect:* A standard change is a pre-authorized change that follows a documented procedure. The script is a workaround for a known error — it is part of Problem Management's error control activities, not a change classification.

---

### Question 5

An organization's SLA with its primary customer commits to 99.5% monthly availability for a payment processing service. The internal network team provides the connectivity infrastructure for this service. What type of agreement should govern the performance commitments of the internal network team to support the SLA?

- A) Service Level Agreement (SLA) — the network team is providing a service and should have the same agreement type as with customers.
- B) Underpinning Contract (UC) — the network team requires a legally binding contract.
- C) Operational Level Agreement (OLA) — the internal network team is an internal support group whose commitments underpin the SLA.
- D) No formal agreement is needed — internal teams are expected to deliver without documentation.

**Correct Answer:** C) Operational Level Agreement — an internal agreement that specifies the network team's commitments to support the SLA.

**Distractor Analysis:**

- *Why C is correct:* An OLA is an agreement between an IT service provider and another part of the same organization. The internal network team providing connectivity is an internal support group — not a customer and not an external supplier. An OLA defines their specific performance commitments (such as network availability targets and incident response times) that collectively enable the provider to meet its SLA with the customer.
- *Why A is incorrect:* SLAs are agreements with customers — external parties who receive the service. The network team is an internal support group within the same organization. Applying SLA terminology to an internal team misidentifies the relationship.
- *Why B is incorrect:* UCs are legally binding contracts with external third-party suppliers. The internal network team is part of the same organization — a UC is not the appropriate agreement type for an internal group.
- *Why D is incorrect:* ITIL 4 Service Level Management emphasizes that all performance commitments — internal and external — should be documented. Undocumented internal commitments create accountability gaps and make it impossible to trace SLA performance problems to their source.

---

### Question 6

Which of the following best describes a "watermelon SLA"?

- A) An SLA that is green on the outside and red on the inside — all technical metrics meet targets but customer satisfaction is low because the metrics do not measure what matters to customers.
- B) An SLA that has too many metrics, making it impossible to determine which ones indicate real service quality.
- C) An SLA negotiated in summer months when IT staffing is reduced, resulting in targets that are easier to meet.
- D) An SLA where the service provider earns financial rewards for exceeding targets — the reverse of the standard penalty model.

**Correct Answer:** A) A watermelon SLA shows green technical metrics while concealing poor customer experience — the metrics measure the wrong things.

**Distractor Analysis:**

- *Why A is correct:* The watermelon SLA concept is introduced in ITIL 4 Service Level Management to describe a specific and important failure mode: all measured metrics are green (system availability, response time, resolution time all meet targets) but customer satisfaction is low. This happens when the agreed metrics do not capture what customers actually care about. The name comes from the visual analogy — green on the outside, red on the inside. The fix is to engage customers to identify what actually matters and redesign the metrics accordingly.
- *Why B is incorrect:* Having too many metrics is a design problem, but it does not specifically create the green-outside-red-inside dynamic that defines the watermelon SLA.
- *Why C is incorrect:* This is not a recognized ITIL 4 concept. SLA negotiation timing is not a defined watermelon SLA characteristic.
- *Why D is incorrect:* Reward-based SLAs are a commercial construct in some outsourcing agreements. This is unrelated to the ITIL 4 watermelon SLA concept, which is about metric validity, not commercial structure.

---

### Question 7

The ITIL 4 guiding principle "Start Where You Are" is being applied to a service desk improvement project. The improvement team has proposed conducting a detailed assessment of the current service desk before making any changes. A project manager objects, saying it would be faster to design the ideal future-state service desk and build toward it. Which response best represents the "Start Where You Are" principle?

- A) The project manager is correct — starting from a blank slate eliminates legacy constraints and produces better outcomes.
- B) The improvement team is correct — assessing current state preserves useful existing capabilities, avoids discarding what works, and grounds improvement decisions in evidence rather than assumptions.
- C) Both approaches are equivalent — the guiding principle does not specify whether to assess first or design first.
- D) The project manager is correct because starting from scratch is faster and ITIL 4 prioritizes speed above all other considerations.

**Correct Answer:** B) The improvement team's approach correctly applies "Start Where You Are" by assessing what exists before making changes.

**Distractor Analysis:**

- *Why B is correct:* "Start Where You Are" specifically advises against designing from a blank slate without assessing the current state. The principle recognizes that existing services, processes, and tools contain value — some elements are working well and should be preserved. Assessing current state also reveals what is actually causing problems, preventing improvement efforts from solving the wrong problems. Measurement of the current state provides the baseline against which improvement will be evaluated.
- *Why A is incorrect:* Starting from a blank slate typically discards working elements along with broken ones, wastes the knowledge embedded in existing systems, and produces improvements that are not grounded in evidence of what actually needs to change.
- *Why C is incorrect:* The "Start Where You Are" principle is clear about the value of current-state assessment. It is not neutral between the two approaches — it explicitly recommends assessing before redesigning.
- *Why D is incorrect:* Speed is not ITIL 4's only consideration. The guiding principles collectively balance speed, quality, value, and sustainability. "Start Where You Are" prioritizes informed improvement over fast but uninformed redesign.

---

### Question 8

ITIL 4 defines four dimensions of service management that must be considered for every service and practice. An organization is deploying a new cloud-based HR system. During the design phase, the team identifies that the cloud vendor has a shared-responsibility model where the vendor manages infrastructure security but the organization manages application and data security. Which dimension does this consideration primarily fall under?

- A) Organizations and People — the shared responsibility model affects staffing and training requirements.
- B) Information and Technology — cloud infrastructure is a technology consideration.
- C) Partners and Suppliers — the relationship with the cloud vendor and the shared-responsibility model fall under supplier management.
- D) Value Streams and Processes — the shared-responsibility model affects how security processes flow between the organization and vendor.

**Correct Answer:** C) Partners and Suppliers — the relationship with and obligations of an external cloud vendor is a supplier dimension consideration.

**Distractor Analysis:**

- *Why C is correct:* The Partners and Suppliers dimension covers all relationships with organizations that contribute to service delivery — including cloud vendors, managed service providers, and technology partners. A cloud vendor's shared-responsibility model defines what the supplier is responsible for and what the organization retains responsibility for. Understanding and documenting this boundary is a Partners and Suppliers dimension activity, directly connected to the Supplier Management practice.
- *Why A is incorrect:* While the shared-responsibility model may influence staffing and training decisions (an Organizations and People consideration), the primary classification of a vendor obligation model is Partners and Suppliers. Training implications are a secondary consideration.
- *Why B is incorrect:* Cloud infrastructure is a technology asset, but the shared-responsibility model is not about the technology itself — it is about who is responsible for what within the relationship between the organization and the vendor. That is a supplier relationship consideration.
- *Why D is incorrect:* Shared-responsibility models do affect process flows, but the primary dimension for vendor relationship management is Partners and Suppliers. Value Streams and Processes would be more relevant to how internal security processes are designed and executed.

---

### Question 9

Which of the following correctly describes the purpose of Continual Improvement in ITIL 4?

- A) To ensure that every IT service meets its SLA targets by continuously monitoring performance against agreed thresholds.
- B) To align the organization's practices and services with changing business needs through ongoing improvement of products, services, and practices.
- C) To manage the improvement backlog for the IT department and ensure improvement projects are delivered on time.
- D) To conduct annual reviews of all ITSM processes and update them to reflect current industry best practices.

**Correct Answer:** B) The purpose of Continual Improvement is to align practices and services with changing business needs through ongoing improvement.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 defines the purpose of the Continual Improvement practice as aligning the organization's practices and services with changing business needs through ongoing improvement of products, services, and practices in all four dimensions of service management. The emphasis on "changing business needs" is important — improvement is driven by evolving requirements, not just by past deficiencies.
- *Why A is incorrect:* Monitoring performance against SLA targets is the purpose of Service Level Management, not Continual Improvement. Continual Improvement draws on SLA performance data as one input but has a broader purpose.
- *Why C is incorrect:* Managing an improvement backlog is an operational activity within Continual Improvement, not the purpose of the practice. The purpose is the broader alignment of practices and services with business needs.
- *Why D is incorrect:* Annual reviews are one possible Continual Improvement activity, but the practice operates continuously — not just annually. Restricting improvement reviews to annual cycles would contradict the "continual" nature of the practice.

---

### Question 10

An organization has just deployed a major update to its customer relationship management system. Two weeks after deployment, the service manager conducts a structured evaluation to determine whether the release achieved its intended outcomes, identify any incidents caused by the release, and capture lessons learned. What is this activity called?

- A) Change audit — a formal review of whether the change was authorized and executed according to the approved change record.
- B) Post-implementation review — a structured evaluation after a release reaches production to assess outcomes and capture lessons learned.
- C) Service review — a periodic meeting between the service provider and the customer to review SLA performance.
- D) Problem review — a Problem Management activity to identify whether the release introduced new problems.

**Correct Answer:** B) Post-implementation review — the structured evaluation conducted after a release to assess outcomes and capture lessons learned.

**Distractor Analysis:**

- *Why B is correct:* The post-implementation review (PIR) is the Release and Deployment Management activity specifically designed to evaluate a release after deployment. It assesses whether outcomes were achieved, identifies release-caused incidents, evaluates deployment plan quality, and captures lessons learned for future releases. PIR outputs feed the Continual Improvement Register.
- *Why A is incorrect:* A change audit is a compliance activity verifying that a change was authorized and executed according to its approved record — it is not the structured outcome assessment described in the scenario. The scenario describes outcome evaluation and lessons learned, not authorization compliance checking.
- *Why C is incorrect:* A service review is a Service Level Management activity — a periodic meeting with the customer to review SLA performance over a defined period. It is not specifically a post-release evaluation of a deployment's outcomes.
- *Why D is incorrect:* A Problem Management review investigates root causes of incidents. A PIR is broader — it evaluates whether the release achieved its goals, whether deployment was executed well, and what can be improved next time. Problem investigation may occur within or alongside the PIR, but the overall activity is the PIR.

---

### Question 11

The ITIL 4 Change Enablement practice defines three types of changes. A software development team deploys bug fixes to a web application multiple times per week using a fully automated CI/CD pipeline. Each deployment follows the same documented procedure, passes automated tests, and has a pre-defined rollback procedure. What change type best describes these deployments?

- A) Emergency change — multiple deployments per week indicate urgency requiring expedited authorization.
- B) Normal change — each deployment must be individually assessed and authorized by the change authority.
- C) Standard change — pre-authorized, low-risk deployments following a documented procedure.
- D) Unauthorized change — automated deployments without manual approval violate change management requirements.

**Correct Answer:** C) Standard change — pre-authorized, low-risk, following a documented procedure.

**Distractor Analysis:**

- *Why C is correct:* Standard changes are pre-authorized as a class. When a deployment approach — automated pipeline with defined tests, rollback procedure, and documented steps — has been assessed and approved as a standard change category, individual deployments following that procedure do not require further authorization. This is what enables DevOps-speed deployment within an ITIL 4 governance framework.
- *Why A is incorrect:* Frequency is not the defining characteristic of emergency changes. Emergency changes are required when urgency demands expedited authorization for an unplanned situation. Routine, frequent, planned deployments through a validated pipeline are not emergency situations.
- *Why B is incorrect:* Requiring individual assessment and CAB authorization for each of multiple weekly deployments would make the process a bottleneck. Standard change pre-authorization exists precisely to avoid this overhead for routine, low-risk, well-understood deployments.
- *Why D is incorrect:* Automated deployments that follow a documented, pre-authorized procedure are fully compliant with ITIL 4. "Optimize and Automate" is an ITIL 4 guiding principle. Automation of pre-authorized standard changes is explicitly supported.

---

### Question 12

Which of the following correctly describes the relationship between a service's "output" and its "outcome"?

- A) Output and outcome are synonyms in ITIL 4 — both describe the result delivered to the customer.
- B) An output is a tangible or intangible deliverable; an outcome is a result for a stakeholder enabled by outputs — outcomes represent the value the customer receives from using the output.
- C) An outcome is always measurable; an output may be intangible and unmeasurable.
- D) Outputs are generated by the service provider; outcomes are generated by the customer independently of any service.

**Correct Answer:** B) An output is a deliverable; an outcome is the result for a stakeholder that the output enables.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 carefully distinguishes outputs from outcomes. An output is what the service produces — a report, a transaction, a software feature, a resolved incident ticket. An outcome is the result this enables for a stakeholder — the business decision made from the report, the purchase completed via the transaction, the increased user productivity from the new feature. This distinction matters because customers purchase services for their outcomes, not for the outputs themselves.
- *Why A is incorrect:* Treating output and outcome as synonyms obscures one of ITIL 4's key value concepts. Conflating them would suggest that delivering outputs is sufficient, when in fact outcomes are what drive customer satisfaction and value co-creation.
- *Why C is incorrect:* Both outputs and outcomes can be tangible or intangible, measurable or difficult to measure. The distinguishing characteristic is not measurability but the level — deliverable (output) versus result enabled by the deliverable (outcome).
- *Why D is incorrect:* Outcomes are not generated by customers independently. Outcomes result from customers using the outputs that services provide. Value is co-created — the provider contributes outputs, the customer realizes outcomes from using those outputs.

---

### Question 13

An IT organization receives feedback from a department manager that the IT service desk is not resolving issues quickly enough. An internal review reveals that the service desk handles 78% of issues at the first point of contact and routes the remaining 22% to specialist teams. The specialist team resolution average is 4.2 days. Which Service Desk concept most directly addresses improving the 4.2-day specialist resolution time?

- A) Omnichannel — adding more contact channels will reduce resolution time.
- B) Shift-left — moving resolution capability closer to the user by expanding what the service desk can resolve without escalating.
- C) Major incident procedure — the 4.2-day delays should be escalated as major incidents.
- D) Service catalogue — publishing a service catalogue will help users understand what the service desk can resolve.

**Correct Answer:** B) Shift-left — increasing the service desk's resolution capability reduces the volume routed to specialist teams with longer resolution times.

**Distractor Analysis:**

- *Why B is correct:* Shift-left is the strategy of moving resolution capability closer to the user — typically to the service desk or to self-service. When the service desk resolves more issues at first contact, fewer issues enter the longer specialist queues. Shift-left is achieved through knowledge articles, training, expanded service desk authority to resolve more issue types, and automation. Improving the first-contact resolution rate from 78% directly reduces the population experiencing 4.2-day delays.
- *Why A is incorrect:* Omnichannel addresses how users contact the service desk — through phone, chat, email, portal, or walk-in. Adding contact channels does not change the service desk's resolution capability or reduce specialist queue times.
- *Why C is incorrect:* A 4.2-day average resolution time for routed issues, while worth improving, does not meet the criteria for a major incident declaration. Major incidents are declared for the highest-impact, most urgent service disruptions — not for routine resolution time performance.
- *Why D is incorrect:* A service catalogue helps users understand available services and how to request them. It does not address the resolution capability gap between service desk and specialist teams that is causing the 4.2-day delay.

---

### Question 14

ITIL 4 describes value as being "co-created" between a service provider and a customer. Which of the following scenarios best illustrates value co-creation?

- A) A cloud provider delivers 99.99% availability for its storage platform — value is fully created by the provider's technical infrastructure.
- B) A software company publishes a collaboration tool that users adopt and integrate into their daily workflows, resulting in measurable productivity improvements for their teams.
- C) An IT department completes all service requests within agreed timeframes — value is demonstrated through SLA compliance.
- D) A vendor delivers a project on time and within budget — value is confirmed by meeting contractual obligations.

**Correct Answer:** B) Users adopt the tool and integrate it into workflows — both provider (delivery) and customer (adoption and use) contribute to the productivity outcome.

**Distractor Analysis:**

- *Why B is correct:* Value co-creation requires both the provider's contribution (the working tool, available and functional) and the customer's contribution (adoption, integration into workflows, effective use). The productivity improvement is an outcome that neither party achieves alone — it requires the provider to deliver a capable tool and the customer to use it effectively. This is what ITIL 4 means by co-creation: value emerges from the interaction between provider capabilities and customer engagement.
- *Why A is incorrect:* This describes the provider's contribution to warranty — high availability. But availability alone does not create value unless customers use the storage platform in ways that produce outcomes. If no one stores anything, 99.99% availability produces no value. Provider-side performance is a necessary but not sufficient condition for value.
- *Why C is incorrect:* SLA compliance demonstrates that agreed service levels were met — an important signal of service quality. But meeting SLAs is an output measurement, not evidence of value co-creation. Value is realized when customers achieve their desired outcomes, which may or may not be captured by SLA metrics.
- *Why D is incorrect:* Delivering on time and within budget demonstrates project management performance. It does not confirm that the delivered product enabled the business outcomes that motivated the project. Value co-creation requires customer realization of outcomes, not just provider delivery of outputs.

---

### Question 15

According to ITIL 4, which of the following is the correct sequence for the Continual Improvement Model?

- A) Take action → Where are we now? → Where do we want to be? → What is the vision? → Did we get there? → How do we keep the momentum going? → How do we get there?
- B) What is the vision? → Where are we now? → Where do we want to be? → How do we get there? → Take action → Did we get there? → How do we keep the momentum going?
- C) Where do we want to be? → What is the vision? → Take action → Where are we now? → How do we get there? → Did we get there? → How do we keep the momentum going?
- D) How do we get there? → What is the vision? → Where are we now? → Take action → Where do we want to be? → Did we get there? → How do we keep the momentum going?

**Correct Answer:** B) The Continual Improvement Model follows the sequence: vision → current state → desired state → plan → act → verify → sustain.

**Distractor Analysis:**

- *Why B is correct:* The ITIL 4 Continual Improvement Model has seven steps in this specific sequence: (1) What is the vision? — establish business vision and objectives; (2) Where are we now? — assess current state; (3) Where do we want to be? — define measurable targets; (4) How do we get there? — plan the improvement; (5) Take action — implement the improvement; (6) Did we get there? — measure and evaluate; (7) How do we keep the momentum going? — sustain and build on improvements. This sequence ensures that improvement is grounded in vision, evidence, and measurement.
- *Why A is incorrect:* This sequence begins with action before establishing vision or current state — a fundamental violation of the model's logic. Improvement without a vision is directionless; improvement without current-state assessment lacks a baseline for measuring success.
- *Why C is incorrect:* This sequence begins with "Where do we want to be?" before establishing the vision that should drive that target. Without a clear vision, improvement targets may not align with business objectives.
- *Why D is incorrect:* Beginning with "How do we get there?" before establishing vision, current state, or desired state means planning without a defined destination or starting point — making the plan impossible to validate.

---

### Question 16

An organization is adopting ITIL 4 alongside its existing Scrum development practices. A developer asks whether the ITIL 4 "Progress Iteratively with Feedback" principle conflicts with Scrum's two-week sprint model. What is the most accurate response?

- A) There is a conflict — ITIL 4 requires longer planning cycles that are incompatible with two-week sprints.
- B) There is no conflict — ITIL 4's iterative principle is directly aligned with Scrum's sprint model; both emphasize delivering in increments and adapting based on feedback from each iteration.
- C) The developer should choose between ITIL 4 and Scrum — combining them creates unnecessary complexity.
- D) ITIL 4's iterative principle only applies to infrastructure improvements — software development follows different rules.

**Correct Answer:** B) ITIL 4's iterative principle directly aligns with Scrum's sprint model — both emphasize incremental delivery and feedback-driven adaptation.

**Distractor Analysis:**

- *Why B is correct:* "Progress Iteratively with Feedback" is one of ITIL 4's seven guiding principles. It advises against big-bang delivery and comprehensive upfront planning, recommending instead that work be organized in iterations with feedback reviewed after each. This is exactly what Scrum's sprint model does — deliver working output every two weeks, review with stakeholders, incorporate feedback into the next sprint. The alignment is intentional in ITIL 4's design.
- *Why A is incorrect:* ITIL 4 does not require long planning cycles. This misconception derives from older ITIL versions. ITIL 4 specifically embraces iterative, adaptive approaches to both service delivery and improvement.
- *Why C is incorrect:* ITIL 4 was designed to coexist with Agile frameworks including Scrum. Modern IT organizations routinely combine them — Scrum governs development methodology while ITIL 4 governs service management governance and operational practices.
- *Why D is incorrect:* ITIL 4's guiding principles apply across all aspects of the Service Value System — including software development, service design, improvement initiatives, and operations. They are not domain-restricted.

---

### Question 17

A service desk analyst receives a call from a user who wants to request a laptop upgrade for a new project. The user's current laptop is functioning correctly but does not meet the specifications required by the project software. How should the analyst classify this contact?

- A) Incident — the laptop's failure to meet project specifications represents a degradation in service quality.
- B) Problem — the underlying cause of the specification gap must be investigated.
- C) Service request — this is a pre-defined, user-initiated request for a service item.
- D) Change — the laptop upgrade requires a formal change record.

**Correct Answer:** C) Service request — the user is requesting a planned, pre-defined service item (hardware upgrade), not reporting an unplanned disruption.

**Distractor Analysis:**

- *Why C is correct:* Service requests are formal requests from users for things to be provided — they include hardware requests, access provisioning, information requests, and standard service items. The user's laptop is functioning correctly; the request is for an upgrade to meet project needs. This is a planned, expected, pre-defined request type — a service request, not an incident.
- *Why A is incorrect:* An incident is an unplanned interruption to a service. The laptop is working — there is no service interruption. The user is making a proactive request for a resource upgrade, not reporting a failure.
- *Why B is incorrect:* Problem Management investigates root causes of incidents. There is no incident to investigate. A proactive hardware upgrade request does not trigger a problem investigation.
- *Why D is incorrect:* While fulfilling the laptop upgrade request may eventually generate a change record when the hardware is deployed and configured, the initial contact is classified as a service request. The service request lifecycle manages the request; change management handles the deployment step within it.

---

### Question 18

Which of the following best describes the role of the PESTLE factors in ITIL 4?

- A) PESTLE factors are internal management considerations that ITSM teams use to assess the readiness of their own organization for service improvements.
- B) PESTLE factors represent the external environment (Political, Economic, Social, Technological, Legal, Environmental) that surrounds and influences all four dimensions of service management.
- C) PESTLE is the ITIL 4 name for the five components of the Service Value System.
- D) PESTLE factors are only relevant to organizations operating internationally — domestic IT organizations do not need to consider them.

**Correct Answer:** B) PESTLE factors are external environmental forces that influence all four dimensions of service management.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 uses PESTLE (Political, Economic, Social, Technological, Legal, Environmental) to represent the external factors that organizations cannot control but must respond to. These external forces affect how services are designed, delivered, and governed. For example, a legal change (GDPR) affects the Information and Technology and Partners and Suppliers dimensions. A technological change (cloud adoption) affects all four dimensions. PESTLE factors form the outer ring of the ITIL 4 four-dimensions model.
- *Why A is incorrect:* PESTLE factors are external to the organization — they represent the environment the organization operates in, not internal readiness factors. Internal assessments use tools like gap analysis and current-state assessment.
- *Why C is incorrect:* The five components of the SVS are guiding principles, governance, service value chain, practices, and continual improvement. PESTLE is not part of the SVS components — it is the external environment surrounding the four dimensions model.
- *Why D is incorrect:* Every organization operates within an external environment. Legal changes, economic conditions, and technological developments affect domestic organizations as much as international ones. PESTLE applicability is not limited by geographic scope.

---

### Question 19

An IT organization is evaluating whether to automate its incident escalation process. Currently, analysts manually review and escalate incidents to specialist teams. A consultant recommends automating the escalation routing based on incident category and keywords. The ITIL 4 guiding principle "Optimize and Automate" advises which of the following before automation is implemented?

- A) Automate immediately — the principle prioritizes speed of automation above all other considerations.
- B) First optimize the escalation process — remove unnecessary steps and ensure the routing logic is sound — then automate the optimized process.
- C) Do not automate manual human judgment — the principle only applies to infrastructure provisioning, not incident routing.
- D) Automate and then optimize — automation will reveal which parts of the process need improvement.

**Correct Answer:** B) Optimize first, then automate — the principle explicitly advises removing waste before embedding the process in automation.

**Distractor Analysis:**

- *Why B is correct:* "Optimize and Automate" is explicit in its sequencing: optimize first, then automate. If the escalation routing logic has unnecessary steps, incorrect categorizations, or poor keyword rules, automating it will embed those flaws into the automated system — making them execute faster but not better. Optimizing the routing logic (ensuring categories are accurate, escalation paths are appropriate, and unnecessary intermediate steps are removed) before automation produces a faster and more accurate automated process.
- *Why A is incorrect:* Speed of automation is not the priority. The principle is named "Optimize and Automate" — optimization precedes automation. Automating without optimizing creates faster failure, not better performance.
- *Why C is incorrect:* The principle applies broadly — to any repeatable process including incident routing, change approvals, service request fulfillment, and monitoring alerts. It is not restricted to infrastructure provisioning.
- *Why D is incorrect:* Reversing the sequence — automate first, then optimize — is the mistake the principle is designed to prevent. Once a flawed process is automated, organizations tend to work around the automation rather than fixing it, and the flaws become harder to address.

---

### Question 20

Which combination of factors must both be satisfied for a service to deliver value to a customer?

- A) Cost control and risk elimination — the service must be financially efficient and free of all risk.
- B) Utility and warranty — the service must be fit for purpose (does what is needed) and fit for use (available, secure, and reliable when needed).
- C) Output and efficiency — the service must produce measurable outputs and operate below target cost.
- D) Incident-free operation and SLA compliance — no incidents and all metrics green confirm value delivery.

**Correct Answer:** B) Utility (fit for purpose) and warranty (fit for use) must both be satisfied for a service to deliver value.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 explicitly states that both utility and warranty must be present for a service to deliver value. Utility alone — the service has the right features — is insufficient if the service is frequently unavailable, performs poorly, or is insecure. Warranty alone — the service is always available — is insufficient if the service does not do what the customer needs. Both dimensions of service quality must be met simultaneously.
- *Why A is incorrect:* Cost control and risk elimination are ITAM and risk management objectives — they are not the ITIL 4 definition of service value delivery. Additionally, "eliminating all risk" is not achievable — ITIL 4 focuses on managing risk to acceptable levels, not eliminating it.
- *Why C is incorrect:* Output and efficiency describe production characteristics, not the customer value framework. ITIL 4 defines value delivery in terms of utility and warranty — fit for purpose and fit for use — not by output count or cost efficiency.
- *Why D is incorrect:* Incident-free operation and SLA compliance are performance indicators — but a watermelon SLA can show all metrics green while delivering low value to customers. Value is confirmed by customers achieving their desired outcomes, not by metrics alone.
