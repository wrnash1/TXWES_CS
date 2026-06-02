# Lab Activity: Module 02 - Subnetting and VLSM Configurations

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 75-90 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will design a VLSM address plan for a given network scenario, then implement and verify that plan on a multi-router topology in Cisco Packet Tracer. You will calculate subnets on paper before touching Packet Tracer, configure IP addressing on router interfaces, and verify full connectivity using Cisco IOS show commands and ping.

This lab maps directly to CCNA 200-301 exam objectives 1.6 (configure and verify IPv4 addressing and subnetting) and 1.7 (describe the need for private IPv4 addressing).

---

## Objectives

By completing this lab you will be able to:

- Perform VLSM design to allocate a /24 address space into correctly-sized subnets
- Configure IP addresses and subnet masks on Cisco router interfaces in Packet Tracer
- Use `no shutdown` to bring up router interfaces
- Verify interface addressing with `show ip interface brief`
- Test inter-subnet reachability with `ping`
- Identify and correct subnet mask misconfiguration errors

---

## Equipment List

Use the following devices in Packet Tracer:

- 2x Cisco 1941 routers (R1 and R2)
- 4x Cisco 2960 switches (SW-A, SW-B, SW-C, SW-D)
- 4x PCs (PC-A, PC-B, PC-C, PC-D)
- DCE serial cable between R1 and R2 (for the WAN link)
- Straight-through cables for all LAN connections

---

## Scenario

Your company has been assigned the address block 192.168.20.0/24. You must design a VLSM address plan for the following five network segments:

| Segment | Required Hosts | Connected To |
|---|---|---|
| LAN A | 60 | R1 Gi0/0 - SW-A |
| LAN B | 28 | R1 Gi0/1 - SW-B |
| LAN C | 12 | R2 Gi0/0 - SW-C |
| LAN D | 6 | R2 Gi0/1 - SW-D |
| WAN Link | 2 (point-to-point) | R1 Se0/0/0 - R2 Se0/0/0 |

---

## Part 1: VLSM Design (Paper Work Before Packet Tracer)

Complete this section on paper or in a separate document before opening Packet Tracer. Show your calculations clearly in your submission.

### Step 1: Determine the Correct Prefix for Each Segment

For each segment in the scenario table, identify the smallest subnet that satisfies the host requirement. Use the formula: usable hosts = 2^h - 2, and select the smallest h that satisfies the requirement.

Fill in the table:

| Segment | Hosts Required | Host Bits Needed | Prefix Length | Usable Hosts Provided |
|---|---|---|---|---|
| LAN A | 60 | ? | ? | ? |
| LAN B | 28 | ? | ? | ? |
| LAN C | 12 | ? | ? | ? |
| LAN D | 6 | ? | ? | ? |
| WAN Link | 2 | ? | ? | ? |

### Step 2: Allocate Subnets from 192.168.20.0/24

Allocate subnets in order from largest to smallest. Start each new subnet at the next available address after the previous subnet's broadcast address.

Complete the VLSM allocation table:

| Segment | Prefix | Network Address | First Usable | Last Usable | Broadcast |
|---|---|---|---|---|---|
| LAN A | /26 | 192.168.20.0 | .1 | ? | ? |
| LAN B | /27 | 192.168.20.64 | .65 | ? | ? |
| LAN C | /28 | 192.168.20.96 | .97 | ? | ? |
| LAN D | /29 | 192.168.20.112 | .113 | ? | ? |
| WAN Link | /30 | 192.168.20.120 | .121 | ? | ? |

The first row is completed as an example. Calculate all remaining rows. Show your block-size calculation for each row.

### Step 3: Assign Specific Interface Addresses

For each router interface, assign the first usable host address. For each PC, assign the second usable host address. Record these in your addressing plan — you will enter them in Packet Tracer in Part 2.

---

## Part 2: Packet Tracer Configuration

### Step 4: Build the Physical Topology

Open Packet Tracer and place devices according to the equipment list. Arrange the topology logically:

- R1 on the left with SW-A below Gi0/0 and SW-B below Gi0/1
- R2 on the right with SW-C below Gi0/0 and SW-D below Gi0/1
- A WAN serial cable connecting R1 Se0/0/0 to R2 Se0/0/0

### Step 5: Configure Hostnames and Passwords

On R1:

```ios
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# enable secret cisco123
R1(config)# line vty 0 4
R1(config-line)# password cisco123
R1(config-line)# login
R1(config-line)# exit
R1(config)# end
R1# write memory
```

Repeat with hostname R2 on the second router.

### Step 6: Configure LAN Interfaces on R1

Use the addresses from your Part 1 addressing plan:

```ios
R1# configure terminal
R1(config)# interface GigabitEthernet0/0
R1(config-if)# description LAN-A
R1(config-if)# ip address 192.168.20.1 255.255.255.192
R1(config-if)# no shutdown
R1(config-if)# interface GigabitEthernet0/1
R1(config-if)# description LAN-B
R1(config-if)# ip address 192.168.20.65 255.255.255.224
R1(config-if)# no shutdown
R1(config-if)# end
R1# write memory
```

### Step 7: Configure the WAN Interface on R1 (DCE Side)

```ios
R1# configure terminal
R1(config)# interface Serial0/0/0
R1(config-if)# description WAN-to-R2
R1(config-if)# ip address 192.168.20.121 255.255.255.252
R1(config-if)# clock rate 64000
R1(config-if)# no shutdown
R1(config-if)# end
R1# write memory
```

### Step 8: Configure LAN and WAN Interfaces on R2

```ios
R2# configure terminal
R2(config)# interface GigabitEthernet0/0
R2(config-if)# description LAN-C
R2(config-if)# ip address 192.168.20.97 255.255.255.240
R2(config-if)# no shutdown
R2(config-if)# interface GigabitEthernet0/1
R2(config-if)# description LAN-D
R2(config-if)# ip address 192.168.20.113 255.255.255.248
R2(config-if)# no shutdown
R2(config-if)# interface Serial0/0/0
R2(config-if)# description WAN-to-R1
R2(config-if)# ip address 192.168.20.122 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# end
R2# write memory
```

### Step 9: Add Static Routes for End-to-End Connectivity

Add static routes on each router so all subnets are reachable:

```ios
R1(config)# ip route 192.168.20.96 255.255.255.240 192.168.20.122
R1(config)# ip route 192.168.20.112 255.255.255.248 192.168.20.122

R2(config)# ip route 192.168.20.0 255.255.255.192 192.168.20.121
R2(config)# ip route 192.168.20.64 255.255.255.224 192.168.20.121
```

### Step 10: Configure PC IP Addresses

On each PC, set the IP address, subnet mask, and default gateway manually in Packet Tracer. Use the second usable address for each PC. Confirm that the default gateway matches the router interface address for that LAN.

---

## Part 2: Verification and Troubleshooting

### Step 11: Verify Interface Status

On both routers, verify all interfaces are up and correctly addressed:

```ios
R1# show ip interface brief
```

Expected output (R1):

```text
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0    192.168.20.1    YES manual up                    up
GigabitEthernet0/1    192.168.20.65   YES manual up                    up
Serial0/0/0           192.168.20.121  YES manual up                    up
```

If any interface shows "administratively down," re-enter that interface and apply `no shutdown`.

### Step 12: Verify Routing Table

```ios
R1# show ip route
```

Confirm that all five subnets appear in the routing table — two as directly connected (C) and the remaining three from static routes (S).

### Step 13: Test Connectivity with Ping

From R1, ping all remote interfaces:

```ios
R1# ping 192.168.20.122
R1# ping 192.168.20.97
R1# ping 192.168.20.113
```

From PC-A, open the Packet Tracer command prompt and ping PC-C (which is on R2's LAN C network):

```text
C:\> ping 192.168.20.98
```

A successful ping confirms full end-to-end connectivity through both routers.

### Step 14: Troubleshooting Scenarios

Work through each troubleshooting scenario and document your analysis.

Scenario A: PC-B cannot ping R1 Gi0/1 (192.168.20.65) even though the interface is up/up. What are the two most likely causes?

Expected causes: PC-B has an incorrect IP address or subnet mask configured, or the default gateway on PC-B is wrong. Verify with `ipconfig` on the PC.

Scenario B: R1 can ping 192.168.20.122 (R2 WAN IP) but cannot ping 192.168.20.97 (R2 LAN C). What does this indicate and what command do you run to diagnose it?

Expected analysis: R2's Gi0/0 may be administratively down, or the static route on R1 may be missing or incorrect. Run `show ip route` on R1 and `show ip interface brief` on R2.

Scenario C: A static route is configured as `ip route 192.168.20.96 255.255.255.192 192.168.20.122`. Will this route correctly reach LAN C (192.168.20.96/28)? Explain.

Expected answer: No. The mask should be 255.255.255.240 (/28), not 255.255.255.192 (/26). The /26 mask covers a larger range (192.168.20.64 - 192.168.20.127) and would route traffic incorrectly, potentially including LAN B addresses.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Your completed VLSM design table from Part 1 (Steps 1-3) showing all calculations
2. Screenshot of `show ip interface brief` from R1 (all interfaces Up/Up)
3. Screenshot of `show ip interface brief` from R2 (all interfaces Up/Up)
4. Screenshot of `show ip route` from R1 showing all five subnets
5. Screenshot of successful pings from R1 to all three R2 addresses
6. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| VLSM Design Table | 25 | All five segments have correct prefix, network address, host range, and broadcast (5 pts each) |
| R1 Interface Verification | 15 | All three R1 interfaces show Up/Up with correct addresses |
| R2 Interface Verification | 15 | All three R2 interfaces show Up/Up with correct addresses |
| Routing Table Verification | 15 | R1 routing table shows all five subnets (5 connected, static routes present) |
| Ping Connectivity | 15 | Successful pings from R1 to all three R2 addresses |
| Troubleshooting Scenarios | 15 | Correct analysis for each scenario (5 pts each) |

Partial credit is awarded for correctly completed sections even if later sections are incomplete.
