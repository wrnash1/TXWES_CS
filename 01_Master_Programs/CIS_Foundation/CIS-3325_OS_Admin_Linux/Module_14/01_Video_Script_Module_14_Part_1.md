# Video Script: Module 14 — SSH and Remote Administration (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome to Module 14: SSH and Remote Administration.

SSH — the Secure Shell protocol — is the single most important tool in remote Linux administration. Every server you manage, every cloud instance you deploy, every automated pipeline you build will involve SSH. Module 14 goes deep: key generation and distribution, server-side hardening, secure file transfer, port forwarding, and an introduction to Ansible for managing multiple systems at scale.

In Part 1, we'll cover SSH key cryptography, generating keys with `ssh-keygen`, distributing public keys with `ssh-copy-id`, and hardening the SSH server daemon with `sshd_config`. Part 2 covers SCP, SFTP, port forwarding, and Ansible basics.

Let's start with the fundamentals of SSH key authentication.

---

### Section 1: SSH Authentication Overview

**Password vs. Key Authentication**

SSH supports two primary authentication methods:

- **Password authentication** — the client submits a password that the server verifies. Simple but vulnerable to brute-force attacks, phishing, and credential reuse.
- **Public key authentication** — the client holds a private key; the server holds the corresponding public key. Authentication is a cryptographic challenge-response that cannot be replayed or brute-forced.

Key authentication is always preferred in production. The Linux+ exam expects you to understand both methods and the configuration for each.

**The Asymmetric Key Pair**

SSH uses asymmetric (public-key) cryptography:

- The **private key** is kept secret on the client. Never share it, never copy it to servers.
- The **public key** is placed on every server you want to access. It is safe to distribute freely.

During authentication:

1. The server presents a challenge encrypted with your public key
2. Your SSH client decrypts it using your private key
3. The response proves you hold the private key without ever transmitting it

---

### Section 2: Generating SSH Keys with ssh-keygen

**Basic Key Generation**

```bash
ssh-keygen -t ed25519 -C "william.nash@example.com"
```

- `-t ed25519` — key type: Ed25519 (modern, fast, secure)
- `-C "comment"` — a comment to identify the key (usually email or hostname)

You will be prompted for:

1. **File path** — default is `~/.ssh/id_ed25519`. Accept the default or specify a different path.
2. **Passphrase** — encrypts the private key on disk. Always use a passphrase in production.

**Key Types Comparison**

| Type | Algorithm | Key Size | Security | Notes |
|------|-----------|----------|----------|-------|
| `ed25519` | EdDSA | 256-bit | Excellent | Recommended; fastest; not on very old SSH |
| `rsa` | RSA | 4096-bit | Very Good | Widely compatible; use `-b 4096` |
| `ecdsa` | ECDSA | 521-bit | Good | Avoid P-256; weak curve concerns |
| `dsa` | DSA | 1024-bit | Weak | Deprecated; do not use |

For maximum compatibility with older systems, use RSA 4096:

```bash
ssh-keygen -t rsa -b 4096 -C "william.nash@example.com"
```

**The Generated Files**

After running `ssh-keygen`, two files are created:

- `~/.ssh/id_ed25519` — private key (permissions must be `600`)
- `~/.ssh/id_ed25519.pub` — public key (safe to copy anywhere)

**Verify permissions:**

```bash
ls -la ~/.ssh/
```

Correct permissions:

```
drwx------  ~/.ssh/
-rw-------  ~/.ssh/id_ed25519
-rw-r--r--  ~/.ssh/id_ed25519.pub
```

If permissions are wrong, SSH will refuse to use the key.

---

### Section 3: Distributing Public Keys

**The authorized_keys File**

On each server you want to access, your public key must be added to `~/.ssh/authorized_keys` for the account you'll log in as.

Format of `authorized_keys`:

```
ssh-ed25519 AAAA...base64data... william.nash@example.com
ssh-rsa AAAA...base64data... william.nash@workstation
```

Each line is one key. Multiple keys can be present for multiple clients.

**Using ssh-copy-id**

The easiest and safest way to distribute your public key:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@hostname
```

This connects via password (or existing key), creates `~/.ssh/` with correct permissions on the server, and appends your public key to `authorized_keys`.

After running `ssh-copy-id`, test the connection:

```bash
ssh user@hostname
```

If configured correctly, you will authenticate without a password prompt.

**Manual Key Installation**

When `ssh-copy-id` is not available:

```bash
# On the client, copy the public key:
cat ~/.ssh/id_ed25519.pub

# On the server, paste it:
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "ssh-ed25519 AAAA...data... user@client" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

The permissions are critical. If `~/.ssh/` is not mode `700` or `authorized_keys` is not mode `600`, SSH will ignore the keys silently.

**Authorized Key Options**

You can restrict what an authorized key can do with options at the start of the line:

```
from="192.168.1.0/24" ssh-ed25519 AAAA... restricted backup key
no-pty,no-port-forwarding ssh-rsa AAAA... monitoring key
command="/usr/local/bin/backup-only.sh" ssh-ed25519 AAAA... deploy key
```

The `command=` option forces execution of a specific command regardless of what the client requests — useful for automated scripts that should only be able to run one specific command.

---

### Section 4: SSH Server Hardening — sshd_config

The SSH daemon configuration file is `/etc/ssh/sshd_config`. Changes here affect all incoming SSH connections. After any change, reload the service:

```bash
sudo systemctl reload sshd
```

**Always keep a second terminal open** while editing `sshd_config`. A syntax error in sshd_config can prevent the daemon from reloading, potentially locking you out.

**Disable Root Login**

```
PermitRootLogin no
```

This is non-negotiable. Root access over SSH should always be prohibited. Administrators must log in as a regular user and use `sudo`.

If a specific automation requires root SSH access (rare), use:

```
PermitRootLogin without-password
```

This allows root login only with key authentication, not passwords.

**Disable Password Authentication**

Once key authentication is fully deployed:

```
PasswordAuthentication no
```

This forces all users to authenticate with keys. If a user loses their key, they cannot log in until a backup key is installed.

**Change the Default Port**

Moving SSH from port 22 to a non-standard port reduces automated scanner noise:

```
Port 2222
```

This is "security through obscurity" and not a substitute for real security, but it dramatically reduces log noise.

**Restrict Login to Specific Users**

```
AllowUsers admin deploy backup
AllowGroups sshusers
```

Only explicitly listed users or groups can connect. Everyone else is denied.

**Set Idle Timeout**

Disconnect idle sessions automatically:

```
ClientAliveInterval 300
ClientAliveCountMax 2
```

After 300 seconds of inactivity, the server sends a keepalive check. After 2 unanswered checks (10 minutes total), the connection is dropped.

**Limit Authentication Attempts**

```
MaxAuthTries 3
```

After 3 failed authentication attempts, the connection is closed. This slows brute-force attacks.

**Disable Empty Passwords**

```
PermitEmptyPasswords no
```

Never allow accounts with no password to log in via SSH.

**Restrict to Protocol Version 2**

Modern SSH only uses protocol version 2, but explicitly enforcing it:

```
Protocol 2
```

(In recent OpenSSH versions, SSHv1 support has been removed entirely — this directive may not be recognized.)

**Configure Allowed Ciphers**

For high-security environments, restrict to strong ciphers:

```
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com
KexAlgorithms curve25519-sha256,diffie-hellman-group16-sha512
```

**Minimal Hardened sshd_config**

A production-hardened SSH server configuration:

```
Port 22
Protocol 2
PermitRootLogin no
PasswordAuthentication no
PermitEmptyPasswords no
MaxAuthTries 3
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
ClientAliveInterval 300
ClientAliveCountMax 2
AllowGroups sshusers
X11Forwarding no
Banner /etc/ssh/ssh_banner
```

**Testing sshd_config Syntax**

Before reloading:

```bash
sudo sshd -t
```

If this returns no output, the configuration is syntactically valid. If there are errors, they will be displayed.

---

### Summary — Part 1

Part 1 covered the core of SSH security:

- Asymmetric key cryptography: public and private keys
- Generating Ed25519 and RSA keys with `ssh-keygen`
- Distributing public keys with `ssh-copy-id` and manual installation
- `authorized_keys` file format and per-key options
- `sshd_config` hardening: disabling root, disabling passwords, restricting users, setting timeouts

In Part 2: secure file transfer with `scp` and `sftp`, SSH port forwarding (local, remote, and dynamic tunneling), and Ansible basics for multi-host administration.

See you in Part 2.
