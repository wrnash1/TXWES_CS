# Quiz: Module 14 - Service Management Practices - IT Asset Management and Service Configuration Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
What is the primary purpose of the IT Asset Management practice in ITIL 4?
*   A) To record and track all configuration items and their relationships in a central database to support service delivery.
*   B) To plan and manage the full lifecycle of all IT assets to maximize value, control costs, manage risks, and meet regulatory requirements.
*   C) To authorize changes to IT assets and ensure that all modifications are properly assessed before implementation.
*   D) To monitor IT assets for performance events that may indicate approaching failure or degradation.
*   **Correct Answer:** B) The purpose of IT Asset Management is to plan and manage the full lifecycle of IT assets to maximize value, control costs, manage risks, and meet obligations.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 defines the purpose of IT Asset Management as planning and managing the full lifecycle of all IT assets to help the organization maximize value, control costs, manage risks, support decision-making about purchase, reuse, retirement, and disposal, and meet regulatory and contractual requirements. The focus is financial and lifecycle governance.
    *   *Why A is incorrect:* Recording configuration items and their relationships is the purpose of Service Configuration Management, not IT Asset Management. While there is overlap in data, the practices serve different purposes.
    *   *Why C is incorrect:* Authorizing changes is the purpose of Change Enablement. IT Asset Management governs the financial and lifecycle dimensions of assets — it does not authorize changes.
    *   *Why D is incorrect:* Monitoring assets for performance events is the purpose of Monitoring and Event Management. IT Asset Management tracks asset value and lifecycle, not real-time performance.

---

**Question 2**
Which of the following most accurately describes the difference between an IT asset and a configuration item (CI)?
*   A) An IT asset is tracked in the CMDB; a configuration item is tracked in the financial accounting system. They are stored separately and never overlap.
*   B) An IT asset is any financially valuable component tracked through its lifecycle; a CI is any component managed to support IT service delivery, recorded with its attributes and relationships in the CMDB.
*   C) Configuration items include only hardware and software; IT assets include a broader range of components including people and documentation.
*   D) IT assets and configuration items are identical — ITIL 4 uses both terms interchangeably to describe components of the IT infrastructure.
*   **Correct Answer:** B) An IT asset has financial value and is tracked through its lifecycle; a CI is managed for operational service delivery and recorded in the CMDB with its relationships.
*   **Distractor Analysis:**
    *   *Why B is correct:* ITIL 4 distinguishes these by purpose. An IT asset is tracked for financial and lifecycle reasons (cost, depreciation, procurement, disposal). A CI is tracked for operational service management reasons (impact on services, relationships to other components, change history). Many items are both — a server is an asset (financial value) and a CI (operational relationships). Some assets are not CIs, and some CIs are not assets.
    *   *Why A is incorrect:* The storage location is not the defining distinction. Many organizations store both in related or integrated systems. The distinction is the purpose for which each is tracked, not where the data lives.
    *   *Why C is incorrect:* This reverses the relationship. CIs in ITIL 4 can include hardware, software, documentation, people, facilities, and relationships — not just hardware and software. IT assets are defined by financial value, not breadth of type.
    *   *Why D is incorrect:* ITIL 4 explicitly maintains these as distinct concepts with different definitions, purposes, and governing practices. Using them interchangeably would conflate financial governance with operational service management.

---

**Question 3**
An IT service manager is planning a significant change to a core database server. Before submitting the change request, the manager uses the Configuration Management Database to review which services depend on that server and which other infrastructure components are connected to it. How does the CMDB support the Change Enablement practice in this scenario?
*   A) The CMDB authorizes the change on behalf of the Change Advisory Board, removing the need for a separate authorization step.
*   B) The CMDB provides relationship and dependency data that allows the change manager to assess the potential impact of the change on services and other CIs before proceeding.
*   C) The CMDB automatically schedules the change in the change calendar and notifies all affected service owners.
*   D) The CMDB replaces the need for a change record — since the server is already documented, no formal change request is required.
*   **Correct Answer:** B) The CMDB provides relationship and dependency data that enables impact assessment before the change proceeds.
*   **Distractor Analysis:**
    *   *Why B is correct:* One of the primary uses of the CMDB is to support impact assessment in Change Enablement. By mapping the relationships between CIs — which services run on which servers, which applications depend on which databases — the CMDB allows change managers and the CAB to understand what could be affected by a proposed change, enabling better risk assessment and authorization decisions.
    *   *Why A is incorrect:* The CMDB provides data — it does not hold authorization authority. Authorization belongs to the change authority designated in the Change Enablement practice. The CMDB informs the decision but does not make it.
    *   *Why C is incorrect:* The CMDB is a repository of configuration data. Scheduling changes and notifying stakeholders are activities performed by people and tools in the Change Enablement practice, not automatic CMDB functions.
    *   *Why D is incorrect:* Having a CI documented in the CMDB does not exempt any change to that CI from the Change Enablement process. All changes to services and infrastructure still require assessment and authorization.

---

**Question 4**
A company's IT team is conducting an audit and discovers that 45 software licenses in use are not recorded anywhere in the organization's asset management records. What risk does this unrecorded usage create, and which practice is responsible for addressing it?
*   A) The unrecorded licenses create a security vulnerability because they may contain malware — Service Configuration Management should quarantine the affected systems.
*   B) The unrecorded licenses create financial, legal, and compliance risks — the organization may be non-compliant with software licensing agreements. IT Asset Management is responsible for tracking and managing all software licenses.
*   C) The unrecorded licenses create a performance risk because unmanaged software increases system load — Monitoring and Event Management should detect and remove them.
*   D) The unrecorded licenses are a service disruption risk — Incident Management should log each license as an incident and restore compliance.
*   **Correct Answer:** B) Unrecorded software licenses create financial, legal, and compliance risks. IT Asset Management is responsible for tracking the full lifecycle of software licenses.
*   **Distractor Analysis:**
    *   *Why B is correct:* Software licenses are IT assets with financial value and legal obligations. Unrecorded licenses mean the organization cannot verify license compliance, may be violating software agreements (exposing it to audit penalties), and may be paying for unused licenses or failing to renew active ones. IT Asset Management governs the acquisition, tracking, and lifecycle management of all software licenses to prevent exactly these risks.
    *   *Why A is incorrect:* Unrecorded licenses are not inherently a security or malware issue. The risk is financial, legal, and compliance-based, not a security threat. Service Configuration Management tracks operational relationships, not software license compliance.
    *   *Why C is incorrect:* Unregistered licenses do not inherently indicate a performance issue. Monitoring and Event Management monitors service performance events — it does not manage asset records or license compliance.
    *   *Why D is incorrect:* A missing license record is not an incident — it is an administrative and compliance gap. Incident Management handles unplanned service disruptions, not asset record gaps.

---

**Question 5**
Which of the following statements about the Configuration Management Database (CMDB) in ITIL 4 is CORRECT?
*   A) The CMDB must be implemented as a single, centralized database — federated or distributed implementations are not compliant with ITIL 4.
*   B) The CMDB contains only hardware and software records — personnel, documentation, and supplier relationships are outside its scope.
*   C) The CMDB stores configuration records that include CI attributes, status, and relationships to other CIs, providing the visibility needed to support multiple ITIL 4 practices including Change Enablement, Incident Management, and Problem Management.
*   D) The CMDB is updated only during scheduled maintenance windows to prevent data conflicts from concurrent updates.
*   **Correct Answer:** C) The CMDB stores CI attributes, status, and relationships to support multiple practices including Change Enablement, Incident Management, and Problem Management.
*   **Distractor Analysis:**
    *   *Why C is correct:* ITIL 4 defines the CMDB as storing configuration records containing CI details — type, attributes, status, version, owner — and the relationships between CIs. This relationship data is what makes the CMDB valuable across multiple practices: Change Enablement uses it for impact assessment, Incident Management uses it to trace affected services, Problem Management uses it to identify common CIs in recurring incidents.
    *   *Why A is incorrect:* ITIL 4 explicitly acknowledges that the CMDB may be implemented as a logical concept spanning multiple federated data stores. A single centralized database is one implementation option, not a requirement.
    *   *Why B is incorrect:* ITIL 4 states that CIs can include hardware, software, documentation, people, facilities, and service relationships. The CMDB is not limited to technical components.
    *   *Why D is incorrect:* The CMDB should be kept as current as possible. Limiting updates to scheduled windows would result in stale data that undermines the accuracy needed by Change Enablement, Incident Management, and other practices that depend on it.
