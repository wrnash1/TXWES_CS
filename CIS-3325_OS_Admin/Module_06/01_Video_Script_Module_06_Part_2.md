# Video Script: Module 06 - Process Management (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - Signals, systemctl, and Service Management

---

### Opening

Welcome back to Part 2 of Module 06. In Part 1 we covered process monitoring with ps, top,
and htop, process priority with nice and renice, and background job control. In Part 2 we
cover process signals, killing processes, zombie processes, and systemd service management
with systemctl. These are the hands-on skills that differentiate an administrator who can
fix problems from one who watches them persist.

---

### Section 1: Linux Process Signals

A signal is a software interrupt sent to a process. The process's signal handler code decides
what to do with it - unless the signal is SIGKILL, which the kernel handles directly and
cannot be intercepted.

[SHOW TERMINAL]

```bash
kill -l
```

This lists all signals and their numbers. Know these for the exam:

| Signal | Number | Name | Default Action |
|--------|--------|------|----------------|
| SIGHUP | 1 | Hangup | Reload config or terminate |
| SIGINT | 2 | Interrupt | Terminate (from Ctrl+C) |
| SIGKILL | 9 | Kill | Force terminate (cannot be caught) |
| SIGTERM | 15 | Terminate | Graceful shutdown (default kill) |
| SIGSTOP | 19 | Stop | Pause process (cannot be caught) |
| SIGCONT | 18 | Continue | Resume stopped process |

---

### Section 2: The kill Command

[SHOW TERMINAL]

```bash
kill 12345
```

Sends SIGTERM (15) to process 12345. Requests graceful shutdown. Well-behaved processes
save their state and exit cleanly. Some processes ignore SIGTERM.

```bash
kill -9 12345
```

Sends SIGKILL. The kernel forces immediate termination. The process cannot catch or ignore this.
Use this only when SIGTERM fails. SIGKILL does not allow the process to clean up - files may
be left in an inconsistent state.

```bash
kill -1 12345
```

Sends SIGHUP. Many daemons use this to reload their configuration without restarting.
Apache and nginx both support SIGHUP for config reload.

```bash
kill -SIGTERM 12345
kill -TERM 12345
```

You can use signal names instead of numbers.

```bash
killall nginx
```

killall sends a signal to all processes matching the name. Convenient but potentially
dangerous - verify the process name before using killall on a production system.

```bash
pkill -u alice
```

pkill kills all processes owned by user alice. Useful when disabling a user account.

---

### Section 3: Zombie Processes

[SHOW TERMINAL]

```bash
ps aux | grep Z
```

A zombie process shows STAT value Z. It is a process that has finished executing but whose
parent process has not yet called wait() to collect its exit status.

Zombies cannot be killed with SIGKILL because they are already dead - there is no code running
to kill. The only fix is to address the parent process:

Option 1: If the parent is misbehaving, fix or restart it.
Option 2: If the parent is stuck and cannot be fixed, kill the parent. The zombie will then
be adopted by PID 1 (systemd), which will properly reap it.

A small number of zombies is normal and harmless. A large or growing number indicates a bug
in a parent process that is not properly cleaning up after child processes.

---

### Section 4: systemd and systemctl Overview

Modern Linux uses systemd as PID 1 - the first process started by the kernel and the parent
of all other processes. systemd manages services (daemons), mounts, sockets, and system state.

[SHOW TERMINAL]

```bash
ps -p 1
```

PID 1 is systemd on modern systems.

```bash
systemctl list-units --type=service
```

List all service units and their current state.

```bash
systemctl list-units --type=service --state=running
```

Show only actively running services.

```bash
systemctl list-unit-files --type=service
```

Show all service unit files and whether they are enabled (start at boot) or disabled.

---

### Section 5: Controlling Services with systemctl

[SHOW TERMINAL]

```bash
systemctl status ssh
```

Shows current state: active (running) or inactive (dead), start time, PID, recent log lines.

```bash
sudo systemctl start ssh
```

Start the service right now.

```bash
sudo systemctl stop ssh
```

Stop the service right now.

```bash
sudo systemctl restart ssh
```

Stop then start. Use this after major configuration changes.

```bash
sudo systemctl reload ssh
```

Ask the service to reload its configuration without stopping. Many services support this.
Preferred over restart when possible because it avoids dropping active connections.

```bash
sudo systemctl enable ssh
```

Configure the service to start automatically at every boot. Creates a symlink in the
appropriate systemd target directory.

```bash
sudo systemctl disable ssh
```

Remove from boot sequence. Does not stop the currently running service.

```bash
sudo systemctl enable --now ssh
```

Enable at boot AND start immediately. This is the most common pattern for new service setup.

```bash
sudo systemctl is-active ssh
sudo systemctl is-enabled ssh
```

These return active/inactive or enabled/disabled, and exit with code 0 for the first state.
Useful in scripts: if systemctl is-active nginx returns non-zero, the service is not running.

---

### Section 6: Editing Unit Files and daemon-reload

[SHOW TERMINAL]

```bash
cat /lib/systemd/system/ssh.service
```

This is the package-installed unit file for SSH. Never edit files in /lib/systemd/system/
directly because package upgrades will overwrite your changes.

To customize, create a drop-in override:

```bash
sudo systemctl edit ssh
```

This creates a file in /etc/systemd/system/ssh.service.d/override.conf. Changes here survive
package upgrades.

After any unit file edit:

```bash
sudo systemctl daemon-reload
```

This is mandatory before your changes take effect. Without daemon-reload, systemd is still
running with its cached copy of the old unit file.

```bash
sudo systemctl restart ssh
```

After daemon-reload, restart the service to apply changes.

This is one of the most tested exam scenarios: "edited a unit file, restarted the service,
but old configuration is still active." The missing step is daemon-reload.

---

### Section 7: journalctl for Service Logs

[SHOW TERMINAL]

```bash
journalctl -u ssh
```

Show all journal entries for the ssh service.

```bash
journalctl -u ssh -b
```

Journal entries for ssh since the last boot (-b).

```bash
journalctl -u ssh -f
```

Follow the ssh log in real time, showing new entries as they arrive.

```bash
journalctl -u ssh --since "2026-01-01"
journalctl -u ssh --since "1 hour ago"
```

Restrict to a time range.

```bash
journalctl -p err -b
```

Show only error and higher priority messages from the current boot.

```bash
journalctl -n 50
```

Show the last 50 journal entries across all services.

---

### Section 8: Exam Tips for Module 06

SIGKILL versus SIGTERM: SIGTERM (15) is the default, allows graceful shutdown. SIGKILL (9)
forces immediate termination, cannot be caught. Use SIGTERM first; only escalate to SIGKILL
if the process is unresponsive.

systemctl enable versus systemctl start: enable configures boot-time autostart. start starts
immediately. Both are needed for a new service: enable --now does both in one command.

daemon-reload is required after editing unit files. This is a tested scenario every semester.

Zombie processes (STAT=Z) are already dead. SIGKILL has no effect. Fix the parent.

Load average: the three numbers after "load average:" are the 1-minute, 5-minute, and 15-minute
averages. A value above the number of CPU cores indicates CPU saturation.

journalctl -u servicename is the primary log inspection tool on systemd systems.

---

### Lab Preview

This week's lab has you using ps aux, top, and pgrep to find specific processes, sending signals
with kill, starting and stopping services with systemctl, enabling a service at boot, running
daemon-reload after editing a unit file, and inspecting service logs with journalctl.

---

### Summary

Module 06 covers the complete Linux process and service management workflow: monitoring with
ps, top, and htop; signals and kill; zombie processes; and systemd service management with
systemctl and journalctl.

Module 07 covers shell scripting fundamentals - automating all the commands you have learned
so far.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
