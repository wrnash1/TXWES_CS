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

---

## Question 11 (5 points)

A malware sample is submitted to a sandbox. The sandbox report shows the sample checks for the following before executing its payload: running process list for `vmware.exe` and `vboxservice.exe`, screen resolution below 1024x768, and system uptime under 2 minutes. If any condition is true, the sample exits without executing. What technique does this behavior represent?

- A) Privilege escalation
- B) Anti-sandbox / virtualization evasion (ATT&CK T1497)
- C) DLL hijacking
- D) Credential dumping

Correct Answer: B

Distractor Analysis:

- A is incorrect. Privilege escalation involves the malware gaining higher system permissions. Checking for virtualization indicators and exiting early is an evasion behavior, not a privilege gain behavior.
- B is correct. Checking for VMware/VirtualBox processes, unusually low screen resolution (common in sandbox VMs), and short uptime (indicating a freshly spun-up sandbox VM) are all classic sandbox detection evasion techniques documented as ATT&CK T1497 (Virtualization/Sandbox Evasion). The sample is trying to determine if it is being analyzed and terminating to avoid behavioral detection.
- C is incorrect. DLL hijacking involves placing a malicious DLL in a location where a legitimate application will load it ahead of the real DLL. It is a persistence/execution technique, not an evasion check.
- D is incorrect. Credential dumping involves extracting authentication credentials from OS memory or storage. It has no relationship to sandbox environment checks.

---

## Question 12 (5 points)

Which analysis type — static or dynamic — would most effectively reveal that a malware sample uses polymorphic code that changes its binary signature on every execution?

- A) Static analysis, because PE header analysis reveals encryption routines used to generate new signatures
- B) Dynamic analysis, because executing the sample in a controlled sandbox captures the runtime behavior regardless of how the binary signature changes between executions
- C) Static analysis using strings extraction, because the strings visible in the binary reveal the polymorphic engine's source code
- D) Neither — polymorphic malware cannot be analyzed using standard SOC analysis techniques

Correct Answer: B

Distractor Analysis:

- A is incorrect. While static PE analysis can sometimes identify encryption or packing stubs, polymorphic code is specifically designed to change its binary content and evade static signature-based detection. Relying on static analysis for polymorphic samples is unreliable.
- B is correct. Dynamic analysis executes the sample in a sandboxed environment and captures what it actually does — network connections, file writes, registry changes, process creation — regardless of how the binary mutates. The behavior remains consistent even as the static signature changes, making dynamic analysis the more effective approach for polymorphic samples.
- C is incorrect. Polymorphic malware's code changes are at the binary level. The strings extracted from one execution are not the engine source code and will differ between executions.
- D is incorrect. Both static and dynamic analysis have value even for polymorphic malware. Dynamic analysis is particularly effective precisely because it bypasses the signature-evasion mechanism.

---

## Question 13 (5 points)

A malware sample creates the Windows registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\UpdateService` pointing to `C:\Users\Public\svchost32.exe`. Which ATT&CK technique does this represent and what is its purpose?

- A) T1059.001 — PowerShell execution for lateral movement
- B) T1547.001 — Boot or Logon Autostart Execution via Registry Run Keys for persistence
- C) T1003.001 — OS Credential Dumping via LSASS memory
- D) T1078 — Valid Accounts for initial access

Correct Answer: B

Distractor Analysis:

- A is incorrect. T1059.001 describes using PowerShell as an execution vehicle. Creating a registry Run key is not a PowerShell execution technique — it is a persistence mechanism that survives reboots.
- B is correct. T1547.001 (Registry Run Keys / Startup Folder) is the canonical ATT&CK sub-technique for using `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` to execute a binary at user logon. This creates persistence so the malware runs every time the user logs in, which is the explicit purpose of this registry key location.
- C is incorrect. T1003.001 involves reading LSASS process memory to extract credential hashes. Registry key creation has no relationship to LSASS credential dumping.
- D is incorrect. T1078 (Valid Accounts) describes using legitimate credentials for initial access or persistence. Creating a registry key is a technical persistence mechanism, not a credential-based technique.

---

## Question 14 (5 points)

During static analysis of a suspected malware sample, an analyst uses a strings extraction tool and finds the string `cmd.exe /c net user administrator P@ssw0rd! /add`. What does the presence of this string indicate?

- A) The binary is a legitimate Microsoft administrative utility because it contains Windows command syntax
- B) The malware contains hardcoded commands to create a new Windows administrator account — likely for backdoor persistence
- C) The string is meaningless because static strings can be present in any binary for documentation purposes
- D) The binary is a Trojan horse masquerading as a calculator application

Correct Answer: B

Distractor Analysis:

- A is incorrect. Legitimate Microsoft utilities do not embed hardcoded `net user` account creation commands with specific passwords. The presence of this specific string in a suspicious binary is a red flag indicating malicious intent.
- B is correct. `net user administrator P@ssw0rd! /add` is the Windows command to create or modify the Administrator account. Finding this hardcoded in a malware sample indicates it is designed to create a privileged backdoor account — a persistence technique (ATT&CK T1136.001 — Create Local Account).
- C is incorrect. Strings found in malware during static analysis provide direct evidence of intended functionality. A string like a `net user` account creation command is not documentation — it is an operational capability embedded in the binary.
- D is incorrect. While Trojans do masquerade as legitimate software, the defining finding here is the backdoor account creation string. The malware's disguise (if any) is a separate characteristic from what this specific string reveals.

---

## Question 15 (5 points)

A SOC analyst is reviewing a VirusTotal report for a file hash submitted after a malware detection. The report shows 4 out of 72 antivirus engines flag the file as malicious. The majority (68 engines) return clean. How should the analyst interpret this result?

- A) 4 flagging engines confirms the file is definitively malicious and the system must be reimaged immediately
- B) 0 flagging engines would confirm the file is clean — 4 detections is a borderline result that requires additional investigation, including sandbox analysis and hash lookup in threat intelligence feeds
- C) A clean result from 68 engines is definitive proof the file is benign; the 4 flagging engines are false positives
- D) VirusTotal results should not be used for malware analysis and the analyst should close the investigation

Correct Answer: B

Distractor Analysis:

- A is incorrect. A 4/72 detection ratio alone is not sufficient to confirm malicious classification and trigger reimaging. The sample may be a low-prevalence or newly created malware not yet in most engines' databases, or it may be a false positive from the 4 engines. Additional analysis is required.
- B is correct. VirusTotal detection ratios require contextual interpretation. Low detection counts can indicate newly crafted or targeted malware that most engines have not yet encountered. The appropriate response is to enrich the finding with sandbox execution, behavioral analysis, and additional threat intelligence correlation before classifying definitively.
- C is incorrect. 68 clean results do not definitively prove benignity. Zero-day and custom malware regularly achieve 0/72 on VirusTotal because no engine has a signature for it yet. Clean results reduce suspicion but do not eliminate it.
- D is incorrect. VirusTotal is a widely used, legitimate threat intelligence platform. It is appropriate to use for malware investigation. Discarding it as a tool without basis is not professional SOC procedure.

---

## Question 16 (5 points)

Which of the following Windows API calls in a malware sample's Import Address Table (IAT) most strongly indicates the malware has credential dumping capability?

- A) `WriteFile` and `CreateFile`
- B) `OpenProcess` with access to LSASS combined with `ReadProcessMemory`
- C) `RegSetValueEx` and `RegCreateKeyEx`
- D) `InternetOpen` and `InternetConnect`

Correct Answer: B

Distractor Analysis:

- A is incorrect. `WriteFile` and `CreateFile` indicate the malware reads and writes files. This is common across many malware types (file droppers, ransomware) and is not specific to credential dumping.
- B is correct. Credential dumping from LSASS memory (ATT&CK T1003.001) requires opening a handle to the `lsass.exe` process using `OpenProcess` with PROCESS_VM_READ access, then extracting credential data using `ReadProcessMemory`. The combination of these two API calls in the IAT is a well-known credential dumping indicator.
- C is incorrect. `RegSetValueEx` and `RegCreateKeyEx` indicate registry write operations — associated with persistence mechanisms like Run key installation, not credential dumping.
- D is incorrect. `InternetOpen` and `InternetConnect` are WinInet API calls indicating the malware performs network communication — consistent with C2 beaconing or download functionality, not credential dumping.

---

## Question 17 (5 points)

A malware sample drops a DLL into `C:\Windows\System32\wbem\` with the same name as a legitimate Windows DLL. When a legitimate application loads the DLL, it loads the malicious version first due to DLL search order. Which technique does this represent?

- A) Process injection
- B) DLL search order hijacking (ATT&CK T1574.001)
- C) Reflective DLL loading
- D) AppLocker bypass via trusted publisher

Correct Answer: B

Distractor Analysis:

- A is incorrect. Process injection involves writing and executing code within another process's memory space. DLL search order hijacking places a malicious DLL on disk in a path that Windows searches before the legitimate DLL location.
- B is correct. Windows DLL load order follows a defined search path. DLL search order hijacking (T1574.001) places a malicious DLL in a location that Windows searches before the directory containing the legitimate DLL. When a legitimate application loads the DLL by name without a full path, it finds the malicious version first.
- C is incorrect. Reflective DLL loading injects a DLL directly into process memory without writing it to disk and without using the normal Windows DLL loader. This is an in-memory execution technique distinct from on-disk path manipulation.
- D is incorrect. AppLocker bypass via trusted publisher involves exploiting code signing trust to execute unsigned code. It does not involve DLL search path manipulation.

---

## Question 18 (5 points)

A malware analyst receives a sample that is a 64-bit Windows PE executable. Before submitting it to a sandbox, the analyst wants to quickly determine if it is packed without running it. Which static analysis approach best answers this question?

- A) Check the file's digital signature certificate to see if it is signed by a known publisher
- B) Examine the PE section entropy values — sections with entropy near 8.0 indicate packing
- C) Count the number of imported DLLs — packed samples import more DLLs than unpacked samples
- D) Check the file creation timestamp in the PE header — packed files always have creation timestamps after 2020

Correct Answer: B

Distractor Analysis:

- A is incorrect. Digital signatures indicate publisher identity and integrity, not packing status. Many malware samples are unsigned; some are even signed with stolen certificates. Signature presence or absence does not indicate packing.
- B is correct. Entropy analysis is the standard static method for detecting packed PE files. Normal code sections have entropy between 5.0 and 7.0. A section with entropy near 8.0 (maximum randomness) indicates compressed or encrypted content — the characteristic of a packed payload waiting to be decompressed at runtime.
- C is incorrect. Packed samples typically import very few DLLs because the actual imports are hidden inside the packed payload and resolved dynamically at runtime. Unpacked malware may import many DLLs. The relationship is inverse to what the option states.
- D is incorrect. PE header timestamps can be easily modified by the malware author and provide no reliable indication of packing. There is no time-based correlation between packing and creation date.

---

## Question 19 (5 points)

Which malware category is specifically designed to intercept and record keystrokes, screenshots, clipboard content, and browser credentials without the user's knowledge?

- A) Ransomware
- B) Rootkit
- C) Spyware / Keylogger
- D) Worm

Correct Answer: C

Distractor Analysis:

- A is incorrect. Ransomware encrypts files and demands payment for decryption keys. While some ransomware variants perform data exfiltration before encryption, credential and keystroke surveillance is not the defining ransomware capability.
- B is incorrect. A rootkit is designed to hide the presence of malware by modifying the operating system or firmware. Rootkits provide stealth capability and often accompany other malware types, but keystroke recording is not their defining function.
- C is correct. Spyware and keyloggers are explicitly designed for covert data collection — capturing keystrokes to harvest credentials, taking periodic screenshots, logging clipboard content, and extracting saved browser passwords. This category directly targets confidentiality through surveillance.
- D is incorrect. A worm is designed for self-replication and propagation across networks. Its defining characteristic is spreading, not surveillance or data collection.

---

## Question 20 (5 points)

A malware analyst observes that a sample creates a mutex named `Global\MutexForSingleInstance_v3` immediately upon execution. What is the purpose of this behavior?

- A) The mutex protects user files from being modified during the infection process
- B) The mutex prevents multiple instances of the malware from running simultaneously on the same host — a standard technique used to avoid detection from redundant process behavior
- C) The mutex establishes the C2 communication channel over a named pipe
- D) The mutex is used to escalate privileges to SYSTEM by exploiting mutex handle inheritance

Correct Answer: B

Distractor Analysis:

- A is incorrect. Mutexes in malware are not designed to protect files. File locking uses different Windows mechanisms. A malware-created mutex is a control structure, not a file protection mechanism.
- B is correct. Malware creates a uniquely named mutex at startup and checks for its existence on subsequent executions. If the mutex already exists, the new instance exits — ensuring only one copy of the malware runs at a time. This prevents redundant behavior that might trigger behavioral alerts and is a well-documented anti-analysis technique. The mutex name itself becomes a host-based IOC for detection.
- C is incorrect. Named pipes are a separate Windows inter-process communication mechanism. Mutexes are mutual exclusion objects — they coordinate access but do not transmit data or establish network channels.
- D is incorrect. Mutexes do not provide a privilege escalation mechanism. Privilege escalation requires exploiting specific vulnerabilities or abusing token/impersonation APIs — not mutex handle operations.
