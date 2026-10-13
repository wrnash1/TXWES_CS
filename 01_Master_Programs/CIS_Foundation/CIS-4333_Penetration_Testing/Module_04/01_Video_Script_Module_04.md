# Video Script: Module 04 - Active Reconnaissance - Nmap and Enumeration

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Estimated Duration:** 20-24 minutes
**Professor:** Nash

---

## Pre-Recording Checklist

- [ ] Title slide loaded: "Module 04 - Active Reconnaissance - Nmap and Enumeration"
- [ ] Kali Linux VM running with Nmap installed
- [ ] Lab network isolated — Nmap demos run against authorized lab targets only
- [ ] Sample Nmap output files ready for display

---

## [00:00 - 01:30] Opening

**[SLIDE: Module 04 — Active Reconnaissance - Nmap and Enumeration]**

Welcome back to CIS-4333. I'm Professor Nash. In Module 03 we gathered intelligence using only publicly available sources — WHOIS, DNS, Google dorking, Shodan, LinkedIn. We never touched the target's systems.

Module 04 is where that changes. Active reconnaissance means sending packets to target systems and analyzing the responses. This is the phase where Nmap enters the picture. Nmap is the most widely used network scanner in the world, and it is tested heavily on the CompTIA PenTest+ PT0-002 exam. You need to know its syntax, its scan types, its output formats, and how to interpret its results.

Authorization must be fully in place before any activity in this module. Everything we do here sends traffic to target systems and will appear in their logs.

By the end of this module you will be able to:

- Explain the difference between passive and active reconnaissance
- Describe the six primary Nmap scan types and when to use each
- Interpret Nmap output to identify open ports, services, and operating systems
- Use Nmap service version detection and OS fingerprinting flags
- Apply Nmap NSE scripts for targeted enumeration
- Document active reconnaissance findings in a structured format

---

## [01:30 - 04:30] Active Reconnaissance Fundamentals

**[SLIDE: Active vs. Passive Recap]**

Let's start with a clear distinction. Passive reconnaissance uses third-party sources and leaves no trace on the target's systems. Active reconnaissance sends packets directly to the target — and those packets appear in firewall logs, IDS alerts, and web server access logs.

This distinction matters for two reasons. First, legal: active reconnaissance requires written authorization. You cannot claim your Nmap scan was "passive" because you were curious. Second, operational: stealth-conscious engagements use slow, staged active scanning to avoid triggering intrusion detection systems.

### The Active Reconnaissance Toolkit

The primary tools for active reconnaissance include:

- **Nmap**: port scanning, service detection, OS fingerprinting, scripted enumeration
- **Netcat**: manual banner grabbing, port verification, raw TCP/UDP connections
- **Nikto**: web server scanning — identifies misconfigurations and common vulnerabilities
- **enum4linux**: Windows/Samba enumeration over SMB
- **SNMPwalk**: SNMP community string enumeration
- **WPScan**: WordPress-specific enumeration

Nmap is the foundation. In a professional penetration test, Nmap is typically run first to build the inventory of live hosts and open services that all subsequent testing is built upon.

---

## [04:30 - 10:00] Nmap — Core Scan Types

**[SLIDE: Nmap Scan Type Reference]**

Nmap supports dozens of scan types. You need to know the following six for the PT0-002 exam.

### TCP SYN Scan (-sS)

The TCP SYN scan — also called the half-open scan or stealth scan — is the default Nmap scan when run with root privileges. It works by sending a SYN packet to each target port. If the port is open, the target responds with SYN/ACK. Nmap sends RST to close the connection without completing the TCP handshake, which means the connection is never fully established and may not appear in application-level logs (though it will appear in firewall and IDS logs).

**[SHOW TERMINAL]**

```text
nmap -sS 192.168.1.0/24

Starting Nmap 7.94 ( https://nmap.org )
Nmap scan report for 192.168.1.10
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https
3306/tcp closed mysql
```

### TCP Connect Scan (-sT)

The TCP connect scan completes the full three-way handshake. It is used when root privileges are not available or when SYN scanning is blocked. It is less stealthy than SYN scanning because the full connection is established and will appear in application logs.

### UDP Scan (-sU)

UDP scanning probes UDP ports. Many critical services run over UDP: DNS (port 53), DHCP (67/68), SNMP (161), TFTP (69), NTP (123). UDP scanning is slower than TCP because UDP has no equivalent of a SYN/ACK response — Nmap must wait for ICMP port unreachable messages to identify closed ports.

```text
nmap -sU -p 53,67,68,69,123,161 192.168.1.10
```

### Version Detection (-sV)

Version detection probes open ports to identify the specific service and version running. This is critical for vulnerability analysis — a service version string like "Apache httpd 2.4.49" maps directly to known CVEs.

```text
nmap -sV 192.168.1.10

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
80/tcp open  http    Apache httpd 2.4.49
443/tcp open  ssl/http Apache httpd 2.4.49
```

### OS Detection (-O)

OS detection uses TCP/IP stack fingerprinting — analyzing TTL values, TCP window sizes, and other packet characteristics — to identify the target operating system and version.

```text
nmap -O 192.168.1.10

Running: Linux 5.X
OS details: Linux 5.4 - 5.10
```

### Aggressive Scan (-A)

The aggressive scan flag combines OS detection, version detection, script scanning, and traceroute into a single command. It is thorough but noisy — it generates significantly more traffic than individual scan types and is more likely to trigger IDS alerts.

```text
nmap -A 192.168.1.10
```

---

## [10:00 - 13:30] Nmap Output Formats and Port States

**[SLIDE: Nmap Port States]**

Nmap classifies every probed port into one of six states. You must know all six for the exam.

| State | Meaning |
|---|---|
| open | An application is actively accepting connections on this port |
| closed | The port is accessible but no application is listening |
| filtered | Nmap cannot determine the state; a firewall is likely blocking the probe |
| unfiltered | The port is accessible but Nmap cannot determine open or closed (only returned by ACK scan) |
| open/filtered | Nmap cannot determine if open or filtered (common with UDP scans) |
| closed/filtered | Nmap cannot determine if closed or filtered |

The most important distinction for penetration testing is between **open** (exploit target) and **filtered** (firewall-protected, may warrant further investigation).

### Output Formats

Nmap supports multiple output formats for different use cases:

- `-oN filename` — Normal output (human-readable, saved to file)
- `-oX filename` — XML output (machine-parseable, compatible with Metasploit import)
- `-oG filename` — Grepable output (one line per host, easy to parse with shell tools)
- `-oA basename` — All three formats simultaneously (creates .nmap, .xml, .gnmap files)

Always save Nmap output. Reconstructing a scan from memory is not a substitute for documented results.

---

## [13:30 - 17:00] Nmap NSE Scripts

**[SLIDE: Nmap Scripting Engine (NSE)]**

The Nmap Scripting Engine extends Nmap's capabilities through Lua-based scripts that can perform targeted enumeration, vulnerability detection, and service brute-forcing. NSE scripts are organized into categories.

| Category | Purpose |
|---|---|
| default | Runs with `-sC`; safe, informational scripts |
| safe | Scripts unlikely to crash services or cause harm |
| auth | Authentication-related scripts (anonymous FTP, default creds) |
| vuln | Vulnerability detection scripts |
| exploit | Scripts that attempt exploitation (use with caution) |
| brute | Credential brute-forcing scripts |
| discovery | General information gathering |

**[SHOW TERMINAL]**

Running the default script set against a target (authorized lab environment):

```text
nmap -sC -sV 192.168.1.10

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu
| ssh-hostkey:
|   3072 4a:ab:f5:27:2a:db:78:51:a3:f4:55:2e:d6:49:c6:12 (RSA)
|_  256 d2:a8:46:f3:a1:62:1c:36:5c:1e:5f:b5:dc:a3:c0:c3 (ECDSA)
80/tcp open  http    Apache httpd 2.4.49
|_http-title: Welcome to TargetCorp
|_http-server-header: Apache/2.4.49 (Ubuntu)
```

Running a specific script against SMB (authorized lab environment):

```text
nmap --script smb-vuln-ms17-010 -p 445 192.168.1.10

PORT    STATE SERVICE
445/tcp open  microsoft-ds
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1
|     State: VULNERABLE
|     Risk factor: HIGH
```

---

## [17:00 - 19:30] Interpreting Nmap Output — A Complete Example

**[SLIDE: Reading Nmap Results Professionally]**

Let me walk through interpreting a complete Nmap result as a professional penetration tester would. This is exactly the kind of analysis you will perform in your Module 04 lab.

**[SHOW TERMINAL]**

```text
Nmap scan report for 192.168.10.20
Host is up (0.00089s latency).
Not shown: 990 closed tcp ports (reset)
PORT      STATE    SERVICE       VERSION
21/tcp    open     ftp           vsftpd 2.3.4
22/tcp    open     ssh           OpenSSH 7.2p2 Ubuntu
80/tcp    open     http          Apache httpd 2.2.8
139/tcp   open     netbios-ssn   Samba 3.X - 4.X
443/tcp   filtered https
445/tcp   open     microsoft-ds  Samba 3.X - 4.X
3306/tcp  open     mysql         MySQL 5.0.51a-3ubuntu5
8080/tcp  open     http          Apache Tomcat/Coyote 1.1
OS: Linux 2.6.X (likely Metasploitable 2 — authorized lab target)
```

What does a professional penetration tester see in this output?

Port 21 vsftpd 2.3.4 — this specific version of vsftpd contains a backdoor vulnerability that opens a shell on port 6200 when a smiley face is sent in the username. This is a critical, easily exploitable finding.

Port 22 OpenSSH 7.2p2 — older version of OpenSSH with known vulnerabilities. Note the Ubuntu distribution tag.

Port 80 Apache 2.2.8 — very old Apache version (end-of-life). Many critical CVEs apply.

Port 443 filtered — HTTPS is blocked by a firewall. Worth investigating further.

Ports 139 and 445 Samba — SMB services. Run smb-vuln NSE scripts to identify EternalBlue or other SMB vulnerabilities.

Port 3306 MySQL 5.0.51 — old MySQL version, check for anonymous access and known CVEs.

Port 8080 Tomcat — Apache Tomcat often runs with default credentials. Check for exposed manager application.

---

## [19:30 - 22:00] Enumeration Beyond Nmap

**[SLIDE: Service-Specific Enumeration]**

After Nmap identifies open ports and services, you enumerate each service to gather additional detail. This is still active reconnaissance — you are interacting with target services.

For SSH: banner grabbing reveals the exact version. Attempt to identify supported authentication methods.

For HTTP/HTTPS: use `nikto` for basic web server enumeration. Use `gobuster` or `dirb` for directory brute-forcing. Check for common files like `robots.txt`, `sitemap.xml`, and `.git` directories.

For SMB: use `enum4linux` to enumerate shares, users, groups, and OS information.

For SNMP: use `snmpwalk` with common community strings (`public`, `private`) to retrieve system information, running processes, and network interface data.

For FTP: check for anonymous login. If allowed, list and review accessible files.

All of these enumeration activities must remain within the authorized scope defined in the RoE.

---

## [22:00 - 23:30] Exam Tips and Summary

**[SLIDE: PT0-002 Exam Tips — Module 04]**

Key exam tips for this module:

First: know Nmap's primary scan types by flag and behavior. SYN scan `-sS` is the stealth scan. Connect scan `-sT` completes the full handshake. UDP scan `-sU`. Version detection `-sV`. OS detection `-O`. Aggressive `-A` combines multiple.

Second: know all six Nmap port states — open, closed, filtered, unfiltered, open/filtered, closed/filtered. The exam presents scenarios asking what a specific state indicates.

Third: `filtered` means a firewall or filter is blocking the probe. `closed` means the port is reachable but no service is listening.

Fourth: NSE scripts are organized into categories. The `-sC` flag runs default scripts. The `--script vuln` category runs vulnerability detection scripts.

Fifth: always save Nmap output using one of the output flags. The XML format is importable into Metasploit.

For additional study, visit **professormesser.com** and the official PT0-002 objectives at **comptia.org**.

---

## [23:30 - 24:00] Closing

Your lab for Module 04 provides sample Nmap output and asks you to interpret it — identifying open ports, services, OS guesses, and potential vulnerabilities based on version information. This mirrors exactly what you will do in a real engagement.

Complete your quiz, submit your lab, and I'll see you in Module 05 where we cover automated vulnerability scanning with Nessus and OpenVAS.

---

*All Nmap commands demonstrated in this module are run exclusively in authorized, isolated lab environments. Never run active scanning tools against systems without explicit written authorization.*
