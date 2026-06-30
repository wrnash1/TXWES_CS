# Lab Assignment: Module 05 – QoS & HSRP Configuration
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 22, 2026 at 11:59 PM CST

---

## Lab Overview
**Estimated Time:** 3–4 hours
**Tools Required:** Cisco Packet Tracer (free) + Python environment (for bonus exercise)
**Deliverables:** (1) Completed `.pkt` file, (2) Professional Lab Report (PDF)

This lab implements enterprise QoS using MQC and first-hop redundancy using HSRP on a distribution layer.

---

## Lab Topology

```
        [PC-VoIP]   [PC-Video]   [PC-Data]   [PC-Backup]
             |           |           |             |
           [AS1 — Access Switch]
             |
        [DS1]═══════════[DS2]   ← HSRP Active/Standby
             |               |
           [WAN-RTR] ──── [ISP]
```

**IP Addressing:**
| Device | Interface | IP Address | Role |
|---|---|---|---|
| DS1 | VLAN10 SVI | 10.10.10.1/24 | HSRP Active |
| DS2 | VLAN10 SVI | 10.10.10.2/24 | HSRP Standby |
| HSRP Virtual IP | — | 10.10.10.254/24 | Default Gateway for PCs |
| WAN-RTR | Gi0/0 (to DS1) | 10.10.10.3/24 | WAN edge router |
| WAN-RTR | Gi0/1 (to ISP) | 203.0.113.1/30 | WAN uplink |
| PC-VoIP | — | 10.10.10.10/24, GW: 10.10.10.254 | Simulated voice traffic |
| PC-Video | — | 10.10.10.20/24, GW: 10.10.10.254 | Simulated video traffic |
| PC-Data | — | 10.10.10.30/24, GW: 10.10.10.254 | Simulated critical data |
| PC-Backup | — | 10.10.10.40/24, GW: 10.10.10.254 | Simulated backup traffic |

---

## Lab Instructions

### Part 1: Build the Topology & Configure IP Addressing (10 pts)
1. Place devices in Packet Tracer per the topology.
2. Configure all IP addresses on switch SVIs, router interfaces, and PCs.
3. Enable IP routing on DS1 and DS2.
4. Configure a default route on DS1 and DS2 pointing to WAN-RTR.
5. Verify basic connectivity — ping from PC-VoIP to WAN-RTR's WAN interface.

**Screenshot Checkpoint 1:** `show ip route` on DS1. Ping from PC-VoIP to 203.0.113.1.

### Part 2: Configure HSRP on DS1 and DS2 (25 pts)
Configure HSRP Group 1 for VLAN 10:
- DS1: Active (priority 110), Virtual IP 10.10.10.254, preempt enabled.
- DS2: Standby (default priority 100), same virtual IP, preempt enabled.

**On DS1:**
```
interface Vlan10
 standby version 2
 standby 1 ip 10.10.10.254
 standby 1 priority 110
 standby 1 preempt
 standby 1 timers 1 3
```

**On DS2:**
```
interface Vlan10
 standby version 2
 standby 1 ip 10.10.10.254
 standby 1 priority 100
 standby 1 preempt
 standby 1 timers 1 3
```

**Failover Test:**
1. Confirm DS1 is Active: `show standby brief` on both switches.
2. Simulate DS1 failure: `shutdown` DS1's uplink interface to AS1.
3. Confirm DS2 becomes Active: `show standby` on DS2.
4. Restore DS1: `no shutdown`. Confirm DS1 preempts and becomes Active again.

**Screenshot Checkpoint 2:** `show standby` on DS1 (Active state, priority 110). `show standby` on DS2 after DS1 fails (showing Active state on DS2). `show standby` on DS1 after recovery (Active again via preemption).

### Part 3: Configure QoS Using MQC on WAN-RTR (40 pts)
Apply a DiffServ QoS policy outbound on the WAN-RTR's WAN interface (Gi0/1):

**Step 1: Create Class Maps**
```
class-map match-any VOICE
 match dscp ef

class-map match-any VIDEO
 match dscp af41

class-map match-any CRITICAL-DATA
 match dscp af31

class-map match-any BACKUP-TRAFFIC
 match dscp af11
```

**Step 2: Create Policy Map**
```
policy-map WAN-QOS
 class VOICE
  priority percent 20
 class VIDEO
  bandwidth percent 25
 class CRITICAL-DATA
  bandwidth percent 20
 class BACKUP-TRAFFIC
  bandwidth percent 10
  police rate percent 10 conform-action transmit exceed-action drop
 class class-default
  fair-queue
```

**Step 3: Apply to WAN Interface**
```
interface GigabitEthernet0/1
 service-policy output WAN-QOS
```

**Step 4: Test DSCP Marking**
In Packet Tracer, use the PDU simulation mode to send packets and examine DSCP markings. Manually set DSCP values:
- PC-VoIP: Tag traffic with DSCP EF (can test with extended ping and DSCP option).
- PC-Backup: Tag with DSCP AF11.

**Screenshot Checkpoint 3:** `show policy-map interface GigabitEthernet0/1` on WAN-RTR — show class statistics including bytes matched per class.

### Part 4: Configure DSCP Marking at Access Layer (15 pts)
On AS1, configure port trust to accept DSCP markings from connected PCs (simulating an environment where applications mark their own traffic):
```
mls qos trust dscp

interface range FastEthernet0/1-4
 mls qos trust dscp
```

Add a marking policy for any traffic arriving **unmarked** (DSCP 0) from the backup PC port:
```
class-map match-any UNMARKED
 match dscp default

policy-map MARK-BACKUP
 class UNMARKED
  set dscp af11   ! Re-mark unmarked traffic as low-priority

interface FastEthernet0/4   ! PC-Backup port
 service-policy input MARK-BACKUP
```

**Screenshot Checkpoint 4:** `show policy-map interface FastEthernet0/4` — verify backup traffic is being re-marked.

### Part 5: End-to-End Verification (10 pts)
1. `show standby brief` on DS1 and DS2 — confirm correct Active/Standby state.
2. `show policy-map interface GigabitEthernet0/1` — confirm all 4 classes show matched traffic.
3. Simulate DS1 failure and re-ping from PC-VoIP to ISP — connectivity should continue through DS2.

---

## Lab Report Requirements
1. **Topology Diagram** — annotated screenshot.
2. **All 4 Screenshot Checkpoints** — labeled.
3. **Key Configurations** — full running config of WAN-RTR and DS1.
4. **Analysis Section (2–3 paragraphs):**
   - Why is the VOICE class configured as `priority percent 20` (LLQ) while VIDEO uses `bandwidth percent 25` (CBWFQ)? What is the behavioral difference in how the router treats each class?
   - Explain why reducing HSRP hello/dead timers from the default (3s/10s) to 1s/3s is beneficial for VoIP environments, and what risk it introduces.
   - If `police rate percent 10` on the BACKUP class drops packets when backup traffic exceeds 10%, what impact could this have on the backup application's reliability? How would you mitigate this?
5. **Troubleshooting Log** — one issue and resolution.

---

## Grading Rubric
| Component | Points |
|---|---|
| Topology & IP Addressing (Part 1) | 10 |
| HSRP with Failover Test (Part 2) | 25 |
| QoS MQC Policy (Part 3) | 40 |
| DSCP Marking at Access Layer (Part 4) | 15 |
| End-to-End Verification (Part 5) | 10 |
| **Total** | **100** |
