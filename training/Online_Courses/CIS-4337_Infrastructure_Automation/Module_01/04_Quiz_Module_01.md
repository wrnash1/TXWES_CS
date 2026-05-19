# Quiz: Module 01 - IaC Concepts & Benefits
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What is a primary advantage of declarative IaC over imperative scripting?
*   A) Declarative requires detailing exact deployment commands
*   B) Declarative defines the target end-state; the tool handles deployment steps
*   C) Declarative executes faster
*   D) Declarative does not require code
*   **Correct Answer:** B) Declarative tools (like Terraform) allow you to specify 'what' you want, rather than scripting the 'how' step-by-step.
*   **Distractor Analysis:**
    *   *Why correct:* Declarative tools (like Terraform) allow you to specify 'what' you want, rather than scripting the 'how' step-by-step.
    *   Imperative requires detailing exact script commands.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **drift**?
B) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **drift**.
    * *Why A is correct:* This describes the exact role and function of **drift**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **drift**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **drift**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
B) chmod 600 config.conf
D) systemctl restart service
C) ps aux
A) df -h
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.


---

**Question 4**
While working on **IaC Concepts & Benefits** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **IaC Concepts & Benefits**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..

