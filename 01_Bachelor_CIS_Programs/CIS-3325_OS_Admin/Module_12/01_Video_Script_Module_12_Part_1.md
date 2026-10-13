# Video Script: Module 12 - System Logging and Monitoring (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 12. Logging is the memory of a Linux system. When something goes wrong —
a service crashes, a security breach occurs, a user makes an unauthorized change — the logs
are how you find out what happened and when. In this module we cover the two logging
architectures on modern Linux (rsyslog and systemd journal), the key log files and their
locations, and log rotation with logrotate. In Part 2 we cover performance monitoring with
vmstat, top, iostat, and free.

---

### Section 1: Logging Architecture Overview

Traditional Linux logging used the syslog protocol: applications send messages to a syslog
daemon (like rsyslog or syslog-ng), which routes them to log files based on facility and
priority.

Modern Linux uses systemd-journald: the journal daemon collects messages from all systemd
services, the kernel, and applications. Messages are stored in a binary format.

On most modern distributions, both are running simultaneously: journald captures everything,
and rsyslog can receive a forwarded copy to write traditional text log files.

[SHOW TERMINAL]

```bash
systemctl status rsyslog
systemctl status systemd-journald
```

Both should be active on a typical Ubuntu or RHEL system.

---

### Section 2: Key Log Files

[SHOW TERMINAL]

```bash
ls -lh /var/log/
```

Important log files by location:

| File | Distro | Contents |
|------|--------|---------|
| /var/log/syslog | Ubuntu/Debian | General system messages |
| /var/log/messages | RHEL/CentOS | General system messages |
| /var/log/auth.log | Ubuntu/Debian | Authentication events, sudo, SSH |
| /var/log/secure | RHEL/CentOS | Authentication events |
| /var/log/kern.log | Ubuntu | Kernel messages |
| /var/log/dmesg | All | Boot-time hardware and driver messages |
| /var/log/dpkg.log | Ubuntu | Package install/remove history |
| /var/log/apt/history.log | Ubuntu | apt transaction history |
| /var/log/nginx/access.log | All (nginx) | HTTP requests |
| /var/log/nginx/error.log | All (nginx) | Nginx errors |
| /var/log/audit/audit.log | RHEL (auditd) | SELinux and audit events |

```bash
sudo tail -f /var/log/syslog
```

Follow the syslog in real time. Very useful during troubleshooting — reproduce the problem
and watch what gets logged.

```bash
sudo tail -20 /var/log/auth.log
```

Recent authentication events. Look here for failed login attempts, sudo usage.

```bash
sudo grep "Failed password" /var/log/auth.log | tail -10
```

Find failed SSH login attempts. On a public-facing server, you will likely see many of these.

---

### Section 3: syslog Priority and Facility

[SHOW TERMINAL]

syslog messages have two classifications:

Facility: the type of program that generated the message (kern, auth, mail, daemon, user, etc.)

Priority (severity, from highest to lowest):
0 = emerg (system is unusable)
1 = alert (action must be taken immediately)
2 = crit (critical conditions)
3 = err (error conditions)
4 = warning (warning conditions)
5 = notice (normal but significant)
6 = info (informational)
7 = debug (debug-level messages)

The rsyslog configuration in /etc/rsyslog.conf uses facility.priority selectors to route
messages to destinations.

```bash
sudo logger -p auth.warning "Lab test message from logger"
sudo grep "Lab test" /var/log/auth.log
```

logger manually injects a message into the syslog system with a specified facility.priority.
Useful for testing log routing or adding custom messages from scripts.

---

### Section 4: journalctl

[SHOW TERMINAL]

```bash
journalctl
```

Shows all journal entries from all time. Pipe to less (default behavior) for navigation.

```bash
journalctl -b
```

Current boot only. This is the most common starting point.

```bash
journalctl -b -1
```

Previous boot. -b -2 is the boot before that.

```bash
journalctl -u sshd
```

All entries for the sshd unit.

```bash
journalctl -u sshd -b
```

sshd entries for this boot.

```bash
journalctl -u sshd -f
```

Follow sshd entries in real time.

```bash
journalctl -p err -b
```

Error priority and higher, current boot.

```bash
journalctl --since "2026-01-01" --until "2026-01-02"
```

Entries in a date range.

```bash
journalctl --since "1 hour ago"
```

Entries from the last hour.

```bash
journalctl -n 50
```

Last 50 entries.

```bash
journalctl --disk-usage
```

Total space used by the journal.

---

### Section 5: Journal Persistence

[SHOW TERMINAL]

By default on many systems, the journal is stored in volatile memory at /run/log/journal/
and is lost on reboot. To make it persistent:

```bash
sudo mkdir -p /var/log/journal/
sudo systemctl restart systemd-journald
```

After creating /var/log/journal/, the daemon switches to storing entries there. Now
journalctl -b -1 will show the previous boot.

Journal configuration is in /etc/systemd/journald.conf. Key settings:

```
Storage=persistent     # store on disk
SystemMaxUse=500M      # maximum journal disk usage
SystemKeepFree=20%     # keep this much disk free
MaxRetentionSec=1month # delete entries older than this
```

```bash
sudo journalctl --vacuum-time=30d
```

Remove journal entries older than 30 days.

```bash
sudo journalctl --vacuum-size=500M
```

Remove old journal entries until total size is under 500 MB.

---

### Section 6: logrotate

[SHOW TERMINAL]

Log files grow indefinitely without rotation. logrotate compresses, renames, and deletes
old log files on a schedule.

```bash
cat /etc/logrotate.conf
```

Global logrotate configuration.

```bash
ls /etc/logrotate.d/
```

Per-application rotation rules. Each file defines how a specific application's logs are rotated.

```bash
cat /etc/logrotate.d/nginx
```

Example nginx rotation: daily, keep 14 days, compress.

A typical logrotate stanza:

```
/var/log/nginx/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        nginx -s reopen
    endscript
}
```

Key directives:
- daily/weekly/monthly: rotation frequency
- rotate N: keep N old files
- compress: gzip old files
- delaycompress: wait one rotation before compressing (for actively written files)
- missingok: do not error if the log file is missing
- create PERM USER GROUP: create a new empty log file with these permissions
- postrotate/endscript: run commands after rotation (to signal the application to reopen log files)

```bash
sudo logrotate -f /etc/logrotate.d/nginx
```

Force an immediate rotation. Useful for testing your logrotate configuration.

---

### Certification Connection

Logging maps to Linux+ Domain 3.0 (Troubleshooting). Key exam objectives:

Know the log file locations for authentication, system messages, and kernel messages on
both Ubuntu (/var/log/auth.log) and RHEL (/var/log/secure).

Know journalctl flags: -u (unit), -b (boot), -f (follow), -p (priority), -n (lines),
--since, --until.

Know how to make the journal persistent: create /var/log/journal/.

Know logrotate directives: rotate N, daily/weekly, compress, postrotate.

---

### Transition to Part 2

In Part 2 we cover performance monitoring tools: vmstat, free, iostat, top, sar, and
uptime. These complement logging by showing the current resource state.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
