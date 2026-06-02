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
