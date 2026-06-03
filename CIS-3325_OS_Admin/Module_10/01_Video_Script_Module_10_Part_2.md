# Video Script: Module 10 - SSH and Remote Access Security (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - Hardening, File Transfer, and Tunneling

---

### Opening

Welcome back to Part 2 of Module 10. In Part 1 we covered SSH key-based authentication,
the sshd_config and ssh_config files, known_hosts, and the SSH agent. In Part 2 we cover
sshd security hardening, file transfers with scp and rsync, SSH port forwarding, and the
client-side ~/.ssh/config file.

---

### Section 1: sshd Hardening Best Practices

[SHOW TERMINAL]

```bash
sudo nano /etc/ssh/sshd_config
```

Key hardening changes:

Disable root login:
```
PermitRootLogin no
```

Root should not log in directly. Administrators log in as themselves and use sudo.
PermitRootLogin prohibit-password (the default on Ubuntu) allows root with key-based
auth but not password. Setting it to no completely blocks root.

Disable password authentication:
```
PasswordAuthentication no
```

After setting up key-based authentication for all users, disable password auth entirely.
This eliminates brute-force attacks against passwords. Only do this after verifying
key access works.

Restrict to specific users:
```
AllowUsers labadmin alice bob
```

Only listed users can SSH in. An implicit deny for everyone else. AllowGroups sshusers
is an alternative — add authorized users to the sshusers group.

Change the default port:
```
Port 2222
```

Security through obscurity: not a strong control, but eliminates most automated port 22
scanning noise from logs.

Restrict to specific interfaces:
```
ListenAddress 192.168.1.100
```

Only listen on the management interface, not on public-facing interfaces.

After editing:

```bash
sudo sshd -t
```

sshd -t tests the configuration for syntax errors without restarting the service. Always
run this before restarting.

```bash
sudo systemctl restart sshd
```

Apply the changes.

---

### Section 2: File Transfers with scp

[SHOW TERMINAL]

scp (Secure Copy) transfers files over SSH.

```bash
scp localfile.txt user@192.168.1.50:/home/user/
```

Copy a local file to a remote server.

```bash
scp user@192.168.1.50:/etc/hosts /tmp/hosts-remote
```

Copy a file from a remote server to the local system.

```bash
scp -r /local/directory user@192.168.1.50:/remote/path/
```

-r copies a directory recursively.

```bash
scp -P 2222 file.txt user@192.168.1.50:/home/user/
```

-P specifies a non-standard port (capital P, unlike ssh which uses lowercase -p).

```bash
scp user1@server1:/data/file.txt user2@server2:/backup/
```

Copy directly between two remote servers.

---

### Section 3: File Synchronization with rsync

[SHOW TERMINAL]

rsync is more powerful than scp for synchronization: it only transfers changed blocks,
supports resuming interrupted transfers, and preserves permissions and timestamps.

```bash
rsync -av /local/source/ user@remote:/remote/dest/
```

a = archive mode (preserves permissions, timestamps, owner, group, symlinks)
v = verbose output

```bash
rsync -avz /local/source/ user@remote:/remote/dest/
```

z = compress data in transit. Useful over slow links.

```bash
rsync -avz --delete /local/source/ user@remote:/remote/dest/
```

--delete removes files from the destination that no longer exist in the source. Makes
the destination a mirror of the source.

```bash
rsync -avn /local/source/ user@remote:/remote/dest/
```

n = dry run. Shows what would be transferred without actually transferring. Always test
with -n before using --delete.

```bash
rsync -e "ssh -p 2222" -av /local/source/ user@remote:/dest/
```

-e specifies the SSH command. Use this to specify a non-standard port.

---

### Section 4: SSH Port Forwarding

[SHOW TERMINAL]

SSH can tunnel other protocols through the encrypted SSH connection.

Local port forwarding: access a remote service as if it were local.

```bash
ssh -L 8080:127.0.0.1:80 user@remote-server
```

After running this, connecting to localhost:8080 on your local machine sends traffic
through the SSH tunnel to port 80 on the remote server's localhost. Use case: access
a web admin interface that is only accessible locally on the remote server.

Remote port forwarding: expose a local service through the remote server.

```bash
ssh -R 9090:127.0.0.1:3000 user@remote-server
```

After running this, connecting to port 9090 on the remote server forwards to port 3000
on your local machine. Use case: expose a local development server through a public host.

```bash
ssh -N -f -L 5432:db-server:5432 user@jump-server
```

-N: do not execute a remote command (port forwarding only)
-f: run in background

This creates a persistent tunnel to a database server (db-server:5432) through a jump
server. Tools on your local machine can connect to localhost:5432 and reach the remote
database securely.

---

### Section 5: SSH Client Configuration (~/.ssh/config)

[SHOW TERMINAL]

The ~/.ssh/config file lets you create aliases and pre-configure connection settings for
frequently accessed servers.

```bash
cat ~/.ssh/config
```

Example configuration:

```
Host prod-web
    HostName 10.20.30.50
    User deployadmin
    Port 2222
    IdentityFile ~/.ssh/prod_key

Host dev-*
    User devuser
    IdentityFile ~/.ssh/dev_key

Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

With this config, ssh prod-web is equivalent to:
ssh -p 2222 -i ~/.ssh/prod_key deployadmin@10.20.30.50

The Host * section applies to all connections. ServerAliveInterval 60 sends a keepalive
every 60 seconds to prevent idle connections from being dropped by firewalls.

Permissions on ~/.ssh/config must be 600.

---

### Section 6: Exam Tips for Module 10

Private key stays on the client. Public key goes to the server's ~/.ssh/authorized_keys.
Never copy the private key to the server.

Required permissions: ~/.ssh must be 700, private key and authorized_keys must be 600.
SSH will refuse key authentication if these are too permissive.

sshd_config is the server configuration. ssh_config is the client configuration. They
are different files that do different things.

After editing sshd_config: run sshd -t to test syntax, then systemctl restart sshd.

PasswordAuthentication no eliminates password brute-force attacks. Only disable after
confirming key-based access works.

scp -P (capital P) for non-standard port. ssh -p (lowercase p) for non-standard port.

rsync -n is a dry run. Always test with -n before using --delete.

SSH host key warnings (REMOTE HOST IDENTIFICATION HAS CHANGED) must be investigated
before proceeding. Do not silently bypass them.

---

### Summary

Module 10 covers SSH end to end: key generation, key distribution, permission requirements,
sshd hardening, file transfers with scp and rsync, port forwarding, and client configuration
with ~/.ssh/config.

Module 11 covers firewall management with iptables and firewalld.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
