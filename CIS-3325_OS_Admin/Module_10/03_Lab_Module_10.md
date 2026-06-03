# Lab 10: SSH and Remote Access Security

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will generate SSH key pairs, configure key-based authentication, harden the
SSH server configuration, use scp and rsync for file transfers, and configure the SSH client
with ~/.ssh/config.

**What you will practice:**

- ssh-keygen for key pair generation
- ssh-copy-id and authorized_keys configuration
- SSH permission requirements
- sshd_config hardening directives
- scp file transfers
- rsync synchronization with and without --delete
- ~/.ssh/config client configuration

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin
- You have watched both parts of the Module 10 video lecture
- For key transfer exercises, you will connect from the VM to itself (localhost) to simulate a remote server

---

### Part 1 - SSH Key Generation

**Step 1.1 - Generate an Ed25519 key pair**

```bash
ssh-keygen -t ed25519 -C "labadmin-lab10"
```

When prompted:
- File location: press Enter to accept the default (~/.ssh/id_ed25519)
- Passphrase: enter a passphrase you will remember for this lab

**Step 1.2 - Examine the generated files**

```bash
ls -la ~/.ssh/
```

Record the permissions on each file. Identify which file is the private key and which is
the public key.

```bash
cat ~/.ssh/id_ed25519.pub
```

Note the structure: algorithm, key data, and your comment at the end.

**Step 1.3 - Verify key permissions**

```bash
stat ~/.ssh/
stat ~/.ssh/id_ed25519
stat ~/.ssh/id_ed25519.pub
```

Record the permission bits shown for each.

**Step 1.4 - Demonstrate incorrect permissions**

```bash
chmod 755 ~/.ssh/
ssh -v labadmin@localhost 2>&1 | grep -A2 "identity"
```

Note the verbose output mentioning permission problems.

Restore correct permissions:

```bash
chmod 700 ~/.ssh/
```

---

### Part 2 - Key-Based Authentication Setup

**Step 2.1 - Create a second test user**

```bash
sudo useradd -m -s /bin/bash sshtest
sudo passwd sshtest
```

Enter a simple password for this lab user.

**Step 2.2 - Copy the public key to the test user**

```bash
ssh-copy-id sshtest@localhost
```

Enter the password for sshtest when prompted.

**Step 2.3 - Test key-based login**

```bash
ssh sshtest@localhost
```

You should be prompted for your SSH key passphrase (not sshtest's password). After entering
the passphrase, you are logged in as sshtest.

```bash
whoami
exit
```

**Step 2.4 - Examine the authorized_keys file**

```bash
sudo cat /home/sshtest/.ssh/authorized_keys
```

The file contains your public key.

```bash
sudo ls -la /home/sshtest/.ssh/
```

Verify the permissions: ~/.ssh should be 700 and authorized_keys should be 600.

---

### Part 3 - sshd_config Hardening

**Step 3.1 - Backup the original configuration**

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.lab10.bak
```

**Step 3.2 - View the current active configuration**

```bash
sudo grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"
```

**Step 3.3 - Test syntax before making changes**

```bash
sudo sshd -t
echo "Syntax OK: $?"
```

A return code of 0 means the syntax is valid.

**Step 3.4 - Modify sshd_config**

```bash
sudo nano /etc/ssh/sshd_config
```

Make the following changes (uncomment or add the lines):

```
PermitRootLogin no
MaxAuthTries 3
LoginGraceTime 30
```

**Step 3.5 - Test the modified configuration**

```bash
sudo sshd -t
```

If the test passes, restart the service:

```bash
sudo systemctl restart sshd
systemctl status sshd
```

**Step 3.6 - Verify root login is blocked**

```bash
ssh root@localhost
```

Expected result: "Permission denied, please try again" or "root@localhost: Permission denied."

---

### Part 4 - File Transfers with scp

**Step 4.1 - Create test files**

```bash
mkdir -p ~/lab10_files
echo "File 1 content" > ~/lab10_files/file1.txt
echo "File 2 content" > ~/lab10_files/file2.txt
echo "File 3 content" > ~/lab10_files/file3.txt
```

**Step 4.2 - Copy a single file to a remote location**

```bash
scp ~/lab10_files/file1.txt sshtest@localhost:/home/sshtest/
```

**Step 4.3 - Verify the file was copied**

```bash
ssh sshtest@localhost "ls -la /home/sshtest/"
```

**Step 4.4 - Copy a file from remote to local**

```bash
scp sshtest@localhost:/home/sshtest/file1.txt /tmp/file1_from_remote.txt
cat /tmp/file1_from_remote.txt
```

**Step 4.5 - Copy a directory recursively**

```bash
scp -r ~/lab10_files/ sshtest@localhost:/home/sshtest/lab10_files_copy/
ssh sshtest@localhost "ls -la /home/sshtest/lab10_files_copy/"
```

---

### Part 5 - rsync Synchronization

**Step 5.1 - Create a source directory**

```bash
mkdir -p ~/rsync_source
echo "Alpha" > ~/rsync_source/alpha.txt
echo "Beta"  > ~/rsync_source/beta.txt
echo "Gamma" > ~/rsync_source/gamma.txt
```

**Step 5.2 - rsync dry run**

```bash
rsync -avn ~/rsync_source/ sshtest@localhost:/home/sshtest/rsync_dest/
```

Note which files would be transferred. No actual transfer occurs.

**Step 5.3 - rsync actual transfer**

```bash
rsync -av ~/rsync_source/ sshtest@localhost:/home/sshtest/rsync_dest/
```

**Step 5.4 - Verify the destination**

```bash
ssh sshtest@localhost "ls -la /home/sshtest/rsync_dest/"
```

**Step 5.5 - Demonstrate incremental sync**

Add a new file to the source:

```bash
echo "Delta" > ~/rsync_source/delta.txt
rsync -av ~/rsync_source/ sshtest@localhost:/home/sshtest/rsync_dest/
```

Note that only delta.txt is transferred this time.

**Step 5.6 - Demonstrate --delete**

Remove a file from the source:

```bash
rm ~/rsync_source/alpha.txt
rsync -avn --delete ~/rsync_source/ sshtest@localhost:/home/sshtest/rsync_dest/
```

The dry run shows that alpha.txt would be deleted from the destination.

```bash
rsync -av --delete ~/rsync_source/ sshtest@localhost:/home/sshtest/rsync_dest/
ssh sshtest@localhost "ls /home/sshtest/rsync_dest/"
```

alpha.txt is no longer in the destination.

---

### Part 6 - SSH Client Configuration

**Step 6.1 - Create ~/.ssh/config**

```bash
cat > ~/.ssh/config << 'EOF'
Host lab10local
    HostName localhost
    User sshtest
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60

Host *
    ServerAliveCountMax 3
EOF
chmod 600 ~/.ssh/config
```

**Step 6.2 - Test the alias**

```bash
ssh lab10local
whoami
exit
```

The connection uses the settings from ~/.ssh/config without typing the full command.

**Step 6.3 - Use the alias with scp**

```bash
scp ~/lab10_files/file2.txt lab10local:/home/sshtest/
```

---

### Part 7 - Analysis Questions

**Question 1:** A colleague generates an SSH key pair and copies both id_rsa and id_rsa.pub to the remote server's ~/.ssh/ directory. Explain why copying the private key is a serious security mistake. What can an attacker do if they gain access to the remote server and find the private key? What is the correct procedure?

**Question 2:** After setting PasswordAuthentication no in sshd_config and restarting sshd, a user reports they can no longer log in with their password (as expected) but also cannot log in with their key. They receive "Permission denied (publickey)." List at least three possible causes and the command to check each one.

**Question 3:** You run ssh-keygen and choose NOT to set a passphrase on the private key. Describe the security trade-off: what is the convenience benefit, what is the security risk if the private key file is compromised, and what mechanism (other than a passphrase) can partially mitigate the risk?

**Question 4:** Explain why sshd -t should always be run before systemctl restart sshd after editing sshd_config. Describe the specific failure scenario where skipping this test could leave an administrator locked out of a remote server.

**Question 5:** Write the rsync command that would create a nightly backup of /var/www/html/ on server1 to /backups/www/ on server2 (accessible as webbackup in ~/.ssh/config), preserving all permissions and timestamps, compressing data in transit, and automatically removing files from the destination that have been deleted from the source. The command should be safe to schedule in cron.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.2 showing ls -la ~/.ssh/ with the generated key files
2. Screenshot of Part 2, Step 2.4 showing the authorized_keys file content and permissions
3. Screenshot of Part 3, Step 3.6 showing root login being denied after PermitRootLogin no
4. Screenshot of Part 4, Step 4.5 showing the recursive scp directory transfer
5. Screenshot of Part 5, Step 5.6 showing the rsync --delete dry run and actual deletion
6. Screenshot of Part 6, Step 6.2 showing the successful ssh lab10local connection
7. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Key files with permissions screenshot | 10 |
| authorized_keys content screenshot | 10 |
| Root login denied screenshot | 10 |
| Recursive scp screenshot | 10 |
| rsync --delete screenshot | 10 |
| SSH config alias screenshot | 10 |
| Analysis Question 1 (private key mistake) | 5 |
| Analysis Question 2 (publickey denied diagnosis) | 5 |
| Analysis Question 3 (passphrase trade-off) | 5 |
| Analysis Question 4 (sshd -t importance) | 10 |
| Analysis Question 5 (rsync cron command) | 15 |
| **Total** | **100** |
