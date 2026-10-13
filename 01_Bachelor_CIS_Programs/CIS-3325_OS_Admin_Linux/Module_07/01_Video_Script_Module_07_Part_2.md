# Video Script: Module 07 — User and Group Administration (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome Back

Welcome back to Module 7. In Part 1 we built our foundation: the identity files, user creation, modification, deletion, and group management.

In Part 2 we tackle the remaining high-value topics: `sudo` and `visudo` for privilege escalation, PAM basics for authentication control, and then we run through practical exam-style scenarios and the critical commands the Linux+ exam tests.

---

### Slide 2 — Understanding sudo

`sudo` — superuser do — allows a permitted user to execute a command as root or as another user. It is the safe, auditable alternative to logging in directly as root.

Why is `sudo` preferred over `su` or root login?

- Every `sudo` invocation is logged — typically to `/var/log/auth.log` or `/var/log/secure`
- Users only need elevated privileges for specific commands, not full root sessions
- Credentials are cached briefly (default 15 minutes) so repeated commands don't require repeated password entry
- Roles can be delegated granularly — a DBA can run database service commands without touching network configuration

```bash
# Run a single command as root
sudo apt update

# Run a command as a different user
sudo -u postgres psql

# Start an interactive root shell
sudo -i        # Login shell (reads root's environment)
sudo -s        # Non-login shell (inherits current environment)

# Run a command and show what sudo would execute without doing it
sudo -l                  # List allowed commands for current user
sudo -l -U jsmith       # List allowed commands for jsmith (root only)

# Check sudo version
sudo --version
```

---

### Slide 3 — Configuring sudo with visudo

The sudo policy is defined in `/etc/sudoers`. You must NEVER edit this file directly with a text editor. Always use `visudo`.

`visudo` locks the file to prevent simultaneous edits and performs syntax validation before saving. A syntax error in `/etc/sudoers` can lock everyone — including root — out of sudo permanently.

```bash
# Open sudoers for editing (always use visudo)
sudo visudo

# Open sudoers with a specific editor
sudo EDITOR=nano visudo

# Edit a drop-in file in /etc/sudoers.d/ (preferred on modern systems)
sudo visudo -f /etc/sudoers.d/webteam
```

Drop-in files under `/etc/sudoers.d/` are the modern approach. Each application or team gets its own file, reducing the risk of conflicting edits to the main sudoers file.

---

### Slide 4 — The sudoers File Syntax

```bash
# The sudoers rule format:
# WHO  WHERE=(AS_WHOM)  WHAT

# Allow jsmith to run ALL commands as root on this machine
jsmith  ALL=(ALL)  ALL

# Allow jsmith without a password
jsmith  ALL=(ALL)  NOPASSWD: ALL

# Allow jsmith to restart the web server only
jsmith  ALL=(ALL)  /bin/systemctl restart httpd

# Allow the 'developers' group (note the % prefix) to use sudo
%developers  ALL=(ALL)  ALL

# Allow developers group to run specific commands without password
%developers  ALL=(ALL)  NOPASSWD: /usr/bin/git, /usr/bin/npm

# Aliases make complex policies readable
User_Alias    WEBADMINS = alice, bob, carol
Cmnd_Alias    WEBSERVICES = /bin/systemctl restart httpd, /bin/systemctl restart nginx
WEBADMINS  ALL=(ALL)  WEBSERVICES

# Restrict to specific hosts
jsmith  webserver01=(ALL)  ALL
```

The four-field structure: WHO runs the command, on WHICH HOST, AS WHICH USER, running WHAT COMMANDS. The `ALL` keyword means "no restriction on that field."

---

### Slide 5 — The wheel Group

On RHEL/CentOS/Fedora systems, the `wheel` group is pre-configured in sudoers to have full sudo access. This is the conventional way to grant admin privileges.

```bash
# Check sudoers for wheel group (RHEL)
grep wheel /etc/sudoers
# %wheel  ALL=(ALL)  ALL   (or with NOPASSWD variant)

# Add a user to the wheel group
sudo usermod -aG wheel jsmith

# On Debian/Ubuntu, the equivalent group is 'sudo'
sudo usermod -aG sudo jsmith

# Verify group membership immediately
groups jsmith
id jsmith
```

After adding a user to the wheel or sudo group, the change takes effect at the next login. Existing sessions do not automatically receive the new group membership.

---

### Slide 6 — Switching Users with su

While `sudo` is preferred, `su` (switch user) still appears on the exam and in legacy environments.

```bash
# Switch to root (non-login shell — keeps current environment)
su

# Switch to root with a full login shell (reads root's profile)
su -

# Switch to another user
su - jsmith

# Run a single command as root (then return)
su -c "systemctl restart sshd"

# Run a command as another user
su -c "whoami" jsmith
```

The key distinction: `su -` gives you a full login environment — root's PATH, root's home directory, root's shell configuration. Plain `su` inherits your current environment, which can cause "command not found" errors when root's binaries are not in the inherited PATH.

---

### Slide 7 — Introduction to PAM

PAM — Pluggable Authentication Modules — is the framework that Linux uses to authenticate users for all kinds of services. SSH uses PAM. Login uses PAM. sudo uses PAM. Even screen savers use PAM.

The beauty of PAM is separation of concerns: application developers write their software to make PAM calls, and system administrators configure authentication policy separately without touching application code.

PAM configuration lives in `/etc/pam.d/`. Each file corresponds to a service:

```bash
# List PAM service files
ls /etc/pam.d/

# Common files:
# /etc/pam.d/sshd      — SSH authentication
# /etc/pam.d/login     — console login
# /etc/pam.d/sudo      — sudo authentication
# /etc/pam.d/passwd    — password changes
# /etc/pam.d/common-auth  (Debian) or /etc/pam.d/system-auth (RHEL)

# View the sudo PAM configuration
cat /etc/pam.d/sudo
```

---

### Slide 8 — PAM Configuration File Structure

Each line in a PAM configuration file has four fields:

```
type   control   module-path   module-arguments
```

The **type** is the management group:

- `auth` — verifies the user's identity (checks password)
- `account` — checks account validity (not expired, not locked)
- `password` — handles password updates
- `session` — sets up and tears down the user session (mount home, set limits)

The **control** flag determines what happens when a module succeeds or fails:

- `required` — must succeed; failure is noted but PAM continues evaluating
- `requisite` — must succeed; immediate failure if it fails
- `sufficient` — if this succeeds and no prior required module failed, accept; skip remaining
- `optional` — result doesn't matter unless it's the only module for this type

```bash
# Example: /etc/pam.d/sshd excerpt
# auth    required      pam_sepermit.so
# auth    substack      password-auth
# auth    include       postlogin
# account required      pam_nologin.so

# Common PAM modules on the exam:
# pam_unix.so      — traditional Unix password authentication
# pam_ldap.so      — LDAP authentication
# pam_limits.so    — apply resource limits from /etc/security/limits.conf
# pam_tally2.so    — account lockout after failed attempts (older systems)
# pam_faillock.so  — account lockout (modern replacement for pam_tally2)
# pam_pwquality.so — password complexity enforcement
```

---

### Slide 9 — Password Quality with PAM

`pam_pwquality.so` enforces password complexity rules. Its configuration file is `/etc/security/pwquality.conf`.

```bash
# View password quality settings
cat /etc/security/pwquality.conf

# Key parameters:
# minlen = 12        — minimum password length
# dcredit = -1       — require at least 1 digit (-N means require N)
# ucredit = -1       — require at least 1 uppercase
# lcredit = -1       — require at least 1 lowercase
# ocredit = -1       — require at least 1 special character
# maxrepeat = 3      — no more than 3 consecutive identical characters
# difok = 5          — must differ from old password by 5 characters

# Alternatively, set on the PAM module line:
# password  requisite  pam_pwquality.so retry=3 minlen=12 dcredit=-1

# Account lockout with pam_faillock (RHEL 8+):
# auth  required  pam_faillock.so preauth silent audit deny=5 unlock_time=600

# Check lockout status
sudo faillock --user jsmith

# Reset lockout
sudo faillock --user jsmith --reset
```

---

### Slide 10 — Practical Scenarios: Exam-Style Walkthrough

Let's work through three scenarios you will encounter on the Linux+ exam.

**Scenario 1: New employee onboarding**

```bash
# Create account, set password, add to groups, force first-login password change
sudo useradd -m -c "Alice Wilson, DevOps" -s /bin/bash -G developers,docker awilson
sudo passwd awilson
sudo chage -d 0 awilson         # Expire immediately → forced change at login
sudo chage -M 90 -W 14 awilson  # 90-day max, 14-day warning
```

**Scenario 2: Grant limited sudo access to a contractor**

```bash
# Create the account
sudo useradd -m -s /bin/bash -e 2025-06-30 contractor1

# Create a targeted sudoers rule
sudo visudo -f /etc/sudoers.d/contractors
# Add this line:
# contractor1  ALL=(ALL)  NOPASSWD: /bin/systemctl status *, /usr/bin/journalctl
```

**Scenario 3: Disable an account for an employee on leave**

```bash
# Lock the account (immediate effect)
sudo usermod -L jsmith
# Or with passwd:
sudo passwd -l jsmith

# Set expiration to today as a double lock
sudo chage -E $(date +%Y-%m-%d) jsmith

# Verify all sessions are terminated
sudo pkill -u jsmith
sudo w | grep jsmith
```

---

### Slide 11 — Key Files Quick Reference

For the exam, you must know these files cold:

| File | Purpose |
|---|---|
| `/etc/passwd` | User account definitions (7 fields) |
| `/etc/shadow` | Password hashes and aging (9 fields) |
| `/etc/group` | Group definitions (4 fields) |
| `/etc/gshadow` | Group passwords and admins |
| `/etc/sudoers` | sudo policy (edit only with visudo) |
| `/etc/sudoers.d/` | Drop-in sudo policy files |
| `/etc/pam.d/` | PAM configuration per service |
| `/etc/security/pwquality.conf` | Password complexity rules |
| `/etc/login.defs` | Default UID/GID ranges, password aging defaults |
| `/etc/default/useradd` | Default values for useradd |
| `/etc/skel/` | Template files for new home directories |

---

### Slide 12 — CompTIA Linux+ Exam Tips

The Linux+ exam tests both knowledge and application. Here are the highest-yield points for this module:

- Know all seven fields of `/etc/passwd` in order — UID, GID positions matter
- Know all nine fields of `/etc/shadow` — especially what `!` in the hash means (locked)
- `usermod -aG` vs `usermod -G` — the `-a` flag is a common exam trap
- `visudo` is the ONLY correct way to edit sudoers — never direct editing
- PAM control flags: `required` vs `requisite` vs `sufficient` — subtle but tested
- `chage -d 0` forces password reset at next login — common onboarding step
- `find / -nouser` locates orphaned files after account deletion
- The `wheel` group (RHEL) and `sudo` group (Debian) grant administrative access
- `getent passwd` queries all name sources, not just local files

```bash
# Quick study commands — run these in your lab VM:
id                          # Show current user identity
who                         # Show who is logged in
w                           # Show who is logged in with activity
last                        # Show login history
lastlog                     # Show last login for all accounts
getent passwd               # Query all users via NSS
getent group                # Query all groups via NSS
```

---

### Slide 13 — Module 07 Wrap-Up

You have now completed both parts of Module 7. Here is what you should be able to do:

- Create, modify, and delete user accounts using `useradd`, `usermod`, `userdel`
- Set passwords and aging policy with `passwd` and `chage`
- Manage groups with `groupadd`, `groupmod`, `groupdel`, `gpasswd`
- Read and interpret `/etc/passwd`, `/etc/shadow`, and `/etc/group`
- Configure granular sudo access with `visudo` and the sudoers syntax
- Explain PAM management types and control flags
- Enforce password complexity with `pam_pwquality`

Head over to the Reading Guide for deeper dives into each topic, then complete the Lab where you will build a complete user management environment from scratch. The quiz at the end covers all content from both video parts.

See you in Module 8, where we cover file system permissions and ownership.
