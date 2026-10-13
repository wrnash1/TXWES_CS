# Video Script: Module 05 — Process Management and System Monitoring (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Production Notes

- **Screen recording**: Terminal emulator (dark theme, 18pt font)
- **Demonstrations**: Show live ps output and top interactively; use a background sleep process as a controllable target
- **Slide overlays**: Process state table shown as a callout during state discussion
- **Pacing**: Allow top/htop to run for several seconds before narrating interactive commands

---

## SEGMENT 1 — Opening and Context (0:00–1:30)

### Narration

Welcome to Module 05, Part 1: Process Management. I'm Professor Nash, and we're continuing our progression through OS administration fundamentals.

In Module 04 we worked with files and text. Now we turn to what is running on the system — the processes that consume CPU, memory, and I/O. A sysadmin who cannot read process state, identify resource hogs, and safely terminate misbehaving processes cannot maintain system health under pressure.

This module maps directly to CompTIA Linux+ objective 2.6 — given a scenario, manage processes and services. We will cover: what a process is, how to inspect processes with ps and top, and how to send signals to control process behavior. Part 2 continues with priority, background jobs, resource monitoring, and scheduling.

---

## SEGMENT 2 — What is a Process? (1:30–3:30)

### Narration

A process is a running instance of a program. When you type `ls` at a shell prompt, the kernel creates a process for ls, runs it, and destroys it when it exits. When Apache is serving web pages, that is a long-running process (or group of processes) that persists until stopped.

Every process has a Process ID — a PID — which is a unique integer assigned by the kernel at creation time. PID 1 is special: it is the init process, which on modern Linux systems is systemd. Every other process on the system is a descendant of PID 1.

Every process also has a Parent Process ID — a PPID — which identifies which process created it. When you run a command from bash, the shell forks a child process. The child's PPID is the shell's PID.

Processes exist in several states. Let me put the key ones on screen.

### Slide Overlay: Process States

| Code | State | Meaning |
|---|---|---|
| R | Running | Actively executing on CPU or ready to run |
| S | Sleeping | Waiting for an event (interruptible) |
| D | Uninterruptible Sleep | Waiting for I/O — cannot be killed with SIGTERM |
| Z | Zombie | Process has exited but parent has not read its exit status |
| T | Stopped | Process execution suspended by a signal |

### Narration

The states you will encounter most are R and S. D state is important because a process in D state cannot be killed by normal signals — it is waiting on hardware, typically disk I/O. If you see many processes in D state, investigate disk health or storage performance. A zombie process (Z) is not consuming resources but indicates a programming error in the parent process. Stopped processes (T) have been paused, usually intentionally.

---

## SEGMENT 3 — ps: Snapshot of Processes (3:30–7:00)

### Narration

ps — process status — takes a snapshot of currently running processes. It has two syntax styles: the BSD style without dashes, and the POSIX/SysV style with dashes. Most Linux documentation uses BSD style, but both work on Linux.

The most common invocation is `ps aux`:

### On-Screen Demo

```bash
ps aux
```

### Narration

The output columns: USER is the owner. PID is the process ID. %CPU and %MEM are resource usage percentages. VSZ is virtual memory size. RSS is resident set size — actual physical memory in use. STAT is the process state. START is when the process started. TIME is cumulative CPU time consumed. COMMAND is the executable and its arguments.

Let me pause on STAT for a moment. You will see codes like `Ss`, `Ssl`, or `Rn`. The first letter is the primary state we discussed. Additional letters are flags:

- `s` — session leader
- `l` — multi-threaded
- `+` — in the foreground process group
- `N` — low-priority (nice)

### On-Screen Demo

```bash
ps aux | grep sshd
```

### Narration

This narrows the output to just the SSH daemon. Notice grep itself also appears in the output — a normal artifact.

The `-ef` flags use SysV syntax and give similar output with different column layout. `-e` means every process, `-f` means full format:

### On-Screen Demo

```bash
ps -ef | head -20
```

### Narration

The `--forest` option is particularly useful for visualizing process hierarchy:

### On-Screen Demo

```bash
ps --forest -eo pid,ppid,cmd | head -30
```

### Narration

You can see the parent-child relationships as an indented tree. This helps you trace which service spawned a suspicious process.

For sorting by resource usage, use `--sort`:

### On-Screen Demo

```bash
# Top 10 processes by CPU usage
ps aux --sort=-%cpu | head -10

# Top 10 by memory
ps aux --sort=-%mem | head -10
```

---

## SEGMENT 4 — top and htop: Real-Time Monitoring (7:00–10:30)

### Narration

ps gives you a snapshot. For real-time monitoring, use top — it refreshes every few seconds and shows a live view of system state.

### On-Screen Demo

```bash
top
```

### Narration

The top section of top's display shows system-level information. Let me walk through it.

The first line: uptime and load averages for 1, 5, and 15 minutes. We will discuss load averages more in Part 2.

The second line: task counts by state — running, sleeping, stopped, zombie.

Third line: CPU breakdown — `us` is user space, `sy` is kernel (system) space, `id` is idle. When `id` drops toward zero, the system is CPU-saturated.

Fourth and fifth lines: memory and swap usage.

The process table below sorts by CPU usage by default. Columns include PID, USER, PR (priority), NI (nice value), VIRT, RES, SHR (shared memory), S (state), %CPU, %MEM, TIME+, and COMMAND.

Now the interactive commands. While top is running:

- Press **k** to kill a process: top will prompt for the PID, then the signal
- Press **r** to renice a process (change its priority): top prompts for PID and new nice value
- Press **M** to sort by memory usage
- Press **P** to sort by CPU usage (the default)
- Press **1** to toggle per-CPU display showing each core separately
- Press **q** to quit

### On-Screen Demo

*Run top, press 1 to show per-core display, press M to sort by memory, press q to exit*

### Narration

htop is an enhanced, more visual version of top. It may not be installed by default but is available in every distribution's package repository.

### On-Screen Demo

```bash
# Install if needed
sudo apt install htop   # Debian/Ubuntu
# or
sudo yum install htop   # RHEL/CentOS

htop
```

### Narration

htop adds colored bar charts for CPU and memory, mouse support for clicking processes, and F-key shortcuts at the bottom. For the Linux+ exam, know top — htop is a bonus tool.

---

## SEGMENT 5 — Signals and kill (10:30–15:00)

### Narration

To control processes, Linux uses signals — integer values sent to a process that trigger a specific response. You send signals with the `kill` command. Despite its name, kill sends any signal, not just termination signals.

The syntax is:

```
kill [-signal] PID
```

The signals you must know:

### Slide Overlay: Key Signals

| Signal | Number | Meaning |
|---|---|---|
| SIGHUP | 1 | Hang up — many daemons reload config on SIGHUP |
| SIGTERM | 15 | Terminate gracefully (default if no signal specified) |
| SIGKILL | 9 | Kill immediately — cannot be caught or ignored |
| SIGSTOP | 19 | Pause/suspend execution |
| SIGCONT | 18 | Resume a stopped process |

### Narration

Let's demonstrate. First, start a long-running process:

### On-Screen Demo

```bash
sleep 300 &
```

### Narration

The ampersand sends it to the background. The shell prints the job number in brackets and the PID. Let's find that PID:

### On-Screen Demo

```bash
ps aux | grep "sleep 300"
```

### Narration

Now send SIGTERM — a polite termination request. Well-behaved programs catch SIGTERM and clean up before exiting:

### On-Screen Demo

```bash
kill PID_HERE
# Verify it's gone:
ps aux | grep "sleep 300"
```

### Narration

Start another sleep process and this time use SIGKILL — the forceful option that the kernel enforces directly without giving the process any chance to respond:

### On-Screen Demo

```bash
sleep 300 &
kill -9 PID_HERE
# or equivalently:
kill -SIGKILL PID_HERE
```

### Narration

SIGKILL cannot be caught, blocked, or ignored by the process. It is the last resort when a process is frozen or refusing to respond to SIGTERM. However, SIGKILL bypasses cleanup — open files may not be flushed, temp files may not be removed. Always try SIGTERM first, wait a few seconds, then escalate to SIGKILL if needed.

SIGHUP is important for system administration. Many daemons — sshd, nginx, rsyslog — are written to reload their configuration file when they receive SIGHUP, without restarting entirely:

### On-Screen Demo

```bash
# Tell nginx to reload its config (no downtime)
kill -HUP $(pgrep nginx)
```

### Narration

`pgrep` is a convenience that returns the PID of processes matching a name pattern — we can combine it with kill using command substitution.

For killing by name rather than PID, use `killall` or `pkill`:

### On-Screen Demo

```bash
# Kill all processes named "sleep"
killall sleep

# pkill matches by pattern
pkill -f "sleep 300"
```

### Narration

`pkill -f` matches the full command line, not just the process name. This is useful when multiple different programs are running but you need to kill only those matching a specific argument pattern.

Let me close with a safety note: on a production system, always confirm the PID before killing. A typo in a PID can terminate a critical service. The pattern `kill -0 PID` checks whether a process exists without sending an actual signal — use it to verify before acting.

That wraps Part 1. You can now observe, snapshot, and control processes. In Part 2 we add priority management, background jobs, resource monitoring tools, the /proc filesystem, and scheduled tasks with cron. See you there.

---

## Summary Slide

### Part 1 Key Concepts

- **Process**: running program instance; every process has PID and PPID
- **States**: R (running), S (sleeping), D (uninterruptible), Z (zombie), T (stopped)
- `ps aux` — snapshot; `ps -ef --forest` — tree view; `--sort=-%cpu` — by resource
- `top` — real-time; k=kill, r=renice, M=memory sort, P=CPU sort, q=quit
- `kill PID` — sends SIGTERM (15); `kill -9 PID` — SIGKILL (forced)
- `kill -HUP PID` — reload config (signal 1)
- `killall name` — kill by process name; `pkill -f pattern` — kill by command pattern

---

*End of Module 05 Part 1 Script*
