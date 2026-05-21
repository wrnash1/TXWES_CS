# Quiz: Module 06 - Exploitation – Metasploit Framework
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
In the Metasploit Framework, which payload type is entirely self-contained, requiring no stager, and executes immediately when delivered to the target?
*   A) Staged payload
*   B) Stager payload
*   C) Single (inline) payload
*   D) Meterpreter payload
*   **Correct Answer:** C) Single (inline) payload — self-contained shellcode that executes directly on the target without needing a second-stage connection.
*   **Distractor Analysis:**
    *   *Why correct:* A single (inline) payload is entirely self-contained. It includes all necessary shellcode in one package. No stager is needed to download additional components — it executes immediately upon delivery.
    *   *Why A is incorrect:* A staged payload is split into two parts: a small stager that connects back to the attacker to download the larger stage. It is the opposite of self-contained.
    *   *Why B is incorrect:* A stager is the small first-stage component of a staged payload — it establishes a connection and pulls down the second stage. It is not self-contained.
    *   *Why D is incorrect:* Meterpreter is a staged payload delivered as a second stage — it is powerful and feature-rich but requires a stager to load it into memory. It is not a single/inline payload type.

---

**Question 2**
In Metasploit, what is the purpose of the **`LHOST`** option when configuring a reverse shell exploit module?
*   A) The IP address of the target system that will be exploited.
*   B) The attacker's own IP address that the compromised target will connect back to when the reverse shell executes.
*   C) The local hostname of the Metasploit console machine used to identify it on the network.
*   D) The loopback address (127.0.0.1) used to test payload functionality before deployment.
*   **Correct Answer:** B) The attacker's own IP address that the compromised target will connect back to when the reverse shell executes.
*   **Distractor Analysis:**
    *   *Why B is correct:* In a reverse shell, the target initiates the TCP connection to the attacker. `LHOST` tells the payload embedded in the exploit where to call back — it must be set to the attacker's reachable IP address. Misconfiguring `LHOST` is one of the most common reasons a reverse shell fails.
    *   *Why A is incorrect:* The target IP is set with `RHOSTS` (Remote Hosts), not `LHOST`. Confusing these two is a PT0-002 exam trap.
    *   *Why C is incorrect:* Metasploit does not use a hostname field called LHOST for identification purposes — it is specifically the IP address the payload will connect to, not a name.
    *   *Why D is incorrect:* Setting LHOST to 127.0.0.1 would cause the payload to connect to itself on the target — not back to the attacker. This would cause the reverse shell to fail.

---

**Question 3**
A penetration tester is targeting a Windows host behind a firewall that blocks all inbound TCP connections but allows outbound traffic on port 443. Which Metasploit payload configuration is most likely to establish a successful shell?
*   A) `windows/shell/bind_tcp` — opens a listener on the target and waits for the attacker to connect inbound.
*   B) `windows/meterpreter/reverse_tcp` with LPORT set to 443 — target connects outbound to the attacker on a commonly allowed port.
*   C) `windows/shell_reverse_udp` — uses UDP which bypasses all TCP firewall rules.
*   D) `linux/x86/shell/reverse_tcp` — designed for Linux targets and compatible with Windows firewall bypass.
*   **Correct Answer:** B) `windows/meterpreter/reverse_tcp` with LPORT set to 443 — target connects outbound to the attacker on a commonly allowed port.
*   **Distractor Analysis:**
    *   *Why B is correct:* When inbound connections are blocked, a reverse shell is required. Using port 443 (HTTPS) for the callback is a common technique because outbound 443 is almost always permitted through corporate firewalls. The Windows Meterpreter reverse TCP payload is the correct choice for a Windows target.
    *   *Why A is incorrect:* A bind shell opens a listener on the target and requires the attacker to connect inbound — which is exactly what the firewall blocks in this scenario.
    *   *Why C is incorrect:* UDP reverse shells exist but are unreliable and rarely used in practice. More importantly, `windows/shell_reverse_udp` is not a standard Metasploit payload and UDP port 443 would still be subject to inspection. This is a distractor.
    *   *Why D is incorrect:* `linux/x86/shell/reverse_tcp` is a Linux payload. Running a Linux payload against a Windows target would produce a binary the Windows OS cannot execute.

---

**Question 4**
After successfully exploiting a target and opening a Meterpreter session, which Meterpreter command would a penetration tester use to extract password hashes from the Windows SAM database?
*   A) `getuid` — displays the current user identity on the compromised system.
*   B) `sysinfo` — retrieves operating system version and hostname information.
*   C) `hashdump` — extracts NTLM password hashes from the Windows SAM database for offline cracking.
*   D) `getsystem` — attempts to escalate privileges to SYSTEM level on the target.
*   **Correct Answer:** C) `hashdump` — extracts NTLM password hashes from the Windows SAM database for offline cracking.
*   **Distractor Analysis:**
    *   *Why C is correct:* The `hashdump` Meterpreter command reads the Windows SAM (Security Account Manager) registry hive and extracts stored NTLM password hashes. These hashes can then be cracked offline with Hashcat or John the Ripper, or used directly in Pass-the-Hash attacks.
    *   *Why A is incorrect:* `getuid` returns the username the Meterpreter session is running as — useful for privilege verification but does not extract password hashes.
    *   *Why B is incorrect:* `sysinfo` returns OS version, hostname, and architecture information — useful for reconnaissance but does not access credentials.
    *   *Why D is incorrect:* `getsystem` attempts privilege escalation (e.g., via token impersonation or named pipe impersonation) to reach SYSTEM level. This is a prerequisite step before `hashdump`, not the hash extraction command itself.

---

**Question 5**
A penetration tester uses `msfvenom` to generate a standalone payload file. Which scenario best describes the appropriate use of `msfvenom` versus `msfconsole` exploit modules?
*   A) `msfvenom` is used when the target is already compromised and the tester wants to establish a second persistent session.
*   B) `msfvenom` generates standalone payload files (EXE, ELF, APK, shellcode) for delivery via client-side attacks such as phishing, while `msfconsole` exploit modules directly attack network services.
*   C) `msfvenom` is the updated replacement for `msfconsole` and handles both payload generation and exploit execution.
*   D) `msfvenom` is only used for Android (APK) payload generation and has no use against Windows or Linux targets.
*   **Correct Answer:** B) `msfvenom` generates standalone payload files (EXE, ELF, APK, shellcode) for delivery via client-side attacks such as phishing, while `msfconsole` exploit modules directly attack network services.
*   **Distractor Analysis:**
    *   *Why B is correct:* `msfvenom` is a command-line tool that combines payload generation and encoding into a single utility. It produces files that can be delivered to targets via email, USB, or web download — enabling client-side attacks. It is distinct from `msfconsole` exploit modules, which actively attack listening network services.
    *   *Why A is incorrect:* Post-exploitation persistence in Metasploit is typically handled by `post/multi/manage/persistence` modules within an active Meterpreter session — not `msfvenom` as a standalone step.
    *   *Why C is incorrect:* `msfvenom` does not replace `msfconsole`. They serve complementary roles — `msfvenom` generates payloads, `msfconsole` manages the full framework including exploit modules, listeners, and session management.
    *   *Why D is incorrect:* `msfvenom` supports payload generation for Windows (EXE), Linux (ELF), macOS (DYLIB/MACHO), Android (APK), web shells (PHP, ASP, JSP), and raw shellcode — it is platform-agnostic.
