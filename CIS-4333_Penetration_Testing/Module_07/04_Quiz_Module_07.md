# Quiz: Module 07 - Post-Exploitation – Privilege Escalation
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which type of shell payload instructs the target machine to connect back to the attacker's listening machine?
*   A) Bind Shell
*   B) Reverse Shell
*   C) SSH Shell
*   D) Interactive Shell
*   **Correct Answer:** B) Reverse shells initiate connections outwards from the target, bypassing inbound firewall blocks.
*   **Distractor Analysis:**
    *   *Why correct:* Reverse shells instruct the compromised target to initiate an outbound TCP connection to the attacker's listener. Since the connection originates from inside the target network, inbound firewall rules do not block it.
    *   *Why A is incorrect:* A bind shell opens a listening port on the target and waits for the attacker to connect inbound. This is blocked when the target has strict inbound firewall rules.
    *   *Why C is incorrect:* SSH provides an encrypted remote shell but requires valid credentials and an SSH service — it is a legitimate remote access protocol, not a post-exploitation payload delivery mechanism.
    *   *Why D is incorrect:* "Interactive shell" describes any shell that accepts keyboard input, including both bind and reverse shells. It is not a specific payload type that initiates connections.

---

**Question 2**
In post-exploitation privilege escalation on Linux, which of the following best defines **SUID (Set User ID) binary abuse**?
*   A) A technique where an attacker adds malicious entries to the `/etc/sudoers` file to grant themselves permanent root access.
*   B) A privilege escalation method that exploits executables with the SUID permission bit set, causing them to run with the file owner's privileges (often root) instead of the invoking user's privileges.
*   C) A method of injecting shellcode into a running process to take over its execution context and inherit its privilege level.
*   D) A persistence technique that places a malicious binary in a directory that appears before system directories in the PATH variable.
*   **Correct Answer:** B) A privilege escalation method that exploits executables with the SUID permission bit set, causing them to run with the file owner's privileges (often root) instead of the invoking user's privileges.
*   **Distractor Analysis:**
    *   *Why B is correct:* When an executable has the SUID bit set and is owned by root, any user who executes it will run it with root privileges. If such a binary can be manipulated (e.g., by passing shell-escape sequences, exploiting a vulnerable version, or leveraging its functionality), it provides a path to root access. The command `find / -perm -4000 2>/dev/null` enumerates all SUID binaries.
    *   *Why A is incorrect:* Modifying `/etc/sudoers` requires root access already — it is a persistence or lateral movement technique, not a privilege escalation path from a standard user.
    *   *Why C is incorrect:* Injecting shellcode into a running process is process injection — a technique used for evasion and persistence, not specifically the definition of SUID abuse.
    *   *Why D is incorrect:* Placing a malicious binary in PATH before system directories is PATH hijacking — a distinct privilege escalation technique that exploits relative command names in scripts run by privileged users.

---

**Question 3**
A penetration tester has a low-privilege shell on a Linux target and wants to identify potential privilege escalation paths systematically. Which command enumerates all SUID binaries on the system?
*   A) `sudo -l`
*   B) `find / -perm -4000 2>/dev/null`
*   C) `cat /etc/passwd`
*   D) `ps aux`
*   **Correct Answer:** B) `find / -perm -4000 2>/dev/null`
*   **Distractor Analysis:**
    *   *Why B is correct:* `find / -perm -4000` searches the entire filesystem for files with the SUID bit set (octal 4000). The `2>/dev/null` redirects permission-denied errors to suppress noise. The output is a list of SUID binaries that can be cross-referenced against GTFOBins to identify exploitable ones.
    *   *Why A is incorrect:* `sudo -l` lists commands the current user can run with sudo privileges — this is important for sudo misconfiguration checks, but it does not enumerate SUID binaries.
    *   *Why C is incorrect:* `cat /etc/passwd` displays user account information (usernames, UIDs, home directories, shells). It is useful for understanding user accounts but does not identify SUID binaries or privilege escalation paths directly.
    *   *Why D is incorrect:* `ps aux` lists all running processes. It is useful for identifying privileged processes to migrate into but does not enumerate SUID binaries on the filesystem.

---

**Question 4**
During post-exploitation on a Windows target, a tester has a Meterpreter session running as a standard user. The `getsystem` command fails. What is the recommended next step?
*   A) Immediately run `hashdump` — credential extraction does not require elevated privileges.
*   B) Run `post/multi/recon/local_exploit_suggester` to identify privilege escalation exploits applicable to the target's OS version and patch level.
*   C) Close the session and re-exploit the system using a different exploit module to obtain a SYSTEM-level shell directly.
*   D) Run `migrate` into the `lsass.exe` process, which automatically grants SYSTEM privileges.
*   **Correct Answer:** B) Run `post/multi/recon/local_exploit_suggester` to identify privilege escalation exploits applicable to the target's OS version and patch level.
*   **Distractor Analysis:**
    *   *Why B is correct:* When automated techniques like `getsystem` fail, the next step is structured enumeration. The `local_exploit_suggester` module checks the target's OS version, service pack, and architecture against a database of local privilege escalation exploits to recommend applicable ones. This is the professional and systematic approach.
    *   *Why A is incorrect:* `hashdump` requires SYSTEM-level or at minimum high-integrity Administrator privileges to access the SAM database. Running it from a standard user context will fail with access denied errors.
    *   *Why C is incorrect:* Re-exploiting via the network attack surface does not guarantee a SYSTEM shell and wastes engagement time. Local escalation from an existing session is the correct approach.
    *   *Why D is incorrect:* Migrating into `lsass.exe` does run under SYSTEM context, but migration requires SYSTEM privileges to inject into `lsass.exe` in the first place — creating a circular dependency. You cannot migrate into a higher-privilege process than you currently have without first escalating.

---

**Question 5**
After successfully escalating to SYSTEM on a Windows target, a tester wants to extract all local account password hashes for offline cracking. Which Meterpreter command accomplishes this?
*   A) `run post/windows/gather/enum_logged_on_users`
*   B) `load kiwi` followed by `creds_all`
*   C) `hashdump`
*   D) `getuid`
*   **Correct Answer:** C) `hashdump`
*   **Distractor Analysis:**
    *   *Why C is correct:* The `hashdump` Meterpreter command extracts NTLM hashes from the Windows SAM (Security Account Manager) database for all local user accounts. These hashes can then be passed directly (Pass-the-Hash) or cracked offline using Hashcat or John the Ripper. It requires SYSTEM or Administrator privileges.
    *   *Why A is incorrect:* `post/windows/gather/enum_logged_on_users` lists currently logged-on user sessions — it does not extract password hashes from the SAM database.
    *   *Why B is incorrect:* `load kiwi` / `creds_all` uses the Kiwi (Mimikatz) module to extract plaintext passwords, hashes, and Kerberos tickets from memory — a more powerful technique, but the question asks specifically about extracting local account hashes from the SAM, for which `hashdump` is the direct and standard answer.
    *   *Why D is incorrect:* `getuid` returns the current username the Meterpreter session is running as — it is used for privilege verification, not credential extraction.
