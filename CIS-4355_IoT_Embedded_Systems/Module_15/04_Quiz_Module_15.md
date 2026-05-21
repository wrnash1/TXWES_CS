# Quiz: Module 15 - Secure IoT Network Architecture
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Which design principle recommends securing an IoT system at the device level, the network level, and the cloud application level?
*   A) Single Point of Failure
*   B) Defense in Depth (End-to-End Security)
*   C) Simple Access Controls
*   D) Direct Interface Trust
*   **Correct Answer:** B) Defense-in-depth ensures that if a control fails at one layer (e.g. Wi-Fi security), other layers (e.g. device auth, TLS) protect the system.
*   **Distractor Analysis:**
    *   *Why correct:* Defense-in-depth ensures that if a control fails at one layer (e.g. Wi-Fi security), other layers (e.g. device auth, TLS) protect the system.
    *   Direct interface trust assumes elements inside are safe, which is a security risk.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **device lifecycle management**?
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
B) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **device lifecycle management**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **device lifecycle management**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **device lifecycle management**.
    * *Why A is correct:* This describes the exact role and function of **device lifecycle management**.


---

**Question 3**
A systems administrator or developer needs to **verify the active status and resource usage of the background service daemon**. Which of the following commands is the most appropriate to execute?
C) docker-compose up -d
D) terraform validate
B) git log --oneline -n 5
A) systemctl status iot_service
*   **Correct Answer:** A) systemctl status iot_service
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl status iot_service` command is directly designed to verify the active status and resource usage of the background service daemon.


---

**Question 4**
While working on **Secure IoT Network Architecture** in a production environment, you encounter a system alert indicating a **Dependency Bottleneck** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
A) Re-assign resources to critical path tasks and establish clear communication protocols.
D) Reboot the physical machine and wait for services to reload.
C) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Correct Answer:** A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why A is correct:* Because A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline. The appropriate fix is to Re-assign resources to critical path tasks and establish clear communication protocols..
    * *Why D is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why C is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.


---

**Question 5**
When designing a system for **Secure IoT Network Architecture**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.

