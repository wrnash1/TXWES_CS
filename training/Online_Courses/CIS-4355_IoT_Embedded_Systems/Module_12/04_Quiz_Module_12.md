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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **anonymization techniques**?
B) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
C) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
D) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **anonymization techniques**.
    * *Why A is correct:* This describes the exact role and function of **anonymization techniques**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **anonymization techniques**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **anonymization techniques**.


---

**Question 3**
A systems administrator or developer needs to **review the last five project commits in a concise single-line format**. Which of the following commands is the most appropriate to execute?
C) systemctl status iot_service
A) git log --oneline -n 5
D) docker-compose up -d
B) terraform validate
*   **Correct Answer:** A) git log --oneline -n 5
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `git log --oneline -n 5` command is directly designed to review the last five project commits in a concise single-line format.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Privacy in IoT Networks** in a production environment, you encounter a system alert indicating a **SLA Breach Alert** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Implement strict change control boards (CCB) and re-baseline the project constraints.
A) Optimize service resources, implement load balancing, or update failover mechanisms.
B) Re-assign resources to critical path tasks and establish clear communication protocols.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why A is correct:* Because A system outage or slow response time has exceeded the limits guaranteed in the Service Level Agreement. The appropriate fix is to Optimize service resources, implement load balancing, or update failover mechanisms..
    * *Why B is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why D is incorrect:* This action does not resolve the root cause of SLA Breach Alert.


---

**Question 5**
When designing a system for **Data Privacy in IoT Networks**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
B) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Correct Answer:** A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why A is correct:* Implementing Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services. mitigates the risk of A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented..

