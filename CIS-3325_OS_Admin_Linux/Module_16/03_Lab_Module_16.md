# Lab: Module 16 — Linux+ XK0-005 Exam Preparation

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Lab Overview

**Estimated Time:** 90–120 minutes

**Purpose:** This lab simulates a performance-based question (PBQ) scenario similar to those on the Linux+ exam. Unlike earlier labs with guided steps, this lab presents tasks with expected outcomes — you must determine the correct commands without step-by-step guidance.

**Environment:** Linux VM (Rocky Linux 9 or Ubuntu 22.04). Root or sudo access required.

This lab is designed to replicate the PBQ experience. Read each scenario carefully, determine what to do, execute the commands, and document your results.

---

### PBQ-Style Scenario 1: System Services Investigation

**Situation:**

You are investigating a server that may be running unnecessary services. Complete all of the following tasks:

**Task 1a:** List all currently RUNNING service units. Redirect the output to `/tmp/running_services.txt`.

**Task 1b:** Identify which services failed at the last boot. Display the output on screen.

**Task 1c:** Check whether the `cups` print service is installed and running. If it is running but not needed, stop it (do not disable it — just stop it for this lab).

**Task 1d:** Create a simple custom service unit file at `/etc/systemd/system/labcheck.service` that runs `/bin/true` once at startup (Type=oneshot) with the description "Lab Health Check". Enable it.

**Expected verification:**

```bash
systemctl is-enabled labcheck
```

Should return `enabled`.

**Cleanup after verification:**

```bash
sudo systemctl disable labcheck
sudo rm /etc/systemd/system/labcheck.service
sudo systemctl daemon-reload
```

---

### PBQ-Style Scenario 2: User and Permission Audit

**Situation:**

You are auditing user accounts and file permissions on this server.

**Task 2a:** Create a new user named `auditor` with home directory `/home/auditor`, shell `/bin/bash`, and primary group `auditor`. Do not add to any supplementary groups.

**Task 2b:** Set a password for `auditor`. Then configure the account to require a password change every 60 days, with a 7-day minimum between changes and a 14-day warning before expiry.

**Task 2c:** Create a directory `/opt/audit-reports`. Set permissions so that:

- The directory owner is `root`
- The group is `auditor`
- Owner has full access (rwx)
- Group has read and execute (r-x)
- Others have no access (---)

**Task 2d:** Find all SUID files on the system. Save the list to `/tmp/suid_files.txt`.

**Task 2e:** Check if `auditor` can log in via SSH. Is SSH key auth configured for this account? (Answer by examining whether `~auditor/.ssh/authorized_keys` exists.)

**Expected verification for 2c:**

```bash
ls -ld /opt/audit-reports
```

Should show: `drwxr-x--- 2 root auditor ...`

**Cleanup:**

```bash
sudo userdel -r auditor
sudo rm -rf /opt/audit-reports /tmp/suid_files.txt
```

---

### PBQ-Style Scenario 3: Networking Configuration

**Situation:**

You need to investigate and document the network configuration of this server.

**Task 3a:** Display all network interfaces and their IP addresses in a single command that shows IPv4 addresses only.

**Task 3b:** What is the default gateway? Use a command that shows the routing table.

**Task 3c:** Determine what DNS server(s) this system is configured to use. Show the method you used to find this (resolv.conf, nmcli, or resolvectl).

**Task 3d:** Test DNS resolution by querying the A record for `github.com` using `dig`. Record the resolved IP address.

**Task 3e:** What TCP ports is this server currently listening on? List them using `ss` with the appropriate flags for TCP listening with numeric output and process names.

**Task 3f:** Verify the firewall is running. List all currently allowed services and ports in the default zone.

Document your findings in `/tmp/network_audit.txt`.

---

### PBQ-Style Scenario 4: Storage Health Check

**Situation:**

Perform a storage health assessment.

**Task 4a:** Display all mounted filesystems with their type, size, used, available, and usage percentage. Exclude tmpfs and devtmpfs.

**Task 4b:** Check inode usage for all mounted filesystems. Which filesystem has the highest inode usage percentage?

**Task 4c:** Find the 5 largest directories under `/var`. Save output sorted by size (largest first) to `/tmp/large_dirs.txt`.

**Task 4d:** Is LVM configured on this system? Run the appropriate commands to show all physical volumes, volume groups, and logical volumes.

**Task 4e:** The `/etc/fstab` file is the key to persistent storage configuration. Display the file contents and identify: (a) which entry is for the root filesystem, and (b) whether UUIDs or device paths are used for each entry.

Document your findings in `/tmp/storage_audit.txt`.

---

### PBQ-Style Scenario 5: Security Hardening Check

**Situation:**

Assess the security posture of this server.

**Task 5a:** What is the current SELinux or AppArmor status? Is it in enforcing/complain mode? Record the output of the appropriate status command.

**Task 5b:** Check the SSH server configuration for these specific directives:

- `PermitRootLogin`
- `PasswordAuthentication`
- `MaxAuthTries`
- `ClientAliveInterval`

For each, report the current configured value (or "not configured" if absent).

**Task 5c:** Review `/etc/login.defs` for password aging defaults. Report the current values for PASS_MAX_DAYS, PASS_MIN_DAYS, and PASS_WARN_AGE.

**Task 5d:** Is `fail2ban` installed and running? If installed, what jails are active?

**Task 5e:** Are there any audit rules currently active? List them.

Document your findings in `/tmp/security_audit.txt`.

---

### PBQ-Style Scenario 6: Scripting Task

**Situation:**

Write a shell script that performs a system summary and saves it to a file.

**Task 6:** Create the script `/opt/sysinfo.sh` with the following requirements:

- The script takes one argument: the output file path
- If no argument is provided, print a usage message and exit with code 1
- The script must collect and write to the output file:
  - Hostname
  - Operating system name and version
  - Kernel version
  - Uptime
  - Number of running processes
  - Memory total and available
  - Disk usage for the root filesystem (percentage used)
  - IP address of the primary interface
- The script must be executable
- The script must have a shebang line

Test your script:

```bash
sudo bash /opt/sysinfo.sh /tmp/sysinfo_output.txt
cat /tmp/sysinfo_output.txt
```

**Cleanup:**

```bash
sudo rm /opt/sysinfo.sh /tmp/sysinfo_output.txt
```

---

### Lab Submission Requirements

Submit a lab report in PDF format containing:

1. Terminal output or screenshots for each task's verification step
2. The complete contents of `/opt/sysinfo.sh` (Scenario 6)
3. Answers to all "record" and "document" tasks above
4. Self-assessment: For each scenario, rate your confidence (High/Medium/Low) and identify which topic areas you need to review before the exam

---

### Grading Rubric

| Scenario | Points |
|---------|--------|
| Scenario 1: Service management | 15 |
| Scenario 2: User and permission audit | 20 |
| Scenario 3: Networking | 15 |
| Scenario 4: Storage health check | 15 |
| Scenario 5: Security hardening check | 15 |
| Scenario 6: Shell script | 20 |
| **Total** | **100** |

---

### Exam Tips Embedded in this Lab

This lab deliberately lacks step-by-step guidance because the Linux+ exam will not give it to you either. If you struggled with specific scenarios:

- Scenario 1 weakness: review Module 12 (systemctl, unit files)
- Scenario 2 weakness: review Module 6 (user management, permissions)
- Scenario 3 weakness: review Module 11 (networking, DNS)
- Scenario 4 weakness: review Module 13 (LVM, fstab)
- Scenario 5 weakness: review Module 14 and 15 (SSH, SELinux, security)
- Scenario 6 weakness: review Module 9 (shell scripting)

Complete each scenario without looking at module notes on your first attempt. Then review, correct, and document what you had to look up — those are your study priorities.

---

## Part 9 — Challenge Exercise

### Challenge 1: Timed Full-System Audit

Simulate an exam performance-based question under timed conditions by completing a comprehensive system audit with no reference materials.

1. Set a 20-minute timer. Without referencing any module notes, complete all of the following tasks and document each command and its output: (a) display the full kernel version and architecture; (b) show all block devices and their filesystems with UUIDs; (c) list all LVM volume groups and their free space; (d) show all listening TCP/UDP ports with the process owning each; (e) display the currently active firewalld zone and its allowed services; (f) show the SELinux status and current mode; (g) list all users with UID >= 1000 from `/etc/passwd`; (h) display the last 5 failed authentication attempts from the journal.
2. After completing step 1 (or when time expires), review your answers. For each task where you used an incorrect command, needed to look something up, or produced incomplete output — add that topic to a "gap list." This gap list represents your personalized final study priorities before the Linux+ exam.
3. Re-attempt any tasks from step 1 that were on your gap list, this time checking the correct syntax from the relevant module's reading guide. Document the correct command for each gap item with a brief explanation of what flag or syntax you missed.
4. Calculate your audit speed: how many of the 8 tasks did you complete correctly within 20 minutes? Exam pace requires roughly 1 minute per question for the 90-minute, 90-question exam. Repeat this exercise with a different set of tasks until you can complete 8 tasks correctly in under 15 minutes.

### Challenge 2: End-to-End Automation Script

Write a single orchestration script that ties together skills from every module in the course — demonstrating integrated Linux administration competency.

1. Create `~/final_challenge.sh` with strict mode (`set -euo pipefail`). The script should accept a `--report` or `--fix` argument: in report mode, it surveys the system and outputs a status report; in fix mode, it applies remediations. Implement argument parsing with `case "$1" in --report) MODE=report ;; --fix) MODE=fix ;; *) echo "Usage: $0 [--report|--fix]"; exit 1 ;; esac`.
2. Implement the following report checks (in `--report` mode, print PASS/FAIL for each): (a) SSH `PasswordAuthentication` is disabled: `grep -q "^PasswordAuthentication no" /etc/ssh/sshd_config`; (b) `root` account is locked: `sudo passwd -S root | grep -q " L "`; (c) `/tmp` is mounted with `noexec`: `mount | grep " /tmp " | grep -q "noexec"`; (d) `fail2ban` is active: `systemctl is-active fail2ban > /dev/null 2>&1`; (e) no world-writable files exist in `/etc`: `[ -z "$(sudo find /etc -maxdepth 1 -type f -perm -002 2>/dev/null)" ]`.
3. Implement the `--fix` mode that automatically remediates each FAIL item: (a) disable SSH password auth by running `sudo sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config && sudo systemctl reload sshd`; (b) lock root: `sudo passwd -l root`; (c) add `noexec` to `/tmp` fstab entry if absent; (d) enable and start fail2ban: `sudo systemctl enable --now fail2ban`. Each fix should be idempotent — running it twice should produce no errors.
4. Test both modes: run `bash ~/final_challenge.sh --report` and record the baseline state. Apply one deliberate misconfiguration (e.g., `sudo passwd -u root` to unlock root). Run `--report` again to confirm it detects the change. Run `--fix` to remediate. Run `--report` one final time to confirm all checks pass. Document the complete test cycle output.

### Reflection Questions

1. Throughout this course you have used dozens of commands across system administration, security, networking, storage, and automation. Identify the single command or utility you found most counterintuitive (had the hardest time remembering the correct syntax or flags) and explain the mental model or mnemonic you developed to remember it reliably. What does this exercise suggest about how you learn command-line tools?

2. Linux administration is increasingly automated through tools like Ansible, Terraform, and container orchestration. Despite this, the CompTIA Linux+ exam still tests manual command-line skills. Argue both sides of the following question: "In a world where infrastructure is managed as code, is deep knowledge of individual Linux commands still professionally valuable, or has it become an anachronism?" Base your argument on specific scenarios from the lab exercises in this course where manual command knowledge was essential.
