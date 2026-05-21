# Reading Guide: Module 07 - Network Security - Firewalls, IDS/IPS, VPNs
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 07 – Network Security: Firewalls, IDS/IPS, and VPNs**! This module covers the core network security controls that form the defensive perimeter of enterprise environments. SY0-701 tests your ability to select the right tool for a given scenario, understand how each device works, and distinguish between detection-only and prevention controls.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Stateful Firewall**: A firewall that tracks the state of active network connections (TCP three-way handshake, established sessions) and makes filtering decisions based on the full context of a connection, not just individual packets. Stateful inspection blocks unsolicited inbound packets that do not belong to an established session. This is the baseline standard for enterprise perimeter firewalls on SY0-701.
*   **Next-Generation Firewall (NGFW)**: A firewall that combines traditional stateful inspection with deep packet inspection (DPI), application-layer visibility, intrusion prevention, SSL inspection, and identity-based policies. NGFWs can block Facebook but allow business applications on the same port — a capability that packet-filter firewalls lack. SY0-701 tests NGFW features in application control scenarios.
*   **Intrusion Detection System (IDS)**: A passive monitoring device that analyzes network traffic or host activity and generates alerts when suspicious patterns are detected. An IDS does NOT block traffic — it only alerts. Signature-based IDS matches known attack patterns; anomaly-based IDS flags deviations from a baseline. False positives are a key IDS management challenge.
*   **Intrusion Prevention System (IPS)**: An active inline device that sits in the traffic path, detects malicious activity, and automatically blocks or drops the offending traffic in real time. An IPS can generate false positives that block legitimate traffic — this is why tuning signatures and establishing baselines is critical before deployment.
*   **VPN (Virtual Private Network)**: An encrypted tunnel that allows remote users or branch offices to communicate securely over an untrusted public network. Site-to-site VPNs connect entire networks; remote-access VPNs connect individual users. IPsec (tunnel or transport mode) and SSL/TLS VPNs are the two primary protocols tested on SY0-701.
*   **Network Access Control (NAC)**: A security solution that enforces policy-based access to the network by verifying that connecting devices meet security requirements (OS patch level, antivirus status, certificates) before granting access. Non-compliant devices are redirected to a quarantine VLAN for remediation. NAC is a key Zero Trust enabling technology.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Network security controls fall under **Domain 3 – Security Architecture (18%)** and **Domain 4 – Security Operations (28%)** of SY0-701. Expect scenario questions asking you to choose between IDS/IPS, firewall types, and VPN protocols.
*   **IDS vs. IPS in One Line:** IDS = monitor and alert (passive, out-of-band). IPS = monitor and block (active, inline). If the question asks which device stopped an attack, the answer is IPS. If it detected and reported but did not stop, the answer is IDS.
*   **False Positive vs. False Negative:** False positive = legitimate traffic flagged as malicious (causes disruption). False negative = malicious traffic not detected (causes breach). For IPS, false positives are the greater operational concern because they block real users.
*   **VPN Protocol Trap:** IPsec in tunnel mode encrypts the entire original packet including the IP header (used for site-to-site VPNs). IPsec in transport mode encrypts only the payload (used between hosts). SSL VPNs use TLS over port 443 and do not require a dedicated VPN client — useful for clientless remote access.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include firewall rule logic diagrams and IDS/IPS placement scenarios that directly mirror exam question formats.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Network Security" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on device placement, traffic flow, and the difference between detection and prevention.
*   **Required Video:** Watch the network security device video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos include network diagrams showing where each device is placed in a typical enterprise architecture.

---

### Lab & Command Integration
In this week's hands-on lab, you will configure basic firewall rules, analyze IDS alert logs, and verify VPN tunnel establishment. Understanding how to read firewall rule tables and IDS logs is a direct SY0-701 performance-based question skill.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to choose the correct device type for any given network security scenario.
- [ ] Read the "Network Security" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the network security video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: IDS = passive alert only; IPS = active inline block; NGFW = application-layer awareness.
- [ ] Proceed to the weekly hands-on lab activity.
