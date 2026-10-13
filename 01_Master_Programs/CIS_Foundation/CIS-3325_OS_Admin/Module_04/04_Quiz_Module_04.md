# Quiz: Module 04 - User and Group Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

An administrator runs a script that produces both normal output and error messages, and wants
to save everything to a single log file. Which command correctly redirects both standard output
and standard error to output.log?

- A) ./script.sh > output.log
- B) ./script.sh >> output.log
- C) ./script.sh > output.log 2>&1
- D) ./script.sh < output.log

Correct Answer: C) ./script.sh > output.log 2>&1

Distractor Analysis:

- Why A is incorrect: The > operator redirects only stdout (file descriptor 1). Error messages on stderr (file descriptor 2) still print to the terminal and are not captured.
- Why B is incorrect: >> appends stdout to the file but still does not capture stderr. Errors continue printing to the screen.
- Why D is incorrect: The < operator feeds a file into stdin as input for the script. This does not capture any output from the script.

---

**Question 2**

A new web server service has been installed and started manually. After a reboot the service is
not running. Which command ensures the service starts automatically on every future boot?

- A) systemctl start nginx
- B) systemctl enable nginx
- C) systemctl reload nginx
- D) systemctl status nginx

Correct Answer: B) systemctl enable nginx

Distractor Analysis:

- Why A is incorrect: systemctl start turns the service on only for the current running session. It has no effect on whether the service starts at the next boot.
- Why C is incorrect: systemctl reload tells a running service to re-read its configuration without dropping active connections. It does not configure boot-time behavior.
- Why D is incorrect: systemctl status displays whether the service is currently active or inactive and shows recent log lines. It makes no configuration changes.

---

**Question 3**

An administrator wants to add an existing user alice to the developers group without removing
her from any groups she currently belongs to. Which command is correct?

- A) usermod -G developers alice
- B) usermod -aG developers alice
- C) groupmod -a alice developers
- D) useradd -G developers alice

Correct Answer: B) usermod -aG developers alice

Distractor Analysis:

- Why A is incorrect: usermod -G developers alice replaces ALL of alice's current supplementary groups with only developers, removing her from every other group she was previously a member of. The -a (append) flag is required to avoid this.
- Why C is incorrect: groupmod is used to rename a group or change its GID, not to add members. This command would produce an error.
- Why D is incorrect: useradd creates a new user account. Running it against an existing username will either fail or cause unexpected behavior.

---

**Question 4**

An administrator needs to lock a user account named bob so he cannot log in, but without
deleting the account or its files. Which command is most appropriate?

- A) userdel bob
- B) passwd -d bob
- C) usermod -L bob
- D) chown root /home/bob

Correct Answer: C) usermod -L bob

Distractor Analysis:

- Why A is incorrect: userdel bob deletes the user account entirely. Adding -r also removes the home directory and mail spool. This is destructive and does not preserve the account.
- Why B is incorrect: passwd -d bob removes (deletes) bob's password, which may allow passwordless login on some configurations - the opposite of the intended effect.
- Why D is incorrect: Changing ownership of the home directory to root does not prevent the user from logging in. It only prevents them from writing to their own home directory.

---

**Question 5**

Which file should always be used to edit /etc/sudoers, and why?

- A) A standard text editor like nano, because /etc/sudoers is a plain text file.
- B) visudo, because it locks the file during editing and validates syntax before saving, preventing lockouts from typos.
- C) vi with root privileges, because only vi can write to protected system configuration files.
- D) usermod --sudoers, because direct editing of /etc/sudoers is prohibited by the kernel.

Correct Answer: B) visudo, because it locks the file during editing and validates syntax before saving, preventing lockouts from typos.

Distractor Analysis:

- Why A is incorrect: While /etc/sudoers is technically a text file, editing it with a standard editor risks saving a syntax error. A single typo can prevent all sudo access system-wide, requiring recovery mode to fix.
- Why C is incorrect: Any text editor can write to root-owned files when run with sudo. The reason to use visudo is syntax checking, not vi-specific write capabilities.
- Why D is incorrect: There is no usermod --sudoers option. The kernel does not prohibit direct editing of /etc/sudoers. It is a deliberate administrative choice to use visudo for safety.

---

**Question 6**

An administrator needs to create a user account for an automated backup service. The account
should be a system account that cannot be used for interactive login. Which useradd command is
correct?

- A) useradd -m -s /bin/bash backupsvc
- B) useradd -r -s /usr/sbin/nologin backupsvc
- C) useradd -G root -s /bin/sh backupsvc
- D) useradd backupsvc && passwd -l backupsvc

Correct Answer: B) useradd -r -s /usr/sbin/nologin backupsvc

Distractor Analysis:

- Why A is incorrect: -m creates a home directory and -s /bin/bash gives a full interactive shell. This creates a regular interactive user account, not a service account. Service accounts should not have login shells.
- Why C is incorrect: -G root adds the account to the root group, granting elevated group permissions that a backup service should not have. The principle of least privilege says service accounts should have minimal access.
- Why D is incorrect: passwd -l locks the account after creation, but the account still has the default shell (/bin/sh) and a UID in the regular user range (1000+). A properly created service account uses -r for a system UID and /usr/sbin/nologin for the shell.

---

**Question 7**

A Linux administrator creates a new user with the command useradd -m -s /bin/bash -e 2026-06-30
contractdev. What does the -e flag accomplish?

- A) Sets the password expiration date to June 30, 2026, after which the user must change their password.
- B) Sets the account expiration date to June 30, 2026, after which the account is locked and cannot be used for login.
- C) Sets the home directory expiration to automatically delete /home/contractdev on June 30, 2026.
- D) Enables extended permissions for the account, granting temporary sudo access until June 30, 2026.

Correct Answer: B) Sets the account expiration date to June 30, 2026, after which the account is locked and cannot be used for login.

Distractor Analysis:

- Why A is incorrect: Password expiration is controlled by chage -M (maximum days) or chage -E for expiration. The -e flag in useradd and usermod sets the account expiration date, not the password expiration date. These are separate concepts stored in different /etc/shadow fields.
- Why C is incorrect: useradd -e does not delete any files. Account expiration only prevents login. The home directory persists indefinitely unless explicitly removed with userdel -r.
- Why D is incorrect: There is no "extended permissions" or automatic sudo access concept in Linux. useradd -e strictly controls account login availability based on a date.

---

**Question 8**

The /etc/passwd file on a Linux server shows the following entry for a user named sysmonitor:

sysmonitor:x:998:998:System Monitor:/var/sysmonitor:/bin/false

What does the /bin/false shell entry indicate about this account?

- A) The sysmonitor account has an incorrect shell path and will generate errors when processes run as this user.
- B) The /bin/false shell immediately exits with a failure code when called, preventing interactive login while allowing the system to run processes as sysmonitor.
- C) The account is permanently disabled and cannot be used for any purpose including running background services.
- D) The sysmonitor account is a root-equivalent account that can run any command without authentication.

Correct Answer: B) The /bin/false shell immediately exits with a failure code when called, preventing interactive login while allowing the system to run processes as sysmonitor.

Distractor Analysis:

- Why A is incorrect: /bin/false is a valid executable on every Linux system. It is intentionally used as a no-login shell. It generates no errors - it simply exits with a non-zero code when executed as a login shell.
- Why C is incorrect: /bin/false prevents interactive login but does not prevent the system from running processes as sysmonitor. Services, cron jobs, and other system processes can still be configured to run under this identity.
- Why D is incorrect: UID 998 is a system account in the normal range, not UID 0 (root). Nothing about /bin/false or this entry grants elevated privileges. The account has standard permissions dictated by its group memberships.

---

**Question 9**

An administrator needs to determine all groups that a user named alice is a member of, including
her primary group. Which command displays this information?

- A) cat /etc/passwd | grep alice
- B) groups alice
- C) getent group alice
- D) grep alice /etc/shadow

Correct Answer: B) groups alice

Distractor Analysis:

- Why A is incorrect: /etc/passwd shows only the primary GID (field 4) for alice. It does not list supplementary group memberships. Those are stored in /etc/group.
- Why C is incorrect: getent group alice queries the group database for a group named alice, not groups that alice is a member of. This would show the alice group (her primary group entry) but not all groups she belongs to.
- Why D is incorrect: /etc/shadow contains password hashes and aging information. It has no group membership data.

---

**Question 10**

After running usermod -aG docker labadmin on a running Ubuntu server, the administrator
immediately tests whether the change worked by running docker ps. The command returns
"permission denied." What is the most likely reason?

- A) The docker group does not exist. The administrator must first create it with groupadd docker.
- B) The usermod command failed silently because only root can belong to the docker group.
- C) Group membership changes from usermod take effect only after the user logs out and logs back in. The current shell session still has the old group list.
- D) The administrator must run systemctl restart docker to apply the new group membership to the Docker daemon.

Correct Answer: C) Group membership changes from usermod take effect only after the user logs out and logs back in. The current shell session still has the old group list.

Distractor Analysis:

- Why A is incorrect: If the docker group did not exist, usermod -aG would fail with an error. The scenario implies the command ran successfully. Docker installation creates the docker group automatically.
- Why B is incorrect: Any user can belong to the docker group. Group membership has no user restrictions by type or privilege level. The limitation is that being in the docker group itself grants significant privileges equivalent to root on some systems.
- Why D is incorrect: Restarting the docker daemon affects the Docker service process, not the user's shell environment. The user's shell retains its original group list until a new login session is created. Running newgrp docker would activate the group in the current shell without logging out.

---

Questions 11-20 — 5 pts each

---

**Question 11**

An administrator needs to force a user named newstaff to change their password on their
very first login. Which command achieves this without deleting or resetting the password?

- A) passwd --expire newstaff
- B) chage -d 0 newstaff
- C) usermod --force-reset newstaff
- D) passwd -e newstaff

Correct Answer: D) passwd -e newstaff

Distractor Analysis:

- Why A is incorrect: passwd --expire is not valid syntax. The correct flag is passwd -e (expire) or chage -d 0. The --expire flag does not exist for the passwd command.
- Why B is incorrect: chage -d 0 also forces a password change at next login by setting the last password change date to epoch day 0 (January 1, 1970). Both B and D are technically valid, but passwd -e is the more direct single-command approach and is what CompTIA tests.
- Why C is incorrect: usermod --force-reset is not a valid option. usermod manages account attributes like shell, home directory, and group membership, but not password reset forcing.

---

**Question 12**

A systems administrator creates a user with useradd -m -s /bin/bash -c "Web App Service"
-r webapp. Which statement correctly describes the resulting account?

- A) The account is a regular user account with UID above 1000 and a home directory at /home/webapp.
- B) The account is a system account with a UID below 1000 (system range), a home directory, and /bin/bash as its shell.
- C) The account is created without a home directory because -r system accounts never get home directories.
- D) The account cannot run any processes because system accounts are blocked by PAM.

Correct Answer: B) The account is a system account with a UID below 1000 (system range), a home directory, and /bin/bash as its shell.

Distractor Analysis:

- Why A is incorrect: The -r flag creates a system account with a UID in the system range (below 1000 on most distributions). Without -r, the UID would be in the regular user range (1000+).
- Why C is incorrect: By default, useradd -r does not create a home directory. However, the -m flag was explicitly included in this command, which forces home directory creation even for system accounts. The -m flag overrides the default no-home behavior of -r.
- Why D is incorrect: System accounts run processes constantly. Daemons, web servers, and database services all run under system accounts. PAM does not block process execution based on UID range.

---

**Question 13**

Which /etc/sudoers entry allows only the user alice to run the systemctl command as root
with no password prompt, while restricting all other sudo commands?

- A) alice ALL=(ALL) NOPASSWD: ALL
- B) alice ALL=(root) NOPASSWD: /usr/bin/systemctl
- C) alice ALL=(ALL) /usr/bin/systemctl
- D) %alice ALL=(root) NOPASSWD: /usr/bin/systemctl

Correct Answer: B) alice ALL=(root) NOPASSWD: /usr/bin/systemctl

Distractor Analysis:

- Why A is incorrect: NOPASSWD: ALL grants alice passwordless access to every command on every host as any user. This violates least privilege and is far too permissive.
- Why C is incorrect: This entry allows alice to run systemctl as any user but still requires her sudo password. The question specifies no password prompt, which requires the NOPASSWD: keyword.
- Why D is incorrect: The % prefix in sudoers denotes a group name, not a user name. %alice applies the rule to the group named alice, not the user named alice.

---

**Question 14**

An administrator reviews /etc/login.defs and finds the line PASS_MAX_DAYS 90. What does
this setting control?

- A) The maximum number of days a session can remain idle before the user is logged out.
- B) The maximum number of days a password is valid before the user must change it.
- C) The maximum number of failed login attempts before the account is locked.
- D) The maximum number of days after account creation before the first password must be set.

Correct Answer: B) The maximum number of days a password is valid before the user must change it.

Distractor Analysis:

- Why A is incorrect: Session idle timeout is controlled by shell variables like TMOUT or by PAM's pam_limits module and /etc/security/limits.conf. It has nothing to do with /etc/login.defs PASS_MAX_DAYS.
- Why C is incorrect: Failed login lockout is configured in PAM with pam_faillock or pam_tally2, not in /etc/login.defs. The relevant /etc/login.defs parameter for login attempts is LOGIN_RETRIES.
- Why D is incorrect: The time before first password change after account creation is not what PASS_MAX_DAYS tracks. PASS_MAX_DAYS is about password age from the last change date, not from account creation.

---

**Question 15**

After running getent passwd webdev, an administrator sees:

webdev:x:1001:1001:Web Developer:/home/webdev:/bin/bash

The administrator wants to change webdev's login shell to /usr/sbin/nologin to disable
interactive login. Which command is correct?

- A) chsh -s /usr/sbin/nologin webdev
- B) usermod -s /usr/sbin/nologin webdev
- C) passwd --shell /usr/sbin/nologin webdev
- D) Both A and B

Correct Answer: D) Both A and B

Distractor Analysis:

- Why A alone is partially correct: chsh -s changes the login shell for a user. When run with sudo for another user's account, it correctly updates /etc/passwd.
- Why B alone is partially correct: usermod -s is the standard administrative tool for changing a user's shell attribute. Both commands write the same field in /etc/passwd.
- Why C is incorrect: The passwd command manages password-related attributes (setting, locking, expiring). It has no --shell option. Shell changes are made with usermod or chsh.

---

**Question 16**

A security policy requires all user passwords on a server to be at least 12 characters with
complexity requirements. Which PAM module and configuration file enforce this policy on
Ubuntu 22.04?

- A) pam_unix.so with settings in /etc/pam.d/login
- B) pam_pwquality.so with settings in /etc/security/pwquality.conf
- C) pam_cracklib.so with settings in /etc/login.defs
- D) pam_limits.so with settings in /etc/security/limits.conf

Correct Answer: B) pam_pwquality.so with settings in /etc/security/pwquality.conf

Distractor Analysis:

- Why A is incorrect: pam_unix.so handles standard Unix password authentication but does not enforce complexity requirements. It verifies passwords against /etc/shadow but imposes no minlen or character class rules.
- Why C is incorrect: pam_cracklib.so is the older predecessor to pam_pwquality.so. On Ubuntu 22.04, pam_pwquality.so has replaced it. /etc/login.defs does not configure PAM module parameters.
- Why D is incorrect: pam_limits.so enforces resource limits (open files, CPU time, process count) per user or group from /etc/security/limits.conf. It has nothing to do with password complexity.

---

**Question 17**

A Linux administrator needs to display the password aging information for the user bob,
including the last change date, minimum days, maximum days, and expiry warning. Which
command shows this?

- A) passwd -S bob
- B) chage -l bob
- C) getent shadow bob
- D) cat /etc/shadow | grep bob

Correct Answer: B) chage -l bob

Distractor Analysis:

- Why A is incorrect: passwd -S bob shows a brief one-line password status (locked, usable, or no password) with a date and policy summary. It is less detailed than chage -l and uses a different format.
- Why C is incorrect: getent shadow bob requires root and displays the raw /etc/shadow entry in colon-delimited format with epoch-day integers, which requires manual conversion to be readable. chage -l presents the information in a human-readable labeled format.
- Why D is incorrect: Direct cat of /etc/shadow also displays raw epoch values. On most systems cat /etc/shadow is not readable by non-root users. chage -l requires sudo but formats the output clearly.

---

**Question 18**

The /etc/skel directory contains template files. When is the content of /etc/skel relevant?

- A) When an existing user's home directory is rebuilt by running usermod -m.
- B) When a new user account is created with useradd -m, the files from /etc/skel are copied to the new home directory.
- C) When a user logs in via SSH, /etc/skel files are read to configure the remote session.
- D) When the root user runs cp -r /etc/skel /home/username to manually provision a user.

Correct Answer: B) When a new user account is created with useradd -m, the files from /etc/skel are copied to the new home directory.

Distractor Analysis:

- Why A is incorrect: usermod -m moves an existing home directory. It does not repopulate it from /etc/skel. /etc/skel is only consulted during initial home directory creation.
- Why C is incorrect: SSH sessions read ~/.bashrc, ~/.bash_profile, and similar files from the user's existing home directory. /etc/skel has no role after the account is created.
- Why D is incorrect: While manually copying /etc/skel would produce a similar result, this is not when /etc/skel is automatically used. Its automatic use is exclusively triggered by useradd -m during account creation.

---

**Question 19**

An administrator runs su - bob and is prompted for bob's password. After authenticating,
the prompt changes and the administrator runs pwd. Which directory is shown?

- A) The directory the administrator was in before running su -.
- B) /root, because su - always switches to the root home directory.
- C) /home/bob, because su - starts a login shell that loads bob's full environment and places the session in bob's home directory.
- D) /tmp, because su - uses a clean environment with no home directory context.

Correct Answer: C) /home/bob, because su - starts a login shell that loads bob's full environment and places the session in bob's home directory.

Distractor Analysis:

- Why A is incorrect: su - (with the dash) is a login shell switch. It changes the working directory to the target user's home directory. su without the dash stays in the calling user's current directory.
- Why B is incorrect: su - root (or just su -) switches to root's home (/root). su - bob switches to bob's home (/home/bob). The destination depends on the target user.
- Why D is incorrect: /tmp is not associated with su - behavior. The login shell reads ~/.bash_profile and ~/.profile which set HOME to the user's home directory, so pwd shows that directory.

---

**Question 20**

A user account named oldadmin has been terminated. The administrator needs to prevent any
login while preserving all files and audit trails, and must not delete the account. Which
two actions accomplish this most effectively?

- A) rm -rf /home/oldadmin && passwd -d oldadmin
- B) usermod -L oldadmin && usermod -e 1 oldadmin
- C) userdel oldadmin && chattr +i /var/log/auth.log
- D) passwd -l oldadmin && chage -E 0 oldadmin

Correct Answer: D) passwd -l oldadmin && chage -E 0 oldadmin

Distractor Analysis:

- Why A is incorrect: rm -rf /home/oldadmin destroys files and audit evidence, violating the requirement to preserve files. passwd -d removes the password (allows passwordless login in some configurations) rather than preventing login.
- Why B is incorrect: usermod -L locks the password field (same effect as passwd -l) but usermod -e 1 sets the account expiry to January 2, 1970 (one day after epoch), which is essentially expired but an unusual convention. chage -E 0 is cleaner. The combination is functionally similar to D but less standard.
- Why C is incorrect: userdel deletes the account entirely, violating the requirement not to delete it. chattr +i makes a file immutable, which is an unrelated operation that would prevent log rotation.

---

Note: For Question 11, both passwd -e and chage -d 0 are technically valid approaches to force password expiry. On the CompTIA Linux+ exam, passwd -e (or passwd --expire) is the primary tested syntax.
