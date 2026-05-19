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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Terraform workspaces**?
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
C) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform workspaces**.
    * *Why A is correct:* This describes the exact role and function of **Terraform workspaces**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform workspaces**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform workspaces**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
D) ps aux
A) df -h
C) systemctl restart service
B) chmod 600 config.conf
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Workspaces & Multi-Env** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
D) Reboot the physical machine and wait for services to reload.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.


---

**Question 5**
When designing a system for **Workspaces & Multi-Env**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

