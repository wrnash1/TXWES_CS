# Video Script: Module 12 — Network Virtualization and SDN (Part 2)

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

Estimated Runtime: 11–13 minutes

---

### [INTRO]

Welcome back. In Part 1 we covered hypervisors, virtual machines, virtual switches, NFV, and containers. In Part 2 we cover Software-Defined Networking — the architectural shift that separates how traffic is forwarded from how forwarding decisions are made. We also cover overlay networks, cloud networking concepts, and the terminology the Network+ exam tests in this domain.

---

### [SECTION 1: THE TRADITIONAL NETWORK PROBLEM]

[SHOW DIAGRAM: Traditional network — each switch and router has its own control plane and data plane, requiring manual configuration on each device]

In a traditional network, every switch and router is a self-contained unit with two functional components:

Data plane (forwarding plane) — The hardware that actually forwards packets and frames based on tables (routing tables, MAC address tables). This happens at line speed in ASICs.

Control plane — The software that builds those tables. OSPF runs on the control plane and populates the routing table. STP runs on the control plane and populates forwarding decisions.

The problem: in a large network with hundreds of switches, every change — a new VLAN, a new route, a new access control policy — must be configured on every affected device individually. There is no central intelligence. Each device makes its own forwarding decisions in isolation.

---

### [SECTION 2: SOFTWARE-DEFINED NETWORKING (SDN)]

[SHOW DIAGRAM: SDN architecture — SDN Controller at top, connected to switches via southbound API; applications connected to controller via northbound API; data plane (switches) only forward based on flow tables]

Software-Defined Networking (SDN) separates the control plane from the data plane. Instead of each device running its own control plane software, a centralized SDN Controller makes all forwarding decisions and pushes them down to the switches.

The SDN architecture has three layers:

Application Layer (top) — Business applications and network management tools that define what the network should do. Connected to the controller via the northbound API.

Control Layer (middle) — The SDN Controller. This is the "brain." It maintains a global view of the network topology and computes forwarding rules. Examples: OpenDaylight, Cisco ACI, VMware NSX Controller.

Infrastructure Layer (bottom) — Physical and virtual switches that forward traffic. They follow instructions from the controller. Connected to the controller via the southbound API (commonly OpenFlow protocol).

---

### [SECTION 3: SDN INTERFACES AND APIS]

[SHOW DIAGRAM: SDN controller with labeled northbound and southbound interfaces]

Northbound API — The interface between the SDN controller and higher-layer applications. Allows applications to request network services (create a path, enforce a policy, prioritize traffic) without knowing the underlying topology details. REST APIs are common for northbound interfaces.

Southbound API — The interface between the SDN controller and the network devices (switches, routers). The controller uses this API to push flow tables and forwarding rules. OpenFlow (developed at Stanford, standardized by ONF) is the most common southbound protocol. It allows the controller to install forwarding rules directly into switch flow tables.

East/West APIs — Communication between multiple SDN controllers to share topology information and coordinate forwarding across controller domains.

---

### [SECTION 4: OPENFLOW AND FLOW TABLES]

[SHOW DIAGRAM: OpenFlow-enabled switch — flow table with match fields (source IP, destination IP, in-port) and actions (forward, drop, modify)]

OpenFlow defines how SDN controllers communicate forwarding rules to switches. An OpenFlow switch maintains a flow table instead of a traditional MAC address table or routing table.

A flow table entry has two parts:

Match fields — Criteria that identify a packet. Can match on Layer 2 (MAC, VLAN), Layer 3 (IP address, protocol), or Layer 4 (port number). This is fundamentally different from a traditional switch — OpenFlow can make forwarding decisions based on any combination of header fields.

Actions — What to do with a matching packet: forward to a specific port, drop it, modify a header field, or send it to the controller for a policy decision.

When a packet arrives at an OpenFlow switch and no matching flow entry exists, the switch sends the packet to the SDN controller. The controller makes a forwarding decision and installs a new flow entry in the switch for future packets.

---

### [SECTION 5: OVERLAY NETWORKS]

[SHOW DIAGRAM: Overlay network — logical tunnel (VXLAN) running over a physical underlay network, connecting VMs across different physical hosts]

An overlay network is a virtual network built on top of an existing physical network infrastructure. The overlay creates tunnels between endpoints, encapsulating traffic from one network inside another network's packets.

Why overlays? In a virtualized data center, VMs can move between physical hosts. If VMs moved between hosts and retained their IP addresses, the underlying network would need to route traffic to a new physical location constantly. Overlays abstract the VM's network location from the physical topology.

VXLAN (Virtual Extensible LAN) — The most common data center overlay protocol. Encapsulates Layer 2 Ethernet frames inside UDP packets (UDP port 4789). Supports up to 16 million logical networks (24-bit VXLAN Network Identifier — VNI) versus only 4094 VLANs. VXLAN is used in VMware NSX, Cisco ACI, and major cloud providers.

GRE (Generic Routing Encapsulation) — Encapsulates any Layer 3 protocol inside another protocol. Used for point-to-point tunnels. IP Protocol 47.

MPLS (Multiprotocol Label Switching) — Used by service providers to create virtual private networks over shared infrastructure. Traffic is forwarded based on labels attached to packets rather than IP addresses.

---

### [SECTION 6: CLOUD NETWORKING CONCEPTS]

[SHOW DIAGRAM: AWS or Azure VPC — subnets, internet gateway, security groups, and virtual network interfaces shown]

Cloud providers implement networking through software-defined virtual infrastructure. Key concepts:

VPC (Virtual Private Cloud) — A logically isolated section of a cloud provider's network assigned to a tenant. The customer defines subnets, route tables, and access controls within the VPC. AWS VPC, Azure Virtual Network (VNet), and Google Cloud VPC are the major examples.

Cloud subnet — A range of IP addresses within a VPC. Subnets can be public (routable to the internet) or private (internal only).

Security Group — A stateful virtual firewall applied at the VM instance level. Controls inbound and outbound traffic based on IP, port, and protocol rules. Cloud-provider specific implementation.

Network ACL (Access Control List) — A stateless firewall applied at the subnet boundary in a VPC. Works like a packet filter — both inbound and outbound rules must be explicitly defined.

Internet Gateway — A gateway that connects a VPC to the public internet. Only VMs in public subnets with an internet gateway route can send and receive internet traffic.

NAT Gateway — Allows VMs in private subnets to initiate outbound internet connections (for software updates) without being reachable from the internet.

---

### [SECTION 7: MICROSEGMENTATION]

[SHOW DIAGRAM: Traditional perimeter security (firewall at network edge only) versus microsegmentation (policy applied between every VM pair)]

Microsegmentation is a security architecture enabled by SDN and overlay networks. Traditional network security relied on a firewall at the perimeter — traffic inside the LAN was largely trusted. Once an attacker gained access inside the perimeter, lateral movement was relatively easy.

Microsegmentation applies security policies between individual workloads — between every VM pair if needed. A web server VM cannot communicate with a database VM unless an explicit policy allows it, even though they are on the same physical host.

VMware NSX is the leading enterprise microsegmentation platform. It implements distributed firewalling at the vNIC level — every packet between VMs is inspected against policy, regardless of whether the traffic stays on the same host or traverses the physical network.

The key phrase for the exam: microsegmentation moves security from the network perimeter to individual workloads.

---

### [SECTION 8: SDN USE CASES AND VENDORS]

[SHOW DIAGRAM: SDN use cases — data center automation, WAN optimization, campus network policy management]

Major SDN deployments and vendor platforms:

Cisco ACI (Application Centric Infrastructure) — Cisco's data center SDN solution. Uses a centralized APIC controller and purpose-built Nexus switches. Defines network policy around application needs rather than VLAN IDs.

VMware NSX — Software-defined networking and security for virtualized environments. Creates overlay networks with VXLAN, implements microsegmentation with distributed firewall, integrates directly with vSphere hypervisor.

OpenDaylight — Open-source SDN controller project. Used in carrier and enterprise environments for programmable networking.

SD-WAN (Software-Defined WAN) — Applies SDN principles to WAN connectivity. SD-WAN controllers manage traffic routing across multiple WAN links (MPLS, internet, LTE) based on application policy and link quality. Vendors: Cisco Viptela, VMware Velocloud, Fortinet, Silver Peak.

---

### [SECTION 9: KEY EXAM CONCEPTS SUMMARY]

For the CompTIA Network+ exam, ensure you know:

Control plane vs. data plane: control plane builds tables (routing, MAC), data plane forwards traffic using those tables.

SDN: centralizes the control plane in an SDN controller; data plane devices follow controller instructions.

Northbound API: controller to application.

Southbound API: controller to network device (OpenFlow).

VXLAN: Layer 2 overlay in UDP, 24-bit VNI (up to 16M networks), port 4789.

Type 1 vs. Type 2 hypervisor: bare-metal versus hosted.

NFV: network functions as software VMs instead of physical appliances.

Microsegmentation: per-workload security policy, not just perimeter security.

VPC: logically isolated cloud network. Security Groups = stateful per-instance firewall. Network ACL = stateless per-subnet filter.

---

### [SUMMARY — PART 2]

In Part 2 we covered:

- SDN architecture: control plane/data plane separation, three-layer model
- Northbound and southbound APIs, OpenFlow protocol
- Flow tables: match fields and actions
- Overlay networks: VXLAN (UDP 4789, 24-bit VNI), GRE, MPLS
- Cloud networking: VPC, security groups, network ACLs, internet gateway, NAT gateway
- Microsegmentation: per-workload security policy enabled by SDN
- SDN vendor platforms: Cisco ACI, VMware NSX, OpenDaylight, SD-WAN

Module 12 connects virtual infrastructure concepts to the physical networking you have studied throughout this course. The exam will test whether you can identify hypervisor types, explain the role of an SDN controller, and distinguish overlay protocols.

See you in the lab.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
