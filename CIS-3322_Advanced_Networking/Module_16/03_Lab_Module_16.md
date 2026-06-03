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
