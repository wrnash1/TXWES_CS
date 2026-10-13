# Quiz: Module 16 — CCNA 200-301 Exam Preparation and Capstone

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Instructions

This capstone quiz covers all six CCNA 200-301 exam domains. Select the single best answer for each question. Each question is worth 5 points (20 questions, 100 points total).

---

## Question 1

A host at 172.16.5.200/20 needs to communicate with a host at 172.16.14.100/20. Are these hosts on the same subnet?

A. Yes — both are within the 172.16.0.0/20 network.

B. No — 172.16.5.200/20 is in 172.16.0.0/20 but 172.16.14.100/20 is in 172.16.0.0/12.

C. No — they are in different /20 blocks and require inter-VLAN routing.

D. Yes — /20 masks always place all 172.16.x.x addresses in the same subnet.

Correct Answer: A — A /20 mask is 255.255.240.0. For 172.16.x.x/20, the block size in the third octet is 16. Starting at 172.16.0.0/20, the block covers 172.16.0.x through 172.16.15.x. Both 172.16.5.200 and 172.16.14.100 fall within this range. Both are in 172.16.0.0/20.

Distractor Analysis:

* B — /12 is a much larger block (172.16.0.0–172.31.255.255). This mixes up CIDR prefix lengths.
* C — Both hosts are in the same /20 block (0–15 in the third octet). A second /20 block would start at 172.16.16.0.
* D — /20 does not cover all 172.16.x.x. That range requires /16.

---

## Question 2

Four switches participate in STP. Switch A has priority 28672. Switches B, C, and D each have the default priority 32768. Switch C has the lowest MAC address among B, C, and D. Which switch becomes the root bridge?

A. Switch A

B. Switch B

C. Switch C

D. Switch D

Correct Answer: A — The root bridge is elected by the lowest bridge ID. Bridge ID equals priority plus VLAN ID plus MAC. Switch A has priority 28672 versus 32768 for all others. A lower priority always wins regardless of MAC address. Switch A becomes the root bridge.

Distractor Analysis:

* B, C, D — These switches all have priority 32768. Among them Switch C would win (lowest MAC), but Switch A's lower priority takes precedence over all three.

---

## Question 3

An OSPF adjacency between two routers is stuck in the EXSTART state. What is the most likely cause?

A. Mismatched hello and dead intervals between the two routers.

B. Duplicate OSPF router IDs on both routers.

C. Mismatched area IDs on the connected interfaces.

D. The interface toward the neighbor is in the passive-interface state.

Correct Answer: B — EXSTART is the state where master/slave negotiation and initial sequence number exchange occurs. If both routers have the same router ID, they cannot resolve the negotiation and the adjacency freezes in EXSTART.

Distractor Analysis:

* A — Mismatched hello/dead intervals prevent the neighbor from progressing past the INIT state, not EXSTART.
* C — Mismatched area IDs would prevent full adjacency but typically manifest differently. Routers in different areas can still form adjacencies on the boundary.
* D — A passive interface would not send or receive hellos. The neighbor would never appear at all.

---

## Question 4

The output of `show ip nat translations` shows: Inside local 10.0.0.50 — Inside global 203.0.113.5. What does the inside global address represent?

A. The private IP of the internal host assigned by DHCP.

B. The public IP representing the internal host as seen from the Internet.

C. The IP address of the NAT router's inside interface.

D. The actual IP of the external destination server.

Correct Answer: B — Inside global is the public IP address that represents the inside host to external parties. When 10.0.0.50 sends traffic outbound, NAT replaces the source address with 203.0.113.5. The inside local (10.0.0.50) is the actual private IP assigned to the host.

Distractor Analysis:

* A — The private IP of the host is the inside local address.
* C — The router's inside interface IP is typically the default gateway for inside hosts, not the inside global address.
* D — The external destination's IP is the outside global address, which is a separate NAT concept.

---

## Question 5

A routing table entry reads: `O 192.168.5.0/24 [110/2] via 10.0.0.2`. What does the value 110 represent?

A. The OSPF process ID

B. The administrative distance of OSPF

C. The OSPF cost (metric) to reach 192.168.5.0/24

D. The OSPF hello interval in seconds

Correct Answer: B — In routing table entries, the format is `[AD/metric]`. The first number is administrative distance; the second is the metric. OSPF has a default administrative distance of 110. The metric (cost) is 2 in this entry.

Distractor Analysis:

* A — OSPF process ID is configured with `router ospf X` and does not appear in routing table entries.
* C — The OSPF cost (metric) is the second number in brackets, which is 2 here.
* D — Hello intervals are OSPF operational timers and do not appear in routing table entries.

---

## Question 6

Which syslog severity level indicates a condition requiring immediate action while the system remains operational?

A. Level 0 — Emergencies

B. Level 1 — Alerts

C. Level 2 — Critical

D. Level 3 — Errors

Correct Answer: B — Level 1 Alerts requires immediate action. Level 0 Emergencies indicates the system is unusable. The key distinction is that Alerts are urgent but the system can still function, while Emergencies indicate system failure.

Distractor Analysis:

* A — Level 0 Emergencies means the system itself is unusable, which is more severe than Alerts.
* C — Level 2 Critical indicates critical conditions but is less urgent than Alerts.
* D — Level 3 Errors needs attention but is not immediate like Alerts.

---

## Question 7

A switch port is in err-disabled state after a port-security violation. Which of the following are valid methods to restore port operation?

A. `no switchport port-security` removes and re-adds security.

B. `shutdown` followed by `no shutdown` on the interface.

C. `errdisable recovery cause psecure-violation` with a recovery interval.

D. Both B and C are valid methods.

Correct Answer: D — Both the manual shutdown/no shutdown method and the configured automatic recovery method are valid. The shutdown/no shutdown immediately restores the port; automatic recovery restores it after the configured timer expires.

Distractor Analysis:

* A — Removing port-security clears all sticky MAC entries, which is destructive and not the standard recovery method.
* B alone — Correct but incomplete since C is also valid.
* C alone — Correct but incomplete since B is also valid.

---

## Question 8

An HSRP group is configured. Router A has priority 120 and Router B has priority 100. Router A fails and Router B becomes active. When Router A recovers, what must be configured on Router A to ensure it reclaims the active role?

A. `standby 1 priority 120`

B. `standby 1 preempt`

C. `standby 1 track 1 decrement 30`

D. `standby 1 timers 1 3`

Correct Answer: B — `standby 1 preempt` allows a higher-priority router to reclaim the active role after returning from a failure. Without preempt, the router that became active during the outage (Router B) remains active regardless of Router A's higher priority.

Distractor Analysis:

* A — Setting priority is required but insufficient alone. Preempt must be separately configured to trigger role recovery.
* C — Interface tracking adjusts priority dynamically when a tracked interface fails. It does not control post-recovery role reclamation.
* D — HSRP timers control failover detection speed, not role recovery after restoration.

---

## Question 9

Which command displays the current DHCP snooping status including trusted ports and active VLANs?

A. `show ip dhcp server`

B. `show ip dhcp snooping`

C. `show ip arp inspection`

D. `show dhcp lease`

Correct Answer: B — `show ip dhcp snooping` displays whether snooping is globally enabled, which VLANs are protected, which ports are trusted, and the Option 82 setting. This is the primary verification command for DHCP snooping configuration.

Distractor Analysis:

* A — `show ip dhcp server` is not a valid Cisco IOS command.
* C — `show ip arp inspection` verifies DAI status, not DHCP snooping.
* D — `show dhcp lease` is not a standard Cisco IOS command; lease info is shown with `show ip dhcp binding`.

---

## Question 10

In an 802.1X deployment, which device communicates directly with the RADIUS server using RADIUS protocol?

A. The user's laptop (supplicant)

B. The switch port (authenticator)

C. The default gateway router

D. The DHCP server

Correct Answer: B — The switch port (authenticator) communicates with the RADIUS server using the RADIUS protocol. The supplicant communicates with the authenticator using EAPOL (EAP over LAN). The authenticator encapsulates EAPOL messages in RADIUS packets and forwards them to the authentication server.

Distractor Analysis:

* A — The supplicant communicates with the switch using EAPOL, not directly with the RADIUS server.
* C — The default gateway has no role in 802.1X authentication.
* D — The DHCP server provides IP addressing after authentication. It is not part of the 802.1X authentication exchange.

---

## Question 11

Which IPv6 address type is automatically assigned to every IPv6-capable interface and is only valid for local-link communication?

A. Global unicast (2000::/3)

B. Unique local (FC00::/7)

C. Link-local (FE80::/10)

D. Multicast (FF00::/8)

Correct Answer: C — Link-local addresses in the FE80::/10 range are automatically configured on every IPv6-enabled interface. They are valid only within a single network segment and are never routed beyond the local link. They are essential for neighbor discovery and routing protocol exchanges.

Distractor Analysis:

* A — Global unicast addresses are routable on the Internet and are not automatically assigned to every interface.
* B — Unique local addresses are private-scope and not automatically assigned.
* D — Multicast addresses represent delivery groups, not individual interface addresses.

---

## Question 12

Which combination of evidence most directly confirms a full OSPF adjacency with a neighbor?

A. `show ip route ospf` shows routes from the neighbor only.

B. `show ip ospf neighbor` shows the neighbor in FULL state only.

C. `show ip interface brief` shows the neighbor-facing interface as Up/Up only.

D. Both A and B together confirm full adjacency.

Correct Answer: D — `show ip ospf neighbor` showing FULL is the direct confirmation of adjacency state. Routes appearing in `show ip route ospf` also confirm that OSPF has exchanged LSAs and completed SPF. Together they provide definitive confirmation.

Distractor Analysis:

* A alone — Routes in the table imply full adjacency but do not explicitly show the adjacency state.
* B alone — Correct and most direct, but D is more complete.
* C — An Up/Up interface is required for OSPF to run but does not confirm that adjacency was established.

---

## Question 13

Which command configures a floating static route to 192.168.5.0/24 via 10.0.0.2 that will only be used if the OSPF-learned route disappears?

A. `ip route 192.168.5.0 255.255.255.0 10.0.0.2 111`

B. `ip route 192.168.5.0 255.255.255.0 10.0.0.2 1`

C. `ip route 192.168.5.0 255.255.255.0 10.0.0.2`

D. `ip route 0.0.0.0 0.0.0.0 10.0.0.2 111`

Correct Answer: A — A floating static route requires an administrative distance higher than the backing dynamic protocol. OSPF has AD 110. Setting the static route to AD 111 makes it install only when no OSPF route exists. The syntax appends the AD after the next-hop: `ip route network mask next-hop AD`.

Distractor Analysis:

* B — AD 1 would permanently prefer this static route over OSPF (AD 110), defeating the floating purpose.
* C — Default static route AD is 1, which always overrides OSPF. Not a floating static.
* D — This configures a default route, not a specific /24 prefix.

---

## Question 14

A Python script calls the DNA Center REST API and receives HTTP status code 403. What is the correct interpretation?

A. The authentication token has expired.

B. The URL endpoint does not exist.

C. The authenticated user lacks permission for the requested operation.

D. The server encountered an internal processing error.

Correct Answer: C — HTTP 403 Forbidden means the client is authenticated but not authorized. The server knows who the client is but the client's role does not permit the requested operation. This is distinct from 401 (not authenticated at all).

Distractor Analysis:

* A — An expired token returns 401 Unauthorized. 401 vs. 403 is a common exam distinction.
* B — A non-existent endpoint returns 404 Not Found.
* D — A server internal error returns 500 Internal Server Error.

---

## Question 15

Which transport protocol and port does NETCONF use?

A. HTTPS, TCP 443

B. SSH, TCP 830

C. HTTPS, TCP 8443

D. SSH, TCP 22

Correct Answer: B — NETCONF is transported over SSH on TCP port 830, as defined in RFC 4742. Port 830 is dedicated to NETCONF to allow firewalls to differentiate it from standard SSH management sessions on port 22.

Distractor Analysis:

* A — RESTCONF uses HTTPS on port 443. This is a common NETCONF/RESTCONF confusion trap.
* C — Port 8443 is sometimes used for RESTCONF in non-standard configurations, not NETCONF.
* D — Port 22 is standard SSH for CLI management. NETCONF uses the dedicated port 830.

---

## Question 16

A network engineer is configuring a Cisco WLC and needs traffic on SSID "CORP" to be placed in VLAN 10. What must she create on the WLC to map this WLAN to VLAN 10?

A. A VLAN access map

B. A dynamic interface

C. A service port interface

D. A virtual interface

Correct Answer: B — A dynamic interface on the Cisco WLC defines the VLAN ID, IP address, and DHCP server for a given WLAN. The CORP WLAN configuration references this dynamic interface to ensure client traffic is tagged with VLAN 10 when it reaches the wired network.

Distractor Analysis:

* A — VLAN access maps are a Catalyst switch security feature unrelated to WLC WLAN mapping.
* C — The service port is for out-of-band management of the WLC hardware, not for WLAN-to-VLAN mapping.
* D — The virtual interface handles DHCP relay and web authentication portal functions, not WLAN-to-VLAN mapping.

---

## Question 17

A network manager needs to automate configuration of 300 Cisco IOS switches. No software may be installed on the switches. Which tool meets this requirement?

A. Puppet — uses a declarative language

B. Chef — uses Ruby Cookbooks

C. Ansible — agentless, communicates over SSH

D. NETCONF — uses SSH port 830

Correct Answer: C — Ansible is agentless and requires no software on managed devices. It uses SSH to communicate with Cisco IOS devices via the cisco.ios Ansible collection. This is the only tool listed that operates without an agent on the managed switch.

Distractor Analysis:

* A — Puppet requires a Puppet agent on managed nodes. Network switches typically cannot run a Puppet agent.
* B — Chef requires a Chef client on managed nodes. Same limitation as Puppet.
* D — NETCONF is a configuration protocol, not an automation framework. It does not replace Ansible's orchestration capabilities.

---

## Question 18

Which two 2.4 GHz channels should adjacent access points use to avoid channel overlap?

A. Channels 1 and 2

B. Channels 1 and 6

C. Channels 6 and 7

D. Channels 3 and 9

Correct Answer: B — Only channels 1, 6, and 11 are non-overlapping in the US 2.4 GHz band. Adjacent APs must use different channels from this set. Channels 1 and 6 are non-overlapping and are a correct assignment for two adjacent APs.

Distractor Analysis:

* A — Channels 1 and 2 overlap significantly. Their centers are only 5 MHz apart but each channel is 22 MHz wide.
* C — Channels 6 and 7 overlap in the same way as channels 1 and 2.
* D — Channels 3 and 9 are partially overlapping and neither is in the standard non-overlapping set.

---

## Question 19

A switch port has sticky port security with violation shutdown and a maximum of 1 MAC address. One sticky MAC is already learned. A second device is connected. What happens?

A. The second MAC is added since the default maximum is 2.

B. The port enters err-disabled state immediately.

C. The second device's frames are silently dropped; the port stays up.

D. A syslog message is generated and the second device communicates normally.

Correct Answer: B — The default port-security maximum is 1. With violation shutdown, any frame from a second MAC exceeds the maximum and triggers err-disabled state immediately.

Distractor Analysis:

* A — The default maximum is 1, not 2. A second device violates the policy unless maximum is explicitly raised.
* C — Silent dropping describes the protect violation mode, not shutdown.
* D — Logging with continued connectivity describes the restrict violation mode, not shutdown.

---

## Question 20

Hosts in VLAN 10 cannot ping hosts in VLAN 20. The Layer 3 switch has correctly addressed SVIs for both VLANs. Which single command is most likely missing?

A. `spanning-tree vlan 10 priority 4096`

B. `ip routing`

C. `ip default-gateway 192.168.10.1`

D. `switchport trunk allowed vlan 10,20`

Correct Answer: B — On a Layer 3 switch, `ip routing` must be explicitly enabled to activate the routing engine. Without it, SVIs are configured but the switch does not route between them. This is the single most common omission in inter-VLAN routing configurations.

Distractor Analysis:

* A — Spanning Tree priority affects root bridge election and has no effect on routing between VLANs.
* C — `ip default-gateway` is for Layer 2 switches without ip routing enabled. It does not enable inter-VLAN routing.
* D — Trunk allowed VLANs affect which VLANs cross uplinks. If hosts on each VLAN can reach their default gateway, VLAN trunking is already working.

---

---

## Question 21

A network engineer receives a complaint that PC-A can reach PC-B within the same VLAN but cannot reach PC-C in a different VLAN. Both PCs receive valid IP addresses and correct default gateways from DHCP. OSPFv2 is running between the access switches and the core switch. What is the most likely root cause?

A. The trunk port connecting the access switch to the core switch does not allow PC-C's VLAN.

B. PC-A's ARP cache is stale and needs to be cleared.

C. The default gateway IP on the SVI for PC-A's VLAN is not reachable because OSPFv2 is down.

D. PAT is translating PC-A's packets and removing the destination MAC address.

Correct Answer: A — Intra-VLAN connectivity works (PC-A to PC-B) but inter-VLAN connectivity fails. With correct IP addresses and gateways, the most likely Layer 2 cause is that PC-C's VLAN is not allowed on the trunk connecting the switches. If the trunk does not carry VLAN traffic for PC-C's VLAN, frames never reach the routing engine. Verify with `show interfaces trunk` on the core switch.

Distractor Analysis:

* B — A stale ARP cache affects a specific host-to-host communication attempt but would not produce the consistent symptom of all inter-VLAN traffic failing for PC-A. ARP issues resolve on the next ARP refresh cycle.
* C — If OSPFv2 were down, all inter-VLAN routing would fail for all hosts. The scenario is specific to PC-A failing to reach PC-C, making a VLAN configuration issue more likely than a global OSPF outage.
* D — PAT only translates addresses on the NAT router's outside interface for internet-bound traffic. It does not affect inter-VLAN communication on the internal network.

---

## Question 22

A network engineer runs `show ip route` on R1 and sees:

```text
S*   0.0.0.0/0 [1/0] via 203.0.113.254
O    192.168.10.0/24 [110/2] via 10.0.0.2, GigabitEthernet0/0
C    10.0.0.0/30 is directly connected, GigabitEthernet0/0
```

A packet arrives for destination 8.8.8.8. Which entry does the router use and why?

A. The router drops the packet because 8.8.8.8 does not match any specific route.

B. The router uses the OSPF route to 192.168.10.0/24 because OSPF is the most trusted protocol.

C. The router uses the static default route `S* 0.0.0.0/0` because it matches all destinations not covered by more specific routes.

D. The router uses the connected route to 10.0.0.0/30 because directly connected routes have administrative distance 0.

Correct Answer: C — The default route `0.0.0.0/0` matches any destination. It is the gateway of last resort. When a packet's destination matches no more specific route, the router uses the default route. 8.8.8.8 does not match 192.168.10.0/24 or 10.0.0.0/30, so the default route is the match. The packet is forwarded to 203.0.113.254.

Distractor Analysis:

* A — Routers do not drop packets just because no specific host or subnet route exists. The default route `0.0.0.0/0` is specifically designed to match any destination and prevent this drop.
* B — Longest prefix match is the routing decision rule, not protocol trustworthiness. The OSPF route matches only 192.168.10.0/24 prefixes and does not match 8.8.8.8.
* D — While connected routes have AD 0, the connected route 10.0.0.0/30 does not match 8.8.8.8. The router uses longest prefix match, not lowest AD, as the primary selection criterion when multiple routes exist for the same destination.

---

## Question 23

Which of the following correctly describes the purpose of the Spanning Tree Protocol in an enterprise network?

A. STP prevents routing loops in Layer 3 networks by poisoning routes that form cycles.

B. STP prevents Layer 2 forwarding loops by placing redundant switch paths into a blocking state.

C. STP provides load balancing across all active redundant links between switches.

D. STP encrypts traffic on trunk ports to prevent VLAN hopping between switches.

Correct Answer: B — STP (and RSTP/PVST+) solves the Layer 2 broadcast storm problem created by redundant switch paths. Without STP, a broadcast frame would loop indefinitely around a redundant topology. STP elects a root bridge and calculates a loop-free tree by blocking all redundant paths except the lowest-cost path to the root. Blocked ports can unblock if the primary path fails.

Distractor Analysis:

* A — Route poisoning is a distance-vector routing protocol mechanism for preventing Layer 3 routing loops (used in RIP). STP operates at Layer 2 and has no knowledge of IP routes.
* C — Basic STP does not load balance — it blocks redundant links entirely. Load balancing across VLANs is possible with PVST+ by placing different VLANs on different root bridges, but STP's primary purpose is loop prevention, not load balancing.
* D — STP has no encryption capability. 802.1AE (MACsec) provides Layer 2 encryption. VLAN hopping prevention is addressed by native VLAN configuration and port hardening, not STP.

---

## Question 24

An engineer runs `show ip ospf neighbor` on R1 and sees no output. R1's OSPF configuration appears correct. Which of the following would NOT cause this symptom?

A. The interface connecting to the neighbor is configured as a passive interface.

B. The OSPF area number on R1's connecting interface does not match the neighbor's area number.

C. The OSPF process ID on R1 (router ospf 1) is different from the neighbor's process ID (router ospf 2).

D. The MTU on R1's interface is 1500 but the neighbor's interface MTU is 9000.

Correct Answer: C — The OSPF process ID is locally significant and does not need to match between neighbors. Two routers with `router ospf 1` and `router ospf 99` will still form an adjacency as long as area IDs, Hello/Dead timers, subnet masks, and MTU match. This is a commonly tested OSPF misconception.

Distractor Analysis:

* A — A passive interface does not send or receive OSPF Hello packets. If the connecting interface is passive on either router, adjacency cannot form — this IS a valid cause.
* B — OSPF requires both ends of a link to be in the same area. An area mismatch prevents adjacency — this IS a valid cause.
* D — An MTU mismatch causes the OSPF adjacency to get stuck in the Exstart or Exchange state rather than reaching Full. If the mismatch is severe, the adjacency may never complete — this IS a valid cause.

---

## Question 25

A PAT-enabled router is receiving requests from inside hosts to reach external servers. An inside host at 192.168.1.100 port 54321 has an active translation. The same host then opens a new connection from port 54321 to a different external server. How does PAT handle this?

A. PAT rejects the second connection because port 54321 is already in use by the first translation.

B. PAT creates a second translation entry with a different inside global port number to distinguish the two sessions.

C. PAT merges both connections into the same translation entry sharing port 54321.

D. PAT drops the second connection until the first translation times out.

Correct Answer: B — PAT tracks sessions using the combination of inside local IP + inside local port + outside destination IP + outside destination port. When the same inside host opens a connection to a different server, the outside destination is different, so PAT creates a separate translation entry. Each session is uniquely identified in the translation table. The inside global port may be reassigned or kept the same depending on whether there is a port conflict on the outside.

Distractor Analysis:

* A — PAT does not reject connections based on port reuse on the inside local side. Port uniqueness is maintained on the inside global (public) side. Multiple inside sessions can use the same local port number.
* C — PAT never merges translation entries. Each session has its own row in the NAT translation table with unique identifying information.
* D — PAT does not queue or hold connections pending timeout. It handles multiple simultaneous connections continuously.

---

## Question 26

A network engineer is implementing IPv6 on a campus network. All routers are configured with OSPFv3. A PC on one subnet can ping its local router's IPv6 address but cannot reach a PC on a different subnet. The engineer checks `show ipv6 route` on the intermediate router and sees no OSPFv3 routes. What is the most likely cause?

A. IPv6 unicast routing is not enabled on the router (`ipv6 unicast-routing` is missing).

B. OSPFv3 uses a different multicast address than OSPFv2 and the router has blocked it.

C. The PC's link-local address is being used as the next-hop and cannot be routed between subnets.

D. OSPFv3 requires GRE tunnels between all routers to carry IPv6 routing updates.

Correct Answer: A — `ipv6 unicast-routing` must be explicitly enabled on Cisco IOS routers before IPv6 routing (including OSPFv3) functions. Without this command, the router processes IPv6 packets only for its directly connected interfaces and does not forward or participate in dynamic IPv6 routing protocols. This is the IPv6 equivalent of the `ip routing` command on Layer 3 switches.

Distractor Analysis:

* B — OSPFv3 does use different multicast addresses (FF02::5 for All OSPF Routers, FF02::6 for All DR Routers) compared to OSPFv2. However, these are well-known link-local multicast addresses that are handled correctly by default. Blocking them would require an explicit ACL.
* C — Link-local addresses are never used as next-hops for inter-subnet routing in the user data plane. When OSPFv3 learns routes, it uses the link-local next-hop of the neighboring router, not the PC's link-local address.
* D — OSPFv3 runs natively over IPv6 without GRE tunnels. GRE tunneling for IPv6 is one of several IPv6 transition mechanisms (like 6to4) but is not required for OSPFv3 operation.

---

## Question 27

A Cisco CCNA candidate reviews a network diagram showing a hub-and-spoke topology with eight spoke sites. How many virtual circuits (or logical connections) are required for full mesh connectivity between all nine sites (1 hub + 8 spokes)?

A. 8

B. 16

C. 36

D. 72

Correct Answer: C — The formula for full mesh connections is n(n-1)/2 where n is the number of sites. For 9 sites: 9 × 8 / 2 = 36 unique connections required. Full mesh ensures every site has a direct path to every other site without traversing the hub. This number grows rapidly — 36 connections for 9 sites demonstrates why hub-and-spoke is commonly preferred for cost and operational simplicity.

Distractor Analysis:

* A — 8 connections describes only the hub-and-spoke model where each spoke connects only to the hub. Full mesh requires many more connections.
* B — 16 is not produced by the full mesh formula for any common network size near 9. It may represent a miscalculation doubling the spoke count.
* D — 72 = 9 × 8 (without dividing by 2). This counts each connection twice (once from each endpoint). The correct formula divides by 2 because each link is shared between two endpoints.

---

## Question 28

A switch has the following port security configuration on GigabitEthernet0/5:

```text
Maximum MAC Addresses: 3
Total MAC Addresses: 3
Configured MAC Addresses: 1
Sticky MAC Addresses: 2
Violation Mode: Restrict
```

A fourth device connects to the port. What happens?

A. The port shuts down because the maximum is exceeded.

B. The fourth device's frames are dropped; the violation counter increments; a syslog message is generated.

C. The fourth device's MAC address replaces the oldest sticky entry.

D. The fourth device is allowed because the configured MAC is static and does not count against the maximum.

Correct Answer: B — The maximum is 3 MACs (1 configured static + 2 learned sticky). With violation mode set to restrict, any frame from a fourth (unknown) MAC is dropped silently and the violation counter increments with a syslog message. The port does not shut down in restrict mode. The configured and sticky MACs all count toward the maximum.

Distractor Analysis:

* A — Port shutdown (err-disabled) only occurs in shutdown violation mode, not restrict. The configuration shows restrict mode.
* C — Port security does not implement a MAC aging or replacement algorithm. Sticky MACs become static entries in the running config. A new MAC exceeding the maximum is a violation event.
* D — All MAC address types (configured, sticky, and dynamically learned) count toward the maximum. There is no exception for configured static MACs.

---

## Question 29

A network engineer is troubleshooting a WAN link between two routers. `show interface Serial0/0/0` shows the line protocol is up but `show ip ospf neighbor` shows no neighbors. All other OSPF settings appear correct. What is the most likely cause?

A. The serial interface does not support OSPF — use a GRE tunnel instead.

B. The interface is configured as passive-interface in the OSPF process.

C. The serial clock rate has not been set on the DCE end of the cable.

D. The OSPF Dead interval has expired because the Hello interval was changed on only one router.

Correct Answer: D — If the Hello timer is changed on one router but not the other, the Hello packets from one router will be ignored by the neighbor (different Hello interval = OSPF rejects the neighbor). Since the Dead timer is typically 4x the Hello interval, if the Hello interval does not match, adjacency cannot form. The line protocol being `up` confirms the physical/data-link layer is working — the issue is at the OSPF protocol layer.

Distractor Analysis:

* A — Serial interfaces fully support OSPF. They form point-to-point OSPF adjacencies without the need for GRE. This is a common lab topology for OSPF practice.
* C — If the clock rate were missing on the DCE end, the serial interface line protocol would be `down`, not `up`. The scenario states line protocol is up, ruling out a clock rate issue.
* B — Passive interface prevents Hello packets from being sent or received. If the interface were passive, it is a valid cause of no neighbors. However, the question specifies "all other OSPF settings appear correct" — a passive interface misconfiguration is implied as ruled out, making the timer mismatch the better answer for a more subtle misconfiguration.

---

## Question 30

An enterprise network is undergoing a security audit. The auditor identifies that all management access to core switches uses Telnet on VTY lines. Which combination of changes improves the security of management access?

A. Replace Telnet with SSH, restrict VTY access with an ACL, and enable `service password-encryption`.

B. Replace Telnet with TFTP for configuration transfers and disable all VTY lines.

C. Configure a banner MOTD and increase the VTY timeout to 30 minutes.

D. Enable port security on all access ports and change the enable secret password.

Correct Answer: A — This addresses the three most critical management security concerns: (1) SSH replaces Telnet, providing encrypted management sessions instead of cleartext; (2) an ACL on the VTY lines restricts which source IP addresses can initiate SSH sessions; (3) `service password-encryption` encrypts all plaintext passwords in the running configuration. Together these form a comprehensive management plane hardening posture.

Distractor Analysis:

* B — TFTP is an unencrypted file transfer protocol — replacing Telnet with TFTP does not improve interactive management security. Disabling all VTY lines would prevent any remote management, which is operationally unacceptable.
* C — A banner MOTD provides a legal disclaimer but does not encrypt sessions or restrict access. Increasing the VTY timeout to 30 minutes actually worsens security by leaving idle sessions open longer.
* D — Port security and enable secret are both good security practices but address different vectors. Port security protects switch ports from unauthorized physical devices. Changing the enable password improves privilege escalation security. Neither addresses the Telnet management session encryption problem identified in the audit.

---

End of Quiz — Module 16 | 30 Questions | 150 Points
