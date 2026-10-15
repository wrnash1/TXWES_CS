# Video Script: Module 01 – Advanced IP Routing: Multi-Area OSPF & EIGRP
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 2 of 2 | Estimated Duration: 15–18 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Kurose & Ross / David Bombal &bull; Computer Networks Graduate Lecture Series &bull; Module 01</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=k9Znd_f6rO0" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/k9Znd_f6rO0" title="Kurose & Ross / David Bombal &bull; Computer Networks Graduate Lecture Series" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Kurose & Ross / David Bombal &bull; Computer Networks Graduate Lecture Series</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

### Pre-Roll Slide

---

### Section 1: EIGRP — From Basics to CCNP Depth

Welcome back to Module 01, Part 2. In Part 1, we built a deep understanding of multi-area OSPF. Now we turn to EIGRP — Enhanced Interior Gateway Routing Protocol — and examine it at CCNP depth.

EIGRP was developed by Cisco as a proprietary protocol and became an open standard in 2013 via RFC 7868. It is widely deployed in enterprise networks, particularly in legacy Cisco-heavy environments and WAN edge designs where its fast convergence and low overhead are advantageous. Understanding EIGRP is essential both for the CCNP exam and for real-world network engineering.

---

### Section 2: The DUAL Algorithm

[Alt-text: A table showing an EIGRP topology table for a destination network 10.2.0.0/24. The table has columns: Via (next-hop router), Reported Distance (RD), Feasibility Condition (RD < FD?), and Status. Row 1: Via R2, RD=1000, FD=1500, Status=Successor. Row 2: Via R3, RD=800, FD=1600, Status=Feasible Successor. Row 3: Via R4, RD=2000, FD=2400, Status=Neither (Stuck in Active if needed).]

EIGRP uses the **Diffusing Update Algorithm (DUAL)** to guarantee loop-free, fast convergence. Understanding DUAL is what separates a network technician from a network engineer.

**Key DUAL Terminology:**
- **Feasible Distance (FD):** The total metric from the local router to the destination via the best path (the Successor route). This is what appears in the routing table.
- **Reported Distance (RD) / Advertised Distance (AD):** The metric that a neighbor reports for a destination — in other words, the cost from your neighbor to the destination.
- **Successor:** The primary next-hop router — the one with the lowest FD to the destination.
- **Feasible Successor (FS):** A backup next-hop that satisfies the **Feasibility Condition**: its Reported Distance must be **less than** the current Feasible Distance. This guarantees the backup route is loop-free.

**Why the Feasibility Condition matters:**
If a Feasible Successor exists and the Successor fails, EIGRP instantly promotes the Feasible Successor to Successor — this is called a **local computation**, and it happens in milliseconds with zero query traffic. This is EIGRP's killer feature for fast convergence.

If no Feasible Successor exists, EIGRP enters an **Active** state for that route and sends **Query** packets to neighbors. The router cannot use that route until all Query replies are received. If a router takes too long to reply, the neighbor relationship is torn down — this is called **Stuck In Active (SIA)**, and it is a common EIGRP design problem in large networks.

> **Graduate-Level Insight:** SIA is the primary reason experienced network engineers recommend careful EIGRP summarization in large networks. By summarizing routes at boundaries, you limit the scope of Query propagation and prevent SIA cascades. This is a direct parallel to OSPF's multi-area design rationale.

---

### Section 3: EIGRP Named Mode Configuration

Cisco introduced **EIGRP Named Mode** (also called EIGRP Multi-AF Mode) starting in IOS 15.x. Named mode is now the preferred configuration style on CCNP exams and in modern enterprise deployments.

**Classic EIGRP Configuration:**
```
router eigrp 100
 network 10.0.0.0 0.0.0.255
 network 192.168.1.0 0.0.0.3
 no auto-summary
 passive-interface GigabitEthernet0/2
```

**EIGRP Named Mode Configuration (preferred):**
```
router eigrp ENTERPRISE-DOMAIN
 !
 address-family ipv4 unicast autonomous-system 100
  !
  af-interface GigabitEthernet0/2
   passive-interface
  exit-af-interface
  !
  af-interface default
   hello-interval 5
   hold-time 15
  exit-af-interface
  !
  topology base
   redistribute ospf 1 metric 10000 100 255 1 1500
  exit-af-topology
  !
  network 10.0.0.0 0.0.0.255
  network 192.168.1.0 0.0.0.3
  eigrp router-id 1.1.1.1
 exit-address-family
```

Named mode provides:
- **Per-interface configuration** (hello timers, passive-interface, authentication) within the routing process instead of requiring separate interface-level commands.
- **Single configuration block** for both IPv4 and IPv6 address families.
- **More granular topology configuration** within `topology base`.
- **Cleaner redistribution** management.

---

### Section 4: OSPF–EIGRP Redistribution

[Alt-text: A diagram showing two separate routing domains. On the left, three routers connected in Area 0 (OSPF). On the right, three routers running EIGRP AS 100. In the center, a single router labeled "ASBR/Redistribution Router" has one interface in the OSPF domain and one in the EIGRP domain. Two arrows indicate mutual redistribution between protocols.]

In an enterprise environment, you will frequently encounter situations where OSPF and EIGRP coexist — often as a result of acquisitions, legacy network segments, or multi-vendor WAN connections. **Route redistribution** allows routes learned by one routing protocol to be injected into another.

**Redistribution from EIGRP into OSPF:**
```
router ospf 1
 redistribute eigrp 100 subnets metric 20 metric-type E2
```
- `subnets`: Required keyword to redistribute classless subnets (without it, only classful routes are redistributed).
- `metric 20`: Sets the external OSPF metric (cost) for redistributed routes.
- `metric-type E2`: Type 2 external — metric does not accumulate as the route traverses OSPF (default); E1 would add OSPF internal cost to external metric.

**Redistribution from OSPF into EIGRP (Named Mode):**
```
router eigrp ENTERPRISE-DOMAIN
 address-family ipv4 unicast autonomous-system 100
  topology base
   redistribute ospf 1 metric 10000 100 255 1 1500
```
The EIGRP `metric` keyword requires five values: **bandwidth** (Kbps), **delay** (tens of microseconds), **reliability** (0–255), **load** (0–255), **MTU**. These are the components of the EIGRP composite metric formula.

**⚠ Redistribution Design Warning:**
Mutual redistribution (redistributing OSPF into EIGRP AND EIGRP into OSPF simultaneously) creates **routing loops** if not properly controlled. Always use **route maps with tags** to prevent routing domain feedback loops. This is a critical design point that the CCNP exam tests directly.

---

### Section 5: Module 01 Lab Preview

In the Module 01 lab, you will build the following topology in Cisco Packet Tracer:
- **4 routers:** R1 and R2 in OSPF Area 0, R3 as the ABR connecting Area 1 (containing R4 and R5), R4 as the redistribution router connecting to an EIGRP domain (R5, R6).
- Configure multi-area OSPF with inter-area summarization on R3.
- Configure EIGRP Named Mode on R4, R5, R6.
- Configure mutual redistribution between OSPF and EIGRP on R4 using route tags to prevent feedback loops.
- Verify all routers can reach all networks. Document with `show ip route`, `show ip ospf database`, and `show ip eigrp topology`.

All lab instructions and the starter `.pkt` topology file are in Canvas Module 01.

---

### Section 6: Part 2 Summary & Looking Ahead

This week you learned:
- **Multi-Area OSPF** architecture, LSA types, stub areas, and ABR summarization (Part 1).
- **EIGRP DUAL** algorithm with Feasible Successor, Feasibility Condition, and SIA avoidance (Part 2).
- **EIGRP Named Mode** configuration syntax and benefits.
- **OSPF–EIGRP mutual redistribution** with route tag loop prevention.

**Looking ahead to Module 02:** Campus Network Design. We leave the routing layer and go into the switching layer — advanced VLANs, Spanning Tree Protocol variants (RSTP, MST), and EtherChannel (LACP/PAgP). Module 02 is the switching counterpart to this week's routing depth.

Assignments are due Sunday, October 25 at 11:59 PM CST. Good luck!

---

### Additional Resources
- IETF RFC 7868 — Cisco EIGRP: https://datatracker.ietf.org/doc/html/rfc7868
- Cisco EIGRP Named Mode Configuration Guide (free): https://www.cisco.com/
- Cisco OSPF to EIGRP Redistribution Design Guide: https://www.cisco.com/

---
*End of Part 2 — Module 01*
