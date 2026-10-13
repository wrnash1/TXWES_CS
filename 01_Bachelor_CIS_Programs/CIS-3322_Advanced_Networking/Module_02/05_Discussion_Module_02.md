# Discussion Forum: Module 02 - Subnetting and VLSM Configurations

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: University Campus Addressing

A new state university is designing its IP address plan for the main campus network. The university's ISP has assigned the block 172.20.0.0/16. The network team must allocate subnets for six departments: the College of Business (200 hosts), College of Sciences (150 hosts), College of Arts (80 hosts), the Library (40 hosts), Administrative Offices (20 hosts), and a Data Center WAN link between two core routers (2 hosts). The team is debating whether to use a fixed /24 subnet for every department or apply VLSM.

Sub-questions:

1. If the team uses a fixed /24 for every department, how many host addresses per subnet would go unused in each of the six segments? Calculate the total wasted addresses across all six segments combined.

2. Using VLSM, identify the smallest correct prefix length for each of the six segments and calculate the total number of usable addresses across all six subnets. How many fewer addresses are consumed compared to the fixed /24 approach?

3. The VLSM plan saves address space, but a colleague argues that it makes the network harder to summarize for routing. Explain what route summarization is, give a one-line example of how it applies to this university scenario, and describe whether the colleague's concern is valid in a /16 address space.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario B: Manufacturing Plant Subnet Design

A manufacturing plant is installing a new IP network across three production floors. Floor 1 has 45 programmable logic controllers (PLCs) and 10 workstations; Floor 2 has 25 PLCs and 8 workstations; Floor 3 has 12 PLCs and 5 workstations. There is also a management network for IT staff with 6 devices and a dedicated link between the plant's two routers. The plant has been assigned 10.50.0.0/24 for all internal addressing.

Sub-questions:

1. Calculate the total host requirement for each of the five segments (three floors, one management segment, one WAN link). Then design a complete VLSM allocation from 10.50.0.0/24, showing the network address, prefix, and broadcast address for each segment. Show your allocation order and explain why you chose that order.

2. Floor 1 has the most devices, but a technician suggests using a /24 for Floor 1 to allow future growth to 200 devices. Evaluate this suggestion in terms of address efficiency and explain what would need to change in the overall VLSM plan if the /24 were adopted for Floor 1.

3. The plant's security team wants each floor to be on a separate subnet so that a firewall can apply different access rules to PLCs versus office workstations. Does your VLSM design support this security requirement? Explain how subnet boundaries and inter-VLAN routing interact with firewall policy enforcement at the Distribution layer.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Scenario C: ISP Address Block Management

A regional ISP has been allocated the address block 203.0.113.0/24 to assign to small business customers. The ISP assigns each customer a /28 subnet. The ISP also reserves a /30 for each customer's router-to-ISP WAN link. The ISP's network engineer is evaluating how many customers can be served from this single /24 block.

Sub-questions:

1. Calculate how many /28 customer subnets and how many /30 WAN link subnets can be carved from 203.0.113.0/24. Explain whether it is possible to serve 14 customers (each needing one /28 and one /30) from this single block without running out of addresses.

2. A customer calls to report that one of their 14 hosts cannot communicate on the network. After checking the customer's switch, the engineer sees the host's IP address is 203.0.113.47. The customer's subnet is 203.0.113.32/28. Is this a valid host address, the network address, or the broadcast address for that subnet? Show your work.

3. The ISP is planning to grow to 20 customers in the next year and is considering whether to request a second /24 from their upstream provider or to split the existing /24 more efficiently. Describe one approach that would allow serving more customers from the existing /24 without assigning a new block. Include the trade-off of this approach for the customer's usable host count.

Write an initial post of 175-225 words addressing all three sub-questions.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct subnetting math and accurate VLSM terminology |
| Initial Post - Depth and Analysis | 2 | Responses demonstrate analysis beyond formula application, addressing trade-offs and design rationale |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that verifies or challenges the peer's subnet calculations with supporting math |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

Responses that simply agree without checking the peer's math receive 0 points for that peer response.

---

## Professor Nash's Note

Subnetting is the one skill where the exam does not give you extra time. Practice these calculations until the block-size shortcut is automatic. When you read a peer's VLSM design, verify their numbers — if you spot an error and explain it respectfully and correctly, that is exactly the kind of peer response that earns full credit. The best thing you can do for your classmates right now is to be their independent answer key.
