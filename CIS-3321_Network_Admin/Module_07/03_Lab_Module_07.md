# Lab Activity: Module 07 — Network Monitoring and Troubleshooting Tools

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

### Overview

This lab has two parts. Part 1 uses the command-line diagnostic tools covered in the video lectures — ping, traceroute/tracert, nslookup, and netstat — to investigate real network connectivity and DNS behavior from your own machine. Part 2 introduces Wireshark packet capture, where you will capture live traffic, apply display filters, and identify the TCP three-way handshake and DNS query/response pairs in a real capture.

Estimated Time: 60–75 minutes

Required Tools:

- Windows 10 or 11 with Command Prompt, or Linux/macOS with terminal
- Wireshark (free download at wireshark.org) — install before the lab session
- Active internet connection

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Use ping to test Layer 3 reachability and interpret TTL and RTT values.
2. Use traceroute/tracert to map a network path and explain intermediate hop behavior.
3. Use nslookup to resolve hostnames and query specific DNS record types.
4. Use netstat to identify active connections and listening ports on a live system.
5. Capture live network traffic in Wireshark and apply display filters.
6. Identify the TCP three-way handshake in a Wireshark capture.
7. Identify DNS Query and DNS Response packets in a Wireshark capture.

---

### Part 1: Command-Line Diagnostic Tools

### Part 1A: ping — Testing Reachability and Interpreting Output

Step 1: Open a Command Prompt (Windows) or terminal (Linux/macOS).

Step 2: Run the following three ping commands. On Windows, 4 packets are sent by default. On Linux/macOS, press Ctrl+C after 4 replies.

```text
ping 127.0.0.1
ping 8.8.8.8
ping txwes.edu
```

Step 3: Record your results in the table below.

Ping Results Table:

| Target | Packets Sent | Packets Received | Packet Loss % | Average RTT (ms) | TTL Received |
|--------|-------------|-----------------|--------------|-----------------|-------------|
| 127.0.0.1 | | | | | |
| 8.8.8.8 | | | | | |
| txwes.edu | | | | | |

Step 4: Answer the following questions based on your results.

Question 1A-1: The target 127.0.0.1 is the loopback address. What does a successful ping to 127.0.0.1 tell you about the health of the TCP/IP stack on your own machine? What OSI layer does this test verify?

Question 1A-2: Compare the TTL value you received from 8.8.8.8 to the TTL value from txwes.edu. Assuming a standard starting TTL of 128 for Windows hosts and 64 for Linux hosts, calculate the approximate number of hops to each destination. Show your calculation.

Question 1A-3: If a ping to 8.8.8.8 succeeds (receives replies) but a ping to txwes.edu fails with "Ping: unknown host," what specific network service has failed, and what command would you run next to diagnose it?

---

### Part 1B: tracert / traceroute — Mapping the Network Path

Step 1: Run a traceroute to two destinations. On Windows use `tracert`; on Linux/macOS use `traceroute`.

```text
tracert 8.8.8.8
tracert txwes.edu
```

Step 2: For each traceroute, record the first hop, the last hop, the total hop count, and the RTT values at the hop where you observe the largest single increase in latency.

Traceroute Results Table:

| Destination | Total Hops | First Hop IP | Last Hop IP | Largest RTT Jump at Hop # | RTT Before Jump | RTT After Jump |
|------------|-----------|-------------|------------|--------------------------|----------------|---------------|
| 8.8.8.8 | | | | | | |
| txwes.edu | | | | | | |

Question 1B-1: Examine your traceroute to 8.8.8.8. At what hop number does the largest RTT jump occur? What does a sudden large increase in RTT between two consecutive hops suggest about the geographic or infrastructure relationship between those two routers?

Question 1B-2: If hop 4 in your traceroute shows three asterisks (***), does this mean hop 4 is down and the path to the destination is broken? Explain two reasons why a router might not respond to traceroute probes even when it is actively forwarding traffic.

Question 1B-3: The first hop in your traceroute should be your default gateway (typically your home router or campus router). What is the IP address of your first hop? Is it a private IP address (RFC 1918)? What RFC 1918 range does it fall into?

---

### Part 1C: nslookup — DNS Diagnostics

Step 1: Run the following nslookup commands and record the results.

Default resolver lookup:

```text
nslookup txwes.edu
```

Query against an alternate resolver:

```text
nslookup txwes.edu 8.8.8.8
```

Query for MX records:

```text
nslookup -type=MX txwes.edu
```

Query for NS records:

```text
nslookup -type=NS txwes.edu
```

Reverse lookup:

```text
nslookup 8.8.8.8
```

Step 2: Record results.

nslookup Results Table:

| Query | DNS Server Used | Result / Answer |
|-------|----------------|----------------|
| nslookup txwes.edu (default) | | |
| nslookup txwes.edu 8.8.8.8 | | |
| nslookup -type=MX txwes.edu | | |
| nslookup -type=NS txwes.edu | | |
| nslookup 8.8.8.8 | | |

Question 1C-1: When you ran `nslookup txwes.edu`, the output likely showed "Non-authoritative answer." What does this mean? Which server would provide an authoritative answer for txwes.edu, and how would you query it directly?

Question 1C-2: Examine the MX records returned for txwes.edu. What is the purpose of MX records in DNS? If a mail server cannot deliver email to a txwes.edu address, why would checking MX records be an early troubleshooting step?

Question 1C-3: Compare the results of `nslookup txwes.edu` (using your default resolver) with `nslookup txwes.edu 8.8.8.8` (using Google's resolver). Are the IP addresses the same? What does it mean if they differ?

---

### Part 1D: netstat — Active Connections and Listening Ports

Step 1: Open an elevated Command Prompt (Run as Administrator on Windows) or terminal.

Step 2: Run the following commands and record a sample of the output.

```text
netstat -an
```

```text
netstat -r
```

Step 3: From the `netstat -an` output, identify at least one LISTENING port, one ESTABLISHED connection (if any), and any UDP entries.

netstat Results Table:

| Protocol | Local Address:Port | Foreign Address:Port | State | Notes |
|---------|-------------------|---------------------|-------|-------|
| (record one LISTENING) | | | LISTENING | |
| (record one ESTABLISHED, if any) | | | ESTABLISHED | |
| (record one UDP entry) | | | | |

Question 1D-1: What is the significance of a TCP port showing state LISTENING? What would you expect to find if you opened a web browser and navigated to a website — which new state should appear in the netstat output?

Question 1D-2: Review the netstat -r (routing table) output. Identify the default route entry (destination 0.0.0.0 on Windows or default on Linux). What is the gateway address shown? How does this relate to the first hop you saw in your traceroute?

Question 1D-3: A security analyst discovers that a process is listening on TCP port 4444 on a workstation. The workstation is not a server and no applications should be listening on non-standard ports. What does this finding suggest, and what netstat flag (on Windows) would reveal which executable is associated with that listening port?

---

### Part 2: Wireshark Packet Capture and Analysis

### Part 2A: Capture Setup and Basic Filtering

Step 1: Launch Wireshark. On the main screen, select your active network interface (the one with traffic activity shown on the waveform graph — typically "Ethernet" or "Wi-Fi").

Step 2: Click the blue shark-fin Start button to begin capturing.

Step 3: Open a web browser and navigate to http://neverssl.com (this site deliberately uses unencrypted HTTP so you can see the content in Wireshark).

Step 4: Return to Wireshark and click the red Stop button after about 10 seconds of capture.

Step 5: In the Display Filter bar, enter the following filter and press Enter:

```text
http
```

You should now see only HTTP packets. Browse through a few packets and note the HTTP GET request and the HTTP 200 OK response.

Step 6: Clear the display filter and try:

```text
dns
```

You should see DNS query and response packets.

---

### Part 2B: Identifying the TCP Three-Way Handshake

Step 1: Clear all display filters (empty the filter bar and press Enter).

Step 2: Apply this filter to isolate TCP connection establishment:

```text
tcp.flags.syn == 1
```

Step 3: Find a SYN packet in the list. Note the source IP, destination IP, and destination port.

Step 4: Right-click that SYN packet and select "Follow > TCP Stream." Wireshark will automatically filter to show all packets in that TCP conversation.

Step 5: Identify the three packets that form the handshake:

- Packet 1: SYN — flags show SYN=1, ACK=0
- Packet 2: SYN-ACK — flags show SYN=1, ACK=1
- Packet 3: ACK — flags show SYN=0, ACK=1

Record the frame numbers and timestamp of each handshake packet.

Handshake Capture Table:

| Step | Frame Number | Source IP | Destination IP | TCP Flags | Sequence Number |
|------|-------------|-----------|---------------|-----------|----------------|
| SYN | | | | SYN | |
| SYN-ACK | | | | SYN, ACK | |
| ACK | | | | ACK | |

---

### Part 2C: Identifying DNS Queries and Responses

Step 1: Clear the display filter and apply:

```text
dns
```

Step 2: Locate a DNS Query packet (the Info column shows "Standard query"). Click on it. In the packet detail pane, expand the "Domain Name System (query)" section. Note the queried name and query type (A, AAAA, MX, etc.).

Step 3: Locate the corresponding DNS Response packet immediately following the query (same transaction ID, Info column shows "Standard query response"). Note the answer section — the returned IP address.

DNS Capture Table:

| Frame | Type | Queried Name | Record Type | Answer / IP Returned | Latency (ms) |
|-------|------|-------------|-------------|---------------------|-------------|
| (Query) | Query | | | N/A | |
| (Response) | Response | | | | |

Question 2C-1: In the DNS packets you captured, what port number was used as the destination port for DNS queries, and what transport protocol (TCP or UDP) was used? Why is this protocol typically chosen for DNS?

Question 2C-2: Each DNS query and response pair shares a "Transaction ID" field. What is the purpose of this identifier? What would happen if two DNS queries were outstanding simultaneously and there were no transaction IDs?

---

### Part 2D: Wireshark Display Filter Practice

Write the correct Wireshark display filter for each of the following requirements. Do not run these — write them as answers.

Question 2D-1: Show only traffic where the source OR destination IP is 192.168.1.50.

Question 2D-2: Show only TCP traffic on port 443 (HTTPS).

Question 2D-3: Show only ICMP packets (ping traffic).

Question 2D-4: Show only DNS response packets (not queries).

Question 2D-5: Show traffic between 192.168.1.10 and 10.0.0.1 only.

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Result Tables — All four tables (ping, traceroute, nslookup, netstat) with all columns filled from your actual command output.

2. Part 1 Written Responses — Answers to Questions 1A-1 through 1D-3 in complete sentences (11 questions total). Include at least one screenshot of actual command output for each Part 1 section.

3. Part 2 Capture Tables — Completed handshake table (Part 2B) and DNS capture table (Part 2C).

4. Part 2 Wireshark Screenshots — One screenshot showing the TCP three-way handshake with the packet detail pane open on the SYN packet. One screenshot showing a DNS query and response pair.

5. Part 2 Written Responses — Answers to Questions 2C-1, 2C-2, and all five filter-writing questions (2D-1 through 2D-5).

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1A — Ping table complete with all three targets | 6 |
| Part 1A — Questions 1A-1 through 1A-3 correct | 9 |
| Part 1B — Traceroute table with RTT jump data | 6 |
| Part 1B — Questions 1B-1 through 1B-3 correct | 9 |
| Part 1C — nslookup table complete | 5 |
| Part 1C — Questions 1C-1 through 1C-3 correct | 9 |
| Part 1D — netstat table with LISTENING and ESTABLISHED entries | 5 |
| Part 1D — Questions 1D-1 through 1D-3 correct | 9 |
| Part 2B — Handshake table with correct frame/flag data | 8 |
| Part 2B — Wireshark screenshot showing three-way handshake | 5 |
| Part 2C — DNS table with query and response pair | 8 |
| Part 2C — Questions 2C-1 and 2C-2 correct | 6 |
| Part 2D — Display filter questions 2D-1 through 2D-5 | 10 |
| Screenshots — One per Part 1 section (4 total) | 5 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab07_Firstname_Lastname.pdf

Submit to the Module 07 Lab assignment in the course LMS before the posted deadline. Late submissions are subject to the course late policy.

---

## Part 9 — Challenge Exercise

These advanced steps extend the Module 07 lab with advanced Wireshark analysis and SNMP simulation.

### Challenge Step 1: Capture and Analyze a Complete HTTP Transaction

1. Start a fresh Wireshark capture on your active network interface.
2. Open a terminal and use curl to request a plain HTTP page:
   ```
   curl http://httpforever.com/
   ```
   (This site intentionally serves unencrypted HTTP for testing purposes.)
3. Stop the Wireshark capture immediately after the response is received.
4. Apply the display filter: `http`
5. Find the HTTP GET request and the HTTP 200 OK response.
6. For the GET request, expand all protocol layers and record the header at each OSI layer (Ethernet frame, IP packet, TCP segment, HTTP request).

**Challenge Question 1:** In the HTTP GET request packet, identify and record the following values: source MAC address, destination MAC address, source IP address, destination IP address, source port, destination port, TCP sequence number, and HTTP request line (method + path). Map each value to its OSI layer. What does this exercise demonstrate about encapsulation?

### Challenge Step 2: Write and Test Advanced Wireshark Display Filters

Without running a live capture, write the correct Wireshark display filter syntax for each of the following scenarios. Then, if you have a previous capture file from this lab, test them.

1. Show all DNS queries for A records only (record type = 1).
2. Show all TCP resets (RST flag set).
3. Show all packets larger than 1400 bytes.
4. Show all ARP requests (not replies).
5. Show all packets where the HTTP host header contains "google."

**Challenge Question 2:** For each filter above, write the filter string. Then select any two of the five filters and explain what network troubleshooting scenario would lead an administrator to use each filter — what problem would you be investigating, and what would you expect to find in the results?

### Challenge Step 3: Configure SNMP on a Cisco Device in Packet Tracer

1. In Packet Tracer, add a Cisco 2911 router and a generic server (set up as an NMS).
2. Connect them with a crossover cable and assign IP addresses (e.g., router Gi0/0: 10.0.0.1/24, server: 10.0.0.2/24).
3. On the router CLI, configure SNMPv2c with a read-only community string:
   ```
   snmp-server community NetPlus2024 RO
   snmp-server enable traps
   snmp-server host 10.0.0.2 version 2c NetPlus2024
   ```
4. On the server, open the SNMP Services tab and add the community string `NetPlus2024`.
5. From the server, send an SNMP GET to the router for the sysDescr OID (1.3.6.1.2.1.1.1.0).
6. Record the response.

**Challenge Question 3:** The community string `NetPlus2024` is transmitted in cleartext in SNMPv2c. Describe the security risk this creates. Rewrite the router configuration to use SNMPv3 with authentication and encryption — write the full IOS commands you would use to create an SNMPv3 user named `netadmin` with SHA authentication and AES-128 encryption.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
