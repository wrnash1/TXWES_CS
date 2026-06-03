# Lab: Module 14 — SSH and Remote Administration

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Lab Overview

**Estimated Time:** 60–75 minutes

**Environment:** A Linux VM with SSH server (`sshd`) installed and running. The lab performs self-connections (localhost) for most tasks, so a single VM is sufficient. An optional second VM is noted where it enhances the exercise.

**Objectives:**

- Generate Ed25519 and RSA SSH key pairs
- Deploy public keys and verify key-based authentication
- Harden the SSH server configuration
- Transfer files using `scp` and `sftp`
- Create an SSH local port forwarding tunnel
- Write a basic Ansible inventory and run an ad-hoc command

---

### Lab Environment Setup

Verify SSH server is running:

```bash
systemctl status sshd
ss -tlnp | grep :22
```

If `sshd` is not running:

```bash
sudo systemctl enable --now sshd
```

---

### Part 1: SSH Key Generation

**Task 1.1 — Generate an Ed25519 Key**

```bash
ssh-keygen -t ed25519 -C "lab-key-$(hostname)" -f ~/.ssh/lab_ed25519
```

When prompted for a passphrase, enter a passphrase (do not leave it empty).

Verify the files were created:

```bash
ls -la ~/.ssh/lab_ed25519 ~/.ssh/lab_ed25519.pub
```

Record:

- What are the permissions on the private key?
- What are the permissions on the public key?

**Task 1.2 — Generate an RSA 4096 Key**

```bash
ssh-keygen -t rsa -b 4096 -C "lab-rsa-key" -f ~/.ssh/lab_rsa
```

Verify:

```bash
ls -la ~/.ssh/lab_rsa ~/.ssh/lab_rsa.pub
```

**Task 1.3 — View Key Fingerprints**

```bash
ssh-keygen -lf ~/.ssh/lab_ed25519.pub
ssh-keygen -lf ~/.ssh/lab_rsa.pub
```

Record the fingerprint and algorithm for each key.

**Task 1.4 — View the Public Key Content**

```bash
cat ~/.ssh/lab_ed25519.pub
```

Identify the three components: algorithm, base64 key data, and comment.

---

### Part 2: Public Key Deployment

**Task 2.1 — Deploy the Key to localhost**

For this lab, we deploy the key to the same machine (connecting to localhost):

```bash
ssh-copy-id -i ~/.ssh/lab_ed25519.pub $(whoami)@localhost
```

You will be prompted for your user's password. After successful copy, verify:

```bash
cat ~/.ssh/authorized_keys
```

Confirm your Ed25519 public key appears.

**Task 2.2 — Test Key Authentication**

```bash
ssh -i ~/.ssh/lab_ed25519 $(whoami)@localhost
```

You should be prompted for the key passphrase (not your account password). Type the passphrase you set.

Once connected, verify you are on the same machine:

```bash
hostname
exit
```

**Task 2.3 — Use ssh-agent to Avoid Repeated Passphrase Entry**

```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/lab_ed25519
```

Enter the passphrase when prompted. Now test connecting without being prompted:

```bash
ssh -i ~/.ssh/lab_ed25519 $(whoami)@localhost
```

The agent provides the key automatically. Exit the session.

List keys in the agent:

```bash
ssh-add -l
```

---

### Part 3: SSH Server Hardening

**IMPORTANT:** Before making any changes to `sshd_config`, open a second terminal session to the server. Keep this second terminal open throughout Part 3. If a configuration error locks you out, you can fix it from the second terminal.

**Task 3.1 — Backup sshd_config**

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

**Task 3.2 — View Current Configuration**

```bash
grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"
```

Record which key directives are currently set and their values.

**Task 3.3 — Apply Hardening Settings**

Edit `sshd_config`:

```bash
sudo nano /etc/ssh/sshd_config
```

Locate and modify (or add) these directives:

```
PermitRootLogin no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
X11Forwarding no
```

**Do NOT set `PasswordAuthentication no` yet** — wait until key auth is fully verified.

**Task 3.4 — Test Config Syntax**

```bash
sudo sshd -t
```

No output means the configuration is valid. If errors appear, fix them before continuing.

**Task 3.5 — Reload sshd**

```bash
sudo systemctl reload sshd
```

**Task 3.6 — Verify Changes**

From a new SSH connection (not the existing terminal):

```bash
ssh -i ~/.ssh/lab_ed25519 $(whoami)@localhost
```

Confirm you can still connect. If you cannot, use your backup terminal to restore:

```bash
sudo cp /etc/ssh/sshd_config.backup /etc/ssh/sshd_config
sudo systemctl reload sshd
```

**Task 3.7 — Create a Login Banner**

```bash
sudo bash -c 'cat > /etc/ssh/ssh_banner << EOF
*************************************************************
AUTHORIZED ACCESS ONLY - CIS-3325 Lab System
All activity is monitored and logged.
*************************************************************
EOF'
```

Add to sshd_config:

```
Banner /etc/ssh/ssh_banner
```

Reload and test:

```bash
sudo systemctl reload sshd
ssh -i ~/.ssh/lab_ed25519 $(whoami)@localhost
```

Confirm the banner appears before authentication.

---

### Part 4: Secure File Transfer

**Task 4.1 — SCP File Copy**

Create a test file:

```bash
echo "SCP lab test file - $(date)" > /tmp/scp_test.txt
```

Copy it to a remote directory (using localhost):

```bash
scp -i ~/.ssh/lab_ed25519 /tmp/scp_test.txt $(whoami)@localhost:/tmp/scp_remote.txt
```

Verify:

```bash
ls -la /tmp/scp_remote.txt
cat /tmp/scp_remote.txt
```

**Task 4.2 — SCP Directory Copy**

Create a test directory:

```bash
mkdir -p /tmp/scp_dir/{subdir1,subdir2}
echo "file1" > /tmp/scp_dir/file1.txt
echo "file2" > /tmp/scp_dir/subdir1/file2.txt
```

Copy the directory recursively:

```bash
scp -r -i ~/.ssh/lab_ed25519 /tmp/scp_dir $(whoami)@localhost:/tmp/scp_dir_remote
```

Verify:

```bash
find /tmp/scp_dir_remote -type f
```

**Task 4.3 — SFTP Session**

Start an SFTP session to localhost:

```bash
sftp -i ~/.ssh/lab_ed25519 $(whoami)@localhost
```

Once connected, practice these commands:

```
sftp> pwd
sftp> ls /tmp
sftp> cd /tmp
sftp> get scp_test.txt /tmp/sftp_download.txt
sftp> put /tmp/scp_test.txt sftp_upload.txt
sftp> ls sftp_upload.txt
sftp> exit
```

Verify the downloaded file:

```bash
cat /tmp/sftp_download.txt
```

---

### Part 5: SSH Port Forwarding

**Task 5.1 — Start a Simple HTTP Server**

Start a basic Python HTTP server on port 8888 for testing:

```bash
cd /tmp && python3 -m http.server 8888 &
HTTP_PID=$!
```

Verify it is running:

```bash
ss -tlnp | grep 8888
```

**Task 5.2 — Create a Local Port Forward**

Open a tunnel that forwards local port 9999 to localhost:8888 through an SSH connection:

```bash
ssh -f -N -L 9999:localhost:8888 -i ~/.ssh/lab_ed25519 $(whoami)@localhost
```

**Task 5.3 — Test the Tunnel**

```bash
curl http://localhost:9999/ 2>/dev/null | head -5
```

You should see an HTML directory listing from the Python HTTP server, accessed through the SSH tunnel.

**Task 5.4 — Cleanup**

Kill the tunnel and HTTP server:

```bash
kill $(lsof -ti:9999 2>/dev/null)
kill $HTTP_PID 2>/dev/null
```

---

### Part 6: Ansible Basics

**Task 6.1 — Install Ansible**

```bash
# RHEL/Rocky:
sudo dnf install ansible -y

# Ubuntu:
sudo apt install ansible -y
```

Verify:

```bash
ansible --version
```

**Task 6.2 — Create an Inventory File**

```bash
cat > /tmp/lab_inventory.ini << EOF
[local]
localhost ansible_connection=local

[local:vars]
ansible_python_interpreter=/usr/bin/python3
EOF
```

**Task 6.3 — Test Connectivity**

```bash
ansible -i /tmp/lab_inventory.ini local -m ping
```

You should see:

```
localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

**Task 6.4 — Run Ad-hoc Commands**

```bash
ansible -i /tmp/lab_inventory.ini local -m command -a "uptime"
ansible -i /tmp/lab_inventory.ini local -m shell -a "df -h /"
ansible -i /tmp/lab_inventory.ini local -m setup -a "filter=ansible_os_family"
```

Record the output of each command.

**Task 6.5 — Write a Simple Playbook**

```bash
cat > /tmp/lab_playbook.yml << 'EOF'
---
- name: CIS-3325 Lab Playbook
  hosts: local
  gather_facts: yes

  tasks:
    - name: Print system information
      debug:
        msg: "Host: {{ ansible_hostname }}, OS: {{ ansible_distribution }} {{ ansible_distribution_version }}"

    - name: Create a lab directory
      file:
        path: /tmp/ansible_lab
        state: directory
        mode: '0755'

    - name: Write a test file
      copy:
        content: "Ansible lab file created at {{ ansible_date_time.iso8601 }}\n"
        dest: /tmp/ansible_lab/test.txt
EOF
```

Run the playbook:

```bash
ansible-playbook -i /tmp/lab_inventory.ini /tmp/lab_playbook.yml
```

Verify:

```bash
cat /tmp/ansible_lab/test.txt
```

**Task 6.6 — Dry Run**

```bash
ansible-playbook -i /tmp/lab_inventory.ini /tmp/lab_playbook.yml --check
```

The `--check` flag shows what would change without making changes.

---

### Lab Cleanup

```bash
# Restore original sshd_config
sudo cp /etc/ssh/sshd_config.backup /etc/ssh/sshd_config
sudo systemctl reload sshd

# Remove test keys from authorized_keys
# Edit authorized_keys and remove the lab_ed25519 line
nano ~/.ssh/authorized_keys

# Remove test files
rm -f /tmp/scp_test.txt /tmp/scp_remote.txt /tmp/sftp_download.txt
rm -rf /tmp/scp_dir /tmp/scp_dir_remote /tmp/ansible_lab
rm -f /tmp/lab_inventory.ini /tmp/lab_playbook.yml
rm -f ~/.ssh/lab_ed25519 ~/.ssh/lab_ed25519.pub
rm -f ~/.ssh/lab_rsa ~/.ssh/lab_rsa.pub
sudo rm -f /etc/ssh/ssh_banner
```

---

### Lab Submission Requirements

Submit a PDF report containing:

1. Key fingerprints from Task 1.3
2. Screenshot of successful key-based authentication (Task 2.2 terminal output)
3. Screenshot of banner display before authentication (Task 3.7)
4. Output of the Ansible ping test (Task 6.3) and playbook run (Task 6.5)
5. Brief paragraph explaining why keeping a second terminal open during `sshd_config` changes is essential operational procedure

---

### Grading Rubric

| Section | Points |
|---------|--------|
| Part 1: Key generation and inspection | 15 |
| Part 2: Key deployment and agent | 20 |
| Part 3: sshd_config hardening | 25 |
| Part 4: SCP and SFTP transfers | 15 |
| Part 5: Port forwarding | 10 |
| Part 6: Ansible basics | 10 |
| Written explanation | 5 |
| **Total** | **100** |
