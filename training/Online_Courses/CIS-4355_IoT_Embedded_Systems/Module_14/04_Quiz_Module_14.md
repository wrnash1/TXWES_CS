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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **time-series data**?
C) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
B) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **time-series data**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **time-series data**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **time-series data**.
    * *Why A is correct:* This describes the exact role and function of **time-series data**.


---

**Question 3**
A systems administrator or developer needs to **verify the active status and resource usage of the background service daemon**. Which of the following commands is the most appropriate to execute?
B) terraform validate
A) systemctl status iot_service
C) docker-compose up -d
D) git log --oneline -n 5
*   **Correct Answer:** A) systemctl status iot_service
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl status iot_service` command is directly designed to verify the active status and resource usage of the background service daemon.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Analyzing Telemetry Data** in a production environment, you encounter a system alert indicating a **Dependency Bottleneck** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Re-assign resources to critical path tasks and establish clear communication protocols.
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
D) Reboot the physical machine and wait for services to reload.
C) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Correct Answer:** A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Distractor Analysis:**
    * *Why A is correct:* Because A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline. The appropriate fix is to Re-assign resources to critical path tasks and establish clear communication protocols..
    * *Why B is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why D is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why C is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.


---

**Question 5**
When designing a system for **Analyzing Telemetry Data**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.

