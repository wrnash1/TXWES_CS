# Lab Activity: Module 09 - WAN Technologies and VPNs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 4: IP Services / Domain 5: Security Fundamentals)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure a GRE tunnel between two routers over a simulated WAN connection in Cisco Packet Tracer. You will configure the underlying WAN routing, create the GRE tunnel interfaces, assign tunnel IP addresses, run OSPF across the tunnel to exchange LAN routes, and verify end-to-end connectivity between hosts at two sites. You will also troubleshoot two common GRE tunnel failures.

This lab maps to CCNA 200-301 exam objectives related to WAN connectivity concepts and GRE tunnel operation.

---

## Objectives

By completing this lab you will be able to:

- Configure WAN-facing interfaces with public IP addresses
- Create a GRE tunnel interface with correct source, destination, and tunnel IP address
- Run OSPFv2 across a GRE tunnel to exchange LAN routes
- Verify GRE tunnel state with `show interface Tunnel0`
- Verify end-to-end connectivity from LAN host to remote LAN host
- Diagnose and fix a tunnel `up/down` state caused by missing routes

---

## Equipment List

- 2x Cisco 1941 Routers (R1, R2)
- 1x Cisco 1941 Router (ISP) — simulates internet core
- 2x Cisco Catalyst 2960-24TT Switches (SW1, SW2)
- 2x PCs (PC-A, PC-B)
- Serial DCE/DTE cables for WAN connections
- Straight-through Ethernet cables for LAN connections

---

## Topology

```text
PC-A --Gi0/0-- R1 --Se0/0/0-- ISP --Se0/0/1-- R2 --Gi0/0-- PC-B
               |                                |
          Tunnel0 (logical overlay) -------Tunnel0
```

### IP Address Table

| Device | Interface | IP Address | Subnet Mask | Notes |
|---|---|---|---|---|
| R1 | Gi0/0 | 192.168.1.1 | 255.255.255.0 | LAN |
| R1 | Se0/0/0 | 203.0.113.1 | 255.255.255.252 | WAN to ISP (DCE) |
| R1 | Tunnel0 | 172.16.0.1 | 255.255.255.252 | GRE tunnel |
| ISP | Se0/0/0 | 203.0.113.2 | 255.255.255.252 | WAN to R1 |
| ISP | Se0/0/1 | 203.0.114.1 | 255.255.255.252 | WAN to R2 |
| R2 | Se0/0/1 | 203.0.114.2 | 255.255.255.252 | WAN to ISP |
| R2 | Gi0/0 | 192.168.2.1 | 255.255.255.0 | LAN |
| R2 | Tunnel0 | 172.16.0.2 | 255.255.255.252 | GRE tunnel |
| PC-A | NIC | 192.168.1.11 | 255.255.255.0 | GW 192.168.1.1 |
| PC-B | NIC | 192.168.2.11 | 255.255.255.0 | GW 192.168.2.1 |

---

## Part 1: WAN Routing Configuration

### Step 1: Configure Hostnames and Physical Interfaces

Set hostnames on R1, ISP, and R2. Configure all physical interface IP addresses from the IP address table. On DCE serial interfaces, add clock rate:

```ios
R1(config)# interface Serial0/0/0
R1(config-if)# ip address 203.0.113.1 255.255.255.252
R1(config-if)# clock rate 128000
R1(config-if)# no shutdown
```

### Step 2: Configure Static Routes for WAN Reachability

R1 needs a default route to the ISP, and a route to R2's WAN address:

```ios
R1(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

R2 needs a route to reach R1's WAN address:

```ios
R2(config)# ip route 0.0.0.0 0.0.0.0 203.0.114.1
```

ISP needs routes to both WAN subnets (already directly connected) and nothing else.

### Step 3: Verify WAN Reachability

From R1, ping R2's WAN interface:

```ios
R1# ping 203.0.114.2
```

All five pings should succeed. This confirms the underlying WAN routing is working — a prerequisite for the GRE tunnel to come up.

---

## Part 2: GRE Tunnel Configuration

### Step 4: Configure GRE Tunnel on R1

```ios
R1# configure terminal
R1(config)# interface Tunnel0
R1(config-if)# tunnel mode gre ip
R1(config-if)# tunnel source 203.0.113.1
R1(config-if)# tunnel destination 203.0.114.2
R1(config-if)# ip address 172.16.0.1 255.255.255.252
R1(config-if)# no shutdown
R1(config)# end
```

### Step 5: Configure GRE Tunnel on R2

```ios
R2# configure terminal
R2(config)# interface Tunnel0
R2(config-if)# tunnel mode gre ip
R2(config-if)# tunnel source 203.0.114.2
R2(config-if)# tunnel destination 203.0.113.1
R2(config-if)# ip address 172.16.0.2 255.255.255.252
R2(config-if)# no shutdown
R2(config)# end
```

### Step 6: Verify Tunnel State

```ios
R1# show interface Tunnel0
R1# show ip interface brief
```

Expected output:

```text
Tunnel0                    172.16.0.1      YES manual up       up
```

The tunnel should be `up/up`. If it shows `up/down`, verify that the static route to the tunnel destination exists and that the WAN ping in Step 3 was successful.

### Step 7: Ping Across the Tunnel

```ios
R1# ping 172.16.0.2
```

A successful ping confirms the GRE tunnel is forwarding traffic.

---

## Part 3: OSPF Across the GRE Tunnel

### Step 8: Configure OSPF on R1

Include both the LAN and the tunnel interface in OSPF:

```ios
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
R1(config-router)# network 172.16.0.0 0.0.0.3 area 0
R1(config-router)# passive-interface GigabitEthernet0/0
R1(config-router)# end
```

### Step 9: Configure OSPF on R2

```ios
R2(config)# router ospf 1
R2(config-router)# router-id 2.2.2.2
R2(config-router)# network 192.168.2.0 0.0.0.255 area 0
R2(config-router)# network 172.16.0.0 0.0.0.3 area 0
R2(config-router)# passive-interface GigabitEthernet0/0
R2(config-router)# end
```

### Step 10: Verify OSPF Neighbor and Routes

```ios
R1# show ip ospf neighbor
R1# show ip route ospf
```

Expected: R2 appears as an OSPF neighbor in Full state via Tunnel0. R1's routing table shows an OSPF route to 192.168.2.0/24.

### Step 11: Test End-to-End Connectivity

From PC-A, ping PC-B:

```text
PC-A> ping 192.168.2.11
```

Expected result: 5 successful replies.

---

## Part 4: Troubleshooting Scenarios

### Scenario A: Tunnel up/down State

Remove R1's default static route to the ISP:

```ios
R1(config)# no ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

Run `show interface Tunnel0`. The tunnel goes `up/down`. Explain why and fix it.

Expected answer: The GRE tunnel's `up/down` state means the line protocol is down. The tunnel line protocol comes up only when the router can route packets to the tunnel destination IP address. Without a route to 203.0.114.2, R1 cannot forward GRE-encapsulated packets, so the tunnel fails. Fix: restore the static route.

### Scenario B: Tunnel Source/Destination Mismatch

Change R2's tunnel destination to an incorrect IP (203.0.113.9):

```ios
R2(config)# interface Tunnel0
R2(config-if)# tunnel destination 203.0.113.9
```

Run `show ip ospf neighbor`. The OSPF neighbor disappears. Explain the cause and fix.

Expected answer: The tunnel destination on R2 no longer matches R1's WAN address. GRE packets from R2 are sent to a nonexistent address. R1 never receives GRE packets from R2, so the OSPF hello exchange fails. Fix: correct R2's tunnel destination back to 203.0.113.1.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show interface Tunnel0` on R1 showing `up/up`
2. Screenshot of `show ip ospf neighbor` on R1 showing R2 in FULL state via Tunnel0
3. Screenshot of `show ip route ospf` on R1 showing the OSPF-learned route to 192.168.2.0/24
4. Screenshot of successful ping from PC-A to PC-B
5. Written answers to Troubleshooting Scenarios A and B (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| WAN Routing Configuration | 15 | WAN interfaces up; static routes allowing R1-to-R2 WAN ping |
| GRE Tunnel Configuration | 25 | Tunnel0 up/up on both routers; correct source, destination, and tunnel IP |
| OSPF Across Tunnel | 20 | OSPF neighbor in FULL state via Tunnel0 on both routers |
| Routing Table Verification | 15 | OSPF routes present on both routers |
| End-to-End Connectivity | 10 | Successful ping from PC-A to PC-B |
| Troubleshooting Scenarios | 15 | Correct analysis for both scenarios (7-8 pts each) |

Partial credit awarded for demonstrably attempted but incomplete work.
