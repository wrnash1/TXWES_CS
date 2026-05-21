# Quiz: Module 16 - Final Exam Prep & CompTIA Linux+ Certification
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
A Linux administrator needs to extend logical volume `/dev/vg_data/lv_data` by 5 gigabytes and immediately make the new space available to a mounted ext4 filesystem without unmounting it. Which sequence of commands is correct?
A) lvextend -L +5G /dev/vg_data/lv_data && mkfs.ext4 /dev/vg_data/lv_data
B) lvextend -L +5G /dev/vg_data/lv_data && resize2fs /dev/vg_data/lv_data
C) vgextend vg_data /dev/sdd && mount -o remount /dev/vg_data/lv_data
D) lvresize -L +5G /dev/vg_data/lv_data && xfs_growfs /dev/vg_data/lv_data
*   **Correct Answer:** B) lvextend -L +5G /dev/vg_data/lv_data && resize2fs /dev/vg_data/lv_data
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running `mkfs.ext4` on an existing logical volume destroys all data on it by creating a new empty filesystem. `lvextend` grows the block device; `resize2fs` grows the filesystem non-destructively to fill the new space — `mkfs` is never the correct follow-up.
    *   *Why C is incorrect:* `vgextend` adds a new physical volume to a volume group to increase the VG's total capacity — it does not extend an existing logical volume. `mount -o remount` remounts with updated options but does not resize the filesystem.
    *   *Why D is incorrect:* `xfs_growfs` is the correct filesystem resize tool for XFS, not ext4. The scenario specifies an ext4 filesystem, which requires `resize2fs`. Using `xfs_growfs` on an ext4 filesystem would fail.

---

---

**Question 2**
An administrator is troubleshooting a failed SSH connection to a server. Running `ssh -v user@server` shows the connection reaches the authentication stage but fails with "Permission denied (publickey)." The user's `~/.ssh/` directory has permissions `755`. What is the most likely cause and fix?
A) The SSH daemon is not running. Start it with `systemctl start sshd`.
B) The `~/.ssh/` directory permissions are too permissive. SSH requires `700`. Run `chmod 700 ~/.ssh` and verify `~/.ssh/authorized_keys` is `600`.
C) The user's public key must be re-generated with `ssh-keygen -t rsa` because the existing key has expired.
D) Port 22 is blocked by the firewall. Run `firewall-cmd --permanent --add-service=ssh --reload`.
*   **Correct Answer:** B) The `~/.ssh/` directory permissions are too permissive. SSH requires `700`. Run `chmod 700 ~/.ssh` and verify `~/.ssh/authorized_keys` is `600`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If the SSH daemon were not running, the connection would fail at the TCP level — the client would not reach the authentication stage. The scenario states authentication was reached, confirming `sshd` is active.
    *   *Why C is incorrect:* SSH keys do not expire by default. There is no built-in expiration mechanism for RSA key pairs generated with `ssh-keygen`. Key age is not a valid cause of authentication failure.
    *   *Why D is incorrect:* If port 22 were blocked by a firewall, the connection would time out before reaching authentication. Again, the scenario confirms the authentication stage was reached, ruling out a firewall block.

---

---

**Question 3**
A RHEL 9 server running a web application returns HTTP 403 errors for files in `/srv/app/static/`. File permissions are correct (644, owned by apache). The SELinux mode is enforcing. `ausearch -m avc -ts recent` shows AVC denials for `httpd_t` accessing files with type `default_t`. What is the correct permanent fix?
A) Run `setenforce 0` to put SELinux in permissive mode so the web server can read all files.
B) Run `semanage fcontext -a -t httpd_sys_content_t "/srv/app/static(/.*)?"` then `restorecon -Rv /srv/app/static/`.
C) Run `chcon -R -t httpd_sys_content_t /srv/app/static/` to relabel the files.
D) Run `setsebool -P httpd_can_network_connect on` to allow Apache to access the directory.
*   **Correct Answer:** B) Run `semanage fcontext -a -t httpd_sys_content_t "/srv/app/static(/.*)?"` then `restorecon -Rv /srv/app/static/`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disabling SELinux enforcement removes the MAC layer system-wide and is not a valid production fix for a context mismatch. The correct approach is to fix the file context so the policy permits the access.
    *   *Why C is incorrect:* `chcon` applies the context change immediately but does not update the SELinux policy database. The next `restorecon` run or filesystem relabel will revert the files back to `default_t`, causing the problem to recur. `semanage fcontext` + `restorecon` is the permanent solution.
    *   *Why D is incorrect:* `httpd_can_network_connect` controls whether Apache can make outbound network connections — it has nothing to do with file access. The AVC denial is for file type `default_t`, which requires a context fix, not a network boolean.

---

**Question 4**
An administrator writes the following crontab entry: `*/5 * * * * /usr/local/bin/check_disk.sh`. A colleague says the script will run "at minute 5 of every hour." Who is correct and why?
A) The colleague is correct — `*/5` in the minute field means "at minute 5."
B) The administrator is correct — `*/5` means "every 5 minutes" (at minutes 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55). The script runs 12 times per hour.
C) Neither — `*/5` is invalid cron syntax and the job will not be scheduled.
D) The colleague is correct — the `/` in cron syntax indicates a specific minute, not an interval.
*   **Correct Answer:** B) The administrator is correct — `*/5` means "every 5 minutes" (at minutes 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55). The script runs 12 times per hour.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `5` (without the `*/`) in the minute field means "at minute 5 of every hour." The `*/5` step expression means "every 5 units" — it divides the full range (0–59) by 5 and matches every 5th value starting from 0.
    *   *Why C is incorrect:* `*/N` is valid standard cron step syntax supported by all major cron implementations including Vixie cron, cronie, and systemd timers. It is not a syntax error.
    *   *Why D is incorrect:* The `/` in cron syntax is the step operator, not a "specific value" indicator. `*/5` means "every 5 steps across the entire range." A specific minute is expressed as a plain integer (e.g., `5`).

---

**Question 5**
A Docker container named `app` is running but the application inside it is not responding. An administrator wants to open an interactive bash shell inside the running container to investigate. Which command is correct?
A) docker attach app
B) docker exec -it app /bin/bash
C) docker run -it app /bin/bash
D) docker inspect app --shell bash
*   **Correct Answer:** B) docker exec -it app /bin/bash
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `docker attach app` connects to the container's main process stdin/stdout/stderr — it attaches to PID 1's terminal, not a new shell. If the main process is not an interactive shell, this produces confusing output or no prompt, and detaching (Ctrl+C) may stop the container.
    *   *Why C is incorrect:* `docker run -it app /bin/bash` creates and starts a brand new container from the `app` image — it does not connect to the already-running container named `app`. This would start a second, separate container instance.
    *   *Why D is incorrect:* `--shell` is not a valid flag for `docker inspect`. `docker inspect` only outputs JSON metadata about a container or image. It does not provide an interactive shell or any execution capability.
