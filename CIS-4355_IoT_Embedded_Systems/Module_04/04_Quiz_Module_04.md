# Quiz: Module 04 - RTOS Concepts
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What is the defining characteristic of a Real-Time Operating System (RTOS)?
*   A) It features a graphical user interface
*   B) It guarantees deterministic, predictable task execution and meeting timing constraints
*   C) It requires massive hard drive spaces
*   D) It only supports web servers
*   **Correct Answer:** B) RTOS priority-driven scheduling guarantees that critical tasks complete within strict deadlines.
*   **Distractor Analysis:**
    *   *Why correct:* RTOS priority-driven scheduling guarantees that critical tasks complete within strict deadlines.
    *   RTOS environments are minimal and rarely include graphical UI systems.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **preemptive kernels**?
B) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
C) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
D) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **preemptive kernels**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **preemptive kernels**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **preemptive kernels**.
    * *Why A is correct:* This describes the exact role and function of **preemptive kernels**.


---

**Question 3**
A systems administrator or developer needs to **verify the active status and resource usage of the background service daemon**. Which of the following commands is the most appropriate to execute?
C) terraform validate
A) systemctl status iot_service
B) docker-compose up -d
D) git log --oneline -n 5
*   **Correct Answer:** A) systemctl status iot_service
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl status iot_service` command is directly designed to verify the active status and resource usage of the background service daemon.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **RTOS Concepts** in a production environment, you encounter a system alert indicating a **Dependency Bottleneck** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Optimize service resources, implement load balancing, or update failover mechanisms.
D) Reboot the physical machine and wait for services to reload.
C) Implement strict change control boards (CCB) and re-baseline the project constraints.
A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Correct Answer:** A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why D is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why C is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why A is correct:* Because A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline. The appropriate fix is to Re-assign resources to critical path tasks and establish clear communication protocols..


---

**Question 5**
When designing a system for **RTOS Concepts**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..

