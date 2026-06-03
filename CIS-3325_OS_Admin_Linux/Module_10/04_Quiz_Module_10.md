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
