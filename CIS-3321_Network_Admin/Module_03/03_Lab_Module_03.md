# Lab Activity: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Lab Overview

**Lab Title:** IPv4 Subnetting Calculations and IP Configuration Verification

**Format:** Part 1 — Written Subnet Calculations; Part 2 — Cisco Packet Tracer Simulation

**Estimated Time:** 75–90 minutes

**Points:** 100 points total

**Prerequisites:**

- Module 03 video lectures watched (both Part 1 and Part 2)
- Module 03 Reading Guide reviewed, especially Sections 4–7 (subnet table and practice problems)
- Pencil and paper for Part 1 calculations
- Cisco Packet Tracer installed for Part 2

**Learning Objectives:**

By completing this lab, you will be able to:

- Apply the four-step subnet calculation process to determine network address, broadcast address, and usable host range
- Verify that a given host IP falls within a valid subnet range
- Design a subnetting scheme to meet a given host count requirement
- Configure IP addresses and subnet masks in Cisco Packet Tracer
- Test inter-host connectivity using ping to validate subnetting decisions

---

### Background

Subnetting is a critical skill for network administrators. In the real world, you will regularly be asked to design IP addressing schemes, troubleshoot hosts that are misconfigured on the wrong subnet, and determine whether two hosts can communicate without a router. This lab makes those skills practical by combining calculation exercises with hands-on configuration and testing.

---

### Part 1: Subnet Calculation Exercises

**Instructions:** For each problem, use the four-step process from the reading guide. Show your work for each step. All calculations must be completed by hand — do not use an automated subnet calculator.

**The four-step process:**

1. Identify the CIDR prefix; calculate block size (256 minus interesting mask octet).
2. Find the network address (largest multiple of block size ≤ interesting octet of IP).
3. Find the broadcast address (network octet + block size - 1).
4. Determine usable host range (network + 1 through broadcast - 1).

---

#### Problem 1

Given: IP address 192.168.10.45, subnet mask 255.255.255.224 (/27)

Answer each of the following:

A. Block size: ____________________

B. Network address: ____________________

C. Broadcast address: ____________________

D. First usable host: ____________________

E. Last usable host: ____________________

F. Number of usable hosts: ____________________

G. Is 192.168.10.62 in the same subnet as 192.168.10.45? Explain: ____________________

---

#### Problem 2

Given: IP address 172.16.4.200, subnet mask 255.255.255.192 (/26)

A. Block size: ____________________

B. Network address: ____________________

C. Broadcast address: ____________________

D. First usable host: ____________________

E. Last usable host: ____________________

F. Number of usable hosts: ____________________

G. Is 172.16.4.129 in the same subnet as 172.16.4.200? Explain: ____________________

---

#### Problem 3

Given: IP address 10.0.0.100, subnet mask 255.255.255.240 (/28)

A. Block size: ____________________

B. Network address: ____________________

C. Broadcast address: ____________________

D. First usable host: ____________________

E. Last usable host: ____________________

F. Number of usable hosts: ____________________

---

#### Problem 4

A network design requires connecting exactly two routers on a point-to-point link. The address space is 192.168.50.0/24. What is the most efficient subnet mask to use? Provide:

A. CIDR prefix: ____________________

B. Subnet mask: ____________________

C. Network address (use the first available block): ____________________

D. Router A interface address: ____________________

E. Router B interface address: ____________________

F. Broadcast address: ____________________

G. Number of usable hosts: ____________________

---

#### Problem 5

A company needs to subnet 192.168.20.0/24 to create at least 6 subnets, each supporting at least 25 hosts. Identify:

A. Minimum prefix length to create at least 6 subnets: ____________________

B. Subnet mask in dotted-decimal: ____________________

C. Hosts per subnet (usable): ____________________

D. List all subnet network addresses within 192.168.20.0/24: ____________________

---

#### Problem 6

Determine whether the following host pairs are on the same subnet or different subnets. For each pair, show the network address of each host.

A. 192.168.1.33/27 and 192.168.1.62/27 — Same or different subnet? ____________________

B. 10.0.5.50/28 and 10.0.5.65/28 — Same or different subnet? ____________________

C. 172.16.10.130/26 and 172.16.10.191/26 — Same or different subnet? ____________________

---

### Part 2: Packet Tracer IP Configuration and Verification

**Objective:** Build a two-subnet topology in Packet Tracer, assign IP addresses based on your subnetting calculations, and verify connectivity.

#### Scenario Description

Your company uses the network block 192.168.5.0/24. You need to create two separate subnets:

- Subnet A: Must support at least 50 hosts
- Subnet B: Must support at least 25 hosts

You will subnet 192.168.5.0/24 to create these two subnets, then configure and test the addresses in Packet Tracer.

#### Step 1: Plan Your Subnets

Before opening Packet Tracer, complete the planning table:

| Subnet   | Prefix | Network Address | Broadcast     | Host Range                 | Max Hosts |
|----------|--------|-----------------|---------------|----------------------------|-----------|
| Subnet A |        |                 |               |                            |           |
| Subnet B |        |                 |               |                            |           |

Note: For Subnet A supporting 50+ hosts, a /26 (62 hosts) is the smallest suitable prefix. For Subnet B supporting 25+ hosts, a /27 (30 hosts) works.

#### Step 2: Build the Topology in Packet Tracer

1. Place four PCs on the workspace: PC1, PC2 (for Subnet A) and PC3, PC4 (for Subnet B).
2. Place one router (use Cisco 1941 or 2901) in the center.
3. Connect PC1 and PC2 to the router's GigabitEthernet0/0 interface (or via a switch).
4. Connect PC3 and PC4 to the router's GigabitEthernet0/1 interface (or via a switch).

#### Step 3: Configure IP Addresses on PCs

Using your planning table, assign addresses as follows:

- PC1: First usable host address in Subnet A, correct mask, gateway = router's Gi0/0 address
- PC2: Second usable host address in Subnet A, correct mask, gateway = router's Gi0/0 address
- PC3: First usable host address in Subnet B, correct mask, gateway = router's Gi0/1 address
- PC4: Second usable host address in Subnet B, correct mask, gateway = router's Gi0/1 address

#### Step 4: Configure Router Interfaces

Click the router, go to the CLI tab, and configure each interface:

```
enable
configure terminal
interface GigabitEthernet0/0
 ip address [Subnet A gateway IP] [Subnet A mask]
 no shutdown
interface GigabitEthernet0/1
 ip address [Subnet B gateway IP] [Subnet B mask]
 no shutdown
```

#### Step 5: Test Connectivity

From PC1, ping PC2 (same subnet):

`ping 192.168.5.[PC2 address]`

From PC1, ping PC3 (different subnet, through router):

`ping 192.168.5.[PC3 address]`

Record all ping results in the table below:

| Source | Destination | Packets Sent | Packets Received | Result |
|--------|-------------|--------------|------------------|--------|
| PC1    | PC2         | 4            |                  |        |
| PC1    | PC3         | 4            |                  |        |
| PC3    | PC4         | 4            |                  |        |
| PC3    | PC1         | 4            |                  |        |

---

### Deliverables

Submit the following to the Canvas assignment dropbox:

**Deliverable 1 (40 points):** Completed Part 1 calculation worksheet. Show your work for each step of each problem. Scan or photograph your handwritten work, or type the answers clearly.

**Deliverable 2 (20 points):** Screenshot of the completed Packet Tracer topology showing all four PCs and the router with green link lights.

**Deliverable 3 (20 points):** Screenshot showing successful ping results between PC1–PC2 (same subnet) and PC1–PC3 (cross-subnet through router).

**Deliverable 4 (20 points):** A typed reflection (100–150 words) explaining how the router enables communication between Subnet A and Subnet B, referencing the specific OSI layer and IP addressing concepts involved.

---

### Grading Rubric

| Deliverable | Points | Full Credit Criteria |
|-------------|--------|----------------------|
| Subnet calculation worksheet | 40 | All 6 problems completed; four-step work shown; answers correct |
| Topology screenshot | 20 | 4 PCs and router visible; green link lights; devices correctly connected to separate subnets |
| Ping verification screenshot | 20 | Successful pings shown for same-subnet and cross-subnet tests |
| Written reflection | 20 | 100–150 words; correctly identifies Layer 3 routing and IP addressing concepts |
| **Total** | **100** | |

---

### Common Issues and Fixes

**Issue:** Ping fails between PC1 and PC3 (cross-subnet).

**Fix:** Verify that the router interfaces are configured with the correct IP address from each subnet's gateway address, that both interfaces are in the "no shutdown" state, and that each PC has the correct default gateway address pointing to the router's interface on their subnet.

**Issue:** Ping fails between PC1 and PC2 (same subnet).

**Fix:** Verify that both PCs are configured with addresses in the same subnet (same network address after applying the mask) and the same subnet mask. Use the four-step process to confirm both addresses fall within the same host range.

**Issue:** Calculation answers do not match expected values.

**Fix:** Verify that you are subtracting the correct mask octet from 256 to get the block size, and that you are finding the largest multiple of the block size that does not exceed (not equal to) the interesting octet of the IP address.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
