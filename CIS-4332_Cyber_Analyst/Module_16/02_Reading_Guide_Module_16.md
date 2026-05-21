# Reading Guide: Module 16 - Final Exam Preparation & CompTIA CySA+ CS0-003 Certification
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 16 - Final Exam Preparation & CompTIA CySA+ CS0-003 Certification**! This final module is your comprehensive review of all four exam domains covered across the course. You will consolidate your knowledge of security operations, vulnerability management, incident response, and security reporting — the four pillars tested on the CompTIA CySA+ CS0-003 exam. This module aligns with all four domains: **Domain 1: Security Operations (33%)**, **Domain 2: Vulnerability Management (30%)**, **Domain 3: Incident Response and Management (20%)**, and **Domain 4: Reporting and Communication (17%)**.

As a student, you will review high-yield concepts from all prior modules, identify your weakest domain areas for targeted study, practice applying the CySA+ scenario-question decision framework, and complete a final comprehensive practice assessment before sitting for the certification exam. Complete the glossary review and study checklist before beginning the final lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **CySA+ Scenario Question Framework**: CompTIA CySA+ CS0-003 is scenario-heavy — most questions describe a specific situation (a SIEM alert, a log excerpt, a vulnerability finding, an incident timeline) and ask what an analyst should do next, what the root cause is, or which control best addresses the problem. The exam tests application of knowledge, not memorization. The correct approach: (1) identify the domain (Security Operations, Vulnerability Management, IR, or Reporting), (2) identify the phase within that domain (e.g., which NIST IR phase), (3) eliminate clearly wrong answers, and (4) select the answer that matches both the correct technical concept and the appropriate analyst action at that phase.
*   **Cross-Domain Integration**: Real-world security analyst work crosses all four CySA+ domains simultaneously. A complete analyst action sequence for a ransomware incident, for example, involves Domain 1 (SIEM correlation, alert triage), Domain 2 (vulnerability that enabled initial access), Domain 3 (containment, eradication, recovery), and Domain 4 (lessons-learned report, executive briefing). CySA+ tests whether you understand how these domains connect — not each domain in isolation. Review the full incident lifecycle from detection through reporting as an integrated workflow.
*   **Exam Domain Weighting and Study Priority**: Domain 1 (Security Operations, 33%) is the largest domain and includes threat intelligence, SIEM operations, EDR, log analysis, and threat hunting — topics covered in Modules 1–6, 13, and 14. Domain 2 (Vulnerability Management, 30%) covers CVSS scoring, scan interpretation, remediation prioritization, and web application vulnerabilities — Modules 7–9 and 13. Domain 3 (Incident Response, 20%) covers NIST IR phases, containment, forensics, and cloud incident response — Modules 8–11. Domain 4 (Reporting and Communication, 17%) covers vulnerability reports, executive summaries, lessons-learned, and risk communication — Module 15. Allocate final study time proportional to domain weight.

---

### 2. Certification Exam Tips
*   **Focus Area – Scenario Questions Require Phase Identification (All Domains):** The single most common CySA+ mistake is selecting the right action at the wrong phase. Example: isolating a compromised host is correct during Containment (Domain 3), but performing forensic imaging is correct during Evidence Collection — not before containment. When you read a scenario, identify the phase first, then select the action appropriate to that phase.
*   **Scenario Trap – "Best" vs. "First" Action:** CySA+ frequently asks what an analyst should do "first" versus "best." These are different questions. "First" tests sequence knowledge (containment before eradication, evidence collection before remediation). "Best" tests which control is most effective for a stated goal. Never apply a "best practice" answer to a "first action" question — they test different things.
*   **High-Yield Cross-Domain Connections to Review:** (1) CVSS score vs. organizational risk rating — CVSS measures technical severity; business context changes the risk decision. (2) True/false positive/negative classification — know all four, including which is worse (false negative = missed threat). (3) EDR host isolation vs. shutdown — isolate, never shut down, to preserve volatile memory. (4) Order of volatility — RAM first, then swap, then disk, then remote logs. (5) DNS sinkholing — containment AND host identification simultaneously. (6) Shared responsibility model — customers always own data classification and IAM governance regardless of cloud deployment model.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers all four domains with scenario walkthroughs mapped directly to CS0-003 exam objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource is the recommended final review — watch the domain summary videos for each of the four exam domains in the week before the exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete a full review of all four domain sections in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference is the authoritative source for all exam objectives — review any domain section where you scored below 80% on module quizzes throughout the course.
*   **Required Video:** Watch the domain summary lectures for all four CySA+ domains in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). The playlist includes dedicated exam prep segments with practice scenario walkthroughs that simulate the CS0-003 question format.

---

### Lab & Command Integration
In this week's final lab, you will perform the following steps to consolidate your exam readiness:
*   **Complete a cross-domain scenario practice set**: Using the provided 20-question final practice assessment (covering all four domains), answer each question without reference materials, document your reasoning for each answer, review your incorrect answers against the domain-specific explanations, and identify which domain you need to prioritize for final review before the exam.
*   **Build a personal exam cheat sheet (study artifact)**: Create a one-page reference (for study use only, not permitted in the exam room) listing: the NIST IR lifecycle phases in order with one key analyst action per phase; the CVSS metric groups (Base, Temporal, Environmental) with one key metric from each; five ATT&CK technique IDs covered in the course with their associated data sources; the three web vulnerability types (SQLi, XSS, SSRF) with their primary preventive controls; and the four components of a complete vulnerability report.
*   **Simulate an exam scenario and apply the decision framework**: Read the following scenario and document your analysis: "A SIEM alert fires indicating a workstation is sending DNS queries to a domain registered 48 hours ago with a high-entropy name. The workstation is used by a member of the finance team. No other hosts are affected. The alert was generated by a new threat intelligence feed integration, not a custom rule. What should the analyst do first?" Apply the scenario question framework — identify the domain, identify the phase, eliminate wrong answers, and write a 3-sentence justification for your answer.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Complete a full review of all four domain sections in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the domain summary lectures for all four CySA+ domains in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Complete the 20-question final practice assessment and review all incorrect answers by domain.
- [ ] Build your personal one-page exam study reference covering all high-yield cross-domain connections.
- [ ] Proceed to the final hands-on lab activity.
