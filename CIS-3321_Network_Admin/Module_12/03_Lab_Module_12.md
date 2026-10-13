# Lab: Module 12 — Wide Area Networks

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Lab Overview

This lab uses Cisco Packet Tracer (free from the Cisco Networking Academy) to simulate WAN topologies. You will build a multi-site WAN, configure serial leased line links, simulate MPLS routing behavior, and analyze WAN failover using dual-path SD-WAN-style routing. You will also use a web-based tool to compare WAN latency across satellite types.

**Estimated Time:** 90–120 minutes

**Required Tools:**

- Cisco Packet Tracer 8.x (free at netacad.com — create a free account)
- Web browser (for latency simulation exercise)
- Calculator or spreadsheet (for bandwidth calculations)

---

## Safety and Submission Notice

Save your Packet Tracer file (.pkt) frequently. Export screenshots at each checkpoint. Submit the .pkt file and a lab report PDF. All work must be your own.

---

## Part 1: WAN Topology Build — Multi-Site Leased Line Network

### Part 1 Objective

Build a three-site WAN using serial leased line connections in Packet Tracer. Configure IP addressing and verify end-to-end connectivity.

### Step 1: Create the Topology

Open Packet Tracer. Using the logical workspace, place the following devices:

- Three 2911 routers: name them HQ, Branch1, Branch2
- Three switches (2960): one behind each router for LAN connectivity
- Three PCs: one connected to each switch

Connect devices as follows:

- HQ Router Serial0/0/0 → Branch1 Router Serial0/0/0 (use a Serial DCE cable from HQ to Branch1)
- HQ Router Serial0/0/1 → Branch2 Router Serial0/0/0 (use a Serial DCE cable from HQ to Branch2)
- Each router FastEthernet0/0 → its local switch → PC

### Step 2: Configure IP Addressing

Use this addressing scheme:

WAN links:

- HQ–Branch1: `10.1.1.0/30` (HQ = .1, Branch1 = .2)
- HQ–Branch2: `10.1.2.0/30` (HQ = .1, Branch2 = .2)

LAN subnets:

- HQ LAN: `192.168.1.0/24` (router = .1, PC = .10)
- Branch1 LAN: `192.168.2.0/24` (router = .1, PC = .10)
- Branch2 LAN: `192.168.3.0/24` (router = .1, PC = .10)

On each router, configure interfaces. Example for HQ:

```bash
interface Serial0/0/0
 ip address 10.1.1.1 255.255.255.252
 clock rate 64000
 no shutdown

interface Serial0/0/1
 ip address 10.1.2.1 255.255.255.252
 clock rate 64000
 no shutdown

interface FastEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
```

### Step 3: Configure Static Routing

On HQ, add static routes to reach each branch LAN:

```bash
ip route 192.168.2.0 255.255.255.0 10.1.1.2
ip route 192.168.3.0 255.255.255.0 10.1.2.2
```

On Branch1, add static routes:

```bash
ip route 192.168.1.0 255.255.255.0 10.1.1.1
ip route 192.168.3.0 255.255.255.0 10.1.1.1
```

On Branch2, add static routes:

```bash
ip route 192.168.1.0 255.255.255.0 10.1.2.1
ip route 192.168.2.0 255.255.255.0 10.1.2.1
```

Configure default gateways on each PC to match its router LAN interface.

### Step 4: Verify Connectivity

From Branch1 PC (192.168.2.10), ping:

- Branch1 router LAN: `192.168.2.1`
- HQ router WAN: `10.1.1.1`
- HQ PC: `192.168.1.10`
- Branch2 PC: `192.168.3.10`

All pings should succeed.

### Checkpoint 1

Screenshot the topology showing all green link indicators. Screenshot the successful ping output from Branch1 PC to Branch2 PC.

---

## Part 2: Simulating WAN Redundancy

### Part 2 Objective

Add a backup WAN link between Branch1 and Branch2 to simulate dual-path redundancy, similar to an SD-WAN multi-transport design.

### Step 5: Add a Direct Branch-to-Branch Link

Add a serial link between Branch1 Serial0/0/1 and Branch2 Serial0/0/1:

- Link subnet: `10.1.3.0/30` (Branch1 = .1, Branch2 = .2)

Configure both interfaces with the appropriate IP addresses.

### Step 6: Update Routing for Redundancy

On Branch1, add a floating static route to Branch2 LAN via the direct link (higher administrative distance = lower preference — backup route):

```bash
ip route 192.168.3.0 255.255.255.0 10.1.3.2 5
```

The number `5` is the administrative distance — lower than the default static route AD of 1 is NOT what we want here. Use `200` to make it a floating (backup) route:

```bash
no ip route 192.168.3.0 255.255.255.0 10.1.3.2 5
ip route 192.168.3.0 255.255.255.0 10.1.3.2 200
```

Do the same on Branch2 for the reverse path to Branch1 LAN.

### Step 7: Test Failover

With the primary paths (via HQ) active, verify Branch1 can reach Branch2.

Now simulate an HQ WAN failure: right-click the HQ-Branch1 serial cable and select "Shutdown" on HQ Serial0/0/0. Wait 30 seconds for route convergence, then re-ping from Branch1 to Branch2.

The ping should still succeed — now routed via the direct Branch1–Branch2 link.

### Checkpoint 2

Screenshot the routing table on Branch1 (`show ip route`) before and after the simulated failure. Screenshot successful ping from Branch1 to Branch2 after the failure.

---

## Part 3: Bandwidth and Latency Calculations

### Part 3 Objective

Calculate WAN bandwidth requirements and analyze the impact of latency on application performance.

### Step 8: Bandwidth Requirement Calculations

A company has three branch offices connecting to HQ via WAN. Calculate the minimum WAN bandwidth needed for each scenario:

Scenario A — Branch1:

- 25 concurrent VoIP calls (G.711 codec: 87.2 Kbps per call including overhead)
- 15 users transferring files simultaneously (average 500 Kbps each)
- 10 users browsing web applications (average 200 Kbps each)
- Add 20% overhead for protocol and management traffic

Show your calculation and state the minimum link speed required. What T-carrier service (T1 or fractional T3) would you provision?

Scenario B — Branch2:

- 10 concurrent video conference sessions (HD video: 3 Mbps per session)
- 20 users accessing SaaS applications (average 1 Mbps each)
- Add 25% overhead

Show your calculation. Would a single T1 suffice? What alternative WAN technology would you recommend?

### Step 9: Latency Impact Analysis

Answer the following questions in your lab report:

A company is evaluating two WAN options for its remote Alaska office:

- Option 1: GEO satellite — 50 Mbps, 650 ms one-way latency
- Option 2: LEO satellite (Starlink) — 150 Mbps, 25 ms one-way latency, $500/month more expensive

The office has these requirements:

- 50 VoIP calls daily (acceptable VoIP one-way latency: under 150 ms per ITU G.114)
- Video conferencing 4 hours/day
- File transfers and email (latency-insensitive)

Which option meets the VoIP latency requirement? Show your math (round-trip time = 2 × one-way latency). Is the additional cost of Option 2 justified? Explain your reasoning with reference to specific applications.

### Checkpoint 3

Show all calculations in your lab report. Clearly state your T-carrier recommendation for Scenario A and your WAN recommendation for the Alaska office.

---

## Part 4: SD-WAN Concepts — Policy Mapping Exercise

### Part 4 Objective

Apply SD-WAN application-aware routing concepts by mapping application traffic to appropriate WAN transports.

### Step 10: SD-WAN Policy Design

A company has three WAN transports at each branch:

- Transport A: MPLS — 10 Mbps, 8 ms latency, $2,000/month, SLA-guaranteed
- Transport B: Broadband fiber — 500 Mbps, 15 ms latency, $300/month, best-effort
- Transport C: 4G LTE — 50 Mbps, 35 ms latency, $150/month, usage-capped at 100 GB/month

For each application below, identify which transport(s) should carry it and explain your policy reasoning:

1. Microsoft Teams voice calls (VoIP)
2. Microsoft 365 email and calendar sync
3. Nightly backup to cloud storage (2 TB)
4. Salesforce CRM (interactive web app)
5. Emergency failover when Transport A and B are both down

Record your policy table in the lab report: Application | Primary Transport | Secondary Transport | Reasoning.

### Checkpoint 4

Complete the policy mapping table and submit with the lab report. For each choice, reference at least one SD-WAN concept from the Module 12 lecture (e.g., application-aware routing, dynamic path selection, zero-touch provisioning).

---

## Lab Report Requirements

Submit a PDF lab report containing:

1. Checkpoint 1: Topology screenshot and ping output.
2. Checkpoint 2: Routing table screenshots (before and after failure) and failover ping output.
3. Checkpoint 3: Full bandwidth calculations for both scenarios with final recommendations.
4. Checkpoint 4: Completed SD-WAN policy mapping table with reasoning.
5. Reflection (150–200 words): How does simulated WAN redundancy in Packet Tracer reflect real-world SD-WAN dynamic failover? What limitations does static routing have compared to SD-WAN dynamic path selection?
6. Packet Tracer file (.pkt) attached to submission.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Topology build and connectivity screenshots | 20 |
| Part 2 — Redundancy config and failover screenshots | 20 |
| Part 3 — Bandwidth calculations (both scenarios) | 20 |
| Part 3 — Latency analysis with correct math | 15 |
| Part 4 — SD-WAN policy mapping table | 15 |
| Reflection paragraph | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

These advanced steps extend the Module 12 lab with MPLS label analysis, QoS policy design, and SD-WAN policy expansion.

### Challenge Step 1: Calculate T-Carrier Bandwidth Requirements for a Real Scenario

A company needs to support the following simultaneous WAN traffic between its headquarters and a branch office:

- 50 concurrent VoIP calls using G.711 codec (64 Kbps per call, plus 20% overhead)
- 10 video conferencing sessions at 1 Mbps each (with 10% overhead)
- Background file replication: 20 Mbps average sustained
- Headroom requirement: 30% above peak usage

Show all work:

1. Calculate total VoIP bandwidth with overhead.
2. Calculate total video conferencing bandwidth with overhead.
3. Sum all traffic and add 30% headroom.
4. Determine the minimum T-carrier circuit (T1, T2, or T3) that meets this requirement.
5. Calculate how many T1 channels (DS0s) the selected circuit uses.

**Challenge Question 1:** What T-carrier circuit did you select? What is its total bandwidth? What percentage of the circuit's total capacity will be consumed by the calculated peak traffic? Is there sufficient headroom for traffic spikes beyond the stated 30% requirement?

### Challenge Step 2: Design a Complete SD-WAN Policy for a 5-Application Enterprise

A healthcare enterprise has the following WAN transports at each clinic:
- Transport A: MPLS — 50 Mbps, 8 ms, $1,500/month
- Transport B: Fiber broadband — 1 Gbps, 12 ms, $400/month
- Transport C: 5G cellular — 200 Mbps, 25 ms, $200/month (5 GB/day cap)

Design complete routing policies for these five applications. For each, specify: primary transport, secondary transport, failover transport, and the metric (latency/bandwidth/cost) that drives each choice.

1. Epic EHR (Electronic Health Records) — interactive clinical application, extremely latency-sensitive, HIPAA-regulated
2. HD video telemedicine sessions — 4 Mbps per session, maximum 15 ms latency
3. Nightly PACS backup (medical imaging archives) — 500 GB nightly, 12-hour window
4. Staff email and Teams chat — bursty, latency-tolerant
5. IoT medical device telemetry — small packets, continuous, must never drop

**Challenge Question 2:** For application 1 (Epic EHR), explain why MPLS is the appropriate primary transport despite being the most expensive option. What specific SD-WAN monitoring metric would trigger automatic failover from MPLS to the fiber broadband backup, and what threshold value (ms latency or % packet loss) would you set in a production healthcare environment?

### Challenge Step 3: Build a Multi-Site Redundant WAN in Packet Tracer with Floating Static Routes

1. Extend your existing topology to three sites: HQ, Branch-A, and Branch-B.
2. Connect HQ to Branch-A via two serial links (primary Gi0/1, backup Gi0/2).
3. Connect HQ to Branch-B via one serial link.
4. Configure floating static routes on HQ:
   - Primary route to Branch-A: administrative distance 1 (default)
   - Backup route to Branch-A via Branch-B: administrative distance 10
5. Verify that the primary path is active with `show ip route`.
6. Shut down the primary link to Branch-A. Verify the backup route becomes active within 30 seconds.

**Challenge Question 3:** Explain the concept of administrative distance in Cisco IOS routing. Why does setting the backup static route to AD 10 instead of AD 1 prevent it from being used unless the primary fails? Compare this static-route failover mechanism to SD-WAN dynamic path selection — list two specific capabilities SD-WAN provides for failover that static routing with floating routes cannot provide.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
