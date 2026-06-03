# Lab Activity: Module 09 — Network Services: DNS, DHCP, and NTP

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Overview

This lab has two parts. Part 1 uses command-line tools to investigate DNS resolution — querying record types, interpreting results, and tracing the resolution hierarchy. Part 2 uses Cisco Packet Tracer to configure a DHCP server on a router and verify that clients on two subnets receive correct addresses through a relay agent.

Estimated Time: 60–75 minutes

Required Tools:

- Windows Command Prompt or Linux/macOS Terminal (for Part 1)
- Cisco Packet Tracer 8.x (free download at netacad.com with a free account)

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Use nslookup to query A, AAAA, MX, NS, TXT, and PTR records for real domains.
2. Explain the difference between a non-authoritative answer and an authoritative answer.
3. Configure a DHCP scope on a Cisco router and exclude static device addresses.
4. Configure ip helper-address on a router interface to relay DHCP broadcasts to a central DHCP server.
5. Verify DHCP lease assignment and trace the DORA exchange in Packet Tracer simulation mode.

---

### Part 1: DNS Query Investigation

#### Step 1: Query an A Record

Open a Command Prompt (Windows) or Terminal (Linux/macOS) and run:

```bat
nslookup google.com
```

On Linux/macOS:

```bash
nslookup google.com
```

Record the output: the server address, the response IP addresses, and whether the answer is labeled "Non-authoritative answer."

#### Step 2: Query an MX Record

```bat
nslookup -type=MX gmail.com
```

Record the mail server hostnames and their priority values.

#### Step 3: Query an NS Record

```bat
nslookup -type=NS google.com
```

Record the authoritative name server hostnames returned.

#### Step 4: Query a TXT Record for SPF

```bat
nslookup -type=TXT google.com
```

Find the record beginning with "v=spf1" in the output.

#### Step 5: Perform a Reverse DNS Lookup

Choose one of the IP addresses returned in Step 1. Run:

```bat
nslookup 142.250.80.46
```

Replace the IP with one you received for google.com.

#### Step 6: Query an Alternate DNS Server

```bat
nslookup example.com 8.8.8.8
```

This queries Google's public DNS server directly instead of your default resolver.

Lab Questions — Part 1:

Question 1: What is the difference between a non-authoritative and an authoritative DNS answer? Which query returned a non-authoritative answer, and why?

Question 2: A user reports they cannot reach a company intranet site by name but can reach it by IP address. Which DNS diagnostic command would you run first, and what output would confirm the problem?

Question 3: Explain the full DNS resolution path that your resolver followed when you queried google.com in Step 1. Include each level of the hierarchy and what each server responded with.

Question 4: An email administrator needs to verify that an SPF record is published for their domain. Write the exact nslookup command to query the TXT record for the domain yourdomain.com and explain what a v=spf1 record means.

---

### Part 2: DHCP Server and Relay Agent Configuration in Packet Tracer

#### Part 2 Step 1: Build the Topology

Open Packet Tracer and create the following three-subnet topology:

Subnet A — Client LAN 1:

- Network: 192.168.10.0/24
- Router1 interface Fa0/0: 192.168.10.1/24
- PC1 and PC2 will receive DHCP assignments

Subnet B — Client LAN 2:

- Network: 192.168.20.0/24
- Router1 interface Fa0/1: 192.168.20.1/24
- PC3 will receive DHCP assignment

Server Subnet:

- Network: 10.0.0.0/30
- Router1 interface Fa1/0: 10.0.0.1/30
- DHCP-Server: 10.0.0.2/30 (static)

Connect PC1 and PC2 to a switch on Fa0/0 side; PC3 to a switch on Fa0/1 side; DHCP-Server directly to Router1 Fa1/0.

#### Part 2 Step 2: Configure Router1 Interfaces

```cisco
interface FastEthernet0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
!
interface FastEthernet0/1
 ip address 192.168.20.1 255.255.255.0
 no shutdown
!
interface FastEthernet1/0
 ip address 10.0.0.1 255.255.255.252
 no shutdown
```

#### Part 2 Step 3: Configure the DHCP Server

On the DHCP-Server device in Packet Tracer, click Services then DHCP.

Create two pools:

Pool 1 — for Subnet A:

- Pool name: LAN_A
- Default gateway: 192.168.10.1
- DNS server: 8.8.8.8
- Start IP: 192.168.10.100
- Subnet mask: 255.255.255.0
- Maximum users: 50

Pool 2 — for Subnet B:

- Pool name: LAN_B
- Default gateway: 192.168.20.1
- DNS server: 8.8.8.8
- Start IP: 192.168.20.100
- Subnet mask: 255.255.255.0
- Maximum users: 50

Enable the DHCP service on the server.

#### Part 2 Step 4: Configure DHCP Relay Agents

On Router1, configure ip helper-address on both client-facing interfaces:

```cisco
interface FastEthernet0/0
 ip helper-address 10.0.0.2
!
interface FastEthernet0/1
 ip helper-address 10.0.0.2
```

#### Part 2 Step 5: Test DHCP Assignment

On each PC, set IP Configuration to DHCP. PC1 and PC2 should receive addresses in 192.168.10.100 range; PC3 in 192.168.20.100 range.

Verify on each PC:

```bat
ipconfig /all
```

Record the IP address, subnet mask, default gateway, and DNS server for each PC.

#### Part 2 Step 6: Observe DORA in Simulation Mode

Switch Packet Tracer to Simulation mode. Filter to DHCP only. Click Fast Forward to generate DHCP traffic. Observe the Discover, Offer, Request, ACK sequence.

Lab Questions — Part 2:

Question 5: Explain why ip helper-address is required. What happens to a DHCP Discover broadcast at a router interface if ip helper-address is not configured?

Question 6: PC1 and PC3 are on different subnets but use the same DHCP server. How does the server know which pool to assign to each client?

Question 7: In simulation mode, was the DHCP Discover sent as a broadcast or unicast? Was the ACK sent as broadcast or unicast? Explain the technical reason for each.

Question 8: A rogue DHCP server on the network responds to DHCP Discovers before the legitimate server. What attack is this, and which switch security feature prevents it?

Question 9: What is the disadvantage of setting a very short DHCP lease time (for example, 2 hours)?

Question 10: An administrator needs a specific device to always receive the same IP address via DHCP. What DHCP feature accomplishes this, and what information must be configured?

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Screenshots — all six nslookup command outputs.
2. Part 1 Written Responses — answers to Questions 1 through 4.
3. Part 2 Topology Screenshot — completed Packet Tracer topology.
4. Part 2 DHCP Verification — ipconfig /all output from PC1, PC2, and PC3.
5. Part 2 Simulation Screenshot — DORA sequence in Simulation mode.
6. Part 2 Written Responses — answers to Questions 5 through 10.

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1 nslookup screenshots — all six commands shown | 12 |
| Question 1 — non-authoritative vs. authoritative explained | 8 |
| Question 2 — correct diagnostic command described | 8 |
| Question 3 — DNS resolution path with all hierarchy levels | 8 |
| Question 4 — correct nslookup syntax and SPF explanation | 8 |
| Part 2 topology screenshot | 8 |
| Part 2 DHCP verification — correct IPs from correct pools | 8 |
| Part 2 simulation screenshot — DORA sequence visible | 8 |
| Question 5 — ip helper-address function explained | 6 |
| Question 6 — subnet identification in relayed DHCP explained | 6 |
| Question 7 — broadcast vs. unicast reasoning correct | 6 |
| Question 8 — rogue DHCP and DHCP Snooping described | 6 |
| Question 9 — short lease disadvantage described | 4 |
| Question 10 — DHCP reservation described | 4 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab09_Firstname_Lastname.pdf

Submit to the Module 09 Lab assignment in the course LMS before the posted deadline.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
