# Reading Guide: Module 05 — Process Management and System Monitoring

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide supports Module 05. Process management is the skill set that separates a reactive sysadmin from a proactive one. Understanding process states, signals, and scheduling — combined with the ability to read resource metrics — allows you to prevent problems and respond effectively when systems degrade.

---

## Section 1 — Process Fundamentals

### 1.1 Process Identity

Every process in Linux is identified by:

- **PID** (Process ID) — unique integer assigned at creation; recycled after process exits
- **PPID** (Parent Process ID) — the PID that created this process via fork()
- **UID/GID** — user and group context under which the process runs
- **Session ID** — group of related processes from the same login session

PID 1 (systemd on modern systems) is the ancestor of all user-space processes. When a process's parent dies before it does, the orphaned process is re-parented to PID 1.

### 1.2 Process States

| Code | Name | Description |
|---|---|---|
| R | Running | On CPU or waiting in the run queue |
| S | Sleeping | Waiting for an event; can be interrupted by a signal |
| D | Uninterruptible Sleep | Waiting for I/O; cannot be killed by normal signals |
| Z | Zombie | Exited but not yet reaped by parent |
| T | Stopped | Suspended; typically via SIGSTOP or Control+Z |
| I | Idle (Linux 4.14+) | Kernel idle thread |

### 1.3 Fork and Exec

When a shell runs a command, it uses two system calls:

1. **fork()** — creates a copy of the current process (the child has the same memory, file descriptors, environment)
2. **exec()** — replaces the child's program with the requested command

This fork-exec model is why every command inherits the environment of its parent shell and why PID relationships form a tree.

---

## Section 2 — Inspecting Processes

### 2.1 ps Reference

```bash
ps aux                          # BSD: all processes, user-oriented format
ps -ef                          # SysV: all processes, full format
ps -eo pid,ppid,user,cmd        # Custom column selection
ps aux --sort=-%cpu | head -10  # Top CPU consumers
ps aux --sort=-%mem | head -10  # Top memory consumers
ps --forest -eo pid,ppid,cmd    # Process tree
```

### ps aux Column Meanings

| Column | Meaning |
|---|---|
| USER | Process owner |
| PID | Process ID |
| %CPU | CPU usage percentage |
| %MEM | Physical memory percentage |
| VSZ | Virtual memory size (KB) |
| RSS | Resident set size — physical RAM in use (KB) |
| STAT | Process state (see table above, plus flags) |
| START | Time/date process started |
| TIME | Cumulative CPU time |
| COMMAND | Command name and arguments |

### STAT Flag Letters

| Letter | Meaning |
|---|---|
| `s` | Session leader |
| `l` | Multi-threaded |
| `+` | In foreground process group |
| `N` | Low-priority (nice > 0) |
| `<` | High-priority (nice < 0) |

### 2.2 top Interactive Reference

| Key | Action |
|---|---|
| `k` | Kill a process (prompts for PID and signal) |
| `r` | Renice a process (prompts for PID and nice value) |
| `M` | Sort by memory usage |
| `P` | Sort by CPU usage |
| `1` | Toggle per-CPU display |
| `q` | Quit |
| `h` | Help |
| `z` | Color display toggle |

---

## Section 3 — Signals

### 3.1 Common Signals

| Signal | Number | Default Action | Description |
|---|---|---|---|
| SIGHUP | 1 | Terminate | Terminal hangup; daemons use it to reload config |
| SIGINT | 2 | Terminate | Interrupt from keyboard (Control+C) |
| SIGQUIT | 3 | Core dump | Quit from keyboard (Control+\\) |
| SIGKILL | 9 | Terminate (forced) | Cannot be caught or ignored |
| SIGTERM | 15 | Terminate | Graceful termination request (default for kill) |
| SIGSTOP | 19 | Stop | Cannot be caught; suspend process |
| SIGCONT | 18 | Continue | Resume a stopped process |
| SIGUSR1/2 | 10/12 | User-defined | Application-specific handling |

### 3.2 Sending Signals

```bash
kill PID                # SIGTERM (15)
kill -9 PID             # SIGKILL
kill -SIGKILL PID       # Same as above
kill -HUP PID           # SIGHUP (1) — reload config
kill -l                 # List all signal names and numbers

killall process_name    # Kill all processes with this name
pkill pattern           # Kill by name pattern
pkill -f "full cmdline" # Match against full command line
pgrep pattern           # Print PIDs matching name
```

---

## Section 4 — Priority Management

### 4.1 Nice Values

The nice value is an integer from -20 (highest priority) to +19 (lowest priority). Default is 0.

- Only root can set negative nice values
- Users can only increase (lower priority) their own processes
- Lower nice = higher priority = more CPU time

```bash
nice -n 10 command           # Start at nice 10
renice 15 -p PID             # Change PID's nice to 15
renice 5 -u username         # Change all processes of user
```

### 4.2 Real-Time Priorities

Beyond nice values, Linux supports real-time scheduling classes for time-critical tasks. The `chrt` command manages real-time priority — this is beyond Linux+ scope but worth knowing exists.

---

## Section 5 — Background Jobs

### 5.1 Job Control

| Command | Action |
|---|---|
| `command &` | Start in background |
| `Control+Z` | Suspend foreground process |
| `jobs` | List background jobs |
| `fg %N` | Bring job N to foreground |
| `bg %N` | Resume stopped job N in background |
| `disown %N` | Remove job from shell's job table (survives logout) |

### 5.2 nohup

```bash
nohup command &                           # Output goes to nohup.out
nohup command > /path/to/log 2>&1 &      # Redirect to custom log
```

nohup makes the process immune to SIGHUP. Combined with `&`, the process continues after the terminal session ends.

---

## Section 6 — System Resource Monitoring

### 6.1 uptime and Load Average

```bash
uptime
# Output: up 5 days, 3:14, 2 users, load average: 0.45, 0.62, 0.78
```

Load average represents the average number of processes in the run queue (running + waiting for CPU + in D state) over the past 1, 5, and 15 minutes.

**Rule of thumb:** For a system with N CPU cores, a healthy load average stays below N. A load average above N × 2 sustained over 15 minutes warrants investigation.

### 6.2 Memory

```bash
free -h       # Human-readable memory and swap
```

Key row — "available": the actual free + reclaimable memory. Do not confuse "free" (truly unused) with "available" (what applications can actually get). Linux aggressively uses free RAM as file cache; this is normal and healthy.

### 6.3 vmstat

```bash
vmstat 2 5    # 5 samples, 2-second interval
```

| Column | Meaning |
|---|---|
| `r` | Processes in run queue |
| `b` | Processes in uninterruptible sleep |
| `si` / `so` | Pages swapped in/out per second |
| `bi` / `bo` | Blocks in/out from block devices per second |
| `wa` | CPU time waiting for I/O |
| `id` | CPU idle percentage |

### 6.4 iostat

```bash
iostat -x 2 3
```

| Column | Meaning |
|---|---|
| `r/s` / `w/s` | Reads/writes per second |
| `await` | Average I/O wait time (ms) |
| `%util` | Device utilization (100% = saturated) |

### 6.5 Disk Space

```bash
df -h                           # All filesystems
df -h /var                      # Specific mount point
du -sh /var/log                 # Total for directory
du --max-depth=1 /var           # Breakdown by subdirectory
du --max-depth=1 /var | sort -hr | head -10  # Largest first
```

### 6.6 lsof

```bash
lsof -p PID          # Files open by a process
lsof -u username     # Files open by a user
lsof -i              # All network connections
lsof -i :80          # Processes using port 80
lsof /path/to/file   # Which processes have this file open
```

---

## Section 7 — The /proc Filesystem

`/proc` is a virtual filesystem — not on disk. The kernel populates it dynamically.

| Path | Contents |
|---|---|
| `/proc/cpuinfo` | CPU model, cores, features |
| `/proc/meminfo` | Detailed memory statistics |
| `/proc/loadavg` | Load averages and task counts |
| `/proc/uptime` | Seconds since boot and idle time |
| `/proc/mounts` | Currently mounted filesystems |
| `/proc/PID/` | Per-process directory |
| `/proc/PID/cmdline` | Full command line (null-separated) |
| `/proc/PID/status` | Human-readable process status |
| `/proc/PID/fd/` | Symbolic links to open file descriptors |
| `/proc/PID/maps` | Memory mapping |

---

## Section 8 — Scheduled Tasks

### 8.1 crontab Syntax

```
MIN  HOUR  DAY  MONTH  DOW  COMMAND
```

Special strings:

| String | Meaning |
|---|---|
| `@reboot` | Run once at startup |
| `@daily` | Once per day (midnight) |
| `@weekly` | Once per week (Sunday midnight) |
| `@monthly` | Once per month (first day midnight) |

Field wildcards and ranges:

- `*` — every value
- `*/5` — every 5th value (e.g., every 5 minutes)
- `1,3,5` — specific values
- `1-5` — range

### 8.2 crontab Commands

```bash
crontab -e    # Edit (opens $EDITOR)
crontab -l    # List
crontab -r    # Remove ALL cron jobs (dangerous!)
```

### 8.3 System Cron Directories

| Path | Purpose |
|---|---|
| `/etc/crontab` | System crontab (includes user field) |
| `/etc/cron.d/` | Drop-in crontab files |
| `/etc/cron.daily/` | Scripts run daily |
| `/etc/cron.weekly/` | Scripts run weekly |
| `/etc/cron.monthly/` | Scripts run monthly |
| `/etc/cron.hourly/` | Scripts run hourly |

### 8.4 at: One-Time Scheduling

```bash
at 15:30                    # Opens interactive prompt
at 15:30 tomorrow
at now + 2 hours
echo "command" | at 23:00   # Non-interactive
atq                         # List pending jobs
atrm JOB_NUMBER             # Remove a job
```

---

## CompTIA Linux+ Exam Relevance

- **2.6** — Given a scenario, manage processes and services
- **4.2** — Given a scenario, write and execute basic shell scripts

Expect exam questions on:

- Process state codes (R, S, D, Z, T)
- The difference between SIGTERM and SIGKILL
- How to find processes consuming the most CPU or memory
- Nice value range and who can set negative values
- crontab field order (minute, hour, day, month, dow)
- What `/proc` is and how to access process information from it

---

## Key Terms

- **PID** — Process ID; unique integer identifying a running process
- **Signal** — integer sent to a process to request a state change or action
- **SIGKILL** — signal 9; cannot be caught or ignored; kernel enforces immediately
- **SIGTERM** — signal 15; graceful termination request; process can handle cleanup
- **SIGHUP** — signal 1; traditionally hang-up; used by daemons as a config-reload trigger
- **nice value** — CPU scheduling bias; -20 (highest priority) to +19 (lowest priority)
- **Load average** — rolling average of processes in run or uninterruptible wait state
- **cron** — daemon that executes scheduled commands based on time-based rules
- **nohup** — wrapper that makes a process immune to SIGHUP
- **/proc** — virtual kernel filesystem exposing system and process state as files

---

---

## 9. Supplemental Resources

**1. [man7.org — proc(5) Virtual Filesystem](https://man7.org/linux/man-pages/man5/proc.5.html)**
The complete reference for the Linux `/proc` virtual filesystem. Documents every `/proc/PID/` subdirectory and key system-wide files (`/proc/loadavg`, `/proc/meminfo`, `/proc/cpuinfo`). Essential when troubleshooting process behavior directly from kernel-exposed data without relying on higher-level tools.

**2. [Red Hat — Understanding Linux Process States](https://www.redhat.com/sysadmin/linux-process-states)**
A practical Red Hat sysadmin article covering all process state codes with real-world diagnostic scenarios. Includes guidance on interpreting large numbers of `D`-state processes (I/O wait) and zombie processes, and the commands used to investigate each.

**3. [Crontab Guru — Interactive Cron Expression Editor](https://crontab.guru/)**
An interactive web tool that parses and explains crontab expressions in plain English. Invaluable for verifying complex cron expressions before deploying them. Also includes a list of common cron schedule patterns and the special `@reboot`, `@daily`, and `@weekly` shorthand strings.

---

*End of Module 05 Reading Guide*
