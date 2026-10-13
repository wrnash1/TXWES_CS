# Quiz: Module 01 - Network Architectures & Topologies

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

In a three-tier enterprise design, at which layer is routing between VLANs and policy-based traffic control (ACLs, QoS) typically implemented?

- A) Access Layer
- B) Distribution Layer
- C) Core Layer
- D) Physical Layer

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The Access layer connects end devices and operates primarily at Layer 2. It does not perform inter-VLAN routing.
- B is correct: The Distribution layer aggregates Access switches, performs inter-VLAN routing via SVIs, enforces ACLs, and applies QoS markings before traffic reaches the Core.
- C is incorrect: The Core layer is designed exclusively for high-speed packet forwarding. Applying ACLs or routing policies at the Core would introduce latency and defeat the purpose of the layer.
- D is incorrect: The Physical layer is OSI Layer 1, describing cables and electrical signals. It is not a tier in the three-tier network design model.

---

## Question 2

Which of the following most accurately describes a spine-leaf topology?

- A) A two-tier data center design where every leaf switch connects to every spine switch, providing equal-cost multipath paths with no Spanning Tree Protocol dependency.
- B) A hierarchical campus design with three discrete layers: Core, Distribution, and Access, each performing a specific forwarding or policy role.
- C) A WAN topology where all remote branch sites connect back to a single central hub router with no direct branch-to-branch links.
- D) A redundant design where two core switches are connected with a cross-link and each distribution switch dual-homes to both core switches.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: Spine-leaf is a two-tier data center architecture where every leaf connects to every spine, enabling ECMP and eliminating STP dependency.
- B is incorrect: This describes the traditional three-tier campus model (Core, Distribution, Access), not spine-leaf.
- C is incorrect: This describes a hub-and-spoke WAN topology.
- D is incorrect: This describes a redundant collapsed-core or dual-core campus design, not a spine-leaf architecture.

---

## Question 3

A network engineer is documenting a small single-building office network with approximately 200 users. The engineer merges the Core and Distribution layers into a single tier of multilayer switches. What design model is this?

- A) Spine-leaf
- B) Three-tier
- C) Collapsed core
- D) Hub-and-spoke

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Spine-leaf is a data center topology used for server-to-server traffic, not a small office campus design.
- B is incorrect: Three-tier has separate Core, Distribution, and Access layers — three distinct tiers, not two.
- C is correct: Collapsed core merges the Core and Distribution layers into a single tier, producing a two-tier model appropriate for small campuses.
- D is incorrect: Hub-and-spoke is a WAN topology describing how remote branches connect to a headquarters site.

---

## Question 4

A network topology uses dedicated point-to-point links between every node and every other node. For a network with 6 nodes, how many links are required?

- A) 6
- B) 12
- C) 15
- D) 30

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: 6 links would form a ring or a star from a single central node, not a full mesh.
- B is incorrect: 12 is n x 2 — this does not follow the full mesh formula.
- C is correct: Full mesh uses n(n-1)/2 links. For 6 nodes: 6 x 5 / 2 = 15.
- D is incorrect: 30 would be n(n-1) without dividing by 2, which counts each link twice.

---

## Question 5

A rogue laptop is physically plugged into an Access layer switch port in a secure office. Which control most directly prevents the unauthorized device from communicating on the network?

- A) Implement switch port security to restrict access based on approved MAC addresses
- B) Configure SSH on all switches for encrypted management access
- C) Deploy a syslog server to record connection events
- D) Configure 802.1X port-based authentication requiring valid credentials before network access is granted

**Correct Answer:** D

**Distractor Analysis:**

- A is partially correct but D is stronger: Port security restricts MACs, but an attacker can spoof a MAC address. 802.1X requires credential-based authentication, which is significantly harder to bypass.
- B is incorrect: SSH protects management sessions but does not prevent an unauthorized device from using a data port.
- C is incorrect: Syslog is a detective control that records events after they occur. It does not prevent unauthorized access.
- D is correct: 802.1X port-based authentication requires a supplicant to present valid credentials to an authentication server before the switch port grants network access. This is the most robust preventive control.

---

## Question 6

Which Cisco IOS command displays all currently active trunk ports on a switch and shows which VLANs are allowed on each trunk?

- A) `show vlan brief`
- B) `show interfaces trunk`
- C) `show ip route`
- D) `show cdp neighbors`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `show vlan brief` displays VLAN names and their port assignments, but does not specifically list trunk port status or allowed VLANs.
- B is correct: `show interfaces trunk` displays all ports currently operating in trunk mode, their encapsulation type (802.1Q), native VLAN, and the list of VLANs allowed and active on each trunk.
- C is incorrect: `show ip route` displays the routing table on a Layer 3 device. It has no relationship to trunk port status.
- D is incorrect: `show cdp neighbors` displays directly connected Cisco neighbors. It does not show trunk or VLAN configuration.

---

## Question 7

In a spine-leaf data center topology, how many hops does traffic traverse when traveling from a server connected to Leaf-A to a server connected to Leaf-B?

- A) 1
- B) 2
- C) 3
- D) It varies depending on which spine switch is available

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A single hop would require Leaf-A and Leaf-B to connect directly, which violates the spine-leaf rule that leaf switches do not connect to each other.
- B is correct: Traffic always travels Leaf-A to a Spine switch (hop 1) and then Spine to Leaf-B (hop 2). This consistent two-hop path is a core advantage of spine-leaf.
- C is incorrect: Three hops would imply an intermediate device between the spine switches, which does not exist in a standard spine-leaf design.
- D is incorrect: The number of hops is always exactly 2 regardless of which spine switch carries the traffic, because every leaf connects to every spine.

---

## Question 8

An engineer runs `show cdp neighbors` on SW-CORE-1 and sees SW-DIST-1 listed but not SW-DIST-2, even though a cable is connected between SW-CORE-1 and SW-DIST-2. What is the most likely cause?

- A) SW-DIST-2 is not a Cisco device and therefore does not support CDP
- B) The cable between SW-CORE-1 and SW-DIST-2 is connected to the wrong port or CDP was disabled on the connected interface
- C) CDP requires IP addressing to be configured on both devices before neighbors can be discovered
- D) `show cdp neighbors` only displays one neighbor per device

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The question states SW-DIST-2 is in the topology as a distribution switch. Cisco Catalyst switches support CDP by default.
- B is correct: CDP does not require IP addressing and is enabled by default. If a neighbor is not appearing, the cable is connected to the wrong port, the interface is down, or CDP was explicitly disabled on that interface with `no cdp enable`.
- C is incorrect: CDP operates at Layer 2 and does not require IP addresses to discover neighbors.
- D is incorrect: `show cdp neighbors` displays all directly connected Cisco neighbors, not just one.

---

## Question 9

A campus network engineer is designing a new building addition. The building will have 800 users spread across four floors, and the network must scale to 1,200 users within two years. Which design model is most appropriate?

- A) Spine-leaf with two spine switches and one leaf per floor
- B) Three-tier with dedicated Core, Distribution, and Access layers
- C) Collapsed core with two multilayer switches and four access switches
- D) Hub-and-spoke with the main building as the hub

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Spine-leaf is designed for data center east-west server traffic, not for campus user access networks.
- B is correct: With 800 to 1,200 users across multiple floors and a need for scalability, a three-tier design is appropriate. The separate Core layer allows the distribution and access layers to grow without redesigning the entire network.
- C is incorrect: A collapsed core is appropriate for smaller, single-building networks with limited growth expectations. 1,200 users would strain a two-tier design.
- D is incorrect: Hub-and-spoke is a WAN topology for connecting remote branch sites. It does not apply to a multi-floor campus building design.

---

## Question 10

Which statement correctly distinguishes between physical topology and logical topology?

- A) Physical topology describes IP addressing; logical topology describes how cables are physically connected
- B) Physical topology and logical topology are always identical on Ethernet networks
- C) Physical topology describes how devices are physically cabled; logical topology describes how data actually flows through the network
- D) Logical topology only applies to wireless networks

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: IP addressing belongs to Layer 3 and is not part of the definition of physical topology.
- B is incorrect: Physical and logical topologies can differ. A classic example is Token Ring, which was physically wired as a star through a multistation access unit (MAU) but operated logically as a ring.
- C is correct: Physical topology is the actual arrangement of cables and hardware. Logical topology is how data flows, which may differ — for example, a switched Ethernet network is physically a star but logically allows any-to-any communication.
- D is incorrect: Logical topology applies to all network types, not just wireless networks.

---

## Question 11

A network engineer is designing a campus addition. The requirements specify that the Core layer must never have ACLs applied and must only perform high-speed Layer 3 forwarding. A junior engineer suggests applying a QoS policy directly on the Core switches to mark traffic. What should the senior engineer recommend?

- A) Apply QoS marking on Core switches because they are the most powerful in the hierarchy
- B) Move QoS marking to the Distribution layer where policy enforcement is the defined role
- C) Apply QoS on Access switches to mark traffic as close to the source as possible, and do not apply policy at Core
- D) Both B and C are correct — Distribution enforces policy and Access marks at the source

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: The Core layer exists solely for fast packet forwarding. Applying QoS marking on Core switches violates the three-tier design principle and introduces processing overhead that degrades the Core's primary function.
- B is partially correct: The Distribution layer is the correct policy enforcement point in the three-tier model; however, CCNA best practice also recommends marking traffic as close to the source as possible, meaning Access layer marking is preferred when feasible.
- C is partially correct: Access layer marking is preferred but the Distribution layer still enforces policy for traffic arriving from the Access layer, so both are correct in practice.
- D is correct: Best practice is to mark traffic at the Access layer (closest to the source) and enforce policy and QoS at the Distribution layer. Neither the Core switches nor the Core layer should perform policy functions.

---

## Question 12

A company's WAN connects its headquarters to 40 branch offices. All inter-branch communication must route through the headquarters router. Traffic volumes between individual branches are low. Which WAN topology best describes this design and what is its primary drawback?

- A) Full mesh — primary drawback is the cost of n(n-1)/2 WAN links
- B) Partial mesh — primary drawback is that not all branches have direct connectivity
- C) Hub-and-spoke — primary drawback is that the hub is a single point of failure and bottleneck for spoke-to-spoke traffic
- D) Point-to-point — primary drawback is that it only supports two sites

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Full mesh between 40 branches would require 40x39/2 = 780 WAN links, which is cost-prohibitive. The described design routes all traffic through headquarters, which is hub-and-spoke behavior.
- B is incorrect: Partial mesh provides some branch-to-branch direct connectivity. The described design routes all traffic through headquarters, which is hub-and-spoke behavior.
- C is correct: Hub-and-spoke matches this description exactly — all spokes connect only to the hub (headquarters), and all inter-spoke traffic must traverse the hub. The hub becomes both a bottleneck for bandwidth and a single point of failure.
- D is incorrect: Point-to-point describes a single dedicated link between exactly two devices. A network with 40 branches and one headquarters is not point-to-point.

---

## Question 13

An engineer uses `show cdp neighbors detail` on R1 and sees that R2 has IP address 10.1.1.2. The engineer cannot ping 10.1.1.2 from R1. CDP is working but ping fails. What is the most likely cause?

- A) CDP is disabled on R2
- B) The IP address on R1's connecting interface is in a different subnet than 10.1.1.2
- C) CDP requires both routers to be in the same OSPF area
- D) The `ping` command requires SSH to be configured first

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: If CDP were disabled on R2, R2 would not appear in the `show cdp neighbors detail` output. The fact that R2 is visible confirms CDP is working on R2.
- B is correct: CDP operates at Layer 2 and discovers neighbors regardless of IP addressing. If the two interfaces are in different subnets (e.g., R1 is 10.1.2.1/24 and R2 is 10.1.1.2/24), Layer 3 ping will fail even though CDP succeeds. This is a common troubleshooting scenario.
- C is incorrect: CDP has no relationship to OSPF. CDP is a Layer 2 proprietary protocol that operates independently of any routing protocol.
- D is incorrect: The `ping` command on Cisco IOS does not require SSH to be configured. SSH is for encrypted management access, not for ICMP connectivity testing.

---

## Question 14

How many links are required to build a full mesh topology connecting 5 routers in a WAN?

- A) 5
- B) 8
- C) 10
- D) 20

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: 5 links would form a ring (each router connected to the next in a loop) or a star from one hub, not a full mesh.
- B is incorrect: 8 does not correspond to the full mesh formula for any small integer. This is not a valid result of n(n-1)/2.
- C is correct: Full mesh links = n(n-1)/2 = 5x4/2 = 10. Each of the 5 routers has 4 connections to the other routers, and dividing by 2 eliminates double-counting of bidirectional links.
- D is incorrect: 20 = n(n-1) without dividing by 2, which counts each link twice. The correct formula divides by 2 because each link is shared by two routers.

---

## Question 15

In the three-tier campus model, an Access layer switch sends traffic to a Distribution switch. The Distribution switch performs inter-VLAN routing and forwards the packet to the Core. What device type does the Distribution switch most likely use for inter-VLAN routing?

- A) A dedicated external router with subinterfaces (router-on-a-stick)
- B) A multilayer switch with SVIs (Switched Virtual Interfaces)
- C) A Layer 2 switch with an uplink module
- D) A firewall acting as the default gateway for each VLAN

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Router-on-a-stick is a valid inter-VLAN routing method but is typically used in smaller deployments. The Distribution layer in an enterprise three-tier design uses multilayer switches for performance and redundancy reasons.
- B is correct: The Distribution layer uses multilayer switches (e.g., Catalyst 9300, 3850) that run both Layer 2 switching and Layer 3 routing. SVIs provide a virtual interface for each VLAN, acting as the default gateway for hosts in that VLAN.
- C is incorrect: A Layer 2 switch cannot perform routing between VLANs. Layer 2 switches only forward frames based on MAC addresses within the same VLAN.
- D is incorrect: While firewalls can act as default gateways, placing a firewall as the inter-VLAN routing device in the Distribution layer is not standard three-tier campus design. Firewalls are typically deployed at network perimeters.

---

## Question 16

An administrator runs `show vlan brief` on an Access switch and notices that a port appears under VLAN 1 instead of VLAN 30. The port was configured with `switchport access vlan 30`. What is the most likely reason the port shows in VLAN 1?

- A) VLAN 30 must be created on the switch before a port can be assigned to it; if VLAN 30 does not exist, the port defaults to VLAN 1
- B) `show vlan brief` only shows VLANs in the range 1–29
- C) The `switchport access vlan 30` command requires a reload to take effect
- D) VLAN 1 is always the native VLAN and overrides all manual assignments

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: On Cisco IOS switches, if you assign a port to a VLAN that does not yet exist in the VLAN database, the port may show as inactive or revert to VLAN 1 behavior. Creating VLAN 30 with the `vlan 30` command in global configuration mode resolves the issue.
- B is incorrect: `show vlan brief` displays all VLANs in the range 1–4094 that exist on the switch. There is no display limitation based on VLAN number.
- C is incorrect: VLAN assignments take effect immediately after the `switchport access vlan` command is entered. No reload is required.
- D is incorrect: VLAN 1 is the default native VLAN for trunk ports, but it does not override access port VLAN assignments. A correctly configured access port in an existing VLAN will not revert to VLAN 1.

---

## Question 17

Which of the following correctly describes the purpose of LLDP (Link Layer Discovery Protocol) compared to CDP?

- A) LLDP is Cisco-proprietary and CDP is the IEEE standard
- B) LLDP is the IEEE 802.1AB standard and works with non-Cisco devices; CDP is Cisco-proprietary
- C) LLDP operates at Layer 3 using IP multicast; CDP operates at Layer 2
- D) LLDP and CDP are functionally identical and can be used interchangeably on all networks

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: This reverses the correct relationship. CDP is Cisco-proprietary; LLDP is the open IEEE standard.
- B is correct: LLDP (IEEE 802.1AB) is the vendor-neutral Layer 2 neighbor discovery protocol. It operates on non-Cisco equipment including Juniper, HP, and Aruba devices. CDP is Cisco-proprietary and only works between Cisco devices.
- C is incorrect: Both LLDP and CDP operate at Layer 2. Neither uses IP addressing for neighbor discovery. Both use multicast MAC addresses to send frames.
- D is incorrect: LLDP and CDP are similar in function but are separate protocols. A Cisco device running CDP cannot discover a non-Cisco device unless LLDP is also enabled. They are not interchangeable in mixed-vendor environments without explicit configuration.

---

## Question 18

A network administrator is designing a small office with 50 users in a single building. Cost is the primary constraint. Which design model is most appropriate?

- A) Three-tier with dedicated Core, Distribution, and Access switches
- B) Spine-leaf with two spine switches and one leaf switch
- C) Collapsed core with a single multilayer switch acting as both Core and Distribution, plus Access layer switches
- D) Hub-and-spoke with the main router as the hub

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: A three-tier design with separate Core, Distribution, and Access switches is appropriate for large campus networks. For 50 users in one building, this design is overbuilt and unnecessarily expensive.
- B is incorrect: Spine-leaf is a data center architecture for server-to-server traffic. It is not appropriate for a small office user-access network.
- C is correct: A collapsed core design merges the Core and Distribution layers into a single multilayer switch tier. This reduces hardware cost and complexity while providing sufficient routing and policy enforcement for a small office. It is the standard recommendation for small single-building networks.
- D is incorrect: Hub-and-spoke is a WAN topology for connecting geographically distributed sites. It does not describe a LAN design for a single-building office.

---

## Question 19

A trunk link between two switches carries VLANs 10, 20, and 30. An engineer runs `show interfaces trunk` and sees that VLAN 40 is not listed under "VLANs allowed and active in management domain" even though VLAN 40 exists on both switches. What is the most likely cause?

- A) VLAN 40 is not permitted on the trunk because the `switchport trunk allowed vlan` command does not include VLAN 40
- B) VLAN 40 automatically becomes the native VLAN and is therefore not listed
- C) Trunk ports can only carry a maximum of three VLANs simultaneously
- D) VLAN 40 is a reserved VLAN and cannot be carried on 802.1Q trunk links

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The `switchport trunk allowed vlan` command explicitly controls which VLANs are permitted to cross the trunk. If this command specifies only VLANs 10, 20, and 30, VLAN 40 traffic will be dropped on that trunk regardless of whether VLAN 40 exists on both switches. The fix is `switchport trunk allowed vlan add 40`.
- B is incorrect: The native VLAN is sent untagged on the trunk but still appears in `show interfaces trunk` output in the native VLAN field. VLAN 40 not appearing in the allowed list suggests it is excluded, not native.
- C is incorrect: 802.1Q trunk links can carry up to 4094 VLANs simultaneously. There is no three-VLAN limit.
- D is incorrect: VLAN 40 is not a reserved VLAN. Reserved VLANs include 1002–1005 (legacy Token Ring and FDDI). VLANs 2–4001 are available for general use.

---

## Question 20

What is the default administrative distance of a directly connected route on a Cisco IOS router, and how does this affect route selection when a routing protocol also has a route to the same destination?

- A) Administrative distance 0; directly connected routes are always preferred over all other route sources
- B) Administrative distance 1; directly connected routes are preferred over static routes (AD 1) using a tiebreaker
- C) Administrative distance 90; EIGRP internal routes (AD 90) would be preferred over directly connected routes
- D) Administrative distance 110; OSPF routes (AD 110) and directly connected routes tie and are load-balanced

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: Directly connected routes have an administrative distance of 0, which is the lowest possible value. Lower AD means higher trustworthiness. A directly connected route is always preferred over any other route source for the same prefix because no routing protocol or static route can have an AD lower than 0.
- B is incorrect: Directly connected routes have AD 0, not AD 1. Static routes have AD 1. Since directly connected is AD 0 and static is AD 1, directly connected always wins — but not due to a tiebreaker. AD 0 simply beats AD 1.
- C is incorrect: EIGRP internal routes have AD 90, which is much higher than AD 0. The directly connected route would always be preferred.
- D is incorrect: OSPF has AD 110. A directly connected route at AD 0 is always preferred over the OSPF route. There is no tie and no load-balancing between different route sources with different ADs.
