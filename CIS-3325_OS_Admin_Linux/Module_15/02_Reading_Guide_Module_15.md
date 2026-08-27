# Reading Guide: Module 15 — Linux Security Hardening

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This guide accompanies the Module 15 video lectures on SELinux, AppArmor, auditd, fail2ban, password policies, and CIS Benchmarks. Estimated reading and review time: 90 minutes.

---

### Learning Objectives

After completing this module, you will be able to:

- Explain the difference between Discretionary and Mandatory Access Control
- Configure and troubleshoot SELinux: check mode, change mode, manage contexts, use booleans
- Describe AppArmor profiles and the difference between enforce and complain modes
- Configure `auditd` rules for file and system call monitoring
- Query audit logs using `ausearch` and generate reports with `aureport`
- Deploy and configure `fail2ban` to prevent brute-force attacks
- Configure password aging and complexity policies using `chage`, PAM, and `login.defs`
- Describe the CIS Benchmark framework and use OpenSCAP for system assessment

---

### Key Terms

**DAC (Discretionary Access Control)**
The traditional Unix permission model where resource owners control access. Owner discretion determines who can read, write, or execute.

**MAC (Mandatory Access Control)**
Access control enforced by the system based on policy, overriding owner discretion. Processes are confined to specific types even if running as root.

**SELinux Context**
A security label applied to every file, process, port, and object: `user:role:type:level`.

**Type Enforcement**
The primary mechanism in SELinux's targeted policy. Processes in one domain type can only access objects with permitted types.

**AVC**
Access Vector Cache. SELinux logs denials as AVC messages in the audit log.

**AppArmor Profile**
A file in `/etc/apparmor.d/` that defines what files, capabilities, and network resources an application may access.

**auditd**
The Linux audit daemon. Writes kernel-generated security events to `/var/log/audit/audit.log`.

**fail2ban Jail**
A configured set of rules defining which log file to monitor, what pattern constitutes a failure, how many failures trigger a ban, and what action to take.

**PAM**
Pluggable Authentication Modules. A framework allowing flexible, modular authentication configuration. Configured in `/etc/pam.d/`.

**CIS Benchmark**
A consensus-based security configuration guide published by the Center for Internet Security. Contains specific, actionable hardening recommendations with rationale.

---

### Section 1: SELinux Policy Details

**The Targeted Policy**

The `targeted` SELinux policy (default on RHEL) confines a specific set of high-risk daemons:

- httpd (Apache)
- named (BIND)
- sshd (OpenSSH)
- mysqld / postgresql
- vsftpd, dovecot, postfix
- And many others

Processes NOT covered by the targeted policy run in the `unconfined_t` domain, which has nearly unrestricted access. This is a deliberate tradeoff — covering all user processes would create too many policy conflicts.

**The MLS Policy**

The `mls` (Multi-Level Security) policy enforces Bell-LaPadula model confidentiality. Every object has a sensitivity level and category. A process can only access objects at or below its clearance level. Used in government and defense environments.

**SELinux Audit Log Location**

All SELinux denials are logged to:

```
/var/log/audit/audit.log
```

AVC (Access Vector Cache) denial messages look like:

```
type=AVC msg=audit(1234567890.123:456): avc:  denied  { read } for
pid=1234 comm="httpd" name="secret.txt"
scontext=system_u:system_r:httpd_t:s0
tcontext=staff_u:object_r:staff_home_t:s0 tclass=file permissive=0
```

Reading this: `httpd_t` (Apache) was denied `read` access to a file with context `staff_home_t`. This is a type enforcement violation.

**SELinux Port Contexts**

SELinux also controls which ports services can bind to. If you change Apache to listen on port 8080, SELinux may block it because only port 80/443 are labeled `http_port_t` by default.

Manage port contexts with `semanage port`:

```bash
sudo semanage port -l | grep http
sudo semanage port -a -t http_port_t -p tcp 8080
```

---

### Section 2: AppArmor Profile Development

**Profile Components**

An AppArmor profile consists of:

- **Path rules**: specify files the application can access and with what permissions
- **Capability rules**: specify POSIX capabilities the application may use
- **Network rules**: specify network protocol access
- **Include abstractions**: reusable rule sets for common access patterns

**Permission flags in path rules:**

| Flag | Meaning |
|------|---------|
| `r` | Read |
| `w` | Write |
| `x` | Execute |
| `m` | mmap (memory-map) |
| `l` | Link |
| `k` | Lock |

**Glob patterns:**

- `@{HOME}/**` — everything under the home directory variable
- `/var/log/myapp/*` — files directly in this directory
- `/etc/myapp/**` — all files recursively

**Generating Profiles with aa-genprof**

For new applications, `aa-genprof` creates a profile interactively:

```bash
sudo aa-genprof /usr/bin/myapp
```

Run the application and perform typical operations. `aa-genprof` captures accesses and prompts you to allow or deny each one, building the profile incrementally.

**Viewing AppArmor Denials**

```bash
sudo journalctl -k | grep DENIED
sudo grep DENIED /var/log/syslog
sudo grep DENIED /var/log/kern.log
```

---

### Section 3: auditd Advanced Configuration

**auditd.conf Settings**

Key settings in `/etc/audit/auditd.conf`:

```
log_file = /var/log/audit/audit.log
max_log_file = 50          # MB per log file
max_log_file_action = ROTATE
num_logs = 5               # Keep 5 rotated logs
space_left = 100           # MB free before warning
space_left_action = email
admin_space_left = 50      # MB before halt
admin_space_left_action = halt
```

`admin_space_left_action = halt` stops the system rather than allow audit records to be lost. This is required by some high-security policies.

**System Call Auditing**

Beyond watching files, `auditd` can audit specific system calls:

```bash
# Audit all execve() calls (every command execution) by specific user:
sudo auditctl -a always,exit \
  -F arch=b64 \
  -S execve \
  -F uid=1001 \
  -k user_commands
```

**Predefined Rule Sets**

The `audit-rules` package includes predefined rule sets based on standards like STIG and PCI-DSS:

```bash
ls /usr/share/audit/sample-rules/
```

**Log Integrity**

The audit log is a critical security artifact. Protect it:

- Log to a remote server using `audisp-remote`
- Set immutable flag on rules at startup: `-e 2` at end of rules file
- Monitor log file access with an audit rule on the audit log itself

---

### Section 4: fail2ban Configuration Reference

**Filter Files**

Filters use regular expressions to identify failure patterns in logs.

Example filter for a custom application:

```ini
# /etc/fail2ban/filter.d/myapp.conf
[Definition]
failregex = ^<HOST> .* Authentication failed
ignoreregex =
```

**Action Files**

Actions define what happens when a ban is triggered. Default action (`firewallcmd-ipset`) uses firewalld:

```ini
# /etc/fail2ban/action.d/firewallcmd-ipset.conf
[Definition]
actionstart = ...
actionstop = ...
actionban = firewall-cmd --add-rich-rule="rule family='ipv4' source address='<ip>' reject"
actionunban = firewall-cmd --remove-rich-rule="rule family='ipv4' source address='<ip>' reject"
```

**Common Jail Configurations**

Apache authentication failures:

```ini
[apache-auth]
enabled  = true
port     = http,https
filter   = apache-auth
logpath  = /var/log/httpd/error_log
maxretry = 5
```

Nginx bad requests:

```ini
[nginx-http-auth]
enabled  = true
filter   = nginx-http-auth
logpath  = /var/log/nginx/error.log
maxretry = 5
```

---

### Section 5: PAM Architecture

**PAM Module Types**

PAM modules are organized into four types:

| Type | Purpose |
|------|---------|
| `auth` | Authenticate the user (verify identity) |
| `account` | Check account validity (expiration, access time) |
| `session` | Set up/tear down user session environment |
| `password` | Update authentication credentials |

**PAM Control Flags**

| Flag | Effect |
|------|--------|
| `required` | Must succeed; failure noted but other modules continue |
| `requisite` | Must succeed; immediate failure stops processing |
| `sufficient` | If this succeeds, no further processing needed |
| `optional` | Result is ignored unless the only module for this type |

**PAM Password Module Stack**

In `/etc/pam.d/passwd`:

```
password    requisite     pam_pwquality.so try_first_pass local_users_only
password    sufficient    pam_unix.so sha512 shadow nullok try_first_pass use_authtok
password    required      pam_deny.so
```

**pam_tally2 vs. pam_faillock**

- `pam_tally2` — older lockout module (RHEL 7 and earlier)
- `pam_faillock` — modern replacement (RHEL 8+)

Both track failed authentication attempts and lock accounts after a threshold.

---

### Section 6: Security Hardening Checklist

A practical hardening checklist based on CIS Benchmarks Level 1:

**Filesystem:**

- Ensure separate partitions for `/tmp`, `/var`, `/var/log`, `/home`
- Set `noexec`, `nosuid`, `nodev` on `/tmp`
- Disable unused filesystem modules

**Network:**

- Ensure IPv4 forwarding is disabled (unless router)
- Ensure TCP SYN cookies are enabled
- Ensure firewalld or iptables is active

**Logging:**

- auditd installed and running
- Audit rules for `passwd`, `shadow`, `sudoers` changes
- Remote logging configured

**Access Control:**

- Root login disabled for SSH
- Password complexity configured via PAM
- Password aging configured: max 90 days, min 7 days
- Account lockout after 5 failures

**Services:**

- Disable: bluetooth, cups (if no printing), avahi, nfs-server (unless needed)
- Enable: auditd, firewalld, sshd
- SSH: key auth only, no root login, banner configured

---

### Practice Review Questions

Answer these before taking the quiz:

1. What is the difference between SELinux `Enforcing` and `Permissive` mode?

2. A web server cannot read a file in `/srv/webdata/`. SELinux is in enforcing mode. What two things would you check first?

3. What command displays all AppArmor profiles and their current mode?

4. Write an `auditctl` rule to monitor all writes to `/etc/sudoers` with key `sudoers_watch`.

5. What fail2ban directive controls how many failures within what time period trigger a ban?

6. What is the difference between `chage -M` and `chage -d`?

7. What does the `pam_pwquality` module `dcredit = -1` setting mean?

8. In the CIS Benchmark framework, what is the difference between Level 1 and Level 2 profiles?

---

### Additional Resources

- SELinux User's and Administrator's Guide: access.redhat.com/documentation
- `man 8 semanage-fcontext` — managing file contexts
- `man 8 auditctl` — audit rules syntax
- `man 5 jail.conf` — fail2ban configuration reference
- `man 5 pam_pwquality` — password quality module
- CIS Benchmarks: [cisecurity.org/cis-benchmarks](https://www.cisecurity.org/cis-benchmarks)
- OpenSCAP documentation: [open-scap.org](https://www.open-scap.org)

---

### Key Takeaways

- SELinux Enforcing mode is the security baseline for RHEL-family systems. Running in Permissive or Disabled is a compliance violation in most regulated environments.
- The most common SELinux fix is `restorecon` — files copied from other locations often have the wrong context.
- `auditd` captures events at the kernel level; it cannot be bypassed by userspace processes.
- fail2ban is a detective control, not a preventive one — it acts after failures occur. Combine with SSH key-only authentication for defense in depth.
- CIS Benchmarks provide the industry-standard checklist for Linux hardening. Know the Level 1 items for the Linux+ exam.

---

## 9. Supplemental Resources

**1. [Red Hat SELinux User's and Administrator's Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/index)**
The authoritative Red Hat documentation for SELinux on RHEL 9. Covers concepts (DAC vs MAC, type enforcement, MLS), common administration tasks (`semanage`, `restorecon`, booleans), troubleshooting AVC denials with `ausearch` and `sealert`, writing custom policy modules, and confined vs. unconfined users. Essential for both the Module 15 lab and the CompTIA Linux+ security objectives.

**2. [Lynis — Security Auditing Tool Documentation](https://cisofy.com/documentation/lynis/)**
The official Lynis documentation for the open-source security auditing and hardening tool. Covers installation, performing a system audit (`sudo lynis audit system`), interpreting the hardening index score, understanding warnings and suggestions, and integrating Lynis into a CI/CD pipeline for continuous compliance checking. Lynis reports map directly to CIS Benchmark controls, making it ideal for exam preparation and real-world hardening projects.

**3. [fail2ban Documentation — fail2ban.readthedocs.io](https://fail2ban.readthedocs.io/en/latest/)**
The official fail2ban documentation. Covers the architecture (jail → filter → action), writing custom filters using regular expressions, defining custom actions beyond firewall bans (email notifications, database logging), the `fail2ban-client` management interface, and testing filters with `fail2ban-regex`. Understanding how to write custom filters is the key skill for applying fail2ban to non-standard application logs.
