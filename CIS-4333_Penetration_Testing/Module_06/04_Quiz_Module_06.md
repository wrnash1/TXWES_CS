# Quiz: Module 06 — Scanning and Enumeration

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

**Instructions:** Select the single best answer for each question. Questions are aligned to CompTIA PenTest+ PT0-002 Domain 2: Information Gathering and Vulnerability Scanning.

---

### Question 1

A penetration tester needs to perform a port scan that generates the fewest log entries on the target system. The tester has root-level access on their Kali machine. Which Nmap scan type is most appropriate?

- A) `-sT` (TCP Connect scan)
- B) `-sU` (UDP scan)
- C) `-sS` (SYN/stealth scan)
- D) `-sA` (ACK scan)

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The SYN scan (`-sS`) sends a SYN packet and, if the port is open, receives a SYN-ACK but never completes the TCP handshake — it sends RST instead. Because no connection is fully established, most application-layer loggers do not record the connection attempt. Requires root.
- **Why A is incorrect:** The TCP Connect scan (`-sT`) completes the full three-way handshake. Application-layer logging (web servers, SSH, etc.) records completed connections, making this scan more detectable.
- **Why B is incorrect:** UDP scanning is appropriate for UDP services but produces different traffic patterns and is unrelated to minimizing TCP connection logs. UDP scans are notoriously slow.
- **Why D is incorrect:** The ACK scan is used for firewall rule mapping — it determines whether ports are filtered or unfiltered, not whether ports are open. It does not replace SYN scanning for stealthy port discovery.

---

### Question 2

An Nmap scan returns a port state of `filtered` for port 443. What is the most likely explanation for this result?

- A) A service is actively accepting HTTPS connections on port 443
- B) No service is running on port 443 and the port is accessible
- C) A firewall or packet filter is blocking Nmap's probes to port 443, preventing a definitive open or closed determination
- D) The target host is offline and not responding to any probes

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The `filtered` state means Nmap sent probes to the port and received no response (or received ICMP unreachable errors), indicating that a packet filter — typically a firewall — is blocking access. Nmap cannot determine whether a service is actually running behind the filter.
- **Why A is incorrect:** An actively accepting service would return `open` — Nmap would receive a SYN-ACK in response to its SYN probe.
- **Why B is incorrect:** A port with no running service but no filter would return `closed` — the target sends a TCP RST in response to the SYN probe.
- **Why D is incorrect:** If the host is completely offline, Nmap marks the host as down during host discovery. An individual port returning `filtered` while other ports return `open` or `closed` confirms the host is online but a filter is in place.

---

### Question 3

A tester runs `sudo nmap -sU -p 161 192.168.1.50` and the result shows port 161 as `open|filtered`. The tester wants to confirm whether SNMP is running and enumerate the device. What is the most appropriate next step?

- A) Run `nmap -sS -p 161 192.168.1.50` to switch to TCP scanning for SNMP
- B) Run `snmpwalk -v2c -c public 192.168.1.50` to attempt enumeration using the default read community string
- C) Run `nikto -h 192.168.1.50` to check whether SNMP is accessible via HTTP
- D) Run `enum4linux -a 192.168.1.50` to enumerate SNMP users over SMB

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** SNMP runs on UDP 161. The `open|filtered` state is normal for UDP — Nmap cannot always distinguish between open and filtered UDP ports. The correct next step is to directly attempt SNMP communication using snmpwalk with the default "public" community string. A successful response confirms the port is open and the community string is valid.
- **Why A is incorrect:** SNMP is a UDP protocol. Switching to TCP SYN scanning on port 161 would not find SNMP services.
- **Why C is incorrect:** Nikto is an HTTP web server scanner. SNMP operates at UDP/161 and has no HTTP interface. Nikto is irrelevant here.
- **Why D is incorrect:** enum4linux enumerates Windows and Samba systems over SMB protocols (ports 139/445). It has no capability to enumerate SNMP services.

---

### Question 4

During an Nmap service scan, a tester discovers that port 21 is open and running vsftpd 2.3.4. The tester runs `nmap --script=ftp-anon 192.168.1.10 -p 21` and the script reports "Anonymous FTP login allowed." What two security implications does this finding represent?

- A) FTP anonymous login is a required feature of all FTP servers and represents no security concern
- B) The server allows unauthenticated file access, and vsftpd 2.3.4 contains a known backdoor that opens a shell on port 6200 when triggered
- C) Anonymous FTP is only a problem if the server is internet-facing; on internal networks it is acceptable practice
- D) The vsftpd version indicates the server is patched and up to date, reducing exploitation risk

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** vsftpd 2.3.4 contains a backdoor introduced by a compromised source package (CVE-2011-2523). Sending a smiley face in the username `:)` triggers a bind shell on TCP port 6200. Combined with anonymous FTP login allowing unauthenticated access, this represents both an information exposure and a critical remote code execution vulnerability.
- **Why A is incorrect:** Anonymous FTP login is not a required feature — it must be explicitly enabled. It allows any user to access the FTP server without credentials, which is a significant security concern on any network.
- **Why C is incorrect:** Defense in depth principles reject the "internal-only" justification. Internal threats, lateral movement by attackers, and misconfigured firewalls all mean that insecure internal services represent real risk.
- **Why D is incorrect:** vsftpd 2.3.4 is specifically a version known to contain a backdoor — this is not a current or patched version.

---

### Question 5

A penetration tester is enumerating a Windows network and runs `enum4linux -a 192.168.1.20`. The output includes a list of usernames, group memberships, and a password policy showing minimum password length of 0 and no lockout threshold. What is the most significant security implication of the password policy finding?

- A) A minimum password length of 0 and no lockout threshold means users cannot set passwords at all
- B) This policy allows blank passwords and permits unlimited brute force attempts without account lockout, dramatically lowering the barrier to credential-based attacks
- C) Password policies are advisory only and do not affect actual authentication security
- D) This finding is insignificant because enum4linux results require independent verification before they represent real security findings

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A minimum password length of 0 allows blank or single-character passwords. No lockout threshold means an attacker can attempt unlimited passwords without being blocked. Combined with the user list from enum4linux, this creates ideal conditions for online brute force attacks using tools like Hydra or Medusa.
- **Why A is incorrect:** Minimum password length of 0 does not prevent password setting — it simply allows passwords of any length including empty. Users can still set passwords; the policy just does not enforce a minimum security standard.
- **Why C is incorrect:** Password policies are enforced by the operating system and domain controllers. They directly govern what authentication credentials are permitted and are not merely advisory.
- **Why D is incorrect:** While verification is always good practice, the password policy finding from enum4linux reflects actual domain policy configuration. It does not require independent verification before being documented as a finding.

---

### Question 6

A tester runs `nmap -A 192.168.1.30` against a target. Which four operations does the `-A` flag combine?

- A) TCP SYN scan, UDP scan, firewall evasion, and fragmentation
- B) Service version detection (`-sV`), OS fingerprinting (`-O`), default NSE scripts (`-sC`), and traceroute (`--traceroute`)
- C) Full port scan, vulnerability scripts, exploit scripts, and output to all formats
- D) Authentication scan, brute force, service banner grab, and SNMP enumeration

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The `-A` flag in Nmap is the "aggressive" mode that combines four specific operations: `-sV` for service and version detection, `-O` for OS fingerprinting, `-sC` to run default NSE scripts, and `--traceroute` to map the path to the target. This is explicitly defined in Nmap documentation and tested on PT0-002.
- **Why A is incorrect:** While Nmap does support TCP SYN scanning and UDP scanning separately, the `-A` flag does not include UDP scanning or fragmentation options. Those require explicit flags like `-sU` or `-f`.
- **Why C is incorrect:** `-A` does not enable a full port scan (that requires `-p-`), does not run exploit scripts (those are in the `exploit` NSE category, not `default`), and does not control output format (separate `-o` flags handle that).
- **Why D is incorrect:** None of the operations listed — authentication scanning, brute force, banner grabbing as a category, or SNMP enumeration — are part of what the `-A` flag enables.

---

### Question 7

A tester wants to check a web server for dangerous default files, outdated software versions, and misconfigured HTTP methods. Which tool is specifically designed for this purpose?

- A) Nmap with the `-sV` flag
- B) Nikto
- C) enum4linux
- D) snmpwalk

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Nikto is a web server scanner that performs comprehensive checks specifically for dangerous default files (phpinfo.php, /admin/, test files), outdated software with known CVEs, enabled dangerous HTTP methods (PUT, DELETE, TRACE), directory listing, default credentials, and header security issues. It is the correct tool for this task.
- **Why A is incorrect:** Nmap `-sV` detects service versions by probing ports. While useful for identifying the web server version, it does not crawl the web application for dangerous files or test HTTP methods in the way Nikto does.
- **Why C is incorrect:** enum4linux enumerates Windows and Samba SMB resources (users, shares, groups, password policy). It has no web server scanning capability.
- **Why D is incorrect:** snmpwalk queries SNMP MIB trees for network management information. It has no relevance to web server configuration or content enumeration.

---

### Question 8

Which SNMP community string represents the default read-write access string on many poorly configured network devices, and what risk does it create?

- A) "admin" — allows remote configuration changes to the device
- B) "private" — allows an attacker to modify device configuration, routing tables, and interface settings if the device accepts SNMP writes
- C) "public" — provides read access to all MIB data including usernames, processes, and network configuration
- D) "community" — is the default master key for all SNMP operations on Cisco devices

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** "private" is the default read-write community string for SNMPv1/v2c. Write access via SNMP allows an attacker to modify device configuration — changing routing tables, interface configurations, and potentially taking the device offline or redirecting traffic. This is a critical finding.
- **Why A is incorrect:** "admin" is a common default username/password for web interfaces and CLI access, not an SNMP community string convention.
- **Why C is incorrect:** "public" is the default read-only community string — it allows an attacker to enumerate device information (processes, interfaces, installed software) but not to make changes. It is a significant finding, but "private" represents greater risk due to write access.
- **Why D is incorrect:** "community" is not a standard default SNMP community string. SNMP does not have a "master key" concept — access is controlled by community strings that function like passwords.

---

### Question 9

A tester runs `nmap -p- --min-rate 1000 -T4 192.168.1.40` and discovers 22 open ports. The tester then runs `nmap -sV -O -sC -p 22,80,139,445,3306 192.168.1.40`. What is the correct term for this two-phase approach, and why is it preferred over running a single `-A -p-` scan?

- A) It is called credential stuffing; the two-phase approach is preferred because it avoids triggering SNMP alerts
- B) It is called a phased scan workflow; running full port discovery first then targeted version/script scanning on only the open ports is faster and reduces unnecessary traffic against closed ports
- C) It is called a stealth scan; the two-phase approach is required because Nmap cannot run `-sV` and `-p-` simultaneously
- D) It is called network segmentation testing; the approach is required by the Rules of Engagement for all external assessments

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The phased approach — full port discovery first, then detailed enumeration on discovered open ports only — is a professional best practice. Running version detection and OS fingerprinting against all 65,535 ports would be extremely slow and generate unnecessary traffic. Targeting only confirmed open ports makes the detailed scan significantly faster and more efficient.
- **Why A is incorrect:** Credential stuffing is an authentication attack technique using known username/password pairs from data breaches. It has no relationship to Nmap scan phasing.
- **Why C is incorrect:** Nmap can run `-sV` and `-p-` simultaneously (e.g., `nmap -sV -p-`). The reason to separate the phases is efficiency, not a technical limitation.
- **Why D is incorrect:** Network segmentation testing is a specific type of assessment verifying that network segments are properly isolated. It is not the name for a two-phase Nmap workflow, and no universal RoE requirement mandates this specific approach.

---

### Question 10

A penetration tester uses Netcat to banner grab a service on port 25 of an authorized target and receives this response:

```text
220 mail.targetcorp.com ESMTP Postfix (Ubuntu)
```

What information has been revealed and how should the tester use it?

- A) The banner reveals only that port 25 is open; version information requires a credentialed scan
- B) The banner reveals the mail server software (Postfix), operating system (Ubuntu), and hostname; the tester should search for Postfix CVEs, confirm the Ubuntu version via other scans, and note that the hostname reveals internal naming
- C) The banner is a honeypot indicator because legitimate mail servers do not display their software version
- D) The hostname in the banner proves the server is internet-facing and outside the authorized scope

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The SMTP banner reveals the MTA (Postfix), OS hint (Ubuntu), and internal hostname (mail.targetcorp.com). A professional tester cross-references the Postfix version against CVE databases, uses the OS hint to refine exploitation approach, and notes that the hostname reveals internal DNS naming conventions — useful for further enumeration.
- **Why A is incorrect:** Banner grabbing is specifically effective for unauthenticated version identification. The banner explicitly states Postfix and Ubuntu without any credentials required.
- **Why C is incorrect:** Legitimate mail servers routinely include software identification in SMTP banners. Banners can be customized to reduce disclosure, but standard banners are not honeypot indicators.
- **Why D is incorrect:** The hostname in the banner does not determine whether a server is in scope. Scope is defined by the written authorization document, not by the server's hostname or connectivity to the internet.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
