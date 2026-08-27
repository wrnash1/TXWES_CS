# Quiz: Module 07 - Inter-VLAN Routing Solutions

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

In a router-on-a-stick topology, how are multiple VLANs handled on a single physical router interface?

- A) Multiple IP addresses are assigned to the parent physical interface, one per VLAN
- B) Logical subinterfaces are created on the physical interface, each configured with 802.1Q encapsulation and an IP address for one VLAN
- C) The physical interface is connected to multiple switches simultaneously, one per VLAN
- D) PortFast is enabled on the router interface to allow multiple VLAN frames to pass

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A single parent physical interface in ROAS does not receive an IP address at all. Only the subinterfaces receive IP addresses, one per VLAN.
- B is correct: Subinterfaces (e.g., Gi0/0.10, Gi0/0.20) are logical divisions of the physical interface. Each subinterface is configured with `encapsulation dot1Q [vlan-id]` and an IP address serving as the default gateway for that VLAN.
- C is incorrect: Router-on-a-stick uses a single physical connection to a single switch trunk port. Connecting to multiple switches defeats the purpose of the design.
- D is incorrect: PortFast is an STP feature for access ports. It has nothing to do with VLAN encapsulation or inter-VLAN routing on a router interface.

---

## Question 2

Which of the following most accurately describes a Layer 3 Switch SVI?

- A) A virtual Layer 3 interface on a multilayer switch that represents a VLAN, assigned an IP address that becomes the default gateway for hosts in that VLAN
- B) A physical router interface subdivided into logical subinterfaces, each carrying 802.1Q-tagged frames for a separate VLAN over a single trunk link
- C) A loopback interface on a Cisco router used as a stable management address that stays up regardless of physical interface state
- D) A virtual port-channel interface that aggregates multiple physical switch ports into a single logical link for increased bandwidth

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: SVIs are created with `interface vlan [id]` on a multilayer switch. They require `ip routing` globally and must have at least one active access port in the VLAN to reach up/up state.
- B is incorrect: This describes router subinterfaces used in router-on-a-stick. Subinterfaces are on a router, not on a multilayer switch.
- C is incorrect: This describes a loopback interface, which is a separate IOS construct used for management addressing and routing protocol configuration.
- D is incorrect: This describes a port-channel (EtherChannel) interface. Port-channels aggregate physical links for bandwidth — they are not Layer 3 VLAN interfaces.

---

## Question 3

A network engineer configures subinterfaces for ROAS but all inter-VLAN pings fail. `show ip interface brief` shows the subinterfaces as up/up with correct IP addresses. Which of the following is the most likely cause?

- A) `ip routing` was not entered on the router
- B) The switch port connected to the router is configured as an access port instead of a trunk port
- C) The subinterface numbers do not match the VLAN IDs
- D) `no shutdown` was entered on the subinterfaces instead of the parent interface

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `ip routing` is required on multilayer switches to enable inter-VLAN routing via SVIs. Cisco routers route by default — `ip routing` is not needed on a standalone router.
- B is correct: If the switch port toward the router is an access port, it only passes one VLAN untagged. Subinterfaces expecting tagged 802.1Q frames from multiple VLANs receive no traffic. The switch port must be configured as a trunk with the VLANs allowed.
- C is incorrect: Subinterface numbers do not need to match VLAN IDs. The VLAN association is set exclusively by the `encapsulation dot1Q [vlan-id]` command. Mismatched numbers do not cause failure as long as encapsulation is correct.
- D is incorrect: Entering `no shutdown` on subinterfaces is fine, but the parent physical interface also requires `no shutdown`. However, if the subinterfaces show `up/up`, the parent is already up, eliminating this as the cause.

---

## Question 4

Which of the following commands must be entered first on a router subinterface before the IP address command will be accepted?

- A) `switchport mode trunk`
- B) `no shutdown`
- C) `encapsulation dot1Q [vlan-id]`
- D) `ip routing`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `switchport mode trunk` is a Layer 2 switch command. It is not entered on a router subinterface. The switch port facing the router is set to trunk — not the router itself.
- B is incorrect: `no shutdown` activates the interface but is not required before the IP address command. It can be entered in any order relative to the IP address assignment.
- C is correct: Cisco IOS requires `encapsulation dot1Q [vlan-id]` to be configured on a subinterface before an IP address can be assigned. Without encapsulation, the router does not know which VLAN the subinterface serves and rejects the IP address command.
- D is incorrect: `ip routing` is a global command required on multilayer switches to enable routing. Standalone routers do not require it — they route by default.

---

## Question 5

An engineer configures a multilayer switch with three SVIs (VLAN 10, 20, 30) and assigns IP addresses to each. After configuration, hosts in different VLANs still cannot ping each other. `show ip interface brief` shows all three SVIs as up/up. What is the most likely cause?

- A) The physical access ports have not been assigned to their VLANs
- B) `ip routing` has not been enabled on the multilayer switch
- C) The SVIs require `encapsulation dot1Q` to identify their VLANs
- D) No trunk port has been configured between the SVIs

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: If access ports were not assigned to VLANs, the SVIs would show `up/down`, not `up/up`. The fact that SVIs are `up/up` confirms active ports exist in each VLAN.
- B is correct: `ip routing` is the required global command to enable Layer 3 routing on a multilayer switch. Without it, the switch treats all traffic as Layer 2 and will not route between VLANs even if SVIs are configured and up.
- C is incorrect: SVIs do not require `encapsulation dot1Q`. That command is used on router subinterfaces for ROAS. An SVI is inherently associated with its VLAN by the `interface vlan [id]` command.
- D is incorrect: SVIs route internally within the switch hardware. There is no requirement for a trunk port between SVIs — they are virtual interfaces on the same physical device.

---

## Question 6

An engineer needs to trace the Layer 3 hop-by-hop path to a remote destination to verify inter-VLAN routing is working correctly. Which command is most appropriate?

- A) `ping`
- B) `traceroute`
- C) `netstat -ano`
- D) `nslookup`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `ping` tests end-to-end reachability and measures round-trip time. It does not reveal intermediate router hops or confirm which Layer 3 device is performing the routing.
- B is correct: `traceroute` sends packets with incrementing TTL values to discover each router hop along the path. In an inter-VLAN routing scenario, it confirms that traffic is passing through the expected gateway (router subinterface or SVI).
- C is incorrect: `netstat -ano` is a Windows/Linux command that lists active TCP/UDP connections and listening ports on a host. It does not test or display network routing paths.
- D is incorrect: `nslookup` resolves DNS hostnames to IP addresses. It has no function in testing routing path or inter-VLAN connectivity.

---

## Question 7

When configuring router-on-a-stick, an engineer enters the IP address command on the parent physical interface Gi0/0 instead of on a subinterface. What is the result?

- A) The IP address on the parent interface becomes the gateway for the native VLAN only and all subinterfaces inherit it
- B) The parent interface routes traffic for all VLANs since it receives all tagged frames from the trunk
- C) The parent interface IP address has no effect on subinterface routing; only subinterfaces with `encapsulation dot1Q` can route VLAN-specific traffic
- D) IOS rejects the IP address on the parent interface because it already has subinterfaces configured

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: An IP address on the parent interface can serve the native VLAN (untagged traffic), but it does not become a gateway for tagged VLAN traffic. Subinterfaces with `encapsulation dot1Q` are required for tagged VLANs.
- B is incorrect: The parent interface cannot route all VLAN traffic. Each VLAN requires a dedicated subinterface with the correct `encapsulation dot1Q` command to associate tagged frames with an IP address.
- C is correct: The parent interface can optionally have an IP address for the native VLAN, but it has no role in routing traffic for tagged VLANs. Each tagged VLAN requires its own subinterface. IOS does not prevent an IP address on the parent, but it does not replace subinterface configuration.
- D is incorrect: IOS does not reject an IP address on a parent interface that has subinterfaces. Both the parent and its subinterfaces can have IP addresses simultaneously.

---

## Question 8

An SVI for VLAN 30 is configured on a multilayer switch with an IP address of 192.168.30.1/24. The SVI shows `up/down` in `show ip interface brief`. Which of the following is the most likely cause?

- A) `ip routing` is not enabled on the multilayer switch
- B) No access ports are assigned to VLAN 30, or all ports in VLAN 30 are down
- C) The SVI IP address is in the wrong subnet for VLAN 30
- D) `encapsulation dot1Q 30` has not been applied to the SVI

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Without `ip routing`, SVIs may still show `up/up` — they just do not route. The `up/down` state is not caused by a missing `ip routing` command; it is caused by the absence of active ports in the VLAN.
- B is correct: An SVI is `up/down` when the interface itself is administratively enabled but no active access ports exist in that VLAN. Run `show vlan brief` to confirm port-to-VLAN assignment and verify port operational state.
- C is incorrect: The IP address subnet does not affect SVI up/down state. A misconfigured IP address would allow the SVI to come up but would cause routing failures — not an `up/down` line protocol state.
- D is incorrect: `encapsulation dot1Q` is a router subinterface command used in ROAS configuration. SVIs on a multilayer switch do not use this command — the VLAN association is implicit in the `interface vlan [id]` command itself.

---

## Question 9

A network administrator wants to prevent attackers from capturing plaintext management credentials on a multilayer switch. Which configuration directly addresses this threat?

- A) Configure SSH for terminal access and HTTPS for web management, disabling Telnet and HTTP
- B) Apply an ACL to each SVI interface to block access from all VLANs except VLAN 99
- C) Enable `ip routing` and create a dedicated management SVI on VLAN 99
- D) Use `service password-encryption` to protect passwords stored in the configuration file

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: SSH and HTTPS encrypt management sessions in transit, preventing credential capture by a packet sniffer. Configure with `transport input ssh` on VTY lines and `ip http secure-server` for HTTPS. Disable Telnet with `transport input ssh` (removing telnet from the allowed list) and HTTP with `no ip http server`.
- B is incorrect: ACLs on SVI interfaces restrict which hosts can reach the management plane, but they do not encrypt traffic. If Telnet is still permitted on VTY lines, credentials remain plaintext regardless of SVI ACLs.
- C is incorrect: A management VLAN isolates management traffic onto a dedicated VLAN, which is a good practice, but does not encrypt credentials. Telnet on a dedicated VLAN still transmits passwords in cleartext.
- D is incorrect: `service password-encryption` applies a weak reversible cipher to passwords stored in the running-config. It does not encrypt credentials transmitted over the network during a management session.

---

## Question 10

Which verification command confirms that a multilayer switch has connected routes for both VLAN 10 (192.168.10.0/24) and VLAN 20 (192.168.20.0/24) in its routing table?

- A) `show vlan brief`
- B) `show ip interface brief`
- C) `show ip route`
- D) `show interfaces trunk`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show vlan brief` displays VLAN names, status, and which switch ports are assigned to each VLAN. It does not display Layer 3 routing information.
- B is incorrect: `show ip interface brief` displays the IP address and operational state of each interface including SVIs. It confirms IP addresses and up/down states but does not show the routing table or confirm which routes are installed.
- C is correct: `show ip route` displays the complete routing table. Connected routes (marked C) appear for each SVI subnet when `ip routing` is enabled and the SVI is up/up. This is the definitive command to verify that the switch is routing between VLANs.
- D is incorrect: `show interfaces trunk` displays trunk port status, allowed VLANs, and native VLAN. It applies to Layer 2 trunks between switches and has no relevance to Layer 3 SVI routing confirmation.

---

## Question 11

An SVI for VLAN 30 on a multilayer switch shows as `down/down` in `show ip interface brief`. Which condition is the most likely cause?

- A) The `ip routing` command has not been entered on the switch
- B) No switch ports are currently assigned to VLAN 30 and active (up)
- C) VLAN 30 does not exist in the VLAN database on the switch
- D) The SVI IP address is in the same subnet as another SVI

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: If `ip routing` is missing, SVIs will still show as up/up if configured correctly — they just will not route traffic. The absence of `ip routing` does not cause an SVI to go down/down.
- B is partially correct: An SVI with no active access ports in the VLAN will also go down/down. However, the most direct cause for a newly configured SVI being immediately down/down is the VLAN not existing in the database.
- C is correct: For an SVI to come up, three conditions must be met: (1) VLAN must exist in the VLAN database, (2) at least one access or trunk port assigned to that VLAN must be up, and (3) the SVI must not be administratively shut down. If the VLAN does not exist in the database (`show vlan brief` does not list it), the SVI will remain down/down regardless of port configuration.
- D is incorrect: A duplicate subnet on two SVIs would cause routing conflicts but would not put the SVIs in a down/down state. Both interfaces would come up, but routing would behave unexpectedly.

---

## Question 12

In a router-on-a-stick configuration, which command on the physical interface is required to allow 802.1Q subinterface traffic to pass?

- A) `switchport mode trunk`
- B) `no shutdown` (the physical interface does not require any additional commands beyond enabling it)
- C) `encapsulation dot1q native`
- D) `ip routing`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `switchport mode trunk` is a switch command. A router's physical interface does not use switchport commands — it uses subinterfaces with `encapsulation dot1q [vlan-id]`.
- B is correct: The physical parent interface in a ROAS configuration requires only `no shutdown` to be active. It does not require an IP address. The IP addresses are assigned to the subinterfaces. The only requirement is that the physical interface is up (not administratively shut down).
- C is incorrect: `encapsulation dot1q native` is applied to a subinterface, not the physical parent interface. It configures a specific subinterface to handle the native VLAN (untagged traffic).
- D is incorrect: `ip routing` is required on a multilayer switch to enable routing between SVIs. On a router, routing is always active by default. `ip routing` is not a router command in the context of enabling the routing engine.

---

## Question 13

A PC in VLAN 10 (192.168.10.0/24) sends a packet to a PC in VLAN 20 (192.168.20.0/24) via a multilayer switch with SVIs. Describe the correct path the packet takes.

- A) PC in VLAN 10 → VLAN 10 SVI (receives packet) → IP routing table lookup → VLAN 20 SVI (sends packet) → PC in VLAN 20
- B) PC in VLAN 10 → trunk uplink → router subinterface → trunk downlink → PC in VLAN 20
- C) PC in VLAN 10 → VLAN 10 SVI → dedicated inter-VLAN routing module → VLAN 20 SVI → PC in VLAN 20
- D) PC in VLAN 10 → VLAN 10 SVI → default gateway of VLAN 10 router → VLAN 20 default gateway → PC in VLAN 20

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: In SVI-based inter-VLAN routing, the packet from PC in VLAN 10 is received by the VLAN 10 SVI (acting as the default gateway). The multilayer switch performs a routing table lookup and determines the destination is in 192.168.20.0/24, which is directly connected via the VLAN 20 SVI. The packet exits through the VLAN 20 SVI and is forwarded to the destination PC.
- B is incorrect: This describes router-on-a-stick (ROAS), not SVI-based routing. ROAS uses a trunk uplink to a router with subinterfaces. SVI routing occurs entirely within the multilayer switch hardware.
- C is incorrect: There is no separate "inter-VLAN routing module" in Cisco IOS. Routing between SVIs occurs using the switch's Layer 3 hardware forwarding engine, not a separate module. The description in option A accurately represents the process.
- D is incorrect: There is not a separate VLAN 10 router and VLAN 20 router in an SVI design. A single multilayer switch acts as the default gateway for both VLANs simultaneously through its two SVIs.

---

## Question 14

A multilayer switch has `ip routing` enabled and SVIs for VLAN 10 and VLAN 20. A host in VLAN 10 can ping the VLAN 10 SVI but cannot ping any host in VLAN 20. `show ip route` shows connected routes for both VLANs. What is the most likely cause?

- A) The host in VLAN 10 has the wrong default gateway configured
- B) The VLAN 20 SVI is administratively shut down
- C) `ip routing` needs to be re-entered to refresh the routing table
- D) The hosts in VLAN 20 do not have the multilayer switch SVI as their default gateway

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: The host can ping the VLAN 10 SVI, which means the default gateway is reachable and correctly configured for VLAN 10. The problem is at the VLAN 20 end, not the VLAN 10 source.
- B is incorrect: If the VLAN 20 SVI were down, it would not appear in the routing table as a connected route. The question states both connected routes are present in `show ip route`.
- C is incorrect: Re-entering `ip routing` does not refresh the routing table. The routing table is correct — routes for both VLANs are present. The issue is not with the routing configuration on the switch.
- D is correct: If the hosts in VLAN 20 have the wrong default gateway (e.g., pointing to a different address or not configured), they will receive the ICMP packet from the VLAN 10 host (routed correctly by the switch) but will not know how to send the reply back. The symptom of one-way communication (VLAN 10 host can initiate but no reply) strongly indicates a missing or incorrect default gateway on the VLAN 20 hosts.

---

## Question 15

What happens to traffic destined for an external network (outside the switch's directly connected subnets) when inter-VLAN routing is configured on a multilayer switch but no default route is configured?

- A) Traffic is forwarded using OSPF routes learned from the upstream router
- B) Traffic is dropped with an "ICMP unreachable" message because no route exists in the routing table for the destination
- C) Traffic is forwarded out the lowest-numbered interface by default
- D) Traffic is forwarded to VLAN 1 as the default management VLAN

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: If OSPF is not configured, no OSPF routes exist. Routes are not automatically learned from neighboring routers without a routing protocol or static route.
- B is correct: If no route exists for the destination (and no default route is configured), the switch drops the packet and may send an ICMP Destination Unreachable message back to the source. This is standard IPv4 routing behavior — traffic to unknown destinations cannot be forwarded.
- C is incorrect: Cisco IOS does not use a "lowest interface" fallback for unknown destinations. Traffic with no matching route is always dropped.
- D is incorrect: VLAN 1 has no special routing role in this context. The switch does not forward unknown destinations to VLAN 1 or any other default VLAN.

---

## Question 16

In a ROAS configuration, a subinterface `GigabitEthernet0/0.20` is configured with `encapsulation dot1q 20` and IP address `192.168.20.1/24`. What must the switch trunk port connected to this router do for VLAN 20 traffic to reach the subinterface?

- A) The switch trunk must be configured with `switchport trunk allowed vlan 20`
- B) The switch trunk must use ISL encapsulation instead of 802.1Q for ROAS to work
- C) The switch trunk must remove VLAN 20 from the allowed list so frames arrive untagged
- D) No special configuration is needed on the switch trunk — ROAS automatically detects the subinterface

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: For VLAN 20 frames to cross the trunk from the switch to the router, VLAN 20 must be in the trunk's allowed VLAN list. The `encapsulation dot1q 20` on the subinterface tells the router how to interpret arriving tagged frames, but the switch must also be configured to send VLAN 20 frames over the trunk.
- B is incorrect: ISL is Cisco-proprietary and is legacy technology. Modern Cisco IOS uses 802.1Q (`encapsulation dot1q`) for ROAS subinterfaces, not ISL. Most modern platforms have dropped ISL support entirely.
- C is incorrect: Removing VLAN 20 from the allowed list would prevent VLAN 20 traffic from crossing the trunk. VLAN 20 must be in the allowed list for tagged frames to reach the router.
- D is incorrect: ROAS does not auto-detect or configure the switch trunk. The trunk configuration on the switch is completely independent of the router subinterface configuration. Both must be manually configured.

---

## Question 17

Which inter-VLAN routing method is most appropriate for a high-density enterprise campus distribution layer with 20 VLANs and thousands of users requiring low-latency routing?

- A) Router-on-a-stick (ROAS) with a single 1 Gbps uplink
- B) SVIs on a multilayer switch using hardware ASIC-based routing
- C) A dedicated firewall acting as the default gateway for each VLAN
- D) A single router with 20 physical interfaces, one per VLAN

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: ROAS funnels all inter-VLAN traffic through a single physical link, which becomes a bottleneck at high traffic volumes. It is designed for small networks, not enterprise distribution layers with thousands of users.
- B is correct: SVIs on a multilayer switch use dedicated ASIC hardware to route between VLANs at near-wire-speed without the latency of sending traffic to an external router. This is the standard enterprise solution for high-performance inter-VLAN routing at the Distribution layer.
- C is incorrect: Firewalls introduce latency and are designed for security inspection, not high-throughput inter-VLAN routing. Using a firewall as the default gateway for every VLAN in a large campus is a design anti-pattern for performance reasons.
- D is incorrect: A router with 20 physical interfaces (one per VLAN) is cost-prohibitive and impractical. Enterprise routers rarely have 20 LAN interfaces. SVIs on a multilayer switch provide the same functionality at a fraction of the cost and with better performance.

---

## Question 18

An engineer adds VLAN 30 to a trunk between a Layer 2 switch and a multilayer switch. The multilayer switch has `ip routing` enabled. What additional step is required to enable routing for hosts in VLAN 30?

- A) Create VLAN 30 in the VLAN database and configure an SVI with an IP address for VLAN 30
- B) Add a static route pointing to the VLAN 30 subnet
- C) Enable `ip routing` again — it must be re-entered whenever a new VLAN is added
- D) Configure a new subinterface on the trunk port of the multilayer switch

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: To enable routing for a new VLAN, two things must be done: (1) VLAN 30 must exist in the VLAN database (`vlan 30` in global config), and (2) an SVI must be created (`interface vlan 30`) and assigned an IP address. With `ip routing` already enabled, the new SVI subnet will automatically appear as a connected route in the routing table once the SVI is up.
- B is incorrect: Static routes are used to reach networks that are not directly connected. VLAN 30 will be directly connected via the SVI — no static route is needed for the directly connected subnet.
- C is incorrect: `ip routing` is a global switch function that enables Layer 3 routing on the switch. It does not need to be re-entered when new VLANs are added. It persists across VLAN additions.
- D is incorrect: Multilayer switches with SVIs do not use subinterfaces. Subinterfaces are used on routers for ROAS. Multilayer switches use logical SVI interfaces instead.

---

## Question 19

Why does a router-on-a-stick configuration experience degraded performance compared to SVI-based inter-VLAN routing in high-traffic environments?

- A) ROAS uses a software routing table while SVIs use hardware ASIC routing
- B) ROAS requires all inter-VLAN traffic to traverse the same physical uplink twice (once in each direction), creating a bandwidth bottleneck on that single link
- C) ROAS cannot route more than 10 VLANs simultaneously
- D) ROAS introduces additional TCP sequence number processing for each subinterface

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Both ROAS (on a router) and SVIs (on a multilayer switch) can use hardware-based routing in their respective devices. The performance difference is primarily about link utilization, not routing table implementation.
- B is correct: In ROAS, all inter-VLAN traffic must cross the single physical uplink between the switch and the router — once in the inbound direction (source VLAN to router) and once in the outbound direction (router back to destination VLAN). This double traversal of a single physical link creates a bottleneck. SVIs route traffic internally within the switch ASIC without using any external links.
- C is incorrect: ROAS has no built-in limit on the number of VLANs it can route. The limit is the number of subinterfaces supported by the IOS image and router hardware, which is typically in the hundreds or thousands.
- D is incorrect: ROAS does not process TCP sequence numbers. Routing is a Layer 3 function that forwards packets based on IP destination. TCP sequence numbers are a Layer 4 concern that routers do not modify.

---

## Question 20

A host at 172.16.10.100/24 with default gateway 172.16.10.1 sends a packet to 172.16.20.200/24. The multilayer switch has SVI 172.16.10.1 and SVI 172.16.20.1. What source and destination MAC addresses does the packet carry when it arrives at the VLAN 20 destination host?

- A) Source: host MAC of 172.16.10.100 / Destination: host MAC of 172.16.20.200
- B) Source: MAC of SVI 172.16.10.1 / Destination: MAC of SVI 172.16.20.1
- C) Source: MAC of SVI 172.16.20.1 / Destination: MAC of 172.16.20.200
- D) Source: MAC of 172.16.10.100 / Destination: MAC of SVI 172.16.20.1

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: When a packet crosses a router or Layer 3 switch boundary, the Layer 2 frame is re-created for the new segment. The source and destination MAC addresses are updated at each hop. The original source host MAC is not preserved across inter-VLAN routing.
- B is incorrect: The source MAC on the outbound frame is the MAC of the exit interface (SVI 172.16.20.1), not the MAC of the incoming SVI (172.16.10.1). The destination MAC is the destination host's MAC address, not the SVI MAC.
- C is correct: After inter-VLAN routing, the multilayer switch builds a new Layer 2 frame for the VLAN 20 segment. The source MAC is the MAC address of the VLAN 20 SVI (the exit interface, 172.16.20.1) and the destination MAC is the MAC address of 172.16.20.200 (resolved via ARP). This is standard Layer 3 routing behavior.
- D is incorrect: Once the packet crosses from VLAN 10 to VLAN 20 via the switch, the source MAC is updated to the VLAN 20 SVI MAC, not the original host MAC. The destination MAC is the target host's MAC, which is correct here.
