# Lab Activity: Module 12 - System Logging and Monitoring

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Time:** 75 minutes
**Points:** 100

---

### Objectives

By the end of this lab you will be able to:

- Locate and read the correct log files for authentication and system events
- Use journalctl to filter journal entries by unit, boot, priority, and time range
- Enable journal persistence across reboots
- Vacuum journal entries by time and size
- Configure logrotate for a custom application log
- Use vmstat, free, and iostat to identify CPU, memory, and I/O bottlenecks
- Use sar to review historical system performance data

---

### Prerequisites

- Ubuntu 22.04 LTS virtual machine with sudo access
- rsyslog and systemd-journald both running (default on Ubuntu 22.04)
- sysstat package installed: `sudo apt install -y sysstat`
- Internet connectivity for package installation

---

### Part 1 — Log File Exploration (15 points)

#### Step 1.1 — Locate key log files

```bash
ls -lh /var/log/
```

Note the sizes of syslog, auth.log, and kern.log.

```bash
sudo tail -20 /var/log/syslog
```

Observe the format: timestamp, hostname, process name, PID, and message.

```bash
sudo tail -20 /var/log/auth.log
```

Look for SSH, sudo, and PAM entries.

#### Step 1.2 — Search for specific events

```bash
sudo grep "sudo" /var/log/auth.log | tail -10
```

This shows recent sudo usage. Every sudo command is logged here.

```bash
sudo grep "Failed password" /var/log/auth.log | wc -l
```

Count failed SSH login attempts. On a VM this should be a small number.

#### Step 1.3 — Follow a log in real time

Open a second terminal window and run:

```bash
sudo tail -f /var/log/auth.log
```

In the first terminal, run a sudo command:

```bash
sudo ls /root
```

Watch the auth.log entry appear in the second terminal. Press Ctrl+C to stop following.

#### Step 1.4 — Inject a test log message with logger

```bash
sudo logger -p auth.warning "Lab12 test message from logger"
sudo grep "Lab12" /var/log/auth.log
```

Verify the message appears with the correct facility and timestamp.

---

### Part 2 — journalctl Filtering (20 points)

#### Step 2.1 — Basic journal navigation

```bash
journalctl -b
```

Press G to jump to the end, then q to quit. This is the current boot journal.

```bash
journalctl -b -n 30
```

Last 30 entries from this boot.

#### Step 2.2 — Filter by unit

```bash
journalctl -u ssh -b
```

All sshd entries for the current boot. (Ubuntu uses the unit name `ssh`, not `sshd`.)

```bash
journalctl -u ssh -b -n 20
```

Last 20 entries for the ssh unit.

#### Step 2.3 — Filter by priority

```bash
journalctl -b -p err
```

Error-level and above from the current boot. The `-p err` flag sets a floor at priority 3 — you will see err (3), crit (2), alert (1), and emerg (0).

```bash
journalctl -b -p warning
```

Warning and above (priorities 0-4).

#### Step 2.4 — Filter by time

```bash
journalctl --since "1 hour ago"
```

Entries from the last hour.

```bash
journalctl --since "$(date +%Y-%m-%d) 00:00:00" --until "$(date +%Y-%m-%d) 00:05:00"
```

Entries from the first 5 minutes of today. (Likely empty on a VM that booted later.)

#### Step 2.5 — Combine filters

```bash
journalctl -u ssh -b -p warning
```

SSH entries at warning priority or above, current boot.

```bash
journalctl -u cron -b -n 10 2>/dev/null || journalctl -u cron.service -b -n 10
```

Recent cron entries. (The unit may be named cron or cron.service depending on the system.)

---

### Part 3 — Journal Disk Usage and Vacuuming (10 points)

#### Step 3.1 — Check journal disk usage

```bash
journalctl --disk-usage
```

Record the current journal size.

#### Step 3.2 — Simulate journal vacuuming

```bash
sudo journalctl --vacuum-time=90d
```

Remove entries older than 90 days. On a recently installed VM this will likely report that nothing was removed.

```bash
sudo journalctl --vacuum-size=200M
```

Trim the journal to 200 MB maximum. Again, likely a no-op on a small VM.

```bash
journalctl --disk-usage
```

Confirm the size after vacuuming.

---

### Part 4 — Journal Persistence (15 points)

#### Step 4.1 — Check current journal storage location

```bash
ls /run/log/journal/ 2>/dev/null && echo "Volatile storage found" || echo "No volatile journal"
ls /var/log/journal/ 2>/dev/null && echo "Persistent storage found" || echo "No persistent journal yet"
```

Determine where the journal is currently stored.

#### Step 4.2 — Enable persistent storage

```bash
sudo mkdir -p /var/log/journal/
sudo systemctl restart systemd-journald
```

#### Step 4.3 — Verify persistence is active

```bash
ls /var/log/journal/
journalctl --disk-usage
```

You should now see a machine ID directory under /var/log/journal/.

#### Step 4.4 — View journald configuration

```bash
cat /etc/systemd/journald.conf
```

Locate the `[Journal]` section. Note the commented-out directives including Storage, SystemMaxUse, and MaxRetentionSec.

---

### Part 5 — logrotate Configuration (15 points)

#### Step 5.1 — Explore existing logrotate configuration

```bash
cat /etc/logrotate.conf
```

Note the global defaults: weekly, rotate 4, compress.

```bash
ls /etc/logrotate.d/
cat /etc/logrotate.d/rsyslog
```

Examine the rsyslog rotation configuration.

#### Step 5.2 — Create a test application log and rotation config

Create a simulated application log:

```bash
sudo mkdir -p /var/log/lab12app
sudo touch /var/log/lab12app/app.log
sudo bash -c 'for i in $(seq 1 100); do echo "$(date) INFO Request $i processed successfully" >> /var/log/lab12app/app.log; done'
wc -l /var/log/lab12app/app.log
```

Create a logrotate configuration:

```bash
sudo tee /etc/logrotate.d/lab12app > /dev/null << 'EOF'
/var/log/lab12app/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 0644 root root
}
EOF
```

#### Step 5.3 — Test and force logrotate

```bash
sudo logrotate -d /etc/logrotate.d/lab12app
```

Debug mode: shows what would happen without making changes. Note the "rotating pattern" and "considering log" output.

```bash
sudo logrotate -f /etc/logrotate.d/lab12app
ls -lh /var/log/lab12app/
```

Force an immediate rotation. You should see app.log (new empty file) and app.log.1 (rotated copy, not yet compressed because of delaycompress).

```bash
sudo logrotate -f /etc/logrotate.d/lab12app
ls -lh /var/log/lab12app/
```

Force a second rotation. Now you should see app.log.1 and app.log.2.gz (the first rotation is now compressed).

---

### Part 6 — Memory and CPU Monitoring with vmstat and free (15 points)

#### Step 6.1 — Memory status with free

```bash
free -h
```

Identify the available column. This is the memory available for new processes (free + reclaimable cache).

```bash
free -h -s 2
```

Watch for 5 updates (Ctrl+C to stop). On an idle VM the numbers should be stable.

#### Step 6.2 — System overview with vmstat

```bash
vmstat 1 5
```

Ignore the first row (boot average). Focus on rows 2-5.

Record the values from your output:

| Metric | Your Value | What it means |
|--------|-----------|----------------|
| r (run queue) | | Processes waiting for CPU |
| wa (I/O wait) | | % time waiting for disk I/O |
| si (swap-in) | | Pages read from swap per sec |
| so (swap-out) | | Pages written to swap per sec |
| id (idle) | | % CPU idle |

#### Step 6.3 — Simulate CPU load and observe vmstat

Open a second terminal and start a CPU stress loop:

```bash
# Terminal 2 — run for 15 seconds
timeout 15 bash -c 'while true; do :; done' &
echo "Stress PID: $!"
```

In the first terminal, run vmstat and observe the change in `us` (user CPU) and drop in `id` (idle):

```bash
vmstat 1 10
```

After the 15-second loop exits, run vmstat again and confirm idle recovers.

---

### Part 7 — Disk I/O Monitoring with iostat and sar (10 points)

#### Step 7.1 — Basic iostat

```bash
iostat
```

The first section shows CPU averages since boot. The second shows device statistics.

```bash
iostat -x 1 3
```

Extended output, 3 samples. Key columns: `%util` (device utilization) and `await` (average I/O wait time in ms).

On an idle VM, %util should be near 0 and await should be a low number.

#### Step 7.2 — Historical data with sar

```bash
sar -u 1 5
```

CPU utilization, 5 samples at 1-second intervals. Compare %idle to the vmstat id column.

```bash
sar -r 1 5
```

Memory utilization. Note %memused.

```bash
sar -d 1 3
```

Disk I/O statistics.

#### Step 7.3 — View historical sar data

```bash
sar -u -f /var/log/sysstat/sa$(date +%d) 2>/dev/null || echo "No historical sar data yet (sysstat collection may not be configured)"
```

On Ubuntu, sysstat collection may need to be enabled:

```bash
sudo sed -i 's/ENABLED="false"/ENABLED="true"/' /etc/default/sysstat 2>/dev/null
sudo systemctl restart sysstat 2>/dev/null
echo "sysstat enabled — historical data will be available after the next collection interval"
```

---

### Analysis Questions

Answer these questions in writing after completing the lab. Submit with your lab screenshots.

1. Your server uses Ubuntu 22.04. A security auditor asks for all failed SSH login attempts from the past 30 days. Name the specific log file to check and write the exact grep command you would use to extract the failed attempts.

2. You run `journalctl -b -p err` and see 12 entries. You run `journalctl -b -p warning` and see 47 entries. Explain why the second command shows more results than the first, referencing the syslog priority number system.

3. After adding `rotate 7` to a logrotate stanza and running logrotate 10 times, how many rotated files will exist on disk? Explain what happens on the 8th rotation.

4. You run `vmstat 1 5` and observe: r=8, wa=2, si=0, so=0, id=5, us=87. The system has 4 CPU cores. What is the most likely performance bottleneck? What command would you run next to identify which processes are responsible?

5. A user reports the server was slow between 2:00 AM and 3:00 AM last night. You were asleep. Which tool would you use to investigate, and what specific command would you run to view CPU utilization from that time window? What file would it read the data from?

---

### Submission Requirements

- Screenshots of each Part completion (terminal output visible)
- Written answers to all 5 analysis questions
- Save your /etc/logrotate.d/lab12app configuration file content in your submission

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Part 1: Log file exploration and logger injection | 15 |
| Part 2: journalctl filtering (unit, priority, time) | 20 |
| Part 3: Journal disk usage and vacuum | 10 |
| Part 4: Journal persistence enabled correctly | 15 |
| Part 5: logrotate config created and tested | 15 |
| Part 6: vmstat and free output interpreted | 15 |
| Part 7: iostat and sar commands executed | 10 |
| **Total** | **100** |

---

### Cleanup

```bash
# Remove the test logrotate config and log directory
sudo rm -f /etc/logrotate.d/lab12app
sudo rm -rf /var/log/lab12app/
echo "Lab 12 cleanup complete"
```
