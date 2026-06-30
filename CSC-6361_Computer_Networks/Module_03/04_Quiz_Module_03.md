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
