# Quiz: Module 13 — Maintaining Access & Pivoting

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

**Instructions:** Choose the single best answer for each question.

---

**Question 1**

A penetration tester has SSH access to a Linux jump host at `10.10.10.5`. Behind that host is an isolated internal network `192.168.50.0/24` that is not directly reachable from the tester's machine. The tester wants to run any tool against internal hosts by routing traffic through the jump host. Which SSH command creates the most flexible pivoting configuration?

- A) `ssh -L 8080:192.168.50.10:80 user@10.10.10.5`
- B) `ssh -R 4444:localhost:4444 user@10.10.10.5`
- C) `ssh -D 9050 user@10.10.10.5`
- D) `ssh -N user@10.10.10.5`

**Correct Answer:** C) `ssh -D 9050 user@10.10.10.5`

**Distractor Analysis:**

- *Why C is correct:* Dynamic port forwarding (`-D 9050`) creates a SOCKS proxy on the attacker's localhost at port 9050. Any application configured to use this SOCKS proxy — via proxychains or direct SOCKS support — routes its traffic through the SSH connection to the jump host and from there to any host on `192.168.50.0/24`. This is the most flexible option because it supports any destination port and any target host in the reachable network, without needing to specify a single destination in advance.
- *Why A is incorrect:* Local port forwarding (`-L 8080:192.168.50.10:80`) reaches only one specific destination — port 80 on `192.168.50.10`. It is useful for accessing a single internal service but cannot be used to route arbitrary tools to arbitrary hosts across the internal network. A new `-L` flag is required for each individual service you want to reach.
- *Why B is incorrect:* Remote port forwarding (`-R 4444:localhost:4444`) binds port 4444 on the SSH server (`10.10.10.5`) and forwards connections back to the attacker's port 4444. This is used to expose an attacker service through the jump host — the direction of the forwarding is reversed. It does not provide outbound access to the `192.168.50.0/24` network.
- *Why D is incorrect:* The `-N` flag suppresses command execution, telling SSH not to run a remote command. It is used as a modifier with other tunneling flags (e.g., `ssh -D 9050 -N user@host`) to keep the SSH tunnel open without an interactive shell. By itself, `-N` does not create any port forwarding or proxy.

---

**Question 2**

A penetration tester uses SSH dynamic port forwarding on port 9050 and wants to run nmap against an internal host `192.168.50.20` through the SOCKS proxy. Which nmap scan type is compatible with proxychains routing?

- A) SYN scan: `proxychains nmap -sS 192.168.50.20`
- B) UDP scan: `proxychains nmap -sU 192.168.50.20`
- C) TCP connect scan: `proxychains nmap -sT -Pn 192.168.50.20`
- D) OS detection: `proxychains nmap -O 192.168.50.20`

**Correct Answer:** C) TCP connect scan: `proxychains nmap -sT -Pn 192.168.50.20`

**Distractor Analysis:**

- *Why C is correct:* Proxychains intercepts TCP socket calls made by applications using the standard socket API. A TCP connect scan (`-sT`) completes the full three-way handshake using the standard `connect()` system call, which proxychains can intercept and route through the SOCKS proxy. The `-Pn` flag skips ICMP ping discovery, which is necessary because ICMP is not TCP and cannot be proxied. Full TCP connect scans are the only nmap scan type compatible with proxychains.
- *Why A is incorrect:* SYN (half-open) scans use raw socket operations, not the standard `connect()` call. Proxychains cannot intercept raw socket operations because they bypass the standard socket API that proxychains hooks. SYN scans through proxychains will fail or produce incorrect results.
- *Why B is incorrect:* UDP scans use UDP sockets, not TCP. SOCKS proxies are TCP-only — they cannot relay UDP traffic (SOCKS5 has optional UDP associate support but it is rarely supported in practice). UDP scans through proxychains will not work.
- *Why D is incorrect:* OS detection uses TCP with additional fingerprinting techniques including packet timing and flag variations that require raw socket access. These raw socket operations are not intercepted by proxychains. Additionally, OS detection works poorly through a proxy because packet timing characteristics change significantly.

---

**Question 3**

A Windows penetration tester wants to establish persistence using the registry. The current user is a standard (non-administrator) user account. Which registry key can the tester modify without administrator privileges to achieve persistence?

- A) `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
- B) `HKLM\System\CurrentControlSet\Services`
- C) `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
- D) `HKLM\Security\Policy\Secrets`

**Correct Answer:** C) `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

**Distractor Analysis:**

- *Why C is correct:* The `HKCU` (HKEY_CURRENT_USER) hive stores per-user settings and is writeable by the logged-in user without administrator privileges. Any value placed in `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` executes when that specific user logs on. A standard user can add, modify, and delete values in their own HKCU hive. This makes it an accessible persistence mechanism even from a low-privilege account.
- *Why A is incorrect:* `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` is in the HKEY_LOCAL_MACHINE hive, which stores system-wide settings. Modifying HKLM requires administrator privileges. A standard user will receive an "Access Denied" error when attempting to write to HKLM keys.
- *Why B is incorrect:* `HKLM\System\CurrentControlSet\Services` contains Windows service configurations. Modifying this key to register a new service requires administrator privileges. This is a different persistence mechanism (service-based) and is also HKLM-protected.
- *Why D is incorrect:* `HKLM\Security\Policy\Secrets` is a protected registry key containing LSA secrets. It requires SYSTEM-level access (not just administrator) to read or modify. A standard user cannot access this key at all.

---

**Question 4**

After establishing a Meterpreter session on a pivot host (`Session 1`), a tester wants to scan the internal network `10.10.20.0/24` that is reachable from the pivot host but not from the attacker's machine. Which Metasploit command correctly adds a route through the session?

- A) `route add 10.10.20.0 255.255.255.0 1`
- B) `route add 10.10.20.0/24 1`
- C) `sessions -r 10.10.20.0/24`
- D) `use auxiliary/server/socks_proxy` then `set SUBNET 10.10.20.0/24`

**Correct Answer:** B) `route add 10.10.20.0/24 1`

**Distractor Analysis:**

- *Why B is correct:* In Metasploit, `route add <subnet/cidr> <session_id>` adds a routing entry that directs traffic destined for the specified subnet through the specified Meterpreter session. The session ID (1) identifies which active Meterpreter session to use as the pivot. After adding the route, Metasploit modules and exploits targeting addresses in `10.10.20.0/24` are automatically routed through Session 1 on the pivot host. `route print` confirms the routing table.
- *Why A is incorrect:* While `route add 10.10.20.0 255.255.255.0 1` uses traditional subnet mask notation rather than CIDR notation, the real issue is that Metasploit's `route add` command uses CIDR notation and a session ID. The syntax in Option A is more reminiscent of a network device command syntax than the Metasploit command format. The correct Metasploit syntax uses CIDR.
- *Why C is incorrect:* `sessions -r` is not a valid Metasploit command for routing. `sessions -l` lists active sessions, `sessions -i <id>` interacts with a session, and `sessions -k <id>` kills a session. There is no `-r` flag for routing in the sessions command — routing is managed with the `route` command.
- *Why D is incorrect:* `auxiliary/server/socks_proxy` creates a SOCKS proxy through active sessions for use with external tools like proxychains. It is a complementary tool to routing, but it is not the command that adds a route. Routes must be added with `route add` before or alongside the SOCKS proxy. The `socks_proxy` module does not accept a `SUBNET` option.

---

**Question 5**

A penetration tester wants to execute commands on a remote Windows host using valid administrator credentials. They want the technique to generate as little forensic evidence as possible and avoid creating a new Windows service on the target. Which Impacket tool is most appropriate?

- A) `psexec.py` — SMB-based remote execution via service installation
- B) `wmiexec.py` — WMI-based remote execution without service installation
- C) `secretsdump.py` — Remote credential dumping via DCOM
- D) `smbclient.py` — Interactive SMB share access

**Correct Answer:** B) `wmiexec.py` — WMI-based remote execution without service installation

**Distractor Analysis:**

- *Why B is correct:* `wmiexec.py` executes commands on remote Windows systems using Windows Management Instrumentation (WMI). Unlike PsExec, it does not install a service on the target — it uses the WMI Win32_Process class to create processes. This leaves a smaller forensic footprint because no service binaries are written to disk and no service registration events appear in the Windows System event log. WMI does generate WMI activity events (Event ID 4688 for process creation, WMI provider events) but these are less commonly monitored than service installation events.
- *Why A is incorrect:* `psexec.py` executes commands by writing a service binary to the target's ADMIN$ share, registering it as a Windows service, starting the service, and cleaning up afterward. This generates Windows Event ID 7045 (service installation) and Event ID 7036 (service start/stop), which are commonly monitored by security tools. The question specifically asks for a technique that avoids service creation.
- *Why C is incorrect:* `secretsdump.py` performs remote credential dumping — extracting SAM hashes, LSA secrets, and cached domain credentials from the target. It is not a command execution tool. It is used to harvest credentials, not to run arbitrary commands interactively on the target.
- *Why D is incorrect:* `smbclient.py` provides interactive access to SMB shares for file operations (listing, uploading, downloading). It does not execute commands on the remote system. It is useful for data access but not for command execution or lateral movement.

---

**Question 6**

A penetration tester has root access on a Linux server and wants to establish a persistence mechanism that survives reboots and does not require any user interaction to trigger. Which mechanism best meets both requirements?

- A) Adding a malicious script to the current user's `~/.bashrc` file
- B) Adding an entry to the root user's crontab that runs a reverse shell every minute
- C) Creating a new SSH key pair and adding it to `~/.ssh/authorized_keys`
- D) Dropping a reverse shell executable in the `/tmp` directory

**Correct Answer:** B) Adding an entry to the root user's crontab that runs a reverse shell every minute

**Distractor Analysis:**

- *Why B is correct:* A cron job in root's crontab runs automatically on its schedule (every minute in this case) without requiring any user interaction. The `crond` daemon runs as a system process that starts automatically at boot — so the cron job survives reboots and begins executing again as soon as cron starts. This provides persistent, automated call-back without requiring anyone to log in or trigger the payload manually.
- *Why A is incorrect:* `~/.bashrc` entries execute when the user opens an interactive shell. They require the user to actually log in and start a bash session. The mechanism does not survive meaningfully without user interaction — if no one logs in, the payload never runs. Additionally, `~/.bashrc` does not execute at boot.
- *Why C is incorrect:* SSH authorized keys allow the tester to authenticate and get a shell when they choose to connect. The mechanism survives reboots and does not require the victim to do anything. However, it requires the tester to actively initiate the connection — it is not an automated call-back. SSH keys provide access on demand, not automated persistence that reaches out without the tester's initiation.
- *Why D is incorrect:* Dropping an executable in `/tmp` provides no persistence mechanism at all. The file sits on disk waiting to be executed. It does not run automatically, does not survive reboots (many systems clear `/tmp` on reboot), and requires manual execution to do anything.

---

**Question 7**

A penetration tester has completed an authorized engagement that included installing persistence mechanisms for testing purposes. The Rules of Engagement require all artifacts to be removed within 24 hours. Which statement correctly describes the tester's cleanup obligations?

- A) The tester should clear all Windows Event Logs to remove evidence of the test activity, then remove persistence artifacts.
- B) The tester must remove all installed persistence mechanisms, delete dropped tools and payloads, restore modified configurations, and document every removed artifact in the final report.
- C) The tester only needs to remove the persistence mechanisms that the client's security team did not detect, as detected artifacts are already being handled by the security team.
- D) Cleanup is optional if the engagement has ended and the final report has been delivered.

**Correct Answer:** B) The tester must remove all installed persistence mechanisms, delete dropped tools and payloads, restore modified configurations, and document every removed artifact in the final report.

**Distractor Analysis:**

- *Why B is correct:* Professional penetration testing standards require complete cleanup of all artifacts introduced during the test. This includes persistence mechanisms (cron jobs, registry keys, scheduled tasks, SSH keys), dropped tools and payloads (LinPEAS, WinPEAS, Mimikatz, reverse shell executables), and configuration changes. Each removed artifact must be documented in the engagement log and confirmed in the final report. This protects both the client (their environment is clean) and the tester (documented evidence of responsible conduct).
- *Why A is incorrect:* Log clearing without explicit authorization is not a cleanup activity — it is evidence destruction. If the RoE authorizes log clearing as a demonstration of attacker capability, it should be documented as a finding showing that attackers can cover their tracks. Proactively clearing logs without authorization violates professional ethics and potentially legal obligations. The question does not indicate that log clearing is authorized.
- *Why C is incorrect:* Cleanup obligations are not conditional on whether the client's security team detected the artifacts. The tester is responsible for removing everything they introduced regardless of detection status. Leaving artifacts because they were detected misunderstands the cleanup obligation — detected artifacts still need to be removed to restore the environment to its pre-test state.
- *Why D is incorrect:* Cleanup is never optional when the RoE requires it. Leaving backdoors, tools, and persistence mechanisms on client systems after an engagement creates ongoing security risk, legal liability, and professional credibility damage. The professional standard is unconditional: clean up everything you installed.

---

**Question 8**

Which data exfiltration channel is most difficult to block at the perimeter because the underlying protocol is typically permitted outbound and carries only small requests that blend into normal baseline traffic?

- A) HTTPS file upload to a cloud storage service
- B) FTP transfer to an external server on port 21
- C) DNS tunneling using encoded data in DNS query labels
- D) ICMP tunneling using data embedded in ping packet payloads

**Correct Answer:** C) DNS tunneling using encoded data in DNS query labels

**Distractor Analysis:**

- *Why C is correct:* DNS is almost universally permitted outbound because blocking DNS would break internet connectivity for the entire organization. Individual DNS queries are small (under 253 characters for the total name), appear as routine lookups for domain names, and are not commonly subject to deep packet inspection. Tools like `dnscat2` encode data in the subdomain labels of DNS queries directed to an attacker-controlled authoritative nameserver. The queries appear as legitimate-looking recursive lookups. While high query volume, unusual query lengths, and lookups for non-existent domains are detectable with DNS analytics, many organizations have no such monitoring in place.
- *Why A is incorrect:* HTTPS file uploads to cloud storage are also commonly permitted and encrypted, but they can be blocked by URL/domain filtering (many organizations block unauthorized cloud storage services), traffic volume analysis, or TLS inspection. Cloud storage destinations are also known and can be enumerated. DNS is harder to block because there is no discrete destination — the attacker controls the authoritative DNS server, not a cloud storage endpoint.
- *Why B is incorrect:* FTP on port 21 is frequently blocked at enterprise perimeters as a known legacy protocol. Many organizations block outbound FTP entirely or only allow it to specific business-justified destinations. It is one of the easier exfiltration channels to block.
- *Why D is incorrect:* ICMP tunneling embeds data in ping packet payloads. While ICMP is often permitted outbound, ICMP payloads are normally fixed-size and content-predictable. Many firewalls inspect ICMP payload size and content, and large or variable-size ICMP payloads are easier to detect than DNS queries. DNS tunneling is generally considered more covert than ICMP tunneling.

---

**Question 9**

A penetration tester has a Meterpreter session on a compromised Windows host. They want to access an internal web application at `172.16.5.20:443` that is only reachable from the pivot host. Which Meterpreter command creates a local port forward to access this service?

- A) `route add 172.16.5.0/24 1`
- B) `portfwd add -l 8443 -p 443 -r 172.16.5.20`
- C) `ssh -L 8443:172.16.5.20:443 user@pivot`
- D) `socks5 172.16.5.20 443`

**Correct Answer:** B) `portfwd add -l 8443 -p 443 -r 172.16.5.20`

**Distractor Analysis:**

- *Why B is correct:* The Meterpreter `portfwd` command manages port forwarding through the active session. `portfwd add -l 8443 -p 443 -r 172.16.5.20` creates a local port forward: `-l 8443` binds port 8443 on the attacker's local machine, `-r 172.16.5.20` specifies the remote destination host, and `-p 443` specifies the destination port. After running this command, connecting to `localhost:8443` from the attacker machine routes through the Meterpreter session to `172.16.5.20:443`. This enables direct browser or tool access to the internal web application.
- *Why A is incorrect:* `route add 172.16.5.0/24 1` adds a routing entry for the subnet through Session 1. This allows Metasploit modules to reach hosts in that subnet, but it does not create a local port forward. To access the web application directly in a browser, a port forward (not just a route) is needed.
- *Why C is incorrect:* This is the SSH command syntax for local port forwarding, not the Meterpreter command syntax. In a Meterpreter session, port forwarding is managed with `portfwd`, not with SSH flags. This command would only work if SSH were available separately, not within Meterpreter.
- *Why D is incorrect:* `socks5 172.16.5.20 443` is not a valid Meterpreter command. It appears to confuse the Meterpreter command syntax with an external configuration syntax. Meterpreter's SOCKS proxy is created through the Metasploit `auxiliary/server/socks_proxy` module from the MSF console, not via a `socks5` Meterpreter command.

---

**Question 10**

A penetration tester installs a Linux cron-based reverse shell during an authorized engagement. Which cleanup action correctly removes this persistence mechanism?

- A) Delete the `/etc/cron.d/` directory entirely to remove all cron configurations
- B) Edit the specific crontab (using `crontab -e` for the current user or editing the system crontab directly) and remove only the line containing the reverse shell entry
- C) Reboot the system, as cron entries are cleared on restart
- D) Change the cron service port to prevent the reverse shell from connecting

**Correct Answer:** B) Edit the specific crontab (using `crontab -e` for the current user or editing the system crontab directly) and remove only the line containing the reverse shell entry

**Distractor Analysis:**

- *Why B is correct:* Cron persistence is removed by editing the crontab that contains the malicious entry and deleting only that specific line. For user-level cron entries, `crontab -e` opens the current user's crontab for editing. For entries placed in `/etc/crontab` or `/etc/cron.d/`, the files are edited directly (with appropriate permissions). Removing only the malicious entry preserves any legitimate cron jobs that were present before the test, restoring the system to its pre-test state without collateral damage.
- *Why A is incorrect:* Deleting the `/etc/cron.d/` directory would remove all system cron configurations, not just the attacker's entry. This would break legitimate scheduled tasks and cause service disruptions. Cleanup must be surgical — remove only what was added, nothing else.
- *Why B (clarification on C being incorrect):* Cron entries are not cleared on reboot. The `crond` daemon reads crontab files from disk and those files persist across reboots. That is precisely why cron is an effective persistence mechanism. Rebooting without removing the crontab entry would simply cause the malicious job to execute again as soon as cron starts after reboot.
- *Why D is incorrect:* Cron executes commands — it does not have a "service port." The reverse shell is an outbound TCP connection initiated by the shell command in the cron entry, not a service listening on a port. There is no cron port to change. This option demonstrates a fundamental misunderstanding of how cron-based persistence works.

---

---

**Question 11**

A tester has a Meterpreter session on a compromised host with two network interfaces: `eth0` (10.10.10.50, accessible from attacker) and `eth1` (192.168.50.1, internal network). After running `run post/multi/manage/autoroute -s 192.168.50.0/24`, a tester wants to use `proxychains nmap` to scan 192.168.50.0/24. What additional step is required?

- A) Run `portfwd add -l 1080 -p 1080 -r 192.168.50.1` to create a port-specific tunnel
- B) Start a SOCKS proxy in Metasploit with `use auxiliary/server/socks_proxy`, set `SRVPORT 1080`, and run it — then configure `/etc/proxychains4.conf` with `socks5 127.0.0.1 1080`
- C) Autoroute automatically enables proxychains — no additional configuration is required
- D) Change the attacker's default gateway to 192.168.50.1 to enable direct routing

**Correct Answer:** B) Start a SOCKS proxy in Metasploit with `use auxiliary/server/socks_proxy`, set `SRVPORT 1080`, and run it — then configure `/etc/proxychains4.conf` with `socks5 127.0.0.1 1080`

**Distractor Analysis:**

- *Why B is correct:* Autoroute routes traffic within Metasploit's internal routing table — it enables Metasploit modules to reach the internal subnet but does not expose that routing to the attacker's OS. To route external tools (Nmap, curl, browsers) through the pivot, a SOCKS proxy must be created within Metasploit's routing context and proxychains must be configured to forward traffic through it. This two-step setup extends Metasploit's routing to any tool that supports SOCKS.
- *Why A is incorrect:* `portfwd` creates a specific port-to-specific-host tunnel, not a subnet-wide SOCKS proxy. It would allow reaching one port on one host but cannot provide general subnet routing for an Nmap sweep.
- *Why C is incorrect:* Autoroute does not automatically configure proxychains. Autoroute modifies Metasploit's internal routing only. Proxychains requires a listening SOCKS proxy to forward through.
- *Why D is incorrect:* Changing the attacker machine's default gateway would require administrative access to the attacker's OS networking and would redirect all traffic through the pivot — a disruptive change that could break the attacker's own connectivity. It is not the correct pivoting approach.

---

**Question 12**

A tester adds a Windows registry Run key for persistence during an authorized engagement. The key is `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` with value name `LabTest` and data `C:\Windows\Temp\agent.exe`. When does this persistence mechanism trigger?

- A) Every time the system boots, regardless of which user logs in
- B) Every time the specific user whose `HKCU` hive was modified logs into Windows — `HKCU` is per-user and executes in the context of that user at login
- C) Every 5 minutes via a Windows Task Scheduler integration with the registry
- D) Only when the user manually runs `regedit.exe` after login

**Correct Answer:** B) Every time the specific user whose `HKCU` hive was modified logs into Windows — `HKCU` is per-user and executes in the context of that user at login

**Distractor Analysis:**

- *Why B is correct:* `HKCU` (HKEY_CURRENT_USER) is a per-user registry hive — modifications affect only the currently logged-in user whose profile is loaded. Run keys in `HKCU\...\Run` execute when that specific user logs in. For system-wide persistence (any user login), `HKLM\...\Run` is used instead. The distinction matters for both attack scope and cleanup — only the targeted user's session triggers the payload.
- *Why A is incorrect:* `HKCU` persistence is user-specific, not system-wide. Every-boot execution for all users requires `HKLM\...\Run`, not `HKCU`. The scope of `HKCU` is limited to one user's login.
- *Why C is incorrect:* Registry Run keys have no relationship to Task Scheduler. They are processed by the Windows login session manager (winlogon) when a user logs in, not by a scheduler on a time interval.
- *Why D is incorrect:* Registry Run keys execute automatically at login — the user does not need to manually run anything. That is the purpose of Run key persistence: execution without user interaction.

---

**Question 13**

During a Linux post-exploitation engagement, a tester adds an SSH public key to `/root/.ssh/authorized_keys`. What cleanup action ensures complete removal of this persistence mechanism?

- A) Delete the entire `/root/.ssh/` directory to remove all SSH configuration
- B) Remove only the specific public key entry added during the test from `authorized_keys`, preserving any pre-existing keys, then verify with `cat` that only original keys remain
- C) Run `ssh-keygen -R target_ip` on the attacker machine to revoke the key remotely
- D) Restart the SSH service — the daemon clears authorized_keys on restart

**Correct Answer:** B) Remove only the specific public key entry added during the test from `authorized_keys`, preserving any pre-existing keys, then verify with `cat` that only original keys remain

**Distractor Analysis:**

- *Why B is correct:* Cleanup must be surgical — remove only what the tester added without disturbing pre-existing configuration. The correct procedure is to open `authorized_keys`, identify and remove the line containing the tester's public key (identified by its unique comment field or key fingerprint), save the file, and verify the remaining content matches the pre-test state. Deleting other users' legitimate keys would disrupt their access.
- *Why A is incorrect:* Deleting the entire `.ssh/` directory removes all authorized keys and SSH configuration, including any keys that existed before the test. This disrupts legitimate administrative access and is a destructive overstep beyond removing only the added persistence.
- *Why C is incorrect:* `ssh-keygen -R` removes a host key from the attacker's own `known_hosts` file — it removes the target from the attacker's trusted hosts list. It has no effect on the target's `authorized_keys` file and does not remove persistence on the target.
- *Why D is incorrect:* SSH reads `authorized_keys` from disk on each connection attempt — restarting the SSH daemon does not clear or reset the file. Keys in `authorized_keys` persist indefinitely until manually removed.

---

**Question 14**

What distinguishes DNS tunneling from ICMP tunneling as a covert channel for data exfiltration?

- A) DNS tunneling uses UDP port 53 and encodes data in DNS query names/responses; ICMP tunneling encodes data in ICMP echo request/reply payloads — both bypass many firewalls but DNS is more reliable because DNS queries are almost universally permitted through corporate egress controls
- B) DNS tunneling requires root access; ICMP tunneling works as any user
- C) ICMP tunneling is encrypted; DNS tunneling sends data in plaintext
- D) DNS tunneling only works on Windows; ICMP tunneling works cross-platform

**Correct Answer:** A) DNS tunneling uses UDP port 53 and encodes data in DNS query names/responses; ICMP tunneling encodes data in ICMP echo request/reply payloads — both bypass many firewalls but DNS is more reliable because DNS queries are almost universally permitted through corporate egress controls

**Distractor Analysis:**

- *Why A is correct:* DNS tunneling encodes data in DNS query subdomain names (e.g., `data.exfil.attacker.com`) and extracts data from DNS responses. Because DNS is a fundamental protocol required for internet access, outbound DNS is almost never blocked — making it a highly reliable exfiltration channel. ICMP tunneling embeds data in the payload field of ICMP echo packets. While ICMP is often permitted for ping, many environments block ICMP outbound or do deep packet inspection that detects large/unusual ICMP payloads.
- *Why B is incorrect:* Both DNS and ICMP tunneling tools typically require elevated privileges for raw socket access. The privilege requirement is similar for both, not a distinguishing factor.
- *Why C is incorrect:* Neither DNS nor ICMP tunneling provides native encryption. Both send data in a format that can be inspected. Encryption requires a separate layer (e.g., encrypting the payload before encoding it in DNS queries).
- *Why D is incorrect:* Both techniques are cross-platform and have implementations for Linux, Windows, and macOS. Platform availability is not a distinguishing factor.

---

**Question 15**

A tester uses `ssh -D 1080 user@pivot_host` to create a dynamic SOCKS proxy through a pivot. What does the `-D` flag specifically configure?

- A) A local port forward that maps `localhost:1080` to `pivot_host:1080`
- B) A dynamic application-level port forwarding (SOCKS proxy) that listens on the attacker's `localhost:1080` and forwards all connections through the SSH tunnel to the pivot, enabling the pivot to reach any destination on its behalf
- C) A remote port forward that exposes the attacker's port 1080 on the pivot host
- D) Direct shell access to the pivot host's SOCKS proxy service running on port 1080

**Correct Answer:** B) A dynamic application-level port forwarding (SOCKS proxy) that listens on the attacker's `localhost:1080` and forwards all connections through the SSH tunnel to the pivot, enabling the pivot to reach any destination on its behalf

**Distractor Analysis:**

- *Why B is correct:* SSH's `-D` flag creates a SOCKS proxy — a dynamic port forward where the destination is not pre-specified. Any application configured to use the SOCKS proxy at `localhost:1080` has its connections forwarded through the SSH tunnel and initiated by the pivot host. This enables the attacker to reach any host accessible to the pivot (internal subnets, services behind the pivot's firewall). Combined with proxychains, all traffic from any tool is routed through the pivot.
- *Why A is incorrect:* `-L` creates local port forwards with a fixed destination. `-D` is specifically for dynamic SOCKS proxying where the destination is determined at runtime by the connecting application, not pre-configured.
- *Why C is incorrect:* `-R` creates remote port forwards that expose an attacker's local port on the remote (pivot) host. `-D` creates a local SOCKS listener, not a remote forward.
- *Why D is incorrect:* `-D` creates a new SOCKS proxy service using SSH — the pivot does not need to be running any pre-existing SOCKS service. The proxy is created dynamically by the SSH connection itself.

---

**Question 16**

After completing a penetration test, a tester reviews their engagement log and identifies four artifacts left on client systems: a cron job on a Linux server, an SSH key in `/root/.ssh/authorized_keys`, a Windows registry Run key, and a Meterpreter payload at `C:\Windows\Temp\agent.exe`. Which cleanup sequence is most professional?

- A) Delete only the Meterpreter payload since it is the most dangerous artifact; document the others as known residuals in the final report
- B) Remove all four artifacts in reverse order of creation, verify removal of each with a screenshot, and document each removal with timestamp in the engagement log before closing the engagement
- C) Notify the client's IT team of the artifacts and let them handle removal — cleanup is the client's responsibility
- D) Leave the artifacts in place until the final report is delivered; remove them after the client confirms they have read the report

**Correct Answer:** B) Remove all four artifacts in reverse order of creation, verify removal of each with a screenshot, and document each removal with timestamp in the engagement log before closing the engagement

**Distractor Analysis:**

- *Why B is correct:* All artifacts installed during a penetration test must be removed by the tester before the engagement closes. Removing them with verification and documenting each removal with timestamps ensures there is a clean chain of custody showing the system was restored to its pre-test state. Reverse-order removal is a best practice that prevents dependency issues (e.g., removing the payload before the persistence mechanism that calls it).
- *Why A is incorrect:* All persistence mechanisms are dangerous, not just the payload. A registry Run key or cron job pointing to a non-existent file is a broken artifact — but a cron job could be modified by another party to execute different content. All artifacts must be removed.
- *Why C is incorrect:* The tester is responsible for removing what they installed. Leaving cleanup to the client is unprofessional and potentially a contractual breach. The client hired the tester to test, not to create long-term IT remediation work.
- *Why D is incorrect:* Artifacts must be removed before the engagement closes, not after report delivery. Report delivery may take days or weeks — leaving active persistence mechanisms during that time creates unauthorized ongoing access.

---

**Question 17**

A tester uses WMI (Windows Management Instrumentation) for lateral movement by running `wmic /node:192.168.1.20 /user:Administrator /password:P@ssw0rd process call create "cmd /c whoami > C:\result.txt"`. What makes WMI an attractive lateral movement technique compared to PsExec?

- A) WMI requires no authentication — it works anonymously on all Windows versions
- B) WMI uses a different network protocol (DCOM/RPC over dynamic ports) than PsExec (SMB port 445), making it less likely to be blocked by host-based firewalls that specifically block SMB; WMI also does not require dropping an executable to disk
- C) WMI is encrypted end-to-end while PsExec sends credentials in plaintext
- D) WMI escalates privileges automatically to SYSTEM without requiring administrator credentials

**Correct Answer:** B) WMI uses a different network protocol (DCOM/RPC over dynamic ports) than PsExec (SMB port 445), making it less likely to be blocked by host-based firewalls that specifically block SMB; WMI also does not require dropping an executable to disk

**Distractor Analysis:**

- *Why B is correct:* WMI uses DCOM over RPC (initially port 135, then dynamic high ports) rather than SMB (445). Environments with host-based firewalls blocking SMB may still allow WMI traffic. Additionally, WMI-based execution is "fileless" — it does not require uploading an executable to the remote host, leaving fewer artifacts compared to PsExec which drops a service binary.
- *Why A is incorrect:* WMI requires valid credentials just like PsExec. The command in the question explicitly provides username and password. Anonymous WMI access is not a feature of modern Windows.
- *Why C is incorrect:* Neither WMI nor PsExec inherently encrypts credentials in a way that the other does not. Both use Windows authentication mechanisms (NTLM or Kerberos) that operate at the protocol level. This is not the meaningful distinction between the two techniques.
- *Why D is incorrect:* WMI does not provide automatic privilege escalation. It executes with the credentials provided — if Administrator credentials are supplied, commands run as Administrator. It does not grant SYSTEM access automatically.

---

**Question 18**

A tester running Impacket's `psexec.py` achieves a SYSTEM shell on a Windows target through SMB. What Windows event is generated on the target that a defender monitoring for lateral movement should detect?

- A) Event ID 4624 (Successful logon) and Event ID 7045 (New service installed) — PsExec creates a temporary service on the target to execute commands
- B) Event ID 4648 (Logon using explicit credentials) only — PsExec logons are silent and generate no service events
- C) Event ID 4625 (Failed logon) followed by Event ID 4624 — PsExec always fails once before succeeding
- D) No Windows events are generated — PsExec operates entirely below the event log layer

**Correct Answer:** A) Event ID 4624 (Successful logon) and Event ID 7045 (New service installed) — PsExec creates a temporary service on the target to execute commands

**Distractor Analysis:**

- *Why A is correct:* PsExec works by connecting to the target's SMB share (`ADMIN$`), uploading a service binary (`PSEXESVC.exe`), creating a new Windows service (generating Event ID 7045 — New service installed), starting the service to execute commands, then cleaning up. The SMB authentication generates Event ID 4624. Monitoring for 7045 events with unusual service names (short random names or "PSEXESVC") combined with 4624 from unexpected source IPs is a standard PsExec detection rule.
- *Why B is incorrect:* PsExec always generates service installation events (7045) in addition to logon events. The service creation is the fundamental mechanism by which PsExec achieves code execution, and it is always logged.
- *Why C is incorrect:* PsExec does not inherently fail before succeeding — if the credentials are correct and connectivity exists, the first authentication attempt succeeds. Multiple 4625 events before a 4624 would suggest credential guessing, not normal PsExec operation.
- *Why D is incorrect:* Windows event logging operates at a level that captures all service installations, process creations, and authentication events. PsExec does not have any mechanism to bypass the Windows event log. Detection is straightforward for defenders monitoring the correct event IDs.

---

**Question 19**

What is the primary professional obligation when a penetration tester discovers, during a pivoting phase, that they have inadvertently accessed a system that is NOT listed in the engagement's authorized scope?

- A) Continue testing the out-of-scope system — since the access was unintentional, no authorization is violated
- B) Immediately cease all activity against the out-of-scope system, document the inadvertent access with timestamps and actions taken, and notify the client's point of contact as defined in the RoE — treat it as a potential incident
- C) Document the finding privately and include it in the final report without notifying the client during the test
- D) Remove all traces of access from the out-of-scope system and do not mention it in any documentation

**Correct Answer:** B) Immediately cease all activity against the out-of-scope system, document the inadvertent access with timestamps and actions taken, and notify the client's point of contact as defined in the RoE — treat it as a potential incident

**Distractor Analysis:**

- *Why B is correct:* Intent does not authorize access under the CFAA — accessing an out-of-scope system without authorization is a legal issue regardless of how the access occurred. The professional response is to stop immediately, document precisely what occurred (to demonstrate the tester's good faith and to enable the client to assess any impact), and notify the client so they can determine whether any action is required. This is the RoE-required incident response for scope violations.
- *Why A is incorrect:* "Unintentional" does not constitute authorization. Continuing to test an out-of-scope system after realizing the scope violation compounds the legal exposure and professional liability.
- *Why C is incorrect:* Delaying client notification until the report deprives the client of the opportunity to assess potential impact while the engagement is still active. The RoE typically specifies immediate notification for scope violations and unexpected sensitive discoveries.
- *Why D is incorrect:* Removing traces and concealing the event is a serious professional violation and potentially evidence tampering. The engagement log must accurately reflect all actions taken — including accidental scope violations.

---

**Question 20**

Which MITRE ATT&CK technique most accurately describes an attacker using a compromised web server as a hop point to reach an isolated internal database server?

- A) TA0010 Exfiltration — data is being transferred across network boundaries
- B) TA0008 Lateral Movement, specifically T1021 Remote Services — the attacker is using an already-compromised host to access additional internal systems
- C) TA0003 Persistence — maintaining long-term access is the primary goal
- D) TA0001 Initial Access — gaining initial entry to the environment through the web server

**Correct Answer:** B) TA0008 Lateral Movement, specifically T1021 Remote Services — the attacker is using an already-compromised host to access additional internal systems

**Distractor Analysis:**

- *Why B is correct:* Using a compromised host as a pivot point to reach additional internal systems is the definition of Lateral Movement (TA0008). The attacker has moved from one compromised host (web server) to another internal target (database server) by leveraging the network access of the intermediate host. T1021 (Remote Services) covers techniques like SSH, RDP, WMI, and SMB used to access additional systems.
- *Why A is incorrect:* Exfiltration (TA0010) covers moving data out of the compromised environment to attacker-controlled infrastructure. Moving from one internal host to another internal host is lateral movement, not exfiltration — no data is leaving the target environment.
- *Why C is incorrect:* Persistence (TA0003) covers mechanisms that maintain access across restarts or credential changes. Using a compromised host to reach another host is movement, not persistence installation.
- *Why D is incorrect:* Initial Access (TA0001) covers the first entry into the target environment — the original compromise of the web server. Pivoting from the web server to the database server is a post-initial-access activity.

---

*End of Module 13 Quiz*
