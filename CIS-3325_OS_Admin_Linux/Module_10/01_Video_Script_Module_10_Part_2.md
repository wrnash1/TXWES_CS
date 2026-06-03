# Video Script: Module 10 — Package Management and Software Installation (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Slide 1 — Welcome Back

Welcome back to Module 10. In Part 1 we covered the RHEL family: `rpm`, `yum`, `dnf`, and repository management.

In Part 2 we cover the Debian family with `dpkg` and `apt`, then move into compiling software from source, and finally walk through the exam-critical scenarios that tie everything together.

---

### Slide 2 — dpkg: The Low-Level Debian Tool

`dpkg` is the foundation of Debian package management. It handles individual `.deb` files without dependency resolution.

```bash
# Install a .deb package file
sudo dpkg -i package_name_1.0_amd64.deb

# Remove a package (keeps configuration files)
sudo dpkg -r package-name

# Remove a package AND its configuration files (purge)
sudo dpkg -P package-name
sudo dpkg --purge package-name

# Query installed packages
dpkg -l                          # List all installed packages
dpkg -l package-name             # Is this package installed?
dpkg -L package-name             # List all files installed by package
dpkg -S /path/to/file            # Which package owns this file?
dpkg -s package-name             # Show package status and info

# Reconfigure an installed package (re-run post-install questions)
sudo dpkg-reconfigure package-name
sudo dpkg-reconfigure tzdata     # Common use: change timezone

# Fix broken packages (often needed after dpkg errors)
sudo dpkg --configure -a

# Show packages in a broken state
dpkg --audit
```

---

### Slide 3 — APT: The High-Level Debian Tool

`apt` (Advanced Package Tool) provides dependency resolution, repository management, and a user-friendly interface over dpkg. `apt-get` and `apt-cache` are the older equivalents; `apt` is the modern unified tool.

```bash
# ALWAYS update the package index before installing
sudo apt update

# Install a package
sudo apt install nginx

# Install multiple packages
sudo apt install nginx postgresql php-fpm

# Remove a package (keeps config files)
sudo apt remove nginx

# Remove package AND config files (purge)
sudo apt purge nginx

# Remove auto-installed packages no longer needed
sudo apt autoremove
sudo apt autoremove --purge      # Also purge their configs

# Upgrade installed packages
sudo apt upgrade                  # Upgrade without removing packages
sudo apt full-upgrade             # Upgrade, removing packages if needed (dist-upgrade)

# Search for packages
apt search "web server"
apt-cache search nginx

# Get information about a package
apt show nginx
apt-cache show nginx

# List installed packages
dpkg -l
apt list --installed

# Check what packages have updates available
apt list --upgradable

# Download without installing (saves to current directory)
apt download nginx
```

---

### Slide 4 — APT Repository Management

APT repositories are configured in two locations:

- `/etc/apt/sources.list` — main repository list
- `/etc/apt/sources.list.d/` — drop-in repository files (modern approach)

```bash
# View current repositories
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Format of sources.list entries:
# deb [options] URI Suite Component1 Component2 ...
# deb https://deb.debian.org/debian bookworm main contrib non-free

# Components:
# main    — officially supported, open source
# contrib — open source, depends on non-free
# non-free — not open source
# security — security updates
# updates  — non-security updates

# Ubuntu sources.list example:
# deb http://archive.ubuntu.com/ubuntu jammy main restricted
# deb http://archive.ubuntu.com/ubuntu jammy-updates main restricted
# deb http://security.ubuntu.com/ubuntu jammy-security main restricted

# Add a repository using add-apt-repository (Ubuntu/Debian with apt tool)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Add a repository manually
echo "deb https://example.com/apt stable main" | sudo tee /etc/apt/sources.list.d/myrepo.list
sudo apt update

# Add a GPG key for a repository
curl -fsSL https://example.com/gpg-key.asc | sudo gpg --dearmor -o /etc/apt/keyrings/myrepo.gpg

# Modern DEB822 format (Ubuntu 22.04+)
# /etc/apt/sources.list.d/myrepo.sources
# Types: deb
# URIs: https://example.com/apt
# Suites: stable
# Components: main
# Signed-By: /etc/apt/keyrings/myrepo.gpg

# Remove a repository
sudo add-apt-repository --remove ppa:deadsnakes/ppa
sudo rm /etc/apt/sources.list.d/myrepo.list
sudo apt update
```

---

### Slide 5 — APT Pinning and Preferences

APT pinning controls which repository a package is installed from and lets you hold packages at specific versions.

```bash
# Hold a package at current version (prevent upgrades)
sudo apt-mark hold nginx
sudo apt-mark showhold             # Show held packages
sudo apt-mark unhold nginx         # Release the hold

# Install a specific version
sudo apt install nginx=1.18.0-6ubuntu14

# Show all available versions of a package
apt-cache policy nginx
apt-cache madison nginx

# List files installed by a package
dpkg -L nginx

# Find which package provides a file
dpkg -S /usr/sbin/nginx
apt-file search /usr/sbin/nginx    # Searches even not-installed packages
# (requires: sudo apt install apt-file && sudo apt-file update)
```

---

### Slide 6 — Compiling Software from Source

Sometimes a package is not available in any repository — or you need a newer version, or custom compile-time options. Compiling from source is the solution.

The standard process for software using GNU Autotools:

```bash
# Step 1: Install build dependencies
# On RHEL:
sudo dnf groupinstall "Development Tools"
sudo dnf install gcc make

# On Debian/Ubuntu:
sudo apt install build-essential
sudo apt install libssl-dev libpcre3-dev zlib1g-dev    # Common deps

# Step 2: Download the source code
wget https://nginx.org/download/nginx-1.24.0.tar.gz
# or
curl -O https://nginx.org/download/nginx-1.24.0.tar.gz

# Step 3: Verify the download (check the checksum against the website)
sha256sum nginx-1.24.0.tar.gz

# Step 4: Extract the archive
tar xzf nginx-1.24.0.tar.gz
cd nginx-1.24.0/

# Step 5: Configure the build
# ./configure examines your system and generates a Makefile
./configure --prefix=/usr/local/nginx --with-http_ssl_module

# ./configure --help shows all available options
./configure --help | less

# Step 6: Compile
# 'make' reads the Makefile and compiles the source code
make
# Speed up with parallel jobs:
make -j$(nproc)    # Use all available CPU cores

# Step 7: Install
sudo make install

# Verify installation
/usr/local/nginx/sbin/nginx -v
```

---

### Slide 7 — Managing Source-Compiled Software

Software installed from source is not tracked by your package manager. This requires extra administrative care.

```bash
# Remove source-compiled software
# Check if the software provides an uninstall target
make uninstall

# Or manually remove the prefix directory
sudo rm -rf /usr/local/nginx

# Better approach: use checkinstall to create a .deb or .rpm
# This integrates the source-compiled software into the package manager
sudo apt install checkinstall       # Debian
# sudo dnf install checkinstall     # RHEL

# Replace 'sudo make install' with:
sudo checkinstall

# checkinstall creates a .deb (or .rpm) and installs it via dpkg
# Now you can track and remove it like any other package

# CMAKE-based software (common for modern C++ projects)
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install

# Meson/Ninja-based software (Python projects, GNOME apps)
meson setup builddir
cd builddir
ninja
sudo ninja install
```

---

### Slide 8 — Package Verification and Security

Package verification is a critical security practice, especially after a system compromise.

```bash
# RHEL family: verify all installed packages
sudo rpm -Va
# Output codes:
# S — file size differs
# M — mode (permissions/type) differs
# 5 — MD5 sum differs
# D — device major/minor differs
# L — symlink path changed
# U — user ownership differs
# G — group ownership differs
# T — modification time differs
# P — capabilities differ
# '.' — test passed

# Verify a specific package
sudo rpm -V httpd

# Example output showing a modified config:
# .M.......  c /etc/httpd/conf/httpd.conf
# (M = mode changed, c = config file — this may be expected)
# 5........ /usr/lib64/httpd/modules/mod_alias.so
# (5 = MD5 mismatch — this is suspicious for a binary)

# Debian family: debsums
sudo apt install debsums
sudo debsums nginx          # Verify nginx files
sudo debsums -c             # Show only changed files
sudo debsums -ca            # Check all packages, show changed

# Find packages with verification failures
sudo rpm -Va 2>/dev/null | grep -v "^..c"    # Exclude config file changes
```

---

### Slide 9 — Practical Exam Scenarios

Let's run through high-frequency Linux+ exam scenarios.

**Scenario 1: Which package provides a specific file?**

```bash
# RHEL — which package owns /usr/bin/vim?
rpm -qf /usr/bin/vim
# Or if not installed:
dnf provides /usr/bin/vim

# Debian — which package owns /usr/bin/vim?
dpkg -S /usr/bin/vim
# Or if not installed:
apt-file search /usr/bin/vim
```

**Scenario 2: List all files installed by a package**

```bash
# RHEL
rpm -ql httpd

# Debian
dpkg -L nginx
```

**Scenario 3: Undo a bad package installation**

```bash
# RHEL — undo the last transaction
sudo dnf history undo last
# Or undo a specific transaction number
sudo dnf history undo 15

# Debian — there is no built-in undo; you must remove and reinstall
sudo apt remove newly-installed-package
sudo apt install previous-version=1.0.0-1
```

**Scenario 4: Fix a broken package installation**

```bash
# Debian — fix broken dependencies
sudo apt --fix-broken install
sudo dpkg --configure -a

# RHEL — reinstall a corrupted package
sudo dnf reinstall httpd
# Or repair the RPM database
sudo rpm --rebuilddb
```

---

### Slide 10 — CompTIA Linux+ Exam Tips

Critical facts for the exam:

```bash
# RHEL command reference:
rpm -qa          # list all installed
rpm -ql PKG      # list files in package
rpm -qf FILE     # which package owns file
rpm -qi PKG      # package info
rpm -V PKG       # verify integrity
dnf provides FILE  # which package provides file (not installed)
dnf history undo N # undo transaction

# Debian command reference:
dpkg -l          # list all installed
dpkg -L PKG      # list files in package
dpkg -S FILE     # which package owns file
dpkg -s PKG      # package status/info
apt update       # ALWAYS before apt install
apt --fix-broken install  # fix dependencies

# Configuration file locations:
# RHEL repos:    /etc/yum.repos.d/*.repo
# Debian repos:  /etc/apt/sources.list and /etc/apt/sources.list.d/
# RPM database:  /var/lib/rpm/
# dpkg database: /var/lib/dpkg/

# Source build sequence (on exam: configure → make → make install):
./configure
make
sudo make install
```

The exam will ask you to identify the correct command family (RPM vs. dpkg) and the correct flags. Know `rpm -qf` vs. `dpkg -S` — both find which package owns a file, but for different systems.

---

### Slide 11 — Module 10 Wrap-Up

You have now completed Module 10. You can:

- Install, remove, and query packages with `rpm` on RHEL-family systems
- Use `yum` and `dnf` for high-level package management with dependency resolution
- Manage RHEL repositories in `/etc/yum.repos.d/`
- Install, remove, and query packages with `dpkg` on Debian-family systems
- Use `apt` for high-level Debian package management
- Manage Debian repositories in `/etc/apt/sources.list` and `sources.list.d/`
- Compile software from source using the configure/make/install sequence
- Verify package integrity with `rpm -V` and `debsums`
- Apply GPG key verification for repository security

Complete the Reading Guide for a full command comparison table, then work through the Lab which covers both package families. The quiz tests both RPM and APT commands.

Excellent work completing Modules 7 through 10. You are building a solid foundation for the CompTIA Linux+ exam and for professional Linux administration.
