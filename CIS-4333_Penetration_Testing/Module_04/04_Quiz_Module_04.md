# Quiz: Module 04 - Active Reconnaissance – Nmap and Enumeration
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which Nmap scan type is known as "stealth" or "half-open" scanning because it does not complete the TCP three-way handshake?
*   A) TCP Connect Scan (-sT)
*   B) TCP SYN Scan (-sS)
*   C) UDP Scan (-sU)
*   D) Ping Sweep (-sn)
*   **Correct Answer:** B) SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK to keep connections half-open.
*   **Distractor Analysis:**
    *   *Why correct:* SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK — never completing the handshake, which leaves minimal log entries on the target.
    *   *Why A is incorrect:* Connect scans (-sT) complete the full three-way handshake using the OS socket API, creating established connection records in target logs — the opposite of stealth.
    *   *Why C is incorrect:* UDP scans probe UDP ports (not TCP), using a fundamentally different protocol. They are not classified as "stealth" or "half-open" scans.
    *   *Why D is incorrect:* A ping sweep (-sn) discovers live hosts via ICMP — it does not scan ports at all and is not related to half-open TCP scanning.

---

**Question 2**
In Nmap, which flag enables **OS detection** by analyzing TCP/IP stack fingerprinting characteristics such as TTL values and TCP window sizes?
*   A) `-sV` — probes open ports to identify the software name and version number of running services.
*   B) `-O` — sends specially crafted probe packets and analyzes response characteristics to fingerprint the target operating system.
*   C) `-sC` — runs the default NSE script set against discovered open ports to enumerate services and check for common vulnerabilities.
*   D) `-A` — enables aggressive mode combining OS detection, version detection, script scanning, and traceroute in one scan.
*   **Correct Answer:** B) `-O` — sends specially crafted probe packets and analyzes response characteristics to fingerprint the target operating system.
*   **Distractor Analysis:**
    *   *Why B is correct:* The `-O` flag specifically enables OS detection. Nmap sends TCP/IP probes and compares the responses against its OS fingerprint database to identify the target OS and version. It requires at least one open and one closed port, and needs root/admin privileges.
    *   *Why A is incorrect:* `-sV` is service version detection — it identifies what software is running on open ports, not the underlying operating system.
    *   *Why C is incorrect:* `-sC` runs the default NSE scripts (equivalent to `--script=default`). It performs service enumeration and vulnerability checks, not OS fingerprinting.
    *   *Why D is incorrect:* `-A` is an umbrella flag that includes `-O` among other options, but `-A` alone is not the specific OS detection flag — and it also includes much more, making it the "aggressive" option.

---

**Question 3**
A penetration tester needs to scan a target for open ports and determine the software versions running on those ports in a single Nmap command. Which command is most appropriate?
*   A) `nmap -sn target_ip`
*   B) `nmap -O target_ip`
*   C) `nmap -sV target_ip`
*   D) `nmap --script vuln target_ip`
*   **Correct Answer:** C) `nmap -sV target_ip`
*   **Distractor Analysis:**
    *   *Why C is correct:* The `-sV` flag enables service version detection. Nmap probes each discovered open port with protocol-specific banners to identify the software name and version (e.g., "Apache httpd 2.4.51"). This is the standard flag for combining port scanning with version identification.
    *   *Why A is incorrect:* `-sn` performs a ping sweep (host discovery only) — it does not scan ports or detect service versions.
    *   *Why B is incorrect:* `-O` performs OS detection only. It does not report individual service versions running on open ports.
    *   *Why D is incorrect:* `--script vuln` runs NSE vulnerability scripts against discovered ports. It requires ports to be discovered first and does not itself combine port scanning with version identification in a clean single-purpose way.

---

**Question 4**
During an authorized penetration test, a tester needs maximum stealth while scanning a target. Which Nmap timing template should they use?
*   A) `-T5` (Insane) — fastest scan, best for stealth because it completes before IDS signatures trigger.
*   B) `-T3` (Normal) — the default timing; appropriate for all engagements.
*   C) `-T1` (Sneaky) — very slow scan rate that reduces detection probability by spacing probes far apart.
*   D) `-T0` (Paranoid) — sends one probe every 5 minutes, designed to evade nearly all IDS rate-based detection.
*   **Correct Answer:** C) `-T1` (Sneaky) — very slow scan rate that reduces detection probability by spacing probes far apart.
*   **Distractor Analysis:**
    *   *Why C is correct:* PT0-002 tests that slower timing templates (-T0, -T1, -T2) are used for stealth because they send fewer packets per second, making it harder for rate-based IDS/IPS rules to trigger. `-T1` (Sneaky) is practical for authorized engagements requiring stealth without the extreme slowness of `-T0`.
    *   *Why A is incorrect:* `-T5` (Insane) is the fastest and loudest template — it generates high traffic volume that easily triggers IDS alerts. Speed does not equal stealth.
    *   *Why B is incorrect:* `-T3` is the default general-purpose timing. It makes no attempt at stealth and will trigger many common IDS signatures.
    *   *Why D is incorrect:* `-T0` (Paranoid) is technically stealthier than `-T1` but is impractical for most engagements because one probe every 5 minutes means a full port scan could take days. `-T1` is the practical stealth choice tested by PT0-002.

---

**Question 5**
A tester runs `nmap --script smb-vuln-ms17-010 target_ip` against a Windows host and receives a positive result. What does this finding indicate?
*   A) The target has SMB port 445 open but no vulnerability was confirmed — further manual testing is required.
*   B) The target is likely vulnerable to the EternalBlue exploit, which can allow unauthenticated remote code execution via SMBv1.
*   C) The target's SMB service is misconfigured and is broadcasting its NetBIOS name in cleartext.
*   D) The target has outdated SSL/TLS certificates on port 443 that need to be renewed immediately.
*   **Correct Answer:** B) The target is likely vulnerable to the EternalBlue exploit, which can allow unauthenticated remote code execution via SMBv1.
*   **Distractor Analysis:**
    *   *Why B is correct:* MS17-010 is the Microsoft SMB vulnerability exploited by EternalBlue (used in WannaCry and NotPetya). The NSE script `smb-vuln-ms17-010` actively checks whether the target responds to the specific SMBv1 probe that confirms vulnerability. A positive result indicates high confidence the target is unpatched and exploitable for unauthenticated RCE.
    *   *Why A is incorrect:* The `smb-vuln-ms17-010` script performs an active check beyond just confirming the port is open — a positive result is a meaningful vulnerability indicator, not an inconclusive finding.
    *   *Why C is incorrect:* NetBIOS name broadcasting is a separate issue tested by different scripts (e.g., `nbstat`). It is unrelated to MS17-010.
    *   *Why D is incorrect:* MS17-010 is an SMB vulnerability on port 445. It has no connection to SSL/TLS certificates or port 443 web services.

---

**Question 6**
When Nmap reports a port as "open," what does that state specifically indicate about the port and the host?

*   A) A firewall is blocking the probe packets so Nmap cannot determine whether a service is listening.
*   B) The port is reachable but no service is actively listening — the host replied with a TCP RST.
*   C) An application is actively accepting connections on that port — the host responded with a TCP SYN-ACK (or equivalent UDP response).
*   D) The port is in a transitional state between open and closed while the service restarts.

*   **Correct Answer:** C) An application is actively accepting connections on that port — the host responded with a TCP SYN-ACK (or equivalent UDP response).
*   **Distractor Analysis:**
    *   *Why C is correct:* The "open" state means Nmap received a TCP SYN-ACK in response to its SYN probe (for TCP scans), confirming that a process is listening on that port and accepting connections. This is the most important state in pen testing because open ports expose services that may contain vulnerabilities.
    *   *Why A is incorrect:* A firewall blocking probes results in the "filtered" state — Nmap receives no response or an ICMP unreachable message. "Filtered" does not mean open.
    *   *Why B is incorrect:* A TCP RST response indicates the "closed" state — the port is reachable but no service is listening. Closed ports actively reject connections rather than accepting them.
    *   *Why D is incorrect:* Nmap port states are point-in-time snapshots, not dynamic transitions. There is no "transitional" state; ports are reported as open, closed, filtered, open|filtered, closed|filtered, or unfiltered at the time of the scan.

---

**Question 7**
A penetration tester uses Nmap's NSE (Nmap Scripting Engine) and wants to run only scripts that are unlikely to crash services or have harmful effects on the target. Which NSE script category is most appropriate?

*   A) `intrusive` — scripts that actively attempt to exploit vulnerabilities on the target
*   B) `brute` — scripts that perform credential brute-force attacks against discovered services
*   C) `safe` — scripts designed to be unlikely to crash services, use large amounts of bandwidth, or negatively impact the target
*   D) `exploit` — scripts that deliver working exploits against known CVEs

*   **Correct Answer:** C) `safe` — scripts designed to be unlikely to crash services, use large amounts of bandwidth, or negatively impact the target
*   **Distractor Analysis:**
    *   *Why C is correct:* The NSE `safe` category contains scripts that are low-risk and non-destructive. They gather information passively or with minimal interaction, making them suitable for use in sensitive environments or early reconnaisance phases where avoiding detection and minimizing impact is a priority.
    *   *Why A is incorrect:* The `intrusive` category contains scripts that actively probe targets in ways that may crash services, trigger IDS alerts, or cause harm. They are explicitly labeled as higher-risk and should only be used with explicit authorization and caution.
    *   *Why B is incorrect:* The `brute` category performs automated credential brute-force attacks against services such as SSH, FTP, and SMB. These generate significant log entries and may lock out accounts, making them far from low-impact.
    *   *Why D is incorrect:* The `exploit` category delivers working exploitation code. Running exploit scripts without explicit authorization for that level of testing would exceed the scope of a reconnaissance phase and potentially cause damage.

---

**Question 8**
A tester needs to complete an Nmap scan of a production network as quickly as possible and is not concerned about detection. Which timing template provides the fastest scan speed, and what is a key risk of using it?

*   A) `-T3` (Normal) — fastest template; risk is that it creates audit log entries on the target.
*   B) `-T4` (Aggressive) — fastest template; risk is that it may trigger rate-based IDS rules due to high packet volume.
*   C) `-T5` (Insane) — fastest template; risk is that it may cause packet loss on slow networks, leading to inaccurate results and missed open ports.
*   D) `-T2` (Polite) — fastest template; risk is that it takes longer than default scans.

*   **Correct Answer:** C) `-T5` (Insane) — fastest template; risk is that it may cause packet loss on slow networks, leading to inaccurate results and missed open ports.
*   **Distractor Analysis:**
    *   *Why C is correct:* `-T5` is the highest and fastest Nmap timing template. It sends probes as rapidly as the network and target can theoretically handle. The key operational risk is that on congested or slow networks, probes outpace responses, causing Nmap to miss replies and report open ports as filtered or closed — producing inaccurate results.
    *   *Why A is incorrect:* `-T3` is the default timing template, not the fastest. It is a balanced middle-ground template suitable for most general-purpose scans.
    *   *Why B is incorrect:* `-T4` is the second fastest template and is commonly used for fast authorized scans. It is not the fastest — `-T5` is faster and is the correct answer for maximum speed.
    *   *Why D is incorrect:* `-T2` (Polite) is a slow template that reduces scan speed to lower the impact on the network. It is the opposite of the fastest template.

---

**Question 9**
A penetration tester connects to an open port using `nc target_ip 22` (netcat) and receives the response: `SSH-2.0-OpenSSH_7.4`. What technique is this, and what actionable information does it provide?

*   A) Port scanning — it confirms the port is open, but provides no information about the running service.
*   B) Banner grabbing — it reveals the service type (SSH), the protocol version (SSHv2), and the specific software version (OpenSSH 7.4), which can be used for CVE research.
*   C) Vulnerability scanning — the response indicates that OpenSSH 7.4 has been automatically exploited.
*   D) OS fingerprinting — the SSH banner reveals the operating system version and kernel build number.

*   **Correct Answer:** B) Banner grabbing — it reveals the service type (SSH), the protocol version (SSHv2), and the specific software version (OpenSSH 7.4), which can be used for CVE research.
*   **Distractor Analysis:**
    *   *Why B is correct:* Banner grabbing is the technique of connecting to a network service and reading the text it displays upon connection. The banner `SSH-2.0-OpenSSH_7.4` identifies: the service (SSH), the protocol version (2.0), and the software + version (OpenSSH 7.4). A tester can then search the NVD or Exploit-DB for CVEs specific to OpenSSH 7.4 — for example, CVE-2017-15906 (a write access vulnerability in OpenSSH 7.4).
    *   *Why A is incorrect:* Banner grabbing provides significantly more information than just port state. The text response is the primary reconnaissance output of this technique.
    *   *Why C is incorrect:* Banner grabbing is a passive information-gathering technique — simply reading the banner does not exploit or attack the service. No exploitation has occurred.
    *   *Why D is incorrect:* While SSH banner data can sometimes hint at the OS platform (e.g., Debian-based systems often include a package suffix), it does not reveal kernel version or full OS details. OS fingerprinting requires TCP/IP stack analysis with the `-O` flag, not banner reading.

---

**Question 10**
A tester runs `nmap -sV --version-intensity 5 target_ip` against a web server and receives: `80/tcp open http Apache httpd 2.4.29`. What does the `-sV` flag enable, and why is the version number `2.4.29` particularly significant?

*   A) `-sV` enables OS fingerprinting; `2.4.29` identifies the target's kernel version.
*   B) `-sV` enables service version detection; `2.4.29` is the specific Apache version, which can be cross-referenced against CVE databases to identify unpatched vulnerabilities affecting that release.
*   C) `-sV` enables stealth scanning; `2.4.29` is the scan session ID assigned by Nmap.
*   D) `-sV` runs the default NSE scripts; `2.4.29` is the response latency in milliseconds.

*   **Correct Answer:** B) `-sV` enables service version detection; `2.4.29` is the specific Apache version, which can be cross-referenced against CVE databases to identify unpatched vulnerabilities affecting that release.
*   **Distractor Analysis:**
    *   *Why B is correct:* The `-sV` flag instructs Nmap to probe each open port with application-layer banners and fingerprint responses to identify the software name and exact version. Apache httpd 2.4.29 (released 2017) has multiple known CVEs — for example, CVE-2017-9798 (Optionsbleed) and CVE-2017-7679. Version detection is a critical step in the vulnerability research phase of a penetration test.
    *   *Why A is incorrect:* OS fingerprinting is performed by the `-O` flag, not `-sV`. The `2.4.29` value refers to the Apache web server version, not the operating system kernel.
    *   *Why C is incorrect:* Stealth scanning involves timing templates and scan type selection (e.g., `-sS`, `-T1`). The `-sV` flag has no relationship to stealth, and Nmap does not assign session IDs to scan results.
    *   *Why D is incorrect:* Running default NSE scripts is performed with `-sC` (equivalent to `--script=default`). The version number in Nmap output is the detected software version, not a timing or latency value.

---

**Question 11**
A penetration tester wants to scan only ports 22, 80, 443, and 8080 on a target host using Nmap. Which command syntax correctly limits the scan to those specific ports?

*   A) `nmap -sV --ports=22,80,443,8080 target_ip`
*   B) `nmap -sV -p 22,80,443,8080 target_ip`
*   C) `nmap -sV -range 22-8080 target_ip`
*   D) `nmap -sV --only 22,80,443,8080 target_ip`
*   **Correct Answer:** B) `nmap -sV -p 22,80,443,8080 target_ip`
*   **Distractor Analysis:**
    *   *Why B is correct:* The `-p` flag followed by a comma-separated list of port numbers is the standard Nmap syntax for specifying individual ports to scan. This is one of the most commonly tested Nmap flags on PT0-002.
    *   *Why A is incorrect:* `--ports` is not a valid Nmap flag. The correct flag for specifying port numbers is `-p`.
    *   *Why C is incorrect:* `-range` is not a valid Nmap flag. A continuous port range is specified as `-p 22-8080`, but that scans all ports between 22 and 8080, not just the four specific ports listed.
    *   *Why D is incorrect:* `--only` is not a valid Nmap flag. Port specification is done with `-p`.

---

**Question 12**
What does the Nmap port state "filtered" indicate when returned in scan results?

*   A) The port is confirmed closed — the target actively sent a TCP RST in response to the probe
*   B) The port is confirmed open — a service is accepting connections on that port
*   C) A firewall, packet filter, or network device is blocking the probes so Nmap cannot determine whether the port is open or closed
*   D) The port is running an application that requires authentication before reporting its state
*   **Correct Answer:** C) A firewall, packet filter, or network device is blocking the probes so Nmap cannot determine whether the port is open or closed
*   **Distractor Analysis:**
    *   *Why C is correct:* "Filtered" means Nmap received no response or received an ICMP unreachable message, indicating a firewall or packet filter is dropping or blocking the probe packets. Nmap cannot determine the actual state of the port behind the filter.
    *   *Why A is incorrect:* A port that actively returns a TCP RST is reported as "closed" — not filtered. Closed means the port is reachable but no service is listening.
    *   *Why B is incorrect:* An open port returns a SYN-ACK for TCP SYN probes. "Filtered" means the probe was blocked, not accepted.
    *   *Why D is incorrect:* Authentication requirements on an application do not cause a "filtered" port state. A service requiring authentication still accepts the TCP connection, resulting in an "open" state.

---

**Question 13**
A tester runs `nmap -sU -p 161 target_ip` and the result shows port 161/udp as "open|filtered." What does this state mean, and what service should the tester investigate further?

*   A) The TCP connection on port 161 was refused, indicating a closed service; no further investigation is needed
*   B) UDP port 161 may be open but Nmap cannot confirm it because no response was received; the service associated with port 161 is SNMP and should be investigated further with SNMP enumeration tools
*   C) The port is confirmed open and running HTTPS; the tester should run Burp Suite against it
*   D) "open|filtered" for UDP means the port has a misconfigured firewall rule that alternates between open and closed states
*   **Correct Answer:** B) UDP port 161 may be open but Nmap cannot confirm it because no response was received; the service associated with port 161 is SNMP and should be investigated further with SNMP enumeration tools
*   **Distractor Analysis:**
    *   *Why B is correct:* UDP scanning often returns "open|filtered" because UDP services do not respond to probes that don't match their protocol. No response means Nmap cannot distinguish between a firewall dropping the packet and a service that simply didn't respond. Port 161 is SNMP, and a potential open SNMP port should be enumerated with tools like snmpwalk to check for community string exposure.
    *   *Why A is incorrect:* Port 161 is not associated with TCP or HTTPS. The "open|filtered" state does not mean the connection was refused — it means the UDP probe received no response.
    *   *Why C is incorrect:* Port 161 is SNMP (UDP), not HTTPS. Burp Suite is a web application testing tool for HTTP/HTTPS traffic, not SNMP enumeration.
    *   *Why D is incorrect:* "open|filtered" is a standard Nmap UDP scan state indicating uncertainty — it does not describe an alternating or intermittent firewall rule behavior.

---

**Question 14**
Which Nmap flag instructs the tool to skip host discovery and treat all target hosts as online, which is useful when a firewall blocks ICMP?

*   A) `-sn`
*   B) `-Pn`
*   C) `-n`
*   D) `-T0`
*   **Correct Answer:** B) `-Pn`
*   **Distractor Analysis:**
    *   *Why B is correct:* `-Pn` (formerly `-P0`) tells Nmap to skip the host discovery phase and assume all targets are online. This is essential when scanning through firewalls that block ICMP ping probes, which would otherwise cause Nmap to mark live hosts as down.
    *   *Why A is incorrect:* `-sn` performs a ping sweep — host discovery only without port scanning. This is the opposite of skipping host discovery.
    *   *Why C is incorrect:* `-n` instructs Nmap to skip DNS resolution of discovered IP addresses. It has no effect on whether host discovery is performed.
    *   *Why D is incorrect:* `-T0` is the paranoid timing template that slows scan rate to evade detection. It does not affect whether the host discovery phase is skipped.

---

**Question 15**
A tester wants to save Nmap results in XML format for later import into a vulnerability management tool. Which output flag should they use?

*   A) `-oN filename` — saves output in normal human-readable text format
*   B) `-oG filename` — saves output in grepable format for command-line parsing tools
*   C) `-oX filename` — saves output in XML format suitable for import into tools like Metasploit and vulnerability management platforms
*   D) `-oA filename` — saves output simultaneously in normal, XML, and grepable formats
*   **Correct Answer:** C) `-oX filename`
*   **Distractor Analysis:**
    *   *Why C is correct:* `-oX` saves Nmap results in XML format. XML output is the format required by tools such as Metasploit's `db_import`, OpenVAS, and various vulnerability management platforms that parse Nmap data automatically.
    *   *Why A is incorrect:* `-oN` produces human-readable text output that mirrors what appears on screen. It is not structured for machine parsing or tool import.
    *   *Why B is incorrect:* `-oG` produces grepable output useful for command-line parsing but is not the XML format required by vulnerability management tools.
    *   *Why D is incorrect:* `-oA` saves in all three formats simultaneously, which may be useful in some situations, but is not the specific flag for XML-only output.

---

**Question 16**
What is the purpose of the Nmap `-A` flag and why should it be used carefully during a penetration test?

*   A) It enables anonymous scanning mode, which hides the tester's IP address from target logs
*   B) It enables aggressive mode combining OS detection, version detection, script scanning, and traceroute — generating significantly more traffic and increasing detection probability
*   C) It enables authentication bypass mode, attempting to log into discovered services with default credentials
*   D) It instructs Nmap to use ARP requests instead of TCP/IP probes for host discovery on local subnets
*   **Correct Answer:** B) It enables aggressive mode combining OS detection, version detection, script scanning, and traceroute
*   **Distractor Analysis:**
    *   *Why B is correct:* `-A` is an umbrella flag that runs OS detection (`-O`), version detection (`-sV`), default NSE scripts (`-sC`), and traceroute simultaneously. It is highly comprehensive but generates substantial traffic, making it easily detectable by IDS/IPS and firewall logging.
    *   *Why A is incorrect:* Nmap has no anonymous scanning mode. The tester's IP address is always the source of scan packets unless separately obscured through a decoy or proxy configuration.
    *   *Why C is incorrect:* Authentication bypass and default credential testing are performed by specific NSE scripts (e.g., `--script=auth` or `--script=brute`), not the `-A` flag.
    *   *Why D is incorrect:* ARP-based host discovery is used automatically by Nmap on local subnets when running with root privileges. This behavior is not controlled by `-A`.

---

**Question 17**
A penetration tester runs `nmap -sV -p 21 target_ip` and receives the banner: `220 FileZilla Server 0.9.41 beta`. Why is the version string in this banner significant?

*   A) It confirms the FTP service is disabled and the port is not listening for connections
*   B) It identifies a specific software version that can be cross-referenced against CVE databases to find known vulnerabilities applicable to that exact version
*   C) It confirms the server uses FTPS (FTP over SSL) and all data transfers are encrypted
*   D) Version strings in FTP banners are always falsified by administrators and carry no reconnaissance value
*   **Correct Answer:** B) It identifies a specific software version that can be cross-referenced against CVE databases
*   **Distractor Analysis:**
    *   *Why B is correct:* Service version strings are the primary input for CVE research. Knowing the exact software (FileZilla Server) and version (0.9.41 beta) allows the tester to query the NVD, Exploit-DB, or Metasploit module list for known vulnerabilities affecting that specific version.
    *   *Why A is incorrect:* Receiving a banner response on port 21 confirms the service is actively listening. A banner is a positive indication of an open, responding service.
    *   *Why C is incorrect:* FileZilla 0.9.41 running on port 21 is plain FTP, not FTPS. FTPS typically uses port 990 or requires explicit TLS negotiation.
    *   *Why D is incorrect:* While some administrators modify banners, version strings are generally reliable starting points for CVE research. Dismissing all banner data as falsified would cause testers to miss real vulnerabilities.

---

**Question 18**
During an authorized Nmap scan, a tester wants to run the default NSE script set against a target. Which flag enables this, and what do default scripts typically perform?

*   A) `--script=all` — runs every available NSE script including destructive and exploit scripts
*   B) `-sC` — runs the default NSE script set, performing safe service enumeration, banner grabbing, and common misconfiguration checks without attempting exploitation
*   C) `--script=vuln` — runs only vulnerability detection scripts, which is what "default" refers to in Nmap documentation
*   D) `-sN` — enables null scan mode, which is Nmap's term for the default script execution mode
*   **Correct Answer:** B) `-sC`
*   **Distractor Analysis:**
    *   *Why B is correct:* `-sC` runs the `default` NSE script category, which includes safe enumeration scripts that gather service information, perform banner analysis, and check for common misconfigurations without attempting exploitation.
    *   *Why A is incorrect:* `--script=all` runs every available NSE script including destructive, brute-force, and exploit scripts. This is dangerous in production environments and is not what "default scripts" means.
    *   *Why C is incorrect:* `--script=vuln` runs the vulnerability detection category, which focuses specifically on identifying CVE-related vulnerabilities — a distinct and more aggressive category from the default set.
    *   *Why D is incorrect:* `-sN` is a TCP null scan (sends packets with no TCP flags set) — a stealthy port scanning technique unrelated to NSE script execution.

---

**Question 19**
A tester scans a target subnet with `nmap -sn 192.168.1.0/24` and receives responses from 12 IP addresses. What has this scan accomplished, and what has it NOT accomplished?

*   A) It has identified all open ports on 12 hosts; it has not identified the services running on those ports
*   B) It has identified 12 live (responding) hosts on the subnet; it has not scanned any ports or identified any services on those hosts
*   C) It has identified 12 hosts with open web servers; it has not checked whether HTTPS is also running
*   D) It has identified 12 hosts running Windows; it has not determined whether they are patched
*   **Correct Answer:** B) It has identified 12 live hosts; it has not scanned any ports or identified services
*   **Distractor Analysis:**
    *   *Why B is correct:* `-sn` is the ping sweep flag — it performs host discovery only and does not scan ports. The 12 responding IP addresses are confirmed live hosts. No port scanning, service detection, or OS fingerprinting has occurred.
    *   *Why A is incorrect:* `-sn` explicitly disables port scanning. It performs only host discovery — no port states are returned.
    *   *Why C is incorrect:* A ping sweep cannot identify what services are running. It only confirms which IP addresses are responding to the discovery probes.
    *   *Why D is incorrect:* OS identification requires the `-O` flag and TCP/IP fingerprinting. A ping sweep does not perform OS detection.

---

**Question 20**
During an authorized scan, a tester runs `nmap -sV --version-intensity 9 target_ip`. What does `--version-intensity 9` do, and what is the trade-off of using the highest intensity level?

*   A) It limits version detection to only nine ports, making the scan faster but less comprehensive
*   B) It sets version detection to maximum thoroughness, sending the greatest number of probe types to identify service versions — at the cost of increased scan time and greater network noise
*   C) It configures Nmap to retry each port exactly nine times before marking it as filtered
*   D) It sets the TCP timing template to level 9, which is faster than the default -T3 template
*   **Correct Answer:** B) It sets version detection to maximum thoroughness at the cost of increased scan time and network noise
*   **Distractor Analysis:**
    *   *Why B is correct:* `--version-intensity` controls how aggressively Nmap probes services for version information. A value of 9 (maximum) sends the widest variety of service probes, improving accuracy for uncommon services — at the cost of more packets sent, longer scan duration, and greater detectability by monitoring systems.
    *   *Why A is incorrect:* `--version-intensity` does not limit the number of ports scanned. It controls the depth of version probing for each service encountered.
    *   *Why C is incorrect:* Retry behavior is controlled by `--max-retries`, not `--version-intensity`. These are independent Nmap options.
    *   *Why D is incorrect:* Timing templates are set with `-T0` through `-T5`. The `--version-intensity` flag has no effect on timing.
