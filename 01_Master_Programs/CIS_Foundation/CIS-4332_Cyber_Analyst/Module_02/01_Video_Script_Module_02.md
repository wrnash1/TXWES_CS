# Video Script: Module 02 - Threat Intelligence and MITRE ATT&CK

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20-24 minutes

## CySA+ CS0-003 Domain Alignment: Domain 1 - Security Operations (33%)

---

### [00:00 - 01:30] Introduction

Professor Nash on camera. Title card: Module 02 — Threat Intelligence and MITRE ATT&CK.

"Welcome back. In Module 01 we established the SOC structure and the analyst role. Now we go deeper into the intelligence layer — the knowledge that separates a reactive SOC from a proactive one. This module covers two of the most important topics on the CySA+ CS0-003 exam: Cyber Threat Intelligence and the MITRE ATT&CK framework.

If you learn nothing else from this course, learn MITRE ATT&CK. It is the universal language of modern threat analysis. Every major security tool, every incident report, every threat intelligence feed references it. By the end of this module, you will be able to map an attack scenario to specific tactics and techniques, and you will understand how that mapping drives detection, hunting, and response. Let's get to it."

---

### [01:30 - 05:00] What Is Cyber Threat Intelligence?

"Threat intelligence — often abbreviated CTI — is processed, analyzed information about adversaries that helps defenders make better decisions. Let me break that sentence down carefully because every word in it matters.

It is processed and analyzed, not raw. Raw logs, packet captures, and dark web chatter are not intelligence — they are data. Intelligence is what you get after a trained analyst or automated system has evaluated that data, determined its reliability, and extracted actionable meaning from it.

It is about adversaries — who is attacking, why they are attacking, how they operate, and what they are targeting.

It helps defenders make decisions. If intelligence doesn't change what your team does — if it sits in a report nobody reads — it has no operational value. Good CTI drives action: a new detection rule, a new block on a threat feed, a hunt for a specific technique.

The intelligence lifecycle has five phases: Direction, Collection, Processing, Analysis, and Dissemination. Direction is where you define what questions you need answered. Collection is gathering raw data from sources. Processing is normalizing and organizing that data. Analysis is the human or machine work of extracting meaning. Dissemination is getting that intelligence to the people who need it — Tier 1 analysts, firewall engineers, leadership.

The CySA+ exam tests this lifecycle. Know the phases and know that the cycle is iterative — the results of one round of intelligence feed the requirements for the next."

[SHOW DIAGRAM: Five-phase cycle labeled clockwise: Direction, Collection, Processing, Analysis, Dissemination, with an arrow returning from Dissemination to Direction labeled "New Requirements Generated." Center label: "CTI Lifecycle — Iterative."]

---

### [05:00 - 08:30] Intelligence Types and Sources

"Not all threat intelligence is the same. The CySA+ exam organizes it into three types: Strategic, Operational, and Tactical.

Strategic intelligence is high-level, long-term, and designed for executives and risk managers. It answers questions like: What threat actor groups target our industry? What attack trends should we anticipate over the next year? Strategic intelligence informs budget decisions and security program direction.

Operational intelligence sits in the middle. It is about specific campaigns, threat actor intentions, and upcoming attack patterns. It helps security managers and architects make decisions about defensive priorities. An example: a threat intelligence provider reports that a specific ransomware group is actively targeting healthcare organizations with a particular phishing lure. That is operational intelligence — it tells you what is coming and who is targeted.

Tactical intelligence is the most granular. It is about specific indicators and techniques. File hashes, malicious IP addresses, domain names, YARA rules, MITRE technique IDs — all tactical intelligence. This is what Tier 1 and Tier 2 analysts consume directly in their daily work.

Intelligence sources include open source intelligence — OSINT — which covers publicly available information such as vendor reports, government advisories from CISA and the FBI, academic research, security blogs, and CVE databases. Commercial threat feeds are proprietary data purchased from vendors. They provide higher confidence and curated data with analyst context.

Information Sharing and Analysis Centers, or ISACs, are sector-specific sharing communities. The FS-ISAC serves financial services; H-ISAC serves healthcare.

Your own internal telemetry — logs, alerts, and incident data — is the most contextually accurate source for your specific environment.

The Traffic Light Protocol, or TLP, governs how intelligence can be shared. TLP:RED means only the recipient can see it. TLP:AMBER means limited sharing within an organization. TLP:GREEN means sharing within the community. TLP:CLEAR means public distribution is permitted. You will see TLP markings on every intelligence report in the industry."

---

### [08:30 - 13:00] MITRE ATT&CK — The Framework

"Now let's talk about MITRE ATT&CK. ATT&CK stands for Adversarial Tactics, Techniques, and Common Knowledge. It is a publicly available, community-maintained knowledge base that describes how real-world adversaries operate — based on documented observations from actual attacks, not theoretical models.

The framework is organized around three levels: Tactics, Techniques, and Sub-techniques.

Tactics represent the adversary's goal at each phase of an operation — the why. There are 14 tactics in the Enterprise ATT&CK matrix. Memorize them in order because the exam presents scenario questions where you need to identify which tactic is being used.

The 14 Enterprise ATT&CK tactics are: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, and Impact.

Techniques represent the specific how — the method an adversary uses to achieve a tactic. Under the Initial Access tactic, one technique is Phishing — T1566. Under Persistence, one technique is Scheduled Task/Job — T1053. Under Execution, Command and Scripting Interpreter is T1059.

Sub-techniques add specificity below the technique level. T1566 Phishing has three sub-techniques: T1566.001 Spearphishing Attachment, T1566.002 Spearphishing Link, and T1566.003 Spearphishing via Service."

[SHOW DIAGRAM: ATT&CK matrix layout. Top row: all 14 tactic column headers from Reconnaissance through Impact. Below each column, stacked technique boxes. Three technique boxes highlighted: T1566 Phishing under Initial Access, T1053 Scheduled Task under Persistence, T1059 Command and Scripting Interpreter under Execution. Expanded view of T1566 showing sub-techniques .001, .002, .003.]

---

### [13:00 - 16:30] Applying ATT&CK to Attack Scenarios

"Understanding the theory is only half the work. The real value of ATT&CK is applying it. Let me walk through a realistic attack scenario and map each stage to a tactic and technique.

The scenario: An employee receives an email with a malicious PDF attachment. They open it. The PDF exploits a vulnerability in the reader, drops a file to disk, and executes it. That file establishes a connection to an external server. The attacker uses that connection to run commands on the system. They create a scheduled task to survive a reboot. They then run discovery commands to enumerate the network and identify a domain controller. They move laterally to the domain controller, dump credential hashes, and establish a second foothold.

Mapping this scenario to ATT&CK:

The email with the malicious PDF maps to Initial Access — T1566.001, Spearphishing Attachment.

The PDF exploiting a vulnerability and dropping a file maps to Execution — the exploit triggers execution of the dropped payload.

Establishing a connection to an external server is Command and Control — T1071, Application Layer Protocol, because the attacker is communicating over HTTP or HTTPS to blend into normal traffic.

Creating a scheduled task maps to Persistence — T1053.005, Scheduled Task.

Running discovery commands to enumerate the network maps to Discovery — T1018, Remote System Discovery.

Moving to the domain controller is Lateral Movement — T1021, Remote Services.

Dumping credential hashes is Credential Access — T1003, OS Credential Dumping.

This is the workflow you will practice in the lab. You receive a scenario narrative and identify the correct tactic and technique for each observed behavior. This exact skill appears on the CySA+ exam."

---

### [16:30 - 19:30] Threat Actor Groups and Intelligence-Driven Defense

"ATT&CK also documents specific threat actor groups. Each group entry lists the techniques that group has been observed using, the malware and tools associated with them, and citations to public intelligence reports.

For example, APT29 — also known as Cozy Bear — is a threat group attributed to Russian intelligence services. Their ATT&CK profile documents techniques including T1566 Phishing for initial access, T1078 Valid Accounts for persistence using stolen credentials, and T1071.001 Web Protocols for command and control over HTTPS.

Why does this matter? Because if your organization operates in a sector targeted by APT29 — government agencies, think tanks, healthcare organizations — you can pull up their ATT&CK technique list and build detection rules for those specific techniques before an attack occurs. You are not guessing what to look for. You are building defenses around documented adversary behavior.

This is intelligence-driven defense. You use CTI to anticipate, detect, and disrupt attacks that align with known adversary patterns. It is far more effective than trying to detect every possible attack in the abstract."

---

### [19:30 - 22:00] The Cyber Kill Chain

"Before we close, let me briefly address the Cyber Kill Chain because the CySA+ exam tests both frameworks and sometimes asks you to compare them.

The Cyber Kill Chain was developed by Lockheed Martin and describes an attack as a linear seven-phase sequence: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, and Actions on Objectives.

The Kill Chain is intuitive and explains well to non-technical audiences. However, it was designed for external threat actors and does not model insider threats or complex multi-stage intrusions as effectively as ATT&CK. It also does not provide the technique-level specificity of ATT&CK.

MITRE ATT&CK was built to address those limitations. It is not linear — adversaries do not always follow a clean sequence. ATT&CK models how adversaries actually behave, including skipping phases, reusing techniques, and operating over extended dwell periods.

For the exam: know both. The Kill Chain is linear and seven-phase. ATT&CK is matrix-based with 14 tactics and hundreds of techniques. Both are used in the industry, often together. The Diamond Model is a third analytical model the exam tests — four vertices are Adversary, Capability, Infrastructure, and Victim."

[SHOW DIAGRAM: Side-by-side comparison. Left side: Kill Chain as seven horizontal chain links labeled Reconnaissance through Actions on Objectives. Right side: ATT&CK matrix thumbnail with 14 columns. Labels: "Kill Chain — Linear, 7 phases, external attacker model." "ATT&CK — Matrix, 14 tactics, models observed real-world behavior, technique-level specificity."]

---

### [22:00 - 24:00] Module Summary and Lab Preview

"Let's bring it together.

Cyber Threat Intelligence is processed, analyzed information about adversaries that drives defensive decisions. The lifecycle has five phases: Direction, Collection, Processing, Analysis, Dissemination.

Intelligence is categorized as Strategic (executive level), Operational (campaign level), or Tactical (indicator and technique level for daily analyst use).

MITRE ATT&CK has 14 tactics and hundreds of techniques. Tactics answer why; techniques answer how.

The 14 tactics in order: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact.

The Cyber Kill Chain is a linear seven-phase model. The Diamond Model provides a four-vertex analytical structure.

In your lab this module, you will receive a complete attack scenario narrative and map each observed behavior to the correct ATT&CK tactic and technique. Read the Reading Guide first — it contains the full tactic and technique reference table you will need.

Study resources: professormesser.com and comptia.org.

See you in Module 03."

---

End of Module 02 Video Script

Study Resources: comptia.org | professormesser.com
