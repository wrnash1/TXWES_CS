# Quiz: Module 15 — Linux Security Hardening

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Instructions

Select the best answer for each question. Each question is worth 10 points.

---

### Questions

**Question 1**

An Apache web server on a RHEL 9 system cannot read a configuration file placed in `/srv/webconfig/app.conf`. SELinux is in enforcing mode. The file permissions are correct (644). What is the MOST likely cause and fix?

- A) The file is owned by root; change ownership to `apache` with `chown apache /srv/webconfig/app.conf`
- B) The file has SELinux type `admin_home_t` instead of `httpd_config_t`; fix with `restorecon -v /srv/webconfig/app.conf`
- C) The file has the wrong SELinux type; assign correct type with `semanage fcontext` and run `restorecon`
- D) Add an iptables rule allowing Apache to access `/srv/webconfig/`

**Correct Answer: C**

*Explanation: In a custom directory (`/srv/webconfig/`), there is no default SELinux policy mapping to an http type. The correct fix is: (1) use `semanage fcontext -a -t httpd_config_t "/srv/webconfig(/.*)?"` to permanently define the mapping, then (2) `restorecon -Rv /srv/webconfig/` to apply the context. Option B's `restorecon` alone would restore the `admin_home_t` default context (not the httpd type), since the new mapping hasn't been defined yet.*

---

**Question 2**

A security administrator wants to ensure a specific user's account `jsmith` expires on December 31, 2025, AND requires a password change every 60 days. Which commands accomplish both requirements?

- A) `chage -M 60 jsmith` and `usermod --expiredate 2025-12-31 jsmith`
- B) `chage -M 60 -E 2025-12-31 jsmith`
- C) `passwd --expire 2025-12-31 jsmith` and `passwd --maxdays 60 jsmith`
- D) `chage -d 60 -E 2025-12-31 jsmith`

**Correct Answer: B**

*Explanation: `chage -M 60` sets maximum password age to 60 days. `chage -E 2025-12-31` sets the absolute account expiration date. Both can be combined in a single `chage` command. Option D incorrectly uses `-d` which sets the last password change date, not the maximum age.*

---

**Question 3**

An administrator notices many failed SSH login attempts from external IPs in the auth log. Which tool is BEST suited to automatically block these IPs after a configurable number of failures?

- A) `auditd`
- B) `fail2ban`
- C) `SELinux booleans`
- D) `firewall-cmd --panic-mode`

**Correct Answer: B**

*Explanation: `fail2ban` monitors log files for failure patterns and dynamically adds firewall rules to block offending IPs. `auditd` records events but takes no blocking action. SELinux booleans control access control policies, not IP blocking. `--panic-mode` blocks ALL network traffic, not selective IPs.*

---

**Question 4**

Which `auditctl` command adds a rule to log all write operations to `/etc/shadow` with the key `shadow_watch`?

- A) `auditctl -a /etc/shadow -p write -k shadow_watch`
- B) `auditctl -w /etc/shadow -p w -k shadow_watch`
- C) `auditctl -w /etc/shadow -p wa -k shadow_watch`
- D) `auditctl --watch /etc/shadow --key shadow_watch`

**Correct Answer: C**

*Explanation: `-w /etc/shadow` watches the file. `-p wa` audits write (`w`) and attribute changes (`a`). `-k shadow_watch` assigns the key. Including `a` (attribute changes) is important for capturing `chage` and `chmod` operations that don't write file content but do modify file attributes.*

---

**Question 5**

What is the difference between SELinux `Enforcing` mode and `Permissive` mode?

- A) In Enforcing mode, all traffic is blocked; in Permissive mode, only flagged traffic is blocked
- B) Permissive mode enforces the policy strictly; Enforcing mode allows some violations with logging
- C) Both modes log violations; Enforcing mode also blocks them, Permissive mode does not
- D) Enforcing mode applies to system users only; Permissive mode applies to all users

**Correct Answer: C**

*Explanation: Both modes apply the SELinux policy and log violations as AVC messages. The key difference is enforcement: in Enforcing mode, policy violations are blocked. In Permissive mode, they are only logged and the operation is allowed. Permissive is used to diagnose what a policy would block before enabling enforcement.*

---

**Question 6**

A Linux administrator is configuring fail2ban and wants SSH to be blocked after 5 failed attempts within 15 minutes, and keep the ban active for 2 hours. Which `jail.local` configuration is correct?

- A) `findtime=15 maxretry=5 bantime=2`
- B) `findtime=900 maxretry=5 bantime=7200`
- C) `findtime=15m maxretry=5 bantime=2h`
- D) Both B and C are correct

**Correct Answer: D**

*Explanation: fail2ban accepts both numeric values (seconds) and shorthand strings (minutes/hours). `findtime=900` equals `findtime=15m`, and `bantime=7200` equals `bantime=2h`. Both configurations are valid. The numeric format was the original syntax; shorthand strings are supported in newer versions.*

---

**Question 7**

Which command permanently enables the SELinux boolean `httpd_can_network_connect` so it survives a reboot?

- A) `setsebool httpd_can_network_connect on`
- B) `setenforce httpd_can_network_connect=1`
- C) `setsebool -P httpd_can_network_connect on`
- D) `semanage boolean -e httpd_can_network_connect`

**Correct Answer: C**

*Explanation: `setsebool -P` (persistent) writes the boolean change to the SELinux policy store, making it survive reboots. Without `-P`, `setsebool` changes the runtime value only and is reset on the next boot.*

---

**Question 8**

AppArmor is in "complain" mode for an application. What does this mean for security?

- A) The application is blocked from all network access
- B) Policy violations are logged but the application is not blocked
- C) The application requires user approval for each file access
- D) AppArmor is disabled for this application

**Correct Answer: B**

*Explanation: AppArmor complain mode logs policy violations to the system log (as audit events or syslog entries) but does not block the operation. This allows administrators to identify what access an application needs before switching to enforce mode. It is functionally equivalent to SELinux Permissive mode.*

---

**Question 9**

A PAM configuration file contains `pam_pwquality.so` with the setting `minlen = 14`. A user tries to set a password of 12 characters. What happens?

- A) The password is accepted but a warning is displayed
- B) The password is rejected; the user must use at least 14 characters
- C) The password is accepted if it contains at least one number
- D) The setting only applies to new accounts, not existing users

**Correct Answer: B**

*Explanation: `pam_pwquality.so` enforces password quality rules during the `password` PAM phase. `minlen = 14` sets the minimum password length to 14 characters. A 12-character password will be rejected regardless of complexity, and the user will be prompted to choose a longer password.*

---

**Question 10**

Which tool would an administrator use to run an automated CIS Benchmark assessment against a RHEL 9 system and produce an HTML compliance report?

- A) `fail2ban-client --benchmark`
- B) `auditctl --cis-scan`
- C) `oscap xccdf eval` with appropriate profile and SCAP content
- D) `sestatus --cis-report`

**Correct Answer: C**

*Explanation: OpenSCAP's `oscap xccdf eval` command performs SCAP-based security assessments. The `--profile` flag selects the CIS benchmark profile, and `--report` generates an HTML report. The SCAP Security Guide (SSG) package provides the content files for RHEL/Rocky Linux. The other options are fabricated commands.*

---

**Question 11** (5 points)

An administrator runs `ausearch -k shadow_watch -ts today` to search audit logs. What does the `-ts today` option do?

- A) It filters results to events tagged with the `today` key.
- B) It limits results to audit events that occurred since the start of today.
- C) It sorts the output by timestamp in descending order.
- D) It converts timestamps from epoch format to human-readable format.

**Correct Answer: B**

*Explanation: `-ts` (time start) filters audit records to only those occurring after the specified time. `today` is a special value meaning midnight of the current day. Other valid values include `yesterday`, `recent` (last 10 minutes), a specific time like `10:00:00`, or an epoch timestamp. This makes `ausearch` output manageable on busy systems with large audit logs.*

---

**Question 12** (5 points)

Which `semanage` command displays all current custom SELinux file context mappings that have been added (not part of the default policy)?

- A) `semanage fcontext -l`
- B) `semanage fcontext --list-custom`
- C) `semanage fcontext -l -C`
- D) `restorecon -nl /`

**Correct Answer: C**

*Explanation: `semanage fcontext -l` lists ALL context mappings including default policy entries (thousands of lines). Adding `-C` (customizations only) restricts output to administrator-added mappings, making it easy to audit what custom contexts are in place. This is essential for documentation and troubleshooting custom directory configurations.*

---

**Question 13** (5 points)

A PAM module is configured with the `requisite` control flag. If this module fails, what happens?

- A) Authentication continues evaluating the rest of the stack, and the failure is accumulated.
- B) Authentication fails immediately and no further modules in the stack are evaluated.
- C) The failure is logged but authentication continues and can still succeed.
- D) Authentication is retried up to three times before failing.

**Correct Answer: B**

*Explanation: The `requisite` control flag causes immediate failure — if the module fails, PAM stops evaluating the rest of the stack immediately and returns a failure. This differs from `required` (which marks failure but continues evaluating all modules before returning failure) and `optional` (which ignores module failure). `requisite` is used for hard pre-conditions like MFA or account status checks.*

---

**Question 14** (5 points)

Which command shows the SELinux context of all processes related to the `httpd` service?

- A) `seinfo httpd`
- B) `ps -eZ | grep httpd`
- C) `getfattr httpd`
- D) `sestatus -v httpd`

**Correct Answer: B**

*Explanation: `ps -eZ` shows all running processes with their SELinux security context in the first column (domain). Filtering with `grep httpd` shows only httpd-related processes and their context labels. This reveals whether the processes are running in the expected domain (e.g., `httpd_t`) or an unexpected one. `getfattr` retrieves extended attributes of files, not processes.*

---

**Question 15** (5 points)

A system administrator wants to require users to use a hardware TOTP authenticator for SSH logins in addition to their password. Which PAM module provides this capability?

- A) `pam_tally2.so`
- B) `pam_google_authenticator.so`
- C) `pam_faillock.so`
- D) `pam_cracklib.so`

**Correct Answer: B**

*Explanation: `pam_google_authenticator.so` (from the google-authenticator-libpam package) provides TOTP (Time-based One-Time Password) multi-factor authentication. When configured, it requires users to enter a time-based code from an authenticator app (Google Authenticator, Authy, etc.) in addition to their password. `pam_tally2` and `pam_faillock` track failed logins and implement lockouts. `pam_cracklib` enforces password complexity.*

---

**Question 16** (5 points)

An AppArmor profile is in enforce mode for the `nginx` service. The service fails to start with a permission error. Where should the administrator look first to identify which specific file access is being blocked?

- A) `/var/log/nginx/error.log`
- B) `/etc/apparmor.d/usr.sbin.nginx`
- C) `/var/log/syslog` or `journalctl` for DENIED messages
- D) `aa-status` output

**Correct Answer: C**

*Explanation: AppArmor logs denied operations to the system log (`/var/log/syslog` on Debian/Ubuntu, or accessible via `journalctl -k` for kernel messages). The log entries show `DENIED` with the specific file path, operation type, and profile name. The profile file (option B) shows what IS allowed, not what was denied. `aa-status` shows which profiles are loaded and in what mode.*

---

**Question 17** (5 points)

A security baseline requires that the `/tmp` directory be mounted with `noexec,nosuid,nodev`. What is the primary security benefit of the `noexec` option specifically?

- A) It prevents files in `/tmp` from being owned by setuid binaries.
- B) It prevents binaries placed in `/tmp` from being executed directly, blocking a common malware staging technique.
- C) It prevents new filesystems from being mounted under `/tmp`.
- D) It prevents processes running from `/tmp` from accessing `/dev` devices.

**Correct Answer: B**

*Explanation: `noexec` prevents execution of binaries from the mounted filesystem. Attackers frequently upload malware to world-writable directories like `/tmp` and then execute it. With `noexec`, a file can be written to `/tmp` but running it directly (e.g., `/tmp/evil.sh`) is blocked. Note that `noexec` does not prevent shell interpretation (`bash /tmp/evil.sh` would still work), but it raises the bar for opportunistic attacks.*

---

**Question 18** (5 points)

An administrator runs `ausearch -m AVC -ts recent` and sees many AVC denials for the `httpd_t` domain trying to connect to the network. Before filing a bug report or permanently enabling the boolean, which command would temporarily allow this access to verify it resolves the issue?

- A) `setenforce 0`
- B) `setsebool httpd_can_network_connect on`
- C) `semanage boolean -M httpd_can_network_connect --on`
- D) `semodule --disable-policy httpd`

**Correct Answer: B**

*Explanation: `setsebool httpd_can_network_connect on` (without `-P`) changes the boolean for the current session only — a reboot or `setsebool httpd_can_network_connect off` reverts it. This allows the administrator to confirm that enabling this boolean resolves the application issue before making the change permanent with `-P`. Option A disables ALL SELinux enforcement globally, which is too broad for testing a specific denial.*

---

**Question 19** (5 points)

A security audit finds a world-writable directory with the sticky bit set. What does the sticky bit on a directory prevent?

- A) It prevents any user from writing files to the directory.
- B) It prevents files in the directory from being executed.
- C) It prevents users from deleting or renaming files owned by other users, even though the directory is writable.
- D) It forces all files created in the directory to inherit the directory's group ownership.

**Correct Answer: C**

*Explanation: The sticky bit on a directory means that users can create and write files in the directory, but can only delete or rename files they own. Other users' files are protected even in a world-writable directory. This is why `/tmp` (mode `1777`) allows any user to write files but prevents users from deleting each other's files. Option D describes SGID, not the sticky bit.*

---

**Question 20** (5 points)

Which tool generates a hardening report by comparing a running system's configuration against the CIS (Center for Internet Security) benchmarks for Linux?

- A) `lynis`
- B) `fail2ban-client`
- C) `tripwire`
- D) `ossec`

**Correct Answer: A**

*Explanation: Lynis is an open-source security auditing tool that performs a system hardening audit and checks against CIS benchmarks and other security standards. It produces a scored report with findings, warnings, and recommendations. Tripwire is a file integrity monitoring tool. fail2ban is a log-based IP blocker. OSSEC is a host-based intrusion detection system.*

---

### Answer Key

| Question | Answer |
|----------|--------|
| 1 | C |
| 2 | B |
| 3 | B |
| 4 | C |
| 5 | C |
| 6 | D |
| 7 | C |
| 8 | B |
| 9 | B |
| 10 | C |
| 11 | B |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | B |
| 16 | C |
| 17 | B |
| 18 | B |
| 19 | C |
| 20 | A |
