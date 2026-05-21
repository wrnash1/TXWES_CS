# Quiz: Module 14 - SELinux and AppArmor Security
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator runs `getenforce` on a RHEL server and sees the output `Permissive`. What does this mean for the system's security posture?
A) SELinux is fully enforcing policy — all access violations are blocked and written to the audit log.
B) SELinux is disabled and no policy is loaded. The system uses only standard DAC permissions.
C) SELinux policy violations are logged but not blocked. The system is not actively enforcing MAC policy.
D) SELinux is in a read-only state. Policy can be viewed but not modified until the system is rebooted in enforcing mode.
*   **Correct Answer:** C) SELinux policy violations are logged but not blocked. The system is not actively enforcing MAC policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The description of violations being blocked and logged describes Enforcing mode, not Permissive. `getenforce` would return `Enforcing` in that case.
    *   *Why B is incorrect:* When SELinux is fully disabled, `getenforce` returns `Disabled` and no policy is loaded at all. Permissive mode still has a policy loaded and active for logging — it simply does not block access.
    *   *Why D is incorrect:* There is no "read-only" SELinux state. The three valid modes are Enforcing, Permissive, and Disabled. Permissive mode allows all access while generating audit log entries for any policy violations.

---

---

**Question 2**
A web server on RHEL returns a "403 Forbidden" error for files in a newly created directory `/srv/webdata/`. The Apache process has read permission on the files (DAC is correct), but the error persists. Which SELinux troubleshooting step should be performed first?
A) Run `setenforce 0` to disable SELinux enforcement permanently.
B) Run `ausearch -m avc -ts recent` to check the audit log for SELinux AVC denial messages.
C) Run `chown apache:apache /srv/webdata/` to change ownership to the web server user.
D) Edit `/etc/selinux/config` and set `SELINUX=disabled`, then reboot.
*   **Correct Answer:** B) Run `ausearch -m avc -ts recent` to check the audit log for SELinux AVC denial messages.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `setenforce 0` switches to permissive mode temporarily for troubleshooting — it is not a fix and should not be used to bypass SELinux permanently. The first step is to diagnose whether SELinux is the cause by checking the audit log before taking any action.
    *   *Why C is incorrect:* The scenario states DAC (standard Unix) permissions are already correct. Changing file ownership is a DAC operation and will not resolve an SELinux context mismatch. The Apache process context must be allowed to read files with the correct SELinux type label.
    *   *Why D is incorrect:* Disabling SELinux entirely is not a valid troubleshooting or production response. It removes the MAC layer from the entire system. The correct approach is to identify the specific denial and fix the context or enable the appropriate boolean.

---

---

**Question 3**
After moving HTML files to `/srv/webdata/` with `cp`, Apache cannot serve them due to an SELinux AVC denial. The policy requires the files to have the `httpd_sys_content_t` type. Which command permanently fixes the context so it survives a future relabeling?
A) chcon -t httpd_sys_content_t /srv/webdata/
B) semanage fcontext -a -t httpd_sys_content_t "/srv/webdata(/.*)?" && restorecon -Rv /srv/webdata/
C) chmod 644 /srv/webdata/*
D) setsebool -P httpd_read_user_content on
*   **Correct Answer:** B) semanage fcontext -a -t httpd_sys_content_t "/srv/webdata(/.*)?" && restorecon -Rv /srv/webdata/
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `chcon` applies a context change directly to the filesystem but does not update the SELinux policy database. When `restorecon` is run or the filesystem is relabeled, `chcon` changes are overwritten and the files revert to the policy default context.
    *   *Why C is incorrect:* `chmod 644` sets DAC file permissions (owner read/write, group and others read-only). It has no effect on SELinux context labels and will not resolve an AVC denial caused by an incorrect type.
    *   *Why D is incorrect:* `httpd_read_user_content` is a boolean that allows Apache to read content from user home directories — it does not grant access to arbitrary paths like `/srv/webdata/`. The root cause is an incorrect file context type, not a missing boolean.

---

**Question 4**
On an Ubuntu server, an administrator runs `aa-status` and sees the `nginx` profile listed as being in `complain` mode. What does this indicate about how AppArmor is handling the `nginx` process?
A) AppArmor is fully enforcing the nginx profile — any access outside the profile is blocked.
B) The nginx profile is loaded but AppArmor logs policy violations without blocking them, equivalent to SELinux permissive mode.
C) The nginx profile is unloaded and nginx is running without any AppArmor restrictions.
D) AppArmor has detected a policy violation in the nginx profile and has quarantined the process.
*   **Correct Answer:** B) The nginx profile is loaded but AppArmor logs policy violations without blocking them, equivalent to SELinux permissive mode.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Active blocking describes `enforce` mode, not `complain` mode. In `aa-status` output, profiles in enforce mode are listed under "profiles in enforce mode." The nginx profile listed under complain mode means it only logs.
    *   *Why C is incorrect:* An unloaded profile would not appear in `aa-status` output at all (or would be listed as unloaded). Complain mode means the profile is loaded and active for logging purposes — the process is not running unrestricted.
    *   *Why D is incorrect:* AppArmor does not quarantine processes. It either enforces (blocks and logs) or complains (logs only). There is no quarantine state in AppArmor's operating model.

---

**Question 5**
An administrator changes SELinux to permissive mode using `setenforce 0` to troubleshoot a web server issue. After fixing the context with `restorecon`, they want to restore enforcing mode permanently for the next reboot. Which action ensures the mode persists after reboot?
A) Run `setenforce 1` — this change is automatically written to `/etc/selinux/config`.
B) Edit `/etc/selinux/config` and set `SELINUX=enforcing`, then reboot or run `setenforce 1` for immediate effect.
C) Run `systemctl restart selinux-policy` to reload the policy in enforcing mode.
D) Run `fixfiles relabel /` to relabel the filesystem and re-enable enforcement.
*   **Correct Answer:** B) Edit `/etc/selinux/config` and set `SELINUX=enforcing`, then reboot or run `setenforce 1` for immediate effect.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `setenforce 1` changes the runtime mode immediately but does NOT write to `/etc/selinux/config`. The persistent mode setting is read only at boot from the config file. If the config still says `permissive`, the next reboot will revert to permissive regardless of `setenforce`.
    *   *Why C is incorrect:* There is no `selinux-policy` systemd service to restart. SELinux policy is loaded into the kernel at boot by the init system, not managed as a runtime systemd service. This command would fail with a unit-not-found error.
    *   *Why D is incorrect:* `fixfiles relabel /` triggers a full filesystem relabeling on the next boot — it restores file contexts to policy defaults. It does not control the SELinux enforcement mode. Running a full relabel when the goal is simply to set the mode to enforcing is unnecessary and potentially disruptive.
