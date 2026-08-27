# Reading Guide: Module 02 - Threat Intelligence and MITRE ATT&CK

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Introduction

Module 02 covers the two knowledge systems that underpin every advanced analyst skill in this course: Cyber Threat Intelligence and the MITRE ATT&CK framework. These topics appear throughout every domain of the CySA+ CS0-003 exam. ATT&CK technique IDs appear in vulnerability management, incident response, threat hunting, and reporting questions. Mastering this module's content gives you a foundational advantage across the entire exam.

Work through every section before completing the lab. The lab requires you to map a multi-stage attack scenario to ATT&CK tactics and techniques — you cannot do that successfully without knowing the tactic names, technique IDs, and sub-technique structure in this guide.

---

## Section 1: Cyber Threat Intelligence Fundamentals

### 1.1 Defining CTI

Cyber Threat Intelligence is evidence-based knowledge about existing or emerging threats and threat actors, including their intent, capabilities, and infrastructure, that can be used to inform decisions.

Three properties distinguish intelligence from raw data:

- It has been collected and evaluated from multiple sources
- It has been analyzed to determine reliability and relevance
- It is actionable — it changes what the defender does

Raw firewall logs are data. A curated list of command-and-control IPs attributed to a specific ransomware group, with confidence ratings and recommended block actions, is tactical intelligence.

### 1.2 The Intelligence Lifecycle

| Phase | Description | Key Questions |
|---|---|---|
| Direction | Define intelligence requirements | What do we need to know? What decisions does this support? |
| Collection | Gather raw data from sources | OSINT, commercial feeds, ISAC sharing, internal telemetry |
| Processing | Normalize, deduplicate, structure data | Convert to common format; remove noise |
| Analysis | Extract meaning, assess confidence, draw conclusions | What does this mean? How confident are we? What should we do? |
| Dissemination | Distribute finished intelligence to consumers | Right format, right audience, right time |

The lifecycle is iterative. Dissemination generates new questions that feed back into Direction, starting the cycle again.

### 1.3 Intelligence Types

| Type | Audience | Time Horizon | Examples |
|---|---|---|---|
| Strategic | Executives, Board, CISO | Months to years | Industry threat trends, geopolitical risk, adversary capability assessments |
| Operational | Security managers, architects | Weeks to months | Active campaign reporting, threat actor targeting patterns, attack vector forecasts |
| Tactical | Tier 1/2 analysts, detection engineers | Hours to days | Malicious IPs, file hashes, YARA rules, ATT&CK technique mappings, CVE exploitation data |

### 1.4 Intelligence Sources

| Source Type | Description | Examples |
|---|---|---|
| OSINT | Publicly available information | CISA advisories, FBI flash reports, CVE NVD, vendor security blogs, academic papers |
| Commercial Feeds | Proprietary curated intelligence | Threat intelligence platforms with enriched IOC data and attribution |
| ISAC | Sector-specific sharing communities | FS-ISAC (financial), H-ISAC (healthcare), E-ISAC (energy) |
| Government | National and international bodies | CISA, FBI IC3, NCSC (UK), ENISA (EU) |
| Internal Telemetry | Organization's own logs and incidents | SIEM alerts, EDR events, past incident reports, honeypot data |
| Dark Web Monitoring | Underground forums and marketplaces | Credential leak monitoring, ransomware group communications |

### 1.5 Traffic Light Protocol

The Traffic Light Protocol (TLP) is the standard marking system for intelligence sharing restrictions.

| Marking | Sharing Restriction |
|---|---|
| TLP:RED | No sharing; recipient only |
| TLP:AMBER | Limited sharing within the recipient's organization and its clients |
| TLP:AMBER+STRICT | Limited to the recipient's organization only; no client sharing |
| TLP:GREEN | Sharing within the community or sector |
| TLP:CLEAR | No restriction; public distribution permitted |

---

## Section 2: MITRE ATT&CK Framework

### 2.1 Framework Overview

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a knowledge base of adversary behaviors based on real-world observations. It is maintained by the non-profit MITRE Corporation and is freely available at attack.mitre.org.

Three key properties make ATT&CK uniquely valuable:

- It is based on observed attacker behavior, not theoretical models
- It is community-maintained and continuously updated as new techniques are documented
- It provides a common language for describing threats across teams, organizations, and tools

### 2.2 ATT&CK Structure

| Level | Description | Example |
|---|---|---|
| Tactic | The adversary's goal — the "why" | Initial Access (TA0001) |
| Technique | The method used — the "how" | Phishing (T1566) |
| Sub-technique | Specific variation of a technique | Spearphishing Attachment (T1566.001) |
| Procedure | Specific implementation by a threat actor | APT29 using spearphishing with malicious PDF attachments |

### 2.3 The 14 Enterprise ATT&CK Tactics

Memorize these in order. Exam scenario questions test your ability to identify the correct tactic for a described attacker action.

| ID | Tactic | Adversary Goal |
|---|---|---|
| TA0043 | Reconnaissance | Gather information about the target before attacking |
| TA0042 | Resource Development | Establish infrastructure, acquire tools, develop capabilities |
| TA0001 | Initial Access | Gain a foothold in the target environment |
| TA0002 | Execution | Run malicious code on a target system |
| TA0003 | Persistence | Maintain access across reboots and credential changes |
| TA0004 | Privilege Escalation | Gain higher-level permissions than initially obtained |
| TA0005 | Defense Evasion | Avoid detection and bypass security controls |
| TA0006 | Credential Access | Steal account credentials and authentication material |
| TA0007 | Discovery | Learn about the environment: systems, accounts, network topology |
| TA0008 | Lateral Movement | Move from one system to other systems in the environment |
| TA0009 | Collection | Gather data of interest prior to exfiltration |
| TA0011 | Command and Control | Communicate with compromised systems to control them |
| TA0010 | Exfiltration | Transfer data out of the target environment |
| TA0040 | Impact | Disrupt, destroy, or manipulate systems and data |

### 2.4 High-Frequency Techniques for CySA+ Exam

These techniques appear most frequently in CySA+ scenario questions. Know each by ID, name, tactic, and description.

| Technique ID | Name | Tactic | Description |
|---|---|---|---|
| T1566 | Phishing | Initial Access | Delivery of malicious content via email |
| T1566.001 | Spearphishing Attachment | Initial Access | Malicious file attached to targeted email |
| T1566.002 | Spearphishing Link | Initial Access | Malicious URL in targeted email |
| T1059 | Command and Scripting Interpreter | Execution | Use of shell, scripting language, or interpreter |
| T1059.001 | PowerShell | Execution | Execution via PowerShell |
| T1053.005 | Scheduled Task | Persistence | Creating a scheduled task for persistence or execution |
| T1547.001 | Registry Run Keys / Startup Folder | Persistence | Modifying registry keys to run code at startup |
| T1055 | Process Injection | Defense Evasion / Privilege Escalation | Injecting code into another running process |
| T1003 | OS Credential Dumping | Credential Access | Extracting credentials from OS memory or files |
| T1003.001 | LSASS Memory | Credential Access | Dumping credentials from LSASS process memory |
| T1018 | Remote System Discovery | Discovery | Enumerating other systems on the network |
| T1021 | Remote Services | Lateral Movement | Using legitimate remote access services to move laterally |
| T1021.001 | Remote Desktop Protocol | Lateral Movement | Using RDP to access remote systems |
| T1041 | Exfiltration Over C2 Channel | Exfiltration | Sending data out through the C2 channel |
| T1071 | Application Layer Protocol | Command and Control | Using standard protocols (HTTP, DNS) for C2 |
| T1486 | Data Encrypted for Impact | Impact | Encrypting data to render it unavailable (ransomware) |
| T1490 | Inhibit System Recovery | Impact | Deleting backups or shadow copies to prevent recovery |

### 2.5 ATT&CK Matrices

ATT&CK has multiple matrices for different environments:

| Matrix | Target Environment |
|---|---|
| Enterprise | Windows, macOS, Linux, cloud, containers, network |
| Mobile | Android and iOS devices |
| ICS | Industrial Control Systems and OT environments |

The CySA+ exam primarily tests Enterprise ATT&CK.

---

## Section 3: Complementary Frameworks

### 3.1 Cyber Kill Chain

The Kill Chain (Lockheed Martin) models an attack as a linear seven-phase progression.

| Phase | Description |
|---|---|
| 1. Reconnaissance | Attacker researches the target |
| 2. Weaponization | Attacker creates malicious payload |
| 3. Delivery | Payload delivered to target (email, web, USB) |
| 4. Exploitation | Payload exploits vulnerability to execute |
| 5. Installation | Malware installed on target system |
| 6. Command and Control | Attacker establishes remote access channel |
| 7. Actions on Objectives | Attacker achieves goal (exfiltration, destruction, ransom) |

Limitation: The Kill Chain is linear and was designed for external intrusions. It does not model insider threats, cloud attacks, or complex non-linear operations as effectively as ATT&CK.

### 3.2 Diamond Model

The Diamond Model provides an analytical framework for intrusion analysis using four vertices:

- Adversary: Who is conducting the attack
- Capability: What tools and techniques are being used
- Infrastructure: What servers, domains, and IPs support the attack
- Victim: Who or what is being targeted

Analysts use the model to pivot: identifying one vertex can reveal the others. Identifying a malicious domain (Infrastructure) can lead to other domains used by the same adversary.

### 3.3 Framework Comparison

| Attribute | Kill Chain | ATT&CK | Diamond Model |
|---|---|---|---|
| Structure | Linear, 7 phases | Matrix, 14 tactics, 200+ techniques | 4-vertex analytical model |
| Primary Use | Attack phase identification | Technique-level detection and analysis | Intrusion analysis and pivoting |
| Granularity | Low — phase level | High — sub-technique level | Medium — analytical model |
| Insider Threat Fit | Poor | Good | Good |
| Exam Frequency | Moderate | High | Moderate |

---

## Section 4: Intelligence-Driven Defense

### 4.1 From CTI to Detection Rules

Converting threat intelligence into detection rules follows this workflow:

1. Receive intelligence (a report, a feed update, a shared IOC)
2. Identify the ATT&CK technique the intelligence describes
3. Determine what observable evidence that technique leaves in your log sources
4. Write a SIEM correlation rule or EDR detection rule targeting that evidence
5. Test the rule in a non-production environment
6. Deploy and monitor

### 4.2 STIX and TAXII Standards

STIX (Structured Threat Information Expression) is the data format for expressing threat intelligence in a structured, machine-readable form.

TAXII (Trusted Automated Exchange of Intelligence Information) is the transport protocol for sharing STIX data between systems and organizations.

Together, STIX and TAXII enable automated threat intelligence sharing between platforms, organizations, and government agencies.

---

## Section 5: SIEM Query Examples for ATT&CK Techniques

Detecting T1053.005 — Scheduled Task creation (Windows Event Code 4698):

```splunk
index=wineventlog EventCode=4698
| table _time, host, TaskName, SubjectUserName
| where SubjectUserName != "SYSTEM"
```

Detecting T1003.001 — LSASS Memory access (Sysmon Event ID 10):

```splunk
index=sysmon EventCode=10 TargetImage="*lsass.exe"
| stats count by SourceImage, GrantedAccess, host
```

Detecting T1071 — Outbound HTTP to non-standard ports:

```splunk
index=network dest_port!=80 dest_port!=443 dest_port!=8080
  (app=http OR app=https)
| stats count by src_ip, dest_ip, dest_port
| where count > 5
| sort -count
```

---

## CySA+ Exam Tips

Exam Tip 1: Memorize the 14 tactics in order. Scenario questions ask you to identify the correct tactic for a described attacker action. Knowing the names cold lets you eliminate wrong answers immediately.

Exam Tip 2: Know technique IDs for the high-frequency list in Section 2.4. T1566, T1059, T1053, T1003, T1486, and T1490 appear in exam questions by name and sometimes by ID number.

Exam Tip 3: TLP levels are tested directly. TLP:RED = recipient only. TLP:AMBER = limited organizational sharing. TLP:GREEN = community sharing. TLP:CLEAR = public.

Exam Tip 4: Intelligence types map to audiences. Strategic = executives. Operational = managers. Tactical = analysts. Map audience to type when exam questions ask who consumes a specific intelligence product.

Exam Tip 5: The intelligence lifecycle is iterative, not linear. Know each phase: Direction, Collection, Processing, Analysis, Dissemination.

Exam Tip 6: ATT&CK provides technique-level specificity; the Kill Chain does not. If an exam question asks which framework provides the most granular technique detail, the answer is ATT&CK.

Exam Tip 7: STIX is the data format; TAXII is the transport protocol. If asked which standard governs automated threat intelligence sharing, both are involved.

Exam Tip 8: Diamond Model pivoting allows analysts to move from one known vertex to discover the others. This is a tested analytical technique for CTI investigation.

---

## Glossary

- ATT&CK: Adversarial Tactics, Techniques, and Common Knowledge; MITRE's adversary behavior knowledge base
- CTI: Cyber Threat Intelligence; processed information about adversaries that drives defensive decisions
- Diamond Model: Four-vertex intrusion analysis framework — Adversary, Capability, Infrastructure, Victim
- ISAC: Information Sharing and Analysis Center; sector-specific threat intelligence sharing community
- Kill Chain: Lockheed Martin's seven-phase linear attack model
- OSINT: Open Source Intelligence; publicly available information used as an intelligence source
- STIX: Structured Threat Information Expression; data format for machine-readable threat intelligence
- Sub-technique: A specific variation of an ATT&CK technique, identified by a decimal ID (e.g., T1566.001)
- Tactic: The adversary's goal at an ATT&CK phase (the "why")
- TAXII: Trusted Automated Exchange of Intelligence Information; transport protocol for sharing threat intelligence
- Technique: The specific ATT&CK method used to achieve a tactic (the "how")
- TIP: Threat Intelligence Platform; aggregates and operationalizes CTI from multiple sources
- TLP: Traffic Light Protocol; marking system governing intelligence sharing permissions
- TTP: Tactics, Techniques, and Procedures; how an adversary operates; highest Pyramid of Pain level

---

## Required Resources

- MITRE ATT&CK Enterprise Matrix: attack.mitre.org (free, public)
- Official CySA+ CS0-003 exam objectives: comptia.org
- Professor Messer CySA+ CS0-003 free study materials: professormesser.com

---

## Study Checklist

- [ ] Define CTI and explain each intelligence lifecycle phase without notes
- [ ] Match each intelligence type to its correct audience and time horizon
- [ ] Memorize all five TLP markings and their sharing restrictions
- [ ] Recite all 14 ATT&CK tactics with their IDs and adversary goals
- [ ] Review every high-frequency technique in Section 2.4; self-test by covering the description column
- [ ] Compare Kill Chain, ATT&CK, and Diamond Model on structure, granularity, and use case
- [ ] Explain the six-step process for converting CTI into a detection rule
- [ ] Review all eight exam tips
- [ ] Complete the Module 02 Lab
- [ ] Complete the Module 02 Quiz
- [ ] Post your initial response to the Module 02 Discussion board by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. MITRE ATT&CK Navigator**
<https://mitre-attack.github.io/attack-navigator/>
The official interactive heat-map tool for visualizing ATT&CK technique coverage. Use it to explore the Enterprise matrix, mark techniques with detection or mitigation coverage, and perform the gap analysis described in Section 5 of this guide. Hands-on navigation is the fastest way to internalize the tactic and technique structure.

**2. CISA — Sharing Cyber Threat Intelligence**
<https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing>
CISA's guidance on threat intelligence sharing programs, including the Automated Indicator Sharing (AIS) platform that uses STIX/TAXII. Reading this page connects the academic STIX/TAXII standards in Section 3 to real operational sharing infrastructure used by U.S. government and private sector partners.

**3. FIRST — Traffic Light Protocol (TLP) Standard**
<https://www.first.org/tlp/>
The authoritative TLP specification maintained by the Forum of Incident Response and Security Teams (FIRST). The page defines all five TLP markings with usage guidance. This is the primary reference for TLP questions on the CySA+ exam and for professional CTI sharing decisions.
