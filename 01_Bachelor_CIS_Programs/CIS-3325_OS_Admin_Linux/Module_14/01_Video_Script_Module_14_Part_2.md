# Video Script: Module 14 — SSH and Remote Administration (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA Linux+ / Linux Foundation &bull; Operating System Administration &bull; Module 14</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ / Linux Foundation &bull; Operating System Administration" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ / Linux Foundation &bull; Operating System Administration</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

### Introduction

Welcome back to Module 14, Part 2.

In Part 1, we covered SSH key generation, distribution, and server hardening. Now we'll look at secure file transfer with `scp` and `sftp`, SSH port forwarding for tunneling traffic through encrypted channels, and we'll close with Ansible — the tool that turns SSH into a scalable infrastructure management platform.

---

### Section 5: Secure File Transfer — SCP

SCP (Secure Copy Protocol) copies files over an SSH connection. It uses the same authentication as SSH (key or password) and encrypts all data in transit.

**Basic SCP Syntax**

```
scp [options] source destination
```

**Copying a File to a Remote Host**

```bash
scp /path/to/local/file.txt user@hostname:/remote/path/
```

**Copying a File from a Remote Host**

```bash
scp user@hostname:/remote/path/file.txt /local/path/
```

**Copying a Directory (Recursive)**

```bash
scp -r /local/directory/ user@hostname:/remote/path/
```

**Useful SCP Options**

- `-P 2222` — specify a non-default SSH port (capital P, unlike SSH's lowercase `-p`)
- `-i ~/.ssh/id_ed25519` — specify the identity file
- `-p` — preserve timestamps and permissions (lowercase p)
- `-r` — recursive copy
- `-v` — verbose mode for debugging

**SCP Examples**

Copy a backup file to a remote server:

```bash
scp /backup/db-2024-01-15.sql.gz admin@dbbackup:/backups/
```

Copy logs from a remote server for analysis:

```bash
scp -r admin@webserver:/var/log/nginx/ ./nginx-logs/
```

Copy using a specific key and port:

```bash
scp -i ~/.ssh/prod_key -P 2222 app.conf deploy@10.0.0.5:/etc/myapp/
```

**Note on SCP Deprecation**

OpenSSH 9.0 deprecated the legacy SCP protocol and now uses SFTP as the underlying transfer mechanism by default. The `scp` command still works but uses SFTP internally. The `rsync` utility is generally preferred for bulk transfers.

---

### Section 6: SFTP — Interactive File Transfer

SFTP (SSH File Transfer Protocol) provides an interactive, FTP-like interface over SSH. It supports navigation, upload, download, directory creation, and file deletion.

**Starting an SFTP Session**

```bash
sftp user@hostname
sftp -P 2222 user@hostname
```

**SFTP Commands**

Once connected, you interact with the remote system:

```
sftp> pwd              # Remote working directory
sftp> lpwd             # Local working directory
sftp> ls               # List remote files
sftp> lls              # List local files
sftp> cd /var/log      # Change remote directory
sftp> lcd /tmp         # Change local directory
sftp> get file.log     # Download a file
sftp> put backup.tar   # Upload a file
sftp> mget *.log       # Download multiple files
sftp> mput *.conf      # Upload multiple files
sftp> mkdir uploads    # Create remote directory
sftp> rm old-file.log  # Delete remote file
sftp> exit             # Close session
```

**SFTP Chroot Jail**

For secure file delivery to external partners, you can configure SFTP to restrict users to a specific directory. In `sshd_config`:

```
Match User sftpuser
    ForceCommand internal-sftp
    ChrootDirectory /srv/sftp/%u
    PasswordAuthentication yes
    X11Forwarding no
    AllowTcpForwarding no
```

This forces the user `sftpuser` to use SFTP only, restricts them to `/srv/sftp/sftpuser/`, and prevents them from running any shell commands or forwarding ports.

**rsync Over SSH**

For synchronizing directories efficiently:

```bash
rsync -avz -e ssh /local/data/ user@hostname:/remote/data/
```

- `-a` — archive mode (preserves permissions, timestamps, symlinks)
- `-v` — verbose
- `-z` — compress data during transfer
- `-e ssh` — use SSH as transport

`rsync` only transfers changed blocks, making it much faster than `scp` for large or repeated transfers.

---

### Section 7: SSH Port Forwarding

SSH port forwarding (also called SSH tunneling) creates an encrypted tunnel through the SSH connection and redirects traffic through it. This is used to:

- Access services behind firewalls
- Encrypt otherwise unencrypted protocols
- Bypass network restrictions securely

**Local Port Forwarding**

Local port forwarding redirects a port on your local machine through the SSH connection to a destination reached from the remote server.

```bash
ssh -L 8080:internal-server:80 user@bastion
```

This creates a tunnel where:

- Your machine: listens on port `8080`
- Traffic goes through SSH to `bastion`
- From `bastion`, it connects to `internal-server` port `80`

After running this, you open a browser to `http://localhost:8080` and you're accessing `internal-server:80` through the encrypted tunnel.

Use case: accessing an internal web application when you can only reach the bastion host directly.

**Remote Port Forwarding**

Remote port forwarding exposes a port on the remote server that connects back to your local machine.

```bash
ssh -R 9000:localhost:3000 user@publicserver
```

This creates a tunnel where:

- `publicserver` listens on port `9000`
- Traffic connects back through SSH to your local machine port `3000`

Use case: exposing a development server running on your laptop to a colleague on the internet.

**Dynamic Port Forwarding (SOCKS Proxy)**

Dynamic forwarding creates a SOCKS5 proxy on your local machine. All traffic sent to the proxy is forwarded through the SSH connection and exits from the remote server.

```bash
ssh -D 1080 user@remoteserver
```

Configure your browser or application to use SOCKS5 proxy at `127.0.0.1:1080`. All traffic exits from `remoteserver`.

Use case: secure browsing or accessing geo-restricted resources.

**Running Port Forwarding in Background**

For long-running tunnels without an interactive session:

```bash
ssh -f -N -L 8080:internal-server:80 user@bastion
```

- `-f` — go to background before command execution
- `-N` — do not execute a remote command (just the tunnel)

**SSH Tunneling in ~/.ssh/config**

Add persistent tunnels to your SSH config:

```
Host db-tunnel
    HostName bastion.example.com
    User admin
    LocalForward 5432 db.internal:5432
    ServerAliveInterval 60
```

Now `ssh db-tunnel` opens an encrypted tunnel to the database server on port 5432.

---

### Section 8: Ansible Basics

Ansible is an agentless automation tool that uses SSH to configure and manage Linux servers at scale. Instead of logging into each server individually, you write playbooks — YAML configuration files — that Ansible executes across any number of hosts simultaneously.

**Why Ansible**

- **Agentless**: no software needs to be installed on managed hosts — just SSH and Python
- **Idempotent**: running the same playbook twice produces the same result as running it once
- **Declarative**: you describe the desired state, Ansible figures out how to get there
- **Scalable**: manage 1 host or 10,000 hosts with the same playbook

**The Ansible Inventory**

Ansible's inventory file (`/etc/ansible/hosts` or a custom file) lists the hosts to manage:

```ini
[webservers]
web01.example.com
web02.example.com
192.168.1.100

[dbservers]
db01.example.com
db02.example.com

[production:children]
webservers
dbservers
```

**Ad-hoc Commands**

Run a single command across all hosts in a group:

```bash
ansible webservers -m ping
ansible webservers -m command -a "uptime"
ansible all -m shell -a "df -h" -u admin
```

**Playbook Structure**

An Ansible playbook is a YAML file:

```yaml
---
- name: Configure web servers
  hosts: webservers
  become: yes

  tasks:
    - name: Install nginx
      package:
        name: nginx
        state: present

    - name: Start and enable nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Copy configuration file
      copy:
        src: files/nginx.conf
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
      notify: Restart nginx

  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

**Running a Playbook**

```bash
ansible-playbook -i inventory.ini webservers.yml
ansible-playbook -i inventory.ini webservers.yml --check    # Dry run
ansible-playbook -i inventory.ini webservers.yml -v         # Verbose
```

**Key Ansible Modules**

| Module | Purpose |
|--------|---------|
| `package` / `yum` / `apt` | Install/remove packages |
| `service` / `systemd` | Manage services |
| `copy` | Copy files to remote hosts |
| `template` | Deploy Jinja2 templates |
| `file` | Manage file attributes |
| `user` | Manage user accounts |
| `cron` | Manage crontab entries |
| `firewalld` | Manage firewall rules |
| `command` / `shell` | Run arbitrary commands |

**Ansible and SSH**

Ansible uses SSH for all communication. Key points:

- Ansible connects as the specified user (default: current user)
- It uses `sudo` for privilege escalation when `become: yes` is set
- SSH key authentication must be configured on all managed hosts
- Use `--private-key ~/.ssh/ansible_key` to specify a dedicated Ansible key

---

### Summary — Module 14

Module 14 provided comprehensive coverage of SSH and remote administration:

**Part 1:**

- Asymmetric key cryptography principles
- Generating SSH keys with `ssh-keygen` (Ed25519 and RSA)
- Distributing public keys with `ssh-copy-id` and manual installation
- `authorized_keys` format and per-key restrictions
- `sshd_config` hardening: root login, password auth, user restrictions, timeouts, cipher selection

**Part 2:**

- SCP for file copying with key options and port specification
- SFTP interactive sessions and chroot jail configuration
- `rsync` over SSH for efficient synchronization
- Local, remote, and dynamic port forwarding
- Background tunnel creation with `-f -N`
- Ansible: inventory, ad-hoc commands, playbook structure, and core modules

SSH mastery is foundational to every topic in Linux administration. The concepts from this module appear throughout the Linux+ exam and in every real-world Linux role.

Next: Module 15 — Linux Security Hardening.
