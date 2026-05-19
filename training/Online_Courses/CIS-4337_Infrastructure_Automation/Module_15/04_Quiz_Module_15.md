# Quiz: Module 15 - Terraform Security & Secrets
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which HCL variable attribute prevents its value from being printed to the console stdout during apply runs?
*   A) write = false
*   B) sensitive = true
*   C) hidden = true
*   D) secret = true
*   **Correct Answer:** B) Declaring `sensitive = true` instructs Terraform to mask the values in logs and console outputs.
*   **Distractor Analysis:**
    *   *Why correct:* Declaring `sensitive = true` instructs Terraform to mask the values in logs and console outputs.
    *   The value is still written to the state file in plain text, making backend security critical.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Secret management guidelines**?
B) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Secret management guidelines**.
    * *Why A is correct:* This describes the exact role and function of **Secret management guidelines**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Secret management guidelines**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Secret management guidelines**.


---

**Question 3**
A systems administrator or developer needs to **display total disk space capacity, usage, and available space in a human-readable format**. Which of the following commands is the most appropriate to execute?
B) chmod 600 config.conf
C) systemctl restart service
A) df -h
D) ps aux
*   **Correct Answer:** A) df -h
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `df -h` command is directly designed to display total disk space capacity, usage, and available space in a human-readable format.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform Security & Secrets** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
B) Run log rotations, clean temporary files, or expand the logical volume capacity.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..


---

**Question 5**
When designing a system for **Terraform Security & Secrets**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
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

