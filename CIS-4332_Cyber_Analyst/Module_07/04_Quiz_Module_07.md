# Quiz: Module 07 - Malware Analysis Fundamentals

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer.

---

## Question 1

Which technology monitors system files in real-time by comparing cryptographic hashes against a known-good baseline to detect unauthorized modifications?

- A) Endpoint Detection and Response (EDR)
- B) File Integrity Monitoring (FIM)
- C) Antivirus signature scanning
- D) Host-based firewall

Correct Answer: B

Distractor Analysis:

- A is incorrect. EDR provides broad behavioral monitoring across processes, network connections, and memory. It is not specifically designed for hash-baseline comparison of static files. FIM is the precise tool for detecting file tampering.
- B is correct. FIM tools store SHA-256 hashes of critical files at a known-good point in time and alert whenever a monitored file's hash changes — directly detecting malware-based file modifications, rootkit installations, and unauthorized configuration changes.
- C is incorrect. Antivirus signature scanning looks for known malware patterns within file content. It does not maintain a hash baseline of clean system files to detect arbitrary modifications.
- D is incorrect. A host-based firewall controls inbound and outbound network connections based on rules. It does not monitor file system integrity.

---

## Question 2

In malware analysis, which of the following most accurately defines static malware analysis?

- A) Executing a malware sample in an isolated virtual machine to observe its runtime behavior, network connections, and file system changes without risking production systems
- B) Examining a malware sample without executing it — reviewing file headers, embedded strings, imported functions, and disassembled code to understand its capabilities safely
- C) Monitoring endpoint process trees and memory allocations in real time using an EDR agent to detect living-off-the-land execution chains
- D) Correlating malware-related alerts across multiple log sources in a SIEM to build a unified timeline of attacker activity

Correct Answer: B

Distractor Analysis:

- A is incorrect. Executing a sample in an isolated VM to observe runtime behavior describes dynamic malware analysis, not static analysis. The defining feature of static analysis is that the sample is never executed.
- B is correct. Static analysis inspects the malware artifact directly — PE headers, strings extracted with the strings utility, import address table, disassembly output — without running it. It is safe but may be defeated by packing or obfuscation that hides true functionality until runtime.
- C is incorrect. Monitoring process trees and memory allocations via an EDR agent describes behavioral EDR telemetry collection, which is a form of dynamic detection, not static malware analysis.
- D is incorrect. Correlating alerts across log sources in a SIEM describes incident investigation and log correlation, not malware analysis methodology.

---

## Question 3

A malware analyst receives a suspicious executable and needs to observe exactly what registry keys it creates, what network connections it initiates, and what files it drops — without risking infection of any production system. Which approach is most appropriate?

- A) Run a hash lookup of the executable against a threat intelligence database to check if any antivirus engine has detected it previously
- B) Open the executable in a text editor and search for embedded IP addresses and domain strings manually
- C) Execute the sample in an isolated sandbox environment that records process activity, network traffic, file system changes, and API calls during runtime
- D) Forward the executable to the SIEM as an attachment so the correlation engine can analyze its content against threat intelligence feeds

Correct Answer: C

Distractor Analysis:

- A is incorrect. A hash lookup reveals whether the sample is already known to antivirus engines but does not reveal runtime behavior such as registry keys created, files dropped, or C2 connections initiated by a novel or slightly modified sample.
- B is incorrect. Searching a binary in a text editor may surface some readable strings but is an incomplete static technique. It cannot reveal obfuscated or encrypted configuration data that is only resolved at runtime.
- C is correct. Sandbox analysis executes the malware in a fully instrumented, isolated VM and captures all runtime behavior. This produces the richest IOC set — C2 IPs, domains, registry persistence keys, dropped file hashes, mutex names — without any risk to production systems.
- D is incorrect. SIEMs analyze log data and structured events. They cannot execute binary files or perform behavioral analysis of malware samples.

---

## Question 4

A SOC analyst examines a malware report and finds the sample creates a scheduled task named `WindowsUpdate` that executes a PowerShell script from `%APPDATA%` every 15 minutes, even after a reboot. Which malware capability does this behavior demonstrate?

- A) Lateral movement — the malware is propagating across the network to other hosts using stolen credentials
- B) Data exfiltration — the malware is encoding and transmitting sensitive files to an external server via HTTP POST
- C) Persistence — the malware is establishing a mechanism to survive system reboots and maintain long-term access to the compromised host
- D) Privilege escalation — the malware is exploiting a vulnerability to gain SYSTEM-level privileges from a standard user account

Correct Answer: C

Distractor Analysis:

- A is incorrect. Lateral movement involves the attacker moving between hosts on the network using techniques such as pass-the-hash or RDP. A scheduled task on a single host is not lateral movement.
- B is incorrect. Data exfiltration describes outbound transmission of sensitive data to attacker-controlled infrastructure. Creating a scheduled task is a persistence action, not an exfiltration action.
- C is correct. Persistence mechanisms ensure malware continues running after interruptions such as reboots or user logoffs. Scheduled tasks (T1053.005), registry run keys, and service installations are the most common Windows persistence techniques tested on CySA+.
- D is incorrect. Privilege escalation involves gaining elevated permissions. The described behavior runs in whatever context it was configured and does not describe any privilege elevation event.

---

## Question 5

An organization wants to detect malware that attempts to establish persistence by modifying critical Windows registry run keys. Which control best implements this detection capability?

- A) Deploy full-disk encryption on all endpoints and require BitLocker PIN entry at startup to prevent unauthorized boot access
- B) Deploy a FIM solution that monitors the HKLM Run registry key for changes and forward FIM alerts to the SIEM for correlation with other endpoint events
- C) Enforce a password complexity policy requiring 16-character passwords and disable password reuse for the last 24 passwords
- D) Configure network-layer ACLs on the perimeter firewall to block outbound connections on non-standard ports above 1024

Correct Answer: B

Distractor Analysis:

- A is incorrect. Full-disk encryption and BitLocker PIN protect against physical theft of a powered-off device. They do not detect or alert on runtime registry modifications made by malware on a running system.
- B is correct. Registry-based persistence is one of the most common malware techniques. FIM configured to watch Run key paths will alert when any unauthorized modification occurs. Routing those alerts to the SIEM enables correlation with process creation events or network connections happening at the same time, providing full investigative context.
- C is incorrect. Password complexity policies address credential security. They have no effect on detecting registry modifications made by malware already executing on the system.
- D is incorrect. Perimeter firewall ACLs on outbound ports may limit C2 communication but do not detect or alert on registry key modifications occurring on the endpoint itself.

---

## Question 6

A sandbox report shows that a malware sample's PE Import Address Table includes the following functions: CreateRemoteThread, VirtualAllocEx, WriteProcessMemory, and OpenProcess. What capability does this import profile most strongly indicate?

- A) The malware is a keylogger designed to capture credentials by hooking keyboard input before it reaches the application layer
- B) The malware has process injection capabilities — it can allocate memory in and inject code into another running process
- C) The malware is a worm that uses network scanning functions to identify and spread to other vulnerable hosts
- D) The malware contains ransomware functionality and will use these functions to enumerate and encrypt files on the local file system

Correct Answer: B

Distractor Analysis:

- A is incorrect. Keyloggers typically import SetWindowsHookEx and related hook functions. The import profile described — CreateRemoteThread, VirtualAllocEx, WriteProcessMemory, OpenProcess — is the classic process injection API set, not a keylogging profile.
- B is correct. This import combination is the textbook process injection toolkit: OpenProcess to get a handle to the target process, VirtualAllocEx to allocate memory in the target process's address space, WriteProcessMemory to write the payload into that memory, and CreateRemoteThread to execute it. This maps to ATT&CK T1055.
- C is incorrect. Network scanning and propagation would use socket functions such as WSAStartup, connect, send, recv, and gethostbyname. The described imports are memory manipulation functions, not network functions.
- D is incorrect. Ransomware file enumeration and encryption typically imports FindFirstFile, FindNextFile, CryptEncrypt, or CryptGenRandom. The described imports are process memory manipulation functions.

---

## Question 7

A malware sample executing in a sandbox queries a known virtualization registry path and checks the total physical memory of the system at the start of execution. Which malware behavior do these actions represent?

- A) Credential access — the malware is checking registry locations where Windows stores cached authentication tokens
- B) Persistence establishment — the malware is searching for registry locations where it can store its configuration data for survival across reboots
- C) Sandbox evasion — the malware is checking for environment indicators that suggest it is executing in a virtualized analysis environment rather than a real endpoint
- D) Lateral movement preparation — the malware is enumerating installed software to identify targets for exploitation on the local network

Correct Answer: C

Distractor Analysis:

- A is incorrect. Cached authentication tokens are not stored in virtualization registry paths. Credential access techniques target LSASS memory (T1003.001) or the SAM registry hive.
- B is incorrect. Configuration storage persistence typically uses HKCU or HKLM software paths with the malware's own key names. Checking virtualization registry keys serves no persistence purpose.
- C is correct. Checking for virtualization registry entries and querying physical memory are classic sandbox evasion checks. If the sandbox exposes these artifacts or returns memory values below real-system thresholds, the malware can detect it is under analysis and execute benign behavior, defeating the sandbox. This maps to ATT&CK T1497 (Virtualization/Sandbox Evasion).
- D is incorrect. Lateral movement preparation involves network enumeration using functions like NetShareEnum or credential-gathering operations. Checking virtualization registry keys has no relationship to identifying network targets.

---

## Question 8

Which malware category is specifically designed to capture keystrokes, take screenshots, and record audio or video from the infected endpoint — with the primary objective of silently collecting sensitive information without disrupting normal system operations?

- A) Ransomware
- B) Worm
- C) Rootkit
- D) Spyware

Correct Answer: D

Distractor Analysis:

- A is incorrect. Ransomware's primary objective is encrypting files and demanding payment (T1486). While ransomware may perform some reconnaissance before encryption, it is definitively disruptive — the victim knows their files are encrypted.
- B is incorrect. A worm's defining characteristic is autonomous self-replication and spread across networks without user interaction. Worms may carry payloads but their classification is based on propagation behavior, not silent data collection.
- C is incorrect. A rootkit's primary purpose is hiding its own presence and the presence of other malware by operating at or below the OS level (T1014). Rootkits are an evasion and stealth capability, not primarily a data collection tool.
- D is correct. Spyware is designed for silent, long-duration intelligence collection — keylogging (T1056.001), screenshots (T1113), audio capture (T1123), and file collection — without alerting the victim. The defining characteristic is stealth and data collection as the primary objective.

---

## Question 9

An analyst performing static analysis on a suspicious executable observes that one of the PE sections has an entropy value of 7.94 out of a maximum of 8.0. What does this finding most likely indicate?

- A) The executable is a legitimate signed Microsoft binary — high entropy indicates strong digital signature validation
- B) The executable contains packed or encrypted code, indicating a packer was likely used to hide the malicious payload from signature-based scanning
- C) The executable is a compressed archive file misidentified as an executable, explaining the high entropy
- D) The high entropy value indicates the executable has been modified by a FIM-protected file integrity violation

Correct Answer: B

Distractor Analysis:

- A is incorrect. Digital signatures do not affect section entropy. Microsoft signed binaries have typical entropy values reflecting their normal code distribution. High entropy in a section is a packing indicator, not a signature indicator.
- B is correct. Entropy measures the randomness of data in a file section. Legitimate executable code has predictable entropy patterns. A section with entropy near 8.0 indicates the data is maximally random — characteristic of compressed or encrypted content. Malware packers compress and encrypt the payload, which is only decrypted at runtime, defeating static analysis. This is a standard indicator checked during PE header analysis.
- C is incorrect. While archive files do have high entropy, the question specifies a PE section (part of an executable's internal structure), not the file type itself.
- D is incorrect. FIM detects changes to file hashes. It does not report on or affect entropy values within a file's PE sections.

---

## Question 10

A sandbox report for a malware sample shows it initiates a TCP connection to an external IP address every 60 seconds with identical packet sizes and timing throughout the analysis period. Which malware behavior does this pattern most directly represent?

- A) Data exfiltration — the malware is transmitting collected files to attacker-controlled infrastructure in regular batches
- B) Lateral movement — the malware is scanning adjacent hosts on the local subnet on a regular schedule
- C) C2 beaconing — the malware is maintaining a persistent connection to its command and control server by sending regular check-in signals at a consistent interval
- D) DDoS participation — the malware is part of a botnet performing a distributed denial of service attack against the destination IP

Correct Answer: C

Distractor Analysis:

- A is incorrect. Data exfiltration generates variable-size transmissions corresponding to file sizes and does not typically produce identical packet sizes at regular intervals. The consistent interval and identical size pattern is characteristic of beaconing, not bulk data transfer.
- B is incorrect. Lateral movement involves connections to multiple different destination IPs (other hosts on the subnet) to identify targets. Repeated identical connections to a single external IP are not a lateral movement scan pattern.
- C is correct. C2 beaconing is a well-documented behavioral indicator where compromised malware contacts its C2 server at regular intervals to check for new commands and confirm availability. Consistent timing intervals and uniform packet sizes are the defining characteristics of beaconing behavior, mapped to ATT&CK T1071 (Application Layer Protocol).
- D is incorrect. DDoS participation generates very high-volume traffic to a single target at maximum throughput, not regular low-frequency check-in messages. The pattern described — regular 60-second intervals — is far too infrequent for a denial-of-service contribution.
