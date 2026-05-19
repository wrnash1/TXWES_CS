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
D) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **2.5)**.
    * *Why A is correct:* This describes the exact role and function of **2.5)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **2.5)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **2.5)**.


---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
D) ps aux
B) systemctl restart service
C) df -h
A) chmod 600 config.conf
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.


---

**Question 4**
While working on **Storage Devices** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..


---

**Question 5**
When designing a system for **Storage Devices**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

