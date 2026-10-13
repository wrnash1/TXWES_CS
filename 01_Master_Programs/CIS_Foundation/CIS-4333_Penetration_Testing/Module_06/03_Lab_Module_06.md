# Lab Activity: Module 06 — Scanning and Enumeration

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Authorization and Legal Notice

> **REQUIRED BEFORE STARTING:** All scanning and enumeration activities in this lab are conducted exclusively against your local isolated lab VM (Metasploitable 2) or the TryHackMe room specified below. You have NO authorization to scan any IP address, hostname, domain, or network that is not explicitly listed in this lab guide or confirmed by Professor Nash. Unauthorized port scanning violates the Computer Fraud and Abuse Act (18 U.S.C. § 1030) and may violate your Internet service provider's terms of service. If your scan target is outside this lab environment, STOP immediately.

---

## Lab Overview

In this lab you will build a complete scanning and enumeration picture of a Metasploitable 2 virtual machine — a purposefully vulnerable Linux VM designed for security training. You will follow the four-phase scanning workflow from the module, then perform service-specific enumeration against SMB and SNMP.

**Estimated Time:** 2–2.5 hours

**Authorized Lab Targets:**

- Metasploitable 2 VM — IP address assigned by your local VM network (typically 192.168.X.X or 10.0.X.X — confirm using your hypervisor's network settings)
- TryHackMe room: "Nmap" — [https://tryhackme.com/room/furthernmap](https://tryhackme.com/room/furthernmap)

**Required Setup:**

- Kali Linux VM (attack machine) and Metasploitable 2 VM on the same isolated host-only network
- Both VMs must NOT be on a network with internet-accessible addresses
- Confirm network isolation before beginning

---

## Prerequisites

- Kali Linux VM running with Nmap, Nikto, enum4linux, smbclient, snmpwalk installed
- Metasploitable 2 VM running and accessible from Kali (ping test: `ping METASPLOITABLE_IP`)
- Lab notebook open for documentation
- Text editor ready for saving scan outputs

---

## Part 1 — Host Discovery and Full Port Scan (30 minutes)

### Step 1.1 — Confirm Target is Alive

Before scanning, verify the target responds:

```bash
ping -c 4 METASPLOITABLE_IP
```

Record: response time, TTL value. What OS does the TTL suggest?

### Step 1.2 — Host Discovery Scan

```bash
sudo nmap -sn 192.168.X.0/24 -oN phase1_hosts.txt
```

Record all live hosts discovered. Note which IP is Metasploitable.

### Step 1.3 — Full Port Scan

Scan all 65,535 TCP ports. Save results.

```bash
sudo nmap -p- --min-rate 1000 -T4 METASPLOITABLE_IP -oN phase2_allports.txt
```

This scan takes 2–5 minutes. While it runs, review the Phase 1 results.

After completion, count the open ports. Record the number.

### Step 1.4 — Extract Open Ports

Identify all open port numbers from your results. You will need these for Phase 3.

Record all open ports in your lab notes as a comma-separated list, for example:

```text
21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,3632,5432,5900,6000,6667,8009,8180
```

---

## Part 2 — Service Enumeration (30 minutes)

### Step 2.1 — Service and Version Detection

Run service detection against the open ports discovered in Part 1:

```bash
sudo nmap -sV -O -sC -p OPEN_PORTS METASPLOITABLE_IP -oA phase3_services
```

This produces three output files: `phase3_services.nmap`, `phase3_services.xml`, and `phase3_services.gnmap`.

In your lab notes, create a service table:

| Port | Protocol | Service | Version | Notes |
|------|----------|---------|---------|-------|
| 21 | TCP | FTP | vsftpd 2.3.4 | Known backdoor CVE |
| 22 | TCP | SSH | OpenSSH 4.7p1 | Outdated version |
| ... | ... | ... | ... | ... |

Fill in all open ports from your scan.

### Step 2.2 — Identify Potential Vulnerabilities

For each service discovered, look up the version in the National Vulnerability Database at [https://nvd.nist.gov](https://nvd.nist.gov) or [https://www.exploit-db.com](https://www.exploit-db.com).

Record at least three CVEs corresponding to services found on Metasploitable. For each CVE note:

- CVE identifier
- CVSS score
- Brief description of the vulnerability
- Which service/version is affected

---

## Part 3 — NSE Script Scanning (20 minutes)

### Step 3.1 — Vulnerability Scripts

Run Nmap's vulnerability script category against your target:

```bash
sudo nmap --script=vuln -p OPEN_PORTS METASPLOITABLE_IP -oN phase4_vuln.txt
```

Note: this may take 5–10 minutes. Record any scripts that return positive findings.

### Step 3.2 — SMB-Specific Scripts

```bash
sudo nmap --script=smb-vuln-ms17-010,smb-enum-shares,smb-os-discovery,smb-security-mode METASPLOITABLE_IP -oN smb_scripts.txt
```

Record: Does EternalBlue (MS17-010) apply to this target? What shares are visible? What is the SMB security mode?

### Step 3.3 — FTP Anonymous Check

```bash
sudo nmap --script=ftp-anon METASPLOITABLE_IP -p 21
```

Does FTP anonymous login succeed? What files are visible?

---

## Part 4 — SMB Enumeration with enum4linux (20 minutes)

### Step 4.1 — Full SMB Enumeration

```bash
enum4linux -a METASPLOITABLE_IP | tee enum4linux_full.txt
```

From the output, document:

- Operating system and version
- Workgroup or domain name
- Share names and permissions (read/write/no access)
- User accounts enumerated (if any)
- Password policy (minimum length, lockout threshold)

### Step 4.2 — Null Session Test

Attempt to connect to shares using a null session (no credentials):

```bash
smbclient -L //METASPLOITABLE_IP -N
```

Which shares allow null session listing? What does this indicate about the SMB configuration?

---

## Part 5 — SNMP Enumeration (20 minutes)

### Step 5.1 — Confirm SNMP is Running

```bash
sudo nmap -sU -p 161 METASPLOITABLE_IP
```

Is SNMP open? What version is indicated?

### Step 5.2 — Community String Discovery

```bash
onesixtyone -c /usr/share/doc/onesixtyone/dict.txt METASPLOITABLE_IP
```

Which community strings respond? Record them.

### Step 5.3 — Full SNMP Walk

Using the community string discovered (likely "public"):

```bash
snmpwalk -v2c -c public METASPLOITABLE_IP | tee snmp_full.txt
```

From the output, record:

- System description (OS, version, hardware)
- Running processes (at least five)
- Network interfaces and IP addresses
- Any usernames visible in the MIB data

---

## Part 6 — Nikto Web Server Scan (15 minutes)

### Step 6.1 — Basic Nikto Scan

Metasploitable runs a vulnerable web server on port 80:

```bash
nikto -h http://METASPLOITABLE_IP -o nikto_output.txt
```

From the output, document:

- Server software and version reported
- Number of items found
- At least three specific findings (dangerous files, missing headers, vulnerabilities)
- Any CVE references cited by Nikto

### Step 6.2 — Banner Grabbing

Grab banners from at least three services:

```bash
# HTTP
curl -I http://METASPLOITABLE_IP

# FTP
nc -nv METASPLOITABLE_IP 21

# SSH
nc -nv METASPLOITABLE_IP 22
```

For each banner, record: exact text returned, software version revealed, and whether that version has known CVEs.

---

## Deliverables

Submit the following to the Canvas assignment portal:

1. **Phase 2 port scan screenshot** — showing all open ports discovered
2. **Service table** — completed table with port, protocol, service, version, and notes
3. **CVE research** — three CVEs identified for Metasploitable services with CVSS scores and descriptions
4. **enum4linux output excerpt** — showing shares and user enumeration results
5. **SNMP findings summary** — system info, processes, interfaces from snmpwalk
6. **Nikto output screenshot** — showing at least three findings
7. **Attack surface summary** — 200–300 words describing the overall vulnerability picture of the target based on your enumeration, and which services you would prioritize for exploitation and why

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|---------|
| Port scan output | 15 | Screenshot shows full port list with status |
| Service table | 20 | All open ports documented with version info |
| CVE research | 15 | Three CVEs with CVSS scores and descriptions |
| enum4linux findings | 15 | Shares and user data correctly extracted |
| SNMP findings | 15 | System info, processes, interfaces documented |
| Nikto output | 10 | Three or more findings identified |
| Attack surface summary | 10 | Professional, specific, prioritized analysis |
| **Total** | **100** | |

---

## Troubleshooting

**Metasploitable not responding to ping:**
Check that both VMs are on the same host-only adapter in your hypervisor. Use `ip addr` on both machines to verify they share a subnet.

**Nmap scan taking more than 15 minutes:**
Your `-min-rate` may be too low or the target is not responding. Try `-T4 --min-rate 5000` on a host-only network.

**enum4linux returns empty results:**
Try `enum4linux -a -r METASPLOITABLE_IP`. The `-r` flag enables RID cycling for user enumeration.

**SNMP returns nothing:**
Verify UDP port 161 is open: `sudo nmap -sU -p 161 METASPLOITABLE_IP`. Metasploitable 2 does run SNMP — if it is not responding, confirm the VM is fully booted.

**Nikto hangs:**
Set a timeout: `nikto -h TARGET_IP -timeout 10`. This limits each request to 10 seconds.

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Phased Scan Workflow Analysis

Using your authorized Metasploitable 2 lab target, execute a fully documented phased scan workflow. First, run a fast full-port SYN scan to discover all open ports: `nmap -sS -p- -T4 --min-rate 5000 METASPLOITABLE_IP -oN phase1_discovery.txt`. Second, extract only the open port numbers from that output and run a targeted version and OS detection scan on those ports only: `nmap -sV -O -sC -p <open_ports> METASPLOITABLE_IP -oN phase2_detail.txt`. Compare the time each phase took and the volume of output generated. Write a structured analysis explaining: why running version detection only on confirmed open ports is more efficient than running it across all 65,535 ports, what information was present in phase 2 that was absent in phase 1, and when a single-phase comprehensive scan (`-A -p-`) might be appropriate versus when the two-phase approach is required.

### Challenge 2: Service-to-CVE Research Documentation

From your phase 2 scan output, select any three services that returned version strings (e.g., vsftpd 2.3.4, OpenSSH 4.7p1, Apache 2.2.8). For each service, complete a structured vulnerability research entry containing: the exact version string from the scan, the CVE identifier for the most critical known vulnerability, the CVSS score and attack vector, whether the vulnerability is pre-authentication or requires credentials, whether a public exploit exists in Metasploit or Exploit-DB, and your remediation recommendation. Format your three entries as a table suitable for inclusion in a professional penetration test report. This exercise directly practices the skill of translating raw scan output into actionable client findings.

### Reflection Questions

1. During the lab you ran Nikto against the Metasploitable 2 web server and likely received dozens of findings. Explain the difference between a scanner-reported finding and a confirmed vulnerability, and describe the manual verification step you would perform for two specific Nikto findings before including them in a client report. Why does including unverified scanner output in a report harm the client relationship?

2. A client asks you to run the scanning phase against their production e-commerce server during peak business hours on a Friday afternoon, arguing it will "only take a few minutes." Using the concepts from Module 06, explain what risks this creates, which pre-engagement document should have addressed testing windows, and how you would professionally respond to this request.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
