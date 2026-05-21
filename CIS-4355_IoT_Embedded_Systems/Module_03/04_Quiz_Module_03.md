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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **registers mapping**?
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
C) A project management technique that identifies the sequence of dependent tasks that determines the shortest time to complete a project.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
B) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **registers mapping**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **registers mapping**.
    * *Why A is correct:* This describes the exact role and function of **registers mapping**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **registers mapping**.


---

**Question 3**
A systems administrator or developer needs to **launch all application services in the background using docker-compose configuration**. Which of the following commands is the most appropriate to execute?
A) docker-compose up -d
D) git log --oneline -n 5
B) systemctl status iot_service
C) terraform validate
*   **Correct Answer:** A) docker-compose up -d
*   **Distractor Analysis:**
    * *Why A is correct:* The `docker-compose up -d` command is directly designed to launch all application services in the background using docker-compose configuration.
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
When designing a system for **Embedded Programming C/C++**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
B) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why A is correct:* Implementing Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services. mitigates the risk of A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.

