# Video Script: Module 06 – Cloud Networking & Hybrid Architectures

## CSC-6361 Advanced Computer Networks | Graduate Level

## Part 2 of 2 | Estimated Duration: 15–18 minutes

## Week 6: November 23 – December 1, 2026 (Extended due to Thanksgiving)

## Due: Tuesday, December 1, 2026 at 11:59 PM CST

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CSC-6361 Advanced Computer Networks | Module 06 Part 2: AWS Direct Connect, Azure ExpressRoute & Hybrid Design Patterns | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Welcome to Part 2

[00:00 – 01:30]
[SHOW SLIDE: Professor Nash on camera, hybrid cloud diagram visible behind.]

Welcome back. In Part 1 we built the foundation: SD-WAN architecture with the four Viptela components, OMP protocol, centralized control vs. data policies, VXLAN encapsulation, and EVPN as the BGP control plane.

In Part 2 we move to the cloud provider side of hybrid architecture. Specifically: **AWS Direct Connect** — including Virtual Interface types and Link Aggregation Groups — and **Azure ExpressRoute** — circuits, peering types, and route filters. We will then examine how enterprises design hybrid connectivity for resiliency: active/active vs. active/standby patterns. We close with how **BGP communities** are used to engineer traffic flows across cloud provider connections.

These topics appear directly on the CCNP ENCOR 350-401 exam in the Infrastructure domain and are essential knowledge for any network engineer working in a hybrid enterprise environment today.

---

### Section 2: AWS Direct Connect — Architecture and VIF Types

[01:30 – 07:00]
[SHOW DIAGRAM: AWS Direct Connect architecture — enterprise router at colocation facility connecting to AWS Direct Connect location, then to AWS backbone, then to VPC Virtual Private Gateway and Transit Gateway]

[Alt-text: A diagram showing three zones from left to right. Zone 1 (left): "Enterprise Network — on-premise router connected to enterprise WAN." Zone 2 (center): "Colocation/Carrier Facility — cross-connect between enterprise router and AWS Direct Connect router. Labeled: 'AWS Direct Connect Location (e.g., Equinix Dallas).' A DX router icon is shown." Zone 3 (right): "AWS Region — Virtual Private Gateway attached to VPC-A and VPC-B. Transit Gateway attached to multiple VPCs. Both connected to the DX router in Zone 2 via Virtual Interfaces (VIFs)."]

#### What is AWS Direct Connect?

AWS Direct Connect (DX) is a dedicated private network connection between your enterprise and AWS infrastructure. Instead of routing traffic over the public internet, Direct Connect traffic travels over a private fiber circuit — typically provisioned through a colocation facility (such as Equinix) where your equipment and the AWS Direct Connect router are co-located and connected via a cross-connect.

Key capacity options:

- **1 Gbps and 10 Gbps:** Dedicated connections — a full physical port at the DX location is allocated to your account.
- **50 Mbps to 500 Mbps (Hosted Connections):** Ordered through an AWS Direct Connect Partner — shared physical port, logical capacity guarantee.

The circuit itself is Layer 1 (fiber) and Layer 2 (802.1Q VLAN). All routing is BGP — you establish BGP sessions over the Direct Connect circuit using Virtual Interfaces.

#### Virtual Interface (VIF) Types

This is a critical exam topic. AWS Direct Connect uses three types of Virtual Interfaces:

| VIF Type | Connects To | BGP ASN Required | Use Case |
|---|---|---|---|
| **Private VIF** | A single VPC via Virtual Private Gateway (VGW) | Your private ASN | Connect on-premise to a specific VPC |
| **Public VIF** | AWS public services (S3, DynamoDB, public AWS IPs) | Your public ASN | Access AWS public endpoints without internet |
| **Transit VIF** | AWS Transit Gateway (TGW) | Your private ASN | Connect to multiple VPCs via a single VIF |

> **Graduate Design Note:** For most enterprise deployments, **Transit VIF + Transit Gateway** is the preferred architecture. A single Transit VIF connects to Transit Gateway, which then routes to all attached VPCs. This eliminates the need to create a separate Private VIF for each VPC — scalability advantage as VPC count grows.

#### Private VIF — Routing Details

When you establish a Private VIF to a VPC's Virtual Private Gateway:

- BGP session is established between your on-premise router and the VGW.
- Your router advertises your on-premise prefixes to AWS.
- AWS advertises the VPC CIDR block(s) back to your router.
- Maximum prefixes you can advertise: **100 routes** (soft limit, can be raised via AWS support).

#### Public VIF — Routing Details

A Public VIF is used to access AWS public service endpoints (e.g., S3, CloudFront, SQS) via Direct Connect instead of the internet. You advertise your public IP prefixes to AWS; AWS advertises all AWS public IP ranges to you (this is a very large route table — filter carefully).

> **Key Exam Point:** A Public VIF does NOT give you access to your VPC. It gives you access to AWS public services. To access resources inside a VPC, you need a Private VIF or Transit VIF.

#### Link Aggregation Groups (LAG)

A LAG bundles multiple Direct Connect connections at the same DX location into a single logical link:

- All physical connections in a LAG must be the same speed (e.g., all 1 Gbps or all 10 Gbps).
- LACP (Link Aggregation Control Protocol) is used for LAG negotiation.
- A LAG provides both **increased bandwidth** and **connection redundancy** — if one physical link fails, the LAG continues with the remaining links.
- Maximum 4 connections per LAG.

---

### Section 3: Azure ExpressRoute — Architecture and Peering Types

[07:00 – 12:00]
[SHOW DIAGRAM: Azure ExpressRoute architecture — enterprise network connecting through ExpressRoute circuit to Microsoft Edge, then to Azure Virtual Network and Microsoft 365 services]

[Alt-text: A diagram showing "Enterprise Network" on the left connected via "ExpressRoute Circuit (provider-managed)" to a central "Microsoft Enterprise Edge (MSEE) Router." From the MSEE, two paths go right: (1) "Private Peering — Azure Virtual Networks (VNets)" and (2) "Microsoft Peering — Microsoft 365, Azure Public Services." A third element "ExpressRoute Global Reach" is shown connecting two enterprise sites to each other through the MSEE.]

#### What is Azure ExpressRoute?

Azure ExpressRoute is Microsoft's dedicated private connectivity product — functionally equivalent to AWS Direct Connect. An ExpressRoute Circuit is provisioned through one of Microsoft's connectivity partners (AT&T, Equinix, Megaport, and others) and provides a private, reliable path to Azure and Microsoft 365 services.

ExpressRoute circuit speeds range from **50 Mbps to 100 Gbps**, depending on the provider and tier.

The ExpressRoute architecture uses **two physical connections** (primary and secondary) by default — this is not optional redundancy, it is built into the circuit specification. Both connections terminate at Microsoft Enterprise Edge (MSEE) routers in different physical locations for maximum resilience.

#### ExpressRoute Peering Types

| Peering Type | Connects To | BGP Community Support | Use Case |
|---|---|---|---|
| **Private Peering** | Azure Virtual Networks (VNets) via ExpressRoute Gateway | No BGP community filtering | Connect on-premise to Azure VNets |
| **Microsoft Peering** | Azure public services + Microsoft 365 | Yes — route filters required | Access Office 365, Azure Storage, etc. |

> **Azure vs. AWS Terminology Note:** Azure "Private Peering" is the functional equivalent of AWS "Private VIF." Azure "Microsoft Peering" covers what AWS handles with "Public VIF" — but with a key difference: Microsoft Peering requires explicit **route filters** to control which services' prefixes are received. Without a route filter, no routes are advertised over Microsoft Peering.

#### Route Filters on Microsoft Peering

Route filters are Azure resources that specify which BGP communities you want to receive over Microsoft Peering. Each Azure service region and Microsoft 365 service has a BGP community value. Example:

- Azure East US public services: BGP community `12076:51004`
- Exchange Online (Microsoft 365): BGP community `12076:5010`

You attach a route filter to the Microsoft Peering, selecting only the community values for services you need. This prevents receiving the full Microsoft BGP table (which is enormous) when you only need Office 365 reachability.

#### ExpressRoute Global Reach

ExpressRoute Global Reach is a feature that connects two on-premise networks to each other through the Microsoft backbone — without going through Azure VNets. If your company has offices in Dallas and London, both with ExpressRoute circuits, Global Reach creates a direct path between Dallas and London through Microsoft's network. This is a WAN optimization capability, not just a cloud connectivity feature.

#### ExpressRoute vs. Direct Connect — Comparison

| Feature | AWS Direct Connect | Azure ExpressRoute |
|---|---|---|
| Dedicated circuit speeds | 1 Gbps, 10 Gbps (hosted: 50M–500M) | 50 Mbps to 100 Gbps |
| Redundancy model | Manual — you provision two circuits | Built-in dual connection (primary + secondary) |
| Transit connectivity | Transit VIF + Transit Gateway | ExpressRoute Global Reach |
| BGP community filtering | Not on Private VIF | Required on Microsoft Peering |
| Public service access | Public VIF | Microsoft Peering (with route filters) |

---

### Section 4: Hybrid Connectivity Design Patterns

[12:00 – 15:30]
[SHOW DIAGRAM: Two patterns side by side — active/active (both Direct Connect circuits carry traffic) and active/standby (primary circuit carries all traffic, standby sits idle until failover)]

#### Active/Active Hybrid Design

In an active/active design, two or more paths to the cloud are used simultaneously:

- Two Direct Connect circuits (or a LAG) with BGP load balancing.
- Both circuits advertise the same prefixes to AWS; AWS distributes outbound traffic across both.
- On the enterprise side, ECMP (Equal-Cost Multi-Path) routing distributes inbound traffic.

Benefits:

- Full bandwidth utilization of both circuits.
- Seamless failover — if one circuit fails, traffic immediately shifts to the surviving circuit with no BGP reconvergence delay (BFD on Direct Connect detects failures in milliseconds).

Consideration:

- Requires careful BGP tuning to prevent asymmetric routing (inbound on Circuit A, outbound on Circuit B) if the circuits have different capacities.

#### Active/Standby Hybrid Design

In an active/standby design, one path carries all traffic and the other sits in cold standby:

- Primary: Direct Connect circuit with BGP local preference 200 (preferred).
- Standby: IPsec VPN over internet with BGP local preference 100 (backup).
- When Direct Connect fails, BGP withdraws the preferred routes and traffic shifts to the VPN.

BGP tuning mechanisms for active/standby:

- **AS Path Prepending:** Advertise your prefixes to AWS with extra AS hops on the backup path — AWS prefers the shorter path (Direct Connect) and only uses the VPN when the DX path disappears.
- **Local Preference:** Set higher local preference on routes received via Direct Connect on your enterprise BGP router — your traffic prefers DX outbound.
- **MED (Multi-Exit Discriminator):** Used when advertising the same prefix via two AWS Direct Connect locations in different regions; lower MED = preferred.

#### BGP Communities for Cloud Traffic Engineering

BGP communities are 32-bit values (AS:value format) attached to route advertisements. Both AWS and Azure use well-known communities to signal routing preferences.

AWS Direct Connect BGP communities:

| Community Value | Meaning |
|---|---|
| `7224:9100` | Local AWS Region only (do not propagate to other regions) |
| `7224:9200` | Prefer this path for all AWS traffic in the continent |
| `7224:9300` | Global — propagate to all AWS regions worldwide |

You set these communities on routes you advertise to AWS to control how AWS distributes those prefixes internally. Conversely, AWS tags the routes it advertises to you with communities indicating the originating region — you can use these to set different local preferences for traffic from different AWS regions.

Azure ExpressRoute BGP communities (inbound, from Microsoft):

- Each Azure region has a unique BGP community value in the `12076:5xxxx` range.
- You can use these in route-map `match community` statements to set local preferences per region — for example, prefer the Dallas ExpressRoute for East US traffic and the New York ExpressRoute for West Europe traffic.

---

### Section 5: Part 2 Summary and Module Wrap-Up

[15:30 – 17:30]
[SHOW SLIDE: Module 06 complete summary — SD-WAN + VXLAN/EVPN + cloud connectivity]

In Part 2 you have learned:

- **AWS Direct Connect:** VIF types (Private, Public, Transit), LAG aggregation, BGP routing model, and the Transit VIF + Transit Gateway enterprise pattern.
- **Azure ExpressRoute:** Circuit architecture (dual connections), Private Peering vs. Microsoft Peering, route filters as a requirement for Microsoft Peering, and Global Reach for site-to-site connectivity.
- **Hybrid design patterns:** Active/active (ECMP, full bandwidth utilization) vs. active/standby (AS path prepending, local preference, MED for BGP failover tuning).
- **BGP communities for cloud TE:** AWS 7224:9xxx communities for regional propagation control; Azure 12076:5xxxx regional communities for local preference tuning.

Combined with Part 1 (SD-WAN, VXLAN, EVPN), you now have a complete picture of how modern enterprises connect their campus networks, data centers, and cloud workloads into a unified hybrid architecture. This is the network engineer's domain in 2026 and beyond.

**Reminder:** All Module 06 deliverables — Lab, Discussion, and Research Paper — are due **Tuesday, December 1, 2026 at 11:59 PM CST**.

---

### Additional Resources

- AWS Direct Connect User Guide: [https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
- Azure ExpressRoute Documentation: [https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction](https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction)
- Cisco SD-WAN Cloud OnRamp Configuration Guide: [https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/cloudonramp/ios-xe-17/cloud-onramp-book-xe.html](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/cloudonramp/ios-xe-17/cloud-onramp-book-xe.html)
- IETF RFC 4271 — BGP-4: [https://datatracker.ietf.org/doc/html/rfc4271](https://datatracker.ietf.org/doc/html/rfc4271)

---

End of Part 2 — Module 06
