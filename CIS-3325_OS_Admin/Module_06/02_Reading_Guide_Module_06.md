# Reading Guide: Module 06 - Process Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 1.0 - System Management

---

### Glossary

**Process** - A running instance of a program with its own PID, memory space, file descriptors, and execution state.

**PID (Process ID)** - A unique integer assigned by the kernel to each running process. Assigned sequentially and recycled after processes exit.

**PPID (Parent Process ID)** - The PID of the process that created the current process. Every process except PID 1 has a parent.

**Nice Value** - A scheduling priority hint ranging from -20 (highest CPU priority) to +19 (lowest). Default is 0. Only root can set negative values.

**Signal** - A software interrupt delivered to a process that triggers a predefined or custom response. Some signals can be caught; SIGKILL and SIGSTOP cannot.

**Zombie Process** - A process that has completed execution but whose parent has not called wait() to collect its exit status. Shows STAT=Z in ps output.

**Orphan Process** - A process whose parent has exited. Orphans are adopted by PID 1 (systemd), which will reap them when they exit.

**systemd** - The init system used on modern Linux distributions. Runs as PID 1 and manages all services, mounts, sockets, and system state.

**Unit File** - A configuration file that defines a systemd service, mount, socket, timer, or other managed object.

**daemon-reload** - The systemctl command that instructs systemd to re-read all unit files from disk. Required after editing any unit file.

**journalctl** - The command-line tool for querying the systemd journal, which collects log entries from all systemd-managed services and the kernel.

**Load Average** - A measure of system workload shown as three numbers representing 1-minute, 5-minute, and 15-minute averages. Values above the CPU core count indicate saturation.

---

### Process State Codes (ps STAT Column)

| Code | State | Description |
|------|-------|-------------|
| R | Running | Actively using CPU or waiting in the run queue |
| S | Sleeping (interruptible) | Waiting for input or an event; can be interrupted by a signal |
| D | Uninterruptible sleep | Waiting for I/O (disk, network); cannot be interrupted by signals |
| Z | Zombie | Finished executing; parent has not collected exit status |
| T | Stopped | Suspended by SIGSTOP or Ctrl+Z |
| I | Idle | Idle kernel thread |

Additional modifier characters that may appear after the primary state:

| Modifier | Meaning |
|----------|---------|
| + | Process is in the foreground process group |
| s | Process is a session leader |
| l | Multi-threaded process |
| < | High priority (negative nice value) |
| N | Low priority (positive nice value) |

---

### Linux Signal Reference

| Signal Name | Number | Catchable | Default Action |
|-------------|--------|-----------|----------------|
| SIGHUP | 1 | Yes | Reload config or terminate |
| SIGINT | 2 | Yes | Terminate (Ctrl+C) |
| SIGQUIT | 3 | Yes | Terminate with core dump |
| SIGKILL | 9 | No | Force terminate (kernel handles directly) |
| SIGTERM | 15 | Yes | Graceful terminate (default kill signal) |
| SIGSTOP | 19 | No | Pause process |
| SIGCONT | 18 | Yes | Resume stopped process |
| SIGTSTP | 20 | Yes | Pause process (Ctrl+Z) |

Key exam rules:

- SIGKILL (9) cannot be caught or ignored. The kernel terminates the process immediately.
- SIGSTOP (19) cannot be caught or ignored. Only SIGCONT resumes a stopped process.
- SIGTERM (15) is the default signal sent by kill with no flag. Allows graceful cleanup.
- SIGHUP (1) is used by many daemons as a configuration reload trigger.

---

### Process Monitoring Commands

| Command | Purpose | Key Options |
|---------|---------|-------------|
| ps aux | Snapshot of all processes | a=all users, u=user format, x=no terminal |
| ps -ef | Alternative full-format listing | -e=all, -f=full format with PPID |
| top | Real-time interactive process viewer | q=quit, k=kill, r=renice, M=sort memory, P=sort CPU, 1=per-core |
| htop | Enhanced interactive viewer (install required) | F9=signal, F6=sort, F5=tree view |
| pgrep name | Return PIDs matching process name | -l=include name, -u=filter by user |
| pidof name | Return PIDs of a named program | Simpler than pgrep for exact names |
| ps -p PID | Show information for a specific PID | |

---

### Process Priority Commands

| Command | Effect | Notes |
|---------|--------|-------|
| nice -n VALUE cmd | Start a command with a specified nice value | VALUE range: -20 to +19; default is 0 |
| renice -n VALUE -p PID | Change nice value of a running process | Only root can set negative values |
| renice -n VALUE -u USER | Change nice value for all processes of a user | Requires root for decreasing values |

Nice value conventions:

- -20: Highest priority (reserved for critical system processes)
- 0: Default priority
- +10 to +19: Background/batch jobs (backups, compression)
- Regular users can only increase (worsen) their process priority above 0.

---

### Process Signal Commands

| Command | Signal Sent | Effect |
|---------|------------|--------|
| kill PID | SIGTERM (15) | Request graceful shutdown |
| kill -9 PID | SIGKILL (9) | Force immediate termination |
| kill -1 PID | SIGHUP (1) | Request config reload (most daemons) |
| kill -15 PID | SIGTERM (15) | Explicit graceful shutdown |
| killall name | SIGTERM (15) | Terminate all processes matching name |
| killall -9 name | SIGKILL (9) | Force terminate all matching by name |
| pkill pattern | SIGTERM (15) | Signal processes matching pattern |
| pkill -u USER | SIGTERM (15) | Signal all processes owned by user |

---

### Job Control Commands

| Command | Effect |
|---------|--------|
| command & | Run command in background; shell returns immediately |
| jobs | List all background jobs in the current shell session |
| fg N | Bring job number N to the foreground |
| bg N | Resume suspended job number N in the background |
| Ctrl+Z | Suspend the current foreground job (sends SIGTSTP) |
| nohup command & | Run in background; survives terminal close; output to nohup.out |

---

### systemctl Service Management Commands

| Command | Effect |
|---------|--------|
| systemctl status SERVICE | Show current state, PID, uptime, recent log entries |
| systemctl start SERVICE | Start the service immediately |
| systemctl stop SERVICE | Stop the service immediately |
| systemctl restart SERVICE | Stop then start (use after major config changes) |
| systemctl reload SERVICE | Ask service to reload config without stopping |
| systemctl enable SERVICE | Configure service to start at every boot |
| systemctl disable SERVICE | Remove from boot startup |
| systemctl enable --now SERVICE | Enable at boot AND start immediately |
| systemctl is-active SERVICE | Returns active or inactive; exit code 0 = active |
| systemctl is-enabled SERVICE | Returns enabled or disabled; exit code 0 = enabled |
| systemctl daemon-reload | Re-read all unit files from disk (required after edits) |
| systemctl list-units --type=service | List all service units and their state |
| systemctl list-unit-files --type=service | List all service unit files and enabled/disabled state |

---

### Unit File Locations

| Path | Purpose |
|------|---------|
| /lib/systemd/system/ | Package-installed unit files (do not edit; upgrades overwrite) |
| /etc/systemd/system/ | Administrator-created and override unit files (survives upgrades) |
| /etc/systemd/system/SERVICE.d/override.conf | Drop-in override created by systemctl edit |

The correct workflow for customizing a unit file:

1. Run `sudo systemctl edit SERVICE` to create an override.conf in the .d/ directory.
2. Run `sudo systemctl daemon-reload` to reload systemd's unit file cache.
3. Run `sudo systemctl restart SERVICE` to apply the new configuration.

---

### journalctl Reference

| Command | Output |
|---------|--------|
| journalctl -u SERVICE | All journal entries for the named service |
| journalctl -u SERVICE -b | Journal entries since the last boot |
| journalctl -u SERVICE -f | Follow the log in real time (like tail -f) |
| journalctl -u SERVICE --since "TIME" | Entries since a specific time or relative expression |
| journalctl -p err -b | Error and higher priority messages this boot |
| journalctl -n N | Last N lines across all services |
| journalctl --disk-usage | Show total journal disk usage |

Priority levels for -p flag (from highest to lowest severity): emerg, alert, crit, err, warning, notice, info, debug.

---

### Zombie Process Quick Reference

A zombie (STAT=Z) is a process that has exited but whose parent has not called wait() to collect its exit status. The process entry remains in the process table.

Properties of zombies:

- They consume no CPU time and minimal memory (only the process table entry).
- SIGKILL has no effect because there is no code running to kill.
- They cannot be directly eliminated.

Resolution options:

1. Fix the parent process so it properly calls wait() on its children.
2. Restart the parent process if it is misbehaving.
3. Kill the parent process; systemd (PID 1) will adopt the zombie and reap it immediately.

A small, stable count of zombies is harmless. A growing count indicates a bug in a parent process.

---

### Load Average Interpretation

The load average (from top, uptime, or /proc/loadavg) shows three numbers: 1-minute, 5-minute, and 15-minute averages.

Interpretation rule: compare the 1-minute average to the number of CPU cores.

| Cores | Load = Normal | Load = Saturated |
|-------|--------------|-----------------|
| 1 | 1.0 or below | Above 1.0 |
| 4 | 4.0 or below | Above 4.0 |
| 8 | 8.0 or below | Above 8.0 |

A value above the core count means processes are queued waiting for CPU time. A rising trend from the 15-minute to the 1-minute average indicates increasing load.

---

### Exam Tips

1. SIGKILL (9) versus SIGTERM (15): SIGTERM is the default; it can be caught and allows cleanup. SIGKILL cannot be caught and forces immediate termination. Always try SIGTERM first.

2. daemon-reload is always required after editing a unit file. Forgetting this step is the most commonly tested mistake in the systemctl workflow.

3. systemctl enable does not start a service. systemctl start does not enable a service. Use enable --now to do both in one command.

4. A zombie process (STAT=Z) is already dead. SIGKILL does nothing. The fix is to address the parent.

5. Negative nice values require root. A regular user can only lower their process priority (increase the nice value above 0).

6. SIGSTOP (19) cannot be caught or ignored, like SIGKILL. SIGCONT (18) resumes a stopped process.

7. SIGHUP (1) is used by many daemons (Apache, nginx, sshd) as a signal to reload configuration without restarting.

8. Load average above the number of CPU cores indicates CPU saturation. Check the top I/O wait column (wa) to distinguish CPU-bound from I/O-bound load.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Explain PID, PPID, nice value, and process owner
- Decode every STAT column code in ps aux output (R, S, D, Z, T, I)
- Interpret the load average line in top output
- Send SIGTERM, SIGKILL, and SIGHUP using kill
- Explain the difference between kill, killall, and pkill
- Explain why SIGKILL cannot be used to eliminate a zombie
- Describe the correct resolution for a zombie process
- Use pgrep and pidof to find process IDs
- Start a background job with &, list jobs, bring to foreground, suspend with Ctrl+Z
- Start a new process with a custom nice value using nice
- Change the nice value of a running process using renice
- Explain who can set negative nice values
- Perform the full systemctl workflow: start, stop, restart, reload, enable, disable
- Explain the difference between systemctl reload and systemctl restart
- Explain what daemon-reload does and when it is required
- Identify the correct location for administrator unit file overrides
- Use journalctl to view service logs, filter by time, and follow in real time

---

## 9. Supplemental Resources

**1. Linux man pages — ps(1), top(1), kill(1), nice(1), renice(1)**
URL: https://man7.org/linux/man-pages/man1/ps.1.html
Coverage: The ps man page PROCESS STATE CODES section documents every STAT code (R, S, D,
Z, T, I, W, X). The kill man page lists all signal numbers and names. Essential reference
for interpreting process output and sending the correct signal.

**2. systemd documentation — systemctl(1)**
URL: https://www.freedesktop.org/software/systemd/man/systemctl.html
Coverage: Complete systemctl reference covering all subcommands including start, stop,
restart, reload, enable, disable, mask, daemon-reload, and daemon-reexec. Explains the
difference between enable/disable (boot persistence) and start/stop (runtime state).

**3. TLDP — Linux Processes HOWTO**
URL: https://tldp.org/LDP/tlk/kernel/processes.html
Coverage: Explains how the Linux kernel manages processes including scheduling, context
switching, process states, and the fork/exec model. Background reading for understanding
why zombie processes exist and how orphan adoption works.

**4. Red Hat Documentation — Managing systemd services**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/managing-system-services-with-systemctl_configuring-basic-system-settings
Coverage: RHEL 9 guide for managing services with systemctl, creating drop-in override
files, understanding unit dependencies, and using systemctl list-units to audit running
services. Covers the /etc/systemd/system/ override directory pattern.

**5. Arch Wiki — systemd/Journal**
URL: https://wiki.archlinux.org/title/Systemd/Journal
Coverage: Comprehensive journalctl reference covering all filtering options (--since,
--until, -u, -p, -b, -k, -f, -n), persistent journal configuration, journal size limits,
and forwarding journal entries to syslog. The most complete freely available journalctl
guide outside the man page.
