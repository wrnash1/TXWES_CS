# Reading Guide: Module 11 - NAT and PAT Configurations
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 11 - NAT and PAT Configurations**! This week's study material focuses on the core foundations and configuration mechanics of **NAT and PAT Configurations** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Static vs Dynamic NAT**: Static NAT creates a permanent one-to-one mapping between a specific private (inside local) IP address and a specific public (inside global) IP address — commonly used for servers that must be consistently reachable from the internet. Dynamic NAT maps private addresses to a pool of public addresses on a first-come, first-served basis, but still requires a one-to-one public IP for each active session, meaning the pool may be exhausted.
*   **Port Address Translation (PAT) / Overload**: PAT (also called NAT Overload) maps many private IP addresses to a single public IP address by tracking unique source port numbers for each session. This allows hundreds or thousands of internal hosts to share one public IP simultaneously. PAT is the most common NAT implementation in home and small enterprise networks, configured with the `overload` keyword on Cisco routers.
*   **Inside local/global definitions**: The four NAT address terms are: **Inside Local** (private IP of internal host as seen from inside), **Inside Global** (public IP of internal host as seen from outside), **Outside Local** (IP of external host as seen from inside — typically the same as outside global), **Outside Global** (real IP of the external host). The exam frequently asks you to identify which term applies to a specific address in a NAT translation table.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** NAT falls under **IP Services (10%)** of the CCNA 200-301 exam. Expect 2–3 NAT questions focusing on address terminology and PAT configuration.
*   **Four NAT terms — memorize the matrix:** Inside = your network. Outside = the internet. Local = as seen from inside. Global = as seen from outside. So: Inside Local = your host's private IP (10.x.x.x). Inside Global = the public IP your host appears to be when seen from the internet.
*   **PAT configuration syntax:** The key command is `ip nat inside source list [acl] interface [WAN-interface] overload`. The ACL identifies which inside addresses are translated. The `overload` keyword enables PAT. Interfaces must be tagged `ip nat inside` or `ip nat outside`.
*   **Common Trap:** Forgetting to tag interfaces with `ip nat inside` and `ip nat outside` is the most common PAT configuration error. Without these tags, NAT does not function even if the translation rule is correct.
*   **Study Resource:** Watch the NAT and PAT episodes in the Jeremy's IT Lab CCNA free playlist, which demonstrate static NAT, dynamic NAT, and PAT configurations with Packet Tracer and `show ip nat translations` verification: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for the "NAT" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **NAT and PAT** in the Cisco Skills for All CCNA course. The content includes NAT terminology diagrams, configuration examples, and Packet Tracer labs: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Enterprise Networking, Security, and Automation" — the NAT chapter.
*   **Required Video:** Watch the NAT episodes in the Jeremy's IT Lab CCNA complete playlist. These videos cover all four NAT address types, static/dynamic/PAT configurations, and troubleshooting with `show ip nat translations` and `debug ip nat`: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure NAT pool: `ip nat pool [name] [start-ip] [end-ip] netmask [mask]`**: Define a pool of public IP addresses for dynamic NAT. Give the pool a descriptive name. Then create an ACL to match inside hosts and link the pool with `ip nat inside source list [acl] pool [name]`.
*   **Map inside list to interface with overload: `ip nat inside source list 1 interface g0/0 overload`**: This PAT command translates all addresses matching ACL 1 to the IP address of interface g0/0, using unique port numbers to track each session. Tag the LAN interface `ip nat inside` and the WAN interface `ip nat outside`.
*   **Verify mappings: `show ip nat translations`**: This command displays all active NAT translation entries, including the inside local, inside global, outside local, and outside global addresses and ports for each active session.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **NAT and PAT** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the NAT episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
