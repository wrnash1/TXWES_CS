# Quiz: Module 07 – Troubleshooting, Capstone Lab & Final Exam
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: December 11, 2026 at 11:59 PM CST

---

> **Instructor Note:** Enter these questions into Canvas as a timed Quiz (30 minutes, 1 attempt, no backtracking). Set questions to randomize order. All questions are CCNP Enterprise–style scenario questions covering the full course.

---

### Question 1 (Multiple Choice — 10 pts)
An OSPF neighbor relationship between R2 and R3 is stuck in the **EXSTART** state. Both routers are Cisco IOS-XE, connected via a shared Ethernet segment. `show ip ospf neighbor` shows the neighbor oscillating between EXSTART and DOWN. Which two conditions are the most likely causes? (Select two)

- A) The OSPF area numbers are different on R2 and R3. ❌
- B) The MTU values are mismatched between R2 and R3's connecting interfaces — OSPF Database Description (DBD) packets are being dropped because they exceed the lower MTU. ✅
- C) R2 and R3 have duplicate OSPF Router IDs — both are trying to be the Master in the DBD exchange and neither yields. ✅
- D) The OSPF hello and dead timers are mismatched between R2 and R3. ❌
- E) R2 is configured as a stub router (`max-metric router-lsa`) — this prevents DBD exchange. ❌

**Answer:** B and C — EXSTART is the state where two OSPF neighbors negotiate Master/Slave roles by exchanging DBD packets with sequence numbers. It gets stuck when: (1) **MTU mismatch** causes DBD packets to be dropped (R3 sends a 1500-byte DBD, R2's interface MTU is 1400 — the packet is dropped, R2 keeps retransmitting). Fix: `ip ospf mtu-ignore` on one or both interfaces, or correct the MTU. (2) **Duplicate Router IDs** cause both routers to generate DBDs claiming to be Master (higher Router ID wins Master role, but if IDs are equal, the exchange loops). Fix: ensure each router has a unique Router ID.

**Distractor Analysis:**
- A: Mismatched area numbers would prevent the neighbor from ever reaching INIT/2-WAY — the neighbor would not appear at all if hellos are being exchanged in different areas.
- D: Timer mismatches prevent the neighbor from reaching 2-WAY — the relationship would not even reach EXSTART.
- E: `max-metric router-lsa` marks a router as an overloaded stub but does not prevent DBD exchange.

---

### Question 2 (Multiple Choice — 10 pts)
A BGP session between R1 (AS 65001) and R4 (AS 65002) is in Established state. R1 has a route to 192.168.50.0/24 in its routing table, but R4 is not receiving this prefix via BGP. `show ip bgp neighbors R4 advertised-routes` on R1 shows 192.168.50.0/24 is NOT being advertised. What are the two most likely causes?

- A) The route 192.168.50.0/24 exists in R1's routing table but was learned via OSPF and has not been redistributed into BGP, OR there is an outbound prefix-list or route-map on R1 filtering this prefix toward R4. ✅
- B) R4's `maximum-prefix` limit has been reached — R1 stopped advertising new prefixes. ❌
- C) BGP synchronization is enabled on R1 — the OSPF-learned route is not being synchronized with the BGP table. ✅
- D) The BGP session is in ACTIVE state — routes are only exchanged in ESTABLISHED state. ❌

**Answer:** A and C — Two independent causes can explain a route in the routing table not being advertised via BGP: (1) The route was learned via an IGP and was never redistributed or originated into BGP. BGP only advertises routes that are in the BGP table — IGP routes must be explicitly added via `network` statement, `redistribute`, or aggregation. An outbound `prefix-list` or `route-map` filtering the specific prefix would also suppress it. (2) BGP synchronization (default disabled in modern IOS, but enabled in older configs) requires a route to be present in the IGP before BGP will advertise it to eBGP peers — if the OSPF route exists but the internal BGP path is not synchronized, the route is withheld.

**Distractor Analysis:**
- B: If R4's maximum-prefix limit were reached, the BGP session would be torn down — the session would not be Established.
- D: The question states the BGP session IS in Established state — routes are exchanged in Established.

---

### Question 3 (Scenario — 10 pts)
A network operations center receives alerts that VoIP call quality has degraded on a specific WAN link. An engineer runs `show policy-map interface GigabitEthernet0/1 output` and sees:
```
Class-map: VOICE (match-any)
  5 minute offered rate 22000000 bps
  5 minute drop rate 3500000 bps
  queue depth 0
  priority level 1
    Packet Output 1250000, Drops 87500
```
The interface is 100 Mbps. The priority queue is configured as `priority percent 20`. What is happening and what is the correct fix?

- A) The priority queue depth is 0 — the queue is empty and drops are caused by an upstream ACL. ❌
- B) The VOICE class is receiving 22 Mbps of traffic (22% of 100 Mbps) but the strict priority queue is limited to 20 Mbps (20%). The excess 2 Mbps is being policed/dropped by the LLQ rate limiter. The fix is to either increase `priority percent` to 25, police VoIP sources to ensure they stay within the 20% allocation, or investigate why VoIP traffic is exceeding its expected rate. ✅
- C) The drops indicate a hardware queue buffer overflow — replace the router interface card. ❌
- D) The `queue depth 0` means the queue is misconfigured — LLQ requires a minimum queue depth of 64 packets. ❌

**Answer:** B — LLQ's `priority percent 20` creates a strict 20 Mbps (20% of 100 Mbps) rate limiter for the VOICE class. Traffic exceeding this rate is dropped by the policing action built into LLQ — this is by design to prevent the priority queue from starving other queues. The output shows 22 Mbps offered rate with 3.5 Mbps being dropped, confirming the VoIP traffic is exceeding its 20 Mbps allocation. `queue depth 0` is expected for LLQ — the strict priority queue does not buffer; it either transmits immediately or drops. Possible causes: more calls than planned, a misconfigured softphone marking non-VoIP traffic as EF, or codec changes.

**Distractor Analysis:**
- A: ACL drops appear before the policy map is processed and would not show in `show policy-map` class statistics.
- C: Hardware queue issues produce different symptoms — interface errors, not LLQ policy drop counters.
- D: LLQ (strict priority queue) intentionally has zero queue depth — packets are serviced immediately or dropped; buffering would introduce the very jitter LLQ is designed to prevent.

---

### Question 4 (Multiple Choice — 10 pts)
A network engineer is troubleshooting a Layer 2 loop on a campus switch network. `show spanning-tree vlan 10` on the root bridge shows the topology as expected. However, hosts on VLAN 10 are experiencing traffic storms. Which command output would most directly pinpoint the interface causing the loop?

- A) `show interface counters errors` — high CRC counts indicate a looped interface. ❌
- B) `show mac address-table dynamic vlan 10` — a MAC address appearing on multiple ports simultaneously indicates a loop (the switch is seeing the same source MAC arrive on two different ports). ✅
- C) `show spanning-tree inconsistentports` — ports in BPDU inconsistency state indicate the loop source. ❌
- D) `show cdp neighbors` — duplicate CDP neighbor entries reveal a physical loop. ❌

**Answer:** B — In an active Layer 2 loop, frames circulate endlessly. The most direct symptom visible in the MAC address table is a **MAC address flapping** — the same source MAC address is being seen arriving on two different ports as the looped frame circulates. `show mac address-table dynamic vlan 10` combined with `show mac address-table notification change` (if configured) will show the same MAC toggling between ports rapidly. Additionally, `show interface [port] counters` will show rapidly incrementing input/output packet counters on the affected port.

**Distractor Analysis:**
- A: CRC errors indicate signal integrity issues (cable faults, duplex mismatch) — not specifically a loop.
- C: `show spanning-tree inconsistentports` shows ports placed in BPDU Guard error-disabled state or root inconsistency — useful for STP security issues, but not for active loops that STP failed to prevent.
- D: CDP neighbors show device adjacency; a loop would show the same device reachable via two paths, but this is not the most direct loop diagnostic tool.

---

### Question 5 (Multiple Choice — 10 pts)
An IPv6-enabled enterprise is running a dual-stack network. A host on the IPv6 segment cannot ping an IPv6 address on a remote subnet. `show ipv6 route` on the intermediate router shows the destination prefix exists. `show ipv6 interface` shows the interface is up. What is the most likely cause, and which command would confirm it?

- A) The IPv6 static route has a wrong next-hop. Confirm with `ping ipv6 [next-hop link-local]`. ❌
- B) ICMPv6 Neighbor Discovery (ND) is failing — the router cannot resolve the next-hop's link-local address to a MAC address. Confirm with `show ipv6 neighbors` — if the next-hop shows as INCOMPLETE or is missing, ND is broken. ✅
- C) IPv6 routing is not enabled globally. Confirm with `show ipv6 cef`. ❌
- D) The MTU for IPv6 is too small — IPv6 requires a minimum MTU of 1500 bytes. Confirm with `show interface [int] | include MTU`. ❌

**Answer:** B — IPv6 uses **Neighbor Discovery Protocol (NDP)** instead of ARP. If ND fails (e.g., ICMPv6 is blocked by an ACL, the next-hop is unreachable at Layer 2, or the interface ND cache has expired), the router cannot resolve the next-hop link-local address to a MAC and cannot forward packets even though it has a valid route. `show ipv6 neighbors` reveals neighbor cache state: INCOMPLETE means ND solicitations are being sent but no advertisement is being received. Checking `show ipv6 traffic` will show ICMPv6 ND solicitation counters.

**Distractor Analysis:**
- A: A wrong static route next-hop would result in no route or a route pointing nowhere — the route exists and the interface is up, making this less likely.
- C: If IPv6 routing were disabled, `show ipv6 route` would show no routes — but the route IS present.
- D: IPv6 requires a minimum path MTU of 1280 bytes, not 1500. Path MTU Discovery (PMTUD) handles MTU negotiation for larger packets.

---

### Question 6 (Scenario — 10 pts)
An engineer receives a ticket: "Users in Site B cannot reach the internet after last night's maintenance window. BGP is up. OSPF is converged." The engineer runs these commands on the Site B edge router and sees:

```
show ip route 0.0.0.0
% Network not in table

show ip bgp
BGP table version is 1, router is 10.2.2.1
Status codes: s suppressed, d damped, h history, * valid, > best
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop       Metric  LocPrf  Weight  Path
*> 192.0.2.0/24    10.1.1.1            0          0       65100 i
```

What is the most likely cause of the internet outage, and what is the fix?

- A) BGP is not redistributing routes into OSPF. Fix: add `redistribute bgp 65001 subnets` under `router ospf 1`. ❌
- B) The ISP is not advertising a default route (0.0.0.0/0) via BGP to Site B's router, and there is no static default route configured. The fix is either to request the ISP to advertise a default route, or configure `ip route 0.0.0.0 0.0.0.0 [ISP next-hop]` as a static default. ✅
- C) The BGP table version is 1 — BGP has not fully converged. Wait for the BGP table to stabilize. ❌
- D) The router has no routes in its routing table at all — reboot the router to reload the configuration. ❌

**Answer:** B — The `show ip route 0.0.0.0` output confirms no default route exists. The BGP table only shows one specific prefix (192.0.2.0/24) — no 0.0.0.0/0 is being received from the ISP. Without a default route, traffic to unknown internet destinations has no path. The root cause is likely that during last night's maintenance, either a BGP prefix filter was applied that blocks the default route, the ISP's default route advertisement was inadvertently removed, or a static default that existed previously was deleted. The fix is to verify the ISP is advertising the default and check for any outbound prefix-list on the ISP session that might be suppressing it.

**Distractor Analysis:**
- A: Redistributing BGP into OSPF would help internal routers reach BGP-learned prefixes, but the problem here is that the default route itself does not exist — redistribution cannot fix what is not in the BGP table.
- C: BGP table version 1 simply means only one update has occurred — a stable low-version table is normal in a small BGP deployment.
- D: The routing table clearly has routes (OSPF routes would be present) — the problem is specifically the missing default route, not a global routing failure.

---

### Question 7 (Multiple Choice — 10 pts)
An enterprise is running MPLS L3VPN to connect multiple branch sites. Branch A can reach the provider CE router but cannot reach Branch B. `show ip route vrf BRANCH-VPN` on the PE router serving Branch A shows the correct VRF routes. `show bgp vpnv4 unicast all` on the PE router shows Branch B's prefixes in the VPNv4 table. What is the most likely cause of the data plane failure?

- A) The VRF import/export Route Targets (RTs) are mismatched between PE-A and PE-B — the correct prefixes are in the VPNv4 table but are not being imported into the correct VRF routing table. ✅
- B) MPLS LDP is not running on the provider core links — labels are not being distributed. ❌
- C) The CE router at Branch A does not have a static route to Branch B's subnet. ❌
- D) The BGP VPNv4 session between PE-A and the Route Reflector uses the wrong address family. ❌

**Answer:** A — In MPLS L3VPN, Route Targets (RTs) control VRF route import/export. The fact that Branch B's prefixes appear in `show bgp vpnv4 unicast all` confirms the BGP VPNv4 control plane is working — PE-A is receiving the VPNv4 routes. However, if the VRF on PE-A has an `import` RT that does not match the `export` RT configured on PE-B's VRF, the routes will remain in the global VPNv4 BGP table but will NOT be installed into the BRANCH-VPN VRF routing table — and `show ip route vrf BRANCH-VPN` would not show Branch B's prefixes despite them being visible in the VPNv4 table. This is the classic "routes in BGP VPNv4 but not in VRF" troubleshooting scenario.

**Distractor Analysis:**
- B: If LDP were down, the MPLS data plane would be completely broken and no inter-site traffic would work — not just Branch A to Branch B.
- C: The CE router does not need a static route — the PE redistributes CE routes into the VRF and BGP handles distribution. CE routers typically use BGP or static routes only to the PE.
- D: If the BGP address family were wrong, `show bgp vpnv4 unicast all` would show no routes at all — but routes ARE visible.

---

### Question 8 (Scenario — 10 pts)
A junior engineer reports that after applying a new ACL to a router's WAN interface, web browsing from internal users stopped working, but internal ICMP (ping) to internet destinations still works. The ACL applied inbound on the WAN interface is:
```
permit icmp any 10.0.0.0 0.255.255.255
permit tcp any 10.0.0.0 0.255.255.255 established
deny ip any any log
```
What is the cause of the problem and how should it be fixed?

- A) The ACL is missing a permit for UDP — DNS queries are being blocked, preventing hostname resolution for web browsing. ❌
- B) The `established` keyword only matches TCP packets with ACK or RST set — TCP SYN-only return packets from new connections initiated by external hosts are correctly blocked, but the `established` statement should be working for browser return traffic. The real problem is that HTTPS (port 443) uses TLS, and the ACL is blocking UDP/443 (QUIC/HTTP3). ❌
- C) The ACL is correctly blocking inbound SYN packets (good), but it is also blocking inbound UDP traffic. DNS responses (UDP/53 from DNS servers to internal hosts) are being dropped, causing DNS resolution to fail for web browsing even though ICMP works. Add `permit udp any 10.0.0.0 0.255.255.255 eq 53` to allow DNS responses. ✅
- D) The established keyword is incorrectly used — it should be replaced with `reflect` to create stateful sessions. ❌

**Answer:** C — ICMP is working because the ACL explicitly permits it. TCP web browsing return traffic (SYN-ACK, ACK) is also permitted by the `established` keyword (which matches ACK/RST bits). The failure is DNS: web browsers resolve hostnames via DNS (UDP/53) before initiating TCP connections. The DNS response packets (UDP from the DNS server back to the internal client) are UDP and have no `established` equivalent — they are dropped by the `deny ip any any` at the end of the ACL. The fix is to add `permit udp any 10.0.0.0 0.255.255.255 eq 53` before the deny statement to allow DNS responses.

**Distractor Analysis:**
- A: DNS is indeed the issue, but the specific mechanism is DNS response (UDP/53 inbound) being blocked, not a general "UDP missing" problem.
- B: QUIC/HTTP3 uses UDP/443, but most enterprise browsing uses TCP/443 (HTTPS), which is covered by `established`. DNS is the more fundamental issue.
- D: Reflexive ACLs (`reflect`) are a valid stateful approach but are not required to fix this — a simple UDP/53 permit solves the immediate problem.

---

### Question 9 (Short Answer — 10 pts)
Describe a structured troubleshooting methodology for diagnosing a network problem where a host cannot communicate with a remote server. Your answer should reference the **OSI model layer-by-layer approach**, list specific IOS commands used at each layer, and explain how you would systematically isolate the fault. (4–5 sentences minimum)

**Model Answer:** A structured OSI-layer troubleshooting approach starts at Layer 1 (Physical) and works upward, or can start at Layer 3 and work both up and down depending on initial symptoms. At **Layer 1**, verify the physical link with `show interface [int]` — check for "Line protocol is down," input/output errors, or CRC errors that indicate cable or duplex issues. At **Layer 2**, verify ARP resolution with `show arp` (for the default gateway MAC) and `show mac address-table` on the switch to confirm the host's MAC is learned on the correct port; also check for port security violations with `show port-security interface`. At **Layer 3**, verify routing with `show ip route [destination]` on each hop to confirm a valid path exists, then use `traceroute` to identify where packets stop forwarding — each hop's response confirms Layer 3 forwarding is working to that point. At **Layers 4–7**, if routing is correct but application traffic fails, check for ACLs blocking specific ports with `show ip access-lists` (look for unexpected hit counts on deny statements), verify the application service is listening with connectivity tests (`telnet [IP] [port]` from the router), and check NAT translations with `show ip nat translations` if NAT is in the path. The key discipline is to document each finding before changing anything, make one change at a time, and verify the effect of each change before proceeding.

---

### Question 10 (Short Answer — 10 pts)
An MPLS VPN customer reports that after a BGP configuration change on their PE router, some branch sites can still reach the hub site but others cannot. `debug ip bgp vpnv4 unicast updates` is too verbose to be useful. Describe a systematic approach to isolating which BGP component is broken, listing the specific `show` commands you would use in order, and explaining what each output tells you. (4–5 sentences)

**Model Answer:** Begin with `show bgp vpnv4 unicast all summary` to identify which BGP peers are in Established state and which are Idle/Active — a peer not in Established state immediately identifies a session-level problem (authentication, timer, network reachability to the peer loopback). Next, `show bgp vpnv4 unicast all [prefix]` for one of the missing hub-site prefixes reveals whether the prefix is in the global VPNv4 BGP table and what its best-path selection status is — if the prefix is absent entirely, the originating PE is not advertising it; if it is present but not best, a BGP policy (local-pref, weight, MED, AS-path) is overriding the expected path. Then `show ip route vrf [VRF-NAME]` on the affected PE confirms whether the VPNv4 prefix has been imported into the correct VRF routing table — if the prefix is in the BGP VPNv4 table but absent from the VRF, the Route Target import/export configuration is the fault. Finally, `show bgp vpnv4 unicast all neighbors [peer] advertised-routes` and `received-routes` verifies exactly what prefixes are being exchanged with each peer, pinpointing whether a route-map or prefix-list on the affected peer's BGP session is filtering the missing prefixes.
