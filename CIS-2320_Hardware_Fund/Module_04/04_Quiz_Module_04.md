# Quiz: Module 04 - Memory (RAM) Types and Configuration
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
Which RAM type is specifically designed for space-constrained laptops and thin clients?
*   A) DIMM
*   B) SODIMM
*   C) SDRAM
*   D) GDDR
*   **Correct Answer:** B) Small Outline Dual Inline Memory Module (SODIMM) is the standard compact form factor for laptop RAM.
*   **Distractor Analysis:**
    *   *Why correct:* Small Outline Dual Inline Memory Module (SODIMM) is the standard compact form factor for laptop RAM.
    *   DIMM is for desktop. GDDR is graphics RAM. SDRAM is the general class of synchronous RAM.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **SODIMM vs DIMM**?
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
B) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **SODIMM vs DIMM**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **SODIMM vs DIMM**.
    * *Why A is correct:* This describes the exact role and function of **SODIMM vs DIMM**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **SODIMM vs DIMM**.


---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
B) chmod 600 config.conf
D) df -h
A) systemctl restart service
C) ps aux
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Memory (RAM) Types and Configuration** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Memory (RAM) Types and Configuration**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..

