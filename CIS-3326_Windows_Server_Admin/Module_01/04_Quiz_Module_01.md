# Quiz: Module 01 - Server Core
## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

**Question 1**
Which of the following is a primary advantage of installing Windows Server using the Server Core option instead of Desktop Experience?
A) It provides a larger selection of pre-installed graphical management tools.
B) It has a reduced attack surface and lower hardware footprint.
C) It allows for the installation of Microsoft Office applications directly on the server.
D) It forces the use of IPv6 for all network communications.
*   **Correct Answer:** B) It has a reduced attack surface and lower hardware footprint.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Server Core removes almost all graphical tools; you must manage it remotely or via CLI.
    *   *Why C is incorrect:* You generally do not install client applications like Office on a server, and certainly not on Server Core which lacks a GUI.
    *   *Why D is incorrect:* Server Core supports both IPv4 and IPv6, just like the Desktop Experience.

---

---

**Question 2**
You have just installed a new Windows Server Core machine. Which command-line utility provides a simple, text-based menu to configure the hostname, IP address, and Windows updates?
A) ipconfig
B) sysdm.cpl
C) sconfig
D) ServerManager.exe
*   **Correct Answer:** C) sconfig
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ipconfig` only displays network settings; it does not provide an interactive menu to change hostnames or run updates.
    *   *Why B is incorrect:* `sysdm.cpl` opens the graphical System Properties dialog, which is not available natively in Server Core.
    *   *Why D is incorrect:* `ServerManager.exe` launches the graphical Server Manager, which is omitted from Server Core.

---

---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
C) systemctl restart service
B) ps aux
D) chmod 600 config.conf
A) df -h
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.


---

**Question 4**
While working on **Server Core** in a production environment, you encounter a system alert indicating a **Permission Denied** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The current user account lacks the required read, write, or execute permissions for the target file or system call. The appropriate fix is to Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions..
    * *Why D is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why B is incorrect:* This action does not resolve the root cause of Permission Denied.
    * *Why C is incorrect:* This action does not resolve the root cause of Permission Denied.


---

**Question 5**
When designing a system for **Server Core**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

