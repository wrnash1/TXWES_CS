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

---

Questions 11-20 — 5 pts each

---

**Question 11**

An administrator notices a process with STAT code D in ps aux output. What does this state
indicate, and why can it not be killed with SIGKILL?

- A) The process is stopped (paused) by a debugger. SIGKILL is blocked by the debugging subsystem.
- B) The process is in uninterruptible sleep, waiting for I/O to complete. The kernel ignores all signals, including SIGKILL, until the I/O operation finishes.
- C) The process is a zombie that has already exited. SIGKILL cannot affect already-dead processes.
- D) The process is a daemon started by systemd. systemd intercepts SIGKILL before it reaches the process.

Correct Answer: B) The process is in uninterruptible sleep, waiting for I/O to complete. The kernel ignores all signals, including SIGKILL, until the I/O operation finishes.

Distractor Analysis:

- Why A is incorrect: A process stopped by a debugger shows STAT code T (traced), not D. Debugging uses SIGSTOP/SIGCONT, not uninterruptible sleep.
- Why C is incorrect: Zombie processes show STAT code Z, not D. A zombie has already completed execution and cannot be killed because it no longer has a running process body.
- Why D is incorrect: systemd does not intercept signals to managed processes. The D state is a kernel-level scheduling state that makes the process unresponsive to signals regardless of who started it.

---

**Question 12**

Which command displays a real-time, continuously updating view of processes sorted by CPU
usage, with the ability to send signals interactively?

- A) ps aux --sort=-%cpu | head -20
- B) top
- C) htop
- D) Both B and C

Correct Answer: D) Both B and C

Distractor Analysis:

- Why A is incorrect: ps aux is a static snapshot that executes once and exits. It does not continuously update. It cannot send signals interactively.
- Why B alone is partially correct: top provides real-time continuous updates and allows sending signals by pressing k (kill) then entering a PID and signal number. It is available on all Linux systems by default.
- Why C alone is partially correct: htop is an enhanced version of top with a more visual interface and mouse support. Both provide real-time updates and interactive signal sending, making D the most complete answer.

---

**Question 13**

An administrator runs kill -l and wants to understand what signal number 15 is. Which
statement is correct?

- A) Signal 15 is SIGKILL, which immediately terminates a process and cannot be caught or ignored.
- B) Signal 15 is SIGTERM, which requests graceful termination and can be caught by a process to perform cleanup.
- C) Signal 15 is SIGHUP, which causes daemons to reload their configuration files.
- D) Signal 15 is SIGSTOP, which pauses process execution.

Correct Answer: B) Signal 15 is SIGTERM, which requests graceful termination and can be caught by a process to perform cleanup.

Distractor Analysis:

- Why A is incorrect: SIGKILL is signal number 9, not 15. SIGKILL cannot be caught or ignored. SIGTERM (15) can be caught, allowing a process to clean up before exiting.
- Why C is incorrect: SIGHUP is signal number 1. While SIGHUP does cause many daemons to reload configuration, it is not signal 15.
- Why D is incorrect: SIGSTOP is signal number 19. Like SIGKILL, SIGSTOP cannot be caught or ignored. It pauses a process, which can be resumed with SIGCONT (signal 18).

---

**Question 14**

A systems administrator runs jobs and sees:

[1]+  Stopped    vim /etc/nginx/nginx.conf
[2]-  Running    ./backup.sh &

The administrator wants to bring job 1 back to the foreground. Which command is correct?

- A) bg 1
- B) fg %1
- C) resume 1
- D) kill -SIGCONT %1

Correct Answer: B) fg %1

Distractor Analysis:

- Why A is incorrect: bg 1 resumes job 1 in the background (as if it had been started with &). It does not bring it to the foreground where keyboard input can be sent to it.
- Why C is incorrect: resume is not a valid shell built-in command. The correct shell built-ins for job control are fg and bg.
- Why D is incorrect: kill -SIGCONT %1 sends the continue signal to the job, which resumes it. However, it resumes in the background, not the foreground, and does not reconnect it to the terminal's stdin/stdout in the same way fg does.

---

**Question 15**

An administrator uses systemctl to manage the nginx service on Ubuntu 22.04. They run
systemctl reload nginx instead of systemctl restart nginx. What is the key operational
difference?

- A) reload completely stops and restarts the nginx process, resetting all active connections.
- B) reload sends SIGHUP to nginx, causing it to re-read its configuration without dropping active connections, while restart stops and starts the process, briefly interrupting all connections.
- C) reload only works when nginx has a syntax error in its configuration. restart is used for normal configuration changes.
- D) reload updates the systemd unit file. restart applies new configuration inside nginx.

Correct Answer: B) reload sends SIGHUP to nginx, causing it to re-read its configuration without dropping active connections, while restart stops and starts the process, briefly interrupting all connections.

Distractor Analysis:

- Why A is incorrect: This describes restart, not reload. reload is specifically designed to avoid dropping connections by signaling the process to re-read its config while continuing to serve requests.
- Why C is incorrect: reload is the preferred method for applying configuration changes in production. It is not specific to error scenarios. nginx --test should be run before reload to verify syntax, but reload itself is for normal config updates.
- Why D is incorrect: systemctl daemon-reload updates systemd's in-memory view of unit files. systemctl reload sends a signal to the service process itself. The two concepts are separate and D conflates them.

---

**Question 16**

An administrator wants to find all processes belonging to the user www-data using a single
command. Which command is most appropriate?

- A) ps -u www-data
- B) pgrep -u www-data
- C) pidof www-data
- D) Both A and B

Correct Answer: D) Both A and B

Distractor Analysis:

- Why A alone is partially correct: ps -u www-data lists all processes owned by www-data in a formatted table showing PID, TTY, CPU time, and command name.
- Why B alone is partially correct: pgrep -u www-data lists only the PIDs of processes owned by www-data, one per line, which is useful for scripting.
- Why C is incorrect: pidof finds processes by exact program name, not by user. pidof www-data would look for a program named "www-data", which does not exist. It would return nothing.

---

**Question 17**

After modifying a systemd unit file at /etc/systemd/system/myapp.service, which command
must be run before the changes take effect when restarting the service?

- A) systemctl update myapp
- B) systemctl daemon-reload
- C) systemctl refresh myapp
- D) systemctl reload myapp

Correct Answer: B) systemctl daemon-reload

Distractor Analysis:

- Why A is incorrect: systemctl update is not a valid subcommand. systemctl does not have an update command for unit files.
- Why C is incorrect: systemctl refresh is not a valid subcommand. There is no refresh command in systemctl.
- Why D is incorrect: systemctl reload myapp sends a signal to the running myapp process to re-read its own application configuration. It does not tell systemd to re-read the unit file from disk. daemon-reload is what tells the systemd manager itself to rescan and reload unit files.

---

**Question 18**

An administrator runs ps aux and sees a process with the STAT code Z. What is the correct
resolution for this zombie process?

- A) Send SIGKILL to the zombie process PID.
- B) Run kill -9 on the zombie's parent process (PPID) or wait for the parent to call wait().
- C) Renice the zombie to priority 19 to let the scheduler clean it up.
- D) Run systemctl daemon-reexec to force systemd to reap all zombie processes.

Correct Answer: B) Run kill -9 on the zombie's parent process (PPID) or wait for the parent to call wait().

Distractor Analysis:

- Why A is incorrect: A zombie process has already exited. It has no running process to kill. SIGKILL sent to a zombie PID has no effect because there is no active process body to receive it.
- Why C is incorrect: renice affects the scheduler priority of running processes. A zombie is not running and cannot be reniced. The scheduler does not reap zombie entries.
- Why D is incorrect: systemctl daemon-reexec re-executes the systemd manager binary in place for upgrades. It does not specifically reap zombie processes. Only the zombie's parent can reap it by calling the wait() system call, or the parent can be terminated so init (PID 1) adopts and reaps the zombie.

---

**Question 19**

An administrator starts a long-running script with nohup ./backup.sh > /tmp/backup.log 2>&1 &
and then closes the terminal. What happens to the script?

- A) The script is terminated when the terminal closes because it is a child process of the shell.
- B) The script continues running because nohup makes it immune to the SIGHUP signal sent when the terminal closes.
- C) The script is paused until the administrator opens a new terminal and runs fg.
- D) The script runs in a new virtual console (tty) automatically created by nohup.

Correct Answer: B) The script continues running because nohup makes it immune to the SIGHUP signal sent when the terminal closes.

Distractor Analysis:

- Why A is incorrect: Without nohup, closing the terminal sends SIGHUP to child processes, which normally terminates them. nohup specifically prevents this by ignoring SIGHUP and redirecting output so the process can continue after the terminal disconnects.
- Why C is incorrect: nohup does not pause the process. The & at the end of the command backgrounds it immediately. nohup only handles the SIGHUP signal; it does not pause or suspend the process.
- Why D is incorrect: nohup does not create virtual consoles. The process continues running under its original process group, now adopted by init or systemd after the parent shell exits.

---

**Question 20**

Which command displays the parent-child process hierarchy in a tree format, showing which
processes spawned which child processes?

- A) ps aux --forest
- B) pstree
- C) ps -ejH
- D) All of the above show process hierarchy

Correct Answer: D) All of the above show process hierarchy

Distractor Analysis:

- Why A alone is partially correct: ps aux --forest (or ps auxf) displays an ASCII tree of process parent-child relationships directly in ps output.
- Why B alone is partially correct: pstree is a dedicated tool that displays the complete process tree with branch symbols, optionally showing PIDs and user names with -p and -u flags.
- Why C alone is partially correct: ps -ejH displays all processes in a hierarchical (indented) format showing the tree structure. All three commands reveal parent-child process relationships.
