# Video Script: Module 04 - User and Group Management (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - sudo, Security, and Practical Application

---

### Opening

Welcome back to Part 2 of Module 04. In Part 1 we built a complete picture of Linux user and
group management: the identity files, creating and modifying accounts, password management, and
group operations. In Part 2 we tackle sudo - the most important privilege escalation tool in
Linux administration - and cover account security best practices that appear heavily on the exam.

---

### Section 1: Understanding sudo

sudo stands for "substitute user do" or "superuser do." It allows a permitted user to execute
a command as another user, typically root, according to rules defined in /etc/sudoers.

Why not just log in as root? Several important reasons:

Accountability. When you use sudo, every command is logged with your username. The log entry
shows that labadmin ran "sudo rm -rf /important" - not that root did it anonymously.

Blast radius limitation. Running everything as root means a mistake or a compromised application
affects the entire system. With sudo, each command elevation is a deliberate, logged, audited
action.

Minimum privilege. sudo can be configured to allow specific users to run only specific commands
as root, not everything. This is the principle of least privilege.

[SHOW TERMINAL]

```bash
sudo whoami
```

This runs whoami as root. It returns "root" - confirming you are executing with root privileges.

```bash
sudo -i
```

This drops you into a full root shell with root's environment variables loaded. Use with caution.
Exit with exit or Ctrl+D.

```bash
sudo -s
```

Similar to sudo -i but inherits your current environment. Slightly different but both give you
a root shell.

---

### Section 2: The /etc/sudoers File

The /etc/sudoers file controls who can use sudo and what they can do with it.

[SHOW TERMINAL]

CRITICAL: Never edit /etc/sudoers with a regular text editor like nano or vi directly.

```bash
sudo visudo
```

visudo opens /etc/sudoers in your default editor BUT validates the syntax before saving. If you
introduce a syntax error, visudo refuses to save and asks you to fix it. A syntax error in
/etc/sudoers can lock out all sudo access, potentially requiring recovery mode to fix.

Let us look at the key lines in a default Ubuntu sudoers file:

```
root    ALL=(ALL:ALL) ALL
```

This grants root the ability to run any command as any user on any host.

```
%sudo   ALL=(ALL:ALL) ALL
```

The % prefix means group. Any user in the sudo group can run any command as root with a password.

```
labadmin ALL=(ALL:ALL) ALL
```

This grants labadmin full sudo access. This is equivalent to being in the sudo group.

For limited access, you can restrict to specific commands:

```
alice ALL=(root) /usr/bin/systemctl restart nginx
```

This grants alice permission to restart nginx (and nothing else) using sudo.

To allow sudo without a password prompt (use with caution in automation):

```
%automation ALL=(ALL) NOPASSWD: /usr/bin/systemctl
```

---

### Section 3: Adding Users to sudo

[SHOW TERMINAL]

On Ubuntu/Debian systems, users in the sudo group have full sudo access.

```bash
sudo usermod -aG sudo alice
id alice
```

After this change, alice can use sudo for any command.

On RHEL/CentOS systems, the wheel group is used instead:

```bash
sudo usermod -aG wheel alice
```

This is a common exam distractor. Ubuntu: sudo group. RHEL: wheel group.

---

### Section 4: su - Switch User

su (substitute user) switches to another user account directly without logging out.

[SHOW TERMINAL]

```bash
su - alice
```

The hyphen (-) is critical. It means "login shell" - loads alice's environment variables,
changes to her home directory, and runs her login scripts. Without the hyphen:

```bash
su alice
```

This switches to alice but keeps your current environment variables. This can cause unexpected
behavior because PATH and other variables may not match alice's setup.

To switch to root:

```bash
su -
```

This prompts for the root password. On Ubuntu, root has no password by default, so this fails.
On RHEL systems where root has a password, this works.

The difference between sudo -i and su - root: sudo uses your password, su uses the target
user's password. In production, sudo is preferred because su requires sharing the root password.

---

### Section 5: Account Security Best Practices

[SHOW TERMINAL]

**Lock accounts when users leave the organization:**

```bash
sudo usermod -L formeremployee
```

This immediately prevents login. Do not delete the account until you have confirmed all files
and data are handled properly.

**Set account expiration for temporary users:**

```bash
sudo usermod -e 2026-12-31 contractworker
sudo chage -l contractworker
```

When the expiration date passes, the account is automatically locked.

**Force password change on next login:**

```bash
sudo chage -d 0 newuser
```

Setting the last-changed date to 0 (day 0 of the epoch) forces an immediate password change
on next login.

**Restrict login shell for service accounts:**

```bash
sudo useradd -s /usr/sbin/nologin webservice
```

/usr/sbin/nologin prints a polite message and exits. /bin/false exits immediately with no
message. Both prevent interactive login. Use these for all service accounts.

**Check for accounts with empty passwords:**

```bash
sudo awk -F: '($2 == "" ) { print $1 }' /etc/shadow
```

Any output means an account has no password set - a serious security vulnerability.

**Check for accounts with UID 0 besides root:**

```bash
awk -F: '($3 == "0") { print }' /etc/passwd
```

Only the root account should have UID 0. Any other account with UID 0 has full root privileges.

---

### Section 6: The /etc/skel Directory

When useradd -m creates a home directory, it copies the contents of /etc/skel into the new
home directory.

[SHOW TERMINAL]

```bash
ls -la /etc/skel/
```

By default you will see .bashrc, .bash_logout, and .profile. These are the default shell
configuration files every new user gets.

To standardize environments for new users, add files to /etc/skel:

```bash
sudo cp /etc/motd /etc/skel/welcome.txt
sudo useradd -m testuser
ls -la /home/testuser/
```

The testuser's home directory now contains welcome.txt, copied from /etc/skel.

This is used in production environments to deploy standard shell configurations, SSH config
templates, company policy acknowledgment files, or default application settings.

---

### Section 7: Exam Scenarios

Let me walk through the specific scenarios tested on the exam.

[SHOW TERMINAL]

Scenario: Add alice to the docker group without removing her from other groups.

WRONG: sudo usermod -G docker alice (replaces all groups)
CORRECT: sudo usermod -aG docker alice (appends to existing groups)

Scenario: Prevent bob from logging in while preserving all his files.

CORRECT: sudo usermod -L bob
NOT: sudo userdel bob (this removes the account)

Scenario: Create a service account for a web application with no login capability.

CORRECT: sudo useradd -r -s /usr/sbin/nologin -d /var/www -c "Web Application" webapp

Scenario: Edit the sudoers file safely.

ONLY CORRECT: sudo visudo
WRONG: sudo nano /etc/sudoers (no syntax checking - one typo locks everyone out)

Scenario: Grant a user limited sudo access to restart only one service.

In visudo: alice ALL=(root) /usr/bin/systemctl restart apache2

---

### Section 8: Exam Tips

The -aG trap is the single most common wrong answer in user management questions. When a
question says "add user to a group without removing existing group memberships," the answer
is always usermod -aG, never usermod -G.

visudo is always the correct answer for editing /etc/sudoers. There is no acceptable alternative
for production use.

Ubuntu uses the sudo group for sudo access. RHEL/CentOS uses the wheel group. This distinction
is tested.

System accounts (service accounts) should have /usr/sbin/nologin or /bin/false as their shell.
This prevents interactive login while allowing the system to run processes as that user.

The /etc/skel directory provides template files for new home directories. Know this for exam
questions about standardizing new user environments.

---

### Lab Preview

This week's lab has you creating multiple user accounts with useradd, setting passwords, adding
users to groups with usermod -aG, verifying with id, locking and unlocking accounts, and
configuring a sudo entry with visudo. Follow the instructions carefully, especially around the
-aG versus -G distinction.

---

### Summary

Module 04 covers the complete Linux user and group management lifecycle: the identity files
(/etc/passwd, /etc/shadow, /etc/group), creating accounts with useradd, modifying with usermod,
deleting with userdel, managing passwords with passwd and chage, and configuring privilege
elevation with sudo and visudo.

Module 05 covers package management - how you install, update, and remove software from Linux.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
