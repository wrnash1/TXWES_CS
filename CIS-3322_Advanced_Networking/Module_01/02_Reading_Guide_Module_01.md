# Reading Guide: Module 01 - Network Architectures & Topologies
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 01 - Network Architectures & Topologies**! This week's study material focuses on the core foundations and configuration mechanics of **Network Architectures & Topologies** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Three-tier architecture (Core, Distribution, Access)**: A hierarchical enterprise network design model with three distinct layers. The Core layer provides high-speed backbone switching, the Distribution layer enforces policies and performs inter-VLAN routing, and the Access layer connects end-user devices to the network.
*   **Collapsed Core design**: A two-tier network architecture where the Core and Distribution layers are merged into a single layer, typically used in smaller campus networks to reduce cost and complexity while still maintaining logical separation of access-layer devices.
*   **Spine-leaf topology**: A two-tier data center architecture where every leaf switch connects to every spine switch, providing predictable low-latency and high-bandwidth paths. This design is used in modern hyperscale data centers and eliminates the Spanning Tree Protocol dependency.
*   **Network topology**: The physical or logical arrangement of nodes and connections in a network. Common topologies tested on the CCNA include star, mesh, point-to-point, hub-and-spoke, and full mesh, each with different fault-tolerance and cost trade-offs.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** Network Fundamentals accounts for **20%** of the CCNA 200-301 exam. Topology and architecture questions frequently appear as scenario diagrams — practice reading and labeling three-tier diagrams.
*   **Common Trap:** The exam often asks you to identify which layer performs a function. Remember: routing and policy enforcement (ACLs, QoS) belong at the **Distribution** layer, not the Core. The Core layer exists purely for fast forwarding — never apply ACLs there.
*   **Memorize the difference:** Collapsed core = two tiers (no dedicated core); standard three-tier = separate core, distribution, and access. Exam scenarios will describe a "small campus network" to hint at collapsed core.
*   **Spine-leaf key fact:** Every leaf connects to every spine — this creates equal-cost multipath (ECMP) routing. The CCNA exam tests the concept, not detailed spine-leaf CLI configuration.
*   **Study Resource:** To reinforce these concepts visually, watch the Jeremy's IT Lab CCNA free course videos on network architecture and topology: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Start with the "Network Topology Overview" section for diagrams of each tier.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Network Architectures and Topologies** in the free Cisco Skills for All CCNA course, which includes interactive topology diagrams and module quizzes: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to the "CCNA: Introduction to Networks" or "CCNA: Switching, Routing and Wireless Essentials" course.
*   **Required Video:** Watch the video lecture on **Network Architectures & Topologies** in the Jeremy's IT Lab free CCNA playlist. Focus on the episodes covering enterprise network design and the three-tier model: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Draw a three-tier network diagram in Packet Tracer**: Place Core, Distribution, and Access layer switches in a Packet Tracer topology. Label each device by its layer role and connect them with appropriate trunk links.
*   **Examine routing links at Distribution layer**: On a multilayer switch, verify that Layer 3 routing is enabled between VLANs at the Distribution layer using `show ip route` and `show interfaces`.
*   **Verify VLAN assignments at Access layer switches**: Use `show vlan brief` to confirm that access-layer switch ports are correctly assigned to their respective VLANs before inter-VLAN traffic is tested.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Network Architectures and Topologies** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the video lecture on **Network Architectures & Topologies** in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
