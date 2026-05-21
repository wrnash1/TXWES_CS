# Reading Guide: Module 08 - Incident Response – Detection and Triage
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 08 - Incident Response – Detection and Triage**! This module covers the first two phases of the incident response lifecycle: identifying that a security event has occurred and determining whether it constitutes a true incident requiring escalation. You will learn how to classify events, triage alerts from SIEM and EDR platforms, and apply structured IR frameworks to guide investigation decisions. These topics are tested under **Domain 3: Incident Response and Management (20%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn IR framework phases, alert classification categories, triage decision criteria, and escalation procedures. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Incident Response Lifecycle (NIST SP 800-61)**: The NIST framework for handling security incidents defines four phases: Preparation, Detection and Analysis, Containment/Eradication/Recovery, and Post-Incident Activity. CySA+ CS0-003 exam questions frequently require you to identify which phase a described activity belongs to — for example, creating IR runbooks is Preparation, and deploying EDR isolation is Containment.
*   **True Positive vs. False Positive**: A true positive is an alert that correctly identifies a genuine malicious event — the detection is accurate and action is required. A false positive is an alert that fires on benign activity — the detection is incorrect and the event is not malicious. Alert triage is the process of classifying each alert into one of four categories: true positive, false positive, true negative (no alert, no attack — correct), or false negative (no alert, real attack — missed detection). CySA+ heavily tests these four classifications.
*   **Indicators of Compromise (IOC)**: Forensic artifacts — file hashes, malicious IP addresses, anomalous registry keys, suspicious process names, or unusual network connections — that indicate a host or network has been compromised. Analysts use IOCs during triage to pivot from an initial alert to a broader investigation scope, determining which other systems may share the same indicator.

---

### 2. Certification Exam Tips
*   **Focus Area – IR Lifecycle Phases (Domain 3):** CySA+ CS0-003 presents scenario questions where you must assign an activity to the correct NIST IR phase. Know that building playbooks = Preparation; running SIEM queries to confirm compromise = Detection and Analysis; isolating a host = Containment; reimaging a system = Eradication; scanning for re-infection = Recovery; lessons-learned meeting = Post-Incident Activity.
*   **Scenario Trap – True/False Positive Classification:** The most frequently tested triage trap is confusing false positive with true positive. Always anchor your answer on whether the alert correctly identifies real malicious activity (true positive) or fires incorrectly on legitimate behavior (false positive). An authorized vulnerability scanner triggering a brute-force rule is a false positive.
*   **Escalation Criteria:** CySA+ scenario questions ask when a Tier 1 analyst should escalate to Tier 2. Escalate when: the attack is confirmed active (true positive), the scope is expanding, the affected system holds sensitive data, or the response requires capabilities beyond Tier 1 (e.g., memory forensics, legal hold).
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers the full NIST IR lifecycle, alert triage workflows, and escalation decision scenarios mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes walkthroughs of Tier 1 triage decision trees.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Incident Response** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details IR lifecycle phases, alert classification, and triage procedures tested on the exam.
*   **Required Video:** Watch the video lecture on **Incident Response – Detection and Triage** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of SIEM alert triage workflows and IR phase identification exercises.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Classify a set of SIEM alerts into true/false positive/negative categories**: Review a provided set of ten SIEM alert summaries (including alert type, source, destination, and context) and classify each as true positive, false positive, true negative, or false negative — documenting your reasoning for each classification decision.
*   **Map an alert to an IR lifecycle phase**: For each confirmed true-positive alert in the set, identify the NIST IR phase at which the detection occurred and specify what the next IR phase action should be (e.g., if detection occurred during a scan, the next action is containment/isolation).
*   **Write an escalation note**: For the most critical confirmed true-positive alert, draft a structured Tier 1 to Tier 2 escalation note that includes: alert ID, timestamp, affected host, confirmed IOCs, scope assessment, and recommended next action.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Incident Response** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Incident Response – Detection and Triage** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the NIST IR lifecycle phases and alert classification categories outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
