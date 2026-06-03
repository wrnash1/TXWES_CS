# Lab Activity: Module 08 — Network Security Concepts

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

### Overview

This lab has two parts. Part 1 uses Cisco Packet Tracer to build a DMZ network architecture with two firewalls and apply basic access control lists that enforce a security policy. Part 2 is an ARP analysis exercise using Wireshark, where you will capture ARP traffic on your local network, identify normal and potentially anomalous ARP behavior, and practice identifying the indicators of ARP poisoning in a capture file.

Estimated Time: 60–75 minutes

Required Tools:

- Cisco Packet Tracer 8.x (free at netacad.com with a free account)
- Wireshark (free at wireshark.org)
- Windows, Linux, or macOS with an active network connection

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Build a two-firewall DMZ topology in Packet Tracer.
2. Apply ACL rules that implement a real-world DMZ security policy.
3. Verify that traffic permitted by policy flows correctly and that prohibited traffic is blocked.
4. Capture and interpret ARP traffic in Wireshark.
5. Identify the indicators of ARP poisoning in a packet capture.
6. Explain how Dynamic ARP Inspection would prevent the attack.

---

### Part 1: DMZ Architecture in Cisco Packet Tracer

### Part 1A: Build the Topology

Open Packet Tracer and build the following topology:

Internet Zone (outside):

- 1 PC labeled "Internet-Host" — IP: 203.0.113.100 /24, Gateway: 203.0.113.1

Outer Firewall (Router0):

- GigabitEthernet0/0 (outside/internet): 203.0.113.1 /24
- GigabitEthernet0/1 (DMZ): 10.10.10.1 /24

DMZ Zone:

- 1 Server labeled "Web-Server" — IP: 10.10.10.10 /24, Gateway: 10.10.10.1

Inner Firewall (Router1):

- GigabitEthernet0/0 (DMZ): 10.10.10.2 /24
- GigabitEthernet0/1 (internal LAN): 192.168.1.1 /24

Internal LAN Zone:

- 1 PC labeled "Internal-Host" — IP: 192.168.1.10 /24, Gateway: 192.168.1.1
- 1 Server labeled "DB-Server" — IP: 192.168.1.20 /24, Gateway: 192.168.1.1

Connect devices:

- Internet-Host FastEthernet → Router0 GigabitEthernet0/0
- Router0 GigabitEthernet0/1 → Web-Server FastEthernet (via switch if needed)
- Router0 GigabitEthernet0/1 also connects to Router1 GigabitEthernet0/0 (same DMZ subnet 10.10.10.0/24)
- Router1 GigabitEthernet0/1 → Internal-Host and DB-Server (via switch)

---

### Part 1B: Configure Static Routing

On Router0 (Outer Firewall), add a route to the internal LAN via Router1:

```text
ip route 192.168.1.0 255.255.255.0 10.10.10.2
```

On Router1 (Inner Firewall), add a default route to the internet via Router0:

```text
ip route 0.0.0.0 0.0.0.0 10.10.10.1
```

---

### Part 1C: Test Connectivity Without ACLs

Before applying security rules, verify that all devices can communicate:

From Internet-Host, ping Web-Server (10.10.10.10) — should succeed.

From Internet-Host, ping DB-Server (192.168.1.20) — should succeed (no rules yet).

From Web-Server, ping DB-Server (192.168.1.20) — should succeed.

From Internal-Host, ping Web-Server (10.10.10.10) — should succeed.

Record all ping results. Note that without security rules, the internet can reach the internal database server directly — this is the security problem the DMZ architecture must solve.

---

### Part 1D: Apply the DMZ Security Policy

Now apply the following security policy using ACLs:

Policy rules:

- Internet can reach Web-Server on TCP port 80 (HTTP) only
- Internet cannot directly reach Internal-Host or DB-Server
- Web-Server can reach DB-Server on TCP port 3306 (MySQL) only
- Internal-Host can reach Web-Server (any traffic)
- All other traffic not explicitly permitted is denied

On Router0, apply an inbound ACL on the outside interface (GigabitEthernet0/0) to control internet-to-DMZ traffic:

```text
ip access-list extended OUTSIDE-IN
 permit tcp any host 10.10.10.10 eq 80
 deny   ip any 192.168.1.0 0.0.0.255
 permit ip any any
!
interface GigabitEthernet0/0
 ip access-group OUTSIDE-IN in
```

On Router1, apply an inbound ACL on the DMZ-facing interface (GigabitEthernet0/0) to control DMZ-to-LAN traffic:

```text
ip access-list extended DMZ-TO-LAN
 permit tcp host 10.10.10.10 host 192.168.1.20 eq 3306
 deny   ip 10.10.10.0 0.0.0.255 192.168.1.0 0.0.0.255
 permit ip any any
!
interface GigabitEthernet0/0
 ip access-group DMZ-TO-LAN in
```

---

### Part 1E: Verify the Security Policy

After applying ACLs, repeat the connectivity tests:

Test 1: From Internet-Host, open a browser or send a simulated HTTP request to Web-Server on port 80 — should be permitted.

Test 2: From Internet-Host, ping DB-Server (192.168.1.20) — should be denied by the OUTSIDE-IN ACL.

Test 3: From Web-Server, attempt to connect to DB-Server on port 3306 — should be permitted by DMZ-TO-LAN ACL.

Test 4: From Web-Server, attempt to ping Internal-Host on port 22 (SSH) — should be denied.

Test 5: From Internal-Host, ping Web-Server — should be permitted (the DMZ-TO-LAN ACL does not restrict internal-to-DMZ traffic; only DMZ-to-LAN).

Record all test results in the table below.

Security Policy Verification Table:

| Test | Source | Destination | Port/Protocol | Expected | Actual | Pass/Fail |
|------|--------|-------------|--------------|----------|--------|-----------|
| 1 | Internet-Host | Web-Server | TCP 80 | Permit | | |
| 2 | Internet-Host | DB-Server | ICMP | Deny | | |
| 3 | Web-Server | DB-Server | TCP 3306 | Permit | | |
| 4 | Web-Server | Internal-Host | TCP 22 | Deny | | |
| 5 | Internal-Host | Web-Server | ICMP | Permit | | |

---

### Part 1 Questions

Question 1-1: In your initial testing (before ACLs), Internet-Host could ping DB-Server. What is the security risk this represents in a real-world environment? What type of server is DB-Server, and why should it never be directly reachable from the internet?

Question 1-2: The DMZ-TO-LAN ACL permits Web-Server to reach DB-Server on port 3306 only. This is an example of which security principle? Explain how this specific rule limits the blast radius if the Web-Server is compromised by an attacker.

Question 1-3: The OUTSIDE-IN ACL ends with `permit ip any any`. What would happen if this line were changed to `deny ip any any`? Would Test 5 (Internal-Host pinging Web-Server) still pass? Explain why or why not based on where the OUTSIDE-IN ACL is applied.

Question 1-4: An attacker compromises the Web-Server in the DMZ. They attempt to connect to DB-Server on port 22 (SSH) to exfiltrate data. Trace through the ACL rule-by-rule and explain exactly which ACL and which specific rule blocks this attempt.

---

### Part 2: ARP Analysis with Wireshark

### Part 2A: Capture ARP Traffic

Step 1: Open Wireshark and select your active network interface.

Step 2: Start capturing.

Step 3: Open a Command Prompt (Windows) or terminal (Linux/macOS) and run:

```text
arp -d *
```

This clears the ARP cache on Windows (on Linux use `ip neigh flush all`). This forces your machine to send ARP requests when it next needs to communicate.

Step 4: Ping your default gateway:

```text
ping -n 1 192.168.1.1
```

(Replace 192.168.1.1 with your actual gateway if different.)

Step 5: Run a few more pings to local hosts if available:

```text
ping -n 1 192.168.1.1
```

Step 6: Stop the Wireshark capture after about 20 seconds.

Step 7: Apply the display filter:

```text
arp
```

---

### Part 2B: Analyze ARP Packets

Examine the ARP packets in your capture. Identify at least one ARP Request and one ARP Reply.

ARP Capture Analysis Table:

| Frame | ARP Type | Sender MAC | Sender IP | Target MAC | Target IP |
|-------|----------|-----------|----------|-----------|----------|
| (Request) | Who has? | | | ff:ff:ff:ff:ff:ff | |
| (Reply) | Is at | | | | |

Question 2-1: In the ARP Request, the Target MAC is ff:ff:ff:ff:ff:ff. What does this MAC address represent, and why is it used in ARP Requests?

Question 2-2: After the ARP Reply is received, your machine caches the IP-to-MAC mapping in its ARP table. Run `arp -a` in a command prompt and record the entry for your default gateway. What IP address and MAC address are shown? Does this match the ARP Reply you captured in Wireshark?

---

### Part 2C: ARP Poisoning Indicators

In this section you will not conduct an actual ARP poisoning attack — instead you will analyze what one looks like in a capture and identify the indicators.

The following is a sample ARP capture excerpt (fictional MAC addresses for illustration):

```text
Frame 1: ARP Reply — Sender: 192.168.1.1 is at AA:BB:CC:11:22:33 (legitimate gateway)
Frame 2: ARP Reply — Sender: 192.168.1.1 is at DD:EE:FF:44:55:66 (sent by attacker's host)
Frame 3: ARP Reply — Sender: 192.168.1.1 is at DD:EE:FF:44:55:66 (repeated every 10 seconds)
```

Question 2C-1: What is the specific indicator in this capture that suggests ARP poisoning is in progress? Identify the key observation that distinguishes this from normal ARP behavior.

Question 2C-2: If a host receives both Frame 1 and Frame 2, which ARP Reply will take effect in the host's ARP cache, and why? What impact does this have on traffic flow?

Question 2C-3: The capture shows the attacker's ARP Reply being sent repeatedly every 10 seconds. Why does an ARP poisoning attacker need to send repeated ARP Replies rather than just sending one? What network behavior would cause a single forged reply to eventually become ineffective?

Question 2C-4: A network administrator wants to implement Dynamic ARP Inspection (DAI) to prevent this attack. Explain in your own words how DAI works — what database does it use to validate ARP packets, and what happens to a forged ARP Reply when DAI is enabled?

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Topology Screenshot — A screenshot of your completed Packet Tracer topology showing all devices, labels, and connections.

2. Part 1 Pre-ACL Ping Results — A written record (or screenshot) of the five connectivity tests before ACLs were applied, confirming Internet-Host could reach DB-Server.

3. Part 1 Security Policy Verification Table — Completed table with all five tests showing Actual result and Pass/Fail.

4. Part 1 Questions — Written answers to Questions 1-1 through 1-4 in complete sentences.

5. Part 2 ARP Capture Table — Completed ARP packet analysis table from your live capture.

6. Part 2 Wireshark Screenshot — A screenshot of your ARP-filtered Wireshark capture showing at least one Request and one Reply.

7. Part 2 Questions — Written answers to Questions 2-1, 2-2, and 2C-1 through 2C-4.

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1 Topology Screenshot — all devices and connections correct | 8 |
| Part 1 Pre-ACL results showing unrestricted access (security problem identified) | 7 |
| Part 1 Security Policy Verification Table — all 5 tests recorded correctly | 15 |
| Question 1-1 — DB-Server risk and why it must not be internet-facing | 8 |
| Question 1-2 — Least privilege principle correctly identified and explained | 8 |
| Question 1-3 — ACL placement and permit/deny analysis correct | 8 |
| Question 1-4 — Correct ACL trace identifying the specific blocking rule | 9 |
| Part 2 ARP Capture Table — Request and Reply correctly documented | 8 |
| Part 2 Wireshark Screenshot — ARP filter applied, Request and Reply visible | 5 |
| Question 2-1 — Broadcast MAC address purpose correct | 6 |
| Question 2-2 — arp -a output matches capture | 4 |
| Question 2C-1 — Duplicate IP-to-MAC indicator identified | 6 |
| Question 2C-2 — ARP cache overwrite behavior correct | 4 |
| Question 2C-3 — ARP cache TTL / expiration explanation correct | 5 |
| Question 2C-4 — DAI mechanism and DHCP snooping binding table explained | 9 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab08_Firstname_Lastname.pdf

Submit to the Module 08 Lab assignment in the course LMS before the posted deadline. Late submissions are subject to the course late policy.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
