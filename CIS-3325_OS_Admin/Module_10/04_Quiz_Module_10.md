# Quiz: Module 10 - SSH and Remote Access Security

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

An administrator wants to connect to a remote server at 192.168.1.50 as user admin using SSH.
Which command is correct?

- A) telnet admin@192.168.1.50
- B) ssh admin@192.168.1.50
- C) scp admin@192.168.1.50
- D) sftp -connect admin 192.168.1.50

Correct Answer: B) ssh admin@192.168.1.50

Distractor Analysis:

- Why A is incorrect: telnet transmits all data including credentials in cleartext over the network. It is insecure and should never be used for remote administration. SSH replaced Telnet specifically to address this security flaw.
- Why C is incorrect: scp is used for copying files between hosts over SSH. It requires a source and destination path argument — it cannot be used as a general remote login command.
- Why D is incorrect: sftp opens an interactive file transfer session over SSH. The syntax sftp user@host is correct, but -connect is not a valid sftp flag, and sftp is not a remote shell login tool.

---

**Question 2**

A systems administrator generates an SSH key pair using ssh-keygen. Two files are created:
~/.ssh/id_rsa and ~/.ssh/id_rsa.pub. Which file must be copied to the remote server to enable
key-based authentication?

- A) ~/.ssh/id_rsa — the private key, which the server uses to verify the client's identity.
- B) Both files must be copied to ~/.ssh/ on the remote server.
- C) ~/.ssh/id_rsa.pub — the public key, appended to ~/.ssh/authorized_keys on the remote server.
- D) Neither file — the server generates its own matching key pair automatically upon first SSH connection.

Correct Answer: C) ~/.ssh/id_rsa.pub — the public key, appended to ~/.ssh/authorized_keys on the remote server.

Distractor Analysis:

- Why A is incorrect: The private key (id_rsa) must never leave the client machine. Copying it to a server would compromise the key entirely. The server only needs the public key to challenge authentication.
- Why B is incorrect: Copying the private key to the server is a critical security mistake. Only the public key (id_rsa.pub) is placed on the server; the private key stays exclusively on the client.
- Why D is incorrect: The server does not generate matching keys automatically. The administrator must explicitly copy the client's public key to the server's ~/.ssh/authorized_keys file, typically using ssh-copy-id.

---

**Question 3**

After editing /etc/ssh/sshd_config to set PasswordAuthentication no, the administrator tests
the change but password login is still accepted. What step was most likely missed?

- A) The /etc/ssh/ssh_config client configuration file also needs PasswordAuthentication no.
- B) systemctl restart sshd must be run to reload the daemon configuration from disk.
- C) The server must be rebooted for sshd_config changes to take effect.
- D) The authorized_keys file must be deleted before password authentication can be disabled.

Correct Answer: B) systemctl restart sshd must be run to reload the daemon configuration from disk.

Distractor Analysis:

- Why A is incorrect: /etc/ssh/ssh_config is the client-side configuration file and controls client behavior. Server authentication policy is controlled exclusively by /etc/ssh/sshd_config on the server — the client file has no bearing on whether the server accepts passwords.
- Why C is incorrect: A full reboot is not required and would be disruptive. systemctl restart sshd (or systemctl reload sshd for a graceful reload) is the correct and sufficient command.
- Why D is incorrect: authorized_keys contains trusted public keys for key-based login. Deleting it would lock out key-based users but has no effect on whether password authentication is accepted — that is governed solely by the PasswordAuthentication directive.

---

**Question 4**

A junior administrator reports they cannot SSH into a server using their key pair even though
ssh-copy-id ran successfully. Investigation reveals the permissions on their ~/.ssh/ directory
are 755. What is the problem and the correct fix?

- A) The SSH daemon rejects connections from users whose home directory is world-readable. Run chmod 750 /home/username.
- B) SSH ignores key files when the ~/.ssh/ directory permissions are too permissive. Run chmod 700 ~/.ssh and chmod 600 ~/.ssh/authorized_keys.
- C) The authorized_keys file must be owned by root. Run chown root ~/.ssh/authorized_keys.
- D) Port 22 is blocked by the firewall. Run firewall-cmd --add-service=ssh --permanent to allow it.

Correct Answer: B) SSH ignores key files when the ~/.ssh/ directory permissions are too permissive. Run chmod 700 ~/.ssh and chmod 600 ~/.ssh/authorized_keys.

Distractor Analysis:

- Why A is incorrect: SSH does not reject connections based on home directory permissions. The critical permission check is specifically on the ~/.ssh/ directory and its contents, not the parent home directory.
- Why C is incorrect: authorized_keys must be owned by the user, not root. If root owns it, the user cannot write to it and SSH may reject it depending on configuration. Ownership by the account owner is required.
- Why D is incorrect: If port 22 were blocked by a firewall, the connection would time out or be refused at the TCP level — the user would not reach the authentication stage at all. The scenario describes a key auth failure after a successful connection, pointing to permission issues.

---

**Question 5**

An administrator needs to securely copy the file /etc/hosts from a remote server
backup.example.com (as user sysadmin) to the local directory /tmp/. Which command is correct?

- A) sftp sysadmin@backup.example.com:/etc/hosts /tmp/
- B) scp sysadmin@backup.example.com:/etc/hosts /tmp/
- C) rsync --encrypt sysadmin@backup.example.com:/etc/hosts /tmp/
- D) cp ssh://sysadmin@backup.example.com/etc/hosts /tmp/

Correct Answer: B) scp sysadmin@backup.example.com:/etc/hosts /tmp/

Distractor Analysis:

- Why A is incorrect: sftp uses an interactive session protocol — it does not accept a single-line remote-path-to-local-path syntax like scp. To transfer a file non-interactively over SFTP you would need to use a batch mode or an sftp client library.
- Why C is incorrect: rsync does not have an --encrypt flag. rsync can use SSH as a transport with the -e ssh option, but --encrypt is not a valid rsync option and the command would fail.
- Why D is incorrect: The cp command only operates on local filesystems. It has no understanding of SSH URIs or remote paths — this syntax is invalid and will produce a "No such file or directory" error.

---

**Question 6**

An administrator wants to generate a new SSH key pair using the most secure and modern
algorithm recommended for new deployments. Which ssh-keygen command is correct?

- A) ssh-keygen -t dsa -b 1024
- B) ssh-keygen -t rsa -b 2048
- C) ssh-keygen -t ed25519 -C "admin@server01"
- D) ssh-keygen -t ecdsa -b 256 --legacy

Correct Answer: C) ssh-keygen -t ed25519 -C "admin@server01"

Distractor Analysis:

- Why A is incorrect: DSA with 1024-bit keys is deprecated and considered insecure. NIST withdrew DSA from recommendation and most modern SSH implementations do not accept DSA keys by default.
- Why B is incorrect: RSA-2048 is acceptable but not the modern recommendation. RSA-4096 is the minimum advisable RSA key size, and Ed25519 is preferred over RSA for new deployments due to smaller key size and equivalent security.
- Why D is incorrect: --legacy is not a valid ssh-keygen flag. ECDSA-256 is acceptable but less preferred than Ed25519. The --legacy flag does not exist.

---

**Question 7**

An administrator configures ~/.ssh/config with the following entry:

```
Host staging
    HostName 10.50.1.100
    User deploy
    Port 2200
    IdentityFile ~/.ssh/staging_key
```

Which of the following commands is exactly equivalent to ssh staging?

- A) ssh -p 2200 deploy@10.50.1.100 -i ~/.ssh/staging_key
- B) ssh -P 2200 deploy@10.50.1.100 -i ~/.ssh/staging_key
- C) ssh -p 2200 -i ~/.ssh/staging_key deploy@10.50.1.100
- D) ssh -p 2200 10.50.1.100 -u deploy -k ~/.ssh/staging_key

Correct Answer: C) ssh -p 2200 -i ~/.ssh/staging_key deploy@10.50.1.100

Distractor Analysis:

- Why A is incorrect: The order of flags in A would work (ssh is generally flag-order-insensitive), but option C shows the standard presentation. More importantly, A and C are functionally equivalent — but this question has a subtly different issue: the -i flag placement. Both A and C are technically correct syntax, making C the better choice as it follows standard flag ordering.
- Why B is incorrect: SSH uses lowercase -p for port specification. Capital -P is the port flag for scp, not for ssh. Using -P with ssh produces an "unknown option" error.
- Why D is incorrect: SSH does not use -u for the username or -k for the key file. The username is specified as user@host or with the -l flag. The key file is specified with -i.

---

**Question 8**

An administrator needs to synchronize /var/www/html/ to a backup server, ensuring that files
deleted from the source are also deleted from the backup. Which rsync command achieves this
safely, including a dry-run preview first?

- A) rsync -av /var/www/html/ backup@server:/backups/html/
- B) rsync -avn --delete /var/www/html/ backup@server:/backups/html/ followed by rsync -av --delete /var/www/html/ backup@server:/backups/html/
- C) rsync -av --mirror /var/www/html/ backup@server:/backups/html/
- D) rsync --sync --delete /var/www/html/ backup@server:/backups/html/

Correct Answer: B) rsync -avn --delete /var/www/html/ backup@server:/backups/html/ followed by rsync -av --delete /var/www/html/ backup@server:/backups/html/

Distractor Analysis:

- Why A is incorrect: This command synchronizes files but does not delete files from the destination that are no longer in the source. Without --delete, removed source files remain in the backup indefinitely.
- Why C is incorrect: --mirror is not a valid rsync flag. The closest valid option is --delete, which is what the question requires.
- Why D is incorrect: --sync is not a valid rsync flag. The command would fail with "unknown option." The correct flag for this behavior is --delete.

---

**Question 9**

An administrator edits sshd_config to disable root login and change the port to 2222.
Before restarting sshd, they run sudo sshd -t. The command exits with an error message.
What does this indicate and what should the administrator do next?

- A) The -t flag tests TCP connectivity. The SSH port 2222 is not open in the firewall.
- B) The sshd_config file has a syntax error. The administrator should fix the error before restarting sshd to avoid losing remote access.
- C) The current sshd process detected a conflict. Stop sshd before running sshd -t.
- D) The sshd -t test failed because the current sshd is already running on port 22. Change the port back to 22.

Correct Answer: B) The sshd_config file has a syntax error. The administrator should fix the error before restarting sshd to avoid losing remote access.

Distractor Analysis:

- Why A is incorrect: The -t flag in sshd -t stands for test (configuration syntax check), not TCP. It parses the configuration file and reports errors without starting or connecting to any network port.
- Why C is incorrect: sshd -t does not conflict with a running sshd process. The test mode parses the configuration file only; it does not start a listener. It can be run safely while sshd is running.
- Why D is incorrect: sshd -t does not fail because of the current running port. The test checks configuration file syntax, not whether a port is already in use. The administrator chose port 2222, which is a valid configuration.

---

**Question 10**

An administrator creates an SSH tunnel with the command:
ssh -N -f -L 5432:db-internal:5432 jumpuser@jump.example.com

What does this command accomplish?

- A) It opens an interactive SSH session on jump.example.com and connects to the database at db-internal:5432.
- B) It creates a background tunnel so that local connections to port 5432 are forwarded through jump.example.com to db-internal:5432, without starting a remote shell.
- C) It starts the sshd daemon on jump.example.com and configures it to forward database traffic.
- D) It scans port 5432 on db-internal through the jump server to verify the database is listening.

Correct Answer: B) It creates a background tunnel so that local connections to port 5432 are forwarded through jump.example.com to db-internal:5432, without starting a remote shell.

Distractor Analysis:

- Why A is incorrect: The -N flag prevents executing a remote command, so no interactive shell is started. The -f flag runs the SSH process in the background. This command is specifically designed for tunnel-only operation.
- Why C is incorrect: This SSH command is run from the local administrator's machine and connects outbound to jump.example.com. It does not configure or start any daemon on the remote server.
- Why D is incorrect: The -L flag creates a local port forward, not a port scan. The tunnel forwards traffic; it does not scan or probe ports. Port scanning is done with tools like nmap, not SSH -L.
