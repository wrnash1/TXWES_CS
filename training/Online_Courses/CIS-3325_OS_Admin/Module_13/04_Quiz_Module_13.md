# Quiz: Module 13 - SSH
## Course: CIS-3325_OS_Admin (3325_OS_Admin - CompTIA Linux+ (XK0-005))

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
B) A memory management capability that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data to disk.
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
D) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) An active, running instance of a computer program that has its own isolated memory address space and system resources.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
D) df -h
C) systemctl restart service
A) chmod 600 config.conf
B) ps aux
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **SSH** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..


---

**Question 5**
When designing a system for **SSH**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

