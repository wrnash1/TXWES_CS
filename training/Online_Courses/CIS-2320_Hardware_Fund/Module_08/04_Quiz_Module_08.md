# Quiz: Module 08 - Custom PC Configurations
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What is the most critical hardware component when designing a virtualization workstation?
*   A) High-end GPU
*   B) Fast mechanical HDD
*   C) Maximum CPU cores and RAM
*   D) Liquid nitrogen cooling
*   **Correct Answer:** C) Virtual machines run concurrently and consume logical cores and physical RAM allocations directly.
*   **Distractor Analysis:**
    *   *Why correct:* Virtual machines run concurrently and consume logical cores and physical RAM allocations directly.
    *   Virtualization hosts do not require heavy 3D rendering GPUs or slow hard drives.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **virtualization hosts**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
B) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
D) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **virtualization hosts**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **virtualization hosts**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **virtualization hosts**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **virtualization hosts**.


---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
A) systemctl restart service
D) ps aux
C) chmod 600 config.conf
B) df -h
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Custom PC Configurations** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
D) Reboot the physical machine and wait for services to reload.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.


---

**Question 5**
When designing a system for **Custom PC Configurations**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
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

