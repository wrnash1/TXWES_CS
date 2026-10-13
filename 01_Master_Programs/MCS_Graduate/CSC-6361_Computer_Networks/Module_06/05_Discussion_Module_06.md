# Discussion Board: Module 06 – Cloud Networking & Hybrid Architectures

## CSC-6361 Advanced Computer Networks | Graduate Level

## Initial Post Due: Wednesday, December 9, 2026 at 11:59 PM CST

## Peer Responses Due: Sunday, December 13, 2026 at 11:59 PM CST

---

## Graduate Discussion Instructions

Your initial post must be **400 words or more**, address the specific scenario and all sub-questions for your chosen option, include at least **one citation** from a credible technical source (RFC, Cisco documentation, AWS/Azure documentation, peer-reviewed article, or IEEE/ACM paper), and demonstrate connection between the week's lecture content and real-world enterprise decision-making.

After posting your initial response, provide **substantive replies to at least two classmates**. A substantive reply adds new technical information, poses a challenging follow-up question, offers an alternative design perspective, or identifies a trade-off the original poster did not address. "Great post, I agree!" is not a substantive reply.

---

## Background: SD-WAN, VXLAN, and Hybrid Cloud in the Enterprise

Modern enterprises face a network architecture transformation unlike anything in the past two decades. Traditional hub-and-spoke WAN designs built on MPLS circuits — reliable, predictable, but expensive and inflexible — are being challenged by SD-WAN architectures that separate the underlay transport from the overlay routing and policy planes. Simultaneously, the growth of cloud workloads has made hybrid connectivity (AWS Direct Connect, Azure ExpressRoute) a first-class design requirement rather than an afterthought.

The technologies covered in Module 06 — SD-WAN with Viptela OMP, VXLAN-EVPN data center fabrics, and dedicated cloud interconnects — represent where enterprise networking investment is concentrated right now. As a graduate network engineer, you will be expected not just to configure these technologies, but to make and defend architectural decisions about when to deploy them, at what cost, and with what operational trade-offs.

Choose **one** of the three scenarios below. Your post must be specific — cite actual technology names, protocol behaviors, and configuration or design decisions from the lecture material.

---

## Scenario Options — Choose One

### Scenario A: SD-WAN Design Decision for a Multi-Site Enterprise

You are the lead network architect for a regional healthcare network with 1 headquarters, 4 hospitals, and 22 clinics — 27 sites total. The current WAN is MPLS-only, with dedicated circuits ranging from 10 Mbps (clinics) to 1 Gbps (hospitals). Annual WAN cost: $1.8 million. The CFO has approved a budget for WAN modernization and the CTO has asked for an SD-WAN evaluation.

Address **all** of the following in your post:

1. **Architecture recommendation:** Propose a specific SD-WAN deployment architecture using Cisco Viptela components. Which devices go where? Would you deploy vManage/vSmart/vBond on-premise, in a hosted cloud, or use Cisco's cloud-managed SD-WAN (Cisco SD-WAN Cloud)? Justify your choice.

2. **Transport strategy:** The sites currently have only MPLS. Would you replace MPLS entirely, run dual-transport (MPLS + broadband internet), or triple-transport (MPLS + internet + LTE)? Consider the healthcare compliance implications (HIPAA) when selecting transports and whether IPsec on broadband internet is sufficient for PHI (Protected Health Information) traffic.

3. **Policy design:** Describe a specific centralized data policy you would implement. For example: How would you ensure Electronic Health Records (EHR) traffic to the data center gets the MPLS TLOC, while general internet traffic (Windows Update, YouTube) breaks out locally at each clinic? Reference OMP TLOC colors and application-aware routing in your answer.

4. **Migration risk:** What is the single greatest operational risk during the cutover from MPLS to SD-WAN? Describe a specific mitigation strategy. Reference at least one credible source (Cisco design guide, a vendor white paper, or an IEEE/ACM paper on SD-WAN deployment).

---

### Scenario B: Direct Connect vs. VPN Cost-Benefit Analysis

You are a senior network engineer at a mid-sized financial services firm that processes trading transactions in AWS us-east-1. The application team has reported intermittent latency spikes (50–120ms) on the current site-to-site IPsec VPN connection to AWS, causing failed transactions and SLA violations. The VP of Infrastructure has asked you to evaluate AWS Direct Connect as a replacement.

Address **all** of the following in your post:

1. **Root cause analysis:** Explain specifically why IPsec VPN over the public internet produces variable latency, and how AWS Direct Connect eliminates this problem at the physical and routing level. Reference the VIF types (Private VIF vs. Transit VIF) and BGP routing model in your explanation.

2. **Design proposal:** Design a Direct Connect architecture for this firm. Would you use a single 1 Gbps dedicated connection, a LAG (Link Aggregation Group), or two separate circuits in active/standby? The firm's current WAN throughput to AWS peaks at 400 Mbps with a 99.95% uptime SLA. Show your math on why your chosen option meets the SLA while providing headroom for growth.

3. **Failover strategy:** Even with Direct Connect, you need a backup path. Describe how you would configure BGP AS path prepending on the backup IPsec VPN to ensure it is only used when Direct Connect fails. What BGP attributes would you manipulate on each path, and which side (enterprise or AWS) applies the relevant route preference?

4. **Cost justification:** Direct Connect 1 Gbps costs approximately $1,800–$2,500/month depending on the colocation partner. The current IPsec VPN costs roughly $200/month in AWS VPN gateway fees. Write a one-paragraph cost-benefit argument you would present to the VP — include the business risk cost of SLA violations as a factor.

---

### Scenario C: VXLAN vs. MPLS for Data Center Fabric

Your company is building a new data center to support 2,000 VMs across 20 physical servers. The network team is debating between two fabric approaches: (1) a traditional MPLS L2VPN fabric using existing service provider equipment, or (2) a modern VXLAN-EVPN leaf-spine fabric using Cisco Nexus or Arista switches.

Address **all** of the following in your post:

1. **Technical comparison:** Compare VXLAN-EVPN and MPLS L2VPN as data center overlay technologies on the following dimensions: maximum segment count (VLAN/VNI scale), hypervisor integration, control plane MAC learning approach, and inter-subnet routing model. Reference RFC 7348 (VXLAN) and RFC 7432 (EVPN) in your comparison.

2. **EVPN control plane advantage:** Explain specifically how EVPN Type 2 MAC/IP advertisement routes eliminate broadcast-based MAC learning (ARP flooding) compared to a traditional VLAN/STP fabric. Use a specific example: what happens in each fabric when a new VM is powered on and sends its first ARP request?

3. **BUM traffic handling:** In your proposed VXLAN fabric, would you use multicast underlay or ingress replication for BUM traffic? Justify your choice based on the specific environment (2,000 VMs, 20 servers). What are the operational implications of your choice on the underlay network design?

4. **Design recommendation:** Given the 2,000-VM scale and the need to support multiple tenant VLANs (at least 50 distinct Layer 2 segments), make a final recommendation: VXLAN-EVPN or MPLS L2VPN? Justify with specific technical and operational reasons. Cite at least one credible source beyond the lecture material.

---

## Peer Response Guidance

When responding to classmates, choose posts that made a **design decision different from what you would have chosen** and engage substantively with that difference. Strong peer response prompts:

- "You recommended active/standby Direct Connect with BGP AS path prepending. I argued for active/active with a LAG. Given that your firm's peak throughput is 400 Mbps on a 1 Gbps circuit, what specific event would cause your active/standby design to drop traffic for longer than your 99.95% SLA allows?"
- "You chose ingress replication for BUM traffic. Your design has 20 servers — so 20 VTEPs. At 2,000 VMs, how many ARP broadcasts per second would ingress replication generate at peak, and at what scale would you reconsider multicast underlay?"
- "You kept MPLS for healthcare WAN because of HIPAA. But RFC 7348 VXLAN supports optional IPsec encapsulation of the outer UDP packet. Does that change your security argument against broadband internet as a secondary transport?"

---

## Grading Rubric (100 Points)

| Component | Points |
|---|---|
| Substantive Content — all 4 sub-questions addressed, 400+ words, graduate-level technical depth | 40 |
| External Citation — credible technical source (RFC, Cisco doc, AWS/Azure doc, or peer-reviewed paper), properly integrated and referenced | 30 |
| Peer Engagement — meaningful replies to 2+ classmates that add technical value or challenge a design decision | 30 |
| **Total** | **100** |

Initial Post Due: Wednesday, December 9, 2026 at 11:59 PM CST

Peer Responses Due: Sunday, December 13, 2026 at 11:59 PM CST
