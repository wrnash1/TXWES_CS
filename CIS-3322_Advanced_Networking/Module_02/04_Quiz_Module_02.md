# Quiz: Module 02 - Subnetting and VLSM Configurations

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

How many usable host IP addresses are available in a /28 subnet?

- A) 16
- B) 14
- C) 30
- D) 6

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 16 is the total number of addresses in a /28 subnet (2^4 = 16), not the usable host count.
- B is correct: A /28 has 4 host bits. 2^4 = 16 total addresses. Subtract 2 (network and broadcast) = 14 usable hosts.
- C is incorrect: 30 is the usable host count for a /27 subnet (2^5 - 2 = 30).
- D is incorrect: 6 is the usable host count for a /29 subnet (2^3 - 2 = 6).

---

## Question 2

Which of the following most accurately describes CIDR prefix matching as used in IP routing?

- A) The process by which a router selects the routing table entry with the longest (most specific) matching prefix when forwarding a packet.
- B) A method for assigning Class A, B, or C addresses based on the first octet value without variable-length subnet boundaries.
- C) A technique for splitting a large broadcast domain into smaller subnets by borrowing host bits.
- D) The process of summarizing multiple contiguous network prefixes into a single shorter prefix to reduce routing table size.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: CIDR longest-prefix match is the fundamental IP forwarding rule. The most specific matching route (longest prefix) always wins.
- B is incorrect: This describes classful addressing (pre-CIDR). Classful addressing does not support variable-length subnet masks.
- C is incorrect: This describes subnetting — borrowing host bits — not the prefix-matching lookup process.
- D is incorrect: This describes route summarization (supernetting), which is related but distinct from prefix matching during packet forwarding.

---

## Question 3

Which command on a Cisco router traces the Layer 3 hop-by-hop path to a destination?

- A) `traceroute [destination]`
- B) `nslookup [hostname]`
- C) `netstat -ano`
- D) `ping [destination]`

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: `traceroute` on Cisco IOS (or `tracert` on Windows) sends packets with incrementing TTL values to discover each router hop in the path to a destination.
- B is incorrect: `nslookup` is a DNS lookup tool for resolving hostnames to IP addresses. It does not trace routing paths.
- C is incorrect: `netstat -ano` displays active TCP/UDP connections and listening ports on a host. It is not a routing path tool.
- D is incorrect: `ping` tests end-to-end reachability but does not show individual hop addresses along the path.

---

## Question 4

A network engineer is troubleshooting an IP address conflict on a production subnet. Which action resolves the root cause?

- A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range
- B) Change the interface to use a public DNS resolver such as 8.8.8.8
- C) Correct the subnet mask to match the network segment
- D) Reboot the physical machine and wait for services to reload

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: An IP address conflict occurs when two devices share the same address. Releasing the DHCP lease forces the DHCP server to assign a new unique address. Alternatively, assigning a static address outside the DHCP pool prevents future conflicts.
- B is incorrect: Changing the DNS resolver does not resolve an IP address conflict; DNS and IP addressing are separate functions.
- C is incorrect: A subnet mask error causes routing problems, not address conflicts between devices. The root cause of a conflict is two devices with the same IP, not a mask mismatch.
- D is incorrect: Rebooting may temporarily clear the conflict but does not resolve the underlying address assignment problem.

---

## Question 5

A network administrator needs to prevent attackers from capturing plaintext management passwords on a subnet. Which configuration directly addresses this threat?

- A) Configure SSH for terminal access and HTTPS for web interfaces, disabling Telnet and HTTP
- B) Implement switch port security to restrict access based on MAC addresses
- C) Enable SNMPv3 with authPriv to encrypt SNMP management traffic
- D) Deploy an out-of-band management network to isolate administrative traffic

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: SSH and HTTPS encrypt management session traffic end-to-end, preventing credential capture by packet sniffers. The Cisco IOS command `transport input ssh` on VTY lines enforces SSH-only access.
- B is incorrect: Port security restricts which MAC addresses can use a switch port. It does not encrypt credentials sent over the network.
- C is incorrect: SNMPv3 authPriv encrypts SNMP traffic, which is valuable, but does not address Telnet/HTTP credential exposure on management sessions.
- D is incorrect: An out-of-band network provides isolation but does not encrypt traffic. Telnet on an isolated network is still plaintext.

---

## Question 6

You need to subnet 10.0.0.0/24 to create subnets that support exactly 30 hosts each. Which prefix length should you use?

- A) /25
- B) /26
- C) /27
- D) /28

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: /25 provides 126 usable hosts per subnet, which is far more than needed and wastes address space.
- B is incorrect: /26 provides 62 usable hosts per subnet. This works but is not the smallest prefix that supports 30 hosts.
- C is correct: /27 has 5 host bits. 2^5 - 2 = 30 usable hosts. This is the smallest subnet that satisfies exactly 30 hosts.
- D is incorrect: /28 provides only 14 usable hosts, which does not meet the 30-host requirement.

---

## Question 7

A router has these two entries in its routing table: 172.16.0.0/16 via 10.0.0.1 and 172.16.5.0/24 via 10.0.0.2. A packet arrives destined for 172.16.5.25. Which route does the router use?

- A) 172.16.0.0/16 via 10.0.0.1
- B) 172.16.5.0/24 via 10.0.0.2
- C) Both routes are used simultaneously through load balancing
- D) The router drops the packet because two routes match

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Although 172.16.0.0/16 does match 172.16.5.25, it is a less specific route than /24.
- B is correct: Longest-prefix match always selects the most specific route. 172.16.5.0/24 is more specific than 172.16.0.0/16 for this destination.
- C is incorrect: Load balancing only applies when two routes have equal cost and equal prefix length, not when prefix lengths differ.
- D is incorrect: IP routing does not drop packets due to multiple matches. It always selects the longest-prefix match.

---

## Question 8

Which subnet mask should you use for a point-to-point serial WAN link connecting two routers, to minimize address waste?

- A) /24 (255.255.255.0)
- B) /28 (255.255.255.240)
- C) /30 (255.255.255.252)
- D) /32 (255.255.255.255)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: /24 provides 254 usable hosts on a link that needs only 2, wasting 252 addresses.
- B is incorrect: /28 provides 14 usable hosts, still far more than needed for a two-device point-to-point link.
- C is correct: /30 provides exactly 2 usable host addresses (2^2 - 2 = 2), which is precisely what a point-to-point link between two routers requires.
- D is incorrect: /32 identifies a single host address and provides no usable host range for a link.

---

## Question 9

A network engineer is designing VLSM subnets from 192.168.1.0/24 for four segments needing 100, 50, 20, and 2 hosts respectively. In what order should subnets be allocated?

- A) Smallest to largest, starting with the 2-host segment
- B) Largest to smallest, starting with the 100-host segment
- C) Alphabetically by segment name
- D) Order does not matter; any allocation order produces the same result

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Allocating small subnets first fragments the address space, potentially creating gaps that prevent efficient use of the remaining space for larger subnets.
- B is correct: VLSM best practice is to allocate the largest subnet first, then carve smaller subnets from the remaining contiguous address space. This prevents fragmentation and keeps the address plan organized.
- C is incorrect: Alphabetical order has no relevance to IP address allocation efficiency.
- D is incorrect: Order does matter. Starting with small subnets can waste large blocks and create an unorganized, harder-to-summarize address plan.

---

## Question 11

A router interface is configured with `ip address 172.16.32.0 255.255.240.0`. A host sends a packet destined for 172.16.47.200. Will the router consider this destination as reachable on this directly connected interface?

- A) No — 172.16.47.200 is in a different /20 block
- B) Yes — 172.16.47.200 is within the 172.16.32.0/20 subnet
- C) No — the /20 mask only covers 172.16.32.0 through 172.16.39.255
- D) Yes — but only if OSPF is configured to advertise this network

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The /20 mask (255.255.240.0) has a block size of 16 in the third octet. The subnet 172.16.32.0/20 covers 172.16.32.0 through 172.16.47.255. The address 172.16.47.200 falls within this range.
- B is correct: With a /20 mask, the block size is 16 in the third octet (256-240=16). Starting at .32, the subnet covers .32.0 through .47.255. The destination 172.16.47.200 is within this range and is directly reachable on this interface.
- C is incorrect: A /20 block size of 16 means the range is .32 through .47 in the third octet, not .32 through .39. A /21 would cover only 8 values in the third octet.
- D is incorrect: Directly connected routes are installed automatically with AD 0 when an interface comes up. No routing protocol is needed for directly connected prefixes.

---

## Question 12

Which of the following summarizes the four networks 10.4.0.0/24, 10.5.0.0/24, 10.6.0.0/24, and 10.7.0.0/24 into the most precise (smallest) single summary route?

- A) 10.0.0.0/8
- B) 10.4.0.0/22
- C) 10.4.0.0/21
- D) 10.4.0.0/16

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 10.0.0.0/8 summarizes the entire Class A range 10.0.0.0 through 10.255.255.255, which is far too broad. It would include millions of subnets not in this set.
- B is correct: The four /24 networks (10.4, 10.5, 10.6, 10.7) represent a contiguous block of 4 networks in the third octet starting at 4. Converting to binary: 00000100 through 00000111 — the first 6 bits (000001) are common. The summary mask covers the first 22 bits (8+8+6=22). The summary route is 10.4.0.0/22.
- C is incorrect: 10.4.0.0/21 covers 10.4.0.0 through 10.11.255.255 (block size 8 in the third octet), which includes networks 10.8.x.x through 10.11.x.x that are not in this set. This is less precise.
- D is incorrect: 10.4.0.0/16 covers 10.4.0.0 through 10.4.255.255, which only covers the 10.4.x.x range and misses 10.5, 10.6, and 10.7. This is incorrect for a summary and is actually less inclusive than needed.

---

## Question 13

A network engineer needs to subnet 192.168.50.0/24 to create exactly 6 subnets with the maximum number of hosts per subnet. Which prefix length achieves this?

- A) /26 (provides 4 subnets)
- B) /27 (provides 8 subnets, with 30 usable hosts each)
- C) /28 (provides 16 subnets, with 14 usable hosts each)
- D) /29 (provides 32 subnets, with 6 usable hosts each)

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: /26 provides 2^2 = 4 subnets, which is fewer than the required 6. This does not meet the requirement.
- B is correct: /27 provides 2^3 = 8 subnets, which satisfies the minimum of 6. Each subnet has 2^5 - 2 = 30 usable hosts. This is the most efficient choice — the fewest borrowed bits that still meet the subnet count requirement, maximizing hosts per subnet.
- C is incorrect: /28 provides 16 subnets (more than needed) but reduces hosts per subnet to 14. This wastes subnets unnecessarily when /27 meets the requirement with more hosts per subnet.
- D is incorrect: /29 provides 32 subnets and only 6 usable hosts per subnet. While it meets the subnet count requirement, it dramatically reduces the hosts-per-subnet capacity. /27 is the more efficient solution.

---

## Question 14

An engineer configures R1 with `ip route 10.0.0.0 255.255.0.0 192.168.1.2`. Later, a more specific route to 10.0.5.0/24 is learned via OSPF pointing to 192.168.1.3. A packet arrives for 10.0.5.100. Which route does the router use?

- A) The static route to 10.0.0.0/16 because static routes have lower AD than OSPF
- B) The OSPF route to 10.0.5.0/24 because it is a more specific (longer prefix) match
- C) Both routes are used simultaneously via equal-cost load balancing
- D) The static route because it was installed first

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Although static routes have lower AD (1) than OSPF (110), the longest prefix match rule takes precedence over administrative distance when two routes match the same destination with different prefix lengths. The /24 is more specific than the /16.
- B is correct: IP routing always uses the longest prefix match. The /24 route matches 10.0.5.0 to 10.0.5.255, while the /16 matches 10.0.0.0 to 10.0.255.255. The /24 is more specific and is used regardless of administrative distance.
- C is incorrect: Load balancing only applies to routes with identical prefix lengths and equal metrics. These routes have different prefix lengths (/16 and /24), so longest prefix match applies, not load balancing.
- D is incorrect: Installation order has no effect on route selection. Cisco IOS always selects the best route by prefix length, then administrative distance, then metric — in that order.

---

## Question 15

Which IP address and mask combination is NOT a valid host address in the 192.168.100.128/25 subnet?

- A) 192.168.100.129 /25
- B) 192.168.100.200 /25
- C) 192.168.100.255 /25
- D) 192.168.100.254 /25

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect (it is valid): 192.168.100.129 is the first usable host in the 192.168.100.128/25 subnet. The range of valid hosts is .129 through .254. This is a valid host address.
- B is incorrect (it is valid): 192.168.100.200 falls within the host range .129 through .254 and is a valid host address.
- C is correct: 192.168.100.255 is the broadcast address for the 192.168.100.128/25 subnet. The subnet covers .128 through .255; .255 is the broadcast and cannot be assigned to a host.
- D is incorrect (it is valid): 192.168.100.254 is the last valid host address in this subnet (one below the broadcast of .255). It is a valid assignable address.

---

## Question 16

A /30 subnet is typically used for which type of network link, and how many usable host addresses does it provide?

- A) LAN access segment — 62 usable hosts
- B) Point-to-point WAN link between two routers — 2 usable hosts
- C) Server farm segment — 14 usable hosts
- D) Loopback address assignment — 1 usable host

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A /30 provides only 2 usable hosts (2^2 - 2 = 2), which is far too small for an access LAN with end users. A /30 is explicitly designed for point-to-point links, not LANs. A /26 provides 62 usable hosts.
- B is correct: A /30 subnet (4 addresses: 1 network, 2 usable hosts, 1 broadcast) is the standard choice for point-to-point WAN links where exactly 2 hosts (the two router interfaces) need addresses. It wastes the fewest addresses while still providing a valid network and broadcast address.
- C is incorrect: 14 usable hosts corresponds to a /28 (2^4 - 2 = 14), not /30. A /30 only provides 2 usable addresses.
- D is incorrect: Loopback interfaces typically use /32 masks, which assign exactly one address to one device. A /30 is not used for loopbacks.

---

## Question 17

An engineer is given the block 10.10.0.0/22 to subnet. How many /24 subnets can be created from this block?

- A) 2
- B) 4
- C) 8
- D) 16

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 2 subnets would require only a /23 (which spans 2 class C equivalents). A /22 is larger and contains 4 /24 networks.
- B is correct: A /22 block spans 2^(24-22) = 4 times a /24 in size. The block 10.10.0.0/22 covers 10.10.0.0 through 10.10.3.255, which contains exactly four /24 networks: 10.10.0.0/24, 10.10.1.0/24, 10.10.2.0/24, and 10.10.3.0/24.
- C is incorrect: 8 /24 subnets would require a /21 block (2^3 = 8 times the size of a /24). A /22 only contains 4 /24 networks.
- D is incorrect: 16 /24 subnets would require a /20 block (2^4 = 16 times the size of a /24). A /22 is smaller than a /20.

---

## Question 18

A Cisco router has the command `ip address 10.1.1.1 255.255.255.252` applied to its Serial0/0/0 interface. Which statement is true about this subnet?

- A) The network address is 10.1.1.0 and the broadcast address is 10.1.1.3
- B) The network address is 10.1.1.1 and the broadcast address is 10.1.1.4
- C) The subnet can support up to 6 usable hosts
- D) The mask 255.255.255.252 is equivalent to /30 and allows 4 usable hosts

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: /30 (255.255.255.252) has a block size of 4. Starting at 10.1.1.0, the subnet covers .0 through .3. Network address = 10.1.1.0, broadcast = 10.1.1.3, usable hosts = 10.1.1.1 and 10.1.1.2. This is the standard /30 for a point-to-point WAN link.
- B is incorrect: 10.1.1.1 is the host address assigned to the interface, not the network address. The network address of a /30 starting at .0 is always .0, not .1.
- C is incorrect: A /30 provides exactly 2 usable hosts (2^2 - 2 = 2). 6 usable hosts corresponds to a /29 (2^3 - 2 = 6).
- D is incorrect: 255.255.255.252 is indeed /30, but /30 provides only 2 usable hosts, not 4. The block size is 4 (total addresses), but 2 of those 4 are the network and broadcast addresses.

---

## Question 19

A network engineer configures a static route: `ip route 0.0.0.0 0.0.0.0 203.0.113.1`. What type of route is this and when does it match traffic?

- A) A host route that only matches traffic destined for 0.0.0.0
- B) A default route that matches all traffic with no more specific route in the routing table
- C) An invalid route — the all-zeros network is not a valid destination
- D) A summary route that aggregates all RFC 1918 private address ranges

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 0.0.0.0/0 is not a host route. A host route uses a /32 mask to match exactly one IP address. The 0.0.0.0/0 route matches any IP address that does not have a more specific match.
- B is correct: 0.0.0.0/0 is the default route (also called the gateway of last resort). It matches all traffic — its prefix length is 0, making it the least specific possible route. It is only selected when no longer-prefix route exists for the destination. Cisco IOS displays it as S* in the routing table when configured via a static route.
- C is incorrect: 0.0.0.0/0 is a perfectly valid and widely used route in Cisco IOS. It is set as the gateway of last resort and appears in the routing table of virtually every internet-connected router.
- D is incorrect: Route summarization produces a specific aggregate like 10.0.0.0/8 or 192.168.0.0/16, not 0.0.0.0/0. The default route does not aggregate RFC 1918 ranges — it matches all traffic regardless of address family or range.

---

## Question 20

Using VLSM, an engineer allocates subnets from 172.20.0.0/24 as follows: 172.20.0.0/25 for VLAN 10, 172.20.0.128/26 for VLAN 20, 172.20.0.192/27 for VLAN 30. What is the network address and usable host range of the next available block after these three allocations?

- A) 172.20.0.224/27 — usable hosts .225 through .254
- B) 172.20.0.224/28 — usable hosts .225 through .238
- C) 172.20.1.0/24 — the /24 is exhausted; a new /24 is needed
- D) 172.20.0.240/28 — usable hosts .241 through .254

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The three allocations use: /25 covers .0–.127; /26 covers .128–.191; /27 covers .192–.223. The next available block starts at .224. The remaining space in the /24 is .224–.255, which is exactly a /27 (32 addresses). Network = 172.20.0.224/27, broadcast = 172.20.0.255, usable hosts = .225 through .254.
- B is incorrect: .224/28 would cover .224–.239 (16 addresses), which is a smaller block than the entire remaining /27 space. There is no reason to use a /28 here if a /27 is available.
- C is incorrect: The 172.20.0.0/24 is not exhausted. After the three allocations, the address space .224 through .255 remains available within the /24. No additional /24 block is required.
- D is incorrect: 172.20.0.240/28 starts too late — it skips the .224–.239 range. The next available block begins at .224, not .240.

---

## Question 10

An engineer configures `ip address 192.168.10.64 255.255.255.192` on a router interface. What is the broadcast address for this subnet?

- A) 192.168.10.127
- B) 192.168.10.128
- C) 192.168.10.255
- D) 192.168.10.95

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The mask 255.255.255.192 is /26 with a block size of 64. Starting at 192.168.10.64, the next subnet begins at .128. The broadcast address is one below the next subnet: 192.168.10.127.
- B is incorrect: 192.168.10.128 is the network address of the next /26 subnet, not the broadcast of this subnet.
- C is incorrect: 192.168.10.255 is the broadcast address of the last /26 subnet (192.168.10.192/26), not this one.
- D is incorrect: 192.168.10.95 would be the broadcast of a /27 starting at .64 (block size 32), not a /26 (block size 64).
