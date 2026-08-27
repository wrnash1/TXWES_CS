# Reading Guide: Module 04 - Active Reconnaissance – Nmap and Enumeration
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 04 - Active Reconnaissance – Nmap and Enumeration**! This module transitions from passive intelligence gathering to direct interaction with target systems. Active reconnaissance involves sending packets to target hosts and analyzing the responses to map open ports, identify running services, detect operating systems, and discover potential vulnerabilities. Nmap (Network Mapper) is the industry-standard tool for this phase and is explicitly tested on the CompTIA PenTest+ PT0-002 exam within the **Information Gathering and Vulnerability Scanning** domain (**22% of exam weight**).

Active reconnaissance leaves traces in firewall logs, IDS/IPS alerts, and server logs — so understanding the trade-off between scan thoroughness and detection risk is a key exam topic.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SYN Scan (`-sS`) vs. Connect Scan (`-sT`)**: A SYN scan (also called a "stealth" or "half-open" scan) sends a TCP SYN packet and, upon receiving a SYN-ACK, responds with RST rather than completing the handshake — leaving no established connection and minimal log entries on the target. A Connect scan (`-sT`) completes the full TCP three-way handshake using the OS's connect() system call, which is more detectable but does not require root/admin privileges. PT0-002 expects you to know that `-sS` requires elevated privileges and is stealthier; `-sT` does not require elevated privileges but leaves full connection logs.

*   **Service Version Detection (`-sV`)**: An Nmap flag that probes open ports with protocol-specific banners and responses to identify the exact software and version running on each port (e.g., Apache 2.4.51, OpenSSH 8.2). Version information is critical for matching services to known CVEs during vulnerability analysis. The `--version-intensity` flag (0–9) controls the depth of probing.

*   **OS Detection (`-O`)**: An Nmap technique that analyzes subtle differences in TCP/IP stack behavior — such as TTL values, window sizes, and TCP option ordering — to fingerprint the target's operating system. Accurate OS detection helps prioritize exploitation paths. Requires at least one open and one closed port to function, and requires root/admin privileges.

*   **Nmap Scripting Engine (`-sC` / `--script`)**: The NSE (Nmap Scripting Engine) extends Nmap with Lua-based scripts that perform automated service enumeration, vulnerability detection, and exploitation checks. `-sC` runs the default script set. Common script categories tested on PT0-002 include: `vuln` (vulnerability checks), `auth` (authentication bypass tests), `brute` (credential brute-forcing), `discovery` (service enumeration), and `exploit` (active exploitation). Example: `nmap --script smb-vuln-ms17-010` tests for EternalBlue.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Information Gathering and Vulnerability Scanning is **22% of PT0-002**. Expect multiple Nmap questions testing flag meanings and scan type trade-offs.
*   **Key Nmap Flags to Know:** `-sS` (SYN/stealth), `-sT` (connect), `-sU` (UDP), `-sV` (version), `-O` (OS detect), `-A` (aggressive: OS+version+scripts+traceroute), `-p` (port range), `-Pn` (skip host discovery), `-sn` (ping sweep only), `-oN`/`-oX` (output formats), `-T0` through `-T5` (timing templates).
*   **Exam Trap — UDP Scanning:** UDP scans (`-sU`) are slow and often unreliable. PT0-002 may test that UDP scans work differently from TCP — ports appear "open|filtered" unless a response is received. Common UDP services: DNS (53), SNMP (161/162), DHCP (67/68), NTP (123).
*   **Exam Trap — `-A` Flag:** The `-A` flag enables OS detection, version detection, script scanning, and traceroute simultaneously. It is aggressive and noisy — PT0-002 may ask which flag produces the most comprehensive but detectable scan.
*   **Timing Templates:** `-T0` (paranoid, very slow) through `-T5` (insane, fast/noisy). For stealth, use `-T1` or `-T2`. Default is `-T3`. PT0-002 tests whether students know that faster templates increase detection risk.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Nmap" room series on TryHackMe provides hands-on practice with every major Nmap flag against live vulnerable machines in a legal lab environment. No local VM required.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Active Reconnaissance and Nmap section for PT0-002 domain 2 content covering all tested scan types and flags.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Nmap rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). These guided rooms cover every major scan type, NSE scripts, and output formats with hands-on exercises against vulnerable targets in a safe lab environment.
*   **Required Video:** Watch the Active Reconnaissance and Nmap segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). Use chapter markers to navigate to domain 2 content on active scanning techniques.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Perform a SYN scan: `nmap -sS target_ip`**: You will execute a stealth SYN scan against a lab target, interpret the open/closed/filtered port states in the output, and explain why this scan type is preferred for stealth over a Connect scan.
*   **Identify open services and versions: `nmap -sV target_ip`**: You will use service version detection against the same target, identify the software and version strings returned, and explain how this information would be used to search for matching CVEs.
*   **Use the vulnerability scan script: `nmap --script vuln target_ip`**: You will run the NSE vulnerability script set against the target, interpret the results, and document any detected vulnerabilities by CVE number and severity.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Nmap rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Active Reconnaissance section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.

---

## 9. Supplemental Resources

**1. Nmap Official Documentation and Reference Guide**
[https://nmap.org/book/man.html](https://nmap.org/book/man.html)
The official Nmap reference manual documents every flag, scan type, timing template, and NSE script category. It is the authoritative source for understanding exactly what each option does — essential for PT0-002 exam preparation on the Information Gathering and Vulnerability Scanning domain.

**2. TryHackMe — Nmap Room Series**
[https://tryhackme.com/room/furthernmap](https://tryhackme.com/room/furthernmap)
TryHackMe's Nmap rooms provide guided, hands-on practice with every major scan type against live vulnerable machines in a legal lab environment. Completing the Nmap series directly reinforces Module 04 content and builds practical command-line fluency.

**3. Hack The Box Academy — Network Enumeration with Nmap**
[https://academy.hackthebox.com/course/preview/network-enumeration-with-nmap](https://academy.hackthebox.com/course/preview/network-enumeration-with-nmap)
HTB Academy's Nmap module covers scan types, NSE scripting, output formats, and firewall evasion techniques at a depth aligned to eJPT and OSCP preparation. The free tier includes enough content to reinforce all PT0-002 Nmap objectives covered in Module 04.
