# Lab Activity: Module 01 - Network Architectures & Topologies

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will design and verify a three-tier enterprise campus network topology using Cisco Packet Tracer. You will place and connect devices at the Core, Distribution, and Access layers, configure trunk links between layers, assign VLANs at the Access layer, and verify the full topology using Cisco IOS show commands.

This lab directly maps to CCNA 200-301 exam objectives 1.1 (network components), 1.2 (network topology architectures), and 2.1 (VLANs and trunking concepts).

---

## Objectives

By completing this lab you will be able to:

- Build a three-tier campus network topology in Packet Tracer
- Configure 802.1Q trunk links between Access and Distribution layer switches
- Assign switch ports to VLANs at the Access layer
- Verify the topology using CDP, trunk, and VLAN show commands
- Identify the role of each device based on its position in the hierarchy

---

## Equipment List

Use the following devices in Packet Tracer:

- 2x Cisco Catalyst 3650-24PS (Core layer switches: SW-CORE-1, SW-CORE-2)
- 2x Cisco Catalyst 3650-24PS (Distribution layer switches: SW-DIST-1, SW-DIST-2)
- 4x Cisco Catalyst 2960-24TT (Access layer switches: SW-ACC-1, SW-ACC-2, SW-ACC-3, SW-ACC-4)
- 4x PC (end devices connected to Access switches)
- Straight-through Ethernet cables for all connections

---

## Addressing Table

| Device | Interface | VLAN / Role | Notes |
|---|---|---|---|
| SW-CORE-1 | Gi0/1 | Uplink to SW-DIST-1 | Trunk |
| SW-CORE-1 | Gi0/2 | Uplink to SW-DIST-2 | Trunk |
| SW-CORE-2 | Gi0/1 | Uplink to SW-DIST-1 | Trunk |
| SW-CORE-2 | Gi0/2 | Uplink to SW-DIST-2 | Trunk |
| SW-DIST-1 | Gi0/1 | Uplink to SW-CORE-1 | Trunk |
| SW-DIST-1 | Gi0/2 | Uplink to SW-CORE-2 | Trunk |
| SW-DIST-1 | Fa0/1 | Downlink to SW-ACC-1 | Trunk |
| SW-DIST-1 | Fa0/2 | Downlink to SW-ACC-2 | Trunk |
| SW-DIST-2 | Fa0/1 | Downlink to SW-ACC-3 | Trunk |
| SW-DIST-2 | Fa0/2 | Downlink to SW-ACC-4 | Trunk |
| SW-ACC-1 | Fa0/1 | Access port | VLAN 10 |
| SW-ACC-2 | Fa0/1 | Access port | VLAN 20 |
| SW-ACC-3 | Fa0/1 | Access port | VLAN 10 |
| SW-ACC-4 | Fa0/1 | Access port | VLAN 20 |

---

## Part 1: Topology Construction and Configuration

### Step 1: Build the Physical Topology

Open Cisco Packet Tracer and place devices according to the equipment list. Arrange them in three visual rows:

- Top row: SW-CORE-1 and SW-CORE-2 (Core layer)
- Middle row: SW-DIST-1 and SW-DIST-2 (Distribution layer)
- Bottom row: SW-ACC-1, SW-ACC-2, SW-ACC-3, SW-ACC-4 (Access layer)

Connect devices using the addressing table. Use straight-through cables for all switch-to-switch links in this topology. Label each device using the names in the equipment list.

### Step 2: Configure Hostnames on All Switches

On each switch, enter privileged EXEC mode and apply the correct hostname. Example for SW-CORE-1:

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW-CORE-1
SW-CORE-1(config)# end
SW-CORE-1# write memory
```

Repeat for SW-CORE-2, SW-DIST-1, SW-DIST-2, SW-ACC-1 through SW-ACC-4.

### Step 3: Create VLANs on Distribution and Access Switches

On SW-DIST-1, SW-DIST-2, SW-ACC-1 through SW-ACC-4, create VLAN 10 and VLAN 20 with descriptive names:

```ios
SW-DIST-1# configure terminal
SW-DIST-1(config)# vlan 10
SW-DIST-1(config-vlan)# name ENGINEERING
SW-DIST-1(config-vlan)# vlan 20
SW-DIST-1(config-vlan)# name SALES
SW-DIST-1(config-vlan)# end
```

Repeat this VLAN configuration on SW-DIST-2 and all four Access switches.

### Step 4: Configure Trunk Ports on Distribution Switches

On SW-DIST-1, configure trunk links toward the Core and toward the Access switches:

```ios
SW-DIST-1# configure terminal
SW-DIST-1(config)# interface GigabitEthernet0/1
SW-DIST-1(config-if)# switchport mode trunk
SW-DIST-1(config-if)# switchport trunk allowed vlan 10,20
SW-DIST-1(config-if)# interface GigabitEthernet0/2
SW-DIST-1(config-if)# switchport mode trunk
SW-DIST-1(config-if)# switchport trunk allowed vlan 10,20
SW-DIST-1(config-if)# interface FastEthernet0/1
SW-DIST-1(config-if)# switchport mode trunk
SW-DIST-1(config-if)# switchport trunk allowed vlan 10,20
SW-DIST-1(config-if)# interface FastEthernet0/2
SW-DIST-1(config-if)# switchport mode trunk
SW-DIST-1(config-if)# switchport trunk allowed vlan 10,20
SW-DIST-1(config-if)# end
SW-DIST-1# write memory
```

Repeat for SW-DIST-2 on its respective interfaces.

### Step 5: Configure Trunk Ports on Core Switches

On SW-CORE-1, configure trunk links toward both Distribution switches:

```ios
SW-CORE-1# configure terminal
SW-CORE-1(config)# interface GigabitEthernet0/1
SW-CORE-1(config-if)# switchport mode trunk
SW-CORE-1(config-if)# switchport trunk allowed vlan 10,20
SW-CORE-1(config-if)# interface GigabitEthernet0/2
SW-CORE-1(config-if)# switchport mode trunk
SW-CORE-1(config-if)# switchport trunk allowed vlan 10,20
SW-CORE-1(config-if)# end
SW-CORE-1# write memory
```

Repeat for SW-CORE-2.

### Step 6: Configure Access Ports on Access Switches

On each Access switch, configure the port connected to the PC as an access port in the correct VLAN:

SW-ACC-1 (VLAN 10):

```ios
SW-ACC-1# configure terminal
SW-ACC-1(config)# interface FastEthernet0/1
SW-ACC-1(config-if)# switchport mode access
SW-ACC-1(config-if)# switchport access vlan 10
SW-ACC-1(config-if)# end
SW-ACC-1# write memory
```

SW-ACC-2 (VLAN 20):

```ios
SW-ACC-2# configure terminal
SW-ACC-2(config)# interface FastEthernet0/1
SW-ACC-2(config-if)# switchport mode access
SW-ACC-2(config-if)# switchport access vlan 20
SW-ACC-2(config-if)# end
SW-ACC-2# write memory
```

Repeat for SW-ACC-3 (VLAN 10) and SW-ACC-4 (VLAN 20).

---

## Part 2: Verification and Troubleshooting

### Step 7: Verify VLAN Configuration

On each switch, verify that VLANs 10 and 20 exist and that access ports are correctly assigned:

```ios
SW-ACC-1# show vlan brief
```

Expected output (abbreviated):

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------
1    default                          active    Fa0/2, Fa0/3...
10   ENGINEERING                      active    Fa0/1
20   SALES                            active
```

Record the output for your deliverables. Confirm that Fa0/1 appears under VLAN 10 on SW-ACC-1.

### Step 8: Verify Trunk Links

On SW-DIST-1, verify that trunk links are active and carrying the correct VLANs:

```ios
SW-DIST-1# show interfaces trunk
```

Expected output (abbreviated):

```text
Port      Mode         Encapsulation  Status        Native vlan
Gi0/1     on           802.1q         trunking      1
Gi0/2     on           802.1q         trunking      1
Fa0/1     on           802.1q         trunking      1
Fa0/2     on           802.1q         trunking      1

Port      Vlans allowed and active in management domain
Gi0/1     10,20
Gi0/2     10,20
Fa0/1     10,20
Fa0/2     10,20
```

If a port does not appear in the trunk output, it is not trunking. Return to Part 1 and verify the `switchport mode trunk` command was applied to that interface.

### Step 9: Verify CDP Neighbors

From SW-CORE-1, verify that CDP has discovered the connected Distribution switches:

```ios
SW-CORE-1# show cdp neighbors
```

Expected output (abbreviated):

```text
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW-DIST-1        Gig 0/1           170              S I   WS-C3650  Gig 0/1
SW-DIST-2        Gig 0/2           165              S I   WS-C3650  Gig 0/2
```

If a neighbor is missing, verify the cable connection and that CDP is enabled (it is enabled by default on Cisco IOS).

### Step 10: Troubleshooting Scenarios

Work through the following troubleshooting scenarios. Document your findings for each.

Scenario A: SW-ACC-3's Fa0/1 shows in VLAN 1 instead of VLAN 10 after `show vlan brief`. What command resolves this?

```ios
SW-ACC-3# configure terminal
SW-ACC-3(config)# interface FastEthernet0/1
SW-ACC-3(config-if)# switchport access vlan 10
```

Scenario B: The trunk between SW-DIST-1 and SW-ACC-2 is not appearing in `show interfaces trunk`. What are the two most likely causes and the commands to investigate?

```ios
SW-DIST-1# show interfaces FastEthernet0/2 switchport
SW-ACC-2# show interfaces FastEthernet0/24 switchport
```

Check that both sides show `Operational Mode: trunk`. If one side shows `access`, the trunk negotiation failed. Manually set both sides to `switchport mode trunk`.

Scenario C: SW-CORE-1 shows SW-DIST-1 in CDP neighbors but not SW-DIST-2. Name two possible causes without using show commands.

Answer: The cable between SW-CORE-1 and SW-DIST-2 may be disconnected or the wrong port was cabled. Alternatively, CDP may have been disabled on the SW-DIST-2 uplink interface.

---

## Deliverables

Submit the following in Canvas as a single PDF or Word document:

1. A screenshot of your completed Packet Tracer topology showing all devices, labels, and connections
2. The `show vlan brief` output from SW-ACC-1, SW-ACC-2, SW-ACC-3, and SW-ACC-4
3. The `show interfaces trunk` output from SW-DIST-1 and SW-DIST-2
4. The `show cdp neighbors` output from SW-CORE-1
5. Written answers to Troubleshooting Scenarios A, B, and C (2-4 sentences each)
6. A brief reflection (100-150 words) explaining which layer each switch in your topology belongs to and why that layer assignment matters

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| Topology Screenshot | 15 | All 8 switches placed, labeled, and connected correctly |
| VLAN Verification (4 switches) | 20 | Each switch shows correct VLAN assignments (5 pts each) |
| Trunk Verification (2 switches) | 20 | Both Distribution switches show all trunk ports with correct VLANs (10 pts each) |
| CDP Neighbor Output | 10 | SW-CORE-1 shows both Distribution switches |
| Troubleshooting Scenarios | 25 | Correct diagnosis and resolution for each scenario (A=8, B=9, C=8) |
| Reflection | 10 | Accurate layer identification and explanation for all 8 devices |

Partial credit is awarded for incomplete but demonstrably attempted work. No credit is awarded for screenshots that appear fabricated or do not match the described topology.

---

## Part 9 — Challenge Exercise

This optional challenge extends the lab to CCNA exam difficulty. Complete all steps and include deliverables in your submission for up to 20 bonus points.

### Challenge Step 1: Implement Redundant Uplinks and Verify STP Behavior

Add a second uplink cable from each Access switch to its alternate Distribution switch, creating a redundant triangle between each Access switch, SW-DIST-1, and SW-DIST-2. Verify that Spanning Tree Protocol is automatically blocking one of the redundant links on each Access switch to prevent a Layer 2 loop:

```ios
SW-ACC-1# show spanning-tree vlan 10
```

Identify which port on SW-ACC-1 is in Blocking state and explain in 2-3 sentences why STP selected that specific port to block based on port cost and root port selection rules.

### Challenge Step 2: Configure SVIs on Distribution Switches for Inter-VLAN Routing

Upgrade SW-DIST-1 from a Layer 2 switch to a multilayer switch behavior by enabling `ip routing` and creating SVIs for VLAN 10 and VLAN 20. Assign the SVIs the following addresses:

- VLAN 10 SVI: 192.168.10.1/24
- VLAN 20 SVI: 192.168.20.1/24

Assign PCs in VLAN 10 an address from 192.168.10.0/24 with a default gateway of 192.168.10.1. Assign PCs in VLAN 20 an address from 192.168.20.0/24 with a default gateway of 192.168.20.1. Verify that a PC in VLAN 10 can ping a PC in VLAN 20 through SW-DIST-1:

```ios
SW-DIST-1# configure terminal
SW-DIST-1(config)# ip routing
SW-DIST-1(config)# interface vlan 10
SW-DIST-1(config-if)# ip address 192.168.10.1 255.255.255.0
SW-DIST-1(config-if)# no shutdown
SW-DIST-1(config)# interface vlan 20
SW-DIST-1(config-if)# ip address 192.168.20.1 255.255.255.0
SW-DIST-1(config-if)# no shutdown
```

Capture the successful ping output and include it as a deliverable. If ping fails, run `show ip route` on SW-DIST-1 and troubleshoot using the verification commands from the CLI Command Reference table.

### Challenge Step 3: Verify End-to-End Topology Using show ip route and CDP Depth

From SW-DIST-1, run `show cdp neighbors detail` and confirm you can see both SW-CORE-1 and SW-CORE-2 as neighbors. Then run `show ip route` and verify that routes to VLAN 10 (192.168.10.0/24) and VLAN 20 (192.168.20.0/24) appear as directly connected routes ("C" entries) in the routing table. In your submission, explain in 3-4 sentences why these routes appear as "C" (connected) rather than "O" (OSPF) or "S" (static), and what would need to change for a route learned from another router to appear as "O" in the same table.
