# Quiz: Module 10 - Terraform Modules
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What HCL parameter is required inside a module block to define the location of the module code?
*   A) path
*   B) source
*   C) location
*   D) directory
*   **Correct Answer:** B) The `source` parameter defines where the module code lives (local folder or registry URL).
*   **Distractor Analysis:**
    *   *Why correct:* The `source` parameter defines where the module code lives (local folder or registry URL).
    *   path, location, and directory are not valid HCL parameters.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Module definition**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
C) A memory management capability that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data to disk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Module definition**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Module definition**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Module definition**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Module definition**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
A) ps aux
B) df -h
D) chmod 600 config.conf
C) systemctl restart service
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform Modules** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Terraform Modules**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

