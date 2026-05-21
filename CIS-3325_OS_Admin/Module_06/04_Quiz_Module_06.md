# Quiz: Module 06 - Process Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
A systems administrator wants to view all currently running processes for all users, including processes not attached to a terminal, in a user-friendly format showing CPU and memory usage. Which command is correct?
A) ps -e
B) ps aux
C) top -b -n 1
D) pgrep -l nginx
*   **Correct Answer:** B) ps aux
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ps -e` lists all processes but uses a minimal format that does not include CPU/memory percentages or the full command path.
    *   *Why C is incorrect:* `top -b -n 1` runs top in batch mode for one iteration, which is useful for scripting, but the default `ps aux` is the standard answer for a human-readable snapshot of all processes.
    *   *Why D is incorrect:* `pgrep -l nginx` searches for processes matching the name `nginx` and lists their PIDs. It does not show all processes or include CPU/memory statistics.

---

---

**Question 2**
A web server process with PID 4821 has stopped responding to requests and is consuming 100% CPU. The administrator needs to immediately terminate it without waiting for a graceful shutdown. Which command is correct?
A) kill 4821
B) kill -1 4821
C) kill -9 4821
D) kill -15 4821
*   **Correct Answer:** C) kill -9 4821
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `kill 4821` sends SIGTERM (signal 15), which requests a graceful shutdown. A hung process may be unable or unwilling to respond to SIGTERM, making it ineffective here.
    *   *Why B is incorrect:* `kill -1` sends SIGHUP, traditionally used to tell a process to reload its configuration file. It does not terminate a hung process.
    *   *Why D is incorrect:* `kill -15` is equivalent to the default `kill` with no flag — it sends SIGTERM for graceful termination, which is insufficient for a process that is not responding.

---

---

**Question 3**
An administrator needs to display total disk space usage across all mounted filesystems in a human-readable format. Which command is correct?
A) du -sh /*
B) df -h
C) lsblk -f
D) fdisk -l
*   **Correct Answer:** B) df -h
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `du -sh /*` calculates disk usage consumed by files in each top-level directory, not the total capacity/usage/available space per mounted filesystem.
    *   *Why C is incorrect:* `lsblk -f` shows block device layout, filesystem types, and UUIDs, but does not display used and available space in human-readable sizes.
    *   *Why D is incorrect:* `fdisk -l` lists partition tables on block devices. It shows partition sizes in bytes/sectors but does not report filesystem usage or available space.

---

**Question 4**
After editing the unit file for a custom systemd service at `/etc/systemd/system/myapp.service`, the administrator runs `systemctl restart myapp` but the old configuration is still in effect. What step was missed?
A) The service needed to be stopped with `systemctl stop myapp` before editing the unit file.
B) `systemctl daemon-reload` must be run after editing a unit file to reload systemd's configuration from disk.
C) The unit file must be placed in `/usr/lib/systemd/system/` instead of `/etc/systemd/system/`.
D) The administrator must reboot the system for changes to unit files to take effect.
*   **Correct Answer:** B) `systemctl daemon-reload` must be run after editing a unit file to reload systemd's configuration from disk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Stopping the service before editing the unit file is not required, and does not cause systemd to re-read the file. The missing step is explicitly telling systemd to reload its unit file cache.
    *   *Why C is incorrect:* `/etc/systemd/system/` is the correct and preferred location for administrator-created and administrator-modified unit files. It takes precedence over `/usr/lib/systemd/system/`, which is owned by packages.
    *   *Why D is incorrect:* A full system reboot is not required and would be disruptive. `systemctl daemon-reload` followed by `systemctl restart myapp` is the correct and non-disruptive procedure.

---

**Question 5**
A Linux system shows a process in `ps aux` output with a STAT value of `Z`. What does this indicate, and what is the correct resolution?
A) The process is consuming excessive CPU. Send it SIGKILL to terminate it immediately.
B) The process is sleeping and waiting for I/O. It will resume automatically when the I/O completes.
C) The process has finished executing but its parent has not collected its exit status. Fix or terminate the parent process.
D) The process is stopped by a signal. Send SIGCONT to resume it.
*   **Correct Answer:** C) The process has finished executing but its parent has not collected its exit status. Fix or terminate the parent process.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Z (zombie) process is already dead — it is not consuming CPU. Sending SIGKILL has no effect on a zombie because there is no running code to kill.
    *   *Why B is incorrect:* A process waiting for I/O is shown with the STAT value `D` (uninterruptible sleep), not `Z`.
    *   *Why D is incorrect:* A stopped process is shown with STAT value `T`. SIGCONT resumes a stopped process. Zombies are not stopped — they are complete but uncollected, and SIGCONT is irrelevant to them.

