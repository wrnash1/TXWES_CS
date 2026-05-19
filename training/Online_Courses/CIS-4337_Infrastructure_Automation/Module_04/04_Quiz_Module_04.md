# Quiz: Module 04 - Terraform Variables & Outputs
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which file extension is default for storing variable values in a Terraform project?
*   A) .tf
*   B) .tfvars
*   C) .json
*   D) .hcl
*   **Correct Answer:** B) Terraform automatically loads variables values from files ending with `.tfvars`.
*   **Distractor Analysis:**
    *   *Why correct:* Terraform automatically loads variables values from files ending with `.tfvars`.
    *   .tf stores declarations. .json is alternative layout.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **list**?
B) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) A collection of configuration settings in Microsoft Windows Active Directory that controls user and computer environments.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **list**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **list**.
    * *Why A is correct:* This describes the exact role and function of **list**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **list**.


---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
D) systemctl restart service
B) ps aux
A) chmod 600 config.conf
C) df -h
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform Variables & Outputs** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..


---

**Question 5**
When designing a system for **Terraform Variables & Outputs**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

