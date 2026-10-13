# Video Script: Module 11 — Incident Response (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 11 | Texas Wesleyan University"]**

---

## Opening — Part 2

**[INSTRUCTOR ON CAMERA]**

Welcome back to Module 11. In Part 1 we covered the NIST SP 800-61 IR lifecycle, the four phases, and IR team roles. In Part 2 we tackle communication plans, evidence preservation, chain of custody, containment strategies in more depth, and the lessons learned process that closes the cycle.

---

## Section 1 — Communication Plans

**[SHOW SLIDE: Communication flow chart — internal vs. external notifications]**

Incident communication is one of the most underestimated parts of IR. How and when you communicate an incident has legal, regulatory, and reputational implications.

**Internal communication** follows the escalation chain defined in the IR plan. The chain typically runs: analyst to IR manager to CISO to executive leadership. Each level has authority to escalate further or authorize specific actions. The timing of internal escalation should be defined in advance — for example, critical incidents escalate to the CISO within 30 minutes of confirmation.

**External communication** is more complex and depends on regulatory context. In the United States, HIPAA requires breach notification to affected individuals within 60 days for covered healthcare entities. PCI-DSS requires notification to card brands within 24 to 72 hours. State breach notification laws — all 50 states now have them — impose additional requirements. GDPR mandates notification to the supervisory authority within 72 hours for EU residents' data.

Key external audiences include:

- **Law enforcement**: The FBI Cyber Division handles significant cybercrime. Organizations must decide whether to engage law enforcement, which may affect confidentiality of the investigation.
- **Regulatory bodies**: Depending on industry — SEC for public companies, HHS for healthcare, financial regulators.
- **Customers and business partners**: Affected parties have a right to know if their data was compromised.
- **Public / media**: Managed through corporate communications or public affairs.

The IR plan must pre-designate who is authorized to communicate externally. Unauthorized statements by well-meaning employees can create legal liability and media problems.

---

## Section 2 — Evidence Preservation

**[SHOW SLIDE: Evidence types diagram — volatile vs. non-volatile]**

Evidence preservation is where IR meets forensics. The goal is to collect evidence in a way that maintains its integrity and admissibility if legal proceedings follow.

The **order of volatility** defines which evidence should be collected first, because some evidence disappears quickly. From most volatile to least volatile:

1. CPU registers and cache
2. System RAM (running processes, network connections, encryption keys)
3. Swap space and virtual memory
4. Network state (active connections, ARP cache, routing table)
5. Running processes
6. Disk contents
7. Remote logging data
8. Archived or backup media

If a system must be shut down, volatile data is lost. This is why forensic best practice is to image RAM before shutting down a live system.

**Disk imaging** creates a bit-for-bit forensic copy of a storage device. The image is cryptographically hashed (MD5 and SHA-256) before and after copying to verify that the copy is identical to the original. The original drive is then write-protected and preserved as evidence. Analysts work only from the forensic copy.

**Write blockers** are hardware or software devices that allow reading from a storage device while preventing any writes. Write blockers ensure that the forensic imaging process does not modify the original evidence.

---

## Section 3 — Chain of Custody

**[SHOW SLIDE: Chain of custody form example]**

Chain of custody is the documented history of who handled evidence, when, and for what purpose. It is the legal mechanism that proves evidence was not tampered with between the time of collection and the time it is presented in court.

A chain of custody log records:

- A unique identifier for each piece of evidence.
- The date and time of collection.
- The name and role of the person collecting the evidence.
- The location where evidence was found.
- Every transfer of custody — who received it, when, and why.
- Storage conditions and location.
- Access records during storage.

For digital evidence, chain of custody is supported by forensic hash verification. If the hash of the working copy matches the hash of the original at every stage, the chain of integrity is maintained.

Breaking chain of custody — even through negligence rather than malice — can render evidence inadmissible and undermine prosecution or civil litigation.

---

## Section 4 — Containment Strategies

**[SHOW SLIDE: Containment options matrix]**

Containment decisions involve trade-offs between business continuity and investigation thoroughness. The Security+ exam tests specific containment approaches and when to apply them.

**Segmentation**: Isolating a compromised segment of the network from the rest. For example, moving a compromised workstation to a quarantine VLAN that has no access to internal resources. The system remains running, preserving volatile evidence, but cannot communicate with the rest of the network.

**Isolation**: Complete network disconnection. More aggressive than segmentation. Used when the threat is active and spreading. Kills volatile evidence if the system is powered off.

**Black-holing**: Routing attacker traffic to a dead-end server. Used in DDoS response to absorb traffic without it reaching production systems.

**Sinkholing**: Redirecting malware command-and-control traffic to a controlled server operated by the defender. Useful for observing malware behavior and identifying infected systems across the network without blocking the malware immediately.

**Allow-listing / deny-listing at the firewall**: Blocking specific source IPs, domains, or hashes at the perimeter. Fast to implement but easily bypassed by attackers who rotate infrastructure.

**The observation dilemma**: Sometimes the best containment strategy is to watch the attacker rather than immediately eject them. If the attacker is unaware they have been detected, defenders can observe TTPs (tactics, techniques, procedures), identify the full scope of compromise, and gather evidence for attribution or prosecution. This decision requires careful legal and executive authorization.

---

## Section 5 — The Lessons Learned Process

**[SHOW SLIDE: Lessons learned meeting framework]**

Phase 4 in the NIST model is Post-Incident Activity — what most practitioners call the "lessons learned" or "after-action review." This is the most frequently skipped phase and the most valuable for long-term improvement.

A formal lessons learned meeting should occur within one to two weeks of incident resolution, while details are still fresh. The meeting should be blameless — the goal is process improvement, not individual accountability. A blame culture produces under-reporting and cover-ups that make future incidents worse.

Key questions for the lessons learned meeting:

1. What happened, in what sequence?
2. When was the incident first detectable, and when did detection actually occur?
3. Was the IR plan followed? If not, why not?
4. What worked well in the response?
5. What failed or caused delays?
6. What actions would have reduced impact?
7. What controls would have prevented the incident?
8. What changes to the IR plan, detection tools, or system configuration are recommended?

The output is a written post-incident report and an action item list with owners and due dates. The action items feed back into Phase 1 (Preparation), closing the loop.

---

## Section 6 — Incident Report Documentation

**[SHOW SLIDE: Incident report template]**

The incident report is the formal record of the incident and the response. Security+ tests understanding of what an incident report contains. A complete incident report includes:

- Executive summary suitable for leadership review.
- Timeline of events — when the incident started, when it was detected, key actions taken.
- Technical details — systems affected, attack vectors used, malware analyzed, data involved.
- Impact assessment — number of systems, users, and records affected; business downtime.
- Containment and eradication actions taken.
- Evidence collected and chain of custody documentation.
- Root cause analysis.
- Recommendations for prevention and detection improvement.
- Lessons learned action items with owners and timelines.

---

## Section 7 — Tabletop Exercises

**[SHOW SLIDE: Tabletop exercise facilitator notes]**

Preparation is only as good as its testing. A tabletop exercise is a discussion-based simulation where the IR team walks through a realistic scenario without activating real response activities. The facilitator presents an evolving scenario and asks the team to describe what they would do at each decision point.

Tabletop exercises reveal gaps in the IR plan, test decision-making under pressure, familiarize team members with their roles, and identify communication breakdowns before they happen in a real incident.

A full-scale exercise activates actual response procedures in a controlled simulation. This is more resource-intensive but provides the most realistic preparation.

---

## Closing

**[INSTRUCTOR ON CAMERA]**

Incident response is the profession's answer to the certainty that perfect prevention is impossible. The NIST lifecycle gives us a structured framework. Chain of custody and evidence preservation connect IR to legal proceedings. Communication plans prevent organizational chaos. Lessons learned turn incidents into improvements.

For the Security+ exam: know all four NIST phases, know what chain of custody is and why it matters, understand the order of volatility, and be able to distinguish containment from eradication from recovery.

Complete your Reading Guide, Lab, Quiz, and Discussion for Module 11. Module 12 moves into Digital Forensics — the investigative science behind the evidence you just learned to preserve. I'll see you there.

---

*End of Part 2*
