# Quiz: Module 03 - Settings, Providers, & Resources
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What block type in HCL is used to configure plugins that interact with cloud platforms (e.g., AWS, Azure)?
*   A) resource
*   B) variable
*   C) provider
*   D) output
*   **Correct Answer:** C) The `provider` block configures the plugins that translate HCL declarations into API calls.
*   **Distractor Analysis:**
    *   *Why correct:* The `provider` block configures the plugins that translate HCL declarations into API calls.
    *   resource declares infrastructure objects.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **resource block parameters**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
C) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
D) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **resource block parameters**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **resource block parameters**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **resource block parameters**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **resource block parameters**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
A) df -h
B) ps aux
C) chmod 600 config.conf
D) systemctl restart service
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Settings, Providers, & Resources** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Settings, Providers, & Resources**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
C) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

