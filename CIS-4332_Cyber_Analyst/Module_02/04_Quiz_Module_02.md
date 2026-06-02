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
