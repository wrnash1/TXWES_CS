# Reading Guide: Module 10 - SSH and Remote Access Security

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 2.0 - Security

---

### Glossary

**SSH (Secure Shell)** - An encrypted network protocol for remote terminal access, file transfer, and port forwarding. Replaced insecure protocols like Telnet and rsh.

**Host Key** - A server's permanent key pair used to identify it to SSH clients. The public half is sent to clients during connection; clients store it in ~/.ssh/known_hosts.

**Key Pair** - A matched set of a private key and a public key. The private key proves identity; the public key is distributed to servers. Mathematically linked: only the holder of the private key can prove ownership.

**authorized_keys** - A file in ~/.ssh/ on the server that lists public keys whose owners are allowed to log in as that user without a password.

**known_hosts** - A file in ~/.ssh/ on the client that stores the host keys of previously connected servers. Used to detect man-in-the-middle attacks.

**sshd_config** - The SSH server daemon configuration file at /etc/ssh/sshd_config. Controls what the server accepts.

**ssh_config** - The SSH client configuration file at /etc/ssh/ssh_config. Can be overridden by ~/.ssh/config for per-user settings.

**Port Forwarding** - Using SSH to tunnel other protocols through an encrypted SSH connection. Local forwarding: remote service accessible locally. Remote forwarding: local service accessible through remote server.

**scp (Secure Copy)** - A command-line tool for copying files over SSH. Non-interactive.

**rsync** - A file synchronization tool that transfers only changed blocks. Can use SSH as transport. More efficient than scp for large directory synchronization.

---

### SSH Key Algorithms

| Algorithm | Key Option | Security | Notes |
|-----------|-----------|---------|-------|
| Ed25519 | -t ed25519 | Highest | Recommended for all new keys |
| RSA | -t rsa -b 4096 | High | Use 4096-bit minimum; widely compatible |
| ECDSA | -t ecdsa | Good | Elliptic curve; smaller than RSA |
| DSA | -t dsa | Weak | Deprecated; do not use |

---

### SSH File Locations and Required Permissions

| File | Location | Permissions | Purpose |
|------|----------|------------|---------|
| ~/.ssh/ | Client and server | 700 | SSH configuration directory |
| ~/.ssh/id_ed25519 | Client only | 600 | Private key (never copy to server) |
| ~/.ssh/id_ed25519.pub | Client | 644 | Public key (safe to distribute) |
| ~/.ssh/authorized_keys | Server | 600 | List of trusted public keys |
| ~/.ssh/known_hosts | Client | 600 | Server host key fingerprints |
| ~/.ssh/config | Client | 600 | Per-user client configuration |
| /etc/ssh/sshd_config | Server | 600 | SSH server configuration |
| /etc/ssh/ssh_config | Client | 644 | System-wide client configuration |

SSH enforces these permissions strictly. If ~/.ssh/ is 755 or authorized_keys is 644,
key-based authentication will fail.

---

### Key-Based Authentication Workflow

1. Generate key pair on the client: ssh-keygen -t ed25519
2. Copy public key to server: ssh-copy-id user@server
3. Verify: ssh user@server (should connect without password)
4. Confirm permissions: chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
5. (Optional) Disable password auth after confirming keys work: PasswordAuthentication no in sshd_config

---

### sshd_config Hardening Reference

| Directive | Hardened Value | Effect |
|-----------|---------------|--------|
| PermitRootLogin | no | Completely block root SSH login |
| PasswordAuthentication | no | Require key-based auth; blocks brute-force |
| PubkeyAuthentication | yes | Enable key-based authentication |
| AllowUsers | user1 user2 | Whitelist; all others denied |
| AllowGroups | sshusers | Alternative to AllowUsers |
| Port | 2222 (or other) | Non-standard port reduces scan noise |
| ListenAddress | management_IP | Only listen on specific interface |
| MaxAuthTries | 3 | Reduce before lockout |
| LoginGraceTime | 30 | Seconds to complete auth (default 120) |
| X11Forwarding | no | Disable GUI forwarding if not needed |
| Banner | /etc/ssh/banner | Display legal notice before login |

After every sshd_config change:
1. Test syntax: sudo sshd -t
2. Restart service: sudo systemctl restart sshd

---

### scp Command Reference

| Command | Purpose |
|---------|---------|
| scp file user@host:/path/ | Copy local file to remote |
| scp user@host:/path/file /local/ | Copy remote file to local |
| scp -r /dir/ user@host:/path/ | Copy directory recursively |
| scp -P PORT file user@host:/path/ | Use non-standard port (capital P) |
| scp user1@host1:/path user2@host2:/path | Copy between two remote hosts |

---

### rsync Command Reference

| Flag | Meaning |
|------|---------|
| -a | Archive: preserves permissions, timestamps, owner, group, symlinks |
| -v | Verbose: show files being transferred |
| -z | Compress data in transit |
| -n | Dry run: show what would happen without making changes |
| --delete | Remove destination files not in source (makes destination a mirror) |
| -e "ssh -p PORT" | Use SSH with a specific port |
| --progress | Show transfer progress per file |
| -P | Same as --partial --progress |

---

### SSH Port Forwarding

Local port forwarding (-L):

```bash
ssh -L LOCAL_PORT:REMOTE_HOST:REMOTE_PORT user@jump_server
```

Traffic to localhost:LOCAL_PORT is forwarded through jump_server to REMOTE_HOST:REMOTE_PORT.

Remote port forwarding (-R):

```bash
ssh -R REMOTE_PORT:LOCAL_HOST:LOCAL_PORT user@remote_server
```

Traffic to REMOTE_PORT on remote_server is forwarded back to LOCAL_PORT on your local machine.

Useful flags:
- -N: No remote command (tunnel only)
- -f: Run in background

---

### ~/.ssh/config Syntax

```
Host ALIAS
    HostName IP_OR_HOSTNAME
    User USERNAME
    Port PORT_NUMBER
    IdentityFile PATH_TO_PRIVATE_KEY
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

- Host ALIAS: the name you use with the ssh command
- Host *: applies to all connections
- ServerAliveInterval: seconds between keepalive probes
- Permissions must be 600

---

### Exam Tips

1. Private key stays on the client. Public key goes to the server's authorized_keys. This is the most fundamental SSH concept and is directly tested.

2. ~/.ssh must be 700. Private keys and authorized_keys must be 600. If these permissions are wrong, SSH silently falls back to password auth or refuses to connect.

3. sshd_config is on the server; it controls what the server accepts. ssh_config is on the client; it controls how the client behaves. They are not the same file.

4. Always run sshd -t after editing sshd_config. A syntax error in sshd_config can make sshd refuse to restart, locking you out of remote access.

5. PasswordAuthentication no should only be set after verifying that key-based authentication works. Disabling passwords before setting up keys will lock everyone out.

6. scp uses -P (capital P) for port. ssh uses -p (lowercase). This difference appears on the exam.

7. rsync -n is a dry run that shows what would be transferred without making changes. Always use -n before --delete to preview what will be removed.

8. SSH REMOTE HOST IDENTIFICATION HAS CHANGED is a security warning indicating the server's host key has changed. Investigate before proceeding — this can indicate a MITM attack or a server rebuild.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Generate an Ed25519 key pair with ssh-keygen
- Copy a public key to a server with ssh-copy-id
- Set correct permissions on ~/.ssh/ and authorized_keys
- Explain the difference between id_ed25519 and id_ed25519.pub
- Describe what happens when you SSH to a server for the first time
- Explain what known_hosts does and when its warning appears
- List five sshd_config directives and their hardening values
- Test sshd_config syntax without restarting the service
- Use scp to copy a file to and from a remote server
- Use rsync for directory synchronization with and without --delete
- Explain local port forwarding with a specific use case
- Create a ~/.ssh/config entry for a frequently accessed server
- Explain the SSH agent and its purpose

---

## 9. Supplemental Resources

**1. OpenSSH Manual Pages — ssh(1), sshd(8), sshd_config(5), ssh_config(5)**
URL: https://man.openbsd.org/ssh
Coverage: The OpenBSD project maintains the authoritative OpenSSH manual pages. The ssh(1)
page covers all client flags including -L (local forward), -R (remote forward), -D (dynamic),
-A (agent forward), -N, and -f. The sshd_config(5) page documents every server directive
including PermitRootLogin, PasswordAuthentication, AllowUsers, MaxAuthTries, and
AuthorizedKeysFile. Essential reference for all SSH configuration topics in this module.

**2. SSH Key Management and Best Practices — Red Hat Enterprise Linux 9**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/securing_networks/using-secure-communications-between-two-systems-with-openssh_securing-networks
Coverage: Red Hat's OpenSSH security guide covering key generation with ssh-keygen, deploying
public keys, configuring sshd_config for hardening, certificate-based authentication, and
SSH agent usage. Includes step-by-step procedures for common administrative tasks and a
security hardening checklist aligned with RHEL recommendations.

**3. ssh-keygen(1) and ssh-copy-id(1) Man Pages — man7.org**
URL: https://man7.org/linux/man-pages/man1/ssh-keygen.1.html
Coverage: The ssh-keygen man page documents all key generation options including key types
(-t ed25519, rsa, ecdsa), bit sizes (-b), comments (-C), and passphrase management. The
ssh-copy-id man page explains the -i flag and how it writes keys to authorized_keys. Also
covers key fingerprint display and known_hosts management with -R for host key removal.

**4. rsync(1) Man Page and Tutorial — man7.org**
URL: https://man7.org/linux/man-pages/man1/rsync.1.html
Coverage: The rsync man page is comprehensive but dense. Key sections: -a (archive mode),
-v (verbose), -z (compress), --delete (mirror deletions), --dry-run (simulate), --exclude,
and --bwlimit. The FILTER RULES section covers include/exclude patterns for selective sync.
Understanding the trailing slash behavior (source/ vs source) is critical for correct usage.

**5. Arch Wiki — SSH Keys and OpenSSH**
URL: https://wiki.archlinux.org/title/SSH_keys
Coverage: Practical guide covering key pair generation, adding keys to ssh-agent with
ssh-add, configuring SSH config file entries, multiplexing with ControlMaster, and
troubleshooting authentication failures. The companion OpenSSH article covers server
configuration, security hardening, and jump host configuration with ProxyJump. Both are
regularly updated and include current best-practice recommendations.
