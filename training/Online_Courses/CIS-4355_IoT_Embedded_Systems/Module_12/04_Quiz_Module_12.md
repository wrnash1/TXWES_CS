# Quiz: Module 12 - Data Privacy in IoT Networks
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What risk is presented by storing unencrypted device telemetry logs in a cloud database?
*   A) Logs run out of space
*   B) Unauthorized parties can read sensitive location or activity data during a database breach
*   C) Databases cannot index logs
*   D) The CPU utilization increases
*   **Correct Answer:** B) Telemetry data can contain sensitive information (GPS, power consumption). Encryption protects it from data leaks.
*   **Distractor Analysis:**
    *   *Why correct:* Telemetry data can contain sensitive information (GPS, power consumption). Encryption protects it from data leaks.
    *   It is a confidentiality risk, not a database index limit.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Sensor privacy**?
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
D) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Sensor privacy**.
    * *Why A is correct:* This describes the exact role and function of **Sensor privacy**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Sensor privacy**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Sensor privacy**.


---

**Question 3**
A systems administrator or developer needs to **verify the active status and resource usage of the background service daemon**. Which of the following commands is the most appropriate to execute?
A) systemctl status iot_service
D) git log --oneline -n 5
B) terraform validate
C) docker-compose up -d
*   **Correct Answer:** A) systemctl status iot_service
*   **Distractor Analysis:**
    * *Why A is correct:* The `systemctl status iot_service` command is directly designed to verify the active status and resource usage of the background service daemon.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Privacy in IoT Networks** in a production environment, you encounter a system alert indicating a **SLA Breach Alert** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize service resources, implement load balancing, or update failover mechanisms.
B) Re-assign resources to critical path tasks and establish clear communication protocols.
D) Reboot the physical machine and wait for services to reload.
C) Implement strict change control boards (CCB) and re-baseline the project constraints.
*   **Correct Answer:** A) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Distractor Analysis:**
    * *Why A is correct:* Because A system outage or slow response time has exceeded the limits guaranteed in the Service Level Agreement. The appropriate fix is to Optimize service resources, implement load balancing, or update failover mechanisms..
    * *Why B is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why D is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why C is incorrect:* This action does not resolve the root cause of SLA Breach Alert.


---

**Question 5**
When designing a system for **Data Privacy in IoT Networks**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
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

