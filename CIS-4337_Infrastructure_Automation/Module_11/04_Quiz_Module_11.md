# Quiz: Module 11 - Workspaces & Multi-Env
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which environment variable/parameter references the name of the current active Terraform workspace?
*   A) var.workspace
*   B) terraform.workspace
*   C) local.workspace
*   D) active.workspace
*   **Correct Answer:** B) The `terraform.workspace` path returns the current active workspace name (e.g. 'prod' or 'dev').
*   **Distractor Analysis:**
    *   *Why correct:* The `terraform.workspace` path returns the current active workspace name (e.g. 'prod' or 'dev').
    *   It is a built-in object, not a variable prefix.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **workspace directories**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
D) A memory management capability that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data to disk.
B) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **workspace directories**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **workspace directories**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **workspace directories**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **workspace directories**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
A) df -h
C) chmod 600 config.conf
D) systemctl restart service
B) ps aux
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Workspaces & Multi-Env** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Workspaces & Multi-Env**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
C) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..

