# Lab Activity: Module 10 — NAT and PAT

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Tool: Cisco Packet Tracer 8.x

## Estimated Time: 60–75 minutes

## Total Points: 100

---

## Overview

In this lab you will configure static NAT to make an internal web server reachable from the internet, configure PAT to allow internal LAN hosts to share a single public IP for outbound internet access, and verify both configurations using NAT translation table commands. You will also work through two troubleshooting scenarios targeting the most common NAT misconfiguration patterns. This lab maps directly to CCNA 200-301 IP Services exam objectives.

---

## Objectives

By completing this lab you will be able to:

- Configure static NAT mapping for an internal server
- Configure PAT using an outside interface address with the overload keyword
- Apply `ip nat inside` and `ip nat outside` to correct interfaces
- Verify NAT operation using `show ip nat translations` and `show ip nat statistics`
- Interpret PAT translation table entries including inside local, inside global, and port numbers
- Diagnose and repair two common NAT misconfigurations

---

## Equipment List

- 2x Cisco 1941 Routers (R1 acting as NAT router, ISP simulating internet)
- 1x Cisco Catalyst 2960-24TT Switch (SW1)
- 3x Internal PCs (PC-A, PC-B, PC-C)
- 1x Internal Server (SRV-INT — web server to be statically NATted)
- 1x External Server (SRV-EXT — simulates internet destination, hosted on ISP segment)
- Straight-through Ethernet cables for LAN connections
- Crossover or straight-through cable for R1–ISP WAN link

---

## Topology Description

```text
PC-A (192.168.1.10) ---|
PC-B (192.168.1.20) ---+-- SW1 -- R1 Gi0/0 (192.168.1.1)
PC-C (192.168.1.30) ---|         R1 Gi0/1 (203.0.113.1/30) -- ISP Gi0/0 (203.0.113.2/30)
SRV-INT (192.168.1.100)|                                        ISP Gi0/1 -- SRV-EXT (8.8.8.8)

NAT Translations:
  Static: SRV-INT 192.168.1.100 <--> 203.0.113.10 (public server IP)
  PAT:    PC-A/B/C 192.168.1.x  --> 203.0.113.1  (interface address, overload)
```

---

## IP Address Table

| Device  | Interface | IP Address     | Subnet Mask     | Notes                        |
|---------|-----------|----------------|-----------------|------------------------------|
| R1      | Gi0/0     | 192.168.1.1    | 255.255.255.0   | Inside LAN interface         |
| R1      | Gi0/1     | 203.0.113.1    | 255.255.255.252 | Outside WAN interface        |
| ISP     | Gi0/0     | 203.0.113.2    | 255.255.255.252 | WAN link to R1               |
| ISP     | Gi0/1     | 8.8.8.1        | 255.255.255.0   | External segment             |
| SRV-EXT | NIC       | 8.8.8.8        | 255.255.255.0   | GW 8.8.8.1 — external target |
| PC-A    | NIC       | 192.168.1.10   | 255.255.255.0   | GW 192.168.1.1               |
| PC-B    | NIC       | 192.168.1.20   | 255.255.255.0   | GW 192.168.1.1               |
| PC-C    | NIC       | 192.168.1.30   | 255.255.255.0   | GW 192.168.1.1               |
| SRV-INT | NIC       | 192.168.1.100  | 255.255.255.0   | GW 192.168.1.1               |

---

## Part 1: Baseline Configuration

### Step 1: Configure R1 Interfaces and Default Route

Configure hostnames and all interface IP addresses. Enable all interfaces with `no shutdown`. Add a default route on R1 pointing to the ISP:

```text
R1(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface GigabitEthernet0/1
R1(config-if)# ip address 203.0.113.1 255.255.255.252
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

### Step 2: Configure ISP Router

```text
ISP(config)# hostname ISP
ISP(config)# interface GigabitEthernet0/0
ISP(config-if)# ip address 203.0.113.2 255.255.255.252
ISP(config-if)# no shutdown
ISP(config-if)# exit
ISP(config)# interface GigabitEthernet0/1
ISP(config-if)# ip address 8.8.8.1 255.255.255.0
ISP(config-if)# no shutdown
ISP(config-if)# exit
ISP(config)# ip route 203.0.113.0 255.255.255.248 203.0.113.1
```

The ISP static route covers the 203.0.113.0/29 range (including .10 used for static NAT) and points back to R1.

### Step 3: Verify WAN Reachability

From R1, ping the ISP interface and the external server:

```text
R1# ping 203.0.113.2
R1# ping 8.8.8.8
```

Both pings should succeed from R1's perspective before NAT is configured. Note that pings from PC-A to SRV-EXT will fail at this stage because no NAT is configured yet.

---

## Part 2: Static NAT Configuration

### Step 4: Configure the Static NAT Mapping

Map internal server SRV-INT (192.168.1.100) to public address 203.0.113.10:

```text
R1(config)# ip nat inside source static 192.168.1.100 203.0.113.10
```

### Step 5: Mark NAT Interfaces

```text
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip nat inside
R1(config-if)# exit
R1(config)# interface GigabitEthernet0/1
R1(config-if)# ip nat outside
R1(config-if)# exit
```

### Step 6: Verify Static NAT Entry

```text
R1# show ip nat translations
```

Expected output before any traffic:

```text
Pro  Inside global    Inside local     Outside local    Outside global
---  203.0.113.10     192.168.1.100    ---              ---
```

The static entry appears immediately without requiring any traffic to trigger it, which confirms the mapping is configured correctly.

### Step 7: Test Static NAT from External Server

From SRV-EXT, ping 203.0.113.10:

```text
SRV-EXT> ping 203.0.113.10
```

Expected result: 5 successful replies. R1 intercepts the packet destined for 203.0.113.10, translates the destination to 192.168.1.100, and forwards it to SRV-INT.

Verify the translation table shows an active TCP/ICMP entry after the test traffic:

```text
R1# show ip nat translations
```

---

## Part 3: PAT Configuration

### Step 8: Create ACL Identifying Inside Hosts

```text
R1(config)# access-list 1 permit 192.168.1.0 0.0.0.255
```

### Step 9: Configure PAT Using Interface Address

```text
R1(config)# ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

The `overload` keyword enables PAT. The `interface GigabitEthernet0/1` directive instructs the router to use the current IP address of that interface (203.0.113.1) as the inside global address for all translated sessions.

### Step 10: Test PAT from Multiple Internal Hosts

From PC-A, PC-B, and PC-C, ping SRV-EXT simultaneously:

```text
PC-A> ping 8.8.8.8
PC-B> ping 8.8.8.8
PC-C> ping 8.8.8.8
```

All pings should succeed.

### Step 11: Verify PAT Translation Table

```text
R1# show ip nat translations
```

Expected output showing PAT entries for all three PCs sharing the same inside global address (203.0.113.1) with different port numbers:

```text
Pro  Inside global        Inside local         Outside local    Outside global
icmp 203.0.113.1:512      192.168.1.10:512     8.8.8.8:512      8.8.8.8:512
icmp 203.0.113.1:513      192.168.1.20:512     8.8.8.8:512      8.8.8.8:512
icmp 203.0.113.1:514      192.168.1.30:512     8.8.8.8:512      8.8.8.8:512
---  203.0.113.10          192.168.1.100        ---              ---
```

All three PC addresses translate to 203.0.113.1 with unique identifier values. The static NAT entry for SRV-INT remains at the bottom.

### Step 12: View NAT Statistics

```text
R1# show ip nat statistics
```

Record: total active translations, hits count, inside interfaces, and outside interfaces listed in the output.

---

## Part 4: Troubleshooting Scenarios

### Troubleshooting Scenario A — Missing Interface Marking

Remove the `ip nat inside` designation from Gi0/0, clear the translation table, and attempt to ping from PC-A:

```text
R1(config)# interface GigabitEthernet0/0
R1(config-if)# no ip nat inside

R1# clear ip nat translation *
```

From PC-A, ping SRV-EXT:

```text
PC-A> ping 8.8.8.8
```

Expected result: ping fails. Run `show ip nat statistics` and `show ip nat translations`. Record your observations.

Written question: Explain why removing `ip nat inside` from the LAN interface prevents PAT from working even though the PAT rule and ACL are still configured. What does the router use interface markings for during the NAT decision process?

Restore the configuration before proceeding:

```text
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip nat inside
```

### Troubleshooting Scenario B — ACL Mismatch

Modify ACL 1 so it does not match the internal subnet. Replace the permit with a non-matching entry:

```text
R1(config)# no access-list 1
R1(config)# access-list 1 permit 10.10.10.0 0.0.0.255
R1# clear ip nat translation *
```

From PC-A, ping SRV-EXT. Expected result: ping fails. Run `show access-lists 1` and confirm zero hit counts. Run `show ip nat translations` and confirm no dynamic entries are created.

Written question: Explain why the ACL mismatch prevents NAT from occurring and describe how you would use `show access-lists` and `show ip nat translations` together to diagnose this failure in a production environment.

Restore the correct ACL:

```text
R1(config)# no access-list 1
R1(config)# access-list 1 permit 192.168.1.0 0.0.0.255
```

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show ip nat translations` after Step 6 showing the static NAT entry
2. Screenshot of successful ping from SRV-EXT to 203.0.113.10 (Step 7)
3. Screenshot of `show ip nat translations` after Step 11 showing PAT entries for all three PCs
4. Screenshot of `show ip nat statistics` output from Step 12
5. Written answer for Troubleshooting Scenario A (4–6 sentences)
6. Written answer for Troubleshooting Scenario B (4–6 sentences)

---

## Grading Rubric

| Component                               | Points | Criteria                                                              |
|-----------------------------------------|--------|-----------------------------------------------------------------------|
| Baseline connectivity verified          | 10     | R1 can ping ISP and SRV-EXT before NAT configuration                 |
| Static NAT mapping configured           | 15     | Correct ip nat inside source static command; entry in translation table|
| Interface markings applied              | 10     | ip nat inside on Gi0/0; ip nat outside on Gi0/1                      |
| Static NAT verified from external host  | 15     | SRV-EXT successfully pings 203.0.113.10                              |
| PAT configuration correct               | 15     | Correct ACL, ip nat inside source list ... overload command           |
| PAT translation table shows port reuse  | 15     | Three PCs share 203.0.113.1 with unique ports in show output          |
| Troubleshooting Scenario A              | 10     | Correct explanation of interface marking requirement                  |
| Troubleshooting Scenario B              | 10     | Correct explanation of ACL mismatch diagnosis using show commands     |

Partial credit is awarded for demonstrably attempted but incomplete work.

---

## Part 9 — Challenge Exercise

This optional challenge extends the lab to CCNA exam difficulty. Complete all steps and include deliverables in your submission for up to 20 bonus points.

### Challenge Step 1: Configure Dynamic NAT with a Pool and Observe Pool Exhaustion

Extend the existing topology by configuring a second NAT rule using a named pool instead of the interface method. Create a pool with only two public addresses (203.0.113.30 and 203.0.113.31) and configure dynamic NAT (without overload) for a second inside subnet 192.168.2.0/24.

```ios
R1(config)# ip nat pool LIMITED_POOL 203.0.113.30 203.0.113.31 netmask 255.255.255.252
R1(config)# access-list 2 permit 192.168.2.0 0.0.0.255
R1(config)# ip nat inside source list 2 pool LIMITED_POOL
```

Connect three hosts in the 192.168.2.0/24 subnet and have all three attempt to ping the external server simultaneously. Observe that only two hosts receive translations (one per pool address) and the third host's traffic is dropped. Use `show ip nat translations` to verify the pool entries and `show ip nat statistics` to observe the pool exhaustion counter (`pool exhausted` line). Document the output and explain in 3–4 sentences why PAT with `overload` is almost always preferred over dynamic NAT in enterprise deployments.

### Challenge Step 2: Implement NAT with a DMZ Using Static and PAT Together

Build a topology that simultaneously uses static NAT for an internal server and PAT for LAN users, reflecting a real-world DMZ design. Add a second server (SRV-INTERNAL) at 192.168.1.200 that must be reachable from the internet at 203.0.113.15 (static NAT), while LAN PCs continue to use PAT through the existing interface address.

```ios
R1(config)# ip nat inside source static 192.168.1.200 203.0.113.15
```

Verify that both NAT types coexist:
- From SRV-EXT, ping 203.0.113.15 and confirm it reaches SRV-INTERNAL via static NAT
- From PC-A, ping SRV-EXT and confirm PAT translations still appear for PC-A

Run `show ip nat translations` and identify the two different entry types: the permanent static entry (marked Pro `---`) and the dynamic PAT entries with TCP/UDP port numbers. Explain in 2–3 sentences how the router decides which NAT rule to apply when a packet arrives from the inside network.

### Challenge Step 3: Analyze Translation Table Aging and Configure Custom Timeouts

Investigate NAT translation aging by observing the default timeout behavior and then configuring custom timeouts. After generating PAT translations from PC-A to SRV-EXT, use `show ip nat translations verbose` to observe the timeout countdown on each entry.

```ios
R1# show ip nat translations verbose
```

Note the `create` and `use` timestamps and the remaining time before expiration. Then configure custom NAT timeouts to simulate an environment requiring faster session cleanup:

```ios
R1(config)# ip nat translation timeout 120
R1(config)# ip nat translation tcp-timeout 300
R1(config)# ip nat translation udp-timeout 60
```

Generate new traffic, observe the new timeout values in `show ip nat translations verbose`, and then use `clear ip nat translation *` to manually clear all dynamic entries. Verify with `show ip nat translations` that only the static entry for SRV-INTERNAL remains. Explain in 2–3 sentences the operational difference between `ip nat translation timeout` (generic) and the protocol-specific timeout commands, and describe a scenario where reducing the UDP timeout would be beneficial in a high-traffic environment.
