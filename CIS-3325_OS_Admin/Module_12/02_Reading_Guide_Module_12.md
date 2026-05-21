# Reading Guide: Module 12 - System Logging and Monitoring
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 12 – System Logging and Monitoring**! This week covers Linux log management — from the systemd journal (`journald`) and traditional syslog (`rsyslog`), through log file locations and rotation, to real-time system monitoring with `top`, `vmstat`, and `iostat`. Logging and monitoring map to CompTIA Linux+ XK0-005 Domain 1.0 (System Management) and Domain 3.0 (Troubleshooting).

As you work through this material you will learn how to query the systemd journal, configure log forwarding to rsyslog, interpret standard log files in `/var/log/`, set up log rotation with `logrotate`, and use monitoring tools to diagnose performance problems.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **`journald` and `journalctl`**: The systemd journal daemon collects and stores log data from the kernel, services, and applications in a binary indexed format under `/run/log/journal/` (volatile) or `/var/log/journal/` (persistent). Query logs with `journalctl`: `journalctl -u sshd` (logs for the sshd unit), `journalctl -b` (logs since last boot), `journalctl --since "1 hour ago"` (time-filtered), `journalctl -p err` (error priority and above), `journalctl -f` (follow, like `tail -f`). Journal persistence requires creating `/var/log/journal/` or setting `Storage=persistent` in `/etc/systemd/journald.conf`.
*   **`rsyslog`**: The traditional syslog daemon that writes log messages to text files in `/var/log/`. Configured via `/etc/rsyslog.conf` and `/etc/rsyslog.d/*.conf`. Rules use facility.severity format (e.g., `auth.info /var/log/auth.log`) to route messages. On systems using both `journald` and `rsyslog`, `journald` forwards messages to `rsyslog` via the `/run/systemd/journal/syslog` socket. `systemctl status rsyslog` confirms the service is running.
*   **Key log files in `/var/log/`**: `/var/log/syslog` or `/var/log/messages` — general system messages. `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL) — authentication events, sudo usage, SSH logins. `/var/log/kern.log` — kernel messages. `/var/log/dmesg` — hardware and boot-time kernel ring buffer messages (also viewable live with the `dmesg` command). `/var/log/boot.log` — service start/stop events at boot.
*   **`logrotate`**: A utility that automatically rotates, compresses, and deletes old log files based on rules in `/etc/logrotate.conf` and `/etc/logrotate.d/`. Key directives: `daily`/`weekly`/`monthly` (rotation frequency), `rotate 7` (keep 7 old files), `compress` (gzip old logs), `missingok` (no error if log is absent), `postrotate`/`endscript` (run a command after rotation, e.g., to send SIGHUP to rsyslog). Triggered daily by a cron job or systemd timer.
*   **`top` and `htop`**: Interactive process monitors. `top` displays CPU, memory, and per-process statistics updated in real time. Key `top` interactive commands: `k` (kill a process), `r` (renice), `1` (show per-CPU usage), `q` (quit). `htop` is a more user-friendly alternative with color coding and mouse support. Both show load average, which reflects the average number of runnable and waiting processes over 1, 5, and 15 minutes.
*   **`vmstat` and `iostat`**: System performance snapshot tools. `vmstat 1 5` prints CPU, memory, swap, and I/O statistics every 1 second for 5 iterations. Key columns: `r` (run queue length), `b` (blocked processes), `si`/`so` (swap-in/swap-out — non-zero indicates memory pressure), `wa` (CPU time waiting for I/O — high values indicate a disk bottleneck). `iostat -x 1` shows per-device disk utilization with `%util` indicating how saturated each device is.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Logging and monitoring map to Linux+ Domain 1.0 (System Management) and Domain 3.0 (Troubleshooting). Expect 5–7 questions on log file paths, `journalctl` flags, and performance metric interpretation.
*   **`journalctl` flag trap:** The exam frequently tests `-u` (unit), `-b` (boot), `-p` (priority), and `-f` (follow). Know that `-p err` shows messages at `err` priority AND above (crit, alert, emerg) — it does not filter to only `err` level messages.
*   **Log file path by distro:** `/var/log/auth.log` is Debian/Ubuntu; `/var/log/secure` is RHEL/CentOS. The exam may present a scenario on one distro and ask which file contains SSH authentication failures — match the distro to the correct path.
*   **Journal persistence:** By default on many systems, the journal is stored in volatile memory and lost at reboot. Creating the directory `/var/log/journal/` makes it persistent automatically (systemd checks for this directory). This is a common exam scenario: "logs are lost after reboot — how do you make them persistent?"
*   **Load average interpretation:** A load average equal to the number of CPU cores means the system is fully utilized. A load average consistently higher than the core count means processes are waiting for CPU — the system is overloaded. The exam may present a load average value and ask whether it indicates a problem given a specified CPU count.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers process monitoring and log inspection in chapters 10–11. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of `journalctl`, log file inspection, and system monitoring tools in a live environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 10–11 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering process monitoring, system information commands, and log inspection techniques on Linux.
*   **Required Video:** Watch the system logging and monitoring videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates `journalctl`, rsyslog configuration, and performance monitoring with live examples.

---

### Lab & Command Integration
In this week's hands-on lab you will query the journal with `journalctl -u sshd -b`, inspect `/var/log/auth.log` or `/var/log/secure` for failed login attempts, view kernel messages with `dmesg | tail`, monitor live CPU and memory usage with `top`, and interpret `vmstat 1 5` output to identify I/O wait.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 10–11 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the logging and monitoring videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
