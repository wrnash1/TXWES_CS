# Quiz: Module 09 - Cryptography in Constrained Devices
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Why is symmetric cryptography (like AES) preferred over asymmetric cryptography (like RSA) for securing sensor data transmissions directly on microcontrollers?
*   A) Symmetric crypto does not require keys
*   B) Asymmetric math is highly resource-intensive and computationally expensive for low-power CPUs
*   C) Symmetric crypto is not secure
*   D) Asymmetric is only allowed on servers
*   **Correct Answer:** B) AES utilizes lightweight bitwise operations that execute quickly on small chips with minimal RAM and power.
*   **Distractor Analysis:**
    *   *Why correct:* AES utilizes lightweight bitwise operations that execute quickly on small chips with minimal RAM and power.
    *   Both use keys, and asymmetric can run on small devices but consumes significant battery.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **hashing.**?
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
B) A set of detailed practices for IT service management (ITSM) that focuses on aligning IT services with the needs of business.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **hashing.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **hashing.**.
    * *Why A is correct:* This describes the exact role and function of **hashing.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **hashing.**.


---

**Question 3**
A systems administrator or developer needs to **launch all application services in the background using docker-compose configuration**. Which of the following commands is the most appropriate to execute?
C) systemctl status iot_service
B) terraform validate
D) git log --oneline -n 5
A) docker-compose up -d
*   **Correct Answer:** A) docker-compose up -d
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `docker-compose up -d` command is directly designed to launch all application services in the background using docker-compose configuration.


---

**Question 4**
While working on **Cryptography in Constrained Devices** in a production environment, you encounter a system alert indicating a **SLA Breach Alert** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize service resources, implement load balancing, or update failover mechanisms.
C) Re-assign resources to critical path tasks and establish clear communication protocols.
B) Implement strict change control boards (CCB) and re-baseline the project constraints.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize service resources, implement load balancing, or update failover mechanisms.
*   **Distractor Analysis:**
    * *Why A is correct:* Because A system outage or slow response time has exceeded the limits guaranteed in the Service Level Agreement. The appropriate fix is to Optimize service resources, implement load balancing, or update failover mechanisms..
    * *Why C is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why B is incorrect:* This action does not resolve the root cause of SLA Breach Alert.
    * *Why D is incorrect:* This action does not resolve the root cause of SLA Breach Alert.


---

**Question 5**
When designing a system for **Cryptography in Constrained Devices**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Correct Answer:** A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why A is correct:* Implementing Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services. mitigates the risk of A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented..

