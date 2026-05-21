# Reading Guide: Module 05 - Network Traffic Analysis and Packet Inspection
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 05 - Network Traffic Analysis and Packet Inspection**! This module covers how analysts capture, filter, and interpret network traffic to detect threats and anomalies. You will learn how to use packet capture tools like Wireshark and tcpdump, understand protocol behavior at the packet level, and identify malicious network patterns such as C2 beaconing, data exfiltration, and lateral movement. These topics are tested under **Domain 1: Security Operations (33%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn packet filtering techniques, protocol dissection, and how to correlate network evidence with host-based indicators. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **MITRE ATT&CK Framework**: A globally accessible knowledge base of adversary tactics, techniques, and procedures organized by attack phase. In the context of network traffic analysis, ATT&CK techniques such as T1071 (Application Layer Protocol) and T1048 (Exfiltration Over Alternative Protocol) help analysts map suspicious traffic patterns to known adversary behaviors, guiding investigation priorities.
*   **Cyber Kill Chain**: A seven-stage model (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives) developed by Lockheed Martin to describe the phases of a targeted cyberattack. Network traffic analysts use the Kill Chain to determine at which stage an observed network behavior falls — for example, large outbound transfers to an unusual IP suggest the "Actions on Objectives" exfiltration stage.
*   **Threat Intelligence Feeds (STIX/TAXII)**: Structured streams of curated threat data delivered to security tools via standardized formats. In network monitoring, threat intel feeds supply known-malicious IP addresses, domains, and URL patterns that can be matched against live traffic or PCAP files to identify communications with known threat infrastructure. STIX defines the data format; TAXII is the transport protocol.

---

### 2. Certification Exam Tips
*   **Focus Area – Network Protocol Analysis (Domain 1):** CySA+ CS0-003 expects analysts to know common port/protocol associations and recognize malicious deviations. Know that DNS over non-standard ports, HTTP POST to unusual destinations, and large ICMP payloads are all network anomaly indicators the exam tests.
*   **Scenario Trap – Wireshark vs. IDS:** Wireshark is a passive packet capture and analysis tool — it does not block or alert. An IDS passively monitors and alerts; an IPS actively blocks. The exam tests whether you correctly assign detection vs. blocking capabilities to the right tool.
*   **Beaconing Patterns:** C2 beaconing — regular, timed outbound connections to an external IP — is a high-frequency exam scenario. Know that regular intervals, small packet sizes, and encrypted payloads to uncommon destinations are indicators of C2 activity.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers network traffic analysis and packet inspection scenarios mapped to CS0-003 exam objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes Wireshark filter walkthroughs and protocol anomaly identification exercises.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Network Traffic Analysis and Packet Inspection** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details the network monitoring concepts, tools, and protocol analysis techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Network Traffic Analysis and Packet Inspection** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of Wireshark filters, PCAP analysis, and traffic anomaly identification.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Trace an attack technique in a PCAP file**: Open a provided PCAP in Wireshark and apply display filters (e.g., `tcp.flags.syn == 1 && tcp.flags.ack == 0`) to isolate SYN scan traffic; identify the scanning host and the range of ports probed.
*   **Map threat actors to observed network patterns**: Cross-reference identified suspicious destination IPs from the PCAP against a threat intelligence feed or VirusTotal; document which IPs match known threat actor infrastructure and which ATT&CK technique they correspond to.
*   **Configure a threat feed integration filter**: Using a sample SIEM or firewall rule template, write a rule that blocks or alerts on outbound connections to a list of known-malicious domains extracted from a STIX indicator object.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Network Traffic Analysis and Packet Inspection** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Network Traffic Analysis and Packet Inspection** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the Wireshark filter and tcpdump commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
