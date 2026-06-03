# Video Script: Module 14 — Network Troubleshooting Methodology (Part 2 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome back. This is Part 2 of Module 14 on Network Troubleshooting. In Part 1 we covered the seven-step CompTIA troubleshooting methodology and diagnostic commands. Now we get into the physical world — hardware failures, cable testing, and the specific troubleshooting scenarios that appear on the Network+ exam.

---

## Section 1: Physical Layer Troubleshooting

The most common network problems are physical. Before spending time analyzing routing tables and firewall rules, verify the physical layer.

### Cable Issues

Cables are the most frequently overlooked cause of network problems. Symptoms of cable problems:

- Intermittent connectivity — connection drops randomly
- Slow speeds — running at 10 Mbps when 1 Gbps is expected
- No link light on NIC or switch port
- High error rates — visible in switch port counters

Common cable faults:

- **Open circuit**: A wire is broken completely. No continuity. No signal passes.
- **Short circuit**: Two wires are touching that should not be. Signal bleeds between wires.
- **Crosstalk**: Signal from one wire pair induces interference in an adjacent pair. Caused by untwisting pairs too far at termination or using Category 3 cable for Gigabit Ethernet.
- **Split pair**: A wiring error where a pair is formed from wires that are not in the same original twisted pair. Passes a continuity test but fails at high speeds due to poor NEXT (Near End Crosstalk) performance.
- **Reversed pair**: One end of a pair is wired backwards (TX+ and TX- swapped).
- **Transposed pair**: Two pairs are swapped at the punchdown or connector (e.g., pairs 2 and 3 switched — this is how a crossover cable is made).
- **Attenuation**: Signal loss over distance. Exceeds limits for the cable category at long runs.

### Cable Testing Tools

- **Cable tester (basic)**: Tests continuity for all eight wires. Detects opens, shorts, reversed pairs, and transposed pairs. Does not measure cable performance.
- **Cable certifier (advanced)**: Measures cable performance parameters — attenuation, NEXT, FEXT, return loss, insertion loss — and certifies compliance with TIA/EIA standards (Cat5e, Cat6, Cat6a). Required for structured cabling installations.
- **Time Domain Reflectometer (TDR)**: Sends a signal down the cable and measures the reflection. Calculates the distance to any fault — open or short — within the cable. Built into most cable certifiers.
- **Tone generator and probe (inductive amplifier)**: Injects an audible tone into a cable at one end; the probe detects the tone at the other end to trace cables through walls and patch panels.
- **Optical power meter / Visual fault locator (VFL)**: For fiber cables. The optical power meter measures signal strength (dBm) to detect attenuation. The VFL shines visible red laser light into the fiber — breaks or severe bends glow red, visible through the jacket.

### Fiber Optic Troubleshooting

Fiber problems are less common than copper but critical to recognize:

- **Dirty connectors**: The most common fiber problem. Even microscopic contamination on an SC/LC/ST connector causes significant signal loss. Clean with appropriate fiber cleaning tools before testing.
- **Bent or kinked fiber**: Fiber will break or lose signal at sharp bends. Minimum bend radius must be maintained.
- **Wrong wavelength**: Single-mode and multimode fiber use different wavelengths. Using a multimode SFP in a single-mode fiber run causes signal loss (wavelength mismatch).
- **Mismatched fiber type**: Mixing OM3 and OM4 multimode fiber segments or single-mode and multimode fiber causes loss at the splice point.
- **Polarity**: TX and RX fibers must be crossed between devices. Incorrect polarity = transmit on transmit, no signal received.

---

## Section 2: Hardware Failure Symptoms

### Switch Hardware Failures

- **Port failure**: Single port no longer establishes a link. LED is dark or amber. Test by moving the device to a different port.
- **SFP/GBIC failure**: Fiber or copper transceiver module failed. Replace the SFP module.
- **Power supply failure**: Switch loses power entirely. Check redundant PSU if available; replace failed PSU.
- **Fan failure**: Switch overheats. Check environmental temperature alarms. Switch may throttle performance or shut down.
- **Memory/CPU issues**: Switch behaves erratically, drops packets inconsistently, crashes. May require firmware update or hardware replacement.

### Router Hardware Failures

Similar to switches. Additional considerations:

- **WAN interface failure**: The CSU/DSU or WAN module may fail. Carrier may show the circuit "up" but router interface is down.
- **Routing engine failure**: High CPU utilization leading to packet loss and slow routing convergence. Check with `show processes cpu`.

### NIC Failures

- **No link light**: Cable may be at fault — test with known-good cable first.
- **Duplex mismatch**: One side set to full-duplex, other to half-duplex. Results in late collisions and dramatically reduced throughput. Usually shows as high collision counts in interface statistics.
- **Speed mismatch**: One side auto-negotiated to 10 Mbps, other to 1 Gbps. Interface may not come up or may have extremely poor performance.
- **Failed NIC**: NIC not detected by OS, or detected but unable to establish link even with known-good cable.

### Power over Ethernet (PoE) Issues

- IP phones, wireless APs, and cameras receive power via PoE from the switch.
- **Insufficient PoE budget**: Switch total PoE capacity exceeded — some devices do not power on.
- **Wrong PoE standard**: Device requires PoE+ (802.3at — 30W) but port only provides PoE (802.3af — 15.4W). Device may not power up or may function erratically.
- **PoE port failure**: Individual port's PoE circuitry failed. Device must be moved to another port.

---

## Section 3: Common Network+ Scenario Questions

The Network+ exam presents scenario questions that describe a problem and ask you to select the most likely cause, the next troubleshooting step, or the correct tool. Let us walk through the most common scenario types.

### Scenario Type 1 — Connectivity Works for Some, Not Others

Scenario: Users on VLAN 10 can access the internet. Users on VLAN 20 cannot reach anything beyond the local router.

Analysis using the seven-step model and OSI:

- Layer 3 issue is likely — VLAN 20 may have a missing or incorrect route.
- Check: Does `ping` from VLAN 20 reach the default gateway? If yes, routing beyond the gateway is the issue.
- Check: Is the default gateway address correct for VLAN 20 hosts? Use `ipconfig` or `ip addr`.
- Check: Is a route for VLAN 20 traffic present in the router's routing table? Use `show ip route`.
- Likely cause: Missing inter-VLAN routing configuration for VLAN 20, or ACL blocking VLAN 20 traffic.

### Scenario Type 2 — Slow Network Performance

Scenario: A user reports that file transfers to the server are very slow — 1 Mbps on a Gigabit network.

Analysis:

- Check Layer 1 first: Is the switch port running at 1 Gbps? Use `show interfaces` — look for speed and duplex in the output.
- A duplex mismatch (one end auto-negotiated to half-duplex) is a classic cause of dramatically reduced throughput on what should be a Gigabit link.
- Check the interface for late collisions — present if there is a duplex mismatch.
- Other causes: Cable fault causing the link to negotiate down to 100 Mbps or 10 Mbps; congested uplink from access switch to distribution layer.

### Scenario Type 3 — Intermittent Connectivity

Scenario: A user's connection drops for a few seconds, then comes back. This happens several times per hour.

Analysis:

- Intermittent physical layer issues are the most common cause.
- Check: Is the cable damaged (kinked, chewed, pinched under furniture)?
- Check: Is the RJ-45 connector properly seated? Try reseating the cable.
- Check: Is the switch port showing any input/output errors or CRC errors? Use `show interfaces`.
- Check: Is Spanning Tree reconverging? STP topology changes cause brief traffic interruptions. Look for topology change notifications in switch logs.
- Check: Is there a flapping physical link (link up/down events)? Check switch log.

### Scenario Type 4 — Cannot Reach by Name, Can Reach by IP

Scenario: A user cannot open a web page by name (e.g., intranet.company.com) but can successfully ping the server's IP address.

Analysis:

- Classic DNS failure pattern.
- The fact that ping by IP succeeds means Layers 1–3 are functioning. The problem is name resolution.
- Check: `nslookup intranet.company.com` — does it resolve? If not, DNS is the issue.
- Check: Is the DNS server address correct on the client? (`ipconfig /all`)
- Check: Is the DNS server reachable? (`ping <DNS server IP>`)
- Check: Is the correct A record present in DNS for intranet.company.com?

### Scenario Type 5 — New Device Cannot Connect

Scenario: A new laptop was added to the network and cannot reach any resources. Other devices on the same switch port (using a different cable) work fine.

Analysis:

- Layer 2 or Layer 3 issue on the new device.
- Check: Does the NIC have a valid IP address? Is it a DHCP address or self-assigned (APIPA: 169.254.x.x)?
- A 169.254.x.x address means DHCP failed — check DHCP server availability and network path to DHCP server.
- Check: Is the new laptop in the correct VLAN? If the switch port is access VLAN 10 and the laptop expects VLAN 20, it will not communicate correctly.
- Check: Is 802.1X port authentication enabled? New devices without valid certificates may be blocked.

### Scenario Type 6 — High Latency and Packet Loss

Scenario: Users report web pages load slowly. `ping` shows 30% packet loss and 400 ms latency to the ISP gateway.

Analysis:

- WAN or internet connectivity issue.
- Use `traceroute` to identify where latency and packet loss begin.
- If the first hop (default gateway) is fast but the second hop (ISP) shows high latency, the issue is between your router and the ISP — possibly a congested or failing circuit.
- Contact the ISP with the traceroute output — this is the data they need to investigate.
- Check: Is the WAN interface showing any errors or drops? (`show interfaces WAN-interface`)

---

## Section 4: Exam Strategy for Troubleshooting Questions

The Network+ exam frequently presents performance-based questions (PBQs) and multiple-choice scenarios that test your troubleshooting reasoning. Here is how to approach them.

### Read the Entire Scenario

Exams often embed the answer in details you might miss if you rush. The time of day a problem started, which specific users are affected, what changed recently — all of these are clues.

### Apply the OSI Model Systematically

If the scenario does not immediately suggest a layer, start at Layer 1 and work up. The exam rewards systematic thinking over lucky guessing.

### Eliminate Clearly Wrong Answers

If a scenario says "users can ping the server by IP but not by name," you can eliminate any answer that involves physical connectivity or routing — those are clearly functioning. Focus on DNS.

### Trust the Most Common Causes

The exam tests real-world scenarios. In the real world, most problems are:

- Physical layer issues (cables, ports, transceivers)
- IP configuration errors (wrong address, wrong subnet, wrong gateway)
- DNS failures
- VLAN misconfiguration
- Firewall or ACL blocking

Exotic answers (memory corruption in the routing engine, cosmic ray bit flips) are almost never correct on the Network+ exam.

---

## Summary of Part 2

Key takeaways from Part 2:

- Common cable faults: open, short, crosstalk, split pair, reversed pair, attenuation.
- Cable testing tools: basic tester (continuity), certifier (performance + TDR), tone generator/probe (tracing), optical power meter and VFL (fiber).
- Hardware failure symptoms: port failure, duplex mismatch, PoE budget issues, fan/thermal alerts.
- Common exam scenario patterns: partial connectivity (VLAN/routing), slow performance (duplex mismatch), intermittent (cable or STP), name vs. IP (DNS), new device (DHCP/APIPA), high latency (WAN issue).
- Exam strategy: read fully, apply OSI, eliminate impossibles, trust common causes.

Module 14 is complete. Work through the Reading Guide, Lab, Quiz, and Discussion. Module 15 covers network documentation and policies — essential administrative skills that are also tested on Network+.
