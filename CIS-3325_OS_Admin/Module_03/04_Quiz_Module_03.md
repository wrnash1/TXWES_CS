# Quiz: Module 03 - Users
## Course: CIS-3325_OS_Admin (3325_OS_Admin - CompTIA Linux+ (XK0-005))

---

**Question 1**
An administrator executes the command `chmod 644 confidential.txt`. What permissions does this command assign to the file?
A) The owner has read and write access, while the group and others have read-only access.
B) The owner has full access (read, write, execute), while the group has read-only access.
C) The owner has read-only access, while the group and others have read and write access.
D) The owner and the group have read and write access, while others have no access.
*   **Correct Answer:** A) The owner has read and write access, while the group and others have read-only access.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Full access is represented by a 7 (4+2+1). The first digit here is a 6 (4+2 = read+write).
    *   *Why C is incorrect:* This describes permissions of 466, which is an invalid and insecure configuration.
    *   *Why D is incorrect:* This describes permissions of 660, not 644. The digit 4 represents read-only access.

---

---

**Question 2**
Which file in a standard Linux system contains the securely hashed passwords for local user accounts?
A) /etc/passwd
B) /etc/shadow
C) /etc/group
D) /var/log/auth.log
*   **Correct Answer:** B) /etc/shadow
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Historically, passwords were stored here, but today `/etc/passwd` only contains user information (UID, home directory, shell) and an 'x' indicating the password is in the shadow file.
    *   *Why C is incorrect:* `/etc/group` defines local groups and their members, not passwords.
    *   *Why D is incorrect:* The `auth.log` records authentication attempts (logins, sudo usage), not the actual password hashes.

---

---

**Question 3**
A systems administrator or developer needs to **instruct the systemd init system to restart a specified background service process**. Which of the following commands is the most appropriate to execute?
A) systemctl restart service
D) df -h
B) chmod 600 config.conf
C) ps aux
*   **Correct Answer:** A) systemctl restart service
*   **Distractor Analysis:**
    * *Why A is correct:* The `systemctl restart service` command is directly designed to instruct the systemd init system to restart a specified background service process.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Users** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.


---

**Question 5**
When designing a system for **Users**, you must mitigate the risk of **Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Disable unused system accounts and run a port scan to disable unnecessary active background services.
A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why B is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.
    * *Why A is correct:* Implementing Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC. mitigates the risk of Administrators logging in routinely as root or Administrator, increasing the blast radius of user errors or malware..
    * *Why C is incorrect:* This does not address the security vulnerability of Privileged Access Abuse.

