# Video Script: Module 13 - Cron Jobs and Task Scheduling (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Cron, Crontab, and System Cron Directories

---

### Opening

Welcome to Module 13. Automation is at the heart of Linux administration. Every production system
has jobs that need to run on a schedule: database backups at 2 AM, log cleanup at midnight, health
check reports every 15 minutes. In this module we cover the two primary scheduling mechanisms in
Linux: cron for recurring jobs and at for one-time jobs. We also cover systemd timers, which are
the modern alternative to cron on systemd-based systems.

---

### Section 1: The cron Architecture

[SHOW TERMINAL]

Cron is a daemon that wakes up every minute, checks whether any scheduled jobs need to run, and
executes them. It reads from several locations:

- `/var/spool/cron/crontabs/` — per-user crontab files (edited with `crontab -e`)
- `/etc/crontab` — the system crontab (has an extra "user" field)
- `/etc/cron.d/` — application-installed cron fragments
- `/etc/cron.hourly/`, `/etc/cron.daily/`, `/etc/cron.weekly/`, `/etc/cron.monthly/` — scripts
  run by `run-parts` at the named intervals

```bash
systemctl status cron          # Ubuntu/Debian
systemctl status crond         # RHEL/CentOS
```

The cron daemon logs to syslog. On Ubuntu, cron entries appear in /var/log/syslog.

```bash
grep CRON /var/log/syslog | tail -10
```

---

### Section 2: Crontab Syntax

[SHOW TERMINAL]

A crontab entry has five time fields followed by the command to run:

```
MIN HOUR DOM MON DOW COMMAND
```

| Field | Position | Range |
|-------|----------|-------|
| Minute | 1 | 0-59 |
| Hour | 2 | 0-23 |
| Day of month | 3 | 1-31 |
| Month | 4 | 1-12 |
| Day of week | 5 | 0-7 (0 and 7 both = Sunday) |

Special values:

- `*` — every value (wildcard)
- `*/N` — every N (step): `*/15` in the minute field = every 15 minutes
- `N,M` — list: `1,15` in hour field = 1 AM and 3 PM
- `N-M` — range: `1-5` in day-of-week = Monday through Friday

Examples:

```
# Run at 3:15 AM every day
15 3 * * * /usr/local/bin/backup.sh

# Run every 10 minutes
*/10 * * * * /usr/local/bin/health-check.sh

# Run at 6 AM Monday through Friday
0 6 * * 1-5 /usr/local/bin/report.sh

# Run on the 1st of every month at midnight
0 0 1 * * /usr/local/bin/monthly-cleanup.sh

# Run every hour on weekdays
0 * * * 1-5 /usr/local/bin/sync.sh
```

---

### Section 3: Managing User Crontabs

[SHOW TERMINAL]

```bash
crontab -e
```

Opens the current user's crontab in the default editor ($VISUAL or $EDITOR, falling back to vi).
Always use `crontab -e` rather than editing the file under /var/spool/cron/ directly — the -e flag
validates syntax before saving.

```bash
crontab -l
```

List the current user's crontab.

```bash
crontab -r
```

Remove the current user's crontab entirely. Be careful — there is no confirmation prompt.

```bash
sudo crontab -u alice -l
```

List another user's crontab as root.

```bash
sudo crontab -u alice -e
```

Edit another user's crontab as root.

---

### Section 4: Environment and Output in Crontab

[SHOW TERMINAL]

Cron runs jobs with a minimal environment — it does not load your shell profile. The PATH is
typically just `/usr/bin:/bin`. Always use full paths to commands and scripts.

```
# Good — full paths
*/5 * * * * /usr/local/bin/script.sh >> /var/log/script.log 2>&1

# Bad — relies on PATH
*/5 * * * * script.sh
```

Redirect output explicitly. If you do not redirect, cron emails output to the local user.

```
# Discard all output
*/5 * * * * /usr/local/bin/script.sh > /dev/null 2>&1

# Log stdout and stderr to a file
*/5 * * * * /usr/local/bin/script.sh >> /var/log/script.log 2>&1
```

Set variables at the top of the crontab:

```
SHELL=/bin/bash
MAILTO=admin@example.com
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

*/5 * * * * /usr/local/bin/script.sh
```

MAILTO="" suppresses email entirely. Setting SHELL ensures bash-specific syntax works.

---

### Section 5: System Cron Directories and /etc/cron.d/

[SHOW TERMINAL]

```bash
ls /etc/cron.d/
cat /etc/cron.d/0hourly     # RHEL example
```

Files in /etc/cron.d/ use the same syntax as /etc/crontab — they have a username field between the
time fields and the command:

```
MIN HOUR DOM MON DOW USER COMMAND
```

Example from /etc/cron.d/:

```
# Run as www-data every day at 1 AM
0 1 * * * www-data /usr/bin/php /var/www/html/cron.php > /dev/null 2>&1
```

The drop-in directories (cron.hourly, cron.daily, cron.weekly, cron.monthly) are run by
`run-parts`, which executes every executable file in the directory that matches the naming rules.

```bash
ls /etc/cron.daily/
```

On Debian/Ubuntu, `run-parts` requires filenames to contain only letters, digits, underscores, and
hyphens — no dots, no extensions. A script named `backup.sh` will be silently skipped. Name it
`backup` instead.

---

### Section 6: Cron Access Control

[SHOW TERMINAL]

Two files control who can use cron:

```bash
cat /etc/cron.allow   # If this file exists, only listed users may use cron
cat /etc/cron.deny    # Users listed here are denied cron access
```

Access rules (in priority order):

1. If `/etc/cron.allow` exists: only users listed in it may use cron. All others denied.
2. If `/etc/cron.allow` does not exist but `/etc/cron.deny` exists: all users except those listed
   may use cron.
3. If neither file exists: all users may use cron (on most systems).

This is a critical exam point: the existence of cron.allow overrides cron.deny entirely.

---

### Section 7: Certification Connection

Cron maps to Linux+ Domain 4.0 (Automation). Key exam objectives:

- Know the five crontab fields in order: minute, hour, day-of-month, month, day-of-week.
- Know step syntax `*/N`, list syntax `N,M`, and range syntax `N-M`.
- Know that cron.allow takes precedence over cron.deny when both exist.
- Know that scripts in /etc/cron.daily/ must not have extensions on Debian/Ubuntu (run-parts rule).
- Know that cron runs with a minimal PATH — always use absolute paths in crontab entries.

---

### Transition to Part 2

In Part 2 we cover one-time scheduling with `at`, the `anacron` system for machines that are not
always running, and systemd timers as a modern alternative to cron. We also cover common cron
troubleshooting patterns.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
