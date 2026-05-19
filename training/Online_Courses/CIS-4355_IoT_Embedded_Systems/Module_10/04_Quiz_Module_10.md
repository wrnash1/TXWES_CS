# Quiz: Module 10 - Secure Boot & OTA updates
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
How does Secure Boot protect an embedded IoT device?
*   A) It boots the system faster
*   B) It cryptographically verifies the signature of the bootloader and firmware before executing, preventing unsigned code runs
*   C) It disables the power button
*   D) It deletes system database logs
*   **Correct Answer:** B) Secure Boot checks digital signatures against keys burned into the hardware's root-of-trust, blocking tampered firmware.
*   **Distractor Analysis:**
    *   *Why correct:* Secure Boot checks digital signatures against keys burned into the hardware's root-of-trust, blocking tampered firmware.
    *   It is a verification check, not a boot booster.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **firmware verification**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
C) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
B) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
D) A set of detailed practices for IT service management (ITSM) that focuses on aligning IT services with the needs of business.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **firmware verification**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **firmware verification**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **firmware verification**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **firmware verification**.


---

**Question 3**
A systems administrator or developer needs to **review the last five project commits in a concise single-line format**. Which of the following commands is the most appropriate to execute?
A) git log --oneline -n 5
D) systemctl status iot_service
C) docker-compose up -d
B) terraform validate
*   **Correct Answer:** A) git log --oneline -n 5
*   **Distractor Analysis:**
    * *Why A is correct:* The `git log --oneline -n 5` command is directly designed to review the last five project commits in a concise single-line format.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Secure Boot & OTA updates** in a production environment, you encounter a system alert indicating a **SLA Breach Alert** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Secure Boot & OTA updates**, you must mitigate the risk of **A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented.**. Which of the following security configurations or controls represents the best practice to implement?
A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
D) Enable full disk encryption on all client endpoints.
B) Establish formal authorization procedures and digital signatures for all project scope modifications.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services. mitigates the risk of A disaster or ransomware attack causing prolonged downtime because recovery steps are undocumented..
    * *Why D is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why B is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.
    * *Why C is incorrect:* This does not address the security vulnerability of Lack of Business Continuity Plan.

