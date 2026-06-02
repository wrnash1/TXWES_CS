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
