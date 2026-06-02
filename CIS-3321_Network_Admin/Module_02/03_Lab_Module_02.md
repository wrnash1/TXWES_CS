# Lab Activity: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Lab Overview

**Lab Title:** Protocol Identification and Network Diagnostics Using Command-Line Tools

**Format:** Command-Line Tools on Local Machine (Windows or Linux/Mac)

**Estimated Time:** 60–75 minutes

**Points:** 100 points total

**Prerequisites:**

- Module 02 video lectures watched (both Part 1 and Part 2)
- Module 02 Reading Guide reviewed, especially the port number table
- A Windows, Linux, or macOS computer with internet access
- No additional software required — all tools are built into the OS

**Learning Objectives:**

By completing this lab, you will be able to:

- Use nslookup to query DNS records and identify DNS server addresses
- Use ping to test ICMP connectivity and interpret TTL values
- Use tracert (Windows) or traceroute (Linux/Mac) to trace network paths
- Use netstat to observe active TCP connections and listening ports
- Map observed protocols and ports to entries in the TCP/IP protocol reference table

---

### Background

Every concept in Module 02 — TCP, UDP, ICMP, DNS, port numbers — can be observed directly using command-line tools built into your operating system. This lab uses no special software. You will be making real network requests, observing real protocol behavior, and recording your findings. The commands used here — ping, tracert/traceroute, nslookup, and netstat — are standard tools every network administrator uses daily and appear regularly in Network+ exam scenarios.

---

### Part 1: DNS Queries with nslookup

**Objective:** Use nslookup to resolve hostnames, identify record types, and examine DNS server responses.

#### Step 1: Open a Command Prompt or Terminal

- Windows: Press Win+R, type cmd, press Enter
- Linux/macOS: Open Terminal

#### Step 2: Perform a Basic DNS Lookup

Type the following command (substitute any reachable public hostname):

`nslookup google.com`

Record your results:

- Server (DNS resolver used): ____________________
- Address (DNS resolver IP): ____________________
- Name (resolved hostname): ____________________
- Resolved IP Address(es): ____________________

**Question 1:** What type of DNS record (A or AAAA) does your result represent? How do you know?

#### Step 3: Query for a Specific Record Type

Query the MX record for a domain to identify its mail server:

`nslookup -type=MX gmail.com`

Record your results:

- MX record(s) returned: ____________________
- Preference value(s): ____________________

**Question 2:** What does the MX record tell you, and which protocol uses MX records?

#### Step 4: Perform a Reverse DNS Lookup

`nslookup 8.8.8.8`

Record your results:

- PTR record (hostname): ____________________

**Question 3:** What DNS record type is used for reverse lookups (IP to hostname)?

#### Step 5: Query a Specific DNS Server

`nslookup google.com 8.8.8.8`

**Question 4:** What is the significance of specifying a DNS server in the nslookup command? In what troubleshooting scenario would you do this?

---

### Part 2: ICMP Testing with ping and tracert

**Objective:** Use ping to test reachability and interpret TTL values; use tracert to map network paths.

#### Step 1: Basic Ping Test

`ping google.com`

Windows adds `/n 4` by default (4 packets). Linux/Mac requires `-c 4`.

Record your results:

| Field            | Value                  |
|------------------|------------------------|
| IP resolved      |                        |
| Packets sent     |                        |
| Packets received |                        |
| Packet loss %    |                        |
| Average RTT (ms) |                        |
| TTL value        |                        |

**Question 5:** What does the TTL value in the ping response represent? If the TTL is 115, what can you infer about the operating system of the remote host and the number of hops traversed? (Hint: Windows typically starts TTL at 128; Linux starts at 64.)

#### Step 2: Ping a Nonexistent Host

`ping 192.168.254.254`

**Question 6:** What error or timeout message do you receive? Which ICMP message type is typically returned when a destination is unreachable?

#### Step 3: Trace the Route to a Remote Host

Windows:

`tracert google.com`

Linux/Mac:

`traceroute google.com`

Record your results:

| Hop | RTT (ms) | IP Address or Hostname |
|-----|----------|------------------------|
| 1   |          |                        |
| 2   |          |                        |
| 3   |          |                        |
| 4   |          |                        |
| 5   |          |                        |

**Question 7:** How does tracert use the TTL field to discover each router hop? Describe the mechanism in two to three sentences.

**Question 8:** If a hop shows "* * * Request timed out" instead of a latency value, what does this typically indicate about that router?

---

### Part 3: TCP Connection Inspection with netstat

**Objective:** Use netstat to observe active TCP connections, identify ports, and map them to known protocols.

#### Step 1: View All Active Connections

Windows:

`netstat -an`

Linux/Mac:

`netstat -an`

**Question 9:** In the output, identify and record three TCP connections in the ESTABLISHED state. For each, record the local address and port, the foreign address and port, and identify the protocol name for any well-known port you recognize.

| Local Address:Port | Foreign Address:Port | State       | Protocol (if known) |
|--------------------|----------------------|-------------|---------------------|
|                    |                      |             |                     |
|                    |                      |             |                     |
|                    |                      |             |                     |

#### Step 2: View Listening Ports

Windows:

`netstat -an | findstr LISTEN`

Linux/Mac:

`netstat -an | grep LISTEN`

**Question 10:** List three services listening on your local machine with their port numbers. For each, identify the protocol name from the Module 02 port reference table if applicable.

| Listening Port | Protocol Name (if known) | Transport (TCP/UDP) |
|----------------|--------------------------|---------------------|
|                |                          |                     |
|                |                          |                     |
|                |                          |                     |

#### Step 3: Open a Web Browser and Observe New Connections

1. Open a web browser and navigate to any HTTPS website.
2. Immediately return to the terminal and run netstat -an again.
3. Look for new ESTABLISHED connections to port 443.

**Question 11:** Did you observe a new connection to port 443 after visiting an HTTPS website? What does the presence of port 443 in an ESTABLISHED connection confirm about the transport and encryption used?

---

### Deliverables

Submit the following to the Canvas assignment dropbox:

**Deliverable 1 (25 points):** A screenshot of your nslookup output for Steps 2 through 5, with your answers to Questions 1 through 4 typed below each screenshot.

**Deliverable 2 (25 points):** A screenshot of your ping output (Step 1) and tracert/traceroute output (Step 3), with your answers to Questions 5 through 8 typed below.

**Deliverable 3 (25 points):** A screenshot of your netstat output, with the three ESTABLISHED connections and three LISTEN ports clearly identified, and your answers to Questions 9 through 11 typed below.

**Deliverable 4 (25 points):** A typed summary (150–200 words) connecting your lab observations to the TCP/IP model. Identify which layer each command operates at and what you observed that confirmed your module reading.

---

### Grading Rubric

| Deliverable | Points | Full Credit Criteria |
|-------------|--------|----------------------|
| DNS screenshots and answers | 25 | All 4 nslookup steps captured; Questions 1–4 answered correctly with protocol/record type identification |
| Ping and tracert screenshots and answers | 25 | Ping output captured; tracert table populated with at least 5 hops; Questions 5–8 answered accurately |
| Netstat screenshots and answers | 25 | Connections table populated; LISTEN ports identified; Questions 9–11 answered correctly |
| Written summary | 25 | 150–200 words; connects each command to a specific TCP/IP layer; accurate technical terminology |
| **Total** | **100** | |

---

### Helpful Notes

All commands in this lab require internet access. If you are behind a restrictive firewall that blocks ICMP, ping and tracert may show timeouts — document this and explain why it occurs in your written summary.

On Windows, tracert uses ICMP Echo Requests. On Linux and macOS, traceroute uses UDP by default, but the mechanism (TTL exhaustion) is the same.

The nslookup command is available on Windows, Linux, and macOS without any installation.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
