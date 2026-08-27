# Lab: Module 12 — System Services and Daemons

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Lab Overview

**Estimated Time:** 60–75 minutes

**Environment:** Linux VM (Rocky Linux 9 or Ubuntu 22.04). Root or sudo access required.

**Objectives:**

- Use `systemctl` for full service lifecycle management
- Create and test a custom systemd service unit
- Query the systemd journal with multiple filters using `journalctl`
- Write and verify crontab entries
- Schedule a one-time job using `at`

---

### Lab Environment Setup

Verify systemd is running as PID 1:

```bash
ps -p 1 -o comm=
systemctl --version
```

Record the systemd version number.

---

### Part 1: Service Management with systemctl

**Task 1.1 — Inspect a Running Service**

If your system has `sshd` running, use it for this task. Otherwise use any running service from `systemctl list-units --type=service`.

```bash
systemctl status sshd
```

From the output, record:

- Is the service active?
- What is the main process PID?
- Is it enabled (starts at boot)?
- What are the last 3 log lines shown?

**Task 1.2 — Restart and Reload**

Restart the SSH service:

```bash
sudo systemctl restart sshd
systemctl status sshd
```

Note the new PID (it should be different). Now check if reload is supported:

```bash
systemctl show sshd | grep ExecReload
```

If it has an ExecReload command, test it:

```bash
sudo systemctl reload sshd
systemctl status sshd
```

Note that the PID does NOT change on reload.

**Task 1.3 — Enable/Disable**

Check if sshd is currently enabled:

```bash
systemctl is-enabled sshd
```

Disable it (this does not stop the running service):

```bash
sudo systemctl disable sshd
systemctl is-enabled sshd
systemctl is-active sshd
```

Confirm: disabled means it won't start at boot, but it is still running now.

Re-enable it:

```bash
sudo systemctl enable sshd
systemctl is-enabled sshd
```

**Task 1.4 — Listing Units**

```bash
systemctl list-units --type=service --state=running
systemctl --failed
```

Record:

- How many services are currently running?
- Are there any failed units? If so, what are they?

---

### Part 2: Creating a Custom Service Unit

**Task 2.1 — Create a Simple Script**

Create a script that the service will run:

```bash
sudo mkdir -p /opt/labservice
sudo bash -c 'cat > /opt/labservice/run.sh << '"'"'EOF'"'"'
#!/bin/bash
while true; do
  echo "$(date): Lab service is running" >> /var/log/labservice.log
  sleep 30
done
EOF'
sudo chmod +x /opt/labservice/run.sh
```

**Task 2.2 — Create the Unit File**

```bash
sudo bash -c 'cat > /etc/systemd/system/labservice.service << '"'"'EOF'"'"'
[Unit]
Description=CIS-3325 Lab Service
After=network.target

[Service]
Type=simple
ExecStart=/opt/labservice/run.sh
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF'
```

Reload the systemd daemon to recognize the new unit:

```bash
sudo systemctl daemon-reload
```

**Task 2.3 — Start and Verify**

```bash
sudo systemctl start labservice
systemctl status labservice
```

Verify the service is running. Wait 35 seconds, then check the log:

```bash
cat /var/log/labservice.log
```

You should see at least one entry.

**Task 2.4 — Enable at Boot**

```bash
sudo systemctl enable labservice
systemctl is-enabled labservice
```

Verify the symlink was created:

```bash
ls -la /etc/systemd/system/multi-user.target.wants/labservice.service
```

**Task 2.5 — Create a Drop-in Override**

Use `systemctl edit` to add a description change without modifying the original file:

```bash
sudo systemctl edit labservice
```

In the editor, add:

```ini
[Unit]
Description=CIS-3325 Lab Service (Override Active)
```

Save and close. Reload and verify:

```bash
sudo systemctl daemon-reload
systemctl show labservice | grep "^Description="
```

The override description should appear.

**Task 2.6 — Cleanup**

Stop and disable the service, then remove the files:

```bash
sudo systemctl disable --now labservice
sudo rm /etc/systemd/system/labservice.service
sudo rm -rf /etc/systemd/system/labservice.service.d/
sudo systemctl daemon-reload
sudo rm -rf /opt/labservice
sudo rm -f /var/log/labservice.log
```

---

### Part 3: journalctl Log Analysis

**Task 3.1 — Basic Journal Queries**

```bash
journalctl -n 20
journalctl -r -n 10
```

What are the timestamps on the most recent 10 entries?

**Task 3.2 — Filter by Unit**

```bash
journalctl -u sshd --since "1 hour ago"
journalctl -u sshd -n 20
```

How many SSH-related entries exist in the last hour?

**Task 3.3 — Filter by Priority**

```bash
journalctl -p err -n 20
journalctl -p warning..err --since today
```

Are there any errors or warnings in the journal today? Record what they are.

**Task 3.4 — Boot-based Queries**

```bash
journalctl --list-boots
journalctl -b -n 30
```

How many boots are recorded? What is the boot ID of the current session?

**Task 3.5 — Kernel Messages**

```bash
journalctl -k -n 20
```

What messages appear in the most recent kernel log entries?

**Task 3.6 — Time-bounded Query**

Run the following — adjust the date to today's date:

```bash
journalctl --since "$(date '+%Y-%m-%d') 00:00:00" --until "$(date '+%Y-%m-%d') 01:00:00"
```

How many journal entries were recorded in the first hour of today?

**Task 3.7 — Journal Disk Usage**

```bash
journalctl --disk-usage
```

How much disk space is the journal currently using?

---

### Part 4: cron Scheduling

**Task 4.1 — Verify crond is Running**

```bash
systemctl status crond 2>/dev/null || systemctl status cron 2>/dev/null
```

(The service is named `crond` on RHEL-based and `cron` on Debian-based systems.)

**Task 4.2 — Create a Crontab Entry**

Open your user crontab:

```bash
crontab -e
```

Add the following entry (replace the path with your actual home directory):

```
*/2 * * * * echo "Cron test: $(date)" >> /tmp/cron_test.log
```

Save and exit. Verify it was saved:

```bash
crontab -l
```

Wait 2–3 minutes, then check:

```bash
cat /tmp/cron_test.log
```

You should see entries from cron. The timestamps should be approximately 2 minutes apart.

**Task 4.3 — Add Multiple Entries**

Edit the crontab again and add a second entry:

```
0 * * * * echo "Hourly marker: $(date)" >> /tmp/cron_test.log
```

Verify both entries are saved:

```bash
crontab -l
```

**Task 4.4 — Check cron Logs**

```bash
journalctl -u crond --since "30 minutes ago" 2>/dev/null || \
journalctl -u cron --since "30 minutes ago"
```

You should see entries showing your cron jobs executing.

**Task 4.5 — Cleanup**

Remove the cron entries:

```bash
crontab -r
crontab -l 2>&1
```

Confirm the crontab is empty. Remove the test log:

```bash
rm -f /tmp/cron_test.log
```

---

### Part 5: at — One-Time Scheduling

**Task 5.1 — Verify atd is Running**

```bash
systemctl status atd
```

If it is not running:

```bash
sudo systemctl enable --now atd
```

**Task 5.2 — Schedule a One-Time Job**

```bash
echo "echo 'at job ran at $(date)' >> /tmp/at_test.log" | at now + 1 minute
```

List the pending job:

```bash
atq
```

Record the job number. Wait 90 seconds, then check:

```bash
cat /tmp/at_test.log
```

**Task 5.3 — Schedule and Cancel a Job**

```bash
echo "echo 'This should be cancelled'" | at now + 10 minutes
atq
```

Record the job number, then remove it:

```bash
atrm <job-number>
atq
```

Confirm the job no longer appears.

**Task 5.4 — Cleanup**

```bash
rm -f /tmp/at_test.log
```

---

### Lab Submission Requirements

Submit a lab report in PDF format containing:

1. Answers to all recorded observations above
2. Screenshot or pasted output for each verification step
3. The contents of your custom `labservice.service` unit file
4. Brief explanation (2–3 sentences each) of the difference between:
   - `systemctl restart` vs `systemctl reload`
   - `systemctl enable` vs `systemctl start`
   - `cron` vs `at`

---

### Grading Rubric

| Section | Points |
|---------|--------|
| Part 1: systemctl service management | 20 |
| Part 2: Custom service unit creation | 30 |
| Part 3: journalctl queries | 20 |
| Part 4: cron scheduling and verification | 20 |
| Part 5: at scheduling | 5 |
| Written explanations | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Custom Systemd Service with Watchdog and Timer

Write a custom systemd service that runs a monitoring script, configure it to restart automatically on failure, and pair it with a timer for periodic execution.

1. Create a monitoring script at `/opt/diskmon.sh` that checks if any filesystem is more than 80% full and writes a timestamped warning to `/var/log/diskmon.log` if so: `df -h --output=target,pcent | tail -n +2 | while read mount pct; do PCT=${pct%%%}; if [ "$PCT" -gt 80 ]; then echo "$(date '+%Y-%m-%d %H:%M:%S') WARNING: $mount is ${pct} full" >> /var/log/diskmon.log; fi; done`. Make it executable: `sudo chmod +x /opt/diskmon.sh`. Test it manually first.
2. Create a systemd service unit at `/etc/systemd/system/diskmon.service` with `[Unit]` section including `Description=Disk Usage Monitor`, a `[Service]` section with `Type=oneshot`, `ExecStart=/opt/diskmon.sh`, `User=root`, and a `[Install]` section with `WantedBy=multi-user.target`. Run `sudo systemctl daemon-reload && sudo systemctl start diskmon` and verify with `sudo systemctl status diskmon` and `cat /var/log/diskmon.log`.
3. Create a paired timer unit at `/etc/systemd/system/diskmon.timer` with `[Unit]` description, a `[Timer]` section containing `OnBootSec=2min` (run 2 minutes after boot) and `OnCalendar=*:0/5` (every 5 minutes), and `[Install]` with `WantedBy=timers.target`. Enable and start the timer: `sudo systemctl daemon-reload && sudo systemctl enable --now diskmon.timer`. Verify with `sudo systemctl list-timers diskmon.timer`.
4. Test the recovery behavior: add `Restart=on-failure` and `RestartSec=5` to the `[Service]` section. Temporarily break the service by changing `ExecStart=/opt/nonexistent.sh`. Reload and restart: `sudo systemctl daemon-reload && sudo systemctl restart diskmon`. Watch it attempt recovery with `sudo journalctl -u diskmon -f`. Then restore the correct path and reload.

### Challenge 2: Journal Forensics and Service Failure Analysis

Use journalctl to perform a structured investigation of service behavior across multiple boot sessions and extract meaningful operational insights.

1. Query the journal to produce a boot history report: `sudo journalctl --list-boots`. Count the number of recorded boots. For each of the last 3 boots, extract the boot start time, kernel version, and first systemd message: `sudo journalctl -b -N --output=short-monotonic | head -3` (where N is the boot index -1, -2, -3).
2. Generate a report of all services that failed at any point during the current boot: `sudo systemctl --failed --no-legend`. For each failed unit listed, retrieve its last 20 journal lines: `sudo journalctl -u UNIT -b -n 20`. Document the likely cause of each failure.
3. Measure boot performance: `systemd-analyze` (total boot time), `systemd-analyze blame | head -10` (slowest units), and `systemd-analyze critical-chain` (the critical path through the boot). Identify the single unit contributing most to boot time and research whether it can be safely delayed with `systemctl edit --force UNIT` and a `[Unit]` section adding `After=` to defer it.
4. Write a one-liner that queries journalctl for all SSH authentication failures in the last 7 days and counts them by source IP: `sudo journalctl -u ssh --since "7 days ago" | grep "Failed password" | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -10`. Record the top offending IPs and research what `fail2ban` does to address this problem automatically.

### Reflection Questions

1. systemd's `Requires=` dependency is "strong" (if the required unit fails, this unit fails too) while `Wants=` is "weak" (failure of the wanted unit is tolerated). Describe a specific real-world service where using `Requires=network-online.target` instead of `Wants=network-online.target` would cause an unnecessary and difficult-to-diagnose outage, and explain the exact failure scenario.

2. `systemctl mask` creates a symlink to `/dev/null` to prevent a service from starting, while `systemctl disable` only removes the boot-time symlinks. Describe a scenario where an attacker who gains brief root access could exploit the difference between these two states — specifically, how an attacker might use a disabled-but-not-masked service to achieve persistence after their initial access vector is closed.
