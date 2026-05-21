# Reading Guide: Module 04 - Switching Concepts & VLANs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 04 - Switching Concepts & VLANs**! This week's study material focuses on the core foundations and configuration mechanics of **Switching Concepts & VLANs** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **VLAN membership**: The assignment of a switch port to a specific Virtual LAN, which logically segments the network at Layer 2. Access ports carry traffic for a single VLAN and strip the VLAN tag before delivering frames to end devices, while trunk ports carry traffic for multiple VLANs simultaneously using 802.1Q tagging.
*   **Trunking protocols (802.1Q)**: IEEE 802.1Q is the industry-standard frame-tagging protocol used on VLAN trunk links. It inserts a 4-byte tag field into the Ethernet frame header containing the VLAN ID (12 bits, supporting VLANs 1–4094). The native VLAN is the only VLAN whose frames are sent untagged across an 802.1Q trunk.
*   **Native VLAN**: The VLAN whose traffic crosses an 802.1Q trunk link without a VLAN tag applied. Both ends of a trunk must agree on the native VLAN — a mismatch causes CDP native VLAN mismatch warnings and can create a security vulnerability known as a VLAN hopping attack. Best practice is to change the native VLAN from the default (VLAN 1) to an unused VLAN.
*   **DTP (Dynamic Trunking Protocol)**: A Cisco-proprietary protocol that allows switch ports to automatically negotiate trunk formation with a neighboring switch. DTP modes include `dynamic auto`, `dynamic desirable`, `trunk`, and `access`. Security best practice is to disable DTP on all user-facing ports with `switchport nonegotiate` or `switchport mode access` to prevent rogue switches from forming unauthorized trunks.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** LAN Switching falls under **Network Access (20%)** of the CCNA 200-301 exam. Expect 4–6 VLAN questions including trunk configuration scenarios.
*   **Common Trap:** Know the difference between `switchport mode trunk` (forces trunk), `switchport mode dynamic desirable` (actively negotiates), and `switchport mode dynamic auto` (passively waits). Two ports set to `dynamic auto` will NOT form a trunk — exam scenarios test this frequently.
*   **Native VLAN pitfall:** If native VLAN is different on each end of a trunk, the switch logs a CDP warning and traffic can be miscategorized. The exam may show `%CDP-4-NATIVE_VLAN_MISMATCH` in a syslog output and ask you to identify the cause.
*   **Must-know commands:** `vlan [id]` (creates VLAN in VLAN database), `switchport mode access`, `switchport access vlan [id]`, `switchport mode trunk`, `switchport trunk allowed vlan [list]`, `show vlan brief`, `show interfaces trunk`.
*   **Study Resource:** Watch the VLANs and trunking episodes in the Jeremy's IT Lab CCNA free playlist, which demonstrate Packet Tracer configurations and cover DTP negotiation tables: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for episodes covering "VLANs," "Trunk Ports," and "DTP."

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Switching Concepts and VLANs** in the Cisco Skills for All CCNA course. The labs include Packet Tracer activities where you configure access ports, trunk ports, and verify VLAN assignments: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Switching, Routing and Wireless Essentials" — the VLANs and Trunking chapter.
*   **Required Video:** Watch the VLAN and trunking episodes in the Jeremy's IT Lab CCNA complete playlist. These videos cover the full 802.1Q tagging process, DTP mode combinations, and native VLAN configuration: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create VLAN 10 and 20: `vlan 10`**: Enter VLAN database configuration mode on the switch, create VLAN 10 with `vlan 10` and name it with `name [name]`. Verify with `show vlan brief`.
*   **Assign ports to VLAN: `switchport access vlan 10`**: In interface configuration mode, set the port mode to access and assign it to the VLAN. Verify the port's VLAN membership using `show vlan brief` or `show interfaces [id] switchport`.
*   **Configure trunk link: `switchport mode trunk`**: Set the uplink port to trunk mode. Then use `show interfaces trunk` to confirm the port is trunking and which VLANs are allowed and active on the trunk.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Switching Concepts & VLANs** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the VLAN and trunking episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
