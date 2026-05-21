# Reading Guide: Module 04 - User and Group Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 04 – User and Group Management**! This week covers the commands and configuration files used to create, modify, and delete user accounts and groups on a Linux system. Identity management is a core topic on the CompTIA Linux+ XK0-005 exam under Domain 2.0 (Security) and Domain 1.0 (System Management).

As you work through this material you will learn how Linux stores user identity in flat files, how to manage accounts with `useradd`, `usermod`, and `userdel`, and how group membership controls shared resource access.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **`/etc/passwd`**: A colon-delimited file with one record per user account containing seven fields: username, password placeholder (x), UID, GID, GECOS comment, home directory, and login shell. It is world-readable so that programs can resolve usernames. Actual password hashes are stored in `/etc/shadow`, readable only by root.
*   **`/etc/shadow`**: Stores securely hashed passwords and password aging policy for each local user. Fields include the hashed password, last-changed date (days since epoch), minimum and maximum days between changes, and account expiration date. Only root can read this file.
*   **`useradd` vs `adduser`**: `useradd` is the low-level binary available on all Linux distros; it requires explicit flags to set options (e.g., `useradd -m -s /bin/bash -G sudo alice`). `adduser` is a higher-level Perl or shell wrapper available on Debian/Ubuntu that prompts interactively and creates the home directory by default. The exam tests `useradd` flags: `-m` (create home), `-d` (specify home path), `-s` (shell), `-G` (supplementary groups), `-e` (expiry date).
*   **`usermod`**: Modifies an existing user account. Common flags: `-aG groupname username` (append user to a supplementary group without removing them from existing groups — omitting `-a` will replace all supplementary groups), `-L` (lock account), `-U` (unlock account), `-s` (change shell).
*   **`groupadd` / `groupmod` / `groupdel`**: Create, modify, and delete groups. Group definitions are stored in `/etc/group` (colon-delimited: groupname:password:GID:member-list) and `/etc/gshadow`. Every user has a primary group (set in `/etc/passwd`) and may belong to multiple supplementary groups.
*   **`/etc/sudoers` and `visudo`**: Controls which users and groups can run commands as root via `sudo`. Always edit with `visudo`, which validates syntax before saving — a syntax error in `/etc/sudoers` can lock all administrators out. The `%sudo` or `%wheel` group entry grants sudo to all members; individual user entries follow the format `alice ALL=(ALL:ALL) ALL`.

---

### 2. Certification Exam Tips
*   **Domain alignment:** User and group management maps to Linux+ Domain 2.0 (Security) and Domain 1.0 (System Management). Expect scenario questions about creating users with specific shells, locking accounts, and group membership.
*   **`-aG` trap:** The most commonly missed exam question in this area: `usermod -G sudo alice` replaces all of alice's supplementary groups with only `sudo`. The correct command to *add* alice to `sudo` while keeping her other groups is `usermod -aG sudo alice`. Memorize the `-a` flag.
*   **UID ranges:** UID 0 = root. UIDs 1–999 (or 1–499 on older RHEL) = system accounts. UIDs 1000+ = regular users. The exam tests whether you know why a service account should have a low UID and no login shell.
*   **`/etc/skel`**: When `useradd -m` creates a home directory, it copies template files from `/etc/skel`. Add dotfiles there to standardize new user environments. This is tested in scenario questions about deploying consistent shell configurations.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers user management and permissions in chapters 9–10. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) demonstrates `useradd`, `usermod`, `passwd`, and sudo configuration in practical video sessions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapters 9–10 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which cover user identity, permissions, and process ownership in the context of Linux security.
*   **Required Video:** Watch the user and group management videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free playlist that demonstrates account creation, group membership, and sudo configuration in a live environment.

---

### Lab & Command Integration
In this week's hands-on lab you will create user accounts with `useradd`, set passwords with `passwd`, add users to groups with `usermod -aG`, verify membership with `id` and `groups`, lock and unlock accounts, and configure a sudo entry using `visudo`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapters 9–10 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the user management videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
