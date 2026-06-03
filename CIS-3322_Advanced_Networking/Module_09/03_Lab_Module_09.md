# Lab Activity: Module 09 — Access Control Lists (ACLs)

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Tool: Cisco Packet Tracer 8.x

## Estimated Time: 60–75 minutes

## Total Points: 100

---

## Overview

In this lab you will build a multi-router topology in Packet Tracer, configure both standard and extended ACLs, apply them to the correct interfaces in the correct direction, and verify behavior using ping, Telnet, and show commands. You will also complete two troubleshooting scenarios involving incorrectly placed and incorrectly ordered ACL entries. This lab maps directly to CCNA 200-301 exam objectives for ACL configuration and verification.

---

## Objectives

By completing this lab you will be able to:

- Configure numbered standard ACLs to restrict access based on source address
- Configure named extended ACLs to filter by protocol and port
- Apply ACLs to router interfaces in the correct direction
- Restrict VTY access using `access-class`
- Verify ACL operation using `show access-lists` and `show ip interface`
- Diagnose and correct two common ACL misconfiguration scenarios

---

## Equipment List

- 3x Cisco 1941 Routers (R1, R2, R3)
- 3x Cisco Catalyst 2960-24TT Switches (SW1, SW2, SW3)
- 6x End-user PCs (PC-A, PC-B, PC-C, PC-D, PC-E, PC-F)
- 1x Server (SRV1) representing a web and Telnet server
- Straight-through Ethernet cables for all connections

---

## Topology Description

[SHOW TOPOLOGY: Three-router triangle. R1 connects to SW1 (LAN A: 192.168.1.0/24). R2 connects to SW2 (LAN B: 192.168.2.0/24). R3 connects to SW3 (LAN C: 192.168.3.0/24) and to SRV1. R1-R2 link: 10.0.12.0/30. R1-R3 link: 10.0.13.0/30. R2-R3 link: 10.0.23.0/30.]

```text
   LAN A                        LAN B
192.168.1.0/24               192.168.2.0/24
PC-A, PC-B                   PC-C, PC-D
    |                             |
   SW1                           SW2
    |                             |
   R1 ---10.0.12.0/30--- R2
    |                             |
   10.0.13.0/30          10.0.23.0/30
    |                             |
   R3 ------- SW3 --- SRV1
              |
           PC-E, PC-F
        192.168.3.0/24
            LAN C
```

---

## IP Address Table

| Device | Interface     | IP Address      | Subnet Mask     | Notes       |
|--------|---------------|-----------------|-----------------|-------------|
| R1     | Gi0/0         | 192.168.1.1     | 255.255.255.0   | LAN A gate  |
| R1     | Gi0/1         | 10.0.12.1       | 255.255.255.252 | R1 to R2    |
| R1     | Gi0/2         | 10.0.13.1       | 255.255.255.252 | R1 to R3    |
| R2     | Gi0/0         | 192.168.2.1     | 255.255.255.0   | LAN B gate  |
| R2     | Gi0/1         | 10.0.12.2       | 255.255.255.252 | R2 to R1    |
| R2     | Gi0/2         | 10.0.23.1       | 255.255.255.252 | R2 to R3    |
| R3     | Gi0/0         | 192.168.3.1     | 255.255.255.0   | LAN C gate  |
| R3     | Gi0/1         | 10.0.13.2       | 255.255.255.252 | R3 to R1    |
| R3     | Gi0/2         | 10.0.23.2       | 255.255.255.252 | R3 to R2    |
| SRV1   | NIC           | 192.168.3.100   | 255.255.255.0   | GW .3.1     |
| PC-A   | NIC           | 192.168.1.10    | 255.255.255.0   | GW .1.1     |
| PC-B   | NIC           | 192.168.1.20    | 255.255.255.0   | GW .1.1     |
| PC-C   | NIC           | 192.168.2.10    | 255.255.255.0   | GW .2.1     |
| PC-D   | NIC           | 192.168.2.20    | 255.255.255.0   | GW .2.1     |
| PC-E   | NIC           | 192.168.3.10    | 255.255.255.0   | GW .3.1     |
| PC-F   | NIC           | 192.168.3.20    | 255.255.255.0   | GW .3.1     |

---

## Part 1: Baseline Configuration

### Step 1: Configure Hostnames and Interfaces

Configure all interfaces on R1, R2, and R3 according to the IP address table. Enable each interface with `no shutdown`.

```text
R1(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface GigabitEthernet0/1
R1(config-if)# ip address 10.0.12.1 255.255.255.252
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface GigabitEthernet0/2
R1(config-if)# ip address 10.0.13.1 255.255.255.252
R1(config-if)# no shutdown
```

Repeat equivalent configuration for R2 and R3 using their respective addresses.

### Step 2: Configure OSPF Routing

Enable OSPFv2 on all three routers to provide full reachability between all subnets:

```text
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
R1(config-router)# network 10.0.12.0 0.0.0.3 area 0
R1(config-router)# network 10.0.13.0 0.0.0.3 area 0
R1(config-router)# passive-interface GigabitEthernet0/0
```

Configure equivalent OSPF on R2 (router-id 2.2.2.2) and R3 (router-id 3.3.3.3) including all their directly connected subnets.

### Step 3: Verify Baseline Connectivity

From PC-A, ping SRV1 to confirm full reachability before applying ACLs:

```text
PC-A> ping 192.168.3.100
```

Expected result: 5 successful replies. Record this as your baseline. All subsequent tests compare against this baseline.

---

## Part 2: Standard ACL — Restrict LAN B Access to SRV1

**Policy requirement:** Hosts in LAN B (192.168.2.0/24) must NOT be permitted to reach SRV1 (192.168.3.100). All other traffic should be unaffected.

### Step 4: Create the Standard ACL on R3

Standard ACLs filter only on source IP, so place this ACL on R3 close to the destination SRV1:

```text
R3(config)# ip access-list standard BLOCK_LAN_B
R3(config-std-nacl)# 10 deny 192.168.2.0 0.0.0.255
R3(config-std-nacl)# 20 permit any
R3(config-std-nacl)# exit
```

### Step 5: Apply the ACL to R3 Gi0/0 Outbound

SRV1 is on the LAN C segment connected to R3 Gi0/0. Apply the ACL outbound on that interface:

```text
R3(config)# interface GigabitEthernet0/0
R3(config-if)# ip access-group BLOCK_LAN_B out
R3(config-if)# exit
```

### Step 6: Verify Standard ACL Behavior

From PC-C (LAN B), ping SRV1:

```text
PC-C> ping 192.168.3.100
```

Expected result: All pings fail (U.U.U.U indicating unreachable). From PC-A (LAN A), ping SRV1:

```text
PC-A> ping 192.168.3.100
```

Expected result: 5 successful replies. LAN A traffic is unaffected.

Verify hit counters on R3:

```text
R3# show access-lists BLOCK_LAN_B
```

The deny statement counter should show matches.

---

## Part 3: Extended ACL — Restrict Telnet, Permit HTTP

**Policy requirement:** No host in LAN A should be able to Telnet to SRV1. HTTP (port 80) from LAN A to SRV1 should be permitted. All other IP traffic from LAN A should be permitted.

### Step 7: Enable Telnet on SRV1

In Packet Tracer, configure SRV1 with Telnet service enabled (Services tab > Telnet: On, set a password).

### Step 8: Create the Named Extended ACL on R1

Place this ACL on R1 close to the source (LAN A):

```text
R1(config)# ip access-list extended LAN_A_POLICY
R1(config-ext-nacl)# 10 deny tcp 192.168.1.0 0.0.0.255 host 192.168.3.100 eq 23
R1(config-ext-nacl)# 20 permit ip 192.168.1.0 0.0.0.255 any
R1(config-ext-nacl)# exit
```

### Step 9: Apply the Extended ACL Inbound on R1 Gi0/0

```text
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip access-group LAN_A_POLICY in
R1(config-if)# exit
```

### Step 10: Verify Extended ACL Behavior

From PC-A, attempt Telnet to SRV1:

```text
PC-A> telnet 192.168.3.100
```

Expected result: Connection refused or timeout — Telnet is blocked.

From PC-A, ping SRV1:

```text
PC-A> ping 192.168.3.100
```

Expected result: 5 successful replies — ICMP is permitted by line 20.

Verify counters:

```text
R1# show access-lists LAN_A_POLICY
R1# show ip interface GigabitEthernet0/0
```

Confirm that `LAN_A_POLICY` appears as the inbound ACL on Gi0/0.

---

## Part 4: VTY Line Access Restriction

**Policy requirement:** Only hosts in the 10.0.0.0/8 network (router management addresses) should be able to SSH or Telnet to R2.

### Step 11: Configure VTY ACL on R2

```text
R2(config)# access-list 5 permit 10.0.0.0 0.255.255.255
R2(config)# line vty 0 4
R2(config-line)# access-class 5 in
R2(config-line)# transport input ssh telnet
R2(config-line)# exit
```

### Step 12: Verify VTY Restriction

From PC-C (192.168.2.10), attempt Telnet to R2's LAN interface 192.168.2.1:

```text
PC-C> telnet 192.168.2.1
```

Expected result: Connection refused — 192.168.2.x is not in the 10.0.0.0/8 range permitted by ACL 5.

From R1 (10.0.12.1), Telnet to R2:

```text
R1# telnet 10.0.12.2
```

Expected result: Telnet prompt appears — 10.0.12.1 matches the permit statement.

---

## Part 5: Troubleshooting Scenarios

### Troubleshooting Scenario A — Incorrect ACL Direction

Remove the current application of LAN_A_POLICY and reapply it in the wrong direction:

```text
R1(config)# interface GigabitEthernet0/0
R1(config-if)# no ip access-group LAN_A_POLICY in
R1(config-if)# ip access-group LAN_A_POLICY out
```

Now ping SRV1 from PC-A and attempt Telnet. Record your observations. Explain why the outbound direction on Gi0/0 does not enforce the intended policy for traffic sourced from LAN A. Then restore the correct configuration.

Expected explanation: Outbound on Gi0/0 filters traffic exiting toward LAN A, not traffic entering from LAN A. Traffic from PC-A enters Gi0/0 inbound and exits toward R3 on Gi0/1 or Gi0/2. The outbound ACL on Gi0/0 never sees traffic from LAN A destined for SRV1.

### Troubleshooting Scenario B — Entry Order Problem

Modify LAN_A_POLICY to place the permit before the deny:

```text
R1(config)# ip access-list extended LAN_A_POLICY
R1(config-ext-nacl)# no 10
R1(config-ext-nacl)# no 20
R1(config-ext-nacl)# 10 permit ip 192.168.1.0 0.0.0.255 any
R1(config-ext-nacl)# 20 deny tcp 192.168.1.0 0.0.0.255 host 192.168.3.100 eq 23
```

Attempt Telnet from PC-A to SRV1. Record the result. Explain why the deny entry no longer has any effect. Then restore the correct order.

Expected explanation: Line 10 permits all IP traffic from LAN A to any destination. Because all IP includes TCP, and `permit ip any any` matches before `deny tcp ... eq 23`, the deny line is unreachable. The first match wins and the permit fires before the router evaluates line 20.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show access-lists BLOCK_LAN_B` showing deny counter incremented
2. Screenshot of `show access-lists LAN_A_POLICY` showing deny counter incremented
3. Screenshot of `show ip interface GigabitEthernet0/0` on R1 confirming LAN_A_POLICY inbound
4. Screenshot of failed Telnet attempt from PC-A to SRV1
5. Screenshot of successful ping from PC-A to SRV1 after extended ACL applied
6. Written answer for Troubleshooting Scenario A (4–6 sentences)
7. Written answer for Troubleshooting Scenario B (4–6 sentences)

---

## Grading Rubric

| Component                          | Points | Criteria                                                         |
|------------------------------------|--------|------------------------------------------------------------------|
| Baseline connectivity confirmed    | 10     | Successful ping from PC-A to SRV1 before ACLs applied           |
| Standard ACL configuration         | 15     | BLOCK_LAN_B created with correct deny and permit entries         |
| Standard ACL placement             | 10     | Applied outbound on R3 Gi0/0 with hit counters confirmed         |
| Extended ACL configuration         | 20     | LAN_A_POLICY with correct deny Telnet and permit ip entries      |
| Extended ACL direction             | 10     | Applied inbound on R1 Gi0/0; confirmed with show ip interface    |
| VTY restriction                    | 10     | ACL 5 applied with access-class; correct permit/deny behavior    |
| Troubleshooting Scenario A         | 12     | Correct explanation of direction error and fix                   |
| Troubleshooting Scenario B         | 13     | Correct explanation of order error and fix                       |

Partial credit is awarded for demonstrably attempted but incomplete work.
