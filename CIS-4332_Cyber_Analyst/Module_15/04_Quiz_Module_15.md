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
