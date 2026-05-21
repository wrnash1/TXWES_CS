# Reading Guide: Module 10 - Routing Protocols – Static, OSPF, and BGP
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 10 – Routing Protocols: Static, OSPF, and BGP**! Routing is the mechanism by which packets traverse networks from source to destination. The CompTIA Network+ N10-009 exam tests your ability to distinguish static routing from dynamic routing protocols, understand how routers build and use routing tables, and recognize the roles of interior gateway protocols (like OSPF) versus exterior gateway protocols (like BGP). This module also covers key routing concepts including administrative distance, route summarization, and default routes.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Routing Table**: A data structure maintained by a router that maps destination network prefixes to the next-hop IP address or exit interface used to reach them. Routers consult this table for every forwarding decision.
*   **Static Route**: A manually configured route entered by an administrator. Does not adapt to topology changes — if the path fails, traffic is dropped until the route is updated manually. Used for simple or stub networks and default routes.
*   **Default Route**: A catch-all route (0.0.0.0/0 for IPv4 or ::/0 for IPv6) that matches any destination not found in the routing table. Used to forward traffic to the internet or an upstream router.
*   **Dynamic Routing Protocol**: A protocol that allows routers to automatically discover routes, share routing information with neighbors, and adapt to topology changes. Examples: OSPF, EIGRP, BGP, RIP.
*   **Administrative Distance (AD)**: A value that ranks the trustworthiness of a routing source. When multiple routing sources provide routes to the same destination, the route with the lowest AD is preferred. Connected=0, Static=1, OSPF=110, RIP=120, EBGP=20, IBGP=200.
*   **Metric**: The value a routing protocol uses to compare routes to the same destination from the same protocol. Each protocol uses different metrics: RIP uses hop count; OSPF uses cost (based on bandwidth); EIGRP uses composite metric (bandwidth + delay).
*   **IGP (Interior Gateway Protocol)**: A routing protocol used within a single autonomous system (AS) — an organization's internal network. Examples: OSPF, EIGRP, RIP. IGPs exchange full routing information within the AS.
*   **EGP (Exterior Gateway Protocol)**: A routing protocol used to exchange routing information between different autonomous systems on the internet. BGP is the only EGP in use today.
*   **OSPF (Open Shortest Path First)**: A link-state IGP that uses Dijkstra's shortest-path algorithm. Routers share Link State Advertisements (LSAs) to build a complete map (LSDB) of the network topology and calculate the shortest path to each destination. Uses cost (based on interface bandwidth) as its metric. Open standard — vendor-neutral.
*   **OSPF Areas**: OSPF uses a hierarchical area structure to reduce routing overhead. Area 0 (backbone area) connects all other areas. Routers within the same area share the same LSDB. Area Border Routers (ABRs) connect non-backbone areas to Area 0.
*   **BGP (Border Gateway Protocol)**: The EGP that routes traffic between autonomous systems on the internet. BGP is a path-vector protocol — it selects routes based on a set of attributes including AS path length, local preference, and MED. eBGP (external BGP) runs between different ASes; iBGP runs within the same AS.
*   **RIP (Routing Information Protocol)**: A legacy distance-vector IGP that uses hop count as its metric, with a maximum of 15 hops (16 = unreachable). Sends full routing table updates every 30 seconds. RIPv2 supports CIDR and authentication. Largely replaced by OSPF in modern networks.
*   **Route Summarization (Supernetting)**: Combining multiple contiguous network prefixes into a single summary route advertisement. Reduces the size of routing tables and the frequency of routing updates. Critical for scaling large networks.
*   **Routing Loop**: A condition where packets circulate between routers indefinitely because each router's best path to a destination points to the next router in the loop. Distance-vector protocols are susceptible; mechanisms like split horizon, route poisoning, and holddown timers prevent them.
*   **ECMP (Equal-Cost Multi-Path)**: A routing technique where traffic is distributed across multiple paths that have the same metric to the same destination. Provides load balancing and redundancy without requiring additional routing protocols.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Routing protocols fall under **Domain 2.0 – Network Implementations (20%)**. Static routing, OSPF concepts, and routing table interpretation are the most-tested routing topics.
*   **Administrative distance order — memorize this**: Connected=0, Static=1, EBGP=20, OSPF=110, RIP=120, IBGP=200. The exam presents a router with multiple route sources to the same destination and asks which is installed in the routing table — always the lowest AD.
*   **OSPF cost formula**: Cost = Reference Bandwidth / Interface Bandwidth. Default reference bandwidth = 100 Mbps. A 100 Mbps link has cost 1; a 10 Mbps link has cost 10. The exam may ask which path OSPF selects based on cost.
*   **BGP is the internet routing protocol**: Any question mentioning routing between ISPs, autonomous systems, or the global internet routing table refers to BGP. OSPF, EIGRP, and RIP are all internal (IGP) protocols.
*   **Default route use case**: The exam will describe a small branch office that connects to the internet through a single ISP link. The correct configuration is a default route (0.0.0.0/0) pointing to the ISP router — not a full OSPF or BGP deployment.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers static routing, dynamic routing protocols, and routing table analysis in the Network Implementations section.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **Routing and Routing Protocols** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the routing table structure, administrative distance comparison, and the OSPF link-state operation.
*   **Required Video:** Watch Professor Messer's **Routing Technologies** and **Dynamic Routing Protocols** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will configure static routes and OSPF on Cisco routers in Packet Tracer, verify routing tables using `show ip route`, observe OSPF neighbor adjacency with `show ip ospf neighbor`, and test path selection by changing interface costs to influence OSPF's shortest-path calculation.

---

### 3. Study Checklist
*   [ ] Understand static routes vs. dynamic routing protocols — when to use each.
*   [ ] Memorize administrative distance values for Connected, Static, OSPF, RIP, eBGP, and iBGP.
*   [ ] Know OSPF operation: LSAs, LSDB, Dijkstra algorithm, cost metric, and area structure.
*   [ ] Know BGP's role as the internet EGP and the difference between eBGP and iBGP.
*   [ ] Know the default route (0.0.0.0/0) and its use case for stub/branch networks.
*   [ ] Read the **Routing Protocols** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's routing videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
