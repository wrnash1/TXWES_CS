# Reading Guide: Module 05 - Package Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 05. Package management is how Linux handles software throughout its entire
lifecycle: installation, updates, queries, and removal. This reading guide provides the complete
reference tables for both the Debian and Red Hat ecosystems, repository configuration, and package
integrity verification. These topics appear throughout the Linux+ exam under Domain 1.0.

---

### 1. High-Yield Glossary

**Package:** A compressed archive containing application files, metadata, dependency information,
and pre/post install scripts. Debian uses .deb format; Red Hat uses .rpm format.

**Repository:** A structured server hosting packages with metadata and GPG signatures. Package
managers download package lists from repositories during updates.

**Dependency Resolution:** The process of automatically identifying and installing all packages
required by the target package. High-level tools (apt, dnf) do this automatically. Low-level
tools (dpkg, rpm) do not.

**GPG Key:** A cryptographic signature used to verify the authenticity of packages and
repositories. Packages signed with a trusted key confirm the package has not been tampered with.

**APT (Advanced Package Tool):** High-level package manager for Debian/Ubuntu. Works with
dpkg underneath. Repository config in /etc/apt/sources.list and /etc/apt/sources.list.d/.

**dpkg:** Low-level Debian package tool. Installs, removes, and queries .deb files without
network access or dependency resolution.

**DNF (Dandified YUM):** Modern high-level package manager for RHEL 8+, Fedora, and CentOS
Stream. Repository config in /etc/yum.repos.d/. Successor to yum.

**YUM (Yellowdog Updater Modified):** Legacy Red Hat package manager, still used on RHEL 7 and
CentOS 7. Commands are nearly identical to dnf.

**rpm:** Low-level Red Hat package tool. Works with local .rpm files. Does not auto-resolve
dependencies. The rpm -V command verifies package integrity.

**Package Database:** Local metadata store tracking what packages are installed, their versions,
and checksums of all installed files. Used by rpm -V and dpkg --verify for integrity checking.

**EPEL (Extra Packages for Enterprise Linux):** A free repository of additional packages for
RHEL-based systems, maintained by Fedora. Commonly needed for packages not in official Red Hat
repositories.

---

### 2. APT Command Reference

| Command | Purpose |
|---------|---------|
| sudo apt update | Refresh repository metadata |
| sudo apt upgrade | Upgrade all installed packages |
| sudo apt install pkg | Install package and dependencies |
| sudo apt install -y pkg | Install without confirmation prompts |
| sudo apt remove pkg | Remove binaries (keep config files) |
| sudo apt purge pkg | Remove binaries AND config files |
| sudo apt autoremove | Remove unused dependency packages |
| apt search keyword | Search available packages |
| apt show pkg | Show package details |
| apt list --installed | List all installed packages |
| apt list --upgradable | List packages with available updates |
| sudo apt install -f | Fix broken package dependencies |
| sudo apt install ./local.deb | Install local .deb with dep resolution |

---

### 3. dpkg Command Reference

| Command | Purpose |
|---------|---------|
| dpkg -l | List all installed packages |
| dpkg -l pkg | Show status of specific package |
| dpkg -L pkg | List files installed by package |
| dpkg -S /path/to/file | Find which package owns a file |
| dpkg -s pkg | Show package status information |
| dpkg --verify pkg | Verify package file integrity |
| dpkg -i package.deb | Install local .deb file (no dep resolution) |
| dpkg -r pkg | Remove package (keep config files) |
| dpkg --purge pkg | Remove package and config files |
| dpkg --get-selections | List all package selections |

---

### 4. DNF/YUM Command Reference

| Command | Purpose |
|---------|---------|
| sudo dnf install pkg | Install package and dependencies |
| sudo dnf remove pkg | Remove package |
| sudo dnf update | Update all packages |
| sudo dnf update pkg | Update specific package |
| dnf search keyword | Search packages |
| dnf info pkg | Show package information |
| dnf list installed | List installed packages |
| dnf list available | List available packages |
| dnf history | Show transaction history |
| sudo dnf history undo N | Undo transaction N |
| dnf repolist | List configured repositories |
| sudo dnf config-manager --enable repo | Enable a repository |
| sudo dnf config-manager --disable repo | Disable a repository |
| sudo dnf check-update | Check for available updates |
| sudo dnf groupinstall "Development Tools" | Install a package group |

---

### 5. RPM Command Reference

| Command | Purpose |
|---------|---------|
| rpm -qa | Query all installed packages |
| rpm -qi pkg | Query information about installed package |
| rpm -ql pkg | List files installed by package |
| rpm -qf /path/to/file | Find which package owns a file |
| rpm -qR pkg | List package dependencies (requires) |
| rpm -V pkg | Verify package file integrity |
| rpm -Va | Verify all installed packages |
| rpm -ivh pkg.rpm | Install local .rpm (verbose + hash) |
| rpm -Uvh pkg.rpm | Upgrade local .rpm |
| rpm -e pkg | Erase (remove) package |
| rpm --import key.gpg | Import GPG key |
| rpm -K pkg.rpm | Verify RPM signature |

---

### 6. Package Ecosystem Comparison

| Feature | Debian/Ubuntu | Red Hat/RHEL |
|---------|--------------|--------------|
| Package format | .deb | .rpm |
| High-level tool | apt | dnf (yum on older) |
| Low-level tool | dpkg | rpm |
| Repository config | /etc/apt/sources.list | /etc/yum.repos.d/*.repo |
| Install from repo | apt install pkg | dnf install pkg |
| Install local file | dpkg -i pkg.deb | rpm -ivh pkg.rpm |
| Remove + keep config | apt remove pkg | dnf remove (config varies) |
| Remove + config files | apt purge pkg | dnf remove pkg |
| Find file owner | dpkg -S /path | rpm -qf /path |
| List package files | dpkg -L pkg | rpm -ql pkg |
| Verify integrity | dpkg --verify or debsums | rpm -V pkg |
| History/rollback | Limited | dnf history undo N |

---

### 7. rpm -V Output Codes

When rpm -V shows output, each character in the 9-character code means:

| Code | Meaning |
|------|---------|
| S | File size differs |
| M | File mode (permissions) differs |
| 5 | MD5 checksum mismatch (content changed) |
| D | Device major/minor number mismatch |
| L | Symlink target path mismatch |
| U | User ownership mismatch |
| G | Group ownership mismatch |
| T | Modification time differs |
| . | Test passed (no change) |

A dot in a position means that check passed. Example: .M....T. means only permissions and
timestamp differ.

---

### 8. Repository File Format (RHEL)

A typical /etc/yum.repos.d/nginx.repo file:

```ini
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/8/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
```

Key fields:

| Field | Purpose |
|-------|---------|
| [name] | Repository ID |
| name= | Human-readable name |
| baseurl= | URL to package directory |
| gpgcheck=1 | Verify GPG signatures (always use 1) |
| enabled=1 | Repository is active (0 to disable) |
| gpgkey= | URL or path to GPG key |

---

### 9. CompTIA Linux+ Exam Tips

**Exam Tip 1:** Never mix ecosystems in exam answers. If the scenario says Ubuntu, use apt or
dpkg. If it says RHEL or CentOS, use dnf/yum or rpm. Using apt on RHEL is always wrong.

**Exam Tip 2:** apt remove keeps config files. apt purge removes them. This is tested in
scenarios about clean reinstallation. "I want to completely remove nginx and start fresh" = purge.

**Exam Tip 3:** dpkg -S finds the package that owns a file (search by file). dpkg -L lists
files in a package (list by package). rpm -qf is the equivalent of dpkg -S on RHEL.

**Exam Tip 4:** rpm -V is the integrity verification command. When a question asks how to
detect whether an installed binary has been replaced or modified, the answer is rpm -V.

**Exam Tip 5:** High-level tools (apt, dnf) automatically resolve and install dependencies.
Low-level tools (dpkg -i, rpm -ivh) do not. If a question asks which tool would give
dependency errors when installing a local package file, the answer is dpkg or rpm.

**Exam Tip 6:** dnf history undo is a Red Hat-specific feature allowing transaction rollback.
This has no direct equivalent in apt. It is tested in RHEL-specific scenarios.

**Exam Tip 7:** sudo apt update refreshes package lists. sudo apt upgrade installs updates.
These are two separate operations. Running upgrade without update first may not install the
latest versions.

**Exam Tip 8:** GPG keys authenticate repositories and packages. gpgcheck=0 in a repo file
disables signature verification - a security risk. The exam tests awareness of this setting.

---

### 10. Study Checklist

- [ ] Watch both parts of the Module 05 video lecture
- [ ] Memorize the apt command reference table
- [ ] Memorize the dpkg command reference table (especially -S, -L, -l)
- [ ] Memorize the dnf command reference table
- [ ] Memorize the rpm command reference table (especially -V, -qf, -ql, -qa)
- [ ] Understand apt remove versus apt purge
- [ ] Understand rpm -V output codes
- [ ] Understand the difference between high-level and low-level tools
- [ ] Complete the Module 05 Lab
- [ ] Complete the Module 05 Quiz
- [ ] Post to the Discussion by Wednesday at 11:59 PM
- [ ] Reply to two classmates by Sunday at 11:59 PM

---

### Required Reading

Read chapter 14 of The Linux Command Line by William Shotts (linuxcommand.org/tlcl.php)
covering package management across both Debian and Red Hat ecosystems.
