# Reading Guide: Module 03 - IPv6 Addressing and Configuration
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 03 - IPv6 Addressing and Configuration**! This week's study material focuses on the core foundations and configuration mechanics of **IPv6 Addressing and Configuration** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **IPv6 link-local vs global unicast**: Link-local addresses (FE80::/10) are automatically generated on every IPv6-enabled interface and are used only for communication within a single network segment — they are never routed. Global unicast addresses (2000::/3) are publicly routable IPv6 addresses equivalent to public IPv4 addresses, assigned either statically, through SLAAC, or via DHCPv6.
*   **SLAAC (Stateless Address Autoconfiguration)**: A mechanism that allows IPv6 hosts to automatically configure their own global unicast address without a DHCP server. The host combines the /64 network prefix received in a Router Advertisement (RA) message with an interface identifier (derived from the MAC address via EUI-64 or randomly generated) to form a complete 128-bit address.
*   **EUI-64 configuration**: A method of deriving a 64-bit interface identifier from a device's 48-bit MAC address. The process inserts the hex value FFFE in the middle of the MAC address and inverts the seventh bit (the universal/local bit). On Cisco routers, `ipv6 address 2001:db8::/64 eui-64` instructs the interface to generate its host portion using this method.
*   **Static routing in IPv6**: The manual configuration of IPv6 routes using the command `ipv6 route [destination/prefix-length] [next-hop | exit-interface]`. IPv6 static routes require `ipv6 unicast-routing` to be enabled globally, and next-hop link-local addresses must specify the exit interface (e.g., `ipv6 route ::/0 GigabitEthernet0/0 FE80::1`).

---

### 2. Certification Exam Tips
*   **CCNA Domain:** IP Services and IP Connectivity together cover a large portion of the exam. IPv6 falls primarily under **IP Connectivity (25%)** and **Network Fundamentals (20%)**. Expect 3–5 IPv6 questions.
*   **Common Trap:** The exam frequently confuses students between link-local (FE80::/10), unique local (FC00::/7), and global unicast (2000::/3) address types. Memorize these ranges — questions will describe an address and ask you to identify its type or valid scope.
*   **Must-know commands:** `ipv6 unicast-routing` (global config, enables IPv6 routing), `ipv6 address [addr/prefix]` (interface config), `show ipv6 interface brief`, `show ipv6 route`, `show ipv6 neighbors` (IPv6 equivalent of ARP table).
*   **EUI-64 trap:** The exam may give you a MAC address and ask you to compute the EUI-64 interface ID. Practice inserting FFFE and flipping bit 7. MAC 00:1A:2B:3C:4D:5E becomes 021A:2BFF:FE3C:4D5E.
*   **Study Resource:** Watch the IPv6 addressing and configuration episodes in the Jeremy's IT Lab CCNA free playlist, which include visual breakdowns of EUI-64 conversion and SLAAC operation: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Search for "Jeremy's IT Lab IPv6" episodes 32–34.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **IPv6 Addressing and Configuration** in the Cisco Skills for All CCNA course. The module includes interactive address-type identification exercises and EUI-64 calculation walkthroughs: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Introduction to Networks" — the IPv6 Addressing chapter.
*   **Required Video:** Watch the IPv6 addressing and static routing episodes in the Jeremy's IT Lab CCNA complete playlist. These videos cover all address types, SLAAC, EUI-64, and Cisco IOS CLI configuration: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Enable IPv6 routing globally: `ipv6 unicast-routing`**: Enter this command in global configuration mode on a Cisco router. Without it, the router discards IPv6 packets rather than forwarding them, even if interfaces have IPv6 addresses assigned.
*   **Configure interface with IPv6: `ipv6 address 2001:db8::1/64`**: Assign a static global unicast address to a router interface. Verify the assignment and confirm the auto-generated link-local address using `show ipv6 interface [interface-id]`.
*   **Verify IPv6 neighbor discovery tables**: Use `show ipv6 neighbors` to view the IPv6 neighbor cache (equivalent of the IPv4 ARP table). Confirm that the router has learned neighbor addresses via Neighbor Discovery Protocol (NDP) after successful pings.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **IPv6 Addressing and Configuration** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the IPv6 episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
