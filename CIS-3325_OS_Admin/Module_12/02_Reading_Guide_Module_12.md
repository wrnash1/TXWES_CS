# Reading Guide: Module 12 - System Logging and Monitoring

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 3.0 - Troubleshooting

---

### Glossary

**rsyslog** - A high-performance syslog daemon that receives log messages from applications and the kernel and routes them to files, remote servers, or other destinations based on facility and priority.

**systemd-journald** - The systemd journal daemon that collects log messages from all systemd services, the kernel, and applications. Stores messages in a binary format.

**Syslog Facility** - A category identifying the type of source that generated a log message (kern, auth, mail, daemon, user, local0-7, etc.).

**Syslog Priority** - A severity level from 0 (emerg, most severe) to 7 (debug, least severe). Used in rsyslog routing rules and journalctl -p filtering.

**logrotate** - A utility that automatically compresses, renames, and deletes old log files based on size or time, preventing logs from consuming unlimited disk space.

**vmstat** - A system performance monitoring tool that reports virtual memory, CPU, I/O, and system statistics at configurable intervals.

**iostat** - A tool (part of sysstat) for reporting CPU utilization and disk I/O statistics.

**sar (System Activity Reporter)** - A tool (part of sysstat) that collects and reports historical system performance data including CPU, memory, I/O, and network.

**Load Average** - A measure of system workload reported as three numbers: 1-minute, 5-minute, and 15-minute averages. Values above the CPU core count indicate saturation.

**I/O Wait (wa)** - The percentage of time the CPU is idle because processes are waiting for disk or network I/O to complete.

---

### Key Log Files by Distribution

| Log File | Ubuntu/Debian | RHEL/CentOS | Contents |
|----------|--------------|-------------|---------|
| General system | /var/log/syslog | /var/log/messages | Kernel, daemon, general messages |
| Authentication | /var/log/auth.log | /var/log/secure | SSH logins, sudo, su, PAM |
| Kernel boot | /var/log/kern.log | /var/log/dmesg | Kernel messages |
| Package manager | /var/log/dpkg.log | /var/log/yum.log | Package install/remove |
| SELinux/Audit | Not default | /var/log/audit/audit.log | Audit daemon events |
| Mail | /var/log/mail.log | /var/log/maillog | Mail server messages |

Application-specific logs:

| Service | Log Location |
|---------|-------------|
| nginx | /var/log/nginx/access.log and error.log |
| Apache | /var/log/apache2/ or /var/log/httpd/ |
| MySQL/MariaDB | /var/log/mysql/ or /var/log/mariadb/ |
| cron | /var/log/cron (RHEL) or in /var/log/syslog (Ubuntu) |

---

### journalctl Command Reference

| Command | Output |
|---------|--------|
| journalctl | All journal entries |
| journalctl -b | Current boot only |
| journalctl -b -1 | Previous boot |
| journalctl -b -2 | Boot before that |
| journalctl -u SERVICE | Entries for a specific service unit |
| journalctl -u SERVICE -b | Service entries, current boot |
| journalctl -u SERVICE -f | Follow service entries in real time |
| journalctl -p err | Error priority and above |
| journalctl -p warning | Warning and above (includes err, crit, alert, emerg) |
| journalctl -n N | Last N entries |
| journalctl --since "TIME" | Entries since timestamp |
| journalctl --since "1 hour ago" | Entries from last hour |
| journalctl --disk-usage | Journal disk space used |
| journalctl --vacuum-time=30d | Delete entries older than 30 days |
| journalctl --vacuum-size=500M | Delete old entries until under 500 MB |

---

### Syslog Priority Levels

| Number | Name | Description |
|--------|------|-------------|
| 0 | emerg | System is unusable |
| 1 | alert | Action must be taken immediately |
| 2 | crit | Critical conditions |
| 3 | err | Error conditions |
| 4 | warning | Warning conditions |
| 5 | notice | Normal but significant |
| 6 | info | Informational messages |
| 7 | debug | Debug-level messages |

journalctl -p err shows err (3) and all higher-severity levels (0, 1, 2).
journalctl -p warning shows warning and all higher-severity levels.

---

### logrotate Configuration Reference

| Directive | Meaning |
|-----------|---------|
| daily | Rotate once per day |
| weekly | Rotate once per week |
| monthly | Rotate once per month |
| rotate N | Keep N old log files |
| compress | Compress old files with gzip |
| delaycompress | Delay compression by one rotation cycle |
| missingok | Do not error if log file is missing |
| notifempty | Do not rotate empty files |
| create MODE USER GROUP | Create new empty log with these permissions |
| postrotate/endscript | Run commands after rotation |
| prerotate/endscript | Run commands before rotation |
| size N | Rotate when file reaches size N (e.g., 100M) |

Testing logrotate:

```bash
sudo logrotate -f /etc/logrotate.d/APPNAME    # Force rotation now
sudo logrotate -d /etc/logrotate.d/APPNAME    # Debug: show what would happen
```

---

### vmstat Column Reference

| Column | Category | Meaning |
|--------|----------|---------|
| r | Process | Run queue: processes waiting for CPU |
| b | Process | Processes in uninterruptible sleep |
| swpd | Memory | Swap used (KB) |
| free | Memory | Free memory (KB) |
| si | Memory | Swap pages read in per second |
| so | Memory | Swap pages written out per second |
| bi | I/O | Block input (reads) per second |
| bo | I/O | Block output (writes) per second |
| us | CPU | User space time % |
| sy | CPU | System/kernel time % |
| id | CPU | Idle time % |
| wa | CPU | Waiting for I/O time % |
| st | CPU | Stolen by hypervisor % |

---

### Performance Problem Indicators

| Symptom | Likely Cause | Command to Check |
|---------|-------------|-----------------|
| High vmstat wa (>20%) | I/O bottleneck | iostat -x 1 |
| High vmstat r (>CPU count) | CPU saturation | top, ps aux --sort=-%cpu |
| Non-zero vmstat si/so | Memory pressure (swapping) | free -h |
| High iostat %util | Disk saturation | iostat -x 1 |
| High iostat await | Disk latency | iostat -x 1 |
| Load average > CPU count | CPU or I/O saturation | uptime, vmstat |

---

### Journal Persistence

By default, the journal may be stored in volatile memory:

```bash
ls /run/log/journal/   # volatile (lost on reboot)
ls /var/log/journal/   # persistent (survives reboots)
```

To enable persistence:

```bash
sudo mkdir -p /var/log/journal/
sudo systemctl restart systemd-journald
```

Or set Storage=persistent in /etc/systemd/journald.conf.

---

### Exam Tips

1. Authentication logs differ by distribution: /var/log/auth.log (Ubuntu) vs /var/log/secure (RHEL). This is directly tested.

2. journalctl -p err includes err AND all higher-severity levels (crit, alert, emerg). The -p flag sets a floor, not an exact match.

3. Journal persistence: create /var/log/journal/ directory. Without it, the journal is stored in /run/log/journal/ and is lost on reboot.

4. vmstat wa = I/O wait. vmstat r = run queue (CPU saturation). vmstat si/so = swapping (memory pressure). Know all three.

5. logrotate rotate N keeps N old files. After N+1 rotations, the oldest is deleted. compress gzips old files; delaycompress waits one cycle before compressing.

6. sar -u shows CPU history. sar -r shows memory history. sar -d shows disk history. Historical data is invaluable for "the server was slow at 3 AM" investigations.

7. The first row of vmstat output is the average since boot. Ignore it; focus on subsequent rows for current behavior.

8. logger -p FACILITY.PRIORITY "message" manually injects a syslog message. Useful for testing log routing and for adding messages from scripts.

---

## 9. Supplemental Resources

**1. [systemd-journald Documentation — freedesktop.org](https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html)**
https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html
Official reference for the systemd journal daemon, covering storage modes, configuration directives in journald.conf, and the relationship between volatile and persistent journal storage.

**2. [sysstat — sar, iostat, vmstat User Guide](https://github.com/sysstat/sysstat)**
https://github.com/sysstat/sysstat
The official sysstat project repository with documentation for sar, iostat, mpstat, and pidstat. Includes examples for interpreting %util, await, and run-queue metrics used throughout this module.

**3. [logrotate Man Page — Linux manual pages](https://man7.org/linux/man-pages/man8/logrotate.8.html)**
https://man7.org/linux/man-pages/man8/logrotate.8.html
Complete reference for all logrotate configuration directives including compress, delaycompress, rotate, postrotate, and the missingok and notifempty flags covered in the quiz and lab.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Identify the correct auth log path for Ubuntu and RHEL
- Identify the correct general system log path for Ubuntu and RHEL
- Use tail -f to follow a log file in real time
- Use grep to search for specific patterns in log files
- Use journalctl to filter by unit, boot, priority, and time range
- Make the systemd journal persistent
- Vacuum old journal entries by time and size
- Explain the six syslog priority levels from emerg to info
- Configure logrotate for a simple application log with daily rotation and 7-day retention
- Use vmstat to identify CPU saturation, I/O wait, and memory pressure
- Interpret the vmstat wa, r, si, and so columns
- Use free -h to interpret available versus used memory
- Use iostat -x to identify a disk bottleneck
- Use sar to review historical performance data
