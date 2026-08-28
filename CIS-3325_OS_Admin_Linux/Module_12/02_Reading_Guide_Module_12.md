# Reading Guide: Module 12 — System Services and Daemons

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This guide accompanies the Module 12 video lectures on systemd, journalctl, and job scheduling. Estimated reading and review time: 90 minutes.

---

### Learning Objectives

After completing this module, you will be able to:

- Describe the systemd architecture and explain why it replaced SysVinit
- Use `systemctl` to manage service lifecycle: start, stop, restart, reload, enable, disable, mask
- Read and write systemd unit files with correct `[Unit]`, `[Service]`, and `[Install]` sections
- Map systemd targets to their legacy runlevel equivalents
- Use `journalctl` to query logs by unit, time range, priority, boot session, and process
- Write crontab entries using correct five-field syntax
- Schedule one-time tasks using `at`
- Understand the relationship between systemd timers and cron

---

### Key Terms

**Daemon**
A background process that runs continuously and waits for events or requests. Daemons typically do not have a controlling terminal and have names ending in `d` (e.g., `sshd`, `httpd`, `crond`).

**Unit File**
An INI-style configuration file that describes a systemd resource. Located in `/lib/systemd/system/` (package) or `/etc/systemd/system/` (admin).

**Target**
A special unit type that groups other units and defines system states (equivalent to runlevels).

**Journal**
The binary, structured log database maintained by `systemd-journald`. Stores metadata alongside message text, enabling powerful filtering.

**Drop-in Override**
A partial unit file in a directory named `<unit-name>.d/` that overrides specific directives without replacing the entire unit file.

**Dependency**
A relationship between units. `Requires` is a hard dependency; `Wants` is a soft dependency. `After` and `Before` control ordering without implying dependency.

**crontab**
A file containing cron job definitions. Each user has their own; the system also has `/etc/crontab`.

---

### Section 1: systemd Architecture Deep Dive

**PID 1 and the Process Tree**

systemd is always PID 1. Every process on the system is a descendant of systemd, organized into cgroups (control groups). To see the process tree:

```bash
systemd-cgls
```

To see resource usage per cgroup:

```bash
systemd-cgtop
```

**Unit Loading Sequence**

When systemd starts, it:

1. Reads the default target (e.g., `multi-user.target`)
2. Resolves all dependencies recursively
3. Starts units in dependency order, parallelizing where possible
4. Reports failure if required dependencies fail

**Activation Types**

systemd supports several activation models beyond simple start-on-boot:

- **Socket activation**: systemd creates the socket; the service starts only when the first connection arrives. This speeds boot by deferring service startup.
- **Path activation**: a service starts when a file or directory is created or modified
- **Timer activation**: equivalent to cron, but integrated with the journal
- **D-Bus activation**: a service starts when its D-Bus name is requested

Understanding socket activation explains why some services appear ready before they are fully started.

---

### Section 2: systemctl Reference

**Service States**

A service can be in one of several states:

| State | Meaning |
|-------|---------|
| `active (running)` | Process is running |
| `active (exited)` | Oneshot service completed successfully |
| `active (waiting)` | Waiting for an event |
| `inactive` | Not running |
| `failed` | Process exited with error or was killed |
| `activating` | Starting up |
| `deactivating` | Shutting down |

**Enable vs. Start**

This is a common point of confusion:

- `systemctl start` — starts the service NOW, has no effect on boot behavior
- `systemctl enable` — configures the service to start AT BOOT, has no immediate effect
- `systemctl enable --now` — does both simultaneously

Always use `enable --now` when you want a service running now AND at boot.

**Override Files (Drop-ins)**

Instead of editing `/lib/systemd/system/` files directly (which get overwritten on package updates), create a drop-in override:

```bash
sudo systemctl edit nginx
```

This creates `/etc/systemd/system/nginx.service.d/override.conf`. Add only the directives you want to change:

```ini
[Service]
Restart=always
RestartSec=10
```

The drop-in file is merged with the base unit file, with override values taking precedence.

**Viewing All Unit Properties**

```bash
systemctl show nginx
```

This dumps every property in the unit, including computed values. Useful for debugging.

---

### Section 3: Unit File Writing Guide

**Minimal Service Unit**

The simplest possible service unit:

```ini
[Unit]
Description=My Simple Service

[Service]
ExecStart=/usr/bin/my-program

[Install]
WantedBy=multi-user.target
```

**Dependency Patterns**

For a web application that needs a database:

```ini
[Unit]
Description=Web Application
Requires=postgresql.service
After=postgresql.service network.target
```

For a service that should restart on failure:

```ini
[Service]
Restart=on-failure
RestartSec=5
StartLimitIntervalSec=60
StartLimitBurst=3
```

This restarts on failure, waits 5 seconds between attempts, and stops trying after 3 failures within 60 seconds.

**Security Hardening Directives**

systemd provides numerous sandboxing options for service units:

| Directive | Effect |
|-----------|--------|
| `NoNewPrivileges=yes` | Prevents privilege escalation |
| `PrivateTmp=yes` | Gives service a private `/tmp` |
| `ProtectHome=yes` | Makes home directories read-only |
| `ProtectSystem=full` | Makes system directories read-only |
| `ReadOnlyPaths=` | Specific paths are read-only |
| `ReadWritePaths=` | Only these paths are writable |
| `User=` | Run as specified non-root user |

---

### Section 4: journalctl Advanced Usage

**Structured Fields**

Every journal entry has a set of structured fields that can be used for filtering:

| Field | Description |
|-------|-------------|
| `_SYSTEMD_UNIT` | The systemd unit name |
| `_PID` | Process ID |
| `_UID` | User ID |
| `_GID` | Group ID |
| `_COMM` | Command name |
| `_EXE` | Executable path |
| `_HOSTNAME` | Hostname |
| `PRIORITY` | Syslog priority (0-7) |
| `MESSAGE` | The log message |
| `SYSLOG_IDENTIFIER` | syslog tag |

Combine multiple fields (AND logic):

```bash
journalctl _SYSTEMD_UNIT=nginx.service PRIORITY=3
```

**Cursor-Based Navigation**

For scripting, the `--cursor` option allows resuming from a specific journal position:

```bash
journalctl --after-cursor="s=..."
```

This is used by log shipping tools to avoid re-processing entries.

**Remote Journal**

`systemd-journal-remote` and `systemd-journal-upload` allow centralizing journal data from multiple hosts. This is covered in advanced systemd topics.

**Forwarding to syslog**

Even with the journal, many organizations still use centralized syslog (rsyslog, syslog-ng). Configure `/etc/systemd/journald.conf`:

```ini
[Journal]
ForwardToSyslog=yes
```

---

### Section 5: Cron Deep Dive

**The anacron Difference**

`cron` requires the system to be running at the scheduled time. If a daily job is scheduled at 2 AM but the laptop is off, the job is missed. `anacron` solves this for systems that are not always on — it runs missed jobs when the system next comes online.

Configuration: `/etc/anacrontab`

```
# period  delay  job-id    command
1         5      cron.daily  run-parts /etc/cron.daily
7         10     cron.weekly run-parts /etc/cron.weekly
```

**Crontab Special Strings**

Some cron implementations accept shorthand strings:

| String | Equivalent | Meaning |
|--------|-----------|---------|
| `@reboot` | — | Run once at startup |
| `@yearly` | `0 0 1 1 *` | Once a year |
| `@monthly` | `0 0 1 * *` | Once a month |
| `@weekly` | `0 0 * * 0` | Once a week |
| `@daily` | `0 0 * * *` | Once a day |
| `@hourly` | `0 * * * *` | Once an hour |

**Cron Security Considerations**

- Cron jobs run with the privileges of the owning user
- Root's crontab entries run as root — keep them minimal and audited
- Log cron activity: cron logs to `/var/log/cron` (RHEL) or `/var/log/syslog` (Debian)
- Consider using `MAILTO=""` to suppress email output (or set it to a monitored address)

**Debugging Cron**

If a cron job is not running:

1. Check cron daemon is running: `systemctl status crond`
2. Check cron logs: `journalctl -u crond` or `grep CRON /var/log/syslog`
3. Verify the crontab syntax: `crontab -l`
4. Test the command manually as the cron user with the cron environment
5. Check output redirection — if the command fails silently, add `2>&1` redirect

---

### Section 6: Job Scheduling Strategy

**When to Use Each Tool**

| Scenario | Tool |
|---------|------|
| Recurring task, always-on server | cron |
| Recurring task, sometimes-off system | anacron |
| One-time future task | at |
| Service-integrated scheduling | systemd timer |
| Scripted workflows with dependencies | systemd timer + service |

---

### Practice Review Questions

Answer these before taking the module quiz:

1. What is the difference between `systemctl stop` and `systemctl disable`?

2. A service is in `failed` state. What command shows you the most recent log output for that service?

3. In a unit file, what is the difference between `Requires=` and `Wants=`?

4. You need to add 5 environment variables to an existing package-installed service unit. What is the correct way to do this without modifying the package's unit file?

5. Explain the difference between the journal's runtime storage and persistent storage. How do you enable persistent storage?

6. Write a crontab entry that runs `/opt/backup.sh` every day at 3:15 AM.

7. What is the `at` command equivalent of "run this script in 90 minutes"?

8. A cron job works when run manually but fails when run by cron. What are three likely causes?

---

### Additional Resources

- systemd documentation: [systemd.io](https://systemd.io)
- `man systemctl` — complete reference
- `man 5 systemd.unit` — unit file format reference
- `man 5 systemd.service` — service unit directives
- `man journalctl` — log query reference
- `man 5 crontab` — crontab format reference
- Lennart Poettering's systemd blog series (Red Hat blog archives)

---

### Key Takeaways

- systemd is PID 1 on every modern Linux distribution. Master `systemctl` and `journalctl`.
- Always use `systemctl edit` for drop-in overrides rather than editing package unit files directly.
- `enable --now` is your go-to for deploying a new service (starts it and marks it for boot).
- `journalctl -u <service> -f` is your first debugging tool for any misbehaving service.
- Cron's five time fields (minute, hour, day-of-month, month, day-of-week) must be memorized for the Linux+ exam.
- Always use absolute paths and redirect output in cron jobs to avoid silent failures.

---

## 9. Supplemental Resources

**1. [systemd.service Man Page — man7.org](https://man7.org/linux/man-pages/man5/systemd.service.5.html)**
The authoritative reference for all directives available in service unit files. Covers `ExecStart`, `ExecStartPre`, `ExecStop`, `Restart`, `RestartSec`, `User`, `Group`, `WorkingDirectory`, `EnvironmentFile`, `StandardOutput`, `StandardError`, and all sandboxing/security directives. Bookmarking this page alongside `man 5 systemd.unit` gives you a complete unit file reference for writing production-quality service definitions.

**2. [How to Create a Systemd Service — DigitalOcean Community](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)**
A practical DigitalOcean tutorial covering the full lifecycle of systemd service management: writing unit files, enabling, starting, stopping, and masking services, reading status output, and using `systemctl edit` for drop-in overrides. The tutorial's worked examples reinforce the Module 12 lab scenarios and are available for both Ubuntu and CentOS/RHEL environments.

**3. [Understanding Cron — Crontab Guru](https://crontab.guru/)**
An interactive cron expression editor and validator. Enter any cron expression and it immediately shows the next scheduled run times in plain English. The site also includes a reference for all five time fields and a library of common expressions. Essential for verifying cron schedules before deploying them to production, and directly applicable to the cron scheduling tasks in the Module 12 lab.
