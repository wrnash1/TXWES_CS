# Quiz: Module 14 - Analyzing Telemetry Data
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Which database type is optimized specifically for storing and querying continuous streams of sensor data tagged with timestamps?
*   A) Relational Database (SQL)
*   B) Time-Series Database (TSDB)
*   C) Graph Database
*   D) Key-Value Store
*   **Correct Answer:** B) TSDBs (e.g. InfluxDB) are optimized for sequential write speeds and calculating moving averages over time windows.
*   **Distractor Analysis:**
    *   *Why correct:* TSDBs (e.g. InfluxDB) are optimized for sequential write speeds and calculating moving averages over time windows.
    *   Graph databases track node linkages. Key-value stores hold configuration data.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Data streams**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
C) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
D) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Data streams**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Data streams**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Data streams**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Data streams**.


---

**Question 3**
A systems administrator or developer needs to **review the last five project commits in a concise single-line format**. Which of the following commands is the most appropriate to execute?
D) docker-compose up -d
A) git log --oneline -n 5
B) systemctl status iot_service
C) terraform validate
*   **Correct Answer:** A) git log --oneline -n 5
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git log --oneline -n 5` command is directly designed to review the last five project commits in a concise single-line format.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Analyzing Telemetry Data** in a production environment, you encounter a system alert indicating a **Dependency Bottleneck** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize service resources, implement load balancing, or update failover mechanisms.
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
D) Reboot the physical machine and wait for services to reload.
A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Correct Answer:** A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why B is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why D is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why A is correct:* Because A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline. The appropriate fix is to Re-assign resources to critical path tasks and establish clear communication protocols..


---

**Question 5**
When designing a system for **Analyzing Telemetry Data**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.

