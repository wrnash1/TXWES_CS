# Discussion Forum: Module 03 - IPv6 Addressing and Configuration

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Enterprise IPv6 Migration Planning

A company currently operates an IPv4-only network. The CTO has directed the IT team to begin planning a dual-stack migration where both IPv4 and IPv6 are active simultaneously on the same infrastructure. The network includes 12 Cisco routers, 40 switches, and approximately 1,200 end devices. The team must decide how to assign IPv6 addresses to end devices: statically, via SLAAC, or via DHCPv6.

Sub-questions:

1. Compare SLAAC and DHCPv6 for assigning IPv6 addresses to the 1,200 end devices. What does SLAAC require from the routers, and what information does it not provide that DHCPv6 can? In a company environment where IT needs to track which device has which IPv6 address, which method is more appropriate?

2. In a dual-stack deployment, each router interface will have both an IPv4 and an IPv6 address. The IPv6 addresses are global unicast with /64 prefixes. The IPv4 subnets use VLSM from the 10.0.0.0/8 space. Describe one operational challenge of managing two separate address schemes on the same infrastructure and one tool or practice that helps mitigate it.

3. The security team is concerned about rogue Router Advertisement messages in the IPv6 environment. A rogue RA could redirect end-device default gateways to an attacker's device. What Cisco switch feature addresses this threat, and where on the network (which layer and which port type) should it be configured?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: IPv6 Static Routing Failure Diagnosis

A network engineer has configured a small three-router IPv6 network. R1 has two LANs (2001:DB8:1::/64 and 2001:DB8:2::/64). R2 connects R1 to R3 via serial links. R3 hosts a server on 2001:DB8:3::/64. The engineer added static routes on all three routers but users on R1's LANs cannot reach the R3 server.

Sub-questions:

1. List three specific items the engineer should verify using show commands when troubleshooting this IPv6 static routing failure. For each item, name the specific show command and explain what a correct output looks like versus what a failure looks like.

2. The engineer checks R1's routing table and sees the static route to 2001:DB8:3::/64 is present, but pings still fail. The engineer then runs `ping ipv6 2001:DB8:3::1 source GigabitEthernet0/0` and the pings succeed. What does this tell you about where the routing failure actually exists, and what should the engineer check next?

3. A colleague suggests simply replacing all static routes with OSPFv3. What is one operational advantage and one operational disadvantage of switching from static routes to OSPFv3 on a small three-router network?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: ISP IPv6 Address Assignment and Security

A small ISP has received the block 2001:DB8:A000::/48 from their upstream provider. The ISP serves residential and business customers. Residential customers receive a /64 prefix for home networks. Business customers receive a /56 prefix to allow subnetting within their organization. The ISP also needs to protect its network from IPv6-specific attacks.

Sub-questions:

1. From the /48 block, how many /56 prefixes can the ISP allocate to business customers? How many /64 prefixes can be allocated to residential customers from the remaining space after assigning 100 /56 blocks to business customers? Show your calculation.

2. The ISP network team has observed ICMPv6 packets with unusually large extension headers arriving from external sources. These packets appear to be a resource-exhaustion attack targeting the ISP's routers. What ICMPv6 message type or extension header is most commonly exploited in this way, and what is a general mitigation strategy the ISP can deploy at its edge routers?

3. A residential customer reports that their home router shows a valid IPv6 address and can reach IPv6 websites, but cannot communicate with a business customer on the same ISP using that business customer's 2001:DB8:A0BB:1::100/64 address. Both customers are on the same ISP. What is the most likely cause of this failure from an addressing and routing perspective?

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct IPv6 terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses go beyond definitions to analyze trade-offs, apply diagnostic reasoning, or connect concepts |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that adds a technical detail, corrects an error, or proposes an alternative approach with supporting reasoning |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

---

## Professor Nash's Note

IPv6 is not a future technology — it is a present-tense requirement. Every enterprise network engineer being hired today is expected to understand dual-stack operation, SLAAC versus DHCPv6, and IPv6 security threats. When you respond to peers, focus on the scenarios most relevant to the careers you are planning. If you are interested in enterprise networking, engage deeply with Scenario A. If security is your focus, Scenario C gives you the most to work with.
