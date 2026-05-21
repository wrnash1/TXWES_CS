# Quiz: Module 13 - Cron Jobs and Task Scheduling
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator needs to schedule a backup script at `/usr/local/bin/backup.sh` to run every day at 3:15 AM. Which crontab entry is correct?
A) 15 3 * * * /usr/local/bin/backup.sh
B) 3 15 * * * /usr/local/bin/backup.sh
C) * * 3 15 * /usr/local/bin/backup.sh
D) 0 3 15 * * /usr/local/bin/backup.sh
*   **Correct Answer:** A) 15 3 * * * /usr/local/bin/backup.sh
*   **Distractor Analysis:**
    *   *Why B is incorrect:* The crontab field order is minute, hour, day-of-month, month, day-of-week. This entry has the fields reversed — `3` in the minute position means minute 3, and `15` in the hour position means 3:03 AM, not 3:15 AM.
    *   *Why C is incorrect:* The `*` values in the minute and hour positions mean "every minute of every hour." This entry would run the script every minute whenever the day-of-month is 3 and the month field is 15 — which is an invalid month, so the job would never run.
    *   *Why D is incorrect:* This entry schedules the job at minute 0, hour 3, day-of-month 15 — meaning it would run at 3:00 AM on the 15th of every month, not every day at 3:15 AM.

---

---

**Question 2**
An administrator wants to schedule a cron job that runs every 10 minutes, every hour, every day. Which minute-field value in the crontab entry achieves this?
A) 10
B) 0,10
C) */10
D) 10-60
*   **Correct Answer:** C) */10
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The value `10` in the minute field means the job runs at minute 10 of every hour — that is once per hour, not every 10 minutes.
    *   *Why B is incorrect:* `0,10` is a list that runs the job at minute 0 and minute 10 of every hour — that is twice per hour, not every 10 minutes (which requires 6 executions per hour: 0, 10, 20, 30, 40, 50).
    *   *Why D is incorrect:* `10-60` is a range meaning "run at every minute from minute 10 through minute 60." Minute 60 does not exist (valid range is 0–59), and this would trigger the job every minute for 50 consecutive minutes each hour rather than every 10 minutes.

---

---

**Question 3**
A systems administrator needs to schedule a one-time script execution to run tonight at 11:45 PM. The script should not repeat. Which command is most appropriate?
A) crontab -e, then add: 45 23 * * * /path/to/script.sh
B) at 23:45 (then enter the command at the interactive prompt)
C) systemctl enable --now script.timer
D) cron.daily /path/to/script.sh
*   **Correct Answer:** B) at 23:45 (then enter the command at the interactive prompt)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A crontab entry with `* * *` in the day-of-month, month, and day-of-week fields runs the job every night at 23:45, not just tonight. Cron is for recurring jobs; `at` is designed for one-time future execution.
    *   *Why C is incorrect:* `systemctl enable --now script.timer` would start a systemd timer unit that recurs based on its `OnCalendar` directive — it requires pre-written `.service` and `.timer` unit files and is not appropriate for a quick one-time job.
    *   *Why D is incorrect:* `cron.daily` is a directory (`/etc/cron.daily/`) where scripts are placed for daily execution by `run-parts`. Scripts placed there run at a system-determined daily time, not at a specific user-chosen time, and they recur every day.

---

**Question 4**
An administrator creates a file `/etc/cron.allow` containing only the username `alice`. User `bob` attempts to run `crontab -e` and receives a "permission denied" error. User `alice` is not listed in `/etc/cron.deny`. What is the correct explanation?
A) `bob` needs to be added to the `cron` system group to use `crontab`.
B) When `/etc/cron.allow` exists, only users explicitly listed in it may use cron. All other users are denied, regardless of `/etc/cron.deny`.
C) Both `/etc/cron.allow` and `/etc/cron.deny` must list a user to grant access. `bob` needs to be in both files.
D) `bob` is blocked because `/etc/cron.deny` does not list him — he must be added to `cron.deny` to be explicitly permitted.
*   **Correct Answer:** B) When `/etc/cron.allow` exists, only users explicitly listed in it may use cron. All other users are denied, regardless of `/etc/cron.deny`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cron access is not controlled by group membership in the `cron` group. It is controlled by the `/etc/cron.allow` and `/etc/cron.deny` files. Group membership in `cron` grants no scheduling privileges on standard Linux systems.
    *   *Why C is incorrect:* The two files are not used together in an AND relationship. `/etc/cron.allow` alone is sufficient — if it exists, it is the sole arbiter. A user listed in `cron.allow` is permitted; all others are denied.
    *   *Why D is incorrect:* The logic of `cron.deny` is opposite to this description. `/etc/cron.deny` is a blocklist — users listed there are denied. Being absent from `cron.deny` grants access only when `cron.allow` does not exist. Since `cron.allow` exists here, `cron.deny` is irrelevant.

---

**Question 5**
An administrator places a shell script `cleanup.sh` in `/etc/cron.daily/` but notices it never executes. Investigation shows the script has execute permission. What is the most likely cause on a Debian-based system?
A) Scripts in `/etc/cron.daily/` must be owned by the `cron` user, not root.
B) The script filename has a `.sh` extension, which causes `run-parts` to skip it on Debian-based systems.
C) `/etc/cron.daily/` requires scripts to be registered with `update-rc.d` before they are executed.
D) The `crond` service must be manually reloaded with `systemctl reload cron` after adding a script to `/etc/cron.daily/`.
*   **Correct Answer:** B) The script filename has a `.sh` extension, which causes `run-parts` to skip it on Debian-based systems.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Scripts in `/etc/cron.daily/` are typically owned by root and executed as root by `run-parts`. Ownership by a dedicated `cron` user is not required and is not the standard configuration.
    *   *Why C is incorrect:* `update-rc.d` manages SysV init service symlinks. It has no relationship to cron job directories or `run-parts` script execution. Scripts in `/etc/cron.daily/` do not need to be registered with any init tool.
    *   *Why D is incorrect:* The `cron` daemon continuously scans crontab files and system cron directories — it does not need to be reloaded when a new script is dropped into `/etc/cron.daily/`. The daemon detects the script automatically on its next scheduled run.
