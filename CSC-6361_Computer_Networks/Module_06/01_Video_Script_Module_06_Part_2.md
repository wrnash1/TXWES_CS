# Video Script: Module 06 – Cloud Networking & Hybrid Architectures
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 2 of 2 | Estimated Duration: 15–18 minutes
## Week 6: November 23 – December 1, 2026 (Extended due to Thanksgiving)
## Due: Tuesday, December 1, 2026 at 11:59 PM CST
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 06 Part 2: Multi-Cloud, Network Segmentation & Research Paper Overview | Texas Wesleyan University"]

---

### Section 1: Multi-Cloud Networking

[00:00 – 05:30]
[SHOW DIAGRAM: Multi-cloud — enterprise on-prem connecting to AWS, Azure, and GCP simultaneously via transit hub]

[Alt-text: A hub-and-spoke diagram. In the center is a box labeled "Transit Network (AWS Transit Gateway / Azure Virtual WAN)." Arrows connect to: "AWS VPC-A," "AWS VPC-B," "Azure VNET-1," "GCP VPC," and "On-Premise DC." Each connection is labeled with the appropriate service name.]

Many enterprises use two or more cloud providers simultaneously — a strategy called **multi-cloud**. Reasons include:
- Different cloud providers offer different specialized services (e.g., AWS for general workloads, GCP for BigQuery analytics, Azure for Microsoft 365 integration).
- Avoiding vendor lock-in.
- Regulatory requirements specifying data must not reside in a single provider.

**Challenges of Multi-Cloud Networking:**
1. **Connectivity:** Each cloud has its own VPC/VNET with different IP address ranges. Connecting them requires either:
   - **Cloud-to-Cloud VPN:** IPsec tunnels between AWS VGW and Azure VPN Gateway.
   - **Third-party transit network:** A commercial multi-cloud networking platform (e.g., Megaport, Equinix Fabric) that connects to multiple providers.
   - **SD-WAN overlay:** SD-WAN vEdge devices deployed in each cloud, connected by OMP.

2. **IP Address Management:** With multiple VPCs and VNETs, IP address space must be carefully planned to avoid overlap. A global IPAM (IP Address Management) system is essential.

3. **Security Policy Consistency:** Security Groups and NSGs (Network Security Groups — Azure) are provider-specific. A change made in one cloud's security policy is not automatically reflected in another. Cloud Security Posture Management (CSPM) tools help enforce consistent policies.

**AWS Transit Gateway:**
AWS Transit Gateway is a regional hub that connects multiple VPCs and on-premise networks through a single managed routing hub. Instead of creating a mesh of VPC peering connections (which doesn't scale), all VPCs connect to the Transit Gateway, which handles routing between them.

- Supports up to 5,000 VPC attachments.
- Supports Direct Connect and VPN attachments for hybrid connectivity.
- Enables route table segmentation — different VPCs can be in different "route domains," preventing lateral movement between sensitive workloads.

**VPC Peering vs. Transit Gateway:**
| Feature | VPC Peering | Transit Gateway |
|---|---|---|
| Connection type | Direct 1:1 between 2 VPCs | Hub-and-spoke — all VPCs connect to TGW |
| Scale | Max ~125 peering connections | Thousands of attachments |
| Transitivity | ❌ Not transitive (A↔B, B↔C ≠ A↔C) | ✅ Transitive routing via TGW route tables |
| Cost | No hourly charge | Hourly charge + data processing fee |
| Use case | Simple, few VPCs | Complex, many VPCs, hybrid |

---

### Section 2: Network Segmentation in Hybrid Environments

[05:30 – 10:30]
[SHOW DIAGRAM: Microsegmentation — Group-Based Policy tagging and enforcement across on-prem, cloud, and remote users]

**Macro vs. Microsegmentation:**
- **Macrosegmentation:** Traditional VLAN/VRF-based segmentation — entire subnets or VLANs are separated. A user in VLAN 10 cannot reach VLAN 20 without going through a firewall/router. Coarse-grained.
- **Microsegmentation:** Policy is enforced at the workload level — individual VMs or containers can have their own security policy even if they share the same IP subnet. Software-defined, fine-grained.

**Cisco TrustSec — Group-Based Policy (GBP):**
In the campus (SD-Access), TrustSec assigns a **Security Group Tag (SGT)** to each endpoint based on its identity (user role, device type, authentication state). SGT tags are propagated across the network and enforced at policy enforcement points — routers, switches, firewalls — without requiring IP address-based ACLs.

Example: A contractor's laptop (SGT 20) connecting to the network can only reach internet breakout resources (SGT 10). An employee laptop (SGT 30) can reach corporate applications (SGT 40). This policy travels with the user regardless of which physical port, VLAN, or location they connect from.

**Cloud Workload Segmentation:**
In AWS, the equivalent of microsegmentation is achieved by combining:
- **Security Groups per instance** (stateful, instance-level firewall).
- **VPC Endpoints** — keep traffic to AWS services on the private network (no internet exposure).
- **AWS Network Firewall** — stateful inspection and IDS/IPS for VPC traffic.
- **Private Link** — expose services to other VPCs without routing through the internet.

---

### Section 3: IPv6 in Enterprise and Cloud Networks

[10:30 – 13:00]
[SHOW SLIDE: IPv4 exhaustion → dual-stack transition → IPv6-only cloud paths]

IPv6 adoption is accelerating. All major cloud providers support IPv6, and IPv6-only subnets are increasingly common for new cloud deployments. Key points for the CCNP exam and enterprise design:

**Dual-Stack Design:**
Most current enterprise networks run **dual-stack** — both IPv4 and IPv6 simultaneously. Devices have both an IPv4 and IPv6 address; applications that support IPv6 prefer it, others fall back to IPv4.

**IPv6 Addressing in Enterprise:**
- **Global Unicast (GUA):** Public IPv6 addresses, routable on the internet (equivalent to public IPv4). Prefix: 2000::/3.
- **Link-Local (LLA):** Automatically assigned on every IPv6-enabled interface, used for on-link routing. Prefix: FE80::/10. Never routed beyond the local segment.
- **Unique Local Address (ULA):** Similar to RFC 1918 private space. Prefix: FC00::/7. Not routable on the internet.

**SLAAC — Stateless Address Autoconfiguration:**
IPv6 devices can configure their own GUA without a DHCPv6 server using SLAAC — the router sends a **Router Advertisement (RA)** containing the network prefix, and the device appends its own 64-bit Interface ID (derived from MAC via EUI-64 or randomly generated).

**OSPFv3 for IPv6:**
OSPFv3 is the IPv6 version of OSPF (though modern IOS uses "OSPF with address-family ipv6" in named mode rather than the separate `ipv6 router ospf` process). Configuration parallels OSPFv2.

---

### Section 4: Research Paper Overview

[13:00 – 15:00]
[SHOW SLIDE: Research Paper requirements — 5–7 pages, due December 1]

Your **Graduate Research Paper** is due together with the Module 06 assignments on **December 1, 2026 at 11:59 PM CST**.

**Requirements Recap:**
- **Length:** 5–7 pages, double-spaced, 12pt font (not counting title page and references).
- **Topic:** An advanced networking topic of your choice (approved by the instructor no later than November 13).
- **References:** Minimum 5 credible technical sources.
- **Citation Format:** APA or IEEE (consistent throughout).
- **Thesis:** Your paper must advance a clear, original analytical argument — not just summarize sources.

**If you have not yet submitted your topic proposal**, email me immediately at nash@txwes.edu. Topic approval is required before you can submit the paper.

**Reminder of suggested topics (Module 06 is an excellent source):**
- SD-WAN deployment strategy: MPLS replacement or complement?
- AWS Transit Gateway vs. traditional hub-and-spoke WAN design
- RPKI (Resource Public Key Infrastructure) and BGP route origin validation
- IPv6 enterprise migration planning: challenges and best practices
- Network automation maturity model: from CLI to Intent-Based Networking

**Module 06 assignments due: Tuesday, December 1, 2026 at 11:59 PM CST**
*(Extended from Sunday, November 30 due to Thanksgiving Break November 26–28)*

---
*End of Part 2 — Module 06*
