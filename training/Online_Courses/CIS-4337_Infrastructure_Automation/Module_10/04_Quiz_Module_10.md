# Quiz: Module 10 - Terraform Modules
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What HCL parameter is required inside a module block to define the location of the module code?
*   A) path
*   B) source
*   C) location
*   D) directory
*   **Correct Answer:** B) The `source` parameter defines where the module code lives (local folder or registry URL).
*   **Distractor Analysis:**
    *   *Why correct:* The `source` parameter defines where the module code lives (local folder or registry URL).
    *   path, location, and directory are not valid HCL parameters.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **child modules**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
C) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
B) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **child modules**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **child modules**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **child modules**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **child modules**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
B) systemctl restart service
D) chmod 600 config.conf
C) df -h
A) ps aux
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.


---

**Question 4**
While working on **Terraform Modules** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..


---

**Question 5**
When designing a system for **Terraform Modules**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

