# Quiz: Module 15 - Terraform Security & Secrets
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which HCL variable attribute prevents its value from being printed to the console stdout during apply runs?
*   A) write = false
*   B) sensitive = true
*   C) hidden = true
*   D) secret = true
*   **Correct Answer:** B) Declaring `sensitive = true` instructs Terraform to mask the values in logs and console outputs.
*   **Distractor Analysis:**
    *   *Why correct:* Declaring `sensitive = true` instructs Terraform to mask the values in logs and console outputs.
    *   The value is still written to the state file in plain text, making backend security critical.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **sensitive outputs.**?
C) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
B) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
D) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **sensitive outputs.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **sensitive outputs.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **sensitive outputs.**.
    * *Why A is correct:* This describes the exact role and function of **sensitive outputs.**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
D) chmod 600 config.conf
B) systemctl restart service
C) ps aux
A) df -h
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.


---

**Question 4**
While working on **Terraform Security & Secrets** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.


---

**Question 5**
When designing a system for **Terraform Security & Secrets**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

