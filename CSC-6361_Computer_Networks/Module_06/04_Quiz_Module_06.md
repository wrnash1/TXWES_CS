# Quiz: Module 06 – Cloud Networking & Hybrid Architectures
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: December 1, 2026 (Extended — Thanksgiving Week) at 11:59 PM CST

---

> **Instructor Note:** Enter these questions into Canvas as a timed Quiz (30 minutes, 1 attempt, no backtracking). Set questions to randomize order. All questions are CCNP Enterprise–style scenario questions.

---

### Question 1 (Multiple Choice — 10 pts)
A network engineer is designing a Cisco SD-WAN deployment and must explain the roles of the four control-plane components to the project team. Which statement correctly describes the role of the **vSmart controller**?

- A) vSmart is the management plane — it provides the centralized GUI for policy configuration and device onboarding. ❌
- B) vSmart is the orchestration plane — it authenticates all SD-WAN devices and helps them discover each other during bring-up. ❌
- C) vSmart is the control plane — it distributes routing information and centralized policies (data policies, application-aware routing policies) to all vEdge/cEdge devices via OMP (Overlay Management Protocol). ✅
- D) vSmart is the data plane — it forwards encrypted user traffic across the WAN fabric using IPsec tunnels. ❌

**Answer:** C — In the Cisco SD-WAN architecture, the four components are: **vManage** (management plane — GUI, config, monitoring), **vSmart** (control plane — distributes routes and policies via OMP), **vBond** (orchestration plane — authenticates devices and facilitates NAT traversal), and **vEdge/cEdge** (data plane — the physical or virtual routers that forward actual traffic). The vSmart controller is analogous to a route reflector: all vEdge devices peer with vSmart over OMP, and vSmart propagates TLOCs (Transport Locators) and policies. Devices do not peer directly with each other in the control plane.

**Distractor Analysis:**
- A: vManage is the management plane GUI — not vSmart.
- B: vBond is the orchestration/bootstrapping component that handles initial device authentication and helps devices discover vManage and vSmart.
- D: vEdge and cEdge routers are the data plane devices — vSmart never touches user traffic directly.

---

### Question 2 (Multiple Choice — 10 pts)
An enterprise is connecting its on-premises data center to AWS using **AWS Direct Connect**. The architect needs to choose between a **Private Virtual Interface (Private VIF)** and a **Transit Virtual Interface (Transit VIF)**. The enterprise has 15 VPCs in AWS across multiple regions, connected via AWS Transit Gateway. Which VIF type is correct, and why?

- A) Private VIF — it connects directly to multiple VPCs simultaneously with no bandwidth limit. ❌
- B) Transit VIF — it connects to an AWS Transit Gateway, which then routes traffic to all 15 VPCs through a single Direct Connect connection, providing a scalable hub-and-spoke model. ✅
- C) Public VIF — it provides the lowest latency because it bypasses AWS VPC routing entirely. ❌
- D) Hosted VIF — it is the only VIF type that supports multiple VPCs. ❌

**Answer:** B — A **Private VIF** connects a Direct Connect circuit directly to a single VPC (via a Virtual Private Gateway). When an enterprise needs to reach many VPCs, creating a separate Private VIF per VPC is operationally impractical. A **Transit VIF** connects to an AWS Transit Gateway, which can peer with hundreds of VPCs, on-premises networks, and VPN connections — making it the correct architecture for multi-VPC enterprise deployments. This matches the AWS "Transit Gateway as a cloud router" design pattern.

**Distractor Analysis:**
- A: Private VIF connects to one VPC via one Virtual Private Gateway — it does not scale to 15 VPCs without 15 separate VIFs.
- C: Public VIF is used to access AWS public services (S3, DynamoDB) over Direct Connect, not VPC private resources.
- D: Hosted VIF is a capacity-sharing model (a partner shares their Direct Connect port with you) — it is not a type defined by routing destination.

---

### Question 3 (Multiple Choice — 10 pts)
A data center architect is designing a VXLAN fabric. A VTEP (VXLAN Tunnel Endpoint) on Leaf Switch 1 needs to encapsulate a frame from VLAN 10 (VNI 10010) and send it to a VTEP on Leaf Switch 3. Which statement correctly describes the VXLAN encapsulation added to the original Ethernet frame?

- A) VXLAN adds an 8-byte header containing the 24-bit VNI, which is encapsulated inside a UDP packet (destination port 4789) over an IP outer header. ✅
- B) VXLAN adds a 4-byte header containing the 12-bit VLAN ID and is carried over a GRE tunnel. ❌
- C) VXLAN replaces the inner Ethernet header with a 32-bit VNI and requires MPLS labels for transport. ❌
- D) VXLAN encapsulation adds only a 2-byte VNI tag, making it more efficient than 802.1Q VLAN tagging. ❌

**Answer:** A — VXLAN (RFC 7348) encapsulates Layer 2 Ethernet frames inside a UDP/IP packet. The encapsulation stack (from outer to inner) is: outer Ethernet header, outer IP header (VTEP-to-VTEP transport), UDP header (destination port 4789), 8-byte VXLAN header (containing the 24-bit VNI and reserved bits), and then the original inner Ethernet frame. The 24-bit VNI supports up to 16 million logical segments, far exceeding the 4,094-VLAN limit of 802.1Q — which is exactly why VXLAN was designed for multi-tenant data centers and cloud environments.

**Distractor Analysis:**
- B: VXLAN uses UDP, not GRE. GRE is used by NVGRE (Microsoft's competing overlay standard).
- C: VXLAN preserves the original inner Ethernet header completely — it adds headers around it. MPLS is not part of VXLAN.
- D: The VXLAN header is 8 bytes — significantly larger than 802.1Q's 4 bytes — but provides a 24-bit VNI versus 12-bit VLAN ID.

---

### Question 4 (Multiple Choice — 10 pts)
In a Cisco SD-Access fabric, what is the role of the **Control Plane Node** and the **Border Node**, and how do they interact?

- A) The Control Plane Node routes user traffic; the Border Node applies SGT (Security Group Tag) policies. ❌
- B) The Control Plane Node runs LISP map-server/map-resolver to maintain the endpoint-to-RLOC mapping database; the Border Node connects the SD-Access fabric to external networks (WAN, internet, data center) and handles LISP map-request forwarding for off-fabric destinations. ✅
- C) The Control Plane Node is the DNA Center server; the Border Node is the ISE policy enforcement point. ❌
- D) The Control Plane Node runs spanning tree root for all fabric VLANs; the Border Node provides the default gateway for all endpoints. ❌

**Answer:** B — In SD-Access, the underlay is IP-routed and the overlay uses VXLAN with LISP for endpoint mobility. The **Control Plane Node** runs LISP map-server and map-resolver: when a fabric edge node needs to reach an endpoint, it sends a LISP map-request to the Control Plane Node, which looks up the endpoint-to-RLOC (Routing Locator, i.e., fabric node IP) mapping and returns it. The **Border Node** is the fabric's gateway to the rest of the network — it connects to WAN, internet, traditional campus, or data center. Fabric nodes that need to reach external (off-fabric) destinations send map-requests to the Border Node, which forwards them externally or resolves via BGP.

**Distractor Analysis:**
- A: Both nodes participate in control plane functions — neither is a pure data-plane forwarder.
- C: DNA Center is the management/orchestration platform (analogous to vManage in SD-WAN), and ISE is the policy/identity engine — neither is a Border or Control Plane Node role.
- D: Spanning tree is eliminated in SD-Access fabric — routing replaces L2 spanning tree. Default gateways are anycast SVIs on all fabric edge nodes.

---

### Question 5 (Multiple Choice — 10 pts)
An enterprise migrates from traditional MPLS WAN to Cisco SD-WAN. After migration, a branch router (cEdge) has three WAN transports: MPLS, broadband internet, and LTE. The SD-WAN policy is configured to send VoIP traffic (DSCP EF) over MPLS when available, and fall over to broadband if MPLS latency exceeds 150ms. What SD-WAN feature implements this behavior?

- A) QoS policy-map applied outbound on the MPLS interface. ❌
- B) Application-Aware Routing (AAR) policy — it continuously measures per-transport SLA metrics (loss, latency, jitter) and automatically steers application traffic to the transport that meets the configured SLA threshold. ✅
- C) BGP communities applied to VoIP routes to prefer MPLS next-hop. ❌
- D) DSCP-based interface queuing on the cEdge WAN interfaces. ❌

**Answer:** B — **Application-Aware Routing (AAR)** is a core SD-WAN feature that measures real-time SLA metrics (packet loss, latency, jitter) on every active BFD session between cEdge routers. A centralized data policy on vSmart defines: "For traffic matching VoIP (DSCP EF or application group), use MPLS if MPLS latency < 150ms; fall back to broadband if MPLS exceeds threshold." The cEdge continuously evaluates BFD metrics against the SLA thresholds and steers traffic accordingly — this happens automatically without operator intervention, which is a fundamental capability that traditional MPLS cannot provide.

**Distractor Analysis:**
- A: Traditional QoS policy-maps can prioritize traffic within a single interface queue but cannot redirect traffic between different WAN transports based on real-time SLA conditions.
- C: BGP communities can influence route preference but require manual reconfiguration to change — they have no awareness of real-time latency or jitter.
- D: DSCP queuing only manages relative priority within a single link — it cannot switch traffic to a different physical transport.

---

### Question 6 (Scenario — 10 pts)
A network engineer runs the following on a leaf switch in a VXLAN/EVPN data center fabric:
```
show bgp l2vpn evpn route-type 2
```
The output shows MAC/IP advertisement routes from remote VTEPs. The engineer then runs:
```
show nve peers
```
And sees the remote VTEP is listed with state `UP`. However, a VM on this leaf cannot ping a VM on the remote leaf in the same VNI. What is the most likely cause?

- A) The VNI is misconfigured — VNI numbers must match on both leafs. ❌
- B) EVPN Type-2 routes are present but the NVE interface is missing a `member vni [VNI]` statement for that specific VNI, so frames are not being encapsulated with the correct VNI despite the BGP adjacency being established. ✅
- C) BFD is not configured between the VTEPs — without BFD, VXLAN tunnels do not forward traffic. ❌
- D) The BGP EVPN session requires `next-hop-self` on all spine switches before VMs can communicate. ❌

**Answer:** B — In Cisco NX-OS VXLAN/EVPN, the NVE (Network Virtual Edge) interface must explicitly list each VNI it participates in under `member vni [VNI]`. It is possible to have the BGP EVPN session established and Type-2 routes exchanged (confirming the control plane is working) while the data plane is broken because the NVE interface is not configured to encapsulate/decapsulate that specific VNI. This is a common misconfiguration: the BGP control plane and the NVE data plane configuration are independent — both must be correct for end-to-end connectivity.

**Distractor Analysis:**
- A: VNI mismatch would prevent route exchange entirely, and we can see Type-2 routes are present — so the VNI numbers are matching in BGP.
- C: BFD is not required for VXLAN data plane forwarding — it is optional and used only for faster failure detection.
- D: In a spine-leaf EVPN fabric, `next-hop-self` may or may not be needed depending on the design, but its absence would affect route reachability in BGP, not the NVE data plane encapsulation.

---

### Question 7 (Multiple Choice — 10 pts)
What is the fundamental relationship between the **underlay** and **overlay** networks in a VXLAN SD-Access or data center fabric?

- A) The underlay is a Layer 2 switched network; the overlay is a Layer 3 routed network that tunnels over it. ❌
- B) The underlay is a routed IP network that provides reachability between VTEPs/fabric nodes; the overlay is a logical Layer 2 or Layer 3 network tunneled over the underlay using VXLAN encapsulation — endpoint communication occurs in the overlay while VTEP-to-VTEP transport uses the underlay. ✅
- C) The underlay and overlay are identical — VXLAN simply adds an extra header to the same packets for tracking purposes. ❌
- D) The overlay always uses IPv6 while the underlay uses IPv4 — this is the defining characteristic of VXLAN. ❌

**Answer:** B — The underlay is the physical IP network connecting all switches, routers, or VTEPs. It only needs to route VTEP loopback IP addresses between fabric nodes — it has no knowledge of VMs, VLANs, or tenants. The overlay creates logical networks on top of the underlay: VXLAN-encapsulated frames travel from source VTEP to destination VTEP using underlay IP routing, while the enclosed payload carries the original endpoint's MAC/IP traffic in its logical L2 segment (identified by VNI). This separation means the overlay can span any physical topology, support VM mobility, and provide multi-tenancy without any underlay changes.

**Distractor Analysis:**
- A: In modern data center fabrics (and SD-Access), the underlay is a routed Layer 3 network — not Layer 2 switching.
- C: The underlay and overlay are distinct logical layers — the underlay knows nothing about VXLAN VNIs, tenants, or overlay topologies.
- D: VXLAN works over both IPv4 and IPv6 underlay; the choice of underlay IP version is a design decision, not a VXLAN requirement.

---

### Question 8 (Scenario — 10 pts)
An enterprise is evaluating Azure ExpressRoute for connecting its on-premises data center to Azure. The network architect explains that ExpressRoute uses **BGP** as the routing protocol between the on-premises edge router and the Microsoft Enterprise Edge (MSEE) routers. A junior engineer asks why a static default route pointing to Azure would not work instead of BGP. What is the most technically precise reason BGP is required?

- A) Azure ExpressRoute circuits only accept TCP-based routing protocols — static routes use UDP and are therefore blocked. ❌
- B) BGP is required because Microsoft dynamically advertises Azure service prefixes (Virtual Network address spaces, Azure PaaS prefixes) to the customer edge router — these prefixes change as VNets are added, peered, or removed, and static routes cannot dynamically track these changes. Additionally, the customer must advertise their on-premises prefixes to Azure via BGP for return routing. ✅
- C) Azure requires BGP AS path prepending to prefer ExpressRoute over VPN Gateway routes — static routes have no AS path attribute. ❌
- D) Static routes are blocked by Microsoft's SLA policy — only dynamic routing protocols are permitted on ExpressRoute circuits. ❌

**Answer:** B — ExpressRoute mandates BGP (both eBGP and optionally iBGP) because: (1) Microsoft dynamically announces Azure prefixes over the circuit — the set of prefixes changes as the customer provisions new VNets, configures VNet peering, or uses Azure services; (2) the customer must announce their on-premises CIDR blocks to Microsoft via BGP so Azure knows how to route return traffic back to the data center. A static route on the customer edge could only point at a Microsoft IP but could never automatically learn which Azure VNet prefixes exist or change as the Azure environment evolves. BGP also enables route filtering (prefix lists, route maps) to control precisely which prefixes are exchanged in each direction.

**Distractor Analysis:**
- A: BGP uses TCP port 179 — this is correct. But static routes are not "UDP-based" — they are simply local router configuration with no protocol at all.
- C: AS path prepending is a BGP technique for influencing inbound traffic — while useful, it is not the reason BGP is required over static routes.
- D: While true that Microsoft requires BGP, the technical reason (dynamic prefix advertisement) is more precise than a policy statement.

---

### Question 9 (Short Answer — 10 pts)
Explain what **Network Function Virtualization (NFV)** is, how it differs from a traditional hardware-based network appliance approach, and describe two specific network functions that are commonly virtualized in enterprise or service provider networks. Include the concept of a **VNF (Virtualized Network Function)** and the role of an **NFV Infrastructure (NFVI)** platform. (3–4 sentences)

**Model Answer:** **NFV** is the practice of decoupling network functions (firewall, load balancer, WAN optimization, IDS/IPS, router) from proprietary hardware appliances and implementing them as software — called **VNFs (Virtualized Network Functions)** — running on commodity x86 servers, virtual machines, or containers. This contrasts with the traditional model where each network function requires a dedicated hardware appliance (a physical Cisco ASA for firewall, a physical F5 BIG-IP for load balancing), which is expensive to procure, slow to deploy, and difficult to scale. The **NFVI (NFV Infrastructure)** is the compute, storage, and network resources (hypervisor, OpenStack, or Kubernetes) that host and interconnect VNFs — providing the platform on which VNFs run without being tied to specific hardware. Common enterprise VNFs include **virtual firewalls** (Cisco FTDv, Palo Alto VM-Series) that protect cloud workloads without requiring physical appliance insertion in traffic paths, and **virtual WAN routers/SD-WAN edges** (Cisco CSR 1000v, vEdge cloud) that allow branch routing and SD-WAN functionality to run as VMs in a cloud or hosted data center rather than as physical hardware at branch sites.

---

### Question 10 (Short Answer — 10 pts)
A hybrid cloud architect must decide how to route traffic between an on-premises enterprise network (10.0.0.0/8) and an AWS VPC (172.31.0.0/16). Three options are proposed: (1) AWS Site-to-Site VPN over the internet, (2) AWS Direct Connect private VIF, (3) AWS Direct Connect + VPN (encrypted Direct Connect). Compare these three options in terms of **bandwidth, latency, security, and cost**, and recommend which option is best for a financial services enterprise that transfers 5 TB of sensitive data per day and requires consistent sub-10ms latency. (4–5 sentences)

**Model Answer:** **AWS Site-to-Site VPN** uses IPsec over the public internet — it provides encryption but is subject to internet latency variability (typically 20–100ms depending on geography and congestion) and maximum throughput of ~1.25 Gbps per VPN tunnel; it is the lowest-cost option and is suitable for small data volumes or secondary/backup connectivity. **AWS Direct Connect** (private VIF) provides a dedicated physical circuit from the enterprise to AWS with consistent sub-10ms latency, bandwidth options from 50 Mbps to 100 Gbps, and no public internet traversal — however, it does not encrypt traffic in transit, which is a compliance concern for financial services data. **AWS Direct Connect + VPN** (MACsec at Layer 2 or IPsec overlay on top of Direct Connect) combines the consistent latency and dedicated bandwidth of Direct Connect with IPsec encryption — this is the recommended option for a financial services enterprise transferring 5 TB/day because it satisfies both the latency requirement (sub-10ms on the private circuit) and the security requirement (encrypted in transit for regulatory compliance such as PCI-DSS or SOX). The higher cost of Direct Connect plus encryption overhead is justified for this use case, and using a 10 Gbps Direct Connect circuit provides sufficient bandwidth for 5 TB/day (approximately 462 Mbps sustained average) with headroom for burst.
