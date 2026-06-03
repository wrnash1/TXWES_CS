# Lab: Module 15 — Linux Security Hardening

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Lab Overview

**Estimated Time:** 75–90 minutes

**Environment:** Linux VM (Rocky Linux 9 preferred for SELinux tasks; Ubuntu 22.04 for AppArmor tasks). Root or sudo access required.

**Objectives:**

- Check and change SELinux modes
- Fix an SELinux context issue with `restorecon`
- Manage SELinux booleans
- Configure auditd rules and query results
- Configure fail2ban for SSH protection
- Set password aging policy with `chage`

---

### Lab Environment Setup

Verify your system's security posture:

```bash
getenforce 2>/dev/null || aa-status 2>/dev/null | head -5
```

This will show either the SELinux status or AppArmor status depending on your distribution.

---

### Part 1: SELinux Management (Rocky Linux / RHEL)

**Skip Part 1 if using Ubuntu — proceed to Part 1-A (AppArmor)**

**Task 1.1 — Check SELinux Status**

```bash
getenforce
sestatus
```

Record:

- Current mode (Enforcing/Permissive/Disabled)
- Policy name
- Policy MLS status

**Task 1.2 — Switch to Permissive Mode**

```bash
sudo setenforce 0
getenforce
```

Confirm the mode changed. Note that this is runtime only.

**Task 1.3 — Switch Back to Enforcing**

```bash
sudo setenforce 1
getenforce
```

**Task 1.4 — View File Contexts**

```bash
ls -Z /etc/passwd /etc/shadow
ls -Z /var/www/html/ 2>/dev/null || echo "No web dir found"
ps -Z | head -10
```

Record the security context (user:role:type:level) for `/etc/passwd`.

**Task 1.5 — Create a File and Fix Its Context**

Simulate the common scenario of copying a file to the wrong location:

```bash
sudo touch /var/www/html/test.html 2>/dev/null || sudo mkdir -p /var/www/html && sudo touch /var/www/html/test.html
cp /etc/passwd /var/www/html/misplaced.txt
ls -Z /var/www/html/misplaced.txt
```

The copied file will have type `etc_t` instead of `httpd_sys_content_t`. Fix it:

```bash
sudo restorecon -v /var/www/html/misplaced.txt
ls -Z /var/www/html/misplaced.txt
```

Verify the context was corrected.

Cleanup:

```bash
sudo rm /var/www/html/misplaced.txt
```

**Task 1.6 — SELinux Booleans**

List all booleans related to HTTP:

```bash
getsebool -a | grep httpd
```

Check the value of `httpd_can_network_connect`:

```bash
getsebool httpd_can_network_connect
```

Temporarily enable it:

```bash
sudo setsebool httpd_can_network_connect on
getsebool httpd_can_network_connect
```

Check that it is enabled. Note: this is runtime only (not permanent). Disable it again:

```bash
sudo setsebool httpd_can_network_connect off
```

**Task 1.7 — View the AVC Log**

```bash
sudo ausearch -m avc -ts recent 2>/dev/null
sudo ausearch -m avc -ts today 2>/dev/null | tail -20
```

Are there any recent SELinux denials? If so, record what was denied.

---

### Part 1-A: AppArmor Management (Ubuntu)

**Skip Part 1-A if using Rocky Linux — proceed to Part 2**

**Task 1A.1 — Check AppArmor Status**

```bash
sudo aa-status
```

Record:

- Number of loaded profiles
- Number in enforce mode
- Number in complain mode

**Task 1A.2 — View Profile Location**

```bash
ls /etc/apparmor.d/ | head -20
```

**Task 1A.3 — Switch a Profile to Complain Mode**

If `/usr/sbin/sshd` has a profile:

```bash
sudo aa-complain /usr/sbin/sshd 2>/dev/null || echo "Profile not found, using cups"
sudo aa-complain /usr/sbin/cups-browsed 2>/dev/null || echo "Using next available"
```

If neither is available, choose any profile shown in `aa-status` that is in enforce mode.

Check the status change:

```bash
sudo aa-status | grep complain
```

Return to enforce mode:

```bash
sudo aa-enforce /etc/apparmor.d/usr.sbin.sshd 2>/dev/null || true
```

**Task 1A.4 — View AppArmor Denials**

```bash
sudo journalctl -k --since "1 hour ago" | grep DENIED
```

Are there any AppArmor denials? Record any found.

---

### Part 2: auditd Configuration

**Task 2.1 — Verify auditd is Running**

```bash
systemctl status auditd
sudo auditctl -l
```

Record any currently active rules.

**Task 2.2 — Add Audit Rules**

Add rules to monitor sensitive files:

```bash
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
sudo auditctl -w /etc/shadow -p wa -k shadow_changes
sudo auditctl -w /etc/sudoers -p wa -k sudoers_changes
```

Verify rules were added:

```bash
sudo auditctl -l
```

**Task 2.3 — Generate Audit Events**

Trigger an audit event by modifying `/etc/passwd` metadata (do NOT change its content):

```bash
sudo touch /etc/passwd
```

Wait 2 seconds, then query:

```bash
sudo ausearch -k passwd_changes --format text
```

You should see an event recording the `touch` operation.

**Task 2.4 — Make Rules Persistent**

Create a rules file:

```bash
sudo bash -c 'cat > /etc/audit/rules.d/lab-rules.rules << EOF
-w /etc/passwd -p wa -k passwd_changes
-w /etc/shadow -p wa -k shadow_changes
-w /etc/sudoers -p wa -k sudoers_changes
EOF'

sudo augenrules --load
sudo auditctl -l
```

Verify the rules are loaded.

**Task 2.5 — Generate and View a Report**

```bash
sudo aureport --summary
sudo aureport --auth
sudo aureport --failed
```

Record:

- Total number of events in the report
- Number of authentication events
- Number of failed events

**Task 2.6 — Cleanup Audit Rules**

```bash
sudo rm /etc/audit/rules.d/lab-rules.rules
sudo augenrules --load
sudo auditctl -l
```

Confirm the lab rules are removed.

---

### Part 3: fail2ban Configuration

**Task 3.1 — Install and Start fail2ban**

```bash
# Rocky Linux:
sudo dnf install fail2ban -y

# Ubuntu:
sudo apt install fail2ban -y

sudo systemctl enable --now fail2ban
fail2ban-client status
```

**Task 3.2 — Create jail.local**

```bash
sudo bash -c 'cat > /etc/fail2ban/jail.local << EOF
[DEFAULT]
bantime  = 10m
findtime = 5m
maxretry = 3
backend  = systemd

[sshd]
enabled = true
port    = ssh
maxretry = 3
bantime  = 1h
EOF'
```

Reload fail2ban:

```bash
sudo fail2ban-client reload
```

**Task 3.3 — Verify the Jail is Active**

```bash
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

Record:

- Currently failed count
- Currently banned IPs

**Task 3.4 — Test Manual Ban and Unban**

Manually ban a test IP (use a private address that does not affect production):

```bash
sudo fail2ban-client set sshd banip 192.168.250.99
sudo fail2ban-client status sshd
```

Verify the IP appears as banned.

Unban it:

```bash
sudo fail2ban-client set sshd unbanip 192.168.250.99
sudo fail2ban-client status sshd
```

Verify the IP is no longer banned.

**Task 3.5 — View fail2ban Logs**

```bash
sudo journalctl -u fail2ban --since "30 minutes ago"
```

Confirm the ban and unban events appear in the log.

---

### Part 4: Password Policies

**Task 4.1 — Check Current Password Aging**

```bash
sudo chage -l $(whoami)
```

Record all current values (minimum days, maximum days, warning days, expiration date).

**Task 4.2 — View /etc/login.defs**

```bash
grep -E "^PASS_" /etc/login.defs
```

Record the current PASS_MAX_DAYS, PASS_MIN_DAYS, and PASS_WARN_AGE values.

**Task 4.3 — Create a Test User**

```bash
sudo useradd -m testuser_lab
sudo passwd testuser_lab
```

Set a simple password when prompted.

**Task 4.4 — Configure Password Aging**

```bash
sudo chage -M 90 -m 7 -W 14 testuser_lab
sudo chage -l testuser_lab
```

Verify the changes were applied.

**Task 4.5 — Force Password Change on Next Login**

```bash
sudo chage -d 0 testuser_lab
sudo chage -l testuser_lab
```

Note the "Last password change" field should now show "password must be changed."

**Task 4.6 — Check PAM Password Quality**

```bash
cat /etc/security/pwquality.conf 2>/dev/null || echo "File not found"
grep pam_pwquality /etc/pam.d/common-password 2>/dev/null || \
grep pam_pwquality /etc/pam.d/system-auth 2>/dev/null
```

Record the current password quality settings.

**Task 4.7 — Cleanup Test User**

```bash
sudo userdel -r testuser_lab
```

---

### Part 5: CIS Benchmark Assessment (Optional — if time permits)

**Task 5.1 — Install OpenSCAP**

```bash
# Rocky Linux:
sudo dnf install openscap openscap-utils scap-security-guide -y

# Ubuntu:
sudo apt install libopenscap8 ssg-debderived -y 2>/dev/null || \
sudo apt install openscap-scanner -y
```

**Task 5.2 — Run a Basic Assessment**

```bash
# Rocky Linux:
ls /usr/share/xml/scap/ssg/content/ | grep rl9

sudo oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis_server_l1 \
  --report /tmp/cis-report.html \
  /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml 2>/dev/null | tail -5
```

**Task 5.3 — Review the Report**

If a graphical browser is available, open `/tmp/cis-report.html`.

Otherwise, check the XML results:

```bash
sudo oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis_server_l1 \
  --results /tmp/cis-results.xml \
  /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml 2>/dev/null

grep -c "result>pass" /tmp/cis-results.xml
grep -c "result>fail" /tmp/cis-results.xml
```

Record the number of passing and failing checks.

---

### Lab Submission Requirements

Submit a PDF report containing:

1. SELinux or AppArmor status output (Task 1.1 or 1A.1)
2. Output showing corrected file context (Task 1.5) or AppArmor denial log check (Task 1A.4)
3. auditd query output showing the generated audit event (Task 2.3)
4. fail2ban jail status showing the manual ban (Task 3.4)
5. `chage -l` output before and after setting password aging (Task 4.2 and 4.4)
6. Brief paragraph: describe a realistic scenario where setting SELinux to Permissive "to fix a problem" creates a security risk, and explain the correct alternative

---

### Grading Rubric

| Section | Points |
|---------|--------|
| Part 1: SELinux or AppArmor | 20 |
| Part 2: auditd configuration and queries | 25 |
| Part 3: fail2ban configuration | 20 |
| Part 4: Password policies | 25 |
| Written analysis | 10 |
| **Total** | **100** |
