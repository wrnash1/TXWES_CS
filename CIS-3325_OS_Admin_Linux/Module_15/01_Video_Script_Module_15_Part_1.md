# Video Script: Module 15 — Linux Security Hardening (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 15: Linux Security Hardening.

Security hardening is the process of reducing a system's attack surface by removing unnecessary services, configuring access controls, enabling monitoring, and enforcing policies. In this module, we cover the security frameworks and tools that the Linux+ exam tests most heavily: SELinux, AppArmor, `auditd`, and the broader framework of CIS Benchmarks.

Part 1 focuses on Mandatory Access Control — specifically SELinux and AppArmor. These are fundamentally different from traditional Unix permissions, and understanding them requires a shift in how you think about process security. Part 2 covers intrusion prevention with fail2ban, password policy enforcement, and the CIS Benchmark framework.

Let's begin.

---

### Section 1: Mandatory Access Control Overview

**Traditional Unix Permissions (DAC)**

The permission model you know — user/group/other with read/write/execute — is called **Discretionary Access Control (DAC)**. The owner of a resource has discretion over who can access it. It is flexible but has a critical weakness: if a privileged process is compromised, the attacker gains all permissions of that process.

**Mandatory Access Control (MAC)**

MAC enforces access policies defined by the system administrator or security policy, regardless of what the process owner wants. Even if an attacker compromises a web server process running as root, MAC can prevent that process from accessing files outside a defined policy.

Two major MAC systems exist in Linux:

- **SELinux** — Security-Enhanced Linux, developed by the NSA; default on RHEL/CentOS/Fedora/Rocky
- **AppArmor** — Application Armor; default on Ubuntu/Debian/SUSE

Both systems confine processes to defined policies, but they use different models. You will encounter both on the Linux+ exam.

---

### Section 2: SELinux — Security-Enhanced Linux

**SELinux Architecture**

SELinux assigns **security contexts** (labels) to every file, process, port, and object on the system. The SELinux policy defines which contexts can interact with which. A process with one context cannot access a file with a different context unless the policy explicitly allows it.

**SELinux Modes**

SELinux operates in three modes:

- **Enforcing** — SELinux policy is active; policy violations are blocked and logged
- **Permissive** — SELinux policy is active; violations are logged but NOT blocked (used for troubleshooting)
- **Disabled** — SELinux is completely off; no logging, no enforcement

**Checking the Current Mode**

```bash
getenforce
sestatus
```

`getenforce` returns `Enforcing`, `Permissive`, or `Disabled`.

`sestatus` shows comprehensive status including policy name, MLS status, and loaded policy.

**Changing Mode at Runtime**

Temporarily switch between enforcing and permissive (does not survive reboot):

```bash
sudo setenforce 1   # Enforcing
sudo setenforce 0   # Permissive
```

**Persistent Mode Configuration**

The `/etc/selinux/config` file controls the mode at boot:

```
SELINUX=enforcing
SELINUXTYPE=targeted
```

- `SELINUX` values: `enforcing`, `permissive`, `disabled`
- `SELINUXTYPE` values: `targeted` (most services confined), `mls` (Multi-Level Security, strict)

**Important**: Changing from disabled to enforcing requires a full filesystem relabel at boot. This takes time and can be triggered by creating `/.autorelabel` and rebooting.

---

### Section 3: SELinux Contexts and Labels

**Security Context Format**

Every file and process has a security context in this format:

```
user:role:type:level
```

- **user** — SELinux user (e.g., `system_u`, `unconfined_u`)
- **role** — role (e.g., `object_r`, `system_r`)
- **type** — the most important component; defines what the object is (also called the "domain" for processes)
- **level** — sensitivity level (used in MLS; `s0` is default in targeted policy)

**Viewing Contexts**

```bash
ls -Z /etc/passwd
ls -Z /var/www/html/
ps -Z
id -Z
```

The `-Z` flag displays SELinux context in most standard utilities.

Example output:

```
-rw-r--r--. root root system_u:object_r:etc_t:s0 /etc/passwd
```

The type is `etc_t`.

**Understanding Types**

The type component is what matters in the targeted policy:

- Files in `/var/www/html/` have type `httpd_content_t`
- The Apache web server process has domain type `httpd_t`
- The policy allows `httpd_t` processes to read `httpd_content_t` files
- A file with type `shadow_t` cannot be read by `httpd_t` — even if root placed it there

**Restoring Default Contexts**

If a file gets the wrong context (a common problem when copying files):

```bash
sudo restorecon -v /var/www/html/index.html
sudo restorecon -Rv /var/www/html/    # Recursive
```

**Changing File Contexts**

```bash
sudo chcon -t httpd_content_t /var/www/html/newfile.html
```

`chcon` changes a file's context temporarily. After `restorecon` or a relabel, `chcon` changes may be overwritten. For permanent changes, use `semanage fcontext`.

**Permanent Context Assignment**

```bash
sudo semanage fcontext -a -t httpd_content_t "/opt/website(/.*)?"
sudo restorecon -Rv /opt/website
```

This permanently records that `/opt/website` and everything under it should have `httpd_content_t` type.

---

### Section 4: SELinux Booleans and Troubleshooting

**SELinux Booleans**

Booleans are on/off switches that enable or disable specific behaviors within the SELinux policy without changing the full policy.

List all booleans:

```bash
getsebool -a
getsebool -a | grep httpd
```

Set a boolean temporarily:

```bash
sudo setsebool httpd_can_network_connect on
```

Set permanently:

```bash
sudo setsebool -P httpd_can_network_connect on
```

Common booleans for HTTPD:

- `httpd_can_network_connect` — allow httpd to make network connections
- `httpd_can_connect_db` — allow httpd to connect to databases
- `httpd_use_nfs` — allow httpd to serve NFS-mounted content
- `httpd_enable_homedirs` — allow httpd to serve user home directories

**The Most Common SELinux Problem**

The most frequent SELinux issue for administrators: a service cannot access a file that has the wrong context. This usually happens after:

- Copying a file from a location with different context
- Moving a file (moves preserve source context, unlike copy)
- Creating a file in a location that doesn't match the policy default

**Troubleshooting with ausearch**

View recent SELinux denials:

```bash
sudo ausearch -m avc -ts recent
```

**Troubleshooting with audit2why**

Convert an AVC denial to a human-readable explanation:

```bash
sudo ausearch -m avc -ts recent | audit2why
```

This is the fastest way to understand why SELinux is blocking something.

**Generating a Policy Module with audit2allow**

If SELinux is blocking something legitimate:

```bash
sudo ausearch -m avc -ts recent | audit2allow -M mymodule
sudo semodule -i mymodule.pp
```

This generates and installs a custom policy module. Use sparingly — each custom module reduces security.

---

### Section 5: AppArmor

AppArmor takes a different approach from SELinux. Instead of labeling every file on the filesystem, AppArmor assigns **profiles** to applications that define exactly which files and capabilities each program may access.

**AppArmor Modes**

- **Enforce** — profile is enforced; violations are blocked
- **Complain** — violations are logged but not blocked (troubleshooting mode)
- **Disabled** — no profile loaded for the application

**Checking AppArmor Status**

```bash
sudo aa-status
```

This shows all loaded profiles and which mode each is in.

**AppArmor Profile Location**

Profiles are stored in `/etc/apparmor.d/`. Each profile file is named after the executable it protects.

**Enabling and Disabling Profiles**

```bash
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx    # Enforce mode
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx   # Complain mode
sudo aa-disable /etc/apparmor.d/usr.sbin.nginx    # Disable
```

**Reloading Profiles**

```bash
sudo systemctl reload apparmor
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
```

**AppArmor Profile Syntax**

```
#include <tunables/global>

/usr/sbin/nginx {
  #include <abstractions/base>
  #include <abstractions/nameservice>

  capability net_bind_service,
  capability setuid,
  capability setgid,

  /var/www/html/** r,
  /var/log/nginx/* w,
  /etc/nginx/** r,
  /run/nginx.pid rw,
}
```

**SELinux vs. AppArmor Comparison**

| Feature | SELinux | AppArmor |
|---------|---------|---------|
| Default on | RHEL/Rocky/CentOS | Ubuntu/Debian/SUSE |
| Policy model | Label-based (context on every object) | Path-based (profiles per application) |
| Complexity | Higher | Lower |
| Flexibility | Higher | Lower |
| Troubleshooting | `ausearch`, `audit2why` | `aa-status`, `/var/log/syslog` |
| File relabeling needed | Yes (when enabling) | No |

---

### Summary — Part 1

Part 1 covered Mandatory Access Control:

- DAC vs. MAC: why traditional Unix permissions are insufficient for high-security environments
- SELinux modes: enforcing, permissive, disabled — and how to check and change them
- Security contexts: user:role:type:level format, viewing with `-Z` flag
- `restorecon` for fixing wrong contexts, `semanage fcontext` for permanent changes
- SELinux booleans for fine-grained policy adjustments
- Troubleshooting SELinux denials with `ausearch`, `audit2why`, and `audit2allow`
- AppArmor profiles: path-based confinement, enforce vs. complain modes

In Part 2: `auditd` for system call auditing, `fail2ban` for intrusion prevention, password policies with `chage` and PAM, and the CIS Benchmark framework.
