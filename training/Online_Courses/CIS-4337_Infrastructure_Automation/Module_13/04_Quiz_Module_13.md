# Quiz: Module 13 - Terraform Cloud & Registry
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Where does state storage and HCL compilation execute when using a VCS-connected Terraform Cloud workspace?
*   A) On the developer's laptop
*   B) In the Terraform Cloud remote runtime environment
*   C) In the target virtual machine
*   D) On the GitHub server
*   **Correct Answer:** B) Terraform Cloud acts as a remote agent, running `plan` and `apply` actions on its own containers, storing state securely.
*   **Distractor Analysis:**
    *   *Why correct:* Terraform Cloud acts as a remote agent, running `plan` and `apply` actions on its own containers, storing state securely.
    *   It handles operations remotely, freeing developers from local execution requirements.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Terraform Cloud workspaces**?
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
B) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform Cloud workspaces**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform Cloud workspaces**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Terraform Cloud workspaces**.
    * *Why A is correct:* This describes the exact role and function of **Terraform Cloud workspaces**.


---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
C) df -h
A) chmod 600 config.conf
B) systemctl restart service
D) ps aux
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform Cloud & Registry** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Terraform Cloud & Registry**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..

