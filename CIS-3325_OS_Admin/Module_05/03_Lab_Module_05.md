# Lab 05: Package Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will install and remove packages using apt, query the dpkg database, add a
third-party repository, and verify package integrity. You will practice both high-level apt
commands and low-level dpkg commands for the same operations to understand what each layer does.

**What you will practice:**

- apt update, install, remove, and purge
- dpkg -l, -L, -S, and -s for package queries
- Adding a third-party repository and its GPG key
- apt show and apt search
- Understanding the difference between remove and purge

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running and has internet access
- You are logged in as labadmin
- You have watched both parts of the Module 05 video lecture
- You have read the Module 05 Reading Guide

---

### Part 1 - Package Database Queries

**Step 1.1 - Count installed packages**

```bash
dpkg -l | wc -l
```

This counts all lines in the dpkg list output, giving an approximate count of installed packages.

```bash
dpkg -l | grep "^ii" | wc -l
```

The "^ii" pattern matches lines starting with ii, which represents correctly installed packages.
This gives the actual installed package count.

**Step 1.2 - Find a specific package**

```bash
dpkg -l | grep ssh
```

Search for SSH-related packages. Note which are installed (ii) versus not installed (rc = removed
but config remains, un = unknown/not installed).

**Step 1.3 - List files installed by a package**

```bash
dpkg -L openssh-server
```

This lists every file that the openssh-server package placed on your system. Note the configuration
files in /etc/ssh/ and the binary in /usr/sbin/sshd.

**Step 1.4 - Find the package that owns a file**

```bash
dpkg -S /usr/sbin/sshd
```

This identifies which package installed /usr/sbin/sshd. The answer should be openssh-server.

```bash
dpkg -S /bin/ls
```

Find which package installed the ls command.

**Step 1.5 - Show package details**

```bash
dpkg -s openssh-server
```

Shows full status information including version, architecture, description, and dependencies.

---

### Part 2 - Installing and Removing Packages

**Step 2.1 - Update the package list**

```bash
sudo apt update
```

This refreshes the list of available packages from all configured repositories. Always run this
before installing new packages.

Note: apt update does NOT install anything. It only refreshes metadata.

**Step 2.2 - Install a package**

```bash
sudo apt install -y tree
```

tree is a utility that displays directory structures in a visual tree format. The -y flag
skips the confirmation prompt.

```bash
tree /etc/ssh/
```

Test that tree was installed successfully.

**Step 2.3 - Install multiple packages at once**

```bash
sudo apt install -y htop curl wget
```

Multiple packages can be installed in one command. apt resolves all dependencies and installs
everything in a single operation.

**Step 2.4 - Show package information before installing**

```bash
apt show nginx
```

Review the package details including version, size, dependencies, and description.

**Step 2.5 - Remove a package (keep config)**

```bash
sudo apt remove tree
```

Remove tree but keep any configuration files.

```bash
dpkg -l | grep tree
```

After removal, the package shows as rc (removed, config retained) if it had config files,
or the line disappears entirely.

```bash
which tree
```

tree is no longer in the PATH because the binary was removed.

**Step 2.6 - Reinstall and then purge**

```bash
sudo apt install -y tree
sudo apt purge tree
dpkg -l | grep tree
```

After purge, the package should not appear with rc status. All traces are removed.

**Step 2.7 - Remove unused dependencies**

```bash
sudo apt autoremove -y
```

This removes automatically installed packages that are no longer needed by any explicitly
installed package.

---

### Part 3 - Searching and Browsing Packages

**Step 3.1 - Search the package database**

```bash
apt search "disk usage"
```

Find packages related to disk usage analysis. Note the results.

```bash
apt search "^ncdu"
```

The ^ anchors the search to the beginning of the package name. This finds packages named
exactly ncdu.

**Step 3.2 - Install a searched package**

```bash
sudo apt install -y ncdu
ncdu /home
```

ncdu is an interactive disk usage viewer. Navigate with arrow keys, press q to quit.

**Step 3.3 - List available upgrades**

```bash
apt list --upgradable 2>/dev/null
```

Shows packages with available updates. The 2>/dev/null suppresses a warning about unstable
CLI interface.

---

### Part 4 - Adding a Third-Party Repository

We will add the GitHub CLI repository as an example of third-party repository management.

**Step 4.1 - Import the GPG key**

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
```

**Step 4.2 - Add the repository**

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
```

**Step 4.3 - Update and install**

```bash
sudo apt update
apt show gh
```

The gh package is now visible from the new repository. Note the source repository shown.

```bash
sudo apt install -y gh
gh --version
```

The GitHub CLI is now installed from the third-party repository.

**Step 4.4 - Examine the repository configuration**

```bash
cat /etc/apt/sources.list.d/github-cli.list
ls /usr/share/keyrings/ | grep github
```

---

### Part 5 - Package Integrity Verification

**Step 5.1 - Install debsums**

```bash
sudo apt install -y debsums
```

debsums provides MD5 checksum verification for installed packages on Debian/Ubuntu systems.

**Step 5.2 - Verify an installed package**

```bash
sudo debsums openssh-server
```

Each line shows a file and its verification status. OK means the file matches the package
database. FAILED would indicate the file has been modified.

**Step 5.3 - Check all packages**

```bash
sudo debsums -c 2>/dev/null | head -20
```

The -c flag shows only changed files. On a clean system this produces no output (all files
are unchanged). Any output indicates modified files.

**Step 5.4 - Demonstrate a modified file detection**

```bash
sudo cp /usr/bin/tree /usr/bin/tree.original
echo "modified" | sudo tee -a /usr/bin/tree > /dev/null
sudo debsums tree
```

After modifying the binary, debsums reports FAILED for the modified file.

Restore the original:

```bash
sudo cp /usr/bin/tree.original /usr/bin/tree
sudo rm /usr/bin/tree.original
sudo debsums tree
```

---

### Part 6 - Analysis Questions

**Question 1:** You ran sudo apt remove nginx and then confirmed nginx is no longer running,
but /etc/nginx/ still exists with your configuration files. Explain why this happens and write
the exact command to completely remove nginx including all configuration files.

**Question 2:** You ran dpkg -S /etc/ssh/sshd_config and saw the output openssh-server:
/etc/ssh/sshd_config. What does this tell you? If you then ran sudo apt purge openssh-server,
would /etc/ssh/sshd_config be deleted? Explain your reasoning.

**Question 3:** You ran debsums openssh-server and saw "FAILED" for /usr/sbin/sshd. What does
this mean? List at least two possible causes and explain how you would investigate further to
determine whether this is a security incident or an authorized change.

**Question 4:** Explain the difference between apt update and apt upgrade. Write a single
command that performs both operations sequentially and is safe to run in a production cron job.

**Question 5:** A colleague suggests installing a package directly with dpkg -i
from a downloaded .deb file instead of using apt install from a repository. Describe
two security disadvantages of this approach compared to installing from an official repository.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.3 showing dpkg -L openssh-server output
2. Screenshot of Part 1, Step 1.4 showing dpkg -S /usr/sbin/sshd and dpkg -S /bin/ls
3. Screenshot of Part 2, Step 2.5 showing apt remove tree and dpkg -l output
4. Screenshot of Part 2, Step 2.6 showing apt purge tree
5. Screenshot of Part 3, Step 3.2 showing ncdu /home running
6. Screenshot of Part 4, Step 4.3 showing apt show gh with repository source
7. Screenshot of Part 5, Step 5.4 showing debsums FAILED for modified tree binary
8. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| dpkg -L openssh-server screenshot | 10 |
| dpkg -S file owner screenshots | 10 |
| apt remove + dpkg status screenshot | 10 |
| apt purge screenshot | 10 |
| ncdu running screenshot | 10 |
| apt show gh with repo source | 10 |
| debsums FAILED detection screenshot | 10 |
| Analysis Question 1 (remove vs purge) | 5 |
| Analysis Question 2 (dpkg -S behavior) | 5 |
| Analysis Question 3 (debsums FAILED) | 5 |
| Analysis Question 4 (update vs upgrade) | 5 |
| Analysis Question 5 (dpkg vs apt security) | 10 |
| **Total** | **100** |
