# Reading Guide: Module 16 - Final Exam Prep & CompTIA Linux+ Certification

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 16 – Final Exam Prep & CompTIA Linux+ Certification**! This final module consolidates everything covered across the course — Linux installation, filesystem navigation, permissions, user management, package management, process management, shell scripting, storage, networking, SSH, firewalls, logging, scheduling, SELinux/AppArmor, and containers — all mapped to the CompTIA Linux+ XK0-005 exam domains. This is your integrated review and exam preparation week.

As you work through this material you will review high-yield command summaries by domain, practice identifying exam traps, reinforce your weakest topic areas, and build confidence for the Linux+ certification exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **XK0-005 exam domains and weights**: The CompTIA Linux+ XK0-005 exam is divided into four domains: **Domain 1.0 – System Management** (32%) covers installation, storage, networking, filesystems, process management, and scheduling. **Domain 2.0 – Security** (21%) covers permissions, user management, SSH, firewalls, SELinux/AppArmor, and encryption. **Domain 3.0 – Scripting, Containers, and Automation** (19%) covers bash scripting, Docker, and CI/CD concepts. **Domain 4.0 – Troubleshooting** (28%) covers diagnosing and resolving system, storage, network, and security issues. High-weight domains deserve proportionally more study time.
*   **Domain 1 command recap**: `ip addr show`, `nmcli con mod`, `fdisk`/`parted`, `mkfs.ext4`/`mkfs.xfs`, `mount`, `/etc/fstab` (UUID), `pvcreate`/`vgcreate`/`lvcreate`/`lvextend`/`resize2fs`, `mdadm`, `systemctl start/stop/enable/disable/daemon-reload`, `ps aux`, `top`, `nice`/`renice`, `kill -9`/`kill -15`, `crontab -e`, `at`.
*   **Domain 2 command recap**: `chmod`/`chown`/`umask`, `useradd`/`usermod`/`userdel`, `groupadd`/`usermod -aG`, `visudo`/`/etc/sudoers`, `ssh`/`ssh-keygen`/`ssh-copy-id`, `/etc/ssh/sshd_config` (`PermitRootLogin no`, `PasswordAuthentication no`), `firewall-cmd --permanent --add-service`/`--reload`, `ufw enable`/`ufw allow`, `iptables -A INPUT -j DROP`, `getenforce`/`setenforce`, `restorecon`, `setsebool -P`, `ausearch -m avc`.
*   **Domain 3 command recap**: `#!/bin/bash` shebang, variables (`$VAR`, `${VAR}`), conditionals (`[[ -d dir ]]`, `[[ -f file ]]`, `-eq`/`-ne`/`-z`/`-n`), loops (`for`/`while`/`until`), `$?` exit code, `$#` argument count, `$@` all arguments, `break`/`continue`/`return`, `docker pull`/`run`/`ps`/`stop`/`rm`/`logs`/`exec`/`images`, Dockerfile `FROM`/`RUN`/`COPY`/`CMD`/`EXPOSE`.
*   **Domain 4 troubleshooting recap**: `journalctl -u service -b -p err`, `ausearch -m avc -ts recent`, `/var/log/secure` (RHEL) or `/var/log/auth.log` (Ubuntu), `dmesg | tail`, `df -h` (disk space), `lsblk` (block devices), `ss -tuln` (listening ports), `ping`/`traceroute`/`dig` (connectivity), `vmstat 1 5` (`wa` = I/O wait), `top` (CPU/memory), `rpm -V` (package integrity), `strace` (syscall tracing).
*   **Exam format and strategy**: The Linux+ XK0-005 exam contains up to 90 questions (multiple choice and performance-based). Performance-based questions (PBQs) simulate real Linux command-line scenarios — they appear first and are worth more points. Strategy: answer all multiple-choice questions first, flag PBQs, return to them with remaining time. Passing score is 720/900. The exam is 90 minutes. CompTIA does not penalize for guessing — never leave a question blank.

---

### 2. Certification Exam Tips
*   **Domain weighting strategy:** Domain 1 (System Management, 32%) and Domain 4 (Troubleshooting, 28%) together make up 60% of the exam. Prioritize these if time is limited. Review LVM workflow, RAID levels, `systemctl` commands, log files, and `journalctl` flags thoroughly.
*   **Performance-based question (PBQ) strategy:** PBQs present a simulated terminal or GUI. Read the scenario completely before typing. Use `man` pages or `--help` if available in the simulation. Common PBQ topics: configuring `/etc/fstab`, writing a crontab entry, fixing file permissions, or running `firewall-cmd` commands.
*   **Command flag precision:** The exam tests exact flag syntax. Know `-L` vs `-l`, `--permanent` vs runtime, `-p err` vs `-p emerg`, `chmod 600` vs `chmod 640`. Wrong flags are deliberately placed as distractors.
*   **Distro awareness:** The exam covers both RHEL-family and Debian-family distributions. Know which commands and file paths differ: `apt` vs `dnf`, `/var/log/auth.log` vs `/var/log/secure`, `ufw` vs `firewalld`, `aa-status` (AppArmor/Ubuntu) vs `sestatus` (SELinux/RHEL).
*   **Final review resource:** Use the CompTIA Linux+ XK0-005 Exam Objectives document (available free at comptia.org) as a checklist. Every objective listed is fair game. Cross-reference any objective you cannot confidently explain back to the relevant course module.
*   **Study Resource:** The free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers the majority of Domain 1, 3, and 4 topics across its 36 chapters — it is the most comprehensive single review resource available at no cost. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) provides video reinforcement for all major topic areas covered in this course.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review your notes and revisit weak-area chapters across the complete free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) — pay particular attention to chapters covering storage, scripting, and security, which map to the heaviest exam domains.
*   **Required Video:** Review the full [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) playlist, focusing on any topic areas where you feel least confident — this free YouTube series covers all major XK0-005 topic areas with live demonstrations.

---

### Lab & Command Integration
This week's activity is a comprehensive command review: run through the Domain 1–4 command recaps above in a live Linux VM, execute each command, observe the output, and confirm you understand what each flag does. Pay special attention to any command that produced unexpected output or errors.

---

### 3. Study Checklist
- [ ] Read the glossary terms and review all four domain command recaps.
- [ ] Revisit weak-area chapters in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Review the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) videos for any topics needing reinforcement.
- [ ] Download and review the CompTIA Linux+ XK0-005 Exam Objectives from comptia.org.
- [ ] Complete the final exam practice quiz and review all incorrect answers.

---

## 9. Supplemental Resources

The following free, open-access resources support Module 16 — Linux+ Certification Exam Preparation:

**1. CompTIA Linux+ XK0-005 Exam Objectives (Official)**
https://www.comptia.org/certifications/linux
The official CompTIA Linux+ certification page with downloadable exam objectives PDF. Every objective listed is testable — use this as a final checklist before exam day.

**2. The Linux Command Line by William Shotts (Free OER Textbook)**
https://linuxcommand.org/tlcl.php
Complete, freely available textbook covering bash, scripting, file management, processes, storage, and networking. Cross-references all four XK0-005 exam domains. The definitive single-volume review resource.

**3. Professor Messer — CompTIA Linux+ Study Resources**
https://www.professormesser.com/linux-plus/
Free video study guide covering all XK0-005 exam objectives with short, focused video segments. Includes practice exams and study notes available at no cost.

**4. Linux Foundation — Free Training Courses**
https://training.linuxfoundation.org/resources/?_sft_content_type=free-course
The Linux Foundation's catalog of free courses including Introduction to Linux (LFS101x), which provides an excellent comprehensive review of topics spanning all four exam domains.
