# Reading Guide: Module 06 - EtherChannel Link Aggregation
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 06 - EtherChannel Link Aggregation**! This week's study material focuses on the core foundations and configuration mechanics of **EtherChannel Link Aggregation** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **LACP vs PAgP**: LACP (Link Aggregation Control Protocol, IEEE 802.3ad) is the open-standard protocol for dynamically negotiating EtherChannel bundles between any vendor's equipment. PAgP (Port Aggregation Protocol) is Cisco-proprietary and only works between Cisco devices. Both protocols have an active/passive (LACP) or desirable/auto (PAgP) negotiation mode — two passive or two auto ports will not form a channel. LACP is preferred in multi-vendor environments.
*   **Port channel configuration**: A logical bundle interface (`interface port-channel [number]`) that represents all physical member ports in an EtherChannel. Configuration applied to the port-channel interface (VLAN membership, trunk settings, IP address) automatically applies to all member physical ports. Member ports are added with `channel-group [number] mode [mode]` in interface configuration.
*   **Load balancing algorithms**: EtherChannel distributes traffic across member links using a hashing algorithm based on configurable parameters. Options include source MAC, destination MAC, source-destination MAC (default on most Cisco platforms), source IP, destination IP, or source-destination IP. The hash is computed per-flow, so individual flows are not split across links — bandwidth aggregation is across multiple concurrent flows.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** EtherChannel falls under **Network Access (20%)** of the CCNA 200-301 exam. Expect configuration scenario questions and questions asking why an EtherChannel fails to form.
*   **Common Trap:** EtherChannel member ports must have matching configuration — same speed, duplex, VLAN membership, trunk settings, and STP settings. A mismatch in any parameter causes the channel to fail. The exam frequently presents `show etherchannel summary` output with a suspended (S) status and asks you to identify the cause.
*   **Mode compatibility:** LACP: `active + active = forms`, `active + passive = forms`, `passive + passive = NO`. PAgP: `desirable + desirable = forms`, `desirable + auto = forms`, `auto + auto = NO`. Static (on/on) always forms but has no negotiation. The exam tests all six combinations.
*   **`show etherchannel summary` flags:** Know what P (bundled), S (suspended), I (individual/not bundled), D (down) mean. An (S) flag means a port is suspended due to a configuration mismatch.
*   **Study Resource:** Watch the EtherChannel episodes in the Jeremy's IT Lab CCNA free playlist, which demonstrate LACP and PAgP mode combinations and the port-channel verification commands: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for the "EtherChannel" episode.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **EtherChannel Link Aggregation** in the Cisco Skills for All CCNA course. The labs include Packet Tracer activities where you configure LACP and PAgP channels and verify their status: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Switching, Routing and Wireless Essentials" — the EtherChannel chapter.
*   **Required Video:** Watch the EtherChannel episode in the Jeremy's IT Lab CCNA complete playlist. This video covers LACP vs PAgP, mode combinations, load-balancing options, and common configuration mistakes: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure ports for active negotiation: `channel-group 1 mode active`**: On each member interface (e.g., `interface range g0/0-1`), enter `channel-group 1 mode active` to use LACP active mode. Both sides must be active or one active + one passive. This creates the port-channel interface automatically.
*   **Verify port-channel interface state: `show etherchannel summary`**: Review the output for channel group number, protocol (LACP/PAgP/static), and port status flags. Confirm member ports show (P) for bundled and the port-channel shows (SU) — layer 2 in use.
*   **Configure EtherChannel load-balancing method**: Enter `port-channel load-balance [method]` in global configuration mode to set the hashing algorithm (e.g., `src-dst-mac`). Verify with `show etherchannel load-balance`.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **EtherChannel Link Aggregation** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the EtherChannel episode in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
