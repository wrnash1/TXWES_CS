# Quiz: Module 08 - Service Management Practices - Incident Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the Incident Management practice in ITIL 4?
*   A) To identify the root cause of recurring service disruptions and implement permanent fixes.
*   B) To minimize the negative impact of incidents by restoring normal service operation as quickly as possible.
*   C) To manage all planned changes to IT services and ensure they are properly authorized before implementation.
*   D) To record and fulfill user requests for standard services such as new accounts or software installations.
*   **Correct Answer:** B) The purpose of Incident Management is to restore normal service operation as quickly as possible and minimize business impact.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of Incident Management as minimizing the negative impact of incidents by restoring normal service operation as quickly as possible. Speed of recovery is the priority — not root cause analysis.
    *   *Why A is incorrect:* Identifying root causes and implementing permanent fixes is the purpose of Problem Management, not Incident Management. Incident Management focuses on restoration, not root cause.
    *   *Why C is incorrect:* Managing planned changes and ensuring authorization is the purpose of Change Enablement, not Incident Management.
    *   *Why D is incorrect:* Recording and fulfilling user requests for standard services is the purpose of Service Request Management. Service requests are planned and expected, whereas incidents are unplanned disruptions.

---

**Question 2**
Which of the following most accurately describes the difference between an incident and a problem in ITIL 4?
*   A) An incident is a planned service activity, while a problem is an unplanned service disruption that requires emergency authorization.
*   B) An incident is an unplanned interruption to a service or reduction in its quality, while a problem is the underlying cause of one or more incidents.
*   C) An incident is raised by the service desk on behalf of a user, while a problem is raised by a developer when a software defect is discovered.
*   D) An incident and a problem are the same thing — ITIL 4 uses both terms interchangeably to describe service disruptions.
*   **Correct Answer:** B) An incident is an unplanned interruption or quality reduction, while a problem is the underlying cause of one or more incidents.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 makes a precise distinction: an incident is the immediate disruption experienced by users, while a problem is the underlying cause of that disruption. Incident Management restores service; Problem Management identifies and eliminates the root cause.
    *   *Why A is incorrect:* Incidents are not planned — they are unplanned disruptions. Planned service activities are handled as service requests or changes, not incidents.
    *   *Why C is incorrect:* While incidents are often reported to the service desk, they can originate from monitoring tools or any staff member. The distinction between incident and problem is not about who raises them — it is about what they represent.
    *   *Why D is incorrect:* ITIL 4 explicitly distinguishes incidents from problems. Using them interchangeably would cause the organization to conflate restoring service (incident) with finding root cause (problem), undermining both practices.

---

**Question 3**
A user calls the service desk to report that they cannot access the company's email system. After investigation, the service desk discovers that a network switch failure is causing email outages for all 300 users in one building. The service desk restores service by rerouting traffic through a backup switch. What was applied to restore service, and what should happen next?
*   A) A permanent fix was applied. The incident can be closed and no further action is needed.
*   B) A workaround was applied to restore service. A problem record should be raised to investigate and permanently resolve the underlying switch failure.
*   C) A service request was fulfilled. The user's email access request has been completed through the standard service request process.
*   D) A change was implemented. The service desk should submit a change record to the Change Advisory Board for retrospective approval.
*   **Correct Answer:** B) Rerouting traffic is a workaround that restores service — a problem record should be raised to address the underlying switch failure.
*   **Distractor Analysis:**
    *   *Why B is correct:* Rerouting traffic through a backup switch is a workaround — it restores service but does not fix the failed switch. ITIL 4 directs that a problem record be raised to investigate the root cause (the switch failure) and implement a permanent resolution, which may involve repair or replacement.
    *   *Why A is incorrect:* Rerouting traffic is not a permanent fix — the underlying switch failure remains unresolved. Closing the incident without raising a problem record would leave the root cause unaddressed and risk recurrence.
    *   *Why C is incorrect:* The user did not submit a planned request for email access. This was an unplanned disruption affecting 300 users — it is an incident, not a service request.
    *   *Why D is incorrect:* While the rerouting may require a change record depending on organizational policy, the primary next action is to raise a problem record for the switch failure. The incident scenario does not describe a change requiring CAB approval.

---

**Question 4**
An IT organization uses a two-factor prioritization model for incidents based on impact and urgency. A database server failure is preventing all 800 employees from accessing the order management system during the busiest sales period of the year. How should this incident be classified, and why?
*   A) Low priority — the incident affects a single server, which is a limited technical scope.
*   B) Medium priority — the incident affects a defined group of users, not external customers, so urgency is moderate.
*   C) High priority (major incident) — the high impact on all employees and the business-critical timing creates both high impact and high urgency.
*   D) Standard priority — all incidents follow the same response process regardless of scale, and priority is only assigned after root cause is identified.
*   **Correct Answer:** C) This incident has both high impact (800 employees, business-critical system) and high urgency (peak sales period), qualifying it as a major incident requiring a coordinated response.
*   **Distractor Analysis:**
    *   *Why C is correct:* Priority in ITIL 4 Incident Management is determined by combining impact (the breadth and severity of the effect on the business) with urgency (how quickly the situation will deteriorate). An outage affecting 800 employees during the peak sales period represents maximum impact and urgency — a major incident requiring an escalated, coordinated response.
    *   *Why A is incorrect:* Prioritization is based on business impact and urgency, not on the technical scope of what failed. A single server failure can have massive business impact.
    *   *Why B is incorrect:* Urgency is not limited to external customers. Internal employees relying on a business-critical system during peak sales represent high urgency. The impact-plus-urgency model applies regardless of whether the affected users are internal or external.
    *   *Why D is incorrect:* ITIL 4 explicitly requires incidents to be prioritized based on impact and urgency — not a flat, uniform process. Delaying prioritization until root cause is identified contradicts the Incident Management purpose of rapid restoration.

---

**Question 5**
Which of the following statements correctly distinguishes an incident from a service request in ITIL 4?
*   A) An incident requires technical staff to resolve it, while a service request can be handled by any user without IT involvement.
*   B) An incident is an unplanned interruption or quality reduction in a service, while a service request is a formal request from a user for something to be provided that is a normal part of an agreed service.
*   C) Incidents and service requests are both handled by Incident Management — service requests are simply lower-priority incidents.
*   D) A service request becomes an incident if the fulfillment time exceeds the agreed SLA target.
*   **Correct Answer:** B) An incident is an unplanned disruption; a service request is a planned, expected request for a normal service activity.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines these as distinct categories. Incidents are unplanned — they represent something going wrong. Service requests are planned and expected — they represent users accessing services as designed (such as requesting a new laptop, resetting a password, or requesting access to a system).
    *   *Why A is incorrect:* Many service requests do require IT staff involvement. The distinction is not about who handles them — it is about whether the activity was planned (service request) or represents an unplanned disruption (incident).
    *   *Why C is incorrect:* Service requests are handled by Service Request Management, not Incident Management. They are not lower-priority incidents — they are a fundamentally different category of activity.
    *   *Why D is incorrect:* A service request does not become an incident because of a fulfillment delay. If a service request cannot be fulfilled due to a system outage, that outage may generate a separate incident — but the service request itself remains a service request regardless of its fulfillment time.
