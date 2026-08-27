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

---

*Questions 6–20 — 5 pts each*

---

**Question 6**

An administrator needs to add a new 500 GB physical disk `/dev/sdb` to an existing LVM volume group named `vg_data`, then extend the logical volume `lv_app` by 200 GB. Which sequence of commands is correct?

A) `fdisk /dev/sdb && vgextend vg_data /dev/sdb && lvextend -L +200G /dev/vg_data/lv_app`
B) `pvcreate /dev/sdb && vgextend vg_data /dev/sdb && lvextend -L +200G /dev/vg_data/lv_app`
C) `mkfs.ext4 /dev/sdb && vgcreate vg_data /dev/sdb && lvcreate -L 200G vg_data`
D) `vgextend vg_data /dev/sdb && pvcreate /dev/sdb && lvextend -L +200G /dev/vg_data/lv_app`

*   **Correct Answer:** B) `pvcreate /dev/sdb && vgextend vg_data /dev/sdb && lvextend -L +200G /dev/vg_data/lv_app`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `fdisk` partitions a disk but does not initialize it as an LVM physical volume. LVM requires `pvcreate` to write the PV header before a disk can be added to a volume group. Skipping `pvcreate` causes `vgextend` to fail with "not a physical volume" error.
    *   *Why C is incorrect:* `mkfs.ext4` creates a filesystem on a raw disk — it destroys any LVM metadata and is never part of an LVM workflow. `vgcreate` creates a brand-new volume group rather than extending the existing `vg_data`. This command sequence would create a competing VG, not extend the existing one.
    *   *Why D is incorrect:* `vgextend` must follow `pvcreate`, not precede it. Running `vgextend vg_data /dev/sdb` before `pvcreate /dev/sdb` fails because `/dev/sdb` has not yet been initialized as a physical volume. The correct order is always: `pvcreate` → `vgextend` → `lvextend`.

---

**Question 7**

An administrator generates an SSH key pair with `ssh-keygen -t ed25519 -C "admin@corp.com"`. Which file must be copied to the remote server to enable passwordless authentication, and to which path?

A) `~/.ssh/id_ed25519` copied to `~/.ssh/authorized_keys` on the remote server.
B) `~/.ssh/id_ed25519.pub` appended to `~/.ssh/authorized_keys` on the remote server.
C) `~/.ssh/id_ed25519` copied to `/etc/ssh/authorized_keys` on the remote server.
D) Both `id_ed25519` and `id_ed25519.pub` must be copied to `~/.ssh/` on the remote server.

*   **Correct Answer:** B) `~/.ssh/id_ed25519.pub` appended to `~/.ssh/authorized_keys` on the remote server.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `id_ed25519` (without `.pub`) is the private key. Copying the private key to a remote server is a critical security error — the private key must never leave the local machine. Only the public key (`.pub`) is shared.
    *   *Why C is incorrect:* `/etc/ssh/authorized_keys` is not the standard path for per-user authorized keys. The standard path is `~/.ssh/authorized_keys` in the remote user's home directory. Some hardened configurations use an `AuthorizedKeysFile` directive to change this path, but `/etc/ssh/authorized_keys` is not the default.
    *   *Why D is incorrect:* Only the public key belongs on the remote server. Copying the private key to the remote server defeats the security model entirely — an attacker with access to the remote server would then possess the private key and could impersonate the administrator on any system that trusts it.

---

**Question 8**

A bash script contains the line `if [[ $# -eq 0 ]]; then echo "Usage: $0 filename"; exit 1; fi`. What does `$#` represent and what does this block accomplish?

A) `$#` is the script's process ID. The block prints usage and exits if the PID is zero.
B) `$#` is the number of arguments passed to the script. The block prints a usage message and exits with error code 1 if no arguments were provided.
C) `$#` is the last exit code of the previous command. The block exits if the previous command succeeded.
D) `$#` is the length of the first argument. The block exits if the first argument is an empty string.

*   **Correct Answer:** B) `$#` is the number of arguments passed to the script. The block prints a usage message and exits with error code 1 if no arguments were provided.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The script's process ID is stored in `$$`, not `$#`. `$$` expands to the PID of the current shell process. A PID value of zero is not meaningful in this context — PIDs start at 1 in Linux.
    *   *Why C is incorrect:* The last exit code of the previous command is stored in `$?`, not `$#`. `$?` is checked after running a command to determine whether it succeeded (0) or failed (non-zero). These are distinct special variables with entirely different purposes.
    *   *Why D is incorrect:* The length of the first argument would be `${#1}` (parameter length expansion), not `$#`. `$#` counts the total number of positional parameters passed to the script, regardless of their content or length.

---

**Question 9**

An administrator configures `/etc/ssh/sshd_config` with `PermitRootLogin no` and `PasswordAuthentication no`, then runs `sudo systemctl reload sshd`. A junior admin says this will lock everyone out of the server. Is this assessment correct?

A) Yes — disabling password authentication prevents all logins, including key-based logins.
B) No — disabling password authentication still permits public key authentication. Users with their public key in `~/.ssh/authorized_keys` on the server can still log in. Root can log in as a non-root user and use `sudo`.
C) Yes — `PermitRootLogin no` immediately terminates all active SSH sessions.
D) No — but only if `ChallengeResponseAuthentication yes` is also set to compensate for the disabled password method.

*   **Correct Answer:** B) No — disabling password authentication still permits public key authentication. Users with their public key in `~/.ssh/authorized_keys` on the server can still log in. Root can log in as a non-root user and use `sudo`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `PasswordAuthentication no` disables only keyboard-entered passwords. Public key authentication is a separate authentication method controlled by `PubkeyAuthentication` (which defaults to `yes`). Disabling passwords while leaving key-based auth enabled is standard hardening practice on production servers.
    *   *Why C is incorrect:* `systemctl reload sshd` sends SIGHUP to the SSH daemon, which re-reads the configuration. It does not terminate existing SSH sessions — active connections are unaffected by a reload. Only new connection attempts are evaluated against the new configuration.
    *   *Why D is incorrect:* `ChallengeResponseAuthentication` enables PAM-based authentication challenges (such as TOTP codes). It is not a fallback for disabled password authentication — it is a separate, more complex authentication mechanism. The correct answer does not depend on enabling challenge-response.

---

**Question 10**

A Linux server has the following firewalld rule applied permanently: `firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=10.0.0.0/8 port port=22 protocol=tcp accept'`. After running `firewall-cmd --reload`, what is the effect?

A) All SSH connections to port 22 are blocked globally. Only the 10.0.0.0/8 network can connect on any port.
B) SSH connections on port 22 are accepted only from source addresses within the 10.0.0.0/8 network. Connections from all other addresses follow the zone's default policy.
C) The rule enables SSH for the entire internet because rich rules override zone restrictions.
D) The `--permanent` flag means the rule has no effect until the next reboot. A `--reload` only applies temporary rules.

*   **Correct Answer:** B) SSH connections on port 22 are accepted only from source addresses within the 10.0.0.0/8 network. Connections from all other addresses follow the zone's default policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The rule explicitly allows TCP port 22 from the 10.0.0.0/8 source network — it does not block port 22 globally. Rich rules are additive: they define specific allow or deny actions for matching traffic. The rule does not affect non-SSH traffic to other ports.
    *   *Why C is incorrect:* Rich rules do not override zone restrictions globally. They add specific match-and-action entries to the zone's rule set. Traffic that does not match the rich rule is handled by the zone's other rules and default policy, not automatically allowed.
    *   *Why D is incorrect:* `firewall-cmd --reload` applies all permanent rules to the running configuration. The `--permanent` flag saves the rule to disk so it survives reboots; `--reload` then activates those saved rules immediately without requiring a reboot. This is the standard two-step workflow for permanent firewalld changes.

---

**Question 11**

An administrator needs to find all files owned by user `olduser` anywhere on the filesystem to reassign them before deleting the account. Which command is correct?

A) `ls -la / | grep olduser`
B) `find / -user olduser -ls 2>/dev/null`
C) `grep olduser /etc/passwd | awk -F: '{print $6}'`
D) `locate --user=olduser /`

*   **Correct Answer:** B) `find / -user olduser -ls 2>/dev/null`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `ls -la /` lists only the root directory's immediate contents — it does not recurse into subdirectories. It would miss the vast majority of files owned by `olduser` in `/home`, `/var`, and other locations.
    *   *Why C is incorrect:* This command reads `/etc/passwd` to find the user's home directory path. It does not search the filesystem for files owned by the user. The user may own files outside their home directory (in `/tmp`, `/var`, application directories, etc.) that this command would never find.
    *   *Why D is incorrect:* `locate` does not support a `--user` flag for filtering by file ownership. `locate` searches a filename index database by name pattern. It has no understanding of file ownership metadata.

---

**Question 12**

A junior administrator runs `chmod 777 /etc/passwd` attempting to fix a permissions error. What is the immediate security consequence and what is the correct fix?

A) No security consequence — `/etc/passwd` is a public file and 777 is equivalent to the default permissions.
B) The file becomes world-writable, allowing any user to modify user account entries including adding new users or changing the root account's home directory. The correct permissions are `644` (`-rw-r--r--`): `chmod 644 /etc/passwd`.
C) The file becomes executable, which causes the login system to attempt to run it as a script. Run `chmod -x /etc/passwd` to restore normal operation.
D) Setting 777 on `/etc/passwd` triggers a SELinux AVC denial that automatically reverts the permissions to the correct value.

*   **Correct Answer:** B) The file becomes world-writable, allowing any user to modify user account entries including adding new users or changing the root account's home directory. The correct permissions are `644` (`-rw-r--r--`): `chmod 644 /etc/passwd`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The default permissions on `/etc/passwd` are `644` (world-readable, owner-writable only). `777` adds write and execute permissions for all users, which is a serious vulnerability. Any unprivileged user could modify user account data.
    *   *Why C is incorrect:* While `777` does add the execute bit, the login system does not execute `/etc/passwd` as a script. The shell and login tools read `/etc/passwd` as a text database using library calls. The write bit (`w`) is the critical danger — it enables direct modification of account data.
    *   *Why D is incorrect:* SELinux does not automatically revert DAC permission changes. SELinux enforces MAC policy on top of DAC — it adds additional restrictions but does not monitor or restore DAC permission changes made by the administrator. The administrator must manually correct the permissions.

---

**Question 13**

An administrator runs `ss -tuln` and sees port 3306 listening on `0.0.0.0:3306`. The server runs MySQL. What does `0.0.0.0` as the bind address indicate, and what is the security concern?

A) MySQL is bound to the loopback interface only and is not accessible from the network.
B) MySQL is bound to all network interfaces and accepts connections from any IP address on port 3306. If no firewall rule restricts access, the database is reachable from the network.
C) `0.0.0.0` means the port is in a closed state waiting for a process to bind to it.
D) MySQL is using IPv6 addressing. The equivalent IPv4 bind address is `127.0.0.1`.

*   **Correct Answer:** B) MySQL is bound to all network interfaces and accepts connections from any IP address on port 3306. If no firewall rule restricts access, the database is reachable from the network.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The loopback interface bind address is `127.0.0.1`, not `0.0.0.0`. `127.0.0.1` restricts MySQL to local connections only, which is the recommended default for database servers that should not be externally accessible. `0.0.0.0` is the wildcard address meaning all interfaces.
    *   *Why C is incorrect:* A port shown in `ss -tuln` output is already listening — the process is bound and actively accepting connections. Closed ports do not appear in `ss -tuln` output. The `l` flag in `ss -tuln` means "listening."
    *   *Why D is incorrect:* `0.0.0.0` is a valid IPv4 wildcard address meaning all IPv4 interfaces. The IPv6 equivalent wildcard is `::` or `:::3306`. These are different address families and different bind semantics. `0.0.0.0` has nothing to do with IPv6 addressing.

---

**Question 14**

A bash script needs to iterate over all `.log` files in `/var/log/app/` and print the filename and its line count. Which construct correctly implements this?

A) `for f in /var/log/app/*.log; do echo "$f: $(wc -l < $f) lines"; done`
B) `while /var/log/app/*.log; do wc -l $f; done`
C) `for f in $(ls /var/log/app/); do wc -l $f; done`
D) `foreach f (/var/log/app/*.log) { echo $f }`

*   **Correct Answer:** A) `for f in /var/log/app/*.log; do echo "$f: $(wc -l < $f) lines"; done`
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `while` takes a command and loops while its exit code is zero. Listing glob patterns is not a valid `while` condition. This is a syntax error — `while` requires a command such as `read` or `true`, not a file pattern.
    *   *Why C is incorrect:* Using `$(ls ...)` to generate a file list is fragile and incorrect — it breaks on filenames containing spaces, tabs, or newlines. The glob expansion `for f in /path/*.log` is the correct and safe bash idiom. Additionally, `ls` output without full paths would require `cd` first or path construction.
    *   *Why D is incorrect:* `foreach` with parentheses and braces is `csh`/`tcsh` syntax, not bash. The bash for-loop uses `for VAR in LIST; do ... done` syntax. Using `csh` syntax in a `#!/bin/bash` script causes a syntax error.

---

**Question 15**

An administrator configures a RAID 5 array with `mdadm` using four 2 TB disks. What is the usable storage capacity of this array and how many disk failures can it tolerate?

A) 8 TB usable capacity, tolerates 2 simultaneous disk failures.
B) 6 TB usable capacity, tolerates 1 disk failure.
C) 4 TB usable capacity, tolerates 2 simultaneous disk failures.
D) 6 TB usable capacity, tolerates 2 simultaneous disk failures.

*   **Correct Answer:** B) 6 TB usable capacity, tolerates 1 disk failure.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* RAID 5 uses distributed parity equivalent to one disk's worth of capacity across all drives. With four 2 TB disks, total raw capacity is 8 TB, but 2 TB is consumed by parity — leaving 6 TB usable. RAID 5 tolerates only one disk failure; two simultaneous failures destroy the array.
    *   *Why C is incorrect:* 4 TB usable would require two disks' worth of parity overhead, which is the characteristic of RAID 6. RAID 6 uses dual distributed parity and tolerates 2 simultaneous disk failures. RAID 5 uses single parity. With four 2 TB disks and single parity: (4-1) × 2 TB = 6 TB usable.
    *   *Why D is incorrect:* The usable capacity calculation (6 TB) is correct, but RAID 5 cannot tolerate 2 simultaneous disk failures. If a second drive fails while the array is in a degraded state rebuilding from the first failure, all data is lost. RAID 6 is required for two-fault tolerance.

---

**Question 16**

An administrator needs to set the default umask for all users on an Ubuntu server to `027`, ensuring new files get permissions `640` and new directories get permissions `750`. Where should this setting be configured to apply system-wide for all login shells?

A) `/etc/profile` or a file in `/etc/profile.d/` containing `umask 027`
B) `/etc/umask.conf` with the line `DEFAULT_UMASK=027`
C) `/etc/security/limits.conf` with `* umask 027`
D) `/etc/sysctl.conf` with `fs.umask = 027`

*   **Correct Answer:** A) `/etc/profile` or a file in `/etc/profile.d/` containing `umask 027`
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `/etc/umask.conf` is not a standard Linux configuration file. Some PAM-based systems use `/etc/login.defs` for `UMASK` settings, but `/etc/umask.conf` does not exist as a system-recognized path.
    *   *Why C is incorrect:* `/etc/security/limits.conf` configures PAM resource limits such as maximum open files (`nofile`), maximum processes (`nproc`), and core dump sizes. It does not support a `umask` directive — that is not one of its recognized resource types.
    *   *Why D is incorrect:* `/etc/sysctl.conf` configures kernel parameters at runtime via the `sysctl` interface. The umask is a per-process attribute inherited through the shell environment — it is not a kernel parameter and cannot be set via `sysctl`. The `fs.umask` key does not exist in the sysctl namespace.

---

**Question 17**

An administrator uses `strace -p $(pgrep nginx)` to troubleshoot a slow nginx process. Which type of information does `strace` provide that `top`, `vmstat`, and `iostat` do not?

A) Per-process CPU and memory utilization broken down by function call.
B) A real-time trace of every system call made by the process — such as `read()`, `write()`, `open()`, `connect()`, and `epoll_wait()` — showing the arguments and return values.
C) The process's open file descriptors and socket connections, similar to `lsof`.
D) The process's full call stack showing which functions in its source code are executing.

*   **Correct Answer:** B) A real-time trace of every system call made by the process — such as `read()`, `write()`, `open()`, `connect()`, and `epoll_wait()` — showing the arguments and return values.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Per-process CPU and memory utilization is shown by `top`, `ps aux`, and `pidstat`. `strace` does not report CPU or memory percentages — it traces system calls, which are the boundary crossings between user space and kernel space.
    *   *Why C is incorrect:* Open file descriptors and socket connections are shown by `lsof -p PID` or `ss -p`. While `strace` may show `open()` calls happening in real time, it is not the right tool for listing existing file descriptors — `lsof` and `/proc/PID/fd` are purpose-built for that.
    *   *Why D is incorrect:* `strace` shows kernel system call traces, not user-space function call stacks. User-space call stacks (showing which application functions called which) require a profiler like `perf`, `gprof`, or `gdb`. `strace` operates at the kernel interface boundary, not within the application's own code.

---

**Question 18**

A script uses `set -e` at the top. A command in the middle of the script fails with exit code 1. What happens next?

A) The script continues execution and writes the error to stderr before proceeding.
B) The script immediately exits with the failing command's exit code. No subsequent commands in the script run.
C) The script pauses and waits for the administrator to press Enter before continuing.
D) `set -e` only affects `if` statements — standalone commands that fail are still ignored.

*   **Correct Answer:** B) The script immediately exits with the failing command's exit code. No subsequent commands in the script run.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Without `set -e`, a bash script continues after a failed command by default. `set -e` (errexit) changes this behavior — any command that exits with a non-zero status causes the entire script to exit immediately unless the command is part of an `if`, `while`, `until` condition, or followed by `||`.
    *   *Why C is incorrect:* `set -e` provides no interactive pause mechanism. Scripts run non-interactively. If interactive error handling is needed, the script must explicitly use `read` to prompt the user or `trap ERR` to catch errors and take action.
    *   *Why D is incorrect:* `set -e` applies to all commands in the script, not just those within `if` conditions. The `if` exception is actually the opposite — commands used as conditions in `if` statements and `while`/`until` loops are exempt from `set -e` because their non-zero exit is expected and meaningful. Standalone commands that fail are the primary target of `set -e`.

---

**Question 19**

An administrator runs `rpm -V openssh-server` on a RHEL system after a suspected intrusion and sees the following output:

```
S.5....T.  /usr/sbin/sshd
```

What does this output indicate?

A) The `sshd` binary has normal status — the dots confirm all file attributes are unchanged.
B) The `sshd` binary has been modified — `S` indicates the file size has changed, `5` indicates the MD5 checksum no longer matches the package database, and `T` indicates the modification timestamp has changed. The binary may have been replaced.
C) The output shows that SELinux has blocked the sshd binary from running. Re-enable the binary with `restorecon /usr/sbin/sshd`.
D) The `rpm -V` output confirms the package is installed correctly. The letters indicate which verification checks passed.

*   **Correct Answer:** B) The `sshd` binary has been modified — `S` indicates the file size has changed, `5` indicates the MD5 checksum no longer matches the package database, and `T` indicates the modification timestamp has changed. The binary may have been replaced.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* In `rpm -V` output, dots (`.`) mean the attribute passed verification. A letter in a position means that attribute failed. `S` (size mismatch), `5` (checksum mismatch), and `T` (timestamp mismatch) are all failure indicators — this output is a significant integrity alert, not a clean bill of health.
    *   *Why C is incorrect:* `rpm -V` is a package integrity verification tool that compares installed files against the RPM database. It has no relationship to SELinux. An SELinux denial would appear in `/var/log/audit/audit.log` as an AVC denial, not in `rpm -V` output.
    *   *Why D is incorrect:* This is the exact opposite of the correct interpretation. In `rpm -V` output, letters indicate failures (attributes that do not match the package database) and dots indicate passes (attributes that match). A clean `rpm -V` produces no output at all — any output indicates a discrepancy.

---

**Question 20**

A CompTIA Linux+ XK0-005 exam question presents a performance-based scenario: "Configure the system so that the firewall permanently allows HTTPS traffic on port 443 and the web server starts automatically on boot." The system is RHEL 9 running firewalld and Apache httpd. Which command sequence correctly satisfies both requirements?

A) `iptables -A INPUT -p tcp --dport 443 -j ACCEPT && chkconfig httpd on`
B) `firewall-cmd --permanent --add-service=https --reload && systemctl enable httpd`
C) `ufw allow 443/tcp && systemctl enable --now httpd`
D) `firewall-cmd --add-service=https && systemctl start httpd`

*   **Correct Answer:** B) `firewall-cmd --permanent --add-service=https --reload && systemctl enable httpd`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `iptables` rules are not the correct tool on a RHEL 9 system configured with firewalld — firewalld manages its own iptables rules and direct iptables edits may conflict. `chkconfig` is a legacy SysV init tool deprecated on RHEL 7 and later, replaced entirely by `systemctl enable`. Both commands are the wrong tools for RHEL 9.
    *   *Why C is incorrect:* `ufw` (Uncomplicated Firewall) is the default firewall tool on Ubuntu/Debian. On RHEL 9, `ufw` is not installed by default and `firewalld` is the system firewall. Using distribution-specific tools on the wrong distribution is a common exam trap testing distro awareness.
    *   *Why D is incorrect:* `firewall-cmd --add-service=https` without `--permanent` applies the rule only to the current runtime — it is lost on the next firewall reload or reboot. `systemctl start httpd` starts the service immediately but does not enable it to start on future boots. Both components of this answer are incomplete: the firewall rule is temporary and the service enable is missing.
