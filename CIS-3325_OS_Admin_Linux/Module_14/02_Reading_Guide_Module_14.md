# Reading Guide: Module 14 — SSH and Remote Administration

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This guide accompanies the Module 14 video lectures on SSH, secure file transfer, port forwarding, and Ansible. Estimated reading and review time: 90 minutes.

---

### Learning Objectives

After completing this module, you will be able to:

- Explain asymmetric key cryptography as applied to SSH authentication
- Generate Ed25519 and RSA SSH key pairs with appropriate security parameters
- Distribute and install public keys correctly using `ssh-copy-id` and manual methods
- Harden `sshd_config` by disabling root login, password auth, and applying access controls
- Transfer files securely using `scp` and SFTP
- Configure SSH port forwarding for local, remote, and dynamic tunneling
- Write basic Ansible inventories and playbooks for multi-host administration

---

### Key Terms

**Asymmetric Cryptography**
A cryptographic system using mathematically linked key pairs (public and private). Data encrypted with one key can only be decrypted with the other.

**Ed25519**
An elliptic curve digital signature algorithm considered the current best practice for SSH keys. Fast, compact, and secure.

**Passphrase**
An optional password that encrypts the private key file on disk. Without a passphrase, anyone who copies your private key can use it.

**ssh-agent**
A background process that holds decrypted private keys in memory, allowing key-based authentication without re-entering the passphrase for each connection.

**authorized_keys**
A file in `~/.ssh/` on the server that contains the public keys permitted to authenticate as that user.

**known_hosts**
A file in `~/.ssh/` on the client that records the public key fingerprints of servers you have previously connected to. Used to detect host key changes (potential MITM attacks).

**Port Forwarding**
Redirecting network traffic from one port through an SSH connection to another port on a different host.

**SOCKS Proxy**
A protocol-agnostic proxy server. SSH dynamic forwarding creates a SOCKS5 proxy that can handle any TCP traffic.

**Ansible**
An agentless IT automation platform that uses SSH and Python to configure systems, deploy applications, and orchestrate workflows.

**Idempotent**
An operation that produces the same result regardless of how many times it is applied. Ansible modules are idempotent: running them multiple times does not cause repeated changes.

---

### Section 1: SSH Protocol Details

**OpenSSH Components**

The OpenSSH package provides:

- `ssh` — client
- `sshd` — server daemon
- `ssh-keygen` — key generation and management
- `ssh-copy-id` — public key distribution
- `ssh-agent` — key caching daemon
- `ssh-add` — add keys to ssh-agent
- `scp` — file copy
- `sftp` — interactive file transfer
- `ssh-keyscan` — gather host public keys

**Connection Sequence**

1. TCP connection established (port 22 by default)
2. Protocol version negotiation
3. Algorithm negotiation (ciphers, MACs, key exchange)
4. Key exchange — server's host key verified against `known_hosts`
5. Authentication — public key or password
6. Session — shell, command, or subsystem (SFTP)

**Host Key Verification**

On first connection to a new host, SSH shows a fingerprint:

```
The authenticity of host 'server.example.com' can't be established.
ED25519 key fingerprint is SHA256:abc123...
Are you sure you want to continue connecting (yes/no)?
```

Before accepting, verify the fingerprint out-of-band (by phone, ticketing system, or server console). Accepting an unverified fingerprint is a man-in-the-middle vulnerability.

To view a server's host key fingerprint:

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

**Host Key Rotation**

When a server is reinstalled or its host key changes, SSH clients will refuse to connect with a TOFU (Trust On First Use) warning:

```
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Remove the old entry from `known_hosts`:

```bash
ssh-keygen -R hostname
ssh-keygen -R 192.168.1.10
```

---

### Section 2: SSH Key Management Best Practices

**Dedicated Keys per Role**

Use separate key pairs for different purposes:

- Personal workstation key (`~/.ssh/id_ed25519`)
- Deployment automation key (`~/.ssh/id_ed25519_deploy`)
- Backup automation key (`~/.ssh/id_ed25519_backup`)

This limits the blast radius if one key is compromised.

**Key Rotation**

Rotate SSH keys regularly (at minimum annually, or immediately after a potential compromise):

1. Generate new key pair
2. Add new public key to all `authorized_keys` files
3. Test new key works
4. Remove old public key from all `authorized_keys` files
5. Revoke/delete old private key

**ssh-agent Best Practices**

Start ssh-agent at login:

```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

Limit key lifetime in agent:

```bash
ssh-add -t 3600 ~/.ssh/id_ed25519   # Expire after 1 hour
```

List loaded keys:

```bash
ssh-add -l
```

Remove all keys from agent:

```bash
ssh-add -D
```

**Certificate-Based Authentication**

SSH supports CA-signed certificates as an alternative to per-host `authorized_keys` management. An SSH certificate authority signs user and host keys:

```bash
# Sign a user key (CA side)
ssh-keygen -s ca_key -I "username" -n "username" -V +52w user_key.pub
```

This scales better than managing `authorized_keys` across hundreds of servers. The Linux+ exam covers this conceptually.

---

### Section 3: sshd_config Reference

**Full Hardened sshd_config Options**

| Directive | Recommended Value | Effect |
|-----------|------------------|--------|
| `Port` | 22 or custom | SSH listening port |
| `PermitRootLogin` | `no` | Block root SSH access |
| `PasswordAuthentication` | `no` | Require key auth |
| `PermitEmptyPasswords` | `no` | Block empty passwords |
| `PubkeyAuthentication` | `yes` | Enable key auth |
| `MaxAuthTries` | `3` | Limit auth attempts per connection |
| `MaxSessions` | `10` | Max sessions per connection |
| `ClientAliveInterval` | `300` | Keepalive interval (seconds) |
| `ClientAliveCountMax` | `2` | Keepalive failure limit |
| `AllowUsers` | List | Whitelist specific users |
| `AllowGroups` | `sshusers` | Whitelist specific groups |
| `X11Forwarding` | `no` | Disable X11 forwarding |
| `AllowTcpForwarding` | `no` | Disable port forwarding (restrictive) |
| `Banner` | `/etc/ssh/banner` | Show pre-auth warning banner |
| `LogLevel` | `VERBOSE` | Enhanced logging |
| `LoginGraceTime` | `60` | Seconds to complete authentication |

**The Banner Directive**

A pre-authentication login banner is required by many compliance frameworks (PCI-DSS, HIPAA). Create the banner file:

```bash
sudo nano /etc/ssh/ssh_banner
```

Sample banner content:

```
*********************************************************************
AUTHORIZED ACCESS ONLY
This system is for authorized users only. All activity is monitored
and logged. Unauthorized access will be prosecuted.
*********************************************************************
```

Set in `sshd_config`:

```
Banner /etc/ssh/ssh_banner
```

**Match Blocks**

`sshd_config` supports conditional blocks with the `Match` directive:

```
Match Group sftp-only
    ForceCommand internal-sftp
    ChrootDirectory /srv/sftp/%u
    PasswordAuthentication yes
    X11Forwarding no
    AllowTcpForwarding no
```

Match blocks apply only to connections that match the specified criteria. Supported keywords: `User`, `Group`, `Host`, `LocalAddress`, `LocalPort`, `Address`.

---

### Section 4: File Transfer Tools Comparison

| Tool | Protocol | Interactive | Compression | Incremental | Best For |
|------|----------|-------------|-------------|-------------|---------|
| `scp` | SCP/SFTP | No | Yes | No | Quick one-off copies |
| `sftp` | SFTP | Yes | No | No | Manual file management |
| `rsync` | rsync over SSH | No | Yes | Yes | Synchronization, backups |
| `git` | SSH/HTTPS | No | Yes | Yes | Code deployment |

**rsync Advanced Options**

```bash
# Mirror with delete (remove files on dest that don't exist on source)
rsync -avz --delete /source/ user@host:/dest/

# Exclude patterns
rsync -avz --exclude='*.tmp' --exclude='.git' /source/ user@host:/dest/

# Dry run (show what would be transferred)
rsync -avz --dry-run /source/ user@host:/dest/

# Bandwidth limit (100 KB/s)
rsync -avz --bwlimit=100 /source/ user@host:/dest/
```

---

### Section 5: Ansible Architecture

**Ansible Components**

- **Control Node**: the machine running Ansible (your workstation or CI/CD server)
- **Managed Nodes**: the servers being configured (no agent required)
- **Inventory**: list of managed nodes and groups
- **Playbook**: YAML file describing desired states
- **Module**: reusable Ansible unit that performs a specific action
- **Role**: structured directory of tasks, handlers, templates, and files for a reusable configuration
- **Task**: a single call to an Ansible module
- **Handler**: a task triggered by `notify:` that runs once at the end of a play (typically service restarts)

**Ansible Inventory Formats**

INI format (simple):

```ini
[webservers]
web01 ansible_host=192.168.1.10 ansible_user=admin
web02 ansible_host=192.168.1.11

[dbservers]
db01 ansible_host=192.168.1.20 ansible_ssh_private_key_file=~/.ssh/db_key
```

YAML format (more features):

```yaml
all:
  children:
    webservers:
      hosts:
        web01:
          ansible_host: 192.168.1.10
        web02:
          ansible_host: 192.168.1.11
```

**Ansible Variables**

Variables can be defined at multiple levels:

- Inventory variables (per-host or per-group)
- Playbook `vars:` section
- Role defaults and variables
- Command line `-e "var=value"`
- Vault-encrypted files for secrets

Example with variables:

```yaml
---
- name: Deploy application
  hosts: webservers
  vars:
    app_port: 8080
    app_user: appuser

  tasks:
    - name: Create application user
      user:
        name: "{{ app_user }}"
        state: present
```

---

### Practice Review Questions

Answer these before taking the quiz:

1. What is the difference between `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub`?

2. What permissions must `~/.ssh/authorized_keys` have for SSH to accept it?

3. What is the effect of setting `PasswordAuthentication no` in `sshd_config` before distributing SSH keys to all administrators?

4. Write the `ssh` command to forward local port 3306 to `db.internal:3306` through a bastion at `bastion.example.com`.

5. What is the difference between `scp -r` and `rsync -avz`?

6. In Ansible, what is the purpose of a handler?

7. You want to test an Ansible playbook without making any changes. What flag do you add?

8. What does the `become: yes` directive in an Ansible playbook do?

---

### Additional Resources

- `man 5 sshd_config` — complete SSH server configuration reference
- `man 1 ssh-keygen` — key generation options
- `man 1 ssh` — SSH client options including port forwarding
- Ansible Documentation: [docs.ansible.com](https://docs.ansible.com)
- CompTIA Linux+ XK0-005 Objectives: 2.1 (Security), 4.3 (Automation)
- NIST SP 800-82: Guide to Industrial Control Systems Security (SSH guidance)

---

### Key Takeaways

- Always use Ed25519 for new key generation. RSA 4096 for compatibility with older systems.
- Private key permissions must be `600`; `~/.ssh/` must be `700`. SSH silently ignores improperly permissioned keys.
- Never disable password authentication in `sshd_config` before confirming key authentication works from another terminal.
- Port forwarding (`-L`, `-R`, `-D`) turns SSH into a versatile secure tunneling platform.
- Ansible's agentless model means SSH must be working correctly before Ansible can manage hosts — fixing SSH issues is always the first step in Ansible troubleshooting.

---

## 9. Supplemental Resources

**1. [OpenSSH Manual — ssh.com Academy](https://www.ssh.com/academy/ssh/command)**
The SSH Academy provides accessible, well-organized documentation for all OpenSSH tools: `ssh`, `scp`, `sftp`, `ssh-keygen`, `ssh-agent`, and `ssh-add`. Particularly useful sections cover key algorithm choices (Ed25519 vs RSA), port forwarding types with diagrams, and the `~/.ssh/config` file directives. A strong companion to the official man pages for Module 14 lab preparation.

**2. [Ansible Getting Started Documentation](https://docs.ansible.com/ansible/latest/getting_started/index.html)**
The official Ansible getting started guide. Covers installation, inventory file formats (INI and YAML), ad-hoc commands, basic playbook structure (tasks, modules, handlers), variables, and facts. This is the authoritative source for the Ansible concepts introduced in Module 14 and the starting point for the CompTIA Linux+ automation objectives (XK0-005 Domain 4.3).

**3. [SSH Hardening Guide — Mozilla InfoSec](https://infosec.mozilla.org/guidelines/openssh)**
Mozilla's published SSH hardening guidelines, maintained by their security engineering team. Provides specific `sshd_config` and `ssh_config` recommendations with rationale, organized into Modern, Intermediate, and Old compatibility tiers. Covers key exchange algorithms, ciphers, MACs, authentication methods, and operational security practices. Directly applicable to the Module 14 lab's sshd_config hardening tasks.
