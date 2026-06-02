# Video Script: Module 01 - Security Operations & Analyst Role

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University
## Instructor: Professor Nash
## Estimated Duration: 20-24 minutes
## CySA+ CS0-003 Domain Alignment: Domain 1 - Security Operations (33%)

---

### [00:00 - 01:30] Cold Open and Welcome

Professor Nash on camera. Title card: **Module 01 — Security Operations and the Analyst Role**.

"Welcome to CIS-4332, Cyber Analyst. I'm Professor Nash, and this course is built around one certification that will open doors in the cybersecurity industry: CompTIA CySA+, exam code CS0-003. Before we touch a single tool or write a single query, we need to understand the environment you're going to work in — the Security Operations Center — and your place inside it as an analyst.

This module sets the foundation for every other module in this course. We will cover how a SOC is structured, what analysts actually do day to day, how alerts move through a tiered response model, and how the fundamental principles of security — the CIA Triad — drive every decision you make. Let's get started."

---

### [01:30 - 04:00] What Is a Security Operations Center?

"A Security Operations Center, or SOC, is the nerve center of an organization's cybersecurity program. Think of it as a 24-hours-a-day, 7-days-a-week monitoring station where trained analysts watch for signs of attack, investigate suspicious activity, and coordinate the response when something goes wrong.

The SOC is not a product. It is not a piece of software. It is a combination of people, processes, and technology working together. Let me break that down.

The **people** are the analysts — Tier 1, Tier 2, and Tier 3 — plus managers, threat hunters, and incident responders. The **processes** are the documented workflows, playbooks, and escalation procedures that tell analysts exactly what to do when they see a specific type of alert. The **technology** is the stack of tools the SOC uses: Security Information and Event Management platforms, Endpoint Detection and Response tools, network monitoring sensors, and threat intelligence feeds.

The SOC does not replace an IT department. The IT team builds and maintains systems. The SOC watches those systems for threats."

[SHOW DIAGRAM: Three concentric circles labeled People (center), Process (middle ring), Technology (outer ring). Arrow pointing inward labeled "SOC Mission: Detect, Respond, Recover."]

---

### [04:00 - 07:30] The Tiered Analyst Model

"Inside the SOC, analysts are organized into tiers based on their experience and the complexity of the work they handle. The CySA+ exam will test you on this model, so know it cold.

**Tier 1 — Alert Monitor.** Tier 1 analysts are on the front line. They watch the SIEM alert queue, apply the documented playbook to each alert, and make the first determination: is this a false positive or a true positive? False positives are alerts that fired but don't represent real malicious activity. True positives are real threats. Tier 1's job is to filter the noise, document findings, and escalate confirmed incidents. Tier 1 analysts typically work from runbooks — step-by-step procedures for specific alert types — so they can be consistent even when they're new.

**Tier 2 — Incident Responder.** When Tier 1 escalates a confirmed incident, Tier 2 takes over. These analysts have deeper technical skills. They perform deeper investigation, correlate events across multiple data sources, contain the threat, and manage the incident to closure. They also write incident reports.

**Tier 3 — Threat Hunter and SME.** Tier 3 analysts are the most experienced. They proactively hunt for threats that haven't triggered any alert yet. They build new detection rules, analyze malware, and serve as subject matter experts for the rest of the team. They also feed findings back to improve Tier 1 playbooks.

There is one more role worth mentioning: the **SOC Manager**. This person owns the program — staffing, metrics, reporting to leadership, and coordinating with legal and HR during major incidents.

For the CySA+ exam, the key concept is that escalation flows upward — Tier 1 to Tier 2 to Tier 3 — and knowledge flows downward, as senior analysts improve the playbooks and rules that Tier 1 uses."

[SHOW DIAGRAM: Vertical pyramid with three labeled tiers. Tier 1 at base: "Alert Triage, Playbook Execution, False Positive Filtering." Tier 2 in middle: "Deep Investigation, Containment, Incident Management." Tier 3 at top: "Threat Hunting, Rule Development, Forensics." Arrows: upward labeled "Escalation," downward labeled "Knowledge Transfer."]

---

### [07:30 - 11:00] The CIA Triad and Why It Drives Every Decision

"Everything a SOC analyst does connects back to one foundational model: the CIA Triad. The three letters stand for Confidentiality, Integrity, and Availability. Understanding the CIA Triad is not just an exam requirement — it is the lens you use to understand what an attacker is trying to do and what damage has been done.

**Confidentiality** means ensuring that information is accessible only to those who are authorized to see it. When an attacker exfiltrates sensitive data — customer records, intellectual property, credentials — they are attacking confidentiality. Controls that protect confidentiality include encryption, access controls, data loss prevention tools, and need-to-know policies.

**Integrity** means ensuring that data has not been altered without authorization. When an attacker modifies a financial record, tampers with log files to cover their tracks, or injects malicious code into a software update, they are attacking integrity. Controls that protect integrity include hashing, digital signatures, file integrity monitoring, and change management processes.

**Availability** means ensuring that systems and data are accessible when legitimate users need them. Ransomware attacks, denial-of-service attacks, and destructive malware all target availability. Controls that protect availability include redundancy, backups, failover systems, and rate limiting.

Here is the exam trap to watch for: a question will describe an attack scenario and ask which pillar of the CIA Triad was violated. Train yourself to ask: did the attacker view something they shouldn't have? That's confidentiality. Did they change something? That's integrity. Did they prevent access to something? That's availability."

[SHOW DIAGRAM: Triangle with "Confidentiality" at top vertex, "Integrity" at bottom-left vertex, "Availability" at bottom-right vertex. Example attack types listed beside each vertex. Encryption and access controls beside Confidentiality. Hashing and file integrity monitoring beside Integrity. Redundancy and backups beside Availability.]

---

### [11:00 - 14:30] Data Sources and the SIEM

"A SOC analyst's job depends entirely on the quality and completeness of the data they receive. Let's talk about the primary data sources and how they flow into the SIEM.

**Firewall logs** record every connection attempt — allowed and denied — at the network perimeter. They tell you source IP, destination IP, port, protocol, and whether the connection was permitted. If you see thousands of connection attempts from a single external IP to port 22 (SSH), that pattern in the firewall logs suggests a brute-force scan.

**Authentication logs** come from systems like Active Directory, LDAP, and cloud identity providers. They tell you who logged in, from where, at what time, and whether the attempt succeeded or failed. A spike in failed authentication events followed by a success from the same account is a classic brute-force success pattern.

**Endpoint logs** come from workstations and servers — Windows Event Logs, process creation logs, registry change logs, and host-based firewall logs. They tell you what programs ran, what files were created or deleted, and what network connections were made from each machine.

**Network traffic data** comes from intrusion detection systems, NetFlow collectors, and packet capture appliances. It tells you what is moving across the network at the protocol level.

**Application logs** come from web servers, databases, email gateways, and custom applications. They tell you what users and systems are doing inside specific applications.

All of these sources feed into the SIEM. The SIEM's job is to aggregate logs from every source, normalize them into a common format, apply correlation rules, and generate alerts when those rules fire.

The critical distinction the exam tests: the SIEM aggregates and alerts — it does not block traffic. Blocking is done by the IPS, the firewall, or the EDR tool acting on a containment instruction from an analyst."

[SHOW SCREEN: Mock SIEM dashboard with labeled panels: "Alert Queue" showing 3 high-severity alerts, "Top Source IPs" bar chart, "Authentication Failures Over Time" line graph, "Log Source Health" green/red status indicators for Firewall, AD, Endpoint, and Network sources.]

---

### [14:30 - 17:30] Alert Triage Workflow

"Let's walk through what actually happens when a Tier 1 analyst receives an alert. This workflow is tested directly on the CySA+ exam, and you will practice it in this module's lab.

Step 1: **Review the alert details.** The analyst reads the alert — what rule fired, what the severity is, what the source and destination are, and what the timestamp is.

Step 2: **Gather context.** The analyst pulls supporting data. They check the full log context around the event. They look up the source IP against threat intelligence feeds to see if it's a known malicious address. They check whether the affected user or system is known to perform this type of activity — for example, an administrator account that regularly performs administrative tasks.

Step 3: **Determine true positive or false positive.** Based on the context gathered, the analyst decides: is this real? A true positive means the alert represents actual malicious or suspicious activity. A false positive means the alert fired but the activity is legitimate and authorized.

Step 4: **Document the finding.** Whether it's a true positive or false positive, the analyst documents their reasoning in the ticketing system. This documentation is critical for audit purposes and for improving the detection rules later.

Step 5: **Escalate or close.** True positives are escalated to Tier 2 with the full documentation attached. False positives are closed with a note explaining why, which may trigger a tuning request to reduce that alert type in the future.

One more classification pair worth knowing: **false negative** means a real attack occurred but the SIEM did not generate an alert. This is the most dangerous scenario — you had no visibility into the attack. **True negative** means there was no attack and no alert fired. That is the desired state.

The four combinations — true positive, false positive, false negative, true negative — appear on the CySA+ exam in scenario questions. Memorize them."

---

### [17:30 - 20:00] Indicators of Compromise and Indicator Types

"When a Tier 1 analyst confirms a true positive, they are working with evidence. In the SOC, we call these pieces of evidence Indicators of Compromise, or IOCs. An IOC is any observable artifact that suggests a system has been compromised or is being attacked.

Common IOC types include:

**File-based IOCs**: Cryptographic hashes (MD5, SHA-1, SHA-256) of known malicious files. If a file on a workstation matches the hash of a known piece of malware, that's a file-based IOC.

**Network-based IOCs**: IP addresses, domain names, and URLs associated with malicious infrastructure. Command-and-control server IPs, phishing domains, and malicious download URLs all fall here.

**Host-based IOCs**: Registry key modifications, scheduled task creations, abnormal process names, and persistence mechanisms observed on a specific endpoint.

**Behavioral IOCs**: Patterns of behavior — a process spawning a command shell, unusual outbound connections at 3 AM, a user downloading gigabytes of data from a file share they normally don't access.

The exam also tests the concept of the **Pyramid of Pain**, developed by David Bianco. At the base of the pyramid are hash values — easy for defenders to detect, easy for attackers to change. At the top are Tactics, Techniques, and Procedures, or TTPs — hard for defenders to detect, but very hard for attackers to change. When a SOC blocks at the TTP level, they make it genuinely painful for an attacker to continue. We will dig deeply into TTPs when we reach Module 02 on MITRE ATT&CK."

---

### [20:00 - 22:30] Metrics, Communication, and the Analyst Mindset

"A well-run SOC measures its own performance. Key metrics that a CySA+ analyst should understand include Mean Time to Detect, or MTTD — how long from when a threat enters the environment until the SOC identifies it. Mean Time to Respond, or MTTR — how long from detection until the threat is contained or remediated. False positive rate — what percentage of alerts turn out to not be real threats. Dwell time — how long an attacker was active in the environment before being detected.

These metrics matter because they drive improvement. A high MTTD suggests detection rules need tuning. A high false positive rate suggests rules are too broad. High dwell time suggests the organization is missing indicators.

Finally, I want to address the analyst mindset. The CySA+ exam is not just about tools and commands. It tests your judgment — your ability to look at ambiguous data and make a prioritized, justified decision. The best analysts are skeptical, thorough, and systematic. They do not jump to conclusions. They gather evidence, consider alternatives, and document their reasoning.

For study resources aligned to this exam, I recommend CompTIA's official study materials at comptia.org and Professor Messer's free study guides and practice exams at professormesser.com. Professor Messer has specific CS0-003 videos aligned to every exam objective, and they are free."

---

### [22:30 - 24:00] Module Summary and Lab Preview

"Let's bring it together. In this module you learned:

- The SOC is built on people, process, and technology working in concert.
- The tiered analyst model — Tier 1 triage, Tier 2 investigation and response, Tier 3 hunting and development.
- The CIA Triad — Confidentiality, Integrity, and Availability — is the framework that defines what we are protecting and what attackers are targeting.
- The SIEM aggregates logs, applies correlation rules, and generates alerts. It does not block traffic.
- Alert triage follows a five-step workflow: review, gather context, determine TP or FP, document, and escalate or close.
- IOCs are observable artifacts of compromise, classified as file-based, network-based, host-based, or behavioral.

In this module's lab, you will trace a mock SOC alert from initial trigger through the triage workflow, classify a set of IOCs, and document your findings in the format a Tier 1 analyst would use. That documentation is the deliverable.

Read the Reading Guide before starting the lab. Take the quiz after completing both. Post to the discussion board by Wednesday.

I'll see you in Module 02, where we dive into MITRE ATT&CK and Cyber Threat Intelligence. It is one of the most important modules in this course. Get ready."

---

End of Module 01 Video Script

Study Resources: comptia.org | professormesser.com
