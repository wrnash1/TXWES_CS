# Quiz: Module 02 - AD DS
## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

**Question 1**
In an Active Directory environment, what is the purpose of an Organizational Unit (OU)?
A) To create a boundary for password policies across the entire forest.
B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.
C) To act as a standalone server that authenticates users when the primary Domain Controller fails.
D) To synchronize time across all computers in the domain.
*   **Correct Answer:** B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Password policies are traditionally applied at the Domain level, not the OU level (though Fine-Grained Password Policies allow targeting specific groups, OUs are primarily for management delegation and GPO linking).
    *   *Why C is incorrect:* A standalone server that authenticates users is a Backup Domain Controller (or simply another DC in modern AD), not an OU. An OU is a logical container, not a physical server.
    *   *Why D is incorrect:* Time synchronization in a domain is handled by the PDC Emulator FSMO role, not an OU.

---

---

**Question 2**
After installing the Active Directory Domain Services (AD DS) role via Server Manager or PowerShell, what critical step must be performed before the server can begin authenticating users?
A) The server must be promoted to a Domain Controller.
B) The server must be joined to a workgroup.
C) The schema must be manually modified using ADSI Edit.
D) The Global Catalog service must be disabled.
*   **Correct Answer:** A) The server must be promoted to a Domain Controller.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Domain Controllers cannot belong to a workgroup; they define the domain.
    *   *Why C is incorrect:* The schema is automatically modified/prepared during the promotion process; manual modification is rarely required for initial setup.
    *   *Why D is incorrect:* The first Domain Controller in a new forest is automatically configured as a Global Catalog server, and disabling it would break functionality.

---

---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
B) systemctl restart service
A) df -h
C) chmod 600 config.conf
D) ps aux
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AD DS** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..


---

**Question 5**
When designing a system for **AD DS**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

