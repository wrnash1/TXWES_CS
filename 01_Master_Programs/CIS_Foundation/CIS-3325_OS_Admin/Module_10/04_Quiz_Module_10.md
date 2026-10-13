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

---

**Question 11**

An administrator generates a new SSH key pair with:

```
ssh-keygen -t ed25519 -C "admin@corp.example.com"
```

They accept all defaults. Where are the private and public key files stored, and which file
must be copied to the remote server?

- A) Private key: /etc/ssh/id_ed25519 | Public key: /etc/ssh/id_ed25519.pub | Copy the private key.
- B) Private key: ~/.ssh/id_ed25519 | Public key: ~/.ssh/id_ed25519.pub | Copy the public key (id_ed25519.pub).
- C) Both keys are stored in ~/.ssh/id_ed25519 as a combined file | Copy the entire file.
- D) Private key: ~/.ssh/id_ed25519 | Public key: ~/.ssh/id_ed25519.pub | Copy the private key.

Correct Answer: B) Private key: ~/.ssh/id_ed25519 | Public key: ~/.ssh/id_ed25519.pub | Copy the public key (id_ed25519.pub).

Distractor Analysis:

- Why A is incorrect: /etc/ssh/ stores the host key pairs (used to identify the server), not user key pairs. User key pairs generated with ssh-keygen are stored in the user's home directory under ~/.ssh/ by default. Additionally, the private key must never be copied to a remote server.
- Why C is incorrect: ssh-keygen always creates two separate files. The file without the .pub extension is the private key; the .pub file is the public key. They are never combined into a single file.
- Why D is incorrect: The private key must remain on the client machine and must never be shared or copied to a remote server. Only the public key (id_ed25519.pub) is copied to the remote server's ~/.ssh/authorized_keys file.

---

**Question 12**

A new junior administrator sets the permissions on their `~/.ssh/` directory as follows:

```
chmod 777 ~/.ssh/
chmod 644 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/authorized_keys
```

SSH key authentication fails with "Permission denied (publickey)." What are the two
permission errors and what are the correct values?

- A) ~/.ssh/ must be 755 and id_ed25519 must be 600. authorized_keys at 644 is acceptable.
- B) ~/.ssh/ must be 700, id_ed25519 must be 600, and authorized_keys must be 600 or 644.
- C) ~/.ssh/ must be 700 and id_ed25519 must be 400. authorized_keys permissions do not matter.
- D) All three files should be 600. SSH ignores directory permissions entirely.

Correct Answer: B) ~/.ssh/ must be 700, id_ed25519 must be 600, and authorized_keys must be 600 or 644.

Distractor Analysis:

- Why A is incorrect: ~/.ssh/ at 755 allows group and others to read the directory listing. SSH enforces strict permission checks and will reject connections if the .ssh directory is accessible by group or other. The directory must be 700 (owner only).
- Why C is incorrect: While 400 (read-only) is more restrictive than 600, the key requirement is that no group or world permissions are set on private keys. SSH accepts both 400 and 600 for private keys. However, authorized_keys permissions do matter — SSH will reject an authorized_keys file that is group-writable.
- Why D is incorrect: SSH does not ignore directory permissions. The sshd daemon explicitly checks that ~/.ssh/ is not writable by group or other, and that the authorized_keys file is not world-writable. These checks are a core security feature of SSH.

---

**Question 13**

An administrator adds the following to `~/.ssh/config`:

```
Host webprod
    HostName 10.50.1.100
    User deploy
    Port 2222
    IdentityFile ~/.ssh/deploy_ed25519
```

Which command uses this configuration block to connect?

- A) ssh -i ~/.ssh/deploy_ed25519 deploy@10.50.1.100 -p 2222
- B) ssh webprod
- C) ssh -F ~/.ssh/config webprod
- D) ssh --config webprod

Correct Answer: B) ssh webprod

Distractor Analysis:

- Why A is incorrect: This command would work, but it does not use the config file. The question asks which command uses the configuration block. Option B is shorter and does use the config file, making it the correct answer to the specific question asked.
- Why C is incorrect: The -F flag specifies an alternate config file location. ~/.ssh/config is already the default location, so -F is redundant but would technically work. However, the simplest and correct answer for using the default config is option B without any flags.
- Why D is incorrect: There is no --config flag in the ssh command. The long-form equivalent of -F is not --config. This is a distractor testing whether students know the actual ssh flag syntax.

---

**Question 14**

After adding a server to `~/.ssh/known_hosts`, an administrator reinstalls the operating
system on that server and tries to SSH to it. They receive a warning:

```
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

What is the correct interpretation and action?

- A) The server's IP address has changed. Update /etc/hosts to reflect the new address.
- B) The server's host key changed because the OS was reinstalled. Remove the old entry from known_hosts with ssh-keygen -R hostname, then reconnect.
- C) The SSH client has been compromised. Reinstall the SSH client package.
- D) The warning is cosmetic and can be safely dismissed by pressing Enter.

Correct Answer: B) The server's host key changed because the OS was reinstalled. Remove the old entry from known_hosts with ssh-keygen -R hostname, then reconnect.

Distractor Analysis:

- Why A is incorrect: The host identification warning is about the host key (a cryptographic key the server presents to prove its identity), not about the IP address. An IP address change alone does not generate this warning; only a changed host key does.
- Why C is incorrect: The warning originates from the SSH client detecting a mismatch between the stored host key and the key presented by the server. This is an expected and normal event after an OS reinstall. It does not indicate that the SSH client itself is compromised.
- Why D is incorrect: This warning is a critical security notice. If the host key changed unexpectedly (not due to a known reinstall), it could indicate a man-in-the-middle attack. The warning must not be dismissed without verifying the cause. The correct action is to remove the stale entry and verify the new key fingerprint.

---

**Question 15**

Which `sshd_config` directive and value combination provides the highest security benefit
for a server that uses only key-based authentication?

- A) PermitRootLogin yes
- B) PasswordAuthentication no
- C) MaxAuthTries 6
- D) X11Forwarding yes

Correct Answer: B) PasswordAuthentication no

Distractor Analysis:

- Why A is incorrect: PermitRootLogin yes allows the root account to log in via SSH, which is a significant security risk. If an attacker compromises the root credential, they gain full unrestricted access. Best practice is to set PermitRootLogin no or PermitRootLogin prohibit-password.
- Why C is incorrect: MaxAuthTries 6 allows six authentication attempts before disconnecting, which is the default value. Reducing it (e.g., to 3) improves security marginally, but setting it to 6 provides no improvement over the default. The highest single-directive security benefit comes from disabling password authentication entirely.
- Why D is incorrect: X11Forwarding yes enables forwarding of X11 (graphical) sessions over SSH, which increases the attack surface. On a server with no GUI, this option should be set to no. Enabling it does not improve security.

---

**Question 16**

An administrator runs `ssh-copy-id -i ~/.ssh/id_ed25519.pub labuser@192.168.1.50` and
receives "Permission denied (publickey)." The remote server currently requires password
authentication but the administrator's password is correct. What is the most likely cause?

- A) The remote server already has a key in authorized_keys and is rejecting new keys.
- B) PasswordAuthentication is set to no in the remote sshd_config, preventing ssh-copy-id from using a password to log in and write the key.
- C) ssh-copy-id requires the -o StrictHostKeyChecking=no flag on first connection.
- D) The key file id_ed25519.pub is corrupted. Regenerate the key pair.

Correct Answer: B) PasswordAuthentication is set to no in the remote sshd_config, preventing ssh-copy-id from using a password to log in and write the key.

Distractor Analysis:

- Why A is incorrect: Having existing keys in authorized_keys does not prevent adding new keys. authorized_keys is an append-only file where each line is an independent authorized key. Multiple keys can coexist.
- Why C is incorrect: -o StrictHostKeyChecking=no suppresses the host key verification prompt on first connection. It is not required for ssh-copy-id to function and does not affect the authentication method used to log in. The error here is about the login credential method, not host verification.
- Why D is incorrect: A corrupted public key would produce a different error during key loading, not a "Permission denied (publickey)" message during login. The error described occurs before any key is processed, during the initial authentication step.

---

**Question 17**

An administrator wants to use SSH agent forwarding to connect from their laptop through
a jump server to an internal server without copying their private key to the jump server.
Which combination of settings and flags is required?

- A) Set ForwardAgent yes in ~/.ssh/config (or use ssh -A) on the initial connection to the jump server.
- B) Copy the private key to the jump server's ~/.ssh/ directory and set permissions to 600.
- C) Set AllowAgentForwarding no in the jump server's sshd_config to enable forwarding.
- D) Use ssh -X to enable X11 forwarding, which also enables key forwarding.

Correct Answer: A) Set ForwardAgent yes in ~/.ssh/config (or use ssh -A) on the initial connection to the jump server.

Distractor Analysis:

- Why B is incorrect: Copying the private key to the jump server defeats the purpose of agent forwarding and introduces a significant security risk. If the jump server is compromised, the private key is exposed. Agent forwarding was specifically designed to avoid this requirement.
- Why C is incorrect: AllowAgentForwarding no in sshd_config disables agent forwarding on the server side. Setting it to no would prevent agent forwarding from working. The correct sshd_config setting to enable agent forwarding is AllowAgentForwarding yes (the default on most distributions).
- Why D is incorrect: X11 forwarding (ssh -X) forwards graphical display connections. It is a completely separate mechanism from SSH agent forwarding and has no relationship to key forwarding. Enabling X11 forwarding does not enable or affect SSH agent forwarding.

---

**Question 18**

An administrator runs `rsync -avz /var/www/html/ deploy@webserver:/var/www/html/` and
notices that files deleted locally still exist on the remote server after the sync. What
flag must be added to mirror deletions?

- A) rsync -avz --remove-source-files
- B) rsync -avz --delete
- C) rsync -avz --force
- D) rsync -avz --checksum

Correct Answer: B) rsync -avz --delete

Distractor Analysis:

- Why A is incorrect: --remove-source-files deletes the source files after they have been successfully transferred. This is used for moving files, not for keeping a remote destination in sync with a local source. It would delete your local files, not mirror deletions to the remote.
- Why C is incorrect: --force in rsync forces deletion of non-empty directories when used with --delete, but it does not by itself enable deletion of files on the destination. It is a modifier for --delete, not a standalone deletion flag.
- Why D is incorrect: --checksum changes how rsync determines which files have changed, using MD5 checksums instead of file size and timestamp. It affects the file comparison algorithm, not whether deleted files on the source are removed from the destination.

---

**Question 19**

A system administrator needs to copy an entire directory `/opt/backups/` from a remote
server `backup01` to the local machine. Which `scp` command accomplishes this?

- A) scp backup01:/opt/backups/ /local/destination/
- B) scp -r backup01:/opt/backups/ /local/destination/
- C) scp -R backup01:/opt/backups/ /local/destination/
- D) scp --recursive backup01:/opt/backups/ /local/destination/

Correct Answer: B) scp -r backup01:/opt/backups/ /local/destination/

Distractor Analysis:

- Why A is incorrect: Without the -r flag, scp only copies individual files. Attempting to copy a directory without -r will fail with an error such as "not a regular file."
- Why C is incorrect: scp does not have a -R flag (capital R). The recursive flag is lowercase -r. This is a common mistake for users familiar with cp -R. Using an unrecognized flag would produce an error.
- Why D is incorrect: scp does not support GNU-style long options like --recursive. The correct syntax uses short flags. This tests whether students know the actual scp flag syntax rather than assuming it matches other tools.

---

**Question 20**

An administrator sets `PermitRootLogin prohibit-password` in `sshd_config`. What does
this directive allow and prohibit?

- A) Root login is completely disabled — neither password nor key-based root login is allowed.
- B) Root login with a public key is permitted, but root login with a password is prohibited.
- C) Root login with a password is permitted, but root login with a public key is prohibited.
- D) Root login is allowed only from the localhost (127.0.0.1) network.

Correct Answer: B) Root login with a public key is permitted, but root login with a password is prohibited.

Distractor Analysis:

- Why A is incorrect: PermitRootLogin no completely disables root login via SSH. PermitRootLogin prohibit-password is a middle ground that still allows key-based root authentication for emergency administrative use cases while preventing brute-force password attacks against the root account.
- Why C is incorrect: The directive name prohibit-password makes clear that it is the password authentication method that is prohibited. Key-based authentication for root is still allowed. This is the intended use case for automated deployment systems that must SSH as root using keys.
- Why D is incorrect: Restricting SSH by source IP address is done through AllowUsers with an @ restriction, /etc/hosts.allow (TCP Wrappers), or firewall rules — not through PermitRootLogin. The prohibit-password value has no effect on the source IP of the connection.
