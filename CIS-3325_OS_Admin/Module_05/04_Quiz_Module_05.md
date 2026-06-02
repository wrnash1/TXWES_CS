# Quiz: Module 05 - Package Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

A systems administrator on an Ubuntu server needs to install the nginx web server package from
the official repositories. Which command sequence is correct?

- A) rpm -ivh nginx && rpm -e nginx
- B) apt update && apt install nginx
- C) dnf install nginx --enablerepo=base
- D) dpkg -i nginx && apt resolve nginx

Correct Answer: B) apt update && apt install nginx

Distractor Analysis:

- Why A is incorrect: rpm is the Red Hat package tool and does not function on Ubuntu/Debian systems, which use the .deb format and dpkg/apt toolchain.
- Why C is incorrect: dnf is the package manager for Red Hat-based distributions. It is not available on Ubuntu by default.
- Why D is incorrect: dpkg -i requires a local .deb file path, not a package name. There is no apt resolve subcommand - dependency resolution is handled automatically by apt install.

---

**Question 2**

An administrator on a RHEL 8 system suspects that the files installed by the openssh-server
package have been tampered with. Which command verifies the integrity of the installed package
files against the RPM database?

- A) rpm -qa openssh-server
- B) rpm -ql openssh-server
- C) rpm -V openssh-server
- D) rpm -qf openssh-server

Correct Answer: C) rpm -V openssh-server

Distractor Analysis:

- Why A is incorrect: rpm -qa queries and lists all installed packages (or a specific one when a name is given). It does not perform integrity verification.
- Why B is incorrect: rpm -ql lists all files that were installed by the package. It does not check whether those files have been modified since installation.
- Why D is incorrect: rpm -qf is used to identify which package owns a specific file path. It does not verify integrity.

---

**Question 3**

A systems administrator needs to list all currently running processes on the system along with
their CPU and memory usage. Which command is most appropriate?

- A) ps aux
- B) df -h
- C) lsblk
- D) netstat -tuln

Correct Answer: A) ps aux

Distractor Analysis:

- Why B is incorrect: df -h reports disk space usage on mounted filesystems, not process information.
- Why C is incorrect: lsblk lists block devices (disks and partitions) and their mount points, not running processes.
- Why D is incorrect: netstat -tuln shows active network connections and listening ports, not CPU/memory usage of processes.

---

**Question 4**

An administrator removes a package on Ubuntu using apt remove nginx but later discovers the
nginx configuration files are still present in /etc/nginx/. Which command should have been
used to remove the package AND all its configuration files?

- A) apt delete nginx
- B) apt purge nginx
- C) dpkg -r nginx
- D) apt autoremove nginx

Correct Answer: B) apt purge nginx

Distractor Analysis:

- Why A is incorrect: There is no apt delete subcommand. This will produce an error.
- Why C is incorrect: dpkg -r removes the package binaries like apt remove does, but also leaves configuration files behind. Only dpkg --purge removes config files, but apt purge is the cleaner high-level equivalent.
- Why D is incorrect: apt autoremove removes packages that were automatically installed as dependencies and are no longer needed. It does not target a specific package's configuration files.

---

**Question 5**

A Linux administrator needs to identify which installed package owns the file /usr/sbin/sshd
on a Red Hat-based system. Which command achieves this?

- A) rpm -ql sshd
- B) rpm -Va /usr/sbin/sshd
- C) rpm -qf /usr/sbin/sshd
- D) dnf provides /usr/sbin/sshd

Correct Answer: C) rpm -qf /usr/sbin/sshd

Distractor Analysis:

- Why A is incorrect: rpm -ql lists files owned by a package when you already know the package name. It requires a package name as the argument, not a file path, and works in the opposite direction.
- Why B is incorrect: rpm -Va verifies all installed packages against the RPM database, checking for file modifications. It does not identify the package that owns a specific file.
- Why D is incorrect: dnf provides queries the repository metadata to find which package in the repos provides a file - useful before installation. However, for a file already on disk, rpm -qf is the direct and correct tool.

---

**Question 6**

An administrator needs to determine all packages that the curl package depends on before
installing it on a RHEL system. Which command lists curl's dependencies?

- A) rpm -ql curl
- B) dnf deplist curl
- C) rpm -qR curl
- D) dnf info curl

Correct Answer: C) rpm -qR curl

Distractor Analysis:

- Why A is incorrect: rpm -ql lists the files installed by a package, not its dependencies. This works only after the package is installed and answers "what files did it install," not "what does it need."
- Why B is incorrect: dnf deplist is a valid dnf command for listing dependencies, but rpm -qR is the standard RPM-level query. The question specifically mentions RHEL and the rpm tool is the most direct answer for this query type.
- Why D is incorrect: dnf info shows general package information including description, version, and summary. While it includes some dependency information in its output, rpm -qR specifically lists dependencies in a clean format.

---

**Question 7**

An Ubuntu administrator wants to search for any package that provides a terminal-based
file manager. Which command searches the repository metadata for matching packages?

- A) dpkg -l "file manager"
- B) apt search "file manager"
- C) dpkg -S file-manager
- D) apt list file-manager

Correct Answer: B) apt search "file manager"

Distractor Analysis:

- Why A is incorrect: dpkg -l lists installed packages and can filter by name pattern, but it searches the local installed package database, not repository metadata. It will only find packages already installed.
- Why C is incorrect: dpkg -S searches for which installed package owns a specific file path. It is not a package search tool and does not search repository metadata or package descriptions.
- Why D is incorrect: apt list without --installed or --upgradable simply lists available packages but requires an exact package name or pattern. It does not search descriptions or package summaries.

---

**Question 8**

An administrator runs rpm -V httpd on a RHEL server and receives the following output:

S.5....T.  c /etc/httpd/conf/httpd.conf

What does this output indicate?

- A) The httpd.conf file was installed by the httpd package and has not been modified.
- B) The httpd.conf file has changed in size (S), MD5 checksum (5), and timestamp (T). The c indicates it is a configuration file. These are expected changes from administrator customization.
- C) The httpd.conf file is corrupted and should be deleted immediately.
- D) The httpd package needs to be reinstalled because the checksum validation failed for the main binary.

Correct Answer: B) The httpd.conf file has changed in size (S), MD5 checksum (5), and timestamp (T). The c indicates it is a configuration file. These are expected changes from administrator customization.

Distractor Analysis:

- Why A is incorrect: If the file had not been modified, rpm -V would produce no output for it. Any output indicates a discrepancy from the originally installed state.
- Why C is incorrect: rpm -V output does not mean a file is corrupted in the sense of being damaged. For configuration files (c), these changes are normal and expected because administrators modify configuration files after installation. The output informs, not alarms.
- Why D is incorrect: The output specifically points to /etc/httpd/conf/httpd.conf (a config file, c), not to the httpd binary. The httpd binary itself passed verification. Reinstalling the package would overwrite the administrator's configuration.

---

**Question 9**

An Ubuntu administrator installs the nginx package and then checks /etc/nginx/ for the
configuration files. Later they need to remove nginx completely for security compliance reasons
and want no trace of the package on the system. What is the correct two-step process?

- A) apt remove nginx && rm -rf /etc/nginx/
- B) apt purge nginx && apt autoremove
- C) dpkg -r nginx && dpkg --purge nginx
- D) apt delete nginx && apt clean

Correct Answer: B) apt purge nginx && apt autoremove

Distractor Analysis:

- Why A is incorrect: While apt remove nginx && rm -rf /etc/nginx/ achieves a similar result, manually deleting configuration directories is fragile and may miss files nginx placed elsewhere. apt purge handles all configuration file removal according to the package's own manifest.
- Why C is incorrect: Running dpkg -r (which is like apt remove) followed by dpkg --purge on the same package creates an unnecessary two-step process at the wrong level. The high-level apt purge is cleaner and more appropriate than mixing dpkg operations this way.
- Why D is incorrect: There is no apt delete subcommand. apt clean removes cached downloaded package files from /var/cache/apt/archives/, which is different from removing installed packages.

---

**Question 10**

A Red Hat administrator needs to find out what packages were installed on a server yesterday
afternoon because an unauthorized change may have occurred. Which command provides installation
history?

- A) rpm -qa --last | head -20
- B) dnf history
- C) cat /var/log/packages.log
- D) dpkg -l --history

Correct Answer: B) dnf history

Distractor Analysis:

- Why A is incorrect: rpm -qa --last sorts the installed packages list by install date, which shows when packages were installed, but it does not show the full transaction context (who ran dnf, what was installed together, or what was removed). dnf history is the proper transaction log tool.
- Why C is incorrect: There is no standard /var/log/packages.log file on RHEL systems. Package transaction history is managed by dnf in its own database, not as a flat log file at that path.
- Why D is incorrect: dpkg -l --history is not valid dpkg syntax. The --history flag does not exist for dpkg. On Debian/Ubuntu systems, apt history is found in /var/log/apt/history.log, not via dpkg flags.
