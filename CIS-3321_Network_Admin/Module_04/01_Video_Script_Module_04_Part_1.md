# Video Script: Module 04 – IPv6 Addressing and Transition Technologies
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 12–14 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 04: IPv6 Addressing and Transition Technologies | Texas Wesleyan University"]

---

### Section 1: Introduction — Why IPv6?

[00:00 – 01:30]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 04. I'm Professor Nash. IPv4 has served the internet since the early 1980s, and it has done an incredible job. But there is one fundamental problem: 32-bit IPv4 addresses provide approximately 4.3 billion unique addresses. With smartphones, smart TVs, IoT devices, wearables, and billions of new internet users worldwide, we ran out of available IPv4 addresses. The Internet Assigned Numbers Authority exhausted its pool of unallocated IPv4 blocks in 2011.

IPv6 was designed to replace IPv4. With 128-bit addresses, IPv6 provides approximately 340 undecillion unique addresses — that is 3.4 times 10 to the power of 38. Every grain of sand on every beach on Earth could have an IPv6 address with trillions to spare.

In this module, Part 1 covers IPv6 address structure, notation rules, and the different IPv6 address types. Part 2 covers autoconfiguration mechanisms (SLAAC) and the transition technologies that allow IPv4 and IPv6 to coexist during the migration period.

---

### Section 2: IPv6 Address Structure and Notation

[01:30 – 05:00]

[SHOW DIAGRAM: A full IPv6 address displayed in groups. Address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334. Eight groups of four hexadecimal digits, separated by colons. A label shows "128 bits total, 8 groups of 16 bits each."]

[Alt-text: An IPv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 displayed in large text. The eight groups of four hexadecimal digits are separated by colons. A bracket below shows the total is 128 bits, with each group representing 16 bits.]

An IPv6 address is 128 bits long, written as eight groups of four hexadecimal digits separated by colons. Hexadecimal uses the digits 0 through 9 and letters A through F to represent values 0 through 15.

128 bits divided into 8 groups of 16 bits each. Each group of 16 bits is represented by four hex digits.

To make addresses shorter and more readable, IPv6 defines two abbreviation rules.

**Rule 1 — Omit leading zeros.** Within any 16-bit group, leading zeros may be dropped. The group "0db8" becomes "db8." The group "0000" becomes "0." Note that trailing zeros cannot be dropped — only leading ones.

**Rule 2 — Replace consecutive all-zero groups with double colon.** A contiguous sequence of one or more all-zero groups may be replaced with "::" (double colon). This replacement can be used only once in any address to avoid ambiguity.

Let's apply both rules to our example address.

Full address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Step 1 — Remove leading zeros: 2001:db8:85a3:0:0:8a2e:370:7334

Step 2 — Replace consecutive zeros with "::": 2001:db8:85a3::8a2e:370:7334

The two consecutive all-zero groups become "::". The abbreviated address is much shorter and easier to read.

> **Network+ Exam Tip:** The exam gives you an abbreviated IPv6 address and asks which full address it represents, or vice versa. Practice expanding addresses by reversing the two rules. Remember that "::" can appear only once per address. If you see "::" in an address, count how many groups are present, then fill in the missing groups with zeros to reach eight total groups.

---

### Section 3: IPv6 Address Types

[05:00 – 09:00]

[SHOW DIAGRAM: A table with three columns — Address Type, Prefix, and Description. Six rows: Global Unicast (2000::/3, starts with 2 or 3), Link-Local (fe80::/10), Loopback (::1/128), Unique Local (fc00::/7, typically fd00::/8), Multicast (ff00::/8), Anycast (from unicast space, assigned to multiple interfaces).]

[Alt-text: A six-row table with columns Address Type, Prefix, and Description. Row 1: Global Unicast, prefix 2000::/3 (addresses starting with 2 or 3), described as globally routable IPv6 addresses equivalent to public IPv4. Row 2: Link-Local, prefix fe80::/10, described as auto-generated on every interface, not routable beyond the local segment. Row 3: Loopback, prefix ::1/128, described as equivalent to 127.0.0.1, tests local stack. Row 4: Unique Local, prefix fc00::/7 (fd00::/8 in practice), described as equivalent to RFC 1918, used for private internal networks. Row 5: Multicast, prefix ff00::/8, described as replaces broadcast, delivers packets to group members. Row 6: Anycast, shared from unicast space, described as assigned to multiple interfaces, packets reach the nearest one.]

IPv6 defines several distinct address types. Knowing the prefix for each type is essential for the exam.

**Global Unicast** — These are IPv6's public addresses. They begin with the prefix 2000::/3, meaning the first three bits are "001." In practice, all current global unicast addresses start with 2 or 3 in their first hex character. These are globally unique and routable on the internet, equivalent to public IPv4 addresses.

**Link-Local** — Every IPv6-enabled interface automatically generates a link-local address with the prefix fe80::/10. Link-local addresses are used for communication on the local network segment only — they are not routed beyond that segment. Think of them as similar to APIPA in IPv4, but unlike APIPA, link-local addresses in IPv6 are always present and functional even when global unicast addresses are configured. Link-local addresses are required for IPv6 to function.

**Loopback** — The IPv6 loopback address is ::1/128. This is the IPv6 equivalent of 127.0.0.1. Pinging ::1 tests the local IPv6 stack.

**Unique Local Address (ULA)** — The prefix is fc00::/7, implemented in practice as fd00::/8. ULAs are IPv6's equivalent of RFC 1918 private addresses. They are not routable on the public internet and are used for internal organizational networks.

**Multicast** — The prefix is ff00::/8. IPv6 has no broadcast. Instead, it uses multicast for functions that IPv4 handled via broadcast. All-nodes multicast is ff02::1 (equivalent to 255.255.255.255 broadcast). All-routers multicast is ff02::2.

**Anycast** — An anycast address is assigned to multiple interfaces. Packets sent to an anycast address are delivered to the nearest interface holding that address (nearest in terms of routing metric). Used for load balancing and redundancy in services like DNS root servers.

---

### Section 4: NDP — Neighbor Discovery Protocol

[09:00 – 11:00]

[SHOW DIAGRAM: A comparison table showing IPv4 ARP versus IPv6 NDP. Left column: ARP — resolves IP to MAC on local segment, uses broadcast. Right column: NDP (ICMPv6) — resolves IPv6 address to MAC, uses multicast, also handles router discovery and Duplicate Address Detection.]

[Alt-text: A two-column comparison table. Left column header is ARP (IPv4). Right column header is NDP (IPv6). Row 1: ARP resolves IPv4 address to MAC address versus NDP resolves IPv6 address to link-layer address. Row 2: ARP uses broadcast versus NDP uses multicast (Neighbor Solicitation / Neighbor Advertisement). Row 3: ARP has no equivalent versus NDP includes Router Discovery and Duplicate Address Detection (DAD).]

IPv6 replaces ARP with NDP — the Neighbor Discovery Protocol. NDP uses ICMPv6 messages to handle the functions that ARP and several other IPv4 protocols performed.

NDP performs three key functions.

Address resolution — NDP uses Neighbor Solicitation and Neighbor Advertisement messages (ICMPv6 Type 135 and 136) to resolve an IPv6 address to a MAC address on the local segment. This replaces ARP.

Router discovery — NDP uses Router Solicitation (ICMPv6 Type 133) and Router Advertisement (ICMPv6 Type 134) messages. Routers periodically send Router Advertisements announcing the network prefix. Hosts use these to configure their own addresses.

Duplicate Address Detection (DAD) — Before a host uses an IPv6 address, it sends a Neighbor Solicitation to the multicast address for that IP. If another device responds, the address is already in use (duplicate). The host must not use that address.

> **Network+ Exam Tip:** The exam distinguishes ARP from NDP. In an IPv6 scenario, any question about resolving an IP address to a MAC address refers to NDP, not ARP. ARP does not exist in IPv6. Remember: NDP uses ICMPv6 messages, not separate broadcast frames.

---

### Section 5: Part 1 Summary

[11:00 – 13:00]

[SHOW SLIDE: Summary bullet list]

In Part 1, we covered the IPv6 address structure — 128 bits in eight groups of four hex digits. We practiced the two abbreviation rules — drop leading zeros, use "::" once for consecutive all-zero groups. We examined the six IPv6 address types — Global Unicast, Link-Local, Loopback, Unique Local, Multicast, and Anycast — and their prefixes. We compared NDP to ARP and explained the three NDP functions.

In Part 2, we cover SLAAC address autoconfiguration, DHCPv6, EUI-64 host ID generation, and the transition technologies — dual stack, tunneling, and NAT64.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
