# Lab Assignment: Module 01 – Multi-Area OSPF & EIGRP Redistribution
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, October 25, 2026 at 11:59 PM CST

---

## Lab Overview
**Estimated Time:** 3–4 hours
**Tools Required:** Cisco Packet Tracer (free — download at netacad.com)
**Deliverables:** (1) Completed `.pkt` Packet Tracer file, (2) Professional Lab Report (PDF)

This lab builds an enterprise network spanning two routing domains — OSPF and EIGRP — with mutual redistribution and loop prevention. You will design, configure, verify, and document the topology to CCNP professional standards.

---

## Lab Topology

```
[Area 1 — OSPF]                [Area 0 — Backbone]         [EIGRP AS 100]
R1 (10.1.0.1) --- R3-ABR --- R2 (10.0.0.1) --- R4-ASBR --- R5 (10.100.0.1)
                                                      |
                                                 R6 (10.100.1.1)
```

**Router Assignments:**
| Router | Role | Area/AS | Interfaces |
|---|---|---|---|
| R1 | Internal OSPF Router | Area 1 | Gi0/0: 10.1.0.1/24 (to R3), Lo0: 10.1.99.1/32 |
| R2 | Internal OSPF Router | Area 0 | Gi0/0: 10.0.0.1/24 (to R3), Gi0/1: 10.0.1.1/24 (to R4), Lo0: 10.0.99.1/32 |
| R3 | ABR (Area 0 + Area 1) | Area 0 & Area 1 | Gi0/0: 10.1.0.2/24 (Area 1 to R1), Gi0/1: 10.0.0.2/24 (Area 0 to R2) |
| R4 | ASBR / Redistribution Router | Area 0 + EIGRP | Gi0/0: 10.0.1.2/24 (OSPF side), Gi0/1: 10.100.0.2/24 (EIGRP side) |
| R5 | EIGRP Router | AS 100 | Gi0/0: 10.100.0.1/24 (to R4), Lo0: 10.100.99.1/32 |
| R6 | EIGRP Router | AS 100 | Gi0/0: 10.100.0.3/24 (to R4 via EIGRP), Lo0: 10.100.98.1/32 |

---

## Lab Instructions

### Part 1: Build the Topology in Packet Tracer (20 pts)
1. Open Cisco Packet Tracer. Place 6 routers (use Cisco 4321 or equivalent).
2. Connect the routers per the topology diagram above using straight-through Ethernet cables.
3. Assign IP addresses to all interfaces as specified in the Router Assignments table.
4. Verify all directly connected interfaces can ping each other before proceeding.

**Screenshot Checkpoint 1:** Show all 6 routers connected and IP addresses assigned. Use `show ip interface brief` on each router to capture in your report.

### Part 2: Configure Multi-Area OSPF (R1, R2, R3) (25 pts)
Configure OSPF Process 1 on R1, R2, and R3.
- R1 interfaces: All in Area 1
- R2 interfaces: All in Area 0
- R3: Gi0/0 in Area 1, Gi0/1 in Area 0 (this makes R3 the ABR)
- Advertise all connected networks including loopbacks.
- Configure R3 as the ABR to summarize Area 1 routes as `10.1.0.0/22` toward Area 0.

```
! Example — R3 ABR Summarization:
router ospf 1
 area 1 range 10.1.0.0 255.255.252.0
```

**Screenshot Checkpoint 2:** `show ip ospf neighbor` on all OSPF routers. `show ip ospf database summary` on R2 (should show the summary LSA from R3). `show ip route ospf` on R2.

### Part 3: Configure EIGRP Named Mode (R4, R5, R6) (20 pts)
Configure EIGRP Named Mode on R4, R5, and R6 in AS 100.
- All EIGRP interfaces passive except those connecting to OSPF (R4's Gi0/0).
- Set EIGRP router-IDs explicitly (4.4.4.4, 5.5.5.5, 6.6.6.6).
- Advertise all connected networks including loopbacks.

```
! Example — R5 EIGRP Named Mode:
router eigrp ENTERPRISE-DOMAIN
 address-family ipv4 unicast autonomous-system 100
  af-interface GigabitEthernet0/0
   hello-interval 5
   hold-time 15
  exit-af-interface
  topology base
  exit-af-topology
  network 10.100.0.0 0.0.0.255
  network 10.100.99.0 0.0.0.255
  eigrp router-id 5.5.5.5
 exit-address-family
```

**Screenshot Checkpoint 3:** `show ip eigrp neighbors` on R4, R5, R6. `show ip eigrp topology` on R5 (verify Successors are established).

### Part 4: Configure Mutual Redistribution with Loop Prevention (25 pts)
On R4 (the redistribution router):
1. Create route maps with tags for loop prevention (use tag 100 for OSPF-origin routes, tag 200 for EIGRP-origin routes).
2. Redistribute EIGRP 100 into OSPF 1 using the route map.
3. Redistribute OSPF 1 into EIGRP 100 using the route map.

**Screenshot Checkpoint 4:** `show ip route` on R1 (should see EIGRP loopback networks 10.100.99.0, 10.100.98.0 as External OSPF routes). `show ip route` on R5 (should see OSPF Area 1 loopback 10.1.99.1 and Area 0 loopback 10.0.99.1 as EIGRP external routes). Ping from R1 to 10.100.99.1 (R5 loopback) — must succeed.

### Part 5: End-to-End Verification (10 pts)
1. From R1, ping R5 loopback (10.100.99.1) and R6 loopback (10.100.98.1). Both must succeed.
2. From R5, ping R1 loopback (10.1.99.1). Must succeed.
3. `show ip route` on R4 — verify both OSPF and EIGRP routes are present.

---

## Lab Report Requirements (Graduate Standard)
Your PDF lab report must include:

1. **Topology Diagram** — a clean screenshot or exported image of your Packet Tracer topology with all labels visible.
2. **All 4 Screenshot Checkpoints** — annotated (label what each screenshot shows).
3. **Configuration Listings** — the full running configuration for R3 (ABR) and R4 (redistribution router).
4. **Analysis Section (Required — 2–3 paragraphs):**
   - Explain why the Feasibility Condition is not just a math formula but a guarantee of loop-freedom.
   - Explain what would happen in your topology if R3's Gi0/1 interface (the Area 0 uplink) went down. Which routes would become unreachable, and how would the network respond?
   - Describe two methods you would use to monitor this network in a production environment (tools, commands, or platforms).
5. **Troubleshooting Log** — a brief log of at least one issue you encountered (or deliberately introduced) and how you resolved it.

---

## Grading Rubric
| Component | Points |
|---|---|
| Topology Build (Part 1) | 20 |
| Multi-Area OSPF Config (Part 2) | 25 |
| EIGRP Named Mode Config (Part 3) | 20 |
| Redistribution with Loop Prevention (Part 4) | 25 |
| End-to-End Verification (Part 5) | 10 |
| **Total** | **100** |

**Submission:** Upload both the `.pkt` file AND the PDF report to Canvas Module 01 Lab Assignment by Sunday, October 25 at 11:59 PM CST.

---

## Part 9 — Challenge Exercise

### Challenge 1: OSPF Type 7 to Type 5 LSA Translation
Add a seventh router (R7) to your existing topology as an NSSA ASBR in a new Area 2. Connect R7 to R3 (the existing ABR), making R3 also an ABR for Area 2. Configure Area 2 as NSSA. On R7, redistribute a static route (192.0.2.0/24) into OSPF. Verify the following:
1. On R7, confirm the redistributed route generates a Type 7 LSA: `show ip ospf database nssa-external`.
2. On R3 (the ABR), confirm it translates the Type 7 LSA into a Type 5 LSA for the backbone: `show ip ospf database external`.
3. On R1 (Area 1), confirm the external route 192.0.2.0/24 appears as `O E2` in the routing table.
4. Document why the Type 7-to-Type 5 translation only happens at the ABR and not at the ASBR itself.

### Challenge 2: EIGRP Unequal-Cost Load Balancing with Variance
On the existing EIGRP portion of your topology (R4, R5, R6), add a second path between R5 and R4 through a new router R8 with a higher-cost link (configure a loopback on R8 representing a higher-delay path). Configure `variance 2` in the EIGRP topology base on R5. Verify:
1. `show ip eigrp topology` on R5 — identify the Successor and confirm the alternate path meets the Feasibility Condition.
2. `show ip route eigrp` on R5 — confirm both paths appear in the routing table (unequal-cost load balancing active).
3. `show ip eigrp traffic` — confirm packets are being distributed across both paths.
4. Deliberately set variance to 1 (no unequal-cost LB) and observe the routing table revert to a single path.

### Reflection Questions
1. The NSSA design allows an area with its own ASBR to still minimize Type 5 LSA flooding from the backbone. What is the specific trade-off compared to a Totally NSSA area, and when would a network designer choose NSSA over Totally NSSA?
2. EIGRP unequal-cost load balancing distributes traffic inversely proportional to metric — paths with lower metrics carry proportionally more traffic. In an enterprise WAN design with links of 1 Gbps and 100 Mbps between the same two sites, what are the implications of enabling variance-based load balancing, and what operational problem could arise if the 100 Mbps link becomes congested?
