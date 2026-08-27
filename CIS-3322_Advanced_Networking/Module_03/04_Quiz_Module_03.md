# Quiz: Module 03 - IPv6 Addressing and Configuration

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

What Cisco IOS global configuration command enables a router to forward IPv6 traffic between interfaces?

- A) `ip routing`
- B) `ipv6 address autoconfig`
- C) `ipv6 unicast-routing`
- D) `ipv6 routing enable`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `ip routing` enables IPv4 routing on multilayer switches. It has no effect on IPv6 forwarding.
- B is incorrect: `ipv6 address autoconfig` is an interface command that enables SLAAC on a Cisco router interface. It does not enable packet forwarding.
- C is correct: `ipv6 unicast-routing` is the global configuration command required to enable IPv6 packet forwarding on Cisco routers. Without it, the router behaves as an IPv6 host.
- D is incorrect: `ipv6 routing enable` is not valid Cisco IOS syntax.

---

## Question 2

Which of the following most accurately describes the EUI-64 method of generating an IPv6 interface identifier?

- A) A process that combines the 48-bit MAC address with hex FFFE inserted in the middle and the seventh bit inverted to produce a 64-bit interface ID.
- B) A stateless mechanism where a host listens for Router Advertisement messages and combines the prefix with a randomly generated 64-bit suffix.
- C) A 6-byte hardware address assigned to every NIC at the factory, used by switches to build MAC address tables.
- D) A Cisco proprietary algorithm that generates a 64-bit host identifier by hashing the device hostname and serial number.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: EUI-64 is an IEEE standard method. Steps: split the 48-bit MAC at byte 3, insert FFFE, invert bit 7 (universal/local bit) of the first byte.
- B is incorrect: This describes SLAAC with privacy extensions (random interface ID), not the EUI-64 derivation process.
- C is incorrect: This describes a MAC address itself, not the EUI-64 conversion algorithm.
- D is incorrect: EUI-64 is an IEEE standard, not Cisco proprietary. The interface ID is derived from the MAC address, not hostname or serial number.

---

## Question 3

A host has the IPv6 address 2001:DB8:ACAD:1::200:11FF:FE33:4455/64. What is the MAC address that was used to generate this address via EUI-64?

- A) 00:00:11:33:44:55
- B) 02:00:11:FF:FE:33
- C) 00:00:11:33:44:55 with bit 7 inverted
- D) 02:00:11:33:44:55 reconstructed as 00:00:11:33:44:55

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: This does not account for bit 7 re-inversion to reconstruct the original MAC from the EUI-64.
- B is incorrect: This is only half the interface identifier, not the reconstructed MAC address.
- C is partially correct in concept but D provides the full correct answer with explicit reconstruction.
- D is correct: The interface ID is 0200:11FF:FE33:4455. Remove FFFE: 0200:11 + 33:4455. Re-invert bit 7 of 02 (0000 0010 → 0000 0000 = 00). Reconstructed MAC: 00:00:11:33:44:55.

---

## Question 4

Which IPv6 address type is automatically generated on every IPv6-enabled interface and is never routed beyond the local link?

- A) Global unicast address (2000::/3)
- B) Unique local address (FC00::/7)
- C) Link-local address (FE80::/10)
- D) Solicited-node multicast address (FF02::1:FF/104)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Global unicast addresses are publicly routable and must be manually configured or assigned via SLAAC or DHCPv6.
- B is incorrect: Unique local addresses are the IPv6 equivalent of private addresses. They are not automatically generated.
- C is correct: Link-local addresses in the FE80::/10 range are automatically generated on every IPv6-enabled interface. They are valid only on the local link and are never forwarded by routers.
- D is incorrect: Solicited-node multicast addresses are derived automatically but serve a different purpose (NDP address resolution). They are not a general-purpose communication address.

---

## Question 5

A network engineer wants to configure an IPv6 static default route on R1. The next-hop is the link-local address FE80::2 reachable through Gi0/0. Which command is correct?

- A) `ipv6 route ::/0 FE80::2`
- B) `ipv6 route ::/0 GigabitEthernet0/0 FE80::2`
- C) `ipv6 route 0.0.0.0/0 GigabitEthernet0/0 FE80::2`
- D) `ipv6 default-route GigabitEthernet0/0 FE80::2`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A link-local next-hop address requires the exit interface to be specified. Without the exit interface, IOS cannot determine which segment to forward the packet to.
- B is correct: When a link-local address is the next-hop, the fully specified syntax `ipv6 route prefix/len exit-interface link-local-address` is required.
- C is incorrect: `0.0.0.0/0` is IPv4 notation. IPv6 default routes use `::/0`.
- D is incorrect: `ipv6 default-route` is not valid Cisco IOS syntax.

---

## Question 6

Which Cisco IOS command is the IPv6 equivalent of `show ip arp` and displays the table of IPv6-to-MAC address mappings learned through Neighbor Discovery?

- A) `show ipv6 route`
- B) `show ipv6 interface brief`
- C) `show ipv6 neighbors`
- D) `show ipv6 slaac`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show ipv6 route` displays the IPv6 routing table. It shows network prefixes and next-hops, not address-to-MAC mappings.
- B is incorrect: `show ipv6 interface brief` shows interface status and IP addresses. It does not display the neighbor cache.
- C is correct: `show ipv6 neighbors` displays the IPv6 neighbor cache, which maps IPv6 addresses to MAC addresses. This is the NDP equivalent of the IPv4 ARP table.
- D is incorrect: `show ipv6 slaac` is not a valid Cisco IOS command.

---

## Question 7

What is the compressed notation of the IPv6 address 2001:0DB8:0000:0001:0000:0000:0000:0001?

- A) 2001:DB8::1:0:0:0:1
- B) 2001:DB8:0:1::1
- C) 2001:DB8::1
- D) 2001:0DB8::0001

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: This applies leading-zero removal correctly but does not apply the double-colon to the longest run of zeros (the three consecutive zero groups at positions 5-7).
- B is correct: Remove leading zeros in each group: 2001:DB8:0:1:0:0:0:1. Replace the longest consecutive run of all-zero groups (the three groups from position 5 to 7) with ::. Result: 2001:DB8:0:1::1.
- C is incorrect: 2001:DB8::1 would expand to 2001:DB8:0:0:0:0:0:1, which has seven zero groups between DB8 and 1. That does not match the original address.
- D is incorrect: Leading zeros must be removed from all groups. 0DB8 should be DB8, and 0001 should become 1.

---

## Question 8

What multicast address do IPv6 hosts send a Router Solicitation to when requesting router information?

- A) FF02::1
- B) FF02::2
- C) FF02::5
- D) FE80::1

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: FF02::1 is the all-nodes multicast address. It reaches all IPv6-enabled devices on the link.
- B is correct: FF02::2 is the all-routers multicast address. Hosts send Router Solicitation messages to FF02::2 to request a Router Advertisement.
- C is incorrect: FF02::5 is used by OSPFv3 for router-to-router hello messages.
- D is incorrect: FE80::1 is a link-local unicast address, not a multicast address.

---

## Question 9

An engineer notices that an interface with `ipv6 address 2001:DB8:1::/64 eui-64` shows a different address than expected. What is the most likely explanation?

- A) The EUI-64 command generates a random 64-bit interface identifier each time it is applied
- B) The interface identifier is derived from the interface's MAC address, which differs from the expected MAC
- C) The `eui-64` keyword is only valid on loopback interfaces
- D) Cisco IOS uses the device serial number instead of the MAC address for EUI-64 generation

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: EUI-64 is deterministic — it always generates the same interface ID from the same MAC address. It is not random.
- B is correct: EUI-64 derives the interface identifier from the interface's hardware MAC address. If the interface has a different MAC than expected (for example, a different NIC), the generated address will differ.
- C is incorrect: The `eui-64` keyword is valid on any physical or virtual interface, not only loopbacks.
- D is incorrect: Cisco IOS EUI-64 generation uses the interface's MAC address, not the device serial number.

---

## Question 10

Which IPv6 address range is reserved for documentation purposes and must never be routed on the public internet?

- A) FC00::/7
- B) FE80::/10
- C) 2001:DB8::/32
- D) FF00::/8

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: FC00::/7 is the unique local address range, the IPv6 equivalent of RFC 1918 private addresses. It is not specifically reserved for documentation.
- B is incorrect: FE80::/10 is the link-local address range used for on-link communication. It is not a documentation prefix.
- C is correct: 2001:DB8::/32 is reserved by RFC 3849 specifically for use in documentation, examples, and educational materials. It must not be routed on the public internet.
- D is incorrect: FF00::/8 is the IPv6 multicast address range.

---

## Question 11

A Cisco router interface is assigned the IPv6 address `2001:DB8:A:1::1/64` and a link-local address of `FE80::1`. An IPv6 static route on R2 uses `FE80::1` as the next-hop address without specifying an exit interface. What problem will occur?

- A) The route will not be accepted by IOS because link-local addresses cannot be used as static route next-hops
- B) The route will be accepted but IOS cannot determine which interface to send the packet through; traffic will not be forwarded
- C) IOS will automatically resolve the exit interface using the NDP cache
- D) The route will work correctly because link-local addresses are unique across the entire routing domain

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Cisco IOS does accept link-local addresses as next-hop values for IPv6 static routes. The command syntax is valid, but an exit interface must be specified alongside the link-local next-hop.
- B is correct: Link-local addresses are only significant on a single network segment. Because FE80::1 could theoretically exist on multiple interfaces, IOS cannot determine which exit interface to use without it being explicitly specified. The correct syntax is `ipv6 route prefix/len exit-interface FE80::next-hop`.
- C is incorrect: IOS does not automatically resolve an exit interface from the NDP cache when a link-local next-hop is specified in a static route. The exit interface must be manually specified in the route command.
- D is incorrect: Link-local addresses are NOT unique across a routing domain. They are only valid on the local link. Two different interfaces on the same router (or different routers) can share the same link-local address (e.g., FE80::1) on different segments.

---

## Question 12

Which multicast address does a Cisco router use to send IPv6 OSPF Hello packets to all OSPF routers on a segment?

- A) FF02::1
- B) FF02::2
- C) FF02::5
- D) FF02::6

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: FF02::1 is the all-nodes multicast address. Every IPv6-enabled device listens on FF02::1. OSPF hello packets are not sent to all nodes, only to OSPF routers.
- B is incorrect: FF02::2 is the all-routers multicast address used for router discovery, not for OSPF specifically.
- C is correct: OSPFv3 Hello packets are sent to FF02::5 (all OSPF routers) on broadcast and point-to-point segments. This is the OSPFv3 equivalent of the 224.0.0.5 address used by OSPFv2.
- D is incorrect: FF02::6 is the all-OSPF-DRs (Designated Routers) address, equivalent to 224.0.0.6 in IPv4. It is used for LSU and LSAck packets sent specifically to the DR and BDR, not for Hello packets.

---

## Question 13

An engineer abbreviates the IPv6 address `2001:0DB8:0000:0001:0000:0000:0000:0001`. What is the correct compressed form?

- A) `2001:DB8::1:1`
- B) `2001:DB8:0:1::1`
- C) `2001:DB8::1::1`
- D) `2001:DB8:1::1`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `2001:DB8::1:1` expands to `2001:0DB8:0000:0000:0000:0000:0001:0001`, which replaces groups 3–6 with `::`. The original address has the `0001` in group 4 (position 4) and `0001` in group 8 (position 8), so `::` must preserve the `0:1` structure.
- B is correct: The leading zeros are removed from each group: `2001:DB8:0:1:0:0:0:1`. The longest run of consecutive all-zero groups is groups 5–7 (three consecutive zeros), which are replaced by `::`. Result: `2001:DB8:0:1::1`.
- C is incorrect: Using `::` twice in the same address is not allowed. The double-colon can appear only once in any IPv6 address.
- D is incorrect: `2001:DB8:1::1` drops group 3 entirely. Group 3 is `0000` which becomes `0`, not omitted. The `0:1` in positions 3–4 must be preserved.

---

## Question 14

When a host uses SLAAC (Stateless Address Autoconfiguration) to configure its IPv6 address, which two values does it combine to form its full 128-bit global unicast address?

- A) The prefix from the Router Advertisement and the host's IPv4 address converted to 64 bits
- B) The prefix from the Router Advertisement and the host's EUI-64 interface identifier derived from its MAC address
- C) The prefix assigned by DHCPv6 and a random 64-bit suffix generated by the operating system
- D) The link-local address prefix (FE80::/10) and the host's EUI-64 interface identifier

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: SLAAC does not use IPv4 addresses in address generation. The interface identifier portion of a SLAAC address is derived from the MAC address via EUI-64 (or Privacy Extensions), not from an IPv4 address.
- B is correct: During SLAAC, the host receives the network prefix (typically /64) from the Router Advertisement sent by the default gateway. The host appends its EUI-64 interface identifier (or an RFC 4941 random privacy extension value) to form the full 128-bit address.
- C is incorrect: SLAAC does not use DHCPv6. DHCPv6 is a separate mechanism (stateful or stateless). SLAAC is explicitly "stateless" — no server tracks address assignments.
- D is incorrect: The link-local prefix (FE80::/10) is used for link-local addresses, not global unicast addresses. SLAAC for global unicast uses a globally routable prefix (e.g., 2001:DB8::/32) from the Router Advertisement.

---

## Question 15

Which command verifies that an IPv6 static route to `2001:DB8:2::/64` has been installed in the routing table on a Cisco IOS router?

- A) `show ip route 2001:DB8:2::`
- B) `show ipv6 route`
- C) `show ipv6 interface brief`
- D) `show ip protocols`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `show ip route` displays IPv4 routing table entries only. IPv6 routes do not appear in the IPv4 routing table. The correct command for IPv6 routing verification is `show ipv6 route`.
- B is correct: `show ipv6 route` displays all entries in the IPv6 routing table, including connected routes, static routes (marked "S"), and routes learned via routing protocols. To check a specific prefix, use `show ipv6 route 2001:DB8:2::/64`.
- C is incorrect: `show ipv6 interface brief` displays the IPv6 addresses configured on each interface and their status. It does not show the routing table or static routes.
- D is incorrect: `show ip protocols` displays IPv4 routing protocol information (OSPF, EIGRP timers, networks). It is not applicable to IPv6 routing table verification.

---

## Question 16

A router is configured with `ipv6 address FE80::1 link-local` on interface Gi0/0 and `ipv6 address 2001:DB8:1::1/64` on the same interface. A host on the Gi0/0 segment sends a Neighbor Solicitation message. Which address does the host use as the destination for the Neighbor Solicitation?

- A) FF02::1 (all-nodes multicast)
- B) The solicited-node multicast address corresponding to the target's IPv6 address
- C) FF02::2 (all-routers multicast)
- D) The full global unicast address of the target router

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: FF02::1 (all-nodes) would send the Neighbor Solicitation to every IPv6 node on the segment, creating unnecessary overhead. IPv6 uses solicited-node multicast to limit NS message delivery to only likely matches.
- B is correct: IPv6 Neighbor Discovery Protocol constructs a solicited-node multicast address by appending the last 24 bits of the target's IPv6 address to the prefix FF02::1:FF00:0/104. NS messages are sent to this solicited-node multicast address, which only the target (and any device sharing those last 24 bits) will receive.
- C is incorrect: FF02::2 is the all-routers multicast address used for Router Solicitation messages, not Neighbor Solicitation.
- D is incorrect: The destination of a Neighbor Solicitation (before the target's MAC address is known) cannot be the unicast address because the MAC address for that unicast address is what is being discovered. Multicast delivery is used precisely to avoid this circular dependency.

---

## Question 17

Which IPv6 address type is functionally equivalent to IPv4 private addresses (RFC 1918) and begins with FD::/8?

- A) Link-local (FE80::/10)
- B) Unique local (FC00::/7, with FD::/8 being the locally assigned subset)
- C) Global unicast (2000::/3)
- D) Multicast (FF00::/8)

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Link-local addresses (FE80::/10) are only valid on a single network segment and are not routed between subnets. They are not equivalent to RFC 1918 private addresses, which are used for internal routing across an organization.
- B is correct: Unique local addresses (FC00::/7) are the IPv6 equivalent of RFC 1918 private addresses. Within this range, addresses starting with FD (binary 1111 1101) indicate locally assigned unique local addresses. They are routable within an organization but should not be advertised to the public internet.
- C is incorrect: Global unicast addresses (2000::/3) are publicly routable on the internet. They are the IPv6 equivalent of public IPv4 addresses, not private addresses.
- D is incorrect: Multicast addresses (FF00::/8) are used for one-to-many delivery. They are not equivalent to RFC 1918 private addresses.

---

## Question 18

An engineer types `ping 2001:DB8:1::2` on a Cisco router and the ping fails with "% No valid source address for destination." What is the most likely cause?

- A) The destination address is in the documentation range and cannot be routed
- B) The router does not have an IPv6 address configured on any interface and `ipv6 unicast-routing` is not enabled
- C) The destination must be specified using its link-local address for ping to work in IPv6
- D) The `ping` command requires the `ipv6` keyword before the address

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 2001:DB8::/32 is the documentation range and should not be routed on the internet, but within a Packet Tracer or lab topology it is widely used for educational purposes and lab routers will attempt to route it.
- B is correct: The error "No valid source address for destination" means the router cannot find an interface with an IPv6 address in the same or routable prefix range as the destination. This occurs when IPv6 has not been configured on any interface or `ipv6 unicast-routing` has not been enabled, leaving the router without a usable IPv6 source address.
- C is incorrect: The standard `ping` command on Cisco IOS accepts global unicast addresses as destinations. Link-local addresses require specifying an exit interface (e.g., `ping FE80::2 Gi0/0`) but global unicast addresses do not have this restriction.
- D is incorrect: On Cisco IOS, the `ping` command automatically determines whether to use IPv4 or IPv6 based on the address format entered. Typing `ping 2001:DB8:1::2` is the correct syntax and does not require a separate `ipv6` keyword in standard IOS.

---

## Question 19

Duplicate Address Detection (DAD) is a required process in IPv6 address configuration. Which ICMPv6 message type does a host send during DAD, and what triggers a DAD failure?

- A) Router Solicitation; DAD fails if a Router Advertisement is received before DAD completes
- B) Neighbor Solicitation; DAD fails if a Neighbor Advertisement is received in response, indicating the address is already in use
- C) Echo Request; DAD fails if an Echo Reply is received from the target address
- D) Router Advertisement; DAD fails if another Router Advertisement is received from the same prefix

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Router Solicitation is sent by hosts to discover routers, not for DAD. DAD uses Neighbor Solicitation messages targeted at the address being tested.
- B is correct: During DAD, the host sends a Neighbor Solicitation for its own tentative address (as source) to the address's solicited-node multicast group. If another node responds with a Neighbor Advertisement claiming that address, DAD fails — the address is a duplicate and cannot be used.
- C is incorrect: Echo Request/Reply (ping) is not used for DAD. DAD is performed during address autoconfiguration before the address is fully assigned.
- D is incorrect: Router Advertisement is sent by routers, not hosts, and is used for prefix distribution (SLAAC), not for DAD. DAD uses Neighbor Solicitation.

---

## Question 20

A network is being upgraded to support both IPv4 and IPv6 simultaneously during a transition period. Which transition mechanism allows IPv6 packets to be encapsulated inside IPv4 packets to traverse IPv4-only portions of the network?

- A) NAT64
- B) Dual-stack
- C) 6to4 tunneling
- D) DHCPv6

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: NAT64 translates between IPv6 source addresses and IPv4 destinations, allowing IPv6-only hosts to communicate with IPv4-only servers. It does not encapsulate IPv6 inside IPv4.
- B is incorrect: Dual-stack means a device runs both IPv4 and IPv6 simultaneously on the same interface. It does not involve encapsulation of one protocol inside the other.
- C is correct: 6to4 tunneling (and similar mechanisms like ISATAP and manual IPv6-in-IPv4 tunnels) encapsulate IPv6 packets inside IPv4 packets, allowing IPv6 traffic to traverse IPv4-only infrastructure. This is the classic "tunneling" transition mechanism referenced on the CCNA exam.
- D is incorrect: DHCPv6 is an address assignment protocol for IPv6 networks. It has no role in tunneling or protocol encapsulation for transition mechanisms.
