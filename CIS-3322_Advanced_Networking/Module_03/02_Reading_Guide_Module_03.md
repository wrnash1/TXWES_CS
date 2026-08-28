# Reading Guide: Module 03 - IPv6 Addressing and Configuration

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3322 &BULL; ADVANCED NETWORKING & INFRASTRUCTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

IPv6 is a mandatory topic on the CCNA 200-301 exam. This guide covers IPv6 address format, all address types tested on the exam, SLAAC, EUI-64 conversion, and the complete set of Cisco IOS configuration and verification commands. Work through the EUI-64 conversion examples by hand before the quiz.

---

## 1. High-Yield Glossary

- **IPv6:** Internet Protocol version 6. Uses 128-bit addresses written as eight groups of four hexadecimal digits. Provides approximately 3.4 x 10^38 unique addresses.

- **Link-local address:** An IPv6 address in the FE80::/10 range that is automatically generated on every IPv6-enabled interface. Valid only on the local link segment — never routed. Used for Neighbor Discovery and Router Advertisement messages.

- **Global unicast address:** A publicly routable IPv6 address in the 2000::/3 range. Equivalent to a public IPv4 address. Assigned statically, via SLAAC, or via DHCPv6.

- **Unique local address:** An IPv6 address in the FC00::/7 range (FD00::/8 in practice) that is private and not routed on the public internet. Equivalent to RFC 1918 private IPv4 addresses.

- **Multicast address:** An IPv6 address in the FF00::/8 range used to send traffic to a group of devices simultaneously. IPv6 replaces broadcast with multicast.

- **SLAAC (Stateless Address Autoconfiguration):** A mechanism allowing IPv6 hosts to self-configure global unicast addresses using network prefix information received in Router Advertisement messages, without requiring a DHCPv6 server.

- **Router Advertisement (RA):** An ICMPv6 message sent by routers to advertise the IPv6 prefix, default gateway, and autoconfiguration flags. Hosts use RA information to perform SLAAC.

- **Router Solicitation (RS):** An ICMPv6 message sent by a host to request an immediate Router Advertisement rather than waiting for the periodic RA interval.

- **EUI-64:** A method to derive a 64-bit interface identifier from a 48-bit MAC address. Steps: split the MAC at byte 3, insert FF:FE in the middle, invert bit 7 of the first byte.

- **Duplicate Address Detection (DAD):** An NDP process where a host sends a Neighbor Solicitation to its own tentative address before using it. If no reply is received, the address is confirmed unique.

- **NDP (Neighbor Discovery Protocol):** The IPv6 replacement for ARP. Uses ICMPv6 messages (Neighbor Solicitation and Neighbor Advertisement) to resolve IPv6 addresses to MAC addresses. Also handles Router Discovery and DAD.

- **DHCPv6:** Stateful IPv6 address assignment, similar to DHCPv4. Used when SLAAC is insufficient (for example, when DNS server addresses must be distributed to hosts).

- **ipv6 unicast-routing:** The Cisco IOS global configuration command that enables a router to forward IPv6 packets. Without it, the router silently drops all IPv6 traffic destined for other interfaces.

- **Interface identifier:** The 64-bit right portion of a /64 IPv6 address that identifies a specific interface within the subnet. Can be derived from EUI-64, randomly generated (privacy extensions), or manually configured.

- **Solicited-node multicast address:** An automatically derived multicast address used in NDP address resolution. Formed by appending the last 24 bits of an IPv6 address to the prefix FF02::1:FF00:0/104.

---

## 2. IPv6 Address Type Reference Table

| Type | Prefix | Scope | Equivalent | Notes |
|---|---|---|---|---|
| Global Unicast | 2000::/3 | Public internet | Public IPv4 | Routable everywhere; starts with 2 or 3 |
| Link-Local | FE80::/10 | Single link | N/A | Auto-generated; never routed; always present |
| Unique Local | FC00::/7 (FD::/8 common) | Organization-wide | RFC 1918 private | Not routed publicly |
| Multicast | FF00::/8 | Various | IPv4 multicast | Replaces IPv4 broadcast |
| Loopback | ::1/128 | Local device | 127.0.0.1 | Used for local testing |
| Unspecified | ::/128 | N/A | 0.0.0.0 | Source address before assignment |

---

## 3. Key Multicast Addresses

| Address | Name | Purpose |
|---|---|---|
| FF02::1 | All-nodes multicast | Reaches all IPv6-enabled nodes on the link |
| FF02::2 | All-routers multicast | Used by Router Solicitation messages |
| FF02::5 | OSPFv3 all routers | Used by OSPFv3 hello messages |
| FF02::6 | OSPFv3 DR/BDR | Used by OSPFv3 DR/BDR communication |
| FF02::9 | RIPng all routers | Used by RIPng routing updates |
| FF02::1:FF/104 | Solicited-node | Used by NDP for address resolution |

---

## 4. EUI-64 Conversion Reference

Converting a MAC address to an EUI-64 interface identifier:

Step 1: Write the MAC address in colon notation.
Example MAC: `00:1A:2B:3C:4D:5E`

Step 2: Split the MAC in half at byte 3 and insert FFFE.
Result: `00:1A:2B:FF:FE:3C:4D:5E`

Step 3: Convert the first byte to binary and invert bit 7 (second bit from left, 0-indexed).
First byte `00` = `0000 0000`. Bit 7 inverted: `0000 0010` = `02`.
Result: `02:1A:2B:FF:FE:3C:4D:5E`

Step 4: Write as IPv6 groups of 4 hex digits.
Interface ID: `021A:2BFF:FE3C:4D5E`

Full address with prefix 2001:DB8:1::/64:
`2001:DB8:1::021A:2BFF:FE3C:4D5E`

Bit 7 inversion quick reference:

| First Byte (hex) | Binary | Bit 7 Inverted | Result (hex) |
|---|---|---|---|
| 00 | 0000 0000 | 0000 0010 | 02 |
| 02 | 0000 0010 | 0000 0000 | 00 |
| 04 | 0000 0100 | 0000 0110 | 06 |
| 0C | 0000 1100 | 0000 1110 | 0E |

---

## 5. Cisco IOS IPv6 Configuration Command Reference

| Task | Command | Mode |
|---|---|---|
| Enable IPv6 routing | `ipv6 unicast-routing` | Global config |
| Assign static IPv6 address | `ipv6 address 2001:DB8::1/64` | Interface config |
| Assign IPv6 with EUI-64 | `ipv6 address 2001:DB8::/64 eui-64` | Interface config |
| Enable SLAAC on interface | `ipv6 address autoconfig` | Interface config |
| Configure IPv6 static route | `ipv6 route 2001:DB8:1::/64 2001:DB8:2::2` | Global config |
| Configure IPv6 default route | `ipv6 route ::/0 Gi0/0 FE80::1` | Global config |
| Show IPv6 interface summary | `show ipv6 interface brief` | Privileged EXEC |
| Show detailed IPv6 interface | `show ipv6 interface Gi0/0` | Privileged EXEC |
| Show IPv6 routing table | `show ipv6 route` | Privileged EXEC |
| Show IPv6 neighbor cache | `show ipv6 neighbors` | Privileged EXEC |
| Ping over IPv6 | `ping ipv6 2001:DB8::1` | Privileged EXEC |

---

## 6. IPv6 Static Route Types

| Route Type | Command Syntax | When to Use |
|---|---|---|
| Directly connected (exit interface only) | `ipv6 route prefix/len Gi0/0` | Point-to-point links where exit interface uniquely identifies next hop |
| Recursive (global unicast next-hop) | `ipv6 route prefix/len 2001:DB8::2` | When next-hop is a routable global unicast address |
| Fully specified (link-local + interface) | `ipv6 route prefix/len Gi0/0 FE80::2` | Required when next-hop is a link-local address; must specify exit interface |
| Default route | `ipv6 route ::/0 Gi0/0 FE80::1` | Upstream default gateway |

---

## 7. IPv6 vs IPv4 Comparison Reference

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address length | 32 bits | 128 bits |
| Address notation | Dotted decimal | Colon-hexadecimal |
| Subnet mask | Dotted decimal or prefix | Prefix only |
| ARP | Yes (broadcast) | No — replaced by NDP (multicast) |
| Broadcast | Yes | No — replaced by multicast |
| Address autoconfiguration | DHCP only | SLAAC or DHCPv6 |
| Fragmentation | Routers and hosts | Hosts only (routers do not fragment) |
| Header checksum | Yes | No (removed for efficiency) |
| Flow label | No | Yes (20-bit field in header) |
| Private addresses | RFC 1918 | Unique local (FC00::/7) |

---

## 8. CCNA Exam Tips

1. `ipv6 unicast-routing` is required on Cisco routers to forward IPv6 traffic. Forgetting this command is the most common IPv6 lab error. Without it, the router acts as an IPv6 host, not a router.

2. Know the three main address type prefixes: FE80::/10 (link-local), 2000::/3 (global unicast), FC00::/7 (unique local). The exam gives you an address and asks its type.

3. EUI-64 exam questions give you a MAC and ask for the interface identifier. Practice: split at byte 3, insert FFFE, invert bit 7. The most missed step is bit 7 inversion.

4. When configuring an IPv6 static route with a link-local next-hop, you must include the exit interface. `ipv6 route ::/0 FE80::1` will be rejected — you need `ipv6 route ::/0 Gi0/0 FE80::1`.

5. IPv6 does not have broadcast. It uses multicast instead. Solicited-node multicast replaces ARP. All-nodes multicast (FF02::1) replaces the IPv4 limited broadcast (255.255.255.255).

6. The 2001:DB8::/32 prefix is reserved for documentation. You will see it in every CCNA lab and study guide. It is never routed on the public internet.

7. `show ipv6 neighbors` is the IPv6 equivalent of `show ip arp`. The exam sometimes asks for the command to view the IPv6 address-to-MAC mapping table.

8. IPv6 headers are simpler than IPv4 headers. IPv6 removed the checksum field (offloaded to transport layer) and fragmentation at routers (only hosts fragment in IPv6). The fixed 40-byte header improves router forwarding performance.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Write out the full expanded form of `2001:DB8::1` from memory
- [ ] Identify the type of each address: FE80::1, 2001:DB8:1::1, FD00::1, FF02::2, ::1
- [ ] Convert MAC address `A4:BB:CC:DD:EE:FF` to its EUI-64 interface ID by hand
- [ ] Write the three commands to enable IPv6 routing, assign an address, and bring up the interface
- [ ] Explain SLAAC in four sentences: what it does, what triggers it, what the host combines, and what DAD confirms
- [ ] Write a fully specified static route for 2001:DB8:2::/64 via interface Gi0/1 and link-local FE80::2
- [ ] Review the IPv6 vs IPv4 comparison table and note three key differences you could be tested on
- [ ] Complete the Module 03 Packet Tracer lab activity
- [ ] Post your Module 03 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 10. Supplemental Resources

The following open educational resources extend IPv6 addressing and configuration concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Introduction to Networks, Chapter 13 (IPv6 Addressing)** (skillsforall.com): This free chapter provides interactive IPv6 address type identification exercises, SLAAC simulation activities, and IPv6 static routing labs in Packet Tracer.

2. **Jeremy's IT Lab — IPv6 (Days 31–32)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): These two video lessons cover IPv6 address types, EUI-64 derivation, SLAAC, DHCPv6, and static routing with worked configuration examples.

3. **Cisco Learning Network — IPv6 Addressing Deep Dive** (learningnetwork.cisco.com): The Cisco Learning Network community includes comprehensive IPv6 study threads with practice problems on address compression, prefix identification, and NDP operation at CCNA exam difficulty.

4. **ARIN IPv6 Wiki — Free Educational IPv6 Resources** (arin.net/resources/guide/ipv6): The American Registry for Internet Numbers (ARIN) provides free IPv6 tutorials, address type reference charts, and transition mechanism documentation aligned with current CCNA exam objectives.

5. **Packet Tracer IPv6 Configuration Lab Tutorials** (skillsforall.com/course/getting-started-cisco-packet-tracer): The Cisco Networking Academy offers guided Packet Tracer tutorials specifically for IPv6 routing configuration, including SLAAC verification, static route troubleshooting, and neighbor discovery inspection — all directly applicable to this lab activity.
