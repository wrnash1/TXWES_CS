# Quiz: Module 01 - Introduction to PC Hardware & Safety
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What is the primary danger when working inside a computer case without ESD safety?
*   A) Electric shock to the user
*   B) Electrostatic discharge damaging components
*   C) Setting the case on fire
*   D) Damaging the hard drive platter
*   **Correct Answer:** B) ESD can ruin integrated circuits without the user even noticing a spark.
*   **Distractor Analysis:**
    *   *Why correct:* ESD can ruin integrated circuits without the user even noticing a spark.
    *   PSUs store charge, but normal components pose ESD risk to the PC, not electrical shock to the user.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **grounding**?
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
A) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
C) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
*   **Correct Answer:** A) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **grounding**.
    * *Why A is correct:* This describes the exact role and function of **grounding**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **grounding**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **grounding**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
C) df -h
A) ps aux
D) systemctl restart service
B) chmod 600 config.conf
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Introduction to PC Hardware & Safety** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Introduction to PC Hardware & Safety**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

