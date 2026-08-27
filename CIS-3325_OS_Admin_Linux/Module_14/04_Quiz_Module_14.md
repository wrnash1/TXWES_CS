# Quiz: Module 14 — SSH and Remote Administration

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Instructions

Select the best answer for each question. Each question is worth 10 points.

---

### Questions

**Question 1**

A Linux administrator generates an SSH key pair with `ssh-keygen -t ed25519`. After generation, the permissions on `~/.ssh/id_ed25519` are `644`. What is the consequence of this?

- A) SSH will use the key but display a warning
- B) SSH will refuse to use the key because the private key is world-readable
- C) The key will work normally; permissions only matter for the public key
- D) SSH will automatically fix the permissions on first use

**Correct Answer: B**

*Explanation: OpenSSH enforces strict permission requirements. The private key must be mode `600` (owner read/write only). If the private key is world-readable (e.g., `644`), SSH silently refuses to use it with an "Unprotected private key file" error. Run `chmod 600 ~/.ssh/id_ed25519` to fix this.*

---

**Question 2**

An administrator wants to copy a directory named `configs/` recursively from a local machine to the `/etc/app/` path on a remote server at `10.0.0.5`, connecting on port 2222 as user `deploy`. Which `scp` command is correct?

- A) `scp -p 2222 -r configs/ deploy@10.0.0.5:/etc/app/`
- B) `scp -P 2222 -r configs/ deploy@10.0.0.5:/etc/app/`
- C) `scp -port 2222 -r configs/ deploy@10.0.0.5:/etc/app/`
- D) `scp -r -ssh-port 2222 configs/ deploy@10.0.0.5:/etc/app/`

**Correct Answer: B**

*Explanation: `scp` uses uppercase `-P` for the port number (unlike `ssh` which uses lowercase `-p`). `-r` enables recursive copy. This is a common mistake on the Linux+ exam — the case of the `-P` flag is a deliberate distinction.*

---

**Question 3**

After adding `PasswordAuthentication no` to `/etc/ssh/sshd_config` and running `systemctl reload sshd`, remote users report they can no longer log in to the server. What is the most likely cause?

- A) `sshd_config` requires a full restart (not reload) for authentication changes
- B) The administrator disabled password authentication before distributing SSH keys to users
- C) `PasswordAuthentication no` also disables public key authentication
- D) `systemctl reload` reverted the configuration file to the previous state

**Correct Answer: B**

*Explanation: Disabling password authentication before ensuring every user has a working public key will lock out all users who haven't yet deployed their key. The correct procedure is: deploy keys → verify key auth works → THEN disable password authentication.*

---

**Question 4**

A developer needs to access a web application running on port 8080 on an internal server at `app.internal`, which is not directly reachable from the developer's laptop. The developer can SSH to `bastion.example.com`. Which command creates the appropriate tunnel?

- A) `ssh -R 8080:app.internal:8080 developer@bastion.example.com`
- B) `ssh -L 8080:app.internal:8080 developer@bastion.example.com`
- C) `ssh -D 8080 developer@bastion.example.com`
- D) `ssh -T 8080:app.internal:8080 developer@bastion.example.com`

**Correct Answer: B**

*Explanation: Local port forwarding (`-L`) forwards a local port through the SSH connection to a host reachable from the SSH server. The command listens on local port 8080 and forwards traffic to `app.internal:8080` via `bastion.example.com`. Remote forwarding (`-R`) works in the opposite direction.*

---

**Question 5**

Which `sshd_config` directive restricts SSH access to only members of the `sysadmins` group?

- A) `PermitGroups sysadmins`
- B) `GroupAuthentication sysadmins`
- C) `AllowGroups sysadmins`
- D) `RestrictGroups sysadmins`

**Correct Answer: C**

*Explanation: `AllowGroups` is the correct directive. When set, only users belonging to the listed groups are permitted to authenticate. Users in other groups — even with valid keys — will be denied. `AllowUsers` is the per-user equivalent.*

---

**Question 6**

An Ansible playbook contains `become: yes` at the play level. What does this directive do?

- A) Requires the playbook to be run as root on the control node
- B) Enables privilege escalation (typically via sudo) on managed nodes for all tasks in the play
- C) Forces all tasks to run with the playbook user's home directory permissions
- D) Disables privilege escalation and runs all tasks as the connecting user

**Correct Answer: B**

*Explanation: `become: yes` enables privilege escalation on managed nodes. By default, this uses `sudo` to execute tasks as root. The connecting user must have sudo privileges on the managed node. `become_user` can specify a different target user.*

---

**Question 7**

Which file on a server stores the public keys authorized to authenticate as a specific user?

- A) `/etc/ssh/authorized_keys`
- B) `~/.ssh/known_hosts`
- C) `~/.ssh/authorized_keys`
- D) `/etc/ssh/public_keys`

**Correct Answer: C**

*Explanation: Each user's `~/.ssh/authorized_keys` file contains public keys authorized to authenticate as that user. The `AuthorizedKeysFile` directive in `sshd_config` can change this path. The `known_hosts` file stores host key fingerprints, not user keys.*

---

**Question 8**

A Linux administrator needs to transfer a 50 GB backup file from one server to another nightly. The backup content changes only partially each night. Which tool would be MOST efficient for this repeated transfer?

- A) `scp`
- B) `sftp`
- C) `rsync`
- D) `curl`

**Correct Answer: C**

*Explanation: `rsync` uses delta transfer — it identifies and transfers only the blocks that have changed between the source and destination. For a 50 GB file that changes partially each night, `rsync` transfers only the changed portions, making it far more efficient than `scp` or `sftp`, which always transfer the full file.*

---

**Question 9**

After installing a new OS on a server, an administrator tries to SSH to it but receives: "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!" What should the administrator do?

- A) Check the `/etc/ssh/sshd_config` for a misconfigured `HostKey` directive
- B) Remove the old host key entry from `~/.ssh/known_hosts` using `ssh-keygen -R <hostname>`
- C) Regenerate the client's SSH key pair with `ssh-keygen`
- D) Disable `StrictHostKeyChecking` permanently in the SSH client config

**Correct Answer: B**

*Explanation: When a server is reinstalled, it generates new host keys. The client's `known_hosts` still has the old fingerprint, causing this warning. Run `ssh-keygen -R hostname` to remove the old entry. After connecting and verifying the new fingerprint, the new host key is stored. Permanently disabling StrictHostKeyChecking is a security risk.*

---

**Question 10**

In Ansible, what is the purpose of a **handler**?

- A) A task that runs before all other tasks to check system state
- B) A task triggered by `notify:` that runs once at the end of the play, typically used for service restarts
- C) A variable that controls whether a task runs based on a condition
- D) An error handler that catches and retries failed tasks

**Correct Answer: B**

*Explanation: A handler is a special task that only runs when notified by another task using `notify:`. Even if multiple tasks notify the same handler, it runs only once at the end of the play. The most common use case is restarting a service when its configuration file changes — but only if the file actually changed.*

---

**Question 11** (5 points)

An administrator needs to run a command on 20 servers simultaneously using a bash loop and SSH. The private key for all servers is at `~/.ssh/fleet.key`. Which loop correctly connects without host key prompts for previously unknown hosts?

- A) `for h in "${HOSTS[@]}"; do ssh -i ~/.ssh/fleet.key $h "uptime"; done`
- B) `for h in "${HOSTS[@]}"; do ssh -i ~/.ssh/fleet.key -o StrictHostKeyChecking=accept-new $h "uptime"; done`
- C) `for h in "${HOSTS[@]}"; do ssh -i ~/.ssh/fleet.key -o StrictHostKeyChecking=no $h "uptime"; done`
- D) `for h in "${HOSTS[@]}"; do ssh -i ~/.ssh/fleet.key --no-verify $h "uptime"; done`

**Correct Answer: B**

*Explanation: `StrictHostKeyChecking=accept-new` automatically accepts and saves new host keys (for hosts not yet in `known_hosts`) but still rejects changed keys — protecting against MITM attacks on known hosts. `StrictHostKeyChecking=no` accepts ALL key changes including potentially malicious ones, which is a security risk. Option A would prompt interactively for unknown hosts. Option D is invalid syntax.*

---

**Question 12** (5 points)

Which `rsync` option preserves file permissions, timestamps, symbolic links, and ownership in a single flag?

- A) `-r` (recursive)
- B) `-p` (preserve permissions)
- C) `-a` (archive mode)
- D) `-z` (compress during transfer)

**Correct Answer: C**

*Explanation: The `-a` (archive) flag is equivalent to `-rlptgoD`: recursive, symlinks, permissions, timestamps, group, owner, and device files. It is the standard flag for backup-style copies where you want the destination to be an exact replica. `-r` alone is recursive but does not preserve metadata. `-p` preserves permissions only. `-z` compresses data in transit.*

---

**Question 13** (5 points)

What does `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote-server` accomplish?

- A) It copies the private key to the remote server for passwordless sudo.
- B) It appends the specified public key to the remote user's `~/.ssh/authorized_keys` file.
- C) It replaces all existing authorized keys with the specified public key.
- D) It generates a new key pair on the remote server.

**Correct Answer: B**

*Explanation: `ssh-copy-id` appends (not replaces) the specified public key to `~/.ssh/authorized_keys` on the remote host. It connects using the current authentication method (typically password) and then adds the key. This is the safe, standard way to deploy keys without accidentally deleting existing authorized keys. It also sets correct permissions on the `.ssh` directory and `authorized_keys` file.*

---

**Question 14** (5 points)

An administrator uses `ssh -J bastion.corp.com app-server-01` to reach an internal server via a jump host. What is the advantage of this approach over traditional ProxyCommand with netcat?

- A) `-J` is faster because it bypasses encryption on the intermediate hop.
- B) `-J` creates a fully end-to-end encrypted connection directly to the target — the jump host can only see that a connection passes through it, not the connection's content.
- C) `-J` allows the jump host to inspect and filter the connection content for security.
- D) `-J` requires no SSH server running on the jump host.

**Correct Answer: B**

*Explanation: SSH's ProxyJump (`-J`) creates a direct TCP connection through the jump host using SSH's built-in forwarding. The actual SSH session is end-to-end encrypted between the client and the final destination — the jump host cannot read the session content. This differs from traditional approaches where some implementations could expose unencrypted traffic on the intermediate hop.*

---

**Question 15** (5 points)

In an Ansible inventory file, which format correctly defines a group named `webservers` containing two hosts with specific variables?

- A)

```ini
[webservers]
web1.example.com http_port=80
web2.example.com http_port=8080
```

- B)

```ini
[webservers]
web1.example.com
web2.example.com
[webservers:vars]
http_port=80
```

- C)

```ini
webservers:
  - web1.example.com
  - web2.example.com
```

- D) Both A and B are valid; they differ only in whether variables are per-host or per-group.

**Correct Answer: D**

*Explanation: Both INI-format approaches are valid. Option A sets variables per host (each host can have a different value). Option B uses the `[group:vars]` section to set the same variable for all hosts in the group. Option C is YAML format syntax (valid but only with the `.yml` inventory extension, not `.ini`). Ansible supports both INI and YAML inventory formats.*

---

**Question 16** (5 points)

Which `sshd_config` directive is the most direct way to prevent brute-force password attacks by limiting the number of authentication attempts per connection?

- A) `MaxAuthTries 3`
- B) `MaxSessions 1`
- C) `LoginGraceTime 30`
- D) `PasswordAuthentication no`

**Correct Answer: A**

*Explanation: `MaxAuthTries` limits the number of authentication attempts per connection. After exceeding half this value, failures are logged; after exceeding the full value, the connection is dropped. Typical hardened values are 3-6. `LoginGraceTime` limits the total time before an unauthenticated connection is dropped. `PasswordAuthentication no` eliminates password attacks entirely (best choice) but the question asks about limiting attempts, not eliminating them.*

---

**Question 17** (5 points)

What is the purpose of `ssh-agent` and the `ssh-add` command?

- A) `ssh-agent` manages sshd process lifecycle; `ssh-add` adds keys to the authorized_keys file.
- B) `ssh-agent` holds private keys decrypted in memory so the passphrase is not required for every connection; `ssh-add` loads keys into the agent.
- C) `ssh-agent` rotates SSH host keys periodically; `ssh-add` triggers manual rotation.
- D) `ssh-agent` provides key management for the `root` account; `ssh-add` distributes keys to managed systems.

**Correct Answer: B**

*Explanation: `ssh-agent` is a background process that holds private keys in decrypted form in memory. Once a key is loaded with `ssh-add`, the agent handles cryptographic operations without prompting for the passphrase on every use. Keys are lost when the agent exits or the session ends. The `SSH_AUTH_SOCK` environment variable points SSH clients to the agent's socket.*

---

**Question 18** (5 points)

An Ansible playbook task uses `when: ansible_os_family == "RedHat"`. What is `ansible_os_family` and where does it come from?

- A) A custom variable defined in the playbook's `vars:` section
- B) A fact gathered automatically by Ansible from the managed node during the setup/gather_facts phase
- C) A variable passed from the inventory file that identifies the host type
- D) A built-in Ansible constant that must be manually defined in `ansible.cfg`

**Correct Answer: B**

*Explanation: Ansible facts are variables collected automatically about managed nodes at the start of each play by the `setup` module (also called gather_facts). `ansible_os_family` is one of hundreds of facts that includes OS family, distribution name, version, architecture, IP addresses, and more. These facts allow conditional task execution based on the target system's properties without requiring the operator to pre-configure variables.*

---

**Question 19** (5 points)

An administrator wants to use `rsync` to synchronize a local directory to a remote server, ensuring that files deleted locally are also deleted from the remote destination. Which flag enables this behavior?

- A) `--remove-deleted`
- B) `--delete`
- C) `--sync`
- D) `--mirror`

**Correct Answer: B**

*Explanation: `rsync --delete` removes files from the destination that no longer exist in the source. Without this flag, rsync only copies new and changed files but never removes destination files. The complete flag for a mirror-style sync is `rsync -a --delete source/ dest/`. Be cautious: if source and destination arguments are swapped, `--delete` will delete from what was intended to be the source.*

---

**Question 20** (5 points)

Which directive in `~/.ssh/config` causes all SSH connections through a bastion host to be multiplexed over a single TCP connection, improving speed for repeated connections?

- A) `Compression yes`
- B) `ControlMaster auto` combined with `ControlPath ~/.ssh/sockets/%h_%p_%r`
- C) `ServerAliveInterval 30`
- D) `TCPKeepAlive yes`

**Correct Answer: B**

*Explanation: SSH multiplexing (`ControlMaster auto` + `ControlPath`) allows multiple SSH sessions to share a single underlying TCP connection and authentication. The first connection creates the master socket; subsequent connections reuse it without re-authenticating. This dramatically speeds up tools like Ansible that make many SSH connections to the same hosts. `Compression yes` compresses data; `ServerAliveInterval` sends keepalive packets; `TCPKeepAlive` enables OS-level TCP keepalives — none of these are multiplexing.*

---

### Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | C |
| 9 | B |
| 10 | B |
| 11 | B |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | D |
| 16 | A |
| 17 | B |
| 18 | B |
| 19 | B |
| 20 | B |
