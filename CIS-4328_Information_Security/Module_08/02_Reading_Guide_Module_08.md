# Reading Guide: Module 08 - Identity and Access Management (IAM)
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 08 – Identity and Access Management (IAM)**! IAM is the discipline that governs who can access what resources, under what conditions, and with what level of privilege. SY0-701 tests IAM concepts heavily in Domain 2 (Threats, Vulnerabilities, and Mitigations) and Domain 3 (Security Architecture) — expect scenario questions about access control models, privilege abuse, and account lifecycle management.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Least Privilege**: A foundational security principle requiring that every user, process, or system account be granted only the minimum permissions necessary to perform its assigned function — and nothing more. Violating least privilege is the primary enabler of insider threats and privilege escalation attacks. SY0-701 frequently tests least privilege in scenarios involving account reviews, privilege creep, and separation of duties.
*   **Separation of Duties (SoD)**: An access control principle that divides critical tasks among multiple individuals so that no single person can complete a sensitive operation alone. For example, the person who requests a payment cannot also approve it. SoD reduces the risk of fraud, sabotage, and unintentional errors in high-stakes processes.
*   **Role-Based Access Control (RBAC)**: An access control model that assigns permissions to roles (e.g., "Network Admin," "HR Manager") rather than to individual users. Users inherit permissions by being assigned to roles, which simplifies administration and enforces least privilege by job function. RBAC is the most common enterprise access control model tested on SY0-701.
*   **Attribute-Based Access Control (ABAC)**: An access control model that grants or denies access based on a combination of attributes — user attributes (department, clearance level), resource attributes (classification, owner), and environmental attributes (time of day, location). ABAC is more flexible and granular than RBAC and is used in Zero Trust architectures.
*   **Provisioning and Deprovisioning**: The processes for creating, configuring, and granting access to user accounts (provisioning) and for disabling, revoking, and removing access when a user no longer needs it (deprovisioning). Failure to deprovision accounts promptly — particularly for terminated employees — is a leading cause of account-based breaches and is a key SY0-701 scenario topic.
*   **Privileged Access Management (PAM)**: A security discipline and toolset that controls, monitors, and audits the use of privileged accounts (administrator, root, service accounts). PAM solutions enforce just-in-time (JIT) access, session recording, and credential vaulting to reduce the attack surface of high-privilege accounts. SY0-701 tests PAM in scenarios involving insider threats, third-party vendor access, and credential theft.

---

### 2. Certification Exam Tips
*   **Domain Weight:** IAM falls primarily under **Domain 2 – Threats, Vulnerabilities, and Mitigations (22%)** and **Domain 3 – Security Architecture (18%)** of SY0-701. Expect scenario questions requiring you to select the correct access control model or identify the IAM failure that enabled an attack.
*   **RBAC vs. ABAC Trap:** RBAC grants access by job role — it is simple and widely used. ABAC grants access based on multiple attributes and supports conditional policies ("allow access only if user is in Finance AND connecting from the corporate network AND it is between 8 AM–6 PM"). If a scenario requires dynamic, context-aware access decisions, ABAC is the answer.
*   **Least Privilege vs. Need-to-Know:** Least privilege is the broader principle (minimum permissions for the job). Need-to-know is a stricter application used in classified/sensitive environments where even authorized users are restricted to only the specific data relevant to their current task.
*   **Account Lifecycle Scenarios:** SY0-701 tests every phase: provisioning (new employee onboarding), access reviews (periodic privilege audits to detect privilege creep), and deprovisioning (termination, role change). If a question describes an attacker using a terminated employee's credentials, the failure is inadequate deprovisioning.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include access control model comparison charts and account lifecycle diagrams that map directly to SY0-701 scenario questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Identity and Access Management" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on access control models (MAC, DAC, RBAC, ABAC, Rule-Based) and the account lifecycle.
*   **Required Video:** Watch the IAM video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos walk through access control model comparisons and real-world privilege escalation scenarios.

---

### Lab & Command Integration
In this week's hands-on lab, you will review user account privileges, simulate role assignment in an RBAC model, and practice identifying privilege creep in a sample account audit. Understanding how to read and interpret access control lists (ACLs) and role assignments is a direct SY0-701 performance-based question skill.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to select the correct access control model for any given scenario.
- [ ] Read the "Identity and Access Management" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the IAM video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: RBAC = role-based; ABAC = attribute/context-based; Least Privilege = minimum necessary; SoD = split critical tasks.
- [ ] Proceed to the weekly hands-on lab activity.
