# Lab Activity: Module 08 - OSPFv2 Routing Concepts and Setup

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure single-area OSPFv2 on a three-router topology in Cisco Packet Tracer. You will assign Router IDs, advertise networks using both the `network` command and the `ip ospf` interface command, configure passive interfaces, and verify neighbor adjacency and routing tables. You will also troubleshoot a scenario where OSPF neighbors fail to form.

This lab maps to CCNA 200-301 exam objective 3.4 (configure and verify single-area OSPFv2).

---

## Objectives

By completing this lab you will be able to:

- Configure OSPFv2 with explicit Router IDs on multiple routers
- Use wildcard masks correctly in the OSPF `network` command
- Use the `ip ospf` interface command as an alternative to the network command
- Configure passive interfaces on LAN-facing ports
- Verify OSPF neighbor adjacency with `show ip ospf neighbor`
- Verify OSPF routes in the routing table with `show ip route`
- Identify and fix common OSPF neighbor formation failures

---

## Equipment List

- 3x Cisco 1941 Routers (R1, R2, R3)
- 3x Cisco Catalyst 2960-24TT Switches (SW1, SW2, SW3)
- 3x PCs (PC1, PC2, PC3)
- Serial DCE/DTE cables for WAN links
- Straight-through Ethernet cables for LAN connections

---

## Topology

```text
PC1 --Fa0/1-- SW1 --Gi0/0-- R1 --Se0/0/0-- R2 --Se0/0/1-- R3 --Gi0/0-- SW3 --Fa0/1-- PC3
                                                              |
                                                        Gi0/0 |
                                                           SW2 --Fa0/1-- PC2
```

### IP Address Table

| Device | Interface | IP Address | Subnet Mask | Notes |
|---|---|---|---|---|
| R1 | Gi0/0 | 192.168.1.1 | 255.255.255.0 | LAN segment |
| R1 | Se0/0/0 | 10.0.12.1 | 255.255.255.252 | WAN to R2 |
| R1 | Loopback0 | 1.1.1.1 | 255.255.255.255 | Router ID |
| R2 | Se0/0/0 | 10.0.12.2 | 255.255.255.252 | WAN to R1 |
| R2 | Gi0/0 | 192.168.2.1 | 255.255.255.0 | LAN segment |
| R2 | Se0/0/1 | 10.0.23.1 | 255.255.255.252 | WAN to R3 |
| R2 | Loopback0 | 2.2.2.2 | 255.255.255.255 | Router ID |
| R3 | Se0/0/1 | 10.0.23.2 | 255.255.255.252 | WAN to R2 |
| R3 | Gi0/0 | 192.168.3.1 | 255.255.255.0 | LAN segment |
| R3 | Loopback0 | 3.3.3.3 | 255.255.255.255 | Router ID |
| PC1 | NIC | 192.168.1.11 | 255.255.255.0 | GW 192.168.1.1 |
| PC2 | NIC | 192.168.2.11 | 255.255.255.0 | GW 192.168.2.1 |
| PC3 | NIC | 192.168.3.11 | 255.255.255.0 | GW 192.168.3.1 |

---

## Part 1: Basic Configuration

### Step 1: Configure Hostnames and Loopback Interfaces

Set hostnames on all three routers. Then configure loopback interfaces for use as Router IDs:

```ios
R1# configure terminal
R1(config)# hostname R1
R1(config)# interface Loopback0
R1(config-if)# ip address 1.1.1.1 255.255.255.255
R1(config-if)# end
```

Repeat for R2 (Loopback0: 2.2.2.2/32) and R3 (Loopback0: 3.3.3.3/32).

### Step 2: Configure Physical Interfaces

Configure IP addresses on all router interfaces. On serial interfaces, the DCE end requires a clock rate:

```ios
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown

R1(config)# interface Serial0/0/0
R1(config-if)# ip address 10.0.12.1 255.255.255.252
R1(config-if)# clock rate 128000
R1(config-if)# no shutdown
R1(config)# end
```

Configure all interfaces on R2 and R3 using the IP address table above.

---

## Part 2: OSPFv2 Configuration

### Step 3: Configure OSPF on R1 Using the Network Command

```ios
R1# configure terminal
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
R1(config-router)# network 10.0.12.0 0.0.0.3 area 0
R1(config-router)# passive-interface GigabitEthernet0/0
R1(config-router)# end
```

### Step 4: Configure OSPF on R2 Using the Interface Command

R2 uses the alternative `ip ospf` interface command instead of the `network` command:

```ios
R2# configure terminal
R2(config)# router ospf 1
R2(config-router)# router-id 2.2.2.2
R2(config-router)# passive-interface GigabitEthernet0/0
R2(config-router)# exit

R2(config)# interface Serial0/0/0
R2(config-if)# ip ospf 1 area 0

R2(config)# interface Serial0/0/1
R2(config-if)# ip ospf 1 area 0

R2(config)# interface GigabitEthernet0/0
R2(config-if)# ip ospf 1 area 0
R2(config)# end
```

### Step 5: Configure OSPF on R3

```ios
R3# configure terminal
R3(config)# router ospf 1
R3(config-router)# router-id 3.3.3.3
R3(config-router)# network 192.168.3.0 0.0.0.255 area 0
R3(config-router)# network 10.0.23.0 0.0.0.3 area 0
R3(config-router)# passive-interface GigabitEthernet0/0
R3(config-router)# end
```

---

## Part 3: Verification

### Step 6: Verify OSPF Neighbor Adjacency

```ios
R1# show ip ospf neighbor
R2# show ip ospf neighbor
```

Expected output on R2 (which has two neighbors):

```text
Neighbor ID   Pri   State        Dead Time   Address     Interface
1.1.1.1         0   FULL/  -     00:00:36    10.0.12.1   Serial0/0/0
3.3.3.3         0   FULL/  -     00:00:38    10.0.23.2   Serial0/0/1
```

Serial interfaces are point-to-point — no DR/BDR is elected, so the State column shows a dash. All neighbors should reach FULL state.

### Step 7: Verify OSPF Routes in the Routing Table

```ios
R1# show ip route ospf
```

Expected output on R1:

```text
O    192.168.2.0/24 [110/65] via 10.0.12.2, 00:01:05, Serial0/0/0
O    192.168.3.0/24 [110/129] via 10.0.12.2, 00:01:02, Serial0/0/0
O    10.0.23.0/30   [110/128] via 10.0.12.2, 00:01:02, Serial0/0/0
```

O-prefixed routes are OSPF-learned. Administrative distance 110 is the OSPF default.

### Step 8: Verify OSPF Interface Status

```ios
R1# show ip ospf interface brief
```

Confirm that Gi0/0 shows as passive and Serial0/0/0 shows as active.

### Step 9: Test End-to-End Connectivity

From PC1, ping PC2 and PC3. All pings should succeed.

---

## Part 4: Troubleshooting Scenarios

Work through each scenario and document your analysis.

### Scenario A: Neighbor Not Forming

Change R1's area on the Serial0/0/0 interface to area 1:

```ios
R1(config)# router ospf 1
R1(config-router)# no network 10.0.12.0 0.0.0.3 area 0
R1(config-router)# network 10.0.12.0 0.0.0.3 area 1
```

Run `show ip ospf neighbor` on R1 and observe that the R2 neighbor disappears. Explain why and correct the configuration.

Expected answer: R1 and R2 are now in different areas on their connecting interfaces. OSPF requires both ends of a link to be in the same area to form adjacency. Fix by returning R1's Serial0/0/0 network statement to area 0.

### Scenario B: Missing Routes

Remove the loopback network from R3's OSPF configuration and check R1's routing table.

Expected answer: R1 no longer has a route to 3.3.3.3/32. In a real network, loopbacks often represent management addresses or are used as Router IDs. They must be included in OSPF (or redistributed) to be reachable.

### Scenario C: Passive Interface on Wrong Interface

Configure R1 Gi0/0 as non-passive (remove `passive-interface GigabitEthernet0/0`), wait 30 seconds, and observe if any unexpected OSPF neighbors form on that interface.

Expected answer: Removing passive-interface from a LAN-facing port causes OSPF hellos to be sent out that interface. In a production network, sending OSPF hellos onto a segment with no OSPF neighbors wastes bandwidth and could allow a rogue device to inject false LSAs. Always configure passive-interface on LAN segments with no OSPF neighbors.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show ip ospf neighbor` on R2 showing both R1 and R3 in FULL state
2. Screenshot of `show ip route ospf` on R1 showing OSPF-learned routes to all remote networks
3. Screenshot of `show ip ospf interface brief` confirming passive interface on Gi0/0 of at least one router
4. Screenshot of successful ping from PC1 to PC3
5. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| OSPF Configuration (all three routers) | 30 | Router IDs set; correct network statements; passive interfaces configured |
| Neighbor Adjacency Verification | 20 | show ip ospf neighbor shows FULL state on all neighbor pairs |
| Routing Table Verification | 20 | show ip route ospf shows OSPF routes on all three routers |
| End-to-End Connectivity | 15 | Successful ping from PC1 to PC3 through OSPF-learned routes |
| Troubleshooting Scenarios | 15 | Correct analysis for all three scenarios (5 pts each) |

Partial credit awarded for demonstrably attempted but incomplete work.
