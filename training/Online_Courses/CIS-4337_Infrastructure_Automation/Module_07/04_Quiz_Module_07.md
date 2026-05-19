# Quiz: Module 07 - Provisioners & Local Exec
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which provisioner executes a command on the machine running the Terraform CLI?
*   A) remote-exec
*   B) local-exec
*   C) host-exec
*   D) system-exec
*   **Correct Answer:** B) The `local-exec` provisioner runs commands locally on the operator's shell system.
*   **Distractor Analysis:**
    *   *Why correct:* The `local-exec` provisioner runs commands locally on the operator's shell system.
    *   remote-exec runs command inside the deployed target virtual machine.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **connection blocks**?
C) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
B) Background utility processes that run continuously without direct user interaction to handle system tasks.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **connection blocks**.
    * *Why A is correct:* This describes the exact role and function of **connection blocks**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **connection blocks**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **connection blocks**.


---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
C) systemctl restart service
B) df -h
D) ps aux
A) chmod 600 config.conf
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.


---

**Question 4**
While working on **Provisioners & Local Exec** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Provisioners & Local Exec**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

