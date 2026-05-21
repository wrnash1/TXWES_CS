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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Over-The-Air (OTA) updates**?
C) The descendant node connected to the right branch of a parent node in a binary tree structure.
B) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within management_services operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Over-The-Air (OTA) updates**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Over-The-Air (OTA) updates**.
    * *Why A is correct:* This describes the exact role and function of **Over-The-Air (OTA) updates**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Over-The-Air (OTA) updates**.


---

**Question 3**
A systems administrator or developer needs to **check the configuration files for syntactic and internal consistency correctness**. Which of the following commands is the most appropriate to execute?
C) git log --oneline -n 5
B) docker-compose up -d
D) systemctl status iot_service
A) terraform validate
*   **Correct Answer:** A) terraform validate
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `terraform validate` command is directly designed to check the configuration files for syntactic and internal consistency correctness.


---

**Question 4**
While working on **Secure Boot & OTA updates** in a production environment, you encounter a system alert indicating a **Scope Exceeded Budget Limit** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Implement strict change control boards (CCB) and re-baseline the project constraints.
C) Optimize service resources, implement load balancing, or update failover mechanisms.
B) Re-assign resources to critical path tasks and establish clear communication protocols.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Implement strict change control boards (CCB) and re-baseline the project constraints.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The project scope expanded during execution without adjusting budget or schedule allocations. The appropriate fix is to Implement strict change control boards (CCB) and re-baseline the project constraints..
    * *Why C is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.
    * *Why B is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.
    * *Why D is incorrect:* This action does not resolve the root cause of Scope Exceeded Budget Limit.


---

**Question 5**
When designing a system for **Secure Boot & OTA updates**, you must mitigate the risk of **Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities.**. Which of the following security configurations or controls represents the best practice to implement?
B) Perform a Business Impact Analysis (BIA) and define clear RTO and RPO metrics for all IT services.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Correct Answer:** A) Establish formal authorization procedures and digital signatures for all project scope modifications.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Scope Modification.
    * *Why A is correct:* Implementing Establish formal authorization procedures and digital signatures for all project scope modifications. mitigates the risk of Stakeholders requesting changes directly to developers, leading to untracked features and security vulnerabilities..

