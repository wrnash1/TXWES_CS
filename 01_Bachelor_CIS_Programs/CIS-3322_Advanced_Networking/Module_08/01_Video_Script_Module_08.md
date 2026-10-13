# Video Script: Module 08 - OSPFv2 Routing Concepts and Setup

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Estimated Duration:** 23 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for all OSPF configuration and neighbor state demonstrations
- Show `show ip ospf neighbor` output live as neighbors progress to Full state
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: Why Dynamic Routing and What Is OSPF [00:00 - 04:00]

Welcome to Module 08. I am Professor Nash. Until now we have worked with static routes — routes you manually configure. Static routing works fine in small networks, but it does not scale. When a new subnet is added, every router in the network must be updated manually. When a link fails, static routes do not adapt. Dynamic routing protocols solve both problems.

OSPFv2 — Open Shortest Path First version 2 — is the dynamic routing protocol tested most heavily on the CCNA 200-301 exam. It is a link-state protocol, which means every router builds a complete map of the network topology and independently calculates the best path.

[SHOW DIAGRAM: Three routers in a triangle. Each router is labeled R1, R2, R3. Arrows indicate that each router sends LSAs to all others. All three routers then independently compute shortest-path routes to all destinations]

OSPF belongs to the link-state family. Compare this to RIP, which is distance-vector: a distance-vector router only knows what its neighbors tell it. A link-state router knows the entire topology. The result is faster convergence and loop-free routing.

Key terms you will use throughout this module:

- Link-State Advertisement (LSA): the packet each OSPF router generates to describe its connected links and their costs
- Link-State Database (LSDB): the collection of all LSAs, identical on all routers in an area
- SPF algorithm: Dijkstra's Shortest Path First — the algorithm each router runs against the LSDB to compute the best routes

---

## Section 2: OSPF Areas and the Backbone [04:00 - 09:00]

[SHOW DIAGRAM: A larger OSPF topology showing Area 0 (backbone) in the center, with Area 1 and Area 2 connecting to Area 0 through ABRs. Labels identify each router type: internal router, ABR, ASBR]

OSPF organizes routers into areas to limit the scope of LSA flooding and reduce LSDB size. Every OSPF network must have Area 0, called the backbone area. All other areas must connect to Area 0 either directly or through virtual links.

Router types in OSPF:

- Internal router: all interfaces in one area
- Area Border Router (ABR): connects two or more areas; summarizes routing information between them
- Autonomous System Boundary Router (ASBR): redistributes routes from other routing protocols (such as EIGRP or BGP) into OSPF
- Backbone router: has at least one interface in Area 0

For the CCNA exam, most questions focus on single-area OSPF (all routers in Area 0). You will see multi-area concepts at a conceptual level, but configuration questions are almost always single-area.

CCNA Exam Tip: All OSPF areas must be connected to Area 0. A non-zero area that is not connected to Area 0 is called a discontiguous area, and routes from it will not be installed in the routing table. This is a common exam distractor in multi-area scenarios.

---

## Section 3: OSPF Neighbor States and Adjacency [09:00 - 14:00]

[SHOW DIAGRAM: A state machine diagram showing the seven OSPF neighbor states in sequence: Down → Init → 2-Way → Exstart → Exchange → Loading → Full. Arrows between states labeled with the event that causes each transition]

Before OSPF routers can exchange routing information, they must form a neighbor relationship. The process goes through seven states:

- Down: no OSPF hello packets have been received
- Init: a hello has been received but the local router's ID is not yet in that hello
- 2-Way: both routers see each other in their hello packets — bidirectional communication is established; DR/BDR election occurs here on broadcast segments
- Exstart: routers negotiate the master/slave relationship for database exchange
- Exchange: routers exchange Database Description (DBD) packets listing their LSDB contents
- Loading: routers request any LSAs they are missing
- Full: databases are synchronized; adjacency is complete

CCNA Exam Tip: On a point-to-point link, all OSPF neighbors reach the Full state. On a broadcast segment (Ethernet), only the DR and BDR form Full adjacency with all other routers. Non-DR/BDR routers (called DROthers) stop at 2-Way with each other — they do not form Full adjacency with other DROthers. This is expected behavior, not a failure.

### DR and BDR Election

On a multi-access network (like Ethernet), OSPF elects a Designated Router (DR) and a Backup Designated Router (BDR) to reduce the number of neighbor relationships. Instead of every router forming Full adjacency with every other router, all routers form Full adjacency only with the DR and BDR.

DR/BDR election is based on:

1. Highest OSPF interface priority (default 1; range 0-255)
2. Tiebreaker: highest Router ID

A priority of 0 means the router will never become DR or BDR.

---

## Section 4: OSPFv2 Configuration Walkthrough [14:00 - 19:30]

[SHOW DIAGRAM: Two routers R1 and R2 connected via a serial link (10.0.0.0/30). R1 has Loopback0 1.1.1.1/32. R2 has Loopback0 2.2.2.2/32. Both are in Area 0]

### Router ID Configuration

The Router ID uniquely identifies each OSPF router. Selection order:

1. Manually configured with `router-id`
2. Highest IP address on any loopback interface
3. Highest IP address on any active physical interface

Best practice: always configure the Router ID manually.

```ios
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
```

### Network Command and Wildcard Masks

The `network` command enables OSPF on interfaces whose IP addresses fall within the specified range:

```ios
R1(config-router)# network 10.0.0.0 0.0.0.3 area 0
R1(config-router)# network 192.168.10.0 0.0.0.255 area 0
```

Wildcard mask calculation: subtract subnet mask from 255.255.255.255.

- /30 (255.255.255.252) → wildcard 0.0.0.3
- /24 (255.255.255.0) → wildcard 0.0.0.255
- /28 (255.255.255.240) → wildcard 0.0.0.15

Alternatively, use the `ip ospf [process-id] area [area-id]` command directly on the interface to avoid wildcard masks entirely:

```ios
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip ospf 1 area 0
```

### Passive Interface

Configure passive interface on any interface that has no OSPF neighbor (such as LAN-facing interfaces). This prevents hello packets from being sent out the interface while still advertising the connected subnet:

```ios
R1(config-router)# passive-interface GigabitEthernet0/1
```

Or set all interfaces passive by default and enable OSPF only where needed:

```ios
R1(config-router)# passive-interface default
R1(config-router)# no passive-interface GigabitEthernet0/0
```

CCNA Exam Tip: Passive interface prevents OSPF hellos from being sent out the interface. The connected subnet is still advertised by OSPF to neighbors on other interfaces. This is the correct configuration for LAN segments with no OSPF neighbors.

---

## Section 5: Verification and Troubleshooting [19:30 - 23:00]

Key verification commands:

```ios
R1# show ip ospf neighbor
R1# show ip ospf interface brief
R1# show ip route ospf
R1# show ip protocols
```

### Interpreting show ip ospf neighbor

```text
Neighbor ID   Pri   State       Dead Time   Address     Interface
2.2.2.2         1   FULL/DR     00:00:37    10.0.0.2    Gi0/0
```

Columns to know:

- Neighbor ID: the Router ID of the neighbor
- State: should be FULL for adjacency to be working; 2-WAY for DROther relationships
- Dead Time: countdown; resets when a hello is received

Common reasons OSPF neighbors do not form:

- Mismatched Hello or Dead timers
- Mismatched area IDs
- Mismatched subnet masks on the connecting interfaces
- Authentication mismatch
- Interface not in the network statement range

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 08 Complete
Next: Module 09 - WAN Technologies and VPNs
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
