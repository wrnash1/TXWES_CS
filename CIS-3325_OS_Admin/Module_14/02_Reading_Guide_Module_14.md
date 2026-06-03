# Reading Guide: Module 14 - SELinux and AppArmor Security

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 2.0 - Security

---

### Glossary

**DAC (Discretionary Access Control)** - Standard Unix permission model where the file owner controls access via read/write/execute bits. The owner may grant or restrict access at their discretion.

**MAC (Mandatory Access Control)** - A kernel-enforced security model where policy is defined by the system and cannot be overridden by individual users, including root. SELinux and AppArmor are MAC implementations.

**SELinux (Security-Enhanced Linux)** - A label-based MAC system integrated into the Linux kernel. Developed by the NSA. Default on RHEL, CentOS, and Fedora. Enforces policy based on security contexts (labels) attached to files, processes, ports, and devices.

**Security Context** - The SELinux label attached to every object, in the format `user:role:type:level`. The type field is most relevant for daily administration.

**AVC (Access Vector Cache)** - The SELinux kernel component that caches policy decisions. AVC denial messages in `/var/log/audit/audit.log` identify what was blocked and why.

**restorecon** - A command that resets file SELinux contexts to the values defined in the policy database. Used after `semanage fcontext` to apply new context rules to existing files.

**semanage** - A tool for managing SELinux policy settings including file contexts, port contexts, and user mappings. Changes made with semanage survive filesystem relabeling.

**AppArmor** - A path-based MAC system that confines programs via per-program profiles. Default on Ubuntu, Debian, and SUSE. Simpler than SELinux but less granular.

**AppArmor Profile** - A file in `/etc/apparmor.d/` that defines the allowed files, capabilities, and network operations for a specific program.

**Complain mode (AppArmor)** - AppArmor mode where violations are logged but not blocked. Equivalent to SELinux Permissive mode. Used for profile development and troubleshooting.

---

### SELinux Mode Reference

| Mode | getenforce output | Behavior |
|------|------------------|---------|
| Enforcing | `Enforcing` | Violations blocked and logged to audit.log |
| Permissive | `Permissive` | Violations logged only, not blocked |
| Disabled | `Disabled` | No policy loaded, no enforcement |

---

### SELinux Runtime vs Persistent Mode Commands

| Goal | Command |
|------|---------|
| Check current mode | `getenforce` |
| Check full status | `sestatus` |
| Switch to permissive (runtime only) | `sudo setenforce 0` |
| Switch to enforcing (runtime only) | `sudo setenforce 1` |
| Set mode persistently | Edit `/etc/selinux/config`, set `SELINUX=enforcing` |

`setenforce` changes do NOT survive reboot. The persistent setting is in `/etc/selinux/config`.

---

### SELinux Context Commands

| Command | Purpose |
|---------|---------|
| `ls -Z FILE` | Show file security context |
| `ps auxZ` | Show process security contexts |
| `id -Z` | Show current user security context |
| `chcon -t TYPE FILE` | Set context temporarily (overwritten by restorecon) |
| `semanage fcontext -a -t TYPE "PATH_REGEX"` | Add permanent context rule to policy |
| `restorecon -Rv PATH` | Apply policy contexts to files recursively |
| `sudo touch /.autorelabel && sudo reboot` | Relabel entire filesystem on next boot |

---

### Permanent Context Fix Workflow (Most Tested)

```bash
# Step 1: Add the rule to the policy database
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/webdata(/.*)?"

# Step 2: Apply the new rule to existing files
sudo restorecon -Rv /srv/webdata/
```

`chcon` alone is a temporary fix — it is overwritten when `restorecon` runs. Always use the two-step `semanage + restorecon` approach for production.

---

### SELinux Troubleshooting Commands

| Command | Purpose |
|---------|---------|
| `sudo ausearch -m avc -ts recent` | Show recent AVC denial messages |
| `sudo ausearch -m avc -ts recent \| audit2why` | Human-readable explanation of denials |
| `sudo sealert -a /var/log/audit/audit.log` | Detailed denial analysis with suggested fixes |
| `sudo grep AVC /var/log/audit/audit.log` | Raw AVC entries |

---

### SELinux Boolean Reference

| Command | Purpose |
|---------|---------|
| `getsebool -a` | List all booleans and values |
| `getsebool BOOLEAN` | Check a specific boolean |
| `sudo setsebool BOOLEAN on` | Set boolean at runtime (temporary) |
| `sudo setsebool -P BOOLEAN on` | Set boolean permanently |

Common web server booleans:

| Boolean | Allows |
|---------|--------|
| `httpd_can_network_connect` | Apache to make outbound connections |
| `httpd_can_sendmail` | Apache to send email |
| `httpd_read_user_content` | Apache to read user home directories |
| `httpd_enable_homedirs` | Apache to serve from home directories |

---

### SELinux Port Context Commands

| Command | Purpose |
|---------|---------|
| `semanage port -l` | List all port contexts |
| `semanage port -l \| grep http` | Find HTTP-related ports |
| `sudo semanage port -a -t http_port_t -p tcp 8080` | Allow Apache on port 8080 |

---

### AppArmor Mode Reference

| Mode | aa-status listing | Behavior |
|------|------------------|---------|
| enforce | "profiles in enforce mode" | Violations blocked and logged |
| complain | "profiles in complain mode" | Violations logged only |
| disabled | Not shown / "unloaded" | No restriction |

---

### AppArmor Command Reference

| Command | Purpose |
|---------|---------|
| `sudo aa-status` | Show all loaded profiles and their modes |
| `sudo systemctl status apparmor` | Check AppArmor service status |
| `sudo aa-enforce /etc/apparmor.d/PROFILE` | Switch profile to enforce mode |
| `sudo aa-complain /etc/apparmor.d/PROFILE` | Switch profile to complain mode |
| `sudo aa-disable /etc/apparmor.d/PROFILE` | Disable profile (program runs unrestricted) |
| `sudo apparmor_parser -r /etc/apparmor.d/PROFILE` | Reload modified profile into kernel |
| `sudo systemctl reload apparmor` | Reload all profiles |
| `sudo aa-genprof /path/to/program` | Generate a new profile interactively |
| `sudo aa-logprof` | Update profile based on recent log denials |

---

### AppArmor Log Diagnosis

```bash
sudo journalctl -k | grep apparmor
sudo grep apparmor /var/log/kern.log
```

Key fields in an AppArmor denial message:

* `apparmor="DENIED"` — access was blocked (enforce mode)
* `apparmor="ALLOWED"` — access logged in complain mode
* `profile=` — the confining profile
* `name=` — the file or resource accessed
* `requested_mask=` — the access type attempted (r=read, w=write, x=execute)

---

### SELinux vs AppArmor Comparison

| Feature | SELinux | AppArmor |
|---------|---------|---------|
| Approach | Label-based (inode labels) | Path-based (file paths) |
| Default distro | RHEL / CentOS / Fedora | Ubuntu / Debian / SUSE |
| Complexity | Higher | Lower |
| Permissive equivalent | Permissive mode | Complain mode |
| Log location | /var/log/audit/audit.log | Kernel log / journald |
| Diagnosis command | `ausearch -m avc` | `journalctl -k \| grep apparmor` |

---

### Exam Tips

1. SELinux modes: Enforcing blocks, Permissive logs only, Disabled is off. `getenforce` returns the exact string. Know all three.

2. `setenforce` is runtime only. `/etc/selinux/config` is persistent. Both are needed: set the config file for permanence, then `setenforce 1` for immediate effect without a reboot.

3. `chcon` is temporary — overwritten by `restorecon`. The permanent fix is always `semanage fcontext` + `restorecon`. This scenario (Apache cannot serve files after copying to new directory) is a direct exam question.

4. `setsebool -P` makes boolean changes permanent. Without `-P` the change is lost at reboot.

5. AppArmor `complain` mode = SELinux `permissive` mode. Both log without blocking. Use for troubleshooting and profile development.

6. `ausearch -m avc -ts recent` is the first command in any SELinux troubleshooting workflow. Know it.

7. `apparmor_parser -r` is required after editing a profile file — it reloads the profile into the running kernel.

8. `aa-logprof` reads recent AppArmor denials and interactively offers to add allow rules. It is the primary tool for refining a new profile after running the application in complain mode.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

* State what `getenforce` returns for each of the three SELinux modes
* Use `setenforce 0` and `setenforce 1` correctly and explain why they do not persist
* Edit `/etc/selinux/config` to make the mode change persistent
* Use `ausearch -m avc -ts recent` to find SELinux denials
* Apply a permanent context fix with `semanage fcontext` and `restorecon`
* Set a SELinux boolean permanently with `setsebool -P`
* Use `aa-status` to determine which AppArmor profiles are in enforce vs complain mode
* Switch an AppArmor profile between enforce and complain mode
* Reload a modified AppArmor profile with `apparmor_parser -r`
* Find AppArmor denials in the journal
* Compare SELinux and AppArmor by approach, default distro, and log location
