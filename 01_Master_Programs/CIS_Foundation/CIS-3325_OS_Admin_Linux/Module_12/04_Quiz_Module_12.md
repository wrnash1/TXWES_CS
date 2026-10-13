# Quiz: Module 12 — System Services and Daemons

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Instructions

Select the best answer for each question. Each question is worth 10 points.

---

### Questions

**Question 1**

An administrator needs the `httpd` service to start automatically on the next reboot but does not want to start it right now. Which command is correct?

- A) `systemctl start httpd`
- B) `systemctl enable --now httpd`
- C) `systemctl enable httpd`
- D) `systemctl activate httpd`

**Correct Answer: C**

*Explanation: `systemctl enable` creates the necessary symlinks so the service starts at boot but does not start it immediately. `systemctl enable --now` would start it immediately as well. `systemctl start` starts it now but has no boot effect.*

---

**Question 2**

A junior administrator ran `systemctl stop httpd` to temporarily stop the web server. After the system reboots overnight, the web server does not come back up. What is the most likely explanation?

- A) The httpd binary was deleted
- B) The systemd unit file was corrupted during the stop operation
- C) `systemctl stop` also disabled the service
- D) The service was already disabled before the stop command was run

**Correct Answer: D**

*Explanation: `systemctl stop` only stops a running service; it has no effect on whether the service is enabled for boot. If the service did not start at boot, it was already disabled (or never enabled). The administrator should have checked `systemctl is-enabled httpd`.*

---

**Question 3**

In a systemd service unit file, which directive in the `[Unit]` section ensures the service starts only after `network.target` is active, but does NOT fail if `network.target` fails?

- A) `Requires=network.target`
- B) `BindsTo=network.target`
- C) `After=network.target`
- D) `Wants=network.target` combined with `After=network.target`

**Correct Answer: D**

*Explanation: `Wants=network.target` is a soft dependency (doesn't fail if network.target fails), and `After=network.target` ensures ordering. `Requires=` would cause this service to fail if network.target fails. `After=` alone provides ordering but no dependency.*

---

**Question 4**

Which `journalctl` command displays only error-level messages from the current boot session for the `nginx` unit?

- A) `journalctl -u nginx -b -p err`
- B) `journalctl --unit nginx --boot --priority error`
- C) `journalctl -u nginx --error -b0`
- D) `journalctl nginx error current-boot`

**Correct Answer: A**

*Explanation: `-u nginx` filters by unit, `-b` (without a number) refers to the current boot session, and `-p err` filters by priority level "err" (level 3 and below — all more severe levels are also included).*

---

**Question 5**

A cron job is scheduled with the expression `30 14 * * 1-5`. When does this job run?

- A) Every 30 minutes, Monday through Friday, from 2 PM to 5 PM
- B) At 2:30 PM, Monday through Friday
- C) At 2:30 AM on the 5th day of each month
- D) Every 14 hours and 30 minutes on weekdays

**Correct Answer: B**

*Explanation: The fields are minute(30) hour(14) day-of-month(*) month(*) day-of-week(1-5, Monday through Friday). This runs once daily at 14:30 (2:30 PM) on weekdays.*

---

**Question 6**

An administrator wants to prevent the `bluetooth.service` from ever starting, even if another unit tries to start it as a dependency. Which command accomplishes this?

- A) `systemctl disable bluetooth`
- B) `systemctl stop bluetooth`
- C) `systemctl mask bluetooth`
- D) `systemctl block bluetooth`

**Correct Answer: C**

*Explanation: `systemctl mask` creates a symlink from the unit file to `/dev/null`, preventing the service from starting by any means including as a dependency. `disable` only prevents automatic startup at boot but allows manual starts.*

---

**Question 7**

After modifying an existing service unit file in `/etc/systemd/system/`, the changes do not appear to take effect when the service is restarted. What is the most likely missing step?

- A) The system must be rebooted
- B) `systemctl daemon-reload` must be run before restarting the service
- C) The unit file must be copied to `/lib/systemd/system/`
- D) The `[Install]` section must be updated

**Correct Answer: B**

*Explanation: systemd caches unit file data in memory. After modifying a unit file, `systemctl daemon-reload` must be run to force systemd to re-read the files. Without this, the old unit definition continues to be used.*

---

**Question 8**

Which `journalctl` command would an administrator run to investigate what happened in the journal during the PREVIOUS system boot (not the current one)?

- A) `journalctl -b 0`
- B) `journalctl -b -1`
- C) `journalctl --previous-boot`
- D) `journalctl -b last`

**Correct Answer: B**

*Explanation: `-b 0` refers to the current boot (same as `-b`). `-b -1` refers to the previous boot. `-b -2` would be two boots ago. Use `journalctl --list-boots` to see all available boot records with their IDs.*

---

**Question 9**

A system administrator needs to schedule a one-time task to run the script `/opt/deploy.sh` in exactly 2 hours. Which command is correct?

- A) `crontab -e` and add `+2:00 /opt/deploy.sh`
- B) `at now + 2 hours` and enter `/opt/deploy.sh` at the prompt
- C) `schedule --once +2h /opt/deploy.sh`
- D) `systemctl run-once +2h /opt/deploy.sh`

**Correct Answer: B**

*Explanation: The `at` command is used for one-time future job scheduling. `at now + 2 hours` schedules the job for 2 hours from now. The command to run is entered interactively or piped: `echo "/opt/deploy.sh" | at now + 2 hours`.*

---

**Question 10**

Which systemd target is most equivalent to the legacy SysVinit runlevel 3 (multi-user mode without a graphical interface)?

- A) `default.target`
- B) `basic.target`
- C) `multi-user.target`
- D) `network.target`

**Correct Answer: C**

*Explanation: `multi-user.target` is the systemd equivalent of runlevel 3 — full multi-user mode with networking but no graphical display manager. `graphical.target` is equivalent to runlevel 5 (with GUI). `basic.target` is an earlier stage with basic services only.*

---

**Question 11** (5 points)

Which section of a systemd service unit file contains the `WantedBy=` directive that determines the target at which the service is activated when enabled?

- A) `[Unit]`
- B) `[Service]`
- C) `[Install]`
- D) `[Target]`

**Correct Answer: C**

*Explanation: The `[Install]` section contains directives that control what happens when `systemctl enable` is run. `WantedBy=multi-user.target` causes a symlink to be created in `multi-user.target.wants/`, which pulls the service into that target. `[Unit]` contains metadata and dependencies. `[Service]` contains execution parameters. There is no `[Target]` section in service unit files.*

---

**Question 12** (5 points)

An administrator wants to see the complete dependency tree for `httpd.service` — all units it depends on and all units that depend on it. Which commands provide this?

- A) `systemctl status httpd --full`
- B) `systemctl list-dependencies httpd` and `systemctl list-dependencies --reverse httpd`
- C) `systemctl show httpd --dependencies`
- D) `systemd-analyze httpd`

**Correct Answer: B**

*Explanation: `systemctl list-dependencies httpd` shows the tree of units that httpd depends on. `--reverse` inverts the query to show which units depend on httpd. These two commands together provide both directions of the dependency graph. `systemd-analyze` is used for boot time analysis, not dependency inspection.*

---

**Question 13** (5 points)

A systemd timer unit should trigger its associated service every 15 minutes. Which `OnCalendar=` expression in the timer's `[Timer]` section is correct?

- A) `OnCalendar=*-*-* *:15:00`
- B) `OnCalendar=*/15`
- C) `OnCalendar=*-*-* *:0/15:00`
- D) `OnCalendar=15min`

**Correct Answer: C**

*Explanation: The systemd calendar expression `*-*-* *:0/15:00` means every day, every hour, every 15 minutes starting from minute 0 (i.e., :00, :15, :30, :45). The `/` means "every N" starting from the left value. Option A would run at minute 15 of every hour only. Option B and D are not valid systemd calendar syntax.*

---

**Question 14** (5 points)

What is the correct way to view the environment variables that a running systemd service (`nginx.service`) currently has access to?

- A) `systemctl env nginx`
- B) `cat /proc/$(systemctl show nginx -p MainPID --value)/environ | tr '\0' '\n'`
- C) `journalctl -u nginx | grep ENV`
- D) `systemctl show nginx --environment`

**Correct Answer: B**

*Explanation: A running process's environment is exposed in `/proc/PID/environ` as null-delimited strings. `systemctl show nginx -p MainPID --value` retrieves the PID of the main nginx process, and `tr '\0' '\n'` converts null bytes to newlines for readable output. There is no `systemctl env` or `--environment` flag. journalctl does not record environment variables in log entries by default.*

---

**Question 15** (5 points)

An administrator configures a service with `Restart=on-failure` in the `[Service]` section. The service crashes 10 times in rapid succession. After some time, it stops restarting. What systemd setting controls this behavior?

- A) `RestartSec=` limits the total number of restarts
- B) `StartLimitIntervalSec=` and `StartLimitBurst=` together limit restart attempts within a time window
- C) `MaxRestartCount=` in the `[Unit]` section sets a hard limit
- D) `Restart=on-failure` only allows 3 restart attempts by default

**Correct Answer: B**

*Explanation: `StartLimitIntervalSec=` (default: 10 seconds) and `StartLimitBurst=` (default: 5 attempts) in the `[Unit]` section work together to implement rate limiting. If the service starts and fails more than `StartLimitBurst` times within `StartLimitIntervalSec`, systemd stops attempting restarts and puts the unit into a failed state. `RestartSec=` only adds a delay between restarts. There is no `MaxRestartCount=` directive.*

---

**Question 16** (5 points)

Which `journalctl` filter shows all messages from the current boot that arrived since 30 minutes ago?

- A) `journalctl -b --since "-30 minutes"`
- B) `journalctl -b --since "30 minutes ago"`
- C) `journalctl -b -30m`
- D) `journalctl --last 30min`

**Correct Answer: B**

*Explanation: `--since "30 minutes ago"` uses a human-readable relative time string. The `-b` flag restricts output to the current boot. `journalctl` accepts many time formats including "2024-01-15 14:30:00", "yesterday", "30 minutes ago", and "1 hour ago". Option A's syntax is incorrect. Option C and D are not valid flags.*

---

**Question 17** (5 points)

A user-level systemd service (running in the user session, not system-wide) is configured in `~/.config/systemd/user/myapp.service`. Which command enables and starts it for the current user?

- A) `sudo systemctl enable --now myapp`
- B) `systemctl --user enable --now myapp`
- C) `systemctl enable --user myapp && systemctl start --user myapp`
- D) `systemctl user-enable myapp`

**Correct Answer: B**

*Explanation: The `--user` flag instructs systemctl to interact with the user-level systemd instance instead of the system-wide one. `systemctl --user enable --now myapp` enables the unit in the user's systemd instance and starts it immediately. Using `sudo` would operate on the system instance and would not find the user-level unit file.*

---

**Question 18** (5 points)

The output of `systemctl status myservice` shows `Active: failed (Result: exit-code)`. Which `journalctl` command is the most direct way to see why it failed?

- A) `journalctl -u myservice -b -n 50`
- B) `journalctl -xe`
- C) `journalctl -u myservice -b -p err..emerg`
- D) `journalctl --failed myservice`

**Correct Answer: A**

*Explanation: `journalctl -u myservice -b -n 50` shows the last 50 lines from the current boot session for the specific failing unit. This is the fastest path to the service's own output and error messages. `-xe` shows the last journal entries with context but is not filtered to the failing unit. Option C would miss stdout output that was not logged at error level. Option D is not valid syntax.*

---

**Question 19** (5 points)

An administrator wants to run a script every day at midnight using a systemd timer instead of cron. The timer unit `backup.timer` is configured with `OnCalendar=daily`. What additional file is required for this to work, and what must its name be?

- A) `backup.service` — a service unit with the same base name as the timer
- B) `backup.target` — a target unit that the timer activates
- C) `backup.sh` — the script file must be in the same directory as the timer
- D) `backup.conf` — a configuration file specifying the script path

**Correct Answer: A**

*Explanation: A systemd timer unit activates a corresponding service unit with the same base name by default. `backup.timer` automatically activates `backup.service` when it fires. The service unit defines what command to run in its `ExecStart=` directive. This is why timer and service files are always created in pairs. A different unit can be specified with `Unit=` in the `[Timer]` section.*

---

**Question 20** (5 points)

What is the effect of running `systemctl isolate rescue.target`?

- A) It reboots the system into rescue mode at the next boot.
- B) It immediately switches the running system to rescue mode, stopping all services except those required for rescue.
- C) It schedules a maintenance window and notifies logged-in users.
- D) It creates a snapshot of the current target state for rollback.

**Correct Answer: B**

*Explanation: `systemctl isolate TARGET` immediately transitions the system to the specified target, stopping all units that are not part of that target and starting any that are. `isolate rescue.target` drops the system to single-user rescue mode immediately, terminating normal services and network connections. This is used for emergency maintenance. Unlike `set-default`, it takes effect right now, not at the next boot.*

---

### Answer Key

| Question | Answer |
|----------|--------|
| 1 | C |
| 2 | D |
| 3 | D |
| 4 | A |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | B |
| 9 | B |
| 10 | C |
| 11 | C |
| 12 | B |
| 13 | C |
| 14 | B |
| 15 | B |
| 16 | B |
| 17 | B |
| 18 | A |
| 19 | A |
| 20 | B |
