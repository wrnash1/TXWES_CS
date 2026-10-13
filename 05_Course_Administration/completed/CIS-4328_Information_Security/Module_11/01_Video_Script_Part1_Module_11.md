# Video Script: Module 11 — Incident Response (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Introduction and Why IR Matters (2 minutes)

Welcome to Module 11, Incident Response. This is the module where everything we have studied becomes operational. Knowing about vulnerabilities, cryptography, and access controls is essential — but when an attacker gets through anyway, you need to know what to do next. That is what incident response is.

For Security+, incident response is a primary focus of Domain 4 (Operations and Incident Response). You will face scenario questions that ask you to identify the correct phase of the IR lifecycle, the right team role, or the appropriate action given a described situation. This module gives you the framework.

The hard truth about incident response: you will respond to a security incident. Every organization eventually faces one. The difference between organizations that survive incidents with minimal damage and those that make headlines is whether they had a plan and practiced it before the incident happened.

---

## Segment 2 — The NIST Incident Response Lifecycle (5 minutes)

The authoritative framework for incident response in the United States is NIST Special Publication 800-61, "Computer Security Incident Handling Guide." Security+ is explicitly aligned to this framework. There are four phases:

1. Preparation
2. Detection and Analysis
3. Containment, Eradication, and Recovery
4. Post-Incident Activity

Let us go through each phase in detail.

### Phase 1: Preparation

Preparation is the work you do before any incident occurs. This is not an action you take during an incident — it is everything you build in advance so that your incident response capability exists when you need it.

Preparation activities include:

- **Writing the Incident Response Plan (IRP)** — documented procedures for how incidents are handled
- **Forming the Incident Response Team (IRT)** — identifying who responds, their roles, and their contact information
- **Establishing communication procedures** — how does the team communicate internally? Externally? Who authorizes external communications?
- **Deploying detection and analysis tools** — SIEM, IDS/IPS, EDR (Endpoint Detection and Response), log aggregation
- **Building and maintaining runbooks** — step-by-step playbooks for specific incident types (ransomware, phishing, data breach, DDoS)
- **Conducting training and exercises** — tabletop exercises, red team exercises, and drills

Preparation is the most impactful phase. Organizations that invest in preparation spend dramatically less time and money recovering from incidents. NIST 800-61 emphasizes that an organization cannot effectively respond to incidents without establishing a solid preparation foundation.

### Phase 2: Detection and Analysis

Detection is identifying that an incident has occurred or is occurring. Analysis is determining the scope, severity, and nature of the incident.

**Detection sources include:**

- SIEM alerts (correlation rules triggering on suspicious log patterns)
- IDS/IPS alerts (signature and anomaly-based detection)
- EDR tools (behavioral anomaly detection on endpoints)
- User reports ("I think I clicked something bad")
- Threat intelligence feeds (indicators of compromise matching network traffic)
- External notifications (law enforcement, partner organizations, ISAC)

**Analysis activities include:**

- Validating that an alert is a true positive, not a false positive
- Identifying affected systems, accounts, and data
- Determining the attack vector (how did the attacker get in?)
- Assessing the priority and severity of the incident
- Documenting all findings with timestamps

**Prioritization** is critical during analysis. Not all incidents receive the same response urgency. NIST provides a framework for categorizing incidents by:

- **Functional impact** — what operational impact does this incident have? None → minimal → serious → critical
- **Information impact** — has data been exfiltrated or corrupted? None → suspected but unconfirmed → privacy breach → proprietary information disclosed
- **Recoverability** — how recoverable is the affected system? Fully recoverable → recoverable with time and effort → not recoverable

### Phase 3: Containment, Eradication, and Recovery

This is the most action-intensive phase. It has three sub-phases:

**Containment** — stopping the incident from spreading. There are two types:

- **Short-term containment**: immediate action to isolate the threat (disconnect affected system from network, block a malicious IP, disable a compromised account). The goal is to stop damage quickly, even at the cost of evidence preservation.
- **Long-term containment**: more durable controls while you prepare for eradication. Patch the exploited vulnerability, implement additional network controls, tighten access policies.

The tension in containment: aggressive containment stops damage but may destroy forensic evidence. Measured containment preserves evidence but allows ongoing harm. The correct balance depends on the situation — active ransomware spreading through a network demands immediate aggressive containment. A low-and-slow APT where you want to observe attacker behavior may justify delayed containment to gather intelligence.

**Eradication** — removing the attacker and their artifacts from the environment. This includes:

- Removing malware, backdoors, and persistence mechanisms
- Closing the attack vector (patching the vulnerability, reconfiguring the misconfiguration)
- Resetting compromised credentials
- Removing unauthorized accounts or access the attacker created

**Recovery** — restoring systems to normal operation. This includes:

- Rebuilding compromised systems from known-good images or backups
- Restoring data from clean backups
- Validating system integrity before returning systems to production
- Monitoring restored systems closely for signs of reinfection

### Phase 4: Post-Incident Activity

This phase is often called the **lessons learned** phase, and it is one of the most neglected — because by the time the incident is over, everyone is exhausted and ready to move on. But this phase is where you prevent the same incident from happening again.

Post-incident activities include:

- **Lessons learned meeting** — typically held within two weeks of incident resolution. The entire IR team participates.
- **Incident report** — a formal document capturing the timeline, impact, root cause, what worked, what did not, and recommendations
- **Improvement actions** — updating the IR plan, playbooks, and detection capabilities based on what you learned
- **Evidence retention** — maintaining all collected evidence per legal retention requirements

---

## Segment 3 — Incident Response Plan Components (4 minutes)

The Incident Response Plan is the operational document that guides responders during an incident. Security+ tests your knowledge of what a mature IR plan contains. A well-structured IR plan includes:

### Mission and Scope

What types of incidents does this plan cover? (Security incidents, not operational outages.) Who does it apply to? (All business units? A specific division?) What data and systems are in scope?

### Preparation Section

- Incident Response Team structure and contact information (including after-hours contacts)
- Escalation procedures — at what severity level does the CISO get called? Legal counsel? The CEO? Law enforcement?
- Communication plan — internal communication channels (dedicated Slack/Teams workspace, out-of-band email), external communication procedures, media/PR policy

### IR Process Section

- Step-by-step procedures for each phase of the NIST lifecycle
- Incident classification and prioritization criteria
- Evidence collection and chain of custody procedures
- Decision trees for common scenarios (ransomware, phishing, insider threat, data breach)

### Playbooks (Runbooks)

Playbooks are specific, tactical procedures for responding to a specific incident type. They are more detailed than the general IR plan. A ransomware playbook includes:

- Detection indicators (encrypted file extensions, ransom notes, shadow copy deletion)
- Immediate containment steps (network isolation procedure)
- Evidence preservation steps (memory capture before shutdown)
- Eradication steps (malware removal, root cause identification)
- Recovery steps (restore from backup, system rebuild procedure)
- Communication procedures (who to notify, when, what to say)

### Training and Exercise Schedule

The IR plan must be practiced to be effective. A plan that has never been exercised is a plan that will fail during a real incident. Document:

- Tabletop exercise schedule (quarterly recommended)
- Technical drill schedule
- New hire onboarding to IR procedures

### Legal and Regulatory Considerations

Document legal obligations triggered by incident types:

- Data breach notification requirements (GDPR: 72 hours to supervisory authority; CCPA; state breach notification laws)
- Law enforcement engagement criteria
- Evidence preservation requirements for potential litigation
- Cyber insurance notification requirements

---

## Module 11 Part 1 Summary

The NIST IR Lifecycle and the IR Plan are the backbone of this module:

- NIST 800-61 defines four phases: Preparation, Detection and Analysis, Containment/Eradication/Recovery, and Post-Incident Activity
- Preparation is the most impactful phase — investing before incidents happen dramatically reduces response costs
- Detection requires validating true positives and prioritizing by functional impact, information impact, and recoverability
- Containment balances stopping damage against preserving forensic evidence
- A complete IR plan includes mission/scope, preparation, IR process, playbooks, exercise schedule, and legal considerations

In Part 2 we will cover IR team roles, communication procedures, evidence preservation, chain of custody, and the lessons learned process. See you there.

---

*End of Part 1 Script*
