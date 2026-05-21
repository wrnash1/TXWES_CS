# Reading Guide: Module 08 - Lateral Movement and Persistence
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 08 - Lateral Movement and Persistence**! After gaining initial access and escalating privileges, professional penetration testers move into lateral movement — the process of pivoting from one compromised host to other systems within the same network to expand access and demonstrate the full blast radius of a breach. Persistence techniques are used to maintain access across reboots, patching cycles, and user logoffs. Together, lateral movement and persistence map to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**) and reflect how real-world attackers operate once inside a network.

Demonstrating lateral movement in a pentest is critical evidence for clients: it shows that a single compromised endpoint can lead to domain-wide compromise. This module covers the core Windows and Active Directory attack techniques that PT0-002 tests directly.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Kerberoasting**: An Active Directory attack in which any authenticated domain user requests Kerberos service tickets (TGS) for accounts registered with Service Principal Names (SPNs). Because the ticket is encrypted with the service account's password hash, the attacker can extract it and attempt offline cracking with Hashcat or John the Ripper — no elevated privileges required to request the ticket. The goal is to crack weak service account passwords and use those credentials for lateral movement.

*   **Pass-the-Hash (PtH)**: A lateral movement technique in which an attacker uses a captured NTLM password hash to authenticate to remote services (SMB, WMI, RDP with NTLMv1) without ever knowing the plaintext password. The hash itself acts as the credential. Tools like Mimikatz, Impacket's `psexec.py`, and Metasploit's `psexec` module implement PtH. It works because NTLM authentication accepts the hash directly in the challenge-response protocol.

*   **LSASS Memory Dumping**: The process of extracting credential material (NTLM hashes, Kerberos tickets, and sometimes plaintext passwords) from the Windows Local Security Authority Subsystem Service (`lsass.exe`) process memory. Tools include Mimikatz (`sekurlsa::logonpasswords`), `procdump.exe -ma lsass.exe`, and the `load kiwi` / `creds_all` commands in Meterpreter. Requires SYSTEM-level privileges and is a primary technique for harvesting credentials for lateral movement.

*   **SMB Exploitation and Lateral Movement**: Server Message Block (SMB) protocol is used for Windows file sharing and remote execution. Attackers exploit SMB for lateral movement using tools like `psexec`, `wmiexec`, or `smbexec` (all in the Impacket suite) to remotely execute commands on other hosts using valid credentials or captured hashes. The EternalBlue vulnerability (MS17-010) exploits an SMB buffer overflow and is one of the most well-known SMB exploits, used by WannaCry and NotPetya ransomware.

*   **Persistence Mechanisms**: Techniques attackers use to maintain access after a reboot or session termination. Windows persistence techniques include: registry run keys (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`), scheduled tasks (`schtasks`), Windows services, startup folder entries, and DLL hijacking in auto-run locations. Metasploit's `post/windows/manage/persistence` module automates this. PT0-002 tests testers' ability to recognize and document persistence artifacts during an engagement.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002**. Lateral movement and persistence are core post-exploitation skills tested alongside privilege escalation.
*   **Kerberoasting vs. AS-REP Roasting:** PT0-002 distinguishes these two Kerberos attacks. Kerberoasting requires valid credentials to request service tickets for SPN-registered accounts. AS-REP Roasting targets accounts with Kerberos pre-authentication disabled — no credentials needed. Know which attack works without initial access.
*   **Pass-the-Hash Works on NTLM, Not Kerberos:** PtH exploits the NTLM challenge-response protocol. It does not work against services that enforce Kerberos-only authentication. PT0-002 exam scenarios may describe a network requiring Kerberos — in that case, Pass-the-Ticket (PtT) is the correct lateral movement technique.
*   **Exam Trap — LSASS Dump Requires SYSTEM:** Mimikatz `sekurlsa::logonpasswords` requires SYSTEM or SeDebugPrivilege. A scenario where you have Administrator but not SYSTEM may fail — escalation to SYSTEM first is required.
*   **Lateral Movement Tools Tested:** Know these tool names and their purposes: `psexec` / `wmiexec` / `smbexec` (Impacket), Mimikatz (credential extraction), BloodHound (AD attack path visualization), `net use` / `net view` (native Windows SMB enumeration), and CrackMapExec (CME) for bulk credential spraying across SMB hosts.
*   **BloodHound / SharpHound:** BloodHound is an Active Directory attack path analysis tool that ingests Active Directory relationship data (collected by SharpHound) and graphically shows the shortest path from a compromised account to Domain Admin. PT0-002 expects you to know this tool exists and what it is used for.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Active Directory Basics," "Attacktive Directory," and "Lateral Movement and Pivoting" rooms provide guided, browser-based practice with Kerberoasting, PtH, and AD enumeration against realistic lab environments without requiring a local VM.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Post-Exploitation and Active Directory attack sections for content mapped directly to PT0-002 domain 3 lateral movement objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Active Directory and Lateral Movement rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — all labs run in the browser with no local VM required. The AD rooms walk through Kerberoasting, Pass-the-Hash, and BloodHound enumeration against realistic Windows domain environments.
*   **Required Video:** Watch the Active Directory attacks and Post-Exploitation segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the lateral movement and Active Directory content in domain 3.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Enumerate AD service accounts with SPNs: `GetUserSPNs.py` (Impacket)**: You will identify Active Directory accounts registered with Service Principal Names — these are the targets for Kerberoasting. You will request service tickets and save them in Hashcat-compatible format for offline cracking.
*   **Extract credentials from LSASS: `load kiwi` → `creds_all` in Meterpreter**: From an existing SYSTEM-level Meterpreter session, you will load the Kiwi (Mimikatz) module and dump all cached credentials — including NTLM hashes, Kerberos tickets, and any plaintext passwords cached in memory — documenting what access those credentials provide.
*   **Lateral movement via Pass-the-Hash**: You will use a captured NTLM hash to authenticate to a second target host using Impacket's `psexec.py` or Metasploit's `psexec` module, demonstrating that credential compromise on one host enables access to others without requiring the plaintext password.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Active Directory and Lateral Movement rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Post-Exploitation / Active Directory section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
