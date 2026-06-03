# Video Script: Module 13 - Cron Jobs and Task Scheduling (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - at, anacron, systemd Timers, and Troubleshooting

---

### Opening

Welcome back to Part 2 of Module 13. In Part 1 we covered cron syntax, crontab management, system
cron directories, and access control. In Part 2 we cover one-time scheduling with `at`, anacron
for systems that are not always on, systemd timers, and cron troubleshooting.

---

### Section 1: One-Time Scheduling with at

[SHOW TERMINAL]

`at` schedules a command to run once at a specified future time. Unlike cron, the job does not
repeat.

```bash
sudo apt install at     # Install if not present
systemctl status atd    # The at daemon must be running
```

```bash
at 23:45
```

This opens an interactive prompt. Type your commands, then press Ctrl+D to submit.

```bash
at 2:30 AM tomorrow
at noon
at now + 2 hours
at 09:00 Jul 15
```

Flexible time syntax. `at` accepts natural language time specifications.

```bash
echo "/usr/local/bin/backup.sh" | at 02:00
```

Non-interactive: pipe the command directly.

```bash
atq
```

List pending at jobs (equivalent to `at -l`).

```bash
atrm 3
```

Remove job number 3 from the queue (equivalent to `at -d 3`).

```bash
at -c 3
```

Print the full environment and commands for job 3.

Access control for `at` works the same way as cron: `/etc/at.allow` and `/etc/at.deny` with the
same precedence rules — if `at.allow` exists, only listed users may use `at`.

---

### Section 2: anacron for Non-Always-On Systems

[SHOW TERMINAL]

Cron assumes the system is always running. If a cron job is scheduled for 3 AM and the machine
was off at 3 AM, the job is skipped — it does not run when the machine comes back up.

`anacron` solves this problem. It runs jobs that were missed while the system was off. It reads
from `/etc/anacrontab`:

```bash
cat /etc/anacrontab
```

Anacrontab format:

```
PERIOD  DELAY  JOB-ID  COMMAND
```

- PERIOD: days between runs (1 = daily, 7 = weekly, 30 = monthly)
- DELAY: minutes to wait after boot before running (staggers jobs to avoid boot spike)
- JOB-ID: a unique name used to track last run time in `/var/spool/anacron/`
- COMMAND: the command to run

```
1    5    cron.daily    run-parts /etc/cron.daily
7    10   cron.weekly   run-parts /etc/cron.weekly
30   15   cron.monthly  run-parts /etc/cron.monthly
```

On modern systems, `cron.daily`, `cron.weekly`, and `cron.monthly` are actually managed by
anacron via `/etc/cron.d/0hourly` or similar, not by traditional cron hourly triggers.

```bash
ls /var/spool/anacron/
cat /var/spool/anacron/cron.daily
```

The file contains the date anacron last ran this job. If it is more than PERIOD days ago, the job
runs at the next boot (after the DELAY).

---

### Section 3: systemd Timers

[SHOW TERMINAL]

systemd timers are the modern alternative to cron. A timer unit (`.timer`) activates a service
unit (`.service`) on a schedule. The advantage: the service unit gets full systemd logging,
dependency management, and restart handling.

```bash
systemctl list-timers
```

Show all active timers with their next trigger time, last trigger, and the unit they activate.

A timer requires two unit files — a `.service` and a `.timer`:

Service unit example (`/etc/systemd/system/backup.service`):

```ini
[Unit]
Description=Daily Backup

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

Timer unit example (`/etc/systemd/system/backup.timer`):

```ini
[Unit]
Description=Daily Backup Timer

[Timer]
OnCalendar=daily
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

`OnCalendar` accepts flexible time specifications:
- `daily` — every day at midnight
- `weekly` — every week
- `*-*-* 02:00:00` — every day at 2 AM
- `Mon..Fri *-*-* 06:00:00` — weekdays at 6 AM
- `*-*-* */4:00:00` — every 4 hours

`Persistent=true` is the anacron equivalent for systemd — if the timer was missed (system was off),
it fires at the next boot.

```bash
sudo systemctl enable --now backup.timer
sudo systemctl status backup.timer
journalctl -u backup.service     # View the service log output
```

---

### Section 4: Cron Troubleshooting

[SHOW TERMINAL]

Common reasons a cron job does not run:

1. Wrong PATH — the script uses a command not in cron's minimal PATH

```
# Fix: use full paths or set PATH at the top of crontab
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
```

2. Script not executable

```bash
ls -l /usr/local/bin/backup.sh
chmod +x /usr/local/bin/backup.sh
```

3. Script has a .sh extension in /etc/cron.daily/ (Debian/Ubuntu run-parts rule)

```bash
# rename cleanup.sh to cleanup
sudo mv /etc/cron.daily/cleanup.sh /etc/cron.daily/cleanup
```

4. Output not captured — errors go to local mail, never seen

```
*/5 * * * * /usr/local/bin/script.sh >> /var/log/script.log 2>&1
```

5. Cron daemon not running

```bash
systemctl status cron
```

6. Wrong field order — very common mistake

```
# Wrong: hour then minute
3 15 * * * /path/script.sh   # This runs at 15:03, not 03:15

# Correct: minute then hour
15 3 * * * /path/script.sh   # This runs at 03:15
```

Verify a cron job ran by checking the cron log:

```bash
grep CRON /var/log/syslog | grep backup
```

---

### Section 5: Exam Tips for Module 13

Crontab field order: minute, hour, day-of-month, month, day-of-week. The most common exam trap is
reversing minute and hour.

Step syntax: `*/15` in the minute field = every 15 minutes. `*/2` in the hour field = every 2
hours. The `*` divides the entire range into equal steps.

`at` vs cron: `at` runs once. cron runs repeatedly. The exam will test whether you choose the
right tool for "run this once tonight" versus "run this every night."

anacron vs cron: anacron handles missed jobs on systems that are not always running. Know that
`Persistent=true` is the systemd timer equivalent.

systemd timer: requires both a `.service` unit and a `.timer` unit. `OnCalendar=` sets the
schedule. `Persistent=true` catches missed runs.

run-parts naming: no dots, no extensions on Debian/Ubuntu. Scripts named `backup.sh` are silently
skipped.

cron.allow precedence: if cron.allow exists, it is the only list that matters. cron.deny is
ignored when cron.allow is present.

---

### Summary

Module 13 covers the complete Linux task scheduling stack: cron syntax and crontab management,
system cron directories and run-parts, cron.allow/cron.deny access control, at for one-time jobs,
anacron for catch-up on missed jobs, and systemd timers as the modern alternative with Persistent
support.

Module 14 covers SELinux and AppArmor mandatory access controls.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
