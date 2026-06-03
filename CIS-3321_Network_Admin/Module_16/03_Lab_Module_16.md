# Lab Activity: Module 16 — Network+ N10-008 Exam Preparation Self-Assessment

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Network+ (N10-008)

**Estimated Time:** 90 minutes

**Format:** Written self-assessment, scenario analysis, and timed practice

---

## Overview

This lab is your final exam preparation self-assessment. It does not use Packet Tracer — it uses your brain. Working through this lab under near-exam conditions is one of the highest-value preparation activities you can do in the days before sitting for Network+.

Complete each part in order. Do not skip ahead. Do not look up answers until you have written your best response.

---

## Part 1: Port Number Sprint

### Objective

Recall well-known port numbers from memory without reference material.

### Instructions

Without looking at the Reading Guide or any notes, write the port number and transport protocol (TCP, UDP, or both) for each service listed below. After completing the list, check your answers against the port table in the Module 16 Reading Guide.

### Service List

Write your answers on paper or in a text editor before checking:

1. FTP Control
2. FTP Data
3. SSH
4. Telnet
5. SMTP
6. DNS
7. DHCP server
8. TFTP
9. HTTP
10. POP3
11. NTP
12. IMAP
13. SNMP queries
14. SNMP traps
15. LDAP
16. HTTPS
17. SMB
18. Syslog
19. LDAPS
20. IMAPS
21. POP3S
22. RDP
23. SIP
24. SIP over TLS

### Scoring

Count your correct answers (port number + protocol both required for full credit).

- 22–24 correct: Exam-ready on ports
- 18–21 correct: Review the 3–6 you missed; you are close
- Below 18: Spend 20 minutes with flash cards on the port table before exam day

---

## Part 2: Subnetting Under Pressure

### Part 2 Objective

Perform subnet calculations at the speed required on the actual exam.

### Part 2 Instructions

Set a timer for 8 minutes. Solve all five problems before the timer expires. Show your work.

### Problems

#### Problem 1

A host has IP address 192.168.10.50 and subnet mask 255.255.255.224.

- What is the network address?
- What is the broadcast address?
- What is the usable host range?
- How many usable hosts does this subnet support?

#### Problem 2

You need to subnet 10.0.0.0/8 to support exactly 500 hosts per subnet. What is the minimum prefix length (/XX) that supports this requirement?

#### Problem 3

Your company is allocated the block 172.16.0.0/16. You need to create exactly 8 equal subnets. What prefix length do you use and how many usable hosts does each subnet support?

#### Problem 4

A point-to-point WAN link requires exactly 2 usable IP addresses. What subnet mask do you use and what CIDR notation does that represent?

#### Problem 5

A host at 192.168.100.200/27 cannot communicate with a host at 192.168.100.230/27. Without performing any calculation, explain in one sentence why these hosts cannot communicate at Layer 3 without a router.

### Part 2 Answer Key

Check your work after the timer expires:

- Problem 1: Network = 192.168.10.32; Broadcast = 192.168.10.63; Range = .33–.62; 30 hosts (/27)
- Problem 2: /23 supports 510 hosts (2^9 - 2 = 510)
- Problem 3: /19 (adds 3 bits = 8 subnets); each supports 8,190 hosts (2^13 - 2)
- Problem 4: 255.255.255.252 = /30
- Problem 5: 192.168.100.200/27 is in the .193–.222 subnet; 192.168.100.230/27 is in the .225–.254 subnet — they are in different subnets

---

## Part 3: OSI Layer Identification Drill

### Part 3 Objective

Map symptoms and technologies to the correct OSI layer under timed conditions.

### Part 3 Instructions

For each item below, identify the OSI layer number and name. Set a 5-minute timer. Do not refer to notes.

### Items

1. A frame is tagged with an 802.1Q VLAN ID
2. An IP packet is routed between two subnets
3. The physical wire carries electrical signals
4. TCP establishes a three-way handshake
5. SSL/TLS negotiates an encryption cipher suite
6. DNS resolves a hostname to an IP address
7. ARP resolves an IP address to a MAC address
8. STP elects a Root Bridge
9. A switch forwards a frame based on its MAC address table
10. OSPF distributes routing updates between routers

### Part 3 Answer Key

1. Layer 2 (Data Link) — 802.1Q is a Data Link standard
2. Layer 3 (Network) — routing is a Network layer function
3. Layer 1 (Physical) — electrical signals are Physical layer
4. Layer 4 (Transport) — TCP handshake is Transport layer
5. Layer 6 (Presentation) — TLS is Presentation layer encryption negotiation
6. Layer 7 (Application) — DNS is an Application layer service
7. Layer 2 (Data Link) — ARP resolves MAC addresses (operates at Data Link, though it straddles 2/3)
8. Layer 2 (Data Link) — STP operates on Ethernet frames
9. Layer 2 (Data Link) — MAC address table forwarding is Data Link
10. Layer 3 (Network) — OSPF is a Network layer routing protocol

---

## Part 4: Troubleshooting Scenario — Seven-Step Application

### Part 4 Objective

Apply the CompTIA seven-step troubleshooting model to a realistic scenario.

### Scenario

On Tuesday morning, three users in the Accounting department call the help desk. They cannot access the company's internal accounting application at 10.10.5.20. Other users on the same floor have no issues. The three affected users can browse the internet normally and receive email. The accounting application uses HTTPS on port 8443. All three affected users are on the same switch, connected to ports 9, 10, and 11 on SW-ACC-03. The other users on the floor are connected to SW-ACC-03 ports 1 through 8 on a different VLAN.

### Task

On paper, document your complete troubleshooting response using all seven CompTIA steps. For each step, write at least two sentences explaining what you would do at that step and why.

Include at least:

- Step 2: At least three distinct theories of probable cause, ranked by likelihood
- Step 3: The specific command(s) you would run to test your most likely theory
- Step 4: A rollback plan for your proposed solution
- Step 7: The minimum information required in the documentation record

### Debrief Questions

After writing your response, consider:

- What symptom pattern suggests the problem is Layer 2 (VLAN) rather than Layer 3 (routing)?
- What command would you run on SW-ACC-03 to verify VLAN assignments for ports 9–11?
- What command would you run to verify port 8443 is reachable from an affected host?

---

## Part 5: Protocol Matching Exercise

### Part 5 Objective

Match authentication and security protocols to their key characteristics.

### Part 5 Instructions

Match each item in Column A to its description in Column B. Write your answers before checking.

### Column A

1. RADIUS
2. TACACS+
3. 802.1X
4. SNMPv3
5. IPsec Tunnel mode
6. SSL/TLS VPN
7. WPA3/SAE
8. LDAPS

### Column B

A. Port 49, TCP, Cisco-preferred for device administration, encrypts entire payload

B. Port 443, clientless or full-tunnel, traverses most firewalls

C. Port 1812/1813, UDP, centralized network access authentication, encrypts only the password

D. Uses EAP; three components: supplicant, authenticator, authentication server

E. Encrypts the entire original IP packet including headers; used for site-to-site VPNs

F. Adds authentication and encryption to network device monitoring; uses ports 161/162

G. Resistant to offline dictionary attacks; uses Simultaneous Authentication of Equals

H. LDAP over TLS; port 636; encrypted directory queries

### Part 5 Answer Key

1-C, 2-A, 3-D, 4-F, 5-E, 6-B, 7-G, 8-H

---

## Part 6: Timed Practice Review

### Part 6 Objective

Simulate exam time pressure on scenario-style questions.

### Part 6 Instructions

Set a timer for 20 minutes. Answer the following scenario questions in order. Write your answer and a one-sentence explanation before moving to the next question. Stop when the timer expires.

### Scenarios

#### Scenario 1

A network administrator notices that all traffic between two switches is taking the same slow path even though four physical links exist between the switches. Three of the four links show as blocking in the switch output. What is the most likely cause?

#### Scenario 2

A user reports they can access all internal resources but cannot reach any internet sites. They receive a 169.254.x.x IP address. What is the most likely Layer 3 issue and what command confirms it?

#### Scenario 3

After a router configuration change, the OSPF routes are gone from the routing table and only directly connected and static routes remain. The change removed the `network` statement from the OSPF process. What administrative distance value would a new static route to the same destination need to have to be preferred over a reinstated OSPF route?

#### Scenario 4

A wireless user on 2.4 GHz reports intermittent disconnections during the workday. A Wi-Fi analyzer shows the AP is on channel 6 and a neighboring company's AP is also on channel 6 at -65 dBm. What is the most appropriate remediation?

#### Scenario 5

A company is replacing its legacy WAN with SD-WAN. The primary driver is that branch offices use three ISP connections — fiber, cable broadband, and 4G LTE — but traffic currently uses only the fiber link because all routes point to it. What SD-WAN capability directly solves this problem?

### Debrief

Review your answers after the timer:

- Scenario 1: STP is blocking redundant links; configure EtherChannel (LACP) to bundle the links into one logical link
- Scenario 2: DHCP failure; `ipconfig /all` confirms 169.254.x.x (APIPA) address
- Scenario 3: Less than 110 (OSPF AD); a static route with AD 1 would always be preferred over OSPF AD 110
- Scenario 4: Change the AP to a non-overlapping channel (1 or 11) or migrate the user to 5 GHz
- Scenario 5: Application-aware dynamic path selection across multiple WAN transports

---

## Submission

There is nothing to submit for this lab. The value is entirely in the doing — working through each part honestly, checking your answers accurately, and identifying the gaps you need to close before exam day.

Record your weak areas from each part and spend your remaining study time on those specific topics.

Good luck.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
