# Video Script: Module 12 — System Services and Daemons (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 12: System Services and Daemons.

If Module 11 was about how your Linux system talks to the network, Module 12 is about how your Linux system talks to itself — how it starts services, manages daemons, and coordinates the hundreds of background processes that make a server useful.

The centerpiece of this module is `systemd`, the init system that replaced SysVinit and Upstart on virtually every mainstream Linux distribution. The Linux+ exam tests systemd extensively, and in the real world, you will use `systemctl` and `journalctl` every single day.

In Part 1, we'll cover systemd's architecture, the `systemctl` command for managing services, unit file structure, and the relationship between legacy runlevels and modern systemd targets. In Part 2, we'll work through `journalctl` for centralized log analysis and then cover job scheduling with `cron` and `at`.

Let's begin.

---

### Section 1: systemd Architecture

**The Role of init**

When a Linux system boots, the kernel initializes hardware and then launches a single process with PID 1. That process is responsible for starting everything else — all system services, the login prompt, and user sessions. On modern Linux distributions, that PID 1 process is `systemd`.

You can verify this:

```bash
ps -p 1 -o comm=
```

The output will be `systemd`.

**Why systemd Replaced SysVinit**

SysVinit started services sequentially using shell scripts in `/etc/init.d/`. This was slow and hard to parallelize. systemd addresses this with:

- **Parallel service startup** — services with no dependencies start simultaneously
- **On-demand activation** — services can start when a socket, path, or device appears
- **Declarative unit files** — simple INI-style configuration instead of complex shell scripts
- **Integrated logging** — the journal captures all service output in a structured format
- **Dependency tracking** — explicit `Requires`, `Wants`, and `After` relationships

**systemd Units**

Everything in systemd is a unit. A unit is a configuration file that describes a system resource. The most common unit types are:

- **service** — a background process (daemon)
- **socket** — a network or IPC socket that activates a service on demand
- **timer** — a scheduled task (modern cron alternative)
- **target** — a group of units (replaces runlevels)
- **mount** — a filesystem mount point
- **device** — a kernel device
- **path** — triggers activation when a file or directory changes

Unit files are located in:

- `/lib/systemd/system/` — package-provided units (do not edit)
- `/etc/systemd/system/` — administrator-customized units (override package units)
- `/run/systemd/system/` — runtime-generated units

When the same unit name exists in multiple locations, `/etc/systemd/system/` takes precedence.

---

### Section 2: systemctl — Service Management

The `systemctl` command is your primary interface to systemd. Let's go through the essential operations.

**Checking Service Status**

```bash
systemctl status nginx
```

This shows:

- Active state: `active (running)`, `active (exited)`, `inactive`, `failed`
- PID of the main process
- Recent log output from the journal
- Whether the service is enabled (starts at boot)

**Starting and Stopping Services**

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
```

The difference between `restart` and `reload`:

- `restart` — stops and starts the service (causes brief downtime)
- `reload` — sends the process a signal to re-read its configuration without stopping (zero downtime when supported)

Not all services support `reload`. Check with:

```bash
systemctl show nginx | grep ExecReload
```

If `ExecReload` is empty, the service does not support reloading.

**Enabling and Disabling Services**

Enabling a service creates a symlink in the appropriate target's wants directory, so it starts automatically at boot:

```bash
sudo systemctl enable nginx
sudo systemctl disable nginx
```

Combine start and enable in one command:

```bash
sudo systemctl enable --now nginx
sudo systemctl disable --now nginx
```

**Masking a Service**

Masking creates a symlink to `/dev/null`, preventing the service from being started by any means:

```bash
sudo systemctl mask nginx
sudo systemctl unmask nginx
```

Use masking when you want to ensure a service can never start, even if something tries to start it as a dependency.

**Listing Units**

List all active units:

```bash
systemctl list-units
```

List all service units:

```bash
systemctl list-units --type=service
```

List all units including inactive and failed:

```bash
systemctl list-units --all
```

List failed units — run this during troubleshooting:

```bash
systemctl --failed
```

**Checking if a Service is Enabled**

```bash
systemctl is-enabled nginx
systemctl is-active nginx
```

---

### Section 3: Unit File Anatomy

Understanding unit file structure lets you create custom services and diagnose configuration issues.

**Viewing a Unit File**

```bash
systemctl cat nginx
```

This displays the unit file including any drop-in overrides.

**Basic Unit File Structure**

```ini
[Unit]
Description=The nginx HTTP and reverse proxy server
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t
ExecStart=/usr/sbin/nginx
ExecReload=/bin/kill -s HUP $MAINPID
KillSignal=SIGQUIT
TimeoutStopSec=5
KillMode=mixed
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

**The [Unit] Section**

- `Description` — human-readable name shown in `systemctl status` and logs
- `After` — start this unit after these units are active (ordering only, not dependency)
- `Requires` — hard dependency; if the required unit fails, this unit also fails
- `Wants` — soft dependency; this unit prefers these units to be running but doesn't require them
- `Conflicts` — cannot be active at the same time as these units

**The [Service] Section — Service Types**

The `Type=` directive tells systemd how to track when the service is "ready":

- `simple` — the main process started by `ExecStart` is the service process (default)
- `forking` — the service daemonizes by forking; systemd expects the parent to exit
- `oneshot` — runs once and exits; systemd waits for it to complete
- `notify` — the service sends a notification via `sd_notify()` when ready
- `dbus` — ready when it acquires a D-Bus name

**Other Key [Service] Directives**

- `ExecStart` — command to start the service
- `ExecStop` — command to stop the service (optional; default is SIGTERM)
- `ExecReload` — command to reload configuration
- `Restart` — when to auto-restart: `always`, `on-failure`, `on-abnormal`
- `RestartSec` — delay before restart
- `User` / `Group` — run the service as this user/group
- `EnvironmentFile` — load environment variables from a file
- `WorkingDirectory` — set the working directory
- `StandardOutput` — redirect stdout: `journal`, `syslog`, `null`, `file:/path`

**The [Install] Section**

- `WantedBy` — which target adds this unit to its wants when enabled
- `RequiredBy` — which target requires this unit
- `Alias` — alternative unit names

---

### Section 4: Creating a Custom Service Unit

Here's a practical example: creating a systemd service for a Python web application.

Create the unit file:

```bash
sudo nano /etc/systemd/system/myapp.service
```

```ini
[Unit]
Description=My Python Web Application
After=network.target
Wants=network.target

[Service]
Type=simple
User=appuser
Group=appuser
WorkingDirectory=/opt/myapp
EnvironmentFile=/opt/myapp/.env
ExecStart=/usr/bin/python3 /opt/myapp/app.py
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

Reload systemd to recognize the new file:

```bash
sudo systemctl daemon-reload
```

Enable and start the service:

```bash
sudo systemctl enable --now myapp
```

Check its status:

```bash
systemctl status myapp
```

---

### Section 5: systemd Targets (Replacing Runlevels)

**Legacy Runlevels**

SysVinit used numeric runlevels:

| Runlevel | Purpose |
|----------|---------|
| 0 | Halt |
| 1 | Single-user mode |
| 3 | Multi-user, no GUI |
| 5 | Multi-user with GUI |
| 6 | Reboot |

**systemd Targets**

Targets replace runlevels with named groups:

| Target | Equivalent Runlevel | Description |
|--------|---------------------|-------------|
| `poweroff.target` | 0 | Shutdown |
| `rescue.target` | 1 | Single-user rescue mode |
| `multi-user.target` | 3 | Multi-user, no GUI |
| `graphical.target` | 5 | Multi-user with GUI |
| `reboot.target` | 6 | Reboot |
| `emergency.target` | — | Minimal emergency shell |

**Viewing and Changing the Default Target**

```bash
systemctl get-default
sudo systemctl set-default multi-user.target
```

**Switching Targets at Runtime**

```bash
sudo systemctl isolate rescue.target
sudo systemctl isolate multi-user.target
```

`isolate` switches to the target immediately, stopping units not in that target.

**Compatibility Symlinks**

For backward compatibility, `/etc/init.d/` shell scripts are still processed by systemd through the `systemd-sysv-generator`. The old `service` command (`service nginx start`) still works but calls `systemctl` behind the scenes.

---

### Summary — Part 1

In Part 1 we covered:

- systemd architecture: units, unit types, and file locations
- `systemctl` operations: start, stop, restart, enable, disable, mask, status
- Unit file structure: `[Unit]`, `[Service]`, and `[Install]` sections
- Service types and key directives
- Creating a custom service unit
- systemd targets and their runlevel equivalents

In Part 2, we'll explore `journalctl` for log analysis and then cover job scheduling with `cron` and `at`. See you there.
