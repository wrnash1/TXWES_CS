# Video Script: Module 16 — Network+ N10-008 Exam Preparation (Part 1 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome to Module 16 — our final module and your launch preparation for the CompTIA Network+ N10-008 exam. I am Professor Nash, and this is where we bring everything together.

Over the past fifteen modules you have built a comprehensive foundation in network administration. This module does three things: first, we systematically review all five exam domains with emphasis on the highest-weight topics; second, we discuss exam strategy — how to approach question types, manage time, and avoid common traps; third, you will complete 20 practice questions in the quiz to simulate exam conditions.

Part 1 covers Domain 1 (Networking Concepts) and Domain 2 (Infrastructure) — the two largest domains by exam weight. Part 2 covers Domains 3, 4, and 5, exam strategy, and final preparation guidance.

Let us begin.

---

## Section 1: Exam Overview

### What the N10-008 Exam Looks Like

- Maximum of 90 questions (multiple choice and performance-based)
- 90 minutes to complete
- Passing score: 720 out of 900
- Available in English, Japanese, and Portuguese
- Can be taken at a Pearson VUE testing center or via online proctored testing

### Five Domains and Their Weights

| Domain | Title | Exam Weight |
|---|---|---|
| 1 | Networking Concepts | 23% |
| 2 | Infrastructure | 18% |
| 3 | Network Operations | 17% |
| 4 | Network Security | 20% |
| 5 | Network Troubleshooting | 22% |

Note that Domain 5 (Troubleshooting) is slightly larger than Domain 1. Do not overlook it.

### Performance-Based Questions

Network+ includes performance-based questions (PBQs) that ask you to perform a task rather than select from four options. Common PBQ types:

- Drag-and-drop topology building
- Matching protocols to port numbers
- Identifying the correct OSI layer for a given function
- Selecting the correct network device for a scenario
- Completing a subnetting worksheet

PBQs appear at the beginning of the exam and typically take more time. Many candidates skip them initially and return after completing the multiple-choice questions.

---

## Section 2: Domain 1 Review — Networking Concepts (23%)

Domain 1 is the conceptual foundation. If you understand these topics deeply, they also support your success in every other domain.

### OSI and TCP/IP Models

The OSI model has seven layers; the TCP/IP model has four. You must map protocols to their correct layers.

OSI to protocol mapping for the exam:

- Layer 1 (Physical): Ethernet physical, DSL, cable, fiber — the medium itself
- Layer 2 (Data Link): Ethernet (802.3), Wi-Fi (802.11), ARP, STP, VLANs (802.1Q)
- Layer 3 (Network): IP (v4 and v6), ICMP, OSPF, EIGRP, BGP
- Layer 4 (Transport): TCP, UDP
- Layer 5 (Session): NetBIOS, RPC — rarely tested directly
- Layer 6 (Presentation): SSL/TLS, JPEG, MPEG — data formatting and encryption negotiation
- Layer 7 (Application): HTTP, HTTPS, FTP, SFTP, SSH, DNS, DHCP, SMTP, SNMP, NTP, SIP, H.323, RDP

### IPv4 Addressing

Subnetting is tested on virtually every Network+ exam. You must be able to:

- Determine the network address, broadcast address, and usable host range for any subnet
- Calculate the number of hosts per subnet (2^n - 2 where n = host bits)
- Identify the correct subnet mask for a given number of required hosts or subnets
- Identify CIDR notation (/24, /25, /26, /27, /28, /29, /30)

Key CIDR reference:

- /24 = 255.255.255.0 → 254 hosts
- /25 = 255.255.255.128 → 126 hosts
- /26 = 255.255.255.192 → 62 hosts
- /27 = 255.255.255.224 → 30 hosts
- /28 = 255.255.255.240 → 14 hosts
- /29 = 255.255.255.248 → 6 hosts
- /30 = 255.255.255.252 → 2 hosts (point-to-point links)

Private address ranges (RFC 1918): 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

APIPA: 169.254.0.0/16 — assigned when DHCP fails

Loopback: 127.0.0.0/8 (127.0.0.1 is the standard loopback address)

### IPv6

IPv6 addresses are 128 bits, written as eight groups of four hexadecimal digits separated by colons.

Key IPv6 address types:

- **Global unicast**: 2000::/3 — publicly routable, equivalent to public IPv4
- **Link-local**: fe80::/10 — non-routable, used for communication within a single link (auto-assigned)
- **Loopback**: ::1/128
- **Unspecified**: ::/128 — source address in DAD (Duplicate Address Detection)
- **Multicast**: ff00::/8 — replaces broadcast in IPv6

IPv6 abbreviation rules:

- Leading zeros in a group can be omitted: 0001 → 1
- One consecutive group of all-zero groups can be replaced with :: (only once per address)

DHCPv6 vs. SLAAC: IPv6 hosts can get addresses via DHCPv6 (stateful, like DHCPv4) or SLAAC (Stateless Address Autoconfiguration — derives address from network prefix + EUI-64 or random interface ID).

### Port Numbers

The exam requires memorization of well-known port numbers:

| Port | Protocol | Service |
|---|---|---|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH, SFTP, SCP |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (server/client) |
| 69 | UDP | TFTP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 119 | TCP | NNTP |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 161/162 | UDP | SNMP |
| 389 | TCP/UDP | LDAP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 465/587 | TCP | SMTPS / SMTP Submission |
| 514 | UDP | Syslog |
| 636 | TCP | LDAPS |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 1433 | TCP | MS SQL Server |
| 1521 | TCP | Oracle Database |
| 3306 | TCP | MySQL |
| 3389 | TCP | RDP |
| 5060 | TCP/UDP | SIP |
| 5061 | TCP | SIP over TLS |

### Routing Concepts

Routing protocol classifications:

- **Static routing**: Manually configured routes. No overhead, no automatic failover.
- **Dynamic routing**: Protocols automatically discover routes and adapt to topology changes.
- **Interior Gateway Protocol (IGP)**: Routing within an autonomous system — OSPF, EIGRP, RIP.
- **Exterior Gateway Protocol (EGP)**: Routing between autonomous systems — BGP.
- **Distance vector**: Makes decisions based on hop count and distance — RIP.
- **Link state**: Each router has a complete map of the topology — OSPF, IS-IS.
- **Hybrid**: Combines distance vector and link state — EIGRP.

Administrative distance (lower = preferred):

- Connected: 0
- Static: 1
- EIGRP: 90
- OSPF: 110
- RIP: 120
- External EIGRP: 170

---

## Section 3: Domain 2 Review — Infrastructure (18%)

Domain 2 covers the physical and logical components of network infrastructure.

### Switching

Critical switching concepts:

- **VLAN**: Logical segmentation at Layer 2. Traffic in different VLANs is isolated. Inter-VLAN routing requires a Layer 3 device.
- **802.1Q trunking**: Carries multiple VLANs on a single link using VLAN tags. Native VLAN is untagged.
- **STP (802.1D)**: Prevents Layer 2 loops by blocking redundant paths. Root bridge election based on lowest bridge ID (priority + MAC). Port states: Blocking → Listening → Learning → Forwarding.
- **RSTP (802.1w)**: Rapid STP — faster convergence (sub-second) than original STP.
- **PortFast**: Configures an access port to bypass STP states — for end-device ports only.
- **EtherChannel (LACP)**: Bundles multiple physical links into one logical link. Increases bandwidth and provides redundancy.

### Wireless

Key wireless standards:

| Standard | Band | Max Speed | Notes |
|---|---|---|---|
| 802.11a | 5 GHz | 54 Mbps | Legacy; less interference |
| 802.11b | 2.4 GHz | 11 Mbps | Legacy; widely adopted |
| 802.11g | 2.4 GHz | 54 Mbps | Backward compatible with b |
| 802.11n | 2.4/5 GHz | 600 Mbps | MIMO; dual-band |
| 802.11ac | 5 GHz | 3.5 Gbps | MU-MIMO; beamforming |
| 802.11ax | 2.4/5/6 GHz | 9.6 Gbps | Wi-Fi 6; OFDMA; high density |

Security standards: WEP (broken), WPA (TKIP, flawed), WPA2 (AES/CCMP — enterprise standard), WPA3 (SAE — current best practice).

Wireless frequencies and channels: 2.4 GHz has 11 channels in North America; non-overlapping channels are 1, 6, 11. 5 GHz has many more non-overlapping channels — less interference.

### WAN Technologies

Key exam WAN distinctions:

- **T1**: 1.544 Mbps leased line
- **T3**: 44.736 Mbps leased line
- **MPLS**: Label-switched, any-to-any VPN, traffic engineering — carrier-managed
- **SD-WAN**: Software-defined, multi-transport, application-aware routing
- **Metro Ethernet — E-Line**: Point-to-point Ethernet service
- **Metro Ethernet — E-LAN**: Multipoint-to-multipoint Ethernet service
- **DSL**: Copper local loop — ADSL asymmetric, VDSL higher speed/shorter range
- **Cable (DOCSIS)**: Shared-medium coaxial — DOCSIS 3.1 supports 10 Gbps
- **GEO satellite**: ~35,000 km altitude — 600+ ms latency — not suitable for real-time
- **LEO satellite (Starlink)**: ~550 km altitude — 20–40 ms latency — viable for remote sites

---

## Summary of Part 1

Key review points from Part 1:

- Domain 1 (23%): OSI layers and protocol mapping, IPv4 subnetting, IPv6 address types, port numbers (memorize the table), routing protocols and administrative distance.
- Domain 2 (18%): VLANs, 802.1Q trunking, STP/RSTP, wireless standards (speeds and bands), WAN technologies matched to use cases.

In Part 2, we cover Domains 3 (Operations), 4 (Security), and 5 (Troubleshooting), then discuss exam strategy and final preparation tips.
