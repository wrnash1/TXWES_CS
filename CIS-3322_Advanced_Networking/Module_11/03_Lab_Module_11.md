# Lab Activity: Module 11 — DHCP and DNS Configuration

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Tool: Cisco Packet Tracer 8.x

## Estimated Time: 60–75 minutes

## Total Points: 100

---

## Overview

In this lab you will configure a Cisco IOS router as a DHCP server for two VLANs, configure a second router as a DHCP relay agent to forward client broadcasts to the centralized server, verify DHCP bindings and client connectivity, and enable DHCP snooping on an access switch. You will also configure DNS server settings in the DHCP pool and verify end-to-end name resolution. Two troubleshooting scenarios address the most common DHCP deployment failures. This lab maps to CCNA 200-301 IP Services objectives.

---

## Objectives

By completing this lab you will be able to:

- Configure a Cisco IOS DHCP server with excluded addresses and pool parameters
- Verify DHCP bindings using `show ip dhcp binding`
- Configure `ip helper-address` on a relay router for inter-subnet DHCP forwarding
- Enable and verify DHCP snooping on a Cisco Catalyst switch
- Configure DNS server and domain name settings in a DHCP pool
- Diagnose and repair two DHCP configuration failures

---

## Equipment List

- 2x Cisco 1941 Routers (R1 acting as DHCP server, R2 acting as relay agent and gateway)
- 1x Cisco Catalyst 2960-24TT Switch (SW1 — access layer with DHCP snooping)
- 4x End-user PCs (PC-A, PC-B, PC-C, PC-D — configured for DHCP)
- 1x DNS/Web Server (DNS-SRV at static IP 10.0.0.53)
- Straight-through Ethernet cables for all LAN connections

---

## Topology Description

```text
PC-A ---+                              +--- R1 Gi0/0 (10.0.0.1/24)
PC-B ---+-- SW1 -- R2 Gi0/0           |    R1 = DHCP Server
        |     VLAN10: 192.168.10.0/24  +--- DNS-SRV (10.0.0.53/24)
PC-C ---+
PC-D ---+-- SW1 -- R2 Gi0/1
              VLAN20: 192.168.20.0/24

R2 Gi0/2 = 10.0.0.2/24 (connects to R1 segment)
R2 is relay agent for both VLANs
```

---

## IP Address Table

| Device  | Interface  | IP Address      | Subnet Mask     | Assignment | Notes               |
|---------|------------|-----------------|-----------------|------------|---------------------|
| R1      | Gi0/0      | 10.0.0.1        | 255.255.255.0   | Static     | DHCP server LAN     |
| R2      | Gi0/0      | 192.168.10.1    | 255.255.255.0   | Static     | VLAN10 gateway      |
| R2      | Gi0/1      | 192.168.20.1    | 255.255.255.0   | Static     | VLAN20 gateway      |
| R2      | Gi0/2      | 10.0.0.2        | 255.255.255.0   | Static     | Link to R1          |
| DNS-SRV | NIC        | 10.0.0.53       | 255.255.255.0   | Static     | GW 10.0.0.1         |
| PC-A    | NIC        | DHCP            | DHCP            | Dynamic    | VLAN10 — expect /24 |
| PC-B    | NIC        | DHCP            | DHCP            | Dynamic    | VLAN10 — expect /24 |
| PC-C    | NIC        | DHCP            | DHCP            | Dynamic    | VLAN20 — expect /24 |
| PC-D    | NIC        | DHCP            | DHCP            | Dynamic    | VLAN20 — expect /24 |

---

## Part 1: Baseline Router Configuration

### Step 1: Configure R1 as DHCP Server Router

```text
R1(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 10.0.0.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.2
R1(config)# ip route 192.168.20.0 255.255.255.0 10.0.0.2
```

### Step 2: Configure R2 as Relay Router

```text
R2(config)# hostname R2
R2(config)# interface GigabitEthernet0/0
R2(config-if)# ip address 192.168.10.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit
R2(config)# interface GigabitEthernet0/1
R2(config-if)# ip address 192.168.20.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit
R2(config)# interface GigabitEthernet0/2
R2(config-if)# ip address 10.0.0.2 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit
R2(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

### Step 3: Verify Routing Between R1 and R2

```text
R1# ping 10.0.0.2
R2# ping 10.0.0.1
```

Both pings must succeed before proceeding. This confirms the infrastructure is ready for DHCP relay.

---

## Part 2: DHCP Server Configuration on R1

### Step 4: Configure Excluded Addresses

Reserve gateway and server addresses so DHCP does not assign them dynamically:

```text
R1(config)# ip dhcp excluded-address 192.168.10.1 192.168.10.20
R1(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.20
```

### Step 5: Create DHCP Pool for VLAN10

```text
R1(config)# ip dhcp pool VLAN10_POOL
R1(dhcp-config)# network 192.168.10.0 255.255.255.0
R1(dhcp-config)# default-router 192.168.10.1
R1(dhcp-config)# dns-server 10.0.0.53 8.8.8.8
R1(dhcp-config)# domain-name lab.local
R1(dhcp-config)# lease 1
R1(dhcp-config)# exit
```

### Step 6: Create DHCP Pool for VLAN20

```text
R1(config)# ip dhcp pool VLAN20_POOL
R1(dhcp-config)# network 192.168.20.0 255.255.255.0
R1(dhcp-config)# default-router 192.168.20.1
R1(dhcp-config)# dns-server 10.0.0.53 8.8.8.8
R1(dhcp-config)# domain-name lab.local
R1(dhcp-config)# lease 1
R1(dhcp-config)# exit
```

### Step 7: Verify Pools Are Configured

```text
R1# show ip dhcp pool
```

Confirm both VLAN10_POOL and VLAN20_POOL appear with correct network and gateway entries.

---

## Part 3: DHCP Relay Configuration on R2

### Step 8: Apply ip helper-address to the VLAN10 Gateway Interface

The relay command goes on the interface facing the client subnet — where DHCP broadcasts arrive:

```text
R2(config)# interface GigabitEthernet0/0
R2(config-if)# ip helper-address 10.0.0.1
R2(config-if)# exit
```

### Step 9: Apply ip helper-address to the VLAN20 Gateway Interface

```text
R2(config)# interface GigabitEthernet0/1
R2(config-if)# ip helper-address 10.0.0.1
R2(config-if)# exit
```

### Step 10: Trigger DHCP on Client PCs

On each PC (PC-A through PC-D), open the IP configuration and set it to DHCP. In Packet Tracer use the Desktop tab > IP Configuration > DHCP radio button.

Expected results:

- PC-A and PC-B receive addresses in 192.168.10.21–192.168.10.254 (first 20 excluded)
- PC-C and PC-D receive addresses in 192.168.20.21–192.168.20.254
- Default gateway matches R2's interface for each VLAN
- DNS server field shows 10.0.0.53

### Step 11: Verify DHCP Bindings on R1

```text
R1# show ip dhcp binding
```

Expected output listing all four PCs with their MAC addresses, assigned IP addresses, and lease expiration times.

### Step 12: Verify Client Can Reach DNS Server

From PC-A, ping the DNS server:

```text
PC-A> ping 10.0.0.53
```

Expected result: 5 successful replies. This confirms the DHCP-assigned default gateway and the routing on R1 and R2 are working correctly.

---

## Part 4: DHCP Snooping on SW1

### Step 13: Enable DHCP Snooping Globally and Per VLAN

```text
SW1(config)# ip dhcp snooping
SW1(config)# ip dhcp snooping vlan 10
SW1(config)# ip dhcp snooping vlan 20
```

### Step 14: Trust the Uplink Port Facing R2

The port connecting SW1 to R2 carries DHCP server responses (Offer and ACK) relayed from R1. This port must be explicitly trusted:

```text
SW1(config)# interface GigabitEthernet0/24
SW1(config-if)# ip dhcp snooping trust
SW1(config-if)# exit
```

All other ports facing PCs remain untrusted by default.

### Step 15: Verify Snooping Configuration and Binding Table

```text
SW1# show ip dhcp snooping
SW1# show ip dhcp snooping binding
```

Confirm snooping is enabled for VLANs 10 and 20, Gi0/24 is marked Trusted, and the binding table shows entries for connected PCs.

---

## Part 5: Troubleshooting Scenarios

### Troubleshooting Scenario A — Missing Relay Agent

Remove the `ip helper-address` from R2 Gi0/0, then release and attempt to renew the DHCP lease on PC-A:

```text
R2(config)# interface GigabitEthernet0/0
R2(config-if)# no ip helper-address 10.0.0.1
```

On PC-A: change IP configuration to DHCP and observe the result.

Expected result: PC-A receives no IP address (shows 0.0.0.0 or APIPA 169.254.x.x after timeout).

Written question: Explain step by step why PC-A cannot get an IP address after removing the helper-address. Describe exactly what happens to the DHCP Discover broadcast when it arrives at R2 Gi0/0 without the helper configured.

Restore before continuing:

```text
R2(config)# interface GigabitEthernet0/0
R2(config-if)# ip helper-address 10.0.0.1
```

### Troubleshooting Scenario B — Pool Exclusion Error

Modify the excluded-address range to exclude nearly the entire VLAN20 pool:

```text
R1(config)# no ip dhcp excluded-address 192.168.20.1 192.168.20.20
R1(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.253
```

Release and renew DHCP on PC-C and PC-D. Observe the results.

Expected result: Only 192.168.20.254 remains available. One PC gets an address; the second fails.

Written question: Describe the output of `show ip dhcp pool` when the pool is exhausted. Identify the specific field that indicates remaining address availability. Explain how an overly broad excluded-address range can unintentionally exhaust an entire pool.

Restore by correcting the exclusion range:

```text
R1(config)# no ip dhcp excluded-address 192.168.20.1 192.168.20.253
R1(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.20
```

---

## Deliverables

Submit the following as a single PDF or Word document in Canvas:

1. Screenshot of `show ip dhcp pool` on R1 showing both pools configured
2. Screenshot of `show ip dhcp binding` on R1 showing all four PC leases
3. Screenshot of PC-A IP configuration showing DHCP-assigned address, gateway, and DNS server
4. Screenshot of successful ping from PC-A to 10.0.0.53
5. Screenshot of `show ip dhcp snooping` on SW1 confirming VLAN and trust configuration
6. Written answer for Troubleshooting Scenario A (4–6 sentences)
7. Written answer for Troubleshooting Scenario B (4–6 sentences)

---

## Grading Rubric

| Component                               | Points | Criteria                                                              |
|-----------------------------------------|--------|-----------------------------------------------------------------------|
| R1 DHCP server pools configured         | 15     | Both pools with correct network, gateway, DNS, and exclusions         |
| Relay agent configured on R2            | 15     | ip helper-address on both VLAN interfaces pointing to 10.0.0.1       |
| DHCP bindings verified                  | 15     | show ip dhcp binding shows all four PCs with correct subnets          |
| Client connectivity to DNS server       | 10     | Successful ping from PC-A to 10.0.0.53                               |
| DHCP snooping enabled and verified      | 20     | Snooping on both VLANs; uplink port trusted; binding table populated  |
| Troubleshooting Scenario A              | 12     | Correct explanation of relay mechanism and impact of removal          |
| Troubleshooting Scenario B              | 13     | Correct identification of pool exhaustion and show dhcp pool reading  |

Partial credit is awarded for demonstrably attempted but incomplete work.
