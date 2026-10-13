# Video Script: Module 06 - Process Management (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 06. Every running program on a Linux system is a process. Understanding
processes - how they are created, how they are identified, what they are doing, and how to
control them - is one of the most practical skills in Linux administration. When a server is
slow, a process is probably the reason. When a service fails to start, understanding processes
helps you diagnose why.

By the end of both parts you will be able to inspect all running processes, interpret ps and
top output, send signals to processes, and manage services through systemctl.

---

### Section 1: What Is a Process?

When you run a command like ls or a daemon like sshd, the kernel creates a process: a running
instance of a program with its own memory space, file descriptors, and execution state.

Every process has:

A PID (Process ID): a unique integer assigned by the kernel. PIDs are assigned sequentially.

A PPID (Parent Process ID): the PID of the process that created this one. When you run ls
from your bash shell, ls is a child process of bash.

An owner: the user account the process runs as. This determines what files and resources the
process can access.

A nice value: a scheduling priority number from -20 (highest priority) to +19 (lowest).

[SHOW TERMINAL]

```bash
echo $$
```

$$ is a special shell variable that contains the PID of the current shell. This shows you
your current shell's PID.

```bash
ps
```

Shows processes in the current terminal session. Minimal output - just your shell and ps itself.

```bash
ps aux
```

a = all users, u = user-format, x = include processes not attached to a terminal.
This shows every process running on the system.

---

### Section 2: Reading ps aux Output

[SHOW TERMINAL]

```bash
ps aux | head -15
```

Let us decode the column headers:

USER: the account running the process

PID: process ID

%CPU: percentage of CPU time used in recent period

%MEM: percentage of physical RAM used

VSZ: virtual memory size in kilobytes

RSS: resident set size - actual physical RAM pages currently in use (kilobytes)

TTY: the terminal attached. ? means no terminal (background daemon).

STAT: process state

COMMAND: the command and its arguments

The STAT column codes are critical exam material:

- R: Running or runnable
- S: Sleeping (interruptible) - waiting for input
- D: Uninterruptible sleep - waiting for I/O (disk, network)
- Z: Zombie - process finished but parent has not collected exit status
- T: Stopped by signal
- I: Idle kernel thread

---

### Section 3: The top Command

[SHOW TERMINAL]

```bash
top
```

top provides a real-time, updating view of system processes. Let us navigate it.

The header section shows:
- Uptime and load averages (1, 5, 15 minute averages)
- Task counts (total, running, sleeping, stopped, zombie)
- CPU breakdown (us=user, sy=system, id=idle, wa=I/O wait)
- Memory usage

Load average interpretation: on a single-CPU system, a load of 1.0 means 100% CPU utilization.
On a 4-CPU system, a load of 4.0 means 100% utilization. Load above 1.0 per CPU means processes
are queued waiting for CPU time.

Key top interactions:
- q: quit
- k: kill a process (prompts for PID then signal)
- r: renice (change priority)
- M: sort by memory usage
- P: sort by CPU usage (default)
- 1: toggle showing individual CPU cores

```bash
top -b -n 1
```

Batch mode (-b) with one iteration (-n 1) outputs the current process list to stdout. Useful
in scripts for capturing a snapshot.

---

### Section 4: htop

[SHOW TERMINAL]

```bash
sudo apt install htop -y
htop
```

htop is an enhanced interactive process viewer. It adds color coding, horizontal scrolling,
and function key shortcuts. F9 sends a signal to the selected process. F6 sorts by column.
F5 shows the process tree.

htop is not available by default on all systems and the exam tests top knowledge more often.
But in practice, htop is far more pleasant to use.

---

### Section 5: Finding Specific Processes

[SHOW TERMINAL]

```bash
ps aux | grep sshd
```

Filter the process list for sshd.

```bash
pgrep sshd
```

pgrep returns just the PID of matching processes. Cleaner than ps | grep.

```bash
pgrep -l sshd
```

-l adds the process name to the output.

```bash
pgrep -u labadmin
```

All PIDs belonging to labadmin.

```bash
pidof sshd
```

Similar to pgrep, returns the PID of a running program by name.

---

### Section 6: Process Priority with nice and renice

[SHOW TERMINAL]

Every process has a nice value from -20 (highest scheduling priority) to +19 (lowest).
The default nice value is 0.

Why does this matter? On a busy server, you might want a backup job to run at low priority
so it does not compete with production application processes for CPU time.

```bash
nice -n 15 gzip bigfile.tar
```

Start the gzip compression job with low priority (15).

```bash
ps aux | grep gzip
```

Note the NI column showing the nice value.

```bash
renice -n 5 -p 12345
```

Change the priority of running process 12345 to nice value 5.

```bash
sudo renice -n -5 -p 12345
```

Only root can set negative nice values (higher priority). Regular users can only lower their
processes' priority, not raise it above 0.

---

### Section 7: Background and Foreground Jobs

[SHOW TERMINAL]

```bash
sleep 60 &
```

The & at the end runs the command in the background. Your shell prompt returns immediately.
The kernel prints [1] followed by the PID.

```bash
jobs
```

Lists all background jobs in the current shell session.

```bash
fg 1
```

Bring job number 1 back to the foreground.

```bash
Ctrl+Z
```

Suspend the foreground job (sends SIGSTOP). The shell prompt returns.

```bash
bg 1
```

Resume job 1 in the background.

This job control mechanism is important for long-running tasks in a terminal session. However,
for anything that needs to survive terminal closure, use systemd or nohup.

```bash
nohup long_running_script.sh &
```

nohup (no hangup) prevents the process from being killed when you close the terminal.
Output goes to nohup.out unless redirected.

---

### Certification Connection

Process management maps to Linux+ Domain 1.0 (System Management). Key exam objectives:

Interpret ps aux STAT column codes (R, S, D, Z, T).

Know the difference between pgrep, pidof, and ps | grep.

Know load average interpretation and the CPU column in top.

Know nice value ranges and who can set negative values.

Know job control commands: &, jobs, fg, bg, Ctrl+Z.

---

### Transition to Part 2

In Part 2 we cover signals, kill commands, systemctl service management, and zombie processes.
Take a break and continue.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
