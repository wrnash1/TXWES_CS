# Video Script: Module 06 — Scanning and Enumeration

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

### SLIDE 1 — Introduction (0:00–1:00)

Welcome to Module 06: Scanning and Enumeration. I am Professor Nash. This module covers the active phase where passive OSINT ends and we begin direct interaction with target systems — always within written authorization.

Scanning and enumeration is how we transform a list of IP addresses and domain names from recon into a detailed map of open ports, running services, software versions, and potential vulnerabilities. Every piece of information we collect here feeds directly into exploitation planning.

Today's primary tool is Nmap — the Network Mapper. We will also cover Nikto for web server scanning, enum4linux for Windows/Samba enumeration, SMB enumeration techniques, SNMP enumeration, and banner grabbing. These are all explicitly referenced in the CompTIA PenTest+ PT0-002 exam objectives.

Authorization reminder: all techniques in this module generate traffic against target systems. Written authorization with defined scope is mandatory before executing any command shown today.

---

### SLIDE 2 — Nmap Fundamentals (1:00–3:00)

Nmap is the most widely used network scanning tool in the world. It is installed by default on Kali Linux and is available on all major platforms.

The basic Nmap syntax:

```bash
nmap [options] [target]
```

Targets can be a single IP, a hostname, a CIDR range, or a file of targets:

```bash
nmap 192.168.1.1
nmap 192.168.1.0/24
nmap -iL targets.txt
```

### Scan Types

The three most important scan types for PenTest+:

**TCP SYN scan (-sS)** — also called a "stealth" or "half-open" scan. Sends a SYN packet. If the port is open, the target responds with SYN-ACK, but Nmap never completes the handshake — it sends RST instead. Faster than a full connect scan and generates fewer log entries. Requires root/sudo.

```bash
sudo nmap -sS 192.168.1.10
```

**TCP Connect scan (-sT)** — completes the full TCP three-way handshake. Does not require root. More detectable because connections appear in application logs.

```bash
nmap -sT 192.168.1.10
```

**UDP scan (-sU)** — scans for open UDP ports. Slower than TCP scans because UDP does not acknowledge open ports. Critical for finding DNS (53), SNMP (161), DHCP (67/68), and TFTP (69).

```bash
sudo nmap -sU 192.168.1.10
```

---

### SLIDE 3 — Nmap Port States and Selection (3:00–4:30)

Nmap reports ports in one of six states:

- **open** — a service is actively accepting connections
- **closed** — no service listening; port is accessible
- **filtered** — a firewall or packet filter is blocking probes
- **unfiltered** — port is accessible but Nmap cannot determine open/closed
- **open|filtered** — Nmap cannot determine if open or filtered (common in UDP)
- **closed|filtered** — Nmap cannot determine if closed or filtered

Port selection options:

```bash
# Default: top 1000 ports
nmap 192.168.1.10

# Specific ports
nmap -p 22,80,443 192.168.1.10

# Port range
nmap -p 1-1024 192.168.1.10

# All 65535 ports
nmap -p- 192.168.1.10

# Top N most common ports
nmap --top-ports 100 192.168.1.10
```

For thorough assessments, always scan all 65,535 ports. Default scanning misses services running on non-standard ports — a common finding in real engagements.

---

### SLIDE 4 — Service Version Detection and OS Fingerprinting (4:30–6:00)

Open ports tell you a port is open. Service detection tells you what is running. OS fingerprinting tells you what operating system is hosting the service.

```bash
# Service version detection
sudo nmap -sV 192.168.1.10

# OS fingerprinting (requires root)
sudo nmap -O 192.168.1.10

# Combined: version, OS, scripts, traceroute
sudo nmap -A 192.168.1.10
```

The `-A` flag is an aggressive scan combining:

- `-sV` — service version detection
- `-O` — OS fingerprinting
- `-sC` — default NSE scripts
- `--traceroute` — path tracing

Service version detection works by sending service-specific probes and comparing responses against Nmap's `nmap-service-probes` database — over 9,000 probes for hundreds of services.

OS fingerprinting sends a series of TCP, UDP, and ICMP probes and compares the TCP/IP stack behavior against Nmap's OS fingerprint database. Confidence percentage is included in the output.

On the PenTest+ exam, know that `-sV` is version detection and `-O` is OS detection. Both are tested.

---

### SLIDE 5 — Nmap Scripting Engine (6:00–8:00)

The Nmap Scripting Engine (NSE) extends Nmap with over 600 scripts organized into categories. Scripts are written in Lua and can perform discovery, version detection, vulnerability checking, brute forcing, and exploitation.

NSE script categories:

| Category | Purpose |
|----------|---------|
| `auth` | Authentication bypass or brute force |
| `broadcast` | Network discovery via broadcast |
| `brute` | Credential brute forcing |
| `default` | Run with `-sC`; safe and useful |
| `discovery` | Host and service discovery |
| `exploit` | Active exploitation |
| `fuzzer` | Fuzzing inputs to detect crashes |
| `intrusive` | May crash services; use with care |
| `safe` | Unlikely to harm services |
| `vuln` | Vulnerability checks |

Running NSE scripts:

```bash
# Default scripts (safe, common use)
sudo nmap -sC 192.168.1.10

# Specific script
sudo nmap --script=http-title 192.168.1.10

# Script category
sudo nmap --script=vuln 192.168.1.10

# Multiple scripts with arguments
sudo nmap --script=smb-vuln-ms17-010 192.168.1.10
sudo nmap --script=ftp-anon,ftp-bounce 192.168.1.10
```

Useful individual scripts: `http-title`, `http-methods`, `ssl-cert`, `smb-security-mode`, `smb-vuln-ms17-010` (EternalBlue), `ftp-anon`, `ssh-hostkey`, `smtp-open-relay`.

---

### SLIDE 6 — Nmap Output and Timing (8:00–9:30)

### Output Formats

```bash
# Normal output
nmap -oN scan.txt 192.168.1.0/24

# XML output (for import into other tools)
nmap -oX scan.xml 192.168.1.0/24

# Grepable output
nmap -oG scan.gnmap 192.168.1.0/24

# All formats simultaneously
nmap -oA scan_results 192.168.1.0/24
```

### Timing Templates

Nmap timing templates from -T0 (paranoid) to -T5 (insane):

| Template | Use Case |
|----------|---------|
| `-T0` | Extremely slow; IDS evasion |
| `-T1` | Slow; IDS evasion |
| `-T2` | Polite; low bandwidth impact |
| `-T3` | Normal (default) |
| `-T4` | Aggressive; faster, more packets |
| `-T5` | Insane; very fast, may miss results |

For internal lab scans, `-T4` is common. For stealthy assessments, `-T1` or `-T2` reduces detection likelihood. The exam tests that `-T0` and `-T1` are evasion-focused timing options.

---

### SLIDE 7 — Nikto Web Server Scanner (9:30–11:00)

Nikto is an open-source web server scanner that performs comprehensive tests against web servers for dangerous files, outdated server software, and configuration issues.

```bash
# Basic Nikto scan
nikto -h http://192.168.1.10

# With specific port
nikto -h 192.168.1.10 -p 8080

# SSL/HTTPS target
nikto -h https://192.168.1.10

# Output to file
nikto -h 192.168.1.10 -o nikto_output.txt

# Specific tuning (2=auth files, 4=XSS, 9=SQL injection)
nikto -h 192.168.1.10 -Tuning 2,4,9
```

Nikto checks for:

- Outdated server software versions
- Default files and directories (phpinfo.php, test.php, /admin/)
- Dangerous HTTP methods (PUT, DELETE, TRACE)
- Misconfigurations (directory listing enabled)
- Known vulnerabilities by CVE reference
- Cookie and header issues

Important: Nikto is noisy. It generates hundreds of HTTP requests and will appear in web server logs. Use only against authorized targets.

---

### SLIDE 8 — SMB Enumeration (11:00–13:00)

SMB (Server Message Block) is a network file sharing protocol running on ports 139 and 445. It is a primary attack surface on Windows networks because it handles file shares, printers, named pipes, and authentication.

### Nmap SMB Scripts

```bash
# Enumerate SMB shares
sudo nmap --script=smb-enum-shares 192.168.1.10

# Check SMB security mode (signing, authentication level)
sudo nmap --script=smb-security-mode 192.168.1.10

# Check for EternalBlue vulnerability (MS17-010)
sudo nmap --script=smb-vuln-ms17-010 192.168.1.10

# Enumerate OS via SMB
sudo nmap --script=smb-os-discovery 192.168.1.10

# Full SMB script set
sudo nmap --script=smb* 192.168.1.10
```

### enum4linux

enum4linux is specifically designed for enumerating Windows and Samba systems over SMB/NetBIOS:

```bash
# Full enumeration
enum4linux -a 192.168.1.10

# Users only
enum4linux -U 192.168.1.10

# Shares only
enum4linux -S 192.168.1.10

# Password policy
enum4linux -P 192.168.1.10

# Groups and members
enum4linux -G 192.168.1.10
```

enum4linux reveals: usernames, group memberships, share names and permissions, OS version, workgroup/domain, and password policies. This is critical information for follow-on attacks.

### SMBclient

```bash
# List shares (null session)
smbclient -L //192.168.1.10 -N

# Connect to a share
smbclient //192.168.1.10/share -N

# With credentials
smbclient //192.168.1.10/share -U username
```

---

### SLIDE 9 — SNMP Enumeration (13:00–15:00)

SNMP (Simple Network Management Protocol) runs on UDP port 161. It is used for network device management and monitoring. Misconfigured SNMP can expose enormous amounts of information.

SNMP versions:

- **SNMPv1/v2c** — community string authentication (essentially a plaintext password). "public" is the default read community string. "private" is the default write community string. Both are common in poorly configured devices.
- **SNMPv3** — uses proper authentication and encryption. Significantly more secure.

### SNMP Enumeration Commands

```bash
# snmpwalk — walk the full MIB tree using community string "public"
snmpwalk -v2c -c public 192.168.1.10

# Specific OID — system information
snmpwalk -v2c -c public 192.168.1.10 1.3.6.1.2.1.1

# snmp-check — comprehensive SNMP enumeration
snmp-check 192.168.1.10 -c public

# onesixtyone — fast SNMP community string brute force
onesixtyone -c /usr/share/doc/onesixtyone/dict.txt 192.168.1.10
```

### Nmap SNMP Scripts

```bash
sudo nmap -sU -p 161 --script=snmp-info 192.168.1.10
sudo nmap -sU -p 161 --script=snmp-sysdescr 192.168.1.10
sudo nmap -sU -p 161 --script=snmp-brute 192.168.1.10
```

What SNMP exposes: running processes, installed software, network interfaces and IP addresses, routing tables, open TCP connections, user accounts, and hardware information. A default "public" community string on a router or switch is a critical finding.

---

### SLIDE 10 — Banner Grabbing (15:00–16:30)

Banner grabbing captures the service identification string that many servers return upon connection. Banners often reveal software name, version, and sometimes operating system.

```bash
# Netcat banner grab
nc -v 192.168.1.10 22
nc -v 192.168.1.10 80

# Telnet banner grab
telnet 192.168.1.10 25

# curl — web server headers
curl -I http://192.168.1.10

# OpenSSL — SSL/TLS banner
openssl s_client -connect 192.168.1.10:443

# Nmap banner script
sudo nmap --script=banner -p 22,80,443,21 192.168.1.10
```

A typical SSH banner response:

```text
SSH-2.0-OpenSSH_7.4
```

This tells you the SSH version, which can be cross-referenced against CVE databases. A web server responding with `Server: Apache/2.4.49` tells you exactly which Apache version is running — useful for identifying CVE-2021-41773 (path traversal).

Banner grabbing is fast and requires minimal tooling. It is often the quickest way to identify a specific software version for exploitation research.

---

### SLIDE 11 — Building a Systematic Scan Workflow (16:30–18:30)

Professional penetration testers follow a systematic scanning approach:

**Phase 1 — Host Discovery (which hosts are up?):**

```bash
# Ping sweep
sudo nmap -sn 192.168.1.0/24

# ARP discovery (local network, more reliable)
sudo nmap -PR -sn 192.168.1.0/24
```

**Phase 2 — Port Discovery (what ports are open?):**

```bash
# Fast scan of all ports (no version detection yet)
sudo nmap -p- --min-rate 1000 192.168.1.10 -oN ports.txt
```

**Phase 3 — Service Enumeration (what is running on each port?):**

```bash
# Version and OS detection on discovered open ports
sudo nmap -sV -O -p [OPEN_PORTS] 192.168.1.10 -oN services.txt
```

**Phase 4 — Targeted Script Scanning:**

```bash
# Run relevant NSE scripts based on discovered services
sudo nmap --script=vuln -p [OPEN_PORTS] 192.168.1.10
```

**Phase 5 — Service-Specific Tools:**

Based on discovered services, run specialized tools: Nikto for HTTP, enum4linux for SMB, snmpwalk for SNMP, and banner grabbing for remaining services.

---

### SLIDE 12 — Enumeration Results and Analysis (18:30–20:00)

Raw scan output must be translated into an attack surface map. For each open port and service:

1. Record the port, protocol, service name, and version
2. Look up the service version in CVE databases (NVD, Exploit-DB)
3. Note any default credential risks (SNMP public, FTP anonymous)
4. Identify services that warrant manual enumeration
5. Prioritize high-value targets: SMB, RPC, databases, web servers

The scan results document forms the foundation of your exploitation planning. Every target you attempt to exploit should have a corresponding entry in your scan results.

---

### SLIDE 13 — PenTest+ Exam Alignment (20:00–21:30)

For PT0-002, know these key points from Module 06:

Nmap scan types tested: -sS (SYN/stealth), -sT (connect), -sU (UDP), -sP/-sn (host discovery). Know what each does and when to use it.

Nmap flags tested: -sV (version), -O (OS), -A (aggressive), -p (ports), -T0 through -T5 (timing), -oN/-oX/-oG (output).

NSE categories tested: know the difference between `safe`, `default`, `vuln`, `exploit`, and `intrusive`.

Nikto is tested as a web server scanner — noisy, sends many requests, checks for known vulnerabilities.

enum4linux is tested as a Windows/Samba enumeration tool.

SNMP community strings: "public" (read) and "private" (write) are default values. SNMPv1/v2c use community strings; SNMPv3 uses proper authentication.

Banner grabbing is passive enumeration — connecting to a port and reading the service response.

---

### SLIDE 14 — Closing and Lab Preview (21:30–22:30)

Module 06 gave you the active scanning toolkit for penetration testing. Key takeaways:

- Nmap is the Swiss Army knife of network scanning — learn its flags thoroughly
- NSE scripts extend Nmap into a vulnerability assessment tool
- Nikto provides fast, comprehensive web server enumeration
- SMB enumeration with enum4linux is critical on Windows networks
- SNMP with default community strings is a critical misconfiguration
- Banner grabbing is simple but powerful for version identification
- Always save scan output to files for documentation

In the lab, you will run a systematic Nmap scan against a Metasploitable 2 VM and enumerate SMB and SNMP services. In Module 07, we use this map to perform exploitation.

---

### End of Module 06 Video Script

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
