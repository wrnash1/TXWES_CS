# Quiz: Module 05 - Terraform State Management
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What is the primary purpose of the `terraform.tfstate` file?
*   A) To store user passwords
*   B) To map HCL declarations directly to real-world resources
*   C) To write shell logs
*   D) To compile python modules
*   **Correct Answer:** B) The state file acts as a database mapping your configuration declarations to the actual IDs of deployed cloud resources.
*   **Distractor Analysis:**
    *   *Why correct:* The state file acts as a database mapping your configuration declarations to the actual IDs of deployed cloud resources.
    *   State files store metadata maps.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **state tracking**?
C) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
D) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **state tracking**.
    * *Why A is correct:* This describes the exact role and function of **state tracking**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **state tracking**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **state tracking**.


---

**Question 3**
A systems administrator or developer needs to **restrict file read and write permissions to the file owner only, removing all group and other access**. Which of the following commands is the most appropriate to execute?
C) ps aux
D) df -h
A) chmod 600 config.conf
B) systemctl restart service
*   **Correct Answer:** A) chmod 600 config.conf
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `chmod 600 config.conf` command is directly designed to restrict file read and write permissions to the file owner only, removing all group and other access.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform State Management** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Terraform State Management**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
C) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

