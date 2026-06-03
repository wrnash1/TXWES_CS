# Lab: Module 05 — Process Management and System Monitoring

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Lab Overview

**Estimated Time:** 60–75 minutes

**Environment:** Linux VM (Ubuntu 22.04 LTS or equivalent); sudo required for Parts 3 and 5

**Purpose:** Practice process inspection, signal delivery, priority management, resource monitoring, and cron job scheduling in a controlled lab environment.

---

## Objectives

By the end of this lab you will be able to:

- Identify running processes and their states using ps and top
- Send signals to processes using kill, killall, and pkill
- Manage process priority with nice and renice
- Run background jobs and persist them across logout with nohup
- Read system resource metrics from uptime, free, vmstat, and df
- Query /proc for process and system information
- Schedule a recurring task with crontab

---

## Pre-Lab Setup

No setup script is required. All tools used in this lab are part of the standard Linux installation.

Verify the tools are available:

```bash
which ps top kill nice renice vmstat iostat free df du lsof crontab
```

If `iostat` is missing, install it:

```bash
sudo apt install sysstat   # Ubuntu/Debian
sudo yum install sysstat   # RHEL/CentOS
```

---

## Part 1 — Process Inspection with ps (15 minutes)

### Task 1.1 — Basic ps Output

```bash
# Show all processes in BSD format
ps aux

# Count total processes
ps aux | wc -l

# Show all processes in SysV format
ps -ef | head -20
```

Record: How many total processes are running on your system?

### Task 1.2 — Filtering and Sorting

```bash
# Find the sshd process
ps aux | grep sshd

# Find your shell process
ps aux | grep bash

# Top 5 processes by CPU usage
ps aux --sort=-%cpu | head -6

# Top 5 processes by memory usage
ps aux --sort=-%mem | head -6
```

**Question:** In the `ps aux` output, what does the STAT column `Ss` mean? (Refer to the reading guide.)

### Task 1.3 — Process Tree

```bash
# View process hierarchy
ps --forest -eo pid,ppid,user,cmd | head -40
```

Identify your bash shell in the output. What is its PID and PPID? What is the parent process?

### Task 1.4 — Custom Column Selection

```bash
# Show only PID, PPID, nice value, state, and command
ps -eo pid,ppid,ni,stat,cmd | head -20
```

Examine the NI column. Most processes show 0. Are any showing non-zero nice values?

---

## Part 2 — Process Control with Signals (15 minutes)

### Task 2.1 — Start a Test Process

```bash
# Start a long-running background process
sleep 600 &

# Note the PID printed by the shell
# Verify it is running
ps aux | grep "sleep 600" | grep -v grep
```

Record the PID of the sleep process.

### Task 2.2 — SIGTERM (Graceful Termination)

```bash
# Send SIGTERM (default)
kill YOUR_PID_HERE

# Verify it is gone
ps aux | grep "sleep 600" | grep -v grep
```

**Expected result:** The process is no longer listed.

### Task 2.3 — SIGKILL (Forced Termination)

```bash
# Start another sleep process
sleep 600 &

# This time, force-kill it
kill -9 YOUR_NEW_PID

# Verify
ps aux | grep "sleep 600" | grep -v grep
```

### Task 2.4 — killall and pkill

```bash
# Start three sleep processes simultaneously
sleep 600 & sleep 600 & sleep 600 &

# Verify three are running
ps aux | grep "sleep 600" | grep -v grep

# Kill all processes named "sleep"
killall sleep

# Verify all are gone
ps aux | grep "sleep 600" | grep -v grep
```

### Task 2.5 — Using pgrep

```bash
# Start a sleep process
sleep 600 &

# Find its PID using pgrep (no grep | awk needed)
pgrep sleep

# Kill using pgrep in command substitution
kill $(pgrep sleep)
```

**Question:** What is the advantage of `pgrep` over `ps aux | grep | awk '{ print $2 }'`?

### Task 2.6 — SIGHUP Demonstration

```bash
# View what SIGHUP signal number is
kill -l | grep HUP

# List all available signal names and numbers
kill -l
```

Record: What number is SIGHUP? What number is SIGSTOP?

---

## Part 3 — Priority Management (10 minutes)

### Task 3.1 — Starting a Process with nice

```bash
# Start a process at nice value 10 (lower priority)
nice -n 10 sleep 300 &

# Verify the nice value appears in ps output
ps -eo pid,ni,cmd | grep "sleep 300" | grep -v grep
```

The NI column should show 10.

### Task 3.2 — renice a Running Process

```bash
# Start a default-priority sleep process
sleep 300 &
PID=$!
echo "PID is: $PID"

# Check current nice value
ps -p $PID -o pid,ni,cmd

# Renice to 15
renice 15 -p $PID

# Verify the change
ps -p $PID -o pid,ni,cmd
```

### Task 3.3 — Attempting a Negative Nice (Requires sudo)

```bash
# As a regular user, attempt nice -n -5 (expect failure)
nice -n -5 sleep 30 &

# As root/sudo, this would work:
sudo nice -n -5 sleep 30 &
ps -eo pid,ni,cmd | grep "sleep 30" | grep -v grep

# Clean up
killall sleep
```

**Question:** Why can regular users only increase their nice value (toward +19) but not decrease it below 0?

---

## Part 4 — Background Jobs and nohup (10 minutes)

### Task 4.1 — Job Control

```bash
# Start a sleep process in the foreground
sleep 120

# While it runs, press Control+Z to suspend it
# You should see: [1]+  Stopped    sleep 120

# List background jobs
jobs

# Resume it in the background
bg %1

# Check jobs again
jobs

# Bring it back to foreground
fg %1

# While running, press Control+C to terminate it
```

### Task 4.2 — nohup

```bash
# Create a simple long-running script
cat > /tmp/long_task.sh << 'EOF'
#!/bin/bash
for i in $(seq 1 30); do
    echo "$(date): Iteration $i" >> /tmp/long_task.log
    sleep 5
done
EOF
chmod +x /tmp/long_task.sh

# Run with nohup
nohup /tmp/long_task.sh &

# Note the PID
echo "PID: $!"

# Check the output file
sleep 3
cat /tmp/long_task.log

# Kill when done
kill $(pgrep -f long_task.sh)
```

---

## Part 5 — Resource Monitoring (10 minutes)

### Task 5.1 — uptime and Load

```bash
uptime
cat /proc/loadavg
```

Record the three load average values. How many CPU cores does your system have?

```bash
nproc
cat /proc/cpuinfo | grep "processor" | wc -l
```

Is the load average healthy for your core count?

### Task 5.2 — Memory

```bash
free -h
cat /proc/meminfo | head -15
```

Record:

- Total RAM
- Available RAM
- Swap total and used

### Task 5.3 — vmstat

```bash
vmstat 2 5
```

Observe all 5 rows of output. Record the values for:

- `r` (runnable processes) — should be low unless CPU-saturated
- `wa` (I/O wait) — sustained >10% is worth investigating
- `si`/`so` (swap in/out) — should be 0 on a healthy system

### Task 5.4 — Disk

```bash
df -h
du -sh /var/log
du --max-depth=1 /var | sort -hr | head -10
```

Which filesystem has the highest usage percentage?

### Task 5.5 — /proc Exploration

```bash
# CPU model
grep "model name" /proc/cpuinfo | head -1

# Memory breakdown
cat /proc/meminfo | grep -E "^Mem|^Swap|Cached"

# Your shell's open file count
ls /proc/$$/fd | wc -l

# Your shell's command line
cat /proc/$$/cmdline; echo

# System uptime in seconds
cat /proc/uptime
```

---

## Part 6 — Cron Scheduling (10 minutes)

### Task 6.1 — Create a Monitoring Script

```bash
cat > ~/check_disk.sh << 'EOF'
#!/bin/bash
THRESHOLD=80
USAGE=$(df / | awk 'NR==2 { print $5 }' | tr -d '%')
if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "$(date): WARNING: Root filesystem at ${USAGE}%" >> ~/disk_alerts.log
else
    echo "$(date): OK: Root filesystem at ${USAGE}%" >> ~/disk_alerts.log
fi
EOF
chmod +x ~/check_disk.sh

# Test it manually
~/check_disk.sh
cat ~/disk_alerts.log
```

### Task 6.2 — Add to Crontab

```bash
crontab -e
```

Add the following entries (use your preferred editor, which opens automatically):

```
# Run disk check every 5 minutes
*/5 * * * * /home/YOUR_USERNAME/check_disk.sh

# Run a cleanup every Sunday at 3 AM
0 3 * * 0 find /tmp -type f -mtime +7 -delete
```

Save and exit the editor.

### Task 6.3 — Verify and Manage Crontab

```bash
# List your crontab
crontab -l

# Wait 5+ minutes, then check if the log was updated
cat ~/disk_alerts.log
```

### Task 6.4 — at Scheduling

```bash
# Schedule a one-time command 2 minutes from now
echo "echo 'at job ran at: \$(date)' >> ~/at_test.log" | at now + 2 minutes

# List scheduled at jobs
atq

# Wait 2+ minutes, then check the log
cat ~/at_test.log
```

---

## Challenge Tasks (Optional)

### Challenge 1 — Process Monitor Script

Write a shell script that:

1. Captures the top 5 CPU-consuming processes with ps
2. Captures current memory usage with free
3. Writes both to `~/system_snapshot.txt` with a timestamp header
4. Can be scheduled via cron

### Challenge 2 — Zombie Hunting

Research how to identify zombie processes in ps output. Write a command using ps and grep that shows any zombie processes on the current system. If there are none, write a brief explanation of what conditions create a zombie process and how to resolve it.

### Challenge 3 — Load Average Analysis

Run `vmstat 1 60` (60 samples, 1-second interval) while running a CPU-intensive task in another terminal (`dd if=/dev/zero of=/dev/null bs=1M count=10000`). Observe how the `r` column and `us` column change. Document your findings.

---

## Submission Requirements

Submit a text file named `lab05_answers.txt` containing:

1. Total process count from Task 1.1
2. PID and PPID of your bash shell from Task 1.3
3. Answer to Task 1.2 question about STAT codes
4. Signal numbers for SIGHUP and SIGSTOP from Task 2.6
5. Answer to Task 2.5 question about pgrep
6. Answer to Task 3.3 question about nice security
7. Load average values and CPU count from Task 5.1 with your analysis
8. Crontab listing output from Task 6.3

---

## Grading Rubric

| Section | Points |
|---|---|
| Part 1 — ps inspection and questions | 15 |
| Part 2 — signal delivery | 20 |
| Part 3 — nice and renice | 15 |
| Part 4 — background jobs and nohup | 15 |
| Part 5 — resource monitoring | 20 |
| Part 6 — cron scheduling | 15 |
| **Total** | **100** |

Challenge tasks are extra credit (up to 15 points).

---

*End of Module 05 Lab*
