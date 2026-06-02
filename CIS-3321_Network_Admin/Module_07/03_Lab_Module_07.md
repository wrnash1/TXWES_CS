# Lab Activity: Module 07 – WAN and Cloud Connectivity

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Overview

This lab has two parts. Part 1 uses command-line tools and web resources to observe real-world WAN and cloud connectivity — analyzing traceroute output to identify hops across WAN infrastructure and identifying cloud provider IP ranges. Part 2 uses Cisco Packet Tracer to build and test a site-to-site VPN topology, observing the before-and-after effect of a VPN tunnel on packet routing.

Estimated Time: 60–75 minutes

Required Tools:

- Windows 10 or 11 (for Part 1 commands), or Linux/macOS with equivalent tools
- Cisco Packet Tracer 8.x (free download at netacad.com with a free account)
- Web browser for cloud provider IP lookups

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Interpret traceroute output to identify WAN hops, carrier infrastructure, and cloud provider edge nodes.
2. Identify cloud provider IP address ranges and explain the significance of anycast routing.
3. Build a basic site-to-site VPN topology in Packet Tracer.
4. Explain the difference between pre-tunnel and post-tunnel traffic paths.
5. Describe how IPsec Tunnel mode hides internal IP addresses from the transit network.

---

### Part 1: WAN and Cloud Connectivity Analysis

#### Part 1A: Traceroute to Cloud Provider Infrastructure

Traceroute (or `tracert` on Windows) sends packets with incrementing TTL values to map the path between your machine and a destination. Each hop is a router that decrements the TTL by 1 and returns an ICMP Time Exceeded message when TTL reaches 0.

Step 1: Open a Command Prompt on Windows (or terminal on Linux/macOS).

Step 2: Run a traceroute to three destinations. Record the results for each:

```bat
tracert 8.8.8.8
```

```bat
tracert 1.1.1.1
```

```bat
tracert outlook.com
```

On Linux or macOS, replace `tracert` with `traceroute`.

Step 3: For each traceroute, count the total number of hops and record the hostnames or IP addresses of the first three hops and the last three hops.

Step 4: Look at the round-trip time (RTT) values for each hop. Identify where latency increases significantly — this typically indicates crossing a WAN boundary or a geographic distance.

Observation Table — Part 1A:

| Destination | Total Hops | First 3 Hops (IP/Hostname) | Last 3 Hops (IP/Hostname) | RTT Increase Point |
|-------------|-----------|--------------------------|--------------------------|-------------------|
| 8.8.8.8 | | | | |
| 1.1.1.1 | | | | |
| outlook.com | | | | |

---

#### Part 1B: Cloud Provider IP Range Identification

Major cloud providers publish their IP address ranges for firewall and routing purposes. You will look up the IP address of a cloud-hosted service and identify which provider's infrastructure it uses.

Step 1: Use `nslookup` to resolve the IP addresses of the following hostnames:

```bat
nslookup outlook.office365.com
nslookup s3.amazonaws.com
nslookup storage.googleapis.com
```

Record the IP addresses returned for each hostname.

Step 2: For each IP address obtained, use a WHOIS lookup (whois.domaintools.com or similar) or the ARIN registry (search.arin.net) to identify which organization owns the IP address range.

Step 3: Based on your lookup, identify which cloud provider is hosting each service (Microsoft Azure, AWS, or Google Cloud).

Observation Table — Part 1B:

| Hostname | Resolved IP | IP Range Owner | Cloud Provider |
|----------|------------|---------------|----------------|
| outlook.office365.com | | | |
| s3.amazonaws.com | | | |
| storage.googleapis.com | | | |

Analysis Questions — Part 1A and 1B:

Question 1: In your traceroute to 8.8.8.8, at what hop number did you observe the largest single RTT increase? What does a large RTT jump between two consecutive hops suggest about the network path between those two hops?

Question 2: Traceroute output often shows asterisks (***) at certain hops. What causes this? Does it indicate a network failure? Explain the two reasons why a router might not respond to traceroute probes.

Question 3: When you ran `nslookup outlook.office365.com`, you likely received an IP address owned by Microsoft. Why might different users running the same nslookup command from different locations receive different IP addresses for the same hostname? What routing or DNS technique causes this?

Question 4: Based on what you observed in Part 1, describe in your own words what the term "WAN hop" means. At what point in your traceroute output do you believe traffic leaves your local ISP and enters a larger carrier or backbone network? What clues in the output support your answer?

---

### Part 2: Site-to-Site VPN Topology in Cisco Packet Tracer

In Part 2, you will build a simple topology with two sites connected through a simulated internet cloud, configure static routing between them, and observe how traffic flows. You will then add a VPN tunnel (simulated using Packet Tracer's IPsec capabilities) and compare the traffic path before and after.

#### Step 1: Build the Topology

Open Packet Tracer and create the following topology:

Site A:

- 1 Router (Router0) — this is the Site A edge router
- 1 PC (PC0) — connected to Router0's LAN interface

Site B:

- 1 Router (Router1) — this is the Site B edge router
- 1 PC (PC1) — connected to Router1's LAN interface

Internet (simulated):

- 1 Router (Router2) — simulates an ISP/internet core router

Connect the devices:

- Router0 GigabitEthernet0/0 to Router2 GigabitEthernet0/0 (WAN link A)
- Router1 GigabitEthernet0/0 to Router2 GigabitEthernet0/1 (WAN link B)
- Router0 GigabitEthernet0/1 to PC0 (LAN)
- Router1 GigabitEthernet0/1 to PC1 (LAN)

#### Step 2: Configure IP Addressing

Assign the following addresses. Click each device, go to Config or CLI tab:

Router0:

- GigabitEthernet0/0 (WAN): 203.0.113.1 /30
- GigabitEthernet0/1 (LAN): 10.1.1.1 /24

Router1:

- GigabitEthernet0/0 (WAN): 198.51.100.1 /30
- GigabitEthernet0/1 (LAN): 10.2.2.1 /24

Router2:

- GigabitEthernet0/0: 203.0.113.2 /30
- GigabitEthernet0/1: 198.51.100.2 /30

PC0: IP 10.1.1.10, Mask 255.255.255.0, Gateway 10.1.1.1

PC1: IP 10.2.2.10, Mask 255.255.255.0, Gateway 10.2.2.1

#### Step 3: Configure Static Routing (No VPN)

On Router0, add static routes:

```cisco
ip route 10.2.2.0 255.255.255.0 203.0.113.2
ip route 198.51.100.0 255.255.255.252 203.0.113.2
```

On Router1, add static routes:

```cisco
ip route 10.1.1.0 255.255.255.0 198.51.100.2
ip route 203.0.113.0 255.255.255.252 198.51.100.2
```

On Router2, add static routes:

```cisco
ip route 10.1.1.0 255.255.255.0 203.0.113.1
ip route 10.2.2.0 255.255.255.0 198.51.100.1
```

#### Step 4: Test Connectivity Without VPN

From PC0's Desktop, open Command Prompt and run:

```bat
ping 10.2.2.10
```

This should succeed. The traffic travels: PC0 → Router0 → Router2 → Router1 → PC1.

Switch to Packet Tracer's Simulation Mode (bottom right). Run the same ping and observe the packet path. Note that the packet passes through Router2 (simulating the internet) with the internal addresses (10.1.1.10 and 10.2.2.10) visible in the IP header at every hop.

Record the packet path and note which router sees the internal IP addresses.

#### Step 5: Enable the VPN Tunnel

In Packet Tracer, click on Router0. Go to the Config tab, then select Tunnel interface (or use CLI). Configure a GRE tunnel simulating the VPN tunnel:

On Router0 CLI:

```cisco
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 198.51.100.1
```

On Router1 CLI:

```cisco
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 203.0.113.1
```

Update the static routes on Router0 to use the tunnel:

```cisco
ip route 10.2.2.0 255.255.255.0 172.16.0.2
```

Update the static routes on Router1 to use the tunnel:

```cisco
ip route 10.1.1.0 255.255.255.0 172.16.0.1
```

#### Step 6: Test Connectivity Through the Tunnel

From PC0's Desktop Command Prompt, run:

```bat
ping 10.2.2.10
```

Switch to Simulation Mode and run the ping again. Observe that the packet is now encapsulated in a GRE header — the inner IP header (with 10.1.1.10 and 10.2.2.10) is now inside the tunnel encapsulation, and only the outer header (203.0.113.1 to 198.51.100.1) is visible to Router2.

Lab Questions — Part 2:

Question 5: In Step 4 (without VPN), what IP addresses appear in the packet header when it passes through Router2? Who can see the internal IP addresses of PC0 and PC1?

Question 6: After enabling the GRE tunnel in Step 6, what IP addresses appear in the outer IP header when the packet passes through Router2? What are the inner IP addresses, and can Router2 see them?

Question 7: The tunnel configured in this lab uses GRE without encryption. In a real production VPN, what additional protocol would be layered on top of GRE to provide confidentiality? Name the specific protocol and the IPsec mode that would be used for a site-to-site VPN.

Question 8: The two internal networks in this lab are 10.1.1.0/24 and 10.2.2.0/24. Both are RFC 1918 private addresses. Without a tunnel, could Router2 (simulating the internet) route traffic to 10.1.1.0/24 or 10.2.2.0/24? Explain why or why not using the concept of private address non-routability.

Question 9: In this lab, all traffic between the sites routes through the GRE tunnel. This is analogous to which VPN configuration — full-tunnel or split-tunnel? Explain what the difference would be in the context of a remote-access VPN.

Question 10: A remote sales employee works from hotels and coffee shops. The hotel firewall blocks all traffic except ports 80 and 443. Would the GRE tunnel you configured in this lab work for that employee? What VPN technology and protocol would you recommend instead, and what port does it use?

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Observation Tables — Completed traceroute table (Part 1A) and cloud IP table (Part 1B) with all columns filled.

2. Part 1 Written Responses — Answers to Questions 1 through 4 in complete sentences. Include at least one screenshot of a full traceroute output.

3. Part 2 Topology Screenshot — A screenshot of your Packet Tracer topology showing Router0, Router1, Router2, PC0, and PC1 with all link indicators visible.

4. Part 2 Simulation Screenshots — One screenshot from Simulation Mode showing the packet path without the tunnel (Step 4) and one showing the encapsulated packet path with the tunnel (Step 6).

5. Part 2 Written Responses — Answers to Questions 5 through 10 in complete sentences.

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1A Observation Table — all three destinations recorded with hop counts and RTT data | 10 |
| Part 1B Observation Table — IPs resolved, WHOIS lookup completed, provider identified | 10 |
| Question 1 — RTT hop analysis with correct interpretation | 8 |
| Question 2 — Asterisk explanation (firewall or ICMP rate limit) | 7 |
| Question 3 — Anycast or DNS geo-distribution explanation | 7 |
| Question 4 — WAN hop identification with supporting evidence from output | 8 |
| Part 2 Topology Screenshot — correct devices and connections | 5 |
| Part 2 Simulation Screenshot (no tunnel) — internal IPs visible at Router2 | 5 |
| Part 2 Simulation Screenshot (with tunnel) — encapsulated packet at Router2 | 5 |
| Question 5 — Pre-tunnel IP header analysis correct | 8 |
| Question 6 — Post-tunnel outer/inner header analysis correct | 8 |
| Question 7 — GRE + IPsec ESP + Tunnel mode identified | 8 |
| Question 8 — RFC 1918 non-routability explanation correct | 7 |
| Question 9 — Full-tunnel vs. split-tunnel distinction correct | 7 |
| Question 10 — SSL/TLS VPN on TCP 443 identified correctly | 7 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab07_Firstname_Lastname.pdf

Submit to the Module 07 Lab assignment in the course LMS before the posted deadline. Late submissions are subject to the course late policy.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
