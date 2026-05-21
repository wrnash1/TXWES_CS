# Quiz: Module 05 - Storage Devices
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which RAID level provides data striping without parity or redundancy?
*   A) RAID 0
*   B) RAID 1
*   C) RAID 5
*   D) RAID 10
*   **Correct Answer:** A) RAID 0 stripes data for performance but offers zero fault tolerance.
*   **Distractor Analysis:**
    *   *Why correct:* RAID 0 stripes data for performance but offers zero fault tolerance.
    *   RAID 1 is mirroring. RAID 5 uses parity. RAID 10 is striped mirrors.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **2.5)**?
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
C) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **2.5)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **2.5)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **2.5)**.
    * *Why A is correct:* This describes the exact role and function of **2.5)**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
C) chmod 600 config.conf
B) df -h
A) ps aux
D) systemctl restart service
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Storage Devices** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..


---

**Question 5**
When designing a system for **Storage Devices**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

