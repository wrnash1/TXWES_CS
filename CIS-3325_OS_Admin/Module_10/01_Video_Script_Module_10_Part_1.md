# Video Script: Module 10 - SSH and Remote Access Security (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 12 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 10. SSH — Secure Shell — is the foundation of remote Linux administration.
Every command you run on a remote server, every file you copy between systems, every automated
deployment pipeline runs over SSH. Understanding not just how to use SSH but how to secure it
is an essential skill. In Part 1 we cover SSH fundamentals, key-based authentication, and the
SSH configuration files. In Part 2 we cover sshd hardening, file transfers, SSH tunneling,
and multi-factor authentication concepts.

---

### Section 1: How SSH Works

SSH is an encrypted network protocol that provides:
- Remote terminal access (interactive shell)
- File transfers (scp, sftp, rsync over SSH)
- Port forwarding and tunneling
- Remote command execution

When you connect with SSH, the protocol:
1. Negotiates encryption algorithms
2. The server sends its host key (public key) to identify itself
3. The client verifies the host key against ~/.ssh/known_hosts
4. Authentication occurs (password or key-based)
5. An encrypted channel is established

[SHOW TERMINAL]

```bash
ssh user@192.168.1.50
```

On first connection, SSH shows the server's host key fingerprint and asks you to verify it.
This is your protection against man-in-the-middle attacks. If you accept a fingerprint from
a server you do not control, you are trusting that server's identity.

```bash
ssh -p 2222 user@192.168.1.50
```

Connect to a non-standard port with -p.

```bash
ssh user@192.168.1.50 "df -h"
```

Run a single command on a remote server and return the output locally.

---

### Section 2: Key-Based Authentication

Password authentication has weaknesses: passwords can be guessed, stolen, or reused.
Key-based authentication is cryptographically stronger and enables automation without
storing passwords.

[SHOW TERMINAL]

Step 1: Generate a key pair on the client.

```bash
ssh-keygen -t ed25519 -C "labadmin@workstation"
```

-t ed25519 specifies the Ed25519 algorithm (modern, recommended). -C adds a comment for
identification. You will be prompted for a passphrase — this encrypts the private key on
disk. Use a strong passphrase.

This creates two files:
- ~/.ssh/id_ed25519: The private key. Never share this. Never copy it to a server.
- ~/.ssh/id_ed25519.pub: The public key. This is what you copy to servers.

Step 2: Copy the public key to the server.

```bash
ssh-copy-id user@192.168.1.50
```

ssh-copy-id connects with password authentication (or key if already set up), appends the
public key to ~/.ssh/authorized_keys on the remote server, and sets correct permissions.

Step 3: Test key-based login.

```bash
ssh user@192.168.1.50
```

If the key pair is correctly configured, you will connect without being asked for a password
(or only for the passphrase if you set one).

---

### Section 3: SSH Key Permissions

SSH enforces strict permissions on key files and the .ssh directory. If permissions are
too permissive, SSH refuses to use the keys.

[SHOW TERMINAL]

```bash
ls -la ~/.ssh/
```

Required permissions:
- ~/.ssh/: 700 (only the owner can read/write/execute)
- ~/.ssh/id_ed25519: 600 (private key — owner read/write only)
- ~/.ssh/id_ed25519.pub: 644 (public key — readable by all, written by owner)
- ~/.ssh/authorized_keys: 600 (owner read/write only)
- ~/.ssh/known_hosts: 600 or 644

If you see permissions like 755 on ~/.ssh/, SSH will refuse key authentication and display
a warning about unprotected key files. Fix with:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 600 ~/.ssh/authorized_keys
```

---

### Section 4: SSH Configuration Files

[SHOW TERMINAL]

There are two SSH configuration files:

/etc/ssh/sshd_config: The server daemon configuration. Controls what the SSH server accepts.
Requires root to edit. Changes require service restart.

/etc/ssh/ssh_config: The client configuration. Controls how the SSH client behaves.
Can be overridden by ~/.ssh/config (per-user client configuration).

```bash
cat /etc/ssh/sshd_config | grep -v "^#" | grep -v "^$"
```

Shows active configuration directives, filtering out comments and blank lines.

Important sshd_config directives:

| Directive | Default | Purpose |
|-----------|---------|---------|
| Port | 22 | Listening port |
| PermitRootLogin | prohibit-password | Root login behavior |
| PasswordAuthentication | yes | Allow password login |
| PubkeyAuthentication | yes | Allow key-based login |
| AuthorizedKeysFile | .ssh/authorized_keys | Where public keys are stored |
| AllowUsers | (not set) | Whitelist of users allowed to SSH |
| MaxAuthTries | 6 | Max failed auth attempts before disconnect |
| LoginGraceTime | 2m | Time allowed to authenticate |
| X11Forwarding | no | Forward graphical applications |

---

### Section 5: The known_hosts File

[SHOW TERMINAL]

```bash
cat ~/.ssh/known_hosts
```

This file stores the host keys of servers you have previously connected to. Each line
contains the hostname/IP, key algorithm, and public key.

When you connect to a server and see "The authenticity of host X can't be established,"
SSH is asking you to manually verify the fingerprint matches the real server before
trusting it. Once you type yes, the key is added to known_hosts.

If a server's host key changes (server was rebuilt, or an attacker is intercepting),
SSH shows:

```
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

This is SSH protecting you from connecting to the wrong server. Never bypass this
warning without verifying the cause.

To remove a stale entry:

```bash
ssh-keygen -R 192.168.1.50
```

---

### Section 6: The SSH Agent

[SHOW TERMINAL]

If you use a passphrase on your private key, you have to type it every time you use the
key. The SSH agent caches decrypted keys in memory so you only type the passphrase once
per session.

```bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519
```

After running ssh-add, subsequent SSH connections use the cached key without prompting
for the passphrase. The agent runs in memory and the cached key is cleared when you log out.

```bash
ssh-add -l
```

Lists keys currently loaded in the agent.

---

### Certification Connection

SSH maps to Linux+ Domain 2.0 (Security). Key exam objectives:

Know the difference between the private key (stays on client) and the public key (goes
on the server in authorized_keys).

Know required permissions: ~/.ssh 700, private key 600, authorized_keys 600.

Know sshd_config versus ssh_config (server vs client configuration).

Know what PasswordAuthentication no does and that sshd restart is required after changes.

Know ssh-keygen, ssh-copy-id, and the Ed25519 key type.

---

### Transition to Part 2

In Part 2 we cover sshd hardening best practices, scp and rsync for file transfers,
SSH port forwarding, and the ~/.ssh/config client configuration file.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
