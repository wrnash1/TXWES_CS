# Reading Guide: Module 12 - Technical Management Practices - Deployment Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

### Introduction
Welcome to **Module 12 - Technical Management Practices: Deployment Management**! Deployment Management is the ITIL 4 practice responsible for moving new or changed hardware, software, documentation, processes, or any other component to live environments. Understanding Deployment Management is essential for the Foundation exam, particularly because it is frequently confused with Change Enablement and Release Management — two closely related but distinct practices.

As a student, you will learn the specific purpose and scope of Deployment Management, how it connects to Change Enablement and Release Management, common deployment approaches, and how deployment risks are managed. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ITIL 4 Foundation exam expects you to know these concepts precisely:

*   **Deployment Management**: The ITIL 4 practice whose purpose is to move new or changed hardware, software, documentation, processes, or any other component to live environments. Deployment Management focuses on the physical or logical act of moving components — it is distinct from the authorization process (Change Enablement) and from the release packaging process (Release Management).
*   **Deployment**: The activity of moving a new or changed component into a live environment. Deployments may be discrete events (a single release at a scheduled time) or continuous (components deployed automatically as soon as they pass testing in a CI/CD pipeline).
*   **Continuous Integration / Continuous Delivery (CI/CD)**: A software engineering approach in which code changes are automatically built, tested, and deployed to live or pre-production environments. CI/CD pipelines reduce deployment risk by keeping changes small and frequent, enabling rapid feedback.
*   **Release**: A version of a service or other configuration item made available for use. A release may include one or more changes and is managed by Release Management. Deployment Management then moves that release into the live environment.
*   **Phased Deployment**: A deployment approach where a new version is rolled out gradually — first to a small subset of users or infrastructure, then progressively expanded. This limits blast radius if issues emerge and allows the organization to validate the deployment in production conditions before full rollout.
*   **Big Bang Deployment**: A deployment approach where a new version replaces the old one entirely for all users at once. Higher risk than phased deployment but simpler to coordinate. Sometimes unavoidable when components are tightly coupled.
*   **Rollback**: The process of reverting to a previous version of a service or component if a deployment causes issues in the live environment. Having a tested rollback plan is a key deployment risk mitigation strategy.

---

### 2. Certification Exam Tips
*   **Deployment Management vs. Change Enablement:** A critical exam distinction. Change Enablement assesses risk and authorizes the change — it governs whether a change may proceed. Deployment Management physically moves the component into the live environment — it governs how the change arrives. These are separate practices.
*   **Deployment Management vs. Release Management:** Release Management packages and schedules releases (which changes are bundled together and when). Deployment Management executes the move to live. Think of Release Management as preparing the package and Deployment Management as delivering it.
*   **Deployment Approaches Are Tested:** The exam tests knowledge of big bang versus phased versus continuous deployment. Know the risk profile of each: phased reduces blast radius; big bang is simpler but higher risk; continuous deployment (CI/CD) enables rapid, low-risk incremental changes.
*   **Rollback Planning Is Part of Deployment:** A good deployment plan always includes a tested rollback procedure. The exam may present scenarios where a deployment fails and ask what should have been prepared in advance.
*   **Deployment Can Be Automated:** Modern deployment pipelines automate component movement to live environments. ITIL 4 explicitly supports automation as part of the "Optimize and Automate" guiding principle.
*   **Study Resource:** The Axelos ITIL 4 Foundation resources at [https://www.axelos.com/certifications/itil-service-management/itil-4-foundation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) include official definitions for Deployment Management and its relationship to Release Management and Change Enablement.
*   **Video Resource:** The [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W) on YouTube includes a dedicated video on Deployment Management covering deployment approaches, CI/CD, and exam scenario examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapter covering **Deployment Management** in the OER Textbook: [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/). Focus on the purpose of the practice, deployment approaches, and the relationship to Change Enablement and Release Management.
*   **Required Video:** Watch the video lecture on **Deployment Management** in the official course playlist: [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).

---

### Lab & Command Integration
In this week's hands-on lab, you will apply these concepts in the following activities:
*   **Compare deployment approaches**: Given three deployment scenarios of varying scale and risk, select the most appropriate deployment approach (big bang, phased, or continuous) for each, and justify your selection using ITIL 4 Deployment Management principles.
*   **Draft a deployment plan**: Using a provided template, create a deployment plan for a medium-complexity software release — including pre-deployment checks, deployment steps, post-deployment validation, and a rollback procedure.
*   **Map the Change-Release-Deployment workflow**: For a given scenario involving a new application feature, trace the workflow from change authorization (Change Enablement) through release packaging (Release Management) to deployment execution (Deployment Management), identifying the boundary between each practice's responsibilities.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the definitions of deployment, release, phased deployment, big bang deployment, and rollback.
- [ ] Read the chapter covering **Deployment Management** in [ITIL 4 Foundation Study Notes & Overviews](https://www.axelos.com/).
- [ ] Watch the video lecture on **Deployment Management** in [ITIL 4 Foundation Certification Complete Course Playlist](https://www.youtube.com/playlist?list=PLK-tWc9i-GZ5V68tH3pB2rWn3Bv-yP85W).
- [ ] Review the activities outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
