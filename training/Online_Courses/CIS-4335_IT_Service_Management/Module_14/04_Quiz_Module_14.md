# Quiz: Module 14 - Practices: Release & Deployment Management
## Course: CIS-4335_IT_Service_Management (ITIL 4 Foundation)

---

**Question 1**
Which practice is responsible for moving new or changed components to live environments?
*   A) Release Management
*   B) Deployment Management
*   C) Service Configuration Management
*   D) Change Enablement
*   **Correct Answer:** B) Deployment Management physically moves code/hardware to live environments. Release makes services available to users.
*   **Distractor Analysis:**
    *   *Why correct:* Deployment Management physically moves code/hardware to live environments. Release makes services available to users.
    *   Release is the logical rollout. Deployment is the technical move.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Release packages**?
C) The uncontrolled growth or changes to a project's scope without adjustments to time, cost, and resources.
D) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
B) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Release packages**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Release packages**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Release packages**.
    * *Why A is correct:* This describes the exact role and function of **Release packages**.


---

**Question 3**
A systems administrator or developer needs to **review the last five project commits in a concise single-line format**. Which of the following commands is the most appropriate to execute?
B) systemctl status iot_service
C) terraform validate
D) docker-compose up -d
A) git log --oneline -n 5
*   **Correct Answer:** A) git log --oneline -n 5
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git log --oneline -n 5` command is directly designed to review the last five project commits in a concise single-line format.


---

**Question 4**
While working on **Practices: Release & Deployment Management** in a production environment, you encounter a system alert indicating a **SLA Breach Alert** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Re-assign resources to critical path tasks and establish clear communication protocols.
A) Optimize service resources, implement load balancing, or update failover mechanisms.
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why A is correct:* Because A system outage or slow response time has exceeded the limits guaranteed in the Service Level Agreement. The appropriate fix is to Optimize service resources, implement load balancing, or update failover mechanisms..
    * *Why B is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why D is incorrect:* This action does not resolve the root cause of SLA Breach Alert.


---

**Question 5**
When designing a system for **Practices: Release & Deployment Management**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
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

