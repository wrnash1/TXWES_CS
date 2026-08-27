# Video Script: Module 07 – Troubleshooting, Capstone Lab & Final Exam Preparation

## CSC-6361 Advanced Computer Networks | Graduate Level

## Part 1 of 2 | Estimated Duration: 15–18 minutes

## Week 7: November 30 – December 11, 2026 | Due: December 11, 2026

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CSC-6361 Advanced Computer Networks | Module 07: Structured Troubleshooting Methodology — OSPF, EIGRP, BGP | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Welcome to Module 07

[00:00 – 02:30]
[SHOW SLIDE: Professor Nash on camera, network troubleshooting flowchart visible behind.]

Welcome to Module 07 — the final module of CSC-6361. This week we bring everything together. We have spent six modules building expertise in OSPF, EIGRP, BGP, switching, QoS, security, and cloud/SD-WAN. This week is about applying that knowledge systematically when things go wrong — and things always go wrong in production networks.

Module 07 has two components. Part 1 — this lecture — focuses on structured troubleshooting methodology and how to apply it to the three routing protocols you know best: OSPF, EIGRP, and BGP. Part 2 covers the capstone lab preview and the CCNP ENCOR 350-401 exam strategy. The Module 07 lab is the capstone — a multi-technology topology that deliberately breaks things across all seven modules, and your job is to find and fix each issue.

Let me make one point about the professional value of this week's content. On the CCNP ENCOR exam, a substantial percentage of questions involve interpreting `show` command output and determining what is wrong. In your career, the ability to diagnose a complex multi-vendor, multi-protocol network failure in under 30 minutes is what separates senior engineers from everyone else. That skill is learnable, and it starts with a methodology — not luck.

Let's begin.

---

### Section 2: Structured Troubleshooting Methodology

[02:30 – 06:00]
[SHOW DIAGRAM: Troubleshooting methodology flowchart — three approaches labeled OSI Layer-by-Layer, Divide and Conquer, Follow-the-Path]

The CCNP ENCOR exam and Cisco's official troubleshooting framework recognize three primary structured methodologies. Understanding when to apply each is itself a professional skill.

#### Methodology 1: OSI Layer-by-Layer (Bottom-Up)

Start at Layer 1 (physical) and work upward. Do not skip layers.

The logic: a problem at a lower layer will produce symptoms at higher layers. A BGP session that never comes up (Layer 4) might be caused by an ACL blocking TCP port 179 — but it might also be caused by a duplex mismatch (Layer 1) causing excessive CRC errors that prevent TCP from completing the three-way handshake.

Structured Layer-by-Layer approach:

| Layer | Check | Command |
|---|---|---|
| 1 — Physical | Interface up/up, cable, SFP | `show interfaces` (look for input errors, CRC, resets) |
| 2 — Data Link | Duplex, VLAN membership, MAC table | `show interfaces`, `show mac address-table` |
| 3 — Network | IP addressing, routing table, reachability | `show ip interface brief`, `show ip route`, `ping` |
| 4 — Transport | TCP/UDP port reachability, ACLs blocking ports | `telnet <ip> <port>`, `show ip access-lists` |
| 5–7 — Application | Protocol-specific adjacency, authentication | Protocol-specific `show` commands |

#### Methodology 2: Divide and Conquer

Identify the midpoint of the path and test from there. If the midpoint works, the problem is in the second half. If the midpoint fails, the problem is in the first half. Repeat until the faulty segment is isolated.

Best used when: the network path is long (many hops) and you have console access to intermediate devices. Divide and conquer cuts the diagnosis time roughly in half at each step.

#### Methodology 3: Follow-the-Path (Top-Down or End-to-End Trace)

Start at the source, follow traffic hop by hop to the destination, verifying routing and forwarding at each hop. Use `traceroute` to identify where forwarding fails, then investigate that specific device.

Best used when: you have limited access (can only run commands from one end) or the problem is intermittent (traceroute reveals inconsistent paths suggesting load balancing or route flapping).

> **Graduate Exam Strategy:** The CCNP ENCOR troubleshooting questions almost always give you a specific symptom and specific `show` command output. Apply the methodology: identify the layer the symptom is at, work downward to find the root cause. Do not guess protocol-specific causes before confirming lower layers are functional.

---

### Section 3: OSPF Neighbor Failure Scenarios

[06:00 – 10:00]
[SHOW DIAGRAM: OSPF neighbor state machine — Down → Init → 2-Way → ExStart → Exchange → Loading → Full]

OSPF neighbors that fail to reach the Full state are one of the most common topics on the CCNP ENCOR exam and one of the most common real-world troubleshooting scenarios. A healthy OSPF neighbor relationship progresses through: Down → Init → 2-Way → ExStart → Exchange → Loading → Full. Neighbors stuck in a state other than Full (or 2-Way for DROther routers) indicate a problem at a specific stage.

#### Failure Scenario 1: Neighbors Never Appear (Stuck in Down)

Root causes:

- Interface not in OSPF process: `network` statement does not match the interface IP.
- Interface is passive: `passive-interface` configured — OSPF hellos are suppressed.
- Layer 1/2 issue: interface is down/down or down/up.
- Area mismatch: one router is in Area 0, the other in Area 1 on the same link.
- Hello/dead timer mismatch: defaults are 10s/40s on broadcast, 30s/120s on serial. Both sides must match.

Diagnosis:

```cisco
show ip ospf interface GigabitEthernet0/1   ! Verify area, timers, network type
show ip ospf neighbor                        ! Check if neighbor is visible at all
debug ip ospf adj                            ! Real-time adjacency events
```

If `show ip ospf interface` shows the interface as passive, that is your root cause. If timers don't match between the two sides, OSPF will not form a neighbor relationship.

#### Failure Scenario 2: Stuck in ExStart or Exchange

Root causes:

- MTU mismatch: OSPF uses the interface MTU to set the DD (Database Description) packet size. If Router A has MTU 1500 and Router B has MTU 9000 (jumbo frames), DBD packets from B exceed A's MTU — A drops them and the exchange never completes. This is the most common ExStart failure.
- Duplicate router-IDs: two routers have the same router-ID (from duplicate loopback addresses or static configuration).

Diagnosis:

```cisco
show ip ospf interface                      ! Check MTU value on each side
show ip ospf                                ! Verify router-ID
debug ip ospf adj                           ! Shows "Mismatch in MTU" in output
```

Fix for MTU mismatch when you cannot change the physical MTU: apply `ip ospf mtu-ignore` on the interface. This tells OSPF to skip MTU comparison in DBD exchanges. Use cautiously — if actual MTU is mismatched, IP fragmentation will still occur on data traffic.

#### Failure Scenario 3: Stuck in Loading

Root causes:

- Corrupted LSA database: rare, but occurs when an LSA has a sequence number conflict. Usually self-corrects after the dead timer expires.
- One-way LSA flooding: a firewall or ACL is blocking OSPF LSU (Link State Update) packets in one direction while allowing hellos and DBD in both directions.

Diagnosis:

```cisco
show ip ospf database                        ! Look for unusual LSA counts
debug ip ospf database-timer                 ! Real-time database synchronization events
show ip ospf statistics                      ! Check for excessive LSA retransmissions
```

#### OSPF Authentication Failures

If OSPF MD5 authentication is configured on one side but not the other, or with mismatched keys, neighbors will not form. The `debug ip ospf adj` output will show `Dead timer expired` or `Mismatched Authentication type`.

```cisco
show ip ospf interface                      ! Verify authentication type on each interface
debug ip ospf adj                           ! Shows authentication failure reason
```

---

### Section 4: EIGRP Troubleshooting

[10:00 – 13:30]
[SHOW DIAGRAM: EIGRP neighbor states and DUAL finite state machine — Passive (stable), Active (querying for new path)]

#### Failure Scenario 1: EIGRP Neighbors Not Forming

Root causes with EIGRP-specific additions beyond the OSPF parallels:

- AS number mismatch: EIGRP routers must be in the same autonomous system. A common misconfiguration is AS 100 on one router and AS 1 on another — no error message is generated, neighbors simply never appear.
- K-value mismatch: EIGRP's composite metric uses K-values (K1=bandwidth, K3=delay are enabled by default; K2, K4, K5 are zero). If K-values don't match, EIGRP will log "K-value mismatch" and refuse to form a neighbor relationship.
- Passive interface: same behavior as OSPF — `passive-interface` suppresses EIGRP hellos on that interface.

Diagnosis:

```cisco
show ip eigrp neighbors               ! Check neighbor count and hold time countdown
show ip eigrp interfaces detail       ! Verify interfaces, hello/hold timers, K-values shown
debug ip eigrp notifications          ! Real-time neighbor formation events
```

If `show ip eigrp interfaces detail` shows `K1=1, K2=0, K3=1, K4=0, K5=0` on one router and different values on another, that mismatch is the root cause.

#### Failure Scenario 2: SIA — Stuck-In-Active

This is a critical EIGRP failure mode for both the CCNP ENCOR exam and production network operations.

When EIGRP loses its Successor and has no Feasible Successor (no backup path meets the Feasibility Condition `RD < FD`), it enters Active state for that prefix and sends Query packets to all EIGRP neighbors asking if they have an alternative path. Each neighbor must reply with a Reply packet.

SIA occurs when a neighbor fails to reply to an EIGRP Query within the SIA timer (default 90 seconds). The local router resets the neighbor relationship — tearing down what may otherwise be a healthy adjacency — to break the stuck condition. From the operations team's perspective this looks like a neighbor flap on a circuit that had no physical issues.

Root causes:

- High-latency WAN link causing Query/Reply packets to time out before the 90-second SIA timer expires.
- Neighbor CPU overloaded and unable to process Queries in time.
- Query propagation depth: in large EIGRP networks, a topology change can propagate Queries 10 or more hops deep. Any slow response anywhere in the chain causes SIA at the originating router.

Diagnosis:

```cisco
show ip eigrp topology all-links      ! Shows ALL paths including non-Feasible Successors
show ip eigrp topology active         ! Shows only prefixes currently in Active state
debug eigrp fsm                       ! Real-time DUAL FSM events (use carefully in production)
```

The standard fix for SIA propagation depth is EIGRP route summarization. A summary route suppresses Queries at the summarizing router boundary — when a Query arrives for a prefix covered by the summary, the summarizing router replies immediately with the summary rather than forwarding the Query further into the network.

---

### Section 5: BGP Session Troubleshooting

[13:30 – 17:00]
[SHOW DIAGRAM: BGP finite state machine — Idle → Connect → Active → OpenSent → OpenConfirm → Established]

BGP has a formal finite state machine defined in RFC 4271. Understanding which state a stuck BGP session is in immediately narrows the root cause to a specific layer or configuration element.

#### BGP State Machine Reference

| State | Meaning | Stuck Here Indicates |
|---|---|---|
| Idle | BGP not attempting to connect | `neighbor shutdown`; no route to peer IP; BGP process not running |
| Connect | TCP SYN sent, waiting for SYN-ACK | Layer 3 reachability issue; ACL blocking TCP 179; peer not running BGP |
| Active | TCP connection failed, retrying | Persistent Connect failure — TCP three-way handshake never completing |
| OpenSent | TCP connected, BGP OPEN sent | Peer rejected OPEN: AS number mismatch, router-ID conflict |
| OpenConfirm | OPEN received and accepted, waiting for KEEPALIVE | Authentication mismatch (MD5 password set on one side only) |
| Established | Session up, exchanging routes | Normal — but if PfxRcd=0, check address family, next-hop, or route filters |

Diagnosis commands:

```cisco
show bgp neighbors 10.0.0.2               ! Full BGP neighbor state and statistics
show bgp ipv4 unicast summary             ! All peers — State/PfxRcd column at a glance
debug ip bgp 10.0.0.2 events             ! Real-time BGP events for one specific peer
```

#### Scenario: Session Stays in Active State

- Verify TCP port 179 reachability: `telnet <peer-IP> 179` from the BGP router. If the telnet fails, a firewall or ACL is blocking the BGP port.
- Verify route to peer: `show ip route <peer-IP>`. If no route exists, the TCP session can never establish.
- For iBGP sessions with loopback-addressed peers: verify `update-source Loopback0` is configured under the neighbor statement. Without this, TCP originates from a physical interface IP that the remote router does not have configured as an allowed neighbor.

#### Scenario: Session Established but No Routes Received

This is the most operationally dangerous BGP problem because the session appears healthy while traffic is silently not forwarding.

Root causes:

- Next-hop not reachable: in iBGP, the NEXT_HOP attribute is not automatically changed. If Router A receives an eBGP route with next-hop 203.0.113.1 and reflects it to iBGP peer Router B, Router B must have a route to 203.0.113.1 in its routing table or the BGP route will not be installed. The standard fix is `neighbor <iBGP-peer> next-hop-self` on the eBGP-facing router.
- Route filtering: an inbound `route-map` or `prefix-list` is silently dropping the prefixes. Diagnose with `show bgp neighbors <peer> received-routes` (requires `neighbor <peer> soft-reconfiguration inbound` to be configured first).
- No `network` statement or redistribution: BGP does not automatically originate connected routes. Each prefix must be explicitly configured.

```cisco
show bgp ipv4 unicast neighbors 10.0.0.2 received-routes  ! Routes before inbound filters
show bgp ipv4 unicast neighbors 10.0.0.2 routes           ! Routes after inbound filters applied
show bgp ipv4 unicast 192.168.1.0                         ! Per-prefix: path, next-hop, status
```

---

### Section 6: CCNP Exam Strategy for Troubleshooting Questions

[17:00 – 19:30]
[SHOW SLIDE: CCNP ENCOR troubleshooting question strategy — read symptom, identify layer, eliminate wrong options systematically]

Troubleshooting questions on the CCNP ENCOR 350-401 exam are typically structured as: "A network engineer runs the following command and observes this output. What is the most likely root cause?" You are given one or more `show` command outputs and four answer choices.

#### The Systematic Approach — Apply Every Time

1. Read the symptom first. What is actually broken? Packets not forwarding? Adjacency not forming? Route missing from the routing table? Identify the exact failure layer before reading the output.

2. Read the `show` command output carefully. Look for specific indicators:
   - OSPF: neighbor state not Full, area mismatch in `show ip ospf interface`, timer values, passive-interface flag.
   - EIGRP: neighbor not present, Active state prefix in `show ip eigrp topology active`, K-value mismatch in debug output.
   - BGP: session state in anything other than Established, PfxRcd count of 0 when routes are expected.

3. Eliminate impossible answers first. If the BGP session is in Active state, the problem is at Layer 3 or Layer 4 (reachability or port filtering). Any answer about route filtering, BGP communities, or next-hop-self can be eliminated immediately.

4. Choose the most specific root cause. CCNP exam distractors name real problems that apply to different scenarios. The correct answer is the one that directly explains the specific output shown — not just a plausible general networking problem.

> **Final Exam Tip:** The single most valuable CCNP preparation for troubleshooting questions is to deliberately break your Packet Tracer topologies. Misconfigure an OSPF timer. Add an ACL blocking port 179. Set the wrong EIGRP AS number. Practice diagnosing each break from the `show` command output alone, without looking at the configuration. That is exactly what the exam tests.

---

### Section 7: Part 1 Summary

[19:30 – 21:00]
[SHOW SLIDE: Module 07 Part 1 key concept summary]

In Part 1 you have learned:

- Structured troubleshooting methodology: OSI Layer-by-Layer (bottom-up), Divide and Conquer, and Follow-the-Path — and when each methodology is most appropriate.
- OSPF neighbor failures: how to diagnose from the neighbor state machine (Down, ExStart, Loading) and the specific root cause each stuck state indicates.
- EIGRP troubleshooting: AS number and K-value mismatches, and SIA — Stuck-In-Active — its propagation depth root cause and the summarization fix.
- BGP state machine: what each non-Established state reveals, the next-hop-self iBGP requirement, and how to detect silent route filtering.
- CCNP exam strategy: symptom-first, layer identification, eliminate impossible answers, choose the most specific root cause.

In Part 2, we preview the capstone lab topology — which integrates all seven modules — and walk through the CCNP ENCOR 350-401 exam domains, weights, timing strategy, and final preparation approach.

---

### Additional Resources

- Cisco OSPF Troubleshooting Guide: [https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13733-26.html](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13733-26.html)
- Cisco BGP Troubleshooting Guide: [https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html)
- Cisco EIGRP Troubleshooting White Paper: [https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html)
- CCNP ENCOR 350-401 Exam Topics: [https://learningnetwork.cisco.com/s/encor-exam-topics](https://learningnetwork.cisco.com/s/encor-exam-topics)

---

End of Part 1 — Module 07
