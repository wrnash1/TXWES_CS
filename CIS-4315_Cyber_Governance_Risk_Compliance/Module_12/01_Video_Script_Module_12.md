# Video Script: Module 12 — Digital Forensics and Post-Incident Analysis

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Production Notes

- Slides should advance on each [SHOW SLIDE] marker
- Allow natural pause time at each [PAUSE] marker (2–3 seconds)
- Recommended: screen-record forensic tool demos in a VM snapshot
- Use callout boxes on slides for legal and chain-of-custody warnings

---

## Opening — Welcome and Context (approximately 2 minutes)

[SHOW SLIDE: Module 12 Title Card — Digital Forensics and Post-Incident Analysis]

Welcome back, everyone. I'm Professor Nash, and this is Module 12 of CIS-4315 Cyber Governance, Risk, and Compliance.

We are now deep into the incident management domain, and today's topic is one that separates reactive organizations from truly mature ones. We are talking about digital forensics and post-incident analysis.

[PAUSE]

Think about this scenario for a moment. Your organization just contained a ransomware attack. The malware is gone, the systems are back online, and leadership is breathing a sigh of relief. But here is the question that matters most: what happens next?

Do you know how the attacker got in? Do you know what data they accessed? Do you know whether they left a backdoor? Can you prove in court what occurred? Can you tell your board, your regulators, and your insurance carrier exactly what happened?

[SHOW SLIDE: The Post-Incident Gap — Containment Is Not Closure]

If you cannot answer those questions with documented, defensible evidence, you have not finished the job. That is precisely what digital forensics and post-incident analysis are designed to do.

[PAUSE]

By the end of this module you will be able to describe the principles of forensic evidence collection, explain chain of custody requirements, identify common forensic tools and their use cases, conduct a structured after-action review, and perform a root cause analysis that drives real improvement.

These are CISM Domain 4 competencies, and they are tested directly on the certification exam. Let us get started.

---

## Part 1 — Foundations of Digital Forensics (approximately 5 minutes)

[SHOW SLIDE: What Is Digital Forensics?]

Digital forensics is the application of scientific methods to the identification, preservation, analysis, and presentation of digital evidence in a manner that is legally admissible. That last phrase — legally admissible — is critical. Forensics is not simply about finding out what happened. It is about being able to prove what happened in a way that survives scrutiny.

[PAUSE]

The field draws from four core principles. Let me walk through each one.

[SHOW SLIDE: The Four Forensic Principles]

The first principle is **identification**. Before you collect anything, you must identify what constitutes evidence. This includes disk images, log files, memory dumps, network captures, email headers, authentication records, and cloud activity logs. Anything that can tell the story of the incident is potentially evidence.

[PAUSE]

The second principle is **preservation**. Evidence must be captured in a way that prevents alteration. The golden rule here is: never work on original evidence. You always create a forensic image — a bit-for-bit copy — and you work from that copy. The original is sealed and documented.

[SHOW SLIDE: Write Blockers and Forensic Imaging]

Write blockers are hardware or software tools that prevent any write operations from occurring on the source media during imaging. If you connect a drive without a write blocker, even mounting the drive can change access timestamps and corrupt the integrity of the evidence. This is an exam topic — write blockers are mandatory for sound forensic practice.

[PAUSE]

The third principle is **analysis**. This is where investigators examine the evidence to reconstruct the timeline, identify artifacts of attacker activity, and answer the investigative questions. Analysis produces findings — but those findings are only as credible as the preservation process that came before them.

The fourth principle is **presentation**. Findings must be communicated clearly, whether to a court, a regulator, an insurance carrier, or an executive board. The forensic report is a formal document, and its quality can determine whether your organization wins or loses a legal case.

[SHOW SLIDE: Forensic Readiness — Plan Before You Need It]

Here is a CISM-aligned concept I want you to internalize: **forensic readiness**. This means establishing the capability to collect and preserve evidence before an incident ever occurs. Organizations that are forensically ready have logging enabled on critical systems, retention policies in place, legal hold processes defined, and staff trained on evidence handling. Organizations that are not forensically ready scramble after an incident and often lose the most important evidence before they even realize it is gone.

[PAUSE]

---

## Part 2 — Chain of Custody (approximately 5 minutes)

[SHOW SLIDE: Chain of Custody — Definition and Purpose]

Chain of custody is the documented, unbroken record of who has handled a piece of evidence, when they handled it, what they did with it, and where it was stored at every point from collection through final disposition.

Why does this matter so much? Because in legal proceedings, opposing counsel will attack the integrity of digital evidence by arguing that it was tampered with, improperly stored, or mishandled. A complete, unbroken chain of custody is your defense against those arguments.

[PAUSE]

[SHOW SLIDE: Chain of Custody Form — Required Fields]

A chain of custody form must capture the following elements.

First, **evidence identification** — a unique evidence tag or number assigned at the moment of collection. Every piece of evidence gets its own number.

Second, **description** — what is this item? Hard drive, USB device, server image, memory dump, mobile device? Include make, model, serial number, and any physical identifiers.

Third, **collection details** — who collected the evidence, when was it collected including date, time, and time zone, where was it collected from, and what was the system state at the time of collection.

Fourth, **hash values** — immediately upon collection, you compute a cryptographic hash of the evidence using MD5, SHA-1, or preferably SHA-256. This hash is your integrity fingerprint. If anyone disputes that the evidence was altered, you re-hash it. If the hash matches, the evidence is intact.

[PAUSE]

Fifth, **transfer log** — every time the evidence changes hands, the transfer is documented with sender, recipient, date, time, method of transfer, and reason for transfer.

Sixth, **storage log** — where is the evidence stored? Is it in a locked evidence locker? A secure server? Who has access to that location?

[SHOW SLIDE: Breaking the Chain — Consequences]

Here is the hard truth. A single break in the chain of custody can render evidence inadmissible. I have seen cases where organizations did everything right technically — they found the attacker, they had the logs, they could trace every action — but because someone failed to document a transfer, the evidence was challenged and excluded.

[PAUSE]

From a CISM governance perspective, chain of custody procedures must be documented in your incident response plan before an incident occurs. You cannot improvise this in the middle of a crisis. Roles must be assigned: who is the evidence custodian? Who has authority to release evidence to law enforcement? Who signs off on legal holds?

[SHOW SLIDE: Legal Holds]

A **legal hold** is a directive issued by legal counsel to preserve all potentially relevant information once litigation is reasonably anticipated. In the context of a cyber incident, a legal hold may require you to suspend your normal data retention and deletion schedules and preserve systems, logs, emails, and communications that relate to the incident.

Violating a legal hold — even accidentally — can result in sanctions, adverse inferences in court, and significant financial liability. The CISO and information governance team must be in close coordination with legal counsel from the moment an incident is classified as potentially litigious.

[PAUSE]

---

## Part 3 — Forensic Tools and Techniques (approximately 5 minutes)

[SHOW SLIDE: Forensic Tool Categories]

Let us survey the major categories of forensic tools and some of the industry-standard solutions you will encounter in practice and on the CISM exam.

[PAUSE]

The first category is **disk forensics**. These tools create forensic images of storage media and enable analysis of file systems, deleted files, partition structures, and metadata.

**FTK — Forensic Toolkit** from AccessData is one of the most widely used commercial solutions. It indexes an entire drive image and allows investigators to search, filter, and analyze artifacts efficiently. **EnCase** from OpenText is another industry standard, particularly in law enforcement and large enterprises. Both support write-blocker integration and produce court-admissible reports.

For open-source options, **Autopsy** is built on The Sleuth Kit framework and provides a graphical interface for disk analysis. It is widely used in academic and resource-constrained environments.

[SHOW SLIDE: Memory Forensics]

The second category is **memory forensics**. RAM contains artifacts that never touch the disk — running processes, network connections, encryption keys, injected code, and credentials in cleartext. If you power down a system without capturing memory, you lose this evidence forever.

**Volatility** is the gold standard for memory analysis. It is an open-source framework that supports hundreds of plugins for analyzing Windows, Linux, and macOS memory images. You can extract running processes, DLLs, network sockets, registry hives loaded in memory, and command history.

[PAUSE]

[SHOW SLIDE: Network Forensics]

The third category is **network forensics**. This involves analyzing packet captures, flow data, and proxy logs to reconstruct network-level attacker activity.

**Wireshark** is the universal tool for packet capture analysis. If your organization captured network traffic during the incident, Wireshark allows investigators to reconstruct sessions, identify exfiltrated data, and trace attacker communication.

**Zeek** and **Security Onion** are used for network security monitoring and retrospective analysis of stored network data.

[SHOW SLIDE: Log Analysis and SIEM]

The fourth category is **log analysis**. SIEM platforms like Splunk, IBM QRadar, and Microsoft Sentinel aggregate and correlate log data across the enterprise. During forensic investigations, SIEM logs provide the timeline backbone — authentication events, privilege escalations, lateral movement, data staging, and exfiltration patterns all leave log traces.

[PAUSE]

One practical note: log retention is a forensic readiness issue. If your logs only go back 30 days and the attacker was in your environment for 90 days — which is the average dwell time for advanced threats — you have a 60-day blind spot. CISM guidance recommends at least 12 months of log retention for critical systems.

[SHOW SLIDE: Mobile and Cloud Forensics]

Two emerging areas worth noting: **mobile forensics** uses tools like Cellebrite UFED and Oxygen Forensic Detective to extract data from smartphones and tablets. **Cloud forensics** is more complex because traditional imaging approaches do not apply — investigators must work through provider APIs, cloud-native logging services like AWS CloudTrail, and legal processes such as subpoenas for provider-held data.

[PAUSE]

---

## Part 4 — After-Action Reports and Root Cause Analysis (approximately 5 minutes)

[SHOW SLIDE: After-Action Review — Purpose and Timing]

Now let us shift to the organizational learning side of post-incident analysis. The **after-action report**, also called a post-incident review or lessons-learned report, is a structured assessment conducted after every significant incident.

The goal is not to assign blame. The goal is to understand what happened, identify what worked and what did not, and drive improvements that reduce the likelihood and impact of future incidents.

[PAUSE]

Timing matters. The after-action review should occur within two weeks of incident closure, while memories are fresh and evidence is accessible. For major incidents, you may have an initial hot wash within 48 hours followed by a comprehensive review within two weeks.

[SHOW SLIDE: After-Action Report Structure]

A well-structured after-action report contains the following sections.

**Incident summary** — a concise narrative describing what occurred, when it was detected, how it was classified, and when it was resolved.

**Timeline of events** — a chronological reconstruction of the incident from initial compromise through containment and recovery. This is built from forensic evidence, logs, and team communications.

**Response assessment** — how did the organization perform? Were detection times acceptable? Was escalation followed correctly? Were tools and playbooks adequate?

**Findings and gaps** — specific gaps in controls, processes, tools, or skills that this incident exposed.

**Recommendations** — prioritized, actionable improvements. Each recommendation should have an owner, a target completion date, and a measurable success criterion.

[PAUSE]

[SHOW SLIDE: Root Cause Analysis — Beyond Surface Symptoms]

**Root cause analysis** is the discipline of identifying not just what happened, but why it happened at a fundamental level. Surface symptoms are not root causes.

For example: "A phishing email bypassed our spam filter" is a symptom. The root cause might be that the spam filter had not been updated in six months because there was no owner assigned to that task, which exists because the organization has no formal asset-to-owner assignment process.

[SHOW SLIDE: The Five Whys Technique]

The **Five Whys** is the simplest and most powerful root cause analysis technique. You start with the problem statement and ask "why" repeatedly until you reach a cause that cannot be reduced further.

Let me walk through an example. Problem: Attacker maintained access to the environment for 47 days undetected.

Why? Because no alerts fired on the attacker's lateral movement activity. Why? Because lateral movement detection rules were not configured in the SIEM. Why? Because the SIEM implementation project was declared complete before detection rules were tuned. Why? Because the project plan did not include a detection engineering phase. Why? Because the organization had no standard for what constitutes a complete SIEM deployment.

[PAUSE]

The root cause is a missing standard — a governance gap. The fix is not just adding a few SIEM rules. The fix is establishing a deployment standard that includes detection engineering as a required phase.

[SHOW SLIDE: Fishbone Diagram — Ishikawa Method]

For more complex incidents with multiple contributing factors, the **fishbone diagram** uses the Ishikawa method. You place the problem at the head of the fish and identify contributing cause categories along the bones — typically People, Process, Technology, and Environment. This visual approach helps teams see all contributing factors simultaneously and identify which root causes to address first.

[PAUSE]

[SHOW SLIDE: Closing the Loop — Improvement Tracking]

The final step, and the most important from a governance perspective, is closing the loop. After-action recommendations must be tracked as formal action items with assigned owners and deadlines. They should be reviewed at regular intervals and reported to the security steering committee.

An after-action report that sits in a folder and is never acted upon is a liability, not an asset. It documents what you knew about your weaknesses and chose not to fix.

[PAUSE]

---

## Summary and Closing (approximately 2 minutes)

[SHOW SLIDE: Module 12 Summary]

Let us bring this together. In this module we covered the four principles of digital forensics: identification, preservation, analysis, and presentation. We examined chain of custody requirements and why a single break can undermine an entire investigation. We surveyed forensic tool categories — disk forensics, memory forensics, network forensics, and log analysis. And we walked through after-action report structure and root cause analysis techniques including the Five Whys and fishbone diagrams.

[PAUSE]

[SHOW SLIDE: CISM Exam Alignment — Module 12 Key Terms]

For your CISM exam preparation, focus on these key concepts: forensic readiness, write blockers, chain of custody, legal hold, hash integrity verification, the Five Whys, and after-action report components. These are all Domain 4 topics and they appear regularly on the exam.

[SHOW SLIDE: Coming Up — Module 13]

In Module 13, we move to Business Continuity Planning — a topic that sits at the intersection of governance, risk management, and operational resilience. We will cover Business Impact Analysis, RPO and RTO, continuity strategies, and testing methodologies.

[PAUSE]

Thank you for your time and attention. Complete the assigned reading, finish the lab exercise, and I will see you in the discussion board. This is Professor Nash — take care, everyone.

[END OF MODULE 12 VIDEO SCRIPT]
