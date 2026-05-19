# Quiz: Module 09 - HCL Functions & Expressions
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which built-in Terraform function retrieves a value from a map given its key?
*   A) find()
*   B) lookup()
*   C) element()
*   D) map()
*   **Correct Answer:** B) The `lookup(map, key, default)` function queries map variables dynamically.
*   **Distractor Analysis:**
    *   *Why correct:* The `lookup(map, key, default)` function queries map variables dynamically.
    *   element() retrieves items from lists. find() is not a Terraform function.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **file)**?
B) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) The descendant node connected to the left branch of a parent node in a binary tree structure.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **file)**.
    * *Why A is correct:* This describes the exact role and function of **file)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **file)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **file)**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
D) df -h
A) ps aux
B) chmod 600 config.conf
C) systemctl restart service
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **HCL Functions & Expressions** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..


---

**Question 5**
When designing a system for **HCL Functions & Expressions**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

