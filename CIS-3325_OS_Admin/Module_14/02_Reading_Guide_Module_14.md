# Reading Guide: Module 14 - SELinux and AppArmor Security
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 14 – SELinux and AppArmor Security**! This week covers Mandatory Access Control (MAC) on Linux — Security-Enhanced Linux (SELinux) used on RHEL/CentOS/Fedora, and AppArmor used on Debian/Ubuntu. These frameworks enforce access policies that go beyond standard Unix file permissions. SELinux and AppArmor are tested on CompTIA Linux+ XK0-005 under Domain 2.0 (Security).

As you work through this material you will learn how SELinux labels and policies control process access, how to check and change SELinux modes, how to troubleshoot AVC denials, and how AppArmor profiles restrict application behavior.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SELinux modes**: SELinux operates in three modes. **Enforcing** — the policy is active and access violations are blocked and logged. **Permissive** — violations are logged but not blocked (used for troubleshooting and policy development). **Disabled** — SELinux is completely off; no logging, no enforcement. Check the current mode with `getenforce` or `sestatus`. Change it temporarily with `setenforce 0` (permissive) or `setenforce 1` (enforcing). Persistent mode is set in `/etc/selinux/config` via the `SELINUX=` directive — requires a reboot.
*   **SELinux contexts and labels**: Every file, process, port, and user has an SELinux security context consisting of user, role, type, and level (e.g., `system_u:object_r:httpd_sys_content_t:s0`). The `type` field is the most important for policy decisions — it controls which processes can access which files. View file contexts with `ls -Z`; view process contexts with `ps -Z`. Set or restore file contexts with `chcon -t httpd_sys_content_t /var/www/html/file` (temporary) or `restorecon -v /var/www/html/file` (restore to policy default).
*   **SELinux troubleshooting (`ausearch`, `audit2allow`)**: Access denials are logged to `/var/log/audit/audit.log` as AVC (Access Vector Cache) denial messages. `ausearch -m avc -ts recent` shows recent denials. `audit2why` explains why a denial occurred in plain language. `audit2allow -a` reads the audit log and generates a policy module to permit the denied action. `setsebool -P httpd_can_network_connect on` enables a named boolean (persistent with `-P`) without modifying the core policy.
*   **SELinux booleans**: Predefined policy switches that toggle specific behaviors without rewriting the policy. `getsebool -a` lists all booleans and their current state. `setsebool httpd_can_sendmail on` enables the boolean for the current session; `-P` makes it permanent. Common exam booleans: `httpd_can_network_connect`, `httpd_enable_homedirs`, `ftp_home_dir`, `samba_enable_home_dirs`.
*   **AppArmor**: A MAC system used on Debian, Ubuntu, and SUSE. AppArmor uses per-application profiles stored in `/etc/apparmor.d/` to define what files and capabilities a program may access. Profiles can be in **enforce** mode (violations blocked and logged) or **complain** mode (violations logged only, equivalent to SELinux permissive). `aa-status` shows loaded profiles; `aa-complain /etc/apparmor.d/usr.sbin.nginx` puts a profile in complain mode; `aa-enforce` re-enables enforcement. `apparmor_parser -r /etc/apparmor.d/profile` reloads a profile after editing.
*   **DAC vs MAC**: Discretionary Access Control (DAC) is the standard Unix permission model — the file owner controls access via `chmod`/`chown`. Mandatory Access Control (MAC) — SELinux and AppArmor — enforces policy defined by the system administrator that users and processes cannot override, even as root. A root process can be denied access by SELinux policy, which is the key security advantage of MAC over DAC.

---

### 2. Certification Exam Tips
*   **Domain alignment:** SELinux and AppArmor map to Linux+ Domain 2.0 (Security). Expect 5–7 questions on SELinux modes, context types, boolean management, and AVC denial troubleshooting.
*   **`setenforce` vs `/etc/selinux/config` trap:** `setenforce 0` immediately switches to permissive mode but is lost at reboot. Persistent mode change requires editing `SELINUX=permissive` (or `enforcing`/`disabled`) in `/etc/selinux/config` and rebooting. The exam presents a scenario where the mode reverts after reboot — the answer is that `setenforce` was used instead of editing the config file.
*   **`restorecon` vs `chcon`:** `chcon` sets a context immediately but it is overwritten the next time `restorecon` or a relabeling runs. `restorecon` restores the context from the policy's file context database — this is the permanent fix. The exam scenario: "context was fixed with `chcon` but broke after a relabel" — the correct fix is `restorecon`.
*   **AVC denial workflow:** The standard exam troubleshooting sequence for SELinux denials is: (1) `ausearch -m avc -ts recent` to find the denial, (2) `audit2why` to understand it, (3) check if a boolean covers the use case (`getsebool -a | grep relevant`), (4) if not, use `audit2allow` to generate a policy module.
*   **AppArmor complain mode = SELinux permissive:** The exam tests equivalencies between SELinux and AppArmor terminology. Complain mode in AppArmor is the equivalent of permissive mode in SELinux — both log violations without blocking them.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) provides security and permissions foundation relevant to MAC concepts. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of SELinux mode management, context fixes, and AppArmor profile inspection in a live Linux environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the security and permissions chapters of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which provide the file permission and process security foundation essential for understanding how SELinux and AppArmor extend the Linux security model.
*   **Required Video:** Watch the SELinux and AppArmor videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates SELinux mode switching, context management, boolean configuration, and AppArmor profile usage in a live environment.

---

### Lab & Command Integration
In this week's hands-on lab you will check the SELinux mode with `getenforce`, switch to permissive mode with `setenforce 0`, inspect file contexts with `ls -Z`, fix a wrong context with `restorecon`, toggle an SELinux boolean with `setsebool -P`, and review AppArmor profile status with `aa-status`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the security chapters in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the SELinux and AppArmor videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
