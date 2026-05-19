# Quiz: Module 06 - Power Supplies and System Cooling
## Course: CIS-2320_Hardware_Fund (CompTIA A+)

---

**Question 1**
What standard power connector is used to supply direct auxiliary power to high-end PCIe graphics cards?
*   A) 24-pin ATX
*   B) SATA Power
*   C) 6-pin or 8-pin PCIe
*   D) 4-pin Molex
*   **Correct Answer:** C) PCIe graphics cards use 6-pin or 8-pin auxiliary cables to draw up to 150W of power.
*   **Distractor Analysis:**
    *   *Why correct:* PCIe graphics cards use 6-pin or 8-pin auxiliary cables to draw up to 150W of power.
    *   24-pin is for motherboard. SATA is for storage. Molex is for legacy accessories.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **case airflow (intake vs exhaust).**?
D) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
B) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within os_admin operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **case airflow (intake vs exhaust).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **case airflow (intake vs exhaust).**.
    * *Why A is correct:* This describes the exact role and function of **case airflow (intake vs exhaust).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **case airflow (intake vs exhaust).**.


---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
B) ps aux
C) df -h
A) systemctl restart service
D) chmod 600 config.conf
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Power Supplies and System Cooling** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
D) Reboot the physical machine and wait for services to reload.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Power Supplies and System Cooling**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

