# Lab Activity: Module 10 — Network Services

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Overview

This lab has two parts. Part 1 uses nslookup to investigate DNS record types, the resolution hierarchy, and the difference between authoritative and non-authoritative answers — extending the DNS work from Module 09. Part 2 uses Cisco Packet Tracer to configure a full network services topology: a centralized DHCP server serving two client VLANs through relay agents, with DNS server assignment delivered via DHCP options.

Estimated Time: 60–75 minutes

Required Tools:

- Windows Command Prompt or Linux/macOS Terminal (for Part 1)
- Cisco Packet Tracer 8.x (free download at netacad.com with a free account)

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Query DNS record types (A, AAAA, MX, NS, TXT, PTR, SOA) using nslookup and interpret the output.
2. Identify authoritative vs. non-authoritative answers and explain the difference.
3. Configure a DHCP server with multiple scopes, exclusions, reservations, and scope options.
4. Configure `ip helper-address` on multiple router interfaces to relay DHCP across subnet boundaries.
5. Verify DHCP assignment and confirm correct scope options are delivered to clients.
6. Explain DHCP Snooping configuration concepts and identify trusted vs. untrusted ports.

---

### Part 1: DNS Investigation Using nslookup

#### Step 1: Query an A Record

Open a Command Prompt (Windows) or Terminal (Linux/macOS) and run:

```text
nslookup txwes.edu
```

Record:

- The DNS server name and IP address shown at the top (this is your resolver)
- The IP address(es) returned for txwes.edu
- Whether the output is labeled "Non-authoritative answer"

#### Step 2: Query an AAAA Record

```text
nslookup -type=AAAA google.com
```

Record whether an IPv6 address is returned. Note that many organizations have both A and AAAA records, while others are IPv4-only.

#### Step 3: Query an MX Record

```text
nslookup -type=MX txwes.edu
```

Record:

- The mail exchanger hostname(s) returned
- The priority value associated with each mail exchanger

#### Step 4: Query NS Records

```text
nslookup -type=NS txwes.edu
```

Record the authoritative name server hostnames returned. These are the servers that hold the authoritative zone data for txwes.edu.

#### Step 5: Query a TXT Record

```text
nslookup -type=TXT txwes.edu
```

Find the record beginning with `v=spf1` in the output. Record the full SPF record text.

#### Step 6: Perform a Reverse DNS Lookup (PTR)

Use one of the IP addresses returned in Step 1:

```text
nslookup 54.160.205.12
```

Replace the IP address with one you actually received for txwes.edu. Record the hostname returned, if any.

#### Step 7: Query an Authoritative Name Server Directly

Use one of the NS server names from Step 4:

```text
nslookup txwes.edu ns1.txwes.edu
```

Replace `ns1.txwes.edu` with the actual NS server name you found. Compare this output to Step 1 — is this answer labeled non-authoritative?

#### Step 8: Query an SOA Record

```text
nslookup -type=SOA txwes.edu
```

Record the primary name server, the serial number, and the refresh/retry/expire values.

---

### Lab Questions — Part 1

Question 1: In Step 1, the answer was labeled "Non-authoritative answer." In Step 7, when you queried the authoritative name server directly, was it still labeled non-authoritative? Explain the technical reason for the difference.

Question 2: The MX record you found in Step 3 points to a mail server hostname. What DNS record type would a sending mail server need to query next in order to deliver email, and why?

Question 3: What is the significance of the MX priority value? If txwes.edu had two MX records with priorities of 10 and 20, which mail server would be tried first, and what happens if it is unreachable?

Question 4: Explain what the `v=spf1` TXT record you found in Step 5 is used for. What attack does it help mitigate?

Question 5: The SOA record's serial number is critical for DNS zone replication. Explain how a secondary DNS server uses the SOA serial number to determine whether a zone transfer is needed.

---

### Part 2: DHCP Server and Relay Agent Configuration in Packet Tracer

#### Part 2 Step 1: Build the Topology

Open Packet Tracer and create the following topology:

Router1 (central router) connects three networks:

Network 1 — VLAN 10 Client LAN:

- Interface Fa0/0: 10.10.10.1/24
- Switch1 connected to Fa0/0
- PC1, PC2, PC3 connected to Switch1 (will receive DHCP)

Network 2 — VLAN 20 Client LAN:

- Interface Fa0/1: 10.10.20.1/24
- Switch2 connected to Fa0/1
- PC4, PC5 connected to Switch2 (will receive DHCP)

Network 3 — Server Network:

- Interface Fa1/0: 192.168.1.1/30
- DHCP-Server connected to Fa1/0 with static IP 192.168.1.2/30
- DNS-Server connected to Fa1/0 via Switch3 with static IP 192.168.1.5/29 (adjust as needed)

#### Part 2 Step 2: Configure Router1 Interfaces

```text
interface FastEthernet0/0
 ip address 10.10.10.1 255.255.255.0
 no shutdown
!
interface FastEthernet0/1
 ip address 10.10.20.1 255.255.255.0
 no shutdown
!
interface FastEthernet1/0
 ip address 192.168.1.1 255.255.255.252
 no shutdown
```

#### Part 2 Step 3: Configure the DHCP Server

On the DHCP-Server device in Packet Tracer, click Services then DHCP.

Create two pools:

Pool 1 — for VLAN 10 (10.10.10.0/24):

- Pool name: VLAN10_CLIENTS
- Default gateway: 10.10.10.1
- DNS server: 192.168.1.5 (the DNS server in the server network)
- Start IP: 10.10.10.50
- Subnet mask: 255.255.255.0
- Maximum users: 100

Pool 2 — for VLAN 20 (10.10.20.0/24):

- Pool name: VLAN20_CLIENTS
- Default gateway: 10.10.20.1
- DNS server: 192.168.1.5
- Start IP: 10.10.20.50
- Subnet mask: 255.255.255.0
- Maximum users: 50

Enable the DHCP service on the server.

#### Part 2 Step 4: Configure DHCP Relay Agents

On Router1, add `ip helper-address` to both client-facing interfaces:

```text
interface FastEthernet0/0
 ip helper-address 192.168.1.2
!
interface FastEthernet0/1
 ip helper-address 192.168.1.2
```

#### Part 2 Step 5: Simulate a Reservation

On the DHCP-Server, create a static binding (reservation) for PC1:

- Open PC1 and note its MAC address from its Config tab
- In the DHCP server, create a static mapping:
  - MAC: (the MAC address you noted)
  - IP: 10.10.10.10

Set PC1 to DHCP mode. Verify it receives 10.10.10.10 specifically (not a dynamic address from the pool).

#### Part 2 Step 6: Set PC2–PC5 to DHCP and Verify

On each remaining PC, set IP Configuration to DHCP.

Record the IP address, subnet mask, default gateway, and DNS server received by each PC. Verify:

- PC2 and PC3 receive addresses in 10.10.10.50+ range with gateway 10.10.10.1
- PC4 and PC5 receive addresses in 10.10.20.50+ range with gateway 10.10.20.1
- All PCs show DNS server 192.168.1.5

Fill in the verification table:

| Device | Assigned IP | Subnet Mask | Default Gateway | DNS Server | Scope (Expected) |
|--------|------------|-------------|-----------------|------------|------------------|
| PC1 (reservation) | | | | | VLAN10 (10.10.10.10) |
| PC2 | | | | | VLAN10 |
| PC3 | | | | | VLAN10 |
| PC4 | | | | | VLAN20 |
| PC5 | | | | | VLAN20 |

#### Part 2 Step 7: Test Cross-Subnet Connectivity

From PC1, use the ping tool:

- Ping 10.10.10.1 (Router1 Fa0/0) — should succeed
- Ping 10.10.20.1 (Router1 Fa0/1) — should succeed
- Ping 192.168.1.2 (DHCP Server) — should succeed
- Ping PC4's assigned IP — should succeed (routing through Router1)

Record whether each ping succeeded or failed.

#### Part 2 Step 8: Observe DORA in Simulation Mode

Switch Packet Tracer to Simulation mode. Filter to DHCP only. Reset PC3's IP Configuration to Static and then back to DHCP to force a new DORA exchange. Click Step Forward to observe:

1. PC3 broadcasts DHCP Discover
2. Router1 intercepts and unicasts it to DHCP-Server
3. DHCP-Server sends Offer back to Router1
4. Router1 forwards Offer to PC3
5. PC3 broadcasts DHCP Request
6. DHCP-Server sends ACK

Record the source and destination IP addresses for each of the four DHCP messages at the router interface.

---

### Lab Questions — Part 2

Question 6: In Step 4, you configured `ip helper-address 192.168.1.2` on both client-facing interfaces. Explain specifically what happens to a DHCP Discover broadcast from PC4 (on the 10.10.20.0/24 network) when it reaches Router1's Fa0/1 interface. What does the relay agent change about the packet before forwarding it to the DHCP server?

Question 7: The DHCP server has two pools — one for 10.10.10.0/24 and one for 10.10.20.0/24. Both pools are on the same server. How does the server know which pool to use for PC4 (on VLAN 20) vs. PC2 (on VLAN 10)? Reference the specific field in the relayed DHCP packet.

Question 8: In Step 5, you created a DHCP reservation for PC1. What two pieces of information are required to create a DHCP reservation, and why does the device need to continue using DHCP even with a reservation instead of just having a static IP configured directly?

Question 9: In the DORA simulation (Step 8), the DHCP Request message was sent as a broadcast, not a unicast directly to the DHCP server that made the Offer. Explain why the client broadcasts the Request rather than unicasting it.

Question 10: A network administrator is concerned that a rogue device on Switch1 could act as a DHCP server and assign incorrect addresses to PC2 and PC3 before the legitimate DHCP server responds. What Cisco switch security feature prevents this, and how would you configure it? Identify which port(s) should be trusted and which should be untrusted.

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Screenshots — nslookup output for all eight commands (Steps 1–8).
2. Part 1 Written Responses — answers to Questions 1 through 5.
3. Part 2 Topology Screenshot — completed Packet Tracer topology with all devices labeled.
4. Part 2 DHCP Verification Table — completed table from Step 6 with actual values.
5. Part 2 Simulation Screenshots — DORA sequence showing all four message types.
6. Part 2 Connectivity Test Results — results of the four pings from Step 7.
7. Part 2 Written Responses — answers to Questions 6 through 10.

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1 nslookup screenshots (Steps 1–8) | 16 |
| Question 1 — authoritative vs. non-authoritative explained | 8 |
| Question 2 — follow-up record type for MX delivery | 6 |
| Question 3 — MX priority and failover behavior | 6 |
| Question 4 — SPF record purpose and attack mitigated | 6 |
| Question 5 — SOA serial and zone transfer decision | 6 |
| Part 2 topology screenshot | 5 |
| Part 2 DHCP verification table — all values correct | 8 |
| Part 2 simulation screenshots — DORA visible | 6 |
| Part 2 connectivity test results | 5 |
| Question 6 — relay agent packet modification | 8 |
| Question 7 — scope selection by giaddr | 6 |
| Question 8 — reservation requirements and rationale | 6 |
| Question 9 — broadcast Request rationale | 6 |
| Question 10 — DHCP Snooping configuration | 6 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab10_Firstname_Lastname.pdf

Submit to the Module 10 Lab assignment in the course LMS before the posted deadline.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
