# Reading Guide: Module 02 - VLANs
## Course: CIS-3321_Network_Admin (3321_Network_Admin - CompTIA Network+ (N10-008))

---

### Introduction
Welcome to **Module 02 - VLANs**! This week's study material focuses on the core foundations and configuration mechanics of **VLANs** as aligned with the **3321_Network_Admin - CompTIA Network+ (N10-008)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Layer 1 (Physical)**: Hubs, Repeaters, Cables.
*   **Layer 2 (Data Link)**: Switches, Bridges, Access Points. (They make forwarding decisions based on **MAC Addresses**).
*   **Layer 3 (Network)**: Routers, Layer 3 Switches. (They make routing decisions based on **IP Addresses**).
*   **Layer 7 (Application)**: Firewalls, Proxies, Load Balancers.
*   **Class A**: 1.0.0.0 to 126.255.255.255 (Default mask /8)
*   **Class B**: 128.0.0.0 to 191.255.255.255 (Default mask /16)
*   **Class C**: 192.0.0.0 to 223.255.255.255 (Default mask /24)
*   **10.x.x.x**: 10.0.0.0 - 10.255.255.255 (1 private Class A network)
*   **172.16.x.x**: 172.16.0.0 - 172.31.255.255 (16 private Class B networks)
*   **192.168.x.x**: 192.168.0.0 - 192.168.255.255 (256 private Class C networks)
*   **Link-Local Address**: Starts with `fe80::`. Every IPv6 device automatically generates one of these to talk to devices on the same local network.
*   **VLAN (Virtual LAN)**: Logically separating a single physical switch into multiple isolated broadcast domains.
*   **802.1Q**: The IEEE standard for VLAN trunking (tagging frames with their VLAN ID).
*   **ARP (Address Resolution Protocol)**: The protocol used to find the MAC address associated with a known IP address.
*   **PoE (Power over Ethernet)**: Sending electrical power over standard Cat5e/Cat6 ethernet cables to power devices like IP cameras or Access Points (802.3af/at standards).

---

### 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource:** To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link](https://www.youtube.com/results?search_query=3321_Network_Admin+-+CompTIA+Network%2B+%28N10-008%29+VLANs).

---

### Lab & Command Integration
In this week's hands-on lab, you will run command sequences to verify configuration files and check service statuses. Make sure to execute administrative commands using elevated privileges (sudo/Administrator) and review console outputs for errors.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Watch the curated YouTube study streams matching **VLANs**.
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
