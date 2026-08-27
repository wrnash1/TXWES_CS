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

---

### Question 11

A tester runs `nmap -sU -p 161 192.168.1.50` and the port is reported as `open|filtered`. What does this state indicate?

- A) The port is confirmed open and a UDP service is listening, but no banner was returned
- B) Nmap received no response; UDP `open|filtered` means the port may be open or a firewall is silently dropping packets — Nmap cannot distinguish between the two without a UDP application-layer probe
- C) The port is confirmed filtered by a firewall and the SNMP service is not present on this host
- D) The `open|filtered` state is only possible with TCP scans; UDP scans always return `open` or `closed`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** UDP is connectionless — when Nmap sends a UDP probe and receives no response, it cannot determine whether the service is open and silently dropping the probe or whether a firewall is silently dropping it. This ambiguity produces the `open|filtered` state. A UDP-specific application probe (such as an SNMP GET request for port 161) can resolve the ambiguity.
- **Why A is incorrect:** `open|filtered` does not mean the port is confirmed open. If the port were confirmed open (with a response), Nmap would report it as simply `open`.
- **Why C is incorrect:** `open|filtered` does not mean confirmed filtered. If Nmap received an ICMP port-unreachable response, it would report the port as `closed`. Silent drops are what produce the ambiguous state.
- **Why D is incorrect:** `open|filtered` is specifically a UDP scan result. TCP scans resolve to `open`, `closed`, or `filtered` based on SYN-ACK, RST, or no-response respectively — they do not produce `open|filtered`.

---

### Question 12

Which Nmap output format is most appropriate when another tool or script needs to parse the scan results programmatically?

- A) `-oN` (normal output) because it is human-readable and therefore the easiest to parse
- B) `-oG` (grepable output) because grep is the fastest text-processing tool available
- C) `-oX` (XML output) because structured XML can be parsed by standard XML libraries and tools like `xsltproc` for HTML reports
- D) `-oA` (all formats) because outputting all formats simultaneously is required by most compliance frameworks

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** XML is a structured, machine-readable format with well-defined schema. Tools like `xsltproc`, Python's `xml.etree`, and purpose-built parsers (e.g., python-nmap) consume `-oX` output natively. It is the standard format for importing Nmap results into vulnerability management platforms.
- **Why A is incorrect:** Normal output (`-oN`) is designed for human readability, not programmatic parsing. It lacks consistent delimiters and structure, making it error-prone to parse with scripts.
- **Why B is incorrect:** Grepable output (`-oG`) is useful for quick command-line extraction with grep/awk, but it is a flat format not designed for hierarchical or structured parsing by applications.
- **Why D is incorrect:** `-oA` outputs all three formats simultaneously (normal, XML, grepable) as a convenience flag. No compliance framework mandates outputting all three formats. XML alone is sufficient for programmatic use.

---

### Question 13

A tester wants to find all hosts on the 10.10.10.0/24 subnet that have port 445 open without performing a full port scan on every host. Which command achieves this most efficiently?

- A) `nmap -p 1-1024 10.10.10.0/24` — scan the top 1024 ports on all hosts
- B) `nmap -p 445 10.10.10.0/24` — scan only port 445 across all hosts in the subnet
- C) `nmap -sV 10.10.10.0/24` — version detection will identify SMB automatically
- D) `nmap --script smb-vuln-ms17-010 10.10.10.0/24` — run the vulnerability script which performs host discovery automatically

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Specifying `-p 445` restricts Nmap to testing only that port on each host, making the sweep fast and targeted. The subnet notation causes Nmap to probe all 256 addresses. This is the standard approach for identifying all SMB-capable hosts before deeper enumeration.
- **Why A is incorrect:** Scanning ports 1–1024 on every host generates far more traffic than necessary and takes significantly longer. Only port 445 is needed for this objective.
- **Why C is incorrect:** Version detection (`-sV`) runs against discovered open ports but still scans the default top-1000 ports on each host unless restricted with `-p`. This is less efficient than specifying only the target port.
- **Why D is incorrect:** Running an NSE vulnerability script without first confirming which hosts have port 445 open is wasteful and potentially generates IDS alerts. Vulnerability scripts should follow host and port discovery, not replace them.

---

### Question 14

During SNMP enumeration with `snmpwalk -v2c -c public 192.168.1.100`, the tester receives extensive output including interface descriptions, running processes, and installed software. What does the community string `public` reveal about this device's configuration?

- A) `public` is a custom community string configured by the administrator for authorized testing
- B) `public` is the default read-only SNMP community string; its presence indicates the device was deployed without changing default credentials, which is a misconfiguration
- C) `public` is the SNMPv3 authentication username and its presence confirms that SNMPv3 is in use
- D) `public` is only used by SNMPv1 and has no security implication on modern devices running SNMPv2c

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `public` is the industry-default read-only SNMP community string shipped with virtually all SNMP-capable devices. A device responding to `public` has not had its community string changed from the factory default — a well-documented misconfiguration that exposes system information to any unauthenticated requester on the network.
- **Why A is incorrect:** `public` is the universally known default, not a custom administrator-configured string. Its presence is a finding precisely because it was not customized.
- **Why C is incorrect:** SNMPv3 uses usernames, authentication protocols (MD5/SHA), and privacy protocols (DES/AES), not community strings. The `-v2c` flag in the command explicitly specifies SNMPv2c, which uses community strings.
- **Why D is incorrect:** SNMPv2c uses community strings just as SNMPv1 does. The security implication is identical: anyone knowing the community string (which for `public` is everyone) can read device information. The version alone does not mitigate the default-credential risk.

---

### Question 15

A tester runs `enum4linux -a 192.168.1.50` against a Windows host and receives share names, user account lists, and group memberships without providing any credentials. What vulnerability class does this represent?

- A) Credential stuffing — the tool is using a known password list to authenticate
- B) A null session — Windows SMB/NetBIOS is allowing unauthenticated connections that reveal sensitive enumeration data
- C) A man-in-the-middle attack — enum4linux intercepts domain authentication traffic
- D) An SQL injection — enum4linux queries the Windows registry database using injection techniques

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A null session is an unauthenticated SMB/NetBIOS connection (empty username and password) that older or misconfigured Windows systems allow. Through null sessions, an attacker can enumerate shares, user accounts, groups, password policies, and trust relationships — exactly what enum4linux retrieves. This is a well-known Windows misconfiguration.
- **Why A is incorrect:** Credential stuffing requires having credential pairs to attempt. enum4linux's default behavior does not provide credentials — it connects anonymously (null session).
- **Why C is incorrect:** enum4linux queries the target directly using SMB/RPC protocols. It does not intercept traffic between other hosts, which is the definition of a man-in-the-middle attack.
- **Why D is incorrect:** SQL injection targets database query parsing. enum4linux communicates via SMB/RPC protocols to Windows services, not via SQL queries to a database engine.

---

### Question 16

A tester discovers that an FTP server on port 21 allows anonymous login. After connecting with `ftp 192.168.1.50` and entering `anonymous` as the username with a blank password, they gain access to a directory of internal configuration files. What is the correct immediate action?

- A) Download all accessible files immediately to preserve evidence before the session times out
- B) Document the finding with a screenshot and connection log, note the accessible directory listing, then disconnect — bulk download requires specific RoE authorization for data exfiltration
- C) Attempt to escalate privileges by uploading a webshell to the FTP root directory
- D) Close the connection and do not document the finding, as accessing anonymous services is not a security vulnerability

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Confirming the vulnerability exists (anonymous login with access to sensitive files) is sufficient to document a critical finding. Bulk downloading files — especially configuration files that may contain credentials or PII — constitutes data exfiltration and typically requires explicit RoE authorization. The professional approach is to document access and directory listings without extracting data beyond what is needed to demonstrate impact.
- **Why A is incorrect:** Bulk downloading client data without explicit authorization exceeds the typical scope of a penetration test and may violate the RoE, data handling agreements, and privacy laws regardless of whether the access was "authorized" by the vulnerability.
- **Why C is incorrect:** Uploading files to a target system is a destructive action that changes the target's state and requires specific written authorization. It also escalates far beyond enumeration into exploitation without confirming the finding first.
- **Why D is incorrect:** Anonymous FTP access to sensitive files is a significant vulnerability — insufficient access controls allowing unauthenticated access to internal data. Failing to document confirmed findings is a professional failure.

---

### Question 17

Masscan is capable of scanning the entire IPv4 internet in under six minutes at maximum rate. Why would a professional penetration tester choose Nmap over Masscan for a targeted internal network engagement?

- A) Masscan only works on IPv6 networks; Nmap supports both IPv4 and IPv6
- B) Nmap provides service version detection, OS fingerprinting, and NSE scripting that Masscan lacks; Masscan is optimized for speed across massive address spaces, not for the detailed per-host enumeration needed in a targeted engagement
- C) Masscan requires root privileges on Linux, while Nmap can run as a standard user for all scan types
- D) Masscan is illegal to use in the United States, while Nmap is explicitly authorized by all compliance frameworks

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Masscan's design priority is raw throughput — it sacrifices detailed enumeration for speed. It does not perform service version detection, OS fingerprinting, or scripted checks. For a targeted internal engagement where the tester needs to understand what software is running and identify specific vulnerabilities, Nmap's depth of analysis is essential. Masscan is valuable for initial discovery on very large networks, followed by Nmap for detailed enumeration.
- **Why A is incorrect:** Masscan supports both IPv4 and IPv6. IPv6 capability is not the distinguishing factor.
- **Why C is incorrect:** Both Masscan and Nmap require elevated privileges for SYN scans. Nmap's Connect scan (`-sT`) does not require root, but this is not the reason to choose Nmap over Masscan.
- **Why D is incorrect:** Masscan is not illegal; unauthorized use of any scanning tool is illegal regardless of the tool. No compliance framework explicitly authorizes only Nmap.

---

### Question 18

After completing a scanning phase, a tester has Nmap XML output, enum4linux text files, and Nikto logs from multiple targets. Which documentation practice is required before moving to the exploitation phase?

- A) Delete all scan logs to protect the client from data exposure if the tester's machine is compromised
- B) Archive all output files with timestamps, cross-reference findings to confirm scope compliance, and create a structured finding list mapping each discovered service to its potential vulnerabilities before proceeding
- C) Begin exploitation immediately to take advantage of any time-sensitive vulnerabilities before they are patched
- D) Submit all raw scan outputs directly to the client as the final deliverable without further analysis

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Professional practice requires organizing and reviewing scan data before exploitation: confirming all targets are within scope, timestamping findings for chain-of-custody, and creating a prioritized finding list. This prevents accidental out-of-scope exploitation and ensures the exploitation phase is systematic rather than opportunistic.
- **Why A is incorrect:** Deleting scan logs destroys evidence and violates documentation requirements. Scan output is part of the engagement record and must be retained per the RoE's data retention provisions.
- **Why C is incorrect:** Rushing to exploitation without reviewing and organizing findings increases the risk of out-of-scope actions, missed vulnerabilities, and poor prioritization. Professional engagements follow a structured methodology.
- **Why D is incorrect:** Raw scan outputs are not professional deliverables. Clients receive analyzed, interpreted findings that explain business impact and remediation guidance — not unprocessed tool output.

---

### Question 19

A Nikto scan against a web server returns the finding: `+ OSVDB-3092: /admin/: This might be interesting...`. What should the tester do next?

- A) Immediately attempt to brute-force login credentials against the `/admin/` path
- B) Note the finding, manually browse to `/admin/` in a browser to observe the response, and document whether it presents a login form, redirects, or returns a 403 — then assess whether further testing of this path is within the RoE before proceeding
- C) Dismiss the finding as a false positive since Nikto always flags `/admin/` regardless of whether content exists
- D) Report the finding directly to the client without verifying it, since Nikto findings are always accurate

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Nikto findings require manual verification. Browsing to the path confirms whether an admin interface exists, what it exposes, and whether it is accessible — all without performing any destructive or intrusive action. Verifying before escalating is standard professional practice, and confirming scope authorization for admin interface testing is required before any login attempts.
- **Why A is incorrect:** Brute-forcing credentials is an intrusive, potentially destructive action that requires explicit RoE authorization and should only follow confirmed discovery of a login interface, not immediate action on a Nikto suggestion.
- **Why C is incorrect:** While Nikto does produce false positives, it cannot be dismissed without verification. Many `/admin/` paths contain real, exposed administrative interfaces with significant security impact.
- **Why D is incorrect:** Reporting unverified scanner output as confirmed findings is unprofessional and inflates a client's vulnerability list with noise. All findings should be manually validated before being included in the report.

---

### Question 20

A tester performs a full port scan (`nmap -p-`) and discovers that port 8443 is open on a target. They identify it as running HTTPS. What follow-on enumeration steps are appropriate before noting this as a potential finding?

- A) Immediately exploit the service using Metasploit since HTTPS on a non-standard port is always misconfigured
- B) Run `nmap -sV -p 8443` for version detection, browse the service to identify the application, run Nikto against port 8443, and check the TLS certificate for hostname and expiration details — then document all findings
- C) Skip the port because HTTPS services are encrypted and cannot be enumerated without decrypting traffic
- D) Only document the port number; application-layer enumeration of HTTPS requires credentials and cannot be performed passively

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Non-standard HTTPS ports often host management interfaces, development applications, or alternative web servers with weaker configurations. Version detection identifies the software; manual browsing reveals the application type and any exposed content; Nikto tests for common web vulnerabilities; TLS certificate inspection reveals hostnames, validity, and potential misconfigurations. This comprehensive approach produces actionable findings.
- **Why A is incorrect:** A non-standard HTTPS port is interesting but not automatically exploitable. Skipping enumeration to jump directly to exploitation contradicts the methodology and may target the wrong application or misidentify the software.
- **Why C is incorrect:** HTTPS encrypts traffic in transit but does not prevent enumeration of the service itself. Banner grabbing, certificate inspection, and web application scanning all work against HTTPS services without requiring traffic decryption.
- **Why D is incorrect:** Application-layer enumeration of HTTPS does not require credentials. Public-facing web application headers, TLS certificates, and page content are accessible without authentication.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
