# Video Script: Module 06 – Cloud Networking & Hybrid Architectures
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 1 of 2 | Estimated Duration: 15–18 minutes
## Week 6: November 23 – December 1, 2026 (Extended due to Thanksgiving)
## Due: Tuesday, December 1, 2026 at 11:59 PM CST
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 06 Part 1: Cloud Networking Fundamentals & Hybrid Architecture Design | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Welcome & Thanksgiving Notice

[00:00 – 01:30]
[SHOW SLIDE: Professor Nash on camera]

Welcome to Module 06 — our final full content module before the capstone. This module covers **Cloud Networking and Hybrid Architectures** — the area where enterprise networking and cloud infrastructure converge.

**Important Thanksgiving Notice:** This module opens Monday, November 23. Thanksgiving Break runs November 26–28. Because of this, I have extended the Module 06 deadline to **Tuesday, December 1 at 11:59 PM CST**. You have an extra two days compared to a normal module. Please use that time wisely — do not leave the research paper and discussion until after Thanksgiving.

Now let's dive in.

---

### Section 2: Cloud Networking Fundamentals

[01:30 – 06:00]
[SHOW DIAGRAM: Cloud network layers — physical infrastructure → VPC → subnets → security groups → route tables]

[Alt-text: A layered diagram labeled "AWS Virtual Private Cloud." From top to bottom: "Internet Gateway" connecting to the internet. Below that, two subnets labeled "Public Subnet (10.0.1.0/24)" and "Private Subnet (10.0.2.0/24)." Security Groups and Network ACLs shown as borders around resources in each subnet. A Route Table pointing the public subnet's default route to the Internet Gateway, and the private subnet's default route to a NAT Gateway in the public subnet.]

**The Cloud Networking Model:**
Cloud providers (AWS, Google Cloud, Azure) implement networking as software-defined virtual infrastructure. Understanding the cloud networking model is essential for modern enterprise architects — your on-premise skills map directly to cloud constructs.

**VPC — Virtual Private Cloud:**
A VPC is a logically isolated section of the cloud provider's infrastructure where you launch resources. It is the cloud equivalent of your campus network. You define the IP address space (e.g., 10.0.0.0/16), subnets, routing tables, and security controls.

**Subnets:**
- **Public Subnet:** Has a route to an Internet Gateway — resources here can be directly reached from the internet (with appropriate Security Group rules).
- **Private Subnet:** No direct route to the internet. Resources communicate outbound via a NAT Gateway in a public subnet.

**Route Tables:**
Every subnet has an associated route table. Route tables work similarly to static routes in IOS:
- `0.0.0.0/0 → Internet Gateway` (for public subnets)
- `0.0.0.0/0 → NAT Gateway` (for private subnets)
- `10.0.0.0/8 → Local` (for VPC-internal routing)

**Security Groups vs. Network ACLs:**
| Feature | Security Groups | Network ACLs |
|---|---|---|
| Applies to | Individual EC2 instances/ENIs | Subnet level |
| Statefulness | **Stateful** — return traffic automatically allowed | **Stateless** — must explicitly allow both directions |
| Default | All deny inbound, all allow outbound | All allow inbound and outbound |
| Rule evaluation | All rules evaluated | Rules evaluated in order (lowest rule number first) |
| Analogy | Host-based firewall | Subnet-level ACL |

> **Graduate Insight:** The combination of Security Groups (stateful, instance-level) and Network ACLs (stateless, subnet-level) provides defense-in-depth. The typical enterprise pattern: use Security Groups for application-level controls and Network ACLs for broad subnet-level controls (e.g., block all traffic from a known-malicious IP range at the subnet boundary).

---

### Section 3: Hybrid Cloud Connectivity

[06:00 – 11:00]
[SHOW DIAGRAM: Enterprise hybrid cloud — on-premise DC connected to AWS via Direct Connect + IPsec VPN backup]

[Alt-text: A diagram showing an on-premise data center on the left connected to an AWS VPC on the right via two paths: (1) A thick line labeled "AWS Direct Connect — 1 Gbps dedicated fiber circuit" and (2) a dotted line over a cloud labeled "IPsec VPN over Internet — backup path." Inside the AWS VPC, multiple EC2 instances in private subnets connect to on-premise applications through the hybrid connection.]

**Option 1: IPsec VPN to Cloud (Module 03 extended):**
The same GRE over IPsec or native IPsec site-to-site VPN techniques from Module 03 apply to cloud connectivity. AWS, Azure, and GCP all support site-to-site IPsec VPN:
- Configure a **Virtual Private Gateway** (VGW) on the AWS side.
- Configure a **Customer Gateway** pointing to your on-premise router's public IP.
- The IPsec tunnel is established between your edge router and the cloud VGW.
- Use BGP to exchange routes between on-premise and cloud (dynamic routing), or static routes.

*Pros:* Low cost (pay for the VPN gateway, not a dedicated circuit). *Cons:* Internet-dependent — performance and latency vary.

**Option 2: AWS Direct Connect / Azure ExpressRoute / Google Cloud Interconnect:**
A **dedicated private fiber circuit** from the enterprise directly into the cloud provider's infrastructure — bypassing the public internet entirely.

- **AWS Direct Connect:** 1 Gbps or 10 Gbps dedicated circuits, typically provisioned through a colocation/partner.
- **Azure ExpressRoute:** Similar to Direct Connect, with circuit speeds of 50 Mbps to 100 Gbps.
- **GCP Cloud Interconnect:** Dedicated or Partner Interconnect options.

Benefits of dedicated circuits over VPN:
- **Consistent performance:** No internet jitter or congestion.
- **Predictable latency:** Measured in microseconds for local regions.
- **Higher bandwidth:** Supports 10–100 Gbps vs. typical VPN performance limits.
- **No encryption overhead:** (though traffic should still be encrypted if data is sensitive — the dedicated circuit provides isolation but not encryption).

**Hybrid Routing Design:**
Most enterprise hybrid designs use Direct Connect as the **primary** path and IPsec VPN as the **backup** path:
- Configure BGP over Direct Connect with lower AS path length (preferred route).
- Configure IPsec VPN with a longer AS path or higher local preference (backup route).
- If Direct Connect fails, BGP withdraws the preferred routes and traffic automatically shifts to the VPN backup.

---

### Section 4: Cisco SD-Access (Campus Fabric)

[11:00 – 14:30]
[SHOW DIAGRAM: SD-Access fabric — underlay (physical OSPF routed network) + overlay (VXLAN fabric with LISP control plane)]

**Cisco SD-Access** is the campus network evolution that replaces traditional VLAN/STP campus designs with a fabric-based architecture:

**Underlay:** A traditional IP-routed network (OSPF is common) providing connectivity between all network devices. The underlay only needs to know how to forward IP packets.

**Overlay:** VXLAN (Virtual Extensible LAN) tunnels carry user traffic between fabric edge nodes. VXLAN encapsulates Layer 2 Ethernet frames inside UDP/IP — allowing L2 segments to stretch across the L3 underlay. This enables seamless wireless roaming across subnets and eliminates traditional STP.

**Control Plane — LISP (Locator/ID Separation Protocol):**
LISP separates the identity of an endpoint (its IP/MAC address) from its location (which edge node it connects to). When a device moves, LISP updates the mapping database — traffic is automatically redirected to the device's new location without STP topology changes or IP address changes.

**SD-Access Benefits vs. Traditional Campus:**
- No Spanning Tree between fabric nodes (underlay is L3 routed — no L2 loops).
- Macrosegmentation and microsegmentation via Group-Based Policy (Cisco TrustSec SGT tags).
- Consistent policy enforcement regardless of where a user connects (wired or wireless, any location).

---

### Section 5: Part 1 Summary

[14:30 – 16:00]
[SHOW SLIDE: Cloud networking concepts summary]

In Part 1 you learned:
- **VPC architecture** — subnets (public/private), route tables, Security Groups vs. Network ACLs.
- **Hybrid connectivity** — IPsec VPN vs. Direct Connect, BGP for hybrid routing.
- **SD-Access** — underlay/overlay architecture, VXLAN, LISP, and Group-Based Policy.

In Part 2 we cover **multi-cloud networking**, **network segmentation strategies**, and the **Research Paper overview** for Module 06.

---
*End of Part 1 — Module 06*
