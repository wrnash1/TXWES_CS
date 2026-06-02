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
