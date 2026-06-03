# Discussion Forum: Module 10 — Routing Protocols: Static, OSPF, and BGP

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

Certification Alignment: CompTIA Network+ (N10-008)

---

### Overview

This week's discussion applies routing protocol concepts to real-world network design and troubleshooting scenarios. You will select one of three scenarios and write a substantive initial post of 175–225 words. After posting, reply to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: Static Routing vs. OSPF at a Growing Company

A small manufacturing company currently has three sites: a headquarters building and two warehouses. Each site has its own subnet. The network was originally designed with static routes on each router — a total of nine static route statements across three routers. The company has just announced a fourth site opening in three months. The IT director asks the network administrator to evaluate whether the current static routing approach should be maintained or whether OSPF should be deployed before the fourth site comes online.

Respond to all three questions:

1. Explain what happens to routing table management complexity as the company continues to add sites under a static routing model. Calculate the number of static route statements that would be needed across all four routers when the fourth site is added, assuming each router must have a route to every other site's subnet.

2. Describe the specific technical advantages OSPF would provide for this four-site network compared to static routing. Include at least two OSPF mechanisms (such as neighbor discovery, LSA flooding, or SPF convergence) in your explanation and explain what each mechanism does for this particular use case.

3. The IT director is concerned about OSPF complexity. Identify one legitimate operational consideration that would favor keeping static routes for this specific scenario — for example, a characteristic of the company's network topology or staffing that might make OSPF unnecessary — and explain whether you would ultimately recommend OSPF or static routing given the company's growth trajectory.

---

#### Scenario B: OSPF Troubleshooting at a Hospital Network

A hospital network administrator runs show ip route on a router and notices that a critical subnet hosting the electronic health records (EHR) server is not present in the routing table. The OSPF process is running. The administrator runs show ip ospf neighbor and sees that the router's OSPF neighbor relationship with the next-hop router shows State: INIT rather than State: FULL. Other subnets are reachable.

Respond to all three questions:

1. Explain what the OSPF neighbor states represent. What does INIT state mean, what must happen for the relationship to progress to FULL state, and what are the two most common configuration mismatches that cause an OSPF neighbor relationship to remain stuck in INIT or EXSTART/EXCHANGE states?

2. The EHR subnet is directly connected to the neighbor router but does not appear in the routing table of the local router. Assuming the neighbor relationship progresses to FULL state after the mismatch is fixed, explain the sequence of events that will occur: what OSPF message type will advertise the EHR subnet, how the LSA propagates through the OSPF area, and how the SPF algorithm uses that information to install the route.

3. Once the neighbor reaches FULL state and routes are installed, the administrator discovers the path to the EHR server is taking a 100 Mbps FastEthernet link instead of an available 1 Gbps GigaEthernet link. Using the OSPF cost formula, explain why this happens with default OSPF settings and describe the exact configuration change needed to make the GigaEthernet link preferred.

---

#### Scenario C: Multihomed Enterprise BGP Design

A medium-sized technology company connects to the internet through two different ISPs: ISP-A (AS 64512) and ISP-B (AS 64513). The company has been assigned its own public ASN (AS 65001) and a public IPv4 prefix. Currently, all internet traffic exits through ISP-A. ISP-B is only used when ISP-A is completely down. The network architect wants to redesign the BGP configuration so that outbound traffic to customers in North America exits through ISP-A, while outbound traffic to customers in Europe exits through ISP-B, for latency optimization.

Respond to all three questions:

1. Describe the difference between iBGP and eBGP. The company's AS is 65001. Which type of BGP session connects the company's edge routers to ISP-A and ISP-B? Which type of BGP session would be used if the company had two edge routers and needed to exchange BGP routing information between them internally?

2. Explain which BGP path attribute is used to influence outbound traffic path selection (the direction from the company toward the internet). Describe how this attribute would be configured differently on the ISP-A peering session versus the ISP-B peering session to achieve the traffic engineering goal described in the scenario.

3. The company wants to ensure that if ISP-A becomes unavailable, all traffic automatically fails over to ISP-B without manual intervention. Explain how BGP handles this failover automatically, referencing the mechanism BGP uses to detect that a peer is unreachable. Also explain why this BGP design requires the company to have its own public ASN rather than using a private ASN for the eBGP sessions.

---

### Response Requirements

Initial Post (due Wednesday at 11:59 PM):

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct terminology: administrative distance, static route, OSPF, BGP, AS-PATH, LOCAL_PREF, eBGP, iBGP, LSDB, SPF, adjacency, convergence, cost, floating static route, default route, autonomous system

Peer Responses (due Sunday at 11:59 PM):

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Provide a specific technical addition, correction, or alternative design consideration — do not simply agree or summarize

---

### Grading Rubric (10 Points Total)

Initial Post — 6 Points:

- 5–6 points: All three sub-questions answered with accurate technical terminology, correct routing concept application, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical depth or contains a specification error (such as incorrect administrative distance values or incorrect OSPF cost formula application).
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

Peer Responses — 4 Points:

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding genuine technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

Routing is where network engineering decisions have the highest consequence. A misconfigured administrative distance can silently route traffic through a suboptimal or insecure path. An OSPF cost left at default can cause traffic to prefer a 100 Mbps link over a gigabit link. A BGP attribute misconfiguration can send a company's traffic to the wrong continent. These are not theoretical risks — they are regular findings in enterprise network audits. The scenarios this week mirror real decisions: the small company choosing between static and dynamic routing, the hospital administrator troubleshooting a broken OSPF adjacency, and the enterprise architect doing traffic engineering with BGP. Each decision has right answers, and understanding why requires exactly the protocol knowledge this module covered.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
