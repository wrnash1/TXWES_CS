# Quiz: Module 01 – Advanced IP Routing: Multi-Area OSPF & EIGRP
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: Sunday, October 25, 2026 at 11:59 PM CST

---

> **Instructor Note:** Enter these questions into Canvas as a timed Quiz (30 minutes, 1 attempt, no backtracking). Set questions to randomize order. All questions are CCNP Enterprise–style scenario questions.

---

### Question 1 (Multiple Choice — 10 pts)
A network engineer is designing a multi-area OSPF network with three areas: Area 0, Area 1, and Area 2. Area 1 has no ASBR and has a single connection to Area 0 through one ABR. The engineer wants to minimize the routing table size in Area 1 while still allowing connectivity to external routes as a default. Which area type should Area 1 be configured as?

- A) NSSA
- B) Stub
- C) Totally Stubby ✅
- D) Normal (no stub)

**Answer:** C — Totally Stubby. A Totally Stubby area blocks Type 3, 4, and 5 LSAs and replaces them with a single default route from the ABR. This produces the smallest possible routing table for an area with a single ABR and no ASBR.

**Distractor Analysis:**
- A (NSSA): NSSA is used when the area *has* its own ASBR that needs to redistribute external routes — incorrect here.
- B (Stub): Stub blocks Type 5 LSAs but still allows Type 3 Summary LSAs, producing a larger routing table than Totally Stubby.
- D (Normal): Normal area receives all LSA types — largest routing table of all options.

---

### Question 2 (Multiple Choice — 10 pts)
An OSPF ABR is configured with the command `area 10 range 172.16.0.0 255.255.240.0`. Routers in Area 10 have the following subnets: 172.16.0.0/24, 172.16.3.0/24, 172.16.7.0/24, 172.16.14.0/24, and 172.16.20.0/24. Which subnet will NOT be covered by this summary route?

- A) 172.16.0.0/24
- B) 172.16.7.0/24
- C) 172.16.14.0/24
- D) 172.16.20.0/24 ✅

**Answer:** D — 172.16.20.0/24. The summary `172.16.0.0/20` covers addresses from 172.16.0.0 to 172.16.15.255. The subnet 172.16.20.0/24 starts at 172.16.20.0, which is outside this range. It would be advertised as a separate specific Type 3 LSA.

---

### Question 3 (Multiple Choice — 10 pts)
In an EIGRP topology, Router R1 has the following data for destination network 192.168.50.0/24:
- Via R2: RD = 2000, total metric = 3000
- Via R3: RD = 2500, total metric = 3500
- Via R4: RD = 2800, total metric = 4000

The current Feasible Distance (FD) via the Successor (R2) is 3000. Which of the following statements is TRUE?

- A) R3 is a Feasible Successor because its total metric (3500) is greater than the FD (3000). ❌
- B) R3 is a Feasible Successor because its RD (2500) is less than the FD (3000). ✅
- C) R4 is a Feasible Successor because its RD (2800) is less than the FD (3000). ✅
- D) Neither R3 nor R4 qualifies as a Feasible Successor.

**Answer:** B and C — Both R3 (RD=2500 < FD=3000) and R4 (RD=2800 < FD=3000) meet the Feasibility Condition. Note: if the quiz requires selecting one best answer, select B and C if multi-select is allowed; otherwise the question should be formatted as select-all-that-apply.

**Instructor Note:** Configure as "select all that apply" for this question.

---

### Question 4 (Multiple Choice — 10 pts)
A network engineer configures mutual redistribution between OSPF and EIGRP without using route maps or tags. Which of the following problems is MOST likely to occur?

- A) EIGRP will fail to form neighbor relationships with OSPF routers.
- B) Routes redistributed from OSPF into EIGRP may be redistributed back into OSPF, creating a routing loop. ✅
- C) OSPF will reject all redistributed EIGRP routes due to metric incompatibility.
- D) EIGRP will automatically prevent loops using the Feasibility Condition.

**Answer:** B — Without route maps/tags, mutual redistribution creates feedback loops: OSPF routes are redistributed into EIGRP, then EIGRP redistributes those same routes back into OSPF as external routes, potentially replacing the original OSPF routes with suboptimal external paths.

---

### Question 5 (Multiple Choice — 10 pts)
An OSPF router is in EIGRP Named Mode. A junior engineer shows you this configuration and asks if it is correct. What is wrong?

```
router eigrp CORP
 address-family ipv4 unicast autonomous-system 100
  network 10.0.0.0 0.0.255.255
  passive-interface GigabitEthernet0/2
```

- A) The AS number should be in the `router eigrp` line, not inside the address-family.
- B) The `passive-interface` command is invalid inside an address-family; it must be in an `af-interface` block. ✅
- C) Named mode does not support IPv4 unicast; use `address-family ipv4 multicast`.
- D) The configuration is correct as written.

**Answer:** B — In EIGRP Named Mode, per-interface settings like `passive-interface` must be configured inside an `af-interface` block:
```
af-interface GigabitEthernet0/2
 passive-interface
exit-af-interface
```

---

### Question 6 (Scenario — 10 pts)
A router shows this OSPF database entry:
```
        Type-3 LSA
        LS age: 742
        Options: (No TOS-capability, DC, Upward)
        LS Type: Summary Links (Network)
        Link State ID: 10.5.0.0
        Advertising Router: 2.2.2.2
        Metric: 20
```
What can you conclude from this output?

- A) Router 2.2.2.2 is an ASBR advertising an external route.
- B) Router 2.2.2.2 is an ABR advertising a summary route from another area. ✅
- C) This is a router LSA generated within the local area.
- D) The metric of 20 indicates this is an external Type-2 metric.

**Answer:** B — "Summary Links" is the Cisco IOS name for a Type 3 LSA, which is generated by an ABR to summarize routes from one area into another. Router 2.2.2.2 is the ABR.

---

### Question 7 (Multiple Choice — 10 pts)
Which two EIGRP Named Mode commands correctly configure a router to set the hello timer to 10 seconds and the hold time to 30 seconds on interface GigabitEthernet0/1? (Select two)

- A) `ip hello-interval eigrp 100 10` (interface config mode)
- B) `af-interface GigabitEthernet0/1` → `hello-interval 10` ✅
- C) `af-interface GigabitEthernet0/1` → `hold-time 30` ✅
- D) `timers active-time 30` (inside topology base)
- E) `ip hold-time eigrp 100 30` (interface config mode)

**Answer:** B and C — In EIGRP Named Mode, interface-level timer configuration is done inside the `af-interface` block within the `address-family` stanza.

---

### Question 8 (Scenario — 10 pts)
Router R4 is the redistribution router between OSPF and EIGRP. After configuring redistribution, a network engineer notices that some OSPF routes in the EIGRP domain are appearing with a metric of 4294967295. What is the most likely cause?

- A) EIGRP has reached its maximum route count and is discarding new routes.
- B) The EIGRP metric seed values were not provided in the `redistribute` command. ✅
- C) OSPF is blocking those routes with a distribute list.
- D) The routes are OSPF Type 7 LSAs, which EIGRP cannot import.

**Answer:** B — When redistributing into EIGRP, you MUST provide a seed metric using the `metric` keyword (bandwidth, delay, reliability, load, MTU). Without a seed metric, EIGRP assigns an infinite metric (4294967295), making the routes unreachable.
```
redistribute ospf 1 metric 10000 100 255 1 1500
```

---

### Question 9 (Short Answer — 10 pts)
Explain the difference between an OSPF **Stub** area and a **Not-So-Stubby Area (NSSA)**. In what specific scenario would you choose NSSA over Stub? (2–3 sentences required for full credit)

**Model Answer:** A Stub area blocks Type 5 External LSAs and replaces them with a default route from the ABR. An NSSA also blocks Type 5 LSAs from the backbone, but allows an ASBR within the NSSA to redistribute external routes as Type 7 LSAs, which the ABR then translates to Type 5 LSAs for the rest of the OSPF domain. You would choose NSSA when a remote area needs to connect to an external routing domain (e.g., it has a direct internet connection or connects to a legacy RIP network) while still minimizing the Type 5 LSA flood from the backbone.

---

### Question 10 (Short Answer — 10 pts)
A router's EIGRP topology table shows a route in **Active** state for 3 minutes. What does this mean, and what action might the router take if the Active state continues beyond the active-timer threshold?

**Model Answer:** An **Active** state means the router has lost its Successor for a route, has no Feasible Successor available, and has sent Query packets to all EIGRP neighbors asking for an alternate path. The router is waiting for Reply packets from all queried neighbors. If a neighbor does not reply within the active-timer threshold (default: 3 minutes), the router declares that neighbor **Stuck-in-Active (SIA)** and tears down the EIGRP neighbor relationship with that router, logging an SIA error message.
