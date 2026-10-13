# Video Script: Module 11 — Incident Response (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Incident Response Team Roles (4 minutes)

Welcome back. In Part 1 we covered the NIST IR lifecycle and IR plan components. Now we look at the people, communication, evidence handling, and the lessons learned process.

Effective incident response requires a team, not a solo hero. The Incident Response Team (IRT) — sometimes called the Computer Security Incident Response Team (CSIRT) or Computer Emergency Response Team (CERT) — is the organized group that executes the IR plan. Understanding the roles is an exam requirement.

### Incident Response Team Structure

**Incident Response Manager / Incident Commander**

This person leads the response. During an incident, they are the single authority who makes tactical decisions, coordinates the team, and ensures the response follows the plan. The incident commander prevents the chaos of everyone doing different things simultaneously without coordination. They track the incident timeline, own the incident report, and brief leadership.

**Security Analysts (L1, L2, L3)**

Analysts perform the hands-on technical work: triage alerts, analyze logs, investigate affected systems, identify indicators of compromise (IOCs), and execute containment and eradication steps. In larger organizations, L1 analysts handle initial triage; L2 analysts handle deeper investigation; L3 analysts handle the most complex cases and often have forensics skills.

**Threat Intelligence Analyst**

Correlates current incident indicators against threat intelligence feeds, known threat actor TTPs (Tactics, Techniques, and Procedures), and dark web monitoring to identify who is attacking you and how they operate. May interface with external threat intelligence providers and ISACs (Information Sharing and Analysis Centers).

**Digital Forensics Specialist**

Performs evidence collection, disk imaging, memory capture, and forensic analysis. Responsible for maintaining chain of custody on all evidence. We will cover their work in detail in Module 12.

**Legal Counsel**

Advises on legal obligations during the incident: when to notify regulators, how to communicate with law enforcement, what disclosures are required, and how to preserve evidence for potential litigation. Legal counsel should be involved in all external communications. Their involvement also protects communications under attorney-client privilege in some jurisdictions.

**Public Relations / Communications**

Manages external communications: press statements, customer notifications, regulatory notifications. Works closely with legal. All external communications about the incident should be reviewed by both legal and PR before release.

**Executive Liaison / CISO**

Bridges the IR team and executive leadership. Provides regular status updates to the CEO, CIO, and board. Makes resource decisions (authorizing emergency spend, calling in external IR vendors, engaging cyber insurance).

**Human Resources**

Involved when the incident involves an insider threat or requires employee-related actions (account suspension, termination, law enforcement referral for employees).

**Third-Party IR Vendor (External Responders)**

Many organizations retain a cyber incident response firm (CrowdStrike, Mandiant/Google, Palo Alto Unit 42, KPMG, etc.) either on retainer or engaged when the internal team is overwhelmed. External responders bring specialized expertise, tooling, and capacity. Cyber insurance policies often provide access to an approved IR vendor list.

### Virtual vs. Dedicated Teams

Not every organization has the resources for a full-time dedicated CSIRT. Many organizations use a **virtual CSIRT** — a designated set of people from across the organization (IT, legal, HR, communications, business units) who have defined IR roles but work their normal jobs between incidents. The key is that roles are pre-assigned and people are trained before the incident happens.

---

## Segment 2 — Communication During Incidents (3 minutes)

Communication failures are one of the most common reasons incident responses go poorly. There are two communication dimensions: internal and external.

### Internal Communication

**Dedicated out-of-band communication channel** — Do not use the same email and chat systems that may be compromised. Attackers who have access to your email can monitor your response. Establish a dedicated communication channel before an incident: a separate Slack workspace, an out-of-band phone bridge, or an emergency Microsoft Teams tenant with its own admin credentials.

**Need-to-know principle** — Incident details should be shared on a need-to-know basis. Widespread internal communication about a breach can cause panic, trigger unauthorized actions, or inadvertently alert an insider threat who is part of the incident.

**Regular cadence updates** — The incident commander should provide status updates to executive leadership on a defined schedule (every two to four hours during an active incident). This prevents leadership from calling analysts directly and disrupting the response.

**Incident documentation in real time** — All actions taken during the incident must be documented with timestamps. This is not just for the lessons learned report — it is evidence. Use a ticketing system or dedicated incident log. Recreating a timeline from memory after the fact is unreliable.

### External Communication

**Regulatory notifications** — Many regulations impose strict deadlines for breach notification. GDPR requires notification to a supervisory authority within 72 hours of discovering a breach. US state laws vary: California (CCPA), Texas, New York, and others all have specific timelines and content requirements. The IR plan must document which regulations apply and their deadlines.

**Customer/stakeholder notifications** — Notify affected individuals as required by law and as soon as practical. Communications should be factual, non-speculative, and reviewed by legal counsel. Do not promise what has not happened ("no credit card data was taken") unless you are certain.

**Law enforcement** — Contact FBI or local law enforcement when crimes are suspected. Some organizations are reluctant due to concerns about losing control of the investigation or public disclosure. Legal counsel should advise. Law enforcement can provide threat intelligence and may have investigative resources unavailable to the private sector.

**Media/press** — All media inquiries must go through the designated spokesperson (PR or legal). No technical staff should speak to media without explicit authorization. An unauthorized statement by a technical responder can be legally problematic and create inaccurate public narratives.

---

## Segment 3 — Evidence Preservation and Chain of Custody (4 minutes)

Evidence handling is one of the most critical and most frequently mishandled aspects of incident response. Poor evidence handling can make digital evidence inadmissible in court, eliminate the ability to determine what happened, and expose the organization to legal liability.

### Principles of Evidence Preservation

**Do not modify the evidence.** Every action you take on a potentially compromised system changes that system. Running a malware scanner, opening files, even booting the system can alter timestamps, overwrite volatile memory, and modify logs. This is why forensic analysis is performed on copies of evidence, not originals.

**Document everything before touching.** Before any action is taken on an affected system, document its state: take photographs or screenshots, record the system's running state, document the time and current user session, note any unusual processes or network connections.

**Collect volatile evidence first.** Volatile data — data that will be lost when the system is powered off — must be collected before shutdown. This includes:

- Running processes (process list, open files, network connections)
- System memory (RAM contains malware artifacts, decrypted data, running processes, and credentials)
- Currently logged-in users
- Open network connections
- Command history

The order of volatility (most volatile to least volatile):

1. CPU registers and cache
2. RAM (system memory)
3. Swap space / virtual memory
4. Network state (open connections, ARP cache)
5. Running processes
6. File system (temporary files, log files)
7. Disk storage (persistent files)
8. Remote logs and backup media

**Create forensic images.** Before performing any analysis, create a bit-for-bit forensic image of all storage media. Analyze the image, never the original. We will cover imaging tools in Module 12.

### Chain of Custody

Chain of custody is the documentation that tracks who collected evidence, who handled it, where it was stored, and who accessed it at every step. Without an unbroken chain of custody, digital evidence may be challenged as having been tampered with or contaminated, potentially rendering it inadmissible in legal proceedings.

A chain of custody document must include:

- **Evidence identifier** — a unique label assigned to each piece of evidence
- **Description** — what the item is (laptop, USB drive, server, forensic image file)
- **Collection date, time, and location** — exactly when and where the item was collected
- **Collected by** — name, title, and signature of the person who collected it
- **Transfer records** — every time the evidence changes hands: who transferred it, who received it, when, and why
- **Storage location** — where the evidence is physically stored (evidence room, secure server, offsite facility)
- **Access log** — every time someone accesses the evidence for analysis

Physical evidence (hardware, storage media) is typically stored in sealed, tamper-evident bags with labels. Digital evidence (forensic images) is stored with cryptographic hashes (MD5 and SHA-256) recorded at the time of collection. Any hash mismatch when the evidence is later verified indicates possible tampering.

### Legal Considerations for Evidence

**Do not exceed your authorization.** In the course of investigation, you may encounter systems you do not own (employee personal devices, third-party systems). Accessing those systems without proper authorization may be illegal. Consult legal counsel.

**Preserve logs before they are overwritten.** Log retention periods are often short. If a cloud provider retains security logs for only 90 days and the incident is discovered at 91 days, critical evidence is gone. IR plans should include procedures for immediately preserving logs from all relevant sources at the start of an investigation.

**Criminal vs. civil proceedings have different standards.** Evidence for criminal prosecution must meet higher standards than evidence for civil litigation or internal HR proceedings. If criminal prosecution is anticipated, engage law enforcement and follow their guidance on evidence handling.

---

## Segment 4 — Lessons Learned (4 minutes)

The lessons learned process is the mechanism by which an organization improves after each incident. It is not a blame session — it is an analytical process aimed at identifying systemic failures and implementing improvements.

### The Lessons Learned Meeting

The meeting should be held within two weeks of incident resolution, while details are fresh. Attendees should include all members of the IR team, the business unit(s) affected, and management. The agenda covers:

1. **Incident timeline review** — Walk through what happened, in chronological order. When was the initial compromise? When was it detected? How long was the attacker present?

2. **Root cause analysis** — What vulnerability, misconfiguration, or process failure allowed the incident to occur? Use the "five whys" technique to get to the underlying cause, not just the surface symptom.

3. **What worked well** — Acknowledge controls and responses that functioned as intended. This is important for team morale and for identifying practices worth standardizing.

4. **What did not work** — Identify gaps: detection was too slow, containment took too long, communication broke down, the runbook was missing a step.

5. **Improvement actions** — For each gap, assign a specific action, an owner, and a deadline. These actions should be tracked through to completion.

### The Incident Report

The formal incident report documents the incident for multiple audiences: executive leadership, the board, regulators, legal counsel, and the IR team's own records. A complete incident report includes:

- **Executive summary** — one page, non-technical, impact-focused
- **Incident timeline** — detailed chronological reconstruction of events
- **Impact assessment** — what data was accessed or exfiltrated, what systems were affected, what was the operational and financial impact
- **Root cause analysis** — documented finding of underlying cause
- **Response effectiveness** — what the IR team did well and where gaps were identified
- **Recommendations** — prioritized list of improvements with owners and timelines
- **Evidence inventory** — list of all evidence collected with chain of custody status

### Mean Time to Detect and Mean Time to Respond

Two metrics are commonly tracked to assess IR program maturity:

**MTTD (Mean Time to Detect)** — the average time between when an attacker establishes initial access and when the organization detects the intrusion. Industry research consistently finds MTTD to be shockingly long: the global average has historically exceeded 200 days for advanced persistent threat (APT) intrusions. Every day of undetected access is additional time for the attacker to move laterally, exfiltrate data, and establish persistence.

**MTTR (Mean Time to Respond/Recover)** — the average time from incident detection to full recovery. This includes containment, eradication, and restoration.

Tracking these metrics over time allows security leadership to demonstrate program improvement and benchmark against industry peers.

---

## Module 11 Full Summary

Incident response is a lifecycle, a team, a set of communications protocols, and an improvement engine:

- NIST 800-61 defines four phases: Preparation, Detection and Analysis, Containment/Eradication/Recovery, and Post-Incident Activity
- IR team roles: incident commander, analysts, threat intelligence, forensics, legal, PR, executive liaison, HR, and optional external IR vendors
- Internal communication requires out-of-band channels and need-to-know discipline; external communication requires legal review and regulatory deadline awareness
- Evidence preservation follows the order of volatility; forensic images are analyzed, not originals
- Chain of custody documentation tracks every transfer and access of evidence with timestamps and signatures
- Lessons learned drives continuous improvement; MTTD and MTTR measure program maturity

For the Security+ exam, know the NIST phases, the order of volatility, and the components of chain of custody. Complete the reading, lab, and quiz. See you in Module 12.

---

*End of Part 2 Script*
