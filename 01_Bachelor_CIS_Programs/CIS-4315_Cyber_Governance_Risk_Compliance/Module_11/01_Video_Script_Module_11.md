# Video Script: Module 11 — Incident Detection and Response Procedures

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Production Notes

[INSTRUCTOR: Deliver at a measured pace. Pause at each [PAUSE] marker for 2–3 seconds. Advance slides at each [SHOW SLIDE] marker. Display diagrams at each [SHOW DIAGRAM] marker.]

---

## Opening — Welcome and Context (Minutes 0–2)

Welcome to Module 11 of CIS-4315, Cyber Governance, Risk, and Compliance. I am Professor Nash, and today we execute the plan.

[SHOW SLIDE: Module 11 Title Card]

In Module 10, we built the Incident Response Plan — the roles, the communication protocols, the escalation criteria, and the authorization structure. Today we move through phases two, three, and four of the NIST SP 800-61 lifecycle: Detection and Analysis, Containment-Eradication-Recovery, and Post-Incident Activity.

[PAUSE]

There is a phrase in incident response circles that I want you to carry through this entire lecture: "Every minute of dwell time costs money." Dwell time is the period between when an attacker first gains access to your environment and when you detect them. The average dwell time for a sophisticated adversary is measured in weeks, not hours. Some breaches are not discovered for months.

[SHOW SLIDE: Learning Objectives]

By the end of this module, you will be able to:

- Identify and describe the detection tools and techniques used in enterprise incident detection.

- Apply a structured triage methodology to classify and prioritize security alerts.

- Select appropriate containment strategies based on incident type and scope.

- Describe eradication and recovery procedures aligned to NIST SP 800-61.

- Conduct a structured post-incident lessons-learned review and update the IRP accordingly.

[PAUSE]

Let us begin.

---

## Part 1 — Detection Tools and Techniques (Minutes 2–8)

[SHOW SLIDE: Detection — The Foundation of Response]

Detection is the process of identifying that a security incident has occurred or is in progress. Without detection, there is no response. Organizations can have the best IRP ever written, but if their detection capability is weak, the plan never activates until it is too late.

[PAUSE]

Detection relies on three interconnected capabilities: technology, process, and human judgment. Technology generates signals. Process filters and correlates those signals. Human judgment determines whether a signal represents a genuine threat.

[SHOW SLIDE: Detection Technology Stack]

The primary detection technologies in a modern enterprise security program include:

**SIEM** — We covered this in Module 9. The SIEM aggregates logs from across the environment and applies correlation rules to detect threat patterns. It is the primary alerting platform for most security operations centers.

**Endpoint Detection and Response (EDR)** — Agent-based software deployed on endpoints that monitors process execution, file system changes, network connections, and registry modifications in real time. EDR tools like CrowdStrike Falcon, Microsoft Defender for Endpoint, and SentinelOne provide deep visibility into what is happening on individual systems.

[PAUSE]

**Network Detection and Response (NDR)** — Monitors network traffic patterns to detect anomalous behavior — unusual connection volumes, communication to known malicious infrastructure, lateral movement between internal systems. NDR fills visibility gaps that SIEM and EDR miss.

**Intrusion Detection System (IDS)** — Monitors network traffic for signature-based and anomaly-based threat patterns. Can be network-based (NIDS) or host-based (HIDS).

**Threat Intelligence Feeds** — External data sources providing real-time information about known malicious IP addresses, domains, file hashes, and attack techniques. Integrated into SIEM and EDR to enrich alert context.

[SHOW SLIDE: Detection Process — From Alert to Incident Declaration]

Detection is not just about having the right tools. It is about having a structured process for moving from raw alert to incident declaration.

[SHOW DIAGRAM: Alert to Incident Declaration Flow]

Step one: **Alert generation**. A security tool — SIEM, EDR, IDS — fires an alert based on a detected pattern.

Step two: **Initial triage**. An analyst reviews the alert, assesses whether it represents a genuine threat or a false positive, and determines initial severity.

[PAUSE]

Step three: **Evidence gathering**. For alerts that survive initial triage, the analyst gathers additional context — log data, endpoint telemetry, threat intelligence — to characterize the event.

Step four: **Incident declaration**. If the evidence confirms a genuine security threat, the analyst declares an incident and initiates the IRP. If not, the alert is closed with documentation.

This process must be fast. The longer an alert sits in the queue, the longer the attacker has to operate.

[SHOW SLIDE: Indicators of Compromise]

A critical concept in detection is the **Indicator of Compromise**, or IoC. An IoC is a piece of forensic data that indicates a system or network may have been compromised.

Common IoC types include:

- **File hashes** — Cryptographic signatures of known malicious files. If a file on your system matches a known malware hash, that is a strong IoC.

- **IP addresses and domains** — Known malicious infrastructure that your systems are communicating with.

- **Registry keys** — Persistence mechanisms that malware commonly writes to specific Windows registry locations.

[PAUSE]

- **Behavioral patterns** — Anomalous activities that deviate from established baselines: a user account accessing systems it has never accessed, a process making outbound connections it has never made before.

IoCs are the breadcrumbs of an attack. SIEM correlation rules and EDR detection logic are built around them. Threat intelligence feeds continuously update the known IoC database.

---

## Part 2 — Triage and Scope Determination (Minutes 8–12)

[SHOW SLIDE: Triage — The First Critical Decision]

In emergency medicine, triage is the process of sorting patients by severity to ensure that the sickest patients receive care first. Security incident triage works the same way. When multiple alerts fire simultaneously — which happens during complex attacks — the analyst must determine which requires immediate attention and which can wait.

[PAUSE]

Effective triage answers four questions:

First: Is this a genuine threat, or is it a false positive? Many alerts are false positives. Rapid, accurate false positive identification is a critical analyst skill.

Second: What is the scope? Is this a single compromised endpoint, a segment of the network, or has the attacker moved laterally across multiple systems?

Third: What is the severity? What data is at risk? What business functions are affected? What is the regulatory exposure?

[PAUSE]

Fourth: What is the urgency? Is this an active, in-progress attack, or is this a historical indicator of a past compromise?

[SHOW SLIDE: Triage Decision Framework]

A structured triage process uses a consistent set of criteria to answer these questions quickly.

The first step is **alert validation**. Confirm that the alert reflects real events, not a tool malfunction or known-good activity triggering a rule. Check the raw log data, not just the alert summary.

The second step is **contextual enrichment**. Pull additional data about the assets and users involved. What systems are affected? What data do they hold? What is the user's normal access pattern?

[PAUSE]

The third step is **severity assignment**. Apply the classification criteria from the IRP to assign a severity level. This determines the response speed and escalation requirements.

The fourth step is **scope mapping**. Determine the lateral extent of the compromise. Has the attacker moved from the initially detected system to other systems? What is the blast radius?

[SHOW DIAGRAM: Triage to Scope Determination Flow]

---

## Part 3 — Containment, Eradication, and Recovery (Minutes 12–18)

[SHOW SLIDE: Containment — Stopping the Spread]

Containment is the most time-sensitive phase of the incident response. Its objective is simple: prevent the incident from spreading while preserving the ability to investigate.

[PAUSE]

NIST SP 800-61 defines two containment strategies: short-term and long-term.

**Short-term containment** is immediate, disruptive action taken to stop active harm. Examples: isolating a compromised endpoint from the network, blocking a malicious IP at the firewall, disabling a compromised user account. Short-term containment accepts business disruption in exchange for stopping the bleeding immediately.

**Long-term containment** involves more measured controls that can be sustained while the investigation continues. Examples: applying temporary access controls, deploying monitoring agents to watch for attacker re-entry, implementing emergency firewall rules.

[SHOW SLIDE: Containment Strategy Selection]

The appropriate containment strategy depends on the incident type:

| Incident Type | Primary Containment Action | Key Consideration |
|---|---|---|
| Ransomware | Immediate network isolation of affected systems | Speed is critical; every minute allows more encryption |
| Data breach | Block exfiltration path; preserve evidence | Balance speed with forensic preservation |
| Insider threat | Disable account; preserve evidence without alerting suspect | Coordination with HR and legal required |
| DDoS | Upstream traffic scrubbing; rate limiting | Cannot isolate legitimate traffic |
| Malware infection | Endpoint isolation; credential rotation | Determine if malware persists elsewhere |

[PAUSE]

One of the most important considerations in containment is the **evidence vs. speed trade-off**. Isolating a system stops the attack but may destroy volatile evidence — memory contents, running processes, active network connections. A mature IR process captures volatile evidence before isolation whenever time permits.

[SHOW SLIDE: Eradication — Removing the Threat]

Eradication follows containment. Once the incident is contained, the team works to completely remove the attacker's presence from the environment. Eradication is not complete until you are confident the attacker has no remaining foothold.

[PAUSE]

Eradication activities include:

**Malware removal** — Identifying and removing all malicious files, scripts, and executables. This requires confidence that all malware components — not just the initially detected payload — have been identified.

**Persistence mechanism elimination** — Attackers establish persistence through scheduled tasks, registry run keys, service installations, and web shells. All persistence mechanisms must be found and removed.

[PAUSE]

**Credential rotation** — Any credentials that may have been observed or harvested by the attacker must be rotated. This includes service account credentials, API keys, and privileged user passwords.

**Vulnerability remediation** — The vulnerability or misconfiguration that allowed the attacker to enter must be patched or corrected before recovery begins. Otherwise, the attacker can re-enter through the same path.

[SHOW SLIDE: Recovery — Restoring Operations]

Recovery is the process of returning affected systems and business functions to normal operation. It must be done carefully to avoid reintroducing the threat.

Recovery steps include:

**System restoration** — Rebuilding or restoring from a known-clean backup. The key qualifier is "known-clean." A backup taken after the attacker established persistence may restore the threat along with the data.

[PAUSE]

**Monitoring enhancement** — During the recovery period, monitoring should be intensified. The attacker may attempt to re-enter, and the organization must detect this immediately.

**Business function restoration** — Coordinate with system owners to restore business services in priority order, per the Business Continuity Plan. Not all systems need to come back simultaneously.

**Validation** — Before declaring recovery complete, conduct validation testing to confirm that systems are operating normally, monitoring is functional, and no attacker artifacts remain.

---

## Part 4 — Post-Incident Activity and Lessons Learned (Minutes 18–22)

[SHOW SLIDE: The Lessons-Learned Process]

Post-incident activity is, by far, the most neglected phase of incident response. Organizations that experience an incident are understandably eager to move on once operations are restored. The lessons-learned process feels like looking backward when everyone wants to look forward.

[PAUSE]

But this phase is where the investment in response capability is realized. An organization that goes through a significant incident and extracts no learnings has paid the full cost of the incident without capturing any of the improvement value.

[SHOW SLIDE: Lessons-Learned Review Structure]

NIST SP 800-61 recommends a structured post-incident review meeting — typically called a "lessons-learned" meeting or a "post-mortem" — that should occur within two weeks of incident closure while memory is fresh.

The review should address:

**Exactly what happened, and when** — Reconstruct the timeline of the incident from initial access to detection to containment. This timeline reveals gaps in monitoring, delays in escalation, and breakdowns in procedure.

**What worked well** — Identifying effective elements of the response is as important as identifying gaps. You want to preserve and reinforce what worked.

[PAUSE]

**What could be improved** — Where did the response fall short? Where were there delays? What information was needed but not available? What decisions were made incorrectly?

**Root cause analysis** — What was the technical root cause of the incident? What was the underlying process or control failure that allowed it to occur?

**Recommendations** — Specific, actionable improvements to technical controls, procedures, training, or the IRP itself. Each recommendation should have an owner and a timeline.

[SHOW SLIDE: IRP Update Process]

Every significant incident must trigger a review and potential update of the IRP. The lessons-learned findings drive specific changes:

- New or revised response procedures based on what the team actually did versus what the plan said.

- Updated contact information and role assignments.

- New correlation rules or detection improvements identified during the investigation.

- Revised escalation criteria based on what the team encountered.

[PAUSE]

The updated IRP must go through the same authorization process as the original — reviewed by legal, approved by the CISO, and documented with an updated version date. IRP updates that are made informally and not formally authorized create a governance gap.

[SHOW SLIDE: Incident Documentation Requirements]

Incident documentation serves multiple purposes: governance accountability, regulatory compliance, legal proceedings, and future training. Key documentation requirements:

**Incident timeline** — A complete, timestamped log of all response activities from initial detection to closure.

**Evidence log** — A chain-of-custody record for all evidence collected, including who collected it, when, and how it was stored.

[PAUSE]

**Decision log** — A record of significant decisions made during the response: who made the decision, what information was available, and what the decision was.

**Notification log** — Documentation of all notifications sent, to whom, when, and by what method.

[SHOW SLIDE: CISM Exam Connection]

Let me draw the CISM Domain 4 exam connections for this module.

Expect CISM exam questions on:

- The difference between short-term and long-term containment.

- The principle of forensic evidence preservation during containment.

- Why credential rotation is a required eradication step.

- The structure and purpose of a lessons-learned review.

- Why known-clean backups matter in recovery.

- Documentation requirements during incident response.

[PAUSE]

---

## Summary (Minutes 22–24)

[SHOW SLIDE: Module 11 Summary]

Let us bring it together.

Detection requires a layered technology stack — SIEM, EDR, NDR, IDS, and threat intelligence — operating within a structured process that moves from alert to triage to incident declaration. Indicators of Compromise are the evidence trail that detection tools follow.

[PAUSE]

Triage answers four questions: Is this genuine? What is the scope? What is the severity? What is the urgency? Structured triage enables rapid, consistent classification.

Containment stops the spread. Short-term containment is immediate and disruptive. Long-term containment is sustainable. The evidence-versus-speed trade-off must be managed deliberately.

[PAUSE]

Eradication removes the attacker completely — malware, persistence mechanisms, compromised credentials, and the vulnerability that enabled entry. Recovery restores operations from known-clean backups with enhanced monitoring.

Post-incident activity closes the loop. The lessons-learned review extracts improvement value from every incident. IRP updates ensure the next response is better than this one.

[SHOW SLIDE: Looking Ahead — Module 12]

With Modules 10 and 11, we have now covered the full CISM Domain 4 incident management lifecycle, from planning through post-incident improvement. In Module 12, we move to third-party and supply chain risk — a topic that has become one of the defining security challenges of the current decade following high-profile supply chain attacks.

See you in Module 12.

[END OF SCRIPT]

---

## Appendix: Slide and Diagram List

1. Module 11 Title Card
2. Learning Objectives
3. Detection — The Foundation of Response
4. Detection Technology Stack
5. Detection Process — From Alert to Incident Declaration
6. Alert to Incident Declaration Flow (Diagram)
7. Indicators of Compromise
8. Triage — The First Critical Decision
9. Triage Decision Framework
10. Triage to Scope Determination Flow (Diagram)
11. Containment — Stopping the Spread
12. Containment Strategy Selection
13. Eradication — Removing the Threat
14. Recovery — Restoring Operations
15. The Lessons-Learned Process
16. Lessons-Learned Review Structure
17. IRP Update Process
18. Incident Documentation Requirements
19. CISM Exam Connection
20. Module 11 Summary
21. Looking Ahead — Module 12
