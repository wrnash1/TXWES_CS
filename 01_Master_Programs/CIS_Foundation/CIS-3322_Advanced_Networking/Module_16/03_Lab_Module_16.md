# Lab Activity: Module 16 — CCNA 200-301 Capstone Lab

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Lab Overview

This capstone lab integrates the major technologies from CIS-3322 into a single enterprise network scenario. You will configure a three-tier campus network with a remote branch site, implementing VLANs, inter-VLAN routing, OSPF, DHCP, NAT/PAT, port security, DHCP snooping, dynamic ARP inspection, and AAA. Each section maps to a CCNA 200-301 exam domain.

**Estimated Time:** 120 minutes

**Tool:** Cisco Packet Tracer 8.2 or later

---

## Topology Description

```text
Internet Cloud
      |
  Gi0/0 (10.10.10.2/30)
  [R-HQ — Edge Router]
  Gi0/1 (172.16.0.1/30)
      |
  Gi0/0 (172.16.0.2/30)
  [SW-CORE — Layer 3 Distribution]
  Gi0/1       Gi0/2       Gi0/3
    |            |            |
[SW-ACCESS-1] [SW-ACCESS-2] [WAN to Branch]
  Gi0/1-8     Gi0/1-8      Gi0/0 (10.20.20.1/30)
                                  |
                             [R-BRANCH]
                             Gi0/1 (192.168.50.1/24)
                                  |
                              [PC-BRANCH]

VLANs at Campus:
  VLAN 10: 192.168.10.0/24 (Sales)
  VLAN 20: 192.168.20.0/24 (Engineering)
  VLAN 30: 192.168.30.0/24 (Management)
  VLAN 99: 192.168.99.0/24 (Native/Management)
```

---

## Part 1: VLAN and Access Layer Configuration (Domain 2 — Network Access)

### Step 1.1 — Create VLANs on SW-ACCESS-1

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW-ACCESS-1
SW-ACCESS-1(config)# vlan 10
SW-ACCESS-1(config-vlan)# name SALES
SW-ACCESS-1(config-vlan)# exit
SW-ACCESS-1(config)# vlan 20
SW-ACCESS-1(config-vlan)# name ENGINEERING
SW-ACCESS-1(config-vlan)# exit
SW-ACCESS-1(config)# vlan 30
SW-ACCESS-1(config-vlan)# name MANAGEMENT
SW-ACCESS-1(config-vlan)# exit
SW-ACCESS-1(config)# vlan 99
SW-ACCESS-1(config-vlan)# name NATIVE
SW-ACCESS-1(config-vlan)# exit
```

### Step 1.2 — Configure Access Ports on SW-ACCESS-1

```ios
SW-ACCESS-1(config)# interface range gigabitethernet 0/1 - 3
SW-ACCESS-1(config-if-range)# switchport mode access
SW-ACCESS-1(config-if-range)# switchport access vlan 10
SW-ACCESS-1(config-if-range)# exit
SW-ACCESS-1(config)# interface range gigabitethernet 0/4 - 6
SW-ACCESS-1(config-if-range)# switchport mode access
SW-ACCESS-1(config-if-range)# switchport access vlan 20
SW-ACCESS-1(config-if-range)# exit
```

### Step 1.3 — Configure Trunk to SW-CORE

```ios
SW-ACCESS-1(config)# interface gigabitethernet 0/24
SW-ACCESS-1(config-if)# switchport mode trunk
SW-ACCESS-1(config-if)# switchport trunk allowed vlan 10,20,30,99
SW-ACCESS-1(config-if)# switchport trunk native vlan 99
SW-ACCESS-1(config-if)# exit
```

### Step 1.4 — Configure Port Security on Access Ports

```ios
SW-ACCESS-1(config)# interface range gigabitethernet 0/1 - 6
SW-ACCESS-1(config-if-range)# switchport port-security
SW-ACCESS-1(config-if-range)# switchport port-security maximum 1
SW-ACCESS-1(config-if-range)# switchport port-security mac-address sticky
SW-ACCESS-1(config-if-range)# switchport port-security violation restrict
SW-ACCESS-1(config-if-range)# exit
```

Repeat Steps 1.1–1.4 for SW-ACCESS-2 using the same VLAN structure.

Verification:

```ios
SW-ACCESS-1# show vlan brief
SW-ACCESS-1# show interfaces trunk
SW-ACCESS-1# show port-security
```

---

## Part 2: Distribution Layer and Inter-VLAN Routing (Domain 3 — IP Connectivity)

### Step 2.1 — Configure SVIs on SW-CORE

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW-CORE
SW-CORE(config)# ip routing
SW-CORE(config)# vlan 10
SW-CORE(config-vlan)# name SALES
SW-CORE(config-vlan)# exit
SW-CORE(config)# vlan 20
SW-CORE(config-vlan)# name ENGINEERING
SW-CORE(config-vlan)# exit
SW-CORE(config)# vlan 30
SW-CORE(config-vlan)# name MANAGEMENT
SW-CORE(config-vlan)# exit
SW-CORE(config)# interface vlan 10
SW-CORE(config-if)# ip address 192.168.10.1 255.255.255.0
SW-CORE(config-if)# no shutdown
SW-CORE(config-if)# exit
SW-CORE(config)# interface vlan 20
SW-CORE(config-if)# ip address 192.168.20.1 255.255.255.0
SW-CORE(config-if)# no shutdown
SW-CORE(config-if)# exit
SW-CORE(config)# interface vlan 30
SW-CORE(config-if)# ip address 192.168.30.1 255.255.255.0
SW-CORE(config-if)# no shutdown
SW-CORE(config-if)# exit
SW-CORE(config)# interface gigabitethernet 0/0
SW-CORE(config-if)# no switchport
SW-CORE(config-if)# ip address 172.16.0.2 255.255.255.252
SW-CORE(config-if)# no shutdown
SW-CORE(config-if)# exit
```

Verification:

```ios
SW-CORE# show ip interface brief
SW-CORE# show ip route
```

---

## Part 3: OSPF Configuration (Domain 3 — IP Connectivity)

### Step 3.1 — Configure OSPF on SW-CORE

```ios
SW-CORE(config)# router ospf 1
SW-CORE(config-router)# router-id 2.2.2.2
SW-CORE(config-router)# network 192.168.10.0 0.0.0.255 area 0
SW-CORE(config-router)# network 192.168.20.0 0.0.0.255 area 0
SW-CORE(config-router)# network 192.168.30.0 0.0.0.255 area 0
SW-CORE(config-router)# network 172.16.0.0 0.0.0.3 area 0
SW-CORE(config-router)# exit
```

### Step 3.2 — Configure OSPF on R-HQ

```ios
Router> enable
Router# configure terminal
Router(config)# hostname R-HQ
R-HQ(config)# interface gigabitethernet 0/0
R-HQ(config-if)# ip address 10.10.10.2 255.255.255.252
R-HQ(config-if)# ip nat outside
R-HQ(config-if)# no shutdown
R-HQ(config-if)# exit
R-HQ(config)# interface gigabitethernet 0/1
R-HQ(config-if)# ip address 172.16.0.1 255.255.255.252
R-HQ(config-if)# ip nat inside
R-HQ(config-if)# no shutdown
R-HQ(config-if)# exit
R-HQ(config)# router ospf 1
R-HQ(config-router)# router-id 1.1.1.1
R-HQ(config-router)# network 172.16.0.0 0.0.0.3 area 0
R-HQ(config-router)# default-information originate
R-HQ(config-router)# exit
R-HQ(config)# ip route 0.0.0.0 0.0.0.0 10.10.10.1
```

Verification:

```ios
R-HQ# show ip ospf neighbor
R-HQ# show ip route ospf
SW-CORE# show ip ospf neighbor
```

Record: Is the OSPF neighbor state between R-HQ and SW-CORE showing FULL? ______

---

## Part 4: DHCP Configuration (Domain 4 — IP Services)

### Step 4.1 — Configure DHCP on SW-CORE

```ios
SW-CORE(config)# ip dhcp excluded-address 192.168.10.1 192.168.10.10
SW-CORE(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.10
SW-CORE(config)# ip dhcp excluded-address 192.168.30.1 192.168.30.10
SW-CORE(config)# ip dhcp pool SALES-POOL
SW-CORE(dhcp-config)# network 192.168.10.0 255.255.255.0
SW-CORE(dhcp-config)# default-router 192.168.10.1
SW-CORE(dhcp-config)# dns-server 8.8.8.8
SW-CORE(dhcp-config)# exit
SW-CORE(config)# ip dhcp pool ENG-POOL
SW-CORE(dhcp-config)# network 192.168.20.0 255.255.255.0
SW-CORE(dhcp-config)# default-router 192.168.20.1
SW-CORE(dhcp-config)# dns-server 8.8.8.8
SW-CORE(dhcp-config)# exit
```

Verification:

```ios
SW-CORE# show ip dhcp binding
SW-CORE# show ip dhcp pool
```

---

## Part 5: NAT/PAT Configuration (Domain 4 — IP Services)

### Step 5.1 — Configure PAT on R-HQ

```ios
R-HQ(config)# ip access-list standard NAT-ACL
R-HQ(config-std-nacl)# permit 192.168.0.0 0.0.255.255
R-HQ(config-std-nacl)# exit
R-HQ(config)# ip nat inside source list NAT-ACL interface gigabitethernet 0/0 overload
```

Verification:

```ios
R-HQ# show ip nat translations
R-HQ# show ip nat statistics
```

From a VLAN 10 PC, ping 8.8.8.8 (simulated Internet). After the ping, check:

```ios
R-HQ# show ip nat translations
```

Record the inside local and inside global addresses shown for the ICMP translation: ______

---

## Part 6: DHCP Snooping and Dynamic ARP Inspection (Domain 5 — Security Fundamentals)

### Step 6.1 — Enable DHCP Snooping on SW-ACCESS-1

```ios
SW-ACCESS-1(config)# ip dhcp snooping
SW-ACCESS-1(config)# ip dhcp snooping vlan 10,20,30
SW-ACCESS-1(config)# no ip dhcp snooping information option
SW-ACCESS-1(config)# interface gigabitethernet 0/24
SW-ACCESS-1(config-if)# ip dhcp snooping trust
SW-ACCESS-1(config-if)# exit
SW-ACCESS-1(config)# interface range gigabitethernet 0/1 - 6
SW-ACCESS-1(config-if-range)# ip dhcp snooping limit rate 15
SW-ACCESS-1(config-if-range)# exit
```

### Step 6.2 — Enable DAI on SW-ACCESS-1

```ios
SW-ACCESS-1(config)# ip arp inspection vlan 10,20,30
SW-ACCESS-1(config)# interface gigabitethernet 0/24
SW-ACCESS-1(config-if)# ip arp inspection trust
SW-ACCESS-1(config-if)# exit
```

Verification:

```ios
SW-ACCESS-1# show ip dhcp snooping binding
SW-ACCESS-1# show ip arp inspection
```

---

## Part 7: AAA Configuration (Domain 5 — Security Fundamentals)

### Step 7.1 — Configure AAA on SW-CORE

```ios
SW-CORE(config)# aaa new-model
SW-CORE(config)# username admin privilege 15 secret Admin@Cap1
SW-CORE(config)# aaa authentication login default local
SW-CORE(config)# aaa authorization exec default local
SW-CORE(config)# line vty 0 15
SW-CORE(config-line)# login authentication default
SW-CORE(config-line)# transport input ssh
SW-CORE(config-line)# exit
SW-CORE(config)# ip domain-name txwes.lab
SW-CORE(config)# crypto key generate rsa modulus 2048
SW-CORE(config)# ip ssh version 2
```

Verification:

```ios
SW-CORE# show aaa servers
SW-CORE# show running-config | include aaa
```

---

## Part 8: Branch Site Configuration (Domain 3 — IP Connectivity)

### Step 8.1 — Configure R-BRANCH

```ios
Router> enable
Router# configure terminal
Router(config)# hostname R-BRANCH
R-BRANCH(config)# interface gigabitethernet 0/0
R-BRANCH(config-if)# ip address 10.20.20.2 255.255.255.252
R-BRANCH(config-if)# no shutdown
R-BRANCH(config-if)# exit
R-BRANCH(config)# interface gigabitethernet 0/1
R-BRANCH(config-if)# ip address 192.168.50.1 255.255.255.0
R-BRANCH(config-if)# no shutdown
R-BRANCH(config-if)# exit
R-BRANCH(config)# router ospf 1
R-BRANCH(config-router)# router-id 3.3.3.3
R-BRANCH(config-router)# network 10.20.20.0 0.0.0.3 area 0
R-BRANCH(config-router)# network 192.168.50.0 0.0.0.255 area 0
R-BRANCH(config-router)# exit
```

Also configure SW-CORE with the WAN link to R-BRANCH:

```ios
SW-CORE(config)# interface gigabitethernet 0/3
SW-CORE(config-if)# no switchport
SW-CORE(config-if)# ip address 10.20.20.1 255.255.255.252
SW-CORE(config-if)# no shutdown
SW-CORE(config-if)# exit
SW-CORE(config)# router ospf 1
SW-CORE(config-router)# network 10.20.20.0 0.0.0.3 area 0
SW-CORE(config-router)# exit
```

Verification — from a VLAN 10 PC, ping 192.168.50.1 (branch default gateway):

```ios
SW-CORE# show ip ospf neighbor
SW-CORE# show ip route
```

Record: Is the branch network 192.168.50.0/24 visible in SW-CORE's routing table via OSPF? ______

---

## Part 9: Save All Configurations

```ios
R-HQ# copy running-config startup-config
SW-CORE# copy running-config startup-config
SW-ACCESS-1# copy running-config startup-config
SW-ACCESS-2# copy running-config startup-config
R-BRANCH# copy running-config startup-config
```

---

## Capstone Lab Rubric

| Section | Points | Criteria |
|---|---|---|
| Part 1: VLANs, trunking, port security | 15 | VLANs created and assigned; trunk configured; sticky port security active |
| Part 2: Inter-VLAN routing (SVIs) | 15 | All SVIs addressed; ip routing enabled; VLAN-to-VLAN ping succeeds |
| Part 3: OSPF configured and converged | 20 | OSPF neighbor Full on R-HQ and SW-CORE; routes redistributed |
| Part 4: DHCP pools configured | 10 | Clients receive addresses from correct pools |
| Part 5: PAT operational | 10 | NAT translations visible; Internet ping succeeds |
| Part 6: DHCP snooping and DAI enabled | 10 | Snooping on correct VLANs; uplink trusted; DAI enabled |
| Part 7: AAA and SSH configured | 10 | `aaa new-model` present; SSH v2 enabled; local auth functional |
| Part 8: Branch OSPF connectivity | 10 | Branch routes visible in campus routing table |
| **Total** | **100** | |

---

## Submission Instructions

Submit through the course LMS:

1. Completed Packet Tracer .pka file
2. Screenshots of: OSPF neighbor table, routing table showing all prefixes, NAT translation table, DHCP binding table, and port security output
3. A 200-word reflection describing which part of the capstone was most challenging and why

---

## Part 9 — Challenge Extension

This optional extension adds exam-difficulty scenarios to the capstone lab. Complete all steps for up to 20 bonus points.

### Challenge Step 1: Implement IPv6 Dual-Stack on the Campus Topology

Add IPv6 addressing to the existing IPv4 campus topology. Configure dual-stack (simultaneous IPv4 and IPv6) on SW-CORE and R-HQ using the 2001:DB8:CCNA::/48 prefix space.

```ios
SW-CORE(config)# ipv6 unicast-routing

SW-CORE(config)# interface vlan 10
SW-CORE(config-if)# ipv6 address 2001:DB8:CCNA:10::1/64
SW-CORE(config-if)# ipv6 ospf 1 area 0

SW-CORE(config)# interface vlan 20
SW-CORE(config-if)# ipv6 address 2001:DB8:CCNA:20::1/64
SW-CORE(config-if)# ipv6 ospf 1 area 0

SW-CORE(config)# ipv6 router ospf 1
SW-CORE(config-rtr)# router-id 1.1.1.1
```

Configure PC clients to use SLAAC for IPv6 address assignment (Packet Tracer: set to DHCP6/SLAAC on the PC). Verify IPv6 reachability with `ping 2001:DB8:CCNA:20::11` from a VLAN 10 host. Use `show ipv6 route` and `show ipv6 ospf neighbor` on SW-CORE to verify OSPFv3 operation. Document the auto-configured PC IPv6 addresses and confirm they use the correct /64 prefix with an EUI-64-derived interface identifier.

### Challenge Step 2: Add NAT64 Awareness — Analyze Legacy IPv4 Connectivity

Research and document the NAT64 transition mechanism. In a written analysis (300–400 words) address the following:

Using the existing campus topology as context, explain what changes would be required if the R-HQ PAT configuration (IPv4 internet access) needed to also provide outbound internet access for IPv6-only hosts on the campus network. Cover:

1. What is the role of NAT64 in this scenario and how does it differ from the existing IPv4 PAT?
2. What is DNS64 and why is it required alongside NAT64 for name resolution to work for IPv6-only clients?
3. What Cisco IOS commands would be used to configure a basic stateful NAT64 policy on R-HQ?
4. What are the limitations of NAT64 compared to a full dual-stack deployment?

Include at least two specific Cisco IOS NAT64 configuration commands in your answer (you do not need to implement them in Packet Tracer — this is a design analysis exercise).

### Challenge Step 3: Extend the Branch with SD-WAN Concepts Analysis

The R-BRANCH router currently connects to the campus via OSPF over a simulated WAN link. Write a technical design proposal (400–500 words) for migrating the branch WAN from the current point-to-point OSPF design to a Cisco SD-WAN architecture. Your proposal must address:

1. **Current limitations**: What are the specific operational limitations of the current single-link OSPF WAN design for the branch? Address reliability, visibility, and scalability.
2. **SD-WAN component roles**: Identify which Cisco SD-WAN components (vManage, vSmart, vBond, vEdge) would be deployed and where. Which component replaces R-BRANCH?
3. **Multi-transport design**: Describe how you would configure the branch with two WAN transports (existing WAN link + 4G LTE backup) and what SD-WAN capability ensures voice traffic always uses the better-quality link.
4. **Zero-touch provisioning**: Describe the sequence of events when a new vEdge router is shipped to a new branch and powered on for the first time. Which SD-WAN component does it contact first and what happens?
5. **Migration risk**: Identify one significant operational risk during migration from OSPF to SD-WAN and describe how you would mitigate it.

Attach your written proposal as a separate document in addition to the Packet Tracer file.

---

## Part 9 — Challenge Exercise

### Challenge 1: Tune OSPF for Faster Convergence and Summarize Branch Routes

Extend the OSPF deployment by adjusting hello/dead timers for faster failure detection and configuring manual route summarization on SW-CORE to reduce LSA flooding across the campus/branch boundary.

1. On SW-CORE and R-HQ, reduce the OSPF hello interval to 5 seconds and the dead interval to 15 seconds on the inter-router link (Gi0/0 on each device). Both ends must match or the adjacency will drop.

```ios
SW-CORE(config)# interface gigabitethernet 0/0
SW-CORE(config-if)# ip ospf hello-interval 5
SW-CORE(config-if)# ip ospf dead-interval 15

R-HQ(config)# interface gigabitethernet 0/1
R-HQ(config-if)# ip ospf hello-interval 5
R-HQ(config-if)# ip ospf dead-interval 15
```

1. On SW-CORE, configure an OSPF summary route to advertise the three campus VLANs (192.168.10.0, 192.168.20.0, 192.168.30.0) as a single aggregate toward R-HQ and R-BRANCH.

```ios
SW-CORE(config)# router ospf 1
SW-CORE(config-router)# summary-address 192.168.0.0 255.255.0.0
```

1. Verify that the adjacency re-establishes using the new timers and that R-HQ and R-BRANCH now see 192.168.0.0/16 instead of three individual /24 routes.

```ios
SW-CORE# show ip ospf neighbor
R-HQ# show ip route ospf
R-BRANCH# show ip route ospf
```

1. Record how many OSPF routes appear in R-BRANCH's routing table before and after summarization: Before: ______ After: ______

---

### Challenge 2: Implement a Named ACL to Restrict Inter-VLAN Traffic

Create a named extended ACL on SW-CORE that permits the Engineering VLAN (192.168.20.0/24) to reach all destinations but explicitly denies the Sales VLAN (192.168.10.0/24) from connecting to VLAN 30 Management hosts. All other traffic between VLANs should continue to flow.

1. Define the named extended ACL on SW-CORE.

```ios
SW-CORE(config)# ip access-list extended VLAN-POLICY
SW-CORE(config-ext-nacl)# deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255
SW-CORE(config-ext-nacl)# permit ip any any
SW-CORE(config-ext-nacl)# exit
```

1. Apply the ACL inbound on the VLAN 10 SVI so packets from Sales are filtered before being routed.

```ios
SW-CORE(config)# interface vlan 10
SW-CORE(config-if)# ip access-group VLAN-POLICY in
SW-CORE(config-if)# exit
```

1. Test the policy: from a VLAN 10 PC, attempt to ping a VLAN 30 address (e.g., 192.168.30.11) — the ping should fail. Then ping a VLAN 20 address (e.g., 192.168.20.11) — the ping should succeed.

```ios
SW-CORE# show ip access-lists VLAN-POLICY
```

1. Record the match count on the deny statement after testing: ______

---

### Reflection Questions

1. When you reduced the OSPF hello/dead timers, what is the trade-off between faster failure detection and network stability in a high-traffic campus environment? Under what conditions would the default 10/40-second timers still be preferable?
2. An enterprise security architect argues that inbound ACLs applied to SVIs are insufficient on their own to secure inter-VLAN traffic at scale. What additional security controls — such as 802.1X, private VLANs, or a next-generation firewall in the routing path — would a production campus network use alongside ACLs to enforce consistent segmentation policy?
