# Quiz: Module 16 — Linux+ XK0-005 Exam Preparation (20 Practice Questions)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Instructions

This 20-question practice exam mirrors the format and difficulty of the CompTIA Linux+ XK0-005 exam. Each question is worth 5 points. Time yourself: complete all 20 questions in 20 minutes or less to simulate exam pacing.

---

### Questions

**Question 1**

A Linux administrator adds `/etc/fstab` entry for a new filesystem but receives an error when testing. Which command tests all fstab entries without rebooting?

- A) `fstab --test`
- B) `mount --verify`
- C) `mount -a`
- D) `systemctl restart fstab`

**Correct Answer: C**

*Explanation: `mount -a` mounts all entries in `/etc/fstab` that aren't already mounted. Errors in fstab entries produce error messages.*

---

**Question 2**

Which command makes a change to a user's crontab using the system's default text editor?

- A) `vi /etc/cron.d/username`
- B) `crontab -e`
- C) `crontab -r`
- D) `nano /var/spool/cron/username`

**Correct Answer: B**

*Explanation: `crontab -e` opens the user's crontab in `$EDITOR` and validates syntax on save. Editing `/var/spool/cron/` files directly can bypass validation and permission checks.*

---

**Question 3**

A system administrator is configuring a new RHEL 9 server. The command `dnf install httpd` is run but the package is not found. Which directory should the administrator check for repository configuration?

- A) `/etc/repos.d/`
- B) `/etc/yum.repos.d/`
- C) `/etc/dnf/repos/`
- D) `/usr/share/repos/`

**Correct Answer: B**

*Explanation: DNF (and YUM) repository configuration files are stored in `/etc/yum.repos.d/`. Each `.repo` file defines one or more repositories including the base URL and GPG key settings.*

---

**Question 4**

An administrator needs to view the last 100 lines of journal output for the `sshd` service and continue watching in real time. Which command is correct?

- A) `journalctl -n 100 -f -u sshd`
- B) `journalctl --last 100 --follow sshd`
- C) `journalctl -n 100 sshd`
- D) `tail -100 /var/log/sshd.log -f`

**Correct Answer: A**

*Explanation: `-n 100` shows the last 100 entries, `-f` follows in real time, and `-u sshd` filters for the sshd unit. Options B and D use incorrect syntax.*

---

**Question 5**

A bash script checks if a file exists with `[ -f /tmp/lockfile ]`. Which statement correctly describes what happens if the file does NOT exist?

- A) The test returns exit code 0 (true)
- B) The test returns exit code 1 (false)
- C) The script exits with an error
- D) The variable `$?` is undefined

**Correct Answer: B**

*Explanation: The `-f` test returns exit code 0 (true) if the file exists and is a regular file. If the file does not exist, it returns exit code 1 (false). Exit codes: 0 = success/true, non-zero = failure/false.*

---

**Question 6**

Which command shows the SELinux context for all files in `/var/www/html/`?

- A) `ls -la /var/www/html/`
- B) `ls -Z /var/www/html/`
- C) `secon /var/www/html/`
- D) `chcon -l /var/www/html/`

**Correct Answer: B**

*Explanation: The `-Z` flag added to `ls`, `ps`, and many other standard commands displays the SELinux security context alongside normal output. `ls -Z` shows the context for files and directories.*

---

**Question 7**

An administrator wants to configure SSH so that only members of the `sysadmins` group can log in, and sessions disconnect after 10 minutes of inactivity. Which `sshd_config` directives accomplish this? (Select the correct combination.)

- A) `PermitGroups sysadmins` and `SessionTimeout 600`
- B) `AllowGroups sysadmins` and `ClientAliveInterval 300` with `ClientAliveCountMax 2`
- C) `AllowGroups sysadmins` and `IdleTimeout 10m`
- D) `GroupWhitelist sysadmins` and `Timeout 600`

**Correct Answer: B**

*Explanation: `AllowGroups` is the correct directive for group-based access control. A 10-minute timeout requires `ClientAliveInterval 300` (5-minute check interval) and `ClientAliveCountMax 2` (2 missed checks = 10 minutes total). None of the other option syntax is valid.*

---

**Question 8**

A system has 4 disks of 2 TB each configured as RAID 10. How much usable storage capacity is available?

- A) 8 TB
- B) 6 TB
- C) 4 TB
- D) 2 TB

**Correct Answer: C**

*Explanation: RAID 10 uses 50% of total capacity for mirroring. With 4 × 2 TB = 8 TB total, RAID 10 provides 4 TB usable. RAID 10 can survive one drive failure per mirrored pair.*

---

**Question 9**

A developer ran `cp /etc/passwd /var/www/html/config.txt` to test something and forgot to delete it. Now Apache cannot read the file even though file permissions are correct. SELinux is enforcing. What is the most likely cause?

- A) The file is owned by root; Apache runs as `apache`
- B) The copied file retained the `etc_t` SELinux type, not `httpd_content_t`
- C) The file permissions are wrong; `chmod 644` is needed
- D) Apache's `DocumentRoot` does not include `/var/www/html`

**Correct Answer: B**

*Explanation: When copying files, the destination inherits the source's SELinux type (in this case `etc_t` from `/etc/passwd`). Apache's domain `httpd_t` is not permitted to read `etc_t` files. Fix with `restorecon /var/www/html/config.txt`.*

---

**Question 10**

Which field in a crontab entry specifies "run at 3:30 PM every Friday"?

- A) `30 15 * * 5`
- B) `30 3 * * 5`
- C) `15 30 * * 5`
- D) `30 15 5 * *`

**Correct Answer: A**

*Explanation: Crontab fields: minute(0-59) hour(0-23) day-of-month(1-31) month(1-12) day-of-week(0-7, 5=Friday). 3:30 PM = minute 30, hour 15, day-of-week 5 = `30 15 * * 5`.*

---

**Question 11**

After adding a new physical volume to an LVM volume group, an administrator needs to extend an existing logical volume by 20 GB AND immediately make the space available to an XFS filesystem without unmounting. Which command is correct?

- A) `lvextend -L +20G /dev/vg0/lv0 && xfs_growfs /mount/point`
- B) `lvextend -L +20G -r /dev/vg0/lv0`
- C) `lvcreate -L 20G /dev/vg0 && mount -a`
- D) `vgextend vg0 +20G && lvresize /dev/vg0/lv0`

**Correct Answer: B**

*Explanation: `lvextend -r` resizes both the logical volume and the filesystem. For XFS, it calls `xfs_growfs`; for ext4, it calls `resize2fs`. Option A is also functionally correct but requires two commands; option B is the preferred single-command approach.*

---

**Question 12**

A new administrator cannot execute `sudo` commands despite being listed in `/etc/sudoers`. The error is "sudo: PAM authentication error." What is the most likely cause?

- A) `/etc/sudoers` has incorrect syntax
- B) The PAM module for sudo is misconfigured in `/etc/pam.d/sudo`
- C) The administrator's account password has expired
- D) Both B and C are possible causes

**Correct Answer: D**

*Explanation: "PAM authentication error" during sudo can result from multiple PAM-layer issues. An expired password is a common cause — PAM's `pam_unix` account module blocks authentication when an account password is expired. A misconfigured `/etc/pam.d/sudo` can also cause this. Both must be investigated.*

---

**Question 13**

Which `docker` command connects an interactive bash session to a RUNNING container named `webserver`?

- A) `docker run -it webserver bash`
- B) `docker attach webserver`
- C) `docker exec -it webserver bash`
- D) `docker shell webserver`

**Correct Answer: C**

*Explanation: `docker exec -it container bash` executes a new process (bash) in a running container with an interactive terminal. `docker run` creates a NEW container from an image. `docker attach` connects to the container's main process stdin/stdout.*

---

**Question 14**

A script checks disk usage and alerts when a filesystem exceeds 90%. Which command within a script would capture ONLY the usage percentage (as a number) for the `/data` filesystem?

- A) `df -h /data | awk '{print $5}'`
- B) `df -h /data | tail -1 | awk '{print $5}' | tr -d '%'`
- C) `du -sh /data | cut -f1`
- D) `df /data | grep -v Use | cut -d% -f1`

**Correct Answer: B**

*Explanation: `df -h /data` outputs a header line and one data line. `tail -1` gets the data line. `awk '{print $5}'` extracts the 5th field (Use%). `tr -d '%'` removes the percent sign to get a pure number for comparison. Option A would print both the header "Use%" and the data.*

---

**Question 15**

An administrator runs `systemctl status myapp.service` and sees the state `active (exited)`. What does this state indicate?

- A) The service crashed and exited unexpectedly
- B) The service started successfully, ran its task, and exited normally (Type=oneshot)
- C) The service is queued and waiting to start
- D) The service was manually stopped

**Correct Answer: B**

*Explanation: `active (exited)` means the service completed successfully. This is the expected state for `Type=oneshot` services that perform a single task and exit. It does not indicate failure — a failed service would show `failed` state.*

---

**Question 16**

An administrator needs to find all files modified within the last 24 hours under `/var/log`. Which command is correct?

- A) `find /var/log -modified 24h`
- B) `find /var/log -mtime -1`
- C) `find /var/log -newer 24h`
- D) `find /var/log -age 1d`

**Correct Answer: B**

*Explanation: `find -mtime -1` finds files with modification time less than 1 day ago (within the last 24 hours). The `-mtime` value is in days: `-1` means less than 1 day, `+7` means more than 7 days, `7` means exactly 7 days (±12 hours).*

---

**Question 17**

fail2ban has banned an administrator's IP address by mistake during testing. The administrator can still reach the server via a different network path. Which command removes the ban for IP `10.0.0.50` from the `sshd` jail?

- A) `fail2ban-client unban 10.0.0.50`
- B) `fail2ban-client set sshd unbanip 10.0.0.50`
- C) `iptables -D INPUT -s 10.0.0.50 -j DROP`
- D) `firewall-cmd --remove-rich-rule="... 10.0.0.50 ..."`

**Correct Answer: B**

*Explanation: `fail2ban-client set sshd unbanip 10.0.0.50` removes the ban through fail2ban's own management interface, which also removes the corresponding firewall rule. Manually removing iptables or firewalld rules (options C and D) would also remove the block but leaves fail2ban's internal ban record intact — fail2ban may re-add the block.*

---

**Question 18**

Which `ip` command displays the system's ARP cache (the mapping between IP addresses and MAC addresses)?

- A) `ip arp show`
- B) `ip neigh show`
- C) `ip mac show`
- D) `ip link show arp`

**Correct Answer: B**

*Explanation: `ip neigh show` displays the neighbor cache, which includes ARP (IPv4) and NDP (IPv6) entries mapping IP addresses to MAC addresses. `ip neigh` is the `iproute2` replacement for the deprecated `arp` command.*

---

**Question 19**

An Ansible playbook fails with the error "Missing sudo password." The playbook uses `become: yes`. What is the most likely fix?

- A) Add `sudo: yes` to the playbook
- B) Configure passwordless sudo for the Ansible user on the managed host (`NOPASSWD: ALL` in sudoers)
- C) Add `become_password` to the inventory file
- D) Run the playbook as root on the control node

**Correct Answer: B**

*Explanation: When `become: yes` is used, Ansible needs to run `sudo` on the managed host. If the user requires a password for sudo, Ansible cannot interactively enter it. The solution is to configure passwordless sudo in `/etc/sudoers` or sudoers.d: `ansibleuser ALL=(ALL) NOPASSWD: ALL`. Alternatively, use `--ask-become-pass` (`-K`) on the command line.*

---

**Question 20**

A server's `/var` filesystem is at 98% usage. `du -sh /var/log` shows 45 GB, but the filesystem shows 90 GB used. What is the MOST likely explanation?

- A) `du` only reports disk space for files owned by root
- B) One or more log files were deleted, but a process still holds open file descriptors on them, keeping the blocks allocated
- C) The filesystem is fragmented and `df` includes fragmentation overhead
- D) `/var/log` is on a separate filesystem; `df` is reporting combined usage

**Correct Answer: B**

*Explanation: When files are deleted while processes hold open file descriptors, the file's directory entry is removed (du no longer sees it) but the disk blocks are not freed until the file descriptor is closed. `df` counts all allocated blocks including those held by open file descriptors. Restart the process holding the files (often rsyslog, journald, or a log-writing application) to release the blocks.*

---

### Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | C | Domain 1 |
| 2 | B | Domain 1 |
| 3 | B | Domain 1 |
| 4 | A | Domain 1 |
| 5 | B | Domain 3 |
| 6 | B | Domain 2 |
| 7 | B | Domain 2 |
| 8 | C | Domain 1 |
| 9 | B | Domain 2 |
| 10 | A | Domain 1 |
| 11 | B | Domain 1 |
| 12 | D | Domain 2 |
| 13 | C | Domain 3 |
| 14 | B | Domain 3 |
| 15 | B | Domain 1 |
| 16 | B | Domain 4 |
| 17 | B | Domain 2 |
| 18 | B | Domain 4 |
| 19 | B | Domain 3 |
| 20 | B | Domain 4 |

---

### Score Interpretation

| Score | Percentage | Readiness |
|-------|-----------|----------|
| 18–20 | 90–100% | Exam-ready |
| 15–17 | 75–85% | Minor review needed |
| 12–14 | 60–70% | Focused review of weak domains |
| Below 12 | Below 60% | Comprehensive review recommended |

Review every question you missed, not just the topic — understand WHY the correct answer is correct and why the others are wrong. That reasoning is what the exam tests.
