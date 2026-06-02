# Lab Activity: Module 03 - IPv6 Addressing and Configuration

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure IPv6 addressing on a two-router topology in Cisco Packet Tracer. You will assign static global unicast addresses, configure EUI-64 addressing on selected interfaces, enable IPv6 routing, add static routes, and verify full connectivity using IPv6 show commands and ping.

This lab maps to CCNA 200-301 exam objectives 1.9 (compare IPv6 address types) and 3.3 (configure and verify IPv6 static routing).

---

## Objectives

By completing this lab you will be able to:

- Enable IPv6 unicast routing on Cisco routers
- Configure static and EUI-64 IPv6 addresses on router interfaces
- Identify link-local addresses generated automatically on each interface
- Configure IPv6 static routes including a fully specified route with a link-local next-hop
- Verify IPv6 configuration using show commands
- Interpret the output of `show ipv6 neighbors` to confirm NDP operation

---

## Equipment List

Use the following devices in Packet Tracer:

- 2x Cisco 1941 routers (R1 and R2)
- 2x Cisco 2960 switches (SW-1 and SW-2)
- 2x PCs (PC-A and PC-B)
- Straight-through cables for LAN connections
- Serial DCE cable between R1 and R2

---

## Addressing Table

| Device | Interface | IPv6 Address | Prefix | Default Gateway |
|---|---|---|---|---|
| R1 | Gi0/0 | 2001:DB8:ACAD:1::1 | /64 | N/A |
| R1 | Se0/0/0 | 2001:DB8:ACAD:3::1 | /64 | N/A |
| R2 | Gi0/0 | 2001:DB8:ACAD:2::1 | /64 | N/A |
| R2 | Se0/0/0 | 2001:DB8:ACAD:3::2 | /64 | N/A |
| PC-A | NIC | 2001:DB8:ACAD:1::3 | /64 | 2001:DB8:ACAD:1::1 |
| PC-B | NIC | 2001:DB8:ACAD:2::3 | /64 | 2001:DB8:ACAD:2::1 |

---

## Part 1: Configuration

### Step 1: Build the Physical Topology

Place the devices in Packet Tracer and connect them:

- PC-A connects to SW-1, SW-1 connects to R1 Gi0/0
- PC-B connects to SW-2, SW-2 connects to R2 Gi0/0
- R1 Se0/0/0 connects to R2 Se0/0/0 (DCE cable, R1 is DCE)
- Label all devices according to the equipment list

### Step 2: Configure Hostnames

Set hostnames on both routers:

```ios
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# end
```

Repeat with hostname R2.

### Step 3: Enable IPv6 Routing

On both routers, enable IPv6 unicast routing before configuring any IPv6 addresses:

```ios
R1# configure terminal
R1(config)# ipv6 unicast-routing
R1(config)# end
```

Repeat on R2.

### Step 4: Configure IPv6 Addresses on R1

Assign static global unicast addresses to R1's interfaces:

```ios
R1# configure terminal
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ipv6 address 2001:DB8:ACAD:1::1/64
R1(config-if)# no shutdown
R1(config-if)# interface Serial0/0/0
R1(config-if)# ipv6 address 2001:DB8:ACAD:3::1/64
R1(config-if)# clock rate 64000
R1(config-if)# no shutdown
R1(config-if)# end
R1# write memory
```

### Step 5: Configure IPv6 Addresses on R2 Using EUI-64

Configure R2's LAN interface using EUI-64 address generation. Note: this means the interface ID will be derived from R2's MAC address rather than manually entered.

```ios
R2# configure terminal
R2(config)# interface GigabitEthernet0/0
R2(config-if)# ipv6 address 2001:DB8:ACAD:2::/64 eui-64
R2(config-if)# no shutdown
R2(config-if)# interface Serial0/0/0
R2(config-if)# ipv6 address 2001:DB8:ACAD:3::2/64
R2(config-if)# no shutdown
R2(config-if)# end
R2# write memory
```

After configuring the EUI-64 interface, run `show ipv6 interface Gi0/0` on R2 and record the full IPv6 address that was generated. You will use this in your deliverables to show the EUI-64 derivation.

### Step 6: Configure IPv6 Static Routes

On R1, add a static route to reach R2's LAN:

```ios
R1# configure terminal
R1(config)# ipv6 route 2001:DB8:ACAD:2::/64 2001:DB8:ACAD:3::2
R1(config)# end
```

On R2, add a static route to reach R1's LAN:

```ios
R2# configure terminal
R2(config)# ipv6 route 2001:DB8:ACAD:1::/64 2001:DB8:ACAD:3::1
R2(config)# end
```

### Step 7: Configure PC IPv6 Addresses

On PC-A, open Desktop > IP Configuration in Packet Tracer and enter:

- IPv6 Address: 2001:DB8:ACAD:1::3
- Prefix Length: 64
- Default Gateway: 2001:DB8:ACAD:1::1

On PC-B:

- IPv6 Address: 2001:DB8:ACAD:2::3
- Prefix Length: 64
- Default Gateway: 2001:DB8:ACAD:2::1

---

## Part 2: Verification and Troubleshooting

### Step 8: Verify IPv6 Interface Configuration

On both routers, check IPv6 interface status and addresses:

```ios
R1# show ipv6 interface brief
```

Expected output (R1):

```text
GigabitEthernet0/0      [up/up]
    FE80::1             (link-local, auto-generated)
    2001:DB8:ACAD:1::1
Serial0/0/0             [up/up]
    FE80::1
    2001:DB8:ACAD:3::1
```

Record both the global unicast and link-local addresses for each interface. Note that link-local addresses are automatically generated when IPv6 is configured — you did not manually configure them.

### Step 9: Verify the IPv6 Routing Table

```ios
R1# show ipv6 route
```

Expected output (abbreviated):

```text
C   2001:DB8:ACAD:1::/64 [0/0]
     via GigabitEthernet0/0, directly connected
C   2001:DB8:ACAD:3::/64 [0/0]
     via Serial0/0/0, directly connected
S   2001:DB8:ACAD:2::/64 [1/0]
     via 2001:DB8:ACAD:3::2
```

Confirm that the static route to the remote LAN appears with code S.

### Step 10: Test Connectivity

From R1, ping R2's serial interface:

```ios
R1# ping ipv6 2001:DB8:ACAD:3::2
```

From R1, ping R2's LAN interface using the EUI-64 address you recorded:

```ios
R1# ping ipv6 [R2-Gi0/0-full-address]
```

From PC-A, open the command prompt in Packet Tracer and ping PC-B:

```text
C:\> ping 2001:DB8:ACAD:2::3
```

### Step 11: View IPv6 Neighbor Cache

After successful pings, examine the NDP neighbor table:

```ios
R1# show ipv6 neighbors
```

Expected output format:

```text
IPv6 Address                    Age  Link-layer Addr  State  Interface
2001:DB8:ACAD:3::2             0    xxxx.xxxx.xxxx   REACH  Se0/0/0
FE80::2                        0    xxxx.xxxx.xxxx   REACH  Se0/0/0
```

Record the output. This table is built by the Neighbor Discovery Protocol and replaces the IPv4 ARP table.

### Step 12: Troubleshooting Scenarios

Work through each scenario and document your analysis.

Scenario A: After configuring both routers, `show ipv6 route` on R1 shows only the two directly connected subnets but not the static route to 2001:DB8:ACAD:2::/64. What are two possible causes?

Expected answers: The `ipv6 route` command was entered with an incorrect destination prefix or next-hop address, or the command was entered in interface config mode instead of global config mode.

Scenario B: PC-A can ping R1's Gi0/0 (2001:DB8:ACAD:1::1) but cannot ping PC-B (2001:DB8:ACAD:2::3). Which router should you check first and what command do you use?

Expected answer: Check R1 first because the packet from PC-A must traverse R1 before reaching R2. Run `show ipv6 route` on R1 to confirm the static route to 2001:DB8:ACAD:2::/64 exists and is correct.

Scenario C: A technician enters `ipv6 route ::/0 FE80::2` as a default route on R1. The command is accepted but traffic is not forwarded. What is missing?

Expected answer: When a link-local address is used as the next-hop for an IPv6 route, the exit interface must be specified. The correct command is `ipv6 route ::/0 Serial0/0/0 FE80::2`. Without the exit interface, IOS cannot determine which segment to send the packet toward.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show ipv6 interface brief` from R1
2. Screenshot of `show ipv6 interface brief` from R2 (showing the EUI-64 generated address on Gi0/0)
3. Manual EUI-64 calculation: show the step-by-step derivation of R2's Gi0/0 interface identifier from the MAC address (copy the MAC from the Packet Tracer device properties)
4. Screenshot of `show ipv6 route` from R1 showing all three entries (two connected, one static)
5. Screenshot of successful ping from PC-A to PC-B
6. Screenshot of `show ipv6 neighbors` from R1 after pings
7. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| Interface Verification Screenshots | 20 | R1 and R2 show correct addresses and Up/Up status (10 pts each) |
| EUI-64 Manual Calculation | 15 | All three steps shown correctly: split, FFFE insertion, bit 7 inversion |
| Routing Table Verification | 15 | R1 shows both connected and static routes correctly |
| End-to-End Ping (PC-A to PC-B) | 15 | Successful ping with output screenshot |
| Neighbor Cache Output | 10 | show ipv6 neighbors shows at least one REACH entry |
| Troubleshooting Scenarios | 25 | Correct diagnosis and resolution (A=8, B=8, C=9) |

Partial credit is awarded for demonstrably attempted but incomplete work.
