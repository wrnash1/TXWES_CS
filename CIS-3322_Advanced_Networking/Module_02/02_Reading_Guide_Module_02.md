# Reading Guide: Module 02 - Subnetting and VLSM Configurations
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 02 - Subnetting and VLSM Configurations**! This week's study material focuses on the core foundations and configuration mechanics of **Subnetting and VLSM Configurations** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Variable Length Subnet Masking (VLSM)**: A subnetting technique that allows different-sized subnet masks to be used within the same major network address, enabling efficient IP address allocation. For example, a point-to-point WAN link can use a /30 while a large LAN segment uses a /24, conserving address space.
*   **IP allocation strategies**: Methods for assigning IP address blocks within an organization, including sequential allocation, subnetting by department or floor, and reserving ranges for servers, printers, and management interfaces. Cisco best practice recommends allocating subnets in powers of two to keep address space organized.
*   **CIDR prefix matching**: The process by which a router selects the routing table entry with the longest (most specific) prefix match to forward a packet. A route to 192.168.1.0/28 will be preferred over 192.168.1.0/24 for a destination address that falls within both ranges.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** IP Connectivity accounts for **25%** of the CCNA 200-301 exam — the largest single domain. Subnetting questions appear in multiple-choice and simulation formats; you must calculate subnet IDs, broadcast addresses, and usable host counts quickly.
*   **Speed technique:** Memorize the "magic number" method. Subtract the last non-zero octet of the subnet mask from 256 to get the block size. For 255.255.255.192 (/26), the block size is 64, giving subnets at .0, .64, .128, .192.
*   **Common Trap:** Do NOT confuse the number of addresses (2^n) with usable hosts (2^n - 2). The exam frequently offers both as answer choices. A /28 has 16 total addresses but only **14** usable hosts.
*   **VLSM rule:** Larger subnets must be assigned first (largest host requirement), then subdivide remaining space for smaller segments. Exam scenarios describe a network diagram; you must assign subnets without overlapping.
*   **Study Resource:** To reinforce subnetting calculation skills, watch the dedicated subnetting episodes in the Jeremy's IT Lab CCNA free playlist — they cover binary method and shortcut method side by side: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look specifically for the "Subnetting (Part 1 and Part 2)" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Subnetting and VLSM** in the Cisco Skills for All free CCNA course. The interactive exercises include subnet calculators and drag-and-drop host assignment tools: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to the "CCNA: Introduction to Networks" module on IPv4 Addressing.
*   **Required Video:** Watch the subnetting episodes in the Jeremy's IT Lab CCNA complete playlist. These videos build from binary fundamentals through VLSM design problems: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Subnet a class C network /24 into multiple /27 and /28 subnets**: Calculate the network address, broadcast address, and usable host range for each subnet on paper before entering configuration in Packet Tracer. Verify your math using `show ip interface brief`.
*   **Assign IP addresses to router interfaces**: Use `ip address [address] [mask]` in interface configuration mode, followed by `no shutdown`. Use `show interfaces` to confirm the interface is up/up with the correct IP.
*   **Verify ping connectivity between subnets**: After configuring routing or directly-connected interfaces, use `ping` from the router CLI to test end-to-end connectivity. A failure here indicates a subnet mask error or missing route.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Subnetting and VLSM** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the subnetting episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
