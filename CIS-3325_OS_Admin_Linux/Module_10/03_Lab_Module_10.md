# Lab: Module 10 — Package Management and Software Installation

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Lab Overview

In this lab you will work with both the RHEL/RPM and Debian/APT package management toolchains, explore repository configuration, compile a simple program from source, and practice package verification. Tasks are organized so Ubuntu/Debian users complete the APT sections, RHEL/Rocky/Fedora users complete the DNF sections, and both groups complete the source compilation and verification sections.

**Estimated Time:** 75–100 minutes

**Required Environment:** Linux VM — either Ubuntu 22.04 LTS or Rocky Linux 9 / RHEL 9 (or equivalent). If you have both distributions available, work through both sections.

---

## Prerequisites

- Completion of Module 10 video lectures (Parts 1 and 2)
- A running Linux VM with sudo access and internet connectivity
- Basic terminal proficiency from previous modules

---

## Task 1 — Explore the Current Package State

### Step 1.1 — Count and List Installed Packages

**On RHEL/Rocky/Fedora:**

```bash
# Count installed packages
rpm -qa | wc -l

# List the 10 most recently installed packages
rpm -qa --last | head -10

# Show what groups are installed
dnf group list --installed
```

**On Ubuntu/Debian:**

```bash
# Count installed packages
dpkg -l | grep "^ii" | wc -l

# List packages installed in the last 24 hours
grep " install " /var/log/dpkg.log | tail -20

# Show packages that have updates available
apt list --upgradable 2>/dev/null
```

**Lab Question 1:** How many packages are installed on your system? What are the last 5 packages that were installed?

### Step 1.2 — Query a Specific Package

**On RHEL/Rocky:**

```bash
# Query the openssh-server package
rpm -qi openssh-server
rpm -ql openssh-server | head -20
rpm -qd openssh-server
rpm -qc openssh-server
```

**On Ubuntu:**

```bash
dpkg -s openssh-server
dpkg -L openssh-server | head -20
```

---

## Task 2 — Find Package Ownership

### Step 2.1 — Which Package Owns a File?

**On RHEL/Rocky:**

```bash
# Find which package owns the ssh command
rpm -qf /usr/bin/ssh

# Find which package owns the sudoers file
rpm -qf /etc/sudoers

# Find which package owns the bash binary
rpm -qf /bin/bash

# Find which package would provide something not installed
dnf provides "*/htpasswd"
```

**On Ubuntu:**

```bash
dpkg -S /usr/bin/ssh
dpkg -S /etc/sudoers
dpkg -S /bin/bash

# Find which package provides a file not yet installed
# (requires apt-file)
sudo apt install apt-file -y
sudo apt-file update
apt-file search htpasswd
```

**Lab Question 2:** On your system, which package owns the `sudo` binary (`/usr/bin/sudo`)? Record the full package name including version.

---

## Task 3 — Install and Remove Packages

### Step 3.1 — Install a Package

**On RHEL/Rocky:**

```bash
# Install tree (directory visualization tool)
sudo dnf install tree -y

# Verify it installed
rpm -qi tree
tree /etc/skel
```

**On Ubuntu:**

```bash
sudo apt update
sudo apt install tree -y

dpkg -s tree
tree /etc/skel
```

### Step 3.2 — Install a Package Group (RHEL Only)

```bash
# See if "Development Tools" is installed
dnf group list --installed | grep "Development Tools"

# Get info about it
dnf group info "Development Tools"

# Install it if not present
sudo dnf group install "Development Tools" -y

# Verify gcc is now available
gcc --version
make --version
```

**On Ubuntu:**

```bash
# Ubuntu equivalent
sudo apt install build-essential -y
gcc --version
make --version
```

### Step 3.3 — Remove a Package

**On RHEL/Rocky:**

```bash
# Remove the 'tree' package
sudo dnf remove tree -y

# Verify removal
rpm -q tree
echo "Exit code: $?"
```

**On Ubuntu:**

```bash
sudo apt remove tree -y
dpkg -l tree
echo "Exit code: $?"
```

---

## Task 4 — Repository Management

### Step 4.1 — List Configured Repositories

**On RHEL/Rocky:**

```bash
# List enabled repositories
dnf repolist

# List all repositories including disabled
dnf repolist all

# Show details for a specific repo
dnf repoinfo baseos

# View a repo configuration file
ls /etc/yum.repos.d/
cat /etc/yum.repos.d/rocky.repo 2>/dev/null || cat /etc/yum.repos.d/redhat.repo 2>/dev/null
```

**On Ubuntu:**

```bash
# List configured sources
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# List all repositories (requires apt-show-versions or similar)
apt-cache policy
```

### Step 4.2 — Add and Enable EPEL (RHEL Only)

```bash
# Install EPEL release package (provides access to Extra Packages)
sudo dnf install epel-release -y

# Verify EPEL is now available
dnf repolist | grep epel

# Install something from EPEL
sudo dnf install htop -y
htop --version

# Disable EPEL for a single command
sudo dnf install htop --disablerepo=epel
```

**On Ubuntu:**

```bash
# Ubuntu uses PPAs for additional repositories
# Install htop which is in the standard repos
sudo apt install htop -y
htop --version
```

**Lab Question 3:** What is the base URL of the first repository listed in your repo configuration? Is GPG checking enabled? What GPG key file is referenced?

---

## Task 5 — Package Verification

### Step 5.1 — Verify Package Integrity (RHEL)

```bash
# Verify the openssh-server package
sudo rpm -V openssh-server

# What does empty output mean?
# (Empty = all files match the package database — package is intact)

# Verify all installed packages (takes a while)
# This is a security audit command
sudo rpm -Va 2>/dev/null | head -30

# Focus on non-config-file changes (more security-relevant)
sudo rpm -Va 2>/dev/null | grep -v "^\.\.c" | head -20

# Intentionally corrupt a file to see verification output
sudo cp /etc/hosts /etc/hosts.bak
echo "1.2.3.4 malicious.example.com" | sudo tee -a /etc/hosts > /dev/null
sudo rpm -Vf /etc/hosts

# Restore
sudo cp /etc/hosts.bak /etc/hosts
```

### Step 5.2 — Verify Package Integrity (Debian)

```bash
# Install debsums
sudo apt install debsums -y

# Verify openssh-server
sudo debsums openssh-server

# Verify all packages (takes a while)
sudo debsums -c 2>/dev/null | head -20

# Intentionally modify a file
sudo cp /etc/hosts /etc/hosts.bak
echo "1.2.3.4 test.example.com" | sudo tee -a /etc/hosts > /dev/null
sudo debsums -c 2>/dev/null | grep hosts

# Restore
sudo cp /etc/hosts.bak /etc/hosts
```

**Lab Question 4:** After intentionally modifying `/etc/hosts`, what did the verification output show? What code characters appeared in the RPM output?

---

## Task 6 — Compile a Simple Program from Source

This task works on both distributions. You will compile a small but real utility from source.

### Step 6.1 — Install Build Dependencies

**On RHEL/Rocky:**

```bash
sudo dnf groupinstall "Development Tools" -y
sudo dnf install wget -y
```

**On Ubuntu:**

```bash
sudo apt update
sudo apt install build-essential wget -y
```

### Step 6.2 — Download and Examine Source

```bash
# Download the hello utility from GNU (classic autotools example)
cd /tmp
wget https://ftp.gnu.org/gnu/hello/hello-2.12.1.tar.gz

# Verify the download with checksum (compare against GNU website)
sha256sum hello-2.12.1.tar.gz

# Extract
tar xzf hello-2.12.1.tar.gz
cd hello-2.12.1/

# Examine the source structure
ls -la
cat README
cat configure.ac | head -20    # Autotools configuration
```

### Step 6.3 — Configure

```bash
# Run configure — examines your system and creates a Makefile
./configure --prefix=/usr/local

# Examine the generated Makefile
head -30 Makefile
```

**Lab Question 5:** What does the `--prefix` flag control? What would happen if you ran `./configure` without `--prefix`?

### Step 6.4 — Compile and Install

```bash
# Compile using all available CPU cores
make -j$(nproc)

# Test (hello has a built-in test suite)
make check

# Install
sudo make install

# Verify installation
/usr/local/bin/hello
/usr/local/bin/hello --version
which hello
```

### Step 6.5 — Uninstall

```bash
# Many autotools projects support make uninstall
cd /tmp/hello-2.12.1
sudo make uninstall

# Verify removal
which hello
echo "Exit code: $?"

# Clean up
cd /tmp
rm -rf hello-2.12.1 hello-2.12.1.tar.gz
```

---

## Task 7 — Transaction History (RHEL Only)

```bash
# View DNF transaction history
dnf history

# View details of a recent transaction
dnf history info last

# What packages were installed in transaction #1 (initial OS install)?
dnf history info 1 | head -30

# Undo the 'tree' installation from Task 3
# (Find the transaction number first)
dnf history | grep tree

# Undo that specific transaction
sudo dnf history undo last
```

---

## Task 8 — Write a Package Management Script

Using what you learned in Module 9 (shell scripting), write a script that automates package verification and reporting.

### Step 8.1 — Create the Script

Create `~/scripts_lab/mod10/pkg_audit.sh`:

```bash
#!/usr/bin/env bash
# pkg_audit.sh — Package integrity audit script
# Works on RHEL and Debian family systems

set -euo pipefail

REPORT_FILE="/tmp/pkg_audit_$(date +%Y%m%d_%H%M%S).txt"

# Detect package manager family
detect_family() {
  if command -v rpm &>/dev/null && command -v dnf &>/dev/null; then
    echo "rhel"
  elif command -v dpkg &>/dev/null && command -v apt &>/dev/null; then
    echo "debian"
  else
    echo "unknown"
  fi
}

generate_report() {
  local family="$1"
  echo "============================================"
  echo " Package Integrity Audit Report"
  echo " Host: $(hostname)"
  echo " Date: $(date)"
  echo " Family: $family"
  echo "============================================"
  echo ""

  case "$family" in
    rhel)
      echo "--- Installed Package Count ---"
      rpm -qa | wc -l
      echo ""
      echo "--- Recently Installed (last 10) ---"
      rpm -qa --last | head -10
      echo ""
      echo "--- Verification Issues (non-config files) ---"
      rpm -Va 2>/dev/null | grep -v "^\.\.c" || echo "No issues found"
      ;;
    debian)
      echo "--- Installed Package Count ---"
      dpkg -l | grep "^ii" | wc -l
      echo ""
      echo "--- Recent dpkg Activity ---"
      tail -20 /var/log/dpkg.log 2>/dev/null || echo "Log not available"
      echo ""
      echo "--- Packages with Updates Available ---"
      apt list --upgradable 2>/dev/null | grep -v "^Listing"
      ;;
    *)
      echo "ERROR: Unsupported package management system"
      exit 1
      ;;
  esac
}

FAMILY=$(detect_family)
generate_report "$FAMILY" | tee "$REPORT_FILE"
echo ""
echo "Report saved to: $REPORT_FILE"
```

### Step 8.2 — Test

```bash
chmod +x ~/scripts_lab/mod10/pkg_audit.sh
~/scripts_lab/mod10/pkg_audit.sh
```

---

## Lab Deliverables

Submit the following:

1. Answers to Lab Questions 1–5
2. Output of the package ownership queries from Task 2
3. Screenshot or paste of the repository list from Task 4.1
4. The verification output from Task 5 (after intentional modification and after restoration)
5. Output of `hello --version` after Task 6 installation
6. The `pkg_audit.sh` script code and its output

---

## Troubleshooting Guide

| Problem | Solution |
|---|---|
| `dnf: command not found` | You are on an older RHEL/CentOS 7; use `yum` instead |
| `wget: command not found` | Install with `sudo apt install wget` or `sudo dnf install wget` |
| `configure: error: C compiler cannot create executables` | Install build tools: `sudo apt install build-essential` |
| `make: command not found` | Install with `sudo apt install make` or `sudo dnf install make` |
| GPG check failed | Import the GPG key: `sudo rpm --import URL` or check `apt-key list` |
| `debsums: command not found` | Install with `sudo apt install debsums` |
| `apt-file: command not found` | Install with `sudo apt install apt-file && sudo apt-file update` |
