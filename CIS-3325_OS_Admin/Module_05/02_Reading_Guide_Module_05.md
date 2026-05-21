# Reading Guide: Module 05 - Package Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 05 – Package Management**! This week covers the tools Linux administrators use to install, update, remove, and verify software packages across the two major package ecosystems: Debian/Ubuntu (apt, dpkg) and Red Hat/CentOS/Fedora (dnf, yum, rpm). Package management is tested throughout the CompTIA Linux+ XK0-005 exam under Domain 1.0 (System Management).

As you work through this material you will learn how package managers resolve dependencies, how repositories are configured, and how to query the package database to verify what is installed on a system.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **APT (Advanced Package Tool)**: The high-level package manager for Debian-based distributions including Ubuntu. Common commands: `apt update` (refresh repo metadata), `apt upgrade` (upgrade all installed packages), `apt install packagename` (install), `apt remove packagename` (remove binaries), `apt purge packagename` (remove binaries and config files). Repository sources are defined in `/etc/apt/sources.list` and files under `/etc/apt/sources.list.d/`.
*   **dpkg**: The low-level Debian package tool that installs, removes, and queries `.deb` files directly without network access. Key flags: `dpkg -i package.deb` (install a local file), `dpkg -r packagename` (remove), `dpkg -l` (list all installed packages), `dpkg -L packagename` (list files installed by a package), `dpkg -S /path/to/file` (identify which package owns a file).
*   **DNF / YUM**: DNF (Dandified YUM) is the modern package manager for Red Hat-based distros (RHEL 8+, Fedora, CentOS Stream). YUM is its predecessor, still used on RHEL 7 and CentOS 7. Commands are nearly identical: `dnf install`, `dnf remove`, `dnf update`, `dnf search`, `dnf info`. Repository definitions are in `/etc/yum.repos.d/*.repo` files.
*   **RPM (Red Hat Package Manager)**: The low-level tool for `.rpm` files, analogous to `dpkg`. Key flags: `rpm -ivh package.rpm` (install with verbose output and hash progress), `rpm -e packagename` (erase/remove), `rpm -qa` (query all installed packages), `rpm -ql packagename` (list files), `rpm -qf /path/to/file` (identify owning package), `rpm -V packagename` (verify package integrity against the RPM database).
*   **Package Dependencies**: When you install a package, it may require other packages (libraries, utilities) to be present. High-level tools like apt and dnf resolve and install dependencies automatically. Low-level tools (dpkg, rpm) do not — installing with dpkg/rpm alone will fail with dependency errors that you must resolve manually.
*   **Repository**: A structured collection of packages hosted on a server, accessed over HTTP/HTTPS or FTP. Repositories carry GPG-signed metadata so the package manager can verify package authenticity. Adding a third-party repository typically requires importing its GPG key (`apt-key add` or `rpm --import`).

---

### 2. Certification Exam Tips
*   **Domain alignment:** Package management maps to Linux+ Domain 1.0 (System Management). Expect 4–6 questions requiring you to identify the correct tool and flags for a given distro.
*   **Know which tool belongs to which distro:** The exam presents a scenario set on Ubuntu and expects apt/dpkg commands, or set on RHEL/CentOS and expects dnf/rpm. Mixing them (e.g., using apt on CentOS) is a common wrong-answer trap.
*   **`rpm -V` is frequently tested:** This command verifies installed files against the RPM database and outputs codes like `S` (file size changed), `M` (permissions changed), `5` (MD5 checksum mismatch). It is the correct answer when a scenario asks how to detect tampering with installed software files.
*   **`apt purge` vs `apt remove`:** `remove` leaves configuration files behind (useful for reinstalling with previous settings). `purge` removes everything including config. The exam tests this distinction in scenarios about completely uninstalling software.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers package management concepts in chapter 14. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) demonstrates apt and dnf in live terminal sessions, showing real package installation and repository configuration workflows.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapter 14 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which covers package management across both Debian and Red Hat ecosystems.
*   **Required Video:** Watch the package management videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free playlist covering apt, dnf, and rpm in practical administrative scenarios.

---

### Lab & Command Integration
In this week's hands-on lab you will use `apt` to install and remove packages, query the dpkg database with `dpkg -l` and `dpkg -L`, add a third-party repository, and verify package integrity. You will also practice the equivalent RPM commands to understand how both ecosystems handle the same tasks.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapter 14 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the package management videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
