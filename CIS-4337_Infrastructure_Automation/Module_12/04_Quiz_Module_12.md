# Quiz: Module 12 - Drift Management & Importing
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which command reads real-world resource details and registers them inside your local state file?
*   A) terraform apply
*   B) terraform import
*   C) terraform plan
*   D) terraform state push
*   **Correct Answer:** B) `terraform import` reads the target ID and populates it inside your state. You must manually write the matching HCL code.
*   **Distractor Analysis:**
    *   *Why correct:* `terraform import` reads the target ID and populates it inside your state. You must manually write the matching HCL code.
    *   import does not generate HCL code; it only writes state.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **importing existing resources (terraform import)**?
D) A directory service developed by Microsoft that manages domains, resources, users, and computer permissions in an enterprise network.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) Background utility processes that run continuously without direct user interaction to handle system tasks.
C) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **importing existing resources (terraform import)**.
    * *Why A is correct:* This describes the exact role and function of **importing existing resources (terraform import)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **importing existing resources (terraform import)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **importing existing resources (terraform import)**.


---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
D) df -h
C) chmod 600 config.conf
B) systemctl restart service
A) ps aux
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.


---

**Question 4**
While working on **Drift Management & Importing** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.


---

**Question 5**
When designing a system for **Drift Management & Importing**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

