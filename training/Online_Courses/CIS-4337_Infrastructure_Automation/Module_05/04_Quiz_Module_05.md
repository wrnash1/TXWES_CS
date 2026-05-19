# Quiz: Module 05 - Terraform State Management
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What is the primary purpose of the `terraform.tfstate` file?
*   A) To store user passwords
*   B) To map HCL declarations directly to real-world resources
*   C) To write shell logs
*   D) To compile python modules
*   **Correct Answer:** B) The state file acts as a database mapping your configuration declarations to the actual IDs of deployed cloud resources.
*   **Distractor Analysis:**
    *   *Why correct:* The state file acts as a database mapping your configuration declarations to the actual IDs of deployed cloud resources.
    *   State files store metadata maps.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **mapping local files to cloud APIs.**?
C) A memory management capability that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data to disk.
D) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
B) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **mapping local files to cloud APIs.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **mapping local files to cloud APIs.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **mapping local files to cloud APIs.**.
    * *Why A is correct:* This describes the exact role and function of **mapping local files to cloud APIs.**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
A) ps aux
C) df -h
D) systemctl restart service
B) chmod 600 config.conf
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform State Management** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
D) Reboot the physical machine and wait for services to reload.
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Terraform State Management**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

