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
