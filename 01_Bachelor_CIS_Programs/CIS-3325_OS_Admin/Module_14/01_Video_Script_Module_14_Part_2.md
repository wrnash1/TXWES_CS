# Video Script: Module 14 - SELinux and AppArmor Security (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA Linux+ / Linux Foundation &bull; Operating System Administration &bull; Module 14</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ / Linux Foundation &bull; Operating System Administration" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ / Linux Foundation &bull; Operating System Administration</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - AppArmor Administration

---

### Opening

Welcome back to Part 2 of Module 14. In Part 1 we covered SELinux architecture, modes, context
management, booleans, and the troubleshooting workflow. In Part 2 we cover AppArmor, which is
the MAC system used on Ubuntu, Debian, and SUSE Linux. AppArmor takes a path-based approach rather
than the label-based approach of SELinux, making it simpler to understand but less granular.

---

### Section 1: AppArmor Architecture

[SHOW TERMINAL]

AppArmor confines programs by assigning them a profile. The profile defines exactly which files,
capabilities, and network operations the program is allowed to use. Everything not explicitly
allowed is denied when the profile is in enforce mode.

Key difference from SELinux:

* SELinux uses labels on every file — context is attached to the inode
* AppArmor uses file paths — the profile matches programs by path name

AppArmor profiles are stored in `/etc/apparmor.d/`.

```bash
ls /etc/apparmor.d/
```

Each file is named after the program it confines (using the full path with slashes replaced by
dots): `usr.sbin.nginx`, `usr.bin.man`, etc.

---

### Section 2: AppArmor Status and Modes

[SHOW TERMINAL]

```bash
sudo aa-status
```

Shows loaded profiles, how many are in enforce vs complain mode, and which processes are
confined.

AppArmor profile modes:

* **enforce** — profile is active; violations are blocked and logged
* **complain** — profile is loaded; violations are logged but NOT blocked
* **disabled** — profile is unloaded; program runs without restriction

The enforce/complain distinction mirrors SELinux Enforcing/Permissive.

Check if AppArmor is running:

```bash
sudo systemctl status apparmor
```

---

### Section 3: Switching Profile Modes

[SHOW TERMINAL]

```bash
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
```

Put the nginx profile into enforce mode.

```bash
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx
```

Put the nginx profile into complain mode (for troubleshooting).

```bash
sudo aa-disable /etc/apparmor.d/usr.sbin.nginx
```

Disable the profile entirely (nginx runs unrestricted).

Apply changes to a modified profile:

```bash
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
```

The `-r` flag replaces (reloads) the profile in the kernel. Required after editing a profile file.

Load all profiles:

```bash
sudo systemctl reload apparmor
```

---

### Section 4: Reading AppArmor Logs

[SHOW TERMINAL]

AppArmor logs denials to the system log (syslog/journald), not a dedicated audit log.

```bash
sudo journalctl -k | grep apparmor
```

Or:

```bash
sudo grep apparmor /var/log/kern.log
```

A denial message looks like:

```
apparmor="DENIED" operation="open" profile="/usr/sbin/nginx"
name="/srv/webdata/index.html" pid=1234 comm="nginx"
requested_mask="r" denied_mask="r" fsuid=33 ouid=0
```

Key fields:

* `apparmor="DENIED"` — access was blocked
* `profile=` — which profile denied the access
* `name=` — which file was accessed
* `requested_mask="r"` — read access was attempted

---

### Section 5: AppArmor Profile Syntax

[SHOW TERMINAL]

A simplified AppArmor profile:

```
#include <tunables/global>

/usr/sbin/nginx {
  #include <abstractions/base>
  #include <abstractions/nameservice>

  capability net_bind_service,

  /etc/nginx/** r,
  /var/log/nginx/*.log w,
  /var/www/html/** r,
  /run/nginx.pid rw,

  deny /etc/shadow r,
}
```

Access modes:

| Mode | Meaning |
|------|---------|
| r | Read |
| w | Write |
| x | Execute |
| rw | Read and write |
| ix | Inherit execute (keep current profile) |
| cx | Execute with child profile |

`deny` explicitly blocks access even if another rule would allow it.

---

### Section 6: Creating and Testing Profiles

[SHOW TERMINAL]

`apparmor-utils` provides tools for generating profiles:

```bash
sudo apt install apparmor-utils
```

Generate a profile in complain mode for a program:

```bash
sudo aa-genprof /usr/local/bin/myapp
```

This starts the program and interactively builds a profile based on what the program actually does.
After the program runs, `aa-genprof` presents each access and asks whether to allow or deny it.

Use `aa-logprof` to update an existing profile based on recent log entries:

```bash
sudo aa-logprof
```

This reads AppArmor denials from the log and offers to add allow rules for each one.

Workflow for deploying a new application with AppArmor:

1. Start in complain mode: `aa-complain`
2. Run the application through all its use cases
3. Review denials: `aa-logprof`
4. Switch to enforce mode: `aa-enforce`
5. Monitor for remaining denials

---

### Section 7: SELinux vs AppArmor Comparison

[SHOW TERMINAL]

| Feature | SELinux | AppArmor |
|---------|---------|---------|
| Approach | Label-based (inode labels) | Path-based (file paths) |
| Default distro | RHEL, CentOS, Fedora | Ubuntu, Debian, SUSE |
| Policy scope | Entire system, all objects | Per-program profiles |
| Complexity | Higher | Lower |
| Granularity | Higher (user, role, type, level) | Lower (path and capability) |
| Permissive equivalent | Permissive mode | Complain mode |
| Log location | /var/log/audit/audit.log | Kernel log / journald |
| Diagnosis tool | ausearch, audit2why | aa-status, journalctl -k |

Both provide MAC. Both have a mode where violations are logged but not blocked (used for
troubleshooting and profile development). Both are tested on the Linux+ exam.

---

### Section 8: Exam Tips for Module 14

SELinux modes: Enforcing blocks and logs. Permissive logs only. Disabled means off. Know all
three and what `getenforce` returns for each.

`setenforce` is temporary. `/etc/selinux/config` is permanent. Both are needed for the two-step
"fix and persist" workflow.

`chcon` is temporary. `semanage fcontext + restorecon` is permanent. This is a directly tested
exam scenario.

`setsebool -P` is the permanent boolean change. Without `-P`, the change is lost at reboot.

AppArmor `complain` = SELinux `permissive`. Both log without blocking.

`aa-enforce` and `aa-complain` switch profiles. `apparmor_parser -r` reloads a modified profile.

`ausearch -m avc` finds SELinux denials. `journalctl -k | grep apparmor` finds AppArmor denials.

---

### Summary

Module 14 covers both MAC implementations tested on Linux+: SELinux (label-based, RHEL) and
AppArmor (path-based, Ubuntu). Key skills: reading and fixing file contexts, interpreting AVC
denials, using booleans, switching modes, and using complain/permissive mode for troubleshooting
without permanently disabling MAC enforcement.

Module 15 covers containerization with Docker.

---

### Additional Resources

* professormesser.com - CompTIA Linux+ study materials and practice exams
* comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
