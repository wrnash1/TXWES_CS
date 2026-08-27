# Reading Guide: Module 04 – IPv6 Addressing and Transition Technologies
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 04 covers IPv6 — the protocol replacing IPv4 as the foundation of the modern internet. IPv6 appears frequently on the CompTIA Network+ exam, with questions testing address type identification by prefix, abbreviation rules, SLAAC autoconfiguration, EUI-64 interface ID derivation, and transition technology selection. This module requires memorization of specific prefixes, understanding of the EUI-64 calculation process, and the ability to compare IPv6 mechanisms with their IPv4 equivalents.

---

### 1. Core Vocabulary

**IPv6** — A 128-bit network layer addressing protocol designed to replace IPv4. Provides approximately 3.4 × 10^38 unique addresses. Written as eight groups of four hexadecimal digits separated by colons.

**Hexadecimal** — Base-16 numbering using digits 0–9 and letters A–F. Each hex digit represents 4 binary bits.

**Global Unicast Address** — IPv6 public routable address. Prefix: 2000::/3. All addresses starting with hex 2 or 3. Globally unique and routable on the internet.

**Link-Local Address** — Auto-generated on every IPv6-enabled interface. Prefix: fe80::/10. Used only for local segment communication. Not routed beyond the local link.

**Loopback Address** — ::1/128. IPv6 equivalent of 127.0.0.1. Tests local IP stack.

**Unique Local Address (ULA)** — fc00::/7, implemented as fd00::/8. IPv6 equivalent of RFC 1918 private addresses. Not routed on the public internet.

**Multicast Address** — ff00::/8. Delivers packets to all members of a multicast group. Replaces IPv4 broadcast (IPv6 has no broadcast).

**Anycast Address** — An address assigned to multiple interfaces. Packet is delivered to the nearest interface holding that address. Drawn from unicast address space.

**EUI-64** — Process for deriving a 64-bit interface identifier from a 48-bit MAC address. Steps: split MAC in half, insert FF:FE in the middle, flip the seventh (Universal/Local) bit.

**SLAAC (Stateless Address Autoconfiguration)** — IPv6 mechanism allowing hosts to automatically configure a global unicast address using the prefix advertised in Router Advertisement messages plus their EUI-64 interface ID. No DHCP server required.

**Stateful DHCPv6** — DHCPv6 server assigns specific IPv6 addresses to clients and maintains address-assignment records. Triggered by the "M flag" in Router Advertisements.

**Stateless DHCPv6** — Provides configuration options (DNS server, domain name) without assigning addresses — SLAAC handles addressing. Triggered by the "O flag" in Router Advertisements.

**NDP (Neighbor Discovery Protocol)** — ICMPv6-based protocol replacing IPv4 ARP. Functions: address resolution (Neighbor Solicitation/Advertisement), router discovery (Router Solicitation/Advertisement), and Duplicate Address Detection (DAD).

**DAD (Duplicate Address Detection)** — NDP process where a host sends a Neighbor Solicitation before using an address to verify no other host on the segment is already using that address.

**Dual Stack** — Transition technology where a device runs both IPv4 and IPv6 simultaneously. Can communicate natively using either protocol. Preferred transition approach.

**6to4 Tunneling** — Encapsulates IPv6 packets inside IPv4 packets to traverse IPv4-only infrastructure. Uses prefix 2002::/16.

**Teredo** — Tunneling mechanism that carries IPv6 over IPv4 UDP through NAT devices. Uses prefix 2001::/32. A last-resort tunneling option for hosts behind NAT.

**ISATAP** — Intra-Site Automatic Tunnel Addressing Protocol. IPv6-over-IPv4 tunneling for internal organizational networks.

**NAT64** — Translates between IPv6 and IPv4 at a border device, allowing IPv6-only clients to reach IPv4-only servers.

**ICMPv6** — Internet Control Message Protocol for IPv6. Used for NDP, error reporting, and path MTU discovery. Not the same as ICMPv4 despite the similar name.

**Router Advertisement (RA)** — ICMPv6 Type 134 message sent by routers. Contains the network prefix for SLAAC, M and O flags for DHCPv6, and default router information.

**Router Solicitation (RS)** — ICMPv6 Type 133 message sent by a host requesting an RA immediately rather than waiting for the periodic interval.

---

### 2. IPv6 Address Type Reference Table

Memorize the prefix for every row. This table is directly tested on the exam.

| Address Type      | Prefix        | Scope         | IPv4 Equivalent        | Notes                                     |
|-------------------|---------------|---------------|------------------------|-------------------------------------------|
| Global Unicast    | 2000::/3      | Global internet | Public routable IPv4  | Starts with 2 or 3; assigned by ISPs      |
| Link-Local        | fe80::/10     | Local segment | APIPA 169.254.x.x      | Auto-generated; required for IPv6; not routed |
| Loopback          | ::1/128       | Local host    | 127.0.0.1              | Tests local IP stack only                 |
| Unique Local      | fc00::/7 (fd00::/8) | Org-internal | RFC 1918 private     | Not internet-routable                     |
| Multicast         | ff00::/8      | Group-defined | Broadcast (limited equiv) | No broadcast in IPv6; multicast replaces it |
| Anycast           | Unicast space | Nearest interface | No direct equivalent | Same address on multiple interfaces       |

**Key multicast addresses:**

- ff02::1 — all-nodes multicast (all IPv6 hosts on segment)
- ff02::2 — all-routers multicast
- ff02::fb — mDNS (multicast DNS)

---

### 3. IPv6 Abbreviation Rules with Examples

**Rule 1 — Remove leading zeros within each group (not trailing zeros).**

- 0001 becomes 1
- 0db8 becomes db8
- 0000 becomes 0

**Rule 2 — Replace one contiguous sequence of all-zero groups with "::".**

- Can be used only once per address
- Choose the longest run of zeros for maximum compression

**Example 1 — Full to Abbreviated:**

Full: 2001:0db8:0000:0000:0000:0000:0000:0001

After Rule 1: 2001:db8:0:0:0:0:0:1

After Rule 2: 2001:db8::1

**Example 2 — Abbreviated to Full:**

Abbreviated: fe80::1a2b:3c4d

Count present groups: fe80 and 1a2b and 3c4d = 3 groups

Groups needed: 8 total. Missing: 5 groups → fill with zeros.

Full: fe80:0000:0000:0000:0000:0000:1a2b:3c4d

---

### 4. EUI-64 Calculation Process

Given MAC address: 00:1A:2B:3C:4D:5E

**Step 1:** Split the MAC into two 24-bit halves.

First half: 00:1A:2B | Second half: 3C:4D:5E

**Step 2:** Insert FF:FE between the halves.

Result: 00:1A:2B:FF:FE:3C:4D:5E

**Step 3:** Flip the seventh bit (Universal/Local bit) of the first byte.

First byte: 00 = 00000000 in binary. Seventh bit (bit 1 from left, 0-indexed) = 0. Flip to 1.

00000000 → 00000010 = 0x02

**Final EUI-64 interface ID:** 02:1A:2B:FF:FE:3C:4D:5E

Written as IPv6 groups: 021a:2bff:fe3c:4d5e

**Assembled global unicast address with prefix 2001:db8::/64:**

2001:db8::021a:2bff:fe3c:4d5e

---

### 5. SLAAC vs. DHCPv6 Comparison

| Feature                      | SLAAC                          | Stateful DHCPv6             | Stateless DHCPv6           |
|------------------------------|--------------------------------|-----------------------------|----------------------------|
| Address assignment           | Host self-configures using RA prefix + EUI-64 | Server assigns address | SLAAC handles address      |
| Server required              | No (router RA only)            | Yes                         | Yes (for options only)     |
| Address tracking             | No (stateless)                 | Yes (server maintains lease)| No                         |
| DNS server assignment        | Via RDNSS option in RA         | Yes                         | Yes                        |
| RA flag triggers             | No flags (default behavior)    | M flag set                  | O flag set                 |
| Best suited for              | Simple networks, IoT           | Enterprise managed networks | Mixed approach             |

---

### 6. Transition Technology Comparison

| Technology   | How It Works                                           | Best Use Case                                           | Prefix/Identifier       |
|--------------|--------------------------------------------------------|---------------------------------------------------------|-------------------------|
| Dual Stack   | Both IPv4 and IPv6 run natively on same interface      | Gradual migration; supports both protocol versions simultaneously | N/A (native both)    |
| 6to4         | IPv6 packets encapsulated in IPv4; automatic tunnel    | IPv6 islands over IPv4 WAN                              | 2002::/16               |
| Teredo       | IPv6 over IPv4 UDP through NAT                         | Last resort for hosts behind NAT                        | 2001::/32               |
| ISATAP       | IPv4 as virtual link layer for IPv6 within an org      | Internal enterprise IPv6-over-IPv4 tunneling            | Link-local range        |
| NAT64        | Protocol translation IPv6 ↔ IPv4 at border             | IPv6-only networks reaching IPv4-only servers           | 64:ff9b::/96 (typical)  |

---

### 7. NDP vs. ARP Comparison

| Function                    | IPv4 Mechanism     | IPv6 Mechanism (NDP)                          |
|-----------------------------|-------------------|-----------------------------------------------|
| Resolve IP to MAC address   | ARP (broadcast)   | Neighbor Solicitation / Neighbor Advertisement (multicast) |
| Router discovery            | None (manual/DHCP)| Router Solicitation / Router Advertisement    |
| Duplicate address detection | None              | DAD using Neighbor Solicitation               |
| Protocol                    | ARP (own protocol)| ICMPv6 Types 133–136                          |
| Transport                   | Direct Ethernet   | ICMPv6 over IPv6                              |

---

### 8. Certification Exam Tips

**Tip 1:** Identify IPv6 address types by their prefix — this is the most common exam question format. fe80:: is always link-local. ::1 is always loopback. ff prefix is always multicast. 2 or 3 in the first hex character is global unicast.

**Tip 2:** IPv6 has no broadcast. Any exam answer option that includes "IPv6 broadcast" is incorrect. IPv6 uses multicast to replace all-nodes broadcast.

**Tip 3:** NDP replaces ARP for IPv6. All questions about local address resolution in an IPv6 environment refer to NDP (ICMPv6), not ARP.

**Tip 4:** Dual stack is the preferred and "best practice" transition technology unless the scenario specifically constraints you to IPv4-only or IPv6-only devices. The exam asks for the "best" method — almost always dual stack.

**Tip 5:** The EUI-64 FFFE insertion is a reliable fact. If you see FF:FE in the middle of a 64-bit interface identifier, it was derived from a MAC address using EUI-64.

**Tip 6:** The double colon "::" can appear only once per IPv6 address. If you see two "::" in an address, it is invalid.

**Tip 7:** SLAAC is "stateless" because no server tracks assignments. Stateful DHCPv6 (with the M flag) requires a server and keeps assignment records. Know which is which.

**Tip 8:** Link-local addresses (fe80::/10) are required for IPv6 to function and are generated on every interface automatically. They cannot be used for routing beyond the local segment.

---

### 9. Required Reading and Viewing

**Required Reading:** Computer Networking: Principles, Protocols and Practice — read the IPv6 addressing sections. Focus on SLAAC, NDP, and address type prefixes.

**Required Viewing:** Professor Messer's Network+ N10-008 video series — watch the IPv6 addressing and transition technology segments. Available free at professormesser.com.

**Supplemental Reference:** CompTIA official N10-008 exam objectives at comptia.org — review Domain 1.0 for IPv6 objectives.

---

### 10. Study Checklist

- [ ] Memorize the six IPv6 address types and their prefixes from the reference table
- [ ] Practice applying both IPv6 abbreviation rules — full to abbreviated and abbreviated to full
- [ ] Perform the EUI-64 calculation from a given MAC address without notes
- [ ] Explain SLAAC — the steps a host takes to self-configure a global unicast address
- [ ] Compare stateful DHCPv6, stateless DHCPv6, and SLAAC — when each is used
- [ ] Distinguish NDP from ARP — list three functions NDP performs that ARP does not
- [ ] Compare dual stack, tunneling (6to4, Teredo), and NAT64 as transition technologies
- [ ] Watch Professor Messer's IPv6 videos at professormesser.com
- [ ] Read the IPv6 chapter in the OER textbook
- [ ] Complete the Lab 04 activity using ipconfig /all and ping
- [ ] Post your Module 04 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 04 Quiz

---

## 9. Supplemental Resources

The following free resources extend Module 04 content on IPv6 addressing and transition technologies.

**1. Professor Messer — IPv6 Addressing Free Video Lectures**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer covers IPv6 address types, SLAAC, NDP, and transition technologies in dedicated video segments. These are directly aligned with Network+ exam objectives and this module.

**2. RFC 4291 — IPv6 Addressing Architecture**
URL: https://datatracker.ietf.org/doc/html/rfc4291
Relevance: The authoritative IETF standard defining all IPv6 address types, notation rules, and the meaning of each address prefix. Sections 2.1–2.5 cover address types tested on the exam. This is the primary reference for IPv6 address classification.

**3. Cisco — IPv6 Addressing and Basic Connectivity Configuration Guide**
URL: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6_basic/configuration/xe-16/ip6b-xe-16-book/ip6-add-basic-conn.html
Relevance: Cisco's free official documentation covering IPv6 interface configuration, link-local address generation, and SLAAC on IOS devices. Directly applicable to Packet Tracer lab exercises for this module.

**4. ARIN IPv6 Wiki — IPv6 Address Planning**
URL: https://www.arin.net/resources/guide/ipv6/
Relevance: The American Registry for Internet Numbers provides free IPv6 educational resources including address planning guides and transition technology overviews. Useful for understanding real-world IPv6 deployment practices.

**5. Hurricane Electric IPv6 Certification and Training**
URL: https://ipv6.he.net/certification/
Relevance: Hurricane Electric offers free hands-on IPv6 certification tasks that require configuring and testing real IPv6 connectivity. Completing the first few levels of this free program provides practical IPv6 experience beyond what a simulation can offer.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
