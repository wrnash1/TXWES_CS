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

---

> **Instructor Note — Questions 11–20:** These 10 questions are worth **5 pts each** (50 pts total). Enter as a separate quiz section or append to the existing quiz. Same format rules apply.

---

### Question 11 (Multiple Choice — 5 pts)
An OSPF router's `show ip ospf database` output shows a Type 4 LSA with Advertising Router 3.3.3.3. What does this LSA communicate to routers in the area?

- A) The metric to reach Router 3.3.3.3 as an internal OSPF router.
- B) The metric to reach an ASBR (identified by its router-ID) that is located in another area, as advertised by ABR 3.3.3.3. ✅
- C) A summary of all external routes redistributed into OSPF.
- D) The topology of all links within Area 3.

**Answer:** B — A Type 4 LSA (ASBR Summary LSA) is generated by an ABR to tell routers in other areas how to reach the ASBR that is redistributing external routes. Without it, routers in remote areas would know external routes exist (via Type 5 LSAs) but would not know how to reach the ASBR that originated them.

**Distractor Analysis:**
- A: Metric to an internal router is communicated via Type 1/2 LSAs (Router/Network LSAs).
- C: External routes themselves are in Type 5 LSAs. Type 4 only describes how to reach the originating ASBR.
- D: Intra-area topology is described by Type 1 and Type 2 LSAs.

---

### Question 12 (Multiple Choice — 5 pts)
A network engineer is configuring OSPF on a point-to-point serial link between R1 and R2. The neighbor relationship fails to form. `show ip ospf interface Serial0/0` on R1 shows network type `BROADCAST`, while R2 shows `POINT-TO-POINT`. What is the correct fix?

- A) Serial links must use OSPFv3; OSPFv2 does not support point-to-point serial interfaces. ❌
- B) Configure `ip ospf network point-to-point` on R1's Serial0/0 interface to match R2, eliminating the network-type mismatch. ✅
- C) The DR election must complete on the BROADCAST side before the adjacency can form. ❌
- D) Serial interfaces require manual `neighbor` statements when network types differ. ❌

**Answer:** B — OSPF hello and dead timers, as well as DR/BDR election behavior, differ between BROADCAST and POINT-TO-POINT network types. Mismatched network types prevent adjacency formation. Setting both ends to `point-to-point` is correct for serial links and eliminates the unnecessary DR/BDR election.

**Distractor Analysis:**
- A: OSPFv2 fully supports serial interfaces in both network type modes.
- C: DR/BDR elections should not occur on point-to-point links — they are a multi-access concept.
- D: Manual neighbor statements are only required in NBMA environments.

---

### Question 13 (Multiple Choice — 5 pts)
Two EIGRP routers are not forming a neighbor relationship. `show ip eigrp neighbors` shows no entries on either router. Both are configured in AS 100, are directly connected on 10.1.1.0/24, and interfaces are up/up. What are TWO likely causes? (Select two)

- A) One router has `passive-interface` configured on the connecting interface. ✅
- B) K-values (metric weights) are mismatched between the two routers. ✅
- C) EIGRP requires a loopback interface to be configured before forming neighbors. ❌
- D) Both routers have the same router-ID, causing a conflict that prevents adjacency. ❌
- E) The `network` statement covers the interface IP but uses the wrong wildcard mask syntax. ❌

**Answer:** A and B — A passive interface suppresses EIGRP hello packets, preventing neighbor formation even though the interface is up. Mismatched K-values cause EIGRP to reject the hello packet — K-values are carried in the hello, and if they don't match, the neighbor relationship is refused with a "K-value mismatch" log message. Both are among the most common EIGRP troubleshooting scenarios in production.

**Distractor Analysis:**
- C: Loopback interfaces are not required for EIGRP neighbor formation.
- D: Duplicate router-IDs cause issues with route advertisements but do not prevent adjacency formation in EIGRP (unlike OSPF).
- E: If the network statement covers the interface IP with any valid wildcard mask, the interface participates in EIGRP.

---

### Question 14 (Scenario — 5 pts)
A router running EIGRP shows this topology table entry:
```
P 10.5.0.0/24, 1 successors, FD is 2816
        via 10.1.1.1 (2816/1024), GigabitEthernet0/0
        via 10.2.2.2 (3328/2048), GigabitEthernet0/1
```
Is the path via 10.2.2.2 a Feasible Successor? Which value must be compared to determine this?

- A) No — its total metric (3328) is greater than the FD (2816), so it cannot be a Feasible Successor. ❌
- B) Yes — its Reported Distance (2048) is less than the current Feasible Distance (2816), so the Feasibility Condition IS met. ✅
- C) No — EIGRP can only have one Feasible Successor per destination prefix. ❌
- D) Yes — any path in the topology table automatically qualifies as a Feasible Successor. ❌

**Answer:** B — The Feasibility Condition checks whether RD < FD. Here RD = 2048 and FD = 2816. Since 2048 < 2816, the Feasibility Condition is met and the path via 10.2.2.2 IS a Feasible Successor. Note: the total metric being higher (3328 > 2816) does not disqualify it — only the RD-vs-FD comparison matters.

**Distractor Analysis:**
- A: The total metric comparison is irrelevant to the Feasibility Condition — only RD is compared to FD.
- C: EIGRP can have multiple Feasible Successors per destination.
- D: Only paths meeting the Feasibility Condition (RD < FD) qualify as Feasible Successors.

---

### Question 15 (Multiple Choice — 5 pts)
What is the purpose of OSPF's SPF throttling configured with `timers throttle spf [start] [hold] [max-wait]`?

- A) To limit the rate at which a router can originate new LSAs into the OSPF domain. ❌
- B) To introduce an exponential backoff delay between SPF calculations during rapid topology changes, preventing the router CPU from being overwhelmed by repeated full SPF runs. ✅
- C) To prevent multiple ABRs from simultaneously running SPF calculations in overlapping areas. ❌
- D) To control the frequency of OSPF hello packets during periods of network instability. ❌

**Answer:** B — Without SPF throttling, a flapping link can trigger dozens of full SPF calculations per second, consuming all CPU. The throttle timer introduces an initial delay (`start`), then doubles the hold time after each successive topology change (up to `max-wait`), allowing the network to stabilize before the next SPF run. This is critical in large OSPF domains where full SPF is computationally expensive.

---

### Question 16 (Multiple Choice — 5 pts)
An EIGRP Named Mode topology contains:
```
router eigrp ENTERPRISE
 address-family ipv4 unicast autonomous-system 100
  topology base
   variance 2
   maximum-paths 4
```
A destination has a Successor with FD = 3000 and three Feasible Successors with metrics 4500, 5500, and 6500. Which paths will EIGRP install in the routing table?

- A) Only the Successor (metric 3000) — variance applies only to unequal-cost load balancing in Classic Mode. ❌
- B) The Successor (3000) and the FS with metric 4500 — because 4500 ≤ 2 × 3000 = 6000. Traffic is distributed proportionally. ❌ (incomplete)
- C) The Successor (3000), the FS with metric 4500, and the FS with metric 5500 — all three have metrics ≤ 6000 (2 × FD). The FS with 6500 exceeds the variance threshold. ✅
- D) All four paths including the FS with metric 6500 — variance 2 allows any path up to twice the FD. ❌

**Answer:** C — `variance 2` installs any Feasible Successor with total metric ≤ 2 × FD = 6000. Metrics 4500 and 5500 qualify; 6500 exceeds 6000. `maximum-paths 4` sets the upper limit on installed paths but does not override the variance threshold. Traffic is distributed inversely proportional to metric.

---

### Question 17 (Scenario — 5 pts)
An ABR connects Area 0 and Area 1. Area 1 contains subnets 172.16.100.0/24 through 172.16.103.0/24. The engineer wants to prevent these specific subnets from being advertised into Area 0 as Type 3 LSAs while allowing all other Area 1 routes to reach Area 0. Which command accomplishes this on the ABR?

- A) `area 1 range 172.16.100.0 255.255.252.0 not-advertise` configured on the ABR ✅
- B) `area 0 filter-list prefix BLOCK-172-16-100 in` configured on the ABR ❌
- C) `distribute-list prefix BLOCK-172-16-100 out` configured under `router ospf 1` on the ABR ❌
- D) `area 1 stub no-summary` configured on the ABR and all Area 1 routers ❌

**Answer:** A — The `area [area-id] range [network] [mask] not-advertise` command on an ABR suppresses a specific address range from being advertised as a Type 3 Summary LSA into other areas. It is the precise tool for selective inter-area route filtering at the ABR.

**Distractor Analysis:**
- B: `filter-list` with `in` filters routes being imported into the ABR's topology — it affects what the ABR learns, not what it advertises outward.
- C: `distribute-list` with `out` affects the routing table, not inter-area LSA advertisement.
- D: `no-summary` makes Area 1 Totally Stubby — it blocks ALL Type 3 LSAs, not just a specific range.

---

### Question 18 (Multiple Choice — 5 pts)
After configuring mutual redistribution between OSPF and EIGRP with route-tag loop prevention, a network engineer notices that certain routes show as `O E2` (OSPF External Type 2) in the routing table on OSPF routers, replacing what were formerly `O` (OSPF internal) routes for those same prefixes. The tag-based filters are correctly configured. What is the most likely explanation?

- A) EIGRP's AD (90) is lower than OSPF internal (110), so EIGRP routes are winning over OSPF routes. ❌
- B) The tag filters are correctly blocking redistribution loops, but the OSPF external routes are arriving via a different redistribution point that bypasses the tag filter. ❌
- C) OSPF external routes (O E2) and OSPF internal routes (O) share the same AD (110), and E2 routes use a fixed external metric. If the E2 metric is lower than the intra-area cost, the router prefers the E2 path — the tag filter prevents loops but does not prevent metric-based route preference issues. ✅
- D) The `subnets` keyword was omitted from the redistribution command, causing classful summarization of OSPF routes. ❌

**Answer:** C — Both O and O E2 routes have AD=110. OSPF uses route type as a tie-breaker: intra-area (O) > inter-area (O IA) > external type 1 (O E1) > external type 2 (O E2). However, if the E2 metric is very low (e.g., the seed metric set during redistribution is 1), routers may install the external route via another redistribution path. The solution is setting higher external metrics or using distribute-lists to explicitly block external routes for prefixes that are internal.

---

### Question 19 (Short Answer — 5 pts)
What is an OSPF **virtual link**, when is it required, and what is the significant operational risk of relying on virtual links in a production network? (2–3 sentences)

**Model Answer:** An OSPF virtual link is a logical extension of Area 0 through a non-backbone transit area, used when a non-backbone area cannot be physically connected directly to Area 0 — a situation that violates OSPF's design requirement that all areas connect to the backbone. It is required in legacy or acquired-network scenarios where an isolated area's only physical path to Area 0 must pass through another non-backbone transit area. The significant operational risk is that virtual links depend on the stability and full connectivity of the transit area — any partition, LSA flooding failure, or convergence problem in the transit area disrupts the virtual link and cuts off the isolated area's entire OSPF connectivity, which is why Cisco design guides strongly recommend resolving the physical topology rather than relying on virtual links as a permanent solution.

---

### Question 20 (Short Answer — 5 pts)
Describe how EIGRP's **Stuck-in-Active (SIA)** condition occurs, what the `timers active-time` command controls, and what consequence occurs when SIA is declared against a neighbor. (2–3 sentences)

**Model Answer:** SIA occurs when an EIGRP router sends Query packets to all neighbors while in the Active state (searching for a new Successor after losing its current best path) but fails to receive a Reply from one or more neighbors within the active timer period — the default is 3 minutes, configurable with `timers active-time [minutes]` in the topology base stanza. Reducing the active timer allows faster detection of unresponsive neighbors but risks declaring SIA prematurely on legitimate slow-to-converge paths in large EIGRP domains. When SIA is declared, the router tears down the EIGRP neighbor relationship with the non-responding neighbor entirely, logs a "Neighbor X stuck in active state" error, and the neighbor must rebuild its adjacency from scratch — potentially causing cascading Query/Reply cycles and additional route instability across the network.
