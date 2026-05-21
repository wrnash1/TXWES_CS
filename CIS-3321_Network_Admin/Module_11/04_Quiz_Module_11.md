# Quiz: Module 11 - Switching – VLANs, STP, and EtherChannel
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network administrator needs to configure a switch port that connects an IP phone. The phone should be on VLAN 20 (Voice VLAN) and its attached PC should be on VLAN 10 (Data VLAN), both on the same physical port. Which port configuration accomplishes this?
A) Configure the port as a trunk with VLANs 10 and 20 allowed — the phone and PC negotiate their VLAN assignment via DHCP
B) Configure the port as an access port in VLAN 10 with an additional voice VLAN 20 assignment using Cisco voice VLAN feature
C) Configure the port as a trunk port with VLAN 10 as the native VLAN and VLAN 20 as a tagged VLAN allowed on the trunk
D) Configure two separate physical ports — one access port in VLAN 10 for the PC and one access port in VLAN 20 for the phone
*   **Correct Answer:** B) Configure the port as an access port in VLAN 10 with an additional voice VLAN 20 assignment using Cisco voice VLAN feature
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A trunk port carries multiple VLANs between switches — it is not the correct configuration for an end-device port connecting a phone and PC. Trunk ports are for switch-to-switch or switch-to-router links, not end-device access ports.
    *   *Why C is incorrect:* While a trunk could technically work, the standard enterprise design for a phone/PC port is an access port with a voice VLAN, not a trunk. The native VLAN on a trunk carries untagged traffic — using VLAN 10 as native and VLAN 20 as tagged is a trunk configuration that adds unnecessary complexity for an access port scenario.
    *   *Why D is incorrect:* Using two separate physical ports is wasteful of switch port resources. The Cisco voice VLAN feature was designed specifically to allow a single physical port to support both a data VLAN and a voice VLAN simultaneously.

---

**Question 2**
A network engineer observes that all traffic between two switches is flowing through a single uplink even though four redundant links are physically connected between them. The engineer wants to use all four links simultaneously for increased bandwidth. Which technology and configuration achieves this?
A) Configure STP PortFast on all four inter-switch links to put them all in Forwarding state simultaneously
B) Configure EtherChannel using LACP, bundling all four links into a single logical port-channel interface
C) Disable STP on both switches so all four links can forward traffic without any being blocked
D) Configure each link in a different VLAN so STP creates a separate spanning tree instance per VLAN, using one link per VLAN
*   **Correct Answer:** B) Configure EtherChannel using LACP, bundling all four links into a single logical port-channel interface
*   **Distractor Analysis:**
    *   *Why A is incorrect:* PortFast is designed for access ports connecting end devices — it should never be configured on inter-switch links. Enabling PortFast on switch-to-switch links removes BPDU processing delay but does not allow multiple parallel links to forward simultaneously; STP still blocks redundant inter-switch paths.
    *   *Why C is incorrect:* Disabling STP removes the protection against Layer 2 loops. With four parallel links and no STP, broadcast storms would immediately form, bringing down the network. STP must remain enabled — EtherChannel is the correct way to use multiple links while keeping STP protection.
    *   *Why D is incorrect:* This is the Per-VLAN Spanning Tree (PVST) approach — it uses one link per VLAN by manipulating STP root bridge placement per VLAN. While valid for load distribution, it does not aggregate all four links' bandwidth for any single traffic flow. EtherChannel provides true link aggregation.

---

**Question 3**
After a new switch is added to the network with its default bridge priority of 32768, it wins the STP Root Bridge election and causes suboptimal traffic paths throughout the campus network. The previous Root Bridge had priority 32768 with a lower MAC address. How should the network administrator prevent this from happening in the future?
A) Enable BPDU Guard on all trunk ports to block BPDU messages from the new switch
B) Set the bridge priority of the intended Root Bridge switch to a value lower than 32768 (e.g., 4096) to ensure it always wins the election
C) Configure PortFast on the Root Bridge's uplink ports to accelerate STP convergence
D) Increase the bridge priority of the new switch to 65535 to prevent it from becoming Root Bridge
*   **Correct Answer:** B) Set the bridge priority of the intended Root Bridge switch to a value lower than 32768 (e.g., 4096) to ensure it always wins the election
*   **Distractor Analysis:**
    *   *Why A is incorrect:* BPDU Guard is a security feature for access ports that err-disables a port when a BPDU is received — it does not prevent a switch from participating in STP elections. Enabling BPDU Guard on trunk ports would cause those ports to be disabled when they receive legitimate STP BPDUs from peer switches, breaking the network.
    *   *Why C is incorrect:* PortFast bypasses STP listening/learning states on access ports to speed up end-device connectivity — it has no effect on Root Bridge election. Configuring PortFast on uplinks is a misconfiguration that can create loops.
    *   *Why D is incorrect:* STP Root Bridge election selects the switch with the LOWEST bridge priority. Increasing the new switch's priority to 65535 makes it less likely to become Root — but it does not guarantee the intended switch wins if another switch with default priority 32768 and a lower MAC address is added later. The correct solution is to lower the intended Root's priority.

---

**Question 4**
A network administrator is troubleshooting why workstations on VLAN 30 cannot reach servers on VLAN 40. Both VLANs exist on the same switch. The switch is a Layer 2 switch connected to a router via a single trunk link. Which configuration is required on the router?
A) Create sub-interfaces on the router's trunk-connected interface — one sub-interface per VLAN with an 802.1Q encapsulation tag and a gateway IP address for each VLAN
B) Configure static routes on the router pointing VLAN 30 and VLAN 40 subnets to the switch's management IP address
C) Enable OSPF on the router and redistribute both VLAN subnets so the switch can learn the routes dynamically
D) Configure trunk ports on the router with native VLANs matching each VLAN's ID so traffic can cross VLANs without tagging
*   **Correct Answer:** A) Create sub-interfaces on the router's trunk-connected interface — one sub-interface per VLAN with an 802.1Q encapsulation tag and a gateway IP address for each VLAN
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Static routes on the router do not solve inter-VLAN routing — the router needs sub-interfaces with IP addresses that act as default gateways for each VLAN's hosts. Static routes define where to forward traffic, but without sub-interfaces configured with VLAN-specific IP addresses, the router has no way to communicate with hosts in either VLAN.
    *   *Why C is incorrect:* OSPF is a dynamic routing protocol for discovering routes between networks — it does not configure the VLAN gateway interfaces that hosts need to send inter-VLAN traffic. The router still needs sub-interfaces with IP addresses before OSPF (or any routing) can work.
    *   *Why D is incorrect:* Routers do not have trunk ports in the switch sense — they have interfaces and sub-interfaces. The native VLAN on a trunk sends traffic untagged; using native VLANs for each VLAN would require each VLAN to be the native VLAN simultaneously, which is impossible. Sub-interfaces with 802.1Q encapsulation is the correct Router-on-a-Stick design.

---

**Question 5**
A security team is hardening the switching infrastructure to prevent three common Layer 2 attacks: (1) VLAN hopping via DTP negotiation, (2) unauthorized switches forming STP adjacencies and claiming Root Bridge, and (3) MAC flooding attacks that overflow the CAM table. Which combination of controls addresses all three?
A) Disable DTP on all access ports (`switchport nonegotiate`), enable BPDU Guard on all PortFast-configured access ports, and configure Port Security with a maximum MAC address limit per port.
B) Configure all ports as trunk ports with explicit VLAN allow lists, enable Root Guard on the Root Bridge's uplink ports, and deploy DHCP snooping on all access VLANs.
C) Enable STP on all switches, configure all access ports in VLAN 1, and deploy an IDS to detect MAC flooding events.
D) Configure all inter-switch links as access ports in a dedicated management VLAN, enable PortFast on all trunk ports, and use static MAC address entries for all servers.
*   **Correct Answer:** A) Disable DTP on all access ports (`switchport nonegotiate`), enable BPDU Guard on all PortFast-configured access ports, and configure Port Security with a maximum MAC address limit per port.
*   **Distractor Analysis:**
    *   *Why A is correct:* Disabling DTP prevents trunk negotiation on access ports, eliminating VLAN hopping via double-tagging (requirement 1); BPDU Guard err-disables any access port that receives a BPDU, preventing unauthorized switches from participating in STP (requirement 2); Port Security limits MAC address learning per port, preventing CAM table flooding attacks (requirement 3).
    *   *Why B is incorrect:* Configuring all ports as trunks expands the attack surface rather than reducing it. Root Guard prevents Root Bridge changes on designated ports but is placed on the existing Root Bridge's ports, not uplinks — placement matters. DHCP snooping addresses rogue DHCP servers, not MAC flooding.
    *   *Why C is incorrect:* STP is already enabled by default; this provides no additional hardening. Placing all access ports in VLAN 1 is a security anti-pattern (VLAN 1 is the default management VLAN). An IDS detects MAC flooding after it occurs but does not prevent it — Port Security prevents it proactively.
    *   *Why D is incorrect:* Configuring inter-switch links as access ports breaks trunk functionality and VLAN communication between switches. PortFast on trunk ports is a critical misconfiguration that bypasses STP protection on switch-to-switch links, increasing loop risk. Static MAC entries for servers do not prevent MAC flooding from attack ports.
