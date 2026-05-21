# Reading Guide: Module 04 - Network Attacks - DDoS, Spoofing, MITM
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 04 – Network Attacks: DDoS, Spoofing, and Man-in-the-Middle**! This module covers attacks that target the network layer itself rather than applications or users. SY0-701 tests your ability to identify these attacks from traffic patterns and log descriptions, and to select the correct network-level control to mitigate them.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Distributed Denial of Service (DDoS)**: An attack that overwhelms a target system, service, or network by flooding it with traffic from many compromised hosts (a botnet), making the resource unavailable to legitimate users. DDoS attacks target Availability — one of the three CIA triad pillars. Volume-based, protocol, and application-layer variants are all tested on SY0-701.
*   **IP Spoofing**: Forging the source IP address in network packets to impersonate another host, bypass IP-based access controls, or hide the attacker's true identity. IP spoofing is the underlying technique behind many reflection/amplification DDoS attacks and is mitigated by ingress/egress filtering (BCP38) at network borders.
*   **Man-in-the-Middle (MITM) Attack**: An attack where the adversary secretly intercepts and potentially alters communications between two parties who believe they are communicating directly with each other. ARP poisoning and rogue Wi-Fi access points are common MITM enablers. Mitigations include mutual TLS, certificate pinning, and encrypted protocols.
*   **ARP Poisoning**: A Layer 2 attack that sends fraudulent ARP (Address Resolution Protocol) replies to associate the attacker's MAC address with a legitimate IP address, redirecting traffic through the attacker's machine. ARP poisoning is a primary MITM technique on local network segments and is mitigated by Dynamic ARP Inspection (DAI) on managed switches.
*   **DNS Spoofing (Cache Poisoning)**: An attack that injects fraudulent DNS records into a resolver's cache, causing users who query that resolver to be redirected to attacker-controlled IP addresses even when they type legitimate domain names. DNSSEC (DNS Security Extensions) is the primary defense.
*   **Smurf Attack**: A DDoS amplification attack that spoofs the victim's IP address as the source and sends ICMP echo requests to network broadcast addresses. All hosts on the network reply to the victim, amplifying the attack traffic. Mitigated by disabling directed broadcasts on routers.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Network attacks appear in **Domain 2 – Threats, Vulnerabilities, and Mitigations (22%)** and **Domain 4 – Security Operations (28%)** of SY0-701. Network attack identification and mitigation questions are frequent.
*   **DDoS Sub-type Trap:** Know all three DDoS categories — volumetric (flood the bandwidth), protocol (exploit Layer 3/4 weaknesses like SYN flood), and application-layer (HTTP flood targeting web server resources). The exam describes symptoms and expects you to identify the sub-type.
*   **MITM Enablers:** The exam tests the specific technique used to position the attacker in the middle. ARP poisoning works on local segments; rogue access points work on wireless; SSL stripping downgrades HTTPS to HTTP. Know which layer each operates on.
*   **Amplification Attacks:** DNS amplification and NTP amplification send small spoofed requests to public servers that return large responses to the victim. The key identifier is that the source IP is spoofed and the attacker exploits the size ratio between request and response.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include packet-level diagrams for ARP poisoning, DNS spoofing, and DDoS architecture that match exam scenario questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Network Attacks" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on the mechanism, the detection indicator, and the mitigation for each attack type.
*   **Required Video:** Watch the network attack video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos use network diagrams to show traffic flow during each attack.

---

### Lab & Command Integration
In this week's hands-on lab, you will use tools such as Wireshark to observe network traffic patterns characteristic of DDoS, ARP poisoning, and spoofing attacks. Recognizing these patterns in packet captures is a direct SY0-701 performance-based question (PBQ) skill.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to identify each attack from a traffic description or log snippet.
- [ ] Read the "Network Attacks" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the network attack video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Be able to match each attack type to its primary mitigation control.
- [ ] Proceed to the weekly hands-on lab activity.
