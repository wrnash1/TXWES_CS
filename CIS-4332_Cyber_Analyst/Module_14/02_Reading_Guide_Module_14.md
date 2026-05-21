# Reading Guide: Module 14 - Threat Hunting Methodologies
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 14 - Threat Hunting Methodologies**! This module covers how analysts proactively search for threats that have evaded automated detection — operating under the assumption that adversaries may already be present in the environment. You will learn hypothesis-driven hunting techniques, how to use MITRE ATT&CK as a hunt framework, how to apply DNS sinkholing and network-based containment during threat hunting, and how to structure and document hunt findings. These topics are tested under **Domain 1: Security Operations (33%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn the distinction between reactive (alert-driven) and proactive (hunt-driven) SOC operations, common hunting data sources, and how to translate a threat hypothesis into a hunt query. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Threat Hunting**: A proactive, analyst-led process of searching through network, endpoint, and log data for indicators of adversary activity that has not triggered automated alerts — operating under the assumption of breach. Threat hunting differs from alert triage in that hunting begins with a hypothesis (e.g., "An attacker using T1059 PowerShell execution may be present") rather than waiting for a SIEM alert to initiate investigation. CySA+ tests threat hunting as a proactive security operations capability.
*   **DNS Sinkholing**: A containment and intelligence-gathering technique in which a DNS resolver is configured to return a controlled internal IP address for known-malicious domains instead of the real C2 server address. Infected hosts attempting to contact C2 infrastructure are redirected to the sinkhole, severing the C2 channel and revealing which internal hosts are infected by showing which systems query the sinkholed domain. CySA+ tests DNS sinkholing as both a containment and a threat identification technique.
*   **Hypothesis-Driven Hunting**: A structured approach to threat hunting that begins with a specific, testable hypothesis about attacker behavior — typically based on threat intelligence, recent CVE disclosures, or ATT&CK techniques relevant to the organization's industry. The hunter formulates a hypothesis (e.g., "Attackers may be using scheduled tasks for persistence"), identifies the data sources and query logic to test it, and documents the outcome regardless of whether the hunt finds evidence of compromise.

---

### 2. Certification Exam Tips
*   **Focus Area – Proactive vs. Reactive SOC (Domain 1):** CySA+ CS0-003 tests the distinction between reactive operations (alert triage, incident response) and proactive operations (threat hunting, threat intelligence consumption). When a question asks about improving detection of threats that evade automated tools, threat hunting is the answer — not more SIEM rules, which are still reactive.
*   **Scenario Trap – DNS Sinkholing Purpose:** CySA+ questions about DNS sinkholing frequently offer answer choices that confuse it with DNS filtering (blocking all access to a category of sites) or DNS poisoning (a malicious attack). DNS sinkholing is a defensive technique that redirects malicious domain queries to a controlled address — it is both a containment measure and an infected-host identification tool.
*   **ATT&CK as a Hunt Framework:** Threat hunters use MITRE ATT&CK tactics and techniques to select hunt hypotheses. For example, a hunt for T1053.005 (Scheduled Task/Job) would query endpoint logs for new scheduled task creation events (Windows Event ID 4698) outside of approved change windows. CySA+ tests whether you can connect a hunt hypothesis to the relevant ATT&CK technique and data source.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers threat hunting workflows, hypothesis development, and ATT&CK-mapped hunt techniques aligned to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes demonstrations of SIEM-based hunt queries and containment technique walkthroughs.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Threat Hunting** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details threat hunting methodologies, hypothesis-driven investigation, and hunt data source selection tested on the exam.
*   **Required Video:** Watch the video lecture on **Threat Hunting Methodologies** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of ATT&CK-mapped hunt queries and DNS sinkhole configuration walkthroughs.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a firewall rule to block a known C2 IP address**: Using iptables (Linux) or Windows Firewall with Advanced Security, write a rule that drops all outbound traffic to a specified C2 IP address; verify the rule is in place by attempting a test connection and confirming it is blocked; document the rule syntax and the IOC that justified it.
*   **Implement a DNS sinkhole mapping for a suspicious domain**: Configure a local DNS resolver (e.g., BIND or Windows DNS) to return `127.0.0.1` for a specified malicious domain; test the sinkhole by querying the domain from a lab workstation and confirming the redirected response; explain how monitoring queries to the sinkhole IP would identify infected hosts.
*   **Write and execute a threat hunt hypothesis**: Formulate a hypothesis based on ATT&CK T1053.005 (Scheduled Task Persistence), write a SIEM or PowerShell query to retrieve Windows Event ID 4698 (scheduled task created) events from the past 7 days filtered to non-standard task names, review the results, and document whether the hunt found evidence of malicious activity or confirmed a clean environment.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Threat Hunting** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Threat Hunting Methodologies** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the firewall rule, DNS sinkhole, and hunt query steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
