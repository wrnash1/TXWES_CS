# Reading Guide: Module 13 - Service Management Practices - Service Request Management and Release Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

### Introduction
Welcome to **Module 13 - Service Management Practices: Service Request Management and Release Management**! This module covers two distinct but related practices. Service Request Management handles the fulfillment of planned, expected user requests — a separate stream from incident handling. Release Management governs how new or changed services are packaged, tested, and made ready for deployment. Both practices are tested on the ITIL 4 Foundation exam, and distinguishing them from related practices (Incident Management, Change Enablement, Deployment Management) is a key exam skill.

As a student, you will learn the purpose of each practice, what distinguishes service requests from incidents, how Release Management prepares releases for deployment, and how these practices connect to the broader service value chain. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ITIL 4 Foundation exam expects you to know these concepts precisely:

*   **Service Request Management**: The ITIL 4 practice whose purpose is to support the agreed quality of a service by handling all predefined, user-initiated service requests in an effective and user-friendly manner. Service requests are normal, planned parts of service delivery — not disruptions. Examples include password resets, software installations, and requests for information.
*   **Service Request**: A formal request from a user for something to be provided — information, advice, access to a service, or a standard service activity such as provisioning a new user account. Service requests are pre-approved and expected, and do not require the same assessment as incidents or changes.
*   **Request Catalog**: A structured list of all service requests that users can raise, typically published in a self-service portal. The request catalog helps users understand what they can ask for and sets clear expectations for fulfillment timeframes.
*   **Release**: A version of a service or other configuration item (CI) that is made available for use. A release may contain one or more changes and is typically tested and validated before being handed to Deployment Management for movement to the live environment.
*   **Release Management**: The ITIL 4 practice whose purpose is to make new and changed services and features available for use. Release Management plans, tests, and prepares releases — it does not deploy them to live (that is Deployment Management's role).
*   **Release Policy**: An organization's documented rules for how releases are structured, tested, approved, and scheduled. A release policy helps ensure consistency in how releases are prepared and reduces the risk of poorly tested components reaching live environments.

---

### 2. Certification Exam Tips
*   **Service Request vs. Incident:** The most common exam trap in this practice area. Service requests are planned, normal, pre-approved activities. Incidents are unplanned disruptions. A password reset is a service request; a system crash is an incident. Know this distinction cold.
*   **Service Request Management Is Not Change Enablement:** Routine service requests are pre-approved and do not require the change authorization process. Only requests that result in changes to infrastructure or services requiring assessment feed into Change Enablement.
*   **Release vs. Deployment:** Release Management prepares the release (what is included, testing, readiness). Deployment Management moves it to live. These are two distinct practices with sequential responsibilities.
*   **Request Catalog Reduces Contact Volume:** The exam tests that a well-maintained request catalog with clear self-service options reduces contact volume to the Service Desk, supporting the shift-left strategy.
*   **Releases Can Bundle Multiple Changes:** A single release may include multiple authorized changes. Release Management decides what is grouped together and when the release is scheduled.
*   **Study Resource:** The Axelos ITIL 4 Foundation resources at [https://www.axelos.com/certifications/itil-service-management/itil-4-foundation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) include the official glossary definitions for Service Request Management, Release Management, service request, and release.
*   **Video Resource:** The [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W) on YouTube includes dedicated videos on both Service Request Management and Release Management with exam scenario examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters covering **Service Request Management** and **Release Management** in the OER Textbook: [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/). Focus on the purpose of each practice, the distinction between service requests and incidents, and the release-to-deployment workflow.
*   **Required Video:** Watch the video lectures on **Service Request Management** and **Release Management** in the official course playlist: [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply these concepts in the following activities:
*   **Classify a ticket queue**: Given a list of fifteen IT tickets, classify each as an incident, service request, or change request. For the service requests, identify whether they are pre-approved standard requests or whether they require additional assessment.
*   **Design a release plan**: Using a provided template, draft a release plan for a set of three authorized changes being bundled into a single release — including scope, testing approach, release readiness criteria, and handoff to Deployment Management.
*   **Build a request catalog entry**: Draft a request catalog entry for a common service request (such as new user account provisioning) — including the description, fulfillment steps, expected timeframe, and any pre-approvals in place.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the definitions of service request, release, and the distinction between Service Request Management, Release Management, and Deployment Management.
- [ ] Read the chapters covering **Service Request Management** and **Release Management** in [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/).
- [ ] Watch the video lectures on **Service Request Management** and **Release Management** in [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).
- [ ] Review the activities outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
