# Reading Guide: Module 04 - IPv6 Addressing and Transition Technologies
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 04 – IPv6 Addressing and Transition Technologies**! IPv6 is a growing presence on the CompTIA Network+ N10-009 exam, appearing in both conceptual questions and scenario-based troubleshooting. You must understand IPv6 address types, notation rules, how addresses are auto-configured, and the transition technologies that allow IPv6 and IPv4 to coexist. The exam tests IPv6 with the same rigor as IPv4.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **IPv6 Address**: A 128-bit address written as eight groups of four hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334). Provides approximately 3.4 × 10^38 unique addresses, solving IPv4 exhaustion.
*   **IPv6 Abbreviation Rules**: Two rules simplify notation. (1) Leading zeros in any group may be omitted (0db8 → db8). (2) One contiguous sequence of all-zero groups may be replaced with :: (double colon), but only once per address.
*   **Global Unicast Address**: IPv6's equivalent of a public routable IPv4 address. Begins with the prefix **2000::/3** (addresses starting with 2 or 3). Globally unique and routable on the internet.
*   **Link-Local Address**: Automatically generated on every IPv6-enabled interface using the prefix **fe80::/10**. Used only for communication on the local network segment — not routable. Equivalent to APIPA in IPv4. Generated using EUI-64 or randomly from the MAC address.
*   **Loopback Address**: **::1/128** — the IPv6 equivalent of IPv4's 127.0.0.1. Used to test the local IP stack without sending traffic to the network.
*   **Unique Local Address (ULA)**: Prefix **fc00::/7** (typically fd00::/8 in practice). IPv6's equivalent of RFC 1918 private addresses — not routable on the public internet. Used for internal networks.
*   **Multicast Address**: Prefix **ff00::/8**. Replaces IPv4 broadcast — packets are delivered to all members of a multicast group rather than broadcast to all hosts. IPv6 has no broadcast.
*   **Anycast Address**: An address assigned to multiple interfaces; packets are delivered to the nearest interface holding that address (routing-metric based). Used for load distribution and redundancy.
*   **EUI-64**: A method for auto-generating the 64-bit host portion of an IPv6 address from a 48-bit MAC address. The MAC is split in half, FFFE is inserted in the middle, and the seventh bit (Universal/Local bit) is flipped.
*   **SLAAC (Stateless Address Autoconfiguration)**: IPv6 mechanism allowing a host to automatically configure its own IP address using the network prefix advertised by a router (via Router Advertisement messages) combined with its EUI-64 host ID — no DHCP server required.
*   **DHCPv6**: Stateful or stateless DHCPv6 can be used to assign IPv6 addresses and provide configuration options (like DNS) to hosts. Stateful DHCPv6 tracks address assignments; stateless DHCPv6 only provides options like DNS while SLAAC handles the address.
*   **Dual Stack**: A transition technology where a network device runs both IPv4 and IPv6 simultaneously on the same interface. The device can communicate natively using either protocol. The preferred transition method.
*   **Tunneling (6to4, Teredo, ISATAP)**: Techniques that encapsulate IPv6 packets inside IPv4 packets to traverse IPv4-only infrastructure. 6to4 uses the prefix 2002::/16; Teredo (Windows) uses 2001::/32; ISATAP uses link-local addresses over IPv4 tunnels.
*   **NAT64**: Translates between IPv6 and IPv4 addresses, allowing IPv6-only clients to communicate with IPv4-only servers. Used at the network border when full dual-stack is not feasible.
*   **NDP (Neighbor Discovery Protocol)**: IPv6 replacement for ARP. Uses ICMPv6 messages to discover the link-layer addresses of neighboring devices, detect duplicate addresses (DAD — Duplicate Address Detection), and find default routers.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** IPv6 falls under **Domain 1.0 – Networking Concepts (23%)**. Know address types by prefix — the exam gives you an address and asks what type it is.
*   **Address type quick reference**: fe80:: = Link-Local; ::1 = Loopback; ff00:: = Multicast; 2001::/2xxx: = Global Unicast; fc00::/fd00:: = Unique Local. Memorize these prefixes cold.
*   **IPv6 has no broadcast**: The exam will sometimes present "broadcast" as an IPv6 option — it does not exist. IPv6 uses multicast instead. All-nodes multicast is ff02::1; all-routers multicast is ff02::2.
*   **NDP replaces ARP**: On the exam, any scenario asking about IPv6 address resolution on a local segment refers to NDP (ICMPv6), not ARP. ARP does not exist in IPv6.
*   **Dual stack is the preferred transition answer**: When the exam asks the BEST transition method for a network supporting both IPv4 and IPv6 clients, the answer is almost always dual stack unless the scenario specifically describes a purely IPv4 or IPv6 constraint.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) has a dedicated IPv6 module covering all address types and transition technologies tested on the exam.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **IPv6 Addressing** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Pay particular attention to SLAAC, NDP, and the address type prefixes.
*   **Required Video:** Watch Professor Messer's **IPv6 Addressing** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/). Focus on the address type identification segments.

---

### Lab & Command Integration
In this week's hands-on lab, you will use `ipconfig /all` (Windows) or `ip addr` (Linux) to observe both IPv4 and IPv6 address assignments on your VM interfaces, identify the link-local address generated automatically, and use `ping6` or `ping -6` to test IPv6 loopback and link-local connectivity.

---

### 3. Study Checklist
*   [ ] Memorize all IPv6 address type prefixes: Global Unicast, Link-Local, Loopback, Multicast, Unique Local.
*   [ ] Practice applying the two IPv6 abbreviation rules to shorten full addresses.
*   [ ] Understand SLAAC and EUI-64 host ID generation from a MAC address.
*   [ ] Know dual stack, tunneling, and NAT64 as transition technologies.
*   [ ] Read the **IPv6** chapter in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's IPv6 videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
