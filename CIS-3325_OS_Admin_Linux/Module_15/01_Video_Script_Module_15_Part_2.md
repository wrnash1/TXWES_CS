# Video Script: Module 15 — Linux Security Hardening (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome back to Module 15, Part 2.

In Part 1, we covered SELinux and AppArmor — the Mandatory Access Control systems that confine processes to defined policies. Now we move to the broader security hardening toolkit: `auditd` for detailed system event auditing, `fail2ban` for automated intrusion response, password policy enforcement, and the CIS Benchmark framework that ties it all together.

---

### Section 6: auditd — Linux Audit System

The Linux audit subsystem provides a way to track security-relevant events at the kernel level. Unlike logs that capture what applications choose to report, `auditd` captures events at the system call level — you can audit file access, user authentication, process execution, network connections, and privilege escalation with cryptographic integrity.

**Components**

- **auditd** — the audit daemon that receives events from the kernel and writes them to log files
- **auditctl** — command to add, remove, and list audit rules at runtime
- **auditd.conf** — daemon configuration (`/etc/audit/auditd.conf`)
- **audit.rules** — persistent rules file (`/etc/audit/rules.d/audit.rules`)
- **ausearch** — query and display audit records
- **aureport** — generate summary reports from audit logs
- **augenrules** — compile rules files from `/etc/audit/rules.d/` into `/etc/audit/audit.rules`

**Starting auditd**

```bash
sudo systemctl enable --now auditd
```

**Viewing Current Rules**

```bash
sudo auditctl -l
```

**Adding Rules**

Audit all writes to `/etc/passwd`:

```bash
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
```

- `-w /etc/passwd` — watch this file
- `-p wa` — audit write (`w`) and attribute change (`a`)
- `-k passwd_changes` — label for searching (`-k` is key)

Audit all executions of `su`:

```bash
sudo auditctl -w /usr/bin/su -p x -k privilege_escalation
```

Audit all failed login attempts:

```bash
sudo auditctl -a always,exit -F arch=b64 -S open -F exit=-EACCES -k failed_access
```

**Making Rules Persistent**

Add rules to `/etc/audit/rules.d/custom.rules`:

```
-w /etc/passwd -p wa -k passwd_changes
-w /etc/shadow -p wa -k shadow_changes
-w /etc/sudoers -p wa -k sudoers_changes
-w /usr/bin/su -p x -k privilege_escalation
-w /usr/bin/sudo -p x -k privilege_escalation
```

Reload:

```bash
sudo augenrules --load
```

**Querying with ausearch**

Search for events with key `passwd_changes`:

```bash
sudo ausearch -k passwd_changes
sudo ausearch -k passwd_changes -ts today
sudo ausearch -k passwd_changes --format text
```

Search for failed logins:

```bash
sudo ausearch -m USER_LOGIN -i --success no
```

Search for events by user:

```bash
sudo ausearch -ua 1001
```

**Generating Reports with aureport**

```bash
sudo aureport
sudo aureport --summary
sudo aureport --auth
sudo aureport --failed
sudo aureport --login
```

---

### Section 7: fail2ban — Intrusion Prevention

`fail2ban` monitors log files for patterns indicating attacks (like repeated failed authentication attempts) and dynamically blocks offending IP addresses using firewall rules.

**How fail2ban Works**

1. fail2ban reads log files (SSH, Apache, etc.)
2. It matches lines against patterns (called "filters")
3. When an IP exceeds a threshold (e.g., 5 failures in 10 minutes), it becomes "jailed"
4. A jail action blocks the IP using iptables, firewalld, or nftables
5. After the ban time expires, the IP is unblocked

**Installing and Starting fail2ban**

```bash
sudo dnf install fail2ban    # RHEL/Rocky
sudo apt install fail2ban    # Ubuntu
sudo systemctl enable --now fail2ban
```

**Configuration Files**

- `/etc/fail2ban/fail2ban.conf` — global daemon configuration
- `/etc/fail2ban/jail.conf` — jail definitions (do not edit)
- `/etc/fail2ban/jail.local` — local overrides (create this file)
- `/etc/fail2ban/filter.d/` — filter definitions
- `/etc/fail2ban/action.d/` — action definitions

Always create `jail.local` for local overrides. Changes to `jail.conf` are overwritten on updates.

**Basic jail.local Configuration**

```ini
[DEFAULT]
bantime  = 1h
findtime = 10m
maxretry = 5
backend  = systemd

[sshd]
enabled  = true
port     = ssh
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 3
bantime  = 24h
```

- `bantime` — how long to ban an IP
- `findtime` — time window for counting failures
- `maxretry` — failures within findtime before banning

**fail2ban-client Commands**

Check status of all jails:

```bash
sudo fail2ban-client status
```

Check a specific jail:

```bash
sudo fail2ban-client status sshd
```

Manually ban an IP:

```bash
sudo fail2ban-client set sshd banip 1.2.3.4
```

Unban an IP:

```bash
sudo fail2ban-client set sshd unbanip 1.2.3.4
```

Reload fail2ban after configuration changes:

```bash
sudo fail2ban-client reload
```

---

### Section 8: Password Policies

**The /etc/login.defs File**

System-wide defaults for password aging and account creation:

```
PASS_MAX_DAYS   90    # Maximum password age in days
PASS_MIN_DAYS   7     # Minimum days before change allowed
PASS_MIN_LEN    12    # Minimum password length (PAM may override)
PASS_WARN_AGE   14    # Days before expiry to warn user
```

These settings apply to new accounts at creation. Existing accounts must be updated with `chage`.

**chage — Change User Password Aging**

View password expiration details:

```bash
sudo chage -l username
```

Set password to expire in 90 days:

```bash
sudo chage -M 90 username
```

Set minimum days between changes to 7:

```bash
sudo chage -m 7 username
```

Set warning period to 14 days:

```bash
sudo chage -W 14 username
```

Force password change on next login:

```bash
sudo chage -d 0 username
```

Set absolute account expiration date:

```bash
sudo chage -E 2025-12-31 username
```

**PAM — Pluggable Authentication Modules**

PAM (Pluggable Authentication Modules) provides a modular framework for authentication. Password complexity requirements are configured via PAM.

On RHEL/Rocky — `pam_pwquality.so`:

Configuration file: `/etc/security/pwquality.conf`

```
minlen = 12
dcredit = -1    # Require at least 1 digit
ucredit = -1    # Require at least 1 uppercase
lcredit = -1    # Require at least 1 lowercase
ocredit = -1    # Require at least 1 special character
maxrepeat = 3   # No more than 3 consecutive identical characters
```

**Account Lockout with PAM**

Configure account lockout after failed attempts using `pam_faillock.so` (RHEL 8+):

```
/etc/security/faillock.conf:
deny = 5
unlock_time = 600
```

Check locked accounts:

```bash
faillock --user username
```

Unlock a user:

```bash
sudo faillock --user username --reset
```

---

### Section 9: CIS Benchmarks

The Center for Internet Security (CIS) publishes hardening benchmarks — detailed documents with specific configuration recommendations for every major operating system and application. CIS Benchmarks are used by security teams, compliance auditors, and system administrators worldwide.

**What is a CIS Benchmark?**

A CIS Benchmark is a consensus-based document containing:

- Specific, actionable configuration recommendations
- Rationale explaining why each setting matters
- Assessment procedure showing how to check current state
- Remediation steps to bring the system into compliance
- Scoring and profile levels

**CIS Benchmark Profiles**

- **Level 1** — minimum baseline; low operational impact; required for most environments
- **Level 2** — more restrictive; for high-security environments; may impact functionality

**Key CIS Linux Benchmark Areas**

- Initial setup: patching, filesystem configuration, bootloader security
- Services: disable unnecessary services, configure NTP, mail transfer agent
- Network configuration: disable IPv6 if not needed, restrict routing, configure firewall
- Logging and auditing: auditd configuration, log file permissions, syslog settings
- Access control: PAM configuration, SSH hardening, user account management
- System maintenance: regular patching, file integrity monitoring, permissions review

**CIS-CAT Tool**

The CIS Configuration Assessment Tool (CIS-CAT) automates benchmark assessment:

- Scans the system against selected benchmark profiles
- Produces HTML/JSON reports showing pass/fail for each recommendation
- Provides a compliance score

**OSCAP — OpenSCAP**

A free, open-source security assessment tool:

```bash
sudo dnf install openscap openscap-utils scap-security-guide

# Scan against CIS Level 1 profile for RHEL 9:
sudo oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis \
  --results /tmp/cis-results.xml \
  --report /tmp/cis-report.html \
  /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml
```

**Practical Hardening Steps**

From the CIS Benchmark, key Level 1 items for a fresh Linux server:

1. Enable and configure auditd
2. Enable SELinux (enforcing mode)
3. Configure SSH: `PermitRootLogin no`, `PasswordAuthentication no`
4. Disable unused filesystems: `cramfs`, `squashfs`, `udf`
5. Set sticky bit on world-writable directories
6. Configure password complexity via PAM
7. Set password aging in `/etc/login.defs`
8. Disable unused services (Bluetooth, cups if not needed)
9. Enable and configure firewalld
10. Ensure cron and at access is restricted

---

### Summary — Module 15

Module 15 covered the Linux security hardening toolkit:

**Part 1:**

- MAC principles: DAC vs. MAC and why MAC matters
- SELinux: modes (enforcing/permissive/disabled), security contexts, booleans, troubleshooting with `ausearch` and `audit2why`
- AppArmor: profiles, enforce vs. complain mode, `aa-status`

**Part 2:**

- auditd: kernel-level event auditing, `auditctl` rules, `ausearch` queries, `aureport` summaries
- fail2ban: pattern-based IP blocking, `jail.local` configuration, fail2ban-client management
- Password policies: `/etc/login.defs`, `chage`, PAM `pam_pwquality`, `pam_faillock`
- CIS Benchmarks: profiles, assessment with OpenSCAP, key Level 1 hardening items

Security hardening is not a one-time task — it is a continuous process. The tools in this module provide both the controls and the visibility needed to maintain a defensible Linux environment.

Next: Module 16 — Linux+ XK0-005 Exam Preparation.
