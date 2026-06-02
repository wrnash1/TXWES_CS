# Lab Activity: Module 04 - Switching Concepts & VLANs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure VLANs, access ports, and trunk links on a two-switch topology in Cisco Packet Tracer. You will create VLANs, assign end-device ports to specific VLANs, configure trunk uplinks, change the native VLAN, disable DTP on access ports, and verify the configuration using Cisco IOS show commands.

This lab maps to CCNA 200-301 exam objectives 2.1 (configure and verify VLANs) and 2.2 (configure and verify interswitch connectivity).

---

## Objectives

By completing this lab you will be able to:

- Create VLANs and assign descriptive names using Cisco IOS
- Configure access ports and assign them to the correct VLAN
- Configure 802.1Q trunk links between switches
- Change the native VLAN on a trunk to a non-default VLAN
- Disable DTP on access ports
- Verify VLAN and trunk configuration using `show vlan brief` and `show interfaces trunk`
- Interpret `show vlan brief` output to identify and correct misconfigured ports

---

## Equipment List

Use the following devices in Packet Tracer:

- 2x Cisco Catalyst 2960-24TT switches (SW1 and SW2)
- 6x PCs (PC1 through PC6)
- Straight-through Ethernet cables for all connections

---

## VLAN Assignment Table

| VLAN ID | VLAN Name | Purpose |
|---|---|---|
| 10 | ENGINEERING | Engineering department devices |
| 20 | SALES | Sales department devices |
| 30 | MANAGEMENT | Switch management (SVI) |
| 99 | NATIVE_TRUNK | Native VLAN for trunk links (no devices) |

---

## Port Assignment Table

| Device | Interface | Mode | VLAN | Connected Device |
|---|---|---|---|---|
| SW1 | Fa0/1 | access | 10 | PC1 |
| SW1 | Fa0/2 | access | 10 | PC2 |
| SW1 | Fa0/3 | access | 20 | PC3 |
| SW1 | Gi0/1 | trunk | 10,20,30 | SW2 Gi0/1 |
| SW2 | Fa0/1 | access | 10 | PC4 |
| SW2 | Fa0/2 | access | 20 | PC5 |
| SW2 | Fa0/3 | access | 20 | PC6 |

---

## Part 1: Configuration

### Step 1: Build the Physical Topology

In Packet Tracer, place SW1 and SW2 side by side. Connect PC1-PC3 to SW1 Fa0/1-Fa0/3. Connect PC4-PC6 to SW2 Fa0/1-Fa0/3. Connect SW1 Gi0/1 to SW2 Gi0/1 using a straight-through cable (Packet Tracer auto-detects crossover requirements). Label all devices.

### Step 2: Configure Hostnames on Both Switches

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# end
```

Repeat with hostname SW2.

### Step 3: Create VLANs on SW1

Create all four VLANs with names. Always create VLANs before assigning ports:

```ios
SW1# configure terminal
SW1(config)# vlan 10
SW1(config-vlan)# name ENGINEERING
SW1(config-vlan)# vlan 20
SW1(config-vlan)# name SALES
SW1(config-vlan)# vlan 30
SW1(config-vlan)# name MANAGEMENT
SW1(config-vlan)# vlan 99
SW1(config-vlan)# name NATIVE_TRUNK
SW1(config-vlan)# end
SW1# write memory
```

Verify immediately:

```ios
SW1# show vlan brief
```

Confirm VLANs 10, 20, 30, and 99 appear in the output with their correct names.

### Step 4: Create the Same VLANs on SW2

Repeat Step 3 on SW2. VLANs must exist on both switches for VLAN traffic to cross the trunk.

### Step 5: Configure Access Ports on SW1

```ios
SW1# configure terminal
SW1(config)# interface FastEthernet0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# switchport nonegotiate
SW1(config-if)# interface FastEthernet0/2
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# switchport nonegotiate
SW1(config-if)# interface FastEthernet0/3
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 20
SW1(config-if)# switchport nonegotiate
SW1(config-if)# end
SW1# write memory
```

### Step 6: Configure Access Ports on SW2

```ios
SW2# configure terminal
SW2(config)# interface FastEthernet0/1
SW2(config-if)# switchport mode access
SW2(config-if)# switchport access vlan 10
SW2(config-if)# switchport nonegotiate
SW2(config-if)# interface FastEthernet0/2
SW2(config-if)# switchport mode access
SW2(config-if)# switchport access vlan 20
SW2(config-if)# switchport nonegotiate
SW2(config-if)# interface FastEthernet0/3
SW2(config-if)# switchport mode access
SW2(config-if)# switchport access vlan 20
SW2(config-if)# switchport nonegotiate
SW2(config-if)# end
SW2# write memory
```

### Step 7: Configure the Trunk Link

Configure the Gi0/1 trunk on SW1:

```ios
SW1# configure terminal
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20,30
SW1(config-if)# switchport trunk native vlan 99
SW1(config-if)# end
SW1# write memory
```

Configure the Gi0/1 trunk on SW2:

```ios
SW2# configure terminal
SW2(config)# interface GigabitEthernet0/1
SW2(config-if)# switchport mode trunk
SW2(config-if)# switchport trunk allowed vlan 10,20,30
SW2(config-if)# switchport trunk native vlan 99
SW2(config-if)# end
SW2# write memory
```

### Step 8: Configure PC IP Addresses

Assign IP addresses to each PC in the same subnet for their VLAN. Use this addressing:

- VLAN 10 (Engineering): 192.168.10.x /24, gateway 192.168.10.1
- VLAN 20 (Sales): 192.168.20.x /24, gateway 192.168.20.1

PC1: 192.168.10.11 /24 gateway 192.168.10.1
PC2: 192.168.10.12 /24 gateway 192.168.10.1
PC3: 192.168.20.13 /24 gateway 192.168.20.1
PC4: 192.168.10.14 /24 gateway 192.168.10.1
PC5: 192.168.20.15 /24 gateway 192.168.20.1
PC6: 192.168.20.16 /24 gateway 192.168.20.1

---

## Part 2: Verification and Troubleshooting

### Step 9: Verify VLAN Assignment with show vlan brief

On SW1:

```ios
SW1# show vlan brief
```

Expected output (abbreviated):

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- ----------------------------
1    default                          active    Fa0/4, Fa0/5...
10   ENGINEERING                      active    Fa0/1, Fa0/2
20   SALES                            active    Fa0/3
30   MANAGEMENT                       active
99   NATIVE_TRUNK                     active
```

Confirm:

- Fa0/1 and Fa0/2 are listed under VLAN 10
- Fa0/3 is listed under VLAN 20
- Gi0/1 is NOT listed here (it is a trunk)
- All unused ports default to VLAN 1

### Step 10: Verify Trunk Configuration

```ios
SW1# show interfaces trunk
```

Expected output (abbreviated):

```text
Port      Mode         Encapsulation  Status        Native vlan
Gi0/1     on           802.1q         trunking      99

Port      Vlans allowed on trunk
Gi0/1     10,20,30

Port      Vlans allowed and active in management domain
Gi0/1     10,20,30

Port      Vlans in spanning tree forwarding state and not pruned
Gi0/1     10,20,30
```

Confirm the native VLAN is 99 and VLANs 10, 20, 30 are active on the trunk.

### Step 11: Test Intra-VLAN Connectivity

From PC1 (192.168.10.11) in Packet Tracer, open the command prompt and ping PC4 (192.168.10.14). Both are in VLAN 10 but on different switches — this tests trunk functionality:

```text
C:\> ping 192.168.10.14
```

A successful ping confirms VLAN 10 traffic is passing across the trunk correctly.

Attempt to ping PC5 (192.168.20.15) from PC1:

```text
C:\> ping 192.168.20.15
```

This ping should fail because PC1 (VLAN 10) and PC5 (VLAN 20) are in different VLANs and no inter-VLAN routing is configured. This is the expected result and demonstrates VLAN segmentation working correctly.

### Step 12: Verify a Single Port's Switchport Configuration

```ios
SW1# show interfaces FastEthernet0/1 switchport
```

Expected output (key lines):

```text
Name: Fa0/1
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: dot1q
Access Mode VLAN: 10 (ENGINEERING)
Trunking Native Mode VLAN: 1 (default)
```

### Step 13: Troubleshooting Scenarios

Work through each scenario and document your analysis.

Scenario A: After completing all configuration, `show interfaces trunk` on SW1 shows no trunk ports at all, even though Gi0/1 is cabled to SW2. What are two likely causes?

Expected answers: SW2's Gi0/1 is not configured as a trunk (it may still be in `dynamic auto` mode waiting for the other side), or the cable between the switches is not connected to the correct ports.

Scenario B: PC1 (VLAN 10 on SW1) can ping PC2 (VLAN 10 on SW1) but cannot ping PC4 (VLAN 10 on SW2). The trunk shows as active. What should you check?

Expected answer: Verify that VLAN 10 exists in the VLAN database on SW2 (`show vlan brief` on SW2). If VLAN 10 was only created on SW1, the trunk will carry the VLAN 10 tag but SW2 will not recognize it and will drop the frame.

Scenario C: The `show vlan brief` output on SW1 shows Fa0/1 under VLAN 1 instead of VLAN 10. You are sure you entered the correct commands. What is a possible explanation?

Expected answer: The `switchport access vlan 10` command was entered before `switchport mode access`. Verify the current interface mode with `show interfaces Fa0/1 switchport`. Re-enter `switchport mode access` then `switchport access vlan 10`.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show vlan brief` from SW1 confirming correct VLAN assignments
2. Screenshot of `show vlan brief` from SW2 confirming correct VLAN assignments
3. Screenshot of `show interfaces trunk` from SW1 showing the trunk with native VLAN 99
4. Screenshot of successful ping from PC1 to PC4 (same VLAN, different switches)
5. Screenshot of failed ping from PC1 to PC5 (different VLANs) with a one-sentence explanation of why the failure is expected
6. Screenshot of `show interfaces FastEthernet0/1 switchport` from SW1
7. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| SW1 VLAN Verification | 15 | Correct VLAN names and port assignments visible in show vlan brief |
| SW2 VLAN Verification | 15 | Same VLAN database exists on SW2 |
| Trunk Verification | 20 | Trunk is active, native VLAN is 99, VLANs 10/20/30 are allowed and active |
| Intra-VLAN Ping (PC1 to PC4) | 15 | Successful ping with output screenshot |
| Inter-VLAN Ping Failure | 10 | Failed ping shown with correct explanation |
| Single Port Switchport Detail | 10 | show interfaces switchport output captured and shows access mode in VLAN 10 |
| Troubleshooting Scenarios | 15 | Correct analysis for all three scenarios (5 pts each) |

Partial credit awarded for demonstrably attempted but incomplete work.
