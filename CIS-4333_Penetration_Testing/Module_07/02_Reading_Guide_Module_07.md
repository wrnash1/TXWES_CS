# Reading Guide: Module 07 - Post-Exploitation – Privilege Escalation
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 07 - Post-Exploitation – Privilege Escalation**! Once initial access is gained, professional penetration testers move into the post-exploitation phase — working to expand their access, elevate privileges, and demonstrate the full business impact a real attacker could achieve. Privilege escalation is the process of moving from a low-privilege account (standard user) to a high-privilege account (administrator or root) using misconfigurations, vulnerabilities, or design flaws in the target system. This module maps to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**) and the **Post-Exploitation** activities within that domain.

Understanding privilege escalation is essential for providing accurate, impactful pentest findings — a finding that demonstrates full system compromise is far more compelling evidence than one that shows only limited access.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Metasploit Framework Console (`msfconsole`)**: The primary interface for the Metasploit Framework used throughout exploitation and post-exploitation phases. In post-exploitation, key Meterpreter commands include `getsystem` (automated privilege escalation), `getuid` (current user identity), `hashdump` (credential extraction), `migrate` (move into another process for stability), `upload`/`download` (file transfer), and `load kiwi` (load the Kiwi/Mimikatz module for credential harvesting).

*   **Search Exploits and Auxiliary Modules**: Post-exploitation in Metasploit uses `post/` modules to enumerate the compromised system, collect credentials, and pivot to other hosts. Examples: `post/windows/gather/hashdump`, `post/multi/recon/local_exploit_suggester` (suggests local privilege escalation exploits based on the target's OS version and patch level).

*   **Payloads and Privilege Escalation Paths**: On Windows, escalation paths include: token impersonation (Potato attacks, `getsystem`), unquoted service paths, weak service permissions, DLL hijacking, UAC bypass techniques, and kernel exploits. On Linux, escalation paths include: SUID/SGID binary abuse, writable cron jobs, sudo misconfigurations (`sudo -l`), world-writable files in root-owned scripts, and kernel exploits.

*   **Reverse Shell vs. Bind Shell in Post-Exploitation Context**: After escalating privileges, testers often migrate the existing session to a more stable, privileged process (e.g., `migrate` into `lsass.exe` or `explorer.exe` in Meterpreter) rather than opening new shells. Understanding shell stability and process injection is a post-exploitation skill tested on PT0-002.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002**. Post-exploitation and privilege escalation questions test knowledge of specific techniques, tools, and the sequence of actions after gaining initial access.
*   **Key Privilege Escalation Techniques Tested:** Windows: UAC bypass, unquoted service paths, token impersonation, DLL hijacking. Linux: SUID binary abuse (`find / -perm -4000`), sudo misconfigurations (`sudo -l`), writable cron jobs, PATH hijacking.
*   **Exam Trap — Enumeration Before Escalation:** PT0-002 tests that testers enumerate the system before attempting escalation — running `local_exploit_suggester` or manual enumeration scripts (LinPEAS, WinPEAS) identifies the best escalation path. Blindly running exploits wastes time and increases detection risk.
*   **LinPEAS / WinPEAS:** Automated privilege escalation enumeration scripts that run locally on the compromised host to identify misconfigured services, SUID binaries, writable paths, and other escalation vectors. PT0-002 expects testers to know these tools exist and what they do.
*   **`getsystem` in Meterpreter:** Attempts multiple Windows privilege escalation techniques automatically. If it fails, the tester should fall back to manual enumeration with `local_exploit_suggester`. Know that `getsystem` uses named pipe impersonation and token duplication techniques.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Windows Privilege Escalation" and "Linux Privilege Escalation" rooms provide hands-on practice with every major escalation technique in a guided, legal lab environment.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Post-Exploitation section for privilege escalation content mapped to PT0-002 domain 3.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Windows Privilege Escalation and Linux Privilege Escalation rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). These rooms provide systematic hands-on coverage of every major escalation technique with guided walkthroughs and real vulnerable targets.
*   **Required Video:** Watch the Post-Exploitation and Privilege Escalation segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). Use chapter markers to navigate to post-exploitation content in domain 3.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Launch Metasploit: `msfconsole`**: You will open an existing Meterpreter session on a lab target and use `getuid` to identify current privilege level, confirming you need to escalate before post-exploitation tasks can be fully performed.
*   **Search for a local privilege escalation exploit: `use post/multi/recon/local_exploit_suggester`**: You will run the local exploit suggester against your active session, analyze the output for viable escalation paths, and select the most appropriate module to test.
*   **Configure parameters and attempt privilege escalation**: You will apply the recommended escalation technique (e.g., `getsystem`, a specific token impersonation, or SUID binary exploit), verify the result with `getuid`, and document the access level achieved and the business impact this level of access represents.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Privilege Escalation rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Post-Exploitation section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
