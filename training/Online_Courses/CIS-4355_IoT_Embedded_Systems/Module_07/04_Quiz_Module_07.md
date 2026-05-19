# Quiz: Module 07 - Cloud IoT Gateways
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What is the primary function of a Cloud IoT Gateway?
*   A) To compile device firmware binaries
*   B) To authenticate devices securely and ingest massive streams of telemetry data into cloud systems
*   C) To host web client pages
*   D) To execute local physical tasks
*   **Correct Answer:** B) Cloud IoT Gateways provide the connection bridge, managing client device security certificates and ingesting raw sensor metrics.
*   **Distractor Analysis:**
    *   *Why correct:* Cloud IoT Gateways provide the connection bridge, managing client device security certificates and ingesting raw sensor metrics.
    *   Gateways route messages, they do not write compiled firmware.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **device identity**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
C) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
B) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
D) The uncontrolled growth or changes to a project's scope without adjustments to time, cost, and resources.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **device identity**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **device identity**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **device identity**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **device identity**.


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
While working on **Cloud IoT Gateways** in a production environment, you encounter a system alert indicating a **SLA Breach Alert** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize service resources, implement load balancing, or update failover mechanisms.
B) Re-assign resources to critical path tasks and establish clear communication protocols.
C) Implement strict change control boards (CCB) and re-baseline the project constraints.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Distractor Analysis:**
    * *Why A is correct:* Because A system outage or slow response time has exceeded the limits guaranteed in the Service Level Agreement. The appropriate fix is to Optimize service resources, implement load balancing, or update failover mechanisms..
    * *Why B is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why C is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why D is incorrect:* This action does not resolve the root cause of SLA Breach Alert.


---

**Question 5**
When designing a system for **Cloud IoT Gateways**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.

