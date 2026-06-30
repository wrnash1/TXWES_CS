# Discussion Board: Module 03 – WAN Technologies: MPLS, SD-WAN & VPNs
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 8, 2026 at 11:59 PM CST

---

## Graduate Discussion Instructions
Initial post: **400+ words**, all prompt components addressed, at least **1 credible technical citation** (RFC, Cisco design guide, or peer-reviewed paper).
Peer responses: **Substantive replies to 2+ classmates** — add technical depth, challenge assumptions, or present an alternative architectural approach.

---

## Discussion Prompt: MPLS to SD-WAN Migration at a Retail Chain

**Scenario:**
You are a senior network architect consulting for a national retail chain with 450 store locations across the United States. The current WAN uses private MPLS circuits at every store — 20 Mbps per site — costing approximately $1.2 million per month. The chain's IT director has issued a mandate: modernize the WAN, reduce costs by 40%, and improve performance for cloud-based POS (Point of Sale) and inventory management applications that are increasingly experiencing latency over the hub-and-spoke MPLS topology.

The chain has three requirements that cannot be compromised:
1. **PCI DSS Compliance** — Credit card data must be encrypted in transit at all times.
2. **Store Uptime SLA** — Each store must be able to process transactions even if its primary WAN link fails.
3. **Centralized Visibility** — The security operations team needs application-level visibility at every store.

**Write a graduate-level post (400+ words) addressing ALL of the following:**

1. **SD-WAN Architecture Recommendation:** Describe the SD-WAN architecture you would deploy for this retail chain. Include: which Cisco SD-WAN components you would need (vManage, vSmart, vBond — cloud-hosted or on-premise?), what transport types you would use at each store (MPLS, broadband, LTE), and how you would design the control plane.

2. **PCI DSS Compliance:** How does Cisco SD-WAN satisfy the PCI DSS requirement for data encryption in transit? Be specific about which part of the SD-WAN architecture provides this.

3. **WAN Redundancy for Store Uptime:** Explain how SD-WAN's dual-transport design (e.g., broadband primary + LTE backup) provides store uptime that the current single-MPLS design cannot. What SD-WAN feature detects and responds to link failures sub-second?

4. **MPLS Coexistence During Migration:** You cannot migrate all 450 stores simultaneously. How would you phase the migration? During the transition period, some stores will be on MPLS-only and others on SD-WAN. How does SD-WAN interoperate with the existing MPLS network (hint: MPLS becomes one of the SD-WAN transports/colors)?

5. **Cost Justification:** The SD-WAN solution will cost approximately $600K to deploy (controller licensing + professional services) plus reduced circuit costs. Build a rough business case for the 40% cost reduction target.

**Citation Requirement:** Cite at least one of:
- IETF RFC 3031 (MPLS Architecture)
- IETF RFC 4364 (BGP/MPLS L3VPN)
- Cisco SD-WAN Design Guide (cisco.com — free)
- PCI DSS v4.0 standard (pcisecuritystandards.org — free)

---

## Peer Response Guidance
Challenge your classmates' migration phasing decisions. Consider: "You proposed migrating by region — what would happen if a store in a partially migrated region needs to communicate with a store in an un-migrated region? How does inter-domain routing work during the transition?"

---

## Grading Rubric (100 Points)
| Component | Points |
|---|---|
| SD-WAN Architecture — components, transports, control plane | 25 |
| PCI DSS Compliance — specific SD-WAN mechanism cited | 20 |
| WAN Redundancy — dual-transport and failure detection | 20 |
| Migration phasing — MPLS coexistence strategy | 15 |
| Cost justification — business case elements | 10 |
| Citation — credible, properly integrated | 5 |
| Peer responses — substantive, technically advances discussion | 5 |
| **Total** | **100** |
