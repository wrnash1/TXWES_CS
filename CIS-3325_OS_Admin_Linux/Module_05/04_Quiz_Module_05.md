# Quiz: Module 05 — Process Management and System Monitoring

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

An administrator runs `ps aux` and notices a process with a STAT value of `D`. What does this state indicate?

A. The process has exited but its parent has not collected its exit status

B. The process is actively executing on a CPU core

C. The process is waiting for I/O and cannot be interrupted by a signal

D. The process has been deliberately paused by the administrator

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. That describes a zombie process, which has STAT code `Z`. A zombie has completed execution but its parent has not called `wait()`.
- **B** is incorrect. That describes the `R` (Running) state — the process is on the CPU or ready to run in the scheduler queue.
- **C** is correct. `D` state — Uninterruptible Sleep — means the process is blocked waiting for a hardware event, typically disk I/O. It cannot be killed by SIGTERM or SIGKILL until the I/O completes. Seeing many `D` processes indicates an I/O bottleneck or storage problem.
- **D** is incorrect. A deliberately paused/suspended process has STAT code `T` — Stopped. This is typically caused by Control+Z or SIGSTOP.

---

### Question 2

A sysadmin needs to terminate a frozen application that is not responding to `kill PID`. Which command forces termination regardless of the process's state?

A. `kill -1 PID`

B. `kill -15 PID`

C. `kill -9 PID`

D. `kill -18 PID`

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Signal 1 is SIGHUP. While it terminates some processes, it is conventionally used to trigger a configuration reload in daemon processes and can be caught/ignored by the application.
- **B** is incorrect. Signal 15 is SIGTERM — the default graceful termination signal. If the process is not responding to normal kill attempts, SIGTERM (which is also catchable and ignorable) will also have no effect.
- **C** is correct. Signal 9 is SIGKILL. It is implemented by the kernel directly and cannot be caught, blocked, or ignored by any process regardless of its state. The kernel enforces termination immediately.
- **D** is incorrect. Signal 18 is SIGCONT — it resumes a stopped/paused process rather than terminating it.

---

### Question 3

An administrator starts a data migration script and wants it to continue running even if they log out of the SSH session. Which command achieves this?

A. `nice ./migrate.sh &`

B. `nohup ./migrate.sh &`

C. `bg ./migrate.sh &`

D. `disown ./migrate.sh`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `nice` adjusts the scheduling priority of a process but does not affect whether the process survives a logout. When the SSH session ends, SIGHUP is sent to the process group, which would still terminate it.
- **B** is correct. `nohup` (no hang up) makes the process immune to SIGHUP. When the terminal session closes and SIGHUP is delivered to the process group, the nohup-wrapped process ignores it and continues running. The `&` sends it to the background immediately.
- **C** is incorrect. `bg` resumes a stopped job in the background but does not protect it from SIGHUP on logout. The process would still terminate when the session ends.
- **D** is incorrect while close. `disown` removes the job from the shell's job table, which prevents the shell from sending SIGHUP to it, but it must be used AFTER the process is already running, not as a launch command. The syntax shown (with the command as argument) is also incorrect — `disown` takes a job specification like `%1`.

---

### Question 4

What is the valid range of nice values that a regular (non-root) user can set for their own processes?

A. -20 to 0

B. 0 to 19

C. -19 to 19

D. 1 to 20

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. A regular user cannot set negative nice values (which would increase priority). Values from -20 to -1 require root/sudo. Setting a process to 0 does not require privileges.
- **B** is correct. Regular users can only lower their process priority (increase the nice value) from the default of 0 up to a maximum of +19. This design prevents users from monopolizing CPU resources.
- **C** is incorrect. The range -19 to 19 excludes -20 but still allows negative values, which require elevated privileges. Regular users are restricted to 0 and above.
- **D** is incorrect. The valid range does not use 1–20. The range is -20 to +19, and +20 is not a valid nice value. Also, 1 would mean users cannot start at the default (0).

---

### Question 5

A system shows a load average of 6.5 over the last 15 minutes. The server has 4 CPU cores. How should the administrator interpret this?

A. The system is healthy because the load average is less than 10

B. The system is operating at 65% CPU capacity, which is acceptable

C. The load average exceeds the number of CPU cores, indicating CPU saturation

D. Load average does not relate to CPU cores and cannot be interpreted this way

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. There is no universal threshold of "less than 10." Load average must be evaluated relative to the number of CPU cores. A load of 6.5 on a 4-core system is significantly over capacity.
- **B** is incorrect. Load average does not directly translate to a percentage of CPU capacity. A load average equal to the core count means 100% utilization, not load/10.
- **C** is correct. On a 4-core system, a load average of 4.0 represents 100% utilization. A 15-minute load average of 6.5 means 1.625× CPU saturation — 2–3 processes are on average waiting for CPU time at any given moment. This warrants investigation.
- **D** is incorrect. Load average is explicitly interpreted in relation to CPU core count. This is the foundational rule for load average analysis.

---

### Question 6

An administrator wants to schedule a script to run every weekday at 7:30 AM. Which crontab entry is correct?

A. `30 7 * * 1-5 /usr/local/bin/morning_report.sh`

B. `7 30 * * 1-5 /usr/local/bin/morning_report.sh`

C. `30 7 1-5 * * /usr/local/bin/morning_report.sh`

D. `* * * * 1-5 /usr/local/bin/morning_report.sh`

**Correct Answer: A**

**Distractor Analysis:**

- **A** is correct. Crontab field order is: minute, hour, day-of-month, month, day-of-week. `30 7` means 7:30 AM. `* *` means every day of any month. `1-5` means Monday through Friday (1=Monday, 5=Friday). This is the correct combination.
- **B** is incorrect. The minute and hour fields are swapped. `7 30` would mean minute 7 of hour 30, which is invalid (hours only go 0–23).
- **C** is incorrect. `1-5` is in the day-of-month field, not day-of-week. This would run on the 1st through 5th of every month, not on weekdays.
- **D** is incorrect. `* * * * 1-5` would run every minute of every hour on weekdays, not just at 7:30 AM.

---

### Question 7

An administrator runs `free -h` and sees that "available" memory is only 200MB while "buff/cache" shows 3.5GB. What is the correct interpretation?

A. The system is critically low on memory and applications may crash

B. Most memory is being used as file cache, which is normal; applications can reclaim it

C. 3.5GB of memory is permanently allocated to kernel buffers

D. The system should immediately have swap space added

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. The "available" field in modern `free` output already accounts for reclaimable cache. Low "free" is normal and expected — Linux intentionally uses free RAM as file cache to accelerate I/O.
- **B** is correct. Linux's memory management philosophy uses idle RAM as disk cache (page cache + buffers). When an application requests memory, the kernel evicts cached pages to make room. This is normal, healthy behavior. The "available" column shows how much could be given to an application including reclaimable cache — 200MB here is the concern, not 3.5GB of cache.
- **C** is incorrect. Buffer/cache is not permanently allocated — it is reclaimed on demand. Only a small portion of kernel memory (kernel code, data structures) is truly permanent.
- **D** is incorrect while swap may eventually be warranted. The observation described does not indicate immediate swap pressure. Swap is used when available memory approaches zero and pages must be moved to disk, which is not the stated situation.

---

### Question 8

Which file in the /proc filesystem contains the system load averages?

A. `/proc/cpuinfo`

B. `/proc/meminfo`

C. `/proc/loadavg`

D. `/proc/uptime`

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. `/proc/cpuinfo` contains processor model information, core count, clock speed, and CPU flags. It does not contain load averages.
- **B** is incorrect. `/proc/meminfo` contains detailed memory statistics — total, free, available, cached, buffers, and swap information. Load averages are not there.
- **C** is correct. `/proc/loadavg` contains the same load average values reported by `uptime`, along with the current running/total process count and the most recently created PID.
- **D** is incorrect. `/proc/uptime` contains two values: system uptime in seconds and idle time in seconds. Load averages are not included — those are in `/proc/loadavg`.

---

### Question 9

A sysadmin discovers a process running with a nice value of -10 that is monopolizing CPU time. The process is owned by a service account. What privilege level is required to have started this process at that priority?

A. The service account user only

B. A user in the `sudo` group

C. Root or a process with CAP_SYS_NICE capability

D. Any user, because nice values have no security restriction

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Regular users — including service accounts — cannot set negative nice values. Negative nice = increased priority = more CPU than default. This is a privilege-controlled operation.
- **B** is incorrect while close. Being in the sudo group grants the ability to run commands as root, but the nice value restriction is specifically about the CAP_SYS_NICE capability. A sudo user who ran `sudo nice -n -10` would have root context, which qualifies — but the answer incorrectly frames it as the sudo group membership itself being sufficient.
- **C** is correct. Setting a negative nice value requires root privileges or the CAP_SYS_NICE capability (Linux capability model). The process was either started by root directly, via sudo, or through a system mechanism that granted the capability.
- **D** is incorrect. The nice value system explicitly restricts regular users to values 0–19. This is a security control to prevent any user from degrading system responsiveness for other users.

---

### Question 10

An administrator wants to view all processes that have open connections or sockets on port 443. Which command is correct?

A. `ps aux | grep 443`

B. `lsof -i :443`

C. `netstat -p 443`

D. `df -h | grep 443`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `ps aux | grep 443` would search the COMMAND column of the process list for the string "443." This would match processes whose command name or argument happens to contain "443" but would not find processes listening on a port unless "443" appeared in their command string.
- **B** is correct. `lsof -i :443` lists all open files where the file is an internet socket on port 443. It shows the process name, PID, user, and connection state.
- **C** is incorrect. `netstat -p` shows the PID associated with each connection, but `-p 443` is not valid netstat syntax. `netstat -tlnp` would show listening ports with PIDs, and you would then grep for 443. But as written, the command is invalid.
- **D** is incorrect. `df -h` shows disk filesystem usage. It has nothing to do with network ports and would never show port 443.

---

## Answer Key

| Question | Answer |
|---|---|
| 1 | C |
| 2 | C |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | A |
| 7 | B |
| 8 | C |
| 9 | C |
| 10 | B |

---

*End of Module 05 Quiz*
