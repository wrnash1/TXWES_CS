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

### Question 11 (5 points)

An administrator wants to run a command and give it a lower scheduling priority than any normal user process. Which command starts `/usr/local/bin/report.sh` with the lowest possible nice value?

A. `nice -n 0 /usr/local/bin/report.sh`
B. `nice -n 19 /usr/local/bin/report.sh`
C. `nice -n -20 /usr/local/bin/report.sh`
D. `renice 19 /usr/local/bin/report.sh`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Nice value 0 is the default priority — no change from a normal process. This does not give the command lower priority.
- **B** is correct. Nice value +19 is the lowest possible priority (highest nice number = least CPU time). This tells the scheduler to preempt this process in favor of almost everything else.
- **C** is incorrect. Nice value -20 is the highest possible priority (most CPU time), which is the opposite of what was requested and also requires root privileges.
- **D** is incorrect. `renice` is used to change the priority of an already-running process identified by PID — it cannot be used to launch a new command. The syntax shown is also wrong for `renice`.

---

### Question 12 (5 points)

Which of the following correctly describes a zombie process?

A. A process that is consuming 100% CPU and cannot be stopped.
B. A process that is blocked waiting for disk I/O to complete.
C. A process that has exited but whose parent has not yet called wait() to collect its exit status.
D. A process that was started by a user who has since logged out.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. A process consuming 100% CPU is in the Running (`R`) or Uninterruptible Sleep (`D`) state, not a zombie. Zombies consume almost no resources — they are just a kernel table entry.
- **B** is incorrect. That describes the `D` (Uninterruptible Sleep) state — waiting for I/O. Zombies have already finished executing.
- **C** is correct. A zombie (`Z` state) has called `exit()` and is done, but its entry remains in the process table because the parent process has not called `wait()` to read the exit status. Zombies cannot be killed because they are already dead — you must fix or kill the parent.
- **D** is incorrect. A process whose parent session has ended may become an orphan (re-parented to PID 1/systemd), not a zombie. Orphans continue running normally.

---

### Question 13 (5 points)

An administrator wants to monitor system performance for 10 seconds, sampling every 2 seconds, to check if there is I/O wait occurring. Which command is most appropriate?

A. `free -h`
B. `df -h`
C. `ps aux --sort=-%cpu`
D. `vmstat 2 5`

**Correct Answer: D**

**Distractor Analysis:**

- **A** is incorrect. `free -h` shows memory and swap usage at a single point in time. It does not show I/O wait or provide interval sampling.
- **B** is incorrect. `df -h` shows filesystem disk space usage. It does not measure I/O performance or wait time.
- **C** is incorrect. `ps aux --sort=-%cpu` shows a snapshot of CPU usage per process. It does not measure I/O wait over time.
- **D** is correct. `vmstat 2 5` reports virtual memory statistics with 5 samples at 2-second intervals. The `wa` column shows the percentage of CPU time spent waiting for I/O, making it the correct tool for this task.

---

### Question 14 (5 points)

A sysadmin types `Control+Z` while a long-running command is running in the foreground. What is the result?

A. The process is permanently terminated.
B. The process is sent to the background and continues running.
C. The process is suspended (stopped) and placed in the job list.
D. The process is paused for 5 seconds and then resumes automatically.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. `Control+Z` sends SIGSTOP (or more precisely SIGTSTP) which suspends the process. `Control+C` sends SIGINT which typically terminates the process.
- **B** is incorrect. `Control+Z` suspends the process — it does not continue running in the background. To resume in the background, the administrator would then need to run `bg`.
- **C** is correct. `Control+Z` sends the terminal stop signal, suspending the process and putting it into the `T` (Stopped) state. It appears in the `jobs` list as "Stopped" and can be resumed with `fg` or `bg`.
- **D** is incorrect. There is no automatic timer-based resume behavior in Linux job control. A stopped process remains stopped until explicitly resumed.

---

### Question 15 (5 points)

What is the correct crontab entry to run `/usr/local/bin/backup.sh` at 2:00 AM every Sunday?

A. `0 2 * * 0 /usr/local/bin/backup.sh`
B. `2 0 * * 0 /usr/local/bin/backup.sh`
C. `0 2 0 * * /usr/local/bin/backup.sh`
D. `* * * * 0 /usr/local/bin/backup.sh`

**Correct Answer: A**

**Distractor Analysis:**

- **A** is correct. Crontab field order: minute hour day-of-month month day-of-week. `0 2` = at minute 0 of hour 2 = 2:00 AM. `* *` = every day of any month. `0` in day-of-week = Sunday. This is correct.
- **B** is incorrect. The minute and hour values are swapped. `2 0` means minute 2 of hour 0 = 12:02 AM, not 2:00 AM.
- **C** is incorrect. The third field is day-of-month, not day-of-week. `0` in day-of-month is invalid (days start at 1). The day-of-week field (fifth) should contain `0` for Sunday.
- **D** is incorrect. `* * * * 0` would run every minute of every hour on Sundays — 1,440 executions per Sunday — not once at 2:00 AM.

---

### Question 16 (5 points)

An administrator runs `pgrep httpd` and gets the output `1423`. What does this confirm?

A. There is a process named `httpd` running with PID 1423.
B. `httpd` has made 1,423 system calls since it started.
C. The Apache web server has served 1,423 requests.
D. Port 1423 is open and listening for HTTP connections.

**Correct Answer: A**

**Distractor Analysis:**

- **A** is correct. `pgrep` searches the process list for processes whose name matches the pattern and returns their PIDs. A single output of `1423` means one process named `httpd` is running with that PID.
- **B** is incorrect. `pgrep` only returns PIDs — it has no ability to report system call counts. `strace` or `/proc/PID/status` would be used for process activity information.
- **C** is incorrect. Request counts are tracked by the application's own logging (e.g., Apache access log) or metrics systems. `pgrep` only deals with process IDs.
- **D** is incorrect. Port information is obtained with `lsof -i :1423` or `ss -tlnp`. `pgrep` output is a PID, not a port number.

---

### Question 17 (5 points)

Which `/proc` path would you read to find the full command line that was used to start a process with PID 8372?

A. `/proc/8372/status`
B. `/proc/8372/cmdline`
C. `/proc/8372/maps`
D. `/proc/8372/fd/`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `/proc/PID/status` contains the human-readable process status including name, state, UID, GID, and memory usage — but not the original command line arguments.
- **B** is correct. `/proc/PID/cmdline` contains the full command line used to launch the process, with arguments separated by null bytes. `cat /proc/8372/cmdline` (followed by echo) shows the command.
- **C** is incorrect. `/proc/PID/maps` shows the memory map of the process — what shared libraries and memory regions are mapped, at what addresses. Not command-line information.
- **D** is incorrect. `/proc/PID/fd/` is a directory containing symbolic links to all open file descriptors of the process. It shows what files and sockets the process has open, not its command line.

---

### Question 18 (5 points)

An administrator issues `kill -HUP 2891` to the nginx web server process. What is the expected behavior?

A. The nginx process is immediately and forcefully terminated.
B. nginx gracefully shuts down, waiting for active connections to close.
C. nginx reloads its configuration file without dropping active connections.
D. nginx is suspended and will not accept new connections until resumed.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Forceful termination requires SIGKILL (signal 9). SIGHUP (signal 1) is not handled that way by nginx.
- **B** is incorrect. Graceful shutdown of nginx typically uses SIGQUIT (signal 3), which allows workers to finish current requests before exiting.
- **C** is correct. By convention, well-behaved daemons including nginx handle SIGHUP as a signal to reload their configuration file. This allows configuration changes to take effect without interrupting active connections — a critical capability for zero-downtime deployments.
- **D** is incorrect. Suspending a process requires SIGSTOP (signal 19). SIGHUP is the hangup signal with daemon-specific reload behavior.

---

### Question 19 (5 points)

An administrator looks at `vmstat 1 3` output and sees the `si` and `so` columns consistently showing values greater than 0. What does this indicate?

A. The system is performing more sequential reads than writes.
B. The system is actively swapping pages between RAM and disk.
C. The system input/output interfaces are saturated.
D. Socket connections are being created and closed frequently.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Sequential vs. random I/O patterns are measured by `iostat`. The `si`/`so` columns have no relationship to read/write patterns on block devices.
- **B** is correct. In `vmstat` output, `si` (swap in) and `so` (swap out) measure pages being moved between swap space and RAM. Consistent non-zero values mean the system is under memory pressure and actively using swap — a warning sign that usually means more RAM is needed.
- **C** is incorrect. Network or block device I/O saturation is shown in the `bi`/`bo` columns (blocks in/out from block devices) and `io` column. `si`/`so` are specifically swap-related.
- **D** is incorrect. Socket connection rates are a network metric unrelated to `vmstat` columns. Socket activity would appear in tools like `ss`, `netstat`, or `sar`.

---

### Question 20 (5 points)

A sysadmin needs to schedule a one-time command to run at 11:30 PM tonight. Which command syntax is correct?

A. `crontab -e "command" 23:30`
B. `echo "command" | at 23:30`
C. `at -once 23:30 command`
D. `schedule 23:30 command`

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. `crontab -e` opens an editor for recurring scheduled jobs. It does not accept a command and time as arguments on the command line. Cron is for repeating tasks, not one-time tasks.
- **B** is correct. `at` is the tool for one-time scheduled tasks. Piping the command via `echo ... |` (or entering it interactively after running `at 23:30`) is the standard non-interactive usage.
- **C** is incorrect. `at` has no `-once` flag. The syntax for `at` is simply `at TIME`, where time can be `23:30`, `now + 2 hours`, `midnight`, `tomorrow`, etc.
- **D** is incorrect. `schedule` is not a standard Linux command. This is a distractor.

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
| 11 | B |
| 12 | C |
| 13 | D |
| 14 | C |
| 15 | A |
| 16 | A |
| 17 | B |
| 18 | C |
| 19 | B |
| 20 | B |

---

*End of Module 05 Quiz*
