# Quiz: Module 10 — Package Management and Software Installation

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. A score of 80 or higher is required to advance to Module 11.

---

**Question 1**

A Linux administrator on a RHEL system needs to find out which installed package contains the file `/usr/bin/nmcli`. Which command is correct?

A. `rpm -ql /usr/bin/nmcli`

B. `rpm -qf /usr/bin/nmcli`

C. `dnf list /usr/bin/nmcli`

D. `rpm -qi /usr/bin/nmcli`

**Correct Answer:** B

**Explanation:** `rpm -qf FILE` (query which package owns a file) is the correct command. `-qf` = query, find package owning file. `-ql` lists the files in a package (not the reverse). `-qi` shows info about a package by name. `dnf list` lists packages, not files.

---

**Question 2**

An administrator on Ubuntu needs to fix a failed package installation that left the system in a broken state with unresolved dependencies. Which command should they run first?

A. `sudo dpkg --configure -a && sudo apt --fix-broken install`

B. `sudo apt reinstall broken-package`

C. `sudo apt purge broken-package`

D. `sudo dpkg -r broken-package --force-all`

**Correct Answer:** A

**Explanation:** When dpkg/apt leaves packages in an unconfigured or broken state, `dpkg --configure -a` attempts to configure all pending packages, and `apt --fix-broken install` (also written as `apt -f install`) resolves dependency issues. These two commands together address the most common broken-install scenarios. The other options are more destructive or don't address dependency resolution.

---

**Question 3**

On a RHEL 9 system, an administrator wants to see details about transaction number 7 in the DNF history and then undo it. Which sequence is correct?

A. `yum history info 7` then `yum history undo 7`

B. `dnf history info 7` then `dnf history undo 7`

C. `rpm -Va 7` then `rpm -e --undo 7`

D. `dnf log 7` then `dnf rollback 7`

**Correct Answer:** B

**Explanation:** `dnf history info N` shows details of a specific transaction and `dnf history undo N` reverses it. On RHEL 9, `dnf` is the default tool; `yum` is a compatibility shim. Option A would also work on RHEL 9 because yum calls dnf, but option B is the correct current syntax.

---

**Question 4**

An administrator needs to add an additional package repository on a RHEL system. The repository requires GPG signature verification. Where should the repository configuration file be placed?

A. `/etc/apt/sources.list.d/`

B. `/etc/rpm/repos.d/`

C. `/etc/yum.repos.d/`

D. `/usr/share/yum/repos/`

**Correct Answer:** C

**Explanation:** RHEL-family repository configuration files (`.repo` files) belong in `/etc/yum.repos.d/`. This directory is read by both `yum` and `dnf`. Option A is the Debian/APT directory. Options B and D do not exist.

---

**Question 5**

After running `sudo rpm -Va` on a RHEL server, an administrator sees this output:

```
S.5....T.  /usr/bin/sshd
```

What does this output most likely indicate?

A. The `/usr/bin/sshd` file's configuration was intentionally modified.

B. The `/usr/bin/sshd` binary's size, MD5 checksum, and modification time differ from the package database.

C. The SSH service needs to be restarted to apply pending updates.

D. The sshd package was recently upgraded but not yet configured.

**Correct Answer:** B

**Explanation:** In RPM verification output, `S` = file size changed, `5` = MD5 checksum changed, `T` = modification time changed. These three changes on a system binary (`/usr/bin/sshd`) are a serious security indicator — a potential binary replacement or rootkit. Configuration files changing is normal; system binary changes are not. The `c` code indicating a config file is absent from this output.

---

**Question 6**

An administrator on Ubuntu wants to see all versions of the `nginx` package available from configured repositories, along with which repository each version comes from. Which command provides this?

A. `dpkg -s nginx`

B. `apt show nginx`

C. `apt-cache policy nginx`

D. `apt list nginx`

**Correct Answer:** C

**Explanation:** `apt-cache policy nginx` shows the installed version, all available versions, and the repository (with priority) each version comes from. `dpkg -s` only shows installed package status. `apt show` shows the latest available version's details. `apt list nginx` shows the current available package but not all versions.

---

**Question 7**

An administrator needs to install a package from the EPEL repository on RHEL 9 but wants to keep EPEL disabled by default and only use it for this one installation. Which command is correct?

A. `sudo dnf install --enablerepo=epel htop`

B. `sudo dnf install --repo=epel htop`

C. `sudo dnf config-manager --enable epel && sudo dnf install htop`

D. `sudo dnf install htop --from epel`

**Correct Answer:** A

**Explanation:** `--enablerepo=epel` enables the specified repository temporarily for that single command only. The repository remains disabled for all future commands. Option C would permanently enable EPEL, which is not what was asked. Options B and D use invalid flag syntax.

---

**Question 8**

A developer has compiled software from source and ran `sudo make install`. The software installed files to `/usr/local/bin/`. Which problem does this create for the system administrator?

A. The files will conflict with distribution packages.

B. The package manager has no record of these files and cannot track, update, or remove them.

C. The files will be deleted the next time the operating system is updated.

D. The software will not run because `/usr/local/bin/` is not in the default PATH.

**Correct Answer:** B

**Explanation:** Software installed with `make install` bypasses the package management database entirely. The package manager (rpm/dpkg) has no knowledge of these files — they cannot be listed, verified for integrity, or uninstalled via the package manager. This is why `checkinstall` is recommended as an alternative to `make install`. The other options are incorrect: `/usr/local/bin/` does not conflict with distribution packages, files survive OS updates, and `/usr/local/bin/` is typically in the default PATH.

---

**Question 9**

On a Debian system, an administrator removes a package with `apt remove nginx`. They later discover that Nginx configuration files were left behind in `/etc/nginx/`. What should they have used instead?

A. `apt uninstall nginx`

B. `apt delete nginx`

C. `apt purge nginx`

D. `dpkg -r --with-config nginx`

**Correct Answer:** C

**Explanation:** `apt remove` (and `dpkg -r`) remove the package but preserve configuration files. `apt purge` (and `dpkg -P`) removes the package AND its configuration files. This distinction is by design — it allows administrators to uninstall and reinstall software while preserving their configuration. Option A and B are not valid APT commands. Option D is not valid dpkg syntax.

---

**Question 10**

What is the correct sequence of commands to compile and install software that uses GNU Autotools?

A. `make → ./configure → sudo make install`

B. `./configure → make → sudo make install`

C. `sudo make install → ./configure → make`

D. `gcc → ./configure → sudo make install`

**Correct Answer:** B

**Explanation:** The standard GNU Autotools build sequence is always: `./configure` (examine the system and generate a Makefile), then `make` (compile the source using the generated Makefile), then `sudo make install` (copy compiled files to the system). This sequence cannot be reordered — make requires the Makefile that configure generates, and install requires the compiled binaries that make produces.

---

**Question 11** (5 points)

An administrator wants to list all files installed by the `openssh-server` package on an Ubuntu system. Which command is correct?

A. `apt files openssh-server`

B. `dpkg -L openssh-server`

C. `apt-cache show openssh-server`

D. `dpkg -S openssh-server`

**Correct Answer:** B

**Explanation:** `dpkg -L PACKAGE` lists all files owned by an installed package (L = list files). `dpkg -S FILE` does the reverse — finds which package owns a specific file. `apt-cache show` displays package metadata like description, version, and dependencies, not file lists. `apt files` is not a valid command.

---

**Question 12** (5 points)

Which command removes packages that were automatically installed as dependencies but are no longer needed by any manually installed package?

A. `sudo apt clean`

B. `sudo apt autoremove`

C. `sudo apt purge --auto`

D. `sudo dpkg --remove-orphans`

**Correct Answer:** B

**Explanation:** `apt autoremove` removes packages that were installed as dependencies but are no longer required. These "orphaned" dependencies accumulate over time as software is removed. `apt clean` removes downloaded package cache files from `/var/cache/apt/archives/` but does not remove any installed packages. The other options are not valid commands.

---

**Question 13** (5 points)

An administrator adds a third-party GPG key to verify packages from a new repository. Where does the key belong on a modern Debian/Ubuntu system using the recommended approach?

A. `/etc/apt/trusted.gpg`

B. `/etc/apt/trusted.gpg.d/`

C. `/usr/share/keyrings/`

D. `/etc/apt/keyrings/`

**Correct Answer:** D

**Explanation:** The current recommended practice (Debian/Ubuntu) is to store third-party repository keys in `/etc/apt/keyrings/` as dearmored (binary) `.gpg` files, and then reference them in the `.sources` or `.list` file with `signed-by=/etc/apt/keyrings/keyname.gpg`. `/etc/apt/trusted.gpg` and `trusted.gpg.d/` are the legacy approach that added keys to the global trust store — the modern approach scopes keys to specific repositories. `/usr/share/keyrings/` is used by distribution packages, not administrators.

---

**Question 14** (5 points)

What is the purpose of `dnf makecache` on a RHEL system?

A. It builds a local RPM database from installed packages.

B. It downloads and stores repository metadata locally to speed up subsequent operations.

C. It removes old cached packages from `/var/cache/dnf/`.

D. It verifies the integrity of all installed packages.

**Correct Answer:** B

**Explanation:** `dnf makecache` downloads repository metadata (package lists, checksums, descriptions) from all enabled repositories and stores it locally. Subsequent `dnf install`, `dnf search`, and `dnf info` commands use this cached metadata instead of downloading it fresh each time, which speeds up operations significantly. `dnf clean all` removes cached data. `rpm -Va` verifies installed packages. There is no separate RPM database rebuild command needed in normal operation.

---

**Question 15** (5 points)

An administrator installs a `.deb` file directly with `sudo dpkg -i package.deb`. The installation fails with "dependency problems." What is the correct follow-up command to automatically resolve the missing dependencies?

A. `sudo apt install --fix-depends`

B. `sudo apt --fix-broken install`

C. `sudo dpkg --fix-missing package.deb`

D. `sudo apt-get dep-install package.deb`

**Correct Answer:** B

**Explanation:** When `dpkg -i` fails due to missing dependencies, the package is left in a partially installed state. Running `sudo apt --fix-broken install` (equivalent to `apt -f install`) instructs apt to download and install any missing dependencies, then complete the package configuration. This is the standard recovery procedure after a failed `dpkg -i`. The other commands are either invalid or do not perform dependency resolution.

---

**Question 16** (5 points)

What information does `rpm -qi packagename` provide that `rpm -q packagename` does not?

A. A list of files installed by the package

B. The full package metadata including description, version, license, URL, and install date

C. The package's GPG signature status

D. The list of other packages that depend on this package

**Correct Answer:** B

**Explanation:** `rpm -q PACKAGE` shows only the package name-version-release string (e.g., `nginx-1.20.1-10.el9.x86_64`). Adding the `-i` flag (info) displays full metadata: description, architecture, size, license, URL, build date, install date, packager, and more. `-l` lists files. `rpm -q --whatrequires` shows reverse dependencies. `rpm -K` checks GPG signatures.

---

**Question 17** (5 points)

An administrator runs `sudo dnf update` and the kernel is updated. After rebooting, the old kernel still appears in the GRUB menu. What controls how many old kernel versions are retained?

A. The `keepcache` setting in `/etc/dnf/dnf.conf`

B. The `installonly_limit` setting in `/etc/dnf/dnf.conf`

C. The `kernel_retain` setting in `/boot/grub2/grub.cfg`

D. Old kernels must be removed manually with `rpm -e`

**Correct Answer:** B

**Explanation:** `installonly_limit` in `/etc/dnf/dnf.conf` controls how many versions of "install-only" packages (like the kernel) are kept. The default is 3. When a new kernel is installed and the limit is exceeded, dnf automatically removes the oldest kernel version. `keepcache` controls whether downloaded package files are retained after installation. GRUB configuration is generated automatically and is not where this is configured.

---

**Question 18** (5 points)

Which of the following is a key advantage of Flatpak/Snap packages over distribution packages?

A. They are smaller in size because they share all system libraries.

B. They can run on any Linux distribution without modification and include their own dependencies.

C. They receive security updates faster because they bypass package manager verification.

D. They are always more secure than distribution packages because they require root to install.

**Correct Answer:** B

**Explanation:** Flatpak and Snap packages bundle their own dependencies in a sandboxed environment, making them distribution-agnostic — the same package works on Ubuntu, Fedora, or any other Linux system. This solves the "works on my distribution" problem. The tradeoff is larger package sizes (dependencies are not shared) and potential lag in security updates because the app maintainer, not the distribution, must update bundled libraries. They do not require root to install (Flatpak can install per-user without root).

---

**Question 19** (5 points)

After adding a new repository to `/etc/yum.repos.d/`, a `dnf install` command fails with `repomd.xml: [Errno 14] HTTP Error 404 - Not Found`. What is the most likely cause?

A. The GPG key for the repository has not been imported.

B. The `baseurl` in the `.repo` file points to an invalid or incorrect URL.

C. The repository requires `sudo` to access.

D. The repository is disabled; use `--enablerepo` to activate it.

**Correct Answer:** B

**Explanation:** HTTP 404 means the URL was reached but the resource was not found. The `repomd.xml` file is the repository metadata index. A 404 error on this file almost always means the `baseurl=` or `mirrorlist=` URL in the `.repo` file is incorrect — either a typo, the wrong architecture in the URL, or the repository has moved. A missing GPG key would produce a different error. Repositories without `enabled=0` are active by default.

---

**Question 20** (5 points)

What is the difference between `apt upgrade` and `apt full-upgrade` (`apt-get dist-upgrade`)?

A. `apt upgrade` installs new packages; `apt full-upgrade` only updates existing ones.

B. `apt upgrade` never removes packages; `apt full-upgrade` may remove packages to resolve dependency conflicts.

C. `apt upgrade` requires internet access; `apt full-upgrade` works offline.

D. There is no functional difference — they are synonyms.

**Correct Answer:** B

**Explanation:** `apt upgrade` upgrades all installed packages but will NOT remove any package, even if a dependency conflict requires removal to complete an upgrade. Packages that cannot be upgraded without removing something are "held back." `apt full-upgrade` (the newer name for `apt-get dist-upgrade`) performs a smarter upgrade that may remove packages if necessary to resolve dependency changes — this is appropriate when upgrading to a new distribution release. `apt full-upgrade` does not install entirely new packages unless they are pulled in as dependencies.

---

**Answer Key Summary**

| Question | Answer |
|---|---|
| 1 | B |
| 2 | A |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | C |
| 7 | A |
| 8 | B |
| 9 | C |
| 10 | B |
| 11 | B |
| 12 | B |
| 13 | D |
| 14 | B |
| 15 | B |
| 16 | B |
| 17 | B |
| 18 | B |
| 19 | B |
| 20 | B |
