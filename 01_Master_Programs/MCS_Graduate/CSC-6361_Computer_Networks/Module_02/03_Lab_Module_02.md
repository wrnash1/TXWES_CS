# Lab Assignment: Module 02 – Campus Switching: VLANs, STP & EtherChannel
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 1, 2026 at 11:59 PM CST

---

## Lab Overview
**Estimated Time:** 3–4 hours
**Tools Required:** Cisco Packet Tracer (free — download at netacad.com)
**Deliverables:** (1) Completed `.pkt` Packet Tracer file, (2) Professional Lab Report (PDF)

This lab builds a complete enterprise campus switching infrastructure including VLANs, 802.1Q trunks, LACP EtherChannel, Rapid PVST+ with STP optimization, SVIs for inter-VLAN routing, and STP security features.

---

## Lab Topology

```
                    [DS1] ══════════════ [DS2]
                   (Po1 — 2x LACP)    (Priority: VLANs 30,99)
                   (Priority: VLANs 10,20)
                  /    \              /    \
              [AS1]    [AS2]      [AS3]    [AS4]
              VLAN10   VLAN20     VLAN30   VLAN99(Mgmt)
```

**Device Assignments:**
| Device | Role | VLANs Configured |
|---|---|---|
| DS1 | Distribution Switch 1 (L3) | 10, 20, 30, 99 |
| DS2 | Distribution Switch 2 (L3) | 10, 20, 30, 99 |
| AS1 | Access Switch 1 | 10 (Data), 99 (Mgmt) |
| AS2 | Access Switch 2 | 20 (Voice/Data), 99 (Mgmt) |
| AS3 | Access Switch 3 | 30 (IoT/Medical), 99 (Mgmt) |
| AS4 | Access Switch 4 | 99 (Mgmt only — for STP testing) |
| PC1 | End Device | VLAN 10 (10.10.10.10/24) |
| PC2 | End Device | VLAN 20 (10.10.20.10/24) |
| PC3 | End Device | VLAN 30 (10.10.30.10/24) |

**IP Addressing — SVIs on DS1 and DS2:**
| VLAN | DS1 SVI | DS2 SVI | Default Gateway (HSRP Virtual — covered in Module 05) |
|---|---|---|---|
| VLAN 10 | 10.10.10.1/24 | 10.10.10.2/24 | 10.10.10.254 |
| VLAN 20 | 10.10.20.1/24 | 10.10.20.2/24 | 10.10.20.254 |
| VLAN 30 | 10.10.30.1/24 | 10.10.30.2/24 | 10.10.30.254 |
| VLAN 99 | 10.99.99.1/24 | 10.99.99.2/24 | 10.99.99.254 |

*Note: For this lab, configure PC default gateways to DS1's SVI address. HSRP will be added in Module 05.*

---

## Lab Instructions

### Part 1: Build the Physical Topology (10 pts)
1. Open Cisco Packet Tracer. Place 2 multilayer switches (3650 or 3560) for DS1 and DS2. Place 4 Layer 2 switches (2960) for AS1–AS4. Add 3 PCs.
2. Connect DS1 to DS2 using **two GigabitEthernet cables** (these will become the EtherChannel).
3. Connect AS1 and AS2 to DS1 (one link each). Connect AS3 and AS4 to DS2 (one link each).
4. Connect PC1 to AS1, PC2 to AS2, PC3 to AS3.
5. **Screenshot Checkpoint 1:** Full topology view showing all devices and connections.

### Part 2: Configure VLANs on All Switches (15 pts)
On **every switch** (DS1, DS2, AS1–AS4), configure the following VLANs:
```
vlan 10
 name DATA_STAFF
vlan 20
 name VOICE_DATA
vlan 30
 name IOT_MEDICAL
vlan 99
 name MANAGEMENT
vlan 999
 name NATIVE_UNUSED
```
**Screenshot Checkpoint 2:** `show vlan brief` on DS1 showing all 5 VLANs active.

### Part 3: Configure 802.1Q Trunks (15 pts)
Configure **all inter-switch links** as 802.1Q trunks. Set native VLAN to 999 (unused) and allow only VLANs 10, 20, 30, 99.

```
! On DS1 and DS2 — uplink to access switches
interface GigabitEthernet0/3   ! Link to AS1
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99

! Repeat for all inter-switch links
```

On AS1–AS4, configure all uplinks to distribution switches as trunks with the same settings.
Configure the **access port** to each PC:
```
! On AS1 — port connected to PC1
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
```

**Screenshot Checkpoint 3:** `show interfaces trunk` on DS1 showing all trunk links with correct native VLAN and allowed VLANs.

### Part 4: Configure LACP EtherChannel Between DS1 and DS2 (20 pts)
Bundle the two physical links between DS1 and DS2 into a single EtherChannel using LACP.

**On DS1:**
```
interface range GigabitEthernet0/1-2
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99
 channel-group 1 mode active
 channel-protocol lacp

interface Port-channel1
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99
```
**On DS2:** Same configuration (also `channel-group 1 mode active`).

**Screenshot Checkpoint 4:** `show etherchannel summary` on DS1 — verify Port-channel1 shows `SU` (Layer 2 up) with two member ports showing `P` (bundled in port-channel).

### Part 5: Configure Rapid PVST+ with STP Load Balancing (15 pts)
Configure Rapid PVST+ (the default on modern Cisco IOS). Set STP root bridges to distribute load:
- **DS1 = root for VLAN 10 and VLAN 20**
- **DS2 = root for VLAN 30 and VLAN 99**

```
! On DS1:
spanning-tree mode rapid-pvst
spanning-tree vlan 10,20 root primary
spanning-tree vlan 30,99 root secondary

! On DS2:
spanning-tree mode rapid-pvst
spanning-tree vlan 30,99 root primary
spanning-tree vlan 10,20 root secondary
```

Enable STP security on all **access switch downlinks to PCs**:
```
spanning-tree portfast bpduguard default
spanning-tree portfast default
```

**Screenshot Checkpoint 5:** `show spanning-tree vlan 10` on DS1 — confirm DS1 is root (Bridge ID shows `This bridge is the root`). `show spanning-tree vlan 30` on DS2 — confirm DS2 is root.

### Part 6: Configure SVIs for Inter-VLAN Routing (15 pts)
On both DS1 and DS2, enable IP routing and create SVIs for each VLAN.

```
! On DS1:
ip routing

interface Vlan10
 ip address 10.10.10.1 255.255.255.0
 no shutdown

interface Vlan20
 ip address 10.10.20.1 255.255.255.0
 no shutdown

interface Vlan30
 ip address 10.10.30.1 255.255.255.0
 no shutdown

interface Vlan99
 ip address 10.99.99.1 255.255.255.0
 no shutdown
```
Repeat on DS2 with .2 addresses. Configure PC1 default gateway = 10.10.10.1, PC2 = 10.10.20.1, PC3 = 10.10.30.1.

**Screenshot Checkpoint 6:** Ping from PC1 (VLAN 10) to PC2 (VLAN 20) and PC3 (VLAN 30). All must succeed. Show `show ip route` on DS1 confirming connected routes for all 4 VLANs.

### Part 7: End-to-End Verification (10 pts)
1. Physically unplug one of the two EtherChannel links between DS1 and DS2. Verify traffic still flows (EtherChannel fails over to remaining link).
2. Plug it back in. Verify both links re-join the EtherChannel.
3. `show spanning-tree vlan 10` — confirm the EtherChannel port-channel appears as a single interface in STP.

---

## Lab Report Requirements (Graduate Standard)
1. **Topology Diagram** — annotated screenshot of your final Packet Tracer topology.
2. **All 6 Screenshot Checkpoints** — labeled and annotated.
3. **Key Configurations** — full running configs for DS1 and DS2.
4. **Analysis Section (2–3 paragraphs):**
   - Explain why setting native VLAN to an unused VLAN (999) mitigates VLAN hopping attacks.
   - Explain the consequence if EtherChannel members have a VLAN mismatch between the two ends.
   - Describe how you would add a seventh VLAN to this network — what changes on which devices, and in what order?
5. **Troubleshooting Log:** Document one issue you encountered and how you resolved it.

---

## Grading Rubric
| Component | Points |
|---|---|
| Physical Topology (Part 1) | 10 |
| VLAN Configuration (Part 2) | 15 |
| 802.1Q Trunks (Part 3) | 15 |
| LACP EtherChannel (Part 4) | 20 |
| Rapid PVST+ & STP Security (Part 5) | 15 |
| SVIs & Inter-VLAN Routing (Part 6) | 15 |
| End-to-End Verification (Part 7) | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: MST Migration from Rapid PVST+
Migrate your existing Rapid PVST+ configuration to MST while preserving the same traffic engineering (DS1 preferred for VLANs 10/20, DS2 preferred for VLANs 30/99):
1. On all six switches, enter `spanning-tree mst configuration` mode and configure: `name CAMPUS-MST`, `revision 1`, `instance 1 vlan 10,20`, `instance 2 vlan 30,99`.
2. Change the spanning tree mode: `spanning-tree mode mst` on all switches simultaneously (coordinate this — mismatched MST regions during transition cause temporary topology disruption).
3. Set DS1 as root for MST instance 1 (`spanning-tree mst 1 priority 4096`) and DS2 as root for instance 2 (`spanning-tree mst 2 priority 4096`).
4. Verify with `show spanning-tree mst 1` — confirm DS1 is root for instance 1 and DS2 is root for instance 2. Confirm all VLANs in each instance follow their expected root.

### Challenge 2: STP Topology Change Simulation and Loop Guard
Deliberately introduce a STP topology change and observe the MAC table flush behavior:
1. Connect AS4 to both DS1 and DS2 with two uplinks (creating a redundant path). Verify STP blocks one of the uplinks.
2. Enable Loop Guard on the blocked port: `spanning-tree guard loop` on the DS1 or DS2 port connecting to AS4's secondary uplink.
3. Simulate a unidirectional link failure by applying an inbound ACL on the blocked port that drops all incoming frames (simulating BPDUs no longer arriving). Observe: without Loop Guard the port would transition to Forwarding; with Loop Guard it enters loop-inconsistent state instead.
4. Run `show spanning-tree detail | include transitions` before and after a physical link failure to observe topology change counter increments. Document how many TCN BPDUs are generated.

### Reflection Questions
1. When migrating a 120-VLAN campus network from Rapid PVST+ to MST, what is the primary operational risk during the cutover window, and what specific pre-migration step would you take to minimize the chance of a broadcast storm during the transition?
2. An enterprise campus has two distribution switches connected to eight access switches. The network team is debating whether to use Rapid PVST+ (one instance per VLAN) or MST (two instances for 50 VLANs each). What CPU and memory utilization argument would you make for MST, and at what VLAN count threshold does MST become clearly preferable from an operational standpoint?
