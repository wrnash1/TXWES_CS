# Quiz: Module 03 - Embedded Programming C/C++
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Why is static memory allocation preferred over dynamic allocation (malloc) in high-reliability embedded systems?
*   A) Static memory runs slower
*   B) Dynamic allocation risks heap fragmentation and runtime memory exhaustion (out-of-memory crashes)
*   C) C does not support dynamic allocation
*   D) Pointers are not allowed
*   **Correct Answer:** B) Microcontrollers have tiny RAM capacities; heap fragmentation can trigger unpredictable system crashes during long-term runs.
*   **Distractor Analysis:**
    *   *Why correct:* Microcontrollers have tiny RAM capacities; heap fragmentation can trigger unpredictable system crashes during long-term runs.
    *   Dynamic memory is supported in C but highly restricted in embedded code.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **pointers**?
C) The descendant node connected to the left branch of a parent node in a binary tree structure.
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **pointers**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **pointers**.
    * *Why A is correct:* This describes the exact role and function of **pointers**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **pointers**.


---

**Question 3**
A systems administrator or developer needs to **review the last five project commits in a concise single-line format**. Which of the following commands is the most appropriate to execute?
A) git log --oneline -n 5
D) systemctl status iot_service
B) docker-compose up -d
C) terraform validate
*   **Correct Answer:** A) git log --oneline -n 5
*   **Distractor Analysis:**
    * *Why A is correct:* The `git log --oneline -n 5` command is directly designed to review the last five project commits in a concise single-line format.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Embedded Programming C/C++** in a production environment, you encounter a system alert indicating a **Scope Exceeded Budget Limit** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Implement strict change control boards (CCB) and re-baseline the project constraints.
C) Re-assign resources to critical path tasks and establish clear communication protocols.
B) Optimize service resources, implement load balancing, or update failover mechanisms.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Implement strict change control boards (CCB) and re-baseline the project constraints.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The project scope expanded during execution without adjusting budget or schedule allocations. The appropriate fix is to Implement strict change control boards (CCB) and re-baseline the project constraints..
    * *Why C is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.
    * *Why B is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.
    * *Why D is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.


---

**Question 5**
When designing a system for **Embedded Programming C/C++**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.

