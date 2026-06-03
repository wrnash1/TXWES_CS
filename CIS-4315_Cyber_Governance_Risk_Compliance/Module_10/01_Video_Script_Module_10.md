# Video Script: Module 10 — Incident Management Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Production Notes

[INSTRUCTOR: Deliver at a measured pace. Pause at each [PAUSE] marker for 2–3 seconds. Advance slides at each [SHOW SLIDE] marker. Display diagrams at each [SHOW DIAGRAM] marker.]

---

## Opening — Welcome and Context (Minutes 0–2)

Welcome to Module 10 of CIS-4315, Cyber Governance, Risk, and Compliance. I am Professor Nash, and today we begin the second major domain of the CISM framework: Incident Management.

[SHOW SLIDE: Module 10 Title Card]

Let me open with a statistic that should focus your attention. According to IBM's annual Cost of a Data Breach Report, organizations that can contain a breach in fewer than 200 days save an average of 1.1 million dollars compared to those that take longer. That is not a small number. It is the difference between an incident that damages a quarter's financials and an incident that ends careers, triggers regulatory action, and makes national news.

[PAUSE]

The single most important factor in whether an organization responds to a breach in 200 days or 400 days is not the sophistication of their security tools. It is whether they had a well-designed, practiced Incident Response Plan before the incident began.

[SHOW SLIDE: Learning Objectives]

By the end of this module, you will be able to:

- Describe the components and structure of an Incident Response Plan aligned to NIST SP 800-61.

- Define the roles and responsibilities within an incident response team.

- Develop a communication plan covering internal escalation and external notification.

- Design escalation procedures that govern when and how incidents are elevated.

- Explain how the IRP connects to broader business continuity and disaster recovery planning.

[PAUSE]

Let us get into it.

---

## Part 1 — The Incident Response Plan: Foundation and Framework (Minutes 2–7)

[SHOW SLIDE: What Is an Incident Response Plan?]

An Incident Response Plan, or IRP, is a documented, tested, and maintained set of procedures that defines how an organization will prepare for, detect, contain, and recover from a security incident. The key words in that definition are "documented, tested, and maintained." An IRP that lives on a file server and has never been exercised is not a plan — it is a document. There is a significant difference.

[PAUSE]

The authoritative framework for incident response planning in the United States is NIST Special Publication 800-61, Computer Security Incident Handling Guide. Published by the National Institute of Standards and Technology and updated in revision 2, NIST SP 800-61 defines a four-phase lifecycle for incident response that structures virtually all professional IRP frameworks.

[SHOW DIAGRAM: NIST SP 800-61 Incident Response Lifecycle]

The four phases are:

Phase one — **Preparation**. Everything you do before an incident occurs. Building the team, writing procedures, deploying detection capabilities, conducting training, and running exercises.

Phase two — **Detection and Analysis**. Identifying that an incident has occurred, determining its scope and severity, and characterizing the nature of the attack.

[PAUSE]

Phase three — **Containment, Eradication, and Recovery**. Stopping the spread of the incident, removing the threat actor or malware, and restoring systems to normal operation.

Phase four — **Post-Incident Activity**. The lessons-learned process, root cause analysis, and updates to the IRP based on what you learned.

We will focus primarily on Phase one — Preparation — in this module. Modules 11 covers Phases two, three, and four in detail.

[SHOW SLIDE: What a Strong IRP Contains]

A well-constructed Incident Response Plan contains several essential components. Let us walk through each one.

**Statement of Purpose and Scope** — What is the plan for? What types of incidents does it cover? What systems and data are in scope? What is explicitly out of scope?

**Policy Authorization** — The IRP must be authorized by executive management. An incident response team acting without management authorization lacks the organizational standing to take the actions required during a crisis.

[PAUSE]

**Incident Classification and Severity Framework** — A tiered system that defines what constitutes a minor security event versus a major incident versus a crisis requiring executive notification. Without this framework, the organization will escalate everything to the CEO or nothing at all — both outcomes are failures.

**Roles and Responsibilities** — Who is on the incident response team? What is each person authorized to do? Who activates the plan? This section must be specific: names, titles, and backup contacts.

**Procedures** — Step-by-step response procedures for priority incident types: ransomware, data breach, phishing, unauthorized access, DDoS, insider threat.

**Communication Plan** — Internal notification chains and external notification obligations including regulatory authorities, law enforcement, customers, and the public.

**Plan Maintenance** — How often is the plan reviewed? What triggers an out-of-cycle review? Who owns each section?

[PAUSE]

---

## Part 2 — Roles and Responsibilities (Minutes 7–12)

[SHOW SLIDE: The Incident Response Team Structure]

The Incident Response Team, or IRT, is the organizational unit responsible for executing the IRP. The structure varies by organization size and industry, but a mature IRT includes several defined roles.

[SHOW DIAGRAM: Incident Response Team Role Map]

**Incident Response Manager** — The overall commander of the incident response effort. Coordinates team activities, makes escalation decisions, and serves as the primary interface with senior leadership. In many organizations, this is the CISO or a designated deputy.

**Technical Lead** — Directs forensic investigation, containment actions, and system recovery. Must have deep technical knowledge of the organization's environment. May be a senior security engineer or forensics specialist.

[PAUSE]

**Communications Lead** — Manages all internal and external communications during the incident. Coordinates with legal counsel, public relations, and executive leadership on messaging. Ensures that only authorized parties speak to media or regulators.

**Legal Counsel** — Advises on legal obligations triggered by the incident — breach notification laws, regulatory reporting requirements, preservation of evidence for potential litigation.

**Human Resources Representative** — Required when the incident involves an insider threat or employee misconduct. Manages the investigation process in compliance with employment law.

[SHOW SLIDE: Specialized Response Roles]

Beyond the core team, larger organizations include specialized roles:

**Forensic Investigator** — Collects and preserves digital evidence in a forensically sound manner. Critical when law enforcement involvement is possible or when litigation is anticipated.

**Threat Intelligence Analyst** — Provides context on the adversary, their tactics, and the threat campaign affecting the organization. Informs containment and eradication decisions.

[PAUSE]

**Business System Owner** — For each critical business system affected by the incident, the system owner must be involved in recovery decisions. IT cannot restore a system to service without authorization from the business owner who depends on it.

**Third-Party Response Support** — Many organizations retain an incident response firm on retainer, activated when the internal team needs additional capacity or specialized expertise.

[SHOW SLIDE: RACI Matrix for Incident Response]

A RACI matrix — Responsible, Accountable, Consulted, Informed — is an essential tool for defining who does what during an incident. For each major response activity, the RACI matrix specifies:

- **Responsible** — Who does the work.

- **Accountable** — Who owns the outcome and makes final decisions.

- **Consulted** — Who must provide input before the action is taken.

- **Informed** — Who must be notified when the action is completed.

[PAUSE]

The RACI matrix is particularly important in incident response because incidents create urgency that can lead to chaotic, uncoordinated action. When every team member knows their specific role without needing to ask, response time and effectiveness improve dramatically.

---

## Part 3 — Communication Plans and Escalation Procedures (Minutes 12–18)

[SHOW SLIDE: Why Communication Is a Response Capability]

Most incident response training focuses on the technical response — how to isolate a compromised host, how to capture forensic memory, how to rebuild a system. These skills are essential. But in major incidents, communication failures are often more damaging than technical failures.

[PAUSE]

Consider this scenario. A hospital network discovers ransomware on a Friday afternoon. The security team begins technical response immediately. But no one has authority to notify the hospital CEO until Monday morning. No one has a pre-drafted notification for affected patients. No one knows which regulatory bodies require notification within 72 hours. By Monday morning, the delay has potentially violated HIPAA breach notification rules, and a local journalist has discovered the incident through an employee's social media post.

The technical response was sound. The communication response was catastrophic.

[SHOW SLIDE: Internal Communication Plan Components]

An internal communication plan for incident response defines:

**Notification Chain** — Who is notified at each severity level? A severity-1 incident (data breach affecting customer PII) triggers a different notification chain than a severity-3 incident (a single compromised workstation). The plan must specify: title, contact information, notification method, and time-to-notify requirement.

[PAUSE]

**Need-to-Know Principle** — Not everyone needs to know everything. Over-communication during an incident can tip off an insider threat, trigger premature public disclosure, or create legal problems. The communication plan defines who is authorized to receive what information at each phase of the response.

**Secure Communication Channels** — If the attacker has compromised your primary communication infrastructure — email servers, collaboration platforms — the incident response team needs an out-of-band communication method. This might be personal cell phones, a secure messaging application, or a separate email domain maintained specifically for incident response.

[SHOW SLIDE: External Notification Obligations]

External communication during a security incident is governed by a web of legal, regulatory, and contractual obligations. A CISM-aligned security manager must understand these obligations before an incident occurs.

**Regulatory Notification** — HIPAA requires covered entities to notify the HHS Office for Civil Rights within 60 days of discovering a breach. GDPR requires notification to the supervisory authority within 72 hours. Many US states have breach notification laws with varying timelines, ranging from 30 to 90 days.

[PAUSE]

**Customer and Victim Notification** — Most breach notification laws require organizations to notify affected individuals when their personal information is compromised. The timing and method of notification varies by jurisdiction.

**Law Enforcement** — Not all incidents require law enforcement involvement, but when criminal activity is suspected, the organization must decide early whether to engage law enforcement. This decision affects evidence preservation requirements and may affect the organization's response strategy.

**Cyber Insurance Carrier** — Organizations with cyber insurance must notify their carrier promptly — typically within 24 to 72 hours of discovering a covered incident. Failure to provide timely notice can result in denial of coverage.

**Third-Party Vendors and Partners** — If the incident involves a third-party system or if the organization's breach may affect business partners, contractual notification obligations may apply.

[SHOW SLIDE: Escalation Procedures]

Escalation procedures define when an incident must be elevated from the operational security team to senior management, to the executive team, and potentially to the board.

[PAUSE]

Effective escalation procedures are **criteria-based**, not judgment-based. They define specific conditions — quantitative thresholds or qualitative triggers — that automatically require escalation. Examples:

- Incident involves a regulated data type (PHI, PCI cardholder data, PII): escalate to legal and CISO immediately.

- Number of affected records exceeds a defined threshold (e.g., 500): escalate to executive team.

- Incident has been active for more than 24 hours without containment: escalate to CISO and COO.

- Evidence of nation-state actor involvement or critical infrastructure impact: escalate to board and engage law enforcement.

[PAUSE]

Criteria-based escalation removes the burden of judgment from junior team members in high-stress situations. It also creates a defensible record that the organization followed its defined procedures.

---

## Part 4 — Connecting the IRP to Business Continuity (Minutes 18–22)

[SHOW SLIDE: IRP, BCP, and DRP — The Relationship]

The Incident Response Plan does not operate in isolation. It connects to two broader organizational resilience frameworks: the Business Continuity Plan (BCP) and the Disaster Recovery Plan (DRP).

[PAUSE]

The **Incident Response Plan** handles the security response — detecting, containing, and eradicating a security threat.

The **Disaster Recovery Plan** handles the technical recovery — restoring systems, data, and infrastructure to operational status.

The **Business Continuity Plan** handles the operational response — keeping essential business functions running during and after the incident.

[SHOW DIAGRAM: IRP-DRP-BCP Relationship Model]

These three plans must be aligned and tested together. A scenario illustrates why. A ransomware attack is an incident — the IRP governs the security response. But ransomware may encrypt systems that run critical business processes — the BCP governs how the organization continues operating while those systems are offline. Restoring the encrypted systems is a DRP activity.

[PAUSE]

If these plans are written independently by separate teams, they may conflict. The IRP might require forensic preservation of infected systems for weeks. The DRP might require immediate system reinstallation to meet recovery time objectives. These objectives cannot both be satisfied unless the plans are aligned in advance.

[SHOW SLIDE: Plan Testing and Maintenance]

A plan is only as good as its last test. Incident response plans must be tested regularly using three escalating exercise formats:

**Tabletop Exercise** — Key stakeholders walk through a simulated scenario verbally in a conference room setting. No systems are touched. Tests decision-making and communication, not technical execution.

**Functional Exercise** — Specific response functions are activated and tested with real systems. For example, the communications lead actually drafts and sends a simulated breach notification.

[PAUSE]

**Full-Scale Simulation** — The complete IRP is activated as if a real incident has occurred. All teams play their roles. Technical containment steps are executed in a test environment. This is the most resource-intensive but most realistic test format.

CISM guidance recommends that tabletop exercises occur at minimum annually, with a full review and update of the IRP following each exercise and after every real incident.

[SHOW SLIDE: CISM Exam Connection]

Before we close, here are the key CISM Domain 4 exam connections for this module.

CISM Domain 4, Incident Management, tests candidates on:

- The four phases of the NIST SP 800-61 incident response lifecycle.

- The roles and responsibilities within an incident response team.

- The components of a complete Incident Response Plan.

- Escalation criteria and procedures.

- External notification obligations and their regulatory triggers.

- The relationship between IRP, BCP, and DRP.

[PAUSE]

---

## Summary (Minutes 22–24)

[SHOW SLIDE: Module 10 Summary]

Let us bring it together.

Incident management planning is the preparation phase of incident response. Before an incident occurs, the organization must define its response procedures, build its team, establish communication protocols, and connect the IRP to business continuity planning.

[PAUSE]

The NIST SP 800-61 lifecycle provides the structural framework: Preparation, Detection and Analysis, Containment-Eradication-Recovery, and Post-Incident Activity. Today we focused on preparation.

A strong IRP defines purpose and scope, includes management authorization, establishes severity classification, assigns clear roles through a RACI matrix, and specifies communication and escalation procedures.

[PAUSE]

Communication planning is a response capability, not an afterthought. Internal notification chains, need-to-know controls, external regulatory obligations, and secure out-of-band communication channels must all be designed before an incident occurs.

Escalation procedures must be criteria-based to remove judgment burden from junior team members under pressure.

[SHOW SLIDE: Looking Ahead — Module 11]

In Module 11, we move from planning to execution. We will cover incident detection tools and techniques, triage methodologies, containment and eradication procedures, the recovery process, and the lessons-learned framework. The plan you design in this module becomes the script you execute in Module 11.

See you in Module 11.

[END OF SCRIPT]

---

## Appendix: Slide and Diagram List

1. Module 10 Title Card
2. Learning Objectives
3. What Is an Incident Response Plan?
4. NIST SP 800-61 Incident Response Lifecycle (Diagram)
5. What a Strong IRP Contains
6. The Incident Response Team Structure
7. Incident Response Team Role Map (Diagram)
8. Specialized Response Roles
9. RACI Matrix for Incident Response
10. Why Communication Is a Response Capability
11. Internal Communication Plan Components
12. External Notification Obligations
13. Escalation Procedures
14. IRP, BCP, and DRP — The Relationship
15. IRP-DRP-BCP Relationship Model (Diagram)
16. Plan Testing and Maintenance
17. CISM Exam Connection
18. Module 10 Summary
19. Looking Ahead — Module 11
