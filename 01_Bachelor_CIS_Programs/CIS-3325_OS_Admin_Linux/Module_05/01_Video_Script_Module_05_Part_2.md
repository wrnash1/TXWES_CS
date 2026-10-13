# Video Script: Module 05 — Process Management and System Monitoring (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Production Notes

- **Screen recording**: Terminal emulator (dark theme, 18pt font)
- **Demonstrations**: Run actual monitoring commands; show /proc virtual filesystem contents
- **Slide overlays**: nice value scale shown as graphic; cron syntax table shown as reference
- **Pacing**: Allow vmstat/iostat output to scroll several lines before explaining

---

## SEGMENT 1 — Opening and Recap (0:00–1:00)

### Narration

Welcome back to Module 05, Part 2. In Part 1 we covered process fundamentals — PIDs, states, ps, top, and signals. Now we go deeper: priority management, background jobs, resource monitoring, the /proc filesystem, and scheduled tasks with cron and at. By the end of this part you will have a complete picture of how to keep systems running smoothly and predictably.

---

## SEGMENT 2 — Priority: nice and renice (1:00–3:30)

### Narration

Not all processes deserve equal CPU time. Linux uses a priority system called "niceness" to adjust how much CPU a process receives relative to others.

The nice value ranges from -20 to +19. Lower numbers mean higher priority — the process gets more CPU. Higher numbers mean lower priority — the process yields CPU to others. The name comes from the idea that a process with a high nice value is being "nice" to other processes.

Regular users can only set nice values from 0 to +19 — they can make their processes lower priority but cannot elevate them above the default. Root can use negative values to increase priority.

To start a process with a non-default nice value:

### On-Screen Demo

```bash
# Start a CPU-intensive backup at low priority (nice 10)
nice -n 10 tar czf /backup/home.tar.gz /home/
```

### Narration

To change the nice value of an already-running process, use renice:

### On-Screen Demo

```bash
# Find the PID of a running process
ps aux | grep tar

# Renice it to priority 15 (very low)
renice 15 -p PID_HERE

# Renice a process owned by a specific user
renice 5 -u username
```

### Narration

You can also set priority interactively in top with the `r` key — top will prompt for PID and new value.

A practical rule of thumb: run long-running background tasks like backups and data migrations at nice 10 to 19 so they do not impact foreground user-facing services.

---

## SEGMENT 3 — Background Jobs: nohup, &, jobs, fg, bg (3:30–6:30)

### Narration

When you run a command at the shell prompt, it runs in the foreground — your terminal is blocked until it finishes. For long-running tasks, you have several options.

The ampersand `&` at the end of a command sends it to the background immediately:

### On-Screen Demo

```bash
sleep 120 &
```

### Narration

The shell prints `[1] 12345` — the job number in brackets and the PID. The process is now running in the background. You can continue using the terminal.

However, if you close the terminal or log out, background jobs receive SIGHUP and terminate. To prevent this, use `nohup`:

### On-Screen Demo

```bash
nohup ./long_backup.sh > /tmp/backup.log 2>&1 &
```

### Narration

nohup ignores SIGHUP, keeping the process running after logout. The output that would go to the terminal is redirected — here to a log file. The `2>&1` redirects stderr to the same place as stdout.

To see all background jobs in the current shell:

### On-Screen Demo

```bash
jobs
```

### Narration

The output shows job numbers, state (Running/Stopped), and the command. To bring a background job to the foreground:

### On-Screen Demo

```bash
fg %1
```

### Narration

The `%1` refers to job 1. To suspend the foreground process (send it to background as Stopped): press **Control+Z**. Then use `bg %1` to resume it in the background:

### On-Screen Demo

*Start sleep 300, press Control+Z, run bg %1*

```bash
bg %1
jobs
```

### Narration

This Control+Z → bg pattern is very useful when you start something in the foreground and realize it will take longer than expected.

---

## SEGMENT 4 — Resource Monitoring Tools (6:30–10:30)

### Narration

Beyond tracking individual processes, a sysadmin needs to monitor overall system resources. Let's walk through the essential tools.

### uptime and load averages

### On-Screen Demo

```bash
uptime
```

### Narration

The output shows how long the system has been running and the load averages for the past 1, 5, and 15 minutes. Load average represents the average number of processes that are either running or waiting to run. On a single-core system, a load average of 1.0 means the CPU is fully utilized. On a quad-core system, 4.0 is 100% utilization. A sustained load average significantly above your CPU count indicates saturation.

### free: Memory Usage

### On-Screen Demo

```bash
free -h
```

### Narration

`-h` gives human-readable output. The `total`, `used`, and `available` columns are the most important. The `buff/cache` line shows memory used for disk caching — Linux intentionally uses free RAM as disk cache. This memory is released when applications need it. The `available` column shows how much is actually available for new processes.

### vmstat: Virtual Memory Statistics

### On-Screen Demo

```bash
vmstat 2 5
```

### Narration

`vmstat 2 5` takes 5 samples at 2-second intervals. The columns of interest: `r` is runnable processes (high = CPU contention), `b` is blocked processes (high = I/O bottleneck), `si`/`so` are swap in/out (if these are non-zero, you are swapping — a sign of memory pressure), `us`/`sy`/`id`/`wa` are CPU states — `wa` (wait) being high indicates I/O saturation.

### iostat: Disk I/O Statistics

### On-Screen Demo

```bash
iostat -x 2 3
```

### Narration

`-x` shows extended statistics. The key columns per device: `%util` shows how saturated the device is — approaching 100% means the disk cannot keep up. `await` is average I/O wait time in milliseconds. Over 20ms for a spinning disk or over 2ms for an SSD can indicate problems.

### df and du: Disk Space

### On-Screen Demo

```bash
df -h
df -h /var
du -sh /var/log
du --max-depth=1 /var
```

### Narration

`df -h` shows filesystem usage across all mounted filesystems. `du -sh` shows the total disk usage of a directory. `du --max-depth=1` breaks it down one level deep, letting you identify which subdirectory is consuming space.

### lsof: Open Files

### On-Screen Demo

```bash
# Show all files opened by a specific process
lsof -p 1234

# Show all processes listening on network sockets
lsof -i

# Show processes using a specific port
lsof -i :22
```

### Narration

lsof — list open files — is invaluable for security auditing, diagnosing port conflicts, and understanding what a process is doing with the filesystem and network.

---

## SEGMENT 5 — The /proc Filesystem (10:30–12:00)

### Narration

The `/proc` directory is not a real filesystem — it is a virtual interface the kernel uses to expose system and process information as files. Reading these files reads kernel memory directly.

### On-Screen Demo

```bash
# CPU information
cat /proc/cpuinfo | grep "model name" | head -2

# Memory information
cat /proc/meminfo | head -10

# System load averages (same as uptime)
cat /proc/loadavg

# List of running processes (each number is a PID)
ls /proc | grep -E '^[0-9]+$' | head -10

# Command line of process 1 (systemd)
cat /proc/1/cmdline; echo
```

### Narration

For any PID, `/proc/PID/` contains a directory with files describing that process — its open file descriptors, memory maps, environment variables, and more. This is where monitoring tools read their data. Understanding /proc lets you retrieve information that no user-space tool exposes.

---

## SEGMENT 6 — Scheduled Tasks: cron and at (12:00–15:00)

### Narration

Most systems need tasks to run on a schedule — log rotation, backups, security scans. Linux provides two scheduling mechanisms: cron for recurring tasks and at for one-time future tasks.

### cron

Each user has a crontab file edited with `crontab -e`. The format has five time fields followed by the command:

### Slide Overlay: Crontab Syntax

```
MIN  HOUR  DAY  MONTH  DOW  COMMAND
 *    *     *     *     *   command
```

- MIN: 0–59
- HOUR: 0–23
- DAY: 1–31
- MONTH: 1–12
- DOW: 0–6 (Sunday=0)
- `*` means "every value"

### On-Screen Demo

```bash
# Edit the current user's crontab
crontab -e

# Add these example entries:
# Run backup every day at 2:30 AM
# 30 2 * * * /usr/local/bin/backup.sh

# Run a script every 15 minutes
# */15 * * * * /usr/local/bin/check_disk.sh

# Run every Monday at 6 AM
# 0 6 * * 1 /usr/local/bin/weekly_report.sh
```

### Narration

System-wide crontabs live in `/etc/cron.d/` and `/etc/cron.daily/`, `/etc/cron.weekly/`, etc. Scripts placed in the weekly or daily directories run automatically at the scheduled time without needing a crontab entry.

To list your crontab: `crontab -l`. To remove all your cron jobs: `crontab -r` — be careful, `-r` not `-e`.

### at: One-Time Scheduling

### On-Screen Demo

```bash
# Run a command at 3:00 PM today
echo "/usr/local/bin/deploy.sh" | at 15:00

# Run tomorrow at noon
echo "systemctl restart apache2" | at noon tomorrow

# List scheduled at jobs
atq

# Remove job number 3
atrm 3
```

### Narration

at is perfect for one-time delayed actions — deploying during a maintenance window, restarting a service after an off-hours change, or sending a notification at a specific time.

The cron and at tools, combined with the monitoring commands we covered, give you a complete operational toolkit. You can observe system state in real time, identify problems before they become outages, and schedule corrective actions automatically.

That completes Module 05. In Module 06 we move to storage — partitioning, formatting, mounting, LVM, and disk health monitoring. See you there.

---

## Summary Slide

### Part 2 Key Concepts

- `nice -n 10 cmd` — start at reduced priority; `renice 15 -p PID` — change running process
- `nohup cmd &` — run in background, survive logout
- `jobs` — list background jobs; `fg %1` bring to foreground; `bg %1` resume in background
- `uptime` — load averages (1/5/15 min); `free -h` — memory; `vmstat 2 5` — CPU/memory/swap trends
- `iostat -x` — disk I/O saturation; `df -h` — filesystem usage; `du -sh dir` — directory size
- `lsof -i :PORT` — which process owns a port
- `/proc/cpuinfo`, `/proc/meminfo`, `/proc/loadavg` — kernel data files
- `crontab -e` — edit scheduled jobs; `at TIME` — schedule one-time task

---

*End of Module 05 Part 2 Script*
