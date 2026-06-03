# Video Script: Module 11 — Incident Response for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Slide 1 — Introduction

Welcome back to CIS-4332. I am Professor Nash, and this is Module 11: Incident Response for Analysts.

In previous modules we focused on detection — identifying threats through logs, SIEM alerts, vulnerability data, and threat intelligence. Now we shift from detection to action. When your detection pipeline fires, what happens next?

This module walks you through the analyst's role inside a structured incident response process. We will follow NIST Special Publication 800-61 Revision 2, the industry-standard IR framework, and connect each phase to what you will actually do on the job and on the CySA+ exam.

---

## Slide 2 — Why Analysts Must Understand IR

Some students assume IR is the job of a dedicated IR team, not an analyst. That assumption will hurt you in the field and on the exam.

Security analysts are almost always the first responders to an alert. You are the person deciding whether an event becomes an incident. You are the one performing initial triage. You write the ticket that starts the formal IR workflow.

Understanding the full IR lifecycle makes you a better analyst because you understand what happens downstream from your work. If you scope an incident incorrectly at triage, the IR team responds to the wrong scope. If you fail to preserve evidence, forensic analysis fails.

The CySA+ exam tests your knowledge of every phase, not just triage.

---

## Slide 3 — NIST SP 800-61 Overview

NIST Special Publication 800-61 Revision 2 is titled "Computer Security Incident Handling Guide." It defines four phases:

- Preparation
- Detection and Analysis
- Containment, Eradication, and Recovery
- Post-Incident Activity

These phases are not strictly sequential. Containment may reveal new indicators that push you back into Detection and Analysis. Recovery may surface eradication gaps. The lifecycle is iterative.

The document is free on the NIST website and is explicitly referenced in the CySA+ exam objectives. Read it.

---

## Slide 4 — Phase 1: Preparation

Preparation is everything you do before an incident occurs. It is also the phase most organizations underinvest in, which is why their IR efforts fail.

Preparation includes:

- Building and training the Computer Security Incident Response Team (CSIRT)
- Developing and documenting IR policies and procedures
- Creating playbooks for common incident types
- Deploying and tuning detection tools
- Establishing communication channels and escalation paths
- Conducting tabletop exercises and simulations

As an analyst, your preparation contribution is tuning your SIEM, maintaining your watchlists, and knowing your playbooks before an incident fires.

---

## Slide 5 — Playbooks

A playbook is a documented, step-by-step procedure for responding to a specific incident type. Examples include ransomware playbooks, phishing playbooks, and data exfiltration playbooks.

A good playbook contains:

- Trigger conditions — what alert or event initiates this playbook
- Initial triage steps — what to check first
- Escalation criteria — when to involve senior analysts or the IR team
- Containment actions — specific steps to isolate affected systems
- Evidence collection checklist
- Communication templates
- Recovery milestones

Playbooks reduce cognitive load during high-stress incidents. When you are staring at a ransomware alert at 2 AM, you do not want to improvise. You want a checklist.

---

## Slide 6 — Phase 2: Detection and Analysis

This is the phase analysts own most directly. Detection and Analysis has two components.

Detection is recognizing that something anomalous occurred. Sources include SIEM alerts, IDS/IPS events, endpoint telemetry, user reports, and threat intelligence feeds.

Analysis is determining whether the anomaly represents a real incident. This is where triage happens.

The quality of your detection tooling directly determines your ability to catch incidents early. An analyst working from well-tuned SIEM rules with rich telemetry will detect incidents faster and with lower false-positive rates than an analyst working from sparse, poorly configured data sources.

---

## Slide 7 — Triage

Triage is the process of evaluating an alert to determine its validity, severity, and scope. Triage answers four questions:

1. Is this a true positive or false positive?
2. What systems are affected?
3. What is the potential business impact?
4. What is the initial severity rating?

The NIST framework provides a functional impact scale: None, Minimal, Significant, Severe. It also defines information impact (None, Privacy Breach, Proprietary Breach, Integrity Loss) and recoverability (Regular, Supplemented, Extended, Not Recoverable).

Your job during triage is to collect enough context to answer these questions accurately and quickly — not to investigate everything. Triage should have a defined time box in your playbook.

---

## Slide 8 — Scoping

Scoping extends triage. Once you confirm a true positive, you determine the blast radius of the incident.

Scoping questions include:

- Which IP addresses, hostnames, or user accounts are involved?
- Is this confined to one host or has it spread laterally?
- What data has potentially been accessed or exfiltrated?
- What time window does this incident span?
- Are there related alerts or events we have not yet correlated?

Scoping results feed directly into containment decisions. A poorly scoped incident leads to incomplete containment, which means the threat persists even after you believe it is gone. Lateral movement is the most common scoping failure point.

---

## Slide 9 — Indicators of Compromise

During Detection and Analysis, you extract and document Indicators of Compromise, or IoCs. IoCs are observable evidence that a system has been compromised.

Common IoC types include:

- IP addresses and domains associated with attacker infrastructure
- File hashes of malicious executables
- Registry keys created by malware
- Unusual user account activity patterns
- Anomalous process execution chains
- Suspicious network connections or beaconing patterns

IoCs should be documented in STIX format when shared externally, and recorded in your SIEM and ticketing system for internal tracking. Sharing IoCs with ISAC partners improves the collective defense of your sector.

---

## Slide 10 — Phase 3: Containment, Eradication, and Recovery

These three actions are grouped in one phase but represent distinct steps.

Containment stops the spread of the incident without necessarily fixing it. There are two types.

Short-term containment is immediate action to stop damage, such as isolating a host from the network or blocking a malicious IP at the firewall.

Long-term containment preserves operations while eradication is planned. Examples include applying temporary ACLs or disabling a compromised account while you prepare a clean rebuild.

The tradeoff in containment decisions is always speed versus evidence preservation. Aggressive containment may destroy forensic evidence. Your playbook should define this tradeoff for common incident types.

---

## Slide 11 — Eradication

Eradication removes the threat from the environment. For malware incidents this means removing the malicious software, deleting persistence mechanisms, and patching the vulnerability that was exploited.

Eradication must be thorough. A common mistake is removing the malware binary while leaving behind the scheduled task or registry run key that re-downloads it.

Use threat intelligence and forensic analysis to identify every persistence mechanism before declaring eradication complete. Verify eradication by reviewing endpoint telemetry for several days after the action.

---

## Slide 12 — Recovery

Recovery restores systems to normal operation. This includes:

- Rebuilding or restoring affected systems from clean backups
- Resetting compromised credentials
- Reverting unauthorized configuration changes
- Monitoring the restored environment closely for re-compromise
- Validating that business functions have returned to normal

Recovery has a monitoring tail. Just because the system is back online does not mean the incident is over. Enhanced monitoring should continue for days to weeks depending on incident severity. Many attackers deliberately wait for recovery to complete before reactivating.

---

## Slide 13 — Phase 4: Post-Incident Activity

Post-incident activity is often called the lessons learned phase. NIST recommends a formal meeting within two weeks of major incidents.

The lessons learned discussion should answer:

- What exactly happened and what was the full timeline?
- How did we detect it, and how long did detection take?
- What did we do well?
- What did we do poorly?
- What gaps in controls, tooling, or process did this expose?
- What specific action items will we implement before the next incident?

Organizations that skip this phase repeat the same mistakes. Lessons learned are the primary feedback loop that improves IR capability over time.

---

## Slide 14 — Incident Documentation

Documentation is not optional. It is a professional and often legal obligation.

Incident records should capture:

- Chronological event timeline with precise timestamps
- All analyst actions with timestamps and rationale
- Evidence collected and its chain of custody
- Decisions made and their justification
- Communications sent to which parties
- Escalations triggered and outcomes

Your incident ticket is a legal document. Write it like one. Future investigations, legal proceedings, insurance claims, and regulatory audits may rely on it. Vague or incomplete documentation has cost organizations significantly in legal and regulatory proceedings.

---

## Slide 15 — The Analyst's Role in Coordination

Analysts rarely work alone during significant incidents. You will coordinate with:

- Tier 2 and Tier 3 analysts during escalation
- The formal CSIRT or IR team
- IT operations for containment and recovery actions
- Legal and compliance teams for data breach scenarios
- Management for business impact decisions
- Vendors or MSSPs if external support is engaged

Your role is to be the technical subject-matter expert providing real-time intelligence to these teams. Clear, concise, accurate communication is as important as technical skill. During a major incident, communication breakdowns cause as much damage as technical failures.

---

## Slide 16 — Escalation Criteria

Knowing when to escalate is a critical analyst skill. Escalate when:

- The incident affects critical infrastructure or sensitive data
- The scope is larger than your authorization to contain
- The incident involves a potential insider threat
- You need forensic preservation beyond your capability
- Legal or regulatory notification obligations may apply
- The incident has persisted beyond your playbook time threshold

When in doubt, escalate. It is far better to involve senior resources unnecessarily than to under-escalate a serious incident.

---

## Slide 17 — Metrics and Reporting

IR programs generate metrics that measure effectiveness:

- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- Mean Time to Contain (MTTC)
- Number of incidents by type and severity
- Recurrence rate
- Percentage of incidents contained within service-level agreement

Analysts contribute to these metrics directly. When you triage quickly, document accurately, and escalate appropriately, you improve program-level metrics that drive budget and resource decisions.

---

## Slide 18 — CySA+ Exam Connection

The CySA+ CS0-003 exam Domain 4 covers Incident Response and Digital Forensics. You should be prepared to:

- Describe the phases of the NIST IR lifecycle
- Explain analyst actions in each phase
- Identify appropriate containment strategies by scenario
- Recognize proper documentation practices
- Apply severity and impact categorization frameworks

Expect scenario-based questions. You will not be asked to recite definitions. You will be given a situation and asked what to do next.

---

## Slide 19 — Summary

Let us recap Module 11. Incident Response is a structured process, not an ad-hoc reaction. NIST SP 800-61 provides the four-phase framework that the industry and the CySA+ exam follow.

As an analyst, your most direct contributions are in Detection and Analysis. You own triage, scoping, IoC extraction, and initial documentation. Your accuracy and thoroughness here determine the quality of every downstream IR action.

Preparation makes you effective under pressure. Playbooks are your tool. Documentation is your obligation. Communication is your force multiplier.

---

## Slide 20 — Looking Ahead

In Module 12 we turn to Digital Forensics. You will learn how analysts use memory forensics, disk forensics, and network forensics to reconstruct what happened during an incident. We will work with Volatility, Autopsy, and Wireshark.

Complete the Reading Guide, Lab, Quiz, and Discussion for Module 11 before our next session. The Lab puts you through a simulated IR triage scenario. See you there.

---

End of Module 11 Video Script — 230 lines
