# Reading Guide: Module 10 — Package Management and Software Installation

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This reading guide provides comprehensive reference material for Linux package management across both major distribution families. It includes complete command tables, configuration file references, and the source compilation workflow. Use this as a study reference for the quiz and a practical reference during the lab.

**Estimated Reading Time:** 50–65 minutes

---

## Section 1 — Package Management Fundamentals

### 1.1 What Is a Package?

A Linux package is a compressed archive containing:

- Binary executables or libraries
- Configuration files
- Documentation
- Pre/post installation scripts (scriptlets)
- Metadata: name, version, architecture, dependencies, description, changelog

Packages solve the software distribution problem by bundling everything needed for a program into a single, verifiable, trackable unit.

### 1.2 Package Manager Architecture

Package managers have two layers:

**Low-level tools** (`rpm`, `dpkg`) handle individual package files:

- Install a specific `.rpm` or `.deb` file
- Query the local package database
- Verify installed files
- Do NOT resolve dependencies

**High-level tools** (`dnf`, `apt`) add repository management and dependency resolution:

- Connect to remote repositories
- Download packages and all their dependencies
- Resolve version conflicts
- Provide search, history, and rollback features

### 1.3 The Package Database

Both families maintain a local database of installed packages:

| Family | Database Location | Purpose |
|---|---|---|
| RHEL/RPM | `/var/lib/rpm/` | BerkeleyDB files tracking all installed RPM packages |
| Debian | `/var/lib/dpkg/status` | Text file listing all installed dpkg packages |
| Debian | `/var/cache/apt/` | Downloaded .deb files cache |
| RHEL | `/var/cache/dnf/` | Downloaded package and metadata cache |

---

## Section 2 — RPM Command Reference

### 2.1 rpm Installation Operations

```bash
# Install flags:
# -i = install
# -U = upgrade (installs if not present, upgrades if present)
# -F = freshen (only upgrades if already installed)
# -v = verbose
# -h = hash marks (progress)
# --nodeps = skip dependency check (dangerous)
# --force = force install even if conflicts
# --test = test installation without actually installing

sudo rpm -ivh package.rpm          # Install with verbose + progress
sudo rpm -Uvh package.rpm          # Upgrade (or install if not present)
sudo rpm -Fvh package.rpm          # Freshen only
sudo rpm -e package-name           # Erase/remove
sudo rpm --test -i package.rpm     # Dry run test
```

### 2.2 rpm Query Operations

```bash
# Query syntax: rpm -q[options] [package-name or file]

rpm -q httpd                       # Installed? Shows version if yes
rpm -qa                            # All installed packages
rpm -qa | grep http                # Filter installed list
rpm -qi httpd                      # Detailed package info
rpm -ql httpd                      # Files installed by httpd
rpm -qd httpd                      # Documentation files
rpm -qc httpd                      # Configuration files
rpm -qR httpd                      # Dependencies (Requires)
rpm -q --changelog httpd           # Changelog

rpm -qf /etc/httpd/conf/httpd.conf # Which package owns this file?
rpm -qf /usr/bin/vim

# Query uninstalled .rpm FILE (add 'p' flag)
rpm -qip package.rpm               # Info from file
rpm -qlp package.rpm               # Files in package file
rpm -qRp package.rpm               # Dependencies in package file
```

### 2.3 rpm Verification

```bash
rpm -V httpd               # Verify one package
rpm -Va                    # Verify all packages (slow)
rpm -Vf /path/to/file      # Verify package owning this file

# Output format: 8-char code + type + path
# Code characters: S M 5 D L U G T P
# S = size, M = mode/permissions, 5 = MD5, D = device
# L = symlink, U = user, G = group, T = mtime, P = capabilities
# '.' = attribute OK, '?' = attribute could not be checked

# File type codes:
# c = config, d = documentation, g = ghost
# l = license, r = readme

# Example: binary modified (security concern)
# S.5....T  /usr/bin/httpd
# (size, md5, and mtime differ — suspicious)

# Example: config file changed (expected)
# .M.......  c /etc/httpd/conf/httpd.conf
# (mode changed on config file — may be expected)
```

---

## Section 3 — DNF/YUM Command Reference

### 3.1 Installation and Removal

```bash
# Install
sudo dnf install PACKAGE
sudo dnf install PACKAGE-version    # Specific version
sudo dnf install /path/to/file.rpm  # Local RPM via dnf
sudo dnf install https://url/package.rpm  # Remote RPM

# Remove
sudo dnf remove PACKAGE
sudo dnf autoremove                 # Remove unneeded dependencies

# Reinstall (fix corrupted package)
sudo dnf reinstall PACKAGE

# Downgrade
sudo dnf downgrade PACKAGE

# Update
sudo dnf update PACKAGE             # Update specific package
sudo dnf update                     # Update all packages
sudo dnf upgrade                    # Update + remove obsoletes
sudo dnf update --exclude=PATTERN   # Exclude packages from update
```

### 3.2 Querying and Searching

```bash
dnf search KEYWORD              # Search names and summaries
dnf search all KEYWORD         # Search all metadata
dnf info PACKAGE               # Detailed package information
dnf list installed             # All installed packages
dnf list available             # All available packages
dnf list PACKAGE               # Info for specific package
dnf provides /usr/bin/file     # Find package providing a file
dnf provides "*/httpd.conf"    # Glob pattern search
dnf repoquery --requires PKG   # What does PKG depend on?
dnf repoquery --provides PKG   # What does PKG provide?
dnf repoquery --dependson PKG  # What packages need PKG?
dnf repoquery -l PKG           # Files in PKG (not installed)
```

### 3.3 History and Rollback

```bash
dnf history                    # List all transactions
dnf history info 5             # Details of transaction 5
dnf history info last          # Details of last transaction
dnf history undo 5             # Undo transaction 5
dnf history undo last          # Undo last transaction
dnf history rollback 3         # Rollback to state at transaction 3
dnf history userinstalled      # Packages explicitly installed by users
```

### 3.4 Repository Operations

```bash
dnf repolist                   # List enabled repos
dnf repolist all               # List all repos (enabled + disabled)
dnf repoinfo REPO_ID           # Info about a specific repo
dnf config-manager --add-repo URL     # Add a repo
dnf config-manager --enable REPO_ID  # Enable a disabled repo
dnf config-manager --disable REPO_ID # Disable a repo
dnf clean all                  # Clean all caches
dnf makecache                  # Rebuild metadata cache
```

---

## Section 4 — Repository Configuration (RHEL Family)

### 4.1 Repo File Format

Repository files live in `/etc/yum.repos.d/` with a `.repo` extension:

```ini
[repo-id]
name=Descriptive Name
baseurl=https://mirror.example.com/repo/$releasever/x86_64/
mirrorlist=https://mirrorlist.example.com/?repo=epel-$releasever
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-9
skip_if_unavailable=0
priority=50
```

Key fields:

| Field | Purpose |
|---|---|
| `[repo-id]` | Unique identifier; used with `--enablerepo=` |
| `baseurl` | Direct URL to repository |
| `mirrorlist` | URL returning list of mirrors |
| `enabled` | 1=enabled, 0=disabled |
| `gpgcheck` | 1=verify signatures (ALWAYS keep 1) |
| `gpgkey` | URL or path to GPG public key |
| `priority` | Lower number = higher priority (with priorities plugin) |

### 4.2 Variable Substitution in Repo Files

| Variable | Expands To |
|---|---|
| `$releasever` | Distribution major version (e.g., `9`) |
| `$basearch` | System architecture (e.g., `x86_64`) |
| `$arch` | Full architecture string |
| `$YUM0–$YUM9` | Custom variables from `/etc/yum/vars/` |

---

## Section 5 — dpkg and APT Command Reference

### 5.1 dpkg Operations

```bash
# Install
sudo dpkg -i package.deb
sudo dpkg --install package.deb

# Remove (keeps config)
sudo dpkg -r package-name
sudo dpkg --remove package-name

# Purge (removes config too)
sudo dpkg -P package-name
sudo dpkg --purge package-name

# Reconfigure
sudo dpkg-reconfigure package-name

# Fix broken installs
sudo dpkg --configure -a

# Query
dpkg -l                    # List all (status + version + description)
dpkg -l package-name       # Status of specific package
dpkg -L package-name       # Files installed by package
dpkg -S /path/to/file      # Package owning a file
dpkg -s package-name       # Detailed status
dpkg --get-selections      # All installed (for export)
dpkg --set-selections < file  # Import package selections

# dpkg -l status codes (first two characters):
# ii = installed, properly
# un = not installed
# rc = removed, config remains
# iU = installed, unpacked but not configured
```

### 5.2 APT Operations

```bash
# Always update index before installing
sudo apt update

# Install
sudo apt install PACKAGE
sudo apt install PACKAGE=VERSION    # Specific version
sudo apt install -y PACKAGE        # Auto-yes (for scripts)
sudo apt install --no-install-recommends PACKAGE   # Skip recommended pkgs

# Remove
sudo apt remove PACKAGE            # Remove, keep config
sudo apt purge PACKAGE             # Remove with config
sudo apt autoremove                # Remove unused dependencies
sudo apt autoremove --purge        # Also remove configs

# Upgrade
sudo apt upgrade                   # Safe upgrade (no package removal)
sudo apt full-upgrade              # Full upgrade (may remove packages)
sudo apt dist-upgrade              # Alias for full-upgrade

# Fix broken dependencies
sudo apt --fix-broken install
sudo apt -f install                # Old syntax, same result

# Hold/unhold
sudo apt-mark hold PACKAGE
sudo apt-mark unhold PACKAGE
sudo apt-mark showhold

# Search
apt search KEYWORD
apt-cache search KEYWORD

# Information
apt show PACKAGE
apt-cache show PACKAGE
apt-cache policy PACKAGE           # Shows available versions + sources
apt-cache depends PACKAGE          # Show dependencies
apt-cache rdepends PACKAGE        # Show reverse dependencies

# List
apt list --installed
apt list --upgradable
apt list PACKAGE                   # Info for specific package
```

---

## Section 6 — Repository Configuration (Debian Family)

### 6.1 sources.list Format

```
# Classic single-line format:
# deb [options] URI SUITE COMPONENT...
deb http://archive.ubuntu.com/ubuntu jammy main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu jammy-updates main restricted
deb http://security.ubuntu.com/ubuntu jammy-security main restricted

# Components:
# main       — officially supported, free software
# restricted — officially supported, non-free drivers
# universe   — community maintained, free software
# multiverse — not free software
```

### 6.2 Adding Repositories Safely

```bash
# Modern recommended approach (Ubuntu 22.04+):
# 1. Add the GPG key to the keyring
curl -fsSL https://example.com/key.asc | \
  sudo gpg --dearmor -o /etc/apt/keyrings/example.gpg

# 2. Add the repository with Signed-By pointing to the key
echo "deb [signed-by=/etc/apt/keyrings/example.gpg] https://example.com/apt stable main" | \
  sudo tee /etc/apt/sources.list.d/example.list

# 3. Update and install
sudo apt update
sudo apt install example-package

# Legacy approach (still works):
# wget -qO - https://example.com/key.asc | sudo apt-key add -
# Note: apt-key is deprecated; use the keyring approach above
```

---

## Section 7 — Command Comparison Table

This table is essential for the exam. Know the equivalent commands for each family:

| Task | RPM/DNF (RHEL) | dpkg/APT (Debian) |
|---|---|---|
| Install package file | `rpm -ivh pkg.rpm` | `dpkg -i pkg.deb` |
| Install from repo | `dnf install PKG` | `apt install PKG` |
| Remove package | `dnf remove PKG` | `apt remove PKG` |
| Remove + config | N/A (RPM keeps configs) | `apt purge PKG` |
| Update all | `dnf update` | `apt update && apt upgrade` |
| List all installed | `rpm -qa` | `dpkg -l` |
| List files in pkg | `rpm -ql PKG` | `dpkg -L PKG` |
| Package owning file | `rpm -qf FILE` | `dpkg -S FILE` |
| Find pkg for file | `dnf provides FILE` | `apt-file search FILE` |
| Package info | `rpm -qi PKG` | `dpkg -s PKG` |
| Package deps | `dnf repoquery --requires PKG` | `apt-cache depends PKG` |
| Verify integrity | `rpm -V PKG` | `debsums PKG` |
| Fix broken | `dnf reinstall PKG` | `apt --fix-broken install` |
| Undo transaction | `dnf history undo N` | (no equivalent) |
| Update index | `dnf makecache` | `apt update` |
| Clean cache | `dnf clean all` | `apt clean` |

---

## Section 8 — Compiling from Source

### 8.1 GNU Autotools Workflow

```bash
# Step 1: Install build tools
# RHEL:   sudo dnf groupinstall "Development Tools"
# Debian: sudo apt install build-essential

# Step 2: Install library dependencies
# Check configure output for missing deps
# RHEL: sudo dnf install libssl-devel
# Debian: sudo apt install libssl-dev

# Step 3: Get source
wget https://example.com/software-1.0.tar.gz
tar xzf software-1.0.tar.gz
cd software-1.0/

# Step 4: Configure
./configure --prefix=/usr/local     # Standard prefix
./configure --help                  # See all options

# Step 5: Build
make                                # Single-threaded
make -j4                            # 4 parallel jobs
make -j$(nproc)                     # Auto-detect CPUs

# Step 6: Test (if available)
make check
make test

# Step 7: Install
sudo make install

# Step 8: Verify
ls /usr/local/bin/
/usr/local/bin/myprogram --version
```

### 8.2 Using checkinstall

`checkinstall` wraps `make install` and creates a proper package, allowing package manager tracking:

```bash
sudo apt install checkinstall       # Debian
sudo dnf install checkinstall       # RHEL

# Instead of 'sudo make install', run:
sudo checkinstall

# checkinstall will ask for:
# - Package description
# - Version number
# - Package maintainer
# Then it creates and installs a .deb (or .rpm) file

# You can now track and remove it like any package:
dpkg -l my-custom-package
sudo apt remove my-custom-package
```

---

## Section 9 — Package Security Best Practices

### 9.1 Keeping Systems Updated

```bash
# Set up automatic security updates (Ubuntu)
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades
# Config: /etc/apt/apt.conf.d/50unattended-upgrades

# Set up automatic updates (RHEL)
sudo dnf install dnf-automatic
sudo systemctl enable --now dnf-automatic.timer
# Config: /etc/dnf/automatic.conf

# Manual security-only updates (RHEL)
sudo dnf update --security
sudo dnf updateinfo list security

# Manual security-only updates (Debian)
sudo apt update
sudo apt upgrade -s | grep "^Inst"    # Show what would be upgraded
```

### 9.2 Package Verification in Incident Response

When you suspect a system compromise, verify package integrity:

```bash
# RHEL: Find modified system binaries
sudo rpm -Va | grep "^..5"     # MD5 mismatch (binary modified?)
sudo rpm -Va | grep -v "^..c"  # Ignore config file changes

# Debian:
sudo debsums -c 2>/dev/null    # Show only changed files

# Check recently modified files
find /usr /bin /sbin -newer /var/log/dpkg.log -type f 2>/dev/null
find /usr /bin /sbin -newer /var/lib/rpm/rpmdb.sqlite -type f 2>/dev/null

# Compare against known-good checksums from another system
# or from the original package files
```

---

## Section 10 — Key Terms Glossary

| Term | Definition |
|---|---|
| RPM | RPM Package Manager — package format and low-level tool for RHEL family |
| DNF | Dandified YUM — modern high-level package manager for RHEL 8+ |
| dpkg | Debian Package — low-level package tool for Debian family |
| APT | Advanced Package Tool — high-level package manager for Debian family |
| dependency | Software required by a package to function |
| dependency resolution | Automatic identification and installation of required packages |
| repository | Server hosting packages for a distribution |
| `.repo` file | Repository configuration file for RHEL family (in /etc/yum.repos.d/) |
| `sources.list` | Repository configuration file for Debian family |
| GPG | GNU Privacy Guard — used to sign packages for authenticity verification |
| `checkinstall` | Tool to create packages from source-compiled software |
| `make` | Build tool that reads Makefiles to compile source code |
| `./configure` | Script that examines system and generates a Makefile |
| autoremove | Remove packages installed as dependencies but no longer needed |
| purge | Remove package and its configuration files |

---

## Section 11 — Review Questions

1. What is the difference between `rpm -i` and `rpm -U`?

2. Which command would you use to find which RPM package provides the file `/usr/bin/python3`?

3. What does `rpm -V httpd` output, and what does each character in the result code mean?

4. On a Debian system, what is the difference between `apt remove` and `apt purge`?

5. Why must you always run `sudo apt update` before `sudo apt install`?

6. Where are RHEL repository configuration files stored?

7. What are the steps to compile software from source using GNU Autotools?

8. What is `checkinstall` and why is it preferable to `sudo make install`?

9. What command shows the transaction history and allows you to undo a package installation on a RHEL system?

10. What security risk is created by setting `gpgcheck=0` in a repository configuration file?

---

## 9. Supplemental Resources

**1. [DNF Command Reference — Red Hat Documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_software_with_the_dnf_tool/index)**
Red Hat's official DNF documentation for RHEL 9. Covers all major dnf operations: installing, removing, upgrading, searching, repository management, history and rollback, modules, and configuration options in `/etc/dnf/dnf.conf`. Directly maps to the RHEL portions of the Module 10 lab and the CompTIA Linux+ exam objectives for package management.

**2. [Debian APT User's Guide](https://www.debian.org/doc/manuals/apt-guide/index.en.html)**
The official Debian APT documentation. Explains the relationship between dpkg, apt, apt-get, and apt-cache; covers sources.list format, GPG key management, preference pinning, and the difference between `remove` and `purge`. Essential reading for understanding the APT tool ecosystem at a conceptual level beyond just memorizing commands.

**3. [How to Install Software from Source on Linux — It's FOSS](https://itsfoss.com/install-software-from-source-code/)**
A practical walkthrough of the `./configure && make && sudo make install` workflow with clear explanations of what each step does, common configure flags like `--prefix`, and why `checkinstall` is recommended over bare `make install`. Includes troubleshooting for common build errors such as missing development libraries, which directly prepares students for the source compilation challenge in this module's lab.
