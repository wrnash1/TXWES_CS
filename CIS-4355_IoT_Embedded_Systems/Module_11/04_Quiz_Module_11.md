# Quiz: Module 11 - IoT Gateway Security
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Why should IoT devices be isolated on a separate network segment (VLAN) from corporate workstations?
*   A) To prevent devices from running out of batteries
*   B) To contain security breaches, preventing compromised devices from being used to attack corporate assets
*   C) To double network speeds
*   D) To hide device MAC addresses
*   **Correct Answer:** B) Segmentation restricts lateral movement; if a smart camera is breached, the attacker cannot reach finance servers.
*   **Distractor Analysis:**
    *   *Why correct:* Segmentation restricts lateral movement; if a smart camera is breached, the attacker cannot reach finance servers.
    *   It is about blast-radius containment, not battery life or speed.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Local gateway configurations**?
C) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
D) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
B) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Local gateway configurations**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Local gateway configurations**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Local gateway configurations**.
    * *Why A is correct:* This describes the exact role and function of **Local gateway configurations**.


---

**Question 3**
A systems administrator or developer needs to **verify the active status and resource usage of the background service daemon**. Which of the following commands is the most appropriate to execute?
B) docker-compose up -d
A) systemctl status iot_service
D) git log --oneline -n 5
C) terraform validate
*   **Correct Answer:** A) systemctl status iot_service
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl status iot_service` command is directly designed to verify the active status and resource usage of the background service daemon.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IoT Gateway Security** in a production environment, you encounter a system alert indicating a **Scope Exceeded Budget Limit** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Re-assign resources to critical path tasks and establish clear communication protocols.
C) Optimize service resources, implement load balancing, or update failover mechanisms.
A) Implement strict change control boards (CCB) and re-baseline the project constraints.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Implement strict change control boards (CCB) and re-baseline the project constraints.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.
    * *Why C is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.
    * *Why A is correct:* Because The project scope expanded during execution without adjusting budget or schedule allocations. The appropriate fix is to Implement strict change control boards (CCB) and re-baseline the project constraints..
    * *Why D is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.


---

**Question 5**
When designing a system for **IoT Gateway Security**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..

