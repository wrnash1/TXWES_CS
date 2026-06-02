# Discussion Forum: Module 01 - Network Architectures & Topologies

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Hospital Campus Redesign

A regional hospital is replacing its 15-year-old flat network with a modern design. The hospital has one main building with 12 floors, approximately 1,400 networked devices including IP phones, workstations, medical IoT equipment, and wireless access points. The IT director wants the network to support future growth to 2,500 devices without a full redesign. The hospital cannot afford any single point of failure that would disrupt patient monitoring systems.

Sub-questions:

1. Which network architecture model (three-tier, collapsed core, or spine-leaf) would you recommend for this hospital campus, and what specific characteristics of the hospital's requirements drive your recommendation?

2. The hospital's Access layer switches need to support IP phones and medical IoT devices simultaneously. What Access layer feature allows a single physical port to carry both voice and data traffic to separate VLANs, and why is this important in a medical environment?

3. The IT director asks whether the Core layer switches need to run any routing protocols or ACLs to improve security at the Core. How would you respond, and what layer should those security controls be applied to instead?

Write an initial post of 175-225 words that addresses all three sub-questions using accurate networking terminology.

---

## Scenario B: Data Center Modernization

A financial services company is migrating its legacy three-tier data center to a modern architecture. The current data center uses spanning tree protocol and has frequent convergence delays during failover events. The new design must support virtualized workloads with east-west traffic (server-to-server) that accounts for 80% of all data center traffic. Latency must be consistent and predictable.

Sub-questions:

1. What topology is most appropriate for this data center modernization, and why does it specifically address the problems of STP convergence delays and unpredictable east-west traffic latency?

2. In the recommended topology, what routing mechanism replaces Spanning Tree Protocol to provide both load balancing and fast failover, and how does it work in simple terms?

3. The company's architect says that adding more servers in the future should not require replacing the spine switches. How does the recommended topology's design accommodate this growth, and what is added when server capacity needs to increase?

Write an initial post of 175-225 words that addresses all three sub-questions using accurate networking terminology.

---

## Scenario C: Branch Office Connectivity Design

A national retail chain has 200 store locations across the country. Each store has 15-20 devices (POS terminals, employee workstations, security cameras, and a local printer). All stores must communicate with the corporate headquarters in Dallas for inventory management and payment processing. Direct store-to-store communication is rarely needed. The network budget is limited and each store has only a single WAN connection.

Sub-questions:

1. Which WAN topology model (full mesh, partial mesh, or hub-and-spoke) is most appropriate for this retail chain, and what specific design characteristics of hub-and-spoke match this scenario?

2. A store in Austin needs to send a transaction to a store in Phoenix. Describe the path that traffic takes in the topology you recommended, and explain whether this path represents a design weakness or an acceptable trade-off.

3. The company is considering adding a second WAN link at ten high-priority stores for redundancy. How does adding these redundant links change the topology classification, and does this change require redesigning the entire WAN?

Write an initial post of 175-225 words that addresses all three sub-questions using accurate networking terminology.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post - Technical Accuracy | 3 | All three sub-questions answered with correct networking terminology and accurate concept application |
| Initial Post - Depth and Analysis | 2 | Responses go beyond definitions to analyze trade-offs and justify recommendations |
| Initial Post - Word Count | 1 | Post falls within the 175-225 word range |
| Peer Response 1 | 2 | Substantive reply (50+ words) that adds a new perspective, identifies an alternative approach, or respectfully challenges a point with supporting reasoning |
| Peer Response 2 | 2 | Substantive reply (50+ words) meeting the same criteria as Peer Response 1 |

Responses of "Great post!" or "I agree with everything you said" without additional technical content receive 0 points for that peer response.

---

## Professor Nash's Note

Network architecture decisions are never purely technical — they involve budget, existing infrastructure, staff skill sets, and long-term business goals. As you respond to your peers, push each other to think beyond the textbook answer and consider the real-world trade-offs that engineers face when these designs are proposed in front of a management team with a fixed budget. That is the kind of critical thinking the CCNA exam rewards, and it is exactly what makes a strong network engineer.
