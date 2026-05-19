# Quiz: Module 02 - Command Line
## Course: CIS-3325_OS_Admin (3325_OS_Admin - CompTIA Linux+ (XK0-005))

---

**Question 1**
Which directory in the Linux Filesystem Hierarchy Standard (FHS) is specifically designated to hold system-wide configuration files?
A) /bin
B) /var
C) /etc
D) /home
*   **Correct Answer:** C) /etc
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `/bin` contains essential user command binaries (like `ls` and `cp`), not configuration files.
    *   *Why B is incorrect:* `/var` contains variable data that changes rapidly, such as system logs and print spools.
    *   *Why D is incorrect:* `/home` contains the personal directories and files for individual users, not system-wide configurations.

---

**Question 2**
You are currently in the directory `/home/user/documents/`. You want to navigate directly to the `/var/log/` directory using an absolute path. Which command should you use?
A) cd ../../var/log
B) cd /var/log
C) cd var/log
D) cd ~/var/log
*   **Correct Answer:** B) cd /var/log
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is a relative path utilizing `../` to go up two directories. While it works, it is not an *absolute* path.
    *   *Why C is incorrect:* Missing the leading forward slash makes this a relative path; the shell will look for a folder named `var` inside your current `documents` directory and fail.
    *   *Why D is incorrect:* The tilde `~` expands to the user's home directory (`/home/user/`). This command would try to navigate to `/home/user/var/log`, which likely doesn't exist.

---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
B) df -h
A) ps aux
C) chmod 600 config.conf
D) systemctl restart service
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Command Line** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Command Line**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

