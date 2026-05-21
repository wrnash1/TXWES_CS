# Quiz: Module 10 - SSH and Remote Access Security
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
An administrator wants to connect to a remote server at `192.168.1.50` as user `admin` using SSH. Which command is correct?
A) telnet admin@192.168.1.50
B) ssh admin@192.168.1.50
C) scp admin@192.168.1.50
D) sftp -connect admin 192.168.1.50
*   **Correct Answer:** B) ssh admin@192.168.1.50
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `telnet` transmits all data including credentials in cleartext over the network. It is insecure and should never be used for remote administration. SSH replaced Telnet specifically to address this security flaw.
    *   *Why C is incorrect:* `scp` is used for copying files between hosts over SSH. It requires a source and destination path argument — it cannot be used as a general remote login command.
    *   *Why D is incorrect:* `sftp` opens an interactive file transfer session over SSH. The syntax `sftp user@host` is correct, but `-connect` is not a valid sftp flag, and sftp is not a remote shell login tool.

---

---

**Question 2**
A systems administrator generates an SSH key pair using `ssh-keygen`. Two files are created: `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`. Which file must be copied to the remote server to enable key-based authentication?
A) `~/.ssh/id_rsa` — the private key, which the server uses to verify the client's identity.
B) Both files must be copied to `~/.ssh/` on the remote server.
C) `~/.ssh/id_rsa.pub` — the public key, appended to `~/.ssh/authorized_keys` on the remote server.
D) Neither file — the server generates its own matching key pair automatically upon first SSH connection.
*   **Correct Answer:** C) `~/.ssh/id_rsa.pub` — the public key, appended to `~/.ssh/authorized_keys` on the remote server.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The private key (`id_rsa`) must never leave the client machine. Copying it to a server would compromise the key entirely. The server only needs the public key to challenge authentication.
    *   *Why B is incorrect:* Copying the private key to the server is a critical security mistake. Only the public key (`id_rsa.pub`) is placed on the server; the private key stays exclusively on the client.
    *   *Why D is incorrect:* The server does not generate matching keys automatically. The administrator must explicitly copy the client's public key to the server's `~/.ssh/authorized_keys` file, typically using `ssh-copy-id`.

---

---

**Question 3**
After editing `/etc/ssh/sshd_config` to set `PasswordAuthentication no`, the administrator tests the change but password login is still accepted. What step was most likely missed?
A) The `/etc/ssh/ssh_config` client configuration file also needs `PasswordAuthentication no`.
B) `systemctl restart sshd` must be run to reload the daemon configuration from disk.
C) The server must be rebooted for `sshd_config` changes to take effect.
D) The `authorized_keys` file must be deleted before password authentication can be disabled.
*   **Correct Answer:** B) `systemctl restart sshd` must be run to reload the daemon configuration from disk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `/etc/ssh/ssh_config` is the client-side configuration file and controls client behavior. Server authentication policy is controlled exclusively by `/etc/ssh/sshd_config` on the server — the client file has no bearing on whether the server accepts passwords.
    *   *Why C is incorrect:* A full reboot is not required and would be disruptive. `systemctl restart sshd` (or `systemctl reload sshd` for a graceful reload) is the correct and sufficient command.
    *   *Why D is incorrect:* `authorized_keys` contains trusted public keys for key-based login. Deleting it would lock out key-based users but has no effect on whether password authentication is accepted — that is governed solely by the `PasswordAuthentication` directive.

---

**Question 4**
A junior administrator reports they cannot SSH into a server using their key pair even though `ssh-copy-id` ran successfully. Investigation reveals the permissions on their `~/.ssh/` directory are `755`. What is the problem and the correct fix?
A) The SSH daemon rejects connections from users whose home directory is world-readable. Run `chmod 750 /home/username`.
B) SSH ignores key files when the `~/.ssh/` directory permissions are too permissive. Run `chmod 700 ~/.ssh` and `chmod 600 ~/.ssh/authorized_keys`.
C) The `authorized_keys` file must be owned by root. Run `chown root ~/.ssh/authorized_keys`.
D) Port 22 is blocked by the firewall. Run `firewall-cmd --add-service=ssh --permanent` to allow it.
*   **Correct Answer:** B) SSH ignores key files when the `~/.ssh/` directory permissions are too permissive. Run `chmod 700 ~/.ssh` and `chmod 600 ~/.ssh/authorized_keys`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SSH does not reject connections based on home directory permissions. The critical permission check is specifically on the `~/.ssh/` directory and its contents, not the parent home directory.
    *   *Why C is incorrect:* `authorized_keys` must be owned by the user, not root. If root owns it, the user cannot write to it and SSH may reject it depending on configuration. Ownership by the account owner is required.
    *   *Why D is incorrect:* If port 22 were blocked by a firewall, the connection would time out or be refused at the TCP level — the user would not reach the authentication stage at all. The scenario describes a key auth failure after a successful connection, pointing to permission issues.

---

**Question 5**
An administrator needs to securely copy the file `/etc/hosts` from a remote server `backup.example.com` (as user `sysadmin`) to the local directory `/tmp/`. Which command is correct?
A) sftp sysadmin@backup.example.com:/etc/hosts /tmp/
B) scp sysadmin@backup.example.com:/etc/hosts /tmp/
C) rsync --encrypt sysadmin@backup.example.com:/etc/hosts /tmp/
D) cp ssh://sysadmin@backup.example.com/etc/hosts /tmp/
*   **Correct Answer:** B) scp sysadmin@backup.example.com:/etc/hosts /tmp/
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `sftp` uses an interactive session protocol — it does not accept a single-line remote-path-to-local-path syntax like `scp`. To transfer a file non-interactively over SFTP you would need to use a batch mode or an sftp client library.
    *   *Why C is incorrect:* `rsync` does not have an `--encrypt` flag. `rsync` can use SSH as a transport with the `-e ssh` option, but `--encrypt` is not a valid rsync option and the command would fail.
    *   *Why D is incorrect:* The `cp` command only operates on local filesystems. It has no understanding of SSH URIs or remote paths — this syntax is invalid and will produce a "No such file or directory" error.
