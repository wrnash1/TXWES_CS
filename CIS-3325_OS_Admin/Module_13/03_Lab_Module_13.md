# Lab Activity: Module 13 - Cron Jobs and Task Scheduling

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Time:** 70 minutes
**Points:** 100

---

### Objectives

By the end of this lab you will be able to:

* Write crontab entries for various time specifications
* Manage user crontabs with crontab -e, -l, and -r
* Place scripts in system cron directories and verify run-parts naming rules
* Schedule one-time jobs with at and manage the at queue
* Create a systemd timer unit pair and enable it
* Troubleshoot a cron job that silently fails due to PATH issues

---

### Prerequisites

* Ubuntu 22.04 LTS virtual machine with sudo access
* The `at` daemon installed: `sudo apt install -y at`
* The `atd` service running: `sudo systemctl enable --now atd`

---

### Part 1 — Crontab Syntax Practice (15 points)

#### Step 1.1 — Verify the cron service is running

```bash
systemctl status cron
```

Confirm the cron daemon is active. On RHEL it is named `crond`.

#### Step 1.2 — Open and examine an empty crontab

```bash
crontab -e
```

The editor opens with commented instructions. Read the format reminder at the top. Add this entry at the bottom:

```text
# Lab 13 - runs every minute for testing
* * * * * echo "cron test $(date)" >> /tmp/cron_test.log
```

Save and exit. Wait 2 minutes, then check the log:

```bash
cat /tmp/cron_test.log
```

You should see two entries, one per minute. This confirms cron is working.

#### Step 1.3 — Edit the entry to run every 5 minutes

```bash
crontab -e
```

Change the entry to:

```text
*/5 * * * * echo "cron 5min test $(date)" >> /tmp/cron_test.log
```

#### Step 1.4 — List and verify the crontab

```bash
crontab -l
```

Confirm the entry shows `*/5` in the minute field.

#### Step 1.5 — Review cron log entries

```bash
grep CRON /var/log/syslog | tail -10
```

You should see entries showing cron executing the job and the return code.

---

### Part 2 — Writing Time Specifications (20 points)

#### Step 2.1 — Add multiple timed entries to practice syntax

```bash
crontab -e
```

Add the following entries (do not remove the existing entry):

```text
# At 3:15 AM every day
15 3 * * * echo "daily 3:15am" >> /tmp/cron_times.log

# Every 10 minutes
*/10 * * * * echo "every-10min $(date +%H:%M)" >> /tmp/cron_times.log

# At 6 AM Monday through Friday only
0 6 * * 1-5 echo "weekday 6am" >> /tmp/cron_times.log

# On the 1st of every month at midnight
0 0 1 * * echo "monthly first" >> /tmp/cron_times.log
```

#### Step 2.2 — List and verify all entries

```bash
crontab -l
```

Confirm all four new entries appear. Note the field positions and confirm the syntax matches the intended schedules.

#### Step 2.3 — Interpret crontab entries

Without running them, answer in writing what time each of these would execute:

```text
30 18 * * 5
0 */4 * * *
15,45 * * * *
0 9 1-7 * 1
```

(Include your answers in the lab submission.)

---

### Part 3 — System Cron Directories and run-parts (15 points)

#### Step 3.1 — Examine the daily cron directory

```bash
ls -la /etc/cron.daily/
```

Note which scripts have execute permission and observe their naming conventions — no extensions.

#### Step 3.2 — Create a script with the wrong name (to observe the failure)

```bash
sudo tee /etc/cron.daily/lab13test.sh > /dev/null << 'EOF'
#!/bin/bash
echo "lab13test ran at $(date)" >> /tmp/cron_daily_test.log
EOF
sudo chmod +x /etc/cron.daily/lab13test.sh
```

Test it with run-parts in verbose mode:

```bash
sudo run-parts --test /etc/cron.daily/
```

The `--test` flag lists scripts that would run. Observe that `lab13test.sh` does NOT appear — run-parts skips it because of the `.sh` extension.

#### Step 3.3 — Rename the script to fix it

```bash
sudo mv /etc/cron.daily/lab13test.sh /etc/cron.daily/lab13test
sudo run-parts --test /etc/cron.daily/
```

Now `lab13test` appears in the list. Run it manually to confirm it works:

```bash
sudo run-parts --verbose /etc/cron.daily/ --regex '^lab13test$'
cat /tmp/cron_daily_test.log
```

---

### Part 4 — One-Time Scheduling with at (15 points)

#### Step 4.1 — Install and verify atd

```bash
sudo apt install -y at
sudo systemctl enable --now atd
systemctl status atd
```

#### Step 4.2 — Schedule a one-time job

```bash
echo "echo 'at job executed at $(date)' >> /tmp/at_test.log" | at now + 1 minute
```

#### Step 4.3 — List and inspect the at queue

```bash
atq
```

Note the job number. Inspect the full job:

```bash
at -c $(atq | awk '{print $1}')
```

This shows the environment variables and command that will run.

#### Step 4.4 — Wait and verify execution

Wait 90 seconds, then check:

```bash
cat /tmp/at_test.log
atq
```

The job should have run (log entry present) and the queue should be empty.

#### Step 4.5 — Schedule and cancel a job

```bash
echo "echo 'this should not run' >> /tmp/at_cancel.log" | at now + 10 minutes
atq
```

Record the job number, then cancel it:

```bash
atrm JOB_NUMBER    # replace JOB_NUMBER with the actual number from atq
atq
```

Confirm the queue is empty. Verify `/tmp/at_cancel.log` does not exist after 10 minutes.

---

### Part 5 — systemd Timer (20 points)

#### Step 5.1 — Create the service unit

```bash
sudo tee /etc/systemd/system/lab13-timer-demo.service > /dev/null << 'EOF'
[Unit]
Description=Lab 13 Timer Demo Service

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo "systemd timer fired at $(date)" >> /tmp/timer_demo.log'
EOF
```

#### Step 5.2 — Create the timer unit

```bash
sudo tee /etc/systemd/system/lab13-timer-demo.timer > /dev/null << 'EOF'
[Unit]
Description=Lab 13 Timer Demo - runs every 2 minutes

[Timer]
OnCalendar=*:0/2
Persistent=true

[Install]
WantedBy=timers.target
EOF
```

`OnCalendar=*:0/2` means every 2 minutes at the top and bottom of each hour (:00, :02, :04, ...).

#### Step 5.3 — Enable and start the timer

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now lab13-timer-demo.timer
systemctl status lab13-timer-demo.timer
```

Check when the timer will next fire:

```bash
systemctl list-timers | grep lab13
```

#### Step 5.4 — Verify execution

Wait 3 minutes, then check:

```bash
cat /tmp/timer_demo.log
journalctl -u lab13-timer-demo.service -n 10
```

You should see entries in both the log file and the journal.

---

### Part 6 — Cron Troubleshooting (15 points)

#### Step 6.1 — Create a failing cron job (PATH issue)

Add this entry to your crontab:

```bash
crontab -e
```

Add:

```text
# This will silently fail - uses a command not in cron's PATH
* * * * * datestamp >> /tmp/cron_broken.log 2>&1
```

Wait 2 minutes, then check:

```bash
cat /tmp/cron_broken.log
```

You should see a "command not found" error — `datestamp` is not a real command, but this demonstrates that even real commands not in cron's minimal PATH fail with the same error.

#### Step 6.2 — Diagnose and fix with full paths

Now update the entry to use an absolute path:

```bash
crontab -e
```

Replace the broken entry with:

```text
* * * * * /bin/date >> /tmp/cron_fixed.log 2>&1
```

Wait 2 minutes:

```bash
cat /tmp/cron_fixed.log
```

This time it works because `/bin/date` is an absolute path that does not depend on PATH.

#### Step 6.3 — Clean up test entries

```bash
crontab -r
crontab -l
```

Confirm the crontab is now empty.

---

### Analysis Questions

Answer these questions in writing after completing the lab. Submit with your lab screenshots.

1. You need a script to run at 2:30 AM on the first day of each month, but only in January, April, July, and October. Write the complete crontab entry.

2. A junior administrator placed `backup.sh` in `/etc/cron.daily/` and gave it execute permission. The script never runs. Explain two separate reasons this could fail and the specific fix for each.

3. What is the key difference between `cron` and `at` for scheduling purposes? Give a real-world example where `at` is the correct choice and one where cron is the correct choice.

4. Explain why `Persistent=true` in a systemd timer is useful for a server that has scheduled maintenance windows. What does the timer do at the next boot after a maintenance window that included a downtime period?

5. A developer's crontab entry runs successfully when they test the script manually in their shell, but fails silently when run by cron. List three possible causes and explain how to resolve each one.

---

### Submission Requirements

* Screenshots of each Part completion (terminal output visible)
* Written answers to all 5 analysis questions
* Include the output of `crontab -l` for Part 2 showing all four time entries

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Part 1: crontab basics and cron log verification | 15 |
| Part 2: time specification entries and interpretation | 20 |
| Part 3: run-parts naming rules demonstrated | 15 |
| Part 4: at job created, inspected, and cancelled | 15 |
| Part 5: systemd timer created and verified | 20 |
| Part 6: PATH troubleshooting demonstrated | 15 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Scheduled Disk Space Alert
Create a cron job and supporting script that monitors disk usage and alerts when a threshold is exceeded:
1. Write a script `/usr/local/bin/disk_alert.sh` that checks the usage percentage of the root filesystem (`df /` parsed with `awk`) and appends a warning line to `/var/log/disk_alert.log` if usage exceeds 80%.
2. Add a crontab entry to run the script every 15 minutes using step syntax.
3. Manually trigger the script and confirm the log file is written correctly.
4. Use `grep CRON /var/log/syslog` to confirm cron records the execution after the next 15-minute mark.

### Challenge 2: systemd Timer with Dependency Guard
Extend the systemd timer from Part 5 to add a dependency check before the main task runs:
1. Modify the `lab13-timer-demo.service` unit to include a `ConditionPathExists=/tmp/timer_enabled` check in the `[Unit]` section — the service should only run when that file exists.
2. Create `/tmp/timer_enabled` and verify the timer fires on the next cycle and writes to `/tmp/timer_demo.log`.
3. Remove `/tmp/timer_enabled` and confirm the timer skips execution on the following cycle (check `journalctl -u lab13-timer-demo.service -n 5` for the condition skip message).
4. Run `systemd-analyze calendar "*:0/2"` to validate the OnCalendar expression and note the next scheduled time shown in the output.

### Reflection Questions
1. A script runs perfectly when executed manually as root but produces no output and no error when run by cron at the same schedule. List three distinct root causes and the specific diagnostic step to confirm each one.
2. Your organization runs application servers that are rebooted for patching every Sunday night. A daily database backup cron job is scheduled at 2 AM every day. Should you use cron, anacron, or a systemd timer with `Persistent=true` for this backup job, and why? What would happen to the Sunday-night backup under each approach?

---

### Cleanup

```bash
# Remove crontab if not already done
crontab -r 2>/dev/null

# Remove systemd timer units
sudo systemctl disable --now lab13-timer-demo.timer 2>/dev/null
sudo rm -f /etc/systemd/system/lab13-timer-demo.{service,timer}
sudo systemctl daemon-reload

# Remove system cron script
sudo rm -f /etc/cron.daily/lab13test

# Remove test log files
rm -f /tmp/cron_test.log /tmp/cron_times.log /tmp/cron_daily_test.log
rm -f /tmp/at_test.log /tmp/timer_demo.log /tmp/cron_broken.log /tmp/cron_fixed.log
echo "Lab 13 cleanup complete"
```
