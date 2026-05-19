# Quiz: Module 06 - Data Modeling (ERD)
## Course: CIS-3312_Systems_Analysis_Design (IIBA Entry Certificate in Business Analysis (ECBA))

---

**Question 1**
How must a many-to-many (M:N) relationship between two database entities be resolved in relational database design?
*   A) Using a direct foreign key link
*   B) Creating an associative (junction) entity that links both tables using 1:N relationships
*   C) Combining both tables
*   D) Deleting one of the entities
*   **Correct Answer:** B) Relational engines do not support direct M:N tables; an associative entity maps many-to-many links through two one-to-many relations.
*   **Distractor Analysis:**
    *   *Why correct:* Relational engines do not support direct M:N tables; an associative entity maps many-to-many links through two one-to-many relations.
    *   Direct keys only map 1:1 or 1:N linkages.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **attributes**?
C) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
D) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **attributes**.
    * *Why A is correct:* This describes the exact role and function of **attributes**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **attributes**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **attributes**.


---

**Question 3**
A systems administrator or developer needs to **review the last five project commits in a concise single-line format**. Which of the following commands is the most appropriate to execute?
D) docker-compose up -d
B) terraform validate
A) git log --oneline -n 5
C) systemctl status iot_service
*   **Correct Answer:** A) git log --oneline -n 5
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git log --oneline -n 5` command is directly designed to review the last five project commits in a concise single-line format.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Modeling (ERD)** in a production environment, you encounter a system alert indicating a **Dependency Bottleneck** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
C) Optimize service resources, implement load balancing, or update failover mechanisms.
A) Re-assign resources to critical path tasks and establish clear communication protocols.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why C is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why A is correct:* Because A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline. The appropriate fix is to Re-assign resources to critical path tasks and establish clear communication protocols..
    * *Why D is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.


---

**Question 5**
When designing a system for **Data Modeling (ERD)**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
B) Establish formal authorization procedures and digital signatures for all project scope modifications.
D) Enable full disk encryption on all client endpoints.
A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why A is correct:* Implementing Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services. mitigates the risk of A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented..
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.

