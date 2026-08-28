# Video Script: Module 11 — Incident Response (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 11 | Texas Wesleyan University"]**

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome to Module 11 — Incident Response.

Somewhere in the world right now, a security incident is in progress. A company's endpoint detection system just flagged a suspicious process. An employee opened a phishing attachment. A database is being exfiltrated. The organization's response in the next sixty minutes will determine whether this becomes a contained inconvenience or a front-page breach.

Incident response is the structured process that turns chaos into control. Done well, it limits damage, preserves evidence for prosecution or litigation, and produces lessons that prevent recurrence. Done poorly, it creates additional legal exposure, destroys forensic evidence, and fails to contain the attacker.

The Security+ exam devotes significant coverage to incident response in Domain 4. You need to know the lifecycle phases, the roles on an IR team, communication obligations, and evidence handling. In Part 1 we will cover the lifecycle and team structure. In Part 2 we will go deep on evidence handling, containment decisions, and the lessons learned process.

---

## Section 1 — Why Incident Response Exists

**[SHOW SLIDE: Cost of a breach statistics graphic]**

No security control is perfect. Attackers are creative, persistent, and well-resourced. The question is not whether your organization will experience an incident — it is whether you will respond effectively when you do.

The IBM Cost of a Data Breach 2023 report found that organizations with a formal IR team and regularly tested IR plan saved an average of $1.49 million per breach compared to organizations without one. They also contained breaches 54 days faster. Those are not small numbers.

Incident response without a plan is triage without a doctor. People improvise, evidence gets destroyed, communication channels break down, and the attacker has time to cover their tracks. A tested incident response plan is one of the highest-ROI investments in a security program.

---

## Section 2 — NIST SP 800-61 IR Lifecycle

**[SHOW SLIDE: NIST IR lifecycle diagram — four phases in a cycle]**

The authoritative reference for incident response in the Security+ exam and in the field is NIST Special Publication 800-61, Computer Security Incident Handling Guide. NIST defines four phases that form a continuous cycle.

**Phase 1 — Preparation**

Preparation is everything that happens before an incident. This includes establishing and training the IR team, creating the IR plan and playbooks, deploying monitoring and detection tools, building communication trees, and testing the plan through tabletop exercises and simulations.

The Security+ exam tests preparation in terms of what tools and documents must exist before an incident occurs. Think: IR playbooks, contact lists, escalation procedures, legal counsel contacts, and pre-authorized forensic tools staged on response media.

**Phase 2 — Detection and Analysis**

Detection begins with identifying indicators of compromise (IOCs). IOCs are observable artifacts that indicate a system may have been compromised. Examples include unusual outbound connections, failed login spikes, new scheduled tasks created by non-admin accounts, files with random names in temp directories, and hash values matching known malware.

Precursors are signals that an attack may be imminent — port scanning, reconnaissance activity, or a known threat actor targeting your sector. Precursors are harder to act on but should inform heightened monitoring.

Analysis involves correlating events to determine whether an event is a true incident or a false positive. The Security+ exam tests the difference between events, alerts, and incidents.

- An **event** is any observable occurrence in a system or network.
- An **alert** is an event that a security tool has flagged as potentially significant.
- An **incident** is an event that violates security policy or poses a threat to confidentiality, integrity, or availability.

Not every alert is an incident. Analysis must determine the severity and scope of confirmed incidents and assign a priority level.

---

## Section 3 — Incident Categories and Prioritization

**[SHOW SLIDE: Incident severity matrix — impact vs. urgency]**

IR teams use severity levels to prioritize response effort. NIST suggests a four-level scale: Low, Medium, High, Critical. The criteria for each level depend on business impact — what systems are affected, what data is involved, and how many users are impacted.

Incident categories tested on Security+ include:

- **Malware infection**: Ransomware, trojans, worms, spyware.
- **Unauthorized access**: Account compromise, privilege escalation, external intrusion.
- **Denial of service**: Volumetric DDoS, application-layer DoS.
- **Data exfiltration**: Sensitive data leaving the organization without authorization.
- **Insider threat**: Malicious or accidental damage by an employee or contractor.
- **Social engineering**: Phishing, pretexting, business email compromise.

---

## Section 4 — Phase 3: Containment

**[SHOW SLIDE: Containment decision tree — short-term vs. long-term]**

Once an incident is confirmed, the team must contain it. Containment stops the spread before eradication and recovery. NIST distinguishes between short-term and long-term containment.

**Short-term containment** applies immediate measures to halt damage. Examples include isolating a compromised host from the network by disabling its network interface, blocking a source IP at the firewall, or locking a compromised account. The goal is to stop ongoing harm quickly, even if the system remains unusable.

**Long-term containment** involves stable interim measures that allow business operations to continue while the team prepares for eradication. This may include temporarily replacing a compromised server with a clean backup, applying compensating controls to exposed systems, or redirecting traffic to block attacker infrastructure.

A critical decision in containment is: **should we pull the plug?** Hard shutdown destroys volatile memory — RAM — which may contain decryption keys for ransomware, injected code, network connections, and malware artifacts that exist only in memory. Forensic investigators generally prefer a memory dump and then graceful shutdown to preserve volatile evidence.

---

## Section 5 — Phase 3 Continued: Eradication and Recovery

**[SHOW SLIDE: Eradication and recovery phase diagram]**

**Eradication** removes the root cause of the incident. This means removing malware, closing the exploited vulnerability, eliminating backdoors the attacker installed, and resetting credentials. Eradication must be thorough — partial eradication allows attackers to maintain persistence.

**Recovery** restores systems to normal operation. This involves restoring from clean backups, rebuilding compromised systems from known-good images, re-enabling accounts with new credentials, and validating that systems are clean before returning them to production.

Recovery must include verification. Simply restoring a backup does not mean the restored system is clean if the backup was made after the compromise. Restoration from pre-incident clean backups is critical.

---

## Section 6 — IR Team Roles

**[SHOW SLIDE: IR team org chart]**

The Security+ exam tests roles on an incident response team. Key roles include:

- **IR Manager / Team Lead**: Coordinates the overall response, makes escalation decisions, communicates with leadership.
- **Incident Handler / Analyst**: Performs technical investigation, triage, and containment actions.
- **Forensic Investigator**: Collects and analyzes evidence. Maintains chain of custody. Must remain independent from remediation activities to preserve evidence integrity.
- **Legal Counsel**: Advises on evidence preservation obligations, regulatory notification requirements, and legal exposure. Should be involved early.
- **Communications Lead / Public Affairs**: Manages communications with customers, media, and regulators.
- **Human Resources**: Involved when insider threat is suspected.
- **IT / System Administrators**: Provide system access, perform technical remediation under IR direction.
- **Executive Sponsor (CISO / CIO)**: Provides authority and resource allocation. Decides on business impact trade-offs.

In smaller organizations, one person may fill multiple roles. The critical principle is that forensic collection should be separate from remediation to avoid contaminating evidence.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

We have covered the NIST IR lifecycle and the four phases — Preparation, Detection and Analysis, Containment, and Eradication and Recovery. We also looked at IR team roles and the critical incident categorization and prioritization decisions that shape how a team responds.

In Part 2, we go deeper into communication plans, evidence preservation, chain of custody, and the lessons learned process. These are the parts of IR that often determine legal outcomes and whether the organization improves after an incident.

See you in Part 2.

---

*End of Part 1*
