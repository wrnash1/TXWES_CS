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
C) The core component of an operating system that manages hardware resources, memory, and acts as a bridge between applications and hardware.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
B) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
D) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **importing existing resources (terraform import)**.
    * *Why A is correct:* This describes the exact role and function of **importing existing resources (terraform import)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **importing existing resources (terraform import)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **importing existing resources (terraform import)**.


---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
D) ps aux
B) chmod 600 config.conf
A) systemctl restart service
C) df -h
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Drift Management & Importing** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Drift Management & Importing**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..

