# Lab Activity: Module 06 - EtherChannel Link Aggregation

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure EtherChannel using both LACP and static methods on a multi-switch topology in Cisco Packet Tracer. You will bundle physical links into port-channel interfaces, configure trunking on the port-channels, verify bundle status, and observe the behavior of a configuration mismatch that causes a port to be suspended.

This lab maps to CCNA 200-301 exam objectives 2.3 (configure and verify EtherChannel - Layer 2 and Layer 3).

---

## Objectives

By completing this lab you will be able to:

- Configure LACP EtherChannel using active/passive modes
- Configure a static (on/on) EtherChannel
- Apply trunk configuration on a port-channel interface
- Interpret `show etherchannel summary` output and identify bundle status flags
- Deliberately introduce a configuration mismatch and observe the suspended port behavior
- Recover a suspended port by correcting the mismatch

---

## Equipment List

Use the following devices in Packet Tracer:

- 3x Cisco Catalyst 2960-24TT switches (SW1, SW2, SW3)
- 2x PCs (PC1 and PC2)
- Straight-through Ethernet cables for all connections

---

## Topology

Connect the following links:

- SW1 Gi0/1 to SW2 Gi0/1 (EtherChannel 1 - LACP)
- SW1 Gi0/2 to SW2 Gi0/2 (EtherChannel 1 - LACP, second member link)
- SW2 Fa0/23 to SW3 Fa0/23 (EtherChannel 2 - Static on/on)
- SW2 Fa0/24 to SW3 Fa0/24 (EtherChannel 2 - Static on/on, second member link)
- SW1 Fa0/1 to PC1
- SW3 Fa0/1 to PC2

---

## Part 1: LACP EtherChannel Configuration

### Step 1: Configure Hostnames

Set hostnames on all three switches.

### Step 2: Create VLANs on All Three Switches

Create VLANs 10 and 20 with names on SW1, SW2, and SW3:

```ios
SW1# configure terminal
SW1(config)# vlan 10
SW1(config-vlan)# name ENGINEERING
SW1(config-vlan)# vlan 20
SW1(config-vlan)# name SALES
SW1(config-vlan)# end
```

Repeat on SW2 and SW3.

### Step 3: Configure LACP EtherChannel on SW1

Set SW1's Gi0/1 and Gi0/2 to LACP active mode:

```ios
SW1# configure terminal
SW1(config)# interface range GigabitEthernet0/1 - 2
SW1(config-if-range)# channel-group 1 mode active
SW1(config-if-range)# end
```

### Step 4: Configure LACP EtherChannel on SW2 (LACP Passive)

Set SW2's Gi0/1 and Gi0/2 to LACP passive mode to verify that active + passive forms a channel:

```ios
SW2# configure terminal
SW2(config)# interface range GigabitEthernet0/1 - 2
SW2(config-if-range)# channel-group 1 mode passive
SW2(config-if-range)# end
```

### Step 5: Configure Port-Channel 1 as Trunk

Apply trunk configuration to the port-channel interface on both switches:

```ios
SW1# configure terminal
SW1(config)# interface port-channel 1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20
SW1(config-if)# end
SW1# write memory
```

Repeat on SW2 port-channel 1.

### Step 6: Verify LACP EtherChannel

```ios
SW1# show etherchannel summary
```

Expected output:

```text
Group  Port-channel  Protocol    Ports
------+-------------+-----------+--------------------------------
1      Po1(SU)         LACP      Gi0/1(P)  Gi0/2(P)
```

Confirm SU (Layer 2, in use) on the port-channel and P (bundled) on both member ports.

```ios
SW1# show interfaces port-channel 1
```

Confirm the port-channel is up/up.

---

## Part 2: Static EtherChannel Configuration

### Step 7: Configure Static EtherChannel Between SW2 and SW3

Set SW2's Fa0/23 and Fa0/24 to mode on:

```ios
SW2# configure terminal
SW2(config)# interface range FastEthernet0/23 - 24
SW2(config-if-range)# channel-group 2 mode on
SW2(config-if-range)# end
```

Set SW3's Fa0/23 and Fa0/24 to mode on:

```ios
SW3# configure terminal
SW3(config)# interface range FastEthernet0/23 - 24
SW3(config-if-range)# channel-group 2 mode on
SW3(config-if-range)# end
```

### Step 8: Configure Port-Channel 2 as Trunk

```ios
SW2# configure terminal
SW2(config)# interface port-channel 2
SW2(config-if)# switchport mode trunk
SW2(config-if)# switchport trunk allowed vlan 10,20
SW2(config-if)# end
```

Repeat on SW3 port-channel 2.

### Step 9: Verify Static EtherChannel

```ios
SW2# show etherchannel summary
```

Expected output for group 2:

```text
Group  Port-channel  Protocol    Ports
------+-------------+-----------+--------------------------------
2      Po2(SU)         -         Fa0/23(P)  Fa0/24(P)
```

Note the dash (-) in the Protocol column — this confirms static EtherChannel with no negotiation protocol.

---

## Part 3: Configuration Mismatch Demonstration

### Step 10: Introduce a Speed Mismatch (Observed Behavior)

In Packet Tracer, observe what happens when a native VLAN mismatch exists between the two ends of a port-channel trunk. Change SW3's port-channel 2 native VLAN:

```ios
SW3# configure terminal
SW3(config)# interface port-channel 2
SW3(config-if)# switchport trunk native vlan 99
SW3(config-if)# end
```

Now run `show etherchannel summary` on SW2 and look for suspended (s) ports. Also run `show interfaces trunk` to see the native VLAN mismatch warning.

### Step 11: Recover from Mismatch

Fix the mismatch by applying the same native VLAN to SW2:

```ios
SW2# configure terminal
SW2(config)# interface port-channel 2
SW2(config-if)# switchport trunk native vlan 99
SW2(config-if)# end
```

Or revert SW3 to the default native VLAN 1:

```ios
SW3# configure terminal
SW3(config)# interface port-channel 2
SW3(config-if)# no switchport trunk native vlan
SW3(config-if)# end
```

Verify recovery with `show etherchannel summary`.

---

## Part 4: Verification and Troubleshooting

### Step 12: Configure PC Addresses and Test Connectivity

Assign IP addresses to PC1 (192.168.10.11 /24, gateway 192.168.10.1) and PC2 (192.168.10.12 /24, gateway 192.168.10.1). Configure SW1 Fa0/1 and SW3 Fa0/1 as access ports in VLAN 10.

Ping from PC1 to PC2 to verify end-to-end connectivity through both EtherChannels.

### Step 13: Troubleshooting Scenarios

Work through each scenario and document your analysis.

Scenario A: An engineer configured SW1 Gi0/1-2 with LACP mode `passive` and SW2 Gi0/1-2 with LACP mode `passive`. After configuration, `show etherchannel summary` shows Po1 as `(D)` down. What is the cause and what is the minimal change needed to fix it?

Expected answer: Two LACP passive ports never form a channel. Both sides wait for the other to initiate. Change at least one side to `mode active`.

Scenario B: `show etherchannel summary` on SW2 shows Fa0/23(P) but Fa0/24(s) — one port is bundled and one is suspended. What are two parameters to check for a mismatch?

Expected answer: Verify the speed and duplex settings on Fa0/24 and confirm they match Fa0/23. Also check that Fa0/24 has the same channel-group number and mode as Fa0/23. Any mismatch in speed, duplex, VLAN settings, or channel-group membership causes suspension.

Scenario C: An engineer added port-channel 1 trunk configuration on SW1 but applied VLAN settings directly to Gi0/1 and Gi0/2 instead of port-channel 1. What problem will this cause, and what is the correct approach?

Expected answer: Configuration on individual member ports is overridden by the port-channel configuration. The VLAN settings applied to the physical ports may conflict with the port-channel or may not take effect. All VLAN and trunking configuration must be applied to the port-channel interface, not to member physical ports.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show etherchannel summary` from SW1 showing EtherChannel 1 as SU with both ports bundled (P)
2. Screenshot of `show etherchannel summary` from SW2 showing both EtherChannels (1 and 2)
3. Screenshot of `show etherchannel summary` during the mismatch (Step 10), showing a suspended port
4. Screenshot of `show etherchannel summary` after recovery (Step 11), showing all ports bundled
5. Screenshot of successful ping from PC1 to PC2
6. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| LACP EtherChannel Verification | 25 | SW1 shows EtherChannel 1 SU with both ports P; LACP protocol shown |
| Static EtherChannel Verification | 20 | SW2 shows EtherChannel 2 with static protocol (dash), both ports P |
| Mismatch Demonstration | 20 | Suspended port visible in show etherchannel summary during mismatch |
| Mismatch Recovery | 10 | All ports show P after correction |
| End-to-End Connectivity | 10 | Successful ping from PC1 to PC2 |
| Troubleshooting Scenarios | 15 | Correct analysis for all three scenarios (5 pts each) |

Partial credit awarded for demonstrably attempted but incomplete work.
