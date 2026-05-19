# Quiz: Module 04 - Permissions
## Course: CIS-3325_OS_Admin (3325_OS_Admin - CompTIA Linux+ (XK0-005))

---

**Question 1**
An administrator runs a script that takes a long time to complete and wants to save the output to a log file instead of displaying it on the screen. However, they want to ensure that if the script fails, the error messages are *also* captured in the same log file. Which command achieves this?
A) ./script.sh > output.log
B) ./script.sh >> output.log
C) ./script.sh > output.log 2>&1
D) ./script.sh < output.log
*   **Correct Answer:** C) ./script.sh > output.log 2>&1
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `>` only redirects stdout (1). Errors (stderr, 2) will still print to the screen and be lost.
    *   *Why B is incorrect:* `>>` appends stdout, but still does not capture stderr.
    *   *Why D is incorrect:* `<` is used to feed the contents of a file into a script as input (stdin), not save output. `2>&1` redirects stderr (2) to wherever stdout (1) is currently pointing.

---

**Question 2**
You have just installed a new web server package (nginx) on your Linux machine. You started the service manually and verified it works. However, after rebooting the server, the website is down because the service did not start automatically. Which command must you run to ensure the service starts on every boot?
A) systemctl start nginx
B) systemctl enable nginx
C) systemctl reload nginx
D) systemctl status nginx
*   **Correct Answer:** B) systemctl enable nginx
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `start` only turns the service on for the current session; it does not configure it to start on the next boot.
    *   *Why C is incorrect:* `reload` tells a running service to re-read its configuration files without dropping connections; it does not configure boot behavior.
    *   *Why D is incorrect:* `status` simply reports whether the service is currently running or stopped.

---

**Question 3**
A systems administrator or developer needs to **list all currently active processes running on the system with CPU and memory usage statistics**. Which of the following commands is the most appropriate to execute?
B) df -h
C) chmod 600 config.conf
D) systemctl restart service
A) ps aux
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ps aux` command is directly designed to list all currently active processes running on the system with CPU and memory usage statistics.


---

**Question 4**
While working on **Permissions** in a production environment, you encounter a system alert indicating a **Disk Space Full** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Prepend the command with 'sudo' to run it with superuser administrative privileges, or adjust the file permissions.
D) Reboot the physical machine and wait for services to reload.
C) Identify and terminate the process already utilizing the target port, or modify the service configuration to use an open port.
A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Correct Answer:** A) Run log rotations, clean temporary files, or expand the logical volume capacity.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why D is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why C is incorrect:* This action does not resolve the root cause of Disk Space Full.
    * *Why A is correct:* Because The storage volume has run out of space, preventing files from being written and causing system services to fail. The appropriate fix is to Run log rotations, clean temporary files, or expand the logical volume capacity..


---

**Question 5**
When designing a system for **Permissions**, you must mitigate the risk of **Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enforce the principle of least privilege, requiring users to log in with standard accounts and elevate privileges via sudo/UAC.
D) Enable full disk encryption on all client endpoints.
A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Correct Answer:** A) Disable unused system accounts and run a port scan to disable unnecessary active background services.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why B is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why D is incorrect:* This does not address the security vulnerability of Stale Accounts & Services.
    * *Why A is correct:* Implementing Disable unused system accounts and run a port scan to disable unnecessary active background services. mitigates the risk of Attackers exploiting vulnerabilities in forgotten background services or using abandoned accounts to gain persistent access..

