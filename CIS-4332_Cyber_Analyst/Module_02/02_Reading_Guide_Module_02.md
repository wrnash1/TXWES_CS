# Reading Guide: Module 02 - Threat Intelligence – MITRE ATT&CK and CTI
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 02 - Threat Intelligence – MITRE ATT&CK and CTI**! This module covers how cyber threat intelligence (CTI) is produced, shared, and applied in a SOC. You will learn how to navigate the MITRE ATT&CK framework to map adversary techniques, understand intelligence confidence levels, and use structured formats like STIX/TAXII to exchange threat data. These topics fall primarily under **Domain 1: Security Operations (33%)** and **Domain 2: Vulnerability Management (30%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn the difference between strategic, operational, and tactical intelligence, how threat actors are profiled, and how analysts apply ATT&CK matrices to real detections. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cyber Threat Intelligence (CTI)**: Evidence-based knowledge about existing or emerging threats to an organization's assets, including information about threat actors, their techniques, and indicators of compromise. CTI is categorized as strategic (for executives), operational (for IR planning), or tactical (raw IOCs for tool ingestion). CySA+ exam questions often ask you to match an intelligence type to the correct consumer.
*   **MITRE ATT&CK Framework**: A globally accessible, community-maintained knowledge base of adversary tactics, techniques, and procedures (TTPs) observed in real-world attacks. SOC analysts use ATT&CK to map detections to specific technique IDs (e.g., T1059 – Command and Scripting Interpreter), prioritize detection gaps, and build threat hunting hypotheses. It is one of the most heavily tested frameworks on CySA+ CS0-003.
*   **STIX (Structured Threat Information eXpression)**: A standardized language and serialization format for representing cyber threat intelligence objects (indicators, campaigns, threat actors, attack patterns) in a machine-readable JSON format. STIX defines the data schema; it does not transport data.
*   **TAXII (Trusted Automated Exchange of Intelligence Information)**: The transport protocol used to share STIX-formatted threat intelligence over HTTPS between servers and clients. TAXII enables automated, real-time intelligence sharing between organizations and threat intel platforms. On the CySA+ exam, remember: STIX is the language, TAXII is the carrier.

---

### 2. Certification Exam Tips
*   **Focus Area – MITRE ATT&CK (Domain 1):** CySA+ CS0-003 exam questions frequently present a scenario describing an attacker behavior and ask you to identify the correct ATT&CK tactic (e.g., Persistence, Lateral Movement) or technique. Know the 14 ATT&CK enterprise tactics and be able to distinguish tactics (the "why") from techniques (the "how").
*   **Scenario Trap – STIX vs. TAXII:** The exam consistently presents answer choices that swap STIX and TAXII roles. STIX is the data format/language; TAXII is the transport mechanism. Never confuse them — this is one of the highest-frequency trap questions in CTI topics.
*   **Intelligence Confidence Levels:** Know that threat intelligence sources are rated for confidence and timeliness. An indicator from a government ISAC feed carries higher confidence than an anonymous paste site. The exam may ask which source provides the most reliable tactical intelligence.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers MITRE ATT&CK navigation and CTI workflows with worked examples: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource maps directly to CS0-003 exam objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Threat Intelligence and the MITRE ATT&CK Framework** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). CompTIA's official exam reference outlines exactly which CTI and ATT&CK concepts are tested and at what depth.
*   **Required Video:** Watch the video lecture on **Threat Intelligence – MITRE ATT&CK and CTI** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes a dedicated segment on navigating the ATT&CK matrix and applying it to SOC alert investigations.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Navigate the MITRE ATT&CK matrix**: Access attack.mitre.org, locate a given attacker behavior description, and map it to the correct tactic column and technique ID. Record the technique name, ID, and applicable data sources for detection.
*   **Map threat actors to known techniques**: Select a named threat group from the ATT&CK Groups page and identify three TTPs they are known to use, then determine what log sources or detections would surface each TTP in a SIEM.
*   **Examine a STIX bundle**: Review a sample STIX 2.1 JSON bundle containing an indicator object and an attack-pattern object; identify the relationship between them and note what fields would be ingested by a threat intel platform.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Threat Intelligence and MITRE ATT&CK** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Threat Intelligence – MITRE ATT&CK and CTI** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the ATT&CK navigation steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
