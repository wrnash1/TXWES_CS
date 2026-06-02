# Quiz: Module 06 - Process Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

A systems administrator wants to view all currently running processes for all users, including processes not attached to a terminal, in a user-friendly format showing CPU and memory usage. Which command is correct?

- A) ps -e
- B) ps aux
- C) top -b -n 1
- D) pgrep -l nginx

Correct Answer: B) ps aux

Distractor Analysis:

- Why A is incorrect: ps -e lists all processes but uses a minimal format that does not include CPU/memory percentages or the full command path.
- Why C is incorrect: top -b -n 1 runs top in batch mode for one iteration, which is useful for scripting, but the default ps aux is the standard answer for a human-readable snapshot of all processes.
- Why D is incorrect: pgrep -l nginx searches for processes matching the name nginx and lists their PIDs. It does not show all processes or include CPU/memory statistics.

---

**Question 2**

A web server process with PID 4821 has stopped responding to requests and is consuming 100% CPU. The administrator needs to immediately terminate it without waiting for a graceful shutdown. Which command is correct?

- A) kill 4821
- B) kill -1 4821
- C) kill -9 4821
- D) kill -15 4821

Correct Answer: C) kill -9 4821

Distractor Analysis:

- Why A is incorrect: kill 4821 sends SIGTERM (signal 15), which requests a graceful shutdown. A hung process may be unable or unwilling to respond to SIGTERM, making it ineffective here.
- Why B is incorrect: kill -1 sends SIGHUP, traditionally used to tell a process to reload its configuration file. It does not terminate a hung process.
- Why D is incorrect: kill -15 is equivalent to the default kill with no flag — it sends SIGTERM for graceful termination, which is insufficient for a process that is not responding.

---

**Question 3**

An administrator needs to display total disk space usage across all mounted filesystems in a human-readable format. Which command is correct?

- A) du -sh /*
- B) df -h
- C) lsblk -f
- D) fdisk -l

Correct Answer: B) df -h

Distractor Analysis:

- Why A is incorrect: du -sh /* calculates disk usage consumed by files in each top-level directory, not the total capacity/usage/available space per mounted filesystem.
- Why C is incorrect: lsblk -f shows block device layout, filesystem types, and UUIDs, but does not display used and available space in human-readable sizes.
- Why D is incorrect: fdisk -l lists partition tables on block devices. It shows partition sizes in bytes/sectors but does not report filesystem usage or available space.

---

**Question 4**

After editing the unit file for a custom systemd service at /etc/systemd/system/myapp.service, the administrator runs systemctl restart myapp but the old configuration is still in effect. What step was missed?

- A) The service needed to be stopped with systemctl stop myapp before editing the unit file.
- B) systemctl daemon-reload must be run after editing a unit file to reload systemd's configuration from disk.
- C) The unit file must be placed in /usr/lib/systemd/system/ instead of /etc/systemd/system/.
- D) The administrator must reboot the system for changes to unit files to take effect.

Correct Answer: B) systemctl daemon-reload must be run after editing a unit file to reload systemd's configuration from disk.

Distractor Analysis:

- Why A is incorrect: Stopping the service before editing the unit file is not required, and does not cause systemd to re-read the file. The missing step is explicitly telling systemd to reload its unit file cache.
- Why C is incorrect: /etc/systemd/system/ is the correct and preferred location for administrator-created and administrator-modified unit files. It takes precedence over /usr/lib/systemd/system/, which is owned by packages.
- Why D is incorrect: A full system reboot is not required and would be disruptive. systemctl daemon-reload followed by systemctl restart myapp is the correct and non-disruptive procedure.

---

**Question 5**

A Linux system shows a process in ps aux output with a STAT value of Z. What does this indicate, and what is the correct resolution?

- A) The process is consuming excessive CPU. Send it SIGKILL to terminate it immediately.
- B) The process is sleeping and waiting for I/O. It will resume automatically when the I/O completes.
- C) The process has finished executing but its parent has not collected its exit status. Fix or terminate the parent process.
- D) The process is stopped by a signal. Send SIGCONT to resume it.

Correct Answer: C) The process has finished executing but its parent has not collected its exit status. Fix or terminate the parent process.

Distractor Analysis:

- Why A is incorrect: A Z (zombie) process is already dead — it is not consuming CPU. Sending SIGKILL has no effect on a zombie because there is no running code to kill.
- Why B is incorrect: A process waiting for I/O is shown with the STAT value D (uninterruptible sleep), not Z.
- Why D is incorrect: A stopped process is shown with STAT value T. SIGCONT resumes a stopped process. Zombies are not stopped — they are complete but uncollected, and SIGCONT is irrelevant to them.

---

**Question 6**

An administrator runs the command nice -n 15 tar -czf backup.tar.gz /var/log/ to compress a large log directory. What is the purpose of the nice -n 15 prefix, and why would an administrator use it on a production server?

- A) It runs the tar command with root privileges so it can read all log files.
- B) It starts the tar process with a low-priority nice value of 15, reducing its CPU scheduling priority so it competes less with production workloads.
- C) It sets the maximum number of CPU cores that tar can use to 15, limiting its resource consumption.
- D) It increases the I/O priority of the tar process so the backup completes faster.

Correct Answer: B) It starts the tar process with a low-priority nice value of 15, reducing its CPU scheduling priority so it competes less with production workloads.

Distractor Analysis:

- Why A is incorrect: nice does not affect privileges. It adjusts CPU scheduling priority only. Running a command with elevated privileges requires sudo or similar tools.
- Why C is incorrect: nice does not control the number of CPU cores. The nice value is a scheduling weight, not a CPU affinity or core count limit.
- Why D is incorrect: nice affects CPU scheduling priority, not I/O priority. I/O priority is controlled by ionice, which is a separate command.

---

**Question 7**

An administrator needs to send a signal to the sshd daemon that causes it to reload its configuration file without stopping and restarting the service. Which command achieves this?

- A) sudo kill -9 $(pidof sshd)
- B) sudo kill -15 $(pidof sshd)
- C) sudo kill -1 $(pidof sshd)
- D) sudo pkill -u root sshd

Correct Answer: C) sudo kill -1 $(pidof sshd)

Distractor Analysis:

- Why A is incorrect: kill -9 sends SIGKILL, which forces immediate termination. This would kill the sshd daemon entirely, dropping all active SSH sessions, rather than reloading its configuration.
- Why B is incorrect: kill -15 sends SIGTERM, which requests graceful termination. sshd would shut down, not reload its configuration.
- Why D is incorrect: pkill -u root sshd sends the default SIGTERM to all processes owned by root matching sshd. This would terminate sshd rather than reload it, and targeting all root-owned processes named sshd could have unintended effects.

---

**Question 8**

An administrator runs systemctl enable nginx on a newly configured server. Which of the following best describes what this command does?

- A) It installs the nginx package and starts the service immediately.
- B) It creates a symlink that causes nginx to start automatically at every system boot, but does not start the service right now.
- C) It starts the nginx service immediately and also marks it to start at every boot.
- D) It verifies that the nginx unit file is correctly configured and reports any syntax errors.

Correct Answer: B) It creates a symlink that causes nginx to start automatically at every system boot, but does not start the service right now.

Distractor Analysis:

- Why A is incorrect: systemctl does not install packages. Package installation is handled by apt or dnf. systemctl enable only manages the boot-time autostart configuration.
- Why C is incorrect: systemctl enable does not start the service immediately. To both enable and start, the administrator would need systemctl enable --now nginx, which is a combined command.
- Why D is incorrect: systemctl enable does not validate unit file syntax. The systemd-analyze verify command performs unit file validation.

---

**Question 9**

A systems administrator runs journalctl -u nginx -f and watches the output while testing a web server. What does the -f flag do in this command?

- A) It displays only critical failure (fault) messages from the nginx service log.
- B) It outputs the full journal in a formatted, paginated view suitable for reading.
- C) It follows the nginx journal in real time, displaying new log entries as they are written.
- D) It filters the journal to show only entries from the current filesystem boot.

Correct Answer: C) It follows the nginx journal in real time, displaying new log entries as they are written.

Distractor Analysis:

- Why A is incorrect: There is no -f flag for failure filtering in journalctl. Filtering by priority uses the -p flag with a priority level such as err or crit.
- Why B is incorrect: journalctl already paginates by default using the less pager. The -f flag specifically enables real-time following mode, similar to tail -f for traditional log files.
- Why D is incorrect: The -b flag limits output to entries from the current boot. The -f flag enables live following with no boot-time restriction.

---

**Question 10**

A background process on a Linux system has a nice value of 0. A systems administrator wants to lower its CPU priority so it does not interfere with interactive user sessions. The process PID is 7834. Which command correctly reduces the process scheduling priority?

- A) renice -n -10 -p 7834
- B) renice -n 10 -p 7834
- C) nice -n 10 -p 7834
- D) renice -n 0 -p 7834

Correct Answer: B) renice -n 10 -p 7834

Distractor Analysis:

- Why A is incorrect: renice -n -10 sets the nice value to -10, which is a higher (better) scheduling priority than the default 0. This would make the process more aggressive in consuming CPU, the opposite of the goal. Only root can set negative nice values.
- Why C is incorrect: nice is used to start a new process with a specified nice value. It cannot be applied to an already-running process by PID. renice is the correct tool for modifying a running process's priority.
- Why D is incorrect: renice -n 0 sets the nice value back to 0 (the default), which is no change from the current value. This does not lower the priority.
