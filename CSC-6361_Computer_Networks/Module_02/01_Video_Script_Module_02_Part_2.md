# Video Script: Module 02 – Campus Network Design: VLANs, STP & EtherChannel
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 2 of 2 | Estimated Duration: 15–18 minutes
## Week 2: October 26 – November 1, 2026 | Due: Sunday, November 1, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 02 Part 2: EtherChannel, MST & Campus Troubleshooting | Texas Wesleyan University"]

---

### Section 1: EtherChannel — Link Aggregation at CCNP Depth

[00:00 – 05:30]
[SHOW DIAGRAM: Two distribution switches connected by 4 individual 1G links bundled into one 4G EtherChannel (Port-Channel 1)]

[Alt-text: Diagram showing Distribution Switch 1 connected to Distribution Switch 2 via four parallel lines labeled "Gi0/0, Gi0/1, Gi0/2, Gi0/3" that converge into a single thick line labeled "Port-Channel 1 (4 Gbps logical link)."]

EtherChannel bundles multiple physical links into a single logical link. This provides **bandwidth aggregation** and **redundancy** without STP blocking any of the bundled ports — because STP sees the entire bundle as one logical interface.

**EtherChannel Negotiation Protocols:**

| Protocol | Standard | Modes |
|---|---|---|
| **LACP** (Link Aggregation Control Protocol) | IEEE 802.3ad | `active` (initiates), `passive` (responds) |
| **PAgP** (Port Aggregation Protocol) | Cisco proprietary | `desirable` (initiates), `auto` (responds) |
| **Static (On)** | None | `on` — no negotiation, just bundles |

**LACP mode compatibility:**
| Switch A | Switch B | Result |
|---|---|---|
| active | active | ✅ Forms EtherChannel |
| active | passive | ✅ Forms EtherChannel |
| passive | passive | ❌ Will NOT form (neither initiates) |
| on | on | ✅ Forms (static, no negotiation) |
| on | active/passive | ❌ Will NOT form (mode mismatch) |

**EtherChannel Configuration (LACP):**
```
! Configure on both switches — same config on each end
interface range GigabitEthernet0/1-4
 switchport mode trunk
 switchport trunk encapsulation dot1q
 channel-group 1 mode active
 channel-protocol lacp

interface Port-channel1
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 10,20,30,100
```

**EtherChannel Load Balancing:**
Traffic across an EtherChannel is distributed using a hashing algorithm. The default hash input varies by platform but commonly uses source/destination MAC or IP addresses.
```
! View current load-balance method
show etherchannel load-balance

! Change load-balance method (global command)
port-channel load-balance src-dst-ip
```

> **Graduate Design Note:** The load-balancing algorithm does NOT guarantee even distribution — it guarantees that all frames in a single flow always traverse the same physical link (required for in-order delivery). If you have one dominant flow, it will use only one link regardless of how many are bundled. This is a common misconception in production environments.

**EtherChannel Verification Commands:**
```
show etherchannel summary          ! Status: bundled (P), standby (D), suspended (s)
show etherchannel detail           ! Full detail per port
show interfaces port-channel 1     ! Logical interface stats
show lacp neighbor                 ! LACP partner information
```

**Common EtherChannel Failure Causes:**
1. **Speed/duplex mismatch** — all member ports must match.
2. **Switchport mode mismatch** — all ports must be the same (all trunk or all access).
3. **Allowed VLAN mismatch** — trunk allowed VLANs must be identical on all member ports.
4. **LACP mode incompatibility** — passive/passive never forms.
5. **STP inconsistency** — if member ports have different STP configurations, EtherChannel will not form.

---

### Section 2: Multiple Spanning Tree (MST — 802.1S)

[05:30 – 10:00]
[SHOW DIAGRAM: MST region with 20 VLANs mapped to 2 MST instances]

In an enterprise with 50 VLANs running Rapid PVST+, the switch runs **50 separate STP instances** — one per VLAN. Each instance has its own BPDU flooding, topology database, and CPU load. For large VLAN counts, this overhead becomes significant.

**MST (802.1S)** solves this by allowing you to map **multiple VLANs to a single STP instance**. Instead of 50 STP instances, you might run 2 or 3.

**MST Key Concepts:**
- **MST Region:** A set of switches sharing the same MST configuration (region name, revision, and VLAN-to-instance mapping).
- **IST (Internal Spanning Tree / Instance 0):** The default instance that all VLANs belong to if not explicitly mapped. Also handles interoperability with non-MST switches.
- **MSTI (Multiple Spanning Tree Instance):** A user-defined instance to which specific VLANs are mapped.

**MST Configuration:**
```
spanning-tree mode mst

spanning-tree mst configuration
 name TXWES-CAMPUS
 revision 1
 instance 1 vlan 10,20,30,40,50
 instance 2 vlan 60,70,80,90,100

! Set bridge priorities per instance
spanning-tree mst 1 priority 4096   ! Root for VLANs 10-50
spanning-tree mst 2 priority 8192   ! Secondary for VLANs 60-100
```

> **Important:** All switches within an MST region MUST have identical `name`, `revision`, and VLAN-to-instance mapping. A single mismatch puts a switch in a different MST region, causing STP to treat the inter-region link as an IST boundary.

---

### Section 3: Campus STP Troubleshooting Scenarios

[10:00 – 13:30]
[SHOW SLIDE: Troubleshooting methodology diagram]

At CCNP level, you need to diagnose STP problems from show command output alone. Here are the most common scenarios:

**Scenario 1: Unexpected Root Bridge**
*Symptom:* A low-priority access switch has become root bridge, causing suboptimal traffic flow.
*Diagnosis:* `show spanning-tree vlan X` — check the Root ID and Bridge ID. If an access switch has lower priority than the distribution switch, it wins the election.
*Resolution:* Set explicit priority on the distribution/core switches:
```
spanning-tree vlan 10 root primary
! Or explicitly:
spanning-tree vlan 10 priority 4096
```

**Scenario 2: Port Stuck in BLK/Discarding Despite Being Needed**
*Symptom:* Traffic not flowing on a path that should be active; `show spanning-tree` shows a port in BLK state.
*Diagnosis:* Check if this is expected (preventing a loop) or if a better root port should have been chosen. Compare path costs.
*Resolution:* Adjust path cost on the preferred port to make it the root port:
```
interface GigabitEthernet0/1
 spanning-tree vlan 10 cost 2
```

**Scenario 3: Topology Change (TC) Flooding**
*Symptom:* Network instability, MAC table flushes, excessive broadcast traffic.
*Diagnosis:* `show spanning-tree detail` — look for "Number of topology changes" and the timestamp. Identify which port is generating TCs.
*Resolution:* Enable `spanning-tree portfast` on all access (end-device) ports. PortFast ports do not generate TCs when they transition. If a trunk port is generating TCs, investigate the upstream device.

**Scenario 4: BPDU Guard Err-Disabled**
*Symptom:* An access port is in `err-disabled` state.
*Diagnosis:* `show interfaces GigabitEthernet0/3 status` — shows `err-disabled`. `show errdisable recovery` confirms BPDU Guard triggered it.
*Resolution:* Determine why a BPDU was received (rogue switch, misconfigured AP). Remove the device, then:
```
interface GigabitEthernet0/3
 shutdown
 no shutdown
```
Or configure automatic recovery:
```
errdisable recovery cause bpduguard
errdisable recovery interval 300
```

---

### Section 4: Module 02 Lab Preview

[13:30 – 15:30]
[SHOW SLIDE: Module 02 Lab Topology]

In the Module 02 lab, you will build a campus switching topology in Cisco Packet Tracer:

**Topology:** 2 distribution switches (DS1, DS2) + 4 access switches (AS1–AS4). VLANs 10, 20, 30, and 99 (management). Trunk links on all inter-switch connections. EtherChannel (LACP active) between DS1 and DS2. Inter-VLAN routing via SVIs on the distribution switches.

**Lab Tasks:**
1. Configure VLANs 10, 20, 30, 99 on all switches.
2. Configure 802.1Q trunks between all switches with correct native VLAN (VLAN 999) and allowed VLANs.
3. Configure LACP EtherChannel (Port-Channel 1) between DS1 and DS2.
4. Set DS1 as STP root for VLANs 10 and 20; DS2 as root for VLANs 30 and 99 (load balancing).
5. Enable PortFast and BPDU Guard on all access switch downlinks.
6. Configure SVIs on DS1 and DS2 for inter-VLAN routing.
7. Verify end-to-end connectivity across VLANs.

Full lab instructions are in the Module 02 Lab Assignment.

**Assignments due: Sunday, November 1, 2026 at 11:59 PM CST**

---
*End of Part 2 — Module 02*
