# Quiz: Module 15 — Advanced Threat Hunting

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Instructions

Select the best answer for each question. Distractor analysis is provided after each question to support exam preparation.

---

## Question 1

A senior analyst proposes starting a threat hunt with the goal of "looking for unusual activity." A junior analyst suggests instead that the hunt should be structured around the hypothesis: "Based on a CISA advisory indicating active exploitation of CVE-2024-1234 in VPN appliances, we hypothesize that if our perimeter VPN has been compromised, we will observe PowerShell or bash process creation by the VPN management daemon within the past 14 days." Which statement best explains why the junior analyst's approach is superior?

- A) The junior analyst's approach is more interesting and will keep the team engaged
- B) The specific hypothesis defines clear success and failure criteria, targets a specific data source and indicator, and is tied to credible intelligence — making the hunt efficient and repeatable
- C) "Looking for unusual activity" always produces too many results, causing alert fatigue
- D) Hypotheses must always be based on CVE publications; other intelligence sources are not valid for hunting

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Analyst engagement is not a methodology criterion. The quality of a hypothesis is measured by its precision, testability, and evidence basis — not its entertainment value. Why B is correct: A strong hunting hypothesis defines exactly what evidence would confirm or refute it, what data source to query, and what time range to cover. This enables efficient investigation, clear documentation of findings, and a repeatable playbook. "Looking for unusual activity" produces undefined scope, no success criteria, and no reproducible methodology. Why C is incorrect: While broad searches can produce noise, the problem with "unusual activity" is not result volume — it is that there is no defined indicator to search for and no criteria for what "unusual" means. Why D is incorrect: Threat intelligence for hunting hypotheses can come from CISA advisories, commercial threat feeds, ISAC reports, peer organizations, vendor advisories, internal anomaly data, and analyst intuition. CVE publications are one valid source among many.

---

## Question 2

A threat hunter reviewing endpoint telemetry finds the following process creation event: ParentProcess = `winword.exe`, ChildProcess = `powershell.exe`, CommandLine = `powershell.exe -nop -w hidden -enc JABjAGwAaQBlAG4AdA...`. Which MITRE ATT&CK technique does this most directly represent, and why is this pattern significant?

- A) T1566.001 (Spearphishing Attachment) — the Word document is a phishing artifact
- B) T1059.001 (PowerShell) with parent process anomaly indicating macro execution — a Word document launched encoded PowerShell, consistent with macro-based initial access
- C) T1055 (Process Injection) — the PowerShell process has been injected into winword.exe
- D) T1078 (Valid Accounts) — the use of PowerShell indicates credential-based access

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: T1566.001 describes the delivery mechanism (a spearphishing email with a malicious attachment). While the Word document may have been delivered via spearphishing, the telemetry record described shows the execution stage, not the delivery stage. Why B is correct: T1059.001 (Command and Scripting Interpreter: PowerShell) covers the execution of PowerShell as a malicious tool. The parent process anomaly — `winword.exe` spawning `powershell.exe` — is the classic indicator of a malicious macro executing a PowerShell payload. The `-enc` argument indicates base64 obfuscation (T1027 Obfuscated Files or Information), and `-nop -w hidden` are stealth flags. This combination is a high-confidence macro execution indicator. Why C is incorrect: Process injection (T1055) involves injecting code into an existing process's memory space. The process creation event shows a new child process being created — this is process spawning, not injection. Why D is incorrect: T1078 describes attackers using legitimate stolen credentials. The described event is a code execution event from a document, with no credential involvement indicated.

---

## Question 3

A threat hunter analyzes DNS query logs and observes that a single internal workstation has made 847 DNS queries to unique subdomains under the parent domain `updates-service-cdn.net` in a 6-hour window. Each subdomain is a 32-character hexadecimal string. No responses returned valid IP addresses (all NXDOMAIN). Which threat technique does this pattern most strongly indicate, and which MITRE ATT&CK technique ID applies?

- A) T1566.002 (Spearphishing Link) — the workstation is resolving links from a phishing email
- B) T1071.004 (Application Layer Protocol: DNS) for DNS tunneling — the high query volume with encoded subdomains indicates data exfiltration via DNS
- C) T1568.002 (Dynamic Resolution: Domain Generation Algorithms) — the workstation is infected with malware using DGA to locate its C2 server, and the NXDOMAIN responses indicate the C2 domain has not yet been registered
- D) T1190 (Exploit Public-Facing Application) — the DNS queries indicate a web application is being exploited

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Spearphishing links resolve to specific attacker-controlled domains, not hundreds of unique NXDOMAIN subdomains. A phishing link would produce a small number of DNS queries to specific domains, not 847 queries to random hex subdomains. Why B is incorrect: DNS tunneling (T1071.004) does produce high query volumes with encoded subdomain data, but tunneling requires successful DNS resolution to function — the C2 server must receive and respond to the queries. NXDOMAIN for all queries means no server is answering, making exfiltration via this channel impossible. Why C is correct: DGA malware generates pseudo-random domain names to locate its C2 server. The malware queries these domains in sequence until one resolves successfully. High volumes of NXDOMAIN responses are the defining characteristic of DGA activity in pre-registration or disrupted phases — the C2 infrastructure has been taken down or not yet brought online. The 32-character hex subdomain pattern is consistent with a DGA algorithm. This is a high-confidence DGA indicator. Why D is incorrect: Exploitation of public-facing applications involves inbound attack traffic targeting a server, not outbound DNS queries from an internal workstation. The traffic direction and protocol are inconsistent with this technique.

---

## Question 4

An EDR platform captures the following sequence on a single host over 8 minutes: (1) `excel.exe` spawns `powershell.exe` with a base64 argument, (2) PowerShell makes an outbound HTTPS connection to `185.44.33.121:443`, (3) PowerShell spawns `cmd.exe` with arguments `whoami /all`, (4) `cmd.exe` spawns `net.exe group "Domain Admins" /domain`, (5) `cmd.exe` spawns `net.exe view /domain`. What stage of the ATT&CK kill chain does the sequence of events 3 through 5 represent?

- A) Initial Access — the attacker is establishing the initial foothold
- B) Persistence — the attacker is creating mechanisms to maintain access
- C) Discovery — the attacker is gathering information about the environment and domain structure
- D) Lateral Movement — the attacker is moving to other systems

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Initial Access (in ATT&CK terms) describes how the attacker first gained entry to the environment. That stage is represented by step 1 (the Excel macro). Events 3–5 occur after access is established. Why B is incorrect: Persistence involves creating mechanisms to maintain access after a restart or credential change (scheduled tasks, registry run keys, new user accounts). Querying user groups and network resources with built-in commands does not create persistence. Why C is correct: Events 3–5 are all Discovery techniques. `whoami /all` (T1033 — System Owner/User Discovery), `net group "Domain Admins"` (T1069.002 — Permission Groups Discovery: Domain Groups), and `net view /domain` (T1018 — Remote System Discovery) are textbook Discovery commands. Attackers run these immediately after establishing initial access to understand the environment they have landed in. Why D is incorrect: Lateral Movement involves actually moving to and executing code on other systems. The commands shown are information gathering, not execution on other hosts.

---

## Question 5

A threat hunter wants to detect beaconing behavior in network telemetry. They extract all outbound connections from internal hosts to external IPs, grouped by source-destination pair, and compute statistics on the inter-connection intervals. Which statistical characteristic most strongly indicates beaconing rather than normal user-driven traffic?

- A) A high mean interval time (connections spaced more than an hour apart on average)
- B) A low standard deviation relative to the mean interval (consistent, regular timing)
- C) A high total byte count (large amounts of data transferred)
- D) A high connection count (many individual connections in a short period)

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Long mean intervals might indicate infrequent C2 check-in but are also consistent with cron jobs, scheduled backups, software update checks, and many other legitimate automated processes. Mean interval alone is not a reliable beaconing indicator. Why B is correct: Beaconing is defined by regularity — C2 frameworks check in on a configured interval, optionally with jitter. The statistical signature of beaconing is a low coefficient of variation (standard deviation divided by mean). Human-driven traffic (browsing, email) has high variability in connection timing because humans are unpredictable. Automated C2 beaconing has low variability. A connection that fires every 60 seconds ±2 seconds across 72 hours is almost certainly automated, not human. Why C is incorrect: High byte counts indicate data transfer but could represent legitimate streaming, backup operations, or cloud sync. High bytes alone do not indicate beaconing; they might indicate exfiltration, which is a related but different hunt. Why D is incorrect: High connection counts could indicate beaconing but could equally indicate a chatty legitimate application, a streaming service, or a software update in progress. The defining characteristic of beaconing is the consistency of timing, not the volume of connections.

---

## Question 6

During a threat hunt, an analyst identifies a confirmed Cobalt Strike beacon running inside a `svchost.exe` process. The hunt has confirmed initial access, C2 establishment, and discovery. No lateral movement or exfiltration evidence has been found yet. What is the most appropriate immediate action?

- A) Continue the hunt to find exfiltration evidence before notifying anyone, so the IR team has a complete picture
- B) Escalate immediately to the IR team with the confirmed findings while documenting all evidence collected so far
- C) Isolate the affected host at the network level without notifying the IR team, to contain the threat immediately
- D) Wait 24 hours to confirm the beacon persists across a reboot before escalating, to avoid false positives

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Waiting to find exfiltration evidence before escalating allows an active threat actor to continue operating — including completing exfiltration. Confirmed C2 presence is a high-severity confirmed incident that triggers immediate escalation. The IR team does not need a complete picture before being engaged; they are designed to work with partial information. Why B is correct: A confirmed Cobalt Strike beacon represents an active, in-progress compromise. The correct action is immediate escalation to the IR team with all evidence collected to date, while preserving and documenting the evidence. The hunting analyst's job is to find and hand off; the IR team's job is to respond. Delaying escalation to collect more evidence is a judgment call that should never be made unilaterally by a Tier 1 or 2 analyst. Why C is incorrect: Isolating a host without notifying the IR team denies the IR team control over the response. Host isolation may also destroy volatile evidence (RAM contents, active connections) before the IR team can decide whether to preserve it. Containment decisions must involve the IR team. Why D is incorrect: Waiting 24 hours with a confirmed active C2 beacon is indefensible. The attacker is operating right now. The standard for escalation is a confirmed threat, not a threat confirmed across multiple reboots.

---

## Question 7

A threat hunter uses the MITRE ATT&CK Navigator to map their organization's current detection coverage. Techniques shown in green are currently detectable by automated SIEM or EDR rules. The hunter notices that T1547.001 (Boot or Logon Autostart Execution: Registry Run Keys) is marked red (no coverage). Which data source would provide the best telemetry for detecting this technique?

- A) Network flow data showing outbound connections to known malicious IPs
- B) DNS query logs showing resolution of DGA-generated domains
- C) Windows Registry modification events captured by EDR, specifically for `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and related keys
- D) HTTP proxy logs showing downloads of executable files

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Network flow data provides visibility into network-level indicators. Registry run key creation is a disk/system event, not a network event. Network data would not capture registry modifications. Why B is incorrect: DNS query logs provide visibility into domain resolution activity. Registry persistence creation does not generate DNS queries. Why C is correct: T1547.001 describes persistence achieved by writing to Windows registry autostart keys. The only data source that captures registry write events is endpoint telemetry from an EDR agent that monitors registry modifications. The specific keys to monitor are `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`, and related `RunOnce` variants. This is the precise data source specified in the ATT&CK technique's Detection guidance. Why D is incorrect: HTTP proxy logs show file download activity. While an attacker might download a malicious executable before writing its persistence key, the registry write event itself is not captured in proxy logs.

---

## Question 8

A threat hunting team documents their hunts in a shared repository. After completing a hunt that found no evidence of the hypothesized attacker technique, a junior analyst suggests not documenting the negative result. "Nothing happened, so there is nothing to write up." What is wrong with this reasoning?

- A) The junior analyst is correct — documenting negative results wastes time and clutters the repository
- B) Negative hunt results confirm the hypothesis was tested, establish an environmental baseline, prevent redundant future hunts, and provide evidence of proactive security activity for auditors
- C) Negative results must be reported to management as security incidents, even if nothing was found
- D) All hunt documentation is optional and is only required when findings are escalated to the IR team

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Negative results have significant documentation value. Without them, the team cannot demonstrate coverage, cannot prevent the same hunt from being repeated, and cannot track what has been ruled out over time. Why B is correct: A documented negative result serves four purposes. First, it confirms the hypothesis was tested — providing a basis for confidence that the specific technique was absent in the searched data. Second, it establishes a baseline — the telemetry looked normal on this date, providing a reference point. Third, it prevents wasted effort — a repository of negative results prevents analysts from conducting the same hunt repeatedly. Fourth, it provides audit evidence that the security team is proactively hunting, which is increasingly required in compliance frameworks. Why C is incorrect: Negative hunt results are internal documentation, not incident reports. They do not indicate a security event occurred and should not be escalated as incidents. Why D is incorrect: Hunt documentation is not optional. A hunt without documentation provides no institutional value — the findings exist only in the analyst's memory and are lost when they leave or forget.

---

## Question 9

A threat hunter hypothesizes that a threat actor may have used the living-off-the-land technique T1218.010 (Regsvr32) to execute malicious code by registering a DLL from a user-writable directory. Which query against endpoint process telemetry most directly tests this hypothesis?

- A) Filter for `cmd.exe` processes with CommandLine containing `del` or `rmdir`
- B) Filter for `regsvr32.exe` processes with CommandLine paths pointing to directories outside `C:\Windows\System32\` or `C:\Program Files\`
- C) Filter for `svchost.exe` processes making outbound HTTPS connections
- D) Filter for `powershell.exe` processes with CommandLine containing `-EncodedCommand`

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: `del` and `rmdir` are file deletion commands, unrelated to Regsvr32 execution. These would be relevant for anti-forensic hunting, not T1218.010. Why B is correct: T1218.010 describes attackers using `regsvr32.exe` (a legitimate Windows binary) to register and execute a DLL. The malicious DLL is almost always stored in a user-writable directory (`C:\Users\`, `C:\ProgramData\`, `C:\Temp\`) rather than the legitimate system directories. Filtering for `regsvr32.exe` with CommandLine paths outside trusted directories directly tests for malicious Regsvr32 abuse — the classic LOLBin hunting pattern for this technique. Why C is incorrect: `svchost.exe` outbound connections are relevant for detecting process injection (T1055) or service-based C2, not for Regsvr32 execution. Why D is incorrect: PowerShell with `-EncodedCommand` tests for T1059.001 obfuscated PowerShell execution, not Regsvr32 abuse. While both are execution techniques, they are distinct techniques requiring separate queries.

---

## Question 10

An analyst completes a 4-hour threat hunt and finds no evidence supporting their hypothesis. Which outcome best describes what the analyst should do next, and why?

- A) Repeat the exact same hunt immediately using the same queries, in case data was missed on the first pass
- B) Document the negative finding, note what data sources and time ranges were covered, and propose a refined hypothesis or a hunt for a related technique for the next cycle
- C) Report to management that the organization has no active threats and security investment can be reduced
- D) Mark the technique as permanently excluded from future hunts since it has been ruled out

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Repeating the exact same hunt immediately with the same queries against the same data will produce the same result. If the first hunt was properly executed, re-running it adds no value. A refined query, a different data source, or a different time range might yield different results — but that is a refinement, not a repetition. Why B is correct: A negative finding has documentation and planning value. Documenting what was covered (data sources, time range, queries) creates a baseline and prevents redundant future work. Proposing a related hypothesis or a refined version of the original hypothesis keeps the hunt cycle productive. The hunting loop explicitly continues with a new or refined hypothesis after each hunt completes. Why C is incorrect: A negative result in one hunt covering one technique over one time window absolutely does not mean the organization has no active threats. It means no evidence of the specific hypothesized technique was found in the searched data during the covered time period. Drawing conclusions beyond that is a significant overreach. Why D is incorrect: Adversary techniques evolve. A technique that was not observed last month may be actively used next month against updated infrastructure. ATT&CK techniques are never permanently excluded from future hunt consideration.

---

## Question 11

A threat hunter develops the following hypothesis: "We hypothesize that threat actors may be present on our network." What is the primary weakness of this hypothesis and how should it be corrected?

- A) The hypothesis is too short; a minimum of three sentences is required for a valid hunt hypothesis
- B) The hypothesis lacks specificity — it does not identify a technique, expected evidence, data source, or time boundary; it should be rewritten to reference a specific ATT&CK technique with observable indicators
- C) The hypothesis is valid but should be reviewed by management before being executed
- D) The hypothesis is acceptable for an initial exploratory hunt; specific hypotheses are only needed for advanced hunts

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Hypothesis quality is measured by precision and testability, not sentence count. A one-sentence hypothesis that is precisely formed is superior to a three-sentence hypothesis that is vague. Why B is correct: A valid threat hunting hypothesis must specify: what technique or behavior is being hunted (ATT&CK technique preferred), what observable evidence would confirm or refute the hypothesis, which data source will be queried, and the time range. "Threat actors may be present" defines none of these. Without them, there is no defined search query, no success criteria, and no repeatable methodology. The corrected hypothesis would reference a specific technique, its expected telemetry signature, and the data source. Why C is incorrect: Management review may be a good practice for resource allocation but is not a component of hypothesis quality. The flaw is methodological, not governance-related. Why D is incorrect: All hunts — exploratory or targeted — benefit from a structured hypothesis. An "exploratory" hunt without a hypothesis is not a hunt; it is undirected log browsing, which produces inconsistent and undocumentable results.

---

## Question 12

A threat hunter observes that `mshta.exe` on a workstation spawned `powershell.exe`, which then spawned `cmd.exe`. `mshta.exe` is a legitimate Windows utility for running HTML Applications (.HTA files). Which MITRE ATT&CK technique does `mshta.exe` being used as a parent process for code execution represent?

- A) T1059.001 (PowerShell) — because PowerShell is the child process executing code
- B) T1218.005 (System Binary Proxy Execution: Mshta) — a living-off-the-land binary used to execute malicious code while bypassing application control restrictions
- C) T1053.005 (Scheduled Task/Job: Scheduled Task) — the HTA file was likely launched by a scheduled task
- D) T1134 (Access Token Manipulation) — mshta.exe uses token manipulation to escalate to the child process

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: T1059.001 describes the use of PowerShell for execution. While PowerShell is being used, the technique being exploited here is the use of `mshta.exe` as the execution proxy. The question asks what technique `mshta.exe` being the parent process represents, not what the child process does. Why B is correct: T1218.005 describes attackers using `mshta.exe` to execute arbitrary code (JScript, VBScript, or PowerShell via COM objects in an HTA file) while evading application control tools that whitelist signed Microsoft binaries. `mshta.exe` is a trusted, signed Windows binary and is often not blocked by application control. Using it as a launcher for malicious PowerShell is the definition of living-off-the-land proxy execution. Why C is incorrect: Scheduled tasks are a persistence mechanism. The parent-child relationship described does not indicate scheduled task involvement; it indicates interactive or triggered HTA execution. Why D is incorrect: Access Token Manipulation (T1134) involves modifying security tokens to elevate privileges. The described parent-child process relationship is an execution technique, not a privilege escalation mechanism.

---

## Question 13

A threat hunt for lateral movement using stolen credentials produces no results when searching for `net use` commands in process telemetry. The hunter concludes the hunt result is negative. A senior analyst suggests the hunt was incomplete. What alternative data source would provide additional coverage for credential-based lateral movement that process telemetry alone might miss?

- A) HTTP proxy logs showing outbound web requests
- B) Windows Security Event Log Event ID 4648 (logon with explicit credentials) and Event ID 4624 Type 3 (network logon) on the target systems, which would record successful lateral authentication even if no net commands were used
- C) DNS query logs showing domain resolution for internal hostnames
- D) Firewall egress logs showing outbound connections to external IPs

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: HTTP proxy logs record web browsing and outbound HTTP/HTTPS traffic. Lateral movement using stolen credentials to access internal systems does not produce web proxy log entries. Why B is correct: Credential-based lateral movement using tools like `wmiexec`, `psexec`, or direct RDP does not necessarily involve `net use` commands. The authentication events are recorded in Windows Security Event Logs: EID 4648 records when a process explicitly uses credentials (pass-the-hash style), and EID 4624 Type 3 records network logons to a system. Looking for these events on target systems for the compromised source account provides coverage for lateral movement without relying on specific command-line artifacts. This multi-source approach is precisely why process telemetry alone produces incomplete lateral movement coverage. Why C is incorrect: DNS query logs record domain name resolution. Lateral movement using IP addresses directly would not generate DNS queries. Even if hostnames are used, DNS logs would not show that the connection was successful or malicious. Why D is incorrect: Firewall egress logs record outbound connections to external IPs. Lateral movement between internal hosts is east-west traffic that does not traverse the perimeter firewall.

---

## Question 14

A threat hunter reviewing Windows endpoint telemetry notices that `svchost.exe` (PID 3412) has an unusual parent process: `cmd.exe` (PID 3188). In a legitimate Windows environment, `svchost.exe` is always spawned by `services.exe`. What does this parent process anomaly indicate and what action should the hunter take?

- A) This is normal — svchost.exe can have various parent processes depending on the Windows version
- B) This indicates process masquerading: a malicious process named `svchost.exe` was launched from `cmd.exe` to blend in with legitimate svchost processes; the hunter should investigate the executable path, check the file hash, and correlate with network connections for this PID
- C) This indicates a scheduled task ran svchost.exe on a custom schedule; no investigation is needed
- D) This indicates a Windows update is in progress; svchost.exe parents change during update cycles

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: In a legitimate Windows environment, all `svchost.exe` instances are spawned by `services.exe`. There is no legitimate scenario where `cmd.exe` is the parent of `svchost.exe`. This is a universal indicator of either process masquerading (a malicious binary named svchost.exe) or process injection that altered the process lineage. Why B is correct: Malicious actors commonly name their malware `svchost.exe` to blend in with the dozens of legitimate svchost instances visible in Task Manager. A legitimate svchost.exe running from `C:\Windows\System32\` with a parent of `services.exe` is normal. A process named `svchost.exe` with a parent of `cmd.exe` is not. The investigation steps are correct: check the full path (malware often runs from `C:\Temp\` or `C:\Users\`), check the file hash against known-good, and correlate with network connections to identify any C2 communication from this PID. Why C is incorrect: Scheduled tasks are managed by the Task Scheduler service, which runs as a svchost service. Scheduled tasks do not change the parent process of svchost.exe. Why D is incorrect: Windows updates are delivered through the Windows Update service (also hosted in svchost), but the update process does not change the parent of svchost.exe from services.exe to cmd.exe.

---

## Question 15

Which of the following best describes the difference between threat intelligence-led hunting and IOC-based hunting?

- A) Threat intelligence-led hunting uses paid intelligence sources; IOC-based hunting uses free sources
- B) IOC-based hunting searches for specific known artifacts (IP addresses, file hashes, domains); threat intelligence-led hunting uses adversary behavior profiles and TTPs to develop hypotheses and hunt for patterns that may not yet have associated IOCs
- C) IOC-based hunting is performed by Tier 1 analysts; threat intelligence-led hunting is performed only by red teams
- D) Both approaches are identical — threat intelligence is just a source of IOCs

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: The distinction between the two hunt types is methodological, not budget-related. Both approaches can use paid or free intelligence sources. Why B is correct: IOC-based hunting is reactive — it searches for specific known bad indicators (a hash, an IP, a domain) that have been extracted from previous incidents or threat intelligence reports. If the attacker changes their infrastructure, the IOCs become stale and the hunt misses them. TTP-based hunting searches for attacker behaviors and techniques regardless of the specific tools or infrastructure used. A hunt for "Excel spawning PowerShell with base64 arguments" will detect macro-based attacks whether the C2 IP is known or not. TTP-based hunting is more durable and more likely to detect novel or adapted attacks. Why C is incorrect: Threat hunting is performed by defensive security analysts across all experience levels. It is not a red team function. Red teams simulate attacks; hunters detect them. Why D is incorrect: Threat intelligence produces both IOCs and behavioral intelligence (actor profiles, TTPs, campaign narratives). Treating intelligence only as an IOC source discards the behavioral and strategic value that enables TTP-based hunting.

---

## Question 16

During a threat hunt, an analyst discovers a PowerShell script saved to `C:\ProgramData\Microsoft\Crypto\RSA\trusted_update.ps1`. The script contains obfuscated code. The analyst confirms it is malicious. At what point in the MITRE ATT&CK lifecycle does saving a malicious script to a trusted-looking directory represent an example?

- A) Initial Access — the script was delivered via phishing
- B) Defense Evasion — specifically T1564 (Hide Artifacts) combined with T1027 (Obfuscated Files or Information): storing malicious code in a path associated with legitimate Windows cryptographic services reduces the likelihood of detection by path-based monitoring tools
- C) Persistence — the script is stored on disk so it survives reboots
- D) Collection — the script is gathering data for exfiltration

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Initial Access describes how the attacker first entered the network. Placing a script in a trusted-looking path is a post-access activity. Why B is correct: Storing a malicious file in a directory associated with legitimate Windows functionality (`C:\ProgramData\Microsoft\Crypto\RSA\`) is a classic defense evasion technique. Many security monitoring tools and analysts are conditioned to treat paths under `C:\ProgramData\Microsoft\` as trustworthy. This is T1564 (Hide Artifacts) — concealing malicious content in locations where it blends with legitimate content. Combining this with obfuscation (T1027) makes the file difficult both to locate and to analyze. Why C is incorrect: While a file on disk does survive reboots, persistence requires a mechanism that causes the file to execute after restart — a registry run key, scheduled task, or service. Simply storing a file on disk does not create persistence. Why D is incorrect: Collection (T1005, T1074) involves gathering data for exfiltration. The scenario describes a script being stored, with no indication it is collecting data. The storage method and file path are defense evasion indicators, not collection indicators.

---

## Question 17

A threat hunter wants to evaluate whether their organization's current SIEM detection rules would have detected the TA-FREIGHT attack chain described in the module lab scenario. Which process is the most systematic approach to this evaluation?

- A) Ask the IR team whether they have received any TA-FREIGHT-related incidents
- B) Run the TA-FREIGHT attack chain in a production environment and observe whether alerts fire
- C) Map TA-FREIGHT's known TTPs to MITRE ATT&CK technique IDs, open the ATT&CK Navigator, apply the organization's current detection coverage layer, and identify which TA-FREIGHT techniques fall in uncovered (red) areas
- D) Request a penetration test focused on TA-FREIGHT techniques from an external vendor

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: The absence of reported TA-FREIGHT incidents does not indicate detection capability — it could mean the attacker has not targeted the organization, the attack succeeded but was not detected, or incidents were classified differently. This approach provides no systematic coverage assessment. Why B is incorrect: Running an attack chain in a production environment (as opposed to an isolated lab) risks causing real harm, triggering real incident response, and destroying evidence. Even if controlled, production testing is operationally disruptive and legally problematic without formal authorization. Why C is correct: The ATT&CK Navigator's layering function allows analysts to apply multiple coverage layers to the same matrix. By mapping TA-FREIGHT's TTPs to ATT&CK technique IDs (from the group profile if available, or from incident reports) and overlaying the organization's current detection coverage, uncovered techniques appear immediately. This produces a gap list that directly informs hunt priorities and detection engineering work without requiring any active attack simulation. Why D is incorrect: A penetration test provides detection evaluation but is expensive, time-consuming, and typically not available on demand. The ATT&CK Navigator approach is free, immediate, and provides an equally systematic coverage gap assessment for planning purposes.

---

## Question 18

An analyst reviewing process telemetry identifies `certutil.exe` executing with the argument `-decode base64_payload.txt decoded.exe`. What technique does this represent and why is it significant for threat hunting?

- A) T1140 (Deobfuscate/Decode Files or Information) — certutil.exe is a legitimate Windows binary being used to decode a base64-encoded malicious payload, bypassing security tools that block PowerShell base64 decoding
- B) T1003 (OS Credential Dumping) — certutil.exe is accessing the certificate store to extract credentials
- C) T1071.001 (Web Protocols) — certutil.exe is making an HTTP request to download a file
- D) T1036 (Masquerading) — the analyst should look for certutil.exe running from an unusual path

**Correct Answer:** A

**Distractor Analysis:** Why A is correct: `certutil.exe` is a legitimate Windows binary for managing certificates, but it has well-documented abuse as a living-off-the-land binary. The `-decode` argument is not a certificate management function — it decodes base64-encoded content to a file. Attackers use this to deliver encoded payloads that evade signature-based tools focused on PowerShell or `certutil -urlcache -f` (download). The resulting `decoded.exe` is the actual malicious payload. This is T1140 — using a trusted system binary to deobfuscate malicious content, which is precisely why it is significant for hunting: the process is signed, trusted, and unlikely to trigger antivirus, but the specific argument combination is a high-fidelity hunting indicator. Why B is incorrect: OS Credential Dumping involves accessing LSASS memory or credential stores. The described `certutil.exe` activity is file decoding, not credential access. Why C is incorrect: T1071.001 involves using HTTP for C2 communication. `certutil.exe -decode` is a local file decoding operation, not a network request. `certutil -urlcache -f` would be the network download variant. Why D is incorrect: T1036 masquerading involves naming malware after legitimate binaries. The scenario describes legitimate `certutil.exe` being abused for its built-in functionality, not a file named certutil.exe from an unusual path.

---

## Question 19

A threat hunter wants to create a detection rule in the SIEM based on hunt findings. The hunt identified that `excel.exe` spawning `powershell.exe` with a `-enc` argument is a high-confidence malicious behavior. Which approach produces the most operationally useful detection rule?

- A) Alert on any process creation event where the parent is `excel.exe`
- B) Alert when `excel.exe` spawns `powershell.exe` with a CommandLine argument containing `-enc` or `-EncodedCommand`, and correlate with any outbound network connection from the same PowerShell PID within 5 minutes
- C) Alert on any use of the `-enc` PowerShell argument regardless of parent process
- D) Alert on all PowerShell executions and have analysts manually review each one

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Many legitimate Excel processes spawn children — Excel spawns `dw20.exe` (crash reporting), `splwow64.exe` (print), and other utility processes. Alerting on any Excel child process would produce enormous false-positive volume and suppress analyst attention through alert fatigue. Why B is correct: The compound condition dramatically improves precision. `excel.exe` spawning `powershell.exe` is already suspicious; adding the `-enc` argument filter targets the specific encoded execution pattern; correlating with an outbound network connection from the same PID confirms active C2 — turning a suspicious event into a high-confidence malicious indicator. This multi-condition approach produces fewer alerts with higher fidelity, which is the design goal for production SIEM rules derived from hunt findings. Why C is incorrect: PowerShell with `-enc` is used by many legitimate applications, administrative scripts, and management tools. Alerting on any `-enc` usage without a suspicious parent process context produces significant false-positive volume. Why D is incorrect: Alerting on all PowerShell executions and manually reviewing each one is not operationally sustainable in any environment with more than a handful of endpoints. Modern environments generate hundreds of legitimate PowerShell executions per day.

---

## Question 20

A threat hunt for DGA (Domain Generation Algorithm) activity in DNS logs involves computing the entropy of queried domain names. Which characteristic of DGA-generated domains makes entropy analysis an effective detection technique?

- A) DGA domains are always longer than 20 characters, making length-based detection reliable
- B) DGA algorithms generate pseudo-random character strings that have high Shannon entropy — they lack the natural language patterns (low entropy) that characterize legitimate domain names like company names, product names, or common words
- C) DGA domains always use uncommon top-level domains (.xyz, .info) which are blocked by most firewalls
- D) DGA activity always produces NXDOMAIN responses, so entropy analysis is unnecessary — NXDOMAIN filtering alone is sufficient

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: DGA domain length varies by algorithm. Some DGAs generate 8-character domains; others generate 30+ characters. Length alone is not a reliable detector because many legitimate short domains and many legitimate long domains exist. Why B is correct: Shannon entropy measures the unpredictability of character sequences. Human-generated domain names (company names, product names) have low entropy because they use recognizable word patterns with predictable character distributions. DGA-generated domains use pseudo-random character sequences derived from date seeds or cryptographic functions — producing character distributions that approach random, resulting in high Shannon entropy. A domain like `facebook.com` has low entropy; a domain like `xkqrtmbsz.net` has high entropy. Entropy scoring across DNS query volumes enables statistical identification of DGA domains that evade signature-based tools. Why C is incorrect: While some DGA malware uses uncommon TLDs, modern DGA implementations use common TLDs (.com, .net, .org) specifically to avoid TLD-based blocking. TLD filtering is not a reliable DGA detection method. Why D is incorrect: While NXDOMAIN responses are a DGA indicator when the C2 infrastructure is offline, DGA malware that successfully connects to active C2 infrastructure produces NOERROR responses. NXDOMAIN filtering alone misses all active DGA C2 sessions.
