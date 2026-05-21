# Quiz: Module 10 - Routing Protocols – Static, OSPF, and BGP
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A router has four routes to the 10.10.10.0/24 network learned from different sources: a directly connected interface, a static route, an OSPF route, and a RIP route. Which route will be installed in the routing table and used for forwarding?
A) The RIP route — RIP recalculates routes every 30 seconds, ensuring the most current path is always used
B) The OSPF route — OSPF uses Dijkstra's algorithm to guarantee it always selects the optimal path
C) The static route — static routes have an administrative distance of 1, which is lower than OSPF (110) or RIP (120)
D) The directly connected route — connected interfaces have an administrative distance of 0 and are always preferred over any learned route
*   **Correct Answer:** D) The directly connected route — connected interfaces have an administrative distance of 0 and are always preferred over any learned route
*   **Distractor Analysis:**
    *   *Why A is incorrect:* RIP has an administrative distance of 120 — the highest of the four sources listed. It will not be selected when a directly connected route (AD=0), static route (AD=1), or OSPF route (AD=110) exists for the same destination.
    *   *Why B is incorrect:* OSPF's Dijkstra algorithm selects the best path within the OSPF domain — but OSPF has an administrative distance of 110, which is higher than a connected route (0) or static route (1). When multiple source types compete, AD wins.
    *   *Why C is incorrect:* A static route (AD=1) would be preferred over OSPF (AD=110) and RIP (AD=120), but it loses to a directly connected interface (AD=0). The directly connected route has the lowest possible AD.

---

**Question 2**
An organization has a small branch office with a single internet connection through an ISP router at 203.0.113.1. The branch router needs to forward all internet-bound traffic to the ISP without running a dynamic routing protocol. Which routing configuration accomplishes this with the least administrative overhead?
A) Configure OSPF on the branch router and advertise a host route (0.0.0.0/32) to the ISP
B) Configure a default route `ip route 0.0.0.0 0.0.0.0 203.0.113.1` on the branch router pointing all unmatched traffic to the ISP
C) Configure a static route for every public IP subnet on the internet, each pointing to 203.0.113.1
D) Enable BGP on the branch router and establish an eBGP peering session with the ISP to receive full internet routing tables
*   **Correct Answer:** B) Configure a default route `ip route 0.0.0.0 0.0.0.0 203.0.113.1` on the branch router pointing all unmatched traffic to the ISP
*   **Distractor Analysis:**
    *   *Why A is incorrect:* OSPF is an IGP designed for interior routing within an AS — running OSPF on a branch to reach the internet is incorrect. Additionally, 0.0.0.0/32 is a host route for one specific IP, not a catch-all default route.
    *   *Why C is incorrect:* Configuring individual static routes to every public internet subnet is not feasible — the internet has over 900,000 prefixes. A single default route is the correct solution for stub networks with a single uplink.
    *   *Why D is incorrect:* BGP with full internet routing tables is used by large enterprises and ISPs — it requires significant memory, processing, and BGP expertise. It is completely inappropriate for a small branch office with a single internet connection.

---

**Question 3**
A network administrator uses `show ip route` on a router and sees the following entries for two paths to 192.168.50.0/24: one via OSPF with a cost of 20 (total path cost), and one via RIP with a hop count of 3. Which path does the router install in the routing table?
A) The RIP path — 3 hops is a lower metric than OSPF cost 20, so RIP wins the route selection
B) The OSPF path — OSPF has an administrative distance of 110, which is lower than RIP's administrative distance of 120
C) Both paths are installed — the router uses ECMP to load-balance traffic across OSPF and RIP simultaneously
D) Neither path is installed — the router requires a directly connected route or static route before it can forward traffic
*   **Correct Answer:** B) The OSPF path — OSPF has an administrative distance of 110, which is lower than RIP's administrative distance of 120
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Metrics (hop count, cost) are only compared within the same routing protocol. When two different protocols compete for the same prefix, administrative distance determines the winner — not the metric value. OSPF beats RIP on AD regardless of the metric comparison.
    *   *Why C is incorrect:* ECMP load-balancing only applies to equal-cost paths from the same routing protocol. Routes from two different protocols (OSPF and RIP) cannot share a route entry — the lower-AD protocol wins and the other route is not installed.
    *   *Why D is incorrect:* Routers regularly install dynamically learned routes without requiring connected or static routes for the same prefix. OSPF or RIP learned routes are valid forwarding entries — the premise is incorrect.

---

**Question 4**
An administrator runs `traceroute` from a workstation and discovers that traffic to an external website is taking a suboptimal 12-hop path through a remote data center instead of a 4-hop path through the local ISP. Investigation reveals the OSPF cost on the direct ISP link was left at the default value, making a longer alternate path appear cheaper. What is the correct fix?
A) Increase the OSPF cost on the 12-hop data center path, or decrease the OSPF cost on the direct 4-hop ISP link to make it the preferred route
B) Configure a floating static route with an AD of 200 as a backup for the direct ISP link
C) Enable RIP on the ISP-facing interface so the router receives a lower hop-count metric from the ISP
D) Configure BGP between the branch router and ISP to override OSPF path selection with BGP's path attributes
*   **Correct Answer:** A) Increase the OSPF cost on the 12-hop data center path, or decrease the OSPF cost on the direct 4-hop ISP link to make it the preferred route
*   **Distractor Analysis:**
    *   *Why B is incorrect:* A floating static route (high AD) is a backup route used when the primary path is down — it does not influence which OSPF path is selected when both OSPF paths are active. The problem is OSPF cost misconfiguration, not a missing backup route.
    *   *Why C is incorrect:* Enabling RIP on an OSPF network introduces a second routing protocol and the risk of routing loops. More importantly, RIP uses hop count and has AD=120 — OSPF (AD=110) would still be preferred. This does not fix the OSPF cost misconfiguration.
    *   *Why D is incorrect:* BGP is an EGP used between autonomous systems. Using BGP to override internal OSPF path selection is not the appropriate solution for an interior routing cost misconfiguration. The fix is adjusting OSPF costs within the network.

---

**Question 5**
A network security engineer needs to protect the routing infrastructure from three specific threats: (1) unauthorized routers injecting false OSPF routes, (2) attackers spoofing BGP UPDATE messages to hijack IP prefixes, and (3) administrators accidentally deleting a critical static default route. Which combination of controls addresses all three?
A) Configure OSPF MD5 authentication on all OSPF interfaces, enable BGP route filtering with prefix lists and RPKI validation, and configure a floating static default route with a higher AD as a backup.
B) Enable OSPF passive interfaces on all access ports, configure a BGP route reflector for iBGP scalability, and document all static routes in a network management system.
C) Deploy an IDS sensor on the core router, enable SNMP traps for routing table changes, and configure OSPF stub areas to reduce LSA flooding.
D) Configure OSPF with a higher hello interval to reduce neighbor adjacency formation, enable BGP soft reconfiguration, and create a VLAN for routing protocol traffic.
*   **Correct Answer:** A) Configure OSPF MD5 authentication on all OSPF interfaces, enable BGP route filtering with prefix lists and RPKI validation, and configure a floating static default route with a higher AD as a backup.
*   **Distractor Analysis:**
    *   *Why A is correct:* OSPF MD5 authentication requires routers to prove their identity before forming adjacencies and exchanging LSAs, preventing rogue OSPF injection (requirement 1). BGP prefix lists filter unauthorized prefixes and RPKI validates the legitimacy of BGP route origins, preventing prefix hijacking (requirement 2). A floating static default route (AD higher than OSPF) installs automatically if the primary route disappears, protecting against accidental deletion (requirement 3).
    *   *Why B is incorrect:* OSPF passive interfaces prevent routing updates on access ports but do not authenticate OSPF neighbors on router-to-router links. A BGP route reflector improves iBGP scalability but does not secure BGP against spoofed UPDATE messages. SNMP documentation does not prevent static route deletion.
    *   *Why C is incorrect:* An IDS detects but does not prevent routing attacks — malicious LSAs or BGP updates would still be processed before the IDS alerts. OSPF stub areas reduce LSA types but do not authenticate routing peers. SNMP traps alert after the fact, not prevent the event.
    *   *Why D is incorrect:* A longer OSPF hello interval slows adjacency formation but does not prevent unauthorized routers from eventually forming adjacencies — authentication is required. BGP soft reconfiguration stores received routes for policy changes but does not validate route origins. A separate VLAN for routing protocols provides isolation but not authentication or prefix validation.
