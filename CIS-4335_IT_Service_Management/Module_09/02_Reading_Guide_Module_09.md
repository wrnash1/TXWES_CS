# Reading Guide: Module 09 - Service Management Practices - Problem Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

### Introduction
Welcome to **Module 09 - Service Management Practices: Problem Management**! While Incident Management focuses on restoring service quickly, Problem Management addresses the underlying causes of incidents to prevent recurrence. Together, these two practices form the backbone of operational stability in ITIL 4. This module covers the purpose of Problem Management, the problem lifecycle, root cause analysis, and key concepts such as known errors and workarounds.

As a student, you will learn the distinction between problems, incidents, and known errors, understand how the problem lifecycle progresses from identification through resolution, and explore how Problem Management connects to Incident Management and Change Enablement. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ITIL 4 Foundation exam expects you to know these concepts precisely:

*   **Problem**: A cause, or potential cause, of one or more incidents. Problems are identified when the same or similar incidents recur, or when a single high-impact incident warrants investigation into root cause. A problem remains open until the root cause is permanently resolved or the risk is formally accepted.
*   **Problem Management**: The ITIL 4 practice whose purpose is to reduce the likelihood and impact of incidents by identifying actual and potential causes of incidents, and managing workarounds and known errors. It operates in three modes: reactive (investigating after incidents occur), proactive (identifying risks before incidents occur), and error control (managing known errors until permanent fixes are applied).
*   **Known Error**: A problem that has been analyzed and for which the root cause is understood, but for which a permanent resolution has not yet been implemented. Known errors are documented in the Known Error Database so that service desk staff can apply workarounds efficiently without re-diagnosing the same issue.
*   **Known Error Database (KEDB)**: A repository that stores known error records, including root cause information and documented workarounds. The KEDB enables faster incident resolution by giving service desk staff access to proven workarounds for recurring issues.
*   **Root Cause Analysis (RCA)**: The structured process of identifying the fundamental cause of a problem — the underlying reason why incidents occurred. Common RCA techniques include the "5 Whys," fishbone (Ishikawa) diagrams, and fault tree analysis.
*   **Workaround**: A temporary measure that reduces or eliminates the impact of an incident or problem when a permanent fix is not yet available. A workaround does not resolve the underlying cause — the problem record remains open until a permanent solution is implemented.
*   **Error Control**: The Problem Management activity that manages known errors from identification through permanent resolution. Error control monitors known errors, assesses the risk and cost of applying a fix versus accepting the error, and coordinates with Change Enablement when a change is needed to implement the permanent fix.

---

### 2. Certification Exam Tips
*   **Problem vs. Incident vs. Known Error:** Three closely related terms that the exam distinguishes precisely. An incident is the disruption experienced by users; a problem is the underlying cause; a known error is a problem whose cause is understood but not yet permanently fixed. Know these three in order.
*   **Problem Management Has Three Modes:** The exam tests that Problem Management is not purely reactive. It also operates proactively (identifying risks before incidents occur) and through error control (managing known errors). Know all three modes by name.
*   **KEDB Enables Faster Incident Resolution:** A common exam scenario asks which tool helps the service desk resolve recurring incidents faster. The answer is the KEDB — it provides documented workarounds so staff do not need to re-diagnose known issues every time they recur.
*   **Workaround Closes the Incident, Not the Problem:** When a workaround is applied to restore service, the incident can be closed — but the problem record remains open until a permanent fix is implemented. This is one of the most commonly tested distinctions in Problem Management.
*   **Problem Management and Change Enablement Interact:** When root cause analysis identifies a fix that requires a change to infrastructure or a service, Problem Management raises a change request through Change Enablement. Problem Management does not implement changes directly.
*   **Study Resource:** The Axelos ITIL 4 Foundation resources at [https://www.axelos.com/certifications/itil-service-management/itil-4-foundation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) include the official glossary definitions for problem, known error, and the KEDB.
*   **Video Resource:** The [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W) on YouTube includes a dedicated video on Problem Management covering the problem lifecycle, known errors, and exam scenario examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapter covering **Problem Management** in the OER Textbook: [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/). Focus on the purpose of the practice, the three modes, the problem lifecycle, and the KEDB.
*   **Required Video:** Watch the video lecture on **Problem Management** in the official course playlist: [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply these concepts in the following activities:
*   **Conduct a root cause analysis**: Given a case study describing a recurring service outage, apply the "5 Whys" technique to trace the incident back to its root cause and document your findings in a problem record.
*   **Create a Known Error record**: Using a provided KEDB template, document a known error for the root cause identified in the RCA — including a description of the error, the impact, the documented workaround, and the status of the permanent fix.
*   **Map the problem lifecycle**: For a given scenario, identify which Problem Management activity is occurring at each stage — problem identification, problem control, and error control — and explain how each stage interacts with Incident Management and Change Enablement.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the definitions of problem, known error, KEDB, and workaround.
- [ ] Read the chapter covering **Problem Management** in [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/).
- [ ] Watch the video lecture on **Problem Management** in [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).
- [ ] Review the activities outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
