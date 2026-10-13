# Lab 06: Process Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will inspect running processes using ps, top, and pgrep, manipulate process priority with nice and renice, control background and foreground jobs, send signals with kill, manage systemd services with systemctl, and inspect service logs with journalctl.

**What you will practice:**

- ps aux output decoding and process state interpretation
- pgrep and pidof for locating processes by name
- nice and renice for process priority management
- kill signals: SIGTERM, SIGKILL, and SIGHUP
- Background and foreground job control
- systemctl start, stop, restart, reload, enable, disable, and daemon-reload
- journalctl service log filtering

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running and has internet access
- You are logged in as labadmin
- You have watched both parts of the Module 06 video lecture
- You have read the Module 06 Reading Guide

---

### Part 1 - Process Inspection

**Step 1.1 - View all processes**

```bash
ps aux | head -20
```

Record the column headers. Identify: USER, PID, %CPU, %MEM, STAT, COMMAND.

```bash
ps aux | wc -l
```

This counts all process lines. The result shows approximately how many processes are running on the system.

**Step 1.2 - Identify STAT codes**

```bash
ps aux | awk '{print $8}' | sort | uniq -c | sort -rn
```

This extracts just the STAT column, counts occurrences, and shows the most common states. Record which states are present.

**Step 1.3 - Check your shell PID**

```bash
echo $$
ps -p $$
```

The first command prints your shell's PID. The second shows details about that specific process.

**Step 1.4 - Show parent-child relationships**

```bash
ps -ef | head -20
```

The ps -ef format includes the PPID column. Identify the PPID of your shell process and verify it matches sshd or your terminal emulator.

**Step 1.5 - Find specific processes**

```bash
pgrep -l sshd
```

Lists PIDs of all sshd processes with their names.

```bash
pidof sshd
```

Returns the PIDs of running sshd processes.

```bash
pgrep -u labadmin
```

Lists all PIDs belonging to the labadmin user.

**Step 1.6 - Interactive process monitoring**

```bash
top
```

In top, press the following keys and note what changes:
- 1 (toggle per-CPU display)
- M (sort by memory)
- P (sort by CPU, the default)
- q (quit)

Read the load average line. Note the three numbers and the number of CPUs.

---

### Part 2 - Process Priority

**Step 2.1 - Check the default nice value**

```bash
sleep 300 &
ps aux | grep sleep
```

The NI column shows the nice value. The default is 0.

```bash
kill %1
```

This kills the background job number 1 (the sleep command).

**Step 2.2 - Start a process with a custom nice value**

```bash
nice -n 15 sleep 300 &
ps aux | grep sleep
```

The NI column should show 15 for this sleep process.

```bash
jobs
```

Confirm the background job is listed.

**Step 2.3 - Change the nice value of a running process**

```bash
SLEEP_PID=$(pgrep sleep)
echo "Sleep PID is $SLEEP_PID"
renice -n 10 -p $SLEEP_PID
ps -p $SLEEP_PID -o pid,ni,cmd
```

The NI column should now show 10.

**Step 2.4 - Attempt to set a negative nice value as a regular user**

```bash
renice -n -5 -p $SLEEP_PID
```

Expected output: Permission denied. Regular users cannot set negative nice values.

```bash
sudo renice -n -5 -p $SLEEP_PID
ps -p $SLEEP_PID -o pid,ni,cmd
```

With sudo, the nice value changes to -5 (higher priority).

**Step 2.5 - Clean up**

```bash
kill %1
jobs
```

---

### Part 3 - Signals and Process Termination

**Step 3.1 - List all signals**

```bash
kill -l
```

Record the numbers for SIGHUP, SIGINT, SIGKILL, SIGTERM, SIGSTOP, and SIGCONT.

**Step 3.2 - Send SIGTERM**

```bash
sleep 600 &
SLEEP_PID=$!
echo "Started sleep with PID $SLEEP_PID"
kill $SLEEP_PID
sleep 1
ps -p $SLEEP_PID
```

The kill command with no signal flag sends SIGTERM. After a moment, the process is gone and ps -p returns no output.

**Step 3.3 - Demonstrate SIGKILL**

```bash
sleep 600 &
SLEEP_PID=$!
kill -9 $SLEEP_PID
ps -p $SLEEP_PID
```

SIGKILL forces immediate termination. The process cannot catch it.

**Step 3.4 - Send SIGHUP to reload configuration**

```bash
sudo systemctl status ssh
sudo kill -1 $(pidof sshd | awk '{print $1}')
sudo systemctl status ssh
```

SIGHUP sent to sshd triggers a configuration reload. The service remains running.

**Step 3.5 - Job control**

```bash
sleep 300 &
sleep 300 &
jobs
```

Two background jobs are now running.

```bash
fg 1
```

Job 1 comes to the foreground. Now press Ctrl+Z to suspend it.

```bash
jobs
```

Job 1 shows as Stopped. Job 2 is still Running.

```bash
bg 1
jobs
```

Job 1 resumes running in the background.

```bash
kill %1 %2
jobs
```

Both jobs are terminated.

---

### Part 4 - systemctl Service Management

**Step 4.1 - List running services**

```bash
systemctl list-units --type=service --state=running
```

Record how many services are actively running.

```bash
systemctl list-unit-files --type=service | grep enabled | head -10
```

Shows the first ten services that are enabled at boot.

**Step 4.2 - Inspect a service**

```bash
systemctl status ssh
```

Note the following fields: Active, Main PID, CGroup, and the last log lines.

**Step 4.3 - Stop and start a service**

```bash
sudo systemctl stop ssh
systemctl status ssh
```

The status should show inactive (dead).

```bash
sudo systemctl start ssh
systemctl status ssh
```

The status should show active (running).

**Step 4.4 - Restart a service**

```bash
sudo systemctl restart ssh
systemctl status ssh
```

Note that the start time is now the current time.

**Step 4.5 - Check enabled state**

```bash
systemctl is-enabled ssh
```

Expected output: enabled

```bash
systemctl is-active ssh
```

Expected output: active

**Step 4.6 - Disable and re-enable a service**

```bash
sudo systemctl disable ssh
systemctl is-enabled ssh
```

Expected output: disabled. The service is still running; it just will not start at next boot.

```bash
sudo systemctl enable ssh
systemctl is-enabled ssh
```

Expected output: enabled.

---

### Part 5 - Unit File Editing and daemon-reload

**Step 5.1 - View the installed unit file**

```bash
cat /lib/systemd/system/ssh.service
```

Note the [Unit], [Service], and [Install] sections.

**Step 5.2 - Create an override**

```bash
sudo systemctl edit ssh
```

This opens an editor. Add the following lines between the comment markers and save:

```
[Service]
Environment="CUSTOM_VAR=lab06test"
```

**Step 5.3 - Verify the override file was created**

```bash
cat /etc/systemd/system/ssh.service.d/override.conf
```

The file should contain the two lines you added.

**Step 5.4 - Run daemon-reload**

```bash
sudo systemctl daemon-reload
```

This is the mandatory step after any unit file change.

**Step 5.5 - Restart the service to apply changes**

```bash
sudo systemctl restart ssh
systemctl status ssh
```

The service should be running with the updated configuration.

**Step 5.6 - Remove the override**

```bash
sudo rm /etc/systemd/system/ssh.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl restart ssh
```

---

### Part 6 - journalctl Log Inspection

**Step 6.1 - View service logs**

```bash
journalctl -u ssh
```

Scroll through with arrow keys or spacebar. Press q to quit.

**Step 6.2 - View logs since last boot**

```bash
journalctl -u ssh -b
```

Shows only entries from the current boot session.

**Step 6.3 - Follow logs in real time**

Open a second terminal and run:

```bash
journalctl -u ssh -f
```

In the first terminal, restart the ssh service:

```bash
sudo systemctl restart ssh
```

Watch the real-time log entries appear in the second terminal. Press Ctrl+C to stop following.

**Step 6.4 - Filter by time**

```bash
journalctl -u ssh --since "1 hour ago"
```

```bash
journalctl -u ssh --since "$(date +%Y-%m-%d) 00:00:00"
```

**Step 6.5 - Filter by priority**

```bash
journalctl -p err -b
```

Shows only error-level and higher messages from the current boot. On a healthy system this may produce no output.

**Step 6.6 - View recent entries**

```bash
journalctl -n 20
```

Shows the last 20 journal entries across all services.

---

### Part 7 - Analysis Questions

**Question 1:** You run ps aux and observe several processes showing STAT value D. The system is running slowly. What does D indicate, and why can these processes not be killed with SIGKILL? What diagnostic step would you take to determine whether this is a disk or network I/O issue?

**Question 2:** A colleague says "There are 5 zombie processes on the server. I need to kill them." Explain why this approach will not work. What is the correct procedure to eliminate zombie processes, and why is a small number of zombies considered harmless?

**Question 3:** You edit the file /etc/systemd/system/myapp.service directly. You then run sudo systemctl restart myapp. The service restarts but your changes are not in effect. What went wrong and what is the exact command sequence to apply your changes correctly?

**Question 4:** Your company runs a backup script every night at 2 AM that compresses large log files. The backup is causing response time problems for other services because it is consuming too much CPU. Write the exact command to start the backup script at an appropriate low-priority nice value. Then write the command to check whether the nice value was applied correctly.

**Question 5:** A junior administrator runs sudo systemctl disable nginx thinking it will stop the currently running nginx service and prevent it from starting again. Describe what actually happens when disable is run. What additional command is needed to also stop the currently running service? Write the single command that would have accomplished both goals at once.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.2 showing the STAT code distribution output
2. Screenshot of Part 2, Step 2.4 showing the permission denied error and the successful sudo renice
3. Screenshot of Part 3, Step 3.2 showing the sleep process killed by SIGTERM
4. Screenshot of Part 3, Step 3.5 showing job control with two background jobs, fg, Ctrl+Z, and bg
5. Screenshot of Part 4, Step 4.3 showing ssh stopped and then started
6. Screenshot of Part 5, Step 5.4 showing the daemon-reload command and the override.conf contents
7. Screenshot of Part 6, Step 6.3 showing journalctl -u ssh -f capturing a restart event
8. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| STAT code distribution screenshot | 10 |
| Permission denied + sudo renice screenshot | 10 |
| SIGTERM kill screenshot | 10 |
| Job control screenshot | 10 |
| ssh stop/start screenshot | 10 |
| daemon-reload + override.conf screenshot | 10 |
| journalctl real-time capture screenshot | 10 |
| Analysis Question 1 (STAT=D and I/O) | 5 |
| Analysis Question 2 (zombie resolution) | 5 |
| Analysis Question 3 (daemon-reload) | 5 |
| Analysis Question 4 (nice for backup) | 5 |
| Analysis Question 5 (disable vs stop) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

**Challenge Step 1 — Simulate and identify a high-load process**

Create a controlled CPU load and observe how the system responds in real time:

```bash
dd if=/dev/zero of=/dev/null &
DD_PID=$!
echo "Started dd with PID $DD_PID"
ps -p $DD_PID -o pid,ppid,stat,ni,pcpu,comm
top -b -n 1 | grep dd
renice -n 15 -p $DD_PID
ps -p $DD_PID -o pid,ni,pcpu,comm
kill $DD_PID
```

While dd is running, open a second terminal and observe the output of:

```bash
uptime
cat /proc/loadavg
vmstat 1 5
```

Document the load average before and after starting dd. Explain in two sentences how
the Linux scheduler uses the nice value to decide how much CPU time to allocate between
competing processes of the same priority class.

**Challenge Step 2 — Write and deploy a custom systemd service unit**

Create a minimal but fully functional systemd service that runs a shell script:

```bash
sudo tee /usr/local/bin/healthcheck.sh << 'EOF'
#!/bin/bash
echo "$(date): Health check OK — uptime: $(uptime -p)" >> /var/log/healthcheck.log
EOF
sudo chmod +x /usr/local/bin/healthcheck.sh

sudo tee /etc/systemd/system/healthcheck.service << 'EOF'
[Unit]
Description=System Health Check Logger
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/healthcheck.sh
User=nobody
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start healthcheck.service
sudo systemctl status healthcheck.service
journalctl -u healthcheck.service -n 20
cat /var/log/healthcheck.log
```

Modify the ExecStart line to an invalid path, attempt to start the service, observe the
failure, and use journalctl to diagnose it:

```bash
sudo sed -i 's|/usr/local/bin/healthcheck.sh|/usr/local/bin/MISSING.sh|' \
  /etc/systemd/system/healthcheck.service
sudo systemctl daemon-reload
sudo systemctl start healthcheck.service
journalctl -u healthcheck.service -n 10
```

Document the exact journal error message. Explain in two sentences why journalctl is
more useful than /var/log/syslog for diagnosing systemd service failures.

**Challenge Step 3 — Identify and trace zombie and orphan processes**

Create a controlled zombie process using a Python script to observe the condition:

```bash
python3 - << 'EOF'
import os, time
pid = os.fork()
if pid > 0:
    print(f"Parent PID: {os.getpid()}, child PID: {pid}")
    print("Parent sleeping 30s without calling wait()...")
    time.sleep(30)
else:
    print(f"Child PID {os.getpid()} exiting immediately")
    os._exit(0)
EOF
```

In a second terminal, while the Python script is sleeping, run:

```bash
ps aux | grep -E "Z|zombie|defunct"
ps -o pid,ppid,stat,comm -p $(pgrep -P $(pgrep python3))
```

Document the zombie entry. After the parent exits, verify the zombie is reaped. Then
explain in three sentences: (1) why the zombie exists, (2) why SIGKILL cannot remove it,
and (3) what the correct resolution is when a parent process refuses to call wait().
