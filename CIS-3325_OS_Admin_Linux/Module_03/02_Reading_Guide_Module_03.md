# Reading Guide: Module 03 — Linux Filesystem Hierarchy Standard

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

Module 3 covers the Linux Filesystem Hierarchy Standard (FHS) and the tools used to read, find, and process file content. The FHS is the map of the Linux directory tree — administrators who know it can find configuration files, logs, and system resources immediately, without guessing. The file-reading and searching tools introduced in Part 2 are the day-to-day instruments of Linux administration.

---

### 1. High-Yield Glossary

- **FHS (Filesystem Hierarchy Standard)**: A specification maintained by the Linux Foundation that defines the directory structure and directory contents in Linux and Unix-like operating systems.
- **`/`**: The root directory. The top of the directory tree. Everything on a Linux system is under `/`.
- **`/bin`**: Essential user binaries. Commands required before other filesystems are mounted: `ls`, `cp`, `mv`, `bash`, `grep`. Often symlinked to `/usr/bin` on modern distros.
- **`/sbin`**: System administration binaries typically run by root: `fdisk`, `mkfs`, `mount`, `ip`, `shutdown`.
- **`/usr`**: User system resources. Contains the majority of user programs (`/usr/bin`), system programs (`/usr/sbin`), libraries (`/usr/lib`), and locally installed software (`/usr/local`).
- **`/usr/local`**: For software compiled and installed manually (not from the package manager). Takes precedence over system tools in PATH.
- **`/etc`**: System-wide configuration files. Editable text files that control system behavior. No binaries should be in `/etc`.
- **`/var`**: Variable data that grows over time: logs (`/var/log`), databases (`/var/lib`), mail queues (`/var/spool`), caches (`/var/cache`).
- **`/var/log`**: Log files directory. Subdirectories for specific services (e.g., `/var/log/apache2`).
- **`/tmp`**: Temporary files writable by all users. Cleared at reboot. Sticky bit is set.
- **`/home`**: User home directories. Each user gets `/home/username`.
- **`/root`**: Home directory for the root superuser. Separate from `/home`.
- **`/opt`**: Optional/add-on application software packages. Third-party software installed outside the package manager.
- **`/mnt`**: Temporary mount point for manually mounted filesystems.
- **`/media`**: Mount points for automatically mounted removable devices (USB drives, optical discs).
- **`/dev`**: Device files. `/dev/sda` (first hard drive), `/dev/null` (discard), `/dev/zero` (null bytes), `/dev/random` (random data).
- **`/dev/null`**: A special file that discards all data written to it. Reading returns EOF. Used to suppress command output: `command > /dev/null 2>&1`.
- **`/proc`**: Virtual filesystem exposing kernel and process information. Not on disk. Generated at runtime. Key files: `/proc/cpuinfo`, `/proc/meminfo`, `/proc/uptime`.
- **`/sys`**: Virtual filesystem (sysfs) exposing kernel objects, devices, and driver parameters.
- **`cat`**: Concatenate and print. Shows entire file content to terminal. Best for short files.
- **`less`**: Page-through file viewer. `/` to search, `n` next match, `q` to quit. Handles files of any size efficiently.
- **`more`**: Older page-through viewer. Forward-only navigation. Largely superseded by `less`.
- **`head`**: Shows the first N lines of a file. Default 10. `-n 20` for 20 lines.
- **`tail`**: Shows the last N lines of a file. Default 10. `-f` flag follows the file in real time for live log monitoring.
- **`find`**: Searches the filesystem for files matching criteria. Key options: `-name` (case-sensitive), `-iname` (case-insensitive), `-type f` (files only), `-type d` (dirs only), `-size +10M` (larger than 10 MB), `-mtime -7` (modified in last 7 days), `-exec` (run command on each result).
- **`locate`**: Fast filename search using a pre-built database. Run `sudo updatedb` to refresh. Cannot search by size, permissions, or modification time.
- **`updatedb`**: Rebuilds the locate database. Run as root.
- **Glob (file globbing)**: Shell pattern expansion before a command executes. `*` = any string, `?` = one character, `[abc]` = one of the listed characters. Processed by the shell, not by the command.
- **stdin (fd 0)**: Standard input. Default source: keyboard.
- **stdout (fd 1)**: Standard output. Default destination: terminal.
- **stderr (fd 2)**: Standard error. Default destination: terminal.
- **`>` (redirect stdout)**: Sends stdout to a file, overwriting it.
- **`>>` (append stdout)**: Appends stdout to a file without overwriting.
- **`2>` (redirect stderr)**: Sends stderr to a file.
- **`2>&1`**: Redirects stderr to the same destination as stdout.
- **`<` (redirect stdin)**: Reads stdin from a file.
- **`|` (pipe)**: Connects stdout of one command to stdin of the next.
- **`tee`**: Reads stdin and writes to both stdout and a file simultaneously. Useful for saving output while still seeing it on screen.

---

### 2. FHS Quick Reference

| Directory | Purpose | Key Contents |
|---|---|---|
| `/bin` | Essential user binaries | `ls`, `cp`, `bash`, `grep` |
| `/sbin` | System admin binaries | `fdisk`, `mount`, `ip` |
| `/etc` | Configuration files | `passwd`, `shadow`, `fstab`, `sshd_config` |
| `/home` | User home directories | `/home/username` |
| `/root` | Root user home | Root's config files |
| `/tmp` | Temporary files | Cleared on reboot, sticky bit set |
| `/var/log` | Log files | `syslog`, `auth.log`, `secure` |
| `/var/lib` | Application state | MySQL data, package databases |
| `/opt` | Third-party software | Google Chrome, vendor apps |
| `/dev` | Device files | `sda`, `null`, `zero`, `random` |
| `/proc` | Kernel/process info | `cpuinfo`, `meminfo`, `uptime` |
| `/sys` | Hardware/driver info | Network interfaces, block devices |

---

### 3. find Command Quick Reference

| Task | Command |
|---|---|
| Find by name | `find /path -name "filename"` |
| Case-insensitive | `find /path -iname "filename"` |
| Files only | `find /path -type f` |
| Directories only | `find /path -type d` |
| Larger than 10 MB | `find /path -size +10M` |
| Modified last 7 days | `find /path -mtime -7` |
| Run command on results | `find /path -name "*.log" -exec ls -lh {} \;` |
| Suppress permission errors | `find /path ... 2>/dev/null` |

---

### 4. Standard Streams and Redirection

| Operator | Effect |
|---|---|
| `>` | Redirect stdout to file (overwrite) |
| `>>` | Redirect stdout to file (append) |
| `2>` | Redirect stderr to file |
| `2>&1` | Redirect stderr to stdout |
| `< file` | Redirect file to stdin |
| `\|` | Pipe stdout to next command's stdin |
| `tee file` | Write to stdout and file simultaneously |

---

### Required Readings and Videos

- **Required Reading**: [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) — Chapters 3, 5, 6, and 7. Chapter 3: exploring the system (FHS); Chapter 5: redirection; Chapter 6: pipelines; Chapter 7: seeing the world as the shell sees it (globbing).
- **Required Video**: [LearnLinuxTV — Linux Fundamentals](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), Episodes 7–9. These cover the filesystem hierarchy, working with files, and basic redirection.

---

### Study Checklist

- [ ] Name the purpose of each major FHS directory from memory.
- [ ] Explain the difference between `/bin` and `/usr/bin`.
- [ ] Identify the correct log file path for authentication events on Ubuntu and on RHEL.
- [ ] Demonstrate `find` with at least three different criteria combined.
- [ ] Explain the difference between `locate` and `find`.
- [ ] Write a pipeline that reads a log file, filters for errors, and saves the output to a file.
- [ ] Explain what `2>/dev/null` does and when you would use it.
- [ ] Complete the Module 3 lab.
- [ ] Complete the Module 3 quiz.

---

## 9. Supplemental Resources

**1. [The Linux Documentation Project — Filesystem Hierarchy Standard](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/)**
A thorough walkthrough of every directory in the Linux filesystem hierarchy with explanations of what belongs in each. Directly reinforces the FHS section of this module and is frequently referenced for Linux+ exam questions about file placement.

**2. [man7.org — find(1) Manual Page](https://man7.org/linux/man-pages/man1/find.1.html)**
The complete `find` manual from the Linux man-pages project. Covers every predicate (`-mtime`, `-size`, `-perm`, `-exec`, `-print0`) with precise definitions. Invaluable for understanding the `+N`, `-N`, and `N` semantics of numeric predicates.

**3. [GNU Coreutils — Redirections and Pipes (Bash Manual)](https://www.gnu.org/software/bash/manual/bash.html#Redirections)**
The official GNU Bash manual section on I/O redirection. Covers all redirect operators (`>`, `>>`, `2>`, `&>`, `<<<`, process substitution) with formal definitions. Essential reference for understanding how file descriptors 0, 1, and 2 are manipulated.
