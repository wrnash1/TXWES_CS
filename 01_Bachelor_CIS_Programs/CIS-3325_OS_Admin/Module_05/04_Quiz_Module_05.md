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

---

Questions 11-20 — 5 pts each

---

**Question 11**

An Ubuntu administrator wants to prevent a specific package from being upgraded when running
apt upgrade because a custom configuration depends on the current version. Which command
holds the package at its current version?

- A) apt mark hold nginx
- B) apt-mark hold nginx
- C) dpkg --hold nginx
- D) apt pin nginx

Correct Answer: B) apt-mark hold nginx

Distractor Analysis:

- Why A is incorrect: The correct command is apt-mark (hyphenated) not "apt mark" with a space. "apt mark" is not a valid apt subcommand and will produce an error.
- Why C is incorrect: dpkg --hold is not valid dpkg syntax. The hold state is managed through apt-mark, not directly via dpkg flags.
- Why D is incorrect: apt pin is not a valid apt subcommand. Package pinning is done through /etc/apt/preferences files, not via an apt pin command.

---

**Question 12**

An administrator on Ubuntu 22.04 adds a new third-party repository by placing a .list file
in /etc/apt/sources.list.d/. After running apt update, the command fails with a "NO_PUBKEY"
error. What must the administrator do to resolve this?

- A) Run apt install --fix-missing to download missing package signatures.
- B) Import the repository's GPG signing key using apt-key add or by placing the key in /etc/apt/trusted.gpg.d/.
- C) Edit /etc/apt/sources.list and add a trusted=yes option for the repository.
- D) Disable signature verification globally with APT::Get::AllowUnauthenticated "true" in apt.conf.

Correct Answer: B) Import the repository's GPG signing key using apt-key add or by placing the key in /etc/apt/trusted.gpg.d/.

Distractor Analysis:

- Why A is incorrect: apt install --fix-missing attempts to work around missing packages, not missing cryptographic signing keys. It does not resolve key trust errors.
- Why C is incorrect: Adding trusted=yes to a source entry bypasses signature verification for that repository entirely, which is a security risk and not the correct resolution for a missing key.
- Why D is incorrect: Setting AllowUnauthenticated globally disables package signature verification for all repositories, creating a serious security vulnerability. The correct fix is importing the specific key.

---

**Question 13**

Which file on a Debian/Ubuntu system contains the list of configured apt repositories,
including the main, restricted, universe, and multiverse components?

- A) /etc/dpkg/sources
- B) /etc/apt/sources.list and files in /etc/apt/sources.list.d/
- C) /var/lib/apt/lists/
- D) /etc/apt/apt.conf.d/

Correct Answer: B) /etc/apt/sources.list and files in /etc/apt/sources.list.d/

Distractor Analysis:

- Why A is incorrect: /etc/dpkg/sources does not exist as a standard configuration path. dpkg's configuration directory is /etc/dpkg/ but it does not contain repository source lists.
- Why C is incorrect: /var/lib/apt/lists/ contains the cached repository metadata downloaded by apt update. These are auto-generated index files, not the source configuration that specifies which repositories to use.
- Why D is incorrect: /etc/apt/apt.conf.d/ contains apt behavior configuration files (proxy settings, cache limits, etc.) but not repository source definitions.

---

**Question 14**

On a RHEL 9 system, an administrator wants to install a package from a specific repository
while that repository is normally disabled. Which dnf flag enables a disabled repository
for a single transaction?

- A) dnf install --repo=rhel-extras package
- B) dnf install --enablerepo=rhel-extras package
- C) dnf enable rhel-extras && dnf install package
- D) dnf install --from=rhel-extras package

Correct Answer: B) dnf install --enablerepo=rhel-extras package

Distractor Analysis:

- Why A is incorrect: --repo= is not a valid dnf install flag. The correct flag for enabling a specific repo in a single transaction is --enablerepo=.
- Why C is incorrect: dnf enable is not a valid dnf subcommand. Enabling a repository permanently is done with dnf config-manager --enable rhel-extras. The --enablerepo flag enables it for just one command.
- Why D is incorrect: --from= is not a valid dnf flag. This syntax does not exist in the dnf command set.

---

**Question 15**

An administrator runs dpkg -l | grep "^ii" on an Ubuntu server. What does the "^ii" pattern
in the grep filter match?

- A) Packages whose names begin with the letters "ii".
- B) Lines where the package status is "ii" — installed and correctly configured (desired: install, status: installed).
- C) Packages that are partially installed or in an error state.
- D) Packages installed from a third-party repository rather than the official Ubuntu archive.

Correct Answer: B) Lines where the package status is "ii" — installed and correctly configured (desired: install, status: installed).

Distractor Analysis:

- Why A is incorrect: The pattern ^ii anchors to the beginning of the line. The "ii" in dpkg -l output is a two-character status code in the first columns, not part of the package name.
- Why C is incorrect: Partially installed packages show as "iF" (desired install, failed) or "pF" (purge, failed). The "ii" code specifically means fully installed and configured.
- Why D is incorrect: dpkg -l output does not distinguish package origin (official vs. third-party). The status field only reflects installation state, not repository source.

---

**Question 16**

A systems administrator needs to download a .deb package and all its dependencies to a
directory for offline installation on an air-gapped server. Which apt command downloads
without installing?

- A) apt get --download-only nginx
- B) apt-get download nginx
- C) apt download nginx
- D) Both B and C

Correct Answer: D) Both B and C

Distractor Analysis:

- Why A is incorrect: "apt get --download-only" is not valid syntax. apt-get install --download-only downloads a package and dependencies to the cache but does not install. "apt get" with a space is not a valid command.
- Why B alone is partially correct: apt-get download is a valid legacy command that downloads the .deb file to the current directory. It downloads only the named package, not dependencies.
- Why C alone is partially correct: apt download is the modern equivalent of apt-get download, introduced in newer apt versions. Both B and C download the .deb to the current directory.

---

**Question 17**

After a security incident on a RHEL system, an administrator wants to check whether the
/etc/crontab file has been tampered with. The file is owned by the cronie package. Which
command verifies its integrity?

- A) md5sum /etc/crontab
- B) sha256sum /etc/crontab
- C) rpm -Vf /etc/crontab
- D) dnf check /etc/crontab

Correct Answer: C) rpm -Vf /etc/crontab

Distractor Analysis:

- Why A is incorrect: md5sum produces a checksum but requires a trusted baseline to compare against. Without a pre-established record of the original hash, the output alone cannot confirm integrity.
- Why B is incorrect: Same issue as A — sha256sum is cryptographically stronger but still requires a baseline. rpm -Vf uses the package database as the trusted baseline automatically.
- Why D is incorrect: dnf check is used to verify the consistency of the rpm database itself, not the integrity of individual installed files. It does not check file checksums against the package database.

---

**Question 18**

An Ubuntu administrator wants to see exactly which files would be removed if they ran
apt purge nginx, without actually removing anything. Which command performs a dry run?

- A) apt purge --simulate nginx
- B) apt purge -n nginx
- C) apt-get --dry-run purge nginx
- D) All of the above are valid

Correct Answer: D) All of the above are valid

Distractor Analysis:

- Why A alone is partially correct: apt purge --simulate is valid syntax. --simulate tells apt to show what would happen without making changes.
- Why B alone is partially correct: The -n flag is the short form of --simulate in apt. Both forms are accepted.
- Why C alone is partially correct: apt-get --dry-run is the legacy equivalent. --dry-run and --simulate are synonymous in apt/apt-get. All three expressions trigger a simulation run showing what files would be removed.

---

**Question 19**

A package called legacy-tool is no longer in the Ubuntu repository but a .deb file has
been provided by the vendor. The administrator installs it with dpkg -i legacy-tool.deb
and gets "dpkg: error processing archive ... dependency problems." What is the correct
next step to resolve the dependencies automatically?

- A) apt install -f
- B) apt install legacy-tool
- C) dpkg --configure -a
- D) apt update && apt upgrade

Correct Answer: A) apt install -f

Distractor Analysis:

- Why B is incorrect: The package is not in the repository, so apt install legacy-tool would fail with "package not found." The package was already placed into dpkg's database by the dpkg -i command; apt just needs to resolve its missing dependencies.
- Why C is incorrect: dpkg --configure -a attempts to configure all unpacked but unconfigured packages. While sometimes useful after dpkg errors, it does not fetch or install missing dependency packages from repositories.
- Why D is incorrect: apt update refreshes repository metadata and apt upgrade upgrades existing packages. Neither step resolves the specific dependency error for a manually installed .deb package. apt install -f (fix-broken) is the correct tool.

---

**Question 20**

An administrator reviews /var/log/apt/history.log on Ubuntu and sees a package was
installed at an unexpected time. Which command shows the complete history of apt
transactions including install, remove, and upgrade actions with timestamps?

- A) dpkg --get-selections
- B) cat /var/log/apt/history.log
- C) apt list --installed
- D) dpkg -l | grep ii

Correct Answer: B) cat /var/log/apt/history.log

Distractor Analysis:

- Why A is incorrect: dpkg --get-selections lists packages and their desired installation state (install, deinstall, purge) but does not include timestamps, transaction history, or who performed the action.
- Why C is incorrect: apt list --installed shows currently installed packages with their versions but provides no historical timeline of when they were installed or removed.
- Why D is incorrect: dpkg -l lists installed packages in a formatted table. Like option C, it shows current state only — no historical transactions, timestamps, or action context.
