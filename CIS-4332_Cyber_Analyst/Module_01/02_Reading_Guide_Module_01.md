# Reading Guide: Module 01 - Security Operations & Analyst Role
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 01 - Security Operations & Analyst Role**! This module covers the foundational structure of a Security Operations Center (SOC), the tiered analyst model, and the daily workflows a CySA+ analyst performs. Understanding how a SOC is organized and how analysts triage, escalate, and close alerts is directly tested on the CompTIA CySA+ CS0-003 exam under **Domain 1: Security Operations (33%)**.

As a student, you will learn the roles of Tier 1, Tier 2, and Tier 3 analysts, the types of data sources a SOC monitors, how alert triage works, and how threat indicators are classified. Complete the study checklist and review all glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SOC (Security Operations Center)**: A centralized team and facility responsible for continuously monitoring an organization's security posture, detecting threats, and coordinating incident response. SOC analysts use SIEM platforms, threat intelligence feeds, and playbooks to triage and investigate alerts around the clock.
*   **CIA Triad**: The foundational security model comprising Confidentiality (preventing unauthorized disclosure), Integrity (ensuring data is not altered without authorization), and Availability (ensuring systems and data are accessible when needed). CySA+ scenario questions frequently ask you to identify which pillar of the CIA Triad a given attack or control affects.
*   **Threat Landscape**: The total set of active threats, threat actors, attack vectors, and vulnerabilities that an organization faces at a given time. SOC analysts use threat intelligence and environmental context to understand the current threat landscape and prioritize defensive actions accordingly.
*   **Intelligence Gathering Frameworks**: Structured methodologies — such as MITRE ATT&CK, the Diamond Model, and the Cyber Kill Chain — used by analysts to collect, organize, and apply threat intelligence. These frameworks help analysts map observed attacker behaviors to known techniques and prioritize detection and response actions.

---

### 2. Certification Exam Tips
*   **Focus Area — Domain 1 (33% of exam):** Security Operations is the largest CySA+ CS0-003 domain. Expect scenario-based questions on SOC analyst workflows, alert triage procedures, and how to escalate from Tier 1 to Tier 2. Know the difference between a false positive, true positive, false negative, and true negative.
*   **Scenario Trap — Triage Order:** The exam often asks what a Tier 1 analyst should do first upon receiving an alert. The correct answer is almost always to verify the alert is genuine (true positive) before taking containment action. Jumping straight to isolation or escalation without triage is a common wrong-answer trap.
*   **SIEM Usage:** Know that a SIEM aggregates log data, applies correlation rules, and generates alerts — it does not automatically block traffic (that is an IPS function). Exam questions sometimes conflate SIEM with IPS capabilities.
*   **Study Resource:** The CertifyBreakfast CompTIA CySA+ Complete Playlist covers all CS0-003 domains in mapped video segments. Use this playlist to see worked exam scenarios: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This is a free, community-maintained resource specifically aligned to CySA+ CS0-003 objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Security Operations and the Analyst Role** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). This free resource from CompTIA provides the official exam objective breakdown and recommended study areas for each domain.
*   **Required Video:** Watch the video lecture on **SOC Operations and Analyst Roles** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist provides visual walkthroughs of SOC workflows, SIEM dashboards, and analyst triage scenarios aligned to CS0-003.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Map SOC alert workflows**: Trace an incoming SIEM alert from initial trigger through Tier 1 triage, noting which fields (source IP, event ID, severity) are reviewed first and what the escalation criteria are.
*   **Review log collections in a mock SIEM dashboard**: Examine aggregated log entries from firewall, endpoint, and authentication sources to practice identifying anomalous patterns that warrant further investigation.
*   **Identify indicator classifications (IOCs)**: Classify a set of provided artifacts (file hashes, IP addresses, domain names, registry keys) as Indicators of Compromise (IOCs) and determine their artifact type and confidence level.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Security Operations and the Analyst Role** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **SOC Operations and Analyst Roles** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the commands and workflows outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
