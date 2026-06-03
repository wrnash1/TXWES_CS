# Video Script: Module 14 - SELinux and AppArmor Security (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 14 minutes
**Part:** 1 of 2 - SELinux Architecture and Administration

---

### Opening

Welcome to Module 14. Standard Linux file permissions — owner, group, others, read/write/execute —
are called Discretionary Access Control, or DAC. They are controlled by the file's owner. Module
14 covers Mandatory Access Control: security policies enforced by the kernel itself that override
DAC. Even root cannot override MAC policies without explicitly modifying the policy. We cover two
MAC implementations: SELinux (used on RHEL, CentOS, Fedora) and AppArmor (used on Ubuntu, Debian,
SUSE). Knowing both is required for the Linux+ exam.

---

### Section 1: SELinux Concepts

[SHOW TERMINAL]

SELinux — Security-Enhanced Linux — was developed by the NSA and integrated into the Linux kernel.
It enforces policies based on labels attached to every file, process, port, and device on the
system.

Every object has a security context with four fields:

```
user:role:type:level
```

The type field is the most important for day-to-day administration. Examples:

```bash
ls -Z /var/www/html/
# -rw-r--r--. root root unconfined_u:object_r:httpd_sys_content_t:s0 index.html

ps auxZ | grep httpd
# unconfined_u:system_r:httpd_t:s0  apache  1234  httpd
```

The `httpd_t` process type can access `httpd_sys_content_t` file types. SELinux policy defines
which types can interact. If a file has the wrong type, access is denied regardless of DAC
permissions.

---

### Section 2: SELinux Modes

[SHOW TERMINAL]

SELinux has three modes:

```bash
getenforce
```

Returns: `Enforcing`, `Permissive`, or `Disabled`.

* **Enforcing** — policy is enforced; violations are blocked and logged
* **Permissive** — violations are logged but NOT blocked; useful for troubleshooting
* **Disabled** — SELinux is off; no policy is loaded

```bash
sestatus
```

Shows current mode, policy version, and whether MLS/MCS is active.

Change mode at runtime (does NOT survive reboot):

```bash
sudo setenforce 0    # Switch to Permissive
sudo setenforce 1    # Switch to Enforcing
```

Change mode persistently (survives reboot):

```bash
sudo vi /etc/selinux/config
# Set: SELINUX=enforcing
```

The config file is read at boot. `setenforce` only changes the runtime state.

---

### Section 3: SELinux Troubleshooting Workflow

[SHOW TERMINAL]

When an application fails and DAC permissions are correct, SELinux is the likely cause.

Step 1: Check the audit log for AVC (Access Vector Cache) denial messages:

```bash
sudo ausearch -m avc -ts recent
```

Or:

```bash
sudo tail -f /var/log/audit/audit.log | grep AVC
```

Step 2: Use `audit2why` to get a human-readable explanation:

```bash
sudo ausearch -m avc -ts recent | audit2why
```

Step 3: Temporarily set permissive mode to confirm SELinux is the cause:

```bash
sudo setenforce 0
# Test the application
sudo setenforce 1
```

If the problem disappears in permissive mode, SELinux was blocking it.

Step 4: Fix the root cause (context or boolean), then re-enable enforcing.

---

### Section 4: File Context Management

[SHOW TERMINAL]

The most common SELinux problem: a file is in the wrong location or was copied (not moved) and
has the wrong type context.

```bash
ls -Z /srv/webdata/
# Likely shows: default_t or unlabeled_t — wrong for Apache
```

Temporary fix (does not survive restorecon or relabeling):

```bash
sudo chcon -t httpd_sys_content_t /srv/webdata/index.html
```

Permanent fix (updates policy database, survives relabeling):

```bash
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/webdata(/.*)?"
sudo restorecon -Rv /srv/webdata/
```

`semanage fcontext` adds a rule to the policy database. `restorecon` applies the policy to the
actual files. Always use this two-step approach for permanent fixes.

Relabel an entire filesystem on next boot (for major context problems):

```bash
sudo touch /.autorelabel
sudo reboot
```

---

### Section 5: SELinux Booleans

[SHOW TERMINAL]

SELinux booleans are on/off switches that toggle specific policy behaviors without writing custom
policy.

```bash
getsebool -a             # List all booleans and their current values
getsebool httpd_can_network_connect    # Check a specific boolean
```

Common web server booleans:

| Boolean | Purpose |
|---------|---------|
| httpd_can_network_connect | Allow Apache to make outbound network connections |
| httpd_can_sendmail | Allow Apache to send email |
| httpd_read_user_content | Allow Apache to read user home directories |
| httpd_enable_homedirs | Allow Apache to serve from home directories |

Set a boolean at runtime (temporary):

```bash
sudo setsebool httpd_can_network_connect on
```

Set a boolean permanently:

```bash
sudo setsebool -P httpd_can_network_connect on
```

The `-P` flag writes the change to the policy store, making it persistent across reboots.

---

### Section 6: SELinux Port Contexts

[SHOW TERMINAL]

If an application listens on a non-standard port, SELinux may block it.

```bash
semanage port -l | grep http
```

Allow Apache to listen on port 8080:

```bash
sudo semanage port -a -t http_port_t -p tcp 8080
```

---

### Section 7: Certification Connection

SELinux maps to Linux+ Domain 3.0 (Troubleshooting) and Domain 2.0 (Security). Key exam topics:

* The three SELinux modes: Enforcing, Permissive, Disabled — and their distinction
* `getenforce`/`setenforce` for runtime mode; `/etc/selinux/config` for persistent mode
* `chcon` vs `semanage fcontext + restorecon` — know which is temporary and which is permanent
* `ausearch -m avc` and `audit2why` for reading denial messages
* `setsebool -P` for persistent boolean changes

---

### Transition to Part 2

In Part 2 we cover AppArmor on Ubuntu systems: profiles, enforce vs complain modes, aa-status,
aa-enforce, aa-complain, and profile management with apparmor-utils.

---

### Additional Resources

* professormesser.com - CompTIA Linux+ study materials and practice exams
* comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
