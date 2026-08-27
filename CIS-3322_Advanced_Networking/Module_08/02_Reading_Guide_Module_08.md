# Reading Guide: Module 08 - OSPFv2 Routing Concepts and Setup

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

OSPFv2 is the most heavily tested routing protocol on the CCNA 200-301 exam, accounting for a significant portion of the IP Connectivity domain (25% of the exam). Expect configuration scenarios, neighbor state analysis, and troubleshooting questions. This guide covers all testable OSPF concepts for single-area and introductory multi-area configurations.

---

## 1. High-Yield Glossary

- **OSPFv2:** Open Shortest Path First version 2 — a link-state interior gateway routing protocol (IGP) defined in RFC 2328. Uses Dijkstra's SPF algorithm to compute loop-free shortest paths. Suitable for IPv4 networks; OSPFv3 is the IPv6 equivalent.

- **Link-State Advertisement (LSA):** The fundamental unit of OSPF topology information. Each router generates LSAs describing its connected links, costs, and neighbors, then floods them throughout the OSPF area. All routers in the area build an identical LSDB from received LSAs.

- **Link-State Database (LSDB):** The complete collection of LSAs from all routers in an OSPF area. All routers in the same area maintain identical LSDBs. Routers in different areas have different LSDBs.

- **SPF algorithm:** Dijkstra's Shortest Path First algorithm. Each router runs SPF independently against its LSDB to compute the lowest-cost path tree to all destinations. The result populates the routing table.

- **Router ID (RID):** A 32-bit value formatted like an IP address that uniquely identifies each OSPF router. Selection order: (1) manually configured, (2) highest loopback IP, (3) highest active physical interface IP.

- **Area:** A logical grouping of OSPF routers and links. LSAs are flooded only within an area, reducing LSDB size. All areas must connect to Area 0 (backbone).

- **Area 0:** The OSPF backbone area. All non-zero areas must connect to Area 0 directly or via virtual links.

- **Area Border Router (ABR):** A router with interfaces in two or more OSPF areas. Maintains separate LSDBs for each area and summarizes routing information between areas.

- **Autonomous System Boundary Router (ASBR):** A router that redistributes routes from external routing protocols (EIGRP, BGP, static) into OSPF. Generates Type 5 LSAs for external routes.

- **Designated Router (DR):** On a multi-access network (Ethernet), the OSPF router elected to manage LSA flooding. All routers on the segment form Full adjacency with the DR and BDR only. Elected by highest interface priority, then highest Router ID.

- **Backup Designated Router (BDR):** Takes over if the DR fails. The router with the second-highest priority (or Router ID if tied) becomes the BDR.

- **Wildcard mask:** The inverse of a subnet mask, used in the OSPF `network` command to match interface IP addresses. Calculated by subtracting the subnet mask from 255.255.255.255.

- **Passive interface:** An OSPF interface that advertises its connected subnet but does not send or receive OSPF hello packets. Used on LAN interfaces facing end devices where no OSPF neighbor exists.

- **OSPF cost:** The metric OSPF uses to select best paths. Calculated as reference bandwidth / interface bandwidth (default reference: 100 Mbps). Lower cost is preferred.

---

## 2. OSPF Neighbor State Reference

| State | Description |
|---|---|
| Down | No hello packets received from the neighbor |
| Init | Hello received; local Router ID not yet in the neighbor's hello |
| 2-Way | Bidirectional communication confirmed; DR/BDR election occurs here |
| Exstart | Master/slave negotiation for database exchange |
| Exchange | Database Description (DBD) packets exchanged |
| Loading | Missing LSAs requested and received |
| Full | LSDB synchronized; adjacency complete |

Key rule: on point-to-point links, all neighbors reach Full. On broadcast (Ethernet) segments, DROther-to-DROther neighbor relationships stop at 2-Way — this is expected and not a failure.

---

## 3. OSPF Neighbor Failure Causes

| Cause | Effect | Fix |
|---|---|---|
| Mismatched Hello timer | Neighbor not seen as alive | Match timers with `ip ospf hello-interval` |
| Mismatched Dead timer | Neighbor declared dead prematurely | Match timers with `ip ospf dead-interval` |
| Mismatched area ID | Routers cannot form adjacency | Ensure both ends use same area number |
| Mismatched subnet mask | OSPF rejects the neighbor | Verify interface masks match on both ends |
| Authentication mismatch | Adjacency rejected | Match authentication type and key |
| MTU mismatch | Stuck in Exstart/Exchange | Match MTU or use `ip ospf mtu-ignore` |
| `passive-interface` on link | No hellos sent or accepted | Remove passive from neighbor-facing interfaces |

---

## 4. Wildcard Mask Quick Reference

| Prefix Length | Subnet Mask | Wildcard Mask |
|---|---|---|
| /8 | 255.0.0.0 | 0.255.255.255 |
| /16 | 255.255.0.0 | 0.0.255.255 |
| /24 | 255.255.255.0 | 0.0.0.255 |
| /25 | 255.255.255.128 | 0.0.0.127 |
| /26 | 255.255.255.192 | 0.0.0.63 |
| /27 | 255.255.255.224 | 0.0.0.31 |
| /28 | 255.255.255.240 | 0.0.0.15 |
| /29 | 255.255.255.248 | 0.0.0.7 |
| /30 | 255.255.255.252 | 0.0.0.3 |
| /32 | 255.255.255.255 | 0.0.0.0 |

---

## 5. OSPFv2 IOS Command Reference

| Task | Command | Mode |
|---|---|---|
| Enter OSPF routing process | `router ospf 1` | Global config |
| Configure Router ID | `router-id 1.1.1.1` | Router config |
| Advertise network (wildcard method) | `network 10.0.0.0 0.0.0.3 area 0` | Router config |
| Enable OSPF on interface (direct) | `ip ospf 1 area 0` | Interface config |
| Configure passive interface | `passive-interface GigabitEthernet0/1` | Router config |
| Set all interfaces passive by default | `passive-interface default` | Router config |
| Remove passive from specific interface | `no passive-interface GigabitEthernet0/0` | Router config |
| Set interface priority | `ip ospf priority 100` | Interface config |
| Set interface cost | `ip ospf cost 10` | Interface config |
| View neighbor adjacencies | `show ip ospf neighbor` | Privileged EXEC |
| View OSPF-enabled interfaces | `show ip ospf interface brief` | Privileged EXEC |
| View OSPF routes in routing table | `show ip route ospf` | Privileged EXEC |
| View full routing table | `show ip route` | Privileged EXEC |
| View OSPF process details | `show ip protocols` | Privileged EXEC |
| View LSDB contents | `show ip ospf database` | Privileged EXEC |
| Reset OSPF process | `clear ip ospf process` | Privileged EXEC |

---

## 6. Router ID Selection Rules

OSPF selects the Router ID in this priority order:

1. Manually configured with `router-id [x.x.x.x]` — always use this method
2. Highest IP address on any loopback interface (loopbacks never go down)
3. Highest IP address on any active physical interface at the time OSPF starts

If the Router ID is changed after OSPF has already started, the new ID does not take effect until the OSPF process is cleared with `clear ip ospf process` or the router is reloaded.

---

## 7. DR and BDR Election Reference

| Priority | Behavior |
|---|---|
| Highest (1-255) | Wins DR election |
| Second highest | Wins BDR election |
| 0 | Never becomes DR or BDR |

DR/BDR election is non-preemptive. Once a DR is elected, it retains the role even if a router with a higher priority later comes online. To force re-election, both routers must reset their OSPF process.

---

## 8. CCNA Exam Tips

1. The OSPF `network` command does not specify which network to advertise — it specifies which interfaces to enable OSPF on. Any interface whose IP address falls within the range defined by the network address and wildcard mask is included in OSPF.

2. Two OSPF routers whose interfaces are in different subnets will not form a neighbor relationship. The subnet mask mismatch causes OSPF to reject the neighbor even if Hello and Dead timers match.

3. DROther routers on a broadcast segment show 2-WAY state with other DROthers. This is correct behavior. The exam may present this as a failure scenario — recognize it as expected.

4. Passive interface prevents OSPF hellos from being sent or received on that interface. The connected subnet is still advertised to OSPF neighbors through other interfaces. Always configure passive interface on LAN segments with no OSPF neighbors.

5. The OSPF process ID (the number after `router ospf`) is locally significant. It does not need to match on neighboring routers. Two routers using `router ospf 1` and `router ospf 99` will still form an adjacency.

6. OSPF cost is calculated as: reference bandwidth (100 Mbps by default) / interface bandwidth. A FastEthernet interface (100 Mbps) has a cost of 1. A GigabitEthernet interface (1000 Mbps) also rounds to 1 with the default reference bandwidth. Use `auto-cost reference-bandwidth` to adjust the reference and differentiate high-speed interfaces.

7. When `show ip ospf neighbor` shows no output, OSPF neighbors have not formed. Check: correct network statements, no passive interface on the neighbor-facing link, matching area IDs, and matching subnet masks.

8. The `ip ospf [process-id] area [area-id]` interface command is an alternative to the `network` command. It directly places that interface in OSPF for that process and area. Many network engineers prefer this method because it avoids wildcard mask errors.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Write the OSPF neighbor state progression from memory (all seven states)
- [ ] Calculate the wildcard mask for /30, /28, /27, /25, and /24
- [ ] Write the full OSPF configuration for a two-router topology using both the network command and the ip ospf interface command methods
- [ ] Explain DR/BDR election rules and which state DROthers reach with each other
- [ ] Identify five reasons OSPF neighbors fail to form and the fix for each
- [ ] Explain why passive-interface is used and what it does (and does not) affect
- [ ] Complete the Module 08 Packet Tracer lab activity
- [ ] Post your Module 08 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 10. Supplemental Resources

The following open educational resources extend OSPFv2 concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Enterprise Networking, Security, and Automation, Chapter 1 (OSPF)** (skillsforall.com): This free chapter covers OSPFv2 single-area configuration, Router ID election, DR/BDR election, and the `show ip ospf neighbor` verification workflow with interactive Packet Tracer labs.

2. **Jeremy's IT Lab — OSPF (Days 24–27)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): Four video lessons covering OSPFv2 concepts, neighbor states, cost calculations, DR/BDR election, and troubleshooting. Jeremy's OSPF series is among the most-referenced CCNA study resources available.

3. **Cisco Learning Network — OSPF Study Group** (learningnetwork.cisco.com): The Cisco Learning Network community maintains extensive OSPF discussion threads covering neighbor state machine troubleshooting, cost manipulation, and exam-style scenario questions at CCNA difficulty.

4. **Cisco IOS OSPF Configuration Guide** (cisco.com): Cisco's official IOS configuration guide for OSPF covers all configuration commands, network statement syntax, passive interface behavior, and authentication options with complete CLI examples.

5. **GNS3 Academy — Free OSPF Lab Course** (academy.gns3.com): Free video lessons and GNS3 topology files for OSPFv2 multi-router lab configurations, allowing hands-on practice with neighbor state troubleshooting, DR/BDR observation, and cost manipulation outside of Packet Tracer's limitations.
