# Reading Guide: Module 06 - Exploitation – Metasploit Framework
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 06 - Exploitation – Metasploit Framework**! This module covers the exploitation phase of penetration testing, where identified vulnerabilities are actively leveraged to gain unauthorized access to target systems in a controlled, authorized manner. The Metasploit Framework is the industry-standard exploitation platform and is explicitly tested on the CompTIA PenTest+ PT0-002 exam within the **Attacks and Exploits** domain (**30% of exam weight** — the largest domain).

Exploitation is only performed after proper authorization is confirmed and vulnerabilities have been identified through scanning. The goal is to demonstrate real-world impact to the client, not to cause harm.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Metasploit Framework Console (`msfconsole`)**: The primary command-line interface for the Metasploit Framework — an open-source exploitation platform maintained by Rapid7. `msfconsole` provides access to thousands of exploit modules, auxiliary modules, post-exploitation tools, and payload generators. Key commands include `search` (find modules), `use` (select a module), `show options` (display required parameters), `set` (configure parameters), `run`/`exploit` (execute), and `sessions` (manage active sessions).

*   **Exploit Modules and Search**: Metasploit exploit modules are pre-built attack packages that target specific CVEs or service vulnerabilities. The `search` command filters modules by name, CVE, platform, or type (e.g., `search type:exploit platform:windows cve:2017`). Each module has required options including `RHOSTS` (target), `RPORT` (target port), `LHOST` (attacker IP for reverse shells), and `LPORT` (listener port).

*   **Payloads**: The code that executes on the target after a successful exploit. Payload types in PT0-002: **Singles** (self-contained, small, no stager needed), **Stagers** (small initial payload that establishes a connection and downloads a larger stage), and **Stages** (the full-featured payload delivered by a stager — e.g., Meterpreter). The most commonly tested payload is `windows/meterpreter/reverse_tcp` — a staged, feature-rich post-exploitation shell.

*   **Reverse Shell vs. Bind Shell**: A **reverse shell** instructs the compromised target to initiate a TCP connection back to the attacker's listener — this bypasses inbound firewall rules on the target because the connection originates from inside. A **bind shell** opens a TCP listener port on the target and waits for the attacker to connect to it — this is blocked when the target has strict inbound firewall rules. PT0-002 tests when to use each type based on network topology.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002** — the largest single domain. Metasploit workflow, payload types, and shell types are core exam content.
*   **Metasploit Module Types Tested:** `exploit` (attack a vulnerability), `auxiliary` (scanning, fuzzing, brute force — no payload), `post` (post-exploitation actions on a session), `payload` (shellcode delivered after exploitation), `encoder` (obfuscates payloads), `nop` (no-operation sleds for buffer overflows).
*   **Exam Trap — Meterpreter vs. Shell:** Meterpreter is a staged, in-memory payload that provides an advanced post-exploitation interface. A basic shell payload gives a standard OS command prompt. PT0-002 tests the difference — Meterpreter is more capable (file upload/download, screenshot, hashdump, migrate) but more detectable.
*   **Exam Trap — LHOST vs. RHOSTS:** `LHOST` is the attacker's own IP address (used in reverse payloads for the target to call back to). `RHOSTS` is the target IP range. Confusing these is a common exam trap in scenario questions.
*   **`msfvenom`:** The standalone Metasploit payload generator. Used to create standalone exploit payloads (EXE, ELF, APK, shellcode) outside of `msfconsole`. PT0-002 expects you to know `msfvenom` generates payloads for client-side attacks.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Metasploit" room series provides hands-on guided practice with `msfconsole`, exploit selection, payload configuration, and Meterpreter post-exploitation against vulnerable lab machines in a legal environment.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Attacks and Exploits section for Metasploit workflow, payload types, and shell concepts mapped to PT0-002 domain 3.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Metasploit rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). These rooms guide you through real `msfconsole` sessions, exploit module configuration, payload selection, and Meterpreter usage with hands-on practice against vulnerable targets.
*   **Required Video:** Watch the Attacks and Exploits / Metasploit segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). Use chapter markers to navigate to PT0-002 domain 3 exploitation content.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Launch Metasploit: `msfconsole`**: You will start the Metasploit console, navigate the module hierarchy, and use `help` to explore available commands — building familiarity with the operational workflow before running any exploits.
*   **Search for an exploit matching a target service: `search vsftpd`**: You will use the `search` command to find exploit modules for a known vulnerable service, select the appropriate module with `use`, and inspect its required options with `show options`.
*   **Configure parameters and deploy a test reverse shell payload**: You will set `RHOSTS`, `LHOST`, `LPORT`, and payload options, then execute the exploit against a lab target, establish a reverse shell session, and interact with it — documenting what access was gained and what it would mean in a real engagement.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Metasploit rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Attacks and Exploits section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
