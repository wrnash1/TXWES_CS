# Reading Guide: Module 01 — Introduction to Linux and Open Source

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


## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 1 of CIS-3325 OS Administration Linux. This module establishes the conceptual and historical foundation for everything that follows. Before you can administer a Linux system, you need to understand what Linux is, why it exists, how it is structured, and how the major distribution families differ. This reading guide reinforces the video lecture content and prepares you for the module quiz and lab.

---

### 1. High-Yield Glossary

Review these definitions carefully. These terms appear on the CompTIA Linux+ exam and will be used throughout the course.

- **Linux kernel**: The core of the Linux operating system, written by Linus Torvalds in 1991. Manages hardware resources, memory, processes, and provides system calls that user programs use to interact with hardware. Licensed under GPL v2.
- **GNU Project**: Launched by Richard Stallman in 1983 with the goal of creating a free Unix-like operating system. Produced essential tools including bash, GCC, and the C library. GNU tools combined with the Linux kernel form what most people call "Linux."
- **FOSS**: Free and Open Source Software. "Free" refers to freedom (to run, study, modify, distribute) rather than price. Requires public access to source code.
- **GPL (GNU General Public License)**: A copyleft license — software licensed under the GPL must be distributed with source code, and derivative works must also be licensed under the GPL. The Linux kernel uses GPL v2.
- **MIT License**: A permissive open-source license. Code can be used in proprietary software without requiring the derivative work to be open sourced.
- **Apache License 2.0**: A permissive open-source license similar to MIT but with explicit patent grants. Used by many Apache Software Foundation projects.
- **Kernel**: The core component of an operating system. Runs in privileged mode (kernel space) with direct hardware access. Manages memory, processes, devices, and filesystems.
- **Shell**: The command interpreter — the program that reads user input and executes commands. Bash is the standard Linux shell.
- **Userspace**: All software that runs outside kernel space — applications, services, utilities, and tools. Communicates with the kernel through system calls.
- **System call (syscall)**: The mechanism by which user-space programs request services from the kernel. Examples: `read()`, `write()`, `fork()`, `execve()`.
- **Distribution (distro)**: A complete Linux-based operating system packaged with the Linux kernel, GNU tools, a package manager, and additional software. Examples: Ubuntu, RHEL, Arch.
- **Terminal emulator**: A graphical application that provides a text interface to the shell. Examples: GNOME Terminal, Konsole, Windows Terminal.
- **Bash**: Bourne Again Shell. The standard shell on most Linux distributions, written by Brian Fox for the GNU Project in 1989.
- **Virtual machine (VM)**: Software that simulates a complete computer system, allowing multiple operating systems to run on one physical machine.
- **VirtualBox**: A free, open-source virtualization platform from Oracle that runs on Windows, macOS, and Linux.
- **SSH (Secure Shell)**: A cryptographic network protocol for secure remote login and command execution. Encrypts all traffic including passwords.
- **CompTIA Linux+ XK0-005**: A vendor-neutral Linux administration certification exam. 90 questions, 90 minutes, passing score 720/900, four domains: System Management (32%), Security (21%), Scripting/Containers/Automation (19%), Troubleshooting (28%).
- **Minix**: A small Unix-like OS written by Andrew Tanenbaum in 1987 for educational purposes. Inspired Linus Torvalds to write the Linux kernel.
- **LTS (Long Term Support)**: A distribution release that receives security and maintenance updates for an extended period — typically 5 years for Ubuntu LTS releases.

---

### 2. Linux Distribution Families

The two most important distribution families for the Linux+ exam are the Debian family and the RHEL family.

| Feature | Debian Family | RHEL Family |
|---|---|---|
| Key distros | Debian, Ubuntu, Linux Mint, Kali | RHEL, CentOS Stream, Rocky Linux, Fedora |
| Package manager | `apt` | `dnf` (modern), `yum` (legacy) |
| Package format | `.deb` | `.rpm` |
| Default filesystem | ext4 | XFS |
| Auth log location | `/var/log/auth.log` | `/var/log/secure` |
| SELinux/AppArmor | AppArmor (Ubuntu) | SELinux (RHEL) |
| Firewall tool | `ufw` | `firewalld` |

Both families share the same underlying kernel and GNU tools. Command-line utilities like `ls`, `chmod`, `grep`, `sed`, and `awk` work identically across all distributions.

---

### 3. The Linux Architecture

Linux has three conceptual layers:

**Kernel layer**: Manages hardware. Runs in protected kernel space. Handles memory, process scheduling, device drivers, and filesystem I/O. User programs cannot directly access hardware — they must use syscalls.

**Shell layer**: The command interpreter. Bash reads your commands, parses them, and creates processes. The shell itself runs in userspace and uses syscalls to do its work.

**Userspace layer**: Everything else — applications, services, system utilities. Communicates with the kernel through the system call interface.

---

### 4. FOSS Licensing Quick Reference

For the Linux+ exam, know these three license types:

**GPL (copyleft)**: Derivative works must also be GPL. Share-alike. The Linux kernel uses GPL v2.

**MIT (permissive)**: Can use in proprietary software. No share-alike requirement. Very short, simple license text.

**Apache 2.0 (permissive)**: Similar to MIT but includes explicit patent grants and trademark provisions. Used by many enterprise-grade projects.

---

### Required Readings and Videos

- **Required Reading**: [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) — Chapters 1 and 2 (free online). Chapter 1 covers what the shell is; Chapter 2 covers navigation basics that will be reinforced in Module 2.
- **Required Video**: [LearnLinuxTV — Linux Fundamentals series](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), Episodes 1–3. These cover Linux history, distributions, and the terminal.

---

### Lab and Command Integration

This week's lab focuses on VM setup and first login. Before moving to Module 2, verify:

1. VirtualBox is installed on your host machine.
2. Ubuntu Server 22.04 LTS VM is created and boots successfully.
3. You can log in at the terminal with your username and password.
4. You see the bash prompt: `username@hostname:~$`

---

### 5. Study Checklist

- [ ] Define the four software freedoms that characterize FOSS.
- [ ] Explain the difference between GPL and MIT licenses.
- [ ] Describe the three layers of Linux architecture (kernel, shell, userspace).
- [ ] Name two Debian-family and two RHEL-family distributions.
- [ ] Identify the package manager used on each distribution family.
- [ ] Explain what a terminal emulator does and how it differs from the shell.
- [ ] Install VirtualBox and create an Ubuntu Server 22.04 VM.
- [ ] Complete the Module 1 quiz.

---

## 9. Supplemental Resources

**1. [The Linux Kernel Archives — Official Kernel Releases](https://www.kernel.org/)**
The official home of Linux kernel source releases. Provides historical releases, the latest stable kernel, and release notes. Useful for understanding kernel versioning and the release cadence Torvalds uses.

**2. [GNU Project — Free Software Foundation](https://www.gnu.org/licenses/gpl-3.0.en.html)**
The official text of the GNU General Public License v3 and accompanying explanations from the FSF. Essential reading for understanding copyleft, the four software freedoms, and what is actually required when distributing GPL-licensed software.

**3. [Ubuntu Server Official Documentation — Installation Guide](https://ubuntu.com/server/docs/installation)**
Canonical's official Ubuntu Server installation documentation. Covers the subiquity installer step-by-step, network configuration during install, and post-install verification steps directly relevant to the Module 1 lab.
