# Video Script: Module 05 - Package Management (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - RPM, Integrity Verification, and Exam Application

---

### Opening

Welcome back to Part 2 of Module 05. In Part 1 we covered apt and dpkg for Debian/Ubuntu, and
dnf/yum for Red Hat systems. In Part 2 we go deep into the rpm command, which is critical exam
material, and we cover package integrity verification - an important security skill.

---

### Section 1: RPM - The Red Hat Low-Level Tool

rpm is the low-level package management tool on Red Hat-based systems. Like dpkg on Debian,
it works directly with .rpm files and the local package database.

[SHOW TERMINAL]

```bash
rpm -qa
```

Query All: lists every installed package on the system. This is the complete package inventory.

```bash
rpm -qa | grep openssh
```

Filter the installed package list.

```bash
rpm -qi openssh-server
```

Query information about an installed package: version, architecture, install date, summary.

```bash
rpm -ql openssh-server
```

Query list: shows all files installed by the openssh-server package.

```bash
rpm -qf /etc/ssh/sshd_config
```

Query file: identifies which package owns /etc/ssh/sshd_config. The -f flag means "what
package installed this file?"

```bash
rpm -qR openssh-server
```

Query requirements: lists all dependencies (required packages and libraries).

```bash
rpm -ivh package.rpm
```

Install a local .rpm file. -i = install, -v = verbose, -h = hash progress bars.

```bash
rpm -Uvh package.rpm
```

Upgrade: install or upgrade. If the package is already installed, upgrade it.

```bash
rpm -e openssh-server
```

Erase (remove) a package.

---

### Section 2: Package Integrity Verification with rpm -V

The most exam-tested rpm command is rpm -V (verify). It checks the files installed by a package
against the RPM database record of what they should look like.

[SHOW TERMINAL]

```bash
rpm -V openssh-server
```

If nothing is wrong, there is no output. Any output indicates a discrepancy.

Output codes:
- S: file Size differs
- M: file Mode (permissions) differ
- 5: MD5 checksum mismatch (file contents changed)
- D: Device major/minor number mismatch
- L: readLink path mismatch
- U: User ownership mismatch
- G: Group ownership mismatch
- T: Timestamp mismatch

Example output line:

```
S.5....T.  /usr/sbin/sshd
```

This means the file size (S), checksum (5), and timestamp (T) of /usr/sbin/sshd all differ
from what the package installed. This is a strong indicator of file tampering.

```bash
rpm -Va
```

Verify All: checks every installed package on the system. This is a comprehensive integrity audit.
Output can be very long on a system with many packages.

For the exam: if a question asks how to detect whether an installed package's files have been
tampered with, the answer is rpm -V packagename.

---

### Section 3: Package Integrity Verification with apt/dpkg

On Debian/Ubuntu systems, package integrity checking works differently.

[SHOW TERMINAL]

```bash
sudo debsums openssh-server
```

debsums is a separate utility that checks file checksums against the package database.
It may need to be installed: sudo apt install debsums

```bash
dpkg --verify
```

dpkg --verify checks installed packages against recorded file checksums. Available on modern
dpkg versions.

On both platforms, GPG signature verification happens automatically when packages are
downloaded. If a package's GPG signature does not match the trusted key, the package manager
refuses to install it. This is why adding a third-party repository's GPG key is a prerequisite
before installing from that repo.

---

### Section 4: Practical Cross-Platform Scenarios

Let me work through the specific scenarios tested on the exam.

[SHOW TERMINAL]

Scenario 1: You need to find which package installed a specific file.

Ubuntu: dpkg -S /usr/sbin/nginx
RHEL: rpm -qf /usr/sbin/nginx

Scenario 2: You need to see all files that were installed by a package.

Ubuntu: dpkg -L nginx
RHEL: rpm -ql nginx

Scenario 3: You need to remove a package and all its configuration files.

Ubuntu: sudo apt purge nginx
RHEL: sudo dnf remove nginx (dnf removes configs by default)

Scenario 4: You want to check whether any installed package files have been modified.

RHEL: rpm -V packagename (or rpm -Va for all packages)
Ubuntu: sudo debsums packagename

Scenario 5: You installed a .deb file manually with dpkg and got dependency errors.

Fix: sudo apt install -f (install fixing broken dependencies)

Scenario 6: You need to check what version of a package is currently installed.

Ubuntu: dpkg -s packagename | grep Version
RHEL: rpm -qi packagename | grep Version

---

### Section 5: Package Management for Security

Package management is a security-relevant skill, not just an operational one.

[SHOW TERMINAL]

Keep systems updated:

```bash
sudo apt update && sudo apt upgrade -y
```

On RHEL:

```bash
sudo dnf update -y
```

Installing patches promptly is the most effective defense against known vulnerabilities. Many
high-profile breaches exploited vulnerabilities that had patches available but were not applied.

Install only what you need:

```bash
sudo apt remove packagename
```

Remove packages that are not needed. A minimal package footprint reduces attack surface.

Verify package sources:

```bash
apt-key list
```

Lists all trusted GPG keys for apt repositories. Keys should come from official sources.

```bash
rpm --import /path/to/key.gpg
```

Import a GPG key for RPM package verification.

Check for orphaned packages (installed but no longer in any repo):

```bash
sudo apt list --installed | grep "\[installed,local\]"
```

Locally installed packages not tracked by any repository may not receive security updates.

---

### Section 6: Exam Tips

The apt remove versus apt purge distinction is tested constantly. remove keeps configuration
files. purge removes them. The exam scenario: "completely uninstall including all configuration"
= purge.

dpkg -S finds the package that owns a file. This is the inverse of dpkg -L (which lists files
given a package). -S = search by file. -L = list by package.

rpm -V verifies integrity. The output codes matter: 5 = checksum mismatch, S = size change,
M = mode/permission change.

High-level tools (apt, dnf) auto-resolve dependencies. Low-level tools (dpkg, rpm) do not.
A question asking "which tool installs a local .deb file and automatically resolves all
required dependencies" is tricky - neither apt nor dpkg installs local .deb files with full
dependency resolution by default. apt install ./local.deb (dot-slash syntax) on modern apt
does resolve dependencies.

dnf history and dnf history undo are unique features of dnf not available in apt. The exam
may test this as a Red Hat-specific advantage.

---

### Lab Preview

This week's lab has you installing and removing packages with apt, querying the dpkg database,
adding a third-party repository, and verifying package integrity. You will practice both the
high-level apt commands and the low-level dpkg commands for the same operations to understand
what each layer does.

---

### Summary

Module 05 covers the complete package management landscape: apt and dpkg for Debian/Ubuntu,
dnf/yum and rpm for Red Hat systems, repository configuration, and package integrity verification.
These tools are tested across multiple domains of the Linux+ exam and are used daily in any
Linux environment.

Module 06 covers process management - how to monitor running processes, send signals, and
manage system services.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
