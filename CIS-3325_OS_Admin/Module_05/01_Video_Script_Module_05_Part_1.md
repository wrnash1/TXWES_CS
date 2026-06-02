# Video Script: Module 05 - Package Management (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 05. So far you can install Linux, navigate the filesystem, manage permissions,
and manage user accounts. Now let us talk about how you actually install software. Package
management is how Linux handles software installation, updates, and removal in a consistent,
dependency-aware, and verifiable way. This is tested throughout the Linux+ exam and is a daily
task in any Linux environment.

By the end of both parts you will understand the two major package ecosystems, the difference
between high-level and low-level package tools, how to query the package database, and how to
verify package integrity.

---

### Section 1: The Two Major Package Ecosystems

Linux distributions divide into two major package management ecosystems based on their package
format.

The Debian ecosystem uses the .deb package format. The Debian distribution created this system,
and Ubuntu inherited it. The high-level tool is apt (Advanced Package Tool). The low-level tool
is dpkg. This ecosystem powers Debian, Ubuntu, Linux Mint, and Kali Linux.

The Red Hat ecosystem uses the .rpm package format (Red Hat Package Manager). Red Hat Enterprise
Linux created this system. The high-level tool was originally yum (Yellowdog Updater Modified)
and is now dnf (Dandified YUM) on modern systems. The low-level tool is rpm. This ecosystem
powers RHEL, Fedora, CentOS Stream, Rocky Linux, and AlmaLinux.

The key difference between high-level and low-level tools:

High-level tools (apt, dnf) connect to repositories, download packages and their dependencies,
and install everything needed automatically.

Low-level tools (dpkg, rpm) work with local .deb or .rpm files you already have. They do not
resolve dependencies. If you install a .rpm file with rpm and it requires a library you do not
have, rpm tells you what is missing but does not fetch it.

For the exam: when a question says Ubuntu, use apt or dpkg. When it says RHEL or CentOS, use
dnf/yum or rpm. Mixing the tools is the most common wrong answer in this domain.

---

### Section 2: APT - The Debian/Ubuntu Package Manager

[SHOW TERMINAL]

The first thing you do before installing anything on a new Ubuntu server:

```bash
sudo apt update
```

apt update refreshes the local package metadata from repositories. It does NOT install or
upgrade anything. It just updates the list of available packages and their versions.

```bash
sudo apt upgrade
```

apt upgrade installs available updates for all currently installed packages. It does not
remove packages or install new ones.

```bash
sudo apt install nginx
```

Install a specific package. apt resolves all dependencies and downloads everything needed.

```bash
sudo apt install -y nginx
```

The -y flag automatically answers yes to confirmation prompts. Useful in scripts.

```bash
sudo apt remove nginx
```

Remove the package binary files. Configuration files in /etc/nginx/ remain. This is useful
if you plan to reinstall later with the same configuration.

```bash
sudo apt purge nginx
```

Remove the package AND all configuration files. This is a clean uninstall.

```bash
sudo apt autoremove
```

Remove automatically installed dependency packages that are no longer needed by any explicitly
installed package.

```bash
sudo apt search "web server"
```

Search for packages matching a description keyword.

```bash
apt show nginx
```

Display detailed information about a package including version, size, dependencies, and
description.

```bash
apt list --installed
```

List all currently installed packages.

---

### Section 3: Repository Configuration for APT

Repositories are the servers that host packages. When you run apt update, apt reads repository
definitions and fetches the latest package lists.

[SHOW TERMINAL]

```bash
cat /etc/apt/sources.list
```

This file lists the main repository sources. Each line has the format:
deb [options] repository-url distribution component

```bash
ls /etc/apt/sources.list.d/
```

Additional repository files go in this directory. Third-party repositories like Docker, GitHub
CLI, and Microsoft Teams add their own .list files here.

To add a third-party repository, you need two things: the repository URL and its GPG key.

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

This fetches and installs the Docker repository's GPG signing key.

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt update
```

After adding the repository and updating, Docker is available to install.

---

### Section 4: dpkg - The Low-Level Debian Tool

[SHOW TERMINAL]

```bash
dpkg -l
```

List all installed packages. Output shows status codes and package names.

```bash
dpkg -l | grep nginx
```

Filter the list for a specific package.

```bash
dpkg -L nginx
```

List all files installed by the nginx package. Shows every file the package put on your system.

```bash
dpkg -S /usr/sbin/nginx
```

Identify which package owns a specific file. Very useful when you find an unknown binary.

```bash
dpkg -s nginx
```

Show status information for an installed package.

```bash
dpkg -i /path/to/local.deb
```

Install a local .deb file directly. This does NOT automatically resolve dependencies.

```bash
dpkg -r nginx
```

Remove a package (leaves config files, equivalent to apt remove).

```bash
dpkg --purge nginx
```

Remove package and config files (equivalent to apt purge).

---

### Section 5: DNF - The Red Hat Package Manager

On RHEL 8+, CentOS Stream 8+, Fedora, Rocky Linux, and AlmaLinux:

[SHOW TERMINAL]

```bash
sudo dnf install nginx
```

Install a package with automatic dependency resolution.

```bash
sudo dnf remove nginx
```

Remove a package.

```bash
sudo dnf update
```

Update all installed packages.

```bash
sudo dnf update nginx
```

Update a specific package only.

```bash
sudo dnf search "web server"
```

Search for packages.

```bash
dnf info nginx
```

Show package information.

```bash
dnf list installed
```

List all installed packages.

```bash
dnf list available | grep nginx
```

Search available packages.

```bash
dnf history
```

Show package installation history. Useful for auditing what was installed and when.

```bash
dnf history undo 5
```

Undo transaction number 5. dnf keeps a transaction log allowing rollback.

---

### Section 6: Repository Configuration for DNF/YUM

[SHOW TERMINAL]

```bash
ls /etc/yum.repos.d/
```

Repository files for RHEL/CentOS systems live here.

```bash
cat /etc/yum.repos.d/redhat.repo
```

Each .repo file defines one or more repositories with URL, GPG key, and enabled status.

```bash
dnf repolist
```

List all configured repositories and their status.

```bash
dnf repolist all
```

Show all repositories including disabled ones.

To enable or disable a repository:

```bash
sudo dnf config-manager --enable epel
sudo dnf config-manager --disable optional
```

EPEL (Extra Packages for Enterprise Linux) is a commonly needed third-party repository for
RHEL that provides packages not in the official Red Hat repositories.

---

### Certification Connection

Package management maps to Linux+ Domain 1.0 (System Management). Key exam objectives:

Know apt commands for Ubuntu and dnf/rpm commands for RHEL.

Know the difference between apt remove (keeps config) and apt purge (removes config).

Know dpkg -S to find which package owns a file.

Know rpm -V for package integrity verification.

Know that high-level tools resolve dependencies but low-level tools do not.

---

### Transition to Part 2

In Part 2 we cover the rpm command in depth, package integrity verification, and the practical
exam scenarios that test cross-platform package management knowledge. Take a break and continue.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
