# Reading Guide: Module 13 - Cron Jobs and Task Scheduling

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 4.0 - Automation and Scripting

---

### Glossary

**cron** - A daemon that wakes every minute and executes scheduled commands based on time specifications in crontab files and system cron directories.

**crontab** - A file containing cron job entries for a user or the system. Edited with `crontab -e` for user crontabs; `/etc/crontab` is the system-wide crontab with an added username field.

**run-parts** - A utility that executes all scripts in a directory that match naming rules. Used by cron to execute scripts in cron.hourly, cron.daily, cron.weekly, and cron.monthly.

**at** - A command for scheduling a one-time job to run at a future time. The `atd` daemon executes at jobs. Use when a task should not recur.

**atq** - Lists pending at jobs for the current user. Root sees all users' jobs.

**anacron** - A cron supplement that runs jobs that were missed while the system was powered off. Reads /etc/anacrontab and tracks last-run times in /var/spool/anacron/.

**systemd timer** - A systemd unit file with a .timer extension that activates a .service unit on a schedule. The modern alternative to cron, with full journald logging and dependency management.

**OnCalendar** - The systemd timer directive that specifies a calendar-based schedule (e.g., `daily`, `weekly`, `*-*-* 02:00:00`).

**Persistent=true** - A systemd timer option that triggers the timer immediately at boot if it was missed while the system was off. The systemd equivalent of anacron's catch-up behavior.

**cron.allow / cron.deny** - Files that control user access to cron. If cron.allow exists, only listed users may use cron. If only cron.deny exists, all users except listed ones may use cron.

---

### Crontab Field Reference

```
MIN   HOUR   DOM   MON   DOW   COMMAND
0-59  0-23   1-31  1-12  0-7
```

Day-of-week: 0 and 7 both represent Sunday.

| Field | Meaning | Example |
|-------|---------|---------|
| MIN | Minute (0-59) | `15` = at minute 15 |
| HOUR | Hour (0-23) | `3` = 3 AM |
| DOM | Day of month (1-31) | `1` = 1st of month |
| MON | Month (1-12) | `6` = June |
| DOW | Day of week (0-7) | `1-5` = Mon-Fri |

---

### Crontab Special Value Syntax

| Syntax | Meaning | Example |
|--------|---------|---------|
| `*` | Every value | `* * * * *` = every minute |
| `*/N` | Every N steps | `*/15` in MIN = every 15 min |
| `N,M` | List | `1,15` in HOUR = 1 AM and 3 PM |
| `N-M` | Range | `1-5` in DOW = Mon through Fri |
| `N-M/S` | Range with step | `0-59/10` in MIN = every 10 min |

---

### Common Crontab Examples

| Schedule | Crontab Entry |
|----------|---------------|
| 3:15 AM every day | `15 3 * * *` |
| Every 10 minutes | `*/10 * * * *` |
| Midnight every day | `0 0 * * *` |
| 6 AM Mon-Fri | `0 6 * * 1-5` |
| 1st of every month at midnight | `0 0 1 * *` |
| Every hour | `0 * * * *` |
| Every 30 minutes | `*/30 * * * *` |

---

### crontab Command Reference

| Command | Action |
|---------|--------|
| `crontab -e` | Edit current user's crontab |
| `crontab -l` | List current user's crontab |
| `crontab -r` | Remove current user's crontab (no confirmation) |
| `sudo crontab -u USER -e` | Edit another user's crontab |
| `sudo crontab -u USER -l` | List another user's crontab |

---

### Cron File Locations

| Location | Purpose | Username field? |
|----------|---------|-----------------|
| `/var/spool/cron/crontabs/USER` | Per-user crontab (edit with crontab -e) | No |
| `/etc/crontab` | System-wide crontab | Yes |
| `/etc/cron.d/` | Application-installed cron fragments | Yes |
| `/etc/cron.hourly/` | Scripts run every hour by run-parts | No |
| `/etc/cron.daily/` | Scripts run every day by run-parts | No |
| `/etc/cron.weekly/` | Scripts run every week by run-parts | No |
| `/etc/cron.monthly/` | Scripts run every month by run-parts | No |

---

### run-parts Naming Rules (Debian/Ubuntu)

Scripts in cron.hourly, cron.daily, cron.weekly, cron.monthly must:

* Contain only letters, digits, hyphens, and underscores
* Have NO file extension (no `.sh`, no `.py`, no `.rb`)
* Be executable (`chmod +x`)

A script named `backup.sh` is silently ignored. Rename it to `backup`.

---

### at Command Reference

| Command | Action |
|---------|--------|
| `at 23:45` | Schedule job at 11:45 PM today |
| `at 02:00 tomorrow` | Schedule job at 2 AM tomorrow |
| `at now + 2 hours` | Schedule job 2 hours from now |
| `echo "CMD" \| at 03:00` | Non-interactive at job |
| `atq` | List pending at jobs |
| `atrm N` | Remove at job number N |
| `at -c N` | Show full command for job N |

---

### anacron Configuration (/etc/anacrontab)

```
PERIOD   DELAY   JOB-ID       COMMAND
1        5       cron.daily   run-parts /etc/cron.daily
7        10      cron.weekly  run-parts /etc/cron.weekly
30       15      cron.monthly run-parts /etc/cron.monthly
```

* PERIOD: days between runs
* DELAY: minutes to wait after system boot (prevents boot spike)
* JOB-ID: unique name; last-run date stored in `/var/spool/anacron/JOB-ID`

---

### systemd Timer Unit Structure

Two files are required.

`/etc/systemd/system/example.service`:

```ini
[Unit]
Description=Example Job

[Service]
Type=oneshot
ExecStart=/usr/local/bin/example.sh
```

`/etc/systemd/system/example.timer`:

```ini
[Unit]
Description=Example Timer

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

---

### systemd Timer OnCalendar Examples

| Value | Schedule |
|-------|---------|
| `daily` | Every day at midnight |
| `weekly` | Every Monday at midnight |
| `monthly` | First day of every month |
| `*-*-* 02:00:00` | Every day at 2 AM |
| `Mon..Fri *-*-* 06:00:00` | Weekdays at 6 AM |
| `*-*-* */4:00:00` | Every 4 hours |
| `*:0/15` | Every 15 minutes |

---

### systemd Timer Commands

| Command | Action |
|---------|--------|
| `systemctl list-timers` | Show all active timers |
| `systemctl enable --now NAME.timer` | Enable and start a timer |
| `systemctl status NAME.timer` | Check timer status and next trigger |
| `journalctl -u NAME.service` | View output from the timer's service |
| `systemd-analyze calendar "SPEC"` | Test/validate an OnCalendar expression |

---

### cron.allow / cron.deny Precedence

| State | Who can use cron |
|-------|-----------------|
| cron.allow exists | Only users listed in cron.allow |
| cron.deny exists, cron.allow does not | All users except those in cron.deny |
| Neither file exists | All users (implementation-dependent) |

The same rules apply to `at` via `/etc/at.allow` and `/etc/at.deny`.

---

### Cron Troubleshooting Checklist

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Job never runs | Wrong field order | Verify: MIN HOUR DOM MON DOW |
| Job never runs | Script not executable | `chmod +x /path/script.sh` |
| Job in cron.daily never runs | Filename has extension | Rename: remove `.sh` |
| Command not found in cron | PATH too short | Use full paths or set PATH= |
| No output visible | Not redirected | Add `>> /log/file.log 2>&1` |
| Cron daemon not running | Service stopped | `systemctl start cron` |

---

### Exam Tips

1. Crontab field order is MIN HOUR DOM MON DOW. The most common exam mistake is reversing minute and hour. `15 3 * * *` = 3:15 AM. `3 15 * * *` = 3:03 PM.

2. `*/N` in the minute field means "every N minutes." `*/15` = runs at :00, :15, :30, :45 every hour. This is step syntax, not a range.

3. cron.allow precedence: if `/etc/cron.allow` exists, it is the only file that matters. cron.deny is completely ignored when cron.allow exists.

4. run-parts on Debian/Ubuntu: scripts must have no extension. `backup.sh` is silently skipped. This is a directly testable exam scenario.

5. `at` is for one-time jobs. Cron is for recurring jobs. If the exam says "run once tonight," the answer is `at`, not a crontab entry with `* * *`.

6. anacron catches missed jobs on systems that are not always running. `Persistent=true` in a systemd timer does the same thing. Both are alternatives to standard cron for laptops or machines with unpredictable uptime.

7. Cron runs with a minimal PATH. Always use absolute paths in crontab entries. This is the most common reason a cron job works interactively but fails when run by cron.

8. systemd timers require both a `.timer` unit and a `.service` unit. The timer activates the service. Enable with `systemctl enable --now NAME.timer`, not the service unit directly.

---

## 9. Supplemental Resources

**1. [crontab(5) — Linux manual pages](https://man7.org/linux/man-pages/man5/crontab.5.html)**
https://man7.org/linux/man-pages/man5/crontab.5.html
The authoritative man page for crontab file format, covering field ranges, special characters (*/N, N-M, N,M), the username field in /etc/crontab, and environment variable handling in cron jobs.

**2. [systemd.timer — freedesktop.org](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)**
https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html
Official reference for all systemd timer unit directives including OnCalendar, Persistent, AccuracySec, OnBootSec, and OnUnitActiveSec with calendar expression examples.

**3. [anacron(8) — Linux manual pages](https://man7.org/linux/man-pages/man8/anacron.8.html)**
https://man7.org/linux/man-pages/man8/anacron.8.html
Complete reference for anacron configuration and behavior, covering the /etc/anacrontab format, PERIOD/DELAY/JOB-ID fields, and how anacron determines whether a missed job needs to run using /var/spool/anacron timestamps.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

* Write a crontab entry for any given time specification without reversing minute and hour
* Explain the meaning of `*/15`, `1,15`, and `1-5` in crontab fields
* Use `crontab -e`, `crontab -l`, and `crontab -r` correctly
* Explain why scripts in /etc/cron.daily/ must not have a .sh extension on Ubuntu
* Schedule a one-time job with `at` and list or remove pending jobs with `atq`/`atrm`
* Explain what anacron does that cron cannot
* Create a systemd timer unit pair (.service + .timer) for a scheduled job
* Use `systemctl list-timers` to view active timer schedules
* Explain the difference between cron.allow and cron.deny and their precedence
* Troubleshoot a cron job that silently fails (PATH, permissions, filename extension)
