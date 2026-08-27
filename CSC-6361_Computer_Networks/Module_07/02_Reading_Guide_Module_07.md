# Reading Guide: Module 07 – Troubleshooting, Capstone Lab & Final Exam Preparation

## CSC-6361 Advanced Computer Networks | Graduate Level

## Week 7: November 30 – December 11, 2026 | Due: December 11, 2026

---

## Learning Objectives

By completing this reading guide, you will be able to:

1. Apply a structured troubleshooting methodology — OSI Layer-by-Layer, Divide and Conquer, or Follow-the-Path — to a given network failure scenario, identifying the correct approach and the first three diagnostic commands to run.
2. Diagnose OSPF neighbor adjacency failures from `show ip ospf neighbor` and `show ip ospf interface` output, mapping each stuck neighbor state (Down, ExStart, Loading) to its specific root cause.
3. Identify EIGRP Stuck-In-Active (SIA) conditions from `show ip eigrp topology active` output and explain both the immediate cause and the architectural fix (route summarization to limit Query scope).
4. Interpret BGP finite state machine output to determine root cause when a session is stuck in Idle, Active, OpenSent, or OpenConfirm, and diagnose the "established but no routes received" scenario including next-hop-self requirements.
5. Map the six CCNP ENCOR 350-401 exam domains to the modules of this course, identify your personal gap areas, and construct a structured preparation plan prioritizing the highest-weight domains.
6. Perform a structured multi-protocol troubleshooting exercise across a capstone topology integrating OSPF, STP, BGP, QoS, and ACL technologies simultaneously.

---

## Required Free Readings

### 1. Cisco OSPF Troubleshooting Guide — "OSPF Neighbor Problems Explained"

**URL:** [https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13733-26.html](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13733-26.html)

Focus sections:

- "Neighbor Relationship Requirements" — the complete list of parameters that must match for OSPF to form an adjacency.
- "OSPF Neighbor States" — each state and what failure at that state implies.
- "Troubleshooting with debug ip ospf adj" — read the sample debug output examples and practice interpreting them.

This is the single most referenced Cisco troubleshooting document for OSPF. Read it in full (approximately 15 pages). Graduate reading note: pay attention to the sections on MTU mismatch and duplicate router-ID — these are exam favorites.

### 2. Cisco BGP Troubleshooting Guide

**URL:** [https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html)

Focus sections:

- "Troubleshooting BGP Peer Relationships" — session state walkthrough with specific debug outputs.
- "Routes Not Being Advertised" — the next-hop issue in iBGP, route filtering, and network statement requirements.
- "BGP State Machine" — read the RFC 4271 reference table in this document.

### 3. Cisco EIGRP Troubleshooting — SIA Reference

**URL:** [https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html)

Focus sections: The DUAL algorithm section and the SIA (Stuck-In-Active) section. Understand why summarization fixes SIA propagation depth — this is the conceptual gap most students have coming out of Module 01.

### 4. CCNP ENCOR 350-401 Official Exam Topics (Cisco)

**URL:** [https://learningnetwork.cisco.com/s/encor-exam-topics](https://learningnetwork.cisco.com/s/encor-exam-topics)

This is your most important document for exam preparation. Download it. Print it. For every topic in every domain, ask yourself: "Can I configure this? Can I verify this? Can I diagnose a failure in this?" The topics in Domain 3 (Infrastructure) you can answer yes to all three — they map directly to course modules. The gaps are likely in Domain 6 (Automation) and parts of Domain 2 (Virtualization).

### 5. Cisco Learning Network — CCNP ENCOR Study Hub

**URL:** [https://learningnetwork.cisco.com/s/encor-study-materials](https://learningnetwork.cisco.com/s/encor-study-materials)

Free study resources organized by exam domain. Focus on the "Troubleshooting" section and the video resources for any domain where you rated yourself below 3/5 in the gap analysis.

---

## Key Concepts to Master

### Troubleshooting Decision Tree — Layer-by-Layer Reference

| Layer | Symptom | First `show` Command | What to Look For |
|---|---|---|---|
| 1 — Physical | Interface line protocol down | `show interfaces Gi0/1` | Input errors, CRC errors, resets — indicates physical/cable issue |
| 2 — Data Link | Ping to adjacent device fails | `show interfaces` | Duplex mismatch (half-duplex one side), encapsulation mismatch |
| 3 — Network | Route missing from table | `show ip route`, `show ip interface brief` | Interface down, wrong subnet, routing protocol not advertising |
| 4 — Transport | BGP Active, SSH fails | `telnet <peer> 179`, `show ip access-lists` | ACL blocking TCP port, firewall blocking return traffic |
| 5-7 — Application | Protocol adjacency not forming | Protocol-specific `show` command | Area mismatch, timer mismatch, authentication failure |

### OSPF Neighbor States — Failure Cause Reference

| State Stuck At | Most Likely Root Cause | Diagnosis Command |
|---|---|---|
| Down (no neighbor) | Area mismatch, passive interface, timer mismatch, Layer 1/2 issue | `show ip ospf interface` |
| Init | One-way hello — neighbor hears local router but local router doesn't hear neighbor (multicast blocked one way) | `debug ip ospf adj` |
| 2-Way | Normal state for DROther routers on broadcast. If expected to be Full, DR/BDR election issue | `show ip ospf neighbor` |
| ExStart | MTU mismatch (most common), duplicate router-ID | `show ip ospf interface` for MTU; `show ip ospf` for router-ID |
| Exchange | MTU mismatch causing DBD retransmission failure | `debug ip ospf adj` — look for retransmit messages |
| Loading | ACL blocking LSU in one direction; corrupted LSA | `show ip ospf statistics` — high retransmit count |

### BGP State Machine — Stuck State Diagnosis

| BGP State | Normal Duration | Stuck Here Means |
|---|---|---|
| Idle | Sub-second | `neighbor shutdown`; no route to peer; local BGP process not started |
| Connect | 1–3 seconds | Layer 3 unreachable; ACL blocking TCP 179; peer not running BGP |
| Active | Up to TCP retry timer | TCP SYN not completing — same as Connect but retrying. Check route to peer and port 179 |
| OpenSent | 1–5 seconds | Peer rejected OPEN: wrong remote-as configured; router-ID conflict |
| OpenConfirm | 1–3 seconds | BGP MD5 password mismatch — one side has `password` configured, other does not |
| Established | Indefinite | Normal. If PfxRcd = 0: check next-hop, route filters, missing `network` statement |

### CCNP ENCOR 350-401 Exam Domain Weights

| Domain | Topic Area | Weight | Course Modules Aligned |
|---|---|---|---|
| 1.0 | Architecture (SD-WAN, SD-Access, cloud) | 15% | Module 06 |
| 2.0 | Virtualization (VRF, GRE, IPsec) | 10% | Module 03 |
| 3.0 | Infrastructure (OSPF, EIGRP, BGP, STP, QoS) | 30% | Modules 01–05 |
| 4.0 | Network Assurance (SNMP, NetFlow, IP SLA) | 10% | Module 07 supplemental |
| 5.0 | Security (ACL, 802.1X, IPsec) | 20% | Module 05 |
| 6.0 | Automation (Python, REST, NETCONF, Ansible) | 15% | Supplemental only |

> Domain 3 at 30% is the largest domain and maps directly to five of the seven course modules. Students who have completed Modules 01–05 with mastery are already well-positioned for half the exam. The gaps requiring additional self-study are Domain 6 (Automation) and Domain 4 (Network Assurance tools like NetFlow and IP SLA).

---

## Verification Commands Master Reference

The following 15 commands are the most frequently tested troubleshooting commands on the CCNP ENCOR exam. Practice reading their output until you can immediately identify what is normal and what indicates a fault.

```cisco
! === OSPF ===
show ip ospf neighbor                  ! Neighbor states — anything other than FULL is a fault
show ip ospf interface Gi0/1           ! Area, timers, MTU, passive flag, DR/BDR
show ip ospf database summary          ! Type 3 LSAs — inter-area routes from ABRs
show ip route ospf                     ! OSPF routes in routing table — O, O IA, O E1, O E2

! === EIGRP ===
show ip eigrp neighbors                ! Neighbor table — hold time counting down (0 = dead)
show ip eigrp topology all-links       ! All paths including non-Feasible Successors
show ip eigrp topology active          ! Any prefix in Active state = SIA risk

! === BGP ===
show bgp ipv4 unicast summary          ! All BGP peers — State/PfxRcd; Active state = problem
show bgp neighbors 10.0.0.2           ! Full neighbor detail including BGP state
show bgp ipv4 unicast 192.168.1.0     ! Per-prefix detail: best path, next-hop, attributes

! === Switching ===
show spanning-tree vlan 10             ! Root bridge, port roles (Root, Designated, Alternate)
show interfaces trunk                  ! Trunk ports, allowed VLANs, native VLAN

! === QoS ===
show policy-map interface Gi0/2        ! Per-class matched packets/bytes — zero matches = wrong classifier

! === Security ===
show ip access-lists                   ! ACL hit counters — zero hits on a rule you expect to fire = possible issue

! === General ===
show interfaces GigabitEthernet0/1     ! Input/output errors, CRC, resets — Layer 1/2 health
```

---

## Graduate Discussion Prompt

Due: Wednesday, December 9, 2026 at 11:59 PM CST — Initial Post

Due: Sunday, December 13, 2026 at 11:59 PM CST — Peer Responses

See the Module 07 Discussion Board for the full capstone discussion prompt.

---

## Supplemental Resources

### 1. Cisco Troubleshooting and Fault Management Guide — BGP

[https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html)

Systematic BGP troubleshooting methodology with debug commands and common failure scenarios. Read the "BGP Not Sending Updates" section in full — it covers all three causes of missing route advertisements.

### 2. CCNP ENCOR Official Exam Topics (Cisco)

[https://learningnetwork.cisco.com/s/encor-exam-topics](https://learningnetwork.cisco.com/s/encor-exam-topics)

The authoritative CCNP ENCOR 350-401 exam blueprint. Use this as your gap analysis checklist. Every topic listed here is fair game on the exam.

### 3. Packetlife.net Cheat Sheets

[https://packetlife.net/library/cheat-sheets/](https://packetlife.net/library/cheat-sheets/)

High-quality single-page cheat sheets for OSPF, BGP, spanning tree, QoS DSCP values, subnetting, and more. The QoS DSCP/PHB cheat sheet and the spanning tree cheat sheet are particularly useful for the exam.

### 4. GNS3 Network Simulator

[https://gns3.com/software/download](https://gns3.com/software/download)

Free network simulation platform for practicing all course topics with real Cisco IOS images (or FRRouting open-source alternatives). If you want more advanced OSPF multi-area or BGP practice beyond Packet Tracer's limitations, GNS3 is the tool.

### 5. Boson ExSim-Max for CCNP ENCOR

[https://www.boson.com/practice-exam/350-401-cisco-ccnp-encor-practice-exam](https://www.boson.com/practice-exam/350-401-cisco-ccnp-encor-practice-exam)

The highest-quality commercial practice exam for CCNP ENCOR. Each question includes a detailed explanation of why each answer is correct or incorrect — essential for identifying knowledge gaps. Not free, but worth the investment if you are serious about certification.
