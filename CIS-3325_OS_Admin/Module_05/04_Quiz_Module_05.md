# Quiz: Module 05 - Package Management
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
A systems administrator on an Ubuntu server needs to install the `nginx` web server package from the official repositories. Which command sequence is correct?
A) rpm -ivh nginx && rpm -e nginx
B) apt update && apt install nginx
C) dnf install nginx --enablerepo=base
D) dpkg -i nginx && apt resolve nginx
*   **Correct Answer:** B) apt update && apt install nginx
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `rpm` is the Red Hat package tool and does not function on Ubuntu/Debian systems, which use the `.deb` format and dpkg/apt toolchain.
    *   *Why C is incorrect:* `dnf` is the package manager for Red Hat-based distributions (RHEL, Fedora, CentOS). It is not available on Ubuntu by default.
    *   *Why D is incorrect:* `dpkg -i` requires a local `.deb` file path, not a package name. There is no `apt resolve` subcommand — dependency resolution is handled automatically by `apt install`.

---

---

**Question 2**
An administrator on a RHEL 8 system suspects that the files installed by the `openssh-server` package have been tampered with. Which command verifies the integrity of the installed package files against the RPM database?
A) rpm -qa openssh-server
B) rpm -ql openssh-server
C) rpm -V openssh-server
D) rpm -qf openssh-server
*   **Correct Answer:** C) rpm -V openssh-server
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `rpm -qa` queries and lists all installed packages (or a specific one when a name is given). It does not perform integrity verification.
    *   *Why B is incorrect:* `rpm -ql` lists all files that were installed by the package. It does not check whether those files have been modified since installation.
    *   *Why D is incorrect:* `rpm -qf` is used to identify which package owns a specific file path (e.g., `rpm -qf /etc/ssh/sshd_config`). It does not verify integrity.

---

---

**Question 3**
A systems administrator needs to list all currently running processes on the system along with their CPU and memory usage. Which command is most appropriate?
A) ps aux
B) df -h
C) lsblk
D) netstat -tuln
*   **Correct Answer:** A) ps aux
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `df -h` reports disk space usage on mounted filesystems, not process information.
    *   *Why C is incorrect:* `lsblk` lists block devices (disks and partitions) and their mount points, not running processes.
    *   *Why D is incorrect:* `netstat -tuln` shows active network connections and listening ports, not CPU/memory usage of processes.

---

**Question 4**
An administrator removes a package on Ubuntu using `apt remove nginx` but later discovers the nginx configuration files are still present in `/etc/nginx/`. Which command should have been used to remove the package AND all its configuration files?
A) apt delete nginx
B) apt purge nginx
C) dpkg -r nginx
D) apt autoremove nginx
*   **Correct Answer:** B) apt purge nginx
*   **Distractor Analysis:**
    *   *Why A is incorrect:* There is no `apt delete` subcommand. This will produce an error.
    *   *Why C is incorrect:* `dpkg -r` removes the package binaries like `apt remove` does, but also leaves configuration files behind. Only `dpkg --purge` removes config files, but `apt purge` is the cleaner high-level equivalent.
    *   *Why D is incorrect:* `apt autoremove` removes packages that were automatically installed as dependencies and are no longer needed by any explicitly installed package. It does not target a specific package's configuration files.

---

**Question 5**
A Linux administrator needs to identify which installed package owns the file `/usr/sbin/sshd` on a Red Hat-based system. Which command achieves this?
A) rpm -ql sshd
B) rpm -Va /usr/sbin/sshd
C) rpm -qf /usr/sbin/sshd
D) dnf provides /usr/sbin/sshd
*   **Correct Answer:** C) rpm -qf /usr/sbin/sshd
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `rpm -ql` lists files owned by a package when you already know the package name. It requires a package name as the argument, not a file path, and works in the opposite direction.
    *   *Why B is incorrect:* `rpm -Va` verifies all installed packages against the RPM database, checking for file modifications. It does not identify the package that owns a specific file.
    *   *Why D is incorrect:* `dnf provides` queries the repository metadata to find which package in the repos provides a file — useful before installation. However, for a file already on disk, `rpm -qf` is the direct and correct tool.

