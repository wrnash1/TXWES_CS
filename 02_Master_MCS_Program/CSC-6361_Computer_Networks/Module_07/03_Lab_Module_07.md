# Lab Assignment: Module 07 – Capstone Lab: Multi-Technology Troubleshooting

## CSC-6361 Advanced Computer Networks | Graduate Level

## Due: Friday, December 11, 2026 at 11:59 PM CST

---

## Lab Overview

**Estimated Time:** 4–5 hours
**Tools Required:** Cisco Packet Tracer (free — download at netacad.com)
**Deliverables:** (1) Completed `.pkt` Packet Tracer file, (2) Professional Capstone Lab Report (PDF)

This is the capstone lab for CSC-6361 Advanced Computer Networks. It integrates technologies from all seven modules into a single enterprise network topology. Unlike previous labs — where you built and configured a topology from scratch — this capstone has two phases:

- Phase 1: Verify the fully-configured baseline topology using a structured checklist. This proves you understand what a correctly operating network looks like across all protocol domains.
- Phase 2: Five specific "breaks" are injected into the topology. You must diagnose and fix each one using the structured troubleshooting methodology from Module 07 Part 1. Document your process for each break.

This lab simulates the professional reality of network operations: you inherit a complex, partially-broken network, and your job is to restore it — methodically, with documentation.

---

## Lab Topology

```text
                         OSPF AREA 0 (BACKBONE)
     +-------------------+                 +-------------------+
     |     R1-HQ         |                 |     R2-Core       |
     |   1.1.1.1/32 Lo0  |10.0.0.0/30      |   2.2.2.2/32 Lo0  |
     | Gi0/0: 10.0.0.1   +-----------------+ Gi0/0: 10.0.0.2   |
     | Gi0/1: 10.0.1.1   |                 | (Area 0 only)     |
     | Gi0/2: WAN         |                 +-------------------+
     +--------+----------+
              | Gi0/1 (10.0.1.0/30)
              |
     +--------+----------+
     |     R3-ABR         |   OSPF AREA 1
     |   3.3.3.3/32 Lo0  |
     | Gi0/0: 10.0.1.2   | (Area 0 side)
     | Gi0/1: 10.1.0.1   | (Area 1 side — 10.1.0.0/30)
     +--------+----------+
              | Gi0/1 (10.1.0.0/30)
              |
     +--------+----------+
     |    R4-Branch       |
     |   4.4.4.4/32 Lo0  |
     | Gi0/0: 10.1.0.2   | (Area 1)
     | LAN: 192.168.1.0  |
     +-------------------+

     GRE OVERLAY TUNNEL (simulating SD-WAN):
       Tunnel0: R1-HQ (source Lo0 1.1.1.1) <---> R4-Branch (source Lo0 4.4.4.4)
       Tunnel IPs: R1 = 172.16.0.1/30, R4 = 172.16.0.2/30
       BGP AS 65000 runs over Tunnel0 (overlay routing analog)

     eBGP PEERING (internet simulation):
       R5-Edge Gi0/0: 10.0.2.1/30 (to R1-HQ Gi0/2)
       R5-Edge Gi0/1: 203.0.113.1/30 (to R6-ISP)
       R6-ISP Gi0/0: 203.0.113.2/30 (ISP side)
       R5 AS 65100, R6 AS 65200

     SWITCHING LAYER:
       SW1 — Core switch (root for VLAN 10)
       SW2 — Access switch (root for VLAN 20)
       Trunk: SW1 Gi0/1 <---> SW2 Gi0/1 (VLANs 10, 20)
       SW1 connects to R1-HQ Gi0/3 (router-on-a-stick, subinterfaces)

     QoS:
       Policy-map ENTERPRISE-QOS applied outbound on R1-HQ Gi0/2 (WAN to R5-Edge)
       Classes: VOICE-EF (DSCP 46), DATA-AF31 (DSCP 26), DEFAULT-CLASS

     ACL:
       Extended ACL AREA1-FILTER applied inbound on R3-ABR Gi0/1 (Area 1 interface)
```

---

## Addressing Table

| Device | Interface | IP Address | Description |
|---|---|---|---|
| R1-HQ | Lo0 | 1.1.1.1/32 | OSPF router-ID, GRE tunnel source |
| R1-HQ | Gi0/0 | 10.0.0.1/30 | OSPF Area 0 link to R2-Core |
| R1-HQ | Gi0/1 | 10.0.1.1/30 | OSPF Area 0 link to R3-ABR |
| R1-HQ | Gi0/2 | 10.0.2.2/30 | WAN link to R5-Edge |
| R1-HQ | Gi0/3.10 | 192.168.10.1/24 | Router-on-a-stick subinterface VLAN 10 |
| R1-HQ | Gi0/3.20 | 192.168.20.1/24 | Router-on-a-stick subinterface VLAN 20 |
| R1-HQ | Tunnel0 | 172.16.0.1/30 | GRE overlay to R4-Branch |
| R2-Core | Lo0 | 2.2.2.2/32 | OSPF router-ID |
| R2-Core | Gi0/0 | 10.0.0.2/30 | OSPF Area 0 link to R1-HQ |
| R3-ABR | Lo0 | 3.3.3.3/32 | OSPF router-ID |
| R3-ABR | Gi0/0 | 10.0.1.2/30 | OSPF Area 0 side |
| R3-ABR | Gi0/1 | 10.1.0.1/30 | OSPF Area 1 side |
| R4-Branch | Lo0 | 4.4.4.4/32 | OSPF router-ID, GRE tunnel destination |
| R4-Branch | Gi0/0 | 10.1.0.2/30 | OSPF Area 1 link to R3-ABR |
| R4-Branch | Gi0/1 | 192.168.1.1/24 | Branch LAN gateway |
| R4-Branch | Tunnel0 | 172.16.0.2/30 | GRE overlay to R1-HQ |
| R5-Edge | Gi0/0 | 10.0.2.1/30 | Link to R1-HQ (OSPF redistributed into BGP here) |
| R5-Edge | Gi0/1 | 203.0.113.1/30 | eBGP link to R6-ISP |
| R6-ISP | Gi0/0 | 203.0.113.2/30 | ISP eBGP peer |
| R6-ISP | Lo0 | 8.8.8.8/32 | Simulated internet destination |
| SW1 | VLAN 10 SVI | 192.168.10.2/24 | Core switch management |
| SW2 | VLAN 20 SVI | 192.168.20.2/24 | Access switch management |

---

## Lab Instructions

### Phase 1: Verify the Baseline Topology (30 pts)

The pre-configured `.pkt` file contains a fully operational baseline topology. Before anything is broken, verify each technology domain using the commands below and record the output as your baseline. If any baseline check fails, debug the issue before proceeding to Phase 2 — Phase 2 breaks are injected on top of a working baseline.

#### Baseline Check 1: OSPF Multi-Area (Module 01)

Run the following on each router and confirm expected output:

```cisco
! On R1-HQ:
show ip ospf neighbor
! Expected: R2-Core (10.0.0.2) FULL, R3-ABR (10.0.1.2) FULL

! On R3-ABR:
show ip ospf database summary
! Expected: Type 3 LSA for 10.1.0.0/30 (Area 1 subnet) in the database

! On R2-Core:
show ip route ospf
! Expected: O IA route for 10.1.0.0/22 (summary from R3-ABR)
```

**Screenshot Checkpoint 1:** `show ip ospf neighbor` on R1-HQ. Annotate: which neighbors are present and their state.

#### Baseline Check 2: Spanning Tree (Module 02)

```cisco
! On SW1:
show spanning-tree vlan 10
! Expected: SW1 is Root Bridge for VLAN 10 (This bridge is the root)

! On SW2:
show spanning-tree vlan 20
! Expected: SW2 is Root Bridge for VLAN 20 (This bridge is the root)

! On SW1:
show interfaces trunk
! Expected: Gi0/1 trunk carrying VLANs 10 and 20
```

**Screenshot Checkpoint 2:** `show spanning-tree vlan 10` on SW1, `show spanning-tree vlan 20` on SW2.

#### Baseline Check 3: BGP and Redistribution (Module 03)

```cisco
! On R5-Edge:
show bgp ipv4 unicast summary
! Expected: R6-ISP (203.0.113.2) in Established state, PfxRcd > 0

! On R5-Edge:
show bgp ipv4 unicast
! Expected: OSPF-originated prefixes (10.0.0.0 subnets) visible in BGP table
```

**Screenshot Checkpoint 3:** `show bgp ipv4 unicast summary` on R5-Edge.

#### Baseline Check 4: GRE Overlay Tunnel (Module 06)

```cisco
! On R1-HQ:
show interfaces Tunnel0
! Expected: Line protocol is up

! On R1-HQ:
show ip bgp summary
! Expected: R4-Branch overlay peer (172.16.0.2) in Established state
```

**Screenshot Checkpoint 4:** `show interfaces Tunnel0` on R1-HQ — confirm up/up.

#### Baseline Check 5: QoS (Module 04)

```cisco
! On R1-HQ:
show policy-map interface GigabitEthernet0/2
! Expected: Class VOICE-EF and Class DATA-AF31 showing matched packet counts
! (generate test traffic to produce matches if counts are zero at startup)
```

**Screenshot Checkpoint 5:** `show policy-map interface Gi0/2` on R1-HQ.

#### Baseline Check 6: ACL (Module 05)

```cisco
! On R3-ABR:
show ip access-lists AREA1-FILTER
! Expected: ACL present with permit/deny entries and hit counters incrementing
```

**Screenshot Checkpoint 6:** `show ip access-lists` on R3-ABR.

---

### Phase 2: Break Scenarios — Diagnose and Fix Each (60 pts, 12 pts each)

Load the "break" version of the `.pkt` file provided in the Canvas assignment. Five specific faults have been introduced. You will not be told which five. Follow the structured troubleshooting methodology: observe the symptom, identify the layer, run targeted `show` commands, identify the root cause, apply the fix, verify resolution.

#### Break Scenario Instructions

For each break you find, document:

1. Observed symptom (what failed — include the specific `show` command output that revealed it).
2. Troubleshooting commands run and what each revealed.
3. Root cause identified.
4. Configuration fix applied (show the specific command).
5. Verification after fix (show command confirming resolution).

Use the following format in your lab report for each break:

```text
Break #[N]: [Technology Domain]
Symptom: [What failed and the show command that revealed it]
Diagnosis: [Commands run and what each showed]
Root Cause: [Specific misconfiguration or missing configuration]
Fix Applied: [Exact IOS command(s)]
Verification: [Show command output confirming resolution]
```

#### The Five Breaks

The five breaks span the following technology domains (in no particular order — you must discover which is which):

Break A — OSPF area misconfiguration on R4-Branch. R4-Branch's Gi0/0 interface is placed in the wrong OSPF area, preventing R3-ABR from forming an adjacency with R4.

Break B — STP priority misconfiguration on SW2. SW2's VLAN 20 bridge priority is incorrect, causing SW1 to win the root election for VLAN 20. Traffic in VLAN 20 traverses a suboptimal path through SW1.

Break C — Missing redistribution route-map on R5-Edge. The `redistribute ospf 1 subnets` command on R5-Edge is present but the route-map that prevents redistribution loop-back into OSPF has been removed. Some internal OSPF prefixes begin appearing as O E2 routes on routers that should never see them as external.

Break D — QoS class-map DSCP mismatch on R1-HQ. The `class-map VOICE-EF` is matching `dscp ef` (DSCP 46) but the voice traffic being generated is marked DSCP 40 (CS5). The EF priority queue shows zero matched packets while the default class is absorbing all traffic.

Break E — ACL missing `established` keyword on R3-ABR. The `AREA1-FILTER` ACL on R3-ABR permits TCP traffic outbound from Area 1 but does not permit established return TCP traffic inbound. New TCP connections from Area 0 to Area 1 hosts fail (SYN-ACK is dropped), while pings and UDP succeed.

---

### Phase 3: Document Your Troubleshooting Methodology (10 pts)

After completing all five break diagnoses, write a methodology reflection in your lab report (one page, 300–400 words). Address:

1. For which break did you use OSI Layer-by-Layer methodology? Which break required Divide and Conquer? Which was solved by Follow-the-Path / traceroute? Explain why each methodology was appropriate for that specific break.
2. Which break was the most difficult to diagnose, and why? What `show` command finally revealed the root cause?
3. In a production network, these breaks could coexist simultaneously — you would not know how many or which types. How would you prioritize which to investigate first if all five symptoms appeared at once? Describe your triage logic.

---

## Lab Report Requirements (Graduate Standard)

Your PDF lab report must include:

1. Topology Diagram — annotated screenshot of the Packet Tracer topology with all device labels and key interface IPs visible.
2. All 6 Baseline Screenshot Checkpoints — labeled and annotated with what each verifies.
3. Five Break Documentation Sections — one per break, using the format specified above.
4. Methodology Reflection — Phase 3 written analysis (300–400 words).
5. Troubleshooting Log — a running log of the sequence in which you discovered and addressed each break, including any dead ends or incorrect initial hypotheses. Showing your reasoning process is as important as the correct answer.

---

## Grading Rubric

| Component | Points |
|---|---|
| Phase 1: Baseline Verification (all 6 checkpoints) | 30 |
| Phase 2: Break Scenario A (OSPF) | 12 |
| Phase 2: Break Scenario B (STP) | 12 |
| Phase 2: Break Scenario C (Redistribution) | 12 |
| Phase 2: Break Scenario D (QoS) | 12 |
| Phase 2: Break Scenario E (ACL) | 12 |
| Phase 3: Methodology Reflection | 10 |
| **Total** | **100** |

**Submission:** Upload both the `.pkt` file AND the PDF report to Canvas Module 07 Lab Assignment by Friday, December 11, 2026 at 11:59 PM CST.

---

## Part 9 — Challenge Exercise

### Challenge 1: Structured Troubleshooting Methodology Applied

Using the break-version topology, introduce a sixth hidden break of your own design — one that has not been introduced by the instructor. Choose a technology domain that is not already covered by the five instructor breaks (options: EIGRP if applicable, GRE tunnel failure, BGP next-hop unreachable, spanning tree topology change storm). Document:

1. What break you introduced (the exact configuration command you changed or removed).
2. The symptom a network engineer would observe.
3. The first three `show` commands an engineer would run and what each would reveal.
4. The root cause and fix.

Then swap your break scenario description (not the `.pkt` file) with a classmate in the discussion board. Have them solve your break using only your symptom description and their knowledge of the methodology — without seeing your diagnosis.

### Challenge 2: CCNP ENCOR Exam Readiness Self-Assessment

1. Download the official CCNP ENCOR 350-401 exam topics. For each major domain, rate your confidence level (1–5 scale) and identify the single topic within that domain you feel least prepared on.
2. Create a 3-week study plan that prioritizes your weakest domains. For each domain, identify at least one specific free resource (Cisco documentation, RFC, or Cisco Learning Network content) and a realistic daily study time allocation.
3. Take one full practice exam from a reputable source (Boson, Pearson, or Cisco official practice). Record your score by domain, identify the top 3 question categories where you lost the most points, and write a one-paragraph explanation of the correct answer for each missed question type.
4. Schedule your CCNP ENCOR exam attempt — even a provisional date. The act of scheduling creates accountability. Use [https://home.pearsonvue.com/cisco](https://home.pearsonvue.com/cisco) to find available dates at your nearest testing center or online proctored slot.

### Reflection Questions

1. Looking back across all 7 modules of this course, which single networking technology or concept do you believe will have the most significant impact on enterprise network engineering over the next five years? Support your answer with specific technical reasoning connected to the course material — this is not an opinion question, it is a technical prediction question.
2. Describe a specific complex network problem you would feel confident troubleshooting after completing this course that you could not have approached systematically before. Be specific about the tools, commands, and methodology you would use — and identify one remaining area where you recognize a knowledge gap.
