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
