# Lab Activity: Module 07 - Inter-VLAN Routing Solutions

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Tool:** Cisco Packet Tracer 8.x
**Estimated Time:** 60-75 minutes
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

In this lab you will configure inter-VLAN routing using two different methods in Cisco Packet Tracer. Part 1 uses router-on-a-stick with an external router and a Layer 2 switch. Part 2 replaces the external router with a Catalyst 3650 multilayer switch using SVIs. You will verify inter-VLAN connectivity in both topologies and troubleshoot a scenario where SVIs fail to route.

This lab maps to CCNA 200-301 exam objectives 3.3 (configure and verify IPv4 routing, inter-VLAN routing) and 2.4 (configure and verify Layer 3 switching and inter-VLAN routing).

---

## Objectives

By completing this lab you will be able to:

- Configure a router trunk port and subinterfaces for router-on-a-stick
- Apply 802.1Q encapsulation to router subinterfaces
- Enable `ip routing` on a multilayer switch
- Create and configure SVIs on a multilayer switch
- Verify inter-VLAN connectivity using ping between hosts in different VLANs
- Troubleshoot common ROAS and SVI configuration failures

---

## Equipment List

### Part 1 (Router-on-a-Stick)

- 1x Cisco 1941 Router (R1)
- 1x Cisco Catalyst 2960-24TT Switch (SW1)
- 2x PCs (PC-A in VLAN 10, PC-B in VLAN 20)
- Straight-through Ethernet cables

### Part 2 (Layer 3 Switch SVIs)

- 1x Cisco Catalyst 3650 Multilayer Switch (MLS1)
- 2x PCs (PC-C in VLAN 10, PC-D in VLAN 20)
- Straight-through Ethernet cables

---

## Part 1: Router-on-a-Stick

### Topology

```text
PC-A (VLAN 10) --Fa0/1-- SW1 --Gi0/1 trunk-- R1 Gi0/0 (parent)
PC-B (VLAN 20) --Fa0/2-- SW1                        |
                                              G0/0.10  G0/0.20
```

PC-A: 192.168.10.11/24, gateway 192.168.10.1
PC-B: 192.168.20.11/24, gateway 192.168.20.1

### Step 1: Configure Hostnames

Set hostnames on SW1 and R1.

### Step 2: Create VLANs on SW1

```ios
SW1# configure terminal
SW1(config)# vlan 10
SW1(config-vlan)# name ENGINEERING
SW1(config-vlan)# vlan 20
SW1(config-vlan)# name SALES
SW1(config-vlan)# exit
```

### Step 3: Configure Access Ports on SW1

Assign PC-A's port to VLAN 10 and PC-B's port to VLAN 20:

```ios
SW1(config)# interface FastEthernet0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# no shutdown

SW1(config)# interface FastEthernet0/2
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 20
SW1(config-if)# no shutdown
```

### Step 4: Configure Trunk Port on SW1

Configure the uplink to R1 as a trunk:

```ios
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20
SW1(config-if)# end
SW1# write memory
```

### Step 5: Configure R1 Subinterfaces

Bring up the parent interface and create one subinterface per VLAN:

```ios
R1# configure terminal
R1(config)# interface GigabitEthernet0/0
R1(config-if)# no shutdown

R1(config)# interface GigabitEthernet0/0.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 192.168.10.1 255.255.255.0

R1(config)# interface GigabitEthernet0/0.20
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip address 192.168.20.1 255.255.255.0
R1(config)# end
R1# write memory
```

### Step 6: Verify ROAS Configuration

Verify subinterface states and IP addresses:

```ios
R1# show ip interface brief
R1# show interfaces GigabitEthernet0/0.10
R1# show ip route
```

Expected `show ip interface brief` output:

```text
Interface              IP-Address      OK? Method Status  Protocol
GigabitEthernet0/0     unassigned      YES unset  up       up
GigabitEthernet0/0.10  192.168.10.1    YES manual up       up
GigabitEthernet0/0.20  192.168.20.1    YES manual up       up
```

### Step 7: Configure PC IP Addresses

Set PC-A IP address to 192.168.10.11 with subnet mask 255.255.255.0 and default gateway 192.168.10.1.
Set PC-B IP address to 192.168.20.11 with subnet mask 255.255.255.0 and default gateway 192.168.20.1.

### Step 8: Verify Inter-VLAN Connectivity

From PC-A, ping PC-B:

```text
PC-A> ping 192.168.20.11
```

Expected result: 5 successful replies. If ping fails, verify the gateway addresses on each PC match the subinterface IP addresses on R1.

---

## Part 2: Layer 3 Switch SVIs

### SVI Topology

```text
PC-C (VLAN 10) --Fa0/1-- MLS1 --Fa0/2-- PC-D (VLAN 20)
```

PC-C: 192.168.10.21/24, gateway 192.168.10.1
PC-D: 192.168.20.21/24, gateway 192.168.20.1

### Step 9: Enable IP Routing on MLS1

```ios
MLS1# configure terminal
MLS1(config)# ip routing
```

### Step 10: Create VLANs on MLS1

```ios
MLS1(config)# vlan 10
MLS1(config-vlan)# name ENGINEERING
MLS1(config-vlan)# vlan 20
MLS1(config-vlan)# name SALES
MLS1(config-vlan)# exit
```

### Step 11: Create SVIs on MLS1

```ios
MLS1(config)# interface vlan 10
MLS1(config-if)# ip address 192.168.10.1 255.255.255.0
MLS1(config-if)# no shutdown

MLS1(config)# interface vlan 20
MLS1(config-if)# ip address 192.168.20.1 255.255.255.0
MLS1(config-if)# no shutdown
```

### Step 12: Configure Access Ports on MLS1

```ios
MLS1(config)# interface FastEthernet0/1
MLS1(config-if)# switchport mode access
MLS1(config-if)# switchport access vlan 10

MLS1(config)# interface FastEthernet0/2
MLS1(config-if)# switchport mode access
MLS1(config-if)# switchport access vlan 20
MLS1(config)# end
MLS1# write memory
```

### Step 13: Verify SVI States

```ios
MLS1# show ip interface brief
MLS1# show interfaces vlan 10
MLS1# show ip route
MLS1# show vlan brief
```

Expected `show ip interface brief` output:

```text
Interface              IP-Address      OK? Method Status  Protocol
Vlan10                 192.168.10.1    YES manual up       up
Vlan20                 192.168.20.1    YES manual up       up
```

Both SVIs should show `up/up`. If either shows `up/down`, verify that the access port in that VLAN is connected and up.

### Step 14: Verify Inter-VLAN Connectivity via SVIs

Set PC-C and PC-D IP addresses and gateways as specified in the topology. From PC-C, ping PC-D:

```text
PC-C> ping 192.168.20.21
```

Expected result: 5 successful replies.

---

## Part 3: Troubleshooting Scenarios

Work through each scenario and document your analysis.

### Scenario A: ip routing Missing

Remove `ip routing` from MLS1 and attempt to ping from PC-C to PC-D:

```ios
MLS1(config)# no ip routing
```

Observe the result. The ping fails because the switch no longer routes between VLANs even though the SVIs still exist. Restore `ip routing` and verify connectivity is restored.

Expected answer: Without `ip routing`, the multilayer switch behaves as a Layer 2 switch. SVIs remain configured but are not used for inter-VLAN routing. The fix is to re-enter `ip routing` in global configuration.

### Scenario B: SVI up/down State

Disconnect PC-C from MLS1 Fa0/1 and run `show ip interface brief`. Observe that Vlan10 shows `up/down`. Reconnect the cable and observe the SVI recover to `up/up`.

Expected answer: An SVI is `up/down` when no active access ports are in that VLAN. Reconnecting the cable (or assigning another active port to the VLAN) restores the SVI to `up/up`.

### Scenario C: Wrong Default Gateway on Host

Change PC-D's default gateway to 192.168.10.1 (the VLAN 10 SVI instead of the VLAN 20 SVI). Attempt to ping PC-C from PC-D.

Observe that pings may fail or produce inconsistent results. Correct the gateway to 192.168.20.1 and verify connectivity.

Expected answer: Each host must use the SVI IP address for its own VLAN as its default gateway. Hosts in VLAN 20 use 192.168.20.1. Using the wrong gateway causes routing failures when the host tries to send traffic to another subnet.

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show ip interface brief` on R1 showing both subinterfaces up/up with correct IP addresses
2. Screenshot of successful ping from PC-A to PC-B (through ROAS)
3. Screenshot of `show ip interface brief` on MLS1 showing both SVIs up/up
4. Screenshot of `show ip route` on MLS1 showing connected routes for both VLANs
5. Screenshot of successful ping from PC-C to PC-D (through SVIs)
6. Written answers to Troubleshooting Scenarios A, B, and C (3-5 sentences each)

---

## Grading Rubric (100 Points)

| Component | Points | Criteria |
|---|---|---|
| ROAS Subinterface Configuration | 25 | Both subinterfaces up/up with correct encapsulation and IP addresses |
| ROAS Connectivity | 15 | Successful ping from PC-A to PC-B through R1 |
| SVI Configuration | 25 | Both SVIs up/up on MLS1; ip routing enabled |
| SVI Routing Verification | 10 | show ip route shows connected routes for both VLANs |
| SVI Connectivity | 10 | Successful ping from PC-C to PC-D through MLS1 SVIs |
| Troubleshooting Scenarios | 15 | Correct analysis for all three scenarios (5 pts each) |

Partial credit awarded for demonstrably attempted but incomplete work.

---

## Part 9 — Challenge Exercise

This optional challenge extends the lab to CCNA exam difficulty. Complete all steps and include deliverables in your submission for up to 20 bonus points.

### Challenge Step 1: Add a Third VLAN and Configure Inter-VLAN Routing for It

Add VLAN 30 (name SERVERS, subnet 192.168.30.0/24) to both the ROAS and SVI topologies. Configure the router subinterface for VLAN 30 in the ROAS section and an additional SVI for VLAN 30 in the SVI section. Add a PC in VLAN 30 on each topology. Verify cross-VLAN connectivity from a VLAN 10 host to the VLAN 30 host on both topologies. Document the additional commands required and the routing table entries added.

### Challenge Step 2: Implement and Test an SVI ACL to Restrict Inter-VLAN Traffic

On the multilayer switch, configure an ACL that prevents hosts in VLAN 10 from reaching hosts in VLAN 30, while still allowing VLAN 10 to reach VLAN 20:

```ios
MLS1(config)# ip access-list extended VLAN10_RESTRICT
MLS1(config-ext-nacl)# deny ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255
MLS1(config-ext-nacl)# permit ip any any
MLS1(config)# interface vlan 10
MLS1(config-if)# ip access-group VLAN10_RESTRICT in
```

Verify that VLAN 10 hosts can still reach VLAN 20 but are blocked from VLAN 30. Document the ping results (success and failure) and the `show access-lists` output confirming match counters are incrementing. Explain in 2–3 sentences why this ACL is applied inbound on the VLAN 10 SVI rather than outbound on the VLAN 30 SVI.

### Challenge Step 3: Compare ROAS and SVI Performance by Observing Routing Table Behavior

Configure `show ip route` on both the ROAS router and the multilayer switch simultaneously for the same three-VLAN topology. Compare the two routing tables and document: (1) What type of route entries appear (connected, static, or dynamic), (2) whether the next-hop is an interface or an IP address, and (3) how the exit interface is listed differently between a router's routing table and a multilayer switch's routing table. Write a 3–4 sentence comparison explaining which method you would choose for a 500-user campus building and why.
