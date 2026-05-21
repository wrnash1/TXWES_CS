# Reading Guide: Module 05 - Spanning Tree Protocol (STP & RSTP)
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 05 - Spanning Tree Protocol (STP & RSTP)**! This week's study material focuses on the core foundations and configuration mechanics of **Spanning Tree Protocol (STP & RSTP)** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Root bridge election**: STP elects a single root bridge per VLAN by comparing Bridge IDs (BIDs). The BID is a combination of the 2-byte Bridge Priority (default 32768, adjustable in increments of 4096) plus a 6-byte MAC address. The switch with the lowest BID wins. Cisco supports per-VLAN spanning tree (PVST+), so a separate root bridge is elected for each VLAN.
*   **Port roles (Root, Designated, Blocked)**: In STP, every non-root switch selects its best path to the root bridge — that port becomes the **Root Port**. On each network segment, the switch offering the lowest-cost path to the root becomes the **Designated Port** for that segment. All remaining ports enter the **Blocked (Alternate/Backup)** role to prevent Layer 2 loops while maintaining loop-free topology.
*   **802.1D vs 802.1w (RSTP)**: IEEE 802.1D (classic STP) uses five port states — Blocking, Listening, Learning, Forwarding, and Disabled — and convergence can take 30–50 seconds. IEEE 802.1w (RSTP) reduces this to three states (Discarding, Learning, Forwarding) and converges in 1–2 seconds by introducing rapid transition mechanisms and new port roles (Alternate and Backup). Cisco's implementation of RSTP is called Rapid PVST+.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** STP falls under **Network Access (20%)** of the CCNA 200-301 exam. Expect STP topology diagrams where you must identify port roles and predict which ports are forwarding or blocked.
*   **Root bridge election rule:** Lowest Bridge Priority wins. If priorities are equal (e.g., all default 32768), the switch with the **lowest MAC address** wins. The exam frequently presents a tie-break scenario — remember MAC address is the tiebreaker, not hostname.
*   **Common Trap:** PortFast should only be enabled on **access ports** connected to end devices, never on ports connecting to other switches. Enabling PortFast on a switch-to-switch link bypasses STP and can cause a bridging loop. The exam tests this boundary.
*   **BPDU Guard:** Enable BPDU Guard on PortFast-enabled ports using `spanning-tree bpduguard enable` at the interface or `spanning-tree portfast bpduguard default` globally. If a BPDU is received, the port is placed in `err-disabled` state.
*   **Study Resource:** Watch the STP and RSTP episodes in the Jeremy's IT Lab CCNA free playlist, which include port role diagrams and cost calculation walk-throughs: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for the "Spanning Tree Protocol" series episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Spanning Tree Protocol** in the Cisco Skills for All CCNA course. The activities include STP port role identification exercises with multi-switch topologies: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Switching, Routing and Wireless Essentials" — the STP chapter.
*   **Required Video:** Watch the STP and RSTP episodes in the Jeremy's IT Lab CCNA complete playlist. These videos cover BID calculation, root bridge election, port role assignment, and the differences between 802.1D and 802.1w: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Inspect STP status: `show spanning-tree`**: This command displays the root bridge BID, your switch's own BID, port roles, port states, and path costs for each VLAN. Examine the output to confirm which port is the root port and which are designated or blocked.
*   **Force root bridge election: `spanning-tree vlan 1 root primary`**: This macro sets the bridge priority to 24576 (or lower) to ensure this switch becomes the root for VLAN 1. Alternatively, manually set priority with `spanning-tree vlan 1 priority 4096`.
*   **Configure PortFast on edge ports**: In interface configuration mode, enter `spanning-tree portfast` on any port connected to a PC or server. Immediately follow with `spanning-tree bpduguard enable` to protect against accidental switch connections.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Spanning Tree Protocol** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the STP and RSTP episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
