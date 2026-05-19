# Quiz: Module 14 - Terraform in CI/CD Pipelines
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which flag must be appended to the `apply` command in automation pipelines to prevent it from waiting for user confirmation?
*   A) --force
*   B) -auto-approve
*   C) --yes
*   D) --silent
*   **Correct Answer:** B) The `-auto-approve` flag executes the apply changes immediately without prompting the console operator.
*   **Distractor Analysis:**
    *   *Why correct:* The `-auto-approve` flag executes the apply changes immediately without prompting the console operator.
    *   --force, --yes, and --silent are not valid CLI options.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **non-interactive execution (-auto-approve)**?
B) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
D) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **non-interactive execution (-auto-approve)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **non-interactive execution (-auto-approve)**.
    * *Why A is correct:* This describes the exact role and function of **non-interactive execution (-auto-approve)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **non-interactive execution (-auto-approve)**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
A) ps aux
B) chmod 600 config.conf
D) df -h
C) systemctl restart service
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform in CI/CD Pipelines** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Terraform in CI/CD Pipelines**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
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

