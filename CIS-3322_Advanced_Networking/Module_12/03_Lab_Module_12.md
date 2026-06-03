# Lab Activity: Module 12 — WAN Technologies and Remote Access

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Tool: Cisco Packet Tracer 8.x

## Estimated Time: 60–75 minutes

## Total Points: 100

---

## Overview

In this lab you will configure a GRE tunnel between two branch routers over a simulated internet connection, run OSPF across the tunnel to exchange LAN routes, verify tunnel state and OSPF neighbor relationships, and test end-to-end LAN-to-LAN connectivity. You will also work through two troubleshooting scenarios targeting the most common GRE tunnel failures. This lab maps directly to CCNA 200-301 WAN connectivity and GRE tunnel configuration objectives.

---

## Objectives

By completing this lab you will be able to:

- Configure GRE tunnel interfaces with correct source, destination, and tunnel IP addresses
- Verify GRE tunnel state using `show interface Tunnel0`
- Run OSPFv2 over a GRE tunnel to distribute LAN routes
- Verify OSPF neighbor relationships using `show ip ospf neighbor`
- Confirm end-to-end host connectivity across the GRE tunnel
- Diagnose and repair two common GRE tunnel failures

---

## Equipment List

- 3x Cisco 1941 Routers (R1, ISP, R2)
- 2x Cisco Catalyst 2960-24TT Switches (SW1, SW2)
- 4x End-user PCs (PC-A, PC-B at Site 1; PC-C, PC-D at Site 2)
- Straight-through Ethernet cables for LAN connections
- Serial or Ethernet cables for WAN connections

---

## Topology Description

```text
Site 1 LAN                                          Site 2 LAN
192.168.1.0/24                                      192.168.2.0/24
PC-A (192.168.1.10)  R1 Gi0/1 (203.0.113.1/30)    R2 Gi0/1 (203.0.114.2/30) PC-C (192.168.2.10)
PC-B (192.168.1.20)--R1--Se0/0/0--ISP--Se0/0/1--R2--                         PC-D (192.168.2.20)
       |                |                     |                      |
      SW1           Tunnel0               Tunnel0                   SW2
                   172.16.0.1/30         172.16.0.2/30
                   (GRE overlay)
```

---

## IP Address Table

| Device | Interface    | IP Address      | Subnet Mask     | Notes               |
|--------|--------------|-----------------|-----------------|---------------------|
| R1     | Gi0/0        | 192.168.1.1     | 255.255.255.0   | Site 1 LAN          |
| R1     | Se0/0/0      | 203.0.113.1     | 255.255.255.252 | WAN to ISP (DCE)    |
| R1     | Tunnel0      | 172.16.0.1      | 255.255.255.252 | GRE tunnel          |
| ISP    | Se0/0/0      | 203.0.113.2     | 255.255.255.252 | WAN to R1           |
| ISP    | Se0/0/1      | 203.0.114.1     | 255.255.255.252 | WAN to R2           |
| R2     | Gi0/0        | 192.168.2.1     | 255.255.255.0   | Site 2 LAN          |
| R2     | Se0/0/1      | 203.0.114.2     | 255.255.255.252 | WAN to ISP          |
| R2     | Tunnel0      | 172.16.0.2      | 255.255.255.252 | GRE tunnel          |
| PC-A   | NIC          | 192.168.1.10    | 255.255.255.0   | GW 192.168.1.1      |
| PC-B   | NIC          | 192.168.1.20    | 255.255.255.0   | GW 192.168.1.1      |
| PC-C   | NIC          | 192.168.2.10    | 255.255.255.0   | GW 192.168.2.1      |
| PC-D   | NIC          | 192.168.2.20    | 255.255.255.0   | GW 192.168.2.1      |

---

## Part 1: Baseline WAN Configuration

### Step 1: Configure Hostnames and Physical Interfaces

Configure all three routers with hostnames. Apply all interface IP addresses from the IP address table. Add clock rate on DCE serial interfaces:

```text
R1(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface Serial0/0/0
R1(config-if)# ip address 203.0.113.1 255.255.255.252
R1(config-if)# clock rate 128000
R1(config-if)# no shutdown
```

Configure ISP with both serial interfaces. Configure R2 with Gi0/0 and Se0/0/1.

### Step 2: Configure Static Routes for WAN Reachability

R1 needs a route to reach R2's WAN address (required for the GRE tunnel destination):

```text
R1(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

R2 needs a route to reach R1's WAN address:

```text
R2(config)# ip route 0.0.0.0 0.0.0.0 203.0.114.1
```

ISP already has both WAN subnets as directly connected networks.

### Step 3: Verify WAN Reachability

From R1, ping R2's WAN interface:

```text
R1# ping 203.0.114.2
```

Expected result: 5 successful replies. If this fails, do not proceed — GRE tunnel establishment requires WAN reachability first.

---

## Part 2: GRE Tunnel Configuration

### Step 4: Configure GRE Tunnel on R1

```text
R1(config)# interface Tunnel0
R1(config-if)# tunnel mode gre ip
R1(config-if)# tunnel source Serial0/0/0
R1(config-if)# tunnel destination 203.0.114.2
R1(config-if)# ip address 172.16.0.1 255.255.255.252
R1(config-if)# no shutdown
R1(config-if)# exit
```

### Step 5: Configure GRE Tunnel on R2

```text
R2(config)# interface Tunnel0
R2(config-if)# tunnel mode gre ip
R2(config-if)# tunnel source Serial0/0/1
R2(config-if)# tunnel destination 203.0.113.1
R2(config-if)# ip address 172.16.0.2 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# exit
```

### Step 6: Verify Tunnel State

```text
R1# show interface Tunnel0
R1# show ip interface brief
```

Expected output:

```text
Tunnel0         172.16.0.1   YES manual   up   up
```

The tunnel must show `up/up`. If it shows `up/down`, the route to the tunnel destination is missing or incorrect. Verify with `show ip route 203.0.114.2`.

### Step 7: Ping Across the Tunnel

```text
R1# ping 172.16.0.2
```

Expected result: 5 successful replies confirming GRE forwarding is working end to end.

---

## Part 3: OSPF Across the GRE Tunnel

### Step 8: Configure OSPF on R1

Include the LAN subnet and the tunnel subnet. Mark the LAN interface passive:

```text
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
R1(config-router)# network 172.16.0.0 0.0.0.3 area 0
R1(config-router)# passive-interface GigabitEthernet0/0
R1(config-router)# exit
```

### Step 9: Configure OSPF on R2

```text
R2(config)# router ospf 1
R2(config-router)# router-id 2.2.2.2
R2(config-router)# network 192.168.2.0 0.0.0.255 area 0
R2(config-router)# network 172.16.0.0 0.0.0.3 area 0
R2(config-router)# passive-interface GigabitEthernet0/0
R2(config-router)# exit
```

### Step 10: Verify OSPF Neighbor Relationship

```text
R1# show ip ospf neighbor
```

Expected output showing R2 as a neighbor via Tunnel0 in the FULL state:

```text
Neighbor ID    Pri  State    Dead Time  Address      Interface
2.2.2.2         1   FULL/DR  00:00:34   172.16.0.2   Tunnel0
```

### Step 11: Verify OSPF Routes in Routing Table

```text
R1# show ip route ospf
```

Expected: an OSPF route to 192.168.2.0/24 via 172.16.0.2 (the tunnel). R2 should show a symmetric OSPF route to 192.168.1.0/24.

### Step 12: Test End-to-End LAN Connectivity

From PC-A, ping PC-C at the remote site:

```text
PC-A> ping 192.168.2.10
```

Expected result: 5 successful replies. This confirms GRE tunnel forwarding, OSPF route distribution, and host connectivity are all working correctly.

---

## Part 4: Troubleshooting Scenarios

### Troubleshooting Scenario A — Missing Route to Tunnel Destination

Remove R1's default route and observe the tunnel state:

```text
R1(config)# no ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

Run `show interface Tunnel0` on R1.

Expected result: Tunnel0 shows `up/down`. The line protocol drops because R1 can no longer route packets to 203.0.114.2 (the tunnel destination).

Written question: Explain precisely why the GRE tunnel's line protocol drops when the route to the destination is removed. What specific mechanism causes the `down` state? Write the command to restore the route and confirm the tunnel returns to `up/up`.

Restore before continuing:

```text
R1(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

### Troubleshooting Scenario B — Tunnel Destination Mismatch

Modify R2's tunnel destination to an incorrect IP:

```text
R2(config)# interface Tunnel0
R2(config-if)# tunnel destination 203.0.113.9
```

Observe `show ip ospf neighbor` — the OSPF neighbor disappears. Observe `show interface Tunnel0` on both routers.

Written question: Explain why a tunnel destination mismatch causes the OSPF neighbor relationship to fail even though both tunnel interfaces show `up/up`. What is the router doing with GRE packets destined for 203.0.113.9? Describe the exact sequence of events that breaks the OSPF neighbor relationship.

Restore before submitting:

```text
R2(config)# interface Tunnel0
R2(config-if)# tunnel destination 203.0.113.1
```

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show interface Tunnel0` on R1 showing `up/up` (Step 6)
2. Screenshot of successful ping from R1 to 172.16.0.2 across the tunnel (Step 7)
3. Screenshot of `show ip ospf neighbor` showing R2 in FULL state via Tunnel0 (Step 10)
4. Screenshot of `show ip route ospf` on R1 showing the OSPF route to 192.168.2.0/24 (Step 11)
5. Screenshot of successful ping from PC-A to PC-C (Step 12)
6. Written answer for Troubleshooting Scenario A (4–6 sentences)
7. Written answer for Troubleshooting Scenario B (4–6 sentences)

---

## Grading Rubric

| Component                              | Points | Criteria                                                          |
|----------------------------------------|--------|-------------------------------------------------------------------|
| WAN baseline connectivity verified     | 10     | R1 can ping R2's WAN address before tunnel configuration          |
| GRE tunnel configured on both routers  | 20     | Correct source, destination, tunnel IP on both R1 and R2          |
| Tunnel shows up/up on both routers     | 15     | show interface Tunnel0 confirms up/up; ping across tunnel succeeds|
| OSPF neighbor formed via Tunnel0       | 20     | show ip ospf neighbor shows FULL state via Tunnel0                |
| End-to-end LAN connectivity            | 15     | Successful ping from PC-A to PC-C                                 |
| Troubleshooting Scenario A             | 10     | Correct explanation of missing route causing up/down state        |
| Troubleshooting Scenario B             | 10     | Correct explanation of destination mismatch and OSPF failure      |

Partial credit is awarded for demonstrably attempted but incomplete work.
