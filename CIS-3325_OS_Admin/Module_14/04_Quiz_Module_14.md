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

---

*Questions 11–20 — 5 pts each*

---

### Question 11 (5 points)

An administrator runs `sestatus` on a RHEL 9 server and sees `SELinuxfs mount: /sys/fs/selinux` and `Current mode: permissive` but `Mode from config file: enforcing`. What does this combination indicate?

* A: SELinux has been permanently disabled and will require a full relabel to re-enable.
* B: The runtime mode was changed to permissive with `setenforce 0` but the config file still specifies enforcing, so the system will return to enforcing after the next reboot.
* C: The config file is corrupted — the enforcing value was overwritten by the kernel at boot.
* D: The system is running in enforcing mode. `sestatus` always displays the config file value as the active mode.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: SELinux has not been disabled — permissive mode still has a policy loaded and active. A fully disabled SELinux shows `SELinux status: disabled`. No relabel is required to restore enforcing mode; simply editing the config file or running `setenforce 1` is sufficient.
* Why C is incorrect: The config file is not corrupted. The split between "current mode" and "mode from config file" is the expected output when `setenforce` has been used to temporarily override the boot-time setting. This is normal and intentional behavior.
* Why D is incorrect: `sestatus` accurately reports both the live runtime mode and the persistent config file value as separate fields. When they differ — as here — it is a clear signal that a runtime override is in effect. The current mode field reflects actual enforcement, not the config.

---

### Question 12 (5 points)

After copying web files to `/opt/webapp/static/` on a RHEL server, an administrator correctly runs `semanage fcontext -a -t httpd_sys_content_t "/opt/webapp/static(/.*)?"`. Apache still returns 403 errors. What step was missed?

* A: The SELinux policy must be recompiled with `semodule -B` after every `semanage` change.
* B: `restorecon -Rv /opt/webapp/static/` must be run to apply the new policy rule to the existing files on disk.
* C: The Apache process must be restarted so it re-reads the SELinux policy database.
* D: The boolean `httpd_read_user_content` must be enabled because `/opt/` is outside the default web root.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `semanage fcontext` modifies the file context database without requiring a policy recompilation. `semodule -B` is used to rebuild and reload all SELinux policy modules — it is not needed for routine context rule changes. `semanage` changes take effect after `restorecon` applies them to the existing inodes.
* Why C is incorrect: Apache does not cache or re-read the SELinux policy. The kernel enforces SELinux policy decisions per-access on the fly. Restarting Apache would not affect the file context labels already applied to the files in `/opt/webapp/static/`.
* Why D is incorrect: `httpd_read_user_content` allows Apache to read content from user home directories (`/home/*/public_html`). It is not a blanket permission for non-standard directories. The correct fix for a context mismatch is always `semanage fcontext` + `restorecon`, which was already half-completed — only `restorecon` is missing.

---

### Question 13 (5 points)

A custom application on Ubuntu listens on port 9200. Its AppArmor profile at `/etc/apparmor.d/usr.local.bin.myapp` was written to allow TCP port 80 only. The application is denied when it tries to bind to port 9200. The administrator edits the profile file to add `network tcp,` and saves it. What must happen next for the change to take effect without rebooting?

* A: Run `sudo systemctl restart apparmor` to reload all profiles.
* B: Run `sudo apparmor_parser -r /etc/apparmor.d/usr.local.bin.myapp` to reload only that profile into the kernel.
* C: Run `sudo aa-enforce /etc/apparmor.d/usr.local.bin.myapp` to push the updated rules into enforcement.
* D: The change takes effect automatically — AppArmor polls profile files for modifications every 60 seconds.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `systemctl restart apparmor` reloads all profiles by restarting the AppArmor service. While this would eventually apply the change, it is disruptive because it briefly removes confinement from all confined processes while the service restarts. The targeted `apparmor_parser -r` flag reloads only the specified profile with no disruption to other confined processes.
* Why C is incorrect: `aa-enforce` switches a profile's mode from complain to enforce. It does not re-parse or reload the profile file content. If the profile was already in enforce mode, `aa-enforce` alone would have no effect on the rules. Editing and saving the file requires `apparmor_parser -r` to push the new rules into the kernel.
* Why D is incorrect: AppArmor does not auto-reload profile files. Changes to profile files on disk have no effect until explicitly loaded into the kernel with `apparmor_parser -r` or a service reload. There is no polling mechanism.

---

### Question 14 (5 points)

An administrator needs to allow Apache on a RHEL server to send email through a local MTA for notification purposes. DAC permissions are correct. Which SELinux boolean controls this capability?

* A: `httpd_can_network_connect`
* B: `httpd_can_sendmail`
* C: `httpd_enable_sendmail`
* D: `allow_httpd_mail`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `httpd_can_network_connect` allows the Apache process to make general outbound TCP connections. While this would technically allow connections to an SMTP port, it is far broader than needed and violates the principle of least privilege. The specific boolean for mail is `httpd_can_sendmail`.
* Why C is incorrect: `httpd_enable_sendmail` is not a valid SELinux boolean name. Fabricated option names are common distractors in security questions — always verify boolean names with `getsebool -a | grep httpd`.
* Why D is incorrect: `allow_httpd_mail` is not a valid SELinux boolean. Boolean names follow the pattern of the process type followed by the capability — `httpd_can_sendmail` is the correctly named boolean for this purpose.

---

### Question 15 (5 points)

An administrator is building a new AppArmor profile for a custom binary at `/usr/local/bin/processor` that has never had a profile before. The binary reads input files, writes output files, and makes DNS lookups. Which tool is designed to generate the initial profile interactively while the application runs?

* A: `aa-logprof`
* B: `aa-genprof`
* C: `apparmor_parser -a`
* D: `aa-status --generate`

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: `aa-logprof` is used to update an existing profile that is already in complain mode, by reading log entries generated during test runs and offering to add allow rules. It requires a profile to already exist and to have been running in complain mode. For a brand-new profile with no existing rules, `aa-genprof` is the correct starting point.
* Why C is incorrect: `apparmor_parser -a` adds (loads) a profile file that already exists on disk. The `-a` flag is for loading a newly written profile into the kernel — it does not generate or suggest profile rules. It has no interactive monitoring capability.
* Why D is incorrect: `aa-status --generate` is not a valid flag combination. `aa-status` only displays the current status of loaded profiles. It has no profile generation functionality.

---

### Question 16 (5 points)

An administrator runs `getsebool -a | grep ftp` on a RHEL server and sees `ftp_home_dir --> off`. A user reports they cannot access their home directory via FTP even though DAC permissions are correct. Which command permanently enables home directory access for the FTP process?

* A: `sudo semanage fcontext -a -t public_content_t "/home(/.*)?"`
* B: `sudo setsebool ftp_home_dir on`
* C: `sudo setsebool -P ftp_home_dir on`
* D: `sudo chcon -R -t public_content_t /home/`

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: Adding a `public_content_t` context rule to `/home` would relabel home directories with a type that may allow read access but is not the correct approach for FTP home directory access. The proper fix is enabling the purpose-built boolean that grants the FTP daemon permission to access home directories.
* Why B is incorrect: `setsebool ftp_home_dir on` enables the boolean at runtime only. Without the `-P` (persistent) flag, the boolean reverts to `off` at the next reboot. The administrator would need to re-run the command after every restart.
* Why D is incorrect: `chcon -R -t public_content_t /home/` applies a temporary context change that will be overwritten by `restorecon`. Additionally, relabeling all home directories with `public_content_t` is broader and potentially less secure than enabling the specific boolean designed for this purpose.

---

### Question 17 (5 points)

On an Ubuntu 22.04 server, an administrator checks `aa-status` and sees a profile listed under "profiles in enforce mode" for `/usr/sbin/nginx`. A developer reports that after deploying a new nginx configuration that includes a custom log path at `/data/logs/nginx/`, nginx cannot write to that directory. AppArmor denials appear in the journal. What is the correct sequence of steps to permanently resolve this?

* A: Run `sudo aa-disable /etc/apparmor.d/usr.sbin.nginx` to remove all restrictions from nginx.
* B: Switch the profile to complain mode, confirm the deny is gone, then switch back to enforce — no profile edit needed.
* C: Edit `/etc/apparmor.d/usr.sbin.nginx` to add a write rule for `/data/logs/nginx/`, then run `sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx`.
* D: Run `sudo aa-logprof` to automatically add the missing rule, then run `sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx`.

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: Disabling the profile removes all AppArmor confinement from nginx, eliminating the security benefit entirely. This is never an appropriate production resolution for a path access issue.
* Why B is incorrect: Switching to complain mode stops blocking the access temporarily but does not make any permanent change to the profile rules. When returned to enforce mode, the denial will recur. The profile must be edited to add an explicit allow rule for the new log path.
* Why D is incorrect: `aa-logprof` can suggest rule additions based on recent denial log entries and is a valid alternative workflow, but it still requires `apparmor_parser -r` to be run afterward to reload the modified profile. Option C is the direct and complete solution. Option D is partially correct but incomplete as stated, since the `apparmor_parser` step is still needed after `aa-logprof` finishes.

---

### Question 18 (5 points)

Which command displays the complete SELinux status including the loaded policy name, mount point, policy deny count, and whether MLS policy is enabled?

* A: `getenforce`
* B: `setenforce --status`
* C: `sestatus`
* D: `seinfo`

Correct Answer: C

Distractor Analysis:

* Why A is incorrect: `getenforce` returns only a single word — `Enforcing`, `Permissive`, or `Disabled`. It provides no information about the policy name, MLS status, deny count, or mount point.
* Why B is incorrect: `setenforce` is used to change the SELinux runtime mode. It does not accept a `--status` flag. Attempting `setenforce --status` returns an error because the only valid arguments are `0`, `1`, `Permissive`, and `Enforcing`.
* Why D is incorrect: `seinfo` is a policy analysis tool from the `setools` package that queries policy details such as types, attributes, and roles. It provides deep policy inspection but does not report the simple runtime status fields like current mode, config file value, or MLS status that `sestatus` provides.

---

### Question 19 (5 points)

An administrator copies a file from `/tmp/newconfig.conf` to `/etc/httpd/conf.d/newconfig.conf` using `cp`. Apache fails to start and `ausearch -m avc -ts recent` shows a denial for reading `newconfig.conf` with type `user_tmp_t`. What happened and what is the fix?

* A: The file is owned by the wrong user. Run `chown apache:apache /etc/httpd/conf.d/newconfig.conf`.
* B: The `cp` command inherited the source file's SELinux context `user_tmp_t` from `/tmp`. Run `restorecon /etc/httpd/conf.d/newconfig.conf` to reset it to the correct `httpd_config_t` type.
* C: The file was copied without read permission. Run `chmod 644 /etc/httpd/conf.d/newconfig.conf`.
* D: The `/etc/httpd/conf.d/` directory has the wrong SELinux context. Run `semanage fcontext -a -t httpd_config_t "/etc/httpd/conf.d(/.*)?"` to fix the directory policy.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: The AVC denial is caused by an incorrect SELinux type (`user_tmp_t`), not by ownership. Changing the file owner is a DAC operation and will not resolve a MAC label mismatch. The scenario already confirms the deny is SELinux-based.
* Why C is incorrect: The AVC denial indicates a type label problem, not a permission bits problem. `chmod 644` sets DAC read permission, which is separate from SELinux type enforcement. If the file had the correct `httpd_config_t` type, Apache could read it regardless of whether the permission was 600 or 644 (assuming DAC also allows it).
* Why D is incorrect: The `/etc/httpd/conf.d/` directory already has the correct policy context — it is a standard Apache directory with established policy rules. The problem is the individual file that was copied from `/tmp` and carried the `user_tmp_t` label with it. `restorecon` on the specific file resets it to the policy-defined `httpd_config_t` type.

---

### Question 20 (5 points)

An AppArmor profile contains the line `deny /etc/shadow r,`. The `shadow` file has DAC permissions `640 root:shadow`. A process confined by this profile is running as root. Can the process read `/etc/shadow`?

* A: Yes — root always overrides AppArmor restrictions because MAC does not apply to the root user.
* B: No — AppArmor enforce mode blocks the access regardless of the process's Unix user ID because MAC policy takes precedence over DAC.
* C: Yes — the `deny` keyword in AppArmor only generates a log entry; it does not block access in enforce mode.
* D: No — but only because DAC permissions (640 root:shadow) prevent root from reading the file.

Correct Answer: B

Distractor Analysis:

* Why A is incorrect: This is the fundamental difference between DAC and MAC. Under DAC, root can override most permission checks. Under MAC (SELinux or AppArmor), the kernel enforces policy independently of user ID. A process running as root that is confined by an AppArmor profile in enforce mode is still subject to that profile's restrictions — root UID does not exempt a process from MAC enforcement.
* Why C is incorrect: The `deny` keyword in AppArmor is an explicit denial rule that blocks access in enforce mode and overrides any matching allow rules. It is not merely a logging directive. The `audit` keyword logs without blocking; `deny` blocks unconditionally when the profile is in enforce mode.
* Why D is incorrect: DAC permissions of `640 root:shadow` allow the root user to read the file (the owner bit `6` grants root read and write). If only DAC applied, root could read `/etc/shadow`. The denial is caused entirely by the AppArmor `deny` rule, not by DAC.
