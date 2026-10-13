# Video Script: Module 12 — System Services and Daemons (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome back to Module 12, Part 2.

In Part 1, we built a solid foundation in systemd: architecture, unit files, service management with `systemctl`, and the target system. Now we tackle two more critical topics.

First, `journalctl` — the unified logging system that captures everything from kernel messages to service output to authentication events in one queryable database. Second, job scheduling with `cron` and `at` — the tools Linux administrators have relied on for decades to automate repetitive tasks.

---

### Section 6: journalctl — The systemd Journal

**What Is the Journal?**

The systemd journal replaces the traditional scattered log files with a binary structured log database. It captures:

- Kernel messages (what `dmesg` shows)
- Boot messages
- Service stdout and stderr (via `StandardOutput=journal`)
- syslog messages forwarded from rsyslog or syslog-ng
- Authentication events (from PAM and SSH)

By default, the journal is stored in `/run/log/journal/` (volatile — cleared on reboot) or `/var/log/journal/` (persistent, if that directory exists).

**Making the Journal Persistent**

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

Or simply set `Storage=persistent` in `/etc/systemd/journald.conf`.

**Basic journalctl Usage**

View all journal entries (most recent at the bottom):

```bash
journalctl
```

View entries in reverse order (most recent first):

```bash
journalctl -r
```

Follow the journal in real time (like `tail -f`):

```bash
journalctl -f
```

**Filtering by Service**

View logs for a specific systemd unit:

```bash
journalctl -u nginx
journalctl -u nginx -f
journalctl -u nginx --since "1 hour ago"
```

The `-u` flag (unit) is one of the most useful filters.

**Filtering by Time**

```bash
journalctl --since "2024-01-15 08:00:00"
journalctl --since "2024-01-15" --until "2024-01-16"
journalctl --since yesterday
journalctl --since "1 hour ago"
```

Time formats are flexible — systemd parses them intelligently.

**Filtering by Priority**

Journal entries have syslog-compatible priority levels:

| Level | Number | Meaning |
|-------|--------|---------|
| emerg | 0 | System unusable |
| alert | 1 | Immediate action required |
| crit | 2 | Critical conditions |
| err | 3 | Error conditions |
| warning | 4 | Warning conditions |
| notice | 5 | Normal but significant |
| info | 6 | Informational |
| debug | 7 | Debug-level messages |

Show only errors and above:

```bash
journalctl -p err
journalctl -p warning..err
```

**Viewing Boot Logs**

Show logs from the current boot only:

```bash
journalctl -b
```

Show logs from the previous boot:

```bash
journalctl -b -1
```

List all available boot records:

```bash
journalctl --list-boots
```

This is invaluable after a server crash or unexpected reboot — you can examine what happened before the last boot with `journalctl -b -1`.

**Filtering by Process or User**

```bash
journalctl _PID=1234
journalctl _UID=1000
journalctl _COMM=sshd
```

The underscore-prefixed fields are trusted journal fields set by the kernel or systemd itself (not spoofable by userspace processes).

**Kernel Messages**

```bash
journalctl -k            # kernel messages only
journalctl -k -b         # kernel messages from current boot
```

**Output Formats**

```bash
journalctl -u sshd -o json-pretty    # JSON format
journalctl -u sshd -o short-iso      # ISO timestamps
journalctl -u sshd -o cat            # bare messages only
```

**Disk Usage**

Check how much disk space the journal is using:

```bash
journalctl --disk-usage
```

Vacuum old journal entries:

```bash
sudo journalctl --vacuum-size=500M
sudo journalctl --vacuum-time=30d
```

---

### Section 7: Cron — Scheduled Job Automation

**What Is Cron?**

`cron` is the traditional Unix job scheduler. The `crond` daemon reads crontab (cron table) files and executes commands at the scheduled times. Despite systemd timers being the modern alternative, cron remains extremely common and is heavily tested on Linux+.

**The crontab Format**

Each line in a crontab has five time fields followed by the command:

```
* * * * * /path/to/command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7, 0 and 7 = Sunday)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

**Special Characters**

- `*` — every value in this field
- `,` — list of values: `1,15,30`
- `-` — range: `1-5`
- `/` — step: `*/15` means every 15 units

**Common Crontab Examples**

Run a backup every day at 2:30 AM:

```
30 2 * * * /opt/scripts/backup.sh
```

Run a script every 15 minutes:

```
*/15 * * * * /opt/scripts/health-check.sh
```

Run a cleanup every Monday at midnight:

```
0 0 * * 1 /opt/scripts/cleanup.sh
```

Run a report on the 1st of every month at 6 AM:

```
0 6 1 * * /opt/scripts/monthly-report.sh
```

Run a script every weekday (Monday through Friday) at 8 AM:

```
0 8 * * 1-5 /opt/scripts/morning-task.sh
```

**Managing Crontabs**

Edit your own crontab:

```bash
crontab -e
```

This opens the crontab in your default editor (`$EDITOR`). Always use this method — direct editing of crontab files can cause syntax errors and permissions issues.

View your current crontab:

```bash
crontab -l
```

Edit another user's crontab (root only):

```bash
sudo crontab -u username -e
```

Remove your crontab:

```bash
crontab -r
```

**System-wide Cron**

Beyond per-user crontabs, the system crontab is in `/etc/crontab` and includes a username field:

```
30 2 * * * root /opt/scripts/system-backup.sh
```

The `/etc/cron.d/` directory contains package-installed cron files in the same format.

The directories `/etc/cron.hourly/`, `/etc/cron.daily/`, `/etc/cron.weekly/`, and `/etc/cron.monthly/` contain scripts executed at those intervals by the system crontab via `run-parts`.

**Cron Environment**

Cron runs jobs in a minimal environment — PATH is often just `/usr/bin:/bin`. This is a frequent source of cron job failures: the script works when run manually but fails under cron because a command is not found.

Best practices:

- Use absolute paths for all commands in cron jobs
- Set `PATH=` at the top of the crontab if needed
- Redirect output to a log file to capture errors:

```
30 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1
```

**Cron Access Control**

The files `/etc/cron.allow` and `/etc/cron.deny` control which users may use crontab:

- If `cron.allow` exists, only listed users may use cron
- If only `cron.deny` exists, listed users are denied
- If neither exists, behavior depends on distribution (usually all users allowed)

---

### Section 8: at — One-Time Job Scheduling

While cron is for recurring jobs, `at` schedules a job to run once at a specific future time.

**Scheduling a Job with at**

```bash
at 3:00 PM
at> /opt/scripts/deploy.sh
at> <Ctrl+D>
```

Or supply from a script:

```bash
echo "/opt/scripts/deploy.sh" | at 15:00
```

**at Time Formats**

`at` accepts flexible time specifications:

- `at 3pm`
- `at 15:30`
- `at noon tomorrow`
- `at 9am next Monday`
- `at now + 2 hours`
- `at now + 30 minutes`

**Managing at Jobs**

List pending at jobs:

```bash
atq
```

Remove a job:

```bash
atrm <job-number>
```

View a job's contents:

```bash
at -c <job-number>
```

**at Access Control**

Like cron, `at` uses `/etc/at.allow` and `/etc/at.deny` for access control.

---

### Section 9: systemd Timers — The Modern Alternative

For completeness, understand that systemd timers provide a cron-like capability with advantages:

- Integration with journald (timer execution is logged)
- Ability to catch up missed runs
- Fine-grained calendar expressions

A timer unit pairs with a service unit. The timer file:

```ini
[Unit]
Description=Run cleanup daily

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

The corresponding service file runs the actual command.

List active timers:

```bash
systemctl list-timers
```

The Linux+ exam tests both cron and systemd timers — know both.

---

### Summary — Module 12

Module 12 covered the complete systemd ecosystem and job scheduling:

**Part 1:**

- systemd architecture: units, unit types, file locations, dependency model
- `systemctl`: start, stop, restart, reload, enable, disable, mask, status
- Unit file structure: `[Unit]`, `[Service]`, `[Install]` sections and key directives
- Service types: simple, forking, oneshot, notify
- Creating custom service units
- systemd targets replacing SysVinit runlevels

**Part 2:**

- `journalctl`: filtering by unit, time, priority, boot, process, and user
- Journal persistence and disk management
- `cron`: crontab syntax, time field format, per-user and system-wide cron
- Cron best practices: absolute paths, output redirection, environment
- `at`: one-time job scheduling with flexible time specifications
- systemd timers as the modern cron alternative

Proficiency with systemd and job scheduling is tested throughout the Linux+ exam and used every day in production Linux administration.

Next up: Module 13 — Storage and Logical Volume Management.
