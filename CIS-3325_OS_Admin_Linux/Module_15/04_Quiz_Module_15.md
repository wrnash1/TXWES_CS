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
