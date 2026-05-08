### 4. Lab 4: Managing Processes and Daemons
**Objective:** Monitor system resources, kill rogue processes, and manage background services.
**Instructions:**
1. Log into your Ubuntu Server VM.
2. Start a continuous ping in the background: `ping google.com > /dev/null &`
3. Use the `ps aux | grep ping` command to find the Process ID (PID) of your ping command.
4. Kill the process forcefully: `sudo kill -9 [Your_PID_Here]`
5. Now, let's manage a service. Check the status of the SSH daemon: `systemctl status ssh`
6. Restart the SSH service: `sudo systemctl restart ssh`
7. Verify it is running again using the status command.
**Deliverable:** Take a screenshot showing the output of your `ps aux` command, the `kill` command, and the final `systemctl status ssh` showing it is actively running.

---
