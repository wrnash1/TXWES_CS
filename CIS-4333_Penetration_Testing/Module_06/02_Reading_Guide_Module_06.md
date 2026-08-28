# Reading Guide: Module 06 — Scanning and Enumeration

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

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Introduction

Module 06 covers the active scanning and enumeration phase — the point in the penetration testing lifecycle where we transition from passive intelligence gathering to direct interaction with target systems. This phase falls squarely in PT0-002 Domain 2: Information Gathering and Vulnerability Scanning (22% of exam weight).

Effective scanning means more than running a single Nmap command. Professional testers build a systematic workflow: host discovery, port discovery, service enumeration, and targeted scripting. The results of this phase are the direct inputs to exploitation planning.

**Legal and Ethical Reminder:** All techniques in this module generate network traffic against target systems. Written authorization with explicitly defined scope is required before executing any scan. Unauthorized port scanning may violate the Computer Fraud and Abuse Act and similar laws. All lab work uses isolated, pre-authorized environments only.

---

## 1. Nmap Command Reference

### Scan Type Selection

| Flag | Scan Type | Description | Requires Root |
|------|-----------|-------------|--------------|
| `-sS` | SYN / Stealth | Half-open; no full handshake | Yes |
| `-sT` | TCP Connect | Full three-way handshake | No |
| `-sU` | UDP | Scans UDP ports | Yes |
| `-sn` | Ping sweep | Host discovery only, no port scan | No |
| `-sA` | ACK scan | Firewall rule mapping | Yes |
| `-sN` | NULL scan | No flags set; bypasses some firewalls | Yes |
| `-sF` | FIN scan | FIN flag only; IDS evasion | Yes |
| `-sX` | Xmas scan | FIN, PSH, URG flags; IDS evasion | Yes |

### Port and Target Specification

| Syntax | Effect |
|--------|--------|
| `-p 80` | Single port |
| `-p 22,80,443` | Specific ports |
| `-p 1-1024` | Port range |
| `-p-` | All 65535 ports |
| `--top-ports 100` | 100 most common ports |
| `-iL hosts.txt` | Read targets from file |
| `192.168.1.0/24` | CIDR range |
| `192.168.1.1-254` | IP range |

### Detection and Aggression

| Flag | Function |
|------|---------|
| `-sV` | Service/version detection |
| `-O` | OS fingerprinting |
| `-A` | Aggressive: -sV + -O + -sC + --traceroute |
| `--version-intensity 9` | Maximum version probe intensity |
| `-sC` | Default NSE scripts |
| `--script=NAME` | Specific script |
| `--script=CATEGORY` | Script category |
| `--script-args` | Pass arguments to scripts |

### Timing Templates

| Flag | Name | Use Case |
|------|------|---------|
| `-T0` | Paranoid | IDS evasion; extremely slow |
| `-T1` | Sneaky | IDS evasion; slow |
| `-T2` | Polite | Low bandwidth, minimal disruption |
| `-T3` | Normal | Default behavior |
| `-T4` | Aggressive | Fast; recommended for lab/internal |
| `-T5` | Insane | Very fast; may drop packets |

### Output Formats

| Flag | Format | Extension |
|------|--------|-----------|
| `-oN` | Normal (human readable) | .txt |
| `-oX` | XML (machine readable) | .xml |
| `-oG` | Grepable | .gnmap |
| `-oA` | All three formats | .txt/.xml/.gnmap |

---

## 2. NSE Script Reference

### Script Categories

| Category | Run With | Risk Level | Example Scripts |
|----------|----------|-----------|----------------|
| `default` | `-sC` | Low | `http-title`, `ssh-hostkey` |
| `safe` | `--script=safe` | Very low | Information gathering |
| `discovery` | `--script=discovery` | Low | Network enumeration |
| `vuln` | `--script=vuln` | Medium | CVE checks |
| `auth` | `--script=auth` | Medium | Authentication bypass |
| `brute` | `--script=brute` | High | Credential brute force |
| `exploit` | `--script=exploit` | High | Active exploitation |
| `intrusive` | `--script=intrusive` | High | May crash services |

### High-Value NSE Scripts

```bash
# HTTP enumeration
sudo nmap --script=http-title,http-methods,http-auth 192.168.1.10 -p 80,443,8080

# SMB vulnerability checks
sudo nmap --script=smb-vuln-ms17-010,smb-vuln-ms08-067 192.168.1.10

# SMB enumeration
sudo nmap --script=smb-enum-shares,smb-enum-users,smb-os-discovery 192.168.1.10

# FTP checks
sudo nmap --script=ftp-anon,ftp-bounce,ftp-syst 192.168.1.10 -p 21

# SSH information
sudo nmap --script=ssh-hostkey,ssh2-enum-algos 192.168.1.10 -p 22

# SSL/TLS analysis
sudo nmap --script=ssl-cert,ssl-enum-ciphers 192.168.1.10 -p 443

# SMTP open relay
sudo nmap --script=smtp-open-relay,smtp-commands 192.168.1.10 -p 25

# SNMP enumeration
sudo nmap -sU --script=snmp-info,snmp-brute 192.168.1.10 -p 161
```

---

## 3. Systematic Scan Workflow

### Phase 1 — Host Discovery

```bash
# ICMP ping sweep
sudo nmap -sn 192.168.1.0/24 -oN alive_hosts.txt

# ARP discovery (most reliable on local network)
sudo nmap -PR -sn 192.168.1.0/24

# No ICMP? Try TCP SYN discovery
sudo nmap -PS22,80,443 -sn 192.168.1.0/24
```

### Phase 2 — Full Port Discovery

```bash
# Scan all ports, fast, save results
sudo nmap -p- --min-rate 1000 -T4 192.168.1.10 -oN allports.txt

# Extract just open ports for next phase
grep "^[0-9]" allports.txt | cut -d/ -f1 | tr '\n' ',' | sed 's/,$//'
```

### Phase 3 — Service Enumeration on Open Ports

```bash
# Run on the specific open ports discovered
sudo nmap -sV -O -sC -p 22,80,139,445 192.168.1.10 -oA service_scan
```

### Phase 4 — Targeted NSE and Service-Specific Tools

Based on discovered services, run targeted tools:

```bash
# Web services
nikto -h http://192.168.1.10 -o nikto_output.txt

# SMB
enum4linux -a 192.168.1.10 | tee enum4linux_output.txt

# SNMP
snmpwalk -v2c -c public 192.168.1.10 | tee snmp_output.txt
```

---

## 4. Service-Specific Enumeration Tools

### Nikto Web Server Scanner

```bash
# Basic scan
nikto -h http://TARGET_IP

# HTTPS
nikto -h https://TARGET_IP -p 443

# Specific port
nikto -h TARGET_IP -p 8080

# Output to file
nikto -h TARGET_IP -o report.html -Format htm

# Tuning options (2=auth, 4=XSS, 9=SQLi, b=software, e=retrieve all)
nikto -h TARGET_IP -Tuning 2,4,9
```

Nikto checks: server version and known CVEs, dangerous files (phpinfo.php, .htaccess), HTTP methods enabled (PUT, DELETE, TRACE), directory listing, default credentials, cookie attributes, and content-security-policy headers.

### enum4linux for SMB/NetBIOS

```bash
enum4linux -a TARGET_IP          # Full enumeration
enum4linux -U TARGET_IP          # Users
enum4linux -S TARGET_IP          # Shares
enum4linux -G TARGET_IP          # Groups
enum4linux -P TARGET_IP          # Password policy
enum4linux -o TARGET_IP          # OS information
enum4linux -i TARGET_IP          # Printer information
enum4linux -r TARGET_IP          # RID cycling (user enumeration)
```

### SMBclient and rpcclient

```bash
# List shares (null session — no credentials)
smbclient -L //TARGET_IP -N

# Connect to specific share
smbclient //TARGET_IP/sharename -N

# rpcclient — Windows RPC enumeration
rpcclient -U "" -N TARGET_IP
# Inside rpcclient:
#   enumdomusers    — list domain users
#   enumdomgroups   — list domain groups
#   querydominfo    — domain info
#   getdompwinfo    — password policy
```

### SNMP Enumeration

```bash
# snmpwalk — full MIB tree walk
snmpwalk -v1 -c public TARGET_IP
snmpwalk -v2c -c public TARGET_IP

# Common OIDs
snmpwalk -v2c -c public TARGET_IP 1.3.6.1.2.1.1        # System info
snmpwalk -v2c -c public TARGET_IP 1.3.6.1.2.1.25.4.2.1 # Running processes
snmpwalk -v2c -c public TARGET_IP 1.3.6.1.2.1.25.6.3   # Installed software
snmpwalk -v2c -c public TARGET_IP 1.3.6.1.2.1.4.34     # IP addresses

# snmp-check — formatted output
snmp-check TARGET_IP -c public

# Community string brute force
onesixtyone -c /usr/share/doc/onesixtyone/dict.txt TARGET_IP
```

### Banner Grabbing

```bash
# Netcat
nc -nv TARGET_IP PORT

# curl headers
curl -I http://TARGET_IP

# Telnet
telnet TARGET_IP 25

# openssl for HTTPS
openssl s_client -connect TARGET_IP:443

# Nmap banner script
sudo nmap --script=banner -p PORTS TARGET_IP
```

---

## 5. Port/Service Quick Reference

| Port | Protocol | Service | Common Findings |
|------|----------|---------|----------------|
| 21 | TCP | FTP | Anonymous login, clear-text creds |
| 22 | TCP | SSH | Version-specific CVEs, weak algorithms |
| 23 | TCP | Telnet | Clear-text protocol, should not exist |
| 25 | TCP | SMTP | Open relay, user enumeration via VRFY |
| 53 | TCP/UDP | DNS | Zone transfer, version disclosure |
| 80/443 | TCP | HTTP/HTTPS | Web app vulnerabilities |
| 110/995 | TCP | POP3 | Clear-text email |
| 139/445 | TCP | SMB | EternalBlue, credential attacks |
| 161 | UDP | SNMP | Default community strings |
| 389 | TCP | LDAP | Anonymous bind, user enumeration |
| 3306 | TCP | MySQL | Default/weak credentials |
| 3389 | TCP | RDP | BlueKeep (CVE-2019-0708), brute force |
| 5985 | TCP | WinRM | PowerShell remoting |

---

## 6. PenTest+ Exam Tips

- **Nmap scan type questions**: Know `-sS` (SYN/stealth, requires root), `-sT` (connect, no root), `-sU` (UDP). The exam tests which scan type leaves fewer log entries (SYN).

- **NSE script categories**: The exam distinguishes between `safe`, `default`, `vuln`, `exploit`, and `intrusive`. Know that `intrusive` scripts may crash services and should be used carefully.

- **Nikto vs. Nmap**: Both can test web servers, but Nikto is specialized for web server vulnerability checks. Nmap with `--script=http-*` provides overlapping but different coverage.

- **SNMP community strings**: "public" is read-only, "private" is read-write. These are defaults. SNMPv1 and v2c transmit community strings in plaintext. SNMPv3 provides authentication and encryption.

- **enum4linux purpose**: Specifically designed for Windows and Samba SMB enumeration. It wraps multiple tools (rpcclient, smbclient, net) into a single script.

- **Banner grabbing**: Passive from a logging perspective (the server records your connection) but active recon because you connect to the target service.

- **Output flag mnemonic**: `-oN` = Normal, `-oX` = XML, `-oG` = Grepable, `-oA` = All.

- **Port 445 vs. 139**: Port 445 is direct SMB over TCP/IP. Port 139 is SMB over NetBIOS. Both should be enumerated.

---

## 7. Scanning Methodology Flowchart

```text
Host Discovery (-sn)
        |
        v
Full Port Scan (-p-)
        |
        v
Service/Version Detection (-sV -O)
        |
        +--- HTTP/HTTPS? --> Nikto, web app tools
        |
        +--- SMB (139/445)? --> enum4linux, smbclient
        |
        +--- SNMP (161/UDP)? --> snmpwalk, snmp-check
        |
        +--- FTP (21)? --> Anonymous login check
        |
        +--- SSH (22)? --> Version check, algorithm enum
        |
        v
NSE Targeted Scripts (vuln, auth, discovery)
        |
        v
Banner Grabbing (remaining services)
        |
        v
Document All Findings --> Attack Surface Map
```

---

## 8. Study Checklist

- [ ] Explain the difference between SYN scan and Connect scan, and when each is used
- [ ] List five Nmap flags and their effects
- [ ] Describe what NSE scripts are and name three useful scripts for web or SMB enumeration
- [ ] Run a complete scan workflow against a Metasploitable 2 target in the lab
- [ ] Explain what SNMP community strings are and why default values are dangerous
- [ ] Demonstrate enum4linux usage and interpret the output
- [ ] Explain what information banner grabbing reveals and name two tools to accomplish it
- [ ] Complete the Module 06 lab and submit deliverables
- [ ] Review PT0-002 Domain 2 exam objectives prior to quiz

---

---

## 9. Supplemental Resources

**1. Nmap Network Scanning — Official Reference Guide**
[https://nmap.org/book/](https://nmap.org/book/)
The complete online edition of Gordon "Fyodor" Lyon's Nmap Network Scanning book covers every scan type, NSE scripting, output format, and firewall evasion technique in depth. It is the authoritative reference for all Nmap flags tested in PT0-002 Domain 2 and directly supplements the scanning workflow covered in Module 06.

**2. enum4linux — Tool Documentation and Usage Guide**
[https://github.com/CiscoCXSecurity/enum4linux](https://github.com/CiscoCXSecurity/enum4linux)
The official enum4linux repository includes usage documentation, flag reference, and output interpretation guidance. Understanding enum4linux's null session enumeration capabilities and output format is directly applicable to the SMB enumeration steps in the Module 06 lab and to PT0-002 questions on Windows enumeration techniques.

**3. SNMP Best Practices — SANS Reading Room**
[https://www.sans.org/reading-room/whitepapers/networkdevs/paper/1050](https://www.sans.org/reading-room/whitepapers/networkdevs/paper/1050)
This SANS white paper on SNMP security covers community string vulnerabilities, SNMPv3 configuration, and enumeration risks. It provides the defensive context for understanding why SNMP misconfigurations (default community strings, SNMPv1/v2c exposure) are high-priority findings during a scanning phase.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
