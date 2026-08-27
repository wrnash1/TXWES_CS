# Quiz: Module 03 – WAN Technologies: MPLS, SD-WAN & VPNs
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: Sunday, November 8, 2026 at 11:59 PM CST

---

### Question 1 (Multiple Choice — 10 pts)
In an MPLS network, which device is responsible for adding (pushing) the initial MPLS label to an incoming IP packet from a customer?

- A) P router (Provider core router) ❌
- B) CE router (Customer Edge) ❌
- C) PE router (Provider Edge) ✅
- D) LDP router (Label Distribution Point) ❌

**Answer:** C — The PE (Provider Edge) router receives the IP packet from the CE router, looks up the destination prefix, and pushes the MPLS label stack. P routers perform label swap operations and never see the original IP header. CE routers are customer equipment that speaks standard IP to the PE.

---

### Question 2 (Multiple Choice — 10 pts)
An enterprise uses MPLS L3VPN to connect 10 branch offices. Each branch uses the same private address space: 192.168.1.0/24. What MPLS VPN mechanism prevents routing table confusion when the PE router receives routes from all 10 branches with the same IP prefix?

- A) MPLS Traffic Engineering tunnels assign unique paths per customer. ❌
- B) Route Distinguishers (RDs) prepend a unique 64-bit value to each customer's prefix, making VPNv4 routes globally unique in MP-BGP. ✅
- C) VRF ACLs filter duplicate routes on the PE router. ❌
- D) The PE router uses NAT to translate overlapping customer addresses. ❌

**Answer:** B — The RD makes 192.168.1.0/24 from Customer A's VRF a different route (e.g., 100:1:192.168.1.0/24) than the same prefix from Customer B's VRF (100:2:192.168.1.0/24). MP-BGP carries these VPNv4 routes between PE routers.

---

### Question 3 (Multiple Choice — 10 pts)
What is the primary purpose of a Route Target (RT) in an MPLS L3VPN deployment?

- A) To make overlapping customer IP prefixes unique within the provider's BGP. ❌
- B) To control which VRFs import and export which routes, enabling flexible VPN topologies (full mesh, hub-and-spoke, extranet). ✅
- C) To set the MPLS TTL value on provider core routers. ❌
- D) To identify the customer's CE router by its IP address. ❌

**Answer:** B — While the RD makes prefixes unique, the RT controls reachability. By exporting routes from one VRF with RT 100:1 and importing that same RT in other VRFs, a network engineer controls which sites can reach which other sites — enabling hub-and-spoke or extranet designs.

---

### Question 4 (Multiple Choice — 10 pts)
A network engineer is troubleshooting an IPsec VPN. The command `show crypto isakmp sa` shows the tunnel in `MM_NO_STATE`. What does this indicate?

- A) The ISAKMP (Phase 1) negotiation is complete and the SA is established. ❌
- B) The ISAKMP Phase 1 negotiation failed — likely a mismatch in IKE policy (encryption algorithm, hash, DH group, or pre-shared key). ✅
- C) The Phase 2 IPsec SA was established but Phase 1 timed out. ❌
- D) The tunnel is in main mode and waiting for Phase 2 to complete. ❌

**Answer:** B — `MM_NO_STATE` (main mode, no state) indicates Phase 1 failed to complete. The most common causes: mismatched IKE policy parameters or incorrect pre-shared key. Compare `crypto isakmp policy` and `crypto isakmp key` configurations on both ends.

---

### Question 5 (Multiple Choice — 10 pts)
Why is `ip mtu 1400` typically configured on a GRE over IPsec tunnel interface?

- A) GRE headers add overhead, and IPsec (ESP) adds additional overhead. Without MTU reduction on the tunnel interface, large packets that cannot be fragmented may be silently dropped. ✅
- B) OSPF requires a reduced MTU to form adjacencies over GRE tunnels. ❌
- C) IPsec operates at Layer 2 and requires a smaller frame size. ❌
- D) GRE tunnels automatically fragment all packets, so the MTU should be set low to prevent reassembly at the far end. ❌

**Answer:** A — GRE adds 24 bytes of overhead; IPsec ESP in tunnel mode adds up to 73 additional bytes. A standard 1500-byte Ethernet MTU packet becomes too large to traverse the tunnel without fragmentation. Setting `ip mtu 1400` on the tunnel interface forces the router to fragment packets larger than 1400 bytes before encapsulation, avoiding silent drops. `ip tcp adjust-mss 1360` clamps the TCP MSS so that TCP sessions negotiate a smaller segment size, preventing fragmentation at the application level.

---

### Question 6 (Scenario — 10 pts)
In a Cisco SD-WAN deployment, an engineer notices that Microsoft Teams video traffic is being routed over the MPLS transport even though the internet transport has lower measured latency at the moment. The SD-WAN policy is configured with `prefer mpls for all traffic`. What SD-WAN feature would the engineer configure to override this behavior specifically for real-time collaboration apps?

- A) Modify the OMP route preference globally. ❌
- B) Configure an **Application-Aware Routing (AAR) policy** that measures per-transport SLA metrics (latency, jitter, loss) and routes specific applications to the best-performing transport based on defined thresholds. ✅
- C) Change the TLOC color of the internet transport from `biz-internet` to `public-internet`. ❌
- D) Increase the OSPF metric on the MPLS-facing interface. ❌

**Answer:** B — Application-Aware Routing (AAR) is a core SD-WAN feature. An AAR policy can specify: "For applications matching the Microsoft Teams classifier, prefer the transport with latency < 50ms and jitter < 10ms. If MPLS exceeds these thresholds, switch to the internet transport." BFD continuously measures per-transport metrics to inform these decisions.

---

### Question 7 (Multiple Choice — 10 pts)
Which two statements correctly describe IPsec Tunnel Mode vs. Transport Mode? (Select two)

- A) Tunnel Mode encrypts only the original payload; the original IP header is left intact. ❌
- B) Transport Mode encrypts only the original payload and is typically used for host-to-host encryption. ✅
- C) Tunnel Mode encrypts the entire original IP packet and adds a new outer IP header — the original IP header is hidden. ✅
- D) Transport Mode is required for site-to-site VPNs between two routers. ❌

**Answer:** B and C — Transport Mode is used for host-to-host (e.g., between two servers) where the original IP addresses need to remain visible for routing. Tunnel Mode creates a full encapsulation — both the payload and original IP header are encrypted, and a new outer IP header is used for routing through the public network.

---

### Question 8 (Scenario — 10 pts)
A network engineer shows you this MPLS forwarding table entry on a P (core) router:
```
Local    Outgoing   Prefix           Bytes Label   Outgoing     Next Hop
Label    Label      or Tunnel Id     Switched      Interface
102      Pop Label  10.50.0.0/24     2495788       Gi0/1        10.1.1.2
```
What does "Pop Label" indicate, and what is the significance of this on a P router?

- A) The P router is the ingress PE and is pushing a label onto new packets. ❌
- B) This P router is performing **Penultimate Hop Popping (PHP)** — removing the top label before forwarding to the egress PE, allowing the PE to make the final forwarding decision based on the IP header without a double lookup. ✅
- C) The label for this prefix has expired and will be renewed by LDP. ❌
- D) Pop Label indicates the packet is being dropped. ❌

**Answer:** B — PHP allows the second-to-last router (penultimate hop) to pop the MPLS label before forwarding to the egress PE. This avoids the egress PE having to perform both an MPLS label lookup AND an IP routing table lookup. The PE receives a plain IP packet (or VPN label only) and makes one forwarding decision. This is default behavior in Cisco MPLS and improves PE performance.

---

### Question 9 (Short Answer — 10 pts)
Explain what a TLOC is in Cisco SD-WAN and how it enables the system to use multiple WAN transports simultaneously. (2–3 sentences minimum)

**Model Answer:** A TLOC (Transport Location Identifier) uniquely identifies a specific WAN transport connection on a vEdge/cEdge device, defined by a combination of the device's system IP address, the transport color (e.g., "mpls", "biz-internet", "lte"), and the encapsulation type (IPsec or GRE). TLOCs are advertised via OMP to the vSmart controller, which distributes them to all other vEdge devices in the SD-WAN fabric. This allows each device to know the IP addresses and transport details needed to build direct IPsec data plane tunnels to every other device over every available transport simultaneously — enabling the system to measure performance on each path independently and route traffic based on application SLA policies.

---

### Question 10 (Short Answer — 10 pts)
A junior engineer proposes configuring IPsec in `mode tunnel` on GRE tunnel interfaces to "provide maximum security." A senior engineer objects and says `mode transport` should be used instead. Who is correct, and why? (3–4 sentences)

**Model Answer:** The senior engineer is correct. When IPsec is applied to a GRE tunnel interface, using `mode tunnel` would cause **double encapsulation**: GRE already adds an outer IP header (encapsulating the original packet), and then IPsec tunnel mode would add a second new outer IP header — resulting in three IP headers total, significantly increasing overhead. Using `mode transport` is correct: it encrypts only the GRE payload (the original IP packet), while preserving the GRE outer IP header for routing purposes. The result is a properly structured packet: [GRE outer IP] → [GRE header] → [ESP/AH] → [original encrypted IP packet], with one fewer header than double-tunnel mode would create.

---

> **Instructor Note — Questions 11–20:** These 10 questions are worth **5 pts each** (50 pts total).

---

### Question 11 (Multiple Choice — 5 pts)
An MPLS network engineer runs `show mpls ldp neighbor` on a P router and sees no LDP neighbors, even though all interfaces are up and IGP is running. What is the MOST likely cause?

- A) LDP requires BGP to be running before it can form neighbor relationships. ❌
- B) The `mpls ip` command has not been enabled on the interfaces connecting to neighboring routers. ✅
- C) LDP only operates on PE routers, not P routers. ❌
- D) The MPLS TTL has been set to 0, preventing LDP hello packets from reaching neighbors. ❌

**Answer:** B — LDP must be explicitly enabled per-interface with `mpls ip` (or globally if supported). Without it, the router does not send LDP Hello packets on those interfaces and no LDP session forms. Verifying with `show mpls interfaces` will show which interfaces have MPLS enabled.

**Distractor Analysis:**
- A: LDP is entirely independent of BGP; it runs over TCP directly between IGP neighbors.
- C: LDP runs on all MPLS-enabled routers including P (core) routers.
- D: MPLS TTL affects packet forwarding, not LDP session establishment.

---

### Question 12 (Multiple Choice — 5 pts)
An enterprise runs MPLS L3VPN. Site A and Site B belong to Customer X's VRF, and Site C belongs to Customer Y's VRF. Both customers use the 10.0.0.0/8 address space. The PE router serving Site A shows both a Customer X and Customer Y route for 10.1.0.0/24 in its VPNv4 BGP table. How does the PE router forward traffic from Customer X's CE router destined for 10.1.0.0/24 to the correct site?

- A) The PE uses NAT to translate the overlapping address before forwarding. ❌
- B) The PE looks up the destination in Customer X's VRF routing table only, which contains only routes imported with Customer X's Route Target. The VRF lookup isolates the forwarding decision from Customer Y's routes entirely. ✅
- C) The PE uses the BGP community value to distinguish between customers. ❌
- D) The PE uses the CE router's MAC address to determine which customer the traffic belongs to. ❌

**Answer:** B — VRFs provide complete routing table separation on the PE. When a packet arrives from Customer X's CE router on an interface bound to Customer X's VRF, the PE performs a lookup exclusively in that VRF's routing table — Customer Y's routes are in a separate VRF and are completely invisible to this lookup. The Route Target import/export mechanism controls which routes appear in each VRF.

---

### Question 13 (Scenario — 5 pts)
A network engineer runs `show crypto ipsec sa` on HQ-R and sees that the `#pkts encrypt` counter is incrementing but `#pkts decrypt` is not. Traffic from HQ cannot reach the branch. What is the MOST likely cause?

- A) The IPsec SA has expired and needs to be re-keyed manually. ❌
- B) The crypto map is applied on the wrong interface — it should be on the WAN interface, not a LAN interface. ❌
- C) The IPsec SA exists in one direction only — the branch router is not encrypting return traffic, likely because the crypto map or ACL on the branch is misconfigured. ✅
- D) The transform set encryption algorithm is mismatched, so decryption fails silently. ❌ (mismatch prevents SA establishment)

**Answer:** C — IPsec SAs are unidirectional. If HQ is encrypting traffic (encrypt counter rising) but not receiving encrypted replies (decrypt counter static), the branch's crypto map ACL is likely missing the return traffic entry, the branch's crypto map is not applied to its WAN interface, or the branch's pre-shared key is incorrect preventing its SA from forming. Use `show crypto isakmp sa` on the branch to check Phase 1 state.

---

### Question 14 (Multiple Choice — 5 pts)
In Cisco SD-WAN, what is the role of the **vBond** controller?

- A) vBond stores all network configuration templates and pushes them to vEdge devices. ❌
- B) vBond is the orchestration plane — it authenticates new devices joining the SD-WAN fabric and provides the IP addresses of vSmart and vManage controllers to bootstrapping vEdge/cEdge devices. ✅
- C) vBond computes and distributes OMP routing policies to all vEdge devices. ❌
- D) vBond encrypts the data plane IPsec tunnels between vEdge devices. ❌

**Answer:** B — vBond is the first controller a new vEdge device contacts when it boots. vBond authenticates the device (certificate-based), then provides the device with the IP addresses of vSmart (policy/control) and vManage (management) controllers. It also facilitates NAT traversal for devices behind NAT. After initial bootstrapping, vEdge devices communicate directly with vSmart and vManage — vBond is not in the ongoing control plane path.

---

### Question 15 (Multiple Choice — 5 pts)
An engineer is configuring IKEv2 on a Cisco IOS-XE router. What is one significant operational advantage of IKEv2 over IKEv1 in a large enterprise with hundreds of VPN tunnels?

- A) IKEv2 uses UDP port 443 instead of UDP port 500, making it easier to traverse firewalls. ❌
- B) IKEv2 establishes the full IKE SA and IPsec SA in two exchanges (4 messages) instead of IKEv1's nine messages for main mode, significantly reducing tunnel establishment time and CPU load on the head-end device. ✅
- C) IKEv2 does not require a pre-shared key or certificate — it uses anonymous authentication. ❌
- D) IKEv2 supports only AES-256 encryption, making configuration simpler. ❌

**Answer:** B — IKEv2 completes both Phase 1 (IKE SA) and Phase 2 (IPsec SA) setup in a single four-message exchange. IKEv1 Main Mode requires six messages for Phase 1 plus three more for Quick Mode Phase 2 — nine total. On a hub router with 500 branches simultaneously re-keying, this difference is significant in terms of CPU utilization and tunnel-up time.

---

### Question 16 (Multiple Choice — 5 pts)
A network engineer wants to verify that OSPF is forming adjacencies correctly over the GRE tunnel between HQ-R and BRANCH-A-R. `show ip ospf neighbor` shows BRANCH-A-R stuck in EXSTART state. What is the MOST likely cause?

- A) OSPF hello and dead timers are mismatched between the tunnel endpoints. ❌
- B) The OSPF MTU on the tunnel interface is mismatched — if one side has `ip mtu 1400` and the other has the default 1500, the OSPF DBD exchange fails because the MTU in the DBD packet doesn't match. ✅
- C) GRE tunnels do not support OSPF adjacency formation. ❌
- D) The OSPF process ID must be the same on both routers. ❌

**Answer:** B — OSPF EXSTART/EXCHANGE state failures are almost always caused by MTU mismatch. OSPF includes the interface MTU in Database Description (DBD) packets. If one side sends DBD packets advertising MTU 1500 and the other expects 1400 (due to `ip mtu 1400` on the tunnel), the router rejects the DBD and the adjacency stalls. Fix: ensure both tunnel endpoints have matching `ip mtu` values, or use `ip ospf mtu-ignore` on the tunnel interfaces (not recommended for production).

---

### Question 17 (Scenario — 5 pts)
An SD-WAN deployment has three transports at each site: MPLS (labeled "mpls"), fiber internet (labeled "biz-internet"), and LTE (labeled "lte"). BFD sessions run over all three. The engineer configures an AAR policy: "For VoIP (DSCP EF) traffic, use a transport with loss < 1% and jitter < 10ms. Prefer MPLS first, then biz-internet, then LTE." Currently MPLS has 2% loss. What happens to VoIP traffic?

- A) VoIP traffic continues on MPLS because it is the preferred transport regardless of SLA. ❌
- B) VoIP traffic fails over to biz-internet if biz-internet meets the loss and jitter SLA thresholds. ✅
- C) VoIP traffic is dropped until MPLS loss drops below 1%. ❌
- D) The vSmart controller tears down the MPLS TLOC and reroutes all traffic to LTE. ❌

**Answer:** B — AAR (Application-Aware Routing) continuously measures per-transport SLA metrics via BFD. When MPLS exceeds the configured loss threshold (1%), the policy fails over VoIP to the next preferred transport that meets the SLA — biz-internet in this case. If biz-internet also fails the SLA, the policy falls back to LTE. When MPLS recovers below 1% loss, AAR can optionally fail back to MPLS based on the configured restore timer.

---

### Question 18 (Multiple Choice — 5 pts)
Which statement correctly describes the difference between an MPLS **Label Information Base (LIB)** and the **Label Forwarding Information Base (LFIB)**?

- A) The LIB is the forwarding table used for packet switching; the LFIB is the full database of all label bindings learned from LDP. ❌
- B) The LIB contains all label bindings learned from LDP (all peers, all prefixes); the LFIB contains only the best-path entries actually used for forwarding — analogous to the difference between the BGP table and the routing table. ✅
- C) The LIB is used only on PE routers; the LFIB is used only on P routers. ❌
- D) The LIB and LFIB are the same database with different display commands. ❌

**Answer:** B — The LIB (`show mpls ldp bindings`) contains all label bindings learned from all LDP peers for all prefixes. The LFIB (`show mpls forwarding-table`) contains only the labels that will actually be used for forwarding — one entry per prefix, selected from the LIB based on the best-path in the IP routing table. This mirrors how the BGP RIB (all BGP routes) differs from the IP routing table (best routes only).

---

### Question 19 (Short Answer — 5 pts)
Explain what **Penultimate Hop Popping (PHP)** is, why it is the default behavior in Cisco MPLS networks, and what the operational advantage is for the egress PE router. (2–3 sentences)

**Model Answer:** PHP is a Cisco MPLS optimization where the second-to-last router in the label-switched path (the penultimate hop P router) removes the top MPLS label before forwarding the packet to the egress PE router, so the PE receives either a plain IP packet (for single-label stacks) or a packet with only the inner VPN label remaining. This is the default behavior because it eliminates a double lookup on the egress PE — without PHP, the PE would need to first look up the outer transport label in the LFIB, then look up the inner IP packet in the VRF routing table. With PHP, the PE only performs the IP or VPN label lookup, reducing forwarding latency and CPU load on the most critical (and often most loaded) device in the MPLS fabric.

---

### Question 20 (Short Answer — 5 pts)
A network engineer proposes replacing the hub-and-spoke GRE/IPsec VPN in the lab with **DMVPN (Dynamic Multipoint VPN)**. Explain what specific scalability problem with static hub-and-spoke GRE DMVPN was designed to solve, and describe one key difference between DMVPN Phase 2 and Phase 3. (2–3 sentences)

**Model Answer:** Static hub-and-spoke GRE requires a pre-configured tunnel interface on the hub for every spoke, and all branch-to-branch traffic must traverse the hub twice (spoke→hub→spoke) — with hundreds of branches this creates both administrative overhead (manually configuring hundreds of tunnel interfaces) and a traffic bottleneck at the hub. DMVPN solves this by using mGRE (multipoint GRE) on the hub and NHRP (Next Hop Resolution Protocol) to dynamically map spoke tunnel IPs to their physical WAN addresses, allowing new spokes to register automatically without hub reconfiguration. The key difference between Phase 2 and Phase 3 is spoke-to-spoke routing: in Phase 2, spoke routers can build direct spoke-to-spoke tunnels dynamically (bypassing the hub for data traffic), but the hub must not summarize routes so spokes can see each other's specific prefixes; in Phase 3, the hub can summarize routes and uses NHRP redirect/shortcut to dynamically redirect spoke-to-spoke traffic onto direct tunnels, providing both summarization benefits and optimal routing simultaneously.
