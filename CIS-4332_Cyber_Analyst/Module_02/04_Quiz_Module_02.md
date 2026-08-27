# Quiz: Module 02 - Threat Intelligence and MITRE ATT&CK

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer. Review the distractor analysis to understand why wrong answers are wrong — this reasoning appears directly in CySA+ exam questions.

---

## Question 1

An analyst receives a threat intelligence report describing a known ransomware group's infrastructure, their preferred phishing lure themes, and the specific Windows API calls their malware uses during execution. Which intelligence type does this report represent?

- A) Strategic intelligence
- B) Operational intelligence
- C) Tactical intelligence
- D) Administrative intelligence

Correct Answer: C

Distractor Analysis:

- A is incorrect. Strategic intelligence is long-term and executive-focused — it covers broad threat trends and risk, not specific technical details about a single group's malware behavior.
- B is incorrect. Operational intelligence covers campaign-level patterns and adversary intentions. The report here contains specific technical artifacts (Windows API calls), which places it in the tactical category.
- C is correct. Tactical intelligence is the most granular type and is designed for direct consumption by analysts and detection engineers. Specific IOCs, API call patterns, and infrastructure details are all tactical intelligence.
- D is incorrect. "Administrative intelligence" is not a recognized CTI category.

---

## Question 2

A threat intelligence analyst receives a report marked TLP:AMBER. Which sharing action is appropriate?

- A) Share the report publicly on social media to warn the broader security community
- B) Share the report with all employees during a company-wide security awareness training session
- C) Share the report with security team members within the organization and relevant clients, but not externally beyond that
- D) Restrict the report to the receiving analyst only; no sharing with colleagues is permitted

Correct Answer: C

Distractor Analysis:

- A is incorrect. TLP:AMBER explicitly prohibits public sharing. Public distribution is only permitted for TLP:CLEAR.
- B is incorrect. Sharing TLP:AMBER material in a company-wide session would expose it to employees outside the intended security audience and potentially to contractors or guests, violating the marking's intent.
- C is correct. TLP:AMBER permits limited sharing within the recipient's organization and with the organization's clients on a need-to-know basis. It prohibits broad public disclosure.
- D is incorrect. TLP:RED restricts sharing to the recipient only. TLP:AMBER allows broader but still limited organizational sharing.

---

## Question 3

Which of the following best describes the difference between a MITRE ATT&CK Tactic and a Technique?

- A) A Tactic describes what tool the attacker used; a Technique describes why the attacker targeted this organization
- B) A Tactic represents the adversary's goal at a phase of the attack; a Technique is the specific method used to achieve that goal
- C) A Tactic is used only for nation-state attacks; a Technique applies to all threat actors
- D) A Tactic is a defensive response category; a Technique is an offensive capability

Correct Answer: B

Distractor Analysis:

- A is incorrect. Tactics and Techniques do not map to tools and motivations in this way. Tools are captured in the ATT&CK Software category, and motivations are captured in Group profiles.
- B is correct. In ATT&CK, Tactics answer "why" — the adversary's goal (e.g., gain persistence). Techniques answer "how" — the specific method used (e.g., create a scheduled task). This is the foundational ATT&CK definitional distinction.
- C is incorrect. ATT&CK tactics and techniques apply to all threat actors regardless of sophistication or origin.
- D is incorrect. ATT&CK is an offensive adversary behavior model, not a defensive categorization framework.

---

## Question 4

An analyst observes that malware on a compromised host is communicating with an external server using HTTPS on port 443, blending into normal web traffic. Which ATT&CK technique does this most closely represent?

- A) T1566 — Phishing
- B) T1071 — Application Layer Protocol
- C) T1486 — Data Encrypted for Impact
- D) T1003 — OS Credential Dumping

Correct Answer: B

Distractor Analysis:

- A is incorrect. Phishing (T1566) describes Initial Access via malicious email, not C2 communication behavior.
- B is correct. T1071 — Application Layer Protocol describes adversaries using common application protocols such as HTTPS to blend command-and-control communications into normal traffic, making detection harder.
- C is incorrect. T1486 — Data Encrypted for Impact is a ransomware technique that encrypts victim files; it is not about C2 communication.
- D is incorrect. T1003 — OS Credential Dumping involves extracting credential material from the operating system; it has nothing to do with network communication patterns.

---

## Question 5

Which of the following correctly identifies the ATT&CK tactic associated with an attacker creating a Windows Registry Run key to execute malware on every system startup?

- A) Initial Access
- B) Execution
- C) Persistence
- D) Privilege Escalation

Correct Answer: C

Distractor Analysis:

- A is incorrect. Initial Access describes how an attacker first enters the environment (e.g., phishing, exploiting a public-facing application). Creating a registry key assumes the attacker is already inside.
- B is incorrect. Execution describes running malicious code. A registry Run key creates a trigger for future execution — its primary purpose is to survive reboots, not to run code immediately.
- C is correct. Persistence (TA0003) is the tactic of maintaining access across events that would otherwise interrupt access, such as reboots or credential changes. Registry Run keys (T1547.001) are a classic persistence technique.
- D is incorrect. Privilege Escalation involves gaining higher permissions than initially obtained. A Run key does not elevate privileges.

---

## Question 6

A security team wants to proactively build detection rules for techniques used by a specific nation-state threat actor group that targets their industry. Which resource would be most directly useful for identifying which techniques to focus detection efforts on?

- A) The organization's firewall change log from the past six months
- B) The MITRE ATT&CK Group profile for the threat actor, which lists observed techniques
- C) A commercial antivirus vendor's daily signature update feed
- D) The organization's most recent vulnerability scan results

Correct Answer: B

Distractor Analysis:

- A is incorrect. Internal firewall change logs reflect the organization's own configuration history, not adversary technique usage patterns.
- B is correct. MITRE ATT&CK Group profiles document the specific techniques that named threat actor groups have been observed using, with citations to public intelligence reports. This is the authoritative source for building targeted detection rules against a specific adversary.
- C is incorrect. Antivirus signature feeds detect known malware files but do not provide technique-level intelligence about a specific threat actor's operational methods.
- D is incorrect. Vulnerability scan results identify weaknesses in the organization's environment but do not describe which techniques a specific threat actor uses.

---

## Question 7

Which phase of the intelligence lifecycle involves normalizing raw data from multiple sources into a consistent format and removing duplicate entries before analysis begins?

- A) Direction
- B) Collection
- C) Processing
- D) Dissemination

Correct Answer: C

Distractor Analysis:

- A is incorrect. Direction is the first phase where intelligence requirements are defined — what questions need answering.
- B is incorrect. Collection is the phase where raw data is gathered from sources such as threat feeds, OSINT, and internal telemetry. The data has not yet been normalized.
- C is correct. Processing converts raw data from disparate sources into a normalized, deduplicated, structured format that analysts can efficiently analyze. Without processing, analysts waste time reconciling inconsistent formats.
- D is incorrect. Dissemination is the final phase where finished intelligence is delivered to consumers in the appropriate format.

---

## Question 8

The Cyber Kill Chain model was criticized for which significant limitation compared to MITRE ATT&CK?

- A) The Kill Chain does not include a phase for credential theft
- B) The Kill Chain requires expensive licensing to use in a commercial SOC environment
- C) The Kill Chain is a linear model that does not effectively model post-compromise activity or non-linear attacks
- D) The Kill Chain only applies to attacks against critical infrastructure targets

Correct Answer: C

Distractor Analysis:

- A is incorrect. Credential theft can be mapped to the "Actions on Objectives" phase of the Kill Chain even if it is not an explicit standalone phase.
- B is incorrect. The Cyber Kill Chain is a publicly available framework with no licensing requirement.
- C is correct. The Kill Chain's linear structure assumes attackers follow a clean seven-phase progression, which does not reflect the complexity of modern intrusions. Attackers move between phases non-linearly, operate for extended dwell periods, and the Kill Chain provides limited technique-level detail for post-compromise activity. ATT&CK was designed to address these gaps.
- D is incorrect. The Kill Chain was originally designed around Advanced Persistent Threat intrusions and applies broadly to various attack types, not only critical infrastructure.

---

## Question 9

An analyst uses a threat intelligence report to identify that the attacker's known infrastructure includes the domain `update-cdn-pkg.info` and the IP range 203.0.113.0/24. The analyst blocks both the domain and the IP range at the perimeter. The attacker registers a new domain and moves to a new IP range within 48 hours. According to the Pyramid of Pain, what does this outcome indicate?

- A) The organization has successfully disrupted the attack at the TTP level
- B) Blocking domains and IP addresses provides low-lasting protection because these indicators are inexpensive for attackers to change
- C) The organization should have focused on blocking the attacker's file hashes instead
- D) The Pyramid of Pain predicts that blocking all indicators takes equal effort from the attacker

Correct Answer: B

Distractor Analysis:

- A is incorrect. The TTP level is the top of the Pyramid of Pain — blocking TTPs is the hardest for attackers to recover from. The attacker recovered in 48 hours, indicating the block was at a low pyramid level.
- B is correct. Domains and IP addresses sit in the lower-middle of the Pyramid of Pain. They are relatively easy and inexpensive for attackers to replace. Blocking them has value but provides only temporary disruption. This scenario directly illustrates the Pyramid of Pain's core lesson.
- C is incorrect. File hashes sit at the base of the Pyramid of Pain — they are even easier to change than domains and IPs. Switching to hash-blocking would provide even less durable protection.
- D is incorrect. The Pyramid of Pain explicitly models that different indicator types impose very different costs on attackers. Indicators at the base (hashes) are trivial to change; TTPs at the top are very costly to change.

---

## Question 10

STIX and TAXII are two complementary standards used in threat intelligence. Which statement correctly describes the role of each?

- A) STIX is the transport protocol; TAXII is the data format
- B) STIX defines the data format for expressing threat intelligence; TAXII is the protocol for sharing that data between systems
- C) STIX is used only for sharing malware samples; TAXII is used only for sharing network IOCs
- D) STIX and TAXII are proprietary standards owned by a commercial threat intelligence vendor

Correct Answer: B

Distractor Analysis:

- A is incorrect. This reverses the roles. STIX is the data format; TAXII is the transport protocol.
- B is correct. STIX (Structured Threat Information Expression) provides a standardized, machine-readable format for expressing threat intelligence content. TAXII (Trusted Automated Exchange of Intelligence Information) provides the transport mechanism for sharing STIX data between organizations and systems.
- C is incorrect. STIX can express any type of threat intelligence — actors, campaigns, TTPs, indicators, and more. Neither STIX nor TAXII is limited to a single indicator category.
- D is incorrect. Both STIX and TAXII are open, community-developed standards, not proprietary commercial products.

---

## Question 11 (5 points)

An analyst is reviewing a MITRE ATT&CK Group profile for a threat actor known to target financial institutions. The profile lists 23 techniques across 8 tactics. How should the analyst use this information most effectively to improve the organization's defenses?

- A) Block every IP address and domain listed in the group's infrastructure section
- B) Use the listed techniques to identify detection gaps by cross-referencing them against existing SIEM rules and visibility coverage
- C) Share the group profile publicly to warn other financial institutions immediately
- D) Implement a new IPS signature for each of the 23 techniques listed

Correct Answer: B

Distractor Analysis:

- A is incorrect. Blocking infrastructure IOCs provides temporary low-pyramid protection. The threat actor can trivially move to new infrastructure. The higher-value action is improving technique-level detection.
- B is correct. Cross-referencing the ATT&CK Group profile against existing detection coverage is a gap analysis — it identifies which of the adversary's known techniques the organization cannot currently detect or prevent, enabling prioritized detection engineering.
- C is incorrect. The profile may be marked TLP:AMBER or sourced from proprietary intelligence. Additionally, broad public sharing should follow applicable TLP markings and sharing agreements.
- D is incorrect. IPS signatures are network-level controls; many ATT&CK techniques describe host-based or non-network behaviors that cannot be addressed with IPS signatures alone.

---

## Question 12 (5 points)

Which ATT&CK tactic describes the phase in which an adversary attempts to avoid detection by disabling security tools, clearing logs, or masquerading malicious processes as legitimate ones?

- A) Persistence
- B) Defense Evasion
- C) Collection
- D) Exfiltration

Correct Answer: B

Distractor Analysis:

- A is incorrect. Persistence (TA0003) describes techniques used to maintain access across system reboots or credential changes — not to evade detection after access is gained.
- B is correct. Defense Evasion (TA0005) includes techniques such as disabling security software, clearing Windows Event Logs, masquerading process names, and using obfuscation to avoid detection. This is one of the most populated tactic categories in ATT&CK.
- C is incorrect. Collection (TA0009) describes techniques used to gather data of interest to the adversary prior to exfiltration. It does not involve evading detection mechanisms.
- D is incorrect. Exfiltration (TA0010) describes techniques used to move data out of the victim environment. Avoiding detection before exfiltration occurs falls under Defense Evasion.

---

## Question 13 (5 points)

A CTI analyst receives a report from an external partner with the TLP marking TLP:RED. Which action is appropriate?

- A) Share the report with the entire security team via the team Slack channel
- B) Add the indicators to the organization's public threat sharing platform (ISAC)
- C) Treat the information as restricted to the individuals present at the meeting or call for which it was shared, and do not distribute it further
- D) Forward the report to senior management for awareness since they have higher authority to handle sensitive intelligence

Correct Answer: C

Distractor Analysis:

- A is incorrect. TLP:RED prohibits sharing outside of the specific recipients identified by the original sharer. Distributing to the broader security team violates the marking.
- B is correct when understood in context: TLP:RED explicitly prohibits sharing beyond the named recipients. Sharing to a public platform is a direct violation.
- C is correct. TLP:RED is the most restrictive marking — information is strictly limited to the individuals who received it in the original communication. It must not be forwarded or shared in any way without explicit permission from the originator.
- D is incorrect. Seniority or authority does not override TLP markings. The restriction applies regardless of the recipient's organizational role.

---

## Question 14 (5 points)

In the Diamond Model of intrusion analysis, what do the four vertices represent?

- A) Reconnaissance, Weaponization, Delivery, Exploitation
- B) Adversary, Capability, Infrastructure, Victim
- C) Confidentiality, Integrity, Availability, Authentication
- D) Tactical, Operational, Strategic, Administrative

Correct Answer: B

Distractor Analysis:

- A is incorrect. These are the first four phases of the Cyber Kill Chain, not the Diamond Model vertices.
- B is correct. The Diamond Model describes every intrusion event using four vertices: the Adversary (who is attacking), the Capability (the tools and techniques used), the Infrastructure (the systems and networks leveraged), and the Victim (who is being attacked). These relationships help analysts pivot from known facts to unknown elements of an intrusion.
- C is incorrect. Confidentiality, Integrity, and Availability are the CIA Triad. Authentication is a security mechanism, not a CIA pillar or Diamond Model vertex.
- D is incorrect. These are CTI intelligence types based on time horizon and audience — not the Diamond Model structure.

---

## Question 15 (5 points)

An analyst wants to programmatically ingest a threat intelligence feed and automatically create SIEM rules when new indicators are published. Which two standards enable this automation pipeline?

- A) CVSS and EPSS
- B) STIX and TAXII
- C) MITRE ATT&CK and the Cyber Kill Chain
- D) TLP and ISAC

Correct Answer: B

Distractor Analysis:

- A is incorrect. CVSS (Common Vulnerability Scoring System) and EPSS (Exploit Prediction Scoring System) are vulnerability scoring standards, not threat intelligence exchange formats.
- B is correct. STIX provides the machine-readable format for expressing threat intelligence (IOCs, TTPs, campaigns, actors), and TAXII provides the transport protocol for automated delivery of that data between systems. Together they enable the described automation pipeline.
- C is incorrect. MITRE ATT&CK and the Cyber Kill Chain are conceptual frameworks for understanding adversary behavior. They are not data exchange protocols and do not support automated indicator ingestion.
- D is incorrect. TLP is a sharing classification marking, not a data format. ISAC (Information Sharing and Analysis Center) is an organization type, not a technical standard.

---

## Question 16 (5 points)

Which of the following best describes the purpose of the ATT&CK sub-technique structure?

- A) Sub-techniques represent entirely separate attack chains that are independent of their parent technique
- B) Sub-techniques provide more specific implementation details of a parent technique, enabling more precise detection rule development
- C) Sub-techniques are only applicable to nation-state threat actors and do not apply to cybercriminal groups
- D) Sub-techniques replace the parent technique ID and should not be cited together

Correct Answer: B

Distractor Analysis:

- A is incorrect. Sub-techniques are not independent attack chains. They are specific variations of a parent technique — the parent and sub-technique share the same tactic context.
- B is correct. Sub-techniques (identified by a decimal extension, e.g., T1547.001) specify how a parent technique is implemented. For example, T1547 covers Boot or Logon Autostart Execution; T1547.001 specifies Registry Run Keys specifically. This granularity enables more targeted detection rules.
- C is incorrect. ATT&CK applies to all threat actors — nation-state, cybercriminal, hacktivist, and others. Sub-techniques are documented across all group types.
- D is incorrect. Both the parent technique and the sub-technique ID are cited together in ATT&CK documentation and are used together in threat intelligence reports and detection mapping exercises.

---

## Question 17 (5 points)

An analyst is writing a detection rule for a specific ATT&CK technique. Which data source listed in the ATT&CK technique entry tells the analyst where to look in their log environment?

- A) The Mitigations section
- B) The Detection section, which lists relevant data sources and component types
- C) The Procedure Examples section, which lists specific malware families
- D) The Groups section, which lists known threat actors using the technique

Correct Answer: B

Distractor Analysis:

- A is incorrect. The Mitigations section lists defensive controls that can prevent the technique — not the data sources an analyst needs to detect it.
- B is correct. The Detection section of an ATT&CK technique entry lists the relevant data sources (e.g., Process, Network Traffic, File) and data components (e.g., Process Creation, Network Connection Creation) that analysts should monitor to detect the technique. This is the starting point for detection engineering.
- C is incorrect. Procedure Examples document specific malware or tool implementations of the technique. They provide useful context but do not describe what log sources to enable.
- D is incorrect. The Groups section identifies threat actors who have used the technique. It informs threat modeling and actor-specific hunting but does not describe detection data sources.

---

## Question 18 (5 points)

A threat intelligence report describes a campaign where attackers send spear-phishing emails containing malicious Microsoft Office documents with embedded macros that execute PowerShell commands upon opening. Which ATT&CK tactic does the PowerShell execution represent?

- A) Initial Access
- B) Execution
- C) Persistence
- D) Lateral Movement

Correct Answer: B

Distractor Analysis:

- A is incorrect. Initial Access (TA0001) describes how the attacker first enters the environment — in this case, the spear-phishing email (T1566.001) represents Initial Access. The PowerShell execution occurs after access is achieved.
- B is correct. Execution (TA0002) describes techniques that run adversary-controlled code on a local or remote system. PowerShell (T1059.001) is a canonical Execution technique. Running the macro-launched PowerShell script is an Execution action.
- C is incorrect. Persistence describes maintaining access across system events. Simply executing PowerShell does not establish persistence — additional actions like creating a scheduled task would be required.
- D is incorrect. Lateral Movement describes moving between systems in the environment. The PowerShell execution described occurs on the initially compromised host, not on a secondary target.

---

## Question 19 (5 points)

Which intelligence lifecycle phase involves evaluating collected data for source reliability and determining whether it answers the original intelligence requirement?

- A) Direction
- B) Processing
- C) Analysis
- D) Dissemination

Correct Answer: C

Distractor Analysis:

- A is incorrect. Direction is the first phase — it defines the intelligence requirements and questions that the CTI effort must answer. It does not evaluate collected data.
- B is incorrect. Processing normalizes and deduplicates raw data so it can be efficiently analyzed. It converts data into a workable format but does not answer the intelligence question or evaluate reliability.
- C is correct. Analysis is the phase where processed data is examined for reliability, relevance, and meaning. Analysts evaluate source credibility, corroborate findings across sources, and produce judgments that answer the original requirement. This is the core intellectual work of CTI.
- D is incorrect. Dissemination delivers finished intelligence to consumers. It occurs after analysis is complete.

---

## Question 20 (5 points)

A cybersecurity team creates a heat map showing which ATT&CK techniques they have active detections for versus which ones have no coverage. What is this activity called?

- A) Threat actor profiling
- B) ATT&CK Navigator gap analysis
- C) Incident response planning
- D) Vulnerability remediation prioritization

Correct Answer: B

Distractor Analysis:

- A is incorrect. Threat actor profiling involves researching a specific adversary's known techniques, infrastructure, and targets — not mapping the defender's own detection coverage.
- B is correct. The ATT&CK Navigator is the official tool for creating technique heat maps. Using it to compare existing detection coverage against the full technique matrix — identifying covered versus uncovered techniques — is known as a gap analysis. This is a core threat-informed defense activity.
- C is incorrect. Incident response planning defines procedures for handling confirmed incidents. It does not involve mapping detection coverage against the ATT&CK matrix.
- D is incorrect. Vulnerability remediation prioritization involves ranking patching actions based on CVSS scores, exploitability, and asset criticality — a separate vulnerability management activity.
