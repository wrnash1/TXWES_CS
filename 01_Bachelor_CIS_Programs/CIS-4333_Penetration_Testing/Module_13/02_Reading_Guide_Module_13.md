# Reading Guide: Module 13 — Maintaining Access & Pivoting

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

This reading guide supports Module 13 and prepares you for the CompTIA PenTest+ exam's maintaining access and pivoting content in Domain 3: Attacks and Exploits. These techniques demonstrate the full depth of impact from a compromise — turning a single foothold into documented evidence that an attacker could traverse the entire network. Understanding these techniques is equally valuable for defenders designing detection and response strategies.

---

## Primary Reading Topics

### 1. Persistence Mechanisms on Linux

Review each Linux persistence technique in detail:

- Cron jobs: `/etc/crontab`, `/var/spool/cron/crontabs/`, `/etc/cron.d/` — understand the format, execution timing, and the user context each cron location runs under
- SSH `authorized_keys`: adding an attacker's public key enables passwordless authentication indefinitely; the file is at `~/.ssh/authorized_keys`; permissions must be `600` or SSH rejects it
- Shell profile persistence: adding commands to `~/.bashrc`, `~/.profile`, or `/etc/profile` executes them when the user opens a shell
- Bind vs. reverse shells: a bind shell listens on the target; a reverse shell connects back to the attacker — reverse shells bypass most firewalls because outbound connections are generally less restricted

### 2. Persistence Mechanisms on Windows

Review each Windows persistence mechanism tested on PenTest+:

- Registry Run Keys: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` (user privileges, current user only) and `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` (admin privileges, all users)
- `RunOnce` keys: execute once at next login then delete themselves — useful for one-time payloads
- Scheduled Tasks: `schtasks /create` with triggers including `onlogon`, `onstart`, `daily`, and time-based triggers; can run as `SYSTEM`
- Startup Folder: user-level at `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`; system-level at `%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Startup`
- Windows services: require administrator rights but survive reboots and run independently of user sessions; the `sc create` command registers a new service
- DLL hijacking as a persistence mechanism: placing a malicious DLL in a directory searched before the legitimate DLL location

### 3. Command-and-Control Frameworks

Review these C2 frameworks at a conceptual level for the exam:

- Metasploit Meterpreter: in-memory payload, encrypted communications, extensive post-exploitation module library; `multi/handler` listener receives callbacks
- Cobalt Strike: commercial red team framework; Beacon payload; malleable C2 profiles configure communication to mimic legitimate applications; used by many threat actors (important for detection and threat intelligence context)
- Empire/PowerShell Empire: open-source PowerShell-based C2; operates in-memory without dropping executables; relevant to LOLBAS and fileless attack techniques
- The distinction between a "backdoor" (simple persistent shell) and a "C2 implant" (feature-rich, encrypted, multi-function agent)

### 4. SSH Tunneling Techniques

Review the three forms of SSH port forwarding in detail:

- Local port forwarding (`-L`): binds a local port on the attacker machine and forwards to a destination via the SSH server — enables reaching internal services through a jump host
- Remote port forwarding (`-R`): binds a port on the SSH server and forwards back to the attacker machine — useful for exposing attacker services through the target network
- Dynamic port forwarding (`-D`): creates a SOCKS4/SOCKS5 proxy on the attacker machine that dynamically forwards all connections through the SSH tunnel — the most flexible pivoting technique
- `proxychains`: a tool that intercepts network calls from any command and routes them through configured SOCKS/HTTP proxies; configured in `/etc/proxychains4.conf`

### 5. Network Pivoting with Metasploit

Review Metasploit's built-in pivoting capabilities:

- `route add <subnet> <session_id>`: routes traffic to a subnet through an existing Meterpreter session
- `auxiliary/server/socks_proxy`: creates a SOCKS proxy through active sessions for use with proxychains
- `portfwd add -l <local_port> -p <remote_port> -r <remote_host>`: Meterpreter command for port forwarding through a session
- The difference between routing through Metasploit versus SSH dynamic forwarding: Metasploit routes only apply within the MSF console; SSH dynamic forwarding works with any tool that supports proxychains

### 6. Lateral Movement Methods

Review each lateral movement technique and the appropriate tool:

- PsExec (Impacket `psexec.py`): SMB-based remote execution; requires administrator credentials or hashes; drops a service binary (detectable)
- WMI (Impacket `wmiexec.py`): Windows Management Instrumentation remote execution; less noisy than PsExec; does not create a service
- SMBexec (Impacket `smbexec.py`): SMB execution without service installation; uses SMB shares for command I/O
- RDP with pass-the-hash: requires restricted admin mode to be enabled; `xfreerdp /pth:` supports hash-based RDP
- SSH lateral movement: using stolen SSH keys or forwarded SSH agents to chain through multiple Linux hosts
- `net use` for mapping shares: authenticate to network shares using credentials for data access or pivoting

### 7. Data Exfiltration Concepts

Review these exfiltration channels and their detection implications:

- DNS tunneling: encodes data in DNS query labels; uses `dnscat2` or `iodine`; nearly universally permitted outbound; detected by high DNS query volume, unusual query lengths, and non-existent domain lookups
- HTTP/HTTPS: common and difficult to block; TLS inspection can detect anomalous certificate authorities; traffic analysis identifies unusual data volumes
- ICMP tunneling: embeds data in ping payloads using `ptunnel` or similar tools; ping is often permitted outbound; detected by large or unusual ICMP payload sizes
- Protocol selection for stealth: exfiltrating over protocols that match normal baseline traffic for the environment is more difficult to detect

### 8. Cleanup and Artifact Removal

Review cleanup responsibilities as a PenTest+ exam topic:

- Every modification during the test must be documented with a before state, after state, and restoration timestamp
- Persistence mechanisms installed must be removed: cron entries, registry keys, scheduled tasks, SSH keys, service entries
- Tools and payloads dropped on disk must be deleted
- The final report should include a cleanup confirmation section listing all verified removals
- When cleanup is not fully complete, remaining artifacts must be explicitly documented in the report with instructions for the client
- Log modification (clearing event logs) must be explicitly authorized in the Rules of Engagement — and even when authorized, the fact that logs were cleared should be documented as a finding to demonstrate that an attacker would have done so

---

## Key Vocabulary

Review and be able to define each of the following:

- Persistence
- Registry Run Keys
- Scheduled Task
- Startup folder
- Cron job
- SSH authorized keys
- Bind shell
- Reverse shell
- Meterpreter
- Cobalt Strike
- Empire
- C2 (Command and Control)
- Malleable C2 profile
- Local port forwarding
- Remote port forwarding
- Dynamic port forwarding
- SOCKS proxy
- Proxychains
- Metasploit route
- PsExec
- WMI (Windows Management Instrumentation)
- SMB lateral movement
- RDP (Remote Desktop Protocol)
- Pass-the-hash (for lateral movement context)
- DNS tunneling
- ICMP tunneling
- Exfiltration
- DLL hijacking
- Artifact cleanup
- Fileless malware

---

## Study Questions

These questions are for self-study and are not submitted.

1. What is the difference between a reverse shell and a bind shell? In which network scenario would you use each?

2. Explain the difference between HKCU and HKLM Run keys for Windows persistence. Which requires administrator privileges and which does not?

3. Describe dynamic port forwarding with SSH. What tool do you use alongside it to route arbitrary commands through the proxy?

4. A tester has a Meterpreter session on host `192.168.1.10`. This host has a second NIC on the `10.0.0.0/24` network. How would the tester route Metasploit traffic to reach hosts on `10.0.0.0/24`?

5. What makes WMI-based lateral movement less detectable than PsExec? What specifically does PsExec do that WMI does not?

6. Why is DNS tunneling particularly difficult to block at the network level? What monitoring approach can detect it?

7. List three artifacts a penetration tester must clean up after completing a post-exploitation phase. Why is cleanup documentation important?

8. What is the purpose of a malleable C2 profile in Cobalt Strike? What detection technique is it designed to evade?

9. A client's Rules of Engagement authorize persistence testing but require cleanup within 24 hours of test completion. The tester adds a cron job and a registry Run key. What specific cleanup steps are required for each?

10. Why is ICMP tunneling less reliable than DNS tunneling for data exfiltration even when ICMP is permitted outbound?

---

## Recommended Resources

- Metasploit documentation: docs.metasploit.com — routing, pivoting, and Meterpreter
- Proxychains: github.com/haad/proxychains
- Impacket (psexec, wmiexec, smbexec): github.com/fortra/impacket
- MITRE ATT&CK — Persistence techniques: attack.mitre.org/tactics/TA0003
- MITRE ATT&CK — Lateral Movement: attack.mitre.org/tactics/TA0008
- MITRE ATT&CK — Exfiltration: attack.mitre.org/tactics/TA0010
- TryHackMe "Wreath" network room — multi-host pivoting exercise (strongly recommended)
- TryHackMe "Post-Exploitation Basics" room
- HackTricks pivoting: book.hacktricks.xyz/generic-methodologies-and-resources/tunneling-and-port-forwarding

The TryHackMe "Wreath" room is particularly recommended. It is a multi-machine network that requires pivoting through two hops to reach the final target — exactly the scenario this module prepares you for.

---

## CompTIA PenTest+ Exam Objectives Covered

The following PT0-002 exam objectives are addressed in this module:

- 3.4: Given a scenario, perform post-exploitation techniques

This objective explicitly tests: persistence mechanisms, pivoting, tunneling, lateral movement, and cleanup. The exam presents scenario questions where you must select the appropriate persistence technique for a given context, identify the correct tunneling command syntax, or recognize which lateral movement technique matches a described scenario.

---

## 9. Supplemental Resources

**1. MITRE ATT&CK — Persistence Tactic (TA0003)**
https://attack.mitre.org/tactics/TA0003/
The MITRE ATT&CK framework's full catalog of persistence techniques used by real threat actors, including registry Run keys, scheduled tasks, cron jobs, and SSH authorized keys. Each technique page includes detection guidance, data sources, and real-world usage by named threat groups.

**2. HackTricks — Tunneling and Port Forwarding**
https://book.hacktricks.xyz/generic-methodologies-and-resources/tunneling-and-port-forwarding
A comprehensive reference covering SSH tunneling, Metasploit pivoting, proxychains, and alternative pivoting tools (Chisel, ligolo-ng, socat). Includes command syntax and common troubleshooting steps for each method — useful as a quick reference during labs.

**3. OffSec — Introduction to Pivoting and Tunneling (PEN-200 Module)**
https://www.offsec.com/courses/pen-200/
The Offensive Security PEN-200 (OSCP) course covers pivoting extensively as a core skill. The publicly available course outline and free introductory materials describe the pivoting methodology and tool selection process used in professional penetration testing and the OSCP exam, which closely aligns with PenTest+ objectives.

---

*End of Module 13 Reading Guide*
