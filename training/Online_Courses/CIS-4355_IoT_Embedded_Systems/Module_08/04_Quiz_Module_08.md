# Quiz: Module 08 - Embedded Security Threats
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
According to the OWASP IoT Top 10, which vulnerability is historically the most exploited entry point for building device botnets?
*   A) SQL Injection
*   B) Use of hardcoded, weak, or default credentials
*   C) High CPU temperatures
*   D) Missing code comments
*   **Correct Answer:** B) Default telnet/SSH credentials allow automated scripts to brute-force devices and load malicious botnet scripts.
*   **Distractor Analysis:**
    *   *Why correct:* Default telnet/SSH credentials allow automated scripts to brute-force devices and load malicious botnet scripts.
    *   IoT devices rarely host relational SQL databases.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **physical tampering**?
C) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
D) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
B) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **physical tampering**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **physical tampering**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **physical tampering**.
    * *Why A is correct:* This describes the exact role and function of **physical tampering**.


---

**Question 3**
A systems administrator or developer needs to **launch all application services in the background using docker-compose configuration**. Which of the following commands is the most appropriate to execute?
A) docker-compose up -d
D) git log --oneline -n 5
C) terraform validate
B) systemctl status iot_service
*   **Correct Answer:** A) docker-compose up -d
*   **Distractor Analysis:**
    * *Why A is correct:* The `docker-compose up -d` command is directly designed to launch all application services in the background using docker-compose configuration.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Embedded Security Threats** in a production environment, you encounter a system alert indicating a **Dependency Bottleneck** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize service resources, implement load balancing, or update failover mechanisms.
D) Reboot the physical machine and wait for services to reload.
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Correct Answer:** A) Re-assign resources to critical path tasks and establish clear communication protocols.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why D is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why B is incorrect:* This action does not resolve the root cause of Dependency Bottleneck.
    * *Why A is correct:* Because A critical task is blocked by a delayed prerequisite task, stalling the entire project timeline. The appropriate fix is to Re-assign resources to critical path tasks and establish clear communication protocols..


---

**Question 5**
When designing a system for **Embedded Security Threats**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
B) Establish formal authorization procedures and digital signatures for all project scope modifications.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why A is correct:* Implementing Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services. mitigates the risk of A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented..
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.

