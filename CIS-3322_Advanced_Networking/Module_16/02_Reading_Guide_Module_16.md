# Reading Guide: Module 16 - Final Exam Prep & Cisco CCNA 200-301 Certification
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 16 - Final Exam Prep & Cisco CCNA 200-301 Certification**! This final module consolidates all course content and prepares you to sit the Cisco CCNA 200-301 certification exam. Review every glossary term, study the exam domain weightings below, and complete the final practice activities before scheduling your exam at a Pearson VUE testing center.

As a student, you should now be able to configure, verify, and troubleshoot all major topics covered across Modules 01–15. This module brings those topics together with exam-specific strategies, domain breakdowns, and a final review of the most heavily tested concepts. Cisco CCNA certification validates that you can install, configure, operate, and troubleshoot medium-sized routed and switched networks.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **CCNA 200-301 exam domains**: The Cisco CCNA 200-301 exam covers six weighted domains: Network Fundamentals (20%), Network Access (20%), IP Connectivity (25%), IP Services (10%), Security Fundamentals (15%), and Automation and Programmability (10%). Understanding which domain a topic belongs to helps you prioritize study time — IP Connectivity (25%) and Network Fundamentals (20%) together represent nearly half the exam.
*   **Exam format and scoring**: The CCNA 200-301 exam is 120 minutes long with approximately 100–120 questions in multiple-choice, drag-and-drop, fill-in-the-blank, and simulation (Packet Tracer–based) formats. The passing score is 825 out of 1000. Questions are adaptive — you cannot go back and change answers. Simulation questions are worth more points and require you to configure devices in a virtual IOS environment.
*   **Cisco IOS verification command suite**: The most frequently tested IOS `show` commands across the CCNA exam include: `show ip interface brief`, `show ip route`, `show ip ospf neighbor`, `show running-config`, `show interfaces`, `show vlan brief`, `show interfaces trunk`, `show etherchannel summary`, `show ip nat translations`, `show spanning-tree`, and `show mac address-table`. Know what each command displays and how to interpret its output.

---

### 2. Certification Exam Tips
*   **CCNA Exam Domain summary — memorize these weights:**
    *   Network Fundamentals: **20%** (OSI model, TCP/UDP, IPv4/IPv6 addressing, topologies)
    *   Network Access: **20%** (VLANs, trunking, STP/RSTP, EtherChannel, wireless)
    *   IP Connectivity: **25%** (static routing, OSPF, IPv6 routing — highest weight domain)
    *   IP Services: **10%** (NAT/PAT, DHCP, DNS, NTP, SNMP, Syslog, TFTP/FTP)
    *   Security Fundamentals: **15%** (ACLs, port security, DHCP snooping, DAI, VPNs, device hardening)
    *   Automation and Programmability: **10%** (SDN, REST APIs, JSON, Ansible/Puppet/Chef, DNA Center)
*   **Top 5 exam traps to avoid:**
    1. Standard ACL = near destination; Extended ACL = near source.
    2. Two `dynamic auto` LACP/DTP ports = NO channel/trunk formed.
    3. OSPF neighbors require matching Hello/Dead timers, area ID, subnet mask, and MTU.
    4. Default bridge priority is 32768; the lowest BID wins root bridge election.
    5. `ipv6 unicast-routing` is required for a Cisco router to forward IPv6 packets.
*   **Simulation question strategy:** Read the question carefully, identify what is broken, and make the minimum change to fix it. Use `show` commands first to verify the current state before making changes. Common sim tasks: configure an access/trunk port, fix an OSPF neighbor issue, configure PAT, or fix an ACL.
*   **Study Resource:** Complete the full Jeremy's IT Lab CCNA free course playlist as a final review. Each episode includes practice questions. Also complete the free Cisco Skills for All CCNA assessment exams for all three course modules: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). For additional practice exams, use [Cisco's official CCNA Learning Path on the Skills for All portal](https://skillsforall.com/).

---

### Required Readings & Videos
To prepare for the CCNA 200-301 exam, you must complete the following readings and videos:
*   **Required Reading:** Complete the full assessment exams for all three Cisco Skills for All CCNA courses to identify knowledge gaps before the actual exam. These assessments closely mirror the real exam question style and scenario complexity: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Complete "CCNA: Introduction to Networks," "Switching, Routing and Wireless Essentials," and "Enterprise Networking, Security, and Automation" final assessments.
*   **Required Video:** Review any Jeremy's IT Lab CCNA episodes covering topics where you scored low on practice exams. The full playlist is organized by topic and can be searched for specific subjects. Pay special attention to OSPF, ACLs, NAT, and Automation episodes, which are frequently underrepresented in student preparation: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on review, you will perform the following steps to validate full-course mastery:
*   **Complete a comprehensive Packet Tracer scenario**: Build a multi-router, multi-switch topology that includes VLANs, trunking, inter-VLAN routing with SVIs, OSPF, NAT/PAT, and basic ACLs. Verify end-to-end connectivity with `ping` and `traceroute`.
*   **Run all major verification commands**: Execute the full suite of CCNA verification commands on each device (`show ip route`, `show ip ospf neighbor`, `show vlan brief`, `show interfaces trunk`, `show ip nat translations`, `show etherchannel summary`) and document your expected vs. actual outputs.
*   **Perform a full troubleshooting drill**: Intentionally introduce three faults (e.g., wrong native VLAN, incorrect wildcard mask in OSPF, missing `ip nat inside` on an interface), then systematically diagnose and correct each one using only `show` commands and targeted fixes.


---

### 3. Study Checklist
- [ ] Review all glossary terms from Modules 01–15.
- [ ] Complete the final assessments in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Review all missed topics using [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Complete the comprehensive Packet Tracer review lab.
- [ ] Schedule your CCNA 200-301 exam at a Pearson VUE testing center.
