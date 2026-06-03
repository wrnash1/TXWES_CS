# Quiz: Module 14 - SELinux and AppArmor Security

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

### Question 1

An administrator runs `getenforce` on a RHEL server and sees the output `Permissive`. What does this mean for the system's security posture?

* A: SELinux is fully enforcing policy — all access violations are blocked and written to the audit log.
* B: SELinux is disabled and no policy is loaded. The system uses only standard DAC permissions.
* C: SELinux policy violations are logged but not blocked. The system is not actively enforcing MAC policy.
* D: SELinux is in a read-only state. Policy can be viewed but not modified until the system is rebooted in enforcing mode.

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: The description of violations being blocked and logged describes Enforcing mode, not Permissive. `getenforce` would return `Enforcing` in that case.
* Why B is incorrect: When SELinux is fully disabled, `getenforce` returns `Disabled` and no policy is loaded at all. Permissive mode still has a policy loaded and active for logging — it simply does not block access.
* Why D is incorrect: There is no "read-only" SELinux state. The three valid modes are Enforcing, Permissive, and Disabled. Permissive mode allows all access while generating audit log entries for any policy violations.

---

### Question 2

A web server on RHEL returns a "403 Forbidden" error for files in a newly created directory `/srv/webdata/`. The Apache process has read permission on the files (DAC is correct), but the error persists. Which SELinux troubleshooting step should be performed first?

* A: Run `setenforce 0` to disable SELinux enforcement permanently.
* B: Run `ausearch -m avc -ts recent` to check the audit log for SELinux AVC denial messages.
* C: Run `chown apache:apache /srv/webdata/` to change ownership to the web server user.
* D: Edit `/etc/selinux/config` and set `SELINUX=disabled`, then reboot.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `setenforce 0` switches to permissive mode temporarily for troubleshooting — it is not a fix and should not be used to bypass SELinux permanently. The first step is to diagnose whether SELinux is the cause by checking the audit log before taking any action.
* Why C is incorrect: The scenario states DAC permissions are already correct. Changing file ownership is a DAC operation and will not resolve an SELinux context mismatch. The Apache process context must be allowed to read files with the correct SELinux type label.
* Why D is incorrect: Disabling SELinux entirely is not a valid troubleshooting or production response. It removes the MAC layer from the entire system. The correct approach is to identify the specific denial and fix the context or enable the appropriate boolean.

---

### Question 3

After moving HTML files to `/srv/webdata/` with `cp`, Apache cannot serve them due to an SELinux AVC denial. The policy requires the files to have the `httpd_sys_content_t` type. Which command permanently fixes the context so it survives a future relabeling?

* A: `chcon -t httpd_sys_content_t /srv/webdata/`
* B: `semanage fcontext -a -t httpd_sys_content_t "/srv/webdata(/.*)?" && restorecon -Rv /srv/webdata/`
* C: `chmod 644 /srv/webdata/*`
* D: `setsebool -P httpd_read_user_content on`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `chcon` applies a context change directly to the filesystem but does not update the SELinux policy database. When `restorecon` is run or the filesystem is relabeled, `chcon` changes are overwritten and the files revert to the policy default context.
* Why C is incorrect: `chmod 644` sets DAC file permissions. It has no effect on SELinux context labels and will not resolve an AVC denial caused by an incorrect type.
* Why D is incorrect: `httpd_read_user_content` is a boolean that allows Apache to read content from user home directories — it does not grant access to arbitrary paths like `/srv/webdata/`. The root cause is an incorrect file context type, not a missing boolean.

---

### Question 4

On an Ubuntu server, an administrator runs `aa-status` and sees the `nginx` profile listed as being in `complain` mode. What does this indicate about how AppArmor is handling the `nginx` process?

* A: AppArmor is fully enforcing the nginx profile — any access outside the profile is blocked.
* B: The nginx profile is loaded but AppArmor logs policy violations without blocking them, equivalent to SELinux permissive mode.
* C: The nginx profile is unloaded and nginx is running without any AppArmor restrictions.
* D: AppArmor has detected a policy violation in the nginx profile and has quarantined the process.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: Active blocking describes `enforce` mode, not `complain` mode. In `aa-status` output, profiles in enforce mode are listed under "profiles in enforce mode." The nginx profile listed under complain mode means it only logs.
* Why C is incorrect: An unloaded profile would not appear in `aa-status` output at all (or would be listed as unloaded). Complain mode means the profile is loaded and active for logging purposes — the process is not running unrestricted.
* Why D is incorrect: AppArmor does not quarantine processes. It either enforces (blocks and logs) or complains (logs only). There is no quarantine state in AppArmor's operating model.

---

### Question 5

An administrator changes SELinux to permissive mode using `setenforce 0` to troubleshoot a web server issue. After fixing the context with `restorecon`, they want to restore enforcing mode permanently for the next reboot. Which action ensures the mode persists after reboot?

* A: Run `setenforce 1` — this change is automatically written to `/etc/selinux/config`.
* B: Edit `/etc/selinux/config` and set `SELINUX=enforcing`, then reboot or run `setenforce 1` for immediate effect.
* C: Run `systemctl restart selinux-policy` to reload the policy in enforcing mode.
* D: Run `fixfiles relabel /` to relabel the filesystem and re-enable enforcement.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `setenforce 1` changes the runtime mode immediately but does NOT write to `/etc/selinux/config`. The persistent mode setting is read only at boot from the config file. If the config still says `permissive`, the next reboot will revert to permissive regardless of `setenforce`.
* Why C is incorrect: There is no `selinux-policy` systemd service to restart. SELinux policy is loaded into the kernel at boot by the init system, not managed as a runtime systemd service. This command would fail with a unit-not-found error.
* Why D is incorrect: `fixfiles relabel /` triggers a full filesystem relabeling on the next boot — it restores file contexts to policy defaults. It does not control the SELinux enforcement mode. Running a full relabel when the goal is simply to set the mode to enforcing is unnecessary and potentially disruptive.

---

### Question 6

An administrator has modified the AppArmor profile for a custom application at `/etc/apparmor.d/usr.local.bin.myapp`. What command is required to load the updated profile into the running kernel without rebooting?

* A: `sudo systemctl restart apparmor`
* B: `sudo aa-enforce /etc/apparmor.d/usr.local.bin.myapp`
* C: `sudo apparmor_parser -r /etc/apparmor.d/usr.local.bin.myapp`
* D: `sudo semanage policy -r /etc/apparmor.d/usr.local.bin.myapp`

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: `systemctl restart apparmor` restarts the AppArmor service and reloads all profiles, but it is disruptive — it briefly removes all profile enforcement for every confined process. The targeted `-r` flag with `apparmor_parser` reloads only the specified profile.
* Why B is incorrect: `aa-enforce` switches a profile to enforce mode but does not reload a modified profile's content. If the profile file was edited, `aa-enforce` alone does not pick up the changes — `apparmor_parser -r` is required to re-parse and reload the new rules.
* Why D is incorrect: `semanage` is a SELinux tool for managing policy settings. It has no function in AppArmor administration. AppArmor and SELinux are separate MAC systems with entirely different toolsets.

---

### Question 7

An administrator needs to allow an SELinux-confined Apache process to make outbound network connections to a backend API server. DAC permissions are correct and the network path is clear. Which is the correct SELinux fix?

* A: `sudo chcon -t http_port_t /etc/httpd/conf/httpd.conf`
* B: `sudo semanage port -a -t http_port_t -p tcp 8080`
* C: `sudo setsebool -P httpd_can_network_connect on`
* D: `sudo restorecon -Rv /var/www/html/`

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: `chcon` changes a file's SELinux type label. Setting a config file to `http_port_t` makes no sense — `http_port_t` is a port context type, not a file type, and `chcon` on a config file would not affect whether Apache can make outbound network connections.
* Why B is incorrect: `semanage port -a` adds a port to an existing SELinux port type — it is used when an application listens on a non-standard port. It does not control whether a process is permitted to make outbound connections to remote hosts.
* Why D is incorrect: `restorecon` resets file contexts to policy defaults. It has no effect on network connection permissions. The problem is that Apache's SELinux policy does not allow outbound network connections by default — enabling the `httpd_can_network_connect` boolean is the correct fix.

---

### Question 8

An administrator runs `ausearch -m avc -ts recent` on a RHEL server and sees no output. What is the most likely explanation?

* A: SELinux is in Permissive mode, so no AVC denials are generated.
* B: The audit daemon (auditd) is not running, or there have been no SELinux denials recently.
* C: The `ausearch` command requires root privileges; the administrator ran it as a regular user.
* D: AVC denials are only stored in `/var/log/messages`, not the audit log.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: In Permissive mode, SELinux still generates AVC denial messages — it logs all policy violations even though it does not block them. Permissive mode is frequently used specifically to generate AVC logs for troubleshooting without blocking access.
* Why C is incorrect: `ausearch` does require elevated privileges to read the audit log, but the symptom described is "no output" rather than a permission error. If run without sufficient privilege, `ausearch` returns an error message, not empty output.
* Why D is incorrect: AVC denials are written to `/var/log/audit/audit.log` by the audit daemon. While some messages may also appear in `/var/log/messages`, the audit log is the authoritative source and `ausearch` reads it correctly.

---

### Question 9

An AppArmor profile for a custom application is in complain mode. The administrator wants to refine the profile by reviewing what the application attempted to access during testing and adding appropriate allow rules. Which tool is designed specifically for this workflow?

* A: `aa-genprof`
* B: `aa-logprof`
* C: `apparmor_parser -r`
* D: `aa-status`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `aa-genprof` generates a new profile from scratch for a program that has no profile yet. It watches the program run interactively and builds the initial profile. `aa-logprof` is the correct tool for updating an existing profile based on log entries from a program that has already been running in complain mode.
* Why C is incorrect: `apparmor_parser -r` reloads a profile file into the kernel after it has been manually edited. It does not analyze log entries or suggest new rules.
* Why D is incorrect: `aa-status` displays the current status of all loaded profiles. It does not read logs or make any profile modifications.

---

### Question 10

Which command shows the SELinux type context of a running process?

* A: `ls -Z /proc/$(pgrep httpd)/`
* B: `ps auxZ | grep httpd`
* C: `getenforce httpd`
* D: `sestatus -p httpd`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: While `/proc/PID/` contains process information, `ls -Z` on that path shows the SELinux context of the `/proc` filesystem entries themselves, not the security context under which the process is running. `ps auxZ` is the standard command for viewing process security contexts.
* Why C is incorrect: `getenforce` takes no arguments. It returns only the current SELinux enforcement mode (Enforcing, Permissive, or Disabled) for the entire system — not the context of any specific process.
* Why D is incorrect: `sestatus` takes no process arguments. It reports overall SELinux status including the loaded policy name, current mode, and MLS status — not per-process context information.
