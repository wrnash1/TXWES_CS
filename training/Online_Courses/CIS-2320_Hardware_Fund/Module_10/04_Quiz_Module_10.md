# Quiz: Module 10 - Troubleshooting Boot Issues
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What does a blank screen with continuous short beeps during startup typically indicate?
*   A) OS is corrupted
*   B) POST has failed (typically due to RAM or motherboard issue)
*   C) The monitor is unplugged
*   D) Keyboard is disconnected
*   **Correct Answer:** B) Beep codes are diagnostic indicators emitted by the BIOS/UEFI during POST failures.
*   **Distractor Analysis:**
    *   *Why correct:* Beep codes are diagnostic indicators emitted by the BIOS/UEFI during POST failures.
    *   Syllabus details: OS corruption occurs after POST. Screen is blank because POST did not complete.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **BSOD/Kernel Panic**?
D) The core component of an operating system that manages hardware resources, memory, and acts as a bridge between applications and hardware.
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **BSOD/Kernel Panic**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **BSOD/Kernel Panic**.
    * *Why A is correct:* This describes the exact role and function of **BSOD/Kernel Panic**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **BSOD/Kernel Panic**.


---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
B) ps aux
D) df -h
C) chmod 600 config.conf
A) systemctl restart service
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.


---

**Question 4**
While working on **Troubleshooting Boot Issues** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Troubleshooting Boot Issues**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
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

