# Quiz: Module 06 - State Locking & Backends
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Why is state locking critical in enterprise team environments?
*   A) To encrypt variables
*   B) To prevent concurrent runs from corrupting the state file
*   C) To speed up provisioning
*   D) None of the above
*   **Correct Answer:** B) State locking ensures that if two users run `apply` at the same time, one is queued to avoid overwriting or corruption.
*   **Distractor Analysis:**
    *   *Why correct:* State locking ensures that if two users run `apply` at the same time, one is queued to avoid overwriting or corruption.
    *   Locks do not accelerate deployments or encrypt variables.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Terraform Cloud)**?
B) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
C) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
D) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform Cloud)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform Cloud)**.
    * *Why A is correct:* This describes the exact role and function of **Terraform Cloud)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform Cloud)**.


---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
A) systemctl restart service
C) ps aux
B) chmod 600 config.conf
D) df -h
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **State Locking & Backends** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..


---

**Question 5**
When designing a system for **State Locking & Backends**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..

