# Quiz: Module 01 - OS Basics
## Course: CIS-3325_OS_Admin (3325_OS_Admin - CompTIA Linux+ (XK0-005))

---

**Question 1**
Which of the following describes a Type 1 hypervisor?
A) It runs as an application on top of an existing host operating system like Windows 10.
B) It runs directly on the server's bare-metal hardware.
C) It cannot run Linux virtual machines.
D) It requires Oracle VirtualBox to function.
*   **Correct Answer:** B) It runs directly on the server's bare-metal hardware.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a Type 2 hypervisor (hosted), not Type 1.
    *   *Why C is incorrect:* Type 1 hypervisors can run almost any supported OS, including Linux.
    *   *Why D is incorrect:* VirtualBox is a Type 2 hypervisor. Type 1 hypervisors include ESXi and Hyper-V.

---

**Question 2**
What is the primary function of an operating system's kernel?
A) To provide a graphical user interface (GUI) for the user.
B) To compile source code into executable binaries.
C) To manage hardware resources and act as a bridge between applications and data processing.
D) To run web browsers and word processors.
*   **Correct Answer:** C) To manage hardware resources and act as a bridge between applications and data processing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The GUI is a user-space application (like a desktop environment), not the kernel itself.
    *   *Why B is incorrect:* Compiling code is done by a compiler (like GCC), not the OS kernel.
    *   *Why D is incorrect:* Web browsers run in user space; the kernel simply provides them the resources they need to run.

---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
D) systemctl restart service
B) df -h
C) ps aux
A) chmod 600 config.conf
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.


---

**Question 4**
While working on **OS Basics** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
D) Reboot the physical machine and wait for services to reload.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **OS Basics**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..

