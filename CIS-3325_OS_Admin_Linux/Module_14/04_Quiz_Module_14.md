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
