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
