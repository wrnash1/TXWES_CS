# Reading Guide: Module 12 — Post-Exploitation & Privilege Escalation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4333 &BULL; PENETRATION TESTING & ETHICAL HACKING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This reading guide supports Module 12 and prepares you for the CompTIA PenTest+ exam's post-exploitation and privilege escalation content in Domain 3: Attacks and Exploits. Privilege escalation is one of the most heavily tested areas on the exam — the ability to move from a low-privilege foothold to full system control is the core demonstration of impact in a penetration test.

---

## Primary Reading Topics

### 1. Linux Privilege Escalation Fundamentals

Review the mechanisms that make privilege escalation possible on Linux systems:

- The SUID bit allows a binary to run with the owner's effective UID rather than the executing user's UID. Root-owned SUID binaries can be abused to execute shell commands as root.
- Sudo rules in `/etc/sudoers` may grant specific commands to non-root users. Overly permissive rules allow spawning shells or reading files as root.
- Cron jobs in `/etc/crontab`, `/var/spool/cron/`, and `cron.d/` directories run commands on a schedule. If a root-owned cron job runs a world-writable script, that script is a privilege escalation vector.
- Writable paths in the `PATH` environment variable when a privileged script calls binaries without absolute paths.
- Kernel exploits targeting unpatched vulnerabilities in the Linux kernel itself.

### 2. GTFOBins

GTFOBins (gtfobins.github.io) is an essential reference that you must be able to use during labs and understand conceptually for the exam. Review:

- The categories of abuse: shell, file read, file write, SUID, sudo, capabilities
- At least five examples of common binaries with escalation techniques: `find`, `vim`, `python`, `perl`, `awk`, `nmap`, `tar`
- How the same binary may have different escalation techniques depending on whether it is invoked via SUID, sudo, or capabilities
- The concept of "capabilities" as a more granular alternative to SUID in modern Linux systems

### 3. Windows Privilege Escalation Fundamentals

Review these Windows-specific escalation paths:

- Unquoted service paths: how Windows path parsing with spaces works and why unquoted paths are exploitable when write access to parent directories exists
- Weak service binary permissions: when a low-privilege user can overwrite or replace a service executable, they can inject a malicious binary that runs as the service account
- Weak service configuration permissions: `SERVICE_CHANGE_CONFIG` allows modifying the service binary path without needing to replace the file directly
- `AlwaysInstallElevated` registry policy: when set in both HKLM and HKCU, allows any user to install MSI packages as SYSTEM
- Token impersonation: how `SeImpersonatePrivilege` works and which accounts typically hold it (IIS application pool accounts, SQL Server service accounts)
- User Account Control (UAC) bypass techniques and why UAC is a defense-in-depth control rather than a security boundary

### 4. WinPEAS and LinPEAS

Review these enumeration tools:

- WinPEAS and LinPEAS are part of the PEASS-ng (Privilege Escalation Awesome Scripts Suite) project
- Both tools perform comprehensive automated enumeration and highlight findings by color severity: red is most critical
- WinPEAS checks: services, registry, scheduled tasks, network, users, Defender status, UAC level, credentials in common locations
- LinPEAS checks: sudo rules, SUID binaries, cron jobs, writable directories in PATH, kernel version, running processes, network connections
- Always review automated tool output critically — tools flag potential vectors but humans must confirm exploitability

### 5. Credential Dumping Techniques

Review the following credential sources and tools:

- Mimikatz `sekurlsa::logonpasswords`: dumps credentials from LSASS process memory. Requires SeDebugPrivilege (typically requires administrator rights). May return plaintext passwords on older systems or NTLM hashes on modern systems.
- Mimikatz `lsadump::sam`: dumps the SAM (Security Account Manager) database containing local account NTLM hashes
- Impacket `secretsdump.py`: performs credential dumping remotely using SMB with valid admin credentials, without running anything on the target
- `/etc/shadow` on Linux: contains hashed passwords. Root-readable only. Format: `username:$hash_type$salt$hash:...`
- SSH key theft: private keys in `~/.ssh/id_rsa` or `~/.ssh/id_ecdsa` without a passphrase enable passwordless authentication to other systems
- Configuration file hunting: web server config files, database connection strings, `.env` files, and shell history often contain plaintext credentials

### 6. Pass-the-Hash

Review NTLM authentication and pass-the-hash:

- NTLM is a challenge-response protocol. The server sends a challenge, and the client responds with the NTLM hash of the password applied to that challenge.
- Because the hash is the authentication secret (not the plaintext password), a stolen NTLM hash can authenticate directly without cracking it.
- Tools: Impacket `psexec.py`, `wmiexec.py`, `smbexec.py` all support `-hashes` for pass-the-hash
- Mimikatz `sekurlsa::pth` can inject a hash into a process to spawn an authenticated session
- Mitigations: Protected Users group, Credential Guard, disabling NTLM authentication (requires Kerberos everywhere)

### 7. Pass-the-Ticket

Review Kerberos ticket mechanics and ticket abuse:

- A TGT (Ticket Granting Ticket) is issued by the KDC after initial authentication and is used to request service tickets
- A service ticket grants access to a specific service (e.g., CIFS for SMB, HTTP for web services)
- Both TGTs and service tickets are stored in LSASS memory and can be exported with Mimikatz
- Pass-the-Ticket injects a stolen ticket into the current session using `kerberos::ptt`
- Golden Ticket: forging a TGT using the KRBTGT account hash — provides unlimited Kerberos access across the domain
- Silver Ticket: forging a service ticket using a service account hash — provides access to specific services without interacting with the KDC

### 8. LOLBAS and Living Off the Land

Review the LOLBAS project (lolbas-project.github.io):

- LOLBAS documents Windows binaries, scripts, and libraries that are signed by Microsoft but can be abused
- Categories: execute, download, upload, compile, encode/decode, UAC bypass
- Key binaries to know: `certutil.exe`, `mshta.exe`, `regsvr32.exe`, `rundll32.exe`, `msbuild.exe`, `wmic.exe`
- Why these techniques evade detection: the binaries are trusted, signed, and expected to run in enterprise environments
- The Linux equivalent is GTFOBins, which covers similar abuse of standard Unix utilities

---

## Key Vocabulary

Review and be able to define each of the following:

- Post-exploitation
- Privilege escalation
- SUID (Set User ID)
- GTFOBins
- Sudo misconfiguration
- Cron job exploitation
- PATH hijacking
- Kernel exploit
- LinPEAS / WinPEAS
- Unquoted service path
- Weak service permissions
- Token impersonation
- SeImpersonatePrivilege
- AlwaysInstallElevated
- PrintSpoofer
- Mimikatz
- LSASS (Local Security Authority Subsystem Service)
- SAM database
- LSA secrets
- Impacket secretsdump
- Pass-the-hash (PtH)
- Pass-the-ticket (PtT)
- NTLM hash
- TGT (Ticket Granting Ticket)
- Golden Ticket
- Silver Ticket
- KRBTGT
- LOLBAS
- Living off the land

---

## Study Questions

These questions are for self-study and are not submitted.

1. What does the SUID bit do, and why is a root-owned SUID binary a privilege escalation risk?

2. A user's sudo rules show `(ALL) NOPASSWD: /usr/bin/python3`. How would you use this to get a root shell? Reference GTFOBins in your answer.

3. Explain the unquoted service path vulnerability. Write out the three paths Windows would search for a service binary at `C:\Program Files\My App\app.exe` if it were unquoted.

4. What privilege is required for Mimikatz to dump LSASS credentials, and which Windows user typically holds this privilege?

5. Explain the difference between pass-the-hash and pass-the-ticket. Which authentication protocol does each attack target?

6. Why is the `SeImpersonatePrivilege` privilege dangerous when held by a service account? Which tools exploit it?

7. What is a Golden Ticket attack? What credential does the attacker need to forge one, and what level of access does it provide?

8. What is the purpose of LOLBAS? Give two examples of signed Windows binaries that can be abused to download files from the internet.

9. A tester gains access to a Linux system as `www-data`. They run `sudo -l` and see `(root) NOPASSWD: ALL`. What does this mean, and how would they escalate?

10. What is the risk of running a kernel exploit on a production system during a penetration test? How should the tester handle this risk?

---

## Recommended Resources

- GTFOBins: gtfobins.github.io — Linux binary abuse reference
- LOLBAS Project: lolbas-project.github.io — Windows binary abuse reference
- PEASS-ng (WinPEAS/LinPEAS): github.com/carlospolop/PEASS-ng
- HackTricks Privilege Escalation: book.hacktricks.xyz/linux-hardening/privilege-escalation and book.hacktricks.xyz/windows-hardening/privilege-escalation
- Impacket: github.com/fortra/impacket — Python tools for Windows protocol attacks
- TryHackMe "Linux PrivEsc" and "Windows PrivEsc" rooms — browser-accessible labs for both platforms
- Mimikatz documentation: github.com/gentilkiwi/mimikatz

---

## CompTIA PenTest+ Exam Objectives Covered

Primary objective:

- 3.3: Given a scenario, research attack vectors and perform application-based attacks (includes post-exploitation techniques)
- 3.4: Given a scenario, perform post-exploitation techniques

Post-exploitation is explicitly tested including: privilege escalation (Linux and Windows), credential dumping, pass-the-hash, pass-the-ticket, and lateral movement techniques. The exam presents scenario questions where you must identify the correct technique or tool for a specific post-exploitation situation.

---

---

## 9. Supplemental Resources

**1. GTFOBins — Unix Binary Privilege Escalation Reference**
[https://gtfobins.github.io/](https://gtfobins.github.io/)
GTFOBins is the authoritative reference for Unix binary privilege escalation, documenting SUID, sudo, capabilities, and file read/write abuse techniques for hundreds of binaries. It is directly applicable to Module 12 Linux privilege escalation exercises and is the standard field reference for PT0-002 Domain 3 post-exploitation questions.

**2. PEASS-ng — Privilege Escalation Awesome Scripts Suite**
[https://github.com/carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng)
PEASS-ng provides LinPEAS and WinPEAS — automated privilege escalation enumeration scripts for Linux and Windows. Understanding their output is a core skill for Module 12. The GitHub repository includes output interpretation guides and color-coding explanations that directly support reading and analyzing enumeration results in the lab.

**3. HackTricks — Linux and Windows Privilege Escalation**
[https://book.hacktricks.xyz/linux-hardening/privilege-escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)
HackTricks provides comprehensive methodology for both Linux and Windows privilege escalation, covering SUID, sudo, cron jobs, capabilities, token impersonation, service misconfigurations, and kernel exploits. It is organized as a field reference for active engagements and supplements all Module 12 privilege escalation techniques with real-world payload examples.

*End of Module 12 Reading Guide*
