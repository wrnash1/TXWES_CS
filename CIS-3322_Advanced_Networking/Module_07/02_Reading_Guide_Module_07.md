# Reading Guide: Module 07 - Inter-VLAN Routing Solutions
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 07 - Inter-VLAN Routing Solutions**! This week's study material focuses on the core foundations and configuration mechanics of **Inter-VLAN Routing Solutions** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Router-on-a-stick**: An inter-VLAN routing method that uses a single physical router interface connected to a switch trunk port. The router interface is divided into logical subinterfaces, one per VLAN, each configured with `encapsulation dot1Q [vlan-id]` and an IP address in that VLAN's subnet. Traffic between VLANs exits the switch tagged, hits the router subinterface, gets re-tagged (or de-tagged), and returns via the same physical link.
*   **Subinterfaces**: Logical divisions of a physical router interface, created with commands like `interface g0/0.10`. Each subinterface is independently configured with a VLAN encapsulation and IP address. Subinterfaces share the physical bandwidth of the parent interface but appear to connected switches as separate Layer 3 routed interfaces.
*   **Layer 3 Switch SVI configuration**: A Switched Virtual Interface (SVI) is a virtual Layer 3 interface on a multilayer switch that represents a VLAN. Creating `interface vlan 10` and assigning an IP address effectively makes the switch the default gateway for all hosts in VLAN 10. SVIs require `ip routing` to be enabled globally on the switch and are more efficient than router-on-a-stick for high-traffic inter-VLAN routing.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** Inter-VLAN routing falls under **IP Connectivity (25%)** and **Network Access (20%)** of the CCNA 200-301 exam. Expect configuration scenarios requiring you to choose between router-on-a-stick and Layer 3 switch SVIs.
*   **Router-on-a-stick critical detail:** The physical interface (parent) must be up/up with `no shutdown` and typically has no IP address itself. The subinterface must have `encapsulation dot1Q [vlan-id]` configured **before** the IP address. Forgetting the encapsulation command is a common configuration mistake.
*   **Legacy vs current methods:** The exam may reference legacy "multi-layer switch with routed ports" vs. SVI. Know that SVIs require the `ip routing` command and that the SVI must be in an `up/up` state (which requires at least one active access port in that VLAN).
*   **Exam trap on native VLAN:** For the native VLAN subinterface in router-on-a-stick, use `encapsulation dot1Q [vlan-id] native`. Omitting `native` can cause duplicate IP/routing issues.
*   **Study Resource:** Watch the inter-VLAN routing episodes in the Jeremy's IT Lab CCNA free playlist, which demonstrate both router-on-a-stick and Layer 3 switch SVI configurations in Packet Tracer: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for "Inter-VLAN Routing" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Inter-VLAN Routing** in the Cisco Skills for All CCNA course. The labs walk through router-on-a-stick configuration and Layer 3 switch SVI setup with verification commands: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Switching, Routing and Wireless Essentials" — the Inter-VLAN Routing chapter.
*   **Required Video:** Watch the inter-VLAN routing episodes in the Jeremy's IT Lab CCNA complete playlist. The videos compare all three methods and demonstrate which `show` commands to use for verification: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure router subinterface: `interface g0/0.10`**: Create a subinterface on the router's physical interface. The number after the dot (.10) is a convention — it typically matches the VLAN ID for clarity, though any number is technically valid.
*   **Set encapsulation: `encapsulation dot1Q 10`**: This mandatory subinterface command tags all outbound frames with VLAN 10 and maps inbound 802.1Q-tagged frames from VLAN 10 to this subinterface. Follow immediately with `ip address [address] [mask]`.
*   **Configure IP address on SVI on L3 Switch: `interface vlan 10`**: On a multilayer switch, create the SVI for VLAN 10. Assign an IP address and bring it up with `no shutdown`. Verify with `show ip interface brief` and confirm the SVI state is up/up.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Inter-VLAN Routing** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the inter-VLAN routing episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
