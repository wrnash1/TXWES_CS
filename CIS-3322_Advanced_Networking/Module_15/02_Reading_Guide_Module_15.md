# Reading Guide: Module 15 - CCNA Review and Diagnostics
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 15 - CCNA Review and Diagnostics**! This week's study material focuses on the core foundations and configuration mechanics of **CCNA Review and Diagnostics** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Troubleshooting methodology**: A systematic approach to diagnosing network problems using the OSI model as a framework. Cisco recommends starting at Layer 1 (physical cabling, interface status) and working up through Layer 2 (switching, VLAN, STP), Layer 3 (IP addressing, routing), and above (ACLs, NAT, application issues). Alternatively, the "divide and conquer" method starts at the layer most likely to have the fault based on symptoms.
*   **Interface states**: Cisco IOS displays two status values for each interface: the physical layer state and the line protocol state. `up/up` = fully operational. `down/down` = Layer 1 problem (no cable signal, speed mismatch). `up/down` = Layer 2 problem (encapsulation mismatch, keepalive failure, remote end shut down). `administratively down/down` = the interface has been shut down with the `shutdown` command. Knowing these states is essential for exam troubleshooting scenarios.
*   **Routing loops**: A network condition where packets circulate indefinitely between routers because each router believes the best path to a destination is through another router in the loop. Routing loops cause TTL expiration, high CPU utilization, and network outages. Distance-vector protocols prevent loops using split horizon, route poisoning, hold-down timers, and maximum hop count (e.g., RIP's maximum of 15 hops — 16 is unreachable).
*   **Mismatch symptoms**: Configuration inconsistencies between directly connected devices that prevent communication. Common mismatches include: duplex mismatch (one end full-duplex, other half-duplex — causes late collisions and CRC errors), speed mismatch (causes interface to stay down), native VLAN mismatch (causes CDP warnings and traffic misclassification), and OSPF area mismatch (prevents neighbor adjacency).

---

### 2. Certification Exam Tips
*   **CCNA Domain:** Troubleshooting content is embedded across all domains but is especially prominent in **IP Connectivity (25%)** and **Network Access (20%)**. Exam simulations (sim-lets and drag-and-drops) frequently test troubleshooting methodology.
*   **Interface status cheat sheet:** Know all four `show interfaces` status combinations and their Layer 1/Layer 2 meanings. The exam will show a status and ask you to identify the layer and likely cause. `up/down` on a serial interface often means PPP/HDLC encapsulation mismatch.
*   **`show` commands to memorize:** `show ip interface brief` (all interfaces at a glance), `show interfaces [id]` (detailed stats including errors), `show ip route` (routing table), `show ip ospf neighbor` (OSPF adjacency), `show vlan brief` (VLAN assignments), `show interfaces trunk` (trunk status).
*   **Duplex mismatch identification:** A full-duplex end sees late collisions; the half-duplex end sees regular collisions. CRC errors appear on both sides. This is a common exam troubleshooting scenario — look for a mix of error types in `show interfaces` output.
*   **Study Resource:** Watch the troubleshooting and diagnostics episodes in the Jeremy's IT Lab CCNA free playlist, which include systematic OSI-layer troubleshooting walkthroughs and interpretation of IOS `show` command output: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for troubleshooting-focused episodes throughout the playlist.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the troubleshooting sections in the Cisco Skills for All CCNA courses. Focus on chapters that cover systematic fault isolation using `show` commands, reading interface counters, and diagnosing routing and switching problems: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Review the troubleshooting labs across all three CCNA course modules.
*   **Required Video:** Watch the diagnostic and troubleshooting episodes in the Jeremy's IT Lab CCNA complete playlist. These videos walk through realistic troubleshooting scenarios step-by-step, modeling the methodology you will need for the CCNA exam simulations: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Diagnose a duplex mismatch between router and switch**: Configure one end of a link as full-duplex and the other as half-duplex. Observe the error counters in `show interfaces` — look for late collisions, CRC errors, and input errors. Resolve by matching duplex settings on both ends.
*   **Solve a routing loop issue using CLI interface counters**: In a Packet Tracer scenario with a misconfigured route, observe TTL-exceeded ICMP messages with `debug ip icmp`. Use `show ip route` to trace the loop and identify the incorrect static route or routing protocol configuration.
*   **Trace routing paths: `traceroute`**: Use Cisco IOS `traceroute [destination]` to identify the hop-by-hop path. Interpret `*` (timeout), `!H` (host unreachable), and `!N` (network unreachable) responses to locate the failing hop.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the troubleshooting sections in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the diagnostic and troubleshooting episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
