# Discussion Forum: Module 12 - System Logging and Monitoring

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content.

---

### Scenario A - Investigating a Security Incident with Logs

A web server at your company received a large number of SSH login attempts overnight. The server
runs Ubuntu 22.04 with rsyslog and systemd-journald both active. You arrive in the morning and
need to reconstruct what happened between 1:00 AM and 4:00 AM.

1. Write the specific commands you would use to find failed SSH login attempts in the correct Ubuntu
   log file. Then write the journalctl command to retrieve all SSH-related journal entries from the
   1 AM to 4 AM window. Explain why both sources are available on this system simultaneously.
2. You find 8,000 failed login attempts from a single IP address. Write the commands you would use
   to count attempts by IP address and identify the top offenders. Explain what syslog facility
   and priority level SSH authentication failures are logged under, and how the logger command
   could be used to inject a test entry to verify your log routing is working.
3. After confirming the attack, you want to ensure logs from this incident are preserved for 90 days
   and that the journal will survive the next reboot. What two specific configuration steps would
   you take, and what journalctl command would you use to verify journal disk usage before and
   after making the journal persistent?

---

### Scenario B - Performance Degradation Investigation

A production database server is experiencing slowdowns that appear to follow a pattern: performance
degrades overnight and recovers during business hours. Users report that queries that normally take
2 seconds take 30+ seconds between midnight and 6 AM. You need to diagnose the cause using
performance monitoring tools.

1. Describe the three vmstat columns that would each point to a different root cause (CPU saturation,
   I/O bottleneck, and memory pressure/swapping). For each column, state the threshold that suggests
   a problem and the follow-up command you would use to get more detail on that specific issue.
2. The server's overnight batch jobs run between 2 AM and 5 AM. You were not present during the
   slow period. Explain how you would use sar to review what was happening at 3 AM last night.
   Write the specific sar command, identify the file it reads from, and explain what sar data
   collection must be enabled for this to work.
3. You run `free -h` during the slow period remotely and see: total=32G, used=31G, free=200M,
   buff/cache=2G, available=2.1G. You also see non-zero vmstat si and so values. What does this
   combination of evidence indicate? What is the immediate corrective action and the longer-term
   solution?

---

### Scenario C - logrotate Configuration for a New Application

Your team has deployed a new microservice called `inventoryd`. It writes logs to
`/var/log/inventoryd/app.log` and `/var/log/inventoryd/error.log`. The service writes approximately
500 MB of logs per day. The logs must be retained for 30 days for compliance, compressed to save
disk space, and the service must be signaled to reopen its log file handles after each rotation.
The service is reloaded with `systemctl reload inventoryd`.

1. Write the complete logrotate stanza for this application. Include: daily rotation, 30-day
   retention, compression with a one-cycle delay, handling for missing log files, a new log file
   created with permissions 0640 owned by the inventoryd user and adm group, and a postrotate
   block that signals the service. Explain the purpose of delaycompress in the context of an
   actively-writing service.
2. After deploying the configuration, you want to test it without actually rotating the logs yet,
   then force an immediate rotation to confirm it works. Write both commands. After forcing a
   rotation twice, list the files you expect to see in /var/log/inventoryd/ and explain the
   compression state of each.
3. Six months later, a compliance audit finds that log files from 35 days ago still exist on disk.
   Investigation reveals that logrotate ran but did not delete the old files as expected. What
   logrotate directive controls the number of retained files, what value should it be set to for
   30-day retention with daily rotation, and what does the `rotate N` value actually count? Also
   explain what happens to the oldest file on rotation N+1.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 12 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Logs are only useful if you look at them. Every production Linux system generates thousands of log
entries per day, and most administrators only open the logs when something has already gone wrong.
That is the wrong approach. Set aside ten minutes each week to scan your authentication logs for
unusual patterns, check your journal for err-and-above entries, and verify your logrotate
configurations are actually rotating. The first sign of a brewing problem — a disk filling with
logs, a service generating repeated errors, a user account generating unexpected sudo activity —
almost always shows up in the logs days before it becomes an outage. The tools in this module
(journalctl, logrotate, sar, vmstat) are not just for incident response. They are the instruments
on your dashboard. Learn to read them before you need them.
