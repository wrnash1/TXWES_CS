# Reading Guide: Module 06 - Process Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 06 – Process Management**! This week covers how Linux creates, monitors, and terminates processes, and how `systemd` manages services as the system init process. Process and service management is tested across all domains of the CompTIA Linux+ XK0-005 exam — you will see it in troubleshooting scenarios, security hardening questions, and system optimization contexts.

As you work through this material you will learn the difference between a process and a service, how to use `ps`, `top`, `htop`, and `kill` to monitor and control processes, and how `systemctl` manages the lifecycle of systemd services.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Process vs. Service**: A process is any running instance of a program, identified by a unique PID (Process ID). A service (daemon) is a long-running background process managed by the init system (systemd). Every process has a parent (PPID); PID 1 is the init process (`systemd` on modern Linux).
*   **`ps aux`**: Displays a snapshot of all current processes. `a` = all users, `u` = user-oriented format (shows %CPU, %MEM, command), `x` = include processes not attached to a terminal. Key columns: PID, USER, %CPU, %MEM, VSZ, RSS, STAT (R=running, S=sleeping, Z=zombie, D=uninterruptible sleep), COMMAND.
*   **`top` and `htop`**: Interactive real-time process monitors. `top` is available on all Linux systems. `htop` is an enhanced version with color, mouse support, and easier kill/renice operations. Both display load average (1, 5, 15 minute averages), CPU usage breakdown, and memory utilization in their header.
*   **`kill` and signal numbers**: `kill PID` sends SIGTERM (15) by default, requesting graceful shutdown. `kill -9 PID` sends SIGKILL, which cannot be caught or ignored and forces immediate termination. `kill -1 PID` sends SIGHUP, traditionally used to reload a process's configuration. Use `kill -l` to list all signal names and numbers.
*   **`systemctl`**: The command-line interface to systemd for managing services and the system state. Key subcommands: `start`, `stop`, `restart`, `reload`, `status`, `enable` (start at boot), `disable` (remove from boot), `is-active`, `is-enabled`. The `daemon-reload` subcommand must be run after editing a unit file to reload systemd's in-memory configuration.
*   **`nice` and `renice`**: Control process scheduling priority. Nice values range from -20 (highest priority) to +19 (lowest). `nice -n 10 command` launches a command with a niceness of 10. `renice -n 5 -p PID` changes the niceness of an already-running process. Only root can set negative (higher-priority) nice values.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Process management maps to Linux+ Domain 1.0 (System Management). Expect 4–6 questions involving `ps`, `kill`, `systemctl`, and service troubleshooting.
*   **Signal numbers to memorize:** SIGTERM=15 (graceful stop), SIGKILL=9 (force kill), SIGHUP=1 (reload config), SIGSTOP=19 (pause), SIGCONT=18 (resume). The exam presents scenarios and asks which signal is appropriate — SIGKILL is never the first choice for a well-behaved service.
*   **`systemctl enable` vs `systemctl start`:** A very common exam scenario: "the service runs now but stops after reboot." Answer: `systemctl enable`. "The service is set to auto-start but is not running now." Answer: `systemctl start`. Know that `systemctl enable --now` does both in one command.
*   **Zombie processes:** A zombie (Z in STAT column) is a process that has finished but whose parent has not yet read its exit status. Zombies cannot be killed with SIGKILL because they are already dead — the fix is to terminate or fix the parent process.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers process management in chapters 10–11. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of `ps`, `top`, `kill`, and `systemctl` in realistic server administration scenarios.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 10–11 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering processes, signals, and how to monitor and control running programs.
*   **Required Video:** Watch the process and service management videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist with live terminal demonstrations of process monitoring and systemd service control.

---

### Lab & Command Integration
In this week's hands-on lab you will use `ps aux` and `top` to identify resource-hungry processes, send signals with `kill` and `killall`, start and stop services with `systemctl`, enable a service to start at boot, and inspect the systemd journal with `journalctl -u servicename`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 10–11 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the process management videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
