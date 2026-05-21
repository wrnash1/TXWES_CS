# Reading Guide: Module 10 - SSH and Remote Access Security
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 10 – SSH and Remote Access Security**! This week covers secure remote administration of Linux systems — the SSH protocol, key-based authentication, SSH configuration hardening, file transfer with `scp` and `sftp`, and port forwarding. SSH is tested extensively on CompTIA Linux+ XK0-005 under both Domain 1.0 (System Management) and Domain 2.0 (Security).

As you work through this material you will learn how to generate and deploy SSH key pairs, restrict root login, configure the SSH daemon, transfer files securely, and apply hardening best practices that protect remote access from brute-force and credential-based attacks.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SSH (Secure Shell)**: A cryptographic network protocol for secure remote login, command execution, and file transfer over an unsecured network. SSH replaces Telnet and rsh, which transmit data in cleartext. The SSH daemon (`sshd`) listens on TCP port 22 by default. Clients connect with the `ssh user@host` command. All traffic between client and server is encrypted using negotiated symmetric keys established via asymmetric key exchange.
*   **SSH key-based authentication**: An authentication method that uses a cryptographic key pair instead of a password. The user generates a key pair with `ssh-keygen` — a private key (kept on the client, never shared) and a public key. The public key is copied to the server's `~/.ssh/authorized_keys` file using `ssh-copy-id user@host`. When the client connects, the server challenges with a message that only the holder of the private key can decrypt, proving identity without transmitting a password.
*   **`/etc/ssh/sshd_config`**: The main configuration file for the SSH daemon. Critical security directives: `PermitRootLogin no` (disables direct root SSH login), `PasswordAuthentication no` (forces key-based authentication), `Port 2222` (changes the listening port), `AllowUsers alice bob` (restricts which users may log in via SSH). After editing, restart the daemon with `systemctl restart sshd`.
*   **`scp` and `sftp`**: Secure file transfer tools built on SSH. `scp source user@host:/dest` copies files between hosts using SSH encryption, similar to `cp` syntax. `sftp user@host` opens an interactive FTP-like session over SSH for browsing and transferring files. Both tools authenticate using the same SSH credentials (key or password) as the `ssh` command.
*   **SSH port forwarding (tunneling)**: A feature that forwards network connections through an encrypted SSH session. Local forwarding (`ssh -L 8080:internalserver:80 user@jumphost`) makes a remote service available on a local port. Remote forwarding (`ssh -R`) exposes a local port on the remote server. Used to bypass firewalls or encrypt traffic for insecure protocols.
*   **`~/.ssh/` directory and permissions**: SSH enforces strict file permission requirements for security. The `~/.ssh/` directory must be mode `700` (owner read/write/execute only). The `authorized_keys` file must be mode `600` (owner read/write only). The private key file must also be mode `600`. If permissions are too permissive, SSH will refuse to use the keys and log a warning.

---

### 2. Certification Exam Tips
*   **Domain alignment:** SSH and remote access map to Linux+ Domain 1.0 (System Management) and Domain 2.0 (Security). Expect 4–6 questions on key generation, `sshd_config` directives, and hardening.
*   **`ssh-keygen` output files:** The exam tests which file is the public key. `ssh-keygen` produces two files: `id_rsa` (private key — never leave the client) and `id_rsa.pub` (public key — copied to the server). Confusing which goes to the server is a common trap.
*   **`sshd_config` directive trap:** `PermitRootLogin no` prevents root from logging in via SSH but does not disable the root account itself. `PasswordAuthentication no` forces key-only login — if set before deploying keys to a user, that user will be locked out. Know the order of operations.
*   **Port 22 hardening:** Changing the SSH port (`Port 2222`) is security through obscurity — it reduces automated scan noise but does not prevent a determined attacker. The exam may ask which configuration change provides the greatest security improvement: the answer is `PasswordAuthentication no` (disabling password auth) or deploying key-based authentication, not just changing the port.
*   **`ssh-copy-id` vs manual key deployment:** `ssh-copy-id user@host` appends the public key to `~/.ssh/authorized_keys` with correct permissions. Manually copying the key with incorrect permissions on `~/.ssh/` (e.g., mode 755) causes silent authentication failures. The exam tests permission troubleshooting for SSH key auth.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers SSH and secure file transfer in chapter 17. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video walkthroughs of SSH key generation, `sshd_config` hardening, and `scp`/`sftp` usage in a live environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read chapter 17 of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), covering SSH, `scp`, and secure remote access concepts on Linux systems.
*   **Required Video:** Watch the SSH and remote access videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates key generation, server configuration, and secure file transfer with live examples.

---

### Lab & Command Integration
In this week's hands-on lab you will generate an SSH key pair with `ssh-keygen`, copy the public key to a remote host using `ssh-copy-id`, connect without a password, edit `/etc/ssh/sshd_config` to disable password authentication and root login, restart `sshd`, and transfer a file with `scp`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read chapter 17 in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the SSH videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
