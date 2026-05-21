# Reading Guide: Module 06 - Endpoint Detection and Response (EDR)
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 06 - Endpoint Detection and Response (EDR)**! This module covers how EDR platforms monitor endpoint activity, detect suspicious behaviors, and enable analysts to investigate and respond to threats at the host level. You will learn how EDR differs from traditional antivirus, how behavioral detection works, and how analysts use EDR telemetry to hunt for threats and contain compromised endpoints. These topics are tested under **Domain 1: Security Operations (33%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn EDR agent deployment, telemetry collection, alert triage, and isolation workflows. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Signature-Based vs. Anomaly-Based Detection**: Signature-based detection compares observed activity against a database of known malicious patterns (hashes, strings, byte sequences) — it is fast and precise but fails against novel or obfuscated threats. Anomaly-based detection establishes a behavioral baseline and alerts when activity deviates significantly from normal — it can detect zero-days but produces more false positives. CySA+ exam questions frequently ask which detection type is better suited to detecting previously unknown malware.
*   **Snort Rule Configuration**: Snort is an open-source network intrusion detection and prevention system that uses rule-based logic to match network traffic patterns. A Snort rule consists of a header (action, protocol, source/destination IP and port) and options (content match, metadata, threshold). Understanding Snort rule syntax is tested on CySA+ as part of network-based IDS/IPS configuration knowledge.
*   **Inline vs. Passive Placement**: An inline security device (IPS, next-gen firewall) sits directly in the traffic path and can block malicious packets before they reach the destination. A passive device (IDS, network tap) receives a copy of traffic and can only detect and alert — it cannot block. CySA+ scenario questions frequently ask you to identify which placement is required when a question asks for blocking capability vs. detection-only.

---

### 2. Certification Exam Tips
*   **Focus Area – EDR vs. Traditional AV (Domain 1):** CySA+ CS0-003 distinguishes EDR from antivirus clearly. EDR provides continuous behavioral monitoring, process telemetry, memory inspection, and remote isolation — capabilities traditional AV signature scanning does not offer. Know that EDR is the correct answer when a scenario requires detecting fileless malware or responding to a living-off-the-land attack.
*   **Scenario Trap – Isolation vs. Shutdown:** When a host is confirmed compromised, the correct containment action in EDR is network isolation (severing network connectivity while keeping the host running for forensic collection) — NOT shutting the system down. Shutdown destroys volatile memory evidence. This is a high-frequency exam trap.
*   **Fileless Malware Detection:** Fileless attacks (e.g., PowerShell in-memory execution) leave no file on disk for antivirus to scan. EDR detects these through process behavior monitoring, memory scanning, and PowerShell/WMI activity logging. The exam tests whether you recognize EDR as the appropriate tool for fileless threat detection.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers EDR concepts, behavioral detection, and endpoint investigation scenarios mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes walkthroughs of EDR alert triage and isolation decisions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Endpoint Detection and Response** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details EDR capabilities, behavioral detection concepts, and endpoint investigation techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Endpoint Detection and Response (EDR)** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of EDR telemetry review, alert investigation, and host isolation workflows.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Review a Snort rule file structure**: Open a provided Snort rules file and identify the components of three sample rules — action, protocol, source/destination, and content match options — then explain in writing what each rule is designed to detect.
*   **Write a basic rule to alert on ICMP packets**: Construct a Snort rule that generates an alert for any inbound ICMP echo request (ping) targeting the home network, test it against a sample PCAP, and verify the alert fires correctly.
*   **Examine PCAP captures for alert triggers**: Load a PCAP file containing mixed legitimate and malicious traffic into Wireshark; apply filters to isolate traffic that would trigger the Snort rules reviewed earlier and document the source IPs and packet characteristics.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Endpoint Detection and Response** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Endpoint Detection and Response (EDR)** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the Snort rule syntax and EDR isolation procedures outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
