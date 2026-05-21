# Quiz: Module 04 - User and Group Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator runs a script that produces both normal output and error messages, and wants to save everything to a single log file. Which command correctly redirects both standard output (stdout) and standard error (stderr) to `output.log`?
A) ./script.sh > output.log
B) ./script.sh >> output.log
C) ./script.sh > output.log 2>&1
D) ./script.sh < output.log
*   **Correct Answer:** C) ./script.sh > output.log 2>&1
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The `>` operator redirects only stdout (file descriptor 1). Error messages on stderr (file descriptor 2) still print to the terminal and are not captured.
    *   *Why B is incorrect:* `>>` appends stdout to the file but still does not capture stderr; errors will continue printing to the screen.
    *   *Why D is incorrect:* The `<` operator feeds a file into stdin as input for the script, not the reverse. This does not capture any output from the script.

---

---

**Question 2**
A new web server service has been installed and started manually. After a reboot the service is not running. Which command ensures the service starts automatically on every future boot?
A) systemctl start nginx
B) systemctl enable nginx
C) systemctl reload nginx
D) systemctl status nginx
*   **Correct Answer:** B) systemctl enable nginx
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `systemctl start` turns the service on only for the current running session. It has no effect on whether the service starts at the next boot.
    *   *Why C is incorrect:* `systemctl reload` tells a running service to re-read its configuration without dropping active connections. It does not configure boot-time behavior.
    *   *Why D is incorrect:* `systemctl status` displays whether the service is currently active or inactive and shows recent log lines. It makes no configuration changes.

---

---

**Question 3**
An administrator wants to add an existing user `alice` to the `developers` group without removing her from any groups she currently belongs to. Which command is correct?
A) usermod -G developers alice
B) usermod -aG developers alice
C) groupmod -a alice developers
D) useradd -G developers alice
*   **Correct Answer:** B) usermod -aG developers alice
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `usermod -G developers alice` replaces all of alice's current supplementary groups with only `developers`, removing her from every other group she was previously a member of. The `-a` (append) flag is required to avoid this.
    *   *Why C is incorrect:* `groupmod` is used to rename a group or change its GID, not to add members. This command would produce an error.
    *   *Why D is incorrect:* `useradd` creates a new user account. Running it against an existing username will either fail or create a duplicate entry depending on the system configuration.

---

**Question 4**
An administrator needs to lock a user account named `bob` so he cannot log in, but without deleting the account or its files. Which command is most appropriate?
A) userdel bob
B) passwd -d bob
C) usermod -L bob
D) chown root /home/bob
*   **Correct Answer:** C) usermod -L bob
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `userdel bob` deletes the user account entirely. Adding `-r` also removes the home directory and mail spool. This is destructive and does not preserve the account.
    *   *Why B is incorrect:* `passwd -d bob` removes (deletes) bob's password, which may allow passwordless login on some configurations — the opposite of the intended effect.
    *   *Why D is incorrect:* Changing ownership of the home directory to root does not prevent the user from logging in; it only prevents them from writing to their own home directory.

---

**Question 5**
Which file should always be used to edit `/etc/sudoers`, and why?
A) A standard text editor like `nano`, because `/etc/sudoers` is a plain text file.
B) `visudo`, because it locks the file during editing and validates syntax before saving, preventing lockouts from typos.
C) `vi` with root privileges, because only vi can write to protected system configuration files.
D) `usermod --sudoers`, because direct editing of `/etc/sudoers` is prohibited by the kernel.
*   **Correct Answer:** B) `visudo`, because it locks the file during editing and validates syntax before saving, preventing lockouts from typos.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While `/etc/sudoers` is technically a text file, editing it with a standard editor risks saving a syntax error. A single typo can prevent all sudo access system-wide, requiring recovery mode to fix.
    *   *Why C is incorrect:* Any text editor can write to root-owned files when run with sudo. The reason to use `visudo` is syntax checking, not vi-specific write capabilities.
    *   *Why D is incorrect:* There is no `usermod --sudoers` option. The kernel does not prohibit direct editing of `/etc/sudoers` — it is a deliberate administrative choice to use `visudo` for safety.

