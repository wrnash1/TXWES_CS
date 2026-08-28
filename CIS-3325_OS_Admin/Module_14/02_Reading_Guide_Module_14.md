# Reading Guide: Module 14 - SELinux and AppArmor Security

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

## 9. Supplemental Resources

**1. [SELinux User's and Administrator's Guide — Red Hat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/index)**
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/index
Red Hat's official SELinux guide for RHEL 9, covering enforcing/permissive modes, file context management with semanage and restorecon, boolean administration, AVC denial analysis with audit2why, and port context management.

**2. [AppArmor Documentation — Ubuntu](https://documentation.ubuntu.com/server/how-to/security/apparmor/)**
https://documentation.ubuntu.com/server/how-to/security/apparmor/
Ubuntu's official AppArmor administration guide covering profile modes, aa-genprof and aa-logprof workflows, apparmor_parser usage, and reading denial messages from the kernel journal.

**3. [Linux Security Modules (LSM) — kernel.org](https://www.kernel.org/doc/html/latest/security/lsm.html)**
https://www.kernel.org/doc/html/latest/security/lsm.html
The kernel documentation for the Linux Security Modules framework that underpins both SELinux and AppArmor, explaining how MAC hooks integrate with the kernel's permission checking path and why MAC decisions occur after DAC checks.

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
