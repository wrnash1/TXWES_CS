# Video Script: Module 10 — Package Management and Software Installation (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome and Module Overview

Welcome to Module 10. I'm Professor Nash. Today we cover package management — how Linux systems install, update, remove, and verify software.

Understanding package management is essential for every Linux administrator. Whether you are deploying a new server, keeping systems patched and secure, or troubleshooting a broken dependency, package managers are your primary tool.

Linux+ exam objective 3.2 asks you to: given a scenario, install and manage software on a Linux system. This module covers both major family toolchains.

By the end of both parts, you will be able to work fluently with RPM, YUM, and DNF on RHEL-family systems; dpkg and APT on Debian-family systems; manage repositories; verify package integrity; and compile software from source.

---

### Slide 2 — Why Package Management Matters

Before Linux had sophisticated package managers, installing software meant:

1. Downloading a source tarball
2. Installing its dependencies manually — one by one
3. Compiling from source
4. Copying files to the right locations
5. Never knowing exactly what was installed or where

"Dependency hell" was real — software A requires library version 1.2, but software B requires version 1.5, and they cannot coexist.

Modern package managers solve this:

- **Dependency resolution** — automatically installs everything a package needs
- **Central repositories** — one place to find all software, curated by the distribution
- **Verification** — cryptographic signatures confirm packages are authentic
- **Transaction tracking** — the system knows exactly what is installed
- **Reproducibility** — the same command gives the same result on every machine

---

### Slide 3 — The Two Major Package Family Trees

Linux distributions split into two major families for package management:

**RHEL Family (Red Hat Package Manager)**

- Distributions: RHEL, CentOS, Rocky Linux, AlmaLinux, Fedora, Oracle Linux, Amazon Linux 2
- Low-level tool: `rpm` (RPM Package Manager)
- High-level tools: `yum` (older) → `dnf` (modern; default on RHEL 8+)
- Package format: `.rpm` files
- Database: RPM database at `/var/lib/rpm/`

**Debian Family**

- Distributions: Debian, Ubuntu, Linux Mint, Kali Linux, Raspberry Pi OS
- Low-level tool: `dpkg` (Debian Package)
- High-level tool: `apt` (Advanced Package Tool) — also `apt-get`, `apt-cache`
- Package format: `.deb` files
- Database: dpkg status at `/var/lib/dpkg/`

The exam tests both families. Know at least the basic commands for each.

---

### Slide 4 — RPM: The Low-Level Tool

`rpm` is the foundation of RHEL-family package management. It manages individual `.rpm` files — installing, querying, and removing packages without automatic dependency resolution.

```bash
# Install an RPM package file
sudo rpm -ivh package-name-1.0-1.x86_64.rpm
# -i = install, -v = verbose, -h = progress hash marks

# Upgrade a package (install new, remove old)
sudo rpm -Uvh package-name-2.0-1.x86_64.rpm

# Remove (erase) a package
sudo rpm -e package-name

# Query installed packages
rpm -q package-name              # Is this package installed?
rpm -qa                          # List ALL installed packages
rpm -qi package-name             # Detailed info about installed package
rpm -ql package-name             # List all files installed by package
rpm -qf /path/to/file            # Which package owns this file?
rpm -qd package-name             # List documentation files
rpm -qc package-name             # List configuration files

# Query a package FILE (not installed)
rpm -qip package-file.rpm        # Info from .rpm file
rpm -qlp package-file.rpm        # Files in .rpm file

# Verify installed packages (checks file integrity)
rpm -V package-name
rpm -Va                          # Verify ALL installed packages
```

The `-V` output shows codes for what changed: `S` = file size, `M` = mode, `5` = MD5 checksum, `T` = modification time. An empty output means the package is intact.

---

### Slide 5 — YUM: The High-Level RHEL Tool (Legacy)

`yum` (Yellowdog Updater Modified) was the standard high-level package manager for RHEL 5, 6, and 7. It handles dependency resolution automatically using configured repositories.

```bash
# Install a package
sudo yum install httpd

# Install multiple packages
sudo yum install httpd mariadb-server php

# Remove a package
sudo yum remove httpd

# Update a specific package
sudo yum update httpd

# Update ALL packages (including kernel)
sudo yum update

# Update all packages except the kernel
sudo yum update --exclude=kernel*

# Search for packages
yum search "web server"
yum search httpd

# Get information about a package
yum info httpd

# List installed packages
yum list installed

# List available packages
yum list available

# Check for available updates
yum check-update

# View yum transaction history
sudo yum history
sudo yum history info 5    # Details of transaction #5
sudo yum history undo 5    # Undo transaction #5
```

---

### Slide 6 — DNF: The Modern RHEL Tool

`dnf` (Dandified YUM) replaced `yum` as the default in RHEL 8, Fedora 22+, and is now the standard. The syntax is nearly identical to `yum`, making migration easy.

```bash
# DNF commands mirror YUM closely
sudo dnf install nginx
sudo dnf remove nginx
sudo dnf update
sudo dnf update --exclude=kernel*

# DNF-specific improvements
sudo dnf upgrade                  # Same as update but also removes obsoletes
sudo dnf reinstall httpd         # Reinstall a package
sudo dnf downgrade httpd         # Downgrade to previous version
sudo dnf autoremove              # Remove unused dependencies

# Enhanced search and info
dnf search nginx
dnf info nginx
dnf provides /usr/bin/python3    # Which package provides a file?
dnf repoquery --requires httpd   # What does httpd depend on?
dnf repoquery --dependson httpd  # What depends on httpd?

# History (more detailed than yum)
dnf history
dnf history info 10
dnf history undo 10
dnf history rollback 5           # Rollback to state before transaction 5

# Module streams (RHEL 8+ application streams)
dnf module list
dnf module enable nodejs:16
dnf module install nodejs:16/development
```

---

### Slide 7 — Repository Management (RHEL Family)

Repositories are the servers that host packages. DNF/YUM repositories are configured in `/etc/yum.repos.d/` as `.repo` files.

```bash
# List all configured repositories
dnf repolist
dnf repolist all            # Include disabled repos
yum repolist

# View repository details
dnf repoinfo baseos

# Repository file format
cat /etc/yum.repos.d/redhat.repo
# [BaseOS]
# name=Red Hat Enterprise Linux BaseOS
# baseurl=https://cdn.redhat.com/content/dist/rhel9/...
# enabled=1
# gpgcheck=1
# gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

# Add a repository (EPEL — Extra Packages for Enterprise Linux)
sudo dnf install epel-release
# or manually:
sudo dnf config-manager --add-repo https://example.com/myrepo.repo

# Enable/disable a repository temporarily
sudo dnf install --enablerepo=epel package-name
sudo dnf install --disablerepo=* --enablerepo=baseos package-name

# Enable/disable permanently
sudo dnf config-manager --enable epel
sudo dnf config-manager --disable epel

# Clean the package cache
sudo dnf clean all
sudo dnf makecache           # Rebuild metadata cache
```

---

### Slide 8 — Package Groups (RHEL Family)

Package groups let you install collections of related packages with a single command.

```bash
# List available groups
dnf group list
dnf group list --hidden      # Show all groups including minimal ones

# Get info about a group
dnf group info "Development Tools"

# Install a group
sudo dnf group install "Development Tools"
sudo dnf group install --with-optional "Server with GUI"

# Remove a group
sudo dnf group remove "Development Tools"

# Update all packages in a group
sudo dnf group upgrade "Development Tools"

# Common useful groups:
# "Development Tools"     — gcc, make, git, etc.
# "Server with GUI"       — GNOME desktop for servers
# "Minimal Install"       — smallest possible system
```

---

### Slide 9 — GPG Key Verification

Package managers use GPG (GNU Privacy Guard) digital signatures to verify that packages come from the distribution's signing key and have not been tampered with.

```bash
# Import a GPG key for a repository
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

# Import a GPG key from URL
sudo rpm --import https://example.com/RPM-GPG-KEY

# List imported GPG keys
rpm -qa gpg-pubkey*
rpm -qi gpg-pubkey-fd431d51-4ae0493b    # Details of a specific key

# Verify a downloaded RPM file's signature
rpm --checksig package.rpm
rpm -K package.rpm

# Check if gpgcheck is enabled in your repo config
grep gpgcheck /etc/yum.repos.d/*.repo

# NEVER disable gpgcheck in production:
# gpgcheck=0    <- This allows unsigned packages — INSECURE
```

GPG verification is a critical security control. A repository with `gpgcheck=0` or `gpgkey=` left blank means you are installing packages without verifying their authenticity — a significant attack vector.

---

### Slide 10 — Module 10 Part 1 Summary

In Part 1 we covered the RHEL family package management toolchain:

- Why package management is critical for reliability and security
- The RHEL vs. Debian family distinction
- `rpm` — low-level tool for querying, installing, and verifying `.rpm` files
- `yum` — legacy high-level tool with repository support
- `dnf` — modern replacement for yum with enhanced features
- Repository configuration in `/etc/yum.repos.d/`
- Package group installation
- GPG key verification for package integrity

In Part 2 we will cover the Debian/APT toolchain, compiling from source, and the key exam-focused scenarios that combine both families.

See you in Part 2.
