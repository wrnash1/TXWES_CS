# Lab Activity: Module 10 - Access Control Lists

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 5: Security Fundamentals - 15%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure standard and extended ACLs on a multi-segment router topology in Cisco Packet Tracer. Part 1 configures a standard ACL to restrict inter-VLAN traffic. Part 2 configures an extended ACL to permit specific services while blocking others. You will verify ACL behavior by testing permitted and denied traffic, and you will interpret `show access-lists` match counters.

This lab maps to CCNA 200-301 exam objectives 5.6 (configure and verify access control lists).

---

## Objectives

By completing this lab you will be able to:

- Configure a standard numbered ACL and apply it close to the destination
- Configure an extended numbered ACL and apply it close to the source
- Use the `host` and `any` keywords in ACL entries
- Verify ACL match counters using `show access-lists`
- Verify applied ACLs using `show ip interface`
- Diagnose a blocked traffic problem caused by implicit deny

---

## Equipment List

- 1x Cisco 1941 Router (R1)
- 3x Cisco Catalyst 2960-24TT Switches (SW1, SW2, SW3)
- 4x PCs (PC-A, PC-B, PC-C, PC-D)
- 1x Server (Server-A)
- Straight-through Ethernet cables

---

## Topology

```text
PC-A (192.168.10.11) --SW1--+
PC-B (192.168.10.12) --SW1--+--Gi0/0 (192.168.10.1)--R1--Gi0/1 (192.168.20.1)--SW2--PC-C (192.168.20.11)
                                                        |
                                                   Gi0/2 (192.168.30.1)
                                                        |
                                                       SW3
                                                        |
                                               Server-A (192.168.30.5)
                                                PC-D (192.168.30.11)
```

### IP Address Table

| Device | Interface / NIC | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| R1 | Gi0/0 | 192.168.10.1 | 255.255.255.0 | — |
| R1 | Gi0/1 | 192.168.20.1 | 255.255.255.0 | — |
| R1 | Gi0/2 | 192.168.30.1 | 255.255.255.0 | — |
| PC-A | NIC | 192.168.10.11 | 255.255.255.0 | 192.168.10.1 |
| PC-B | NIC | 192.168.10.12 | 255.255.255.0 | 192.168.10.1 |
| PC-C | NIC | 192.168.20.11 | 255.255.255.0 | 192.168.20.1 |
| Server-A | NIC | 192.168.30.5 | 255.255.255.0 | 192.168.30.1 |
| PC-D | NIC | 192.168.30.11 | 255.255.255.0 | 192.168.30.1 |

---

## Part 1: Standard ACL Configuration

### Objective

Block all traffic from the 192.168.20.0/24 network (Sales, PC-C) from reaching the 192.168.30.0/24 network (Server segment). All other traffic should be permitted.

### Step 1: Verify Baseline Connectivity

Before any ACL configuration, verify end-to-end connectivity:

- PC-A ping PC-C (should succeed)
- PC-A ping Server-A (should succeed)
- PC-C ping Server-A (should succeed)

Document the results.

### Step 2: Create Standard ACL 10

On R1, create the standard ACL to deny the Sales subnet and permit everything else:

```ios
R1# configure terminal
R1(config)# access-list 10 deny 192.168.20.0 0.0.0.255
R1(config)# access-list 10 permit any
```

### Step 3: Apply ACL 10 Close to the Destination

Apply the ACL outbound on the interface facing the server segment (Gi0/2):

```ios
R1(config)# interface GigabitEthernet0/2
R1(config-if)# ip access-group 10 out
R1(config-if)# end
```

### Step 4: Verify ACL Application

```ios
R1# show ip interface GigabitEthernet0/2
```

Confirm the output shows:

```text
Outgoing access list is 10
```

### Step 5: Test ACL Behavior

- PC-C ping Server-A — should be BLOCKED (denied by ACL 10)
- PC-C ping PC-D — should be BLOCKED (same outbound ACL on Gi0/2)
- PC-A ping Server-A — should SUCCEED (192.168.10.x is not denied)

### Step 6: Verify ACL Match Counters

```ios
R1# show access-lists
```

Expected output:

```text
Standard IP access list 10
    10 deny 192.168.20.0 0.0.0.255 (X matches)
    20 permit any (Y matches)
```

The match counter on the deny entry should have increased from the blocked pings.

---

## Part 2: Extended ACL Configuration

### Extended ACL Objective

Block only Telnet (TCP port 23) from the 192.168.10.0/24 network to Server-A (192.168.30.5). Permit all other traffic, including HTTP, ICMP (ping), and all other sources.

### Step 7: Create Extended ACL 110

```ios
R1# configure terminal
R1(config)# access-list 110 deny tcp 192.168.10.0 0.0.0.255 host 192.168.30.5 eq 23
R1(config)# access-list 110 permit ip any any
```

### Step 8: Remove the Standard ACL from Gi0/2

Before applying the extended ACL, remove ACL 10 from Gi0/2:

```ios
R1(config)# interface GigabitEthernet0/2
R1(config-if)# no ip access-group 10 out
```

### Step 9: Apply ACL 110 Close to the Source

Apply the extended ACL inbound on the interface facing the source subnet (Gi0/0):

```ios
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip access-group 110 in
R1(config-if)# end
```

### Step 10: Test Extended ACL Behavior

- PC-A ping Server-A — should SUCCEED (ICMP is permitted by `permit ip any any`)
- PC-A Telnet to Server-A — should be BLOCKED by the deny tcp entry
- PC-C ping Server-A — should SUCCEED (source is 192.168.20.x, not matched by deny entry)

### Step 11: Verify Extended ACL Match Counters

```ios
R1# show access-lists 110
```

Confirm match counters on both entries have incremented as expected.

---

## Part 3: Troubleshooting Scenarios

Work through each scenario and document your analysis.

### Scenario A: All Traffic Blocked by ACL

An engineer configures the following ACL on R1 and applies it inbound on Gi0/0:

```ios
access-list 120 deny tcp 192.168.10.0 0.0.0.255 host 192.168.30.5 eq 23
```

After application, all traffic from PC-A fails — including pings to all destinations. Explain why and write the missing command to fix it.

Expected answer: The ACL has a deny entry but no permit entry. The implicit deny at the end of every ACL drops all unmatched traffic. Add `access-list 120 permit ip any any` after the deny entry to allow all traffic that is not Telnet to 192.168.30.5.

### Scenario B: ACL Applied in Wrong Direction

An engineer creates extended ACL 130 to block traffic from 192.168.20.0/24 to Server-A and applies it `out` on Gi0/0 instead of `in`. Explain what traffic is affected and whether the ACL achieves the intended result.

Expected answer: Outbound on Gi0/0 filters traffic leaving R1 toward the 192.168.10.0/24 segment — the opposite direction from what was intended. The ACL would affect traffic going toward the Engineering network, not traffic coming from the Sales network toward the server. The correct application is `in` on Gi0/1 (the Sales interface) or `out` on Gi0/2 (the server interface). Direction must match the traffic flow being filtered.

### Scenario C: Standard ACL in Wrong Location

An engineer wants to block only PC-C (192.168.20.11) from reaching Server-A (192.168.30.5). They configure `access-list 1 deny host 192.168.20.11` and apply it inbound on Gi0/0 (the Engineering interface). Explain the problem and the correct placement.

Expected answer: Applying this standard ACL inbound on Gi0/0 filters traffic coming from the Engineering segment, not the Sales segment where PC-C is located. The ACL is applied to the wrong interface — it must be applied outbound on Gi0/2 (close to the destination, the server segment) or inbound on Gi0/1 (the Sales interface directly). Standard ACLs cannot identify the destination, so they must be placed as close to the destination as possible to avoid unintentionally blocking traffic to other destinations.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of baseline connectivity test (before ACL) showing successful pings
2. Screenshot of `show access-lists` after Part 1 showing the standard ACL with match counters
3. Screenshot of failed PC-C to Server-A ping (blocked by ACL 10)
4. Screenshot of `show access-lists 110` showing extended ACL match counters after Part 2 tests
5. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| Standard ACL Configuration | 20 | ACL 10 created; applied outbound on Gi0/2 |
| Standard ACL Verification | 15 | show access-lists shows deny entry with match counters; PC-C blocked |
| Extended ACL Configuration | 20 | ACL 110 created; applied inbound on Gi0/0 |
| Extended ACL Verification | 15 | show access-lists 110 shows both entries with match counters; Telnet blocked, ping allowed |
| Baseline and Post-ACL Tests | 15 | Screenshots showing permitted and denied traffic behavior |
| Troubleshooting Scenarios | 15 | Correct analysis for all three scenarios (5 pts each) |

Partial credit awarded for demonstrably attempted but incomplete work.
