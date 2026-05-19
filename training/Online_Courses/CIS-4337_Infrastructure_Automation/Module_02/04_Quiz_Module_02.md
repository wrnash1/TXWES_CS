# Quiz: Module 02 - Terraform Architecture
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which command downloads and installs the provider plugins defined in your Terraform configuration files?
*   A) terraform apply
*   B) terraform init
*   C) terraform plan
*   D) terraform get
*   **Correct Answer:** B) `terraform init` initializes the folder, creating directory paths and downloading required provider plugins.
*   **Distractor Analysis:**
    *   *Why correct:* `terraform init` initializes the folder, creating directory paths and downloading required provider plugins.
    *   apply deploys resources. plan creates templates. get fetches modules.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **providers**?
B) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
C) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **providers**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **providers**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **providers**.
    * *Why A is correct:* This describes the exact role and function of **providers**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
C) systemctl restart service
A) df -h
B) ps aux
D) chmod 600 config.conf
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform Architecture** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Terraform Architecture**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

