# Video Script: Module 04 – IPv6 Addressing and Transition Technologies
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 10–12 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 04 Part 2 — SLAAC, EUI-64, DHCPv6, and IPv4/IPv6 Transition Technologies"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 04. In Part 1 we covered IPv6 address structure, abbreviation rules, address types, and NDP. Now in Part 2 we cover how IPv6 addresses are automatically configured — SLAAC and DHCPv6 — the EUI-64 process, and the three primary transition technologies. These are heavily tested on the Network+ exam.

---

### Section 2: SLAAC — Stateless Address Autoconfiguration

[00:45 – 04:00]

[SHOW DIAGRAM: SLAAC process sequence. Step 1: Router sends a Router Advertisement (RA) containing the network prefix (e.g., 2001:db8::/64). Step 2: Host combines the 64-bit prefix from the RA with its own 64-bit EUI-64 interface identifier derived from its MAC address. Step 3: Host performs Duplicate Address Detection (DAD). Step 4: Host uses the assembled address.]

[Alt-text: A four-step diagram showing the SLAAC process. Step 1 shows a Router icon sending a Router Advertisement arrow to a Host icon, with the label "RA contains prefix 2001:db8::/64." Step 2 shows the Host combining the 64-bit prefix with a 64-bit EUI-64 interface ID generated from its MAC address. Step 3 shows the Host performing Duplicate Address Detection by sending a Neighbor Solicitation to verify the address is not already in use. Step 4 shows the Host configured with the assembled global unicast address.]

SLAAC (Stateless Address Autoconfiguration) is one of the most elegant features of IPv6. It allows a host to automatically configure a globally unique IPv6 address without any DHCP server.

Here is how SLAAC works.

Step 1 — Router Advertisement. A router on the network periodically sends ICMPv6 Router Advertisement (RA) messages. These RAs contain the network's 64-bit prefix (for example, 2001:db8:1234:5678::/64) and indicate that SLAAC is available.

Step 2 — Address Assembly. The host takes the 64-bit network prefix from the RA and appends its own 64-bit interface identifier to form a complete 128-bit IPv6 address. The interface identifier is typically generated using the EUI-64 process from the host's MAC address, or in privacy-enabled systems, a random value.

Step 3 — Duplicate Address Detection. Before using the assembled address, the host sends a Neighbor Solicitation to the solicited-node multicast address for that IP. If another device on the segment is using the same address, it responds. If no response arrives, the address is unique and the host can use it.

Step 4 — Configuration complete. The host now has a valid global unicast IPv6 address, configured entirely without a DHCP server.

SLAAC is called "stateless" because no server tracks which host has which address. The host self-configures based on publicly broadcast information.

One limitation: SLAAC does not provide DNS server configuration by default. To provide DNS server addresses without DHCPv6, routers use the RDNSS (Recursive DNS Server) option in Router Advertisements.

---

### Section 3: EUI-64 Interface Identifier

[04:00 – 06:00]

[SHOW DIAGRAM: EUI-64 calculation steps. Start with MAC address 00:1A:2B:3C:4D:5E. Split into two halves: 00:1A:2B and 3C:4D:5E. Insert FF:FE in the middle: 00:1A:2B:FF:FE:3C:4D:5E. Flip the seventh bit of the first byte: 00 = 00000000, flip bit 7 (Universal/Local), becomes 00000010 = 02. Result: 02:1A:2B:FF:FE:3C:4D:5E. Written as IPv6 interface ID: 021a:2bff:fe3c:4d5e.]

[Alt-text: A step-by-step EUI-64 calculation diagram. Starting MAC address is 00:1A:2B:3C:4D:5E. Step 1 splits the MAC into two three-byte halves: 00:1A:2B and 3C:4D:5E. Step 2 inserts the bytes FF:FE in the middle, producing 00:1A:2B:FF:FE:3C:4D:5E. Step 3 flips the seventh bit (Universal/Local bit) of the first byte from 00000000 to 00000010, changing 00 to 02. The final EUI-64 interface identifier is 021a:2bff:fe3c:4d5e.]

EUI-64 is the process used by SLAAC to derive the 64-bit interface identifier portion of an IPv6 address from a device's 48-bit MAC address.

The three-step process:

Step 1 — Split the MAC address in half. The 48-bit MAC address is split into two 24-bit halves at the midpoint.

Step 2 — Insert FFFE in the middle. The 16-bit value FF:FE is inserted between the two halves. This expands the address from 48 to 64 bits.

Step 3 — Flip the seventh bit. The seventh bit of the first byte (the Universal/Local bit, also called the U/L bit) is inverted. If it was 0 (universally administered), it becomes 1. If it was 1 (locally administered), it becomes 0.

The resulting 64 bits form the interface identifier, which is appended to the 64-bit network prefix to create the complete IPv6 address.

> **Network+ Exam Tip:** The exam may ask what the middle bytes in an EUI-64-derived interface identifier are. The answer is always FFFE. If you see FF:FE in the middle of an IPv6 interface identifier, it was generated using EUI-64 from a MAC address.

---

### Section 4: DHCPv6

[06:00 – 07:30]

[SHOW SLIDE: Two-column comparison: Stateful DHCPv6 versus Stateless DHCPv6]

IPv6 supports two forms of DHCPv6.

Stateful DHCPv6 works similarly to IPv4 DHCP. The DHCPv6 server assigns specific IPv6 addresses to clients and keeps a record of which client holds which address. The router's RA sets the "M flag" (Managed) to tell clients to use stateful DHCPv6 for addressing.

Stateless DHCPv6 does not assign addresses — SLAAC handles address assignment. Instead, stateless DHCPv6 provides additional configuration options such as DNS server addresses. The router's RA sets the "O flag" (Other configuration) to tell clients to use DHCPv6 only for configuration options, not for the address itself.

The combination of SLAAC for addressing plus stateless DHCPv6 for DNS is the most common deployment pattern in modern IPv6 networks.

---

### Section 5: IPv4 to IPv6 Transition Technologies

[07:30 – 10:30]

[SHOW DIAGRAM: Three transition technology diagrams. Left: Dual Stack — one device with both IPv4 and IPv6 addresses simultaneously. Center: Tunneling — IPv6 packet encapsulated inside IPv4 header to cross IPv4-only infrastructure. Right: NAT64 — IPv6-only client communicating with IPv4-only server through a translation border device.]

[Alt-text: Three diagrams illustrating IPv6 transition technologies. The left diagram shows a single network device with two stacked address bars, one labeled IPv4 and one labeled IPv6, with the caption "Dual Stack — both protocols active simultaneously." The center diagram shows an IPv6 packet with an IPv4 outer header wrapped around it, crossing a gray IPv4-only cloud network, with the caption "Tunneling — IPv6 wrapped inside IPv4." The right diagram shows an IPv6-only client on the left communicating through a NAT64 border device to an IPv4-only server on the right, with the caption "NAT64 — protocol translation at the border."]

The transition from IPv4 to IPv6 is a multi-decade process. Three primary technologies enable coexistence.

**Dual Stack** — The device runs both IPv4 and IPv6 simultaneously on the same interface. It has both an IPv4 address and an IPv6 address. When communicating with an IPv4-only host, it uses IPv4. When communicating with an IPv6-capable host, it prefers IPv6. Dual stack is the cleanest and most preferred transition strategy. The exam will almost always choose dual stack as the "best" answer when the question asks about supporting both protocol versions simultaneously.

**Tunneling** — When two IPv6 networks are separated by an IPv4-only infrastructure (such as a legacy WAN), tunneling encapsulates IPv6 packets inside IPv4 headers. The IPv6 packet becomes the payload of an IPv4 packet. Common tunneling mechanisms include 6to4 (prefix 2002::/16), Teredo (prefix 2001::/32, designed to traverse NAT), and ISATAP (Intra-Site Automatic Tunnel Addressing Protocol, for internal use). Tunneling is a workaround for legacy infrastructure, not a permanent solution.

**NAT64** — Network Address Translation between IPv6 and IPv4. Used when IPv6-only clients need to communicate with IPv4-only servers, or vice versa. A border device translates between the two address families. NAT64 is used at the edge of IPv6-only networks that must reach legacy IPv4-only resources.

---

### Section 6: Lab Preview and Module Closing

[SHOW SLIDE: Lab preview — ipconfig /all output showing link-local address]

In this week's lab, you will use ipconfig /all on Windows or ip addr on Linux to observe the automatically generated link-local IPv6 address on your machine. You will identify the address type from its prefix, ping the loopback address (::1), and investigate the EUI-64 derivation from your NIC's MAC address.

Before heading to the lab, memorize these IPv6 address type prefixes: fe80::/10 for link-local, ::1/128 for loopback, ff00::/8 for multicast, 2000::/3 for global unicast (starts with 2 or 3), and fd00::/8 for unique local. These five prefixes cover all questions the Network+ exam will ask about IPv6 address type identification.

Module 04 key takeaways: IPv6 is 128 bits in eight groups of four hex digits. Two abbreviation rules simplify notation. Six address types have specific prefixes you must memorize. NDP replaces ARP using ICMPv6. SLAAC auto-configures global addresses without a DHCP server. EUI-64 derives the interface ID from the MAC address. Dual stack is the preferred transition technology.

In Module 05, we move to physical network infrastructure — cables, switches, and routers.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
