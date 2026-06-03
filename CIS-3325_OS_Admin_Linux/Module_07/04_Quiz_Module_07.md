# Quiz: Module 07 — User and Group Administration

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. A score of 80 or higher is required to advance to Module 08.

---

**Question 1**

A Linux administrator needs to create a new user named `devuser` with a home directory, the bash shell, and membership in the `developers` group as a supplementary group. Which command accomplishes all of this correctly?

A. `useradd -d /home/devuser -s /bin/bash -G developers devuser`

B. `useradd -m -s /bin/bash -G developers devuser`

C. `useradd -m -s /bin/bash -g developers devuser`

D. `adduser -home /home/devuser -shell bash -group developers devuser`

**Correct Answer:** B

**Explanation:** Option B uses `-m` to create the home directory, `-s` to set the shell, and `-G` to assign `developers` as a supplementary group. Option A is missing `-m` (required on Debian systems and good practice everywhere). Option C uses `-g` which sets the primary group, not supplementary. Option D uses invalid flag syntax.

---

**Question 2**

An administrator examines `/etc/shadow` and finds this entry for a user account:

```
jdoe:!$6$salt$hash:19500:0:99999:7:::
```

What does the `!` at the beginning of the password field indicate?

A. The account has no password set.

B. The account password uses an incompatible hashing algorithm.

C. The account is locked.

D. The account requires a password change at next login.

**Correct Answer:** C

**Explanation:** A `!` (or `!!`) prepended to the password hash in `/etc/shadow` indicates the account is locked. This is the result of `passwd -l username` or `usermod -L username`. Option A would show an empty field or `*`. Option D would show the last-changed date field set to 0.

---

**Question 3**

A junior administrator needs to add user `alice` to the `docker` group without removing her from any other groups. Which command is correct?

A. `usermod -G docker alice`

B. `usermod -g docker alice`

C. `usermod -aG docker alice`

D. `groupmod -a alice docker`

**Correct Answer:** C

**Explanation:** `usermod -aG` appends to the supplementary groups list. Without `-a`, the `-G` flag replaces all existing supplementary groups. Option B changes the primary group. Option D is not a valid `groupmod` syntax for adding members.

---

**Question 4**

Which file should NEVER be edited directly with a standard text editor?

A. `/etc/passwd`

B. `/etc/group`

C. `/etc/sudoers`

D. `/etc/shadow`

**Correct Answer:** C

**Explanation:** `/etc/sudoers` must only be edited with `visudo`, which locks the file and validates syntax before saving. A syntax error in `/etc/sudoers` can make sudo completely unusable, potentially locking administrators out. The other files can technically be edited directly, though it is safer to use the appropriate tools.

---

**Question 5**

An administrator wants to force user `newstaff` to change their password at their very first login. Which command accomplishes this?

A. `passwd -e newstaff`

B. `chage -d 0 newstaff`

C. `usermod --expire-password newstaff`

D. Both A and B are correct.

**Correct Answer:** D

**Explanation:** Both `passwd -e newstaff` and `chage -d 0 newstaff` expire the password immediately, forcing a change at next login. `passwd -e` sets the expiration flag; `chage -d 0` sets the last-changed date to epoch day 0, which is treated as immediately expired. Option C is not a valid flag.

---

**Question 6**

An administrator is reviewing the `/etc/passwd` file and sees this line:

```
webserver:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

What is the purpose of `/usr/sbin/nologin` in this entry?

A. It is a placeholder indicating the account has no shell configured.

B. It prevents interactive login for this service account.

C. It causes the account to be automatically locked after creation.

D. It is an error; service accounts should use `/bin/false`.

**Correct Answer:** B

**Explanation:** `/usr/sbin/nologin` (or `/sbin/nologin`) prevents interactive logins by immediately exiting with a message. This is the correct way to configure service accounts. Both `/sbin/nologin` and `/bin/false` are acceptable for this purpose, making option D incorrect.

---

**Question 7**

Which of the following sudoers rules allows members of the `webteam` group to restart the Apache service without entering a password?

A. `webteam ALL=(ALL) /bin/systemctl restart httpd`

B. `%webteam ALL=(ALL) NOPASSWD: /bin/systemctl restart httpd`

C. `@webteam ALL=(root) NOPASSWD: /bin/systemctl restart httpd`

D. `+webteam ALL=(ALL) /bin/systemctl restart httpd NOPASSWD`

**Correct Answer:** B

**Explanation:** In sudoers syntax, group names are prefixed with `%`. The `NOPASSWD:` tag must precede the command list. Option A is missing the `%` prefix and `NOPASSWD`. Option C uses an incorrect `@` prefix. Option D places `NOPASSWD` at the wrong position.

---

**Question 8**

In a PAM configuration file, a module is marked with the `requisite` control flag. What happens if this module fails?

A. Evaluation continues with the next module in the stack.

B. The failure is logged but the user is still permitted access.

C. Evaluation stops immediately and access is denied.

D. The module is skipped and results are ignored.

**Correct Answer:** C

**Explanation:** The `requisite` control flag causes immediate failure — if the module fails, PAM stops processing immediately and returns failure. This is different from `required`, which records the failure but continues evaluating remaining modules. `optional` ignores results. There is no built-in "log but permit" control flag.

---

**Question 9**

An administrator deletes user `olddev` without using the `-r` flag. What is the most likely consequence, and what command would help identify it?

A. The user's processes will be killed; use `ps aux | grep olddev`

B. The user's home directory and files remain, owned by the old UID; use `find / -nouser`

C. All files owned by the user are automatically deleted; no cleanup is needed

D. The account is moved to an archive in `/etc/passwd.d/`

**Correct Answer:** B

**Explanation:** Without `-r`, `userdel` removes the account from `/etc/passwd` and `/etc/shadow` but leaves the home directory and any files intact. These files become "orphaned" — owned by a UID with no corresponding account entry. `find / -nouser` locates files with no valid owner. Option C is incorrect; Linux does not auto-delete files. Option D does not exist.

---

**Question 10**

An administrator needs to configure a password policy requiring users to change passwords every 60 days, with a 10-day warning and a minimum of 2 days before they can change it again. Which `chage` command is correct for user `tsmith`?

A. `chage -M 60 -W 10 -m 2 tsmith`

B. `chage -x 60 -w 10 -n 2 tsmith`

C. `chage --max 60 --warn 10 --min 2 tsmith`

D. `passwd -x 60 -w 10 -n 2 tsmith`

**Correct Answer:** A

**Explanation:** `chage -M` sets maximum days (60), `-W` sets warning days (10), and `-m` sets minimum days (2). Option B uses lowercase flags that `chage` does not support (those are `passwd` flags). Option C shows long-option syntax that does not match `chage`'s actual options. Option D uses `passwd` which does support `-x`, `-w`, and `-n`, but only options A correctly uses `chage` with the right flag cases.
