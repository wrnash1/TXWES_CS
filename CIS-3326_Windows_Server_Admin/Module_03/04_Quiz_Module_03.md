# Quiz: Module 03 - GPOs
## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

**Question 1**
An administrator configures a Group Policy Object (GPO) at the Domain level that sets the minimum password length to 12 characters. However, a separate GPO linked to the "IT_Department" Organizational Unit (OU) sets the minimum password length to 15 characters. Assuming no other settings are modified, what minimum password length will apply to users in the IT_Department OU?
A) 12 characters, because Domain policies always override OU policies.
B) 15 characters, because the OU policy is applied last and overrides the Domain policy.
C) 15 characters, because GPOs always apply the most restrictive setting automatically.
D) The policies will conflict and neither will be applied.
*   **Correct Answer:** B) 15 characters, because the OU policy is applied last and overrides the Domain policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GPOs follow the LSDOU processing order. OU policies are processed *after* Domain policies, meaning the OU policy wins.
    *   *Why C is incorrect:* GPOs do not evaluate restrictiveness; they blindly apply the last policy processed unless the "Enforced" flag is used.
    *   *Why D is incorrect:* GPOs are designed to handle conflicts gracefully through the inheritance order.

---

---

**Question 2**
You need to deploy a specific registry key via Group Policy, but it must only be applied to computers that are running Windows 10, completely ignoring any Windows 11 machines in the same OU. What is the most efficient way to accomplish this?
A) Create two separate OUs, move the computers manually, and link the GPO to the Windows 10 OU.
B) Modify the Security Filtering to explicitly deny the 'Windows 11 Computers' security group.
C) Configure a WMI Filter on the GPO that queries the operating system version.
D) Change the GPO from a Computer Configuration to a User Configuration.
*   **Correct Answer:** C) Configure a WMI Filter on the GPO that queries the operating system version.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While this works, it is highly inefficient and creates administrative overhead to constantly move computer objects around as they are upgraded.
    *   *Why B is incorrect:* Managing OS versions via security groups requires manual tracking of which computer belongs to which group. WMI queries the hardware/OS directly and dynamically.
    *   *Why D is incorrect:* A registry key that targets machine behavior belongs in Computer Configuration. Moving it to User Configuration will apply it based on who logs in, not what OS the machine is running.

---

---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
D) df -h
B) ps aux
A) systemctl restart service
C) chmod 600 config.conf
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **GPOs** in a production environment, you encounter a system alert indicating a **Service Failed to Bind Port** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
C) Run log rotations, clean temporary files, or expand the logical volume capacity.
A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why B is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why C is incorrect:* This action does not resolve the root cause of Service Failed to Bind Port.
    * *Why A is correct:* Because Another application or stale instance of the service is already listening on the designated network port. The appropriate fix is to Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port..


---

**Question 5**
When designing a system for **GPOs**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.

