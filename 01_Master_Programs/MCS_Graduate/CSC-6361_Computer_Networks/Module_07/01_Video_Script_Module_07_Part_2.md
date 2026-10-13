# Video Script: Module 07 – Troubleshooting, Capstone Lab & Final Exam Preparation

## CSC-6361 Advanced Computer Networks | Graduate Level

## Part 2 of 2 | Estimated Duration: 15–18 minutes

## Week 7: November 30 – December 11, 2026 | Due: December 11, 2026

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CSC-6361 Advanced Computer Networks | Module 07 Part 2: Capstone Lab Preview & CCNP ENCOR Exam Strategy | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Welcome to Part 2

[00:00 – 01:30]
[SHOW SLIDE: Professor Nash on camera, multi-topology capstone diagram visible behind.]

Welcome back. In Part 1 we built the troubleshooting methodology: OSI layer-by-layer, divide and conquer, and follow-the-path — and we applied it to OSPF, EIGRP, and BGP failure scenarios. In Part 2 we do two things.

First, I will walk you through the **Module 07 Capstone Lab topology** — a single Packet Tracer network that integrates every major technology from all seven modules. You need to understand the topology before you open the lab file so you can plan your approach. Second, we cover **CCNP ENCOR 350-401 exam strategy** — the exam domains, their weights, timing advice, and how to leverage the troubleshooting methodology from Part 1 on exam day.

Let's start with the capstone.

---

### Section 2: Capstone Lab Preview — Integrating All Seven Modules

[01:30 – 07:00]
[SHOW DIAGRAM: Capstone topology — multi-router network with OSPF multi-area, VLAN/STP, GRE overlay, QoS, ACLs, and BGP routing. Full topology with all device labels and interface connections visible.]

[Alt-text: A network diagram containing: R1-HQ and R2-Core routers in OSPF Area 0 (backbone), connected by a 10.0.0.0/30 link. R3-ABR connects Area 0 to Area 1, which contains R4-Branch. SW1 (core switch) connects to SW2 (access switch) in a two-switch STP topology. R5-Edge connects R1-HQ to an eBGP peer R6-ISP. A GRE tunnel (Tunnel0) runs from R1-HQ to R4-Branch over the OSPF underlay. QoS policy is configured on R1-HQ's WAN-facing interface. An ACL is applied on R3-ABR filtering inter-area traffic.]

The capstone lab topology covers:

- Module 01: Multi-area OSPF with Area 0 (R1, R2), Area 1 (R4), and R3 as the ABR. Route summarization on R3.
- Module 02: Two-switch STP topology (SW1 = root for VLAN 10, SW2 = root for VLAN 20). VLANs 10 and 20 trunked between SW1 and SW2.
- Module 03: eBGP session between R5-Edge and R6-ISP (simulating internet peering). OSPF-to-BGP redistribution on R5.
- Module 03 (GRE overlay): GRE tunnel from R1-HQ to R4-Branch — simulating an SD-WAN analog from Module 06.
- Module 04: DSCP-based QoS policy on R1-HQ's WAN interface — classifying voice (EF) and data (AF31) into separate queues.
- Module 05: Extended ACL on R3-ABR restricting which subnets can transit from Area 1 to Area 0.
- Module 06: GRE tunnel as SD-WAN underlay/overlay analog with BGP overlay routing.

The lab has two phases. In Phase 1, the topology is fully configured and operational — your job is to verify the baseline using a checklist of `show` commands. In Phase 2, five breaks are introduced (one per technology domain). You diagnose and fix each break using the structured troubleshooting methodology from Part 1.

I will walk through the topology device by device so you know what to expect.

#### R1-HQ (Area 0, GRE tunnel source, QoS)

R1 is the hub of the topology. It has four key responsibilities:

1. OSPF Area 0 router — peering with R2-Core (Gi0/0) and R3-ABR (Gi0/1).
2. GRE tunnel source (Tunnel0) — `tunnel source Loopback0`, `tunnel destination` R4-Branch loopback.
3. QoS policy-map applied outbound on Gi0/2 (WAN interface to R5-Edge) — classifying EF traffic into the priority queue.
4. BGP speaker — redistributing OSPF routes into BGP on R5-Edge via OSPF-to-BGP redistribution.

#### R3-ABR (OSPF ABR, ACL enforcement)

R3 sits between Area 0 and Area 1. It:

1. Summarizes Area 1 routes (10.1.0.0/24 through 10.1.3.0/24) into 10.1.0.0/22 when advertising to Area 0.
2. Has an extended ACL applied on its Area 1 interface (`ip access-group AREA1-FILTER in`) restricting specific protocols.
3. In the break scenario: one of the five breaks is a misconfigured ACL on R3 that blocks return ICMP traffic — students must identify this as an ACL issue (not an OSPF issue) using the methodology.

#### SW1 and SW2 (STP, VLANs)

SW1 is the STP root bridge for VLAN 10 (`spanning-tree vlan 10 priority 4096`). SW2 is the STP root for VLAN 20. The trunk between SW1 and SW2 carries both VLANs. One of the five break scenarios is an incorrect STP priority on SW2 that causes SW2 to lose its root election for VLAN 20 — traffic in VLAN 20 takes a suboptimal path.

#### R5-Edge and R6-ISP (eBGP, OSPF redistribution)

R5-Edge has an eBGP session to R6-ISP (AS 65200). R5 also redistributes OSPF routes into BGP. One of the break scenarios involves a missing `redistribute ospf 1 subnets` command — BGP shows the session as Established but no OSPF prefixes are being advertised to the ISP.

---

### Section 3: The Five Break Scenarios — What to Expect

[07:00 – 10:30]
[SHOW SLIDE: Five break scenarios listed — OSPF area, STP priority, route-map, QoS DSCP, ACL return traffic]

In Phase 2 of the capstone lab, the following five specific breaks are injected into the baseline topology. You will not be told which five have been introduced when you open the lab — you must discover them by observing symptoms and verifying with `show` commands.

The five breaks are:

1. OSPF area mismatch on R4-Branch: R4's interface toward R3 is placed in Area 2 instead of Area 1. Symptom: R4 shows no OSPF neighbors. Methodology: `show ip ospf interface` reveals area number; compare to R3's expected Area 1.

2. STP priority misconfiguration: SW2's VLAN 20 priority is set to 32768 (default) instead of 4096, causing SW1 (with default priority) to tie-break and win the election SW2 was supposed to win. Symptom: VLAN 20 traffic traverses a longer STP path. Methodology: `show spanning-tree vlan 20` reveals incorrect root bridge.

3. Missing route-map on redistribution: on R5-Edge, the `redistribute ospf 1 subnets` command is present but the required `route-map` tag preventing routing loops is absent. Symptom: BGP shows prefixes being redistributed, but the same prefixes loop back into OSPF as E2 external routes at unexpected routers. Methodology: `show ip route ospf` on R2-Core reveals unexpected E2 routes; trace to redistribution point.

4. QoS DSCP mismatch: the QoS class-map on R1-HQ is matching DSCP value 46 (EF) for voice traffic, but the ingress marking at SW1 is marking voice traffic as DSCP 40 (CS5) instead of 46. Symptom: voice traffic is falling into the default queue and experiencing queuing delay. Methodology: `show policy-map interface` reveals the EF class has zero matched packets; `show interfaces` shows output drops on the priority queue are zero while default queue drops are high.

5. ACL blocking return traffic: an extended ACL on R3-ABR permits TCP traffic from Area 1 to Area 0 but does not permit the established return traffic (`permit tcp any any established` is missing). Symptom: SSH and HTTP from Area 1 devices to Area 0 devices fail; pings work. Methodology: the asymmetric symptom (ICMP passes, TCP fails) immediately points to an ACL issue; `show ip access-lists` on R3 reveals the missing `established` keyword.

---

### Section 4: CCNP ENCOR 350-401 Exam Overview

[10:30 – 14:30]
[SHOW SLIDE: CCNP ENCOR 350-401 exam domains and weights]

The CCNP Enterprise Core (ENCOR) 350-401 exam is the concentration-independent core exam required for any CCNP Enterprise certification track. Passing it, combined with one concentration exam, earns you the CCNP Enterprise certification.

Exam specifications:

- Exam code: 350-401
- Duration: 120 minutes
- Question count: approximately 90–110 questions
- Passing score: 825 out of 1000 (scaled scoring — Cisco does not publish exact pass/fail question counts)
- Delivery: Pearson VUE testing center or online proctored
- Cost: approximately $400 USD

#### CCNP ENCOR Exam Domains and Weights

| Domain | Topic | Weight |
|---|---|---|
| 1.0 | Architecture | 15% |
| 2.0 | Virtualization | 10% |
| 3.0 | Infrastructure | 30% |
| 4.0 | Network Assurance | 10% |
| 5.0 | Security | 20% |
| 6.0 | Automation | 15% |

Domain 3 — Infrastructure — is the largest domain at 30% and maps directly to this course: OSPF, EIGRP, BGP, spanning tree, QoS, MPLS, and SD-WAN. If you have mastered the seven modules of CSC-6361, you have covered the majority of Domain 3.

Domain 5 — Security — at 20% covers ACLs, 802.1X, IPsec VPN, and infrastructure security — all covered in Module 05.

Domain 6 — Automation — at 15% covers Python basics for network automation, REST APIs, NETCONF/YANG, and Ansible. This topic is not covered in depth in CSC-6361. I recommend dedicating 10–15% of your CCNP exam preparation time specifically to automation — it is a growth area on the exam.

#### Exam Question Types

The CCNP ENCOR uses several question formats:

- Multiple choice (single answer): the most common format.
- Multiple choice (multiple answer): "Select two that apply" — partial credit is not given; you must select exactly the right combination.
- Drag and drop: match items (e.g., match LSA types to their descriptions).
- Testlet: a set of questions based on a shared scenario or topology diagram.
- Simlet: a read-only network simulation — you run `show` commands on a simulated device and answer questions based on the output. You cannot change the configuration.

The simlet questions directly reward the troubleshooting methodology from Part 1. Treat every simlet as: symptom → layer → eliminate → root cause.

---

### Section 5: Final Exam Preparation Strategy

[14:30 – 17:00]
[SHOW SLIDE: 4-week CCNP ENCOR preparation plan]

If you are planning to sit the CCNP ENCOR exam after completing this course, here is a structured preparation approach.

#### Weeks 1–2: Domain Review and Gap Analysis

1. Download the official CCNP ENCOR exam topics from [https://learningnetwork.cisco.com/s/encor-exam-topics](https://learningnetwork.cisco.com/s/encor-exam-topics). Print it or save it as your primary study checklist.
2. For each topic, rate your confidence (1–5). Topics from this course (OSPF, EIGRP, BGP, STP, QoS, SD-WAN fundamentals) should be 4–5. Automation, network assurance, and virtualization may be 2–3.
3. Focus Weeks 1–2 on your weakest domains. Use the Cisco Learning Network free resources and Cisco dCloud sandboxes for hands-on automation practice.

#### Weeks 3–4: Practice Exams and Reinforcement

1. Take at least two full-length practice exams under timed conditions (120 minutes, no breaks). Boson ExSim-Max for CCNP ENCOR is the gold standard for practice exam quality.
2. After each practice exam, review every missed question — not just the ones you flagged. Write a one-sentence explanation of why the correct answer is correct and why your wrong answer was wrong.
3. In the final 3–4 days before the exam: review the `show` command reference, review the exam domain weights, and do a final run through the CCNP ENCOR exam topics checklist. Stop introducing new material — consolidate what you know.

#### Day of Exam

- Arrive or log in 15 minutes early.
- On paper (provided at the testing center) write down the BGP state machine, OSPF neighbor state machine, EIGRP K-values, and DSCP/PHB values from memory during the initial orientation period — before the exam clock starts. This gives you a reference sheet for troubleshooting questions.
- For each question: read the question stem, identify the technology domain, eliminate clearly wrong answers, then select. Do not overthink. Your first instinct on a protocol behavior question is usually right.
- Flag and skip difficult questions. Come back with fresh eyes. 120 minutes for 100 questions is 72 seconds per question — you have time to return to flagged items.

---

### Section 6: Course Closing

[17:00 – 18:30]
[SHOW SLIDE: Professor Nash on camera, course summary slide]

This brings us to the end of CSC-6361 Advanced Computer Networks. Over seven modules you have worked through multi-area OSPF and EIGRP, switched network design with STP and VLANs, BGP and MPLS, QoS, network security, SD-WAN with VXLAN and EVPN, cloud connectivity with Direct Connect and ExpressRoute, and structured troubleshooting methodology. That is the CCNP ENCOR blueprint — and you have covered it at graduate depth.

The capstone lab is your final opportunity to demonstrate that you can work through a complex, integrated network problem the way a senior engineer would in production: methodically, evidence-based, and without guessing.

Good luck on the capstone, on the final discussion, and on your CCNP pursuit. It has been a privilege to work through this material with you. I am proud of the depth you have reached this semester.

All Module 07 assignments are due Friday, December 11, 2026 at 11:59 PM CST.

---

### Additional Resources

- CCNP ENCOR 350-401 Official Exam Topics: [https://learningnetwork.cisco.com/s/encor-exam-topics](https://learningnetwork.cisco.com/s/encor-exam-topics)
- Cisco Learning Network — CCNP ENCOR Study Hub: [https://learningnetwork.cisco.com/s/encor-study-materials](https://learningnetwork.cisco.com/s/encor-study-materials)
- Boson ExSim-Max for CCNP ENCOR: [https://www.boson.com/practice-exam/350-401-cisco-ccnp-encor-practice-exam](https://www.boson.com/practice-exam/350-401-cisco-ccnp-encor-practice-exam)
- Packetlife.net Cheat Sheets: [https://packetlife.net/library/cheat-sheets/](https://packetlife.net/library/cheat-sheets/)
- GNS3 Network Simulator: [https://gns3.com/software/download](https://gns3.com/software/download)

---

End of Part 2 — Module 07
