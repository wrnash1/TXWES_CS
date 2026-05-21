# Quiz: Module 13 - Service Management Practices - Service Request Management and Release Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the Service Request Management practice in ITIL 4?
*   A) To restore normal service operation as quickly as possible following an unplanned disruption to an IT service.
*   B) To support the agreed quality of a service by handling all predefined, user-initiated service requests in an effective and user-friendly manner.
*   C) To authorize and schedule changes to IT services and infrastructure to minimize the risk of service disruption.
*   D) To package a set of authorized changes into a release and prepare it for deployment to the live environment.
*   **Correct Answer:** B) The purpose of Service Request Management is to handle predefined, user-initiated service requests effectively and in a user-friendly manner.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of Service Request Management as supporting the agreed quality of a service by handling all predefined, user-initiated service requests. These are planned, normal parts of service delivery — not disruptions — and include requests for information, access, and standard service activities.
    *   *Why A is incorrect:* Restoring service after an unplanned disruption is the purpose of Incident Management. Service requests are not disruptions — they are expected, pre-approved requests.
    *   *Why C is incorrect:* Authorizing and scheduling changes is the purpose of Change Enablement. Service Request Management handles pre-approved standard requests that do not require the change authorization process.
    *   *Why D is incorrect:* Packaging authorized changes into a release is the purpose of Release Management, not Service Request Management.

---

**Question 2**
A user submits a ticket asking IT to install a specific approved software package on their laptop. The software is on the organization's approved application list and the process for installing it is documented and pre-authorized. Which practice should handle this ticket, and why?
*   A) Incident Management — the user is unable to use the software, which is a service disruption requiring incident resolution.
*   B) Change Enablement — installing software on a user device is a change to the environment and requires change authorization.
*   C) Service Request Management — installing pre-approved software is a predefined, user-initiated service request that follows a documented fulfillment process.
*   D) Problem Management — the absence of the software represents a recurring gap that needs root cause investigation.
*   **Correct Answer:** C) Installing pre-approved software is a predefined service request handled by Service Request Management.
*   **Distractor Analysis:**
    *   *Why C is correct:* The software is on the approved list and the installation process is documented and pre-authorized — all criteria for a standard service request. Service Request Management is the appropriate practice because the request is planned, expected, and follows a defined fulfillment workflow without requiring individual change risk assessment.
    *   *Why A is incorrect:* There is no service disruption here — the user is requesting something new, not reporting a failure. Incidents are unplanned interruptions; this is a planned request.
    *   *Why B is incorrect:* While software installation technically involves a change to the device, routine, pre-approved service requests are handled through Service Request Management without going through the full Change Enablement authorization process. Only non-standard or high-risk changes require Change Enablement.
    *   *Why D is incorrect:* Problem Management investigates root causes of incidents. The absence of software on a laptop is not an incident and has no root cause to investigate — it is simply a user request.

---

**Question 3**
What is the primary purpose of the Release Management practice in ITIL 4?
*   A) To assess the risk of proposed changes and authorize them to proceed through the change schedule.
*   B) To move new or changed hardware, software, documentation, processes, or any other component to live environments.
*   C) To make new and changed services and features available for use by planning, testing, and preparing releases.
*   D) To restore normal service operation as quickly as possible following a failed deployment to the live environment.
*   **Correct Answer:** C) The purpose of Release Management is to make new and changed services and features available for use through planning, testing, and release preparation.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 defines the purpose of Release Management as making new and changed services and features available for use. This includes planning what is included in a release, coordinating testing and validation, and ensuring the release is ready before it is handed to Deployment Management for movement to live.
    *   *Why A is incorrect:* Assessing risk and authorizing changes is the purpose of Change Enablement. Release Management works with already-authorized changes to prepare them for release.
    *   *Why B is incorrect:* Moving components to live environments is the purpose of Deployment Management. Release Management prepares the release; Deployment Management delivers it.
    *   *Why D is incorrect:* Restoring service after a failed deployment is Incident Management. Release Management does not respond to live environment failures — it works upstream, preparing releases before deployment.

---

**Question 4**
An IT organization is preparing to release three authorized changes to its customer portal: a new search feature, a performance optimization, and a security patch. Release Management has decided to bundle all three into a single release, test them together, and deploy them in one scheduled maintenance window. Which of the following best describes what Release Management has done, and why?
*   A) Release Management has performed a deployment — it has moved the three changes into the live environment during the maintenance window.
*   B) Release Management has created a release that bundles multiple authorized changes, tested them as a unit, and prepared them for Deployment Management to move to live.
*   C) Release Management has performed Change Enablement activities by authorizing the three changes to proceed together.
*   D) Release Management has replaced Service Request Management by bundling the three changes as service requests fulfilled during the maintenance window.
*   **Correct Answer:** B) Release Management bundled authorized changes into a release, tested them together, and prepared them for Deployment Management to execute.
*   **Distractor Analysis:**
    *   *Why B is correct:* This describes the core Release Management workflow. Three separately authorized changes are bundled into a single release, tested as a unit (to confirm they work together correctly), and prepared with a release plan. The actual movement to live — the deployment — is then carried out by Deployment Management during the maintenance window.
    *   *Why A is incorrect:* Moving changes to the live environment is Deployment Management's responsibility. Release Management prepares the release but does not perform the deployment itself.
    *   *Why C is incorrect:* The changes were already authorized before Release Management became involved. Change Enablement handles authorization; Release Management handles packaging and preparation.
    *   *Why D is incorrect:* Service requests are user-initiated, predefined requests for standard services. Bundling authorized infrastructure and application changes into a release has nothing to do with Service Request Management.

---

**Question 5**
Which of the following statements correctly distinguishes Service Request Management from Incident Management in ITIL 4?
*   A) Service requests and incidents are handled by the same process — both are logged as tickets and routed to technical teams for resolution.
*   B) Incident Management handles all IT work; Service Request Management is only used when a formal SLA is in place between the provider and the customer.
*   C) Service requests are predefined, user-initiated requests for something to be provided as a normal part of service delivery; incidents are unplanned interruptions to a service or reductions in its quality.
*   D) Service requests require CAB authorization before fulfillment; incidents can be resolved immediately without any authorization.
*   **Correct Answer:** C) Service requests are predefined, planned requests for normal service activities; incidents are unplanned disruptions or quality reductions.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 defines these two categories precisely to ensure they are handled appropriately. Service requests follow a predefined fulfillment workflow and are expected — they are part of normal service delivery. Incidents are unexpected and require diagnosis and restoration of service. Treating them the same leads to inefficiency, misrouting, and incorrect prioritization.
    *   *Why A is incorrect:* While both may be logged as tickets in the same tool, ITIL 4 is explicit that they require different practices, different workflows, and different response approaches. Treating them identically undermines the purpose of having distinct practices.
    *   *Why B is incorrect:* The applicability of Service Request Management is not conditional on an SLA being in place. Service Request Management applies whenever users make predefined requests — regardless of whether a formal SLA governs the service.
    *   *Why D is incorrect:* Standard service requests are pre-approved and do not require CAB authorization — that is one of their defining characteristics. CAB authorization applies to normal changes, not to pre-approved service requests.
