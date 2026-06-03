# Quiz: Module 13 - Cron Jobs and Task Scheduling

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

### Question 1

An administrator needs to schedule a backup script at `/usr/local/bin/backup.sh` to run every day at 3:15 AM. Which crontab entry is correct?

* A: `15 3 * * * /usr/local/bin/backup.sh`
* B: `3 15 * * * /usr/local/bin/backup.sh`
* C: `0 3 15 * * /usr/local/bin/backup.sh`
* D: `0 15 3 * * /usr/local/bin/backup.sh`

Correct Answer: A

Distractor Analysis:

* Why B is incorrect: The crontab field order is minute, hour, day-of-month, month, day-of-week. This entry has minute and hour reversed — `3` in the minute position means minute 3, and `15` in the hour position means 3:03 PM (15:03), not 3:15 AM.
* Why C is incorrect: This entry schedules the job at minute 0, hour 3, day-of-month 15 — meaning it would run at 3:00 AM on the 15th of every month, not every day at 3:15 AM.
* Why D is incorrect: `0 15 3 * *` runs at minute 0, hour 15 (3 PM), day-of-month 3 — once per month at 3:00 PM on the 3rd, not every day at 3:15 AM.

---

### Question 2

An administrator wants a cron job to run every 10 minutes, every hour, every day. Which minute-field value achieves this?

* A: `10`
* B: `0,10`
* C: `*/10`
* D: `10-60`

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: The value `10` in the minute field means the job runs at minute 10 of every hour — once per hour, not every 10 minutes.
* Why B is incorrect: `0,10` is a list that runs the job at minute 0 and minute 10 of every hour — twice per hour, not every 10 minutes (which requires 6 executions: 0, 10, 20, 30, 40, 50).
* Why D is incorrect: `10-60` is a range meaning "every minute from 10 through 60." Minute 60 does not exist (valid range is 0-59), and this would fire every minute for 50 consecutive minutes rather than every 10 minutes.

---

### Question 3

A systems administrator needs to schedule a one-time script execution to run tonight at 11:45 PM. The script should not repeat. Which command is most appropriate?

* A: `crontab -e` and add `45 23 * * * /path/to/script.sh`
* B: `at 23:45` and enter the command at the interactive prompt
* C: `systemctl enable --now script.timer`
* D: Place the script in `/etc/cron.daily/`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: A crontab entry with wildcards in the date fields runs the job every night at 23:45, not just tonight. Cron is for recurring jobs; `at` is designed for one-time future execution.
* Why C is incorrect: `systemctl enable --now script.timer` starts a recurring systemd timer based on its `OnCalendar` directive. It requires pre-written `.service` and `.timer` unit files and is not appropriate for a quick one-time job.
* Why D is incorrect: `/etc/cron.daily/` runs scripts at a system-determined daily time — they recur every day and cannot be scheduled for a specific one-time window.

---

### Question 4

An administrator creates `/etc/cron.allow` containing only the username `alice`. User `bob` attempts `crontab -e` and receives "permission denied." What is the correct explanation?

* A: `bob` needs to be added to the `cron` system group.
* B: When `/etc/cron.allow` exists, only users listed in it may use cron; all others are denied regardless of `/etc/cron.deny`.
* C: Both `/etc/cron.allow` and `/etc/cron.deny` must list a user to grant access.
* D: `bob` must be added to `/etc/cron.deny` to be explicitly permitted.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: Cron access is controlled by `/etc/cron.allow` and `/etc/cron.deny`, not group membership. Being in the `cron` group grants no scheduling privileges on standard Linux systems.
* Why C is incorrect: The two files are not used in an AND relationship. If `cron.allow` exists it is the sole arbiter — a user listed there is permitted; all others are denied. `cron.deny` is irrelevant when `cron.allow` exists.
* Why D is incorrect: `cron.deny` is a blocklist — users listed there are denied. Being absent from `cron.deny` grants access only when `cron.allow` does not exist. Since `cron.allow` exists here, `cron.deny` has no effect.

---

### Question 5

An administrator places `cleanup.sh` in `/etc/cron.daily/` with execute permission, but it never runs. What is the most likely cause on a Debian-based system?

* A: Scripts in `/etc/cron.daily/` must be owned by the `cron` user, not root.
* B: The `.sh` extension causes `run-parts` to silently skip the script on Debian-based systems.
* C: Scripts in `/etc/cron.daily/` must be registered with `update-rc.d` before execution.
* D: The `cron` daemon must be reloaded with `systemctl reload cron` after adding a script.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: Scripts in `/etc/cron.daily/` are owned by root and run as root by `run-parts`. A dedicated `cron` user owner is not required.
* Why C is incorrect: `update-rc.d` manages SysV init service symlinks and has no relationship to cron directories or `run-parts`. Scripts in `/etc/cron.daily/` need no registration.
* Why D is incorrect: The `cron` daemon scans directories automatically — no reload is needed when a script is added to `/etc/cron.daily/`.

---

### Question 6

An administrator wants a systemd timer to fire for any runs missed while the system was powered off. Which timer unit directive enables this behavior?

* A: `OnCalendar=catchup`
* B: `Persistent=true`
* C: `AccuracySec=1s`
* D: `RemainAfterElapse=yes`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `OnCalendar=catchup` is not a valid value. `OnCalendar` takes calendar time specifications such as `daily`, `weekly`, or `*-*-* 02:00:00`. There is no `catchup` keyword.
* Why C is incorrect: `AccuracySec=1s` controls the precision window for timer firing, allowing the kernel to batch events for efficiency. It has no effect on whether missed runs are caught up after a power-off.
* Why D is incorrect: `RemainAfterElapse=yes` keeps the timer unit in an elapsed state after firing, making it queryable with `systemctl status`. It does not cause missed runs to replay after the system comes back online.

---

### Question 7

An administrator adds `0 8 * * 1-5 /home/admin/report.sh` to their user crontab. The script runs correctly when executed manually but produces no output when cron runs it. What is the most likely cause?

* A: The crontab entry is missing the username field required for user crontabs.
* B: The script uses commands or paths not available in cron's minimal PATH environment.
* C: The range `1-5` in the day-of-week field is invalid; only comma-separated values are supported.
* D: Output from cron jobs is always discarded unless MAILTO is set to a valid address.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: User crontabs edited with `crontab -e` do not have a username field. The username field exists only in `/etc/crontab` and `/etc/cron.d/` fragments. Adding a username to a user crontab causes the username itself to be treated as the command, resulting in a "command not found" error.
* Why C is incorrect: The range syntax `1-5` is completely valid in the day-of-week field and means Monday through Friday. Ranges are a standard crontab feature alongside lists (1,3,5) and steps.
* Why D is incorrect: Output is not always discarded. Without redirection, cron attempts to deliver output via local mail. Output is only lost if the job redirects to `/dev/null` or no mail agent is available — but the stated symptom is "no output," which points to the script failing silently due to PATH issues.

---

### Question 8

An administrator needs to list all pending at jobs and cancel job number 4. Which command sequence is correct?

* A: `at --list && at --cancel 4`
* B: `atq && atrm 4`
* C: `crontab -l | grep at && crontab -d 4`
* D: `at -q && at -x 4`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `at --list` and `at --cancel` are not valid flags. The correct commands are `atq` (or `at -l`) to list and `atrm N` (or `at -d N`) to remove a specific job.
* Why C is incorrect: `crontab -l` lists cron jobs, not at jobs. At jobs are managed exclusively through `atq` and `atrm`. There is no `crontab -d` flag.
* Why D is incorrect: `at -q` specifies a queue letter when submitting a new at job, not for listing. `at -x` is not a valid flag. The correct flags are `at -l` for listing and `at -d N` for deletion.

---

### Question 9

A crontab entry reads `0 */6 * * * /usr/local/bin/sync.sh`. How many times per day does this job run and at which hours?

* A: 6 times per day at hours 6, 12, 18, 24, 30, 36
* B: Every 6 minutes, 240 times per day
* C: 4 times per day at hours 0, 6, 12, and 18
* D: Once per day at 6:00 AM

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: The `*/6` step in the HOUR field divides the 0-23 range into steps of 6, producing hours 0, 6, 12, and 18. Hours above 23 do not exist in cron's 0-23 range.
* Why B is incorrect: `*/6` is in the HOUR field (position 2), not the MINUTE field (position 1). Step syntax in the hour field runs the job every 6 hours. The MINUTE field is `0`, meaning the job fires at minute 0 of each selected hour.
* Why D is incorrect: `*/6` starting from 0 hits 0, 6, 12, and 18 — four times per day. The value `6` alone in the HOUR field would run the job once at 6 AM; `*/6` runs at every sixth hour starting from 0.

---

### Question 10

Which statement correctly describes the difference between cron and anacron?

* A: cron runs with root privileges; anacron runs as the logged-in user.
* B: cron requires a graphical desktop; anacron runs on headless servers.
* C: cron assumes the system is always on and skips missed jobs; anacron detects missed jobs and runs them at the next boot after the configured delay.
* D: cron supports only daily, weekly, and monthly schedules; anacron supports arbitrary time specifications using the five-field syntax.

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: Both cron and anacron run system jobs as root. User crontabs run as the owning user. The distinction is not about privilege level — it is about behavior when a scheduled time is missed.
* Why B is incorrect: Neither cron nor anacron requires a graphical desktop. Both are background daemons designed for headless server operation.
* Why D is incorrect: This is backwards. Cron supports the full five-field syntax with arbitrary minute/hour/day specifications. Anacron's schedule is defined only in days (1=daily, 7=weekly, 30=monthly) and cannot schedule jobs at a specific time of day.
