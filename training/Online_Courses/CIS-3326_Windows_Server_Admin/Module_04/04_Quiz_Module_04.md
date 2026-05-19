# Quiz: Module 04 - File Services
## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

**Question 1**
An administrator shares a folder named 'HR_Docs' on the network. The Share permissions are set to give the 'HR_Group' Read-Only access. The NTFS security permissions on the folder give the 'HR_Group' Full Control. When a user in the 'HR_Group' accesses the folder over the network, what are their effective permissions?
A) Full Control
B) Read-Only
C) Write-Only
D) No Access
*   **Correct Answer:** B) Read-Only
*   **Distractor Analysis:**
    *   *Why A is incorrect:* When Share and NTFS permissions conflict during network access, the most restrictive permission wins. Read-Only (Share) is more restrictive than Full Control (NTFS).
    *   *Why C is incorrect:* Neither permission grants Write-Only access.
    *   *Why D is incorrect:* The user is granted Read access, so they are not entirely blocked from the folder.

---

---

**Question 2**
A company has two file servers, one in New York and one in Los Angeles. Users currently have to remember two different server names (`\\NY-FS01\Data` and `\\LA-FS01\Data`) to access company files. Which Windows Server technology should you implement to allow users to access all files via a single, unified path like `\\company.local\SharedData`?
A) DFS Replication (DFSR)
B) File Server Resource Manager (FSRM)
C) DFS Namespaces (DFSN)
D) Storage Spaces Direct (S2D)
*   **Correct Answer:** C) DFS Namespaces (DFSN)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DFSR is used to synchronize the *contents* of folders across servers, but it does not create the unified naming path for users to access them.
    *   *Why B is incorrect:* FSRM is used for storage quotas and file screening (blocking specific file extensions), not for abstracting network paths.
    *   *Why D is incorrect:* S2D is a hyper-converged infrastructure feature used to pool direct-attached storage across clustered servers, not for creating a logical namespace for SMB file shares.

---

---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
C) systemctl restart service
B) ps aux
A) chmod 600 config.conf
D) df -h
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **File Services** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.


---

**Question 5**
When designing a system for **File Services**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..

