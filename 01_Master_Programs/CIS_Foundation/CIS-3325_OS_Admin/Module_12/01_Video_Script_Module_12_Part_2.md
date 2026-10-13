# Video Script: Module 12 - System Logging and Monitoring (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - Performance Monitoring

---

### Opening

Welcome back to Part 2 of Module 12. In Part 1 we covered rsyslog, journald, log file
locations, journalctl usage, and logrotate. In Part 2 we cover performance monitoring
tools that give you a real-time view of system resource utilization: vmstat, free, iostat,
top, uptime, and sar.

---

### Section 1: Memory Status with free

[SHOW TERMINAL]

```bash
free -h
```

Shows memory statistics in human-readable format.

Output columns:
- total: total installed RAM
- used: currently used memory
- free: completely unused memory
- shared: memory shared between processes (tmpfs, etc.)
- buff/cache: memory used for disk cache and buffers
- available: the most useful number — estimated memory available for new processes (free + reclaimable cache)

The available column is what matters for capacity planning. Linux aggressively uses free
memory as disk cache to improve performance. The buff/cache memory is released when
applications need it.

```bash
free -h -s 2
```

-s 2 updates every 2 seconds. Press Ctrl+C to stop.

---

### Section 2: System Overview with vmstat

[SHOW TERMINAL]

```bash
vmstat 1 5
```

Outputs 5 samples, one per second. The first row is averages since boot; ignore it.
Focus on rows 2-5 for current state.

vmstat columns:

| Column | Meaning |
|--------|---------|
| r | Run queue: processes waiting for CPU |
| b | Processes in uninterruptible sleep (waiting for I/O) |
| swpd | Swap used |
| free | Free memory |
| si | Swap-in per second (pages read from swap) |
| so | Swap-out per second (pages written to swap) |
| bi | Block input per second (reads from disk) |
| bo | Block output per second (writes to disk) |
| in | Interrupts per second |
| cs | Context switches per second |
| us | User CPU time % |
| sy | System CPU time % |
| id | Idle CPU time % |
| wa | Wait for I/O % |
| st | Stolen CPU (virtualization) |

Key indicators:
- High r: CPU saturation. More processes than CPUs can run simultaneously.
- High wa: I/O bottleneck. CPU is idle waiting for disk/network.
- Non-zero si/so: Memory pressure — system is swapping.
- High b: Processes blocked on I/O.

---

### Section 3: Disk I/O with iostat

[SHOW TERMINAL]

```bash
sudo apt install sysstat
iostat
```

Shows CPU usage and disk I/O statistics.

```bash
iostat -x 1 3
```

Extended output, 3 samples, 1 second interval.

Key iostat -x columns:

| Column | Meaning |
|--------|---------|
| r/s | Reads per second |
| w/s | Writes per second |
| rMB/s | Read MB per second |
| wMB/s | Write MB per second |
| await | Average I/O wait time in milliseconds |
| %util | Device utilization percentage |

%util near 100% means the disk is saturated. High await (above 10-20ms for SSDs, 50ms
for HDDs) means I/O latency is high.

```bash
iostat -x -d /dev/sda 1
```

Monitor a specific disk.

---

### Section 4: System Activity Reporter (sar)

[SHOW TERMINAL]

sar is part of the sysstat package. It records system metrics periodically and allows
you to review historical data.

```bash
sar -u 1 5
```

CPU utilization, 5 samples every 1 second.

```bash
sar -r 1 5
```

Memory utilization.

```bash
sar -d 1 5
```

Disk I/O.

```bash
sar -n DEV 1 5
```

Network interface statistics.

Historical data (collected by sa1/sa2 cron jobs):

```bash
sar -u -f /var/log/sysstat/sa$(date +%d)
```

Review today's CPU utilization history.

```bash
sar -u -s 09:00:00 -e 10:00:00
```

Review CPU data between 9 AM and 10 AM from today's collected data.

sar is invaluable for investigating past performance problems: "the server was slow at
2 AM" is investigable with sar historical data even though you were asleep.

---

### Section 5: uptime and Load Average

[SHOW TERMINAL]

```bash
uptime
```

Shows: current time, how long the system has been running, number of users, and the
1-minute, 5-minute, and 15-minute load averages.

Load average interpretation: compare to the number of CPU cores (nproc shows the count).
A 1-minute load average equal to the number of cores means the CPUs are exactly saturated.
Above the core count: processes are queued waiting for CPU.

```bash
nproc
```

Number of available processors.

```bash
cat /proc/loadavg
```

Load averages directly from the kernel. The format is:
1min_avg 5min_avg 15min_avg running/total PID_of_last_created_process

---

### Section 6: Monitoring with top

[SHOW TERMINAL]

```bash
top
```

The load average, CPU breakdown, memory, and swap are in the header. These tell the same
story as vmstat but at a glance.

Interactive top fields for performance analysis:
- P: sort by CPU usage (default)
- M: sort by memory usage
- N: sort by PID
- T: sort by running time
- k: kill a process (prompts for PID and signal)
- r: renice (change priority)

The %CPU column in top shows CPU usage for each process. A process using 100% is consuming
one full CPU core.

To show the processes using the most CPU:

```bash
top -b -n 1 | head -20
```

Batch mode, one sample, first 20 lines. Useful in scripts.

```bash
ps aux --sort=-%cpu | head -10
```

Alternative: sort ps output by CPU usage and show the top 10.

---

### Section 7: Exam Tips for Module 12

Know the log file by distribution:
- Auth: /var/log/auth.log (Ubuntu) or /var/log/secure (RHEL)
- System: /var/log/syslog (Ubuntu) or /var/log/messages (RHEL)

journalctl priority filtering: -p err shows err, crit, alert, emerg. The -p flag includes
all messages at the specified priority and above (more severe).

Journal persistence: create /var/log/journal/ directory. Without it, the journal is
volatile (lost on reboot).

vmstat wa column: I/O wait. High wa = disk bottleneck.
vmstat r column: run queue. High r = CPU bottleneck.
vmstat si/so columns: swapping. Non-zero si/so = memory pressure.

logrotate rotate N: keep N old files. compress: gzip them. postrotate: run commands
after rotation.

---

### Summary

Module 12 covers the complete Linux logging and monitoring stack: rsyslog and journald for
log collection, key log files by distribution, journalctl for log querying, logrotate for
log management, and vmstat/free/iostat/sar for performance monitoring.

Module 13 covers cron and task scheduling.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
