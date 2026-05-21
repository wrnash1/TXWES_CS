# Quiz: Module 07 - Malware Analysis Fundamentals
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which technology monitors system files in real-time by comparing cryptographic hashes against a known-good baseline to detect unauthorized modifications?

*   A) Endpoint Detection and Response (EDR)
*   B) File Integrity Monitoring (FIM)
*   C) Antivirus signature scanning
*   D) Host-based firewall
*   **Correct Answer:** B) File Integrity Monitoring (FIM) compares cryptographic hashes of files against a baseline to detect unauthorized modifications.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* EDR provides broad behavioral monitoring across processes, network connections, and memory — it is not specifically designed for hash-baseline comparison of static files. FIM is the precise tool for detecting file tampering.
    *   *Why B is correct:* FIM tools (e.g., Tripwire, AIDE) store SHA-256 hashes of critical files at a known-good point in time and alert whenever a monitored file's hash changes — directly detecting malware-based file modifications, rootkit installations, and unauthorized configuration changes.
    *   *Why C is incorrect:* Antivirus signature scanning looks for known malware patterns within file content; it does not maintain a hash baseline of clean system files to detect arbitrary modifications.
    *   *Why D is incorrect:* A host-based firewall controls inbound and outbound network connections based on rules; it does not monitor file system integrity.

---

**Question 2**
In malware analysis, which of the following most accurately defines **static malware analysis**?

*   A) Executing a malware sample in an isolated virtual machine to observe its runtime behavior, network connections, and file system changes without risking production systems
*   B) Examining a malware sample without executing it — reviewing file headers, embedded strings, imported functions, and disassembled code to understand its capabilities safely
*   C) Monitoring endpoint process trees and memory allocations in real time using an EDR agent to detect living-off-the-land execution chains
*   D) Correlating malware-related alerts across multiple log sources in a SIEM to build a unified timeline of attacker activity
*   **Correct Answer:** B) Examining a malware sample without executing it — reviewing file headers, embedded strings, imported functions, and disassembled code to understand its capabilities safely.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Executing a sample in an isolated VM to observe runtime behavior describes dynamic malware analysis, not static analysis. The defining feature of static analysis is that the sample is never executed.
    *   *Why B is correct:* Static analysis inspects the malware artifact directly (PE headers, strings extracted with `strings`, import address table, disassembly output from tools like Ghidra or IDA) without running it. It is safe but may be defeated by packing or obfuscation that hides true functionality until runtime.
    *   *Why C is incorrect:* Monitoring process trees and memory allocations via an EDR agent describes behavioral EDR telemetry collection — a form of dynamic/live detection, not static malware analysis.
    *   *Why D is incorrect:* Correlating alerts across log sources in a SIEM describes incident investigation and correlation, not malware analysis methodology.

---

**Question 3**
A malware analyst receives a suspicious executable and needs to observe exactly what registry keys it creates, what network connections it initiates, and what files it drops — without risking infection of any production system. Which approach is most appropriate?

*   A) Run a hash lookup of the executable against VirusTotal to check if any antivirus engine has detected it previously
*   B) Open the executable in a text editor and search for embedded IP addresses and domain strings manually
*   C) Execute the sample in an isolated sandbox environment that records process activity, network traffic, file system changes, and API calls during runtime
*   D) Forward the executable to the SIEM as an attachment so the correlation engine can analyze its content against threat intelligence feeds
*   **Correct Answer:** C) Execute the sample in an isolated sandbox environment that records process activity, network traffic, file system changes, and API calls during runtime.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A VirusTotal hash lookup reveals whether the sample is already known to antivirus engines, but it does not reveal runtime behavior such as registry keys created, files dropped, or C2 connections initiated by a novel or slightly modified sample.
    *   *Why B is incorrect:* Searching a binary in a text editor may surface some readable strings but is an incomplete static technique; it cannot reveal obfuscated or encrypted configuration data that is only resolved at runtime.
    *   *Why C is correct:* Sandbox analysis (tools like Cuckoo, Any.run, Joe Sandbox) executes the malware in a fully instrumented, isolated VM and captures all runtime behavior. This produces the richest IOC set — C2 IPs, domains, registry persistence keys, dropped file hashes, mutex names — without any risk to production systems.
    *   *Why D is incorrect:* SIEMs analyze log data and structured events; they cannot execute binary files or perform behavioral analysis of malware samples.

---

**Question 4**
A SOC analyst examines a malware report and finds the sample creates a scheduled task named `WindowsUpdate` that executes a PowerShell script from `%APPDATA%` every 15 minutes, even after a reboot. Which malware capability does this behavior demonstrate?

*   A) Lateral movement — the malware is propagating across the network to other hosts using stolen credentials
*   B) Data exfiltration — the malware is encoding and transmitting sensitive files to an external server via HTTP POST
*   C) Persistence — the malware is establishing a mechanism to survive system reboots and maintain long-term access to the compromised host
*   D) Privilege escalation — the malware is exploiting a vulnerability to gain SYSTEM-level privileges from a standard user account
*   **Correct Answer:** C) Persistence — the malware is establishing a mechanism to survive system reboots and maintain long-term access to the compromised host.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Lateral movement involves the attacker moving between hosts on the network using techniques such as pass-the-hash or RDP; a scheduled task on a single host is not lateral movement.
    *   *Why B is incorrect:* Data exfiltration describes outbound transmission of sensitive data to attacker-controlled infrastructure; creating a scheduled task is a persistence action, not an exfiltration action.
    *   *Why C is correct:* Persistence mechanisms ensure malware continues running after interruptions such as reboots or user logoffs. Scheduled tasks (MITRE ATT&CK T1053.005), registry run keys, and service installations are the most common Windows persistence techniques tested on CySA+.
    *   *Why D is incorrect:* Privilege escalation involves gaining elevated permissions; the described behavior (scheduled task execution) runs in whatever context it was configured, and the question does not describe any privilege elevation event.

---

**Question 5**
An organization wants to detect malware that attempts to establish persistence by modifying critical Windows registry run keys. Which two controls together best implement this detection capability?

*   A) Deploy full-disk encryption on all endpoints and require BitLocker PIN entry at startup to prevent unauthorized boot access
*   B) Deploy a FIM solution that monitors the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` registry key for changes, and forward FIM alerts to the SIEM for correlation with other endpoint events
*   C) Enforce a password complexity policy requiring 16-character passwords and disable password reuse for the last 24 passwords
*   D) Configure network-layer ACLs on the perimeter firewall to block outbound connections on non-standard ports above 1024
*   **Correct Answer:** B) Deploy a FIM solution that monitors the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` registry key for changes, and forward FIM alerts to the SIEM for correlation with other endpoint events.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full-disk encryption and BitLocker PIN protect against physical theft of a powered-off device; they do not detect or alert on runtime registry modifications made by malware on a running system.
    *   *Why B is correct:* Registry-based persistence (adding entries to Run or RunOnce keys) is one of the most common malware techniques. FIM configured to watch these registry paths will alert when any unauthorized modification occurs, and routing those alerts to the SIEM enables correlation with process creation events or network connections happening at the same time — providing full investigative context.
    *   *Why C is incorrect:* Password complexity policies address credential security; they have no effect on detecting registry modifications made by malware already executing on the system.
    *   *Why D is incorrect:* Perimeter firewall ACLs on outbound ports may limit C2 communication but do not detect or alert on registry key modifications occurring on the endpoint itself.
