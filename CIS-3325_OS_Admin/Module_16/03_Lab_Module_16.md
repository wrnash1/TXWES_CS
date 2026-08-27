# Lab Activity: Module 16 - Final Prep
## Course: CIS-3325_OS_Admin (CompTIA Linux+ (XK0-005))

---

**Objective:** 
Your final exam for this course is the official **LPI Linux Essentials (010-160)** certification exam. You must schedule and take this exam at the ComputerMinds testing center.

**Instructions:**
1. Arrive at the ComputerMinds testing center at your scheduled time with two forms of valid ID.
2. Complete the LPI Linux Essentials (010-160) exam.
3. Once finished, you will receive an official printout or digital copy of your score report.

**Deliverable:**
Upload a scanned copy, clear photograph, or official PDF of your final score report to this Canvas drop-box. 

*Note: Your final grade will be calculated based on the prorated score of this exam as outlined in the Syllabus Grading Policy.*

---

## Part 9 — Challenge Exercise

### Challenge 1: Timed Cross-Domain Diagnostic Drill
Simulate exam-day conditions by completing a timed sequence of diagnostic tasks on a live Ubuntu 22.04 or RHEL 9 VM. Set a 30-minute timer before starting.

1. Storage and filesystems: Run `lsblk` and `df -h` to identify all mounted filesystems. Create a 100 MB sparse file with `dd if=/dev/zero of=/tmp/testdisk.img bs=1M count=100`, format it as ext4 with `mkfs.ext4 /tmp/testdisk.img`, and mount it to `/mnt/testdisk`. Confirm the mount with `mount | grep testdisk` and record the filesystem type and size. Unmount and delete the file when done.
2. Process and network inspection: Use `ps aux --sort=-%mem | head -10` to identify the top 10 memory consumers. Run `ss -tuln` and note which ports are in LISTEN state on `0.0.0.0` vs `127.0.0.1`. Use `journalctl -p err -n 20` to list the 20 most recent error-level log entries and identify the service generating the most errors.
3. User and permission audit: Run `awk -F: '$3 >= 1000 {print $1, $3}' /etc/passwd` to list all non-system users and their UIDs. Find all SUID binaries with `find /usr/bin /usr/sbin -perm -4000 -type f`. Calculate the effective permissions for a file with `chmod 640` owned by root:adm when accessed by a user in the `adm` group.
4. After the timer ends, review which tasks slowed you down. Those topics are your highest-priority review areas before exam day.

### Challenge 2: Full-Domain Practice Scenario
Work through a realistic multi-skill scenario that combines topics from Domains 1-4 of the CompTIA Linux+ exam.

1. Create a new user `labfinale` with home directory and bash shell: `sudo useradd -m -s /bin/bash labfinale && sudo passwd labfinale`. Set the account to expire in 30 days using `chage`. Confirm the expiry with `chage -l labfinale`.
2. Write a bash script `/usr/local/bin/disk-guard.sh` that checks if any filesystem listed in `df -h` is above 80% usage and writes a warning line to `/var/log/disk-guard.log` for each one. Use `set -e` at the top. Make it executable and run it manually to confirm it produces output.
3. Schedule the script with a systemd timer: create `/etc/systemd/system/disk-guard.service` (Type=oneshot, ExecStart pointing to the script) and `/etc/systemd/system/disk-guard.timer` (OnCalendar=daily, Persistent=true). Run `systemctl daemon-reload && systemctl enable --now disk-guard.timer`. Verify with `systemctl list-timers | grep disk-guard`.
4. Open port 9090/tcp in the host firewall permanently (`firewall-cmd --permanent --add-port=9090/tcp && firewall-cmd --reload` on RHEL, or `ufw allow 9090/tcp` on Ubuntu). Confirm with `ss -tuln` that the rule is active, then remove the rule and confirm it is gone.

### Reflection Questions

1. You receive an exam question: "A junior admin changed a critical system file and used `chmod 777` to ensure everyone can write to it. What is the security risk, and what is the correct permission set for a world-readable but only root-writable file?" Write a complete answer covering DAC concepts, the numeric permission value, and why world-writable system files are dangerous.
2. After your certification exam, you onboard to a Linux sysadmin role. On day one you need to verify that a RHEL 9 server is healthy before it goes into production. List at least eight specific commands you would run, explain what each one tells you, and identify the single most important thing to check for each of the four exam domains (system management, security, networking, automation).
