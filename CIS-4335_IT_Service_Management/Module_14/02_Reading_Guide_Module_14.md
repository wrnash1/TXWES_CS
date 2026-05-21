# Reading Guide: Module 14 - Service Management Practices - IT Asset Management and Service Configuration Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

### Introduction
Welcome to **Module 14 - Service Management Practices: IT Asset Management and Service Configuration Management**! These two practices provide the foundational visibility that all other ITIL 4 practices depend on. You cannot manage what you cannot see — and these practices ensure the organization has an accurate, up-to-date view of its IT assets and service components. This module covers the purpose of each practice, key definitions including configuration items and the CMDB, and how these practices connect to Change Enablement, Incident Management, and Problem Management.

As a student, you will learn the distinction between IT assets and configuration items, understand how the Configuration Management Database (CMDB) supports service management, and explore how asset and configuration data flows into other practices. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ITIL 4 Foundation exam expects you to know these concepts precisely:

*   **IT Asset Management**: The ITIL 4 practice whose purpose is to plan and manage the full lifecycle of all IT assets in order to help the organization maximize value, control costs, manage risks, support decision-making about purchase, reuse, retirement, and disposal, and meet regulatory and contractual requirements.
*   **IT Asset**: Any financially valuable component that can contribute to the delivery of an IT product or service. IT assets include hardware (servers, laptops, network devices), software licenses, virtual assets, and cloud resources. They are tracked for financial and lifecycle purposes.
*   **Service Configuration Management**: The ITIL 4 practice whose purpose is to ensure that accurate and reliable information about the configuration of services and the configuration items (CIs) that support them is available when and where it is needed.
*   **Configuration Item (CI)**: Any component that needs to be managed in order to deliver an IT service. CIs include hardware, software, documentation, people, facilities, and relationships between components. CIs are recorded in the Configuration Management Database.
*   **Configuration Management Database (CMDB)**: A database used to store configuration records throughout their lifecycle. The CMDB records CIs, their attributes, and the relationships between them. It provides the foundational data that supports Change Enablement, Incident Management, Problem Management, and other practices.
*   **Configuration Record**: A document in the CMDB that contains the details of a CI. A configuration record typically includes the CI's type, owner, version, status, and its relationships to other CIs.
*   **Asset vs. CI Distinction**: All CIs may be assets, but not all assets are CIs. An IT asset has financial value and is tracked through its lifecycle. A CI is tracked for operational service management purposes. A server is both an asset (financial value, depreciation, procurement) and a CI (operational relationships, incidents, changes). A software license may be an asset but not necessarily a CI.

---

### 2. Certification Exam Tips
*   **IT Asset Management vs. Service Configuration Management:** Two distinct practices that are often confused. Asset Management tracks financial value and lifecycle. Configuration Management tracks operational data and relationships for service delivery. Both use overlapping data but serve different purposes.
*   **CMDB Is Not a Single Database:** The exam tests that the CMDB is a logical concept — it may be implemented as a single database or as a federated set of data stores. What matters is that the data is available, accurate, and reliable.
*   **CIs Include Non-Technical Items:** A common exam trap assumes CIs are only hardware and software. ITIL 4 explicitly includes documentation, people, facilities, and service relationships as potential CIs.
*   **CMDB Supports Multiple Practices:** Change Enablement uses the CMDB to assess the impact of proposed changes. Incident Management uses it to trace affected services. Problem Management uses it to identify common CIs involved in recurring incidents. Know these relationships.
*   **Asset Lifecycle Includes Disposal:** IT Asset Management covers the full asset lifecycle — from procurement planning through retirement and disposal. The exam may test that disposal planning (including secure data destruction) is part of the practice.
*   **Study Resource:** The Axelos ITIL 4 Foundation resources at [https://www.axelos.com/certifications/itil-service-management/itil-4-foundation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) include official glossary definitions for IT asset, configuration item, and the CMDB.
*   **Video Resource:** The [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W) on YouTube includes dedicated videos on IT Asset Management and Service Configuration Management with exam scenario examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters covering **IT Asset Management** and **Service Configuration Management** in the OER Textbook: [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/). Focus on the purpose of each practice, the definitions of IT asset and configuration item, and the role of the CMDB.
*   **Required Video:** Watch the video lectures on **IT Asset Management** and **Service Configuration Management** in the official course playlist: [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply these concepts in the following activities:
*   **Classify assets and CIs**: Given a list of twenty IT components (servers, laptops, software licenses, documentation, network cables, contracts), classify each as an IT asset only, a CI only, or both, and justify your classification using ITIL 4 definitions.
*   **Build a CMDB entry**: Using a provided CMDB template, create a configuration record for a sample server — including CI type, owner, version, status, hardware specifications, and at least three relationships to other CIs (such as the services it supports and the applications it hosts).
*   **Map CMDB dependencies**: For a given scenario where a critical server experiences an incident, use a sample CMDB relationship map to identify all services and applications affected, and explain how this information supports faster incident resolution.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the definitions of IT asset, configuration item, CMDB, and the asset-vs-CI distinction.
- [ ] Read the chapters covering **IT Asset Management** and **Service Configuration Management** in [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/).
- [ ] Watch the video lectures on **IT Asset Management** and **Service Configuration Management** in [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).
- [ ] Review the activities outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
